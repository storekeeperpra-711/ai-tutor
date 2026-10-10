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
| `exercise_4_1.py` | `g6-maths-06-exercise-4-1` | `maths.ratio.ex_4_1` |
| `exercise_4_2.py` | `g6-maths-06-exercise-4-2` | `maths.ratio.ex_4_2` |
| `exercise_4_3.py` | `g6-maths-06-exercise-4-3` | `maths.percent.ex_4_3` |
| `exercise_4_4.py` | `g6-maths-06-exercise-4-4` | `maths.time.ex_4_4` |
| `exercise_4_5.py` | `g6-maths-06-exercise-4-5` | `maths.ratio.ex_4_5` |
| `chapter_4_test.py` | `g6-maths-06-chapter-4-test` | `maths.ratio.chapter_4_test` |

The `exercise_4_*.py` scripts write practice sets to use next to Exercises 4.1 to 4.5 of the PCTB Mathematics 6 book (ratio, rate, percentage, time, speed), and `chapter_4_test.py` writes a chapter test in the style of Review Exercise 4 (multiple choice, short questions, longer problems). The book may not be copied, so only the exercise number and the kinds of question come from it; every question, number and story is new. Each has its own skill with the chapter's skills as prerequisites; Exercise 4.3 has a `maths.percent` skill and Exercise 4.4 a `maths.time` skill because the chapter's lessons also live in the Percentages unit and the clock lesson. These have no entry in `why.py`, so they get no why steps.

Every answer, and every common wrong answer (like sharing equally whatever the ratio), is worked out in Python and checked with `assert`, so no number is typed by hand. The word-problems lesson ends with a five-question unit test, one question per earlier lesson, each tagged with that lesson's skill. Typed ratios use the text checker: `2:3`, `2 : 3` and `2 to 3` are all accepted.

To change a lesson, edit its script and run it, then run the validator:

    python content/sources/g6-maths-06/what_is_a_ratio.py
    python tools/validate_lessons.py

Edit the script, not the JSON file, or the next run will undo the change. The unit number (06) is still to be confirmed against the PCTB Grade 6 book.

Every lesson opens with two short "why" steps (`s0_why`: the need that led to the idea and what it solved, with Mithu's question; `s0_use`: where it helps in real life). Their texts are in `why.py`, and `write()` in `common.py` adds them through `content/sources/why_steps.py`. Edit `why.py`, then rerun the lesson script.
