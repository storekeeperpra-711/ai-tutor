# Angles unit lesson sources (Grade 6)

Scripts that write the Grade 6 Maths lessons of the Angles unit (`content/lessons/g6-maths-09-*.json`):

| Script | Lesson | Skill |
|---|---|---|
| `angle_types.py` | `g6-maths-09-types-of-angles` | `maths.geometry.angle_types` |
| `angles_on_a_line.py` | `g6-maths-09-angles-on-a-line` | `maths.geometry.angles_on_line` |
| `angle_pairs.py` | `g6-maths-09-complementary-supplementary` | `maths.geometry.complementary_supplementary` |
| `triangle_angles.py` | `g6-maths-09-angles-in-a-triangle` | `maths.geometry.triangle_angles` |
| `angle_word_problems.py` | `g6-maths-09-angle-word-problems` | `maths.geometry.word_problems` |

Every answer, and every common wrong answer (like using 360° on a straight line), is worked out in Python and checked with `assert`, so no number is typed by hand. The "what kind of angle" questions are built by `kind_question` in `common.py`, which picks the right option from the angle's size. There are no pictures yet: each angle is given in degrees or as a clock or a door. The word-problems lesson ends with a five-question unit test, each question tagged with an earlier lesson's skill.

To change a lesson, edit its script and run it, then run the validator:

    python content/sources/g6-maths-09/angle_types.py
    python tools/validate_lessons.py

Edit the script, not the JSON file, or the next run will undo the change. The unit number (09) and the Urdu terms are still to be confirmed against the PCTB Grade 6 book.
