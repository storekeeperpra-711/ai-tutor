# Phase 8 plan: content pipeline and first chapter

Status: plan approved 2026-10-03. Step 1 (publishing pipeline) merged (PR #11). Step 2 (teacher review) merged (PR #12). Step 3 in progress: lessons 2 and 3 of Unit 5 built.
Spec: [master-prompt.md](../master-prompt.md), Part F, Phase 8.

**Goal:** a repeatable way to write, review and ship lessons.
**Done when:** at least one full chapter is published through the pipeline, approved by a teacher, and playable in the app.

## What exists now

- Four sample lessons, bundled inside the app (`content/lessons/`). A new lesson needs a new app version.
- `tools/validate_lessons.py` checks every lesson (schema, maths answers, chemistry balancing, voice files).
- No review step: a lesson is "done" when I merge it.
- GitHub already holds the Firebase service-account secrets for dev and prod (used by the AI server deploy).

## How it will work

### Where published lessons live (decision 1)

The spec says Firebase Storage. On the free Spark plan, new projects can't create a Storage bucket, so I suggest:

- **Lesson text (JSON) in Firestore**, one document per lesson version. A lesson is small (well under Firestore's 1 MB limit), and Firestore already works offline in the app.
- **Audio and pictures in Cloudflare R2** (free up to 10 GB, no download fees), served through the AI server we already run. Nothing to set up by hand: the publish workflow does it. *(Built with the chapter's content in step 3: no lesson has recordings yet, so step 1 publishes lesson text only.)*
- **Bundled lessons stay** as the starting set, so the app works on first open without internet.

The app checks for new or updated lessons when online, saves them on the phone, and then works offline.

### The upload tool (task 8.1)

`tools/upload.py`, run by a GitHub Action called **Publish lessons** (you click Run, like the AI server deploy):

1. Validates every lesson (the same checks as now). Any error stops everything.
2. Gives each lesson a **version** (a number plus a fingerprint of its content), so a changed lesson is a new version and an old phone never mixes versions.
3. **Dev:** uploads every lesson as a *draft* to the dev project, for review.
4. **Prod:** uploads only lessons whose **exact version** a teacher approved. If a lesson changes after approval, it goes back to review.

### Teacher review (task 8.2)

Teachers review in the dev app on their own phone. No GitHub, no computer needed.

- A teacher account (role `teacher`, which exists already) sees a **Review** list: lessons waiting, approved, and needing changes.
- **Preview:** the teacher plays the lesson exactly as a child would, at any age tier.
- **Notes:** on any step, the teacher taps **Note** and types a comment. *(Typed only for now: recorded voice notes need file storage, which comes with audio in step 3.)*
- **Decision:** **Approve** or **Needs changes**. This is saved with the lesson version, the teacher and the date.
- I read the notes, fix the lesson, and it returns to the list as a new version.
- Reviewers are the emails in the GitHub secrets ADMIN_EMAILS and REVIEWER_EMAILS, and the teacher must confirm their email with a link, so a random sign-up can't approve lessons.

### The pilot chapter (task 8.3, decision 2)

I suggest **Grade 9 Maths, Unit 5: Linear Equations and Inequalities**:

- older students can test it themselves;
- it builds on the balance-scale lesson we have;
- the answers are checked by code, so it's safe.

About 6–8 lessons following the Punjab textbook's sections. Draft list (from the PCTB Grade 9 book, Exercises 5.1 and 5.2):

1. Solving linear equations: the balance scale (exists).
2. Equations with brackets and fractions.
3. Inequalities in one variable on a number line (sign flip with negatives).
4. Inequalities in two variables: shading a region.
5. Several inequalities: the feasible region and its corners.
6. Linear programming: the biggest or smallest value at a corner.
7. Linear programming word problems.

 I draft the list from the textbook's contents page and the teacher confirms it before I write the lessons. Each lesson has explanations, worked examples, practice steps, an AI "explain your thinking" step, and a summary, in English and Urdu.

Grade 10 Chemistry Chapter 15 and Grades 3–5 Maths come next, through the same pipeline, once the first chapter has gone through it.

### Board-exam practice (task 8.4)

- **Practice sets** for the chapter in the board's style: multiple choice, short questions and long questions.
- **Model answers:** step-by-step, as a board examiner expects them written.
- Maths answers are checked by code. The AI step only gives feedback on how the student wrote their working.
- Practice sets go through the same teacher review.

## What I need from you

1. **Storage:** Firestore and Cloudflare R2 instead of Firebase Storage. This changes a decision in the spec. (Recommended: yes, it keeps everything free.)
2. **Pilot chapter:** Grade 9 Maths Unit 5. (Recommended.)
3. **A teacher:** someone who will review on their phone. They need a Google sign-in; I'll give you the steps to make them a reviewer. I can build everything before you find one.

## Order of work

1. Versioning, the upload tool, the Publish lessons workflow, and the app downloading lessons.
2. Review screens, notes and approval.
3. The chapter's lessons and practice sets.
4. Publish to dev, teacher review, fixes, publish to prod.

Steps 1–3 are one pull request each. Step 4 waits on the teacher.
