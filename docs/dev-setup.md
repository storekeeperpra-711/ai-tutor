# Developer setup

## Run the app on a phone

1. Install Flutter **3.47.6** (stable) and Android Studio. Run `flutter doctor` and fix anything it lists.
2. On the phone: Settings → About phone → tap "Build number" 7 times, then turn on **USB debugging** in Developer options. Connect it by USB.
3. In this folder:
   ```sh
   flutter pub get
   flutter run --flavor dev
   ```

### Two versions: dev and prod

| Flavor | Firebase project | Package | Use |
|---|---|---|---|
| `dev` | ai-tutor-dev | `pk.aitutor.app.dev` | Everyday testing; shows a red "DEV" ribbon |
| `prod` | ai-tutor | `pk.aitutor.app` | The real app for students |

Always pass `--flavor dev` or `--flavor prod` to `flutter run` and `flutter build`. Both can be installed on the same phone. Each flavor's Firebase config file is `android/app/src/<flavor>/google-services.json` (downloaded from the Firebase console; it identifies the project and is not a secret).

No Flutter on the computer? Every push to `main` builds both debug APKs in GitHub Actions: open the latest **CI** run → **Artifacts** → `ai-tutor-debug-apks`, unzip, copy `app-dev-debug.apk` to the phone and install it (allow "install unknown apps").

## Checks (the same ones CI runs)

```sh
dart format lib test
flutter analyze
flutter test
python tools/validate_lessons.py
python -m unittest discover -s tools -p 'test_*.py'
# Firestore security rules (needs Node and Java; uses the emulator, not a real project)
cd tools/firestore-rules && npm ci && npm test
```

## Add or change a string

Every student-facing string must exist in English **and** Urdu.

1. Add the key to `lib/l10n/app_en.arb` with a `@key` description, and the Urdu text to `lib/l10n/app_ur.arb`.
2. Run `flutter gen-l10n` (or just `flutter run`). Commit the regenerated `lib/l10n/app_localizations*.dart` files too; CI checks they are up to date.
3. Use it in a widget: `AppLocalizations.of(context).yourKey`.

Right-to-left: when the app is in Urdu, Flutter mirrors every screen. Use `EdgeInsetsDirectional`, `AlignmentDirectional` and start/end instead of left/right so layouts mirror correctly.

## Add a lesson

1. Put the JSON file in `content/lessons/`, named like `g6-maths-02-dividing-fractions.json` (the `id` inside must match the file name). The format is `content/schema/lesson.schema.json`.
2. Check it:
   ```sh
   pip install -r tools/requirements.txt   # once
   python tools/validate_lessons.py
   ```
3. Run the app in debug mode → **Lessons (developer preview)** → tap the lesson. The English/اردو button in the top bar switches language while you play.

`flutter test` also plays every lesson end to end in both languages (`test/lessons/playthrough_shard.dart`, split over four test files), answering wrong first and then right, so a lesson that can't be completed fails CI.

## Checkers (Phase 2)

Answers are checked on the phone by pure Dart code in `lib/checkers/`, never by AI, so checking works offline.

| Checker | Used by | Accepts | Mistakes it names |
|---|---|---|---|
| `numeric` | `number` step | `8`, `۸`, `2.5`, `aath`, `آٹھ` | (lesson's `common_wrong`) |
| `fraction` | `number` or `text_check` | `3/4`, `1 1/2`, `0.75`, Urdu digits | not in lowest terms (if `require_simplest`) |
| `chem_equation` | `text_check` | `2H2 + O2 -> 2H2O`, `→`, `H₂O`, `Ca(OH)2`, `(aq)` | unknown element, wrong substances, changed subscript, unbalanced element (with counts), coefficients not lowest |
| `linear_equation` | `text_check` | working line by line, ending `x = 4` | unreadable line, first broken line, not finished |
| `text` | `text_check` | exact text, ignoring case and spaces, plus `accept` list | (lesson's `common_wrong`) |

`lib/lessons/answer_checking.dart` turns a checker's result into the feedback text in English or Urdu (strings in the ARB files).

## Change the Dart models

The files `lib/models/*.g.dart` and `lib/services/local_db.g.dart` are generated. After editing a model or a database table, run `dart run build_runner build` and commit the `.g.dart` files too; CI checks they are up to date.

## Accounts, profiles and progress (Phase 3)

The app is local first. Each finished step is saved in the on-phone SQLite database (`lib/services/local_db.dart`, drift) and then copied to Firestore by the sync service (`sync_service.dart`) when there is a connection. Lessons never wait for the internet.

- The phone signs in to Firebase anonymously by itself. Parents and teachers create an email account on the account screen (the family icon on the home screen); the phone's data moves into it.
- Firestore layout and the reasons behind it: [docs/plan/03-phase-3.md](plan/03-phase-3.md). Security rules: `firestore.rules`. After changing the rules, run their tests, then paste the file into Firebase console > Firestore Database > Rules in both projects and click Publish.
- Firebase, sign-in and the connection are behind small interfaces (`AuthService`, `RemoteStore`, `onlineProvider`), so widget tests use the in-memory fakes in `test/fakes.dart`. `FakeBackend.setOnline(false)` simulates losing the connection.
- In widget tests, read the database with one-off queries (`db.pendingCount()`), not `stream.first`: a drift stream read inside the test's fake clock can hang the next `pump`.

## Mastery, reviews and the daily plan (Phase 4)

Each lesson question step can say which `skill` it tests (default: the lesson's first skill) and its `question_type` (recall, explain, apply, find_error, exam_style). Only tagged steps count as mastery evidence. The validator checks that every type in `mastery_criteria` has at least one question somewhere in the lesson (steps, alternatives, question bank or review questions); otherwise a child could never reach Mastered.

- The engine is pure Dart in `lib/mastery/` (see its README). Levels, review gaps and the stuck ladder: [docs/plan/04-phase-4.md](plan/04-phase-4.md).
- Skill states are stored in the `skill_states` table (database version 2) and synced to `accounts/{uid}/students/{id}/skills/{skillId}`. After changing `firestore.rules`, republish them in both Firebase projects.
- Today's plan is built once per child per day and saved in shared preferences (`plan.{studentId}`), so it doesn't change while the child works through it.
- To change the database, bump `schemaVersion` in `local_db.dart`, add a step to `onUpgrade`, and add a test like `a version 1 database gets the skill states table`.

## Simulations, videos and animations (Phase 5)

Three step types: `sim` (an HTML simulation in a WebView, or a native interactive), `video` and `lottie`. Plan and decisions: [docs/plan/05-phase-5.md](plan/05-phase-5.md).

- A `sim` step's `expected` names the value to check in the simulation's result and the checker (`numeric`, `fraction`, `chem_equation`, `linear_inequality`, `linear_inequality_2d`, `points`, `text`). With a `question_type` it counts towards mastery like any question.
- HTML simulations live in `assets/sims/` and follow the protocol in `lib/sims/README.md`. Native interactives (`fraction_bars`, `balance_scale`, `atom_balancer`, `number_line`, `graph_plotter`, `inequality_line`, `inequality_plane`, `feasible_region`) are in `lib/sims/native/`.
- In debug builds, **Simulations (developer)** on the home screen opens every simulation and interactive, to try them on the phone.
- Videos and captions go in `assets/videos/` (or an https link). Make them with `tools/video/make_video.py` (see `tools/README.md`).
- Lottie files go in `assets/lottie/` (`tools/lottie/make_lottie.py` makes the current ones).
- **Less movement** in Settings (or the phone's "remove animations" setting) turns off celebrations and UI motion. Code checks `reduceMotion(context)` from `lib/app/motion.dart`.
- Widget tests have no WebView and can't play video, so `test/helpers.dart` swaps both for fakes; tests report simulation results straight to the step (`SimStepViewState.onSimEvent`).

## Where things are

| Path | What |
|---|---|
| `lib/app/` | App root, routing (`router.dart`), language (`locale_controller.dart`), themes per age tier (`theme/`) |
| `lib/models/` | Lesson and step data classes (json_serializable) |
| `lib/lessons/` | Lesson player, step registry (`step_registry.dart`), one widget per step type (`steps/`) |
| `lib/checkers/` | Answer checkers (pure Dart) |
| `lib/sims/` | Simulation host, WebView simulations and native interactives |
| `lib/media/` | Video and caption files: bundled or downloaded once and cached |
| `lib/mastery/` | Mastery engine: skills graph, levels, reviews, stuck advice, daily plan (pure Dart) |
| `lib/features/` | Screens: home and profiles, add learner, PIN pad, account, today's plan, practice, flashcards, the developer lesson previewer |
| `lib/services/` | On-phone database, sign-in, Firestore, sync, connection state |
| `firestore.rules`, `tools/firestore-rules/` | Firestore security rules and their tests |
| `content/lessons/`, `content/schema/` | Lesson files (bundled into the app) and their JSON Schema |
| `tools/validate_lessons.py` | Lesson validator |
| `tools/video/`, `tools/lottie/` | Video and Lottie generators |
| `assets/sims/`, `assets/videos/`, `assets/lottie/` | HTML simulations, videos with captions, animations |
| `lib/l10n/` | Translations (ARB files) |
| `assets/fonts/` | Noto Nastaliq Urdu (SIL Open Font License) |
| `worker/` | AI server, a Cloudflare Worker (Phase 6) |
| `lib/classes/` | Classes, class codes and children's summaries (Phase 9) |
| `lib/dashboard/`, `web/` | Teacher dashboard website (Phase 9), deployed by the "Deploy teacher dashboard" workflow |

## Teacher dashboard

The website is built from the same code: `flutter build web -t lib/dashboard/main_dashboard.dart`. It needs the Firebase web app's settings as `--dart-define=FIREBASE_API_KEY=...` and so on (see `main_dashboard.dart`); the deploy workflow fetches them itself. To try it locally, run `flutter run -d chrome -t lib/dashboard/main_dashboard.dart` with the same defines.

## Developer screens

In debug builds the home screen shows an **Urdu text test** button. Use it on the test phone to check that Urdu letters are not cut off, Urdu digits show correctly, and formulas stay left-to-right.

The age-tier setting in Settings is for developers only for now; later the tier will come from the student's grade.

## Secrets

The Claude API key is **never** put in this repository or in the app. It is stored only as a secret of the AI server in the Cloudflare dashboard (Phase 6). See `worker/README.md` and `docs/setup/ai-setup.md`.
