# Symmetry unit lesson sources (Grade 6)

Scripts that write the Grade 6 Maths lessons of the Symmetry unit (`content/lessons/g6-maths-18-*.json`). The unit follows PCTB Mathematics 6 (SNC 2022), Sub-domain 9: Symmetry.

| Script | Lesson | Skill |
|---|---|---|
| `shapes_2d_3d.py` | `g6-maths-18-1d-2d-3d-shapes` | `maths.symmetry.shapes_2d_3d` |
| `parallel_lines_transversal.py` | `g6-maths-18-parallel-lines-and-transversal` | `maths.symmetry.parallel_transversal` |
| `line_symmetry.py` | `g6-maths-18-line-symmetry` | `maths.symmetry.line_symmetry` |
| `rotational_symmetry.py` | `g6-maths-18-rotational-symmetry` | `maths.symmetry.rotational` (with a 5-question unit test) |

These lessons use drawn figures (the step `figure` block). Every figure's coordinates are worked out in Python: regular shapes and turns with `math.cos`/`math.sin`, line crossings and angle arcs from the stated angles, so the picture matches the numbers. Counts such as lines of symmetry and the order of rotational symmetry are checked by reflecting or turning the drawn shape, and every answer and common wrong answer is checked with `assert`.

To change a lesson, edit its script and run it, then run the validator:

    python content/sources/g6-maths-18/line_symmetry.py
    python tools/validate_lessons.py

Edit the script, not the JSON file, or the next run will undo the change. The Urdu terms are still to be checked.
