/**
 * The AI proxy's logic: checks, limits, the Claude call, cost tracking,
 * logging and fallbacks. No Firebase imports, so it is tested with fakes.
 */
import type { ClaudeCaller, JsonReply } from "./claude";
import { NoReplyError, imageType } from "./claude";
import { LIMITS, MODELS, dayOf, type Limits } from "./config";
import type { AiExplainStep, LessonLibrary, PhotoCheckStep } from "./lessons";
import { costOf } from "./pricing";
import {
  FEEDBACK_SCHEMA,
  FEEDBACK_SYSTEM,
  PHOTO_SCHEMA,
  PHOTO_SYSTEM,
  PROMPT_IDS,
  explainMessage,
  photoMessage,
  verdictMessage,
  type Feedback,
  type Lang,
  type PhotoReading,
} from "./prompts";
import type { Kind, Reservation, Store } from "./store";

export interface Deps {
  store: Store;
  claude: ClaudeCaller;
  lessons: LessonLibrary;
  now: () => Date;
  limits?: Limits;
}

/** A request the app's input made impossible (the app shows its fallback). */
export class BadRequest extends Error {}

/** Why a reply is a fallback, for the app and the logs. */
export type FallbackReason = "student_limit" | "step_limit" | "budget" | "unknown_step" | "error";

export interface FeedbackRequest {
  student_id: string;
  lesson_id: string;
  step_id: string;
  lang: Lang;
  /** explain: an ai_explain step. verdict: explain a checker's verdict on a photo_check step. */
  kind: "explain" | "verdict";
  answer: string;
  /** verdict only: the app's checker message. */
  checker_message?: string;
}

export type FeedbackResponse =
  | { checked_by: "ai"; level: Feedback["level"]; reply: string }
  | { checked_by: "fallback"; reason: FallbackReason };

export interface PhotoRequest {
  student_id: string;
  lesson_id: string;
  step_id: string;
  /** JPEG, PNG or WebP, base64. */
  image: string;
}

export type PhotoResponse =
  | { checked_by: "ai"; readable: boolean; lines: string[]; final_answer: string }
  | { checked_by: "fallback"; reason: FallbackReason };

function str(value: unknown, name: string, max = 200): string {
  if (typeof value !== "string" || value.length === 0 || value.length > max) {
    throw new BadRequest(`${name} is missing or too long`);
  }
  return value;
}

/** Reads and checks the app's request. Unknown fields are ignored. */
export function parseFeedbackRequest(data: unknown): FeedbackRequest {
  const d = (data ?? {}) as Record<string, unknown>;
  const lang = d.lang === "ur" ? "ur" : "en";
  const kind = d.kind === "verdict" ? "verdict" : "explain";
  const answer = typeof d.answer === "string" ? d.answer.trim().slice(0, LIMITS.maxAnswerChars) : "";
  if (!answer) throw new BadRequest("answer is empty");
  return {
    student_id: str(d.student_id, "student_id", 100),
    lesson_id: str(d.lesson_id, "lesson_id"),
    step_id: str(d.step_id, "step_id"),
    lang,
    kind,
    answer,
    checker_message: kind === "verdict" ? str(d.checker_message, "checker_message", 500) : undefined,
  };
}

export function parsePhotoRequest(data: unknown): PhotoRequest {
  const d = (data ?? {}) as Record<string, unknown>;
  const image = str(d.image, "image", Math.ceil((LIMITS.maxPhotoBytes * 4) / 3) + 4);
  if (!/^[A-Za-z0-9+/]+=*$/.test(image)) throw new BadRequest("image is not base64");
  if (!imageType(image)) throw new BadRequest("image is not a JPEG, PNG or WebP photo");
  return {
    student_id: str(d.student_id, "student_id", 100),
    lesson_id: str(d.lesson_id, "lesson_id"),
    step_id: str(d.step_id, "step_id"),
    image,
  };
}

/** Throws BadRequest when the student isn't in the caller's account. */
async function checkStudent(deps: Deps, uid: string, studentId: string) {
  if (!(await deps.store.studentExists(uid, studentId))) {
    throw new BadRequest("not a student of this account");
  }
}

interface Call<T> {
  uid: string;
  studentId: string;
  lessonId: string;
  stepId: string;
  lang: string;
  kind: Kind;
  stepLimit: number;
  promptId: string;
  input: string;
  run: () => Promise<JsonReply<T>>;
  concern: (data: T) => boolean;
}

/** Reserve a place under the limits, call Claude, record cost, log. */
async function guardedCall<T>(deps: Deps, call: Call<T>): Promise<{ ok: true; data: T } | { ok: false; reason: FallbackReason }> {
  const limits = deps.limits ?? LIMITS;
  const day = dayOf(deps.now());
  const reservation: Reservation = {
    uid: call.uid,
    studentId: call.studentId,
    day,
    kind: call.kind,
    stepKey: `${call.lessonId}/${call.stepId}`,
    kindLimit: call.kind === "photo" ? limits.photoPerDay : limits.textPerDay,
    stepLimit: call.stepLimit,
    globalDailyUsd: limits.globalDailyUsd,
  };
  const base = {
    uid: call.uid,
    student_id: call.studentId,
    prompt_id: call.promptId,
    lesson_id: call.lessonId,
    step_id: call.stepId,
    lang: call.lang,
    input: call.input,
    batch: false,
  };

  const reserved = await deps.store.reserve(reservation);
  if (reserved !== "ok") {
    await deps.store.log({
      ...base, output: null, model: null, checked_by: "fallback", reason: reserved, concern: false, cost_usd: 0,
    });
    return { ok: false, reason: reserved };
  }

  try {
    const reply = await call.run();
    const cost = costOf(reply.model, reply.usage);
    await deps.store.recordUsage({ uid: call.uid, studentId: call.studentId, day, calls: 1, usage: reply.usage, costUsd: cost });
    await deps.store.log({
      ...base, output: reply.data, model: reply.model, checked_by: "ai", reason: null,
      concern: call.concern(reply.data), cost_usd: cost,
    });
    return { ok: true, data: reply.data };
  } catch (error) {
    // A refused or broken reply still cost tokens; record them.
    let cost = 0;
    if (error instanceof NoReplyError && error.usage) {
      cost = costOf(error.model ?? "", error.usage);
      await deps.store.recordUsage({ uid: call.uid, studentId: call.studentId, day, calls: 1, usage: error.usage, costUsd: cost });
    }
    await deps.store.release(reservation);
    await deps.store.log({
      ...base, output: { error: String(error) }, model: null, checked_by: "fallback", reason: "error",
      concern: false, cost_usd: cost,
    });
    return { ok: false, reason: "error" };
  }
}

/** Checks the reply's shape; a bad one counts its tokens, then falls back. */
export function validFeedback(reply: JsonReply<Feedback>): Feedback {
  const data = reply.data;
  if (!["got_it", "partly", "not_yet"].includes(data?.level) || typeof data.reply !== "string" || !data.reply.trim()) {
    throw new NoReplyError("feedback has the wrong shape", reply.usage, reply.model);
  }
  return { level: data.level, reply: data.reply.trim(), concern: data.concern === true };
}

/** aiFeedback: feedback on an explanation, or an explanation of a checker's verdict. */
export async function feedback(deps: Deps, uid: string, request: FeedbackRequest): Promise<FeedbackResponse> {
  await checkStudent(deps, uid, request.student_id);
  const limits = deps.limits ?? LIMITS;

  let message: { promptId: string; text: string };
  let stepLimit: number;
  if (request.kind === "explain") {
    const found = deps.lessons.find<AiExplainStep>(request.lesson_id, request.step_id, "ai_explain");
    if (!found) return { checked_by: "fallback", reason: "unknown_step" };
    message = explainMessage(found.lesson, found.step, request.lang, request.answer);
    stepLimit = found.step.limit_per_day ?? limits.stepPerDay;
  } else {
    const found = deps.lessons.find<PhotoCheckStep>(request.lesson_id, request.step_id, "photo_check");
    if (!found) return { checked_by: "fallback", reason: "unknown_step" };
    message = verdictMessage(found.lesson, found.step, request.lang, request.answer, request.checker_message ?? "");
    // One explanation per photo, plus a typed retry.
    stepLimit = (found.step.limit_per_day ?? limits.stepPerDay) * 2;
  }

  const result = await guardedCall<Feedback>(deps, {
    uid,
    studentId: request.student_id,
    lessonId: request.lesson_id,
    stepId: request.step_id,
    lang: request.lang,
    kind: "text",
    stepLimit,
    promptId: message.promptId,
    input: request.kind === "verdict" ? `${request.answer}\n[checker] ${request.checker_message}` : request.answer,
    run: async () => {
      const reply = await deps.claude.json<Feedback>({
        model: MODELS.text,
        system: FEEDBACK_SYSTEM,
        text: message.text,
        schema: FEEDBACK_SCHEMA,
        maxTokens: 400,
      });
      return { ...reply, data: validFeedback(reply) };
    },
    concern: (data) => data.concern,
  });
  if (!result.ok) return { checked_by: "fallback", reason: result.reason };
  // A verdict explanation never says "got it": the checker decided.
  const level = request.kind === "verdict" ? "not_yet" : result.data.level;
  return { checked_by: "ai", level, reply: result.data.reply };
}

function validReading(reply: JsonReply<PhotoReading>): PhotoReading {
  const data = reply.data;
  if (typeof data?.readable !== "boolean" || !Array.isArray(data.lines)) {
    throw new NoReplyError("reading has the wrong shape", reply.usage, reply.model);
  }
  const lines = data.lines
    .filter((l): l is string => typeof l === "string")
    .map((l) => l.trim())
    .filter((l) => l.length > 0)
    .slice(0, 20);
  return {
    readable: data.readable && lines.length > 0,
    lines,
    final_answer: typeof data.final_answer === "string" ? data.final_answer.trim() : "",
    concern: data.concern === true,
  };
}

/** photoRead: AI copies the working from a notebook photo. The app's checker decides. */
export async function readPhoto(deps: Deps, uid: string, request: PhotoRequest): Promise<PhotoResponse> {
  await checkStudent(deps, uid, request.student_id);
  const limits = deps.limits ?? LIMITS;
  if (Buffer.byteLength(request.image, "base64") > limits.maxPhotoBytes) {
    throw new BadRequest("photo is too big");
  }
  const found = deps.lessons.find<PhotoCheckStep>(request.lesson_id, request.step_id, "photo_check");
  if (!found) return { checked_by: "fallback", reason: "unknown_step" };

  const result = await guardedCall<PhotoReading>(deps, {
    uid,
    studentId: request.student_id,
    lessonId: request.lesson_id,
    stepId: request.step_id,
    lang: "-",
    kind: "photo",
    stepLimit: found.step.limit_per_day ?? limits.stepPerDay,
    promptId: PROMPT_IDS.photoRead,
    // The photo itself is never stored; the log keeps what was read.
    input: "[photo]",
    run: async () => {
      const reply = await deps.claude.json<PhotoReading>({
        model: MODELS.photo,
        system: PHOTO_SYSTEM,
        text: photoMessage(found.lesson, found.step),
        imageBase64: request.image,
        schema: PHOTO_SCHEMA,
        maxTokens: 2000,
      });
      return { ...reply, data: validReading(reply) };
    },
    concern: (data) => data.concern,
  });
  if (!result.ok) return { checked_by: "fallback", reason: result.reason };
  const { readable, lines, final_answer } = result.data;
  return { checked_by: "ai", readable, lines, final_answer };
}
