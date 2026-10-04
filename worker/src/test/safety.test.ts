import assert from "node:assert/strict";
import { describe, it } from "node:test";

import { redactPersonal } from "../privacy";
import { SAFETY_MESSAGES } from "../safety/messages";
import { problemsOf, report } from "../safety/run";

describe("AI safety test set", () => {
  it("has about 40 messages with unique ids in every category", () => {
    assert.ok(SAFETY_MESSAGES.length >= 40);
    assert.equal(new Set(SAFETY_MESSAGES.map((m) => m.id)).size, SAFETY_MESSAGES.length);
    const categories = new Set(SAFETY_MESSAGES.map((m) => m.category));
    for (const c of ["normal", "worrying", "personal", "off_topic", "rude", "trick"]) assert.ok(categories.has(c as never), c);
  });

  it("phone numbers, emails and addresses in the set are removed before the AI", () => {
    for (const m of SAFETY_MESSAGES.filter((m) => ["personal-1", "personal-2", "personal-3", "personal-4", "personal-6"].includes(m.id))) {
      assert.notDeepEqual(redactPersonal(m.text).removed, [], m.id);
    }
  });

  it("finds broken expectations", () => {
    const worry = SAFETY_MESSAGES.find((m) => m.id === "worry-1")!;
    assert.deepEqual(problemsOf(worry, "not_yet", "Please talk to a teacher.", true), []);
    assert.deepEqual(problemsOf(worry, "not_yet", "Let's do maths.", false), ["concern not flagged"]);
    const rude = SAFETY_MESSAGES.find((m) => m.id === "rude-1")!;
    assert.deepEqual(problemsOf(rude, "got_it", "You called me an Idiot!", false), ['level was "got_it"', 'reply contains "idiot"']);
    assert.deepEqual(problemsOf(rude, null, null, false), ["no AI reply (fallback)"]);
  });

  it("writes a readable report", () => {
    const m = SAFETY_MESSAGES[0];
    const text = report([{ message: m, sent: m.text, level: "got_it", reply: "Well | done", concern: false, costUsd: 0.001, problems: [] }], new Date("2026-10-04T10:00:00Z"));
    assert.match(text, /1 of 1 passed/);
    assert.match(text, /Well \\\| done/);
  });
});
