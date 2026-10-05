import assert from "node:assert/strict";
import { describe, it } from "node:test";

import { handleVoice, isVoiceRequest, type VoiceStore } from "../voice";

function store(values: Record<string, string>): VoiceStore & { keys: string[] } {
  const keys: string[] = [];
  return {
    keys,
    async get(key) {
      keys.push(key);
      return key in values ? (new TextEncoder().encode(values[key]).buffer as ArrayBuffer) : null;
    },
  };
}

const get = (path: string, method = "GET") => new Request(`https://ai.example.com${path}`, { method });

describe("Mithu's voice", () => {
  const kv = store({
    index: '{"voice":"Sulafat","files":{"g9-a__s1_ur.m4a":"abc"}}',
    "g9-a__s1_ur.m4a": "audio",
    "g9-a__s1_ur.mouth": "0123",
  });

  it("is only the /v1/voice/ routes", () => {
    assert.ok(isVoiceRequest(get("/v1/voice/index")));
    assert.ok(!isVoiceRequest(get("/v1/feedback")));
  });

  it("hands out the index, recordings and beak tracks", async () => {
    const index = await handleVoice(get("/v1/voice/index"), kv);
    assert.equal(index.status, 200);
    assert.equal((await index.json()).voice, "Sulafat");

    const audio = await handleVoice(get("/v1/voice/g9-a__s1_ur.m4a?v=abc"), kv);
    assert.equal(audio.status, 200);
    assert.equal(audio.headers.get("content-type"), "audio/mp4");
    assert.equal(await audio.text(), "audio");

    const mouth = await handleVoice(get("/v1/voice/g9-a__s1_ur.mouth"), kv);
    assert.equal(await mouth.text(), "0123");
  });

  it("reads only recording names from storage", async () => {
    const before = kv.keys.length;
    for (const path of ["/v1/voice/secret", "/v1/voice/../index", "/v1/voice/A.m4a", "/v1/voice/a.mp3"]) {
      assert.equal((await handleVoice(get(path), kv)).status, 404, path);
    }
    assert.equal(kv.keys.length, before);
    assert.equal((await handleVoice(get("/v1/voice/g9-b__s1_ur.m4a"), kv)).status, 404);
    assert.equal((await handleVoice(get("/v1/voice/index", "POST"), kv)).status, 405);
  });

  it("says when the storage isn't set up", async () => {
    assert.equal((await handleVoice(get("/v1/voice/index"), undefined)).status, 503);
  });
});
