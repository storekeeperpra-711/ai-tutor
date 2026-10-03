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

## Teacher review

Teachers review in the **dev app** on their own phone.

### Add a teacher (you, once per teacher)

1. Open the repository on GitHub.
2. Tap **Settings**, then **Secrets and variables**, then **Actions**.
3. Tap **New repository secret** (or edit **REVIEWER_EMAILS** if it exists).
4. Name: `REVIEWER_EMAILS`.
5. Value: the teacher's email. For more than one, put commas between them.
6. Tap **Add secret**.
7. Run **Publish lessons** with **dev** (above). That copies the list to Firebase.

Emails in ADMIN_EMAILS can review too.

### What the teacher does

1. Install the dev app (the one with the **DEV** ribbon).
2. Tap the family button at the top, and create an account with their email and a password.
3. Tap **Settings**, then **Review lessons**.
4. Tap **Email me the link**, open the email, and tap the link in it.
5. Back in the app, tap **I've opened the link**.
6. Tap a lesson, then **Play the lesson**. On any step, the note button writes what should change.
7. Tap **Approve** or **Needs changes**.

After approving, run **Publish lessons** with **prod** to send the approved lessons to children.

## If it fails

- **"Nothing published: fix the lessons above first"**: a lesson has a mistake. Nothing was changed. Send me the run's link.
- **"FIREBASE_SERVICE_ACCOUNT… is not set"**: the Firebase key is missing from the GitHub secrets ([ai-setup.md](ai-setup.md)).

## What it writes (for developers)

`tools/upload.py` writes `lesson_catalog/current` and `published_lessons/{id}` in the target Firebase project, and `lesson_reviews/{id}` and `config/reviewers` in dev. The review screens (`lib/features/review/`) add notes in `lesson_reviews/{id}/notes` and write the decision; `firestore.rules` lets only listed reviewers with a verified email do either, and an approval names the exact version (`approved_hash`). The app's `LessonUpdater` (`lib/lessons/lesson_updates.dart`) downloads changed lessons into the phone's database; a downloaded lesson replaces the bundled copy.
