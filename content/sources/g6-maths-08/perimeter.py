import math
from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, TIMES_TABLES, PA_PERIMETER)

SKILL = PA_PERIMETER


def rect_p(length, width):
    return 2 * (length + width)


# s2
assert 7 * 4 == 28
# s4: garden 8 by 5
S4 = rect_p(8, 5)
assert S4 == 26 == 8 + 5 + 8 + 5 and 8 + 5 == 13 and 8 * 5 == 40
# s5: square side 7
S5 = 4 * 7
assert S5 == 28 and 7 * 7 == 49
# s6: triangle 5, 6, 9
S6 = 5 + 6 + 9
assert S6 == 20
# s7: regular hexagon side 4
S7 = 6 * 4
assert S7 == 24 and 4 * 4 == 16
# s8: perimeter 30, length 9: width?
S8 = 30 // 2 - 9
assert S8 == 6 and rect_p(9, S8) == 30 and 30 - 9 == 21
# s9: 6 by 4
assert rect_p(6, 4) == 20 and 6 + 4 == 10
# s11: square with perimeter 36
S11 = 36 // 4
assert S11 == 9 and 4 * S11 == 36 and 36 - 4 == 32
# question bank and review
QB = rect_p(12, 3)
assert QB == 30 and 12 + 3 == 15 and 12 * 3 == 36
assert 4 * 5 == 20 and 5 * 5 == 25
R1 = rect_p(10, 4)
assert R1 == 28 and 10 * 4 == 40
R2 = 4 * 6
assert R2 == 24 and 6 * 6 == 36



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

def rect_alt(length, width, unit_en, unit_ur, what_en="A rectangle", what_ur="ایک مستطیل", all4=False):
    if all4:
        return T(f"{what_en}, {length} {unit_en} long and {width} {unit_en} wide, drawn to scale. All four sides are labelled: {length}, {width}, {length} and {width} {unit_en}.",
                 f"{what_ur}، {length} {unit_ur} لمبی اور {width} {unit_ur} چوڑی، پیمانے کے مطابق۔ چاروں اضلاع پر لمبائی لکھی ہے: {length}، {width}، {length} اور {width} {unit_ur}۔")
    return T(f"{what_en}, {length} {unit_en} long and {width} {unit_en} wide, drawn to scale. The long side is labelled {length} {unit_en} and the short side {width} {unit_en}.",
             f"{what_ur}، {length} {unit_ur} لمبی اور {width} {unit_ur} چوڑی، پیمانے کے مطابق۔ لمبے ضلع پر {length} {unit_ur} اور چھوٹے ضلع پر {width} {unit_ur} لکھا ہے۔")


def square_fig(n, unit, unit_en, unit_ur, text=None):
    t = unit(n) if text is None else text
    word_en = f"{n} {unit_en}" if text is None else "an unknown length, marked ?"
    word_ur = f"{n} {unit_ur}" if text is None else "نامعلوم لمبائی، ? سے دکھائی گئی"
    return rect_fig(n, n, unit, T(f"A square. Each of its four equal sides is labelled {word_en}.",
                                  f"ایک مربع۔ اس کے چاروں برابر اضلاع میں سے ہر ایک پر {word_ur} لکھا ہے۔"),
                    sides=4, top=t, left=t)


F_GARDEN_HOOK = rect_fig(8, 5, m, rect_alt(8, 5, "m", "میٹر", "Dada's garden, a rectangle", "دادا کا باغیچہ، ایک مستطیل"))
F_GARDEN = rect_fig(8, 5, m, rect_alt(8, 5, "m", "میٹر", "Dada's garden, a rectangle", "دادا کا باغیچہ، ایک مستطیل", all4=True), sides=4)


def explain_fig():
    """A rectangle with sides l, w, l, w and a square with sides s."""
    sc = Scale(14, 4, max_h=56)
    rect = rect_pts(sc, 0, 0, 7, 4)
    sq = rect_pts(sc, 10, 0, 4, 4)
    cr, cs = centre(rect), centre(sq)
    items = [poly(rect), poly(sq)]
    items += [side(rect[0], rect[1], "L", cr), side(rect[3], rect[2], "L", cr),
              side(rect[1], rect[2], "W", cr), side(rect[0], rect[3], "W", cr)]
    items += [side(sq[i], sq[(i + 1) % 4], "S", cs) for i in range(4)]
    return fig(sc.h, T("Left: a rectangle with its two long sides marked L (length) and its two short sides marked W (width). Right: a square with all four sides marked S (side).",
                       "بائیں: ایک مستطیل جس کے دونوں لمبے اضلاع پر L (لمبائی) اور دونوں چھوٹے اضلاع پر W (چوڑائی) لکھا ہے۔ دائیں: ایک مربع جس کے چاروں اضلاع پر S (ضلع) لکھا ہے۔"), items)


F_EXPLAIN = explain_fig()


def triangle_fig(a, b, c):
    """Triangle with base c and the other sides a (left) and b (right), to scale."""
    x = (a * a - b * b + c * c) / (2 * c)
    y = math.sqrt(a * a - x * x)
    sc = Scale(c, y, max_h=56)
    p = [sc(0, y), sc(c, y), sc(x, 0)]
    k = centre(p)
    items = [poly(p), side(p[0], p[1], cm(c), k), side(p[0], p[2], cm(a), k), side(p[1], p[2], cm(b), k)]
    return fig(sc.h, T(f"A triangle drawn to scale. Its sides are labelled {a} cm, {b} cm and {c} cm; the {c} cm side is along the bottom.",
                       f"پیمانے کے مطابق ایک مثلث۔ اس کے اضلاع پر {a}، {b} اور {c} سینٹی میٹر لکھا ہے؛ {c} سینٹی میٹر والا ضلع نیچے ہے۔"), items)


def hexagon_fig(s):
    pts = [(s + s * math.cos(math.radians(60 * k)), s * math.sqrt(3) / 2 + s * math.sin(math.radians(60 * k))) for k in range(6)]
    sc = Scale(2 * s, s * math.sqrt(3), max_h=66, padx=18, pady=10)
    p = [sc(*q) for q in pts]
    k = centre(p)
    items = [poly(p)] + [side(p[i], p[(i + 1) % 6], cm(s), k, gap=1) for i in range(6)]
    return fig(sc.h, T(f"A regular hexagon: six equal sides, each labelled {s} cm.",
                       f"ایک باقاعدہ مسدس: چھ برابر اضلاع، ہر ایک پر {s} سینٹی میٹر لکھا ہے۔"), items)


F_TRIANGLE = triangle_fig(5, 6, 9)
F_HEXAGON = hexagon_fig(4)
F_MISSING = rect_fig(9, S8, cm, T(f"A rectangle drawn to scale. Its long side is labelled 9 cm. Its short side is marked ? because we must find it. The perimeter, all the way round, is 30 cm.",
                                  f"پیمانے کے مطابق ایک مستطیل۔ لمبے ضلع پر 9 سینٹی میٹر لکھا ہے۔ چھوٹے ضلع پر ? ہے کیونکہ وہ معلوم کرنا ہے۔ پورے گرد کا فاصلہ (احاطہ) 30 سینٹی میٹر ہے۔"),
                     sides=4, left="?")
F_AYAN = rect_fig(6, 4, cm, rect_alt(6, 4, "cm", "سینٹی میٹر", all4=True), sides=4)
F_SQUARE_7 = square_fig(7, cm, "cm", "سینٹی میٹر")
F_SQUARE_36 = square_fig(S11, cm, "cm", "سینٹی میٹر", text="?")
F_QB = rect_fig(12, 3, cm, rect_alt(12, 3, "cm", "سینٹی میٹر"))
F_QB_ERR = square_fig(5, cm, "cm", "سینٹی میٹر")
F_R_RECT = rect_fig(10, 4, m, rect_alt(10, 4, "m", "میٹر"))
F_R_SQUARE = square_fig(6, cm, "cm", "سینٹی میٹر")

FIGS = {
    "s1_hook": F_GARDEN_HOOK, "s3_around": F_EXPLAIN, "s4_garden": F_GARDEN, "s5_square": F_SQUARE_7,
    "s6_triangle": F_TRIANGLE, "s7_hexagon": F_HEXAGON, "s8_missing": F_MISSING, "s9_find_error": F_AYAN,
    "s11_square_side": F_SQUARE_36, "qb_apply": F_QB, "qb_find_error": F_QB_ERR,
    "r_rect": F_R_RECT, "r_square": F_R_SQUARE,
}


lesson = {
 "id": "g6-maths-08-perimeter",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Find the perimeter of rectangles, squares and other polygons, and a missing side from the perimeter.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Perimeter", "احاطہ"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": TIMES_TABLES}],
 "misconceptions": [
   {"id": "two_sides_only", "description": "Adds only the two sides given (length + width) instead of all four."},
   {"id": "area_for_perimeter", "description": "Multiplies length by width (the area) when the perimeter is asked."},
   {"id": "missing_side_subtract", "description": "Finds a missing side by taking one side from the whole perimeter, forgetting there are two of each."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_meaning", "type": "recall", "step": {
     "id": "qb_meaning", "type": "choice",
     "prompt": T("What is the perimeter of a shape?", "کسی شکل کا احاطہ کیا ہوتا ہے؟"),
     "options": [
       opt("around", "The distance all the way around its edge.", "اس کے کنارے کے گرد پورا فاصلہ۔", True, "Yes! Add up the lengths of all the sides.", "جی ہاں! تمام اضلاع کی لمبائیاں جمع کریں۔"),
       opt("inside", "The space inside it.", "اس کے اندر کی جگہ۔", False, "That is the area. Perimeter is the distance around.", "یہ رقبہ ہے۔ احاطہ گرد کا فاصلہ ہے۔", "area_for_perimeter"),
       opt("long", "Its longest side.", "اس کا سب سے لمبا ضلع۔", False, "Perimeter uses every side, all the way around.", "احاطے میں ہر ضلع آتا ہے، پورے گرد۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("Find the perimeter of a rectangle 12 cm long and 3 cm wide.", "12 سینٹی میٹر لمبی اور 3 سینٹی میٹر چوڑی مستطیل کا احاطہ معلوم کریں۔"),
     QB,
     T("Add all four sides: 12 + 3 + 12 + 3.", "چاروں اضلاع جمع کریں: 12 + 3 + 12 + 3"),
     T("Right! 30 cm.", "درست! 30 سینٹی میٹر"),
     T("2 × (12 + 3) = 2 × 15 = 30 cm.", "2 × (12 + 3) = 2 × 15 = 30 سینٹی میٹر"),
     common_wrong=[wrong(15, "That is two sides. A rectangle has four: 30 cm.", "یہ دو اضلاع ہیں۔ مستطیل کے چار ہیں: 30 سینٹی میٹر", "two_sides_only"),
                   wrong(36, "12 × 3 is the area. Perimeter adds the sides: 30 cm.", "12 × 3 رقبہ ہے۔ احاطے میں اضلاع جمع ہوتے ہیں: 30 سینٹی میٹر", "area_for_perimeter")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Maryam says a square with 5 cm sides has a perimeter of 25 cm. What went wrong?", "مریم کہتی ہے 5 سینٹی میٹر ضلع والے مربع کا احاطہ 25 سینٹی میٹر ہے۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("area", "She found the area. Perimeter = 4 × 5 = 20 cm.", "اس نے رقبہ نکالا۔ احاطہ = 4 × 5 = 20 سینٹی میٹر", True,
           "Yes! 5 × 5 is the area. Around the edge is 5 + 5 + 5 + 5 = 20.", "جی ہاں! 5 × 5 رقبہ ہے۔ کنارے کے گرد 5 + 5 + 5 + 5 = 20"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "Add the four sides: 5 + 5 + 5 + 5 = 20 cm. 25 is the area.", "چاروں اضلاع جمع کریں: 5 + 5 + 5 + 5 = 20 سینٹی میٹر۔ 25 رقبہ ہے۔", "area_for_perimeter"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_rect", "front": T("Perimeter of a rectangle?", "مستطیل کا احاطہ؟"),
    "back": T("Add all four sides, or 2 × (length + width). 8 m by 5 m: 26 m.", "چاروں اضلاع جمع کریں، یا 2 × (لمبائی + چوڑائی)۔ 8 میٹر ضرب 5 میٹر: 26 میٹر")},
   {"id": "f_square", "front": T("Perimeter of a square?", "مربع کا احاطہ؟"),
    "back": T("4 × side. Side 7 cm: 28 cm.", "4 × ضلع۔ ضلع 7 سینٹی میٹر: 28 سینٹی میٹر")},
 ],
 "home_tasks": [{"id": "h_measure", "text": T(
   "With a ruler or a piece of string, measure the sides of a book, a table top and a door. Work out the perimeter of each. Which is the biggest?",
   "فٹے یا دھاگے سے کسی کتاب، میز کی سطح اور دروازے کے اضلاع ناپیں۔ ہر ایک کا احاطہ نکالیں۔ سب سے بڑا کون سا ہے؟")}],
 "glossary": [T("Perimeter", "احاطہ"), T("Rectangle", "مستطیل"), T("Square", "مربع")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Dada's vegetable garden is 8 m long and 5 m wide. How much fence does he need to go all the way round?",
                     "دادا کا سبزیوں کا باغیچہ 8 میٹر لمبا اور 5 میٹر چوڑا ہے۔ چاروں طرف باڑ کے لیے کتنی تار چاہیے؟"),
    "text": T("The distance around a shape is called its perimeter. First, a quick times-table check.", "کسی شکل کے گرد کے فاصلے کو اس کا احاطہ کہتے ہیں۔ پہلے پہاڑے کا ایک سوال۔")},
   number_question(
     "s2_foundation",
     T("What is 7 × 4?", "7 × 4 کتنا ہے؟"),
     28,
     T("Four sevens: 7, 14, 21 ...", "چار دفعہ سات: 7، 14، 21 ..."),
     T("Right! 28.", "درست! 28"),
     T("7 × 4 = 28.", "7 × 4 = 28"),
     common_wrong=[wrong(11, "That is 7 + 4. Multiply: 28.", "یہ 7 + 4 ہے۔ ضرب دیں: 28")],
     qtype="recall", skill=TIMES_TABLES),
   {"id": "s3_around", "type": "explain",
    "character": say("happy", "Walk all the way round and add every side!", "پورا چکر لگائیں اور ہر ضلع جمع کریں!"),
    "text": T("Perimeter = the lengths of all the sides added together. A rectangle has two lengths and two widths, so perimeter = length + width + length + width = 2 × (length + width). A square has four equal sides, so perimeter = 4 × side.",
              "احاطہ = تمام اضلاع کی لمبائیوں کا مجموعہ۔ مستطیل کی دو لمبائیاں اور دو چوڑائیاں ہوتی ہیں، اس لیے احاطہ = لمبائی + چوڑائی + لمبائی + چوڑائی = 2 × (لمبائی + چوڑائی)۔ مربع کے چار برابر اضلاع ہیں، اس لیے احاطہ = 4 × ضلع۔")},
   number_question(
     "s4_garden",
     T("Dada's garden is 8 m long and 5 m wide. How many metres of fence go all the way round?", "دادا کا باغیچہ 8 میٹر لمبا اور 5 میٹر چوڑا ہے۔ چاروں طرف کتنے میٹر باڑ لگے گی؟"),
     S4,
     T("8 + 5 + 8 + 5.", "8 + 5 + 8 + 5"),
     T("Right! 26 m of fence.", "درست! 26 میٹر باڑ"),
     T("2 × (8 + 5) = 2 × 13 = 26 m.", "2 × (8 + 5) = 2 × 13 = 26 میٹر"),
     common_wrong=[wrong(13, "That covers only two sides. Go all the way round: 26 m.", "یہ صرف دو اضلاع ہیں۔ پورا چکر: 26 میٹر", "two_sides_only"),
                   wrong(40, "8 × 5 is the area. Fence goes around: 26 m.", "8 × 5 رقبہ ہے۔ باڑ گرد لگتی ہے: 26 میٹر", "area_for_perimeter")]),
   number_question(
     "s5_square",
     T("A square tile has sides of 7 cm. What is its perimeter?", "ایک مربع ٹائل کا ہر ضلع 7 سینٹی میٹر ہے۔ اس کا احاطہ کیا ہے؟"),
     S5,
     T("Four equal sides: 4 × 7.", "چار برابر اضلاع: 4 × 7"),
     T("Right! 28 cm.", "درست! 28 سینٹی میٹر"),
     T("4 × 7 = 28 cm.", "4 × 7 = 28 سینٹی میٹر"),
     common_wrong=[wrong(49, "7 × 7 is the area. Perimeter: 4 × 7 = 28 cm.", "7 × 7 رقبہ ہے۔ احاطہ: 4 × 7 = 28 سینٹی میٹر", "area_for_perimeter"),
                   wrong(14, "A square has four sides, not two: 28 cm.", "مربع کے دو نہیں، چار اضلاع ہیں: 28 سینٹی میٹر", "two_sides_only")]),
   number_question(
     "s6_triangle",
     T("A triangle has sides of 5 cm, 6 cm and 9 cm. What is its perimeter?", "ایک مثلث کے اضلاع 5، 6 اور 9 سینٹی میٹر ہیں۔ اس کا احاطہ کیا ہے؟"),
     S6,
     T("Add the three sides.", "تینوں اضلاع جمع کریں۔"),
     T("Right! 20 cm.", "درست! 20 سینٹی میٹر"),
     T("5 + 6 + 9 = 20 cm.", "5 + 6 + 9 = 20 سینٹی میٹر"),
     common_wrong=[wrong(270, "Perimeter adds, it doesn't multiply: 5 + 6 + 9 = 20.", "احاطے میں ضرب نہیں، جمع: 5 + 6 + 9 = 20")]),
   number_question(
     "s7_hexagon",
     T("A regular hexagon has 6 equal sides of 4 cm. What is its perimeter?", "ایک باقاعدہ مسدس کے 6 برابر اضلاع 4 سینٹی میٹر کے ہیں۔ اس کا احاطہ کیا ہے؟"),
     S7,
     T("6 sides of 4 cm: 6 × 4.", "4 سینٹی میٹر کے 6 اضلاع: 6 × 4"),
     T("Right! 24 cm.", "درست! 24 سینٹی میٹر"),
     T("6 × 4 = 24 cm.", "6 × 4 = 24 سینٹی میٹر"),
     common_wrong=[wrong(16, "A hexagon has 6 sides, not 4: 6 × 4 = 24.", "مسدس کے 4 نہیں، 6 اضلاع ہیں: 6 × 4 = 24")]),
   number_question(
     "s8_missing",
     T("A rectangle has a perimeter of 30 cm. Its length is 9 cm. How wide is it?", "ایک مستطیل کا احاطہ 30 سینٹی میٹر ہے۔ اس کی لمبائی 9 سینٹی میٹر ہے۔ چوڑائی کتنی ہے؟"),
     S8,
     T("Half the perimeter is one length + one width: 15 cm.", "آدھا احاطہ = ایک لمبائی + ایک چوڑائی: 15 سینٹی میٹر"),
     T("Right! 6 cm. Check: 9 + 6 + 9 + 6 = 30.", "درست! 6 سینٹی میٹر۔ جانچ: 9 + 6 + 9 + 6 = 30"),
     T("30 ÷ 2 = 15, and 15 − 9 = 6 cm.", "30 ÷ 2 = 15، اور 15 − 9 = 6 سینٹی میٹر"),
     common_wrong=[wrong(21, "There are two lengths: 30 ÷ 2 = 15, then 15 − 9 = 6.", "دو لمبائیاں ہیں: 30 ÷ 2 = 15، پھر 15 − 9 = 6", "missing_side_subtract"),
                   wrong(12, "Take away both lengths: 30 − 9 − 9 = 12 is two widths. One width: 6.", "دونوں لمبائیاں گھٹائیں: 30 − 9 − 9 = 12 دو چوڑائیاں ہیں۔ ایک چوڑائی: 6")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Ayan says a rectangle 6 cm by 4 cm has a perimeter of 10 cm. What went wrong?", "ایان کہتا ہے 6 ضرب 4 سینٹی میٹر کی مستطیل کا احاطہ 10 سینٹی میٹر ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("two", "He added only two sides. All four: 20 cm.", "اس نے صرف دو اضلاع جمع کیے۔ چاروں: 20 سینٹی میٹر", True,
          "Yes! 6 + 4 + 6 + 4 = 20.", "جی ہاں! 6 + 4 + 6 + 4 = 20"),
      opt("area", "It should be 24 cm, 6 × 4.", "یہ 24 سینٹی میٹر ہونا چاہیے، 6 × 4", False,
          "6 × 4 is the area. Perimeter: 6 + 4 + 6 + 4 = 20.", "6 × 4 رقبہ ہے۔ احاطہ: 6 + 4 + 6 + 4 = 20", "area_for_perimeter"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "A rectangle has four sides: 6 + 4 + 6 + 4 = 20 cm.", "مستطیل کے چار اضلاع ہیں: 6 + 4 + 6 + 4 = 20 سینٹی میٹر", "two_sides_only"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why is a rectangle's perimeter 2 × (length + width)? Can you teach me?",
                     "مستطیل کا احاطہ 2 × (لمبائی + چوڑائی) کیوں ہوتا ہے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why can we find a rectangle's perimeter with 2 × (length + width)?",
              "اپنے الفاظ میں بتائیں: مستطیل کا احاطہ 2 × (لمبائی + چوڑائی) سے کیوں نکل آتا ہے؟"),
    "key_idea": "A rectangle has two equal lengths and two equal widths. Going round once means one length + one width, twice. So perimeter = 2 × (length + width).",
    "levels": {
      "got_it": "Explains that opposite sides are equal, so there are two lengths and two widths, which is 2 × (length + width).",
      "partly": "Says you add the sides, without explaining where the 2 comes from.",
      "not_yet": "Confuses it with area, or gives no reason."},
    "keywords": [
      ["two", "twice", "دو", "do"],
      ["opposite", "equal", "same", "برابر", "آمنے سامنے"],
      ["length", "width", "لمبائی", "چوڑائی"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Two lengths and two widths make 2 × (length + width).", "بہت خوب! دو لمبائیاں اور دو چوڑائیاں مل کر 2 × (لمبائی + چوڑائی)۔"),
      "partly": T("Good start! Now say why we multiply by 2: how many lengths does a rectangle have?", "اچھی شروعات! اب بتائیں 2 سے ضرب کیوں: مستطیل کی کتنی لمبائیاں ہیں؟"),
      "not_yet": T("Walk round Dada's garden: 8, 5, 8, 5. Which numbers repeat?", "دادا کے باغیچے کا چکر لگائیں: 8، 5، 8، 5۔ کون سے اعداد دہرائے گئے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_square_side",
     T("A square has a perimeter of 36 cm. How long is each side?", "ایک مربع کا احاطہ 36 سینٹی میٹر ہے۔ ہر ضلع کتنا لمبا ہے؟"),
     S11,
     T("4 equal sides make 36: 36 ÷ 4.", "4 برابر اضلاع مل کر 36: 36 ÷ 4"),
     T("Right! 9 cm. Check: 4 × 9 = 36.", "درست! 9 سینٹی میٹر۔ جانچ: 4 × 9 = 36"),
     T("36 ÷ 4 = 9 cm.", "36 ÷ 4 = 9 سینٹی میٹر"),
     common_wrong=[wrong(6, "6 × 6 = 36 is the area of a 6 cm square. Perimeter ÷ 4: 9 cm.", "6 × 6 = 36 تو 6 سینٹی میٹر مربع کا رقبہ ہے۔ احاطہ ÷ 4: 9 سینٹی میٹر", "area_for_perimeter"),
                   wrong(32, "Divide by 4, don't subtract: 36 ÷ 4 = 9.", "4 سے تقسیم کریں، گھٹائیں نہیں: 36 ÷ 4 = 9")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "You can measure all the way round now!", "اب آپ پورا گرد ناپ سکتے ہیں!"),
    "text": T("Perimeter is the distance around a shape: add all its sides. Rectangle: 2 × (length + width). Square: 4 × side. To find a missing side of a rectangle, halve the perimeter, then take away the side you know.",
              "احاطہ کسی شکل کے گرد کا فاصلہ ہے: تمام اضلاع جمع کریں۔ مستطیل: 2 × (لمبائی + چوڑائی)۔ مربع: 4 × ضلع۔ مستطیل کا نامعلوم ضلع نکالنے کے لیے احاطہ آدھا کریں، پھر معلوم ضلع گھٹائیں۔"),
    "points": [T("Count every side, not just two.", "ہر ضلع گنیں، صرف دو نہیں۔"),
               T("Perimeter is in cm or m, not cm².", "احاطہ سینٹی میٹر یا میٹر میں ہوتا ہے، مربع سینٹی میٹر میں نہیں۔")]},
 ],
 "review_questions": [
   {"id": "r_rect", "type": "apply", "skill": SKILL, "step": number_question(
     "r_rect",
     T("Find the perimeter of a rectangle 10 m long and 4 m wide.", "10 میٹر لمبی اور 4 میٹر چوڑی مستطیل کا احاطہ معلوم کریں۔"),
     R1,
     T("2 × (10 + 4).", "2 × (10 + 4)"),
     T("Right! 28 m.", "درست! 28 میٹر"),
     T("2 × 14 = 28 m.", "2 × 14 = 28 میٹر"),
     common_wrong=[wrong(14, "That is two sides. All four: 28 m.", "یہ دو اضلاع ہیں۔ چاروں: 28 میٹر", "two_sides_only"),
                   wrong(40, "10 × 4 is the area. Perimeter: 28 m.", "10 × 4 رقبہ ہے۔ احاطہ: 28 میٹر", "area_for_perimeter")],
     qtype=None)},
   {"id": "r_square", "type": "recall", "skill": SKILL, "step": number_question(
     "r_square",
     T("Find the perimeter of a square with 6 cm sides.", "6 سینٹی میٹر ضلع والے مربع کا احاطہ معلوم کریں۔"),
     R2,
     T("4 × 6.", "4 × 6"),
     T("Right! 24 cm.", "درست! 24 سینٹی میٹر"),
     T("4 × 6 = 24 cm.", "4 × 6 = 24 سینٹی میٹر"),
     common_wrong=[wrong(36, "6 × 6 is the area. Perimeter: 4 × 6 = 24.", "6 × 6 رقبہ ہے۔ احاطہ: 4 × 6 = 24", "area_for_perimeter")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Perimeter and Area unit. No textbook text or exercises were used.",
   "Most steps show the shape drawn to scale with its side lengths. Drawing each shape on the board helps too.",
   "Urdu terms to check: احاطہ (perimeter), مستطیل (rectangle), مربع (square), مسدس (hexagon).",
   "The numbers were worked out in content/sources/g6-maths-08/perimeter.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
with_figures(lesson, FIGS)
write(lesson)
