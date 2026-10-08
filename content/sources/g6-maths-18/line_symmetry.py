import math

from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, SY_SHAPES, SY_LINE_SYMMETRY)

SKILL = SY_LINE_SYMMETRY


# ---------- geometry helpers ----------

def r1(v):
    return round(v + 0.0, 1)


def pt(x, y):
    return [r1(x), r1(y)]


def regular(n, cx, cy, radius, start=-90):
    """Vertices of a regular n-gon, the first one at angle `start` (degrees, y down)."""
    return [pt(cx + radius * math.cos(math.radians(start + 360 * k / n)),
               cy + radius * math.sin(math.radians(start + 360 * k / n))) for k in range(n)]


def reflect(p, c, deg):
    """Reflect point p in the line through c at angle deg."""
    dx, dy = math.cos(math.radians(deg)), math.sin(math.radians(deg))
    vx, vy = p[0] - c[0], p[1] - c[1]
    dot = vx * dx + vy * dy
    return (2 * dot * dx - vx + c[0], 2 * dot * dy - vy + c[1])


def segments_of(polylines, closed=False):
    segs = []
    for line in polylines:
        pts = list(line) + ([line[0]] if closed else [])
        segs += [(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]
    return segs


def close(p, q, tol=0.2):
    return abs(p[0] - q[0]) <= tol and abs(p[1] - q[1]) <= tol


def same(segs_a, segs_b):
    """Two drawings match if every segment of each has a matching segment in the
    other (either direction), allowing for the 1-decimal rounding."""
    def covered(xs, ys):
        return all(any((close(a, c) and close(b, d)) or (close(a, d) and close(b, c)) for c, d in ys)
                   for a, b in xs)
    return covered(segs_a, segs_b) and covered(segs_b, segs_a)


def count_lines(polylines, center, closed=False):
    """How many mirror lines through `center` map the drawing onto itself
    (tries every whole degree)."""
    segs = segments_of(polylines, closed)
    n = 0
    for deg in range(180):
        n += same([(reflect(a, center, deg), reflect(b, center, deg)) for a, b in segs], segs)
    return n


def mirror_through(center, deg, half):
    """A dashed mirror line of half-length `half` through center at angle deg."""
    dx, dy = math.cos(math.radians(deg)), math.sin(math.radians(deg))
    return {"kind": "line", "from": pt(center[0] - half * dx, center[1] - half * dy),
            "to": pt(center[0] + half * dx, center[1] + half * dy), "style": "dashed"}


def poly(points, fill=True):
    item = {"kind": "polygon", "points": [pt(*p) for p in points]}
    if fill:
        item["fill"] = True
    return item


def seg(a, b, dashed=False):
    item = {"kind": "line", "from": pt(*a), "to": pt(*b)}
    if dashed:
        item["style"] = "dashed"
    return item


def label(at, text):
    return {"kind": "label", "at": pt(*at), "text": text}


def fig(w, h, alt, items):
    return {"width": w, "height": h, "alt": alt, "items": items}


def centre(points):
    return (sum(p[0] for p in points) / len(points), sum(p[1] for p in points) / len(points))


# ---------- shapes and their lines of symmetry ----------

SQUARE = [(30, 10), (70, 10), (70, 50), (30, 50)]
RECT = [(15, 12), (85, 12), (85, 48), (15, 48)]
EQUI = regular(3, 50, 34, 26)
ISO = [(50, 6), (74, 54), (26, 54)]
SCALENE = [(14, 50), (86, 50), (34, 10)]
HEXAGON = regular(6, 50, 32, 26, start=0)
KITE = [(50, 6), (74, 28), (50, 74), (26, 28)]

assert count_lines([SQUARE], centre(SQUARE), closed=True) == 4
RECT_LINES = count_lines([RECT], centre(RECT), closed=True)
assert RECT_LINES == 2
EQUI_LINES = count_lines([EQUI], centre(EQUI), closed=True)
assert EQUI_LINES == 3
ISO_LINES = count_lines([ISO], centre(ISO), closed=True)
assert ISO_LINES == 1
# a scalene triangle has no mirror line through any point; check its centroid
# and a few other centres too
SCALENE_LINES = max(count_lines([SCALENE], c, closed=True)
                    for c in [centre(SCALENE), (50, 30), (50, 50), (34, 30)])
assert SCALENE_LINES == 0
HEX_LINES = count_lines([HEXAGON], (50, 32), closed=True)
assert HEX_LINES == 6
assert count_lines([KITE], (50, 40), closed=True) == 1

# The rectangle's diagonal is NOT a mirror line; the square's diagonal is.
def is_mirror(points, a, b):
    deg = math.degrees(math.atan2(b[1] - a[1], b[0] - a[0]))
    segs = segments_of([points], closed=True)
    return same([(reflect(p, a, deg), reflect(q, a, deg)) for p, q in segs], segs)


assert not is_mirror(RECT, RECT[0], RECT[2])
assert is_mirror(SQUARE, SQUARE[0], SQUARE[2])
assert is_mirror(RECT, (50, 12), (50, 48))

# Capital letters drawn as strokes in a 20 x 28 box (taller than wide).
LETTERS = {
    "A": [[(0, 28), (10, 0), (20, 28)], [(5, 14), (15, 14)]],
    "H": [[(0, 0), (0, 28)], [(20, 0), (20, 28)], [(0, 14), (20, 14)]],
    "M": [[(0, 28), (0, 0), (10, 16), (20, 0), (20, 28)]],
    "T": [[(0, 0), (20, 0)], [(10, 0), (10, 28)]],
    "X": [[(0, 0), (20, 28)], [(20, 0), (0, 28)]],
}
LETTER_LINES = {k: count_lines(v, (10, 14)) for k, v in LETTERS.items()}
assert LETTER_LINES == {"A": 1, "H": 2, "M": 1, "T": 1, "X": 2}
ONE_LINE = sum(1 for v in LETTER_LINES.values() if v == 1)
assert ONE_LINE == 3


def letter_items(name, x0, y0):
    return [{"kind": "line", "from": pt(x0 + a[0], y0 + a[1]), "to": pt(x0 + b[0], y0 + b[1])}
            for a, b in segments_of(LETTERS[name])]


LETTER_ROW = []
for i, name in enumerate("AHMTX"):
    LETTER_ROW += letter_items(name, 8 + 32 * i, 6)
    LETTER_ROW.append(label((18 + 32 * i, 44), str(i + 1)))

# A flag: a pole with a triangular pennant pointing right, to show flipping.
def flag(px, top, sign=1, flip_v=False):
    """Pole at x=px from top to top+40; pennant points right (sign 1) or left (-1).
    flip_v puts the pennant at the bottom of the pole."""
    if flip_v:
        tri = [(px, top + 40), (px + sign * 20, top + 32), (px, top + 24)]
    else:
        tri = [(px, top), (px + sign * 20, top + 8), (px, top + 16)]
    return [seg((px, top), (px, top + 40)), poly(tri)]


def mirror_x(p, m):
    return (2 * m - p[0], p[1])


# Check: reflecting the right-pointing flag at x=20 in the mirror x=50 gives
# the left-pointing flag at x=80; sliding gives a right-pointing flag at x=60.
ORIG_TRI = [(20, 10), (40, 18), (20, 26)]
IMG_TRI = [mirror_x(p, 50) for p in ORIG_TRI]
assert IMG_TRI == [(80, 10), (60, 18), (80, 26)]
SLID_TRI = [(x + 40, y) for x, y in ORIG_TRI]
assert sorted(SLID_TRI) != sorted(IMG_TRI)

# s11 panels: each panel 70 wide, mirror in its middle; left flag at mirror-18.
PANELS = []
for i, kind in enumerate(["slide", "flip", "upside"]):
    m = 35 + 70 * i
    left = m - 18
    PANELS += [seg((m, 4), (m, 52), dashed=True)] + flag(left, 8)
    if kind == "flip":
        img = mirror_x((left, 0), m)[0]
        assert img - m == m - left == 18
        PANELS += flag(img, 8, sign=-1)
    elif kind == "slide":
        PANELS += flag(left + 2 * 18, 8)
    else:
        PANELS += flag(mirror_x((left, 0), m)[0], 8, sign=-1, flip_v=True)
    PANELS.append(label((m, 60), "ABC"[i]))

# Grid reflection: a point 3 squares left of a mirror (s4-style number question in the bank).
CELL = 10
P_SQUARES = 3
IMAGE_SQUARES = P_SQUARES
assert IMAGE_SQUARES == 3 and 2 * P_SQUARES == 6
R_SQUARES = 4
assert 2 * R_SQUARES == 8


def grid_figure(squares, alt):
    cols, rows = 10, 4
    items = []
    for c in range(cols + 1):
        items.append(seg((5 + c * CELL, 5), (5 + c * CELL, 5 + rows * CELL)))
    for r in range(rows + 1):
        items.append(seg((5, 5 + r * CELL), (5 + cols * CELL, 5 + r * CELL)))
    m = 5 + 5 * CELL
    items.append(seg((m, 1), (m, 49), dashed=True))
    p = (m - squares * CELL, 5 + 2 * CELL)
    items += [{"kind": "point", "at": pt(*p)}, label((p[0] - 3, p[1] - 5), "P")]
    return fig(110, 50, alt, items)


# ---------- figures ----------

F_HOOK = fig(100, 80, T(
    "A rooftop kite shape: four sides, wide at the top and long at the bottom. A dashed line goes straight down its middle from the top corner to the bottom corner.",
    "چھت پر اڑنے والی پتنگ کی شکل: چار اضلاع، اوپر سے چوڑی اور نیچے سے لمبی۔ ایک ڈیش والی لکیر اوپر والے کونے سے نیچے والے کونے تک بیچ میں سیدھی جاتی ہے۔"),
    [poly(KITE), seg((50, 2), (50, 78), dashed=True)])

F_EQUI = fig(100, 64, T(
    "An equilateral triangle with three dashed lines. Each dashed line goes from a corner to the middle of the opposite side.",
    "ایک مساوی الاضلاع مثلث جس پر تین ڈیش والی لکیریں ہیں۔ ہر لکیر ایک کونے سے سامنے والے ضلع کے درمیان تک جاتی ہے۔"),
    [poly(EQUI)] + [seg(EQUI[i], ((EQUI[(i + 1) % 3][0] + EQUI[(i + 2) % 3][0]) / 2,
                                   (EQUI[(i + 1) % 3][1] + EQUI[(i + 2) % 3][1]) / 2), dashed=True)
                    for i in range(3)])
for it in F_EQUI["items"][1:]:
    a, b = it["from"], it["to"]
    assert is_mirror(EQUI, a, b)

F_RECT = fig(100, 60, T(
    "A rectangle, longer than it is tall, with no lines drawn on it.",
    "ایک مستطیل جو اونچائی سے زیادہ لمبی ہے، اس پر کوئی لکیر نہیں۔"),
    [poly(RECT)])

F_RECT_DIAG = fig(100, 60, T(
    "A rectangle, longer than it is tall. A dashed line goes from its top left corner to its bottom right corner (a diagonal).",
    "ایک مستطیل جو اونچائی سے زیادہ لمبی ہے۔ ایک ڈیش والی لکیر اوپر بائیں کونے سے نیچے دائیں کونے تک جاتی ہے (وتر)۔"),
    [poly(RECT), seg(RECT[0], RECT[2], dashed=True)])

F_SQUARE_DIAG = fig(100, 60, T(
    "A square. A dashed line goes from its top left corner to its bottom right corner (a diagonal).",
    "ایک مربع۔ ایک ڈیش والی لکیر اوپر بائیں کونے سے نیچے دائیں کونے تک جاتی ہے (وتر)۔"),
    [poly(SQUARE), seg(SQUARE[0], SQUARE[2], dashed=True)])

F_ISO = fig(100, 60, T(
    "A triangle with two equal sloping sides and a shorter flat bottom side (an isosceles triangle). No lines are drawn on it.",
    "ایک مثلث جس کے دو ترچھے اضلاع برابر ہیں اور نیچے کا ضلع چھوٹا ہے (مساوی الساقین مثلث)۔ اس پر کوئی لکیر نہیں۔"),
    [poly(ISO)])

F_HEX = fig(100, 64, T(
    "A regular hexagon: six equal sides and six equal corners, like a floor tile. No lines are drawn on it.",
    "ایک باقاعدہ مسدس: چھ برابر اضلاع اور چھ برابر کونے، فرش کی ٹائل کی طرح۔ اس پر کوئی لکیر نہیں۔"),
    [poly(HEXAGON)])

F_LETTERS = fig(164, 52, T(
    "Five capital letters drawn with straight strokes, numbered 1 to 5: A, H, M, T and X. Each letter is taller than it is wide.",
    "سیدھی لکیروں سے بنے پانچ بڑے انگریزی حروف، 1 سے 5 تک نمبر: A، H، M، T اور X۔ ہر حرف چوڑائی سے زیادہ اونچا ہے۔"),
    LETTER_ROW)

F_SLIDE = fig(100, 56, T(
    "A dashed mirror line goes down the middle. On the left is a flag on a pole with its triangle pointing right. On the right, Ayesha drew the same flag, still pointing right.",
    "بیچ میں اوپر سے نیچے ایک ڈیش والی آئینہ لکیر ہے۔ بائیں طرف ڈنڈے پر جھنڈا ہے جس کی تکون دائیں طرف ہے۔ دائیں طرف عائشہ نے وہی جھنڈا بنایا، اس کی تکون بھی دائیں طرف ہے۔"),
    [seg((50, 2), (50, 54), dashed=True)] + flag(20, 10) + flag(60, 10))

F_PANELS = fig(210, 66, T(
    "Three pictures, A, B and C. Each has a dashed mirror line down the middle and the same flag on the left, pointing right. In A the flag on the right also points right. In B the flag on the right points left, towards the mirror. In C the flag on the right points left but hangs at the bottom of its pole.",
    "تین تصویریں، A، B اور C۔ ہر ایک کے بیچ میں ڈیش والی آئینہ لکیر ہے اور بائیں طرف وہی جھنڈا ہے جس کی تکون دائیں طرف ہے۔ A میں دائیں طرف کا جھنڈا بھی دائیں طرف ہے۔ B میں دائیں طرف کا جھنڈا بائیں طرف، آئینے کی طرف ہے۔ C میں دائیں طرف کا جھنڈا بائیں طرف ہے لیکن ڈنڈے کے نیچے لٹکا ہے۔"),
    PANELS)

F_SCALENE = fig(100, 60, T(
    "A triangle whose three sides all have different lengths (a scalene triangle). No lines are drawn on it.",
    "ایک مثلث جس کے تینوں اضلاع کی لمبائیاں مختلف ہیں (مختلف الاضلاع مثلث)۔ اس پر کوئی لکیر نہیں۔"),
    [poly(SCALENE)])

F_SQUARE4 = fig(100, 60, T(
    "A square with four dashed lines: one down the middle, one across the middle and the two diagonals.",
    "ایک مربع جس پر چار ڈیش والی لکیریں ہیں: ایک بیچ میں اوپر سے نیچے، ایک بیچ میں دائیں سے بائیں، اور دونوں وتر۔"),
    [poly(SQUARE), seg((50, 6), (50, 54), True), seg((26, 30), (74, 30), True),
     seg(SQUARE[0], SQUARE[2], True), seg(SQUARE[1], SQUARE[3], True)])

F_CIRCLE = fig(100, 60, T("A circle with a dot at its centre.", "ایک دائرہ جس کے مرکز پر نقطہ ہے۔"),
               [{"kind": "circle", "center": [50, 30], "radius": 24, "fill": True}, {"kind": "point", "at": [50, 30]}])

F_GRID_QB = grid_figure(P_SQUARES, T(
    "A squared grid 10 squares wide and 4 squares tall. A dashed mirror line goes down the middle. Point P is 3 squares to the left of the mirror line.",
    "10 خانے چوڑا اور 4 خانے اونچا چوکور جال۔ بیچ میں اوپر سے نیچے ڈیش والی آئینہ لکیر ہے۔ نقطہ P آئینہ لکیر سے 3 خانے بائیں ہے۔"))

F_GRID_R = grid_figure(R_SQUARES, T(
    "A squared grid 10 squares wide and 4 squares tall. A dashed mirror line goes down the middle. Point P is 4 squares to the left of the mirror line.",
    "10 خانے چوڑا اور 4 خانے اونچا چوکور جال۔ بیچ میں اوپر سے نیچے ڈیش والی آئینہ لکیر ہے۔ نقطہ P آئینہ لکیر سے 4 خانے بائیں ہے۔"))


def with_figure(step, figure):
    step["figure"] = figure
    return step


lesson = {
 "id": "g6-maths-18-line-symmetry",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Recognise line (reflective) symmetry, find and count the lines of symmetry of 2-D shapes and letters, and complete a shape across a mirror line.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Line symmetry", "خطی تشاکل"),
 "estimated_minutes": 15,
 "prerequisites": [{"skill": SY_SHAPES}],
 "misconceptions": [
   {"id": "rect_diagonals", "description": "Thinks a rectangle's diagonals are lines of symmetry, so gives a rectangle 4 lines."},
   {"id": "every_triangle_3", "description": "Thinks every triangle has 3 lines of symmetry."},
   {"id": "slides_not_flips", "description": "Reflects a shape by sliding it across the mirror line instead of flipping it."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_circle", "type": "recall", "step": with_figure({
     "id": "qb_circle", "type": "choice",
     "prompt": T("How many lines of symmetry does a circle have?", "دائرے کی کتنی تشاکل کی لکیریں ہوتی ہیں؟"),
     "options": [
       opt("many", "Infinitely many", "لا تعداد", True,
           "Yes! Every line through the centre folds a circle into two matching halves.", "جی ہاں! مرکز سے گزرنے والی ہر لکیر دائرے کو دو برابر حصوں میں تہہ کرتی ہے۔"),
       opt("four", "4", "4", False,
           "More than 4! Any line through the centre works, so there are infinitely many.", "4 سے زیادہ! مرکز سے گزرنے والی ہر لکیر چلتی ہے، اس لیے لا تعداد ہیں۔"),
       opt("two", "2", "2", False,
           "Not just up-down and across. Every line through the centre works: infinitely many.", "صرف اوپر نیچے اور دائیں بائیں نہیں۔ مرکز سے ہر لکیر چلتی ہے: لا تعداد۔"),
       opt("none", "0", "0", False,
           "Fold a paper circle in half: the halves match. Every line through the centre works.", "کاغذ کا دائرہ آدھا تہہ کریں: حصے مل جاتے ہیں۔ مرکز سے ہر لکیر چلتی ہے۔"),
     ]}, F_CIRCLE)},
   {"id": "qb_apply", "type": "apply", "step": with_figure(number_question(
     "qb_apply",
     T("Point P is 3 squares to the left of the dashed mirror line. How many squares to the right of the mirror line is its reflection?",
       "نقطہ P ڈیش والی آئینہ لکیر سے 3 خانے بائیں ہے۔ اس کا عکس آئینہ لکیر سے کتنے خانے دائیں ہوگا؟"),
     IMAGE_SQUARES,
     T("A reflection is the same distance from the mirror, on the other side.", "عکس آئینے سے اتنے ہی فاصلے پر ہوتا ہے، دوسری طرف۔"),
     T("Right! 3 squares, the same distance on the other side.", "درست! 3 خانے، دوسری طرف اتنا ہی فاصلہ۔"),
     T("P is 3 squares from the mirror, so its reflection is 3 squares on the other side.", "P آئینے سے 3 خانے دور ہے، اس لیے عکس دوسری طرف 3 خانے پر ہے۔"),
     common_wrong=[wrong(2 * P_SQUARES, "6 is the distance from P all the way to its reflection. From the mirror it is 3 squares.",
                         "6 تو P سے اس کے عکس تک کا پورا فاصلہ ہے۔ آئینے سے یہ 3 خانے ہے۔")],
     qtype=None), F_GRID_QB)},
   {"id": "qb_find_error", "type": "find_error", "step": with_figure({
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Sana says: “Every triangle has 3 lines of symmetry.” She points to this triangle. What went wrong?",
                 "ثنا کہتی ہے: ”ہر مثلث کی 3 تشاکل کی لکیریں ہوتی ہیں۔“ وہ اس مثلث کی طرف اشارہ کرتی ہے۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("depends", "Only an equilateral triangle has 3. This one has all sides different, so it has 0.", "صرف مساوی الاضلاع مثلث کی 3 ہوتی ہیں۔ اس کے سب اضلاع مختلف ہیں، اس لیے 0۔", True,
           "Yes! No fold of this triangle makes the halves match.", "جی ہاں! اس مثلث کو کسی طرح تہہ کریں، حصے نہیں ملتے۔"),
       opt("one", "Every triangle has exactly 1.", "ہر مثلث کی بالکل 1 ہوتی ہے۔", False,
           "Only isosceles triangles have 1. This scalene one has 0.", "صرف مساوی الساقین مثلث کی 1 ہوتی ہے۔ اس مختلف الاضلاع کی 0 ہیں۔"),
       opt("nothing", "Nothing, she is right.", "کوئی غلطی نہیں، وہ ٹھیک ہے۔", False,
           "Try folding it: the halves never match. A triangle with all sides different has 0.", "تہہ کر کے دیکھیں: حصے کبھی نہیں ملتے۔ سب اضلاع مختلف ہوں تو 0۔", "every_triangle_3"),
     ]}, F_SCALENE)},
 ]},
 "flashcards": [
   {"id": "f_line", "front": T("What is a line of symmetry?", "تشاکل کی لکیر کیا ہے؟"),
    "back": T("A mirror line that folds a shape into two halves that match exactly.", "آئینہ لکیر جو شکل کو تہہ کر کے دو بالکل برابر حصوں میں بانٹتی ہے۔")},
   {"id": "f_counts", "front": T("Lines of symmetry: square, rectangle, equilateral triangle?", "تشاکل کی لکیریں: مربع، مستطیل، مساوی الاضلاع مثلث؟"),
    "back": T("Square 4, rectangle 2 (not the diagonals), equilateral triangle 3.", "مربع 4، مستطیل 2 (وتر نہیں)، مساوی الاضلاع مثلث 3۔")},
 ],
 "home_tasks": [{"id": "h_fold", "text": T(
   "Fold a sheet of paper in half. Draw half a mosque, a kite or a butterfly against the fold and cut it out. Open it: the fold is a line of symmetry. Then cut out a paper rectangle, fold it along a diagonal and see that the halves do not match. Write the capital letters of your name and mark any lines of symmetry with a ruler.",
   "کاغذ کو آدھا تہہ کریں۔ تہہ کی طرف آدھی مسجد، پتنگ یا تتلی بنا کر کاٹیں۔ کھولیں: تہہ تشاکل کی لکیر ہے۔ پھر کاغذ کی مستطیل کاٹیں، اسے وتر پر تہہ کریں اور دیکھیں کہ حصے نہیں ملتے۔ اپنے نام کے بڑے انگریزی حروف لکھیں اور فٹے سے ان کی تشاکل کی لکیریں لگائیں۔")}],
 "glossary": [T("Line of symmetry", "تشاکل کی لکیر"), T("Mirror line", "آئینہ لکیر"),
              T("Reflection", "عکس"), T("Diagonal", "وتر")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Fold a rooftop kite down the middle. Do the two halves match exactly? Let's find out!",
                     "چھت والی پتنگ کو بیچ سے تہہ کریں۔ کیا دونوں آدھے بالکل ملتے ہیں؟ آئیں دیکھیں!"),
    "figure": F_HOOK,
    "text": T("Today we look for lines that fold a shape into two matching halves. First, a quick check.",
              "آج ہم وہ لکیریں ڈھونڈیں گے جو شکل کو تہہ کر کے دو برابر حصے بناتی ہیں۔ پہلے ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("How many vertices (corners) does a pentagon have?", "مخمس کے کتنے راس (کونے) ہوتے ہیں؟"),
     5,
     T("Penta means five. Count the sides: there are as many corners as sides.", "مخمس کے پانچ اضلاع ہیں۔ جتنے اضلاع اتنے ہی کونے۔"),
     T("Right! 5 sides and 5 vertices.", "درست! 5 اضلاع اور 5 راس۔"),
     T("A pentagon has 5 sides and 5 vertices.", "مخمس کے 5 اضلاع اور 5 راس ہوتے ہیں۔"),
     common_wrong=[wrong(6, "6 is a hexagon. A pentagon has 5.", "6 مسدس کے ہوتے ہیں۔ مخمس کے 5۔"),
                   wrong(4, "4 is a quadrilateral. A pentagon has 5.", "4 چوکور کے ہوتے ہیں۔ مخمس کے 5۔")],
     qtype="recall", skill=SY_SHAPES),
   {"id": "s3_explain", "type": "explain",
    "character": say("happy", "A mirror line is like a fold. Each side is the flipped picture of the other!",
                     "آئینہ لکیر ایک تہہ کی طرح ہے۔ ہر طرف دوسری طرف کی الٹی تصویر ہے!"),
    "figure": F_EQUI,
    "text": T("A line of symmetry, or mirror line, folds a shape into two halves that match exactly. Each half is the reflection of the other, so we call this reflective symmetry. Some shapes have more than one: an equilateral triangle has 3, a square has 4, a rectangle has only 2. A circle has infinitely many. To test a line, imagine folding along it: if the two halves sit exactly on top of each other, it is a line of symmetry.",
              "تشاکل کی لکیر یا آئینہ لکیر شکل کو تہہ کر کے دو بالکل برابر حصوں میں بانٹتی ہے۔ ہر حصہ دوسرے کا عکس ہوتا ہے، اس لیے اسے انعکاسی تشاکل کہتے ہیں۔ کچھ شکلوں کی ایک سے زیادہ ہوتی ہیں: مساوی الاضلاع مثلث کی 3، مربع کی 4، اور مستطیل کی صرف 2۔ دائرے کی لا تعداد ہوتی ہیں۔ لکیر کو جانچنے کے لیے اس پر تہہ کرنے کا سوچیں: اگر دونوں حصے بالکل ایک دوسرے پر آ جائیں تو یہ تشاکل کی لکیر ہے۔")},
   with_figure(number_question(
     "s4_rectangle",
     T("How many lines of symmetry does this rectangle have?", "اس مستطیل کی کتنی تشاکل کی لکیریں ہیں؟"),
     RECT_LINES,
     T("Try folding it down the middle, across the middle and corner to corner.", "بیچ سے اوپر نیچے، بیچ سے دائیں بائیں اور کونے سے کونے تک تہہ کر کے سوچیں۔"),
     T("Right! 2: one down the middle and one across the middle.", "درست! 2: ایک بیچ میں اوپر نیچے اور ایک بیچ میں دائیں بائیں۔"),
     T("A rectangle has 2 lines of symmetry, through the middles of opposite sides. The diagonals don't work.", "مستطیل کی 2 تشاکل کی لکیریں ہیں، آمنے سامنے اضلاع کے درمیان سے۔ وتر نہیں چلتے۔"),
     common_wrong=[wrong(4, "The diagonals are not lines of symmetry: fold a rectangle corner to corner and the halves don't match. It has 2.",
                         "وتر تشاکل کی لکیریں نہیں: مستطیل کو کونے سے کونے تہہ کریں تو حصے نہیں ملتے۔ اس کی 2 ہیں۔", "rect_diagonals"),
                   wrong(1, "There is a second one: across the middle as well as down the middle. It has 2.",
                         "ایک اور بھی ہے: اوپر نیچے کے ساتھ دائیں بائیں بھی۔ اس کی 2 ہیں۔")]), F_RECT),
   with_figure({"id": "s5_diagonal", "type": "choice", "question_type": "apply",
    "prompt": T("Is the dashed diagonal a line of symmetry of this rectangle?", "کیا ڈیش والا وتر اس مستطیل کی تشاکل کی لکیر ہے؟"),
    "options": [
      opt("no", "No: folded along it, the halves don't match.", "نہیں: اس پر تہہ کریں تو حصے نہیں ملتے۔", True,
          "Yes! The corners stick out past each other. Only a square's diagonals are mirror lines.", "جی ہاں! کونے ایک دوسرے سے باہر نکل جاتے ہیں۔ صرف مربع کے وتر آئینہ لکیریں ہیں۔"),
      opt("yes", "Yes: it cuts the rectangle into two equal halves.", "ہاں: یہ مستطیل کو دو برابر حصوں میں کاٹتا ہے۔", False,
          "The two triangles are equal in size, but folding one onto the other doesn't make them match. So it is not a line of symmetry.", "دونوں مثلثیں برابر ہیں، لیکن ایک کو دوسری پر تہہ کریں تو نہیں ملتیں۔ اس لیے یہ تشاکل کی لکیر نہیں۔", "rect_diagonals"),
    ]}, F_RECT_DIAG),
   with_figure(number_question(
     "s6_isosceles",
     T("This triangle has two equal sides. How many lines of symmetry does it have?", "اس مثلث کے دو اضلاع برابر ہیں۔ اس کی کتنی تشاکل کی لکیریں ہیں؟"),
     ISO_LINES,
     T("Only one fold makes the two equal sides land on each other.", "صرف ایک تہہ سے دونوں برابر اضلاع ایک دوسرے پر آتے ہیں۔"),
     T("Right! 1: from the top corner down to the middle of the bottom side.", "درست! 1: اوپر والے کونے سے نیچے والے ضلع کے درمیان تک۔"),
     T("An isosceles triangle has 1 line of symmetry, from the top corner to the middle of the bottom.", "مساوی الساقین مثلث کی 1 تشاکل کی لکیر ہے، اوپر کے کونے سے نیچے کے درمیان تک۔"),
     common_wrong=[wrong(3, "Only an equilateral triangle, with all three sides equal, has 3. This one has 1.",
                         "صرف مساوی الاضلاع مثلث، جس کے تینوں اضلاع برابر ہوں، کی 3 ہیں۔ اس کی 1 ہے۔", "every_triangle_3")]), F_ISO),
   with_figure(number_question(
     "s7_letters",
     T("Look at the letters A, H, M, T and X. How many of them have exactly one line of symmetry?",
       "حروف A، H، M، T اور X کو دیکھیں۔ ان میں سے کتنے حروف کی بالکل ایک تشاکل کی لکیر ہے؟"),
     ONE_LINE,
     T("For each letter, check down the middle and across the middle.", "ہر حرف کو بیچ سے اوپر نیچے اور دائیں بائیں جانچیں۔"),
     T("Right! A, M and T have one line, straight down. H and X have two.", "درست! A، M اور T کی ایک لکیر ہے، سیدھی نیچے۔ H اور X کی دو ہیں۔"),
     T("A, M and T have 1 line each (down the middle). H and X have 2 (down and across). So the answer is 3.", "A، M اور T کی 1، 1 لکیر ہے (بیچ میں نیچے)۔ H اور X کی 2 ہیں (نیچے اور دائیں بائیں)۔ اس لیے جواب 3۔"),
     common_wrong=[wrong(5, "H and X also fold across the middle, so they have 2 lines, not 1. The answer is 3.",
                         "H اور X دائیں بائیں سے بھی تہہ ہوتے ہیں، اس لیے ان کی 2 لکیریں ہیں۔ جواب 3۔"),
                   wrong(2, "That counts H and X, which have 2 lines. The letters with exactly 1 are A, M and T: 3.",
                         "یہ H اور X ہیں جن کی 2 لکیریں ہیں۔ بالکل 1 والے A، M اور T ہیں: 3۔")]), F_LETTERS),
   with_figure(number_question(
     "s8_hexagon",
     T("A floor tile is a regular hexagon. How many lines of symmetry does it have?", "فرش کی ایک ٹائل باقاعدہ مسدس ہے۔ اس کی کتنی تشاکل کی لکیریں ہیں؟"),
     HEX_LINES,
     T("Lines go corner to opposite corner, and also middle of a side to middle of the opposite side.", "لکیریں کونے سے سامنے والے کونے تک جاتی ہیں، اور ضلع کے درمیان سے سامنے والے ضلع کے درمیان تک بھی۔"),
     T("Right! 6: 3 through opposite corners and 3 through opposite sides.", "درست! 6: 3 آمنے سامنے کونوں سے اور 3 آمنے سامنے اضلاع سے۔"),
     T("3 lines join opposite corners and 3 join the middles of opposite sides: 6 in all.", "3 لکیریں آمنے سامنے کونے ملاتی ہیں اور 3 آمنے سامنے اضلاع کے درمیان: کل 6۔"),
     common_wrong=[wrong(3, "That is only the corner-to-corner lines. Side-to-side lines work too: 6 in all.",
                         "یہ صرف کونے سے کونے والی ہیں۔ ضلع سے ضلع والی بھی چلتی ہیں: کل 6۔"),
                   wrong(12, "A regular hexagon has as many lines of symmetry as sides: 6.",
                         "باقاعدہ مسدس کی جتنے اضلاع اتنی ہی تشاکل کی لکیریں: 6۔")]), F_HEX),
   with_figure({"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Ayesha reflected the flag in the dashed mirror line. Her picture is on the right. What went wrong?",
                "عائشہ نے جھنڈے کا ڈیش والی آئینہ لکیر میں عکس بنایا۔ اس کی تصویر دائیں طرف ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("slid", "She slid the flag across. A reflection flips it, so the flag should point left, towards the mirror.", "اس نے جھنڈا کھسکا دیا۔ عکس الٹ جاتا ہے، اس لیے جھنڈا بائیں طرف، آئینے کی طرف ہونا چاہیے۔", True,
          "Yes! In a mirror, the side nearest the mirror stays nearest the mirror.", "جی ہاں! آئینے میں جو حصہ آئینے کے قریب ہے وہ قریب ہی رہتا ہے۔"),
      opt("upside", "The flag should be upside down.", "جھنڈا الٹا (اوپر نیچے) ہونا چاہیے۔", False,
          "A down-the-middle mirror swaps left and right, not top and bottom. The flag should point left.", "اوپر سے نیچے والا آئینہ دائیں بائیں بدلتا ہے، اوپر نیچے نہیں۔ جھنڈا بائیں طرف ہونا چاہیے۔"),
      opt("nothing", "Nothing, it is correct.", "کوئی غلطی نہیں، یہ درست ہے۔", False,
          "That is a slide, not a reflection. Folded along the mirror, the two flags would not match.", "یہ کھسکانا ہے، عکس نہیں۔ آئینہ لکیر پر تہہ کریں تو دونوں جھنڈے نہیں ملیں گے۔", "slides_not_flips"),
    ]}, F_SLIDE),
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "A rectangle's diagonal cuts it into two equal triangles. So why isn't it a line of symmetry? Can you teach me?",
                     "مستطیل کا وتر اسے دو برابر مثلثوں میں کاٹتا ہے۔ پھر یہ تشاکل کی لکیر کیوں نہیں؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "figure": F_RECT_DIAG,
    "task": T("In your own words: why is a rectangle's diagonal not a line of symmetry, even though it makes two equal halves?",
              "اپنے الفاظ میں بتائیں: مستطیل کا وتر تشاکل کی لکیر کیوں نہیں، حالانکہ یہ دو برابر حصے بناتا ہے؟"),
    "key_idea": "A line of symmetry must fold one half exactly onto the other. If you fold a rectangle along a diagonal, the corners stick out and the halves don't sit on top of each other. The two triangles are equal, but only by turning one, not by folding.",
    "levels": {
      "got_it": "Says that folding along the diagonal makes the halves not match (corners stick out), so equal halves are not enough; it has to be a fold.",
      "partly": "Says the halves don't match when folded, but gives no reason, or says equal halves are not enough without mentioning folding.",
      "not_yet": "Says it is a line of symmetry, or gives no reason."},
    "keywords": [
      ["fold", "تہہ", "tah"],
      ["match", "on top", "stick out", "ملتے", "باہر", "milte"],
      ["corner", "کونے", "kone"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Equal halves are not enough: the fold must make them match.", "بہت خوب! برابر حصے کافی نہیں: تہہ کرنے پر ملنا ضروری ہے۔"),
      "partly": T("Good start! Now say what happens to the corners when you fold along the diagonal.", "اچھی شروعات! اب بتائیں وتر پر تہہ کرنے سے کونوں کا کیا ہوتا ہے۔"),
      "not_yet": T("Fold a paper rectangle corner to corner. Do the halves sit exactly on top of each other?", "کاغذ کی مستطیل کونے سے کونے تہہ کریں۔ کیا حصے بالکل ایک دوسرے پر آتے ہیں؟")},
    "limit_per_day": 3, "max_attempts": 2},
   with_figure({"id": "s11_complete", "type": "choice", "question_type": "apply",
    "prompt": T("Bilal is drawing a truck-art pattern. He has drawn the flag on the left of each dashed mirror line. Which picture, A, B or C, shows it correctly reflected?",
                "بلال ٹرک آرٹ کا نمونہ بنا رہا ہے۔ اس نے ہر ڈیش والی آئینہ لکیر کے بائیں طرف جھنڈا بنایا ہے۔ کون سی تصویر، A، B یا C، میں اس کا درست عکس ہے؟"),
    "options": [
      opt("a", "A", "A", False,
          "In A the flag was slid across, not flipped. A reflection points back towards the mirror: B.", "A میں جھنڈا کھسکایا گیا، الٹا نہیں گیا۔ عکس آئینے کی طرف ہوتا ہے: B۔", "slides_not_flips"),
      opt("b", "B", "B", True,
          "Yes! The flag flips: it is the same distance from the mirror and points towards it.", "جی ہاں! جھنڈا الٹ جاتا ہے: آئینے سے اتنا ہی دور اور اس کی طرف۔"),
      opt("c", "C", "C", False,
          "C is also turned upside down. A down-the-middle mirror only swaps left and right: B.", "C اوپر نیچے بھی الٹا ہے۔ اوپر سے نیچے والا آئینہ صرف دائیں بائیں بدلتا ہے: B۔"),
    ]}, F_PANELS),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Fold, match, flip! You can spot mirror lines everywhere now. Well done!",
                     "تہہ کریں، ملائیں، الٹیں! اب آپ ہر جگہ آئینہ لکیریں پہچان سکتے ہیں۔ شاباش!"),
    "figure": F_SQUARE4,
    "text": T("A line of symmetry folds a shape into two halves that match exactly. Square 4, rectangle 2 (not the diagonals), equilateral triangle 3, isosceles triangle 1, scalene triangle 0, regular hexagon 6, circle infinitely many. To reflect a shape, flip it: each point lands the same distance from the mirror on the other side.",
              "تشاکل کی لکیر شکل کو تہہ کر کے دو بالکل برابر حصے بناتی ہے۔ مربع 4، مستطیل 2 (وتر نہیں)، مساوی الاضلاع مثلث 3، مساوی الساقین مثلث 1، مختلف الاضلاع مثلث 0، باقاعدہ مسدس 6، دائرہ لا تعداد۔ عکس بنانے کے لیے شکل الٹیں: ہر نقطہ دوسری طرف آئینے سے اتنے ہی فاصلے پر آتا ہے۔"),
    "points": [T("Test a line by folding: the halves must match.", "لکیر کو تہہ کر کے جانچیں: حصے ملنے چاہییں۔"),
               T("A rectangle's diagonals are not mirror lines.", "مستطیل کے وتر آئینہ لکیریں نہیں۔"),
               T("Reflect by flipping, not sliding.", "عکس الٹ کر بنائیں، کھسکا کر نہیں۔")]},
 ],
 "review_questions": [
   {"id": "r_square_diag", "type": "apply", "skill": SKILL, "step": with_figure({
     "id": "r_square_diag", "type": "choice",
     "prompt": T("Is the dashed diagonal a line of symmetry of this square?", "کیا ڈیش والا وتر اس مربع کی تشاکل کی لکیر ہے؟"),
     "options": [
       opt("yes", "Yes", "ہاں", True,
           "Right! A square's sides are all equal, so folding corner to corner makes the halves match.", "درست! مربع کے سب اضلاع برابر ہیں، اس لیے کونے سے کونے تہہ کرنے پر حصے مل جاتے ہیں۔"),
       opt("no", "No", "نہیں", False,
           "For a square it works: the halves match when folded corner to corner. (For a rectangle it doesn't.)", "مربع کے لیے یہ چلتا ہے: کونے سے کونے تہہ کرنے پر حصے ملتے ہیں۔ (مستطیل کے لیے نہیں۔)"),
     ]}, F_SQUARE_DIAG)},
   {"id": "r_grid", "type": "apply", "skill": SKILL, "step": with_figure(number_question(
     "r_grid",
     T("Point P is 4 squares to the left of the dashed mirror line. How many squares to the right of the mirror line is its reflection?",
       "نقطہ P ڈیش والی آئینہ لکیر سے 4 خانے بائیں ہے۔ اس کا عکس آئینہ لکیر سے کتنے خانے دائیں ہوگا؟"),
     R_SQUARES,
     T("Same distance from the mirror, on the other side.", "آئینے سے اتنا ہی فاصلہ، دوسری طرف۔"),
     T("Right! 4 squares.", "درست! 4 خانے۔"),
     T("P is 4 squares from the mirror, so its reflection is 4 squares on the other side.", "P آئینے سے 4 خانے دور ہے، اس لیے عکس دوسری طرف 4 خانے پر ہے۔"),
     common_wrong=[wrong(2 * R_SQUARES, "8 is from P to its reflection. From the mirror it is 4.", "8 تو P سے عکس تک ہے۔ آئینے سے 4 ہے۔")],
     qtype=None), F_GRID_R)},
 ],
 "teacher_notes": [
   "Written fresh for the Symmetry unit. No textbook text or exercises were used.",
   "Every count of lines of symmetry in this lesson (and the letters A, H, M, T, X) was checked in the script by reflecting the drawn shape in every line through its centre. Letters are drawn taller than wide, so X has 2 lines, not 4; if a child draws X inside a square, its diagonal strokes are also mirror lines.",
   "The two big slips are giving a rectangle 4 lines (the diagonals cut it into equal halves but don't fold onto each other) and sliding a shape across the mirror instead of flipping it. Paper folding settles both quickly.",
   "Urdu terms to check: خطی تشاکل (line symmetry), تشاکل کی لکیر (line of symmetry), آئینہ لکیر (mirror line), انعکاسی تشاکل (reflective symmetry), عکس (reflection), وتر (diagonal), مساوی الاضلاع / مساوی الساقین / مختلف الاضلاع مثلث, مسدس (hexagon), مخمس (pentagon), راس (vertex), لا تعداد (infinitely many).",
   "The figures and numbers were worked out in content/sources/g6-maths-18/line_symmetry.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)
