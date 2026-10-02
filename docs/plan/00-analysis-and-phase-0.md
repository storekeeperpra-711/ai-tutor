# Analysis and Phase 0 plan

Status: **draft, waiting for Shahid's confirmation.** No code is written until this plan is confirmed.
Source: [../master-prompt.md](../master-prompt.md). Date: 2026-10-02.

---

## 1. What the spec asks for, in short

A Flutter Android app that acts as a patient one-on-one tutor for low-income children in Punjab (nursery to Grade 12, with a focus on girls).

- **Teaching model:** mastery learning (Not started → Learning → Practising → Mastered → Secure), a fixed 11-step lesson pattern, spaced review (2 days, 1 week, 1 month), daily 10–15 minute homework, board-exam preparation.
- **Lessons are data:** one JSON file per lesson (schema v0.2), played by one lesson player with a registry of step widgets. New lessons should never need new code.
- **Correctness by code:** maths and chemistry answers are checked by pure Dart checkers on the device. AI only explains verdicts, reads notebook photos and handles open-ended answers.
- **AI only through Cloud Functions:** the app sends a prompt ID plus the student's input; the server holds prompts, enforces daily limits, uses prompt caching and batch processing, and always has a pre-written fallback.
- **Internet-first with a safety net:** the current lesson keeps working offline; answers queue and sync later; never a "no connection" wall.
- **English and Urdu everywhere** (Nastaliq font, RTL), Punjabi audio later.
- **Four age tiers** with different UI, and a parrot character (Mithu) in Rive.
- **Very low budget, one part-time developer.** Simple code, cheapest model that works, few Firestore writes.
- **12 phases**, from foundations to a 20–50 student pilot. One phase at a time.

## 2. What is good about the plan

- The phase order is sensible: the lesson format and the offline checkers (Phases 1–2) come before accounts, AI and polish. The parts that make the product useful are proven first and cheaply.
- "Lessons are data" and "correctness by code" keep both AI cost and maintenance low.
- The fixed decisions (A3) remove most early architecture debates.

## 3. Risks and things to watch

| # | Risk | Why it matters | Suggested handling |
|---|---|---|---|
| R1 | **Scope is very large for one part-time developer.** 12 phases, 4 age tiers, character animation, teacher web dashboard. | Risk of never reaching a pilot. | Pick **one pilot slice early** (for example Grade 9 Maths Unit 5, older tier only) and build every phase for that slice first. Younger tiers and Mithu can wait until after the first pilot content works. |
| R2 | **Nastaliq rendering in Flutter.** Noto Nastaliq Urdu has tall ascenders/descenders; Flutter can clip it or space it badly, especially mixed with LTR maths. | Urdu is a core requirement; problems found late are costly. | Phase 0 includes a small "Urdu test screen" with mixed Urdu + numbers + a short formula, checked on the cheap phone. |
| R3 | **Cheap phones (2–3 GB RAM, old Android).** Firebase SDKs raise the minimum Android version over time; WebViews and video are heavy. | The target device might not be supported or may be slow. | Confirm the actual test phone and its Android version in Phase 0 and set `minSdkVersion` to match. Measure app size and start-up time from the first build. |
| R4 | **Firebase and Google Cloud setup needs Shahid's own Google account.** I can't create Firebase projects, budget alerts or signing keys from here. | Phase 0 can't be fully finished by me alone. | Phase 0 is split below into tasks I do in the repo and tasks Shahid does in the Firebase/Google Cloud console, with step-by-step notes. |
| R5 | **Children's data and privacy.** Minors, parental consent, logging AI conversations. | Legal and trust risk; hard to retrofit. | Phase 0 only stores nothing personal. Choose the Firebase region now (nearest is usually `asia-south1`, Mumbai; to confirm) because it can't be changed later. Revisit consent in Phase 3. |
| R6 | **Model names and prices change.** The spec names Haiku 4.5 and "current" Sonnet. | Wrong model IDs or cost estimates. | Not needed until Phase 6; check Anthropic's docs then, as the spec says. |
| R7 | **Earlier demos are not in the repo.** The spec refers to HTML demos (fractions, chemistry, gravity, etc.) and a Python video script. | Phases 1, 2 and 5 plan to reuse them. | Upload them before Phase 1 (they can go under `reference/demos/`). |
| R8 | **CI cost.** GitHub Actions on a private repo has limited free minutes per month. | Small, but a budget item. | Keep CI to `flutter analyze` + `flutter test` on Linux (no Android build on every push). |
| R9 | **No Flutter SDK in my cloud environment.** | I can't run or build the app here; only CI and Shahid's machine can. | CI becomes the main check for my changes. Shahid runs the app on the phone. (Can be improved later with a setup script that installs Flutter.) |

## 4. Open questions for Shahid

Answers with **(default)** are what I'll use if you don't say otherwise.

1. **Default branch.** The repo was empty, so these docs are on the branch `claude/project-thread-9ih8s6`. Should I create `main` from it as the default branch? **(default: yes)**
2. **Android package name** (permanent once published), for example `pk.aitutor.app`. **(default: `pk.aitutor.app`, change if you own a domain)**
3. **App display name** for now. **(default: "AI Tutor")**
4. **Test phone:** which phone and Android version do you have for testing?
5. **Cloud Functions language:** JavaScript/TypeScript or Python. Not needed in Phase 0 (only an empty `functions/` folder), but good to decide early. **(default: TypeScript, because Firebase's tooling and examples are strongest there)**
6. **Firebase region.** **(default: `asia-south1` Mumbai)**
7. **Pilot slice** (see R1): which grade and subject comes first? **(default: Grade 9 Maths Unit 5, Linear Equations, older tier)**
8. **Repo visibility and licence:** keep the repo private for now? **(default: private, no licence file yet)**

## 5. Phase 0 task list

**Goal (from the spec):** a clean, runnable project skeleton.
**Done when:** the app builds and runs on the cheap phone, switches between English and Urdu with correct RTL, and CI passes.

Each task is a small pull request you can review on its own.

### Done by me in the repo

| # | Task | Output |
|---|---|---|
| 0.1 | Create the Flutter project (Android only) with the folder structure from D1: `lib/app`, `models`, `lessons`, `checkers`, `mastery`, `services`, `features`, `character`; plus `assets/`, `content/`, `tools/`, `functions/`. Empty folders get a short README saying what goes there. | Runnable "hello" app |
| 0.2 | Add dependencies: `flutter_riverpod`, `go_router`, `json_annotation` + `json_serializable` + `build_runner`, `flutter_localizations`, `intl`. Strict lints (`flutter_lints` plus a few extra rules) and a format check. | `pubspec.yaml`, `analysis_options.yaml` |
| 0.3 | App shell: `ProviderScope`, `go_router` with two placeholder routes (home, settings). | `lib/main.dart`, `lib/app/router.dart` |
| 0.4 | Localization: `l10n.yaml`, `app_en.arb` and `app_ur.arb` with the first strings; a language switch in settings that flips the whole app to Urdu and RTL; the choice is remembered. | Working EN/UR switch |
| 0.5 | Fonts and theme: bundle Noto Nastaliq Urdu (OFL licence, check its size); Urdu text styles with a larger line height; one theme per age tier (`early`, `primary`, `middle`, `older`) with colours and sizes, selectable in a debug menu. | `lib/app/theme/` |
| 0.6 | Urdu test screen (debug only): Urdu paragraphs, Urdu digits, mixed Urdu + English terms, a short LTR formula inside Urdu text. Used to check R2 on the phone. | Debug screen |
| 0.7 | Tests: a widget test that the app starts, that switching language flips text direction, and a theme test per tier. | `test/` |
| 0.8 | CI with GitHub Actions: `flutter pub get`, `dart format --set-exit-if-changed`, `flutter analyze`, `flutter test` on every push and PR. Flutter version pinned. | `.github/workflows/ci.yml` |
| 0.9 | Firebase wiring in code: `firebase_core` added, `Firebase.initializeApp` with separate **dev** and **prod** configs (Android product flavors), no other Firebase features yet. Done after Shahid finishes 0.S2. | Flavors `dev` / `prod` |
| 0.10 | Short docs: how to run the app, how to switch flavors, how to add a string in both languages. | `docs/dev-setup.md` |

### Done by Shahid (I'll write step-by-step instructions)

| # | Task |
|---|---|
| 0.S1 | Install Flutter (stable), Android Studio, and enable USB debugging on the test phone. |
| 0.S2 | Create two Firebase projects (`ai-tutor-dev`, `ai-tutor-prod`), choose the region, register the Android app in each, and run `flutterfire configure` (needs your Google login). |
| 0.S3 | In Google Cloud billing, set a **budget alert** (for example US$5/month) on both projects. Set a spending limit in the Anthropic console later, in Phase 6. |
| 0.S4 | Run the app on the cheap phone and check: it starts, EN/UR switch works, Urdu text looks right, no clipping. Note the phone model, Android version, start-up time and APK size. |

### Not in Phase 0 (on purpose)

No lessons, no checkers, no login, no Firestore data, no AI, no Mithu. Those belong to Phases 1–7.

### Phase 0 acceptance checklist

- [ ] App builds and runs on the cheap phone (0.S4)
- [ ] English ⇄ Urdu switch with correct RTL (0.4, 0.6, 0.S4)
- [ ] Noto Nastaliq Urdu renders without clipping (0.5, 0.6, 0.S4)
- [ ] Four tier themes exist (0.5)
- [ ] Firebase dev and prod connected, budget alert set (0.9, 0.S2, 0.S3)
- [ ] CI passes on `main` (0.8)

## 6. Proposed order of work

0.1 → 0.2 → 0.3 → 0.8 (CI early, so every later PR is checked) → 0.4 → 0.5 → 0.6 → 0.7 → 0.10, then 0.9 once the Firebase projects exist.
