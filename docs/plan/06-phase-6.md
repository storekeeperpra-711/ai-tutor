# Phase 6 plan: AI features

Status: built, waiting for setup and review. Date: 2026-10-03.
Spec: [master-prompt.md](../master-prompt.md), A3 (AI decision), D6 (AI layer), D8 (safety), D9 (costs) and Part F, Phase 6.

**Goal:** safe, cheap, useful AI feedback.
**Done when:** AI feedback works in both languages, limits and fallbacks are verified, a notebook photo with a deliberate mistake is caught by the checker, and the cost per student is visible.

## Models and prices (checked 2026-10-03)

| Use | Model | Input / output per million tokens |
|---|---|---|
| Short text feedback, verdict explanations, weekly reports | Claude Haiku 4.5 (`claude-haiku-4-5`) | $1 / $5 |
| Reading notebook photos | Claude Sonnet 5.5 (`claude-sonnet-5-5`), the current Sonnet | $2 / $10 |

The Batch API costs half of these. Cache reads cost a tenth of the input price.

**Estimated cost per use:**
- One text check costs about $0.0015 (900 tokens in, 120 out).
- One photo check costs about $0.007. That is about $0.006 to read a 1,000-pixel photo, plus a text explanation when the answer is wrong.

**Example:** 30 students, each doing 3 text checks and 1 photo a day for 22 school days, cost about **$8 a month**. A global daily cap (default $0.50 a day) stops spending at about $15 a month in the worst case. After the cap, students get the pre-written feedback.

## How it works

### The AI proxy (a Cloudflare Worker, TypeScript)

The app never talks to Claude. Firebase stays on the free Spark plan, which can't run Cloud Functions, so the proxy is a free Cloudflare Worker in `worker/` (see decision 10). The app calls it over HTTPS and sends the user's Firebase sign-in token; the Worker checks that token, reads and writes Firestore with the Firebase service account, and calls Claude.

1. **The app sends little.** A request carries only the student, the lesson and step ids, the language and the student's answer (or photo).
2. **The server owns the prompts.** It reads the step itself (task, key idea, levels) from its own copy of the lessons, which is bundled in at deploy. Prompts live in `worker/src/prompts.ts`, so a child can't change them.
3. **Checks before Claude is called.** The Worker checks that:
   - the caller is signed in (a valid Firebase ID token for this project);
   - the student belongs to the caller's account;
   - the student's daily limits aren't used up (per step, text and photos);
   - the global daily cap isn't reached.
4. **Short JSON replies.** Claude is asked for 2–4 short sentences as JSON (`{"level", "reply", "concern"}`), using structured outputs, so the reply always has that shape.
5. **The safety rule is in every prompt.** If the student writes anything suggesting they are upset, unsafe or being hurt, the reply is kind and suggests talking to a trusted teacher or parent. `concern: true` is logged for review.
6. **Secure logging.** Each call is saved in `ai_logs`, which only the server and the Firebase console can read. A log has the student id (no name), the answer, the reply, the model, the tokens and the cost. The batch job deletes logs older than 90 days.
7. **Fallbacks.** Any error, refusal, limit or timeout returns `checked_by: "fallback"`, and the app shows its own pre-written feedback. A lesson never gets stuck.
8. **Prompt caching.** The fixed instructions are marked for caching. This takes effect for the photo prompt (Sonnet 5.5 caches prompts from 512 tokens). The text prompts are too short for Haiku 4.5's 4,096-token minimum. They are already cheap, and padding them would cost more.

### The `ai_explain` step

The child explains an idea in their own words (`task_kind: "explain"`), or makes up their own question (`"own_question"`). The lesson gives:
- `task`, `key_idea` and `levels`: what "got it", "partly" and "not yet" mean;
- `keywords`: groups of words, each group being one idea in English, Urdu and Roman Urdu;
- `fallback_feedback` for each level;
- `limit_per_day`.

**Online:** Claude Haiku replies in the child's language. The reply is labelled "Checked by AI".

**Offline or on error:** the keyword fallback scores the answer on the phone. It counts how many idea groups appear in the answer, then shows the pre-written feedback, labelled "Checked by keywords". The answer is queued so Mithu can look at it later (see the batch job below).

**Mastery:** the result counts as an `explain` question, using the level the child reached in this session. This is Phase 4 decision 2.

### The `photo_check` step

The child solves a problem in their notebook and takes a photo.

1. **Small photo.** The camera picture is shrunk on the phone to about 1,000 pixels (about 100 KB).
2. **AI reads it.** Claude Sonnet writes the lines of working and the final answer as JSON. It is told only to copy what is written, never to correct it.
3. **The child confirms.** The app shows "Mithu read this" and the child can fix any misread line. A misreading then can't turn into a wrong verdict.
4. **Code decides.** The Dart checker for the step (`linear_equation`, `chem_equation`, `fraction` or `numeric`) gives the verdict. For algebra it checks every line, so a mistake in line 2 is caught on line 2.
5. **Explaining the verdict.**
   - If the answer is wrong, Claude Haiku turns the checker's verdict into 2–4 kind sentences and a guiding question. It never gives the answer.
   - If it is right, the step's own praise is shown, with no AI call.
6. **Labels.** Each reply shows what checked it: "Read by AI · Checked by the app's checker · Explained by AI".
7. **Fallback.** With no internet, a used-up limit or an unreadable photo, the child types the answer instead and the same checker checks it.

### The batch job (half price)

Two scheduled runs of the Worker (cron triggers) do the batch work. They send all their Firestore writes in one go, because a free Worker may make at most 50 requests per run.

**Every 30 minutes:**
- It sends answers that were queued offline to the Batch API.
- It collects finished batches.
- It writes Mithu's reply onto each answer.
- It deletes logs older than 90 days.

The app shows these replies under "Mithu's notes" on the home screen.

**Every Sunday at 18:00 Pakistan time:**
- It counts each active student's week: lessons finished, questions answered, skills levelled up.
- Haiku writes a 2–3 sentence note for the parents in English and Urdu.
- No names are sent to Claude. The note says "your child".
- Parents see the note under Account → the student → Weekly report.

### The cost dashboard

- Every call adds its tokens and cost to `ai_usage/{date}_{student}`.
- Settings → **AI use and cost** shows calls and estimated cost per student per day for the last 7 days.
- An admin email (yours, set once in the Cloudflare dashboard) sees every student in the project. Other accounts see only their own children.

## Tasks

| # | Task |
|---|---|
| 6.1 | Lesson format: `ai_explain` and `photo_check` in the schema, the Dart models and the validator. Add an `ai_explain` step to the fractions lesson and an explain step to the equations lesson. Add a `photo_check` step to the equations lesson. |
| 6.2 | AI server (TypeScript; first as Cloud Functions, then moved to a Cloudflare Worker): the prompt registry, the lesson lookup, auth and student checks, limits and the global cap, cost tracking, logging, and the Claude calls with fallbacks. Unit tests with a fake Claude and a fake store. |
| 6.3 | `/v1/feedback` (explain, own question, verdict explanation) and `/v1/photo` routes, with the Firebase sign-in check. |
| 6.4 | App: the AI service (HTTPS to the Worker), the keyword fallback, and the offline queue in the phone's database. |
| 6.5 | `ai_explain` step screen. |
| 6.6 | `photo_check` step screen: camera, confirming what was read, the checker, the explanation, and typing as a fallback. |
| 6.7 | Batch job and weekly reports, Mithu's notes screen, and the weekly report on the account screen. |
| 6.8 | Cost dashboard (the `/v1/costs` route and the screen). |
| 6.9 | Firestore rules (the queue, the reports, closed logs and usage) with tests; CI job for the Worker; a deploy workflow; a setup guide for Cloudflare, the API key and the service account. |

## Decisions (tell me if you want any changed)

1. **The server is written in TypeScript.** It is typed like the Dart code and uses Anthropic's official SDK.
2. **The server keeps its own copy of the lessons** for the prompts, bundled in at deploy. The app can't send prompt text. In Phase 8 lessons move to Firestore, and the server will read them from there.
3. **The photo's verdict comes from the Dart checkers on the phone.** The checkers aren't written a second time on the server. This is the spec's "Dart or server-side checker", and it keeps one checker per subject to maintain.
4. **The child confirms what the AI read** before it is checked, so an AI misreading can't mark a right answer wrong.
5. **Right photo answers get the step's own praise**, with no AI call (spec D9.1). Only wrong answers use AI to explain.
6. **Default limits per student per day:** 10 text checks, 3 photos, and each step's `limit_per_day` (default 3). The **global cap is $0.50 a day**. All are in one config file and easy to change.
7. **Answers checked later don't change mastery.** Mastery already counted the keyword result. Mithu's later note is extra feedback only.
8. **Weekly reports are written in both languages in one call**, because the server doesn't know the family's language setting.
9. **No photos are stored.** Only the text the AI read is logged.
10. **The AI server runs on a free Cloudflare Worker, not Cloud Functions** (changed 2026-10-03 at Shahid's request, to keep Firebase on the free Spark plan; the spec said Cloud Functions). Free plan limits: 100,000 requests a day, 10 ms of CPU and 50 outside requests per run. That is plenty for a pilot, and the jobs are written to stay under 50 requests. If the project ever outgrows it, the logic moves back to Cloud Functions unchanged; only `worker.ts`, `auth.ts` and the Firestore client are Worker-specific.
