# Unit 5 lesson sources

Scripts that write the Grade 9 Maths Unit 5 lessons on two-variable inequalities and linear programming (`content/lessons/g9-maths-05-*.json`). Every corner and objective value in them is worked out with exact fractions by `tools/plane.py`, so no number is typed by hand.

To change a lesson, edit its script and run it, then run the validator:

    python content/sources/g9-maths-05/linear_programming.py
    python tools/validate_lessons.py

Edit the script, not the JSON file, or the next run will undo the change.
