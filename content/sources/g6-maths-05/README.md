# Factors and Multiples unit lesson sources (Grade 6)

Scripts that write the Grade 6 Maths lessons of the Factors and Multiples unit (`content/lessons/g6-maths-05-*.json`):

| Script | Lesson | Skill |
|---|---|---|
| `factors_and_multiples.py` | `g6-maths-05-factors-and-multiples` | `maths.factors.factors_multiples` |
| `prime_numbers.py` | `g6-maths-05-prime-numbers` | `maths.factors.primes` |
| `hcf.py` | `g6-maths-05-highest-common-factor` | `maths.factors.hcf` |
| `lcm.py` | `g6-maths-05-lowest-common-multiple` | `maths.factors.lcm` |
| `factor_word_problems.py` | `g6-maths-05-factor-word-problems` | `maths.factors.word_problems` |

Every answer, and every common wrong answer (like giving a multiple when a factor is asked), is worked out in Python and checked with `assert`, so no number is typed by hand. `common.py` has small helpers (`factors`, `is_prime`, `prime_factors`) the scripts check their numbers with.

To change a lesson, edit its script and run it, then run the validator:

    python content/sources/g6-maths-05/hcf.py
    python tools/validate_lessons.py

Edit the script, not the JSON file, or the next run will undo the change. The unit number (05) and the Urdu terms are still to be confirmed against the PCTB Grade 6 book.
