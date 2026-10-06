# Fractions unit lesson sources (Grade 6)

Scripts that write three Grade 6 Maths lessons of the Fractions unit (`content/lessons/g6-maths-02-*.json`):

| Script | Lesson | Skill |
|---|---|---|
| `equivalent_fractions.py` | `g6-maths-02-equivalent-fractions` | `maths.fractions.equivalent` |
| `adding_fractions.py` | `g6-maths-02-adding-fractions` | `maths.fractions.add_unlike` |
| `mixed_numbers.py` | `g6-maths-02-mixed-numbers` | `maths.fractions.mixed_numbers` |

Every answer, and every common wrong answer (like 1/2 + 1/3 = 2/5), is worked out with Python's `fractions.Fraction` and checked with `assert`, so no number is typed by hand. The fourth lesson of the unit, `g6-maths-02-dividing-fractions`, was written by hand and has no script.

To change a lesson, edit its script and run it, then run the validator:

    python content/sources/g6-maths-02/adding_fractions.py
    python tools/validate_lessons.py

Edit the script, not the JSON file, or the next run will undo the change. The unit number (02) is still to be confirmed against the PCTB Grade 6 book.
