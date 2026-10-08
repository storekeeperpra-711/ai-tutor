import math
from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, PA_AREA, PA_COMPOUND)

SKILL = PA_COMPOUND

# s2
assert 7 * 5 == 35
# s4: L-shaped room = 6 by 4 and 3 by 2
S4 = 6 * 4 + 3 * 2
assert S4 == 30 and 6 * 4 == 24 and (6 * 4) * (3 * 2) == 144
# s5: garden 10 by 8 with a 3 by 2 pond
S5 = 10 * 8 - 3 * 2
assert S5 == 74 and 10 * 8 + 3 * 2 == 86 and 10 * 8 == 80
# s6: T shape = 9 by 2 bar + 3 by 5 stem
S6 = 9 * 2 + 3 * 5
assert S6 == 33
# s7: wall 5 by 3 with a 1 by 2 door
S7 = 5 * 3 - 1 * 2
assert S7 == 13 and 5 * 3 == 15
# s8: frame 8 by 6 around a 6 by 4 picture
S8 = 8 * 6 - 6 * 4
assert S8 == 24 and 8 * 6 == 48
# s11: 8 by 5 with a 3 by 2 corner cut out; splitting gives the same
S11 = 8 * 5 - 3 * 2
assert S11 == 34 == 5 * 5 + 3 * 3  # left part 5 by 5, right part 3 wide by 3 tall
# question bank and review
QB = 5 * 4 + 2 * 3
assert QB == 26 and 5 * 4 - 2 * 3 == 14
R1 = 7 * 3 + 4 * 2
assert R1 == 29
R2 = 12 * 10 - 4 * 3
assert R2 == 108 and 12 * 10 == 120



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

def l_shape(a_w, a_h, b_w, b_h, unit, alt, labels=True, split=True, complete=False, max_h=64):
    """An a_w by a_h rectangle with a b_w by b_h rectangle joined under its
    left end (an L lying down), to scale. split: a dashed line between the
    two parts; complete: the dashed missing piece that makes the big
    rectangle around the shape."""
    sc = Scale(a_w, a_h + b_h, max_h=max_h)
    outline = [sc(0, 0), sc(a_w, 0), sc(a_w, a_h), sc(b_w, a_h), sc(b_w, a_h + b_h), sc(0, a_h + b_h)]
    ca, cb = centre(rect_pts(sc, 0, 0, a_w, a_h)), centre(rect_pts(sc, 0, a_h, b_w, b_h))
    items = [poly(outline)]
    if split:
        items.append(seg(sc(0, a_h), sc(b_w, a_h), dashed=True))
    if complete:
        items.append(poly([sc(b_w, a_h), sc(a_w, a_h), sc(a_w, a_h + b_h), sc(b_w, a_h + b_h)], fill=False, dashed=True))
    if labels:
        items += [side(outline[0], outline[1], unit(a_w), ca), side(outline[1], outline[2], unit(a_h), ca),
                  side(outline[4], outline[5], unit(b_w), cb), side(outline[5], sc(0, a_h), unit(b_h), cb)]
    return fig(sc.h, alt, items)


def l_alt(a_w, a_h, b_w, b_h, unit_en, unit_ur, what_en, what_ur):
    return T(f"{what_en} shaped like an L, drawn to scale: a {a_w} {unit_en} by {a_h} {unit_en} rectangle on top, with a {b_w} {unit_en} by {b_h} {unit_en} rectangle joined under its left end. A dashed line separates the two rectangles. The sides are labelled {a_w}, {a_h}, {b_w} and {b_h} {unit_en}.",
             f"L شکل کا {what_ur}، پیمانے کے مطابق: اوپر {a_w} ضرب {a_h} {unit_ur} کی مستطیل، اور اس کے بائیں سرے کے نیچے {b_w} ضرب {b_h} {unit_ur} کی مستطیل جڑی ہے۔ ڈیش والی لکیر دونوں مستطیلوں کو الگ کرتی ہے۔ اضلاع پر {a_w}، {a_h}، {b_w} اور {b_h} {unit_ur} لکھا ہے۔")


F_HOOK = l_shape(6, 4, 3, 2, m, T("The floor of a room shaped like the letter L lying down: a wide part on top and a smaller part sticking out below its left end.",
                                  "لیٹے ہوئے L حرف جیسا کمرے کا فرش: اوپر چوڑا حصہ اور اس کے بائیں سرے کے نیچے نکلا ہوا چھوٹا حصہ۔"),
                 labels=False, split=False)


def two_ways():
    """Way 1 (split) beside way 2 (fill in the missing piece), same L."""
    sc = Scale(6 + 2 + 6, 6, max_h=52, padx=6)
    items = []
    for dx, way in ((0, 1), (8, 2)):
        o = [sc(dx, 0), sc(dx + 6, 0), sc(dx + 6, 4), sc(dx + 3, 4), sc(dx + 3, 6), sc(dx, 6)]
        items.append(poly(o))
        if way == 1:
            items.append(seg(sc(dx, 4), sc(dx + 3, 4), dashed=True))
        else:
            items.append(poly([sc(dx + 3, 4), sc(dx + 6, 4), sc(dx + 6, 6), sc(dx + 3, 6)], fill=False, dashed=True))
    items += [label(sc(1.5, 2), "1"), label(sc(1.5, 5), "2"), label(sc(11, 2), "3")]
    return fig(sc.h, T("Two copies of the same L-shape. Left (way 1): a dashed line splits it into two rectangles, numbered 1 and 2; add their areas. Right (way 2): a dashed outline fills in the missing corner to make one big rectangle, numbered 3; take the missing piece away from it.",
                       "ایک ہی L شکل کی دو کاپیاں۔ بائیں (طریقہ 1): ڈیش والی لکیر اسے دو مستطیلوں میں بانٹتی ہے، نمبر 1 اور 2؛ ان کے رقبے جمع کریں۔ دائیں (طریقہ 2): ڈیش والا خاکہ خالی کونا بھر کر ایک بڑی مستطیل بناتا ہے، نمبر 3؛ اس میں سے خالی حصہ گھٹائیں۔"), items)


F_TWO_WAYS = two_ways()
F_L_ROOM = l_shape(6, 4, 3, 2, m, l_alt(6, 4, 3, 2, "m", "میٹر", "Our room", "ہمارا کمرہ"))


def hole_fig(big_w, big_h, hole_w, hole_h, hx, hy, unit, alt, max_h=64):
    """A big rectangle, shaded, with a dashed hole (pond, door, bed) in it."""
    sc = Scale(big_w, big_h, max_h=max_h)
    p = rect_pts(sc, 0, 0, big_w, big_h)
    q = rect_pts(sc, hx, hy, hole_w, hole_h)
    c, cq = centre(p), centre(q)
    items = [poly(p), poly(q, fill=False, dashed=True)]
    items += [side(p[3], p[2], unit(big_w), c), side(p[1], p[2], unit(big_h), c)]
    # The hole's sizes go just outside it, inside the big rectangle.
    items += [side(q[0], q[1], unit(hole_w), cq), side(q[0], q[3], unit(hole_h), cq)]
    return fig(sc.h, alt, items)


def hole_alt(big_w, big_h, hole_w, hole_h, unit_en, unit_ur, big_en, big_ur, hole_en, hole_ur):
    return T(f"{big_en}, {big_w} {unit_en} by {big_h} {unit_en}, shaded and drawn to scale. Inside it, {hole_en} {hole_w} {unit_en} by {hole_h} {unit_en} is marked with a dashed outline.",
             f"{big_ur}، {big_w} ضرب {big_h} {unit_ur}، رنگا ہوا اور پیمانے کے مطابق۔ اس کے اندر {hole_w} ضرب {hole_h} {unit_ur} کا {hole_ur} ڈیش والے خاکے سے دکھایا گیا ہے۔")


F_POND = hole_fig(10, 8, 3, 2, 6, 2.2, m, hole_alt(10, 8, 3, 2, "m", "میٹر", "A garden", "ایک باغیچہ", "a pond", "تالاب"))


def t_shape():
    sc = Scale(9, 7, max_h=64)
    o = [sc(0, 0), sc(9, 0), sc(9, 2), sc(6, 2), sc(6, 7), sc(3, 7), sc(3, 2), sc(0, 2)]
    cbar, cstem = centre(rect_pts(sc, 0, 0, 9, 2)), centre(rect_pts(sc, 3, 2, 3, 5))
    items = [poly(o), seg(sc(3, 2), sc(6, 2), dashed=True),
             side(o[0], o[1], cm(9), cbar), side(o[1], o[2], cm(2), cbar),
             side(o[4], o[5], cm(3), cstem), side(o[3], o[4], cm(5), cstem)]
    return fig(sc.h, T("A T-shaped sign drawn to scale: a bar 9 cm long and 2 cm high on top, and a stem 3 cm wide and 5 cm high under its middle. A dashed line separates the bar from the stem.",
                       "پیمانے کے مطابق T شکل کا نشان: اوپر 9 سینٹی میٹر لمبی اور 2 سینٹی میٹر اونچی پٹی، اور اس کے بیچ کے نیچے 3 سینٹی میٹر چوڑا اور 5 سینٹی میٹر اونچا تنا۔ ڈیش والی لکیر پٹی کو تنے سے الگ کرتی ہے۔"), items)


F_T = t_shape()
F_WALL = hole_fig(5, 3, 1, 2, 2, 1, m, hole_alt(5, 3, 1, 2, "m", "میٹر", "A wall", "ایک دیوار", "a door", "دروازہ"))


def frame_fig():
    sc = Scale(8, 6, max_h=60)
    p = rect_pts(sc, 0, 0, 8, 6)
    q = rect_pts(sc, 1, 1, 6, 4)
    c, cq = centre(p), centre(q)
    items = [poly(p), poly(q, fill=False, dashed=True),
             side(p[3], p[2], cm(8), c), side(p[1], p[2], cm(6), c),
             side(q[0], q[1], cm(6), (cq[0], cq[1] - 30)), side(q[0], q[3], cm(4), (cq[0] - 50, cq[1]))]
    return fig(sc.h, T("A picture frame drawn to scale: the outside is 8 cm by 6 cm and is shaded. The photo inside, 6 cm by 4 cm, has a dashed outline; its sizes are written just inside it.",
                       "پیمانے کے مطابق تصویر کا فریم: باہر سے 8 ضرب 6 سینٹی میٹر، رنگا ہوا۔ اندر 6 ضرب 4 سینٹی میٹر کی تصویر ڈیش والے خاکے سے دکھائی گئی ہے؛ اس کی لمبائیاں اس کے اندر لکھی ہیں۔"), items)


F_FRAME = frame_fig()


def cut_corner():
    sc = Scale(8, 5, max_h=60)
    o = [sc(0, 0), sc(5, 0), sc(5, 2), sc(8, 2), sc(8, 5), sc(0, 5)]
    cut = rect_pts(sc, 5, 0, 3, 2)
    c, cc = centre(rect_pts(sc, 0, 0, 8, 5)), centre(cut)
    items = [poly(o), poly(cut, fill=False, dashed=True),
             side(o[4], o[5], cm(8), c), side(o[5], o[0], cm(5), c),
             side(cut[0], cut[1], cm(3), cc), side(cut[1], cut[2], cm(2), cc)]
    return fig(sc.h, T("An 8 cm by 5 cm rectangle, drawn to scale, with a 3 cm by 2 cm piece cut from its top right corner. The cut piece is shown by a dashed outline; the part left is shaded.",
                       "پیمانے کے مطابق 8 ضرب 5 سینٹی میٹر کی مستطیل جس کے اوپر دائیں کونے سے 3 ضرب 2 سینٹی میٹر کا ٹکڑا کاٹا گیا ہے۔ کٹا ہوا ٹکڑا ڈیش والے خاکے سے دکھایا گیا ہے؛ بچا ہوا حصہ رنگا ہوا ہے۔"), items)


F_CUT = cut_corner()


def side_step():
    """5 by 4 rectangle with a 2 by 3 rectangle joined to its right, at the bottom."""
    sc = Scale(7, 4, max_h=60)
    o = [sc(0, 0), sc(5, 0), sc(5, 1), sc(7, 1), sc(7, 4), sc(0, 4)]
    ca, cb = centre(rect_pts(sc, 0, 0, 5, 4)), centre(rect_pts(sc, 5, 1, 2, 3))
    items = [poly(o), seg(sc(5, 1), sc(5, 4), dashed=True),
             side(o[0], o[1], cm(5), ca), side(o[5], o[0], cm(4), ca),
             side(sc(5, 4), o[4], cm(2), cb), side(o[3], o[4], cm(3), cb)]
    return fig(sc.h, T("A shape drawn to scale: a 5 cm by 4 cm rectangle with a 2 cm by 3 cm rectangle joined to its right side, at the bottom. A dashed line separates the two rectangles.",
                       "پیمانے کے مطابق ایک شکل: 5 ضرب 4 سینٹی میٹر کی مستطیل جس کے دائیں طرف، نیچے، 2 ضرب 3 سینٹی میٹر کی مستطیل جڑی ہے۔ ڈیش والی لکیر دونوں مستطیلوں کو الگ کرتی ہے۔"), items)


F_QB = side_step()
F_R_ADD = l_shape(7, 3, 4, 2, m, T(
    "A shape drawn to scale: a 7 m by 3 m rectangle on top, with a 4 m by 2 m rectangle joined under its left end. A dashed line separates the two rectangles. The sides are labelled 7, 3, 4 and 2 m.",
    "پیمانے کے مطابق ایک شکل: اوپر 7 ضرب 3 میٹر کی مستطیل، اور اس کے بائیں سرے کے نیچے 4 ضرب 2 میٹر کی مستطیل جڑی ہے۔ ڈیش والی لکیر دونوں مستطیلوں کو الگ کرتی ہے۔ اضلاع پر 7، 3، 4 اور 2 میٹر لکھا ہے۔"))
F_R_HOLE = hole_fig(12, 10, 4, 3, 6.5, 5.5, m, hole_alt(12, 10, 4, 3, "m", "میٹر", "A courtyard", "ایک صحن", "a flower bed", "کیاری"))

FIGS = {
    "s1_hook": F_HOOK, "s3_split": F_TWO_WAYS, "s4_l_shape": F_L_ROOM, "s5_pond": F_POND, "s6_t_shape": F_T,
    "s7_wall": F_WALL, "s8_frame": F_FRAME, "s9_find_error": F_L_ROOM, "s11_cut_corner": F_CUT,
    "qb_apply": F_QB, "qb_find_error": F_POND, "r_add": F_R_ADD, "r_hole": F_R_HOLE,
}


lesson = {
 "id": "g6-maths-08-compound-shapes",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Find the area of shapes made from rectangles, by adding parts or taking away a missing part.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Area of compound shapes", "مرکب شکلوں کا رقبہ"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": PA_AREA}],
 "misconceptions": [
   {"id": "one_part_only", "description": "Finds the area of only one of the rectangles in the shape."},
   {"id": "multiplies_parts", "description": "Multiplies the areas of the parts instead of adding them."},
   {"id": "adds_hole", "description": "Adds the missing piece (a pond, a door) instead of taking it away."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_method", "type": "recall", "step": {
     "id": "qb_method", "type": "choice",
     "prompt": T("How can you find the area of an L-shaped room?", "L شکل کے کمرے کا رقبہ کیسے نکالیں؟"),
     "options": [
       opt("split", "Split it into rectangles, find each area, and add.", "اسے مستطیلوں میں بانٹیں، ہر ایک کا رقبہ نکالیں، اور جمع کریں۔", True, "Yes! Or take a missing piece away from a big rectangle.", "جی ہاں! یا بڑی مستطیل سے خالی حصہ گھٹائیں۔"),
       opt("multiply", "Multiply the two longest sides.", "دو سب سے لمبے اضلاع ضرب دیں۔", False, "That gives a rectangle bigger than the room. Split it into rectangles and add.", "اس سے کمرے سے بڑی مستطیل بنتی ہے۔ مستطیلوں میں بانٹ کر جمع کریں۔"),
       opt("perimeter", "Add up all the sides.", "تمام اضلاع جمع کریں۔", False, "That is the perimeter. Area: split into rectangles and add.", "یہ احاطہ ہے۔ رقبہ: مستطیلوں میں بانٹ کر جمع کریں۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("A shape is made of a 5 cm by 4 cm rectangle and a 2 cm by 3 cm rectangle. What is its area in cm²?", "ایک شکل 5 ضرب 4 سینٹی میٹر اور 2 ضرب 3 سینٹی میٹر کی مستطیلوں سے بنی ہے۔ اس کا رقبہ مربع سینٹی میٹر میں کیا ہے؟"),
     QB,
     T("20 + 6.", "20 + 6"),
     T("Right! 26 cm².", "درست! 26 مربع سینٹی میٹر"),
     T("5 × 4 = 20 and 2 × 3 = 6, so 20 + 6 = 26 cm².", "5 × 4 = 20 اور 2 × 3 = 6، تو 20 + 6 = 26"),
     common_wrong=[wrong(20, "That is one part. Add the other: 20 + 6 = 26.", "یہ ایک حصہ ہے۔ دوسرا جمع کریں: 20 + 6 = 26", "one_part_only"),
                   wrong(120, "Add the parts, don't multiply them: 20 + 6 = 26.", "حصے جمع کریں، ضرب نہیں: 20 + 6 = 26", "multiplies_parts")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("A 10 m by 8 m garden has a 3 m by 2 m pond. Kashif says the grass area is 86 m². What went wrong?", "10 ضرب 8 میٹر کے باغیچے میں 3 ضرب 2 میٹر کا تالاب ہے۔ کاشف کہتا ہے گھاس کا رقبہ 86 مربع میٹر ہے۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("subtract", "He added the pond. Take it away: 80 − 6 = 74 m².", "اس نے تالاب جمع کر دیا۔ اسے گھٹائیں: 80 − 6 = 74 مربع میٹر", True,
           "Yes! There is no grass where the pond is.", "جی ہاں! جہاں تالاب ہے وہاں گھاس نہیں۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "The pond isn't grass, so take it away: 80 − 6 = 74 m².", "تالاب گھاس نہیں، اس لیے گھٹائیں: 80 − 6 = 74", "adds_hole"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_add", "front": T("Area of an L-shape?", "L شکل کا رقبہ؟"),
    "back": T("Split into rectangles and add: 6 × 4 + 3 × 2 = 30.", "مستطیلوں میں بانٹ کر جمع کریں: 6 × 4 + 3 × 2 = 30")},
   {"id": "f_subtract", "front": T("Area with a hole?", "سوراخ والی شکل کا رقبہ؟"),
    "back": T("Big rectangle take away the hole: 10 × 8 − 3 × 2 = 74.", "بڑی مستطیل میں سے سوراخ گھٹائیں: 10 × 8 − 3 × 2 = 74")},
 ],
 "home_tasks": [{"id": "h_room", "text": T(
   "Draw the floor plan of a room or courtyard at home on squared paper. If it isn't a rectangle, split it into rectangles and find its area by counting squares and by multiplying.",
   "گھر کے کسی کمرے یا صحن کا نقشہ خانے دار کاغذ پر بنائیں۔ اگر یہ مستطیل نہیں تو اسے مستطیلوں میں بانٹیں اور رقبہ مربع گن کر بھی اور ضرب دے کر بھی نکالیں۔")}],
 "glossary": [T("Compound shape", "مرکب شکل")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Our room is shaped like the letter L. How can we find its area when it isn't a rectangle?",
                     "ہمارا کمرہ L حرف جیسا ہے۔ جب یہ مستطیل نہیں تو اس کا رقبہ کیسے نکالیں؟"),
    "text": T("Many real floors and gardens are made of rectangles joined together. First, a quick area check.", "بہت سے اصل فرش اور باغیچے جڑی ہوئی مستطیلوں سے بنے ہوتے ہیں۔ پہلے رقبے کا ایک سوال۔")},
   number_question(
     "s2_foundation",
     T("What is the area of a rectangle 7 cm by 5 cm, in cm²?", "7 ضرب 5 سینٹی میٹر مستطیل کا رقبہ مربع سینٹی میٹر میں کیا ہے؟"),
     35,
     T("Length × width.", "لمبائی × چوڑائی"),
     T("Right! 35 cm².", "درست! 35 مربع سینٹی میٹر"),
     T("7 × 5 = 35 cm².", "7 × 5 = 35"),
     common_wrong=[wrong(24, "24 cm is the perimeter. Area: 7 × 5 = 35.", "24 سینٹی میٹر احاطہ ہے۔ رقبہ: 7 × 5 = 35")],
     qtype="recall", skill=PA_AREA),
   {"id": "s3_split", "type": "explain",
    "character": say("thinking", "Cut the shape into rectangles, or fill in the gap and take it away!", "شکل کو مستطیلوں میں کاٹیں، یا خالی جگہ بھر کر گھٹائیں!"),
    "text": T("Way 1: split the shape into rectangles, find each area, and add them. Way 2: draw the big rectangle around it, then take away the area of the missing piece. Both ways give the same answer.",
              "طریقہ 1: شکل کو مستطیلوں میں بانٹیں، ہر ایک کا رقبہ نکالیں، اور جمع کریں۔ طریقہ 2: اس کے گرد بڑی مستطیل بنائیں، پھر خالی حصے کا رقبہ گھٹائیں۔ دونوں طریقوں سے ایک ہی جواب آتا ہے۔")},
   number_question(
     "s4_l_shape",
     T("Our L-shaped room is a 6 m by 4 m rectangle joined to a 3 m by 2 m rectangle. What is its area in m²?", "ہمارا L شکل کا کمرہ 6 ضرب 4 میٹر اور 3 ضرب 2 میٹر کی مستطیلوں سے بنا ہے۔ اس کا رقبہ مربع میٹر میں کیا ہے؟"),
     S4,
     T("6 × 4, then 3 × 2, then add.", "6 × 4، پھر 3 × 2، پھر جمع۔"),
     T("Right! 24 + 6 = 30 m².", "درست! 24 + 6 = 30 مربع میٹر"),
     T("6 × 4 = 24 and 3 × 2 = 6, so 30 m².", "6 × 4 = 24 اور 3 × 2 = 6، تو 30 مربع میٹر"),
     common_wrong=[wrong(24, "That is only the big part. Add the small part: 24 + 6 = 30.", "یہ صرف بڑا حصہ ہے۔ چھوٹا حصہ جمع کریں: 24 + 6 = 30", "one_part_only"),
                   wrong(144, "Add the parts, don't multiply them: 24 + 6 = 30.", "حصے جمع کریں، ضرب نہیں: 24 + 6 = 30", "multiplies_parts")]),
   number_question(
     "s5_pond",
     T("A 10 m by 8 m garden has a 3 m by 2 m pond in it. What area is grass, in m²?", "10 ضرب 8 میٹر کے باغیچے میں 3 ضرب 2 میٹر کا تالاب ہے۔ گھاس کا رقبہ مربع میٹر میں کتنا ہے؟"),
     S5,
     T("Whole garden take away the pond.", "پورا باغیچہ منفی تالاب۔"),
     T("Right! 80 − 6 = 74 m².", "درست! 80 − 6 = 74 مربع میٹر"),
     T("10 × 8 = 80, pond 3 × 2 = 6, so 80 − 6 = 74 m².", "10 × 8 = 80، تالاب 3 × 2 = 6، تو 80 − 6 = 74"),
     common_wrong=[wrong(86, "The pond isn't grass: take it away. 80 − 6 = 74.", "تالاب گھاس نہیں: گھٹائیں۔ 80 − 6 = 74", "adds_hole"),
                   wrong(80, "That includes the pond. Take it away: 74.", "اس میں تالاب شامل ہے۔ گھٹائیں: 74", "one_part_only")]),
   number_question(
     "s6_t_shape",
     T("A T-shaped sign is a 9 cm by 2 cm bar on top of a 3 cm by 5 cm stem. What is its area in cm²?", "ایک T شکل کا نشان 9 ضرب 2 سینٹی میٹر کی پٹی اور اس کے نیچے 3 ضرب 5 سینٹی میٹر کے تنے سے بنا ہے۔ اس کا رقبہ کیا ہے؟"),
     S6,
     T("9 × 2 + 3 × 5.", "9 × 2 + 3 × 5"),
     T("Right! 18 + 15 = 33 cm².", "درست! 18 + 15 = 33 مربع سینٹی میٹر"),
     T("9 × 2 = 18 and 3 × 5 = 15, so 33 cm².", "9 × 2 = 18 اور 3 × 5 = 15، تو 33"),
     common_wrong=[wrong(18, "That is only the bar. Add the stem: 18 + 15 = 33.", "یہ صرف پٹی ہے۔ تنا جمع کریں: 18 + 15 = 33", "one_part_only"),
                   wrong(270, "Add the parts, don't multiply them: 18 + 15 = 33.", "حصے جمع کریں، ضرب نہیں: 18 + 15 = 33", "multiplies_parts")]),
   number_question(
     "s7_wall",
     T("A wall is 5 m wide and 3 m high, with a door 1 m wide and 2 m high. How many m² of wall need paint?", "ایک دیوار 5 میٹر چوڑی اور 3 میٹر اونچی ہے، اس میں 1 میٹر چوڑا اور 2 میٹر اونچا دروازہ ہے۔ کتنے مربع میٹر دیوار پر رنگ ہوگا؟"),
     S7,
     T("Wall take away door.", "دیوار منفی دروازہ۔"),
     T("Right! 15 − 2 = 13 m².", "درست! 15 − 2 = 13 مربع میٹر"),
     T("5 × 3 = 15, door 1 × 2 = 2, so 13 m².", "5 × 3 = 15، دروازہ 1 × 2 = 2، تو 13"),
     common_wrong=[wrong(17, "We don't paint the door: 15 − 2 = 13.", "دروازے پر رنگ نہیں ہوتا: 15 − 2 = 13", "adds_hole"),
                   wrong(15, "That includes the door. Take it away: 13.", "اس میں دروازہ شامل ہے۔ گھٹائیں: 13", "one_part_only")]),
   number_question(
     "s8_frame",
     T("A photo 6 cm by 4 cm sits in a frame that is 8 cm by 6 cm on the outside. What is the area of the frame itself, in cm²?", "6 ضرب 4 سینٹی میٹر کی تصویر ایک فریم میں ہے جو باہر سے 8 ضرب 6 سینٹی میٹر ہے۔ صرف فریم کا رقبہ کتنا ہے؟"),
     S8,
     T("Outside rectangle take away the photo.", "باہر کی مستطیل منفی تصویر۔"),
     T("Right! 48 − 24 = 24 cm².", "درست! 48 − 24 = 24 مربع سینٹی میٹر"),
     T("8 × 6 = 48, photo 6 × 4 = 24, so 24 cm².", "8 × 6 = 48، تصویر 6 × 4 = 24، تو 24"),
     common_wrong=[wrong(48, "That includes the photo. Take it away: 48 − 24 = 24.", "اس میں تصویر شامل ہے۔ گھٹائیں: 48 − 24 = 24", "one_part_only"),
                   wrong(72, "The photo isn't frame: take it away. 48 − 24 = 24.", "تصویر فریم نہیں: گھٹائیں۔ 48 − 24 = 24", "adds_hole")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Hamid splits our L-shaped room into 24 m² and 6 m², then works out 24 × 6 = 144 m². What went wrong?", "حامد L شکل کے کمرے کو 24 اور 6 مربع میٹر میں بانٹ کر 24 × 6 = 144 مربع میٹر نکالتا ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("add", "The parts should be added: 24 + 6 = 30 m².", "حصے جمع ہونے چاہییں: 24 + 6 = 30 مربع میٹر", True,
          "Yes! The room is the two parts together, so add them.", "جی ہاں! کمرہ دونوں حصے مل کر ہے، اس لیے جمع کریں۔"),
      opt("subtract", "He should take away: 24 − 6 = 18 m².", "اسے گھٹانا چاہیے: 24 − 6 = 18", False,
          "Nothing is missing from the room. Add the parts: 30 m².", "کمرے سے کچھ کم نہیں۔ حصے جمع کریں: 30 مربع میٹر"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "144 m² is far bigger than the room. Add the parts: 30 m².", "144 مربع میٹر کمرے سے بہت بڑا ہے۔ حصے جمع کریں: 30", "multiplies_parts"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why do splitting the shape and taking away the gap give the same area? Can you teach me?",
                     "شکل کو بانٹنے اور خالی جگہ گھٹانے سے ایک ہی رقبہ کیوں آتا ہے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why do the two ways (adding parts, or taking away the missing piece) give the same area?",
              "اپنے الفاظ میں بتائیں: دونوں طریقوں (حصے جمع کرنا، یا خالی حصہ گھٹانا) سے ایک ہی رقبہ کیوں آتا ہے؟"),
    "key_idea": "Both ways count exactly the same squares inside the shape. Adding parts counts them piece by piece; taking away starts with too many squares and removes the ones outside the shape.",
    "levels": {
      "got_it": "Explains that both ways count the same squares inside the shape, one by building it up and the other by removing what isn't part of it.",
      "partly": "Says the shape doesn't change, without explaining the counting.",
      "not_yet": "Gives no reason, or thinks the answers would differ."},
    "keywords": [
      ["same", "squares", "ایک", "مربع"],
      ["add", "parts", "جمع", "حصے"],
      ["take away", "missing", "گھٹا", "خالی"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Both ways count the same squares inside.", "بہت خوب! دونوں طریقے اندر کے وہی مربع گنتے ہیں۔"),
      "partly": T("Good start! Now say what each way does with the squares.", "اچھی شروعات! اب بتائیں ہر طریقہ مربعوں کے ساتھ کیا کرتا ہے۔"),
      "not_yet": T("Think of squared paper: does the shape cover more squares if you count them a different way?", "خانے دار کاغذ سوچیں: کیا گننے کا طریقہ بدلنے سے شکل زیادہ مربع ڈھانپ لے گی؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_cut_corner",
     T("An 8 cm by 5 cm rectangle has a 3 cm by 2 cm piece cut from one corner. What area is left, in cm²?", "8 ضرب 5 سینٹی میٹر کی مستطیل کے ایک کونے سے 3 ضرب 2 سینٹی میٹر کا ٹکڑا کاٹا گیا۔ کتنا رقبہ بچا؟"),
     S11,
     T("8 × 5 take away 3 × 2.", "8 × 5 منفی 3 × 2"),
     T("Right! 40 − 6 = 34 cm².", "درست! 40 − 6 = 34 مربع سینٹی میٹر"),
     T("8 × 5 = 40 and 3 × 2 = 6, so 34 cm².", "8 × 5 = 40 اور 3 × 2 = 6، تو 34"),
     common_wrong=[wrong(46, "The piece was cut off: take it away. 40 − 6 = 34.", "ٹکڑا کٹ گیا: گھٹائیں۔ 40 − 6 = 34", "adds_hole"),
                   wrong(40, "That is before the cut. Take away 6: 34.", "یہ کاٹنے سے پہلے کا ہے۔ 6 گھٹائیں: 34", "one_part_only")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "No shape can stop you now!", "اب کوئی شکل آپ کو نہیں روک سکتی!"),
    "text": T("For a shape made of rectangles, split it up, find each area and add. Or start with the big rectangle around it and take away the missing piece. Holes like ponds and doors are always taken away.",
              "مستطیلوں سے بنی شکل کو بانٹیں، ہر حصے کا رقبہ نکالیں اور جمع کریں۔ یا اس کے گرد بڑی مستطیل لیں اور خالی حصہ گھٹائیں۔ تالاب اور دروازے جیسے سوراخ ہمیشہ گھٹائے جاتے ہیں۔"),
    "points": [T("Add the parts; never multiply them.", "حصے جمع کریں؛ کبھی ضرب نہیں۔"),
               T("Check: is your answer smaller than the big rectangle around the shape?", "جانچیں: کیا جواب شکل کے گرد بڑی مستطیل سے چھوٹا ہے؟")]},
 ],
 "review_questions": [
   {"id": "r_add", "type": "apply", "skill": SKILL, "step": number_question(
     "r_add",
     T("A shape is a 7 m by 3 m rectangle joined to a 4 m by 2 m rectangle. What is its area in m²?", "ایک شکل 7 ضرب 3 میٹر اور 4 ضرب 2 میٹر کی مستطیلوں سے بنی ہے۔ اس کا رقبہ کیا ہے؟"),
     R1,
     T("21 + 8.", "21 + 8"),
     T("Right! 29 m².", "درست! 29 مربع میٹر"),
     T("7 × 3 = 21 and 4 × 2 = 8, so 29 m².", "7 × 3 = 21 اور 4 × 2 = 8، تو 29"),
     common_wrong=[wrong(21, "Add the second part: 21 + 8 = 29.", "دوسرا حصہ جمع کریں: 21 + 8 = 29", "one_part_only")],
     qtype=None)},
   {"id": "r_hole", "type": "recall", "skill": SKILL, "step": number_question(
     "r_hole",
     T("A 12 m by 10 m courtyard has a 4 m by 3 m flower bed. What area is left for paving, in m²?", "12 ضرب 10 میٹر کے صحن میں 4 ضرب 3 میٹر کی کیاری ہے۔ فرش کے لیے کتنا رقبہ بچا؟"),
     R2,
     T("120 take away 12.", "120 منفی 12"),
     T("Right! 108 m².", "درست! 108 مربع میٹر"),
     T("12 × 10 = 120, bed 4 × 3 = 12, so 108 m².", "12 × 10 = 120، کیاری 4 × 3 = 12، تو 108"),
     common_wrong=[wrong(132, "The flower bed isn't paved: take it away. 108.", "کیاری پر فرش نہیں: گھٹائیں۔ 108", "adds_hole")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Perimeter and Area unit. No textbook text or exercises were used.",
   "Each shape is drawn to scale with its side lengths; dashed lines split it into rectangles or mark the piece taken away (pond, door, photo). Sketching them on squared paper still helps.",
   "Urdu term to check: مرکب شکل (compound shape).",
   "The numbers were worked out in content/sources/g6-maths-08/compound_shapes.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
with_figures(lesson, FIGS)
write(lesson)
