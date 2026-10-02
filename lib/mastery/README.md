# mastery

The mastery engine (Phase 4). Pure Dart: no Flutter, no network, so it is
fast to test and works offline. Plan and decisions: [docs/plan/04-phase-4.md](../../docs/plan/04-phase-4.md).

| File | What |
|---|---|
| `curriculum.dart` | Skills graph from all lessons: prerequisites, which lesson teaches a skill, the questions for a skill. |
| `skill_state.dart` | One child's state for one skill, the mastery level, and the spaced review schedule. `record()` folds in one answer. |
| `evidence.dart` | Turns a finished step into evidence (skill, question type, right on the first try). |
| `stuck.dart` | What to do when a child is stuck: another explanation, an earlier skill, a break, then "needs help". |
| `daily_plan.dart` | Today's 10–15 minute plan: reviews, practice, the lesson, a mixed question, explain-it, a home task, flashcards. |

`lib/services/mastery_service.dart` connects the engine to the app: it saves
skill states (on the phone, then Firestore) and builds and remembers today's plan.
`test/mastery/simulated_student_test.dart` runs a pretend student for six weeks.
