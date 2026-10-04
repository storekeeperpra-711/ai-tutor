import assert from "node:assert/strict";
import { describe, it } from "node:test";

import { runBatchJob, submitWeeklyReports, weekStats, type BatchDeps } from "../batch";
import { LIMITS, dayOf } from "../config";
import { costReport, parseAdminEmails } from "../costs";
import { FakeBatches, MemoryStore, USAGE, lessons, message } from "./fakes";
import { costOf } from "../pricing";

const NOW = new Date("2026-10-04T13:00:00Z"); // Sunday 18:00 in Pakistan
const G6 = "g6-maths-02-dividing-fractions";

function setup() {
  const store = new MemoryStore();
  store.addStudent("u1", "s1", 6);
  store.addStudent("u2", "s2", 9);
  const batches = new FakeBatches();
  const deps: BatchDeps = { store, batches, lessons: lessons(), now: () => NOW };
  return { store, batches, deps };
}

function queue(store: MemoryStore, id: string, extra: Record<string, unknown> = {}) {
  store.queue.set(id, {
    id,
    uid: "u1",
    student_id: "s1",
    lesson_id: G6,
    step_id: "s6_explain_why",
    lang: "ur",
    answer: "ہر روٹی کے دو آدھے",
    created_at: new Date(NOW.getTime() - 3_600_000),
    status: "waiting",
    ...extra,
  });
}

describe("batch job for queued answers", () => {
  it("sends waiting answers at half price and writes Mithu's reply back", async () => {
    const { store, batches, deps } = setup();
    queue(store, "q1");
    queue(store, "q2", { step_id: "missing" });
    queue(store, "q3", { created_at: new Date(NOW.getTime() - 10 * 86_400_000) });

    assert.deepEqual(await runBatchJob(deps), { collected: 0, submitted: 1, skipped: 2 });
    assert.equal(batches.created[0].requests[0].custom_id, "a_q1");
    assert.equal(store.queue.get("q1")!.status, "in_batch");
    // The typed answer isn't kept once it has been sent.
    assert.equal(store.queue.get("q1")!.answer, "");
    assert.equal(store.queue.get("q2")!.status, "skipped");
    assert.equal(store.queue.get("q3")!.status, "skipped");

    // Not finished yet: nothing changes.
    assert.deepEqual(await runBatchJob(deps), { collected: 0, submitted: 0, skipped: 0 });

    batches.ended.add("batch_1");
    batches.answers.set("a_q1", message({ level: "partly", reply: "اچھی شروعات!", concern: false }));
    assert.deepEqual(await runBatchJob(deps), { collected: 1, submitted: 0, skipped: 0 });
    assert.equal(store.queue.get("q1")!.status, "answered");
    assert.deepEqual(store.queue.get("q1")!.result, { level: "partly", reply: "اچھی شروعات!" });
    assert.equal(store.batches.get("batch_1")!.status, "ended");
    assert.equal(store.totals.get(dayOf(NOW)), costOf("claude-haiku-4-5", USAGE, true));
    assert.equal(store.logs.at(-1)!.batch, true);
  });

  it("removes phone numbers from queued answers before Claude", async () => {
    const { store, batches, deps } = setup();
    queue(store, "q1", { answer: "دو آدھے، میرا نمبر 0300-1234567 ہے" });
    await runBatchJob(deps);
    const content = JSON.stringify(batches.created[0].requests[0]);
    assert.match(content, /\[phone number removed\]/);
    assert.doesNotMatch(content, /1234567/);
  });

  it("marks errored answers as failed", async () => {
    const { store, batches, deps } = setup();
    queue(store, "q1");
    queue(store, "q2");
    await runBatchJob(deps);
    batches.ended.add("batch_1");
    batches.answers.set("a_q1", null);
    await runBatchJob(deps);
    assert.equal(store.queue.get("q1")!.status, "failed");
    assert.equal(store.queue.get("q2")!.status, "failed"); // no result at all
  });

  it("sends at most the daily number of queued answers per student", async () => {
    const { store, batches, deps } = setup();
    for (let i = 0; i < LIMITS.queuedPerDay + 2; i++) queue(store, `q${i}`);
    await runBatchJob(deps);
    assert.equal(batches.created[0].requests.length, LIMITS.queuedPerDay);
  });

  it("waits while the project's daily cap is used up", async () => {
    const { store, batches, deps } = setup();
    queue(store, "q1");
    store.totals.set(dayOf(NOW), LIMITS.globalDailyUsd);
    await runBatchJob(deps);
    assert.equal(batches.created.length, 0);
    assert.equal(store.queue.get("q1")!.status, "waiting");
  });
});

describe("weekly reports", () => {
  const recent = new Date(NOW.getTime() - 2 * 86_400_000);
  const old = new Date(NOW.getTime() - 20 * 86_400_000);

  it("counts the week from progress and skills", () => {
    const stats = weekStats(
      6,
      {
        progress: [
          {
            completed: true,
            updated_at: recent,
            steps: {
              a: { correct: true, at: recent },
              b: { correct: false, at: new Date(recent.getTime() + 86_400_000) },
              c: { correct: null, at: recent },
              d: { correct: true, at: old },
            },
          },
          { completed: true, updated_at: old, steps: {} },
        ],
        skills: [
          { last_answered: recent.toISOString(), mastered_at: recent.toISOString() },
          { last_answered: old.toISOString(), mastered_at: null },
        ],
      },
      new Date(NOW.getTime() - 7 * 86_400_000),
    );
    assert.deepEqual(stats, {
      grade: 6, lessons_finished: 1, questions_answered: 2, first_try_correct: 1,
      skills_practised: 1, skills_mastered: 1, active_days: 2,
    });
  });

  it("writes a note only for students who practised, with no names", async () => {
    const { store, batches, deps } = setup();
    store.activity.set("u1/s1", { progress: [{ steps: { a: { correct: true, at: recent } } }], skills: [] });
    assert.equal(await submitWeeklyReports(deps), 1);
    const request = batches.created[0].requests[0] as { custom_id: string; params: { messages: { content: { text: string }[] }[] } };
    assert.match(request.params.messages[0].content[0].text, /Grade: 6/);

    batches.ended.add("batch_1");
    batches.answers.set("r_0", message({ en: "Your child practised well.", ur: "آپ کے بچے نے اچھی مشق کی۔" }));
    await runBatchJob(deps);
    assert.equal(store.reports.length, 1);
    assert.equal(store.reports[0].studentId, "s1");
    assert.equal(store.reports[0].week, dayOf(NOW));
    assert.deepEqual(store.reports[0].note, { en: "Your child practised well.", ur: "آپ کے بچے نے اچھی مشق کی۔" });
  });
});

describe("cost dashboard", () => {
  async function withUsage() {
    const store = new MemoryStore();
    store.addStudent("u1", "s1");
    store.addStudent("u2", "s2");
    const day = dayOf(NOW);
    await store.recordUsage({ uid: "u1", studentId: "s1", day, calls: 2, usage: USAGE, costUsd: 0.003 });
    await store.recordUsage({ uid: "u2", studentId: "s2", day, calls: 1, usage: USAGE, costUsd: 0.007 });
    return store;
  }

  it("shows an account only its own students", async () => {
    const report = await costReport(await withUsage(), { uid: "u1" }, ["boss@example.com"], NOW);
    assert.equal(report.all, false);
    assert.deepEqual(report.rows.map((r) => r.student_id), ["s1"]);
    assert.equal(report.total_usd, 0.003);
    assert.equal(report.days.length, 7);
  });

  it("shows an admin with a verified email every student", async () => {
    const store = await withUsage();
    const admin = await costReport(store, { uid: "u9", email: "Boss@example.com", emailVerified: true }, ["boss@example.com"], NOW);
    assert.equal(admin.all, true);
    assert.deepEqual(admin.rows.map((r) => r.student_id), ["s2", "s1"]);
    const unverified = await costReport(store, { uid: "u9", email: "boss@example.com", emailVerified: false }, ["boss@example.com"], NOW);
    assert.equal(unverified.all, false);
  });

  it("reads the admin email setting", () => {
    assert.deepEqual(parseAdminEmails(" A@x.com, ,b@y.org,nonsense"), ["a@x.com", "b@y.org"]);
    assert.deepEqual(parseAdminEmails(""), []);
  });
});
