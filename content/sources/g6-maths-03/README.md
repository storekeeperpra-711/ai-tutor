# Decimals unit lesson sources (Grade 6)

Scripts that write the Grade 6 Maths lessons of the Decimals unit (`content/lessons/g6-maths-03-*.json`):

| Script | Lesson | Skill |
|---|---|---|
| `decimals_place_value.py` | `g6-maths-03-decimals-and-place-value` | `maths.decimals.place_value` |
| `comparing_decimals.py` | `g6-maths-03-comparing-decimals` | `maths.decimals.compare` |
| `adding_subtracting_decimals.py` | `g6-maths-03-adding-and-subtracting-decimals` | `maths.decimals.add_subtract` |
| `multiplying_dividing_decimals.py` | `g6-maths-03-multiplying-and-dividing-decimals` | `maths.decimals.multiply_divide` |
| `decimal_word_problems.py` | `g6-maths-03-decimal-word-problems` | `maths.decimals.word_problems` |

Every answer, and every common wrong answer (like lining up the last digits instead of the points), is worked out with Python's exact `Decimal` arithmetic and checked with `assert`, so no number is typed by hand and there are no rounding slips. The word-problems lesson ends with a five-question unit test, each question tagged with an earlier lesson's skill. Number-line steps use the native `number_line` sim with decimal labels.

To change a lesson, edit its script and run it, then run the validator:

    python content/sources/g6-maths-03/decimals_place_value.py
    python tools/validate_lessons.py

Edit the script, not the JSON file, or the next run will undo the change. The unit number (03) is still to be confirmed against the PCTB Grade 6 book.
