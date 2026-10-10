# Geometrical Constructions unit lesson sources (Grade 6)

Scripts that write the Grade 6 Maths lessons of the Geometrical Constructions unit (`content/lessons/g6-maths-19-*.json`). The unit follows PCTB Mathematics 6 (SNC 2022), Sub-domain 10: Geometrical Constructions.

| Script | Lesson | Skill |
|---|---|---|
| `bisectors_perpendiculars.py` | `g6-maths-19-bisectors-and-perpendiculars` | `maths.constructions.perpendicular_bisector` |
| `constructing_angles.py` | `g6-maths-19-constructing-angles` | `maths.constructions.angles` |
| `construction_problems.py` | `g6-maths-19-unknown-angles-and-construction-problems` | `maths.constructions.word_problems` (with a 5-question unit test) |
| `exercise_10_1.py` | `g6-maths-19-exercise-10-1` | `maths.constructions.ex_10_1` |
| `exercise_10_2.py` | `g6-maths-19-exercise-10-2` | `maths.constructions.ex_10_2` |
| `chapter_10_test.py` | `g6-maths-19-chapter-10-test` | `maths.constructions.chapter_10_test` |

The last three are the practice sets for Exercises 10.1 and 10.2 of the book (chapter 10, Geometrical Constructions) and a chapter test (Review Exercise 10) for the whole chapter; Exercise 10.3 is in the Angles unit (`g6-maths-09`). Only the exercise numbers and the kinds of question follow the book; every question, number and story is new. The app cannot check a real drawing, so they ask about the steps, their order and the lengths and angles they give. They have no "why" steps. `figs.py` draws their figures with coordinates worked out in Python, and `common.py` holds the practice helpers (`nq`, `ch`, `practice_lesson`, `practice_intro`).

The app cannot check a real drawing, so the lessons show finished constructions in figures (compass arcs dashed) and ask about the steps, their order and the lengths and angles they give. The drawing itself is a home task with ruler and compass (or string and pencil). Figure coordinates are worked out in Python so drawn angles match the numbers, and every answer and common wrong answer is checked with `assert`.

To change a lesson, edit its script and run it, then run the validator:

    python content/sources/g6-maths-19/constructing_angles.py
    python tools/validate_lessons.py

Edit the script, not the JSON file, or the next run will undo the change. The Urdu terms are still to be checked.

Every lesson opens with two short "why" steps (`s0_why`: the need that led to the idea and what it solved, with Mithu's question; `s0_use`: where it helps in real life). Their texts are in `why.py`, and `write()` in `common.py` adds them through `content/sources/why_steps.py`. Edit `why.py`, then rerun the lesson script.
