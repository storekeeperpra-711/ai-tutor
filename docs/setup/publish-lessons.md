# Publishing lessons

Lessons are written in `content/lessons/`. Publishing sends them to phones without a new app version (Phase 8).

- **dev** sends every lesson to the dev app, as a draft for a teacher to review.
- **prod** sends only the lessons a teacher approved to the real app.

A lesson changed after approval goes back to review. The real app keeps the approved version until the new one is approved.

## Publish

1. Open the repository on GitHub.
2. Tap **Actions**.
3. Tap **Publish lessons** on the left.
4. Tap **Run workflow**.
5. Pick **dev** or **prod**.
6. Leave "Only show what would change" unticked (tick it to just look).
7. Tap the green **Run workflow** button.
8. Wait for the green tick, then tap the run to see which lessons changed.

It also updates the AI server, so it knows the same lessons.

Phones pick up new lessons the next time they are online (checked at most once an hour).

## If it fails

- **"Nothing published: fix the lessons above first"**: a lesson has a mistake. Nothing was changed. Send me the run's link.
- **"FIREBASE_SERVICE_ACCOUNT… is not set"**: the Firebase key is missing from the GitHub secrets ([ai-setup.md](ai-setup.md)).

## What it writes (for developers)

`tools/upload.py` writes `lesson_catalog/current` and `published_lessons/{id}` in the target Firebase project, and `lesson_reviews/{id}` in dev. The app's `LessonUpdater` (`lib/lessons/lesson_updates.dart`) downloads changed lessons into the phone's database; a downloaded lesson replaces the bundled copy.
