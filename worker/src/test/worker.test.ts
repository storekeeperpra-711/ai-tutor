import assert from "node:assert/strict";
import { describe, it } from "node:test";

import { Unauthenticated } from "../auth";
import { CRON, handleRequest, runScheduled, type Services } from "../worker";
import { FakeBatches, FakeClaude, MemoryStore, lessons } from "./fakes";

const G6 = "g6-maths-02-dividing-fractions";

function services(replies: unknown[] = []) {
  const store = new MemoryStore();
  store.addStudent("u1", "s1");
  const claude = new FakeClaude(replies);
  const svc: Services = {
    verify: async (token) => {
      if (token !== "good") throw new Unauthenticated("bad token");
      return { uid: "u1" };
    },
    deps: () => ({ store, claude, lessons: lessons(), now: () => new Date("2026-10-03T06:00:00Z") }),
    store: () => store,
    adminEmails: [],
  };
  return { store, claude, svc };
}

const post = (path: string, body: unknown, token: string | null = "good") =>
  new Request(`https://ai.example.com${path}`, {
    method: "POST",
    headers: token ? { authorization: `Bearer ${token}` } : {},
    body: typeof body === "string" ? body : JSON.stringify(body),
  });

const explain = { student_id: "s1", lesson_id: G6, step_id: "s6_explain_why", lang: "en", kind: "explain", answer: "Each roti has 2 halves" };

describe("Worker routes", () => {
  it("answers a signed-in feedback request", async () => {
    const { svc } = services([{ level: "partly", reply: "Nearly!", concern: false }]);
    const response = await handleRequest(post("/v1/feedback", explain), svc);
    assert.equal(response.status, 200);
    assert.deepEqual(await response.json(), { checked_by: "ai", level: "partly", reply: "Nearly!" });
  });

  it("refuses requests without a valid sign-in, before reading them", async () => {
    const { svc, claude } = services();
    assert.equal((await handleRequest(post("/v1/feedback", explain, null), svc)).status, 401);
    assert.equal((await handleRequest(post("/v1/feedback", explain, "forged"), svc)).status, 401);
    assert.equal(claude.requests.length, 0);
  });

  it("rejects bad input and unknown routes", async () => {
    const { svc } = services();
    assert.equal((await handleRequest(post("/v1/feedback", "{not json"), svc)).status, 400);
    assert.equal((await handleRequest(post("/v1/feedback", { ...explain, answer: "" }), svc)).status, 400);
    assert.equal((await handleRequest(post("/v1/other", {}), svc)).status, 404);
    const get = new Request("https://ai.example.com/v1/costs", { headers: { authorization: "Bearer good" } });
    assert.equal((await handleRequest(get, svc)).status, 405);
  });

  it("returns the caller's costs", async () => {
    const { svc } = services();
    const response = await handleRequest(post("/v1/costs", {}), svc);
    assert.equal(response.status, 200);
    assert.equal(((await response.json()) as { all: boolean }).all, false);
  });
});

describe("Scheduled jobs", () => {
  it("sends the held writes at the end of each job", async () => {
    const store = new MemoryStore();
    const deps = { store, batches: new FakeBatches(), lessons: lessons(), now: () => new Date("2026-10-04T13:00:00Z") };
    assert.deepEqual(await runScheduled(CRON.batchJob, deps), { collected: 0, submitted: 0, skipped: 0, logsDeleted: 0 });
    assert.deepEqual(await runScheduled(CRON.weeklyReports, deps), { reports: 0 });
    assert.equal(store.flushed, 2);
  });
});
