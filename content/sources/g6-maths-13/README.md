# Simplification unit lesson sources (Grade 6)

Scripts that write the Grade 6 Maths lessons of the Simplification unit (`content/lessons/g6-maths-13-*.json`):

| Script | Lesson | Skill |
|---|---|---|
| `order_of_operations.py` | `g6-maths-13-order-of-operations` | `maths.simplify.order_of_operations` |
| `brackets.py` | `g6-maths-13-brackets` | `maths.simplify.brackets` |
| `fractions_decimals.py` | `g6-maths-13-fractions-decimals` | `maths.simplify.fractions_decimals` |
| `estimation.py` | `g6-maths-13-estimation` | `maths.simplify.estimation` |
| `simplification_word_problems.py` | `g6-maths-13-simplification-word-problems` | `maths.simplify.word_problems` |

Every answer, and every common wrong answer (like working strictly left to right, ignoring the brackets, or multiplying only the first number in a bracket), is worked out in Python with exact decimals and fractions and checked with `assert`, so no number is typed by hand. Python follows the same order of operations as BODMAS, so each expression is written in the script just as it appears in the lesson. Rounding uses `round_to` in `common.py`, where a 5 rounds up as taught in school. The word-problems lesson ends with a five-question unit test, each question tagged with an earlier lesson's skill.

Pictures (each expression with its numbered steps drawn under it, groups of counters, fraction bars for "of", bar models for word problems, and number lines for rounding) are drawn by `figs.py` and attached at the end of each script; the expression pictures are built from the same expressions as the steps and checked against the step text.

To change a lesson, edit its script and run it, then run the validator:

    python content/sources/g6-maths-13/brackets.py
    python tools/validate_lessons.py

Edit the script, not the JSON file, or the next run will undo the change. The unit number (13) and the Urdu terms are still to be confirmed against the PCTB Grade 6 book.

Every lesson opens with two short "why" steps (`s0_why`: the need that led to the idea and what it solved, with Mithu's question; `s0_use`: where it helps in real life). Their texts are in `why.py`, and `write()` in `common.py` adds them through `content/sources/why_steps.py`. Edit `why.py`, then rerun the lesson script.
