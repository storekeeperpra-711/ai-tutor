# worker

The AI server for AI Tutor (Phase 6): a Cloudflare Worker that calls Claude. The app never calls Claude itself.

- **Routes** (POST, JSON, `Authorization: Bearer <Firebase ID token>`): `/v1/feedback`, `/v1/photo`, `/v1/costs`.
- **Scheduled runs** (`wrangler.toml`): every 30 minutes, the batch job (queued answers, finished batches, old logs); Sundays 13:00 UTC (18:00 in Pakistan), weekly reports.
- **Firestore**: read and written over the REST API as the Firebase service account (`src/firestore.ts`), so the security rules don't apply to it. The layout is in `src/store.ts`.

| File | What it does |
|---|---|
| `src/worker.ts` | Routes, the sign-in check, scheduled runs |
| `src/auth.ts` | Checks Firebase ID tokens against Google's keys |
| `src/ai.ts` | Feedback and photo reading: limits, the Claude call, costs, logs, fallbacks |
| `src/batch.ts` | Queued answers and weekly reports through the Batch API (half price) |
| `src/prompts.ts` | Every prompt and reply schema (the prompt registry) |
| `src/config.ts` | Models, limits and the daily cap |
| `src/lessons.ts` | The server's own copy of the lessons (bundled from `content/lessons/`) |

## Secrets

The Claude API key and the Firebase service account key are **never** in this repository or the app. They are Worker secrets, set in the Cloudflare dashboard: `ANTHROPIC_API_KEY`, `FIREBASE_SERVICE_ACCOUNT`, plus the text variable `ADMIN_EMAILS`. Setup steps: [docs/setup/ai-setup.md](../docs/setup/ai-setup.md).

## Commands

```sh
npm ci
npm test          # type-check and run the tests (a fake Claude: no key, no cost)
```

Deploying is done by the **Deploy AI server** GitHub workflow (`.github/workflows/deploy-worker.yml`).

To run it on your own computer, put the two secrets in `worker/.dev.vars` (ignored by git) and run `npx wrangler dev --env dev`.
