/**
 * Daily learning totals for the whole project (Phase 10): counted once a
 * day by the batch job from the progress the app already saves. Only
 * totals are stored, never anything about one child. There is no Google
 * Analytics: these numbers are how we see whether the app is used.
 */
import { dayOf } from "./config";
import type { Store } from "./store";

export interface DailyTotals {
  day: string;
  /** Children who answered at least one question that day. */
  students_active: number;
  /** Lessons with at least one answer that day. */
  lessons_active: number;
  /** Lessons finished that day. */
  lessons_finished: number;
  questions_answered: number;
  first_try_correct: number;
  /** AI calls and their estimated cost (all children together). */
  ai_calls: number;
  ai_cost_usd: number;
}

/** One saved lesson-progress document, with the child it belongs to. */
export interface ProgressDoc {
  /** A key for the child (only used to count children, never stored). */
  owner: string;
  data: Record<string, unknown>;
}

const isDate = (v: unknown): v is Date => v instanceof Date && !Number.isNaN(v.getTime());

/** Counts [day] (Pakistan time) from everyone's progress documents. */
export function countDay(
  day: string,
  docs: ProgressDoc[],
  ai: { calls: number; cost_usd: number },
): DailyTotals {
  const students = new Set<string>();
  let lessonsActive = 0;
  let lessonsFinished = 0;
  let answered = 0;
  let firstTry = 0;
  for (const doc of docs) {
    const steps = (doc.data.steps ?? {}) as Record<string, Record<string, unknown>>;
    let touched = false;
    for (const step of Object.values(steps)) {
      if (!isDate(step?.at) || dayOf(step.at) !== day) continue;
      touched = true;
      // Only questions are right or wrong (video and reading steps are null).
      if (typeof step.correct !== "boolean") continue;
      answered++;
      // The app saves "correct" only for a right answer on the first try.
      if (step.correct) firstTry++;
    }
    if (touched) {
      lessonsActive++;
      students.add(doc.owner);
    }
    const updated = doc.data.updated_at;
    if (doc.data.completed === true && isDate(updated) && dayOf(updated) === day) lessonsFinished++;
  }
  return {
    day,
    students_active: students.size,
    lessons_active: lessonsActive,
    lessons_finished: lessonsFinished,
    questions_answered: answered,
    first_try_correct: firstTry,
    ai_calls: ai.calls,
    ai_cost_usd: Math.round(ai.cost_usd * 1e6) / 1e6,
  };
}

/** Yesterday in Pakistan: the last whole day to count. */
export function yesterday(now: Date): string {
  return dayOf(new Date(now.getTime() - 86_400_000));
}

/**
 * Counts yesterday once: the batch job runs every 30 minutes, so this
 * checks whether yesterday is already counted and, if not, counts it.
 * Returns the day counted, or null if there was nothing to do.
 */
export async function countYesterday(store: Store, now: Date): Promise<string | null> {
  const day = yesterday(now);
  if (await store.hasDailyTotals(day)) return null;
  const [docs, ai] = await Promise.all([store.allProgress(), store.projectUsage(day)]);
  await store.saveDailyTotals(countDay(day, docs, ai));
  return day;
}
