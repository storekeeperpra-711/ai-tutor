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
| `exercise_7_1.py` | `g6-maths-16-exercise-7-1` | `maths.equations.ex_7_1` |
| `exercise_7_2.py` | `g6-maths-16-exercise-7-2` | `maths.equations.ex_7_2` |
| `chapter_7_test.py` | `g6-maths-16-chapter-7-test` | `maths.equations.chapter_7_test` |

The last three are practice sets for Exercises 7.1 and 7.2 of the book and a chapter test (Review Exercise 7). Only the exercise number and the kinds of question follow the book; every question is new, because the book may not be copied. Each has its own skill, with the chapter's skills it practises as prerequisites, and no `why.py` entry. Typed equations (`eq_q` in `common.py`) accept the other right ways to write them, and each right and wrong equation is checked with `solves()`.

Every answer is checked with `solves()` in `common.py`, which puts the answer back into the equation, and every common wrong answer (like dividing before subtracting, or reading 3x as 36) is worked out and checked with `assert`. No number is typed by hand.

The pictures (balance scales with boxes for the unknown, bar models, bags for brackets, and rows that put a number in place of a letter) are drawn by `figs.py` from the same numbers the steps use.

To change a lesson, edit its script and run it, then run the validator:

    python content/sources/g6-maths-16/two_step_equations.py
    python tools/validate_lessons.py

Edit the script, not the JSON file, or the next run will undo the change. The unit number (16) and the Urdu terms are still to be confirmed against the PCTB Grade 6 book.

Every lesson opens with two short "why" steps (`s0_why`: the need that led to the idea and what it solved, with Mithu's question; `s0_use`: where it helps in real life). Their texts are in `why.py`, and `write()` in `common.py` adds them through `content/sources/why_steps.py`. Edit `why.py`, then rerun the lesson script.
