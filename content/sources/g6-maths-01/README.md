# Sets unit lesson sources (Grade 6)

Scripts that write the Grade 6 Maths lessons of the Sets unit (`content/lessons/g6-maths-01-*.json`):

| Script | Lesson | Skill |
|---|---|---|
| `what_is_a_set.py` | `g6-maths-01-what-is-a-set` | `maths.sets.meaning` |
| `kinds_of_sets.py` | `g6-maths-01-kinds-of-sets` | `maths.sets.kinds` |
| `subsets.py` | `g6-maths-01-subsets` | `maths.sets.subsets` |
| `union_intersection.py` | `g6-maths-01-union-and-intersection` | `maths.sets.union_intersection` |
| `set_word_problems.py` | `g6-maths-01-set-word-problems` | `maths.sets.word_problems` |
| `universal_set_venn.py` | `g6-maths-01-universal-set-and-venn-diagrams` | `maths.sets.universal_venn` (Venn pictures drawn by the app) |

Every answer is worked out with Python sets and checked with `assert`: element counts, which sets are equal or equivalent, and subset counts (listed with `itertools.combinations`). So no number is typed by hand. Sets are written in braces with `show` in `common.py`. The word-problems lesson ends with a five-question unit test, each question tagged with an earlier lesson's skill.

To change a lesson, edit its script and run it, then run the validator:

    python content/sources/g6-maths-01/subsets.py
    python tools/validate_lessons.py

Edit the script, not the JSON file, or the next run will undo the change. The unit number (01) and the Urdu terms are still to be confirmed against the PCTB Grade 6 book.
