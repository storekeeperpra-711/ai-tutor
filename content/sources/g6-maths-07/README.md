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

Every answer, and every common wrong answer (like reading 3n as thirty-something), is worked out in Python and checked with `assert`, so no number is typed by hand. `common.py` has `value()`, which works out an expression such as `3n + 2` for given numbers; simplifications are checked by putting in many numbers. Typed expressions use the `text` checker, with `accept` listing other right ways to write them (4 + n, b6). Equations are solved by `solve()` in the scripts, which also checks there is only one answer. The word-problems lesson ends with a five-question unit test, each question tagged with an earlier lesson's skill.

`maths.algebra.expressions_basic` is also the warm-up skill of the Grade 9 linear equations lesson, so this unit now teaches it.

To change a lesson, edit its script and run it, then run the validator:

    python content/sources/g6-maths-07/like_terms.py
    python tools/validate_lessons.py

Edit the script, not the JSON file, or the next run will undo the change. The unit number (07) and the Urdu terms are still to be confirmed against the PCTB Grade 6 book.
