import math
from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, PA_PERIMETER, PA_AREA)

SKILL = PA_AREA


def rect_p(length, width):
    return 2 * (length + width)


# s2
assert rect_p(6, 3) == 18
# s4: 4 by 3, counted as 3 rows of 4
S4 = sum(4 for _ in range(3))
assert S4 == 4 * 3 == 12 and rect_p(4, 3) == 14 and 4 + 3 == 7
# s5: rug 6 by 4
S5 = 6 * 4
assert S5 == 24 and rect_p(6, 4) == 20
# s6: square side 9
S6 = 9 * 9
assert S6 == 81 and 4 * 9 == 36 and 9 * 2 == 18
# s7: area 40, length 8
S7 = 40 // 8
assert S7 == 5 and 8 * S7 == 40 and 40 - 8 == 32
# s8: same perimeter, different area
assert rect_p(7, 3) == rect_p(5, 5) == 20
S8 = 5 * 5 - 7 * 3
assert S8 == 4
# s9: 5 by 3
assert 5 * 3 == 15 and rect_p(5, 3) == 16
# s11: 8 m by 6 m floor, 1 m² tiles
S11 = 8 * 6
assert S11 == 48 and rect_p(8, 6) == 28
# question bank and review
QB = 12 * 5
assert QB == 60 and rect_p(12, 5) == 34
assert 4 * 4 == 16
R1 = 9 * 7
assert R1 == 63 and rect_p(9, 7) == 32
R2 = 10 * 10
assert R2 == 100 and 4 * 10 == 40



# ---------- figure helpers ----------
# Shapes are drawn to scale from the same numbers as the step text. Boxes are
# W wide; a label is about CHAR wide per letter and TALL high on a phone, so
# side labels are pushed out far enough not to touch the lines.

W = 100
CHAR = W / 30
TALL = W / 16


def r1(v):
    return round(v + 0.0, 1)


def pt(x, y):
    return [r1(x), r1(y)]


def poly(points, fill=True, dashed=False):
    item = {"kind": "polygon", "points": [pt(*p) for p in points]}
    if fill:
        item["fill"] = True
    if dashed:
        item["style"] = "dashed"
    return item


def seg(a, b, dashed=False):
    item = {"kind": "line", "from": pt(*a), "to": pt(*b)}
    if dashed:
        item["style"] = "dashed"
    return item


def label(at, text):
    return {"kind": "label", "at": pt(*at), "text": text}


def fig(height, alt, items):
    """A figure W wide; checks the labels' letters stay inside the box."""
    assert len(items) <= 60, len(items)
    for it in items:
        if it["kind"] == "label":
            x, y = it["at"]
            half_w, half_h = len(it["text"]) * CHAR / 2, TALL / 2
            assert x - half_w >= 0.5 and x + half_w <= W - 0.5, it
            assert y - half_h >= 0.5 and y + half_h <= height - 0.5, it
    return {"width": W, "height": r1(height), "alt": alt, "items": items}


def cm(n):
    return f"{n}cm"


def m(n):
    return f"{n}m"


class Scale:
    """Maps lengths (cm or m) to the box, the same scale both ways, centred.
    The box height follows the shape (at most max_h)."""

    def __init__(self, width, height, max_h=64, padx=15, pady=10):
        self.s = min((W - 2 * padx) / width, (max_h - 2 * pady) / height)
        self.h = height * self.s + 2 * pady
        self.x0 = (W - width * self.s) / 2
        self.y0 = pady

    def __call__(self, x, y):
        return (self.x0 + x * self.s, self.y0 + y * self.s)


def side(a, b, text, inside, gap=1.5):
    """Label for the side a-b, just outside it (away from the point inside)."""
    mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
    dx, dy = b[0] - a[0], b[1] - a[1]
    n = math.hypot(dx, dy)
    nx, ny = -dy / n, dx / n
    if (inside[0] - mx) * nx + (inside[1] - my) * ny > 0:
        nx, ny = -nx, -ny
    off = gap + abs(nx) * len(text) * CHAR / 2 + abs(ny) * TALL / 2
    return label((mx + nx * off, my + ny * off), text)


def centre(points):
    return (sum(p[0] for p in points) / len(points), sum(p[1] for p in points) / len(points))


def rect_pts(sc, x, y, w, h):
    return [sc(x, y), sc(x + w, y), sc(x + w, y + h), sc(x, y + h)]


def grid(sc, x, y, w, h, rows=None, cols=None):
    """Lines that split a w by h rectangle into unit squares (or only the
    first row and column of them, when rows/cols say how far to go)."""
    rows = h if rows is None else rows
    cols = w if cols is None else cols
    items = []
    for i in range(1, w):
        items.append(seg(sc(x + i, y), sc(x + i, y + (h if i <= cols else rows))))
    for j in range(1, h):
        items.append(seg(sc(x, y + j), sc(x + (w if j <= rows else cols), y + j)))
    return items


def rect_fig(length, width, unit, alt, sides=2, grid_lines=False, top=None, left=None, max_h=64):
    """A length by width rectangle to scale. sides=2 labels the bottom and
    the right; sides=4 labels all four sides. top/left replace a label."""
    sc = Scale(length, width, max_h=max_h)
    p = rect_pts(sc, 0, 0, length, width)
    c = centre(p)
    items = [poly(p)]
    if grid_lines:
        items += grid(sc, 0, 0, length, width)
    bottom_t = unit(length) if top is None else top
    right_t = unit(width) if left is None else left
    items += [side(p[3], p[2], bottom_t, c), side(p[1], p[2], right_t, c)]
    if sides == 4:
        items += [side(p[0], p[1], bottom_t, c), side(p[0], p[3], right_t, c)]
    return fig(sc.h, alt, items)


def right_angle(corner, toward_a, toward_b, size=3.5):
    """A small square mark in the corner between two directions."""
    def step(p, q):
        d = math.hypot(q[0] - p[0], q[1] - p[1])
        return ((q[0] - p[0]) / d * size, (q[1] - p[1]) / d * size)
    ax, ay = step(corner, toward_a)
    bx, by = step(corner, toward_b)
    p1 = (corner[0] + ax, corner[1] + ay)
    p2 = (corner[0] + ax + bx, corner[1] + ay + by)
    p3 = (corner[0] + bx, corner[1] + by)
    return [seg(p1, p2), seg(p2, p3)]


def with_figures(lesson, figures):
    """Attach each figure to the step with that id (main steps, question
    bank and review), and check every figure found its step."""
    used = set()
    steps = list(lesson["steps"])
    steps += [q["step"] for qs in lesson["question_bank"].values() for q in qs]
    steps += [q["step"] for q in lesson.get("review_questions", [])]
    for step in steps:
        if step["id"] in figures:
            step["figure"] = figures[step["id"]]
            used.add(step["id"])
    assert used == set(figures), set(figures) - used

# ---------- figures ----------

def rect_alt(length, width, unit_en, unit_ur, what_en="A rectangle", what_ur="ایک مستطیل", extra_en="", extra_ur=""):
    return T(f"{what_en}, {length} {unit_en} long and {width} {unit_en} wide, drawn to scale. The long side is labelled {length} {unit_en} and the short side {width} {unit_en}.{extra_en}",
             f"{what_ur}، {length} {unit_ur} لمبی اور {width} {unit_ur} چوڑی، پیمانے کے مطابق۔ لمبے ضلع پر {length} {unit_ur} اور چھوٹے ضلع پر {width} {unit_ur} لکھا ہے۔{extra_ur}")


def grid_alt(length, width, unit_en, unit_ur, what_en="A rectangle", what_ur="ایک مستطیل"):
    return rect_alt(length, width, unit_en, unit_ur, what_en, what_ur,
                    f" Lines split it into 1 {unit_en} squares: {width} rows of {length} squares.",
                    f" لکیریں اسے 1 {unit_ur} کے مربعوں میں بانٹتی ہیں: {length} مربعوں کی {width} قطاریں۔")


def square_fig(n, unit, unit_en, unit_ur, grid_lines=False):
    extra_en = f" Lines split it into {n} rows of {n} small squares." if grid_lines else ""
    extra_ur = f" لکیریں اسے {n} چھوٹے مربعوں کی {n} قطاروں میں بانٹتی ہیں۔" if grid_lines else ""
    return rect_fig(n, n, unit, T(f"A square with sides of {n} {unit_en}; two of its sides are labelled {n} {unit_en}.{extra_en}",
                                  f"ایک مربع جس کا ہر ضلع {n} {unit_ur} ہے؛ دو اضلاع پر {n} {unit_ur} لکھا ہے۔{extra_ur}"),
                    grid_lines=grid_lines)


F_RUG_GRID = rect_fig(6, 4, m, grid_alt(6, 4, "m", "میٹر", "Ammi's rug, a rectangle", "امی کا قالین، ایک مستطیل"), grid_lines=True)
F_RUG = rect_fig(6, 4, m, rect_alt(6, 4, "m", "میٹر", "Ammi's rug, a rectangle", "امی کا قالین، ایک مستطیل"))
F_4BY3 = rect_fig(4, 3, cm, grid_alt(4, 3, "cm", "سینٹی میٹر"), grid_lines=True)
F_SQUARE_9 = square_fig(9, cm, "cm", "سینٹی میٹر")
F_MISSING = rect_fig(8, S7, cm, T("A rectangle drawn to scale. Its long side is labelled 8 cm. Its short side is marked ? because we must find it. Its area is 40 cm².",
                                  "پیمانے کے مطابق ایک مستطیل۔ لمبے ضلع پر 8 سینٹی میٹر لکھا ہے۔ چھوٹے ضلع پر ? ہے کیونکہ وہ معلوم کرنا ہے۔ اس کا رقبہ 40 مربع سینٹی میٹر ہے۔"),
                     left="?")


def two_gardens():
    sc = Scale(7 + 2 + 5, 5, max_h=60, padx=10)
    a = rect_pts(sc, 0, 2, 7, 3)
    b = rect_pts(sc, 9, 0, 5, 5)
    ca, cb = centre(a), centre(b)
    items = [poly(a), poly(b)] + grid(sc, 0, 2, 7, 3) + grid(sc, 9, 0, 5, 5)
    items += [side(a[3], a[2], m(7), ca)]
    items += [side(a[0], a[3], m(3), ca), side(b[3], b[2], m(5), cb), side(b[1], b[2], m(5), cb)]
    return fig(sc.h, T("Two gardens drawn to scale on 1 m squares. Left: a rectangle 7 m long and 3 m wide, 3 rows of 7 squares. Right: a square 5 m by 5 m, 5 rows of 5 squares. Both have a perimeter of 20 m.",
                       "1 میٹر کے مربعوں پر پیمانے کے مطابق دو باغیچے۔ بائیں: 7 میٹر لمبی اور 3 میٹر چوڑی مستطیل، 7 مربعوں کی 3 قطاریں۔ دائیں: 5 ضرب 5 میٹر کا مربع، 5 مربعوں کی 5 قطاریں۔ دونوں کا احاطہ 20 میٹر ہے۔"), items)


F_GARDENS = two_gardens()
F_RABIA = rect_fig(5, 3, cm, rect_alt(5, 3, "cm", "سینٹی میٹر"))


def floor_tiles():
    sc = Scale(8, 6, max_h=60)
    p = rect_pts(sc, 0, 0, 8, 6)
    c = centre(p)
    items = [poly(p)] + grid(sc, 0, 0, 8, 6, rows=1, cols=1)
    items += [side(p[3], p[2], m(8), c), side(p[1], p[2], m(6), c)]
    return fig(sc.h, T("A floor 8 m long and 6 m wide, drawn to scale. The first row of 1 m tiles is drawn along the top (8 tiles) and the first column down the left side (6 tiles); the rest of the floor is still to be tiled the same way.",
                       "8 میٹر لمبا اور 6 میٹر چوڑا فرش، پیمانے کے مطابق۔ اوپر 1 میٹر ٹائلوں کی پہلی قطار (8 ٹائلیں) اور بائیں طرف پہلا کالم (6 ٹائلیں) بنا ہے؛ باقی فرش پر بھی اسی طرح ٹائلیں لگنی ہیں۔"), items)


F_TILES = floor_tiles()
F_QB = rect_fig(12, 5, cm, rect_alt(12, 5, "cm", "سینٹی میٹر"))
F_QB_ERR = square_fig(4, cm, "cm", "سینٹی میٹر", grid_lines=True)
F_R_RECT = rect_fig(9, 7, cm, rect_alt(9, 7, "cm", "سینٹی میٹر"))
F_R_SQUARE = square_fig(10, m, "m", "میٹر")

FIGS = {
    "s1_hook": F_RUG_GRID, "s3_squares": F_4BY3, "s4_count": F_4BY3, "s5_rug": F_RUG, "s6_square": F_SQUARE_9,
    "s7_missing": F_MISSING, "s8_same_perimeter": F_GARDENS, "s9_find_error": F_RABIA, "s11_tiles": F_TILES,
    "qb_apply": F_QB, "qb_find_error": F_QB_ERR, "r_rect": F_R_RECT, "r_square": F_R_SQUARE,
}


lesson = {
 "id": "g6-maths-08-area-of-rectangles",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Find the area of rectangles and squares in square units, and a missing side from the area.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Area of rectangles and squares", "مستطیل اور مربع کا رقبہ"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": PA_PERIMETER}],
 "misconceptions": [
   {"id": "perimeter_for_area", "description": "Adds the sides (the perimeter) when the area is asked."},
   {"id": "area_wrong_units", "description": "Writes area in cm or m instead of square units (cm², m²)."},
   {"id": "same_perimeter_same_area", "description": "Thinks shapes with the same perimeter must have the same area."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_units", "type": "recall", "step": {
     "id": "qb_units", "type": "choice",
     "prompt": T("Which unit is right for the area of a page?", "کسی صفحے کے رقبے کے لیے کون سی اکائی درست ہے؟"),
     "options": [
       opt("cm2", "cm² (square centimetres)", "مربع سینٹی میٹر (cm²)", True, "Yes! Area counts squares, so it uses square units.", "جی ہاں! رقبہ مربع گنتا ہے، اس لیے مربع اکائیاں۔"),
       opt("cm", "cm", "سینٹی میٹر", False, "cm measures a length. Area counts squares: cm².", "سینٹی میٹر لمبائی ناپتا ہے۔ رقبہ مربع گنتا ہے: cm²", "area_wrong_units"),
       opt("kg", "kg", "کلوگرام", False, "kg measures weight. Area uses square units: cm².", "کلوگرام وزن ناپتا ہے۔ رقبے کی اکائی مربع ہے: cm²"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("Find the area of a rectangle 12 cm long and 5 cm wide, in cm².", "12 سینٹی میٹر لمبی اور 5 سینٹی میٹر چوڑی مستطیل کا رقبہ مربع سینٹی میٹر میں معلوم کریں۔"),
     QB,
     T("Area = length × width.", "رقبہ = لمبائی × چوڑائی"),
     T("Right! 60 cm².", "درست! 60 مربع سینٹی میٹر"),
     T("12 × 5 = 60 cm².", "12 × 5 = 60 مربع سینٹی میٹر"),
     common_wrong=[wrong(34, "34 cm is the perimeter. Area = 12 × 5 = 60 cm².", "34 سینٹی میٹر احاطہ ہے۔ رقبہ = 12 × 5 = 60 مربع سینٹی میٹر", "perimeter_for_area"),
                   wrong(17, "Multiply, don't add: 12 × 5 = 60.", "جمع نہیں، ضرب: 12 × 5 = 60", "perimeter_for_area")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Talha writes: 'The area of a square with 4 cm sides is 16 cm.' What went wrong?", "طلحہ لکھتا ہے: '4 سینٹی میٹر ضلع والے مربع کا رقبہ 16 سینٹی میٹر ہے۔' کیا غلطی ہوئی؟"),
     "options": [
       opt("units", "The unit: area is 16 cm², square centimetres.", "اکائی: رقبہ 16 مربع سینٹی میٹر ہے۔", True,
           "Yes! The number is right; area counts squares, so cm².", "جی ہاں! عدد درست ہے؛ رقبہ مربع گنتا ہے، اس لیے cm²"),
       opt("number", "The number: it should be 8.", "عدد: یہ 8 ہونا چاہیے۔", False,
           "4 × 4 = 16 is right. Only the unit is wrong: cm².", "4 × 4 = 16 درست ہے۔ صرف اکائی غلط ہے: cm²"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "16 cm is a length. Area is 16 cm².", "16 سینٹی میٹر لمبائی ہے۔ رقبہ 16 مربع سینٹی میٹر ہے۔", "area_wrong_units"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_area", "front": T("Area of a rectangle?", "مستطیل کا رقبہ؟"),
    "back": T("Length × width, in square units. 6 m by 4 m: 24 m².", "لمبائی × چوڑائی، مربع اکائیوں میں۔ 6 میٹر ضرب 4 میٹر: 24 مربع میٹر")},
   {"id": "f_square", "front": T("Area of a square?", "مربع کا رقبہ؟"),
    "back": T("Side × side. Side 9 cm: 81 cm².", "ضلع × ضلع۔ ضلع 9 سینٹی میٹر: 81 مربع سینٹی میٹر")},
 ],
 "home_tasks": [{"id": "h_tiles", "text": T(
   "Find a floor or wall with square tiles. Count the tiles along one side and along the other. Multiply to find how many tiles there are, then count a few rows to check.",
   "کوئی فرش یا دیوار ڈھونڈیں جس پر مربع ٹائلیں ہوں۔ ایک طرف کی ٹائلیں اور دوسری طرف کی ٹائلیں گنیں۔ ضرب دے کر کل ٹائلیں نکالیں، پھر کچھ قطاریں گن کر جانچیں۔")}],
 "glossary": [T("Area", "رقبہ"), T("Square centimetre (cm²)", "مربع سینٹی میٹر")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Ammi wants a new rug for the room. Is it the distance around that matters, or the floor it covers?",
                     "امی کمرے کے لیے نیا قالین چاہتی ہیں۔ کیا گرد کا فاصلہ اہم ہے، یا وہ فرش جو قالین ڈھانپے گا؟"),
    "text": T("The space a flat shape covers is its area. First, a quick check on perimeter.", "کوئی چپٹی شکل جتنی جگہ گھیرتی ہے وہ اس کا رقبہ ہے۔ پہلے احاطے کا ایک سوال۔")},
   number_question(
     "s2_foundation",
     T("What is the perimeter of a rectangle 6 cm by 3 cm?", "6 ضرب 3 سینٹی میٹر مستطیل کا احاطہ کیا ہے؟"),
     18,
     T("6 + 3 + 6 + 3.", "6 + 3 + 6 + 3"),
     T("Right! 18 cm.", "درست! 18 سینٹی میٹر"),
     T("2 × (6 + 3) = 18 cm.", "2 × (6 + 3) = 18 سینٹی میٹر"),
     common_wrong=[wrong(9, "That is two sides. All four: 18 cm.", "یہ دو اضلاع ہیں۔ چاروں: 18 سینٹی میٹر")],
     qtype="recall", skill=PA_PERIMETER),
   {"id": "s3_squares", "type": "explain",
    "character": say("happy", "Area counts the little squares inside!", "رقبہ اندر کے چھوٹے مربع گنتا ہے!"),
    "text": T("Cover a rectangle 4 cm long and 3 cm wide with 1 cm squares: 3 rows of 4 squares. That is 4 × 3 = 12 squares, so the area is 12 square centimetres, written 12 cm². Area of a rectangle = length × width. Area of a square = side × side.",
              "4 سینٹی میٹر لمبی اور 3 سینٹی میٹر چوڑی مستطیل کو 1 سینٹی میٹر کے مربعوں سے ڈھانپیں: 4 مربعوں کی 3 قطاریں۔ یعنی 4 × 3 = 12 مربع، اس لیے رقبہ 12 مربع سینٹی میٹر ہے، جسے 12 cm² لکھتے ہیں۔ مستطیل کا رقبہ = لمبائی × چوڑائی۔ مربع کا رقبہ = ضلع × ضلع۔")},
   number_question(
     "s4_count",
     T("So how many 1 cm squares cover the 4 cm by 3 cm rectangle?", "تو 4 ضرب 3 سینٹی میٹر مستطیل کو 1 سینٹی میٹر کے کتنے مربع ڈھانپتے ہیں؟"),
     S4,
     T("3 rows of 4.", "4 کی 3 قطاریں"),
     T("Right! 12 squares: 12 cm².", "درست! 12 مربع: 12 مربع سینٹی میٹر"),
     T("4 × 3 = 12 squares.", "4 × 3 = 12 مربع"),
     common_wrong=[wrong(14, "14 cm is the perimeter, around the edge. Inside: 4 × 3 = 12.", "14 سینٹی میٹر احاطہ ہے، کنارے کے گرد۔ اندر: 4 × 3 = 12", "perimeter_for_area"),
                   wrong(7, "Multiply the rows and columns: 4 × 3 = 12.", "قطاریں اور کالم ضرب دیں: 4 × 3 = 12", "perimeter_for_area")]),
   number_question(
     "s5_rug",
     T("Ammi's rug is 6 m long and 4 m wide. What is its area in m²?", "امی کا قالین 6 میٹر لمبا اور 4 میٹر چوڑا ہے۔ اس کا رقبہ مربع میٹر میں کیا ہے؟"),
     S5,
     T("Length × width.", "لمبائی × چوڑائی"),
     T("Right! 24 m².", "درست! 24 مربع میٹر"),
     T("6 × 4 = 24 m².", "6 × 4 = 24 مربع میٹر"),
     common_wrong=[wrong(20, "20 m is the perimeter. Area = 6 × 4 = 24 m².", "20 میٹر احاطہ ہے۔ رقبہ = 6 × 4 = 24 مربع میٹر", "perimeter_for_area")]),
   number_question(
     "s6_square",
     T("A square has sides of 9 cm. What is its area in cm²?", "ایک مربع کا ضلع 9 سینٹی میٹر ہے۔ اس کا رقبہ مربع سینٹی میٹر میں کیا ہے؟"),
     S6,
     T("Side × side: 9 × 9.", "ضلع × ضلع: 9 × 9"),
     T("Right! 81 cm².", "درست! 81 مربع سینٹی میٹر"),
     T("9 × 9 = 81 cm².", "9 × 9 = 81 مربع سینٹی میٹر"),
     common_wrong=[wrong(36, "36 cm is the perimeter. Area = 9 × 9 = 81 cm².", "36 سینٹی میٹر احاطہ ہے۔ رقبہ = 9 × 9 = 81", "perimeter_for_area"),
                   wrong(18, "That is 9 × 2. Area of a square is 9 × 9 = 81.", "یہ 9 × 2 ہے۔ مربع کا رقبہ 9 × 9 = 81")]),
   number_question(
     "s7_missing",
     T("A rectangle has an area of 40 cm². Its length is 8 cm. How wide is it?", "ایک مستطیل کا رقبہ 40 مربع سینٹی میٹر ہے۔ اس کی لمبائی 8 سینٹی میٹر ہے۔ چوڑائی کتنی ہے؟"),
     S7,
     T("8 × width = 40.", "8 × چوڑائی = 40"),
     T("Right! 5 cm. Check: 8 × 5 = 40.", "درست! 5 سینٹی میٹر۔ جانچ: 8 × 5 = 40"),
     T("40 ÷ 8 = 5 cm.", "40 ÷ 8 = 5 سینٹی میٹر"),
     common_wrong=[wrong(32, "Divide, don't subtract: 40 ÷ 8 = 5.", "گھٹائیں نہیں، تقسیم کریں: 40 ÷ 8 = 5")]),
   number_question(
     "s8_same_perimeter",
     T("A 7 m by 3 m garden and a 5 m by 5 m garden both have a perimeter of 20 m. How many m² bigger is the square garden?", "7 ضرب 3 میٹر اور 5 ضرب 5 میٹر کے دونوں باغیچوں کا احاطہ 20 میٹر ہے۔ مربع باغیچہ کتنے مربع میٹر بڑا ہے؟"),
     S8,
     T("Find both areas: 5 × 5 and 7 × 3.", "دونوں رقبے نکالیں: 5 × 5 اور 7 × 3"),
     T("Right! 25 − 21 = 4 m². Same perimeter, different area!", "درست! 25 − 21 = 4 مربع میٹر۔ احاطہ ایک، رقبہ مختلف!"),
     T("5 × 5 = 25 and 7 × 3 = 21, so 25 − 21 = 4 m².", "5 × 5 = 25 اور 7 × 3 = 21، تو 25 − 21 = 4 مربع میٹر"),
     common_wrong=[wrong(0, "Same perimeter doesn't mean same area: 25 m² and 21 m². Difference: 4.", "ایک احاطے کا مطلب ایک رقبہ نہیں: 25 اور 21 مربع میٹر۔ فرق: 4", "same_perimeter_same_area")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Rabia says the area of a 5 cm by 3 cm rectangle is 16 cm². What went wrong?", "رابعہ کہتی ہے 5 ضرب 3 سینٹی میٹر مستطیل کا رقبہ 16 مربع سینٹی میٹر ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("perimeter", "She found the perimeter. Area = 5 × 3 = 15 cm².", "اس نے احاطہ نکالا۔ رقبہ = 5 × 3 = 15 مربع سینٹی میٹر", True,
          "Yes! 5 + 3 + 5 + 3 = 16 is the distance round. Inside: 15 squares.", "جی ہاں! 5 + 3 + 5 + 3 = 16 گرد کا فاصلہ ہے۔ اندر: 15 مربع۔"),
      opt("eight", "It should be 8 cm².", "یہ 8 مربع سینٹی میٹر ہونا چاہیے۔", False,
          "8 is 5 + 3. Area multiplies: 5 × 3 = 15.", "8 یعنی 5 + 3۔ رقبے میں ضرب: 5 × 3 = 15", "perimeter_for_area"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "16 cm is the perimeter. The area is 5 × 3 = 15 cm².", "16 سینٹی میٹر احاطہ ہے۔ رقبہ 5 × 3 = 15 مربع سینٹی میٹر ہے۔", "perimeter_for_area"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why does length × width give the area of a rectangle? Can you teach me?",
                     "لمبائی × چوڑائی سے مستطیل کا رقبہ کیوں نکلتا ہے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why do we multiply length by width to find the area of a rectangle?",
              "اپنے الفاظ میں بتائیں: مستطیل کا رقبہ نکالنے کے لیے لمبائی کو چوڑائی سے ضرب کیوں دیتے ہیں؟"),
    "key_idea": "Area counts the unit squares inside. The length tells how many squares fit in one row and the width tells how many rows there are, so the total is length × width.",
    "levels": {
      "got_it": "Explains that the rectangle is rows of unit squares: the length gives squares per row, the width gives the number of rows.",
      "partly": "Says area counts squares, without linking rows and columns to the multiplication.",
      "not_yet": "Confuses it with perimeter, or gives no reason."},
    "keywords": [
      ["square", "مربع", "murabba"],
      ["row", "rows", "قطار", "qataar"],
      ["inside", "cover", "اندر", "ڈھانپ"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Rows of squares: squares in a row × number of rows.", "بہت خوب! مربعوں کی قطاریں: ایک قطار کے مربع × قطاروں کی تعداد۔"),
      "partly": T("Good start! Now say how rows and columns of squares give a multiplication.", "اچھی شروعات! اب بتائیں مربعوں کی قطاروں اور کالموں سے ضرب کیسے بنتی ہے۔"),
      "not_yet": T("Picture the 4 by 3 rectangle: 3 rows of 4 squares. How many squares is that?", "4 ضرب 3 کی مستطیل سوچیں: 4 مربعوں کی 3 قطاریں۔ کل کتنے مربع ہوئے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_tiles",
     T("A floor is 8 m long and 6 m wide. Each tile covers 1 m². How many tiles are needed?", "ایک فرش 8 میٹر لمبا اور 6 میٹر چوڑا ہے۔ ہر ٹائل 1 مربع میٹر ڈھانپتی ہے۔ کتنی ٹائلیں چاہییں؟"),
     S11,
     T("The number of tiles is the area: 8 × 6.", "ٹائلوں کی تعداد رقبہ ہے: 8 × 6"),
     T("Right! 48 tiles.", "درست! 48 ٹائلیں"),
     T("8 × 6 = 48 m², so 48 tiles.", "8 × 6 = 48 مربع میٹر، یعنی 48 ٹائلیں"),
     common_wrong=[wrong(28, "28 m is the perimeter. Tiles cover the inside: 8 × 6 = 48.", "28 میٹر احاطہ ہے۔ ٹائلیں اندر ڈھانپتی ہیں: 8 × 6 = 48", "perimeter_for_area"),
                   wrong(14, "Multiply, don't add: 8 × 6 = 48.", "جمع نہیں، ضرب: 8 × 6 = 48")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Now you can measure the inside of a shape!", "اب آپ شکل کا اندر ناپ سکتے ہیں!"),
    "text": T("Area is the space a shape covers, counted in squares. Rectangle: length × width. Square: side × side. Write area in square units: cm², m². Shapes with the same perimeter can have different areas.",
              "رقبہ وہ جگہ ہے جو شکل ڈھانپتی ہے، مربعوں میں گنی جاتی ہے۔ مستطیل: لمبائی × چوڑائی۔ مربع: ضلع × ضلع۔ رقبہ مربع اکائیوں میں لکھیں: مربع سینٹی میٹر، مربع میٹر۔ ایک جیسے احاطے والی شکلوں کا رقبہ مختلف ہو سکتا ہے۔"),
    "points": [T("Perimeter goes around (cm); area covers inside (cm²).", "احاطہ گرد (سینٹی میٹر)؛ رقبہ اندر (مربع سینٹی میٹر)۔"),
               T("Missing side: area ÷ the side you know.", "نامعلوم ضلع: رقبہ ÷ معلوم ضلع۔")]},
 ],
 "review_questions": [
   {"id": "r_rect", "type": "apply", "skill": SKILL, "step": number_question(
     "r_rect",
     T("Find the area of a rectangle 9 cm by 7 cm, in cm².", "9 ضرب 7 سینٹی میٹر مستطیل کا رقبہ مربع سینٹی میٹر میں معلوم کریں۔"),
     R1,
     T("9 × 7.", "9 × 7"),
     T("Right! 63 cm².", "درست! 63 مربع سینٹی میٹر"),
     T("9 × 7 = 63 cm².", "9 × 7 = 63 مربع سینٹی میٹر"),
     common_wrong=[wrong(32, "32 cm is the perimeter. Area: 9 × 7 = 63.", "32 سینٹی میٹر احاطہ ہے۔ رقبہ: 9 × 7 = 63", "perimeter_for_area")],
     qtype=None)},
   {"id": "r_square", "type": "recall", "skill": SKILL, "step": number_question(
     "r_square",
     T("Find the area of a square with 10 m sides, in m².", "10 میٹر ضلع والے مربع کا رقبہ مربع میٹر میں معلوم کریں۔"),
     R2,
     T("10 × 10.", "10 × 10"),
     T("Right! 100 m².", "درست! 100 مربع میٹر"),
     T("10 × 10 = 100 m².", "10 × 10 = 100 مربع میٹر"),
     common_wrong=[wrong(40, "40 m is the perimeter. Area: 10 × 10 = 100.", "40 میٹر احاطہ ہے۔ رقبہ: 10 × 10 = 100", "perimeter_for_area")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Perimeter and Area unit. No textbook text or exercises were used.",
   "Area is introduced by counting unit squares in rows before the formula. Squared paper helps.",
   "Urdu terms to check: رقبہ (area), مربع سینٹی میٹر (square centimetre).",
   "The numbers were worked out in content/sources/g6-maths-08/area_rectangles.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
with_figures(lesson, FIGS)
write(lesson)
