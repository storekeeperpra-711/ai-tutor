# Developer setup

## Run the app on a phone

1. Install Flutter **3.47.6** (stable) and Android Studio. Run `flutter doctor` and fix anything it lists.
2. On the phone: Settings → About phone → tap "Build number" 7 times, then turn on **USB debugging** in Developer options. Connect it by USB.
3. In this folder:
   ```sh
   flutter pub get
   flutter run
   ```

No Flutter on the computer? Every push to `main` builds a debug APK in GitHub Actions: open the latest **CI** run → **Artifacts** → `ai-tutor-debug-apk`, download it to the phone and install it (allow "install unknown apps").

## Checks (the same ones CI runs)

```sh
dart format lib test
flutter analyze
flutter test
```

## Add or change a string

Every student-facing string must exist in English **and** Urdu.

1. Add the key to `lib/l10n/app_en.arb` with a `@key` description, and the Urdu text to `lib/l10n/app_ur.arb`.
2. Run `flutter gen-l10n` (or just `flutter run`). Commit the regenerated `lib/l10n/app_localizations*.dart` files too; CI checks they are up to date.
3. Use it in a widget: `AppLocalizations.of(context).yourKey`.

Right-to-left: when the app is in Urdu, Flutter mirrors every screen. Use `EdgeInsetsDirectional`, `AlignmentDirectional` and start/end instead of left/right so layouts mirror correctly.

## Where things are

| Path | What |
|---|---|
| `lib/app/` | App root, routing (`router.dart`), language (`locale_controller.dart`), themes per age tier (`theme/`) |
| `lib/features/` | Screens |
| `lib/l10n/` | Translations (ARB files) |
| `assets/fonts/` | Noto Nastaliq Urdu (SIL Open Font License) |
| `content/`, `tools/`, `functions/` | Lessons, Python scripts, Cloud Functions (later phases; see each README) |

## Developer screens

In debug builds the home screen shows an **Urdu text test** button. Use it on the test phone to check that Urdu letters are not cut off, Urdu digits show correctly, and formulas stay left-to-right.

The age-tier setting in Settings is for developers only for now; later the tier will come from the student's grade.

## Secrets

The Claude API key is **never** put in this repository or in the app. It is stored only as a Firebase secret for Cloud Functions (Phase 6). See `functions/README.md`.
