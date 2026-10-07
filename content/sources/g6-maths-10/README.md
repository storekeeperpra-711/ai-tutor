# Data Handling unit lesson sources (Grade 6)

Scripts that write the Grade 6 Maths lessons of the Data Handling unit (`content/lessons/g6-maths-10-*.json`):

| Script | Lesson | Skill |
|---|---|---|
| `tables_tallies.py` | `g6-maths-10-tables-and-tallies` | `maths.data.tables` |
| `bar_graphs.py` | `g6-maths-10-bar-graphs` | `maths.data.bar_graphs` |
| `mean.py` | `g6-maths-10-average-mean` | `maths.data.mean` |
| `mode_range.py` | `g6-maths-10-mode-and-range` | `maths.data.mode_range` |
| `data_word_problems.py` | `g6-maths-10-data-word-problems` | `maths.data.word_problems` |

Every answer, and every common wrong answer (like giving the total instead of the mean), is worked out in Python and checked with `assert`, so no number is typed by hand. There are no pictures yet: tables and bar graphs are written as short lists (`table_text` in `common.py`), and a tally group of five is written `IIII/` (`tally` in `common.py`). The word-problems lesson ends with a five-question unit test, each question tagged with an earlier lesson's skill.

To change a lesson, edit its script and run it, then run the validator:

    python content/sources/g6-maths-10/mean.py
    python tools/validate_lessons.py

Edit the script, not the JSON file, or the next run will undo the change. The unit number (10) and the Urdu terms are still to be confirmed against the PCTB Grade 6 book.
