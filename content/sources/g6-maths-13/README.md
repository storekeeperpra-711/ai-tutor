# Simplification unit lesson sources (Grade 6)

Scripts that write the Grade 6 Maths lessons of the Simplification unit (`content/lessons/g6-maths-13-*.json`):

| Script | Lesson | Skill |
|---|---|---|
| `order_of_operations.py` | `g6-maths-13-order-of-operations` | `maths.simplify.order_of_operations` |
| `brackets.py` | `g6-maths-13-brackets` | `maths.simplify.brackets` |
| `fractions_decimals.py` | `g6-maths-13-fractions-decimals` | `maths.simplify.fractions_decimals` |

Every answer, and every common wrong answer (like working strictly left to right, ignoring the brackets, or multiplying only the first number in a bracket), is worked out in Python with exact decimals and fractions and checked with `assert`, so no number is typed by hand. Python follows the same order of operations as BODMAS, so each expression is written in the script just as it appears in the lesson.

To change a lesson, edit its script and run it, then run the validator:

    python content/sources/g6-maths-13/brackets.py
    python tools/validate_lessons.py

Edit the script, not the JSON file, or the next run will undo the change. The unit number (13) and the Urdu terms are still to be confirmed against the PCTB Grade 6 book.
