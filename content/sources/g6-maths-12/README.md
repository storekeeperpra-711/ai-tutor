# Profit and loss unit lesson sources (Grade 6)

Scripts that write the Grade 6 Maths lessons of the Profit and Loss unit (`content/lessons/g6-maths-12-*.json`):

| Script | Lesson | Skill |
|---|---|---|
| `profit_and_loss.py` | `g6-maths-12-profit-and-loss` | `maths.money.profit_loss` |
| `profit_loss_percent.py` | `g6-maths-12-profit-loss-percent` | `maths.money.profit_loss_percent` |
| `selling_price.py` | `g6-maths-12-selling-price` | `maths.money.selling_price` |
| `bills_and_change.py` | `g6-maths-12-bills-and-change` | `maths.money.bills` |
| `profit_loss_word_problems.py` | `g6-maths-12-profit-loss-word-problems` | `maths.money.word_problems` |

Every answer, and every common wrong answer (like giving the selling price as the profit, dividing by the selling price, or adding 10% as Rs 10), is worked out in Python with exact decimals (`percent_of` and `as_percent` in `common.py`) and checked with `assert`, so no number is typed by hand. The word-problems lesson ends with a five-question unit test, each question tagged with an earlier lesson's skill. Percent answers are typed without the % sign.

To change a lesson, edit its script and run it, then run the validator:

    python content/sources/g6-maths-12/selling_price.py
    python tools/validate_lessons.py

Edit the script, not the JSON file, or the next run will undo the change. The unit number (12) and the Urdu terms are still to be confirmed against the PCTB Grade 6 book.
