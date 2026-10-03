# Phase 9 plan: parents and teachers

Status: approved 2026-10-03. Steps 1 (classes) and 2 (teacher dashboard) built; step 3 next.
Spec: [master-prompt.md](../master-prompt.md), Part F, Phase 9.

**Goal:** adults can see and support learning.
**Done when:** a teacher can assign a lesson and see who struggled with which misconception, and a parent with limited literacy can understand the report by listening.

## What exists now

- Parent and teacher accounts (email sign-in), and several children on one phone, each with a PIN or picture.
- The app already knows, per child and per skill: the mastery level, the next review date, "needs help" after repeated misses, and which misconceptions came up.
- A weekly note for parents, written by AI on the server on Sunday evenings. It is text only and needs internet.
- Lessons have home tasks (for example "find two signs that are inequalities").
- Nothing connects a teacher to students yet. Today the Firestore rules let each account see only its own data.

## How it will work

### 1. Classes (the link between teacher and students)

- In the app, a teacher creates a **class** and gets a 6-letter **class code**.
- On the family phone, a parent opens the child's profile, types the code, and agrees to share. The child joins the class.
- The teacher sees only what is needed: the child's first name and grade, mastery per skill, misconceptions, and "needs help". They see no PIN and no other family data, and nothing goes to AI with a name.
- The phone keeps a short summary per child up to date in the class. The parent can leave the class at any time, which deletes the summary.
- New Firestore rules: only the class's teacher can read the class, and only that child's family phone can write the child's summary.

### 2. Teacher dashboard (Flutter web, task 9.2)

A website the teacher opens on a computer or phone, signed in with the same account. It has five parts:

- **Class mastery:** a grid of students × skills, coloured by mastery level (not started, learning, practising, mastered, secure).
- **Recurring mistakes:** the most common misconceptions in the class, in words a teacher understands (taken from the lessons), with the students who made each one.
- **Stuck students:** anyone marked "needs help", with the skill and since when.
- **Assign:** pick a lesson (or a practice set) and a due date. It appears at the top of each child's daily plan on their phone, and the dashboard shows who has finished it.
- **Content review:** the lesson review screens from Phase 8, for teachers who review lessons.

The dashboard reads Firestore directly. It needs no server and no AI, so it costs nothing to run.

### 3. Parent report you can listen to (task 9.1)

A new **Report** button for each child, made on the phone from the child's own data. It works offline and needs no AI. It shows:

- what the child learned this week (skills that moved up);
- what needs practice, and when the app will bring it back ("on Thursday");
- one home activity, taken from the lesson the child is working on;
- effort: days practised and questions answered (no streak pressure).

**Listening:** a big ▶ button reads the whole report aloud in Urdu (or English), sentence by sentence, with each part highlighted as it is read. There are also big pictures (stars for mastery, a calendar for the review day, a house for the home activity), so a parent who doesn't read can follow.

The AI weekly note stays as an extra "Mithu's note" at the end when it exists.

## Decisions

1. **The report's voice.** Decided 2026-10-03: **the phone's own voice** (text-to-speech). It is free, works offline and needs no recordings. If a phone has no Urdu voice, the app explains how to add it, and the pictures still carry the report. Recorded or cloud voices can be added later without changing the report.
2. **Where the dashboard lives.** Decided 2026-10-03: **Firebase Hosting**, which is free on the Spark plan and sits in the same project. I'll deploy it with a GitHub Action like the AI server. You may need to give one permission once in the Google Cloud console; I'll give you click-by-click steps.
3. **Names for teachers.** Decided 2026-10-03: the teacher sees the child's **first name** (already stored on the phone), only after the parent agrees when joining the class. Names never go to AI.

## Order of work

1. Classes, class codes, joining with parent consent, the shared summaries, the Firestore rules, and assignments reaching the child's daily plan.
2. The teacher dashboard on the web, and the workflow that deploys it.
3. The parent report with pictures and the phone's voice reading it aloud.

Each step is one pull request. Testing with a real teacher and parent comes after step 3, and the teacher who reviews Unit 5 could also try the dashboard.

## Step 1 as built

- **Teacher, in the app:** Account → **My classes** → **New class**. The class gets a 6-letter code (no I, O, 0 or 1, so it can't be misread). The class screen shows the code, the students (grade, skills mastered, "needs help"), the five most common mistakes with who made them, and the assigned lessons with how many finished. Lessons are assigned with an optional due date; a class can be deleted, which also deletes the students' summaries.
- **Parent, on the family phone:** Account → the classes button next to a child → type the code → **Find class** → tick the consent box → **Join class**. Joining and finding need internet. **Leave** deletes the child's summary from the class.
- **The summary** (`classes/{id}/members/{uid}_{studentId}`): first name, grade, each started skill's level, "needs help", last practice day and next review day, how often each misconception came up, and the lessons opened. It is shared at once on joining, then at most every 15 minutes when it changed, so Firestore writes stay low.
- **Assigned lessons** are fetched on joining and then at most once an hour, and show at the top of the child's plan ("From your teacher") until finished.
- **Rules:** only a teacher account creates classes, each code is used once, a code can be looked up but codes can't be listed, only the family's own phone writes its child's summary (with only the fields above), only the class's teacher reads the summaries, and only the teacher assigns lessons. Tested on the emulator in `tools/firestore-rules`.

**For Shahid after merging:** paste the new `firestore.rules` into both Firebase projects (Firestore → Rules → Publish), as before.

## Step 2 as built

- **The website** is the same Flutter code built for the web from `lib/dashboard/main_dashboard.dart`. It reads Firestore directly with the teacher's sign-in, so it needs no server and no AI. Lessons come from the app's bundle plus newer ones published to Firestore.
- **Sign in** with the teacher account from the app, or create a teacher account there. The home page lists the teacher's classes; **New class** works as in the app.
- **A class** has four tabs:
  - **Mastery:** students down, skills across, each cell coloured by level with its first letter; a red border means "needs help".
  - **Mistakes:** the class's misconceptions in the lesson's own words, the ones most students made first, with who made them and how often.
  - **Needs help:** each stuck student, the skill, and the day they last tried it.
  - **Lessons:** assign a lesson with a due date, and see who has finished and who has not.
- **Content review** stays in the dev app for now: its screens play lessons, which needs the phone's database.
- **Deploying:** Actions → **Deploy teacher dashboard** → Run workflow → dev or prod. The first run registers a "Teacher dashboard" web app in that Firebase project. The address is shown in the run's summary: `https://<project>.web.app`.

**For Shahid:** run the workflow for dev. If it stops with "permission denied", the Firebase key needs one more role; see the steps in the thread.
