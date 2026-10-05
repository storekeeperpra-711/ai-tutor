/**
 * The AI Tutor AI server, a Cloudflare Worker (Phase 6). The app calls it
 * over HTTPS with the user's Firebase sign-in; it calls Claude and keeps
 * usage, limits and logs in Firestore.
 *
 * Secrets (set in the Cloudflare dashboard, never in code or the repo):
 *   ANTHROPIC_API_KEY          the Claude API key
 *   FIREBASE_SERVICE_ACCOUNT   the Firebase service account key (JSON text)
 * Variables:
 *   ADMIN_EMAILS               emails (comma-separated) that see every student's cost
 *
 * Routes (POST, JSON, "Authorization: Bearer <Firebase ID token>"):
 *   /v1/feedback   feedback on an explanation, or on a checker's verdict
 *   /v1/photo      reads a notebook photo (the app's checker then decides)
 *   /v1/costs      the cost dashboard
 * and GET /v1/voice/... for Mithu's recorded voice (voice.ts), from the KV
 * storage bound as VOICE.
 */
import Anthropic from "@anthropic-ai/sdk";

import { BadRequest, feedback, parseFeedbackRequest, parsePhotoRequest, readPhoto, type Deps } from "./ai";
import { Unauthenticated, bearerToken, firebaseVerifier, type TokenVerifier } from "./auth";
import { anthropicBatches, runBatchJob, submitWeeklyReports, type BatchDeps } from "./batch";
import { AnthropicCaller } from "./claude";
import { costReport, parseAdminEmails } from "./costs";
import { Firestore, parseServiceAccount } from "./firestore";
import { countYesterday } from "./learning";
import { LessonLibrary } from "./lessons";
import { FirestoreStore, type Store } from "./store";
import { handleVoice, isVoiceRequest, type VoiceStore } from "./voice";

export interface Env {
  ANTHROPIC_API_KEY: string;
  FIREBASE_SERVICE_ACCOUNT: string;
  ADMIN_EMAILS?: string;
  VOICE?: VoiceStore;
}

/** Cron schedules (UTC), as in wrangler.toml. */
export const CRON = {
  /** Collect finished batches, send queued answers, delete old logs, count yesterday's learning. */
  batchJob: "*/30 * * * *",
  /** Weekly notes for parents: Sunday 18:00 in Pakistan. */
  weeklyReports: "0 13 * * SUN",
} as const;

/** Largest request body accepted (a compressed photo is well under this). */
const MAX_BODY_BYTES = 3_000_000;

/** What a request needs; built from [Env] in production, faked in tests. */
export interface Services {
  verify: TokenVerifier;
  deps: () => Deps;
  store: () => Store;
  adminEmails: string[];
}

// Reused while the Worker instance lives (saves sign-ins and parsing).
let cached: { key: string; firestore: Firestore; lessons: LessonLibrary } | undefined;

function shared(env: Env) {
  const key = env.FIREBASE_SERVICE_ACCOUNT;
  if (cached?.key !== key) {
    cached = { key, firestore: new Firestore(parseServiceAccount(key)), lessons: LessonLibrary.bundled() };
  }
  return cached;
}

export function services(env: Env): Services {
  const { firestore, lessons } = shared(env);
  const projectId = parseServiceAccount(env.FIREBASE_SERVICE_ACCOUNT).project_id;
  return {
    verify: firebaseVerifier(projectId),
    store: () => new FirestoreStore(firestore),
    deps: () => ({
      store: new FirestoreStore(firestore),
      claude: new AnthropicCaller(env.ANTHROPIC_API_KEY),
      lessons,
      now: () => new Date(),
    }),
    adminEmails: parseAdminEmails(env.ADMIN_EMAILS ?? ""),
  };
}

function json(status: number, body: unknown): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" },
  });
}

/** Signed in, or 401. Bad input is 400; anything else 500 (the app then uses its fallback). */
export async function handleRequest(request: Request, svc: Services): Promise<Response> {
  const path = new URL(request.url).pathname;
  const routes = ["/v1/feedback", "/v1/photo", "/v1/costs"];
  if (!routes.includes(path)) return json(404, { error: "not found" });
  if (request.method !== "POST") return json(405, { error: "use POST" });
  try {
    const caller = await svc.verify(bearerToken(request.headers.get("authorization")));
    if (Number(request.headers.get("content-length") ?? 0) > MAX_BODY_BYTES) throw new BadRequest("request is too large");
    const text = await request.text();
    if (text.length > MAX_BODY_BYTES) throw new BadRequest("request is too large");
    let data: unknown;
    try {
      data = text ? JSON.parse(text) : {};
    } catch {
      throw new BadRequest("request is not JSON");
    }
    switch (path) {
      case "/v1/feedback":
        return json(200, await feedback(svc.deps(), caller.uid, parseFeedbackRequest(data)));
      case "/v1/photo":
        return json(200, await readPhoto(svc.deps(), caller.uid, parsePhotoRequest(data)));
      default:
        return json(200, await costReport(svc.store(), caller, svc.adminEmails, new Date()));
    }
  } catch (error) {
    if (error instanceof Unauthenticated) return json(401, { error: error.message });
    if (error instanceof BadRequest) return json(400, { error: error.message });
    console.error("AI request failed", path, String(error));
    return json(500, { error: "something went wrong" });
  }
}

/** The scheduled jobs. Writes are held and sent together at the end. */
export async function runScheduled(cron: string, deps: BatchDeps): Promise<unknown> {
  if (cron === CRON.weeklyReports) {
    const reports = await submitWeeklyReports(deps);
    await deps.store.flush();
    return { reports };
  }
  const summary = await runBatchJob(deps);
  const logsDeleted = await deps.store.deleteOldLogs(deps.now());
  const counted = await countYesterday(deps.store, deps.now());
  await deps.store.flush();
  return { ...summary, logsDeleted, counted };
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    // Recordings need no secrets, so they work even before the AI is set up.
    if (isVoiceRequest(request)) return handleVoice(request, env.VOICE);
    let svc: Services;
    try {
      svc = services(env);
    } catch (error) {
      // A secret is missing or wrong: the app falls back until it's fixed.
      console.error("AI server is not set up", String(error));
      return json(503, { error: "not set up" });
    }
    return handleRequest(request, svc);
  },

  async scheduled(controller: { cron: string }, env: Env): Promise<void> {
    const { firestore, lessons } = shared(env);
    const result = await runScheduled(controller.cron, {
      store: new FirestoreStore(firestore, { deferWrites: true }),
      batches: anthropicBatches(new Anthropic({ apiKey: env.ANTHROPIC_API_KEY })),
      lessons,
      now: () => new Date(),
    });
    console.log("Scheduled job", controller.cron, JSON.stringify(result));
  },
};
