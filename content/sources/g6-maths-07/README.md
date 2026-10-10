# Introduction to Algebra unit lesson sources (Grade 6)

Scripts that write the Grade 6 Maths lessons of the Introduction to Algebra unit (`content/lessons/g6-maths-07-*.json`):

| Script | Lesson | Skill |
|---|---|---|
| `letters_for_numbers.py` | `g6-maths-07-letters-for-numbers` | `maths.algebra.variables` |
| `substitution.py` | `g6-maths-07-substitution` | `maths.algebra.substitution` |
| `like_terms.py` | `g6-maths-07-like-terms` | `maths.algebra.expressions_basic` |
| `simple_equations.py` | `g6-maths-07-simple-equations` | `maths.algebra.simple_equations` |
| `algebra_word_problems.py` | `g6-maths-07-algebra-word-problems` | `maths.algebra.word_problems` |
| `number_patterns.py` | `g6-maths-07-number-patterns` | `maths.algebra.sequences` (added after matching the PCTB book) |
| `terms_and_coefficients.py` | `g6-maths-07-terms-and-coefficients` | `maths.algebra.terms` |
| `adding_subtracting_expressions.py` | `g6-maths-07-adding-subtracting-expressions` | `maths.algebra.add_subtract` |
| `exercise_6_1.py` | `g6-maths-07-exercise-6-1` | `maths.algebra.ex_6_1` |
| `exercise_6_2.py` | `g6-maths-07-exercise-6-2` | `maths.algebra.ex_6_2` |
| `exercise_6_3.py` | `g6-maths-07-exercise-6-3` | `maths.algebra.ex_6_3` |
| `exercise_6_4.py` | `g6-maths-07-exercise-6-4` | `maths.algebra.ex_6_4` |
| `exercise_6_5.py` | `g6-maths-07-exercise-6-5` | `maths.algebra.ex_6_5` |
| `chapter_6_test.py` | `g6-maths-07-chapter-6-test` | `maths.algebra.chapter_6_test` |

The last six are practice sets for Exercises 6.1 to 6.5 of the book and a chapter test (Review Exercise 6). Only the exercise number and the kinds of question follow the book; every question is new, because the book may not be copied. Each has its own skill, with the chapter's skills it practises as prerequisites, and no `why.py` entry. Typed expressions (`aq` in `common.py`) accept the terms in any order, and every wrong answer is given as terms that are checked to differ from the right one.

Every answer, and every common wrong answer (like reading 3n as thirty-something), is worked out in Python and checked with `assert`, so no number is typed by hand. `common.py` has `value()`, which works out an expression such as `3n + 2` for given numbers; simplifications are checked by putting in many numbers. Typed expressions use the `text` checker, with `accept` listing other right ways to write them (4 + n, b6). Equations are solved by `solve()` in the scripts, which also checks there is only one answer. The word-problems lesson ends with a five-question unit test, each question tagged with an earlier lesson's skill.

`maths.algebra.expressions_basic` is also the warm-up skill of the Grade 9 linear equations lesson, so this unit now teaches it.

Every lesson has drawn pictures (`figure` blocks): bags of marbles for a letter, algebra tiles, balance scales for equations, bar models for word problems, and number cards, tables and matchstick patterns for sequences; the helpers are in `figs.py`, and each script attaches its pictures at the end with `attach`.

To change a lesson, edit its script and run it, then run the validator:

    python content/sources/g6-maths-07/like_terms.py
    python tools/validate_lessons.py

Edit the script, not the JSON file, or the next run will undo the change. The unit number (07) and the Urdu terms are still to be confirmed against the PCTB Grade 6 book.

Every lesson opens with two short "why" steps (`s0_why`: the need that led to the idea and what it solved, with Mithu's question; `s0_use`: where it helps in real life). Their texts are in `why.py`, and `write()` in `common.py` adds them through `content/sources/why_steps.py`. Edit `why.py`, then rerun the lesson script.
