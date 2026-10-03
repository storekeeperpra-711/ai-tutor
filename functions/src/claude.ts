/**
 * The only place that calls the Claude API. Behind an interface so tests
 * use a fake and never call the real API.
 */
import Anthropic from "@anthropic-ai/sdk";

import { MODELS } from "./config";
import type { TokenUsage } from "./pricing";

export interface JsonRequest {
  model: string;
  system: string;
  /** Text of the user message. */
  text: string;
  /** Optional photo (JPEG, PNG or WebP), base64, placed before the text. */
  imageBase64?: string;
  schema: Record<string, unknown>;
  maxTokens: number;
}

export interface JsonReply<T> {
  data: T;
  model: string;
  usage: TokenUsage;
}

/** Thrown when Claude gives no usable reply; the caller then uses a fallback. */
export class NoReplyError extends Error {
  constructor(
    message: string,
    readonly usage?: TokenUsage,
    readonly model?: string,
  ) {
    super(message);
  }
}

export interface ClaudeCaller {
  json<T>(request: JsonRequest): Promise<JsonReply<T>>;
}

/** The image type from the first bytes of base64 data, or null if unknown. */
export function imageType(base64: string): "image/jpeg" | "image/png" | "image/webp" | null {
  if (base64.startsWith("/9j/")) return "image/jpeg";
  if (base64.startsWith("iVBORw0KGgo")) return "image/png";
  if (base64.startsWith("UklGR")) return "image/webp";
  return null;
}

/** The parameters of one request, shared by live calls and the Batch API. */
export function requestParams(request: JsonRequest): Anthropic.MessageCreateParamsNonStreaming {
  const content: Anthropic.ContentBlockParam[] = [];
  if (request.imageBase64) {
    content.push({
      type: "image",
      source: { type: "base64", media_type: imageType(request.imageBase64) ?? "image/jpeg", data: request.imageBase64 },
    });
  }
  content.push({ type: "text", text: request.text });
  const params: Anthropic.MessageCreateParamsNonStreaming = {
    model: request.model,
    max_tokens: request.maxTokens,
    // The fixed instructions come first and are cached once they are long
    // enough for the model's minimum (Haiku 4.5: 4096 tokens; Sonnet 5.5: 512).
    system: [{ type: "text", text: request.system, cache_control: { type: "ephemeral" } }],
    messages: [{ role: "user", content }],
    output_config: { format: { type: "json_schema", schema: request.schema } },
  };
  // Sonnet 5.5 always thinks; low effort is plenty for copying handwriting.
  // (Haiku 4.5 doesn't take an effort setting.)
  if (request.model === MODELS.photo) {
    params.output_config = { ...params.output_config, effort: "low" };
  }
  return params;
}

/** Reads the JSON reply out of a finished message, or throws [NoReplyError]. */
export function parseReply<T>(message: {
  stop_reason: string | null;
  content: Array<{ type: string; text?: string }>;
  model: string;
  usage: TokenUsage;
}): JsonReply<T> {
  if (message.stop_reason !== "end_turn") {
    throw new NoReplyError(`stop_reason ${message.stop_reason}`, message.usage, message.model);
  }
  const text = message.content.find((block) => block.type === "text")?.text;
  if (!text) throw new NoReplyError("no text", message.usage, message.model);
  try {
    return { data: JSON.parse(text) as T, model: message.model, usage: message.usage };
  } catch {
    throw new NoReplyError("invalid JSON", message.usage, message.model);
  }
}

export class AnthropicCaller implements ClaudeCaller {
  /** The key comes from the ANTHROPIC_API_KEY secret; never from code. */
  constructor(
    apiKey: string,
    private readonly client = new Anthropic({ apiKey, timeout: 25_000, maxRetries: 1 }),
  ) {}

  async json<T>(request: JsonRequest): Promise<JsonReply<T>> {
    const params = requestParams(request);
    if (request.model === MODELS.photo) {
      // If Sonnet 5.5's safety checks decline a photo by mistake, the API
      // retries it on the recommended fallback model in the same call.
      const message = await this.client.beta.messages.create({
        ...(params as Anthropic.Beta.MessageCreateParamsNonStreaming),
        betas: ["server-side-fallback-2026-07-01"],
        fallbacks: "default",
      });
      return parseReply<T>(message);
    }
    return parseReply<T>(await this.client.messages.create(params));
  }

  get batches() {
    return this.client.messages.batches;
  }
}
