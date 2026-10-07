# Whole numbers unit lesson sources (Grade 6)

Scripts that write the Grade 6 Maths lessons of the Whole Numbers unit (`content/lessons/g6-maths-15-*.json`):

| Script | Lesson | Skill |
|---|---|---|
| `lakhs_and_crores.py` | `g6-maths-15-lakhs-and-crores` | `maths.whole.place_value` |
| `millions.py` | `g6-maths-15-millions` | `maths.whole.number_systems` |
| `comparing_numbers.py` | `g6-maths-15-comparing-numbers` | `maths.whole.compare` |
| `properties.py` | `g6-maths-15-properties` | `maths.whole.properties` |
| `whole_number_word_problems.py` | `g6-maths-15-whole-number-word-problems` | `maths.whole.word_problems` (with a 5-question unit test) |

Every answer, and every common wrong answer (like taking a million for a crore, or comparing first digits before counting digits), is worked out in Python and checked with `assert`, so no number is typed by hand. `pk()` and `intl()` in `common.py` write numbers with Pakistani (2,45,67,890) and international (24,567,890) commas. Children may type answers with or without commas.

To change a lesson, edit its script and run it, then run the validator:

    python content/sources/g6-maths-15/millions.py
    python tools/validate_lessons.py

Edit the script, not the JSON file, or the next run will undo the change. The unit number (15) and the Urdu terms are still to be confirmed against the PCTB Grade 6 book.
