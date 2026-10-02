# Phase 3 plan: accounts, profiles and progress

Status: in progress. Date: 2026-10-02.
Spec: [master-prompt.md](../master-prompt.md), Parts D5 (connectivity), D8 (privacy), D9 (costs) and Part F, Phase 3.

**Goal:** students, parents and teachers can sign in and progress is saved.
**Done when:** two children can use one phone with separate progress, and a lesson continues and syncs correctly after the connection drops mid-lesson.

## How it works

The app is **local first**. Everything a child does is saved on the phone at once, in a small SQLite database (drift). A sync service then copies it to Firestore whenever there is a connection. A lesson never waits for the internet.

```
Child answers a step
  -> saved on the phone (profile, lesson, step, result)       always works, offline too
  -> added to the "waiting to sync" list on the phone
  -> sync service writes it to Firestore when online          one write per step
  -> removed from the list when Firestore confirms
```

- **The phone signs in by itself.** On first launch the app signs in to Firebase anonymously, so a family can start without an email address. If there is no internet yet, the app still works and signs in later.
- **Child profiles live on the phone** and belong to the phone's account. A child taps their picture to open their profile. A child can add a 4-digit PIN so a brother or sister can't open their profile. Each profile has its own progress.
- **Parent and teacher accounts** sign in with email and password. When a parent signs in on the family phone, the phone's anonymous account becomes the parent's account, so nothing is lost. Signing in on a new phone brings the children's profiles and progress back.
- **Resume:** the app remembers each child's last finished step in every lesson and reopens the lesson at the next step.
- **Connection states:** a small chip shows "Offline: your work is saved on this phone" or "3 answers waiting to sync". It never stops a lesson.

## Firestore data model (minimal personal data)

```
accounts/{uid}                              role: device | parent | teacher, created_at
accounts/{uid}/students/{studentId}         first_name, grade, avatar, pin_hash (salted, optional), created_at
accounts/{uid}/students/{studentId}/progress/{lessonId}
    lesson_version, next_step, completed, updated_at,
    steps: { stepId: { correct, attempts, misconceptions, at } }
```

Only a first name, grade, picture choice and progress. No surname, school, phone number or photo. Each step is one merged write to the lesson's progress document (spec D9: once per step, not per tap). The security rules in `firestore.rules` let an account read and write only its own data. Teacher access to students comes with classes in Phase 9.

## Tasks

| # | Task |
|---|---|
| 3.1 | Packages: firebase_auth, cloud_firestore, drift (SQLite), connectivity_plus, crypto. |
| 3.2 | Local database: profiles, lesson progress, step results, and the sync queue. Tests run against an in-memory database. |
| 3.3 | Auth service: anonymous sign-in for the phone; email sign-up and sign-in for parents and teachers, keeping the phone's data. Behind an interface so tests use a fake. |
| 3.4 | Profiles: "Who is learning?" screen with big pictures; add a child (first name, grade, picture, optional PIN); PIN pad; switch child. |
| 3.5 | Progress: the lesson player saves each finished step and resumes at the next one; the home screen shows each lesson's progress for the current child. |
| 3.6 | Sync service: sends the queue to Firestore when online, retries safely (each write is idempotent), and pulls profiles and progress after a parent signs in on a new phone. |
| 3.7 | Connection chip: offline and "waiting to sync" states, in English and Urdu. |
| 3.8 | `firestore.rules` and `firebase.json`, with rules tests that run in CI on the Firestore emulator. |
| 3.9 | Tests: two children on one phone keep separate progress; a lesson continues offline, then the queue syncs once the connection is back. |

## Decisions (tell me if you want any changed)

1. **Local first with drift (SQLite) plus Firestore.** The spec lists both. Drift is the answer queue and the source for resume, so the app behaves the same with or without internet. Firestore keeps its own offline cache too.
2. **The phone signs in anonymously; adults use email and password.** Phone-number (SMS) sign-in costs money per message, and Google sign-in needs extra key setup, so both can come later if families need them.
3. **The child PIN is optional and 4 digits.** It keeps siblings out of each other's profiles. It is stored only as a salted hash. Young children (Nursery to Grade 2) can use just their picture.
4. **Teachers get an account and role now.** Classes, assigning lessons and the dashboard are Phase 9.
5. **Parental consent** is a simple "I am the parent or guardian and I agree" tick when adding the first child. The full consent flow is part of the Phase 10 privacy review.

## Firebase console steps (Shahid, for both projects)

Do these in **AI Tutor** and in **AI Tutor dev**:

1. **Authentication:** Build > Authentication > Get started > Sign-in method. Turn on **Anonymous** and **Email/Password** (only the first switch, not "Email link").
2. **Firestore:** Build > Firestore Database > Create database. Choose **Standard edition**, database ID `(default)`, location **asia-south1 (Mumbai)**, and **Start in production mode**.
3. **Rules:** in Firestore Database > Rules, replace everything with the contents of `firestore.rules` from the repo, then click **Publish**.

The location can't be changed later, so please check it says asia-south1 before you click Create.
