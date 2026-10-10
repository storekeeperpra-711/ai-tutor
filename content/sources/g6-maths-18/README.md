# Symmetry unit lesson sources (Grade 6)

Scripts that write the Grade 6 Maths lessons of the Symmetry unit (`content/lessons/g6-maths-18-*.json`). The unit follows PCTB Mathematics 6 (SNC 2022), Sub-domain 9: Symmetry.

| Script | Lesson | Skill |
|---|---|---|
| `shapes_2d_3d.py` | `g6-maths-18-1d-2d-3d-shapes` | `maths.symmetry.shapes_2d_3d` |
| `parallel_lines_transversal.py` | `g6-maths-18-parallel-lines-and-transversal` | `maths.symmetry.parallel_transversal` |
| `line_symmetry.py` | `g6-maths-18-line-symmetry` | `maths.symmetry.line_symmetry` |
| `rotational_symmetry.py` | `g6-maths-18-rotational-symmetry` | `maths.symmetry.rotational` (with a 5-question unit test) |
| `exercise_9_1.py` | `g6-maths-18-exercise-9-1` | `maths.symmetry.ex_9_1` |
| `exercise_9_2.py` | `g6-maths-18-exercise-9-2` | `maths.symmetry.ex_9_2` |
| `exercise_9_3.py` | `g6-maths-18-exercise-9-3` | `maths.symmetry.ex_9_3` |
| `chapter_9_test.py` | `g6-maths-18-chapter-9-test` | `maths.symmetry.chapter_9_test` |

The last four are the practice sets for Exercises 9.1, 9.2 and 9.3 of the book (chapter 9, Symmetry) and a chapter test (Review Exercise 9) for the whole chapter. Only the exercise numbers and the kinds of question follow the book; every question, number and story is new. They have no "why" steps. The shared pictures (solids, letters, grids, parallel lines with a transversal) are drawn by `figs.py`, which checks lines of symmetry and orders of rotation by really flipping and turning the shapes. `common.py` holds the practice helpers (`nq`, `ch`, `practice_lesson`, `practice_intro`).

These lessons use drawn figures (the step `figure` block). Every figure's coordinates are worked out in Python: regular shapes and turns with `math.cos`/`math.sin`, line crossings and angle arcs from the stated angles, so the picture matches the numbers. Counts such as lines of symmetry and the order of rotational symmetry are checked by reflecting or turning the drawn shape, and every answer and common wrong answer is checked with `assert`.

To change a lesson, edit its script and run it, then run the validator:

    python content/sources/g6-maths-18/line_symmetry.py
    python tools/validate_lessons.py

Edit the script, not the JSON file, or the next run will undo the change. The Urdu terms are still to be checked.

Every lesson opens with two short "why" steps (`s0_why`: the need that led to the idea and what it solved, with Mithu's question; `s0_use`: where it helps in real life). Their texts are in `why.py`, and `write()` in `common.py` adds them through `content/sources/why_steps.py`. Edit `why.py`, then rerun the lesson script.
