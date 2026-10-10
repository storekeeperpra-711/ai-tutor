# Solids unit lesson sources (Grade 6)

Scripts that write the Grade 6 Maths lessons of the Solids unit (`content/lessons/g6-maths-14-*.json`):

| Script | Lesson | Skill |
|---|---|---|
| `solids.py` | `g6-maths-14-solids` | `maths.solids.faces_edges_vertices` |
| `volume_cuboid.py` | `g6-maths-14-volume-cuboid` | `maths.solids.volume_cuboid` |
| `volume_cube.py` | `g6-maths-14-volume-cube` | `maths.solids.volume_cube_capacity` |
| `surface_area.py` | `g6-maths-14-surface-area` | `maths.solids.surface_area` |
| `solids_word_problems.py` | `g6-maths-14-solids-word-problems` | `maths.solids.word_problems` (with a 5-question unit test) |
| `exercise_8_3.py` | `g6-maths-14-exercise-8-3` | `maths.solids.ex_8_3` |
| `chapter_8_test.py` | `g6-maths-14-chapter-8-test` | `maths.solids.chapter_8_test` |

The last two are the practice set for Exercise 8.3 of the book (chapter 8, Surface Area and Volume) and a chapter test (Review Exercise 8) for the whole chapter, which also covers the Perimeter and area unit (`g6-maths-08`, which holds the practice sets for Exercises 8.1 and 8.2). Only the exercise number and the kinds of question follow the book; every question is new, because the book may not be copied. Each has its own skill, with the skills of both units as prerequisites, and no `why.py` entry. The helpers they use (`nq`, `ch`, `practice_lesson`...) are repeated at the end of `common.py` in both units.

Every answer, and every common wrong answer (like adding the three lengths, stopping at the area of the base, or taking 100 cm³ as a litre), is worked out in Python (`cuboid_volume` and `cuboid_surface` in `common.py`) and checked with `assert`, so no number is typed by hand. There are no pictures yet, so solids are described with everyday objects: a matchbox, a brick, a dice.

To change a lesson, edit its script and run it, then run the validator:

    python content/sources/g6-maths-14/volume_cube.py
    python tools/validate_lessons.py

Edit the script, not the JSON file, or the next run will undo the change. The unit number (14) and the Urdu terms are still to be confirmed against the PCTB Grade 6 book.

Every lesson opens with two short "why" steps (`s0_why`: the need that led to the idea and what it solved, with Mithu's question; `s0_use`: where it helps in real life). Their texts are in `why.py`, and `write()` in `common.py` adds them through `content/sources/why_steps.py`. Edit `why.py`, then rerun the lesson script.
