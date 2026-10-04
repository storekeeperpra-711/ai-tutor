import assert from "node:assert/strict";
import { describe, it } from "node:test";

import { countDay, countYesterday, yesterday } from "../learning";
import { MemoryStore } from "./fakes";

// 2026-10-03 in Pakistan is 2026-10-02T19:00Z to 2026-10-03T19:00Z.
const DAY = "2026-10-03";
const at = (iso: string) => new Date(iso);

const docs = [
  {
    owner: "accounts/u1/students/s1",
    data: {
      completed: true,
      updated_at: at("2026-10-03T10:00:00Z"),
      steps: {
        video: { correct: null, attempts: 0, at: at("2026-10-03T09:00:00Z") },
        q1: { correct: true, attempts: 1, at: at("2026-10-03T09:05:00Z") },
        q2: { correct: false, attempts: 2, at: at("2026-10-03T09:10:00Z") },
        // The day before, in Pakistan time.
        q3: { correct: true, attempts: 1, at: at("2026-10-02T18:30:00Z") },
      },
    },
  },
  {
    owner: "accounts/u1/students/s1",
    data: { completed: false, updated_at: at("2026-10-03T11:00:00Z"), steps: { q1: { correct: true, attempts: 1, at: at("2026-10-03T11:00:00Z") } } },
  },
  {
    owner: "accounts/u2/students/s2",
    data: {
      // Late evening in Pakistan still counts for that day.
      completed: false,
      updated_at: at("2026-10-03T18:30:00Z"),
      steps: { q1: { correct: false, attempts: 1, at: at("2026-10-03T18:30:00Z") } },
    },
  },
  {
    // Nothing that day.
    owner: "accounts/u3/students/s3",
    data: { completed: true, updated_at: at("2026-10-01T10:00:00Z"), steps: { q1: { correct: true, attempts: 1, at: at("2026-10-01T10:00:00Z") } } },
  },
];

describe("daily learning totals", () => {
  it("counts one day in Pakistan time, totals only", () => {
    assert.deepEqual(countDay(DAY, docs, { calls: 7, cost_usd: 0.0123456789 }), {
      day: DAY,
      students_active: 2,
      lessons_active: 3,
      lessons_finished: 1,
      questions_answered: 4,
      first_try_correct: 2,
      ai_calls: 7,
      ai_cost_usd: 0.012346,
    });
  });

  it("ignores documents without steps or dates", () => {
    const totals = countDay(DAY, [{ owner: "x", data: {} }, { owner: "y", data: { steps: { a: { correct: true } } } }], { calls: 0, cost_usd: 0 });
    assert.equal(totals.questions_answered, 0);
    assert.equal(totals.students_active, 0);
  });

  it("counts yesterday once, after midnight in Pakistan", async () => {
    const now = new Date("2026-10-03T19:30:00Z"); // 00:30 on 4 October in Pakistan
    assert.equal(yesterday(now), DAY);
    const store = new MemoryStore();
    store.progressDocs = docs;
    store.aiCalls.set(DAY, 7);
    assert.equal(await countYesterday(store, now), DAY);
    assert.equal(store.daily.get(DAY)!.questions_answered, 4);
    // No child ids or names are stored.
    assert.doesNotMatch(JSON.stringify([...store.daily.values()]), /u1|s1|accounts/);
    assert.equal(await countYesterday(store, now), null);
  });
});
