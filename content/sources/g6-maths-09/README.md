# Angles unit lesson sources (Grade 6)

Scripts that write the Grade 6 Maths lessons of the Angles unit (`content/lessons/g6-maths-09-*.json`):

| Script | Lesson | Skill |
|---|---|---|
| `angle_types.py` | `g6-maths-09-types-of-angles` | `maths.geometry.angle_types` |
| `angles_on_a_line.py` | `g6-maths-09-angles-on-a-line` | `maths.geometry.angles_on_line` |
| `angle_pairs.py` | `g6-maths-09-complementary-supplementary` | `maths.geometry.complementary_supplementary` |
| `triangle_angles.py` | `g6-maths-09-angles-in-a-triangle` | `maths.geometry.triangle_angles` |
| `angle_word_problems.py` | `g6-maths-09-angle-word-problems` | `maths.geometry.word_problems` |
| `exercise_10_3.py` | `g6-maths-09-exercise-10-3` | `maths.geometry.ex_10_3` |

`exercise_10_3.py` is the practice set for Exercise 10.3 of the book (chapter 10, Geometrical Constructions): unknown angles on a straight line and in a triangle. Only the exercise number and the kinds of question follow the book; every question, number and story is new. It has no "why" steps. `figs.py` draws its angle figures with coordinates worked out in Python, and `common.py` holds the practice helpers (`nq`, `ch`, `practice_lesson`, `practice_intro`).

Every answer, and every common wrong answer (like using 360° on a straight line), is worked out in Python and checked with `assert`, so no number is typed by hand. The "what kind of angle" questions are built by `kind_question` in `common.py`, which picks the right option from the angle's size. There are no pictures yet: each angle is given in degrees or as a clock or a door. The word-problems lesson ends with a five-question unit test, each question tagged with an earlier lesson's skill.

To change a lesson, edit its script and run it, then run the validator:

    python content/sources/g6-maths-09/angle_types.py
    python tools/validate_lessons.py

Edit the script, not the JSON file, or the next run will undo the change. The unit number (09) and the Urdu terms are still to be confirmed against the PCTB Grade 6 book.

Every lesson opens with two short "why" steps (`s0_why`: the need that led to the idea and what it solved, with Mithu's question; `s0_use`: where it helps in real life). Their texts are in `why.py`, and `write()` in `common.py` adds them through `content/sources/why_steps.py`. Edit `why.py`, then rerun the lesson script.
