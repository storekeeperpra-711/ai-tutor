/** Estimated cost of a Claude call, for the cost dashboard and the daily cap. */

/** US dollars per million tokens (Anthropic pricing, checked 2026-10-03). */
const PRICES: Record<string, { input: number; output: number }> = {
  "claude-haiku-4-5": { input: 1, output: 5 },
  "claude-sonnet-5-5": { input: 2, output: 10 },
};

/** Cache writes cost 1.25x the input price; cache reads 0.1x. */
const CACHE_WRITE = 1.25;
const CACHE_READ = 0.1;

export interface TokenUsage {
  input_tokens: number;
  output_tokens: number;
  cache_creation_input_tokens?: number | null;
  cache_read_input_tokens?: number | null;
}

/**
 * Cost in US dollars. Batch requests cost half. [model] may carry a date
 * (claude-haiku-4-5-20251001). Unknown models are priced as Sonnet.
 */
export function costOf(model: string, usage: TokenUsage, batch = false): number {
  const known = Object.keys(PRICES).find((id) => model.startsWith(id));
  const price = PRICES[known ?? "claude-sonnet-5-5"];
  const perToken = (perMillion: number) => perMillion / 1_000_000;
  const cost =
    usage.input_tokens * perToken(price.input) +
    (usage.cache_creation_input_tokens ?? 0) * perToken(price.input) * CACHE_WRITE +
    (usage.cache_read_input_tokens ?? 0) * perToken(price.input) * CACHE_READ +
    usage.output_tokens * perToken(price.output);
  return batch ? cost / 2 : cost;
}
