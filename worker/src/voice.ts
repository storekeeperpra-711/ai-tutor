/**
 * Mithu's recorded voice for the app (tools/voice/make_voice.py makes the
 * recordings once, in GitHub Actions, and stores them in KV).
 *
 * Routes (GET, no sign-in: the recordings are lesson content, the same for
 * every child):
 *   /v1/voice/index          which recordings exist: {"voice", "files": {name: hash}}
 *   /v1/voice/<name>.m4a     one recording
 *   /v1/voice/<name>.mouth   how loud it is over time, for Mithu's beak
 */

/** The part of Cloudflare's KV binding used here. */
export interface VoiceStore {
  get(key: string, options: { type: "arrayBuffer"; cacheTtl?: number }): Promise<ArrayBuffer | null>;
}

const PREFIX = "/v1/voice/";

/** Lesson ids, step ids and languages: lower-case letters, digits, - and _. */
const NAME = /^[a-z0-9_-]+\.(m4a|mouth)$/;

const TYPES: Record<string, string> = {
  index: "application/json; charset=utf-8",
  m4a: "audio/mp4",
  mouth: "text/plain; charset=utf-8",
};

export function isVoiceRequest(request: Request): boolean {
  return new URL(request.url).pathname.startsWith(PREFIX);
}

export async function handleVoice(request: Request, store: VoiceStore | undefined): Promise<Response> {
  const key = new URL(request.url).pathname.slice(PREFIX.length);
  if (request.method !== "GET") return new Response("use GET", { status: 405 });
  if (key !== "index" && !NAME.test(key)) return new Response("not found", { status: 404 });
  if (!store) return new Response("not set up", { status: 503 });
  const isIndex = key === "index";
  // KV keeps a copy near the phone for a while, which saves reads.
  const value = await store.get(key, { type: "arrayBuffer", cacheTtl: isIndex ? 300 : 3600 });
  if (value === null) return new Response("not found", { status: 404 });
  return new Response(value, {
    headers: {
      "content-type": TYPES[isIndex ? "index" : key.slice(key.lastIndexOf(".") + 1)],
      // The app asks for a recording with ?v=<hash>, so a new recording is a
      // new address and an old one can be kept for long.
      "cache-control": isIndex ? "public, max-age=300" : "public, max-age=86400",
    },
  });
}
