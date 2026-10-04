/**
 * Work that can wait goes through the Message Batches API at half price
 * (spec D6, D9): answers that queued while a phone was offline, and the
 * weekly notes to parents.
 */
import type Anthropic from "@anthropic-ai/sdk";

import { validFeedback } from "./ai";
import { parseReply, requestParams } from "./claude";
import { LIMITS, MODELS, dayOf, type Limits } from "./config";
import type { AiExplainStep, LessonLibrary } from "./lessons";
import { costOf } from "./pricing";
import {
  FEEDBACK_SCHEMA,
  FEEDBACK_SYSTEM,
  PROMPT_IDS,
  REPORT_SCHEMA,
  REPORT_SYSTEM,
  explainMessage,
  reportMessage,
  type Feedback,
  type Lang,
  type ReportNote,
  type WeekStats,
} from "./prompts";
import { redactPersonal } from "./privacy";
import type { BatchInfo, Store } from "./store";

/** The parts of the Batch API the jobs use (a fake in tests). */
export interface BatchApi {
  create(requests: { custom_id: string; params: Anthropic.MessageCreateParamsNonStreaming }[]): Promise<{ id: string }>;
  isEnded(id: string): Promise<boolean>;
  results(id: string): AsyncIterable<{ custom_id: string; message: Parameters<typeof parseReply>[0] | null }>;
}

export interface BatchDeps {
  store: Store;
  batches: BatchApi;
  lessons: LessonLibrary;
  now: () => Date;
  limits?: Limits;
}

/** Queued answers older than this are skipped: the moment has passed. */
const MAX_AGE_DAYS = 7;

export interface JobSummary {
  collected: number;
  submitted: number;
  skipped: number;
}

/** Runs every 30 minutes: collect finished batches, then send new work. */
export async function runBatchJob(deps: BatchDeps): Promise<JobSummary> {
  const collected = await collectBatches(deps);
  const { submitted, skipped } = await submitQueuedAnswers(deps);
  return { collected, submitted, skipped };
}

async function collectBatches(deps: BatchDeps): Promise<number> {
  let collected = 0;
  for (const batch of await deps.store.openBatches()) {
    if (!(await deps.batches.isEnded(batch.id))) continue;
    const seen = new Set<string>();
    for await (const result of deps.batches.results(batch.id)) {
      const item = batch.items[result.custom_id];
      if (!item) continue;
      seen.add(result.custom_id);
      await collectOne(deps, batch, result.custom_id, result.message);
      collected++;
    }
    // Anything without a result (expired, cancelled) is closed too.
    for (const [customId, item] of Object.entries(batch.items)) {
      if (!seen.has(customId) && item.kind === "answer") await deps.store.answerQueued(customId.slice(2), null);
    }
    await deps.store.closeBatch(batch.id);
  }
  return collected;
}

async function collectOne(
  deps: BatchDeps,
  batch: BatchInfo,
  customId: string,
  message: Parameters<typeof parseReply>[0] | null,
): Promise<void> {
  const item = batch.items[customId];
  const day = dayOf(deps.now());
  let output: unknown = null;
  let cost = 0;
  let model: string | null = null;
  try {
    if (!message) throw new Error("errored or expired");
    model = message.model;
    cost = costOf(message.model, message.usage, true);
    await deps.store.recordUsage({
      uid: item.uid, studentId: item.student_id, day, calls: 1, usage: message.usage, costUsd: cost,
    });
    if (item.kind === "answer") {
      const feedback = validFeedback(parseReply<Feedback>(message));
      output = feedback;
      await deps.store.answerQueued(customId.slice(2), { level: feedback.level, reply: feedback.reply });
    } else {
      const note = parseReply<ReportNote>(message).data;
      if (typeof note?.en !== "string" || typeof note?.ur !== "string") throw new Error("report has the wrong shape");
      output = note;
      await deps.store.saveReport(item.uid, item.student_id, item.week!, item.stats, note);
    }
  } catch (error) {
    output = { error: String(error) };
    if (item.kind === "answer") await deps.store.answerQueued(customId.slice(2), null);
  }
  const ok = !(output && typeof output === "object" && "error" in output);
  await deps.store.log({
    uid: item.uid,
    student_id: item.student_id,
    prompt_id: item.kind === "answer" ? "batch_answer" : PROMPT_IDS.report,
    lesson_id: "",
    step_id: customId,
    lang: "-",
    input: item.kind === "answer" ? "[queued answer]" : JSON.stringify(item.stats),
    output,
    model,
    checked_by: ok ? "ai" : "fallback",
    reason: ok ? null : "error",
    concern: ok && (output as Feedback).concern === true,
    cost_usd: cost,
    batch: true,
  });
}

/** Sends answers that waited offline to the Batch API. */
export async function submitQueuedAnswers(deps: BatchDeps): Promise<{ submitted: number; skipped: number }> {
  const limits = deps.limits ?? LIMITS;
  const now = deps.now();
  if ((await deps.store.projectCost(dayOf(now))) >= limits.globalDailyUsd) {
    return { submitted: 0, skipped: 0 }; // Wait for tomorrow's budget.
  }
  const waiting = await deps.store.waitingAnswers(500);
  const perStudent = new Map<string, number>();
  const requests: { custom_id: string; params: Anthropic.MessageCreateParamsNonStreaming }[] = [];
  const items: BatchInfo["items"] = {};
  const skipped: string[] = [];

  for (const answer of waiting) {
    const found = deps.lessons.find<AiExplainStep>(answer.lesson_id, answer.step_id, "ai_explain");
    const age = (now.getTime() - answer.created_at.getTime()) / 86_400_000;
    const count = perStudent.get(answer.student_id) ?? 0;
    const typed = typeof answer.answer === "string" ? answer.answer.trim().slice(0, limits.maxAnswerChars) : "";
    // Phone numbers, emails and addresses never reach Claude.
    const text = redactPersonal(typed).text;
    if (!found || age > MAX_AGE_DAYS || count >= limits.queuedPerDay || !text) {
      skipped.push(answer.id);
      continue;
    }
    perStudent.set(answer.student_id, count + 1);
    const lang: Lang = answer.lang === "ur" ? "ur" : "en";
    const message = explainMessage(found.lesson, found.step, lang, text);
    // Queue ids are Firestore ids (letters and digits): valid custom ids.
    const customId = `a_${answer.id}`;
    requests.push({
      custom_id: customId,
      params: requestParams({
        model: MODELS.text, system: FEEDBACK_SYSTEM, text: message.text, schema: FEEDBACK_SCHEMA, maxTokens: 400,
      }),
    });
    items[customId] = { kind: "answer", uid: answer.uid, student_id: answer.student_id };
  }

  if (skipped.length) await deps.store.markQueued(skipped, "skipped");
  if (!requests.length) return { submitted: 0, skipped: skipped.length };
  const batch = await deps.batches.create(requests);
  await deps.store.saveBatch({ id: batch.id, items });
  await deps.store.markQueued(Object.keys(items).map((id) => id.slice(2)), "in_batch", batch.id);
  return { submitted: requests.length, skipped: skipped.length };
}

function toDate(value: unknown): Date | null {
  if (value == null) return null;
  if (value instanceof Date) return value;
  if (typeof value === "string") {
    const d = new Date(value);
    return isNaN(d.getTime()) ? null : d;
  }
  if (typeof (value as { toDate?: unknown }).toDate === "function") {
    return (value as { toDate: () => Date }).toDate();
  }
  return null;
}

/** Counts one student's week from the progress and skill documents the app saves. */
export function weekStats(
  grade: number,
  activity: { progress: Record<string, unknown>[]; skills: Record<string, unknown>[] },
  since: Date,
): WeekStats {
  const days = new Set<string>();
  let lessonsFinished = 0;
  let answered = 0;
  let firstTry = 0;
  for (const lesson of activity.progress) {
    const updated = toDate(lesson.updated_at);
    if (lesson.completed === true && updated && updated >= since) lessonsFinished++;
    const steps = (lesson.steps ?? {}) as Record<string, { correct?: boolean | null; at?: unknown }>;
    for (const step of Object.values(steps)) {
      const at = toDate(step.at);
      if (!at || at < since) continue;
      days.add(dayOf(at));
      if (step.correct === true || step.correct === false) {
        answered++;
        if (step.correct) firstTry++;
      }
    }
  }
  const after = (v: unknown) => {
    const d = toDate(v);
    return d !== null && d >= since;
  };
  return {
    grade,
    lessons_finished: lessonsFinished,
    questions_answered: answered,
    first_try_correct: firstTry,
    skills_practised: activity.skills.filter((s) => after(s.last_answered)).length,
    skills_mastered: activity.skills.filter((s) => after(s.mastered_at)).length,
    active_days: days.size,
  };
}

/** Runs every Sunday evening: a short note for each student who practised this week. */
export async function submitWeeklyReports(deps: BatchDeps): Promise<number> {
  const now = deps.now();
  const since = new Date(now.getTime() - 7 * 86_400_000);
  const week = dayOf(now);
  const requests: { custom_id: string; params: Anthropic.MessageCreateParamsNonStreaming }[] = [];
  const items: BatchInfo["items"] = {};
  for (const student of await deps.store.allStudents()) {
    const stats = weekStats(student.grade, await deps.store.studentActivity(student.uid, student.studentId), since);
    if (stats.active_days === 0) continue; // No practice: no note, no cost.
    const customId = `r_${requests.length}`;
    requests.push({
      custom_id: customId,
      params: requestParams({
        model: MODELS.text, system: REPORT_SYSTEM, text: reportMessage(stats), schema: REPORT_SCHEMA, maxTokens: 500,
      }),
    });
    items[customId] = { kind: "report", uid: student.uid, student_id: student.studentId, week, stats };
  }
  if (!requests.length) return 0;
  const batch = await deps.batches.create(requests);
  await deps.store.saveBatch({ id: batch.id, items });
  return requests.length;
}

/** The real Batch API. */
export function anthropicBatches(client: Anthropic): BatchApi {
  return {
    create: (requests) => client.messages.batches.create({ requests }),
    isEnded: async (id) => (await client.messages.batches.retrieve(id)).processing_status === "ended",
    async *results(id) {
      for await (const result of await client.messages.batches.results(id)) {
        yield {
          custom_id: result.custom_id,
          message: result.result.type === "succeeded" ? result.result.message : null,
        };
      }
    },
  };
}
