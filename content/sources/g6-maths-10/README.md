# Data Handling unit lesson sources (Grade 6)

Scripts that write the Grade 6 Maths lessons of the Data Handling unit (`content/lessons/g6-maths-10-*.json`):

| Script | Lesson | Skill |
|---|---|---|
| `tables_tallies.py` | `g6-maths-10-tables-and-tallies` | `maths.data.tables` |
| `bar_graphs.py` | `g6-maths-10-bar-graphs` | `maths.data.bar_graphs` |
| `mean.py` | `g6-maths-10-average-mean` | `maths.data.mean` |
| `mode_range.py` | `g6-maths-10-mode-and-range` | `maths.data.mode_range` |
| `data_word_problems.py` | `g6-maths-10-data-word-problems` | `maths.data.word_problems` |
| `kinds_of_data.py` | `g6-maths-10-kinds-of-data` | `maths.data.kinds` |
| `median.py` | `g6-maths-10-median` | `maths.data.median` |
| `pie_charts.py` | `g6-maths-10-pie-charts-and-multiple-bar-graphs` | `maths.data.pie_charts` |
| `exercise_11_1.py` | `g6-maths-10-exercise-11-1` | `maths.data.ex_11_1` |
| `exercise_11_2.py` | `g6-maths-10-exercise-11-2` | `maths.data.ex_11_2` |
| `exercise_11_3.py` | `g6-maths-10-exercise-11-3` | `maths.data.ex_11_3` |
| `exercise_11_4.py` | `g6-maths-10-exercise-11-4` | `maths.data.ex_11_4` |
| `chapter_11_test.py` | `g6-maths-10-chapter-11-test` | `maths.data.chapter_11_test` |

The last five are the practice sets for Exercises 11.1 to 11.4 of the book (chapter 11, Data Management) and a chapter test (Review Exercise 11) for the whole chapter. Only the exercise numbers and the kinds of question follow the book; every question, number and story is new. The app cannot check a drawing, so they ask about reading graphs and tables and calculating. They have no "why" steps. `figs.py` draws their graphs (it gained `hbar_graph` for horizontal bar graphs and `with_fig`), and `common.py` holds the practice helpers (`nq`, `ch`, `practice_lesson`, `practice_intro`).

Every answer, and every common wrong answer (like giving the total instead of the mean), is worked out in Python and checked with `assert`, so no number is typed by hand. There are no pictures yet: tables and bar graphs are written as short lists (`table_text` in `common.py`), and a tally group of five is written `IIII/` (`tally` in `common.py`). The word-problems lesson ends with a five-question unit test, each question tagged with an earlier lesson's skill.

To change a lesson, edit its script and run it, then run the validator:

    python content/sources/g6-maths-10/mean.py
    python tools/validate_lessons.py

Edit the script, not the JSON file, or the next run will undo the change. The last three lessons fill gaps found against the PCTB Grade 6 book (Sub-domain 11, Data Management). The Urdu terms are still to be checked.

Every lesson opens with two short "why" steps (`s0_why`: the need that led to the idea and what it solved, with Mithu's question; `s0_use`: where it helps in real life). Their texts are in `why.py`, and `write()` in `common.py` adds them through `content/sources/why_steps.py`. Edit `why.py`, then rerun the lesson script.
