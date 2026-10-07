# Percentages unit lesson sources (Grade 6)

Scripts that write the Grade 6 Maths lessons of the Percentages unit (`content/lessons/g6-maths-11-*.json`):

| Script | Lesson | Skill |
|---|---|---|
| `what_is_a_percent.py` | `g6-maths-11-what-is-a-percent` | `maths.percent.meaning` |
| `percent_fraction_decimal.py` | `g6-maths-11-percents-fractions-decimals` | `maths.percent.convert` |
| `percent_of_amount.py` | `g6-maths-11-percent-of-an-amount` | `maths.percent.of_amount` |
| `finding_the_percentage.py` | `g6-maths-11-finding-the-percentage` | `maths.percent.find_percent` |
| `percent_word_problems.py` | `g6-maths-11-percent-word-problems` | `maths.percent.word_problems` |

Every answer, and every common wrong answer (like reading 7% as 7 out of 10, or giving the percent itself as the answer), is worked out in Python with exact decimals (`percent_of` and `as_percent` in `common.py`) and checked with `assert`, so no number is typed by hand. The word-problems lesson ends with a five-question unit test, each question tagged with an earlier lesson's skill. Percent answers are typed without the % sign.

To change a lesson, edit its script and run it, then run the validator:

    python content/sources/g6-maths-11/percent_of_amount.py
    python tools/validate_lessons.py

Edit the script, not the JSON file, or the next run will undo the change. The unit number (11) and the Urdu terms are still to be confirmed against the PCTB Grade 6 book.
