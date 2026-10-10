# Perimeter and Area unit lesson sources (Grade 6)

Scripts that write the Grade 6 Maths lessons of the Perimeter and Area unit (`content/lessons/g6-maths-08-*.json`):

| Script | Lesson | Skill |
|---|---|---|
| `perimeter.py` | `g6-maths-08-perimeter` | `maths.measurement.perimeter` |
| `area_rectangles.py` | `g6-maths-08-area-of-rectangles` | `maths.measurement.area_rectangle` |
| `compound_shapes.py` | `g6-maths-08-compound-shapes` | `maths.measurement.compound_area` |
| `triangles.py` | `g6-maths-08-area-of-triangles` | `maths.measurement.area_triangle` |
| `area_word_problems.py` | `g6-maths-08-area-word-problems` | `maths.measurement.word_problems` |
| `parallelogram_trapezium.py` | `g6-maths-08-parallelogram-and-trapezium` | `maths.measurement.area_parallelogram` |
| `area_of_path.py` | `g6-maths-08-area-of-a-path` | `maths.measurement.area_path` |
| `exercise_8_1.py` | `g6-maths-08-exercise-8-1` | `maths.measurement.ex_8_1` |
| `exercise_8_2.py` | `g6-maths-08-exercise-8-2` | `maths.measurement.ex_8_2` |

The last two are practice sets for Exercises 8.1 and 8.2 of the book (chapter 8, Surface Area and Volume). Only the exercise number and the kinds of question follow the book; every question is new, because the book may not be copied. Each has its own skill, with the chapter's skills of both this unit and the Solids unit as prerequisites, and no `why.py` entry. Exercise 8.3 and the chapter test are in the Solids unit (`g6-maths-14`). The helpers they use (`nq`, `ch`, `practice_lesson`...) are repeated at the end of `common.py` in both units.

Every answer, and every common wrong answer (like giving the perimeter when the area is asked), is worked out in Python and checked with `assert`, so no number is typed by hand. There are no pictures yet: each shape is described in words. The word-problems lesson ends with a five-question unit test, each question tagged with an earlier lesson's skill.

To change a lesson, edit its script and run it, then run the validator:

    python content/sources/g6-maths-08/perimeter.py
    python tools/validate_lessons.py

Edit the script, not the JSON file, or the next run will undo the change. The last two lessons fill gaps found against the PCTB Grade 6 book (Sub-domain 8). The Urdu terms are still to be checked.

Every lesson opens with two short "why" steps (`s0_why`: the need that led to the idea and what it solved, with Mithu's question; `s0_use`: where it helps in real life). Their texts are in `why.py`, and `write()` in `common.py` adds them through `content/sources/why_steps.py`. Edit `why.py`, then rerun the lesson script.
