# Probability unit lesson sources (Grade 6)

Scripts that write the Grade 6 Maths lessons of the Probability unit (`content/lessons/g6-maths-17-*.json`). The unit follows PCTB Mathematics 6 (SNC 2022), Sub-domain 12: Probability.

| Script | Lesson | Skill |
|---|---|---|
| `sample_space.py` | `g6-maths-17-sample-space` | `maths.probability.sample_space` |
| `probability_of_an_event.py` | `g6-maths-17-probability-of-an-event` | `maths.probability.single_event` |
| `likelihood.py` | `g6-maths-17-likelihood` | `maths.probability.likelihood` |
| `probability_word_problems.py` | `g6-maths-17-probability-word-problems` | `maths.probability.word_problems` (with a 5-question unit test) |

Sample spaces are built in `common.py` (`coins()`, `balls()`, `DICE`), and every probability is worked out with `P()`, which counts outcomes, so no answer is typed by hand. Each common wrong answer (dividing by the other outcomes, counting colours instead of balls, "win or lose is 1/2") is checked with `assert`.

The pictures (dice faces, coins, bags of balls, spinners, cards, ticket and class grids, and the 0 to 1 likelihood line) are drawn by `figs.py` from the same sample spaces the steps use.

Typed probabilities use the fraction checker without "simplest form", so 3/6, 1/2 and 0.5 are all right. Common wrong answers are written the way a child types them (2/4 stays 2/4), because they are matched as text.

To change a lesson, edit its script and run it, then run the validator:

    python content/sources/g6-maths-17/likelihood.py
    python tools/validate_lessons.py

Edit the script, not the JSON file, or the next run will undo the change. The Urdu terms (نمونی فضا، احتمال، واقعہ) are still to be checked by a teacher.

Every lesson opens with two short "why" steps (`s0_why`: the need that led to the idea and what it solved, with Mithu's question; `s0_use`: where it helps in real life). Their texts are in `why.py`, and `write()` in `common.py` adds them through `content/sources/why_steps.py`. Edit `why.py`, then rerun the lesson script.
