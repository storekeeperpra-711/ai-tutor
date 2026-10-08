import math
from common import (T, opt, say, wrong, number_question, write,
                    BOOK, REVIEW, PA_AREA, PA_COMPOUND, PA_PATH)

SKILL = PA_PATH


def outer(length, breadth, w):
    """Outer rectangle of a path of width w running round the outside."""
    return length + 2 * w, breadth + 2 * w


def path_area(length, breadth, w):
    ol, ob = outer(length, breadth, w)
    return ol * ob - length * breadth


def width_once(length, breadth, w):
    """Common slip: adds the path width on one side only."""
    return (length + w) * (breadth + w) - length * breadth


# s2: rectangle 9 by 6
assert 9 * 6 == 54 and 2 * (9 + 6) == 30
# s4-s6: field 20 m by 12 m, path 2 m wide round the outside
S4 = 20 + 2 * 2
assert S4 == 24 and 20 + 2 == 22
S5 = 24 * 16
assert outer(20, 12, 2) == (24, 16) and S5 == 384 and 22 * 14 == 308
S6 = S5 - 20 * 12
assert S6 == 144 == path_area(20, 12, 2)
assert (24 - 20) * (16 - 12) == 16 and width_once(20, 12, 2) == 68
# s7: garden 15 m by 10 m, path 1 m wide outside
S7 = path_area(15, 10, 1)
assert S7 == 204 - 150 == 54 and width_once(15, 10, 1) == 26 and 17 * 12 == 204
# s8: pool 10 m by 6 m, path 2 m outside, Rs 250 per m²
S8_AREA = path_area(10, 6, 2)
assert S8_AREA == 140 - 60 == 80
S8 = S8_AREA * 250
assert S8 == 20000 and 140 * 250 == 35000 and width_once(10, 6, 2) * 250 == 9000
# s9: school ground 30 m by 20 m, path 3 m outside; Bilal adds the width once
assert outer(30, 20, 3) == (36, 26) and path_area(30, 20, 3) == 336
assert 33 * 23 - 600 == 159
# s11: park in Lahore 40 m by 30 m, path 2 m wide inside along the edge
S11 = 40 * 30 - (40 - 2 * 2) * (30 - 2 * 2)
assert S11 == 1200 - 936 == 264
assert 44 * 34 - 1200 == 296 and 1200 - 38 * 28 == 136
# question bank
QB = path_area(10, 8, 1)
assert QB == 120 - 80 == 40 and width_once(10, 8, 1) == 19
assert path_area(12, 8, 2) == 192 - 96 == 96 and (16 - 12) * (12 - 8) == 16
# review
R1 = path_area(12, 9, 1)
assert R1 == 154 - 108 == 46 and width_once(12, 9, 1) == 22
R2 = 6 + 2 * 1
assert R2 == 8 and 6 + 1 == 7



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

def path_fig(length, breadth, w, alt, field=True, band=None, outer=None, max_h=68, padx=14, pady=10, min_band=9):
    """A field (shaded) with a path of width w all round it (the band between
    the field and the outer rectangle). The field is to scale; the path is
    drawn at least min_band thick so its label fits, so a thin path is drawn
    a little wider than it really is.
    field: label the field's length and breadth inside it (True), or give
    the two texts. band: text for the path width, shown in the left and
    right parts of the path. outer: texts for the outer length and breadth."""
    t = min_band
    for _ in range(4):
        s = min((W - 2 * padx - 2 * t) / length, (max_h - 2 * pady - 2 * t) / breadth)
        t = max(min_band, w * s)
    x0, y0 = (W - length * s) / 2, pady + t
    x1, y1 = x0 + length * s, y0 + breadth * s
    inner = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
    out = [(x0 - t, y0 - t), (x1 + t, y0 - t), (x1 + t, y1 + t), (x0 - t, y1 + t)]
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    items = [poly(out, fill=False), poly(inner)]
    if field:
        ft = (m(length), m(breadth)) if field is True else field
        items += [label((cx, y0 + TALL / 2 + 1.5), ft[0])]
        if ft[1]:
            items.append(label((x0 + len(ft[1]) * CHAR / 2 + 2, cy), ft[1]))
    if band:
        # Low in the band, so it is not read together with the field's breadth.
        by = y1 - TALL / 2 - 1
        items += [label((x0 - t / 2, by), band), label((x1 + t / 2, by), band)]
    if outer:
        o = out
        k = ((o[0][0] + o[2][0]) / 2, (o[0][1] + o[2][1]) / 2)
        items.append(side(o[0], o[1], outer[0], k))
        if outer[1]:
            items.append(side(o[1], o[2], outer[1], k))
    return fig(y1 + t + pady, alt, items)


def path_alt(length, breadth, w, what_en, what_ur, outside=True, extra_en="", extra_ur=""):
    where_en = "all round the outside of it" if outside else "inside it, along all four edges"
    where_ur = "اس کے باہر چاروں طرف" if outside else "اس کے اندر چاروں کناروں کے ساتھ"
    return T(f"{what_en} {length} m long and {breadth} m broad, shaded, with a path {w} m wide {where_en}. The path is the white band between the shaded rectangle and the outer rectangle. The path width, {w} m, is written in the path near the bottom of the left end and again of the right end.{extra_en}",
             f"{what_ur} {length} میٹر لمبا اور {breadth} میٹر چوڑا، رنگا ہوا، اور {where_ur} {w} میٹر چوڑا راستہ۔ راستہ رنگی ہوئی مستطیل اور باہر کی مستطیل کے درمیان سفید پٹی ہے۔ راستے کی چوڑائی، {w} میٹر، بائیں سرے اور پھر دائیں سرے کے نچلے حصے میں راستے میں لکھی ہے۔{extra_ur}")


F_HOOK = path_fig(20, 12, 2, T("A school field, a shaded rectangle, with a path of the same width all round it: a white band between the field and a bigger outer rectangle.",
                               "سکول کا میدان، رنگی ہوئی مستطیل، جس کے چاروں طرف ایک جیسی چوڑائی کا راستہ ہے: میدان اور بڑی باہر کی مستطیل کے درمیان سفید پٹی۔"),
                  field=False)
F_EXPLAIN = path_fig(20, 12, 2, T("A field, a shaded rectangle with its length marked L, and a path all round it, the white band out to a bigger outer rectangle. The path's width is marked w at the left end and again at the right end, so the outer length is L + w + w.",
                                  "ایک میدان، رنگی ہوئی مستطیل جس کی لمبائی پر L لکھا ہے، اور اس کے چاروں طرف راستہ، باہر کی بڑی مستطیل تک سفید پٹی۔ راستے کی چوڑائی پر بائیں سرے اور پھر دائیں سرے پر w لکھا ہے، اس لیے باہر کی لمبائی L + w + w ہے۔"),
                     field=("L", None), band="w")
F_OUTER_LEN = path_fig(20, 12, 2, path_alt(20, 12, 2, "The school field,", "سکول کا میدان،",
                       extra_en=" The field's length 20 m and breadth 12 m are written inside it. The outer length, along the top, is marked ?.",
                       extra_ur=" میدان کی لمبائی 20 میٹر اور چوڑائی 12 میٹر اس کے اندر لکھی ہیں۔ اوپر باہر کی لمبائی پر ? ہے۔"),
                       band=m(2), outer=("?", None))
F_OUTER_AREA = path_fig(20, 12, 2, path_alt(20, 12, 2, "The school field,", "سکول کا میدان،",
                        extra_en=" The outer rectangle is labelled 24 m along the top and 16 m down the right side.",
                        extra_ur=" باہر کی مستطیل پر اوپر 24 میٹر اور دائیں طرف 16 میٹر لکھا ہے۔"),
                        field=False, band=m(2), outer=(m(24), m(16)))
F_PATH_AREA = path_fig(20, 12, 2, path_alt(20, 12, 2, "The school field,", "سکول کا میدان،",
                       extra_en=" The field is labelled 20 m and 12 m inside it; the outer rectangle is labelled 24 m along the top and 16 m down the right side.",
                       extra_ur=" میدان کے اندر 20 میٹر اور 12 میٹر لکھا ہے؛ باہر کی مستطیل پر اوپر 24 میٹر اور دائیں طرف 16 میٹر لکھا ہے۔"),
                       outer=(m(24), m(16)))


def simple_path(length, breadth, w, what_en, what_ur, outer=None, extra_en="", extra_ur=""):
    return path_fig(length, breadth, w, path_alt(length, breadth, w, what_en, what_ur,
                    extra_en=f" The {length} m and {breadth} m are written inside the shaded rectangle.{extra_en}",
                    extra_ur=f" {length} میٹر اور {breadth} میٹر رنگی ہوئی مستطیل کے اندر لکھے ہیں۔{extra_ur}"),
                    band=m(w), outer=outer)


F_GARDEN = simple_path(15, 10, 1, "Amna's garden,", "آمنہ کا باغیچہ،")
F_POOL = simple_path(10, 6, 2, "A pool", "ایک تالاب")
F_GROUND = simple_path(30, 20, 3, "A school ground", "سکول کا ایک میدان")
F_PARK = path_fig(40, 30, 2, path_alt(36, 26, 2, "The grass of a park in Lahore,", "لاہور کے ایک پارک کی گھاس،", outside=True,
                  extra_en=" The outer rectangle is the edge of the whole park, labelled 40 m along the top and 30 m down the right side, so the path runs inside the park along its four edges. The grass is labelled 36 m and 26 m inside it.",
                  extra_ur=" باہر کی مستطیل پورے پارک کا کنارہ ہے، اوپر 40 میٹر اور دائیں طرف 30 میٹر، اس لیے راستہ پارک کے اندر چاروں کناروں کے ساتھ ہے۔ گھاس کے اندر 36 میٹر اور 26 میٹر لکھا ہے۔"),
                  field=(m(36), m(26)), band=m(2), outer=(m(40), m(30)))
F_QB = simple_path(10, 8, 1, "A field", "ایک میدان")
F_QB_ERR = simple_path(12, 8, 2, "A pool", "ایک تالاب", outer=(m(16), m(12)),
                       extra_en=" The outer rectangle is labelled 16 m along the top and 12 m down the right side.",
                       extra_ur=" باہر کی مستطیل پر اوپر 16 میٹر اور دائیں طرف 12 میٹر لکھا ہے۔")
F_R_PATH = simple_path(12, 9, 1, "A garden", "ایک باغیچہ")
F_R_OUTER = path_fig(6, 3, 1, T("A flower bed, a shaded rectangle with its length 6 m written inside, and a path 1 m wide all round the outside. The path width, 1 m, is written in the path near the bottom of the left end and again of the right end. The outer length, along the top, is marked ?.",
                                "ایک کیاری، رنگی ہوئی مستطیل جس کے اندر اس کی لمبائی 6 میٹر لکھی ہے، اور باہر چاروں طرف 1 میٹر چوڑا راستہ۔ راستے کی چوڑائی، 1 میٹر، بائیں سرے اور پھر دائیں سرے کے نچلے حصے میں راستے میں لکھی ہے۔ اوپر باہر کی لمبائی پر ? ہے۔"),
                     field=(m(6), None), band=m(1), outer=("?", None), max_h=56)

FIGS = {
    "s1_hook": F_HOOK, "s3_outer_inner": F_EXPLAIN, "s4_outer_length": F_OUTER_LEN, "s5_outer_area": F_OUTER_AREA,
    "s6_path_area": F_PATH_AREA, "s7_garden": F_GARDEN, "s8_cost": F_POOL, "s9_find_error": F_GROUND,
    "s11_inside_path": F_PARK, "qb_apply": F_QB, "qb_find_error": F_QB_ERR, "r_path": F_R_PATH, "r_outer": F_R_OUTER,
}


lesson = {
 "id": "g6-maths-08-area-of-a-path",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Find the area of a path of equal width around or inside a rectangle, by taking the inner area away from the outer area.", "textbook": BOOK}],
 "skills": [SKILL],
 "title": T("Area of a path", "راستے کا رقبہ"),
 "estimated_minutes": 15,
 "prerequisites": [{"skill": PA_COMPOUND}, {"skill": PA_AREA}],
 "misconceptions": [
   {"id": "width_once", "description": "Adds the path width only once to the length and breadth, instead of on both sides."},
   {"id": "outer_only", "description": "Finds the area of the outer rectangle and forgets to take away the inner rectangle."},
   {"id": "subtracts_lengths", "description": "Subtracts the lengths and breadths and multiplies the differences, instead of subtracting the areas."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_method", "type": "recall", "step": {
     "id": "qb_method", "type": "choice",
     "prompt": T("How do you find the area of a path that runs round a rectangular field?", "مستطیل نما میدان کے گرد بنے راستے کا رقبہ کیسے نکالیں؟"),
     "options": [
       opt("outer_minus_inner", "Outer rectangle area take away the field's area.", "باہر کی مستطیل کے رقبے میں سے میدان کا رقبہ گھٹائیں۔", True,
           "Yes! What is left is the path.", "جی ہاں! جو بچتا ہے وہی راستہ ہے۔"),
       opt("outer_only", "Find the area of the outer rectangle.", "باہر کی مستطیل کا رقبہ نکالیں۔", False,
           "That includes the field too. Take the field's area away.", "اس میں میدان بھی شامل ہے۔ میدان کا رقبہ گھٹائیں۔", "outer_only"),
       opt("lengths", "Take the lengths away, then multiply.", "لمبائیاں گھٹا کر ضرب دیں۔", False,
           "Take away areas, not lengths: outer area − inner area.", "لمبائیاں نہیں، رقبے گھٹائیں: باہر کا رقبہ − اندر کا رقبہ۔", "subtracts_lengths"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("A field is 10 m long and 8 m broad. A path 1 m wide runs round the outside. What is the area of the path in m²?", "ایک میدان 10 میٹر لمبا اور 8 میٹر چوڑا ہے۔ اس کے باہر چاروں طرف 1 میٹر چوڑا راستہ ہے۔ راستے کا رقبہ مربع میٹر میں کتنا ہے؟"),
     QB,
     T("Outer rectangle is 12 m by 10 m.", "باہر کی مستطیل 12 ضرب 10 میٹر ہے۔"),
     T("Right! 120 − 80 = 40 m².", "درست! 120 − 80 = 40 مربع میٹر"),
     T("Outer 12 × 10 = 120, field 10 × 8 = 80, so 120 − 80 = 40 m².", "باہر 12 × 10 = 120، میدان 10 × 8 = 80، تو 120 − 80 = 40"),
     common_wrong=[wrong(120, "That includes the field. Take away 80: 40.", "اس میں میدان شامل ہے۔ 80 گھٹائیں: 40", "outer_only"),
                   wrong(19, "The path is on both sides, so add 2 m: 12 by 10. 120 − 80 = 40.", "راستہ دونوں طرف ہے، 2 میٹر جمع کریں: 12 ضرب 10۔ 120 − 80 = 40", "width_once")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("A pool is 12 m by 8 m with a 2 m path round it, so the outside is 16 m by 12 m. Sana says the path area is (16 − 12) × (12 − 8) = 16 m². What went wrong?", "ایک تالاب 12 ضرب 8 میٹر ہے اور گرد 2 میٹر کا راستہ ہے، تو باہر سے 16 ضرب 12 میٹر ہے۔ ثنا کہتی ہے راستے کا رقبہ (16 − 12) × (12 − 8) = 16 مربع میٹر ہے۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("areas", "She took away lengths. Take away areas: 192 − 96 = 96 m².", "اس نے لمبائیاں گھٹائیں۔ رقبے گھٹائیں: 192 − 96 = 96 مربع میٹر", True,
           "Yes! Find both areas first, then subtract.", "جی ہاں! پہلے دونوں رقبے نکالیں، پھر گھٹائیں۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "16 m² is far too small for a path round a pool. 192 − 96 = 96 m².", "تالاب کے گرد راستے کے لیے 16 مربع میٹر بہت کم ہے۔ 192 − 96 = 96", "subtracts_lengths"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_outer", "front": T("Path 2 m wide round a 20 m long field: outer length?", "20 میٹر لمبے میدان کے گرد 2 میٹر کا راستہ: باہر کی لمبائی؟"),
    "back": T("20 + 2 × 2 = 24 m. The path is on both ends.", "20 + 2 × 2 = 24 میٹر۔ راستہ دونوں سروں پر ہے۔")},
   {"id": "f_path", "front": T("Area of a path?", "راستے کا رقبہ؟"),
    "back": T("Outer area − inner area: 24 × 16 − 20 × 12 = 144.", "باہر کا رقبہ − اندر کا رقبہ: 24 × 16 − 20 × 12 = 144")},
 ],
 "home_tasks": [{"id": "h_border", "text": T(
   "Find a rectangular mat, table cloth or carpet at home that has a border of the same width all round. Measure the whole thing and the middle part, and work out the area of the border.",
   "گھر میں کوئی مستطیل چٹائی، میز پوش یا قالین ڈھونڈیں جس کے چاروں طرف ایک جیسی چوڑائی کا کنارا ہو۔ پوری چیز اور درمیانی حصہ ناپیں، اور کنارے کا رقبہ نکالیں۔")}],
 "glossary": [T("Path", "راستہ"), T("Width", "چوڑائی"), T("Outer rectangle", "باہر کی مستطیل")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Our school field has a brick path all round it. How much ground does the path cover?",
                     "ہمارے سکول کے میدان کے چاروں طرف اینٹوں کا راستہ ہے۔ راستہ کتنی زمین گھیرتا ہے؟"),
    "text": T("A path often runs round a field, a garden or a pool. Today we find its area. First, a quick area check.",
              "اکثر میدان، باغیچے یا تالاب کے گرد راستہ بنا ہوتا ہے۔ آج ہم اس کا رقبہ نکالیں گے۔ پہلے رقبے کا ایک سوال۔")},
   number_question(
     "s2_foundation",
     T("What is the area of a rectangle 9 m by 6 m, in m²?", "9 ضرب 6 میٹر مستطیل کا رقبہ مربع میٹر میں کیا ہے؟"),
     54,
     T("Length × breadth.", "لمبائی × چوڑائی"),
     T("Right! 54 m².", "درست! 54 مربع میٹر"),
     T("9 × 6 = 54 m².", "9 × 6 = 54"),
     common_wrong=[wrong(30, "30 m is the perimeter. Area: 9 × 6 = 54.", "30 میٹر احاطہ ہے۔ رقبہ: 9 × 6 = 54")],
     qtype="recall", skill=PA_AREA),
   {"id": "s3_outer_inner", "type": "explain",
    "character": say("thinking", "The path is on both sides, so add its width twice!", "راستہ دونوں طرف ہے، اس لیے اس کی چوڑائی دو بار جمع کریں!"),
    "text": T("Picture a field with a path of the same width all round it. Field and path together make a bigger outer rectangle. Outer length = length + 2 × width of path. Outer breadth = breadth + 2 × width of path. Area of path = outer area − field area.",
              "ایک میدان سوچیں جس کے چاروں طرف ایک جیسی چوڑائی کا راستہ ہے۔ میدان اور راستہ مل کر باہر ایک بڑی مستطیل بناتے ہیں۔ باہر کی لمبائی = لمبائی + 2 × راستے کی چوڑائی۔ باہر کی چوڑائی = چوڑائی + 2 × راستے کی چوڑائی۔ راستے کا رقبہ = باہر کا رقبہ − میدان کا رقبہ۔")},
   number_question(
     "s4_outer_length",
     T("Our school field is 20 m long and 12 m broad. A path 2 m wide runs round the outside. What is the outer length, in m?", "ہمارا سکول کا میدان 20 میٹر لمبا اور 12 میٹر چوڑا ہے۔ اس کے باہر چاروں طرف 2 میٹر چوڑا راستہ ہے۔ باہر کی لمبائی کتنے میٹر ہے؟"),
     S4,
     T("The path adds 2 m at each end.", "راستہ ہر سرے پر 2 میٹر بڑھاتا ہے۔"),
     T("Right! 20 + 2 + 2 = 24 m.", "درست! 20 + 2 + 2 = 24 میٹر"),
     T("The path is at both ends: 20 + 2 × 2 = 24 m.", "راستہ دونوں سروں پر ہے: 20 + 2 × 2 = 24 میٹر"),
     common_wrong=[wrong(22, "The path is at both ends, so add 2 twice: 24.", "راستہ دونوں سروں پر ہے، 2 دو بار جمع کریں: 24", "width_once")]),
   number_question(
     "s5_outer_area",
     T("The outer breadth is 12 + 2 × 2 = 16 m and the outer length is 24 m. What is the area of the outer rectangle, in m²?", "باہر کی چوڑائی 12 + 2 × 2 = 16 میٹر اور باہر کی لمبائی 24 میٹر ہے۔ باہر کی مستطیل کا رقبہ مربع میٹر میں کتنا ہے؟"),
     S5,
     T("24 × 16.", "24 × 16"),
     T("Right! 24 × 16 = 384 m².", "درست! 24 × 16 = 384 مربع میٹر"),
     T("24 × 16 = 384 m².", "24 × 16 = 384"),
     common_wrong=[wrong(308, "That uses 22 by 14. The path is on both sides: 24 × 16 = 384.", "یہ 22 ضرب 14 ہے۔ راستہ دونوں طرف ہے: 24 × 16 = 384", "width_once"),
                   wrong(80, "That is the perimeter. Area: 24 × 16 = 384.", "یہ احاطہ ہے۔ رقبہ: 24 × 16 = 384")]),
   number_question(
     "s6_path_area",
     T("The outer area is 384 m² and the field is 20 m by 12 m. What is the area of the path, in m²?", "باہر کا رقبہ 384 مربع میٹر ہے اور میدان 20 ضرب 12 میٹر ہے۔ راستے کا رقبہ مربع میٹر میں کتنا ہے؟"),
     S6,
     T("Outer area take away the field's area.", "باہر کا رقبہ منفی میدان کا رقبہ۔"),
     T("Right! 384 − 240 = 144 m².", "درست! 384 − 240 = 144 مربع میٹر"),
     T("Field 20 × 12 = 240, so path 384 − 240 = 144 m².", "میدان 20 × 12 = 240، تو راستہ 384 − 240 = 144"),
     common_wrong=[wrong(384, "That includes the field. Take away 240: 144.", "اس میں میدان شامل ہے۔ 240 گھٹائیں: 144", "outer_only"),
                   wrong(16, "Take away areas, not lengths: 384 − 240 = 144.", "لمبائیاں نہیں، رقبے گھٹائیں: 384 − 240 = 144", "subtracts_lengths")]),
   number_question(
     "s7_garden",
     T("Amna's garden is 15 m long and 10 m broad. A path 1 m wide runs round the outside. What is the area of the path, in m²?", "آمنہ کا باغیچہ 15 میٹر لمبا اور 10 میٹر چوڑا ہے۔ اس کے باہر چاروں طرف 1 میٹر چوڑا راستہ ہے۔ راستے کا رقبہ مربع میٹر میں کتنا ہے؟"),
     S7,
     T("Outer rectangle is 17 m by 12 m.", "باہر کی مستطیل 17 ضرب 12 میٹر ہے۔"),
     T("Right! 204 − 150 = 54 m².", "درست! 204 − 150 = 54 مربع میٹر"),
     T("Outer 17 × 12 = 204, garden 15 × 10 = 150, so 54 m².", "باہر 17 × 12 = 204، باغیچہ 15 × 10 = 150، تو 54"),
     common_wrong=[wrong(204, "That includes the garden. Take away 150: 54.", "اس میں باغیچہ شامل ہے۔ 150 گھٹائیں: 54", "outer_only"),
                   wrong(26, "Add 1 m on both sides: 17 by 12. 204 − 150 = 54.", "دونوں طرف 1 میٹر جمع کریں: 17 ضرب 12۔ 204 − 150 = 54", "width_once")]),
   number_question(
     "s8_cost",
     T("A pool is 10 m by 6 m with a path 2 m wide round it, so the path area is 140 − 60 = 80 m². Tiles cost Rs 250 per m². What does tiling the path cost, in rupees?", "ایک تالاب 10 ضرب 6 میٹر ہے اور گرد 2 میٹر چوڑا راستہ ہے، تو راستے کا رقبہ 140 − 60 = 80 مربع میٹر ہے۔ ٹائلیں 250 روپے فی مربع میٹر ہیں۔ راستے پر ٹائلیں لگانے کا خرچ کتنے روپے ہے؟"),
     S8,
     T("Path area × rupees per m².", "راستے کا رقبہ × روپے فی مربع میٹر"),
     T("Right! 80 × 250 = Rs 20000.", "درست! 80 × 250 = 20000 روپے"),
     T("80 × 250 = 20000 rupees.", "80 × 250 = 20000 روپے"),
     common_wrong=[wrong(35000, "That tiles the pool too. Use the path only: 80 × 250 = 20000.", "اس میں تالاب بھی شامل ہے۔ صرف راستہ: 80 × 250 = 20000", "outer_only"),
                   wrong(330, "Multiply, don't add: 80 × 250 = 20000.", "جمع نہیں، ضرب دیں: 80 × 250 = 20000")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("A school ground is 30 m by 20 m with a path 3 m wide round the outside. Bilal says the outer rectangle is 33 m by 23 m. What went wrong?", "ایک سکول کا میدان 30 ضرب 20 میٹر ہے اور باہر چاروں طرف 3 میٹر چوڑا راستہ ہے۔ بلال کہتا ہے باہر کی مستطیل 33 ضرب 23 میٹر ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("both_sides", "The path is on both sides: it should be 36 m by 26 m.", "راستہ دونوں طرف ہے: یہ 36 ضرب 26 میٹر ہونا چاہیے۔", True,
          "Yes! Add 3 m at each end: path area 936 − 600 = 336 m².", "جی ہاں! ہر سرے پر 3 میٹر جمع کریں: راستے کا رقبہ 936 − 600 = 336"),
      opt("subtract", "He should take 3 m away: 27 m by 17 m.", "اسے 3 میٹر گھٹانے چاہییں: 27 ضرب 17", False,
          "The path is outside, so the outer rectangle is bigger: 36 m by 26 m.", "راستہ باہر ہے، اس لیے باہر کی مستطیل بڑی ہے: 36 ضرب 26"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "He added the width on one side only. It is 36 m by 26 m.", "اس نے چوڑائی صرف ایک طرف جمع کی۔ یہ 36 ضرب 26 ہے۔", "width_once"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why do we add the path's width two times, not one? Can you teach me?",
                     "ہم راستے کی چوڑائی ایک بار نہیں، دو بار کیوں جمع کرتے ہیں؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why is the outer length the field's length plus two times the path's width?",
              "اپنے الفاظ میں بتائیں: باہر کی لمبائی میدان کی لمبائی جمع راستے کی دو گنا چوڑائی کیوں ہوتی ہے؟"),
    "key_idea": "The path goes all the way round, so walking along the outer length you cross the path at one end, then the field, then the path again at the other end. That is the width twice.",
    "levels": {
      "got_it": "Explains that the path lies at both ends (both sides), so its width is added once for each end.",
      "partly": "Says the path is on both sides without linking it to adding the width twice.",
      "not_yet": "Gives no reason, or thinks the width is added once."},
    "keywords": [
      ["both", "ends", "sides", "دونوں", "طرف"],
      ["twice", "two", "دو"],
      ["width", "path", "چوڑائی", "راستہ"]],
    "fallback_feedback": {
      "got_it": T("Well explained! The path is at both ends, so its width counts twice.", "بہت خوب! راستہ دونوں سروں پر ہے، اس لیے چوڑائی دو بار گنی جاتی ہے۔"),
      "partly": T("Good start! Now say how that changes the outer length.", "اچھی شروعات! اب بتائیں اس سے باہر کی لمبائی کیسے بدلتی ہے۔"),
      "not_yet": T("Imagine walking across the outer rectangle: how many times do you cross the path?", "باہر کی مستطیل کے آر پار چلنا سوچیں: آپ کتنی بار راستہ پار کرتے ہیں؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_inside_path",
     T("A park in Lahore is 40 m long and 30 m broad. A path 2 m wide runs inside it, along all four edges. The grass inside is 36 m by 26 m. What is the area of the path, in m²?", "لاہور کا ایک پارک 40 میٹر لمبا اور 30 میٹر چوڑا ہے۔ اس کے اندر چاروں کناروں کے ساتھ 2 میٹر چوڑا راستہ ہے۔ اندر کی گھاس 36 ضرب 26 میٹر ہے۔ راستے کا رقبہ مربع میٹر میں کتنا ہے؟"),
     S11,
     T("Whole park take away the grass inside.", "پورا پارک منفی اندر کی گھاس۔"),
     T("Right! 1200 − 936 = 264 m².", "درست! 1200 − 936 = 264 مربع میٹر"),
     T("Park 40 × 30 = 1200, grass 36 × 26 = 936, so 264 m².", "پارک 40 × 30 = 1200، گھاس 36 × 26 = 936، تو 264"),
     common_wrong=[wrong(1200, "That is the whole park. Take away the grass: 264.", "یہ پورا پارک ہے۔ گھاس گھٹائیں: 264", "outer_only"),
                   wrong(296, "This path is inside, so the grass is smaller: 36 by 26. 1200 − 936 = 264.", "یہ راستہ اندر ہے، اس لیے گھاس چھوٹی ہے: 36 ضرب 26۔ 1200 − 936 = 264"),
                   wrong(16, "Take away areas, not lengths: 1200 − 936 = 264.", "لمبائیاں نہیں، رقبے گھٹائیں: 1200 − 936 = 264", "subtracts_lengths")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Now you can work out any path, outside or inside!", "اب آپ کوئی بھی راستہ نکال سکتے ہیں، باہر ہو یا اندر!"),
    "text": T("Area of a path = outer area − inner area. For a path outside, add 2 × width to the length and to the breadth to get the outer rectangle. For a path inside, take 2 × width away to get the inner rectangle. Cost = path area × price per m².",
              "راستے کا رقبہ = باہر کا رقبہ − اندر کا رقبہ۔ باہر والے راستے کے لیے لمبائی اور چوڑائی میں 2 × راستے کی چوڑائی جمع کریں۔ اندر والے راستے کے لیے 2 × چوڑائی گھٹا کر اندر کی مستطیل بنائیں۔ خرچ = راستے کا رقبہ × قیمت فی مربع میٹر۔"),
    "points": [T("The path is on both sides: use 2 × width.", "راستہ دونوں طرف ہے: 2 × چوڑائی لیں۔"),
               T("Take away areas, not lengths.", "لمبائیاں نہیں، رقبے گھٹائیں۔")]},
 ],
 "review_questions": [
   {"id": "r_path", "type": "apply", "skill": SKILL, "step": number_question(
     "r_path",
     T("A garden is 12 m by 9 m with a path 1 m wide round the outside. What is the area of the path, in m²?", "ایک باغیچہ 12 ضرب 9 میٹر ہے اور باہر چاروں طرف 1 میٹر چوڑا راستہ ہے۔ راستے کا رقبہ مربع میٹر میں کتنا ہے؟"),
     R1,
     T("Outer rectangle is 14 m by 11 m.", "باہر کی مستطیل 14 ضرب 11 میٹر ہے۔"),
     T("Right! 154 − 108 = 46 m².", "درست! 154 − 108 = 46 مربع میٹر"),
     T("Outer 14 × 11 = 154, garden 12 × 9 = 108, so 46 m².", "باہر 14 × 11 = 154، باغیچہ 12 × 9 = 108، تو 46"),
     common_wrong=[wrong(154, "That includes the garden. Take away 108: 46.", "اس میں باغیچہ شامل ہے۔ 108 گھٹائیں: 46", "outer_only"),
                   wrong(22, "Add 1 m on both sides: 14 by 11. 154 − 108 = 46.", "دونوں طرف 1 میٹر جمع کریں: 14 ضرب 11۔ 154 − 108 = 46", "width_once")],
     qtype=None)},
   {"id": "r_outer", "type": "recall", "skill": SKILL, "step": number_question(
     "r_outer",
     T("A flower bed is 6 m long. A path 1 m wide runs round the outside. What is the outer length, in m?", "ایک کیاری 6 میٹر لمبی ہے۔ اس کے باہر چاروں طرف 1 میٹر چوڑا راستہ ہے۔ باہر کی لمبائی کتنے میٹر ہے؟"),
     R2,
     T("Add the width at both ends.", "دونوں سروں پر چوڑائی جمع کریں۔"),
     T("Right! 6 + 1 + 1 = 8 m.", "درست! 6 + 1 + 1 = 8 میٹر"),
     T("6 + 2 × 1 = 8 m.", "6 + 2 × 1 = 8 میٹر"),
     common_wrong=[wrong(7, "The path is at both ends: 6 + 2 = 8.", "راستہ دونوں سروں پر ہے: 6 + 2 = 8", "width_once")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Perimeter and Area unit (a gap lesson matching the book chapter on area). No textbook text or exercises were used.",
   "Most steps show the field (shaded) and the path (the white band round it) with the path width written at both ends. The fields are to scale, but a thin path is drawn a little wider than it really is so its label fits. Ask pupils to draw their own on a slate or the board as well.",
   "Step s11 has the path inside the park's edge; point out that here the width is taken away twice to get the inner rectangle.",
   "Urdu terms to check: راستہ (path), چوڑائی (width / breadth), باہر کی مستطیل (outer rectangle).",
   "The numbers were worked out in content/sources/g6-maths-08/area_of_path.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
with_figures(lesson, FIGS)
write(lesson)
