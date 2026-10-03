/** Settings for the AI features. Change limits and the daily cap here. */

/** Cloud Functions region, next to Firestore (Mumbai). */
export const REGION = "asia-south1";

/** Models (spec A3). Prices are checked on Anthropic's pricing page. */
export const MODELS = {
  /** Short text feedback, verdict explanations, weekly reports. */
  text: "claude-haiku-4-5",
  /** Reading photos of notebook working. */
  photo: "claude-sonnet-5-5",
} as const;

export const LIMITS = {
  /** Text checks (explanations, own questions, verdicts) per student per day. */
  textPerDay: 10,
  /** Photos read per student per day. */
  photoPerDay: 3,
  /** Default per-step limit when a lesson doesn't set limit_per_day. */
  stepPerDay: 3,
  /** Spending cap for the whole project per day, in US dollars. */
  globalDailyUsd: 0.5,
  /** Answers longer than this are cut (characters). */
  maxAnswerChars: 1500,
  /** Largest photo accepted (bytes, after base64 decoding). */
  maxPhotoBytes: 1_500_000,
  /** Queued offline answers sent to the batch job per student per day. */
  queuedPerDay: 10,
} as const;

export type Limits = { [K in keyof typeof LIMITS]: number };

/** How long AI logs are kept (Firestore TTL on `expire_at`). */
export const LOG_DAYS = 90;

/** Pakistan Standard Time (UTC+5, no daylight saving). */
const PKT_OFFSET_MS = 5 * 60 * 60 * 1000;

/** The day in Pakistan, e.g. "2026-10-03": daily limits reset at midnight there. */
export function dayOf(now: Date): string {
  return new Date(now.getTime() + PKT_OFFSET_MS).toISOString().slice(0, 10);
}
