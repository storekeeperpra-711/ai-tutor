# Factors and Multiples unit lesson sources (Grade 6)

Scripts that write the Grade 6 Maths lessons of the Factors and Multiples unit (`content/lessons/g6-maths-05-*.json`):

| Script | Lesson | Skill |
|---|---|---|
| `factors_and_multiples.py` | `g6-maths-05-factors-and-multiples` | `maths.factors.factors_multiples` |
| `prime_numbers.py` | `g6-maths-05-prime-numbers` | `maths.factors.primes` |
| `hcf.py` | `g6-maths-05-highest-common-factor` | `maths.factors.hcf` |
| `lcm.py` | `g6-maths-05-lowest-common-multiple` | `maths.factors.lcm` |
| `factor_word_problems.py` | `g6-maths-05-factor-word-problems` | `maths.factors.word_problems` |
| `squares_index_notation.py` | `g6-maths-05-squares-and-index-notation` | `maths.factors.index_notation` |
| `hcf_lcm_product.py` | `g6-maths-05-hcf-times-lcm` | `maths.factors.hcf_lcm_product` |
| `exercise_1_1.py` | `g6-maths-05-exercise-1-1` | `maths.factors.ex_1_1` |
| `exercise_1_2.py` | `g6-maths-05-exercise-1-2` | `maths.factors.ex_1_2` |
| `exercise_1_3.py` | `g6-maths-05-exercise-1-3` | `maths.factors.ex_1_3` |
| `exercise_1_4.py` | `g6-maths-05-exercise-1-4` | `maths.factors.ex_1_4` |
| `exercise_1_5.py` | `g6-maths-05-exercise-1-5` | `maths.factors.ex_1_5` |
| `exercise_1_6.py` | `g6-maths-05-exercise-1-6` | `maths.factors.ex_1_6` |
| `chapter_1_test.py` | `g6-maths-05-chapter-1-test` | `maths.factors.chapter_1_test` |

The `exercise_1_*.py` scripts write practice sets to use next to Exercises 1.1 to 1.6 of the PCTB Mathematics 6 book, and `chapter_1_test.py` writes a chapter test in the style of Review Exercise 1 (multiple choice, short questions, longer problems). The book may not be copied, so only the exercise number and the kinds of question come from it; every question, number and story is new. Each has its own skill with the unit's skills as prerequisites, like the Grade 9 board-exam practice. The division methods for prime factors and the LCM, and the long division method for the HCF, are shown once in these sets, since the unit's lessons do not teach them. `figs.division_ladder` draws them.

Every answer, and every common wrong answer (like giving a multiple when a factor is asked), is worked out in Python and checked with `assert`, so no number is typed by hand. `common.py` has small helpers (`factors`, `is_prime`, `prime_factors`) the scripts check their numbers with.

Pictures (dot arrays for factor pairs and square numbers, factor trees, jumps on number lines for multiples, Venn circles for common factors and shared primes, number grids for primes, and same-area rectangles for HCF × LCM) are drawn by `figs.py` and attached at the end of each script; their numbers come from the same Python values as the steps.

To change a lesson, edit its script and run it, then run the validator:

    python content/sources/g6-maths-05/hcf.py
    python tools/validate_lessons.py

Edit the script, not the JSON file, or the next run will undo the change. The newest lessons fill gaps found against the PCTB Grade 6 book. The Urdu terms are still to be checked.

The seven teaching lessons open with two short "why" steps (`s0_why`: the need that led to the idea and what it solved, with Mithu's question; `s0_use`: where it helps in real life). Their texts are in `why.py`, and `write()` in `common.py` adds them through `content/sources/why_steps.py`. The practice sets and the chapter test have no entry, so they are unchanged. Edit `why.py`, then rerun the lesson script.
