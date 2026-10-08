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

Every answer, and every common wrong answer (like ignoring the minus sign), is worked out in Python and checked with `assert`, so no number is typed by hand. Negative numbers are shown with a real minus sign (−3); the app accepts the keyboard minus too. The word-problems lesson ends with a five-question unit test, each question tagged with an earlier lesson's skill. Number-line steps use the native `number_line` sim from −10 to 10.

To change a lesson, edit its script and run it, then run the validator:

    python content/sources/g6-maths-04/what_are_integers.py
    python tools/validate_lessons.py

Edit the script, not the JSON file, or the next run will undo the change. The unit number (04) is still to be confirmed against the PCTB Grade 6 book.
