import assert from "node:assert/strict";
import { generateKeyPairSync } from "node:crypto";
import { describe, it } from "node:test";

import { Firestore, fieldPath, fromValue, toValue, type ServiceAccount } from "../firestore";
import { FirestoreStore, type Reservation } from "../store";

const { privateKey } = generateKeyPairSync("rsa", { modulusLength: 2048 });
const ACCOUNT: ServiceAccount = {
  project_id: "demo",
  client_email: "sa@demo.iam.gserviceaccount.com",
  private_key: privateKey.export({ type: "pkcs8", format: "pem" }).toString(),
};
const ROOT = "projects/demo/databases/(default)/documents";

type Call = { url: string; method: string; body: any };

/** A pretend Google: answers the token request, and Firestore calls from [answer]. */
function fakeGoogle(answer: (call: Call) => unknown = () => ({})) {
  const calls: Call[] = [];
  const fetchFn = async (url: string, init?: RequestInit) => {
    const raw = init?.body?.toString() ?? "";
    const call = { url, method: init?.method ?? "GET", body: url.includes("oauth2") ? raw : raw ? JSON.parse(raw) : null };
    calls.push(call);
    const body = url.includes("oauth2") ? { access_token: "token-1", expires_in: 3600 } : answer(call);
    return new Response(JSON.stringify(body), { status: 200 });
  };
  const db = new Firestore(ACCOUNT, fetchFn);
  const firestoreCalls = () => calls.filter((c) => c.url.startsWith("https://firestore"));
  return { db, calls, firestoreCalls };
}

const doc = (path: string, fields: Record<string, unknown>) => ({
  name: `${ROOT}/${path}`,
  fields: (toValue(fields) as { mapValue: { fields: object } }).mapValue.fields,
});

const reservation: Reservation = {
  uid: "u1",
  studentId: "s1",
  day: "2026-10-03",
  kind: "text",
  stepKey: "g6-maths-02-dividing-fractions/s6_explain_why",
  kindLimit: 10,
  stepLimit: 3,
  globalDailyUsd: 0.5,
};

describe("Firestore values", () => {
  it("round-trips the types the server stores", () => {
    const data = { n: 3, x: 0.25, s: "hi", b: true, none: null, at: new Date("2026-10-03T00:00:00Z"), list: [1, "a"], map: { k: 2 } };
    assert.deepEqual(fromValue(toValue(data)), data);
    assert.deepEqual(toValue(3), { integerValue: "3" });
    assert.deepEqual(toValue(0.5), { doubleValue: 0.5 });
  });

  it("quotes field names that aren't plain", () => {
    assert.equal(fieldPath("steps", "g6-maths/s6"), "steps.`g6-maths/s6`");
    assert.equal(fieldPath("cost_usd"), "cost_usd");
    assert.equal(fieldPath("a`b"), "`a\\`b`");
  });
});

describe("Firestore client", () => {
  it("signs in once as the service account and reuses the token", async () => {
    const { db, calls } = fakeGoogle(() => [{ missing: `${ROOT}/a/b` }]);
    assert.equal(await db.get("a/b"), null);
    assert.equal(await db.get("a/b"), null);
    const tokenCalls = calls.filter((c) => c.url.includes("oauth2"));
    assert.equal(tokenCalls.length, 1);
    assert.match(tokenCalls[0].body, /grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Ajwt-bearer/);
  });

  it("writes merges with increments and server times", async () => {
    const { db, firestoreCalls } = fakeGoogle();
    await db.commit([
      { kind: "set", path: "ai_queue/q1", data: { status: "x" }, merge: true, exists: true, increments: { [fieldPath("steps", "a-b")]: 1 }, serverTimes: ["at"] },
      { kind: "delete", path: "ai_logs/l1" },
    ]);
    const [write, del] = firestoreCalls()[0].body.writes;
    assert.deepEqual(write, {
      update: { name: `${ROOT}/ai_queue/q1`, fields: { status: { stringValue: "x" } } },
      updateMask: { fieldPaths: ["status"] },
      updateTransforms: [
        { fieldPath: "steps.`a-b`", increment: { integerValue: "1" } },
        { fieldPath: "at", setToServerValue: "REQUEST_TIME" },
      ],
      currentDocument: { exists: true },
    });
    assert.deepEqual(del, { delete: `${ROOT}/ai_logs/l1` });
  });
});

describe("FirestoreStore", () => {
  function storeWith(usage: Record<string, unknown> | null, totalCost = 0) {
    const google = fakeGoogle((call) => {
      if (call.url.endsWith(":beginTransaction")) return { transaction: "tx1" };
      if (call.url.endsWith(":batchGet")) {
        return [
          usage ? { found: doc("ai_usage/2026-10-03_s1", usage) } : { missing: `${ROOT}/ai_usage/2026-10-03_s1` },
          { found: doc("ai_usage_total/2026-10-03", { cost_usd: totalCost }) },
        ];
      }
      return {};
    });
    return { ...google, store: new FirestoreStore(google.db) };
  }

  it("reserves a call inside a transaction", async () => {
    const { store, firestoreCalls } = storeWith({ text: 2, steps: {} });
    assert.equal(await store.reserve(reservation), "ok");
    const commit = firestoreCalls().find((c) => c.url.endsWith(":commit"))!;
    assert.equal(commit.body.transaction, "tx1");
    assert.deepEqual(
      commit.body.writes[0].updateTransforms.map((t: { fieldPath: string }) => t.fieldPath),
      ["text", "steps.`g6-maths-02-dividing-fractions/s6_explain_why`"],
    );
  });

  it("refuses and rolls back at a limit", async () => {
    for (const [usage, total, expected] of [
      [{ text: 10 }, 0, "student_limit"],
      [{ text: 1, steps: { [reservation.stepKey]: 3 } }, 0, "step_limit"],
      [null, 0.5, "budget"],
    ] as const) {
      const { store, firestoreCalls } = storeWith(usage, total);
      assert.equal(await store.reserve(reservation), expected);
      const urls = firestoreCalls().map((c) => c.url);
      assert.ok(urls.some((u) => u.endsWith(":rollback")));
      assert.ok(!urls.some((u) => u.endsWith(":commit")));
    }
  });

  it("holds a job's writes and sends them in one commit, with usage added up", async () => {
    const { db, firestoreCalls } = fakeGoogle();
    const store = new FirestoreStore(db, { deferWrites: true });
    const usage = { input_tokens: 100, output_tokens: 10 };
    await store.recordUsage({ uid: "u1", studentId: "s1", day: "d", calls: 1, usage, costUsd: 0.25 });
    await store.recordUsage({ uid: "u1", studentId: "s1", day: "d", calls: 1, usage, costUsd: 0.5 });
    await store.answerQueued("q1", { level: "got_it", reply: "Well done" });
    assert.equal(firestoreCalls().length, 0);

    await store.flush();
    const commits = firestoreCalls();
    assert.equal(commits.length, 1);
    const writes = commits[0].body.writes;
    assert.equal(writes.length, 3); // the answer, the student's day, the project's day
    const studentDay = writes.find((w: any) => w.update.name.endsWith("ai_usage/d_s1"));
    const cost = studentDay.updateTransforms.find((t: any) => t.fieldPath === "cost_usd");
    assert.deepEqual(cost.increment, { doubleValue: 0.75 });
  });

  it("reads everyone's week in three queries", async () => {
    const { db, firestoreCalls } = fakeGoogle((call) => {
      const collection = call.body.structuredQuery.from[0].collectionId;
      const rows = {
        students: [doc("accounts/u1/students/s1", { grade: 9 }), doc("accounts/u1/students/s2", { grade: 6 })],
        progress: [doc("accounts/u1/students/s1/progress/l1", { completed: true })],
        skills: [doc("accounts/u1/students/s2/skills/k1", { mastered: true })],
      }[collection as "students"];
      return rows.map((document) => ({ document }));
    });
    const store = new FirestoreStore(db);
    const students = await store.allStudents();
    assert.deepEqual(students, [
      { uid: "u1", studentId: "s1", grade: 9 },
      { uid: "u1", studentId: "s2", grade: 6 },
    ]);
    assert.deepEqual(await store.studentActivity("u1", "s1"), { progress: [{ completed: true }], skills: [] });
    assert.deepEqual(await store.studentActivity("u1", "s2"), { progress: [], skills: [{ mastered: true }] });
    assert.equal(firestoreCalls().length, 3);
    assert.ok(firestoreCalls().every((c) => c.body.structuredQuery.from[0].allDescendants));
  });
});
