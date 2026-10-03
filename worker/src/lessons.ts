/**
 * The server's own copy of the lessons (bundled in at build time by
 * scripts/copy-lessons.mjs). Prompts are built from these, so the app can
 * only name a lesson and a step, never send prompt text.
 */
import { LESSONS } from "./generated/lessons";

export interface Text {
  en: string;
  ur: string;
}

export interface Levels<T> {
  got_it: T;
  partly: T;
  not_yet: T;
}

export interface AiExplainStep {
  id: string;
  type: "ai_explain";
  task_kind?: "explain" | "own_question";
  task: Text;
  key_idea: string;
  levels: Levels<string>;
  limit_per_day?: number;
}

export interface PhotoCheckStep {
  id: string;
  type: "photo_check";
  problem: Text;
  checker: "numeric" | "fraction" | "chem_equation" | "linear_equation";
  expected: string;
  hint: Text;
  limit_per_day?: number;
}

export type AiStep = AiExplainStep | PhotoCheckStep;

export interface LessonInfo {
  id: string;
  subject: string;
  grade: number;
  title: Text;
}

export interface FoundStep<T extends AiStep> {
  lesson: LessonInfo;
  step: T;
}

/** Finds AI steps by lesson and step id. */
export class LessonLibrary {
  constructor(private readonly lessons: Map<string, Record<string, unknown>>) {}

  /** Every lesson in content/lessons/, as bundled at build time. */
  static bundled(): LessonLibrary {
    const lessons = new Map<string, Record<string, unknown>>();
    for (const lesson of LESSONS as Record<string, unknown>[]) lessons.set(String(lesson.id), lesson);
    return new LessonLibrary(lessons);
  }

  find<T extends AiStep>(lessonId: string, stepId: string, type: T["type"]): FoundStep<T> | null {
    const lesson = this.lessons.get(lessonId);
    if (!lesson) return null;
    const step = allSteps(lesson).find((s) => s.id === stepId && s.type === type);
    if (!step) return null;
    const info = lesson as unknown as LessonInfo;
    return {
      lesson: { id: info.id, subject: info.subject, grade: info.grade, title: info.title },
      step: step as unknown as T,
    };
  }
}

type RawStep = { id?: unknown; type?: unknown };

/** Main steps, alternatives, question bank and review questions. */
function allSteps(lesson: Record<string, unknown>): RawStep[] {
  const steps: RawStep[] = [...((lesson.steps as RawStep[]) ?? [])];
  for (const alt of (lesson.alternatives as { steps?: RawStep[] }[]) ?? []) {
    steps.push(...(alt.steps ?? []));
  }
  const bank = (lesson.question_bank as Record<string, { step?: RawStep }[]>) ?? {};
  for (const questions of Object.values(bank)) {
    for (const q of questions) if (q.step) steps.push(q.step);
  }
  for (const q of (lesson.review_questions as { step?: RawStep }[]) ?? []) {
    if (q.step) steps.push(q.step);
  }
  return steps;
}
