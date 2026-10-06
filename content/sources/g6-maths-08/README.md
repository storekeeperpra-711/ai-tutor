# Perimeter and Area unit lesson sources (Grade 6)

Scripts that write the Grade 6 Maths lessons of the Perimeter and Area unit (`content/lessons/g6-maths-08-*.json`):

| Script | Lesson | Skill |
|---|---|---|
| `perimeter.py` | `g6-maths-08-perimeter` | `maths.measurement.perimeter` |
| `area_rectangles.py` | `g6-maths-08-area-of-rectangles` | `maths.measurement.area_rectangle` |
| `compound_shapes.py` | `g6-maths-08-compound-shapes` | `maths.measurement.compound_area` |

Every answer, and every common wrong answer (like giving the perimeter when the area is asked), is worked out in Python and checked with `assert`, so no number is typed by hand. There are no pictures yet: each shape is described in words.

To change a lesson, edit its script and run it, then run the validator:

    python content/sources/g6-maths-08/perimeter.py
    python tools/validate_lessons.py

Edit the script, not the JSON file, or the next run will undo the change. The unit number (08) and the Urdu terms are still to be confirmed against the PCTB Grade 6 book.
