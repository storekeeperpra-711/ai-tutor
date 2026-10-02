# Phase 5 plan: rich content

Status: built, waiting for review. Date: 2026-10-02.
Spec: [master-prompt.md](../master-prompt.md), Part C (rich content), D9 (costs) and Part F, Phase 5.

**Goal:** simulations, videos and animations inside lessons.
**Done when:** a lesson with a WebView simulation, a native interactive and a video runs smoothly on the cheap phone, and simulation results feed the checkers and mastery engine.

## How it works

Three new step types join the lesson format:

| Step | What the child sees | How it is built |
|---|---|---|
| `sim` | A simulation to play with, then a question about what they found | `renderer: "webview"` loads one self-contained HTML file from `assets/sims/`; `renderer: "native"` uses a Flutter interactive by `sim_id` |
| `video` | A short explainer video with captions | `video_player`, English and Urdu files, WebVTT captions |
| `lottie` | A small animation (a celebration, a picture that moves) | `lottie` |

### Simulations feed the checkers and the mastery engine

A simulation reports a result, for example `{"children": 8}` or `{"equation": "2H2 + O2 -> 2H2O"}`. The `sim` step names which value to check and which checker to use (`numeric`, `fraction`, `chem_equation`, `text`), the same checkers as Phase 2. So the app, not the simulation and not AI, decides if the answer is right. The result becomes a normal step result (right on the first try or not, attempts, misconception), so it counts towards mastery like any question step when the step has a `question_type`.

A `sim` step without `expected` is for exploring: the child can continue after trying it once.

### WebView rules (spec C)

- Each simulation is one HTML file with its CSS and JavaScript inside. It makes no network requests and works offline.
- Flutter calls `initSim(config)` after the page loads, with `{lang, ...params}`.
- The simulation reports through the `TutorBridge` channel: `{event: "ready" | "result" | "error", data: {...}}`.
- Only one WebView exists at a time. It is disposed when the step ends, and every navigation away from the simulation file is blocked.

### Native interactives

These are reusable Flutter widgets driven by the lesson's `params`. Each one has big buttons as well as dragging, so it works on small screens and for children who find dragging hard.

| `sim_id` | Example params | Reports |
|---|---|---|
| `fraction_bars` | `wholes: 2, part: 4` | `pieces` |
| `balance_scale` | `equation: "2x + 3 = 11"` | `x`, `steps` (each "do the same to both sides" move) |
| `atom_balancer` | `equation: "H2 + O2 -> H2O"` | `equation` with the child's coefficients |
| `number_line` | `min: 0, max: 2, step: 0.25` | `value` |
| `graph_plotter` | `m: 2, c: 1` (or free) | `m`, `c` of the line the child placed |

### Videos

- `src` and `captions` are given per language (`en`, `ur`). A path is either a bundled asset or an `https` link.
- For links, the video is downloaded once and kept on the phone, so watching it again (or offline later) uses no data. The lesson's videos start downloading as soon as the lesson opens, so they are usually ready when the child reaches them.
- If a video can't load (offline, no cached copy), the step shows its text summary and the child carries on. A lesson never gets stuck on a video.
- Videos are made by `tools/video/` (Python, Pillow and ffmpeg): 720p, under 2 minutes, captions, and separate English and Urdu versions. Simple drawn animations compress very well: the first video is 48 seconds and about 100 KB per language. Physics colours: orange = force, teal = velocity, purple = acceleration.

### Animation and "less movement"

- `lottie` steps, and a short celebration when a lesson is finished or a skill reaches a new level.
- `flutter_animate` for small UI motion (feedback appearing, plan items).
- **Less movement:** if the phone's "remove animations" setting is on, or the new **Less movement** switch in Settings is on, celebrations and UI motion are skipped and Lottie shows a still picture.

## Tasks

| # | Task |
|---|---|
| 5.1 | Lesson format: `sim`, `video` and `lottie` steps in the schema and Dart models. The validator checks that files exist, `sim_id` is known, the checker fits, and simulations make no external requests. |
| 5.2 | `sim` step: one screen for both renderers, checking the result with the Phase 2 checkers, with hints, attempts and feedback like other questions. |
| 5.3 | WebView host: `initSim`, `TutorBridge`, navigation blocked, one WebView at a time. HTML simulations: roti strips (fractions) and falling objects (gravity). |
| 5.4 | Native interactives: fraction bars, balance scale, atom balancer, number line, graph plotter. |
| 5.5 | `video` step: asset or link, streaming plus caching, captions in English and Urdu, a fallback when it can't play. |
| 5.6 | `lottie` step, celebrations, `flutter_animate`, and the Less movement setting. |
| 5.7 | Video generator in `tools/video/` and the first video: dividing by a fraction with rotis (English and Urdu). |
| 5.8 | Lessons: the fractions lesson gets the roti strips simulation, fraction bars and the video; the equations lesson gets the balance scale; the chemistry lesson gets the atom balancer. |
| 5.9 | A developer screen listing every simulation and interactive, for testing on the phone. Tests for every new step, interactive and the video fallback. |

## Decisions (tell me if you want any changed)

1. **The old demos aren't in the repo, so the simulations are written fresh.** If you upload the demos later (for example to `reference/demos/`), I'll reuse their ideas.
2. **The balance scale and atom balancer are native only.** The spec lists them both as WebView ports and as native templates. Native is lighter on cheap phones, so I build them once, natively. The WebView simulations are the roti strips and falling objects.
3. **The first video is bundled in the app for now** (about 200 KB for both languages). Links to Firebase Storage already work in the player; uploading content to Storage comes with the content pipeline in Phase 8. New Firebase projects need the paid Blaze plan for Storage, so this keeps you on the free plan until then.
4. **No voice in the videos yet.** They have on-screen text and captions in each language. Narration comes with Mithu's audio in Phase 7.
5. **Videos download first instead of streaming.** Streaming and saving at the same time would download each video twice on mobile data. Our videos are small (about 100 KB), so downloading takes seconds, and it starts when the lesson opens.
6. **The falling-objects simulation has no lesson yet** (there is no physics lesson). It is playable from the developer screen and ready for a physics lesson.
