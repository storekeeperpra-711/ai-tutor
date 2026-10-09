# Linear equations unit lesson sources (Grade 6)

Scripts that write the Grade 6 Maths lessons of the Linear Equations unit (`content/lessons/g6-maths-16-*.json`):

| Script | Lesson | Skill |
|---|---|---|
| `checking_solutions.py` | `g6-maths-16-checking-solutions` | `maths.equations.check_solution` |
| `forming_equations.py` | `g6-maths-16-forming-equations` | `maths.equations.forming` |
| `two_step_equations.py` | `g6-maths-16-two-step-equations` | `maths.equations.two_step` |
| `equations_with_brackets.py` | `g6-maths-16-equations-with-brackets` | `maths.equations.brackets` |
| `equation_word_problems.py` | `g6-maths-16-equation-word-problems` | `maths.equations.word_problems` (with a 5-question unit test) |
| `equations_and_expressions.py` | `g6-maths-16-equations-and-expressions` | `maths.equations.equation_or_expression` |

Every answer is checked with `solves()` in `common.py`, which puts the answer back into the equation, and every common wrong answer (like dividing before subtracting, or reading 3x as 36) is worked out and checked with `assert`. No number is typed by hand.

The pictures (balance scales with boxes for the unknown, bar models, bags for brackets, and rows that put a number in place of a letter) are drawn by `figs.py` from the same numbers the steps use.

To change a lesson, edit its script and run it, then run the validator:

    python content/sources/g6-maths-16/two_step_equations.py
    python tools/validate_lessons.py

Edit the script, not the JSON file, or the next run will undo the change. The unit number (16) and the Urdu terms are still to be confirmed against the PCTB Grade 6 book.
