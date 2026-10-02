# Phase 1 plan: lesson format and previewer

Status: in progress. Date: 2026-10-02.
Spec: [master-prompt.md](../master-prompt.md), Part E2 (lesson format) and Part F, Phase 1.

**Goal:** lessons are data; a previewer plays them.
**Done when:** you can drop a new JSON lesson into the lessons folder, it validates, and it plays end-to-end in both languages.

## Phase 0 items still open

Phase 1 doesn't depend on them, so they can run in parallel:
- Merge PR #1 (CI is green).
- 0.9: Firebase dev/prod projects and budget alert (yours), then wiring (mine).
- 0.S4: run the app on the cheap phone and check the Urdu test screen.

## Tasks

| # | Task | Output |
|---|---|---|
| 1.1 | Lesson JSON Schema v0.2, written from Part E2. | `content/schema/lesson.schema.json` |
| 1.2 | Dart models for lessons and steps (json_serializable). | `lib/models/` |
| 1.3 | Python validator: checks every lesson against the schema, plus rules a schema can't express (see below). Runs in CI. | `tools/validate_lessons.py` |
| 1.4 | Lesson player with the step registry; `explain`, `choice`, `number`, `summary` steps. Other step types show a "not supported yet" card so a lesson never breaks. | `lib/lessons/` |
| 1.5 | Load lessons from the app's assets; developer previewer screen listing every lesson with its review status and a quick EN/اردو switch. | `lib/features/previewer/` |
| 1.6 | First lesson: dividing fractions (roti example), written fresh because the original demo isn't in the repo. | `content/lessons/g6-maths-02-dividing-fractions.json` |

### Validator rules beyond the schema

- File name matches `g{grade}-{subject}-{chapter}-{slug}.json` and equals the `id`.
- Step IDs are unique within a lesson.
- Every `misconception_id` points to an entry in `misconceptions`.
- Every skill in `mastery_criteria` and `question_bank` is listed in `skills`.
- Each `choice` step has at least one correct option.
- No student-facing text is empty in either language.

## Decisions I made (tell me if you want any changed)

1. **Lessons live in `content/lessons/`**, and that folder is bundled into the app as assets. Git stays the master copy and there is only one copy of each file. `assets/lessons/` is removed. In Phase 8, the upload script will read from the same folder.
2. **The spec gives field names but not every sub-structure.** I filled in the shapes the spec leaves open (for example a choice option is `{id, text, correct, feedback, misconception_id?}`). Everything is written in the schema file. No new top-level fields were added.
3. **Grade for nursery/prep** is `0` (grades 1–12 as normal).
4. **Mithu's emotions:** the spec lists idle, talking, happy, thinking, encouraging, surprised and celebrating, but its own example uses `curious`. I allowed `curious` as well. Please confirm.
5. **Some fields are stored but not used yet.** `mastery_criteria`, `question_bank`, `alternatives` and `review_questions` are validated by the schema, but the Dart side keeps them as raw data until Phase 4 needs them.
6. **The `number` step uses a minimal numeric checker for now.** It accepts English and Urdu digits, decimals and simple fractions such as `3/4`. Phase 2 replaces it with the full checkers.
7. **Previewer access:** the previewer shows all lessons, including drafts, and is only reachable in debug builds. The real app will show only `approved` lessons.
8. **Chapter number is not confirmed.** The first lesson is tagged Grade 6, chapter 02. That needs checking against the PCTB book, and the lesson's teacher notes say so.

## Not in Phase 1

Real checkers (Phase 2), saving progress (Phase 3), mastery and spaced review (Phase 4), simulations and video (Phase 5), AI steps (Phase 6), Mithu animation and audio (Phase 7).
