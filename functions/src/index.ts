/**
 * Cloud Functions for AI Tutor (Phase 6). The Claude API key is the
 * ANTHROPIC_API_KEY secret in Google Secret Manager; it is never in the
 * code, the repository or the app.
 */
import Anthropic from "@anthropic-ai/sdk";
import { initializeApp } from "firebase-admin/app";
import { getFirestore } from "firebase-admin/firestore";
import { defineSecret, defineString } from "firebase-functions/params";
import { HttpsError, onCall, type CallableRequest } from "firebase-functions/v2/https";
import { onSchedule } from "firebase-functions/v2/scheduler";
import { logger } from "firebase-functions/v2";

import { BadRequest, feedback, parseFeedbackRequest, parsePhotoRequest, readPhoto, type Deps } from "./ai";
import { anthropicBatches, runBatchJob, submitWeeklyReports, type BatchDeps } from "./batch";
import { AnthropicCaller } from "./claude";
import { REGION } from "./config";
import { costReport, parseAdminEmails } from "./costs";
import { LessonLibrary } from "./lessons";
import { FirestoreStore } from "./store";

initializeApp();

const anthropicKey = defineSecret("ANTHROPIC_API_KEY");
/** Emails (comma-separated) that see every student's AI cost. */
const adminEmails = defineString("ADMIN_EMAILS", { default: "" });

let lessons: LessonLibrary | undefined;
const store = () => new FirestoreStore(getFirestore());

function deps(): Deps {
  lessons ??= LessonLibrary.fromDirectory();
  return { store: store(), claude: new AnthropicCaller(anthropicKey.value()), lessons, now: () => new Date() };
}

function batchDeps(): BatchDeps {
  lessons ??= LessonLibrary.fromDirectory();
  return {
    store: store(),
    batches: anthropicBatches(new Anthropic({ apiKey: anthropicKey.value() })),
    lessons,
    now: () => new Date(),
  };
}

const callable = { region: REGION, secrets: [anthropicKey], memory: "256MiB" as const, timeoutSeconds: 60 };

/** Signed in, or the call is refused. Bad input becomes invalid-argument. */
async function handle<T>(request: CallableRequest, run: (uid: string) => Promise<T>): Promise<T> {
  const uid = request.auth?.uid;
  if (!uid) throw new HttpsError("unauthenticated", "Sign in first.");
  try {
    return await run(uid);
  } catch (error) {
    if (error instanceof BadRequest) throw new HttpsError("invalid-argument", error.message);
    logger.error("AI function failed", error);
    throw new HttpsError("internal", "Something went wrong.");
  }
}

/** Feedback on an explanation, or an explanation of a checker's verdict. */
export const aiFeedback = onCall(callable, (request) =>
  handle(request, (uid) => feedback(deps(), uid, parseFeedbackRequest(request.data))),
);

/** Reads a notebook photo; the app's checker then decides. */
export const photoRead = onCall({ ...callable, memory: "512MiB" }, (request) =>
  handle(request, (uid) => readPhoto(deps(), uid, parsePhotoRequest(request.data))),
);

/** The cost dashboard. */
export const aiCosts = onCall({ region: REGION }, (request) =>
  handle(request, (uid) =>
    costReport(
      store(),
      { uid, email: request.auth?.token.email, emailVerified: request.auth?.token.email_verified },
      parseAdminEmails(adminEmails.value()),
      new Date(),
    ),
  ),
);

/** Collects finished batches and sends queued answers (half price). */
export const aiBatchJob = onSchedule(
  { schedule: "every 30 minutes", region: REGION, secrets: [anthropicKey], timeZone: "Asia/Karachi" },
  async () => {
    const summary = await runBatchJob(batchDeps());
    logger.info("AI batch job", summary);
  },
);

/** Weekly notes for parents, Sunday 18:00 Pakistan time. */
export const weeklyReports = onSchedule(
  { schedule: "0 18 * * 0", region: REGION, secrets: [anthropicKey], timeZone: "Asia/Karachi" },
  async () => {
    const count = await submitWeeklyReports(batchDeps());
    logger.info("Weekly reports sent to the batch", { count });
  },
);
