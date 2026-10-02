# Phase 4 plan: mastery engine and homework

Status: built, waiting for review. Date: 2026-10-02.
Spec: [master-prompt.md](../master-prompt.md), Parts B2 (review over time), B3 (mastery learning), B4 (homework and memory), D9 (costs) and Part F, Phase 4.

**Goal:** the app knows what each student understands and what to do next.
**Done when:** a simulated student's history produces sensible mastery levels, review dates and daily plans, covered by tests.

## How it works

Every answered question is evidence about one skill: which skill it is, what kind of question it was (recall, explain, apply, find the error, exam style), whether it was right **on the first try**, and the date.

The engine (pure Dart in `lib/mastery/`, no Flutter, no network) folds each piece of evidence into a small **skill state** per child and skill. That state holds the level, the question types shown so far, the days with correct answers, the review stage and the next review date. Only this small state is stored and synced (one Firestore document per child per skill), not every answer forever. This keeps reads and writes low.

### Mastery levels (spec B3)

| Level | When |
|---|---|
| Not started | No answers yet. |
| Learning | Started, but no required question type answered right on the first try yet. |
| Practising | At least one required type answered right on the first try. |
| Mastered | **Every** question type in the lesson's `mastery_criteria` answered right on the first try, with correct answers on at least `days` different days. |
| Secure | Mastered, and a spaced review answered right at least a week after mastery. |

A failed review moves the skill back to Practising. The child then has to show it again on new days, and the reviews restart at 2 days.

### Spaced review (adapted to performance)

After mastery, reviews are due after **2 days, 1 week, 1 month**, then 2 months and 4 months.
- Right on the first try: go to the next, longer gap.
- Right after a retry: repeat the same gap.
- Wrong: back to Practising, and the next review is due in 2 days.

### When a child is stuck (spec B3: change the approach, never loop)

"Stuck" means question steps finished without getting them right on the first try, counted since the last correct answer on that skill. The engine gives advice in this order, skipping what doesn't exist:

1. Show an **alternative explanation** for that step (the lesson's `alternatives`).
2. Go back to a **weak prerequisite** skill, and its lesson if one exists.
3. Suggest a **break**.
4. Mark the skill **needs help** for a parent or teacher. The account screen shows it now; the parent report and teacher dashboard (Phase 9) will read it from Firestore.

### Daily plan and homework (spec B4)

About 10 minutes for Nursery to Grade 2 and 15 minutes for older children. The items come in this order and stop when the time is used up:

1. Reviews that are due (retrieval practice).
2. Practice questions on the current skill, choosing the question types still missing for mastery.
3. Continue the unfinished lesson, or start the next lesson whose prerequisites are ready.
4. One mixed question from another skill already practised.
5. One "explain it" or "find the mistake" question.
6. Sometimes (every third day) a real-world task to do at home, from the lesson's `home_tasks`.
7. Flashcards, **only** for skills at Practising or above.

The plan is the same all day for a child (it is built from the child's id and the date), and questions answered in the last few days are skipped where possible.

## Tasks

| # | Task |
|---|---|
| 4.1 | Lessons: optional `question_type` and `skill` on question steps, so lesson answers count as evidence; tag the three lessons; add the missing question types to their question banks; one alternative explanation for the fractions lesson. The validator checks that every question type in `mastery_criteria` has at least one question, and that prerequisites form no loops. |
| 4.2 | Skills graph: skills and prerequisites from all lessons, the lessons that teach each skill, and which lesson to do next. |
| 4.3 | Skill state and mastery levels, with the review schedule. |
| 4.4 | Stuck advice; the lesson player shows the alternative explanation, suggests a break, and marks "needs help". |
| 4.5 | Daily plan generator. |
| 4.6 | Storage: skill states on the phone (database version 2) and in Firestore (`students/{id}/skills/{skillId}`), with rules and rules tests. |
| 4.7 | Screens: "Today's plan" on the home screen, a practice player for plan questions, flashcards, the home task card, and mastery dots on each lesson. |
| 4.8 | Tests: a simulated student over six weeks (levels, review dates, daily plans), and the stuck ladder. |

## Decisions (tell me if you want any changed)

1. **Only first-try answers count towards mastery.** Answers that come right after a hint still count as practice, but not as proof.
2. **Until AI arrives (Phase 6), "explain" questions are "pick the best explanation" choices.** Explaining in the student's own words comes with the `ai_explain` step, and then counts the same way.
3. **Secure means a review answered right at least one week after mastery.** The spec says "still remembered weeks later"; the 1-month review keeps checking after that.
4. **"Needs help" is stored with the skill** (synced to Firestore) and shown on the account screen. Notifications to parents and teachers come with Phase 9.
5. **No new Firestore reads for planning.** The plan is built on the phone from the local skill states.
