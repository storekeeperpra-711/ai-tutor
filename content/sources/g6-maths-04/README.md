# Integers unit lesson sources (Grade 6)

Scripts that write the Grade 6 Maths lessons of the Integers unit (`content/lessons/g6-maths-04-*.json`):

| Script | Lesson | Skill |
|---|---|---|
| `what_are_integers.py` | `g6-maths-04-what-are-integers` | `maths.integers.meaning` |
| `adding_integers.py` | `g6-maths-04-adding-integers` | `maths.integers.add` |
| `subtracting_integers.py` | `g6-maths-04-subtracting-integers` | `maths.integers.subtract` |
| `multiplying_dividing.py` | `g6-maths-04-multiplying-and-dividing-integers` | `maths.integers.multiply_divide` |
| `integer_word_problems.py` | `g6-maths-04-integer-word-problems` | `maths.integers.word_problems` |
| `absolute_value.py` | `g6-maths-04-absolute-value` | `maths.integers.absolute_value` |
| `laws_of_integers.py` | `g6-maths-04-laws-of-integers` | `maths.integers.laws` |
| `exercise_2_1.py` | `g6-maths-04-exercise-2-1` | `maths.integers.ex_2_1` |
| `exercise_2_2.py` | `g6-maths-04-exercise-2-2` | `maths.integers.ex_2_2` |
| `chapter_2_test.py` | `g6-maths-04-chapter-2-test` | `maths.integers.chapter_2_test` |

The `exercise_2_*.py` scripts write practice sets to use next to Exercises 2.1 and 2.2 of the PCTB Mathematics 6 book, and `chapter_2_test.py` writes a chapter test in the style of Review Exercise 2 (multiple choice, short questions, longer problems). The book may not be copied, so only the exercise number and the kinds of question come from it; every question, number and story is new. Each has its own skill with the unit's skills as prerequisites. These have no entry in `why.py`, so they get no why steps.

Every answer, and every common wrong answer (like ignoring the minus sign), is worked out in Python and checked with `assert`, so no number is typed by hand. Negative numbers are shown with a real minus sign (−3); the app accepts the keyboard minus too. The word-problems lesson ends with a five-question unit test, each question tagged with an earlier lesson's skill. Number-line steps use the native `number_line` sim from −10 to 10.

To change a lesson, edit its script and run it, then run the validator:

    python content/sources/g6-maths-04/what_are_integers.py
    python tools/validate_lessons.py

Edit the script, not the JSON file, or the next run will undo the change. The unit number (04) is still to be confirmed against the PCTB Grade 6 book.

Every lesson opens with two short "why" steps (`s0_why`: the need that led to the idea and what it solved, with Mithu's question; `s0_use`: where it helps in real life). Their texts are in `why.py`, and `write()` in `common.py` adds them through `content/sources/why_steps.py`. Edit `why.py`, then rerun the lesson script.
