# Ratio and Proportion unit lesson sources (Grade 6)

Scripts that write the Grade 6 Maths lessons of the Ratio and Proportion unit (`content/lessons/g6-maths-06-*.json`):

| Script | Lesson | Skill |
|---|---|---|
| `what_is_a_ratio.py` | `g6-maths-06-what-is-a-ratio` | `maths.ratio.meaning` |
| `equivalent_ratios.py` | `g6-maths-06-equivalent-ratios` | `maths.ratio.equivalent` |
| `sharing_in_a_ratio.py` | `g6-maths-06-sharing-in-a-ratio` | `maths.ratio.share` |
| `proportion.py` | `g6-maths-06-proportion` | `maths.ratio.proportion` |
| `unitary_method.py` | `g6-maths-06-unitary-method` | `maths.ratio.unitary_method` |
| `ratio_word_problems.py` | `g6-maths-06-ratio-word-problems` | `maths.ratio.word_problems` |
| `rate.py` | `g6-maths-06-rate` | `maths.ratio.rate` (added after matching the PCTB book) |
| `continued_ratio.py` | `g6-maths-06-continued-ratio` | `maths.ratio.continued` |
| `twenty_four_hour_clock.py` | `g6-maths-06-24-hour-clock` | `maths.time.clock_24` |
| `speed.py` | `g6-maths-06-speed` | `maths.ratio.speed` |

Every answer, and every common wrong answer (like sharing equally whatever the ratio), is worked out in Python and checked with `assert`, so no number is typed by hand. The word-problems lesson ends with a five-question unit test, one question per earlier lesson, each tagged with that lesson's skill. Typed ratios use the text checker: `2:3`, `2 : 3` and `2 to 3` are all accepted.

To change a lesson, edit its script and run it, then run the validator:

    python content/sources/g6-maths-06/what_is_a_ratio.py
    python tools/validate_lessons.py

Edit the script, not the JSON file, or the next run will undo the change. The unit number (06) is still to be confirmed against the PCTB Grade 6 book.
