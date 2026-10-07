# Solids unit lesson sources (Grade 6)

Scripts that write the Grade 6 Maths lessons of the Solids unit (`content/lessons/g6-maths-14-*.json`):

| Script | Lesson | Skill |
|---|---|---|
| `solids.py` | `g6-maths-14-solids` | `maths.solids.faces_edges_vertices` |
| `volume_cuboid.py` | `g6-maths-14-volume-cuboid` | `maths.solids.volume_cuboid` |
| `volume_cube.py` | `g6-maths-14-volume-cube` | `maths.solids.volume_cube_capacity` |

Every answer, and every common wrong answer (like adding the three lengths, stopping at the area of the base, or taking 100 cm³ as a litre), is worked out in Python (`cuboid_volume` and `cuboid_surface` in `common.py`) and checked with `assert`, so no number is typed by hand. There are no pictures yet, so solids are described with everyday objects: a matchbox, a brick, a dice.

To change a lesson, edit its script and run it, then run the validator:

    python content/sources/g6-maths-14/volume_cube.py
    python tools/validate_lessons.py

Edit the script, not the JSON file, or the next run will undo the change. The unit number (14) and the Urdu terms are still to be confirmed against the PCTB Grade 6 book.
