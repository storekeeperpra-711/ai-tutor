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

Every lesson has drawn pictures (`figure` blocks): ovals holding the elements of a set, letter tiles, number lines and grids, boxes for subsets, and Venn diagrams with the overlap or union shaded; the helpers are in `figs.py`, and each script attaches its pictures at the end with `attach` (the universal-set lesson keeps its own small Venn helper, which checks every element sits in the right circles).

To change a lesson, edit its script and run it, then run the validator:

    python content/sources/g6-maths-01/subsets.py
    python tools/validate_lessons.py

Edit the script, not the JSON file, or the next run will undo the change. The unit number (01) and the Urdu terms are still to be confirmed against the PCTB Grade 6 book.

Every lesson opens with two short "why" steps (`s0_why`: the need that led to the idea and what it solved, with Mithu's question; `s0_use`: where it helps in real life). Their texts are in `why.py`, and `write()` in `common.py` adds them through `content/sources/why_steps.py`. Edit `why.py`, then rerun the lesson script.
