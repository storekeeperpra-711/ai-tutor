import math

from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, AN_TRIANGLE, CO_BISECTORS, CO_ANGLES,
                    CO_WORD_PROBLEMS)

SKILL = CO_WORD_PROBLEMS
LINE, POINT, TRI = 180, 360, 180


# ---------- drawing helpers (screen coordinates, y down) ----------

def r1(p):
    return [round(p[0], 1), round(p[1], 1)]


def heading(v, p):
    """Direction from v to p in degrees, clockwise on screen from +x."""
    return math.degrees(math.atan2(p[1] - v[1], p[0] - v[0])) % 360


def along(v, deg, d):
    a = math.radians(deg)
    return (v[0] + d * math.cos(a), v[1] + d * math.sin(a))


def mark(v, a, b, text, r=7, gap=7):
    """An arc for the smaller angle a-v-b, and a label just outside it."""
    h1, h2 = heading(v, a), heading(v, b)
    sweep = (h2 - h1) % 360
    if sweep > 180:
        h1, sweep = h2, 360 - sweep
    mid = along(v, h1 + sweep / 2, r + gap)
    return [{"kind": "arc", "center": r1(v), "radius": r, "start": round(h1, 1), "sweep": round(sweep, 1)},
            {"kind": "label", "at": r1(mid), "text": text}]


def right_mark(v, a, b, s=5):
    """A small square in the corner a-v-b (a right angle)."""
    p = along(v, heading(v, a), s)
    q = along(v, heading(v, b), s)
    c = (p[0] + q[0] - v[0], p[1] + q[1] - v[1])
    return [{"kind": "polygon", "points": [r1(v), r1(p), r1(c), r1(q)]}]


def tick(a, b, s=3):
    """A short tick across the middle of side a-b (marks equal sides)."""
    m = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
    h = heading(a, b) + 90
    return [{"kind": "line", "from": r1(along(m, h, s)), "to": r1(along(m, h + 180, s))}]


def triangle(left, length, alpha, beta):
    """Base from `left` going right; base angles alpha (left) and beta (right).
    Returns A, B, C with C above the base."""
    a = left
    b = (left[0] + length, left[1])
    ac = length * math.sin(math.radians(beta)) / math.sin(math.radians(alpha + beta))
    c = along(a, -alpha, ac)
    return a, b, c


def figure(w, h, alt, items):
    for it in items:
        pts = []
        for k in ("points",):
            pts += it.get(k, [])
        for k in ("from", "to", "center", "at"):
            if k in it:
                pts.append(it[k])
        for x, y in pts:
            assert 0 <= x <= w and 0 <= y <= h, (alt["en"][:30], it)
        if it["kind"] in ("arc", "circle"):
            cx, cy = it["center"]
            rad = it["radius"]
            assert rad <= cx <= w - rad and rad <= cy <= h - rad, it
    return {"width": w, "height": h, "alt": alt, "items": items}


def poly(*pts, fill=False):
    item = {"kind": "polygon", "points": [r1(p) for p in pts]}
    if fill:
        item["fill"] = True
    return item


def seg(a, b, dashed=False):
    item = {"kind": "line", "from": r1(a), "to": r1(b)}
    if dashed:
        item["style"] = "dashed"
    return item


def missing(total, *known):
    m = total - sum(known)
    assert 0 < m < total, (total, known)
    return m


# ---------- numbers ----------

# s2: angles of a triangle
assert TRI == 180
# s4: a straight line with 125° and a
S4 = missing(LINE, 125)
assert S4 == 55 and POINT - 125 == 235
# s5: triangle 50°, 70°, x (360 by mistake: 240)
S5 = missing(TRI, 50, 70)
assert S5 == 60 and POINT - 120 == 240
# s6: exterior angle at B, opposite interior angles 40° and 75°
S6 = 40 + 75
INNER6 = missing(TRI, 40, 75)
assert S6 == 115 and INNER6 == 65 and INNER6 + S6 == LINE and INNER6 != S6
# s7: isosceles, base angle 65°, apex a (forgetting the other base angle: 115)
S7 = missing(TRI, 65, 65)
assert S7 == 50 and missing(TRI, 65) == 115
# s8: ramp 15° from the ground, wall at 90°, angle at the top
S8 = missing(TRI, 90, 15)
assert S8 == 75 and missing(TRI, 15) == 165 and POINT - 105 == 255
# s9: interior 50° and 60°, exterior at the third corner (adjacent interior: 70)
S9 = 50 + 60
assert S9 == 110 and missing(TRI, 50, 60) == 70 and S9 + 70 == LINE
# s10: exterior angle = sum of the two opposite interior angles (any triangle)
for p, q in [(40, 75), (50, 60), (30, 100)]:
    assert LINE - missing(TRI, p, q) == p + q
# unit test
U1 = 60 // 2          # kite: long stick bisects the 60 cm cross stick
assert U1 == 30
U2 = 90 // 2          # bisect a constructed right angle
assert U2 == 45
U3 = TRI // 3         # equilateral triangle (how a 60° angle is constructed)
assert U3 == 60 and 3 * U3 == TRI
U4_SETS = {"equal": (60, 60, 60), "two_right": (90, 90, 30), "too_big": (100, 50, 40)}
assert sum(U4_SETS["equal"]) == TRI and sum(U4_SETS["two_right"]) == 210 and sum(U4_SETS["too_big"]) == 190
U5 = 45 + 45          # carpenter: two 45° cuts make the frame corner
assert U5 == 90
# question bank
QB = missing(TRI, 30) // 2   # isosceles, apex 30°, each base angle
assert QB == 75 and missing(TRI, 30) == 150
QB_ERR = missing(TRI, 35, 85)  # Sana used 360 and got 240
assert QB_ERR == 60 and POINT - 35 - 85 == 240
# review
R1 = missing(POINT, 110, 95, 85)
assert R1 == 70 and 110 + 95 + 85 == 290
R2 = missing(TRI, 90, 35)
assert R2 == 55 and missing(TRI, 35) == 145


# ---------- figures ----------

def kite_fig(alt, labels=True, half=False):
    top, bottom, left, right = (50, 6), (50, 70), (26, 26), (74, 26)
    o = (50, 26)
    items = [poly(top, right, bottom, left, fill=True),
             seg(top, bottom), seg(left, right)]
    items += right_mark(o, right, bottom)
    if half:
        items += [{"kind": "label", "at": [38, 31], "text": "?"},
                  {"kind": "label", "at": [62, 31], "text": "?"},
                  {"kind": "point", "at": [50, 26]}]
    return figure(100, 76, alt, items)


F1 = kite_fig(T("A kite frame: a long upright stick and a shorter cross stick meet inside a diamond shape. A small square at the crossing shows the sticks meet at a right angle.",
                "پتنگ کا ڈھانچا: ایک لمبی کھڑی تیلی اور ایک چھوٹی آڑی تیلی ہیرے جیسی شکل کے اندر ملتی ہیں۔ ملنے کی جگہ پر چھوٹا سا مربع بتاتا ہے کہ تیلیاں زاویہ قائمہ پر ملتی ہیں۔"))

# s3: exterior angle picture with a, b and a+b
A3, B3, C3 = triangle((12, 58), 52, 45, 70)
D3 = (94, 58)
F3 = figure(100, 66, T(
    "A triangle sits on a straight line. The two angles inside it at the top and on the left are marked a and b. The base is extended to the right, and the outside angle there is marked a+b.",
    "ایک مثلث سیدھی لکیر پر ہے۔ اس کے اندر اوپر اور بائیں والے زاویوں پر a اور b لکھا ہے۔ قاعدہ دائیں طرف بڑھایا گیا ہے، اور وہاں باہر والے زاویے پر a+b لکھا ہے۔"),
    [poly(A3, B3, C3, fill=True), seg(B3, D3)]
    + mark(C3, A3, B3, "a") + mark(A3, B3, C3, "b", r=8, gap=6)
    + mark(B3, D3, C3, "a+b", r=6, gap=9))
assert C3[1] > 0

# s4: a straight line with 125° and a
O4 = (50, 48)
L4, R4 = (8, 48), (92, 48)
P4 = along(O4, 360 - 125, 38)
F4 = figure(100, 60, T("A straight line with a point in the middle. A ray goes up and to the left from the point. The angle on the right of the ray is 125°. The angle on the left is a.",
                       "ایک سیدھی لکیر جس کے درمیان ایک نقطہ ہے۔ نقطے سے ایک شعاع اوپر بائیں طرف جاتی ہے۔ شعاع کے دائیں طرف کا زاویہ 125° ہے۔ بائیں طرف کا زاویہ a ہے۔"),
            [seg(L4, R4), seg(O4, P4), {"kind": "point", "at": r1(O4)}]
            + mark(O4, R4, P4, "125°", r=8, gap=9) + mark(O4, L4, P4, "a", r=10, gap=6))

# s5: triangle 50°, 70°, x
A5, B5, C5 = triangle((20, 64), 60, 50, 70)
F5 = figure(100, 72, T("A triangle. The angle at the bottom left is 50°, the angle at the bottom right is 70°, and the angle at the top is x.",
                       "ایک مثلث۔ نیچے بائیں زاویہ 50° ہے، نیچے دائیں زاویہ 70° ہے، اور اوپر والا زاویہ x ہے۔"),
            [poly(A5, B5, C5, fill=True)]
            + mark(A5, B5, C5, "50°", r=8, gap=9) + mark(B5, A5, C5, "70°", r=8, gap=9)
            + mark(C5, A5, B5, "x", r=7, gap=6))

# s6: exterior angle at B; interior A = 40°, C = 75°, B inner = 65°
A6, B6, C6 = triangle((12, 60), 56, 40, INNER6)
D6 = (94, 60)
F6 = figure(100, 70, T("A triangle with its base extended to the right. Inside, the angle at the bottom left is 40° and the angle at the top is 75°. The outside angle made by the extended base at the bottom right is x.",
                       "ایک مثلث جس کا قاعدہ دائیں طرف بڑھایا گیا ہے۔ اندر نیچے بائیں زاویہ 40° اور اوپر والا زاویہ 75° ہے۔ نیچے دائیں بڑھائے ہوئے قاعدے سے بننے والا باہر کا زاویہ x ہے۔"),
            [poly(A6, B6, C6, fill=True), seg(B6, D6)]
            + mark(A6, B6, C6, "40°", r=9, gap=9) + mark(C6, A6, B6, "75°", r=6, gap=8)
            + mark(B6, D6, C6, "x", r=7, gap=6))

# s7: isosceles with base angles 65°, apex a
A7, B7, C7 = triangle((25, 66), 50, 65, 65)
F7 = figure(100, 74, T("A tall triangle with two equal sides, each marked with a small tick. The angle at the bottom left is 65°. The angle at the top is a.",
                       "ایک اونچی مثلث جس کے دو اضلاع برابر ہیں، ہر ایک پر چھوٹا سا نشان ہے۔ نیچے بائیں زاویہ 65° ہے۔ اوپر والا زاویہ a ہے۔"),
            [poly(A7, B7, C7, fill=True)] + tick(A7, C7) + tick(B7, C7)
            + mark(A7, B7, C7, "65°", r=7, gap=9) + mark(C7, A7, B7, "a", r=7, gap=6))

# s8: ramp 15° to the ground, upright wall
A8 = (16, 46)
B8 = (90, 46)
C8 = (90, 46 - 74 * math.tan(math.radians(15)))
F8 = figure(100, 62, T("A ramp drawn as a long thin right triangle. The ground runs along the bottom, an upright wall stands on the right with a right-angle square at its foot, and the ramp slopes up from the left. The angle between the ramp and the ground is 15°. The angle at the top, between the ramp and the wall, is x.",
                       "ڈھلوان ایک لمبی پتلی قائمہ زاویہ مثلث کی شکل میں۔ نیچے زمین ہے، دائیں طرف کھڑی دیوار ہے جس کے نیچے قائمہ زاویے کا مربع ہے، اور ڈھلوان بائیں سے اوپر جاتی ہے۔ ڈھلوان اور زمین کے درمیان زاویہ 15° ہے۔ اوپر ڈھلوان اور دیوار کے درمیان زاویہ x ہے۔"),
            [poly(A8, B8, C8, fill=True)] + right_mark(B8, A8, C8)
            + mark(A8, B8, C8, "15°", r=14, gap=9) + mark(C8, A8, B8, "x", r=6, gap=6))

# s9: interior 50° and 60°, exterior at B
A9, B9, C9 = triangle((12, 60), 56, 50, 70)
D9 = (94, 60)
F9 = figure(100, 70, T("A triangle with its base extended to the right. Inside, the angle at the bottom left is 50° and the angle at the top is 60°. The outside angle at the bottom right is x.",
                       "ایک مثلث جس کا قاعدہ دائیں طرف بڑھایا گیا ہے۔ اندر نیچے بائیں زاویہ 50° اور اوپر والا زاویہ 60° ہے۔ نیچے دائیں باہر والا زاویہ x ہے۔"),
            [poly(A9, B9, C9, fill=True), seg(B9, D9)]
            + mark(A9, B9, C9, "50°", r=8, gap=9) + mark(C9, A9, B9, "60°", r=6, gap=8)
            + mark(B9, D9, C9, "x", r=7, gap=6))

FU1 = kite_fig(T("A kite frame. The long upright stick crosses the middle of the shorter cross stick at a right angle, shown by a small square. The two halves of the cross stick are each marked with a question mark.",
                 "پتنگ کا ڈھانچا۔ لمبی کھڑی تیلی چھوٹی آڑی تیلی کے درمیان سے زاویہ قائمہ پر گزرتی ہے، جو چھوٹا سا مربع دکھاتا ہے۔ آڑی تیلی کے دونوں آدھے حصوں پر سوالیہ نشان ہے۔"), half=True)

# u5: carpenter's frame corner, two strips cut at 45°
OU = (12, 62)
FU5 = figure(100, 72, T("The corner of a wooden photo frame. One strip lies flat along the bottom and one stands up on the left. A dashed line runs from the outer corner up and to the right, where the two cut ends meet. Each strip makes a 45° angle with the dashed line.",
                        "لکڑی کے فوٹو فریم کا ایک کونا۔ ایک پٹی نیچے لیٹی ہے اور ایک بائیں طرف کھڑی ہے۔ باہر کے کونے سے اوپر دائیں ایک نقطہ دار لکیر جاتی ہے، جہاں دونوں کٹے سرے ملتے ہیں۔ ہر پٹی نقطہ دار لکیر سے 45° کا زاویہ بناتی ہے۔"),
             [poly(OU, (92, 62), (92, 48), (26, 48), fill=True),
              poly(OU, (26, 48), (26, 6), (12, 6), fill=True),
              seg(OU, (26, 48), dashed=True)]
             + mark(OU, (92, 62), (26, 48), "45°", r=10, gap=12)
             + mark(OU, (12, 6), (26, 48), "45°", r=10, gap=12))


lesson = {
 "id": "g6-maths-19-unknown-angles-and-construction-problems",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Find unknown angles on a straight line, around a point and in triangles (including exterior angles, equilateral and isosceles triangles), and solve simple real-life construction problems.",
                      "textbook": f"{REF}, 10.4"}],
 "skills": [SKILL],
 "title": T("Unknown angles and construction problems", "نامعلوم زاویے اور تعمیر کے سوالات"),
 "estimated_minutes": 18,
 "prerequisites": [{"skill": CO_ANGLES}, {"skill": AN_TRIANGLE}, {"skill": CO_BISECTORS}],
 "misconceptions": [
   {"id": "triangle_is_360", "description": "Uses 360° as the total of the angles of a triangle."},
   {"id": "exterior_is_adjacent", "description": "Thinks the exterior angle equals the interior angle next to it."},
   {"id": "isosceles_forgot", "description": "Forgets that the two base angles of an isosceles triangle are equal."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_exterior", "type": "recall", "step": {
     "id": "qb_exterior", "type": "choice",
     "prompt": T("The exterior angle of a triangle is equal to…", "مثلث کا بیرونی زاویہ برابر ہوتا ہے…"),
     "options": [
       opt("sum", "the sum of the two opposite interior angles", "دو سامنے والے اندرونی زاویوں کے مجموعے کے", True,
           "Yes! Exterior angle = sum of the two opposite interior angles.", "جی ہاں! بیرونی زاویہ = سامنے والے دو اندرونی زاویوں کا مجموعہ۔"),
       opt("next", "the interior angle next to it", "ساتھ والے اندرونی زاویے کے", False,
           "The angle next to it makes 180° with it, so they are usually different.", "ساتھ والا زاویہ اس کے ساتھ مل کر 180° بناتا ہے، تو عموماً دونوں مختلف ہوتے ہیں۔", "exterior_is_adjacent"),
       opt("always", "always 180°", "ہمیشہ 180° کے", False,
           "180° is the exterior and the interior angle next to it together.", "180° تو بیرونی اور ساتھ والا اندرونی زاویہ مل کر ہیں۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("An isosceles triangle has a top angle of 30°. Its two base angles are equal. How big is each base angle?", "ایک متساوی الساقین مثلث کا اوپر والا زاویہ 30° ہے۔ اس کے دونوں قاعدے والے زاویے برابر ہیں۔ ہر قاعدے والا زاویہ کتنا ہے؟"),
     QB,
     T("180 − 30 = 150. Share it between the two base angles.", "180 − 30 = 150۔ اسے دونوں قاعدے والے زاویوں میں بانٹیں۔"),
     T("Right! 75°. Check: 75 + 75 + 30 = 180.", "درست! 75°۔ جانچ: 75 + 75 + 30 = 180"),
     T("180 − 30 = 150, and 150 ÷ 2 = 75°.", "180 − 30 = 150، اور 150 ÷ 2 = 75°"),
     common_wrong=[wrong(150, "150° is both base angles together. Each one is 150 ÷ 2 = 75°.", "150° دونوں قاعدے والے زاویے مل کر ہیں۔ ہر ایک 150 ÷ 2 = 75°", "isosceles_forgot")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("A triangle has angles of 35° and 85°. Sana says the third angle is 360 − 35 − 85 = 240°. What went wrong?", "ایک مثلث کے دو زاویے 35° اور 85° ہیں۔ ثنا کہتی ہے تیسرا زاویہ 360 − 35 − 85 = 240° ہے۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("tri", "A triangle's angles add up to 180°: 180 − 35 − 85 = 60°.", "مثلث کے زاویوں کا مجموعہ 180° ہے: 180 − 35 − 85 = 60°", True,
           "Yes! 360° is for angles around a point.", "جی ہاں! 360° نقطے کے گرد زاویوں کے لیے ہے۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "240° is bigger than a straight angle, so it can't fit in a triangle. Use 180°: 60°.", "240° مستقیم زاویے سے بڑا ہے، مثلث میں نہیں آ سکتا۔ 180° لیں: 60°", "triangle_is_360"),
       opt("add", "She should add: 35 + 85 = 120°.", "اسے جمع کرنا چاہیے: 35 + 85 = 120°", False,
           "120° is the two known angles. Take them from 180°: 60°.", "120° دو معلوم زاویے ہیں۔ انہیں 180° سے نفی کریں: 60°"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_exterior", "front": T("Exterior angle of a triangle = ?", "مثلث کا بیرونی زاویہ = ؟"),
    "back": T("The sum of the two opposite interior angles. 40° and 75° give 115°.", "سامنے والے دو اندرونی زاویوں کا مجموعہ۔ 40° اور 75° سے 115°۔")},
   {"id": "f_special", "front": T("Equilateral and isosceles triangle angles?", "متساوی الاضلاع اور متساوی الساقین مثلث کے زاویے؟"),
    "back": T("Equilateral: 60° each. Isosceles: the two base angles are equal.", "متساوی الاضلاع: ہر زاویہ 60°۔ متساوی الساقین: قاعدے والے دونوں زاویے برابر۔")},
 ],
 "home_tasks": [{"id": "h_exterior", "text": T(
   "Draw any triangle on paper with a ruler and extend one side past a corner. Tear off the two corners opposite that outside angle and place them side by side in the outside angle. Do they fill it exactly? Check with a protractor too.",
   "کاغذ پر رولر سے کوئی بھی مثلث بنائیں اور ایک ضلع کو ایک کونے سے آگے بڑھائیں۔ اس باہر والے زاویے کے سامنے والے دو کونے پھاڑیں اور انہیں ساتھ ساتھ باہر والے زاویے میں رکھیں۔ کیا وہ اسے پورا بھر دیتے ہیں؟ چاندا (پروٹیکٹر) سے بھی جانچیں۔")}],
 "glossary": [T("Exterior angle", "بیرونی زاویہ"), T("Interior angle", "اندرونی زاویہ"),
              T("Isosceles triangle", "متساوی الساقین مثلث"), T("Equilateral triangle", "متساوی الاضلاع مثلث"),
              T("Unknown angle", "نامعلوم زاویہ")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Abbu builds kites to fly from our rooftop. The two sticks must cross at exactly 90°, or the kite flies crooked! How do builders get angles right?",
                     "ابو چھت سے اڑانے کے لیے پتنگیں بناتے ہیں۔ دونوں تیلیاں بالکل 90° پر ملنی چاہییں، ورنہ پتنگ ٹیڑھی اڑتی ہے! بنانے والے زاویے ٹھیک کیسے رکھتے ہیں؟"),
    "figure": F1,
    "text": T("Today we find unknown angles on lines, around points and in triangles, and solve real construction problems. This is the last lesson of the Constructions unit, so it ends with a short unit test. First, a warm-up.",
              "آج ہم لکیروں پر، نقطوں کے گرد اور مثلثوں میں نامعلوم زاویے نکالیں گے، اور تعمیر کے اصل سوال حل کریں گے۔ یہ تعمیرات کے باب کا آخری سبق ہے، اس لیے آخر میں ایک چھوٹا ٹیسٹ ہے۔ پہلے ایک سوال۔")},
   number_question(
     "s2_foundation",
     T("The three angles of a triangle add up to how many degrees?", "مثلث کے تینوں زاویوں کا مجموعہ کتنے درجے ہوتا ہے؟"),
     TRI,
     T("Tear off the three corners and put them together: they make a straight line.", "تینوں کونے پھاڑ کر ساتھ رکھیں: وہ سیدھی لکیر بناتے ہیں۔"),
     T("Right! 180°.", "درست! 180°"),
     T("The angles of a triangle add up to 180°.", "مثلث کے زاویوں کا مجموعہ 180° ہے۔"),
     common_wrong=[wrong(360, "360° is around a point. A triangle's angles make a straight line: 180°.", "360° نقطے کے گرد ہے۔ مثلث کے زاویے سیدھی لکیر بناتے ہیں: 180°", "triangle_is_360"),
                   wrong(90, "90° is a right angle. All three together make 180°.", "90° قائمہ زاویہ ہے۔ تینوں مل کر 180° بناتے ہیں۔")],
     qtype="recall", skill=AN_TRIANGLE),
   {"id": "s3_rules", "type": "explain",
    "character": say("happy", "Line 180, point 360, triangle 180. And the outside angle is the two far angles added!",
                     "لکیر 180، نقطہ 360، مثلث 180۔ اور باہر والا زاویہ دور والے دو زاویوں کا جوڑ ہے!"),
    "figure": F3,
    "text": T("Angles on a straight line add up to 180°. Angles around a point add up to 360°. The angles of a triangle add up to 180°. If you extend one side of a triangle, the outside angle is called the exterior angle. It equals the two opposite interior angles added together (a + b). In an equilateral triangle every angle is 60°. In an isosceles triangle the two base angles are equal. Three angles can make a triangle only if they add up to exactly 180°.",
              "سیدھی لکیر پر زاویوں کا مجموعہ 180° ہے۔ نقطے کے گرد زاویوں کا مجموعہ 360° ہے۔ مثلث کے زاویوں کا مجموعہ 180° ہے۔ اگر مثلث کا ایک ضلع آگے بڑھائیں تو باہر بننے والا زاویہ بیرونی زاویہ (Exterior angle) کہلاتا ہے۔ یہ سامنے والے دو اندرونی زاویوں کے مجموعے (a + b) کے برابر ہوتا ہے۔ متساوی الاضلاع مثلث (Equilateral triangle) کا ہر زاویہ 60° ہے۔ متساوی الساقین مثلث (Isosceles triangle) کے قاعدے والے دونوں زاویے برابر ہوتے ہیں۔ تین زاویے مثلث صرف تب بناتے ہیں جب ان کا مجموعہ بالکل 180° ہو۔")},
   dict(number_question(
     "s4_line",
     T("A ray stands on a straight line. One angle is 125°. What is angle a, in degrees?", "ایک سیدھی لکیر پر ایک شعاع کھڑی ہے۔ ایک زاویہ 125° ہے۔ زاویہ a کتنے درجے ہے؟"),
     S4,
     T("Angles on a straight line: 180 − 125.", "سیدھی لکیر پر زاویے: 180 − 125"),
     T("Right! 55°. Check: 125 + 55 = 180.", "درست! 55°۔ جانچ: 125 + 55 = 180"),
     T("180 − 125 = 55°.", "180 − 125 = 55°"),
     common_wrong=[wrong(235, "That used 360°. A straight line is 180°: 55°.", "اس میں 360° لیا۔ سیدھی لکیر 180° ہے: 55°")]), figure=F4),
   dict(number_question(
     "s5_triangle",
     T("A triangle has angles of 50° and 70°. What is the third angle x?", "ایک مثلث کے دو زاویے 50° اور 70° ہیں۔ تیسرا زاویہ x کتنا ہے؟"),
     S5,
     T("50 + 70 = 120. Then 180 − 120.", "50 + 70 = 120۔ پھر 180 − 120"),
     T("Right! 60°.", "درست! 60°"),
     T("180 − 50 − 70 = 60°.", "180 − 50 − 70 = 60°"),
     common_wrong=[wrong(240, "That used 360°. A triangle's angles add up to 180°: 60°.", "اس میں 360° لیا۔ مثلث کے زاویوں کا مجموعہ 180° ہے: 60°", "triangle_is_360"),
                   wrong(120, "120 is the two known angles. Take it from 180: 60°.", "120 دو معلوم زاویے ہیں۔ 180 سے نفی کریں: 60°")]), figure=F5),
   dict(number_question(
     "s6_exterior",
     T("A triangle has interior angles of 40° and 75°. The base is extended at the third corner. What is the exterior angle x?", "ایک مثلث کے دو اندرونی زاویے 40° اور 75° ہیں۔ تیسرے کونے پر قاعدہ آگے بڑھایا گیا ہے۔ بیرونی زاویہ x کتنا ہے؟"),
     S6,
     T("Exterior angle = the two opposite interior angles added.", "بیرونی زاویہ = سامنے والے دو اندرونی زاویوں کا جوڑ۔"),
     T("Right! 40 + 75 = 115°.", "درست! 40 + 75 = 115°"),
     T("x = 40 + 75 = 115°. (The angle inside next to it is 65°, and 65 + 115 = 180.)", "x = 40 + 75 = 115°۔ (اس کے ساتھ اندر والا زاویہ 65° ہے، اور 65 + 115 = 180)"),
     common_wrong=[wrong(INNER6, "65° is the interior angle next to x. The exterior angle is 40 + 75 = 115°.", "65° اندر والا ساتھی زاویہ ہے۔ بیرونی زاویہ 40 + 75 = 115° ہے۔", "exterior_is_adjacent")]), figure=F6),
   dict(number_question(
     "s7_isosceles",
     T("An isosceles triangle has two equal sides. One base angle is 65°. What is the top angle a?", "ایک متساوی الساقین مثلث کے دو اضلاع برابر ہیں۔ ایک قاعدے والا زاویہ 65° ہے۔ اوپر والا زاویہ a کتنا ہے؟"),
     S7,
     T("The other base angle is also 65°.", "دوسرا قاعدے والا زاویہ بھی 65° ہے۔"),
     T("Right! 180 − 65 − 65 = 50°.", "درست! 180 − 65 − 65 = 50°"),
     T("Both base angles are 65°: 180 − 130 = 50°.", "دونوں قاعدے والے زاویے 65° ہیں: 180 − 130 = 50°"),
     common_wrong=[wrong(115, "Don't forget the other base angle is also 65°: 180 − 65 − 65 = 50°.", "یاد رکھیں دوسرا قاعدے والا زاویہ بھی 65° ہے: 180 − 65 − 65 = 50°", "isosceles_forgot")]), figure=F7),
   dict(number_question(
     "s8_ramp",
     T("Bilal builds a ramp for his bicycle against an upright wall. The ramp makes 15° with the ground, and the wall makes 90° with the ground. What is angle x at the top, between the ramp and the wall?",
       "بلال سائیکل کے لیے ایک کھڑی دیوار کے ساتھ ڈھلوان بناتا ہے۔ ڈھلوان زمین سے 15° بناتی ہے، اور دیوار زمین سے 90°۔ اوپر ڈھلوان اور دیوار کے درمیان زاویہ x کتنا ہے؟"),
     S8,
     T("Ground, wall and ramp make a triangle: 180 − 90 − 15.", "زمین، دیوار اور ڈھلوان مثلث بناتے ہیں: 180 − 90 − 15"),
     T("Right! 75°.", "درست! 75°"),
     T("180 − 90 − 15 = 75°.", "180 − 90 − 15 = 75°"),
     common_wrong=[wrong(165, "Don't forget the right angle at the wall: 180 − 90 − 15 = 75°.", "دیوار والا قائمہ زاویہ نہ بھولیں: 180 − 90 − 15 = 75°"),
                   wrong(255, "That used 360°. It is a triangle: 180 − 90 − 15 = 75°.", "اس میں 360° لیا۔ یہ مثلث ہے: 180 − 90 − 15 = 75°", "triangle_is_360")]), figure=F8),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "figure": F9,
    "prompt": T("A triangle has interior angles of 50° and 60°. Its base is extended to make the exterior angle x. Hamza says x = 70°, the same as the angle inside next to it. What went wrong?",
                "ایک مثلث کے دو اندرونی زاویے 50° اور 60° ہیں۔ اس کا قاعدہ بڑھا کر بیرونی زاویہ x بنایا گیا ہے۔ حمزہ کہتا ہے x = 70° ہے، اندر کے ساتھ والے زاویے جتنا۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("sum", "x is the two opposite interior angles added: 50 + 60 = 110°.", "x سامنے والے دو اندرونی زاویوں کا جوڑ ہے: 50 + 60 = 110°", True,
          "Yes! 70° is the angle inside. Together 70 + 110 = 180 on the line.", "جی ہاں! 70° اندر والا زاویہ ہے۔ لکیر پر 70 + 110 = 180"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "The inside angle and x sit on a straight line, so they add to 180°: x = 110°.", "اندر والا زاویہ اور x سیدھی لکیر پر ہیں، مجموعہ 180°: x = 110°", "exterior_is_adjacent"),
      opt("diff", "x = 60 − 50 = 10°.", "x = 60 − 50 = 10°", False,
          "Add the two opposite angles, don't subtract: 50 + 60 = 110°.", "سامنے والے دو زاویے جمع کریں، نفی نہیں: 50 + 60 = 110°"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why is the outside angle of a triangle the two far inside angles added? Can you teach me?",
                     "مثلث کا باہر والا زاویہ دور والے دو اندرونی زاویوں کا جوڑ کیوں ہوتا ہے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why is the exterior angle of a triangle equal to the sum of the two opposite interior angles?",
              "اپنے الفاظ میں بتائیں: مثلث کا بیرونی زاویہ سامنے والے دو اندرونی زاویوں کے مجموعے کے برابر کیوں ہوتا ہے؟"),
    "key_idea": "The exterior angle and the interior angle next to it sit on a straight line, so they add to 180°. The three interior angles also add to 180°. Both times the angle next to it plus something makes 180°, so the exterior angle must equal the other two interior angles added.",
    "levels": {
      "got_it": "Uses both facts: the exterior and its neighbour make 180° on a line, and the three interior angles make 180°, so the exterior equals the other two.",
      "partly": "Uses only one of the two facts, or shows it with numbers for one triangle without a reason.",
      "not_yet": "Gives no reason, or says it is just the rule."},
    "keywords": [
      ["straight line", "line", "سیدھی لکیر", "لکیر"],
      ["180"],
      ["triangle", "three angles", "مثلث", "تین زاویے"],
      ["same", "equal", "left over", "برابر", "باقی"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Both groups make 180°, so the exterior angle equals the two far angles.", "بہت خوب! دونوں گروہ 180° بناتے ہیں، تو بیرونی زاویہ دور والے دو زاویوں کے برابر ہے۔"),
      "partly": T("Good start! Now use both facts: the straight line makes 180°, and the triangle makes 180° too.", "اچھی شروعات! اب دونوں باتیں استعمال کریں: سیدھی لکیر 180° بناتی ہے، اور مثلث بھی 180°۔"),
      "not_yet": T("Look at the outside angle and the inside angle next to it. What do they add up to? And the three inside angles?", "باہر والے زاویے اور اس کے ساتھ والے اندرونی زاویے کو دیکھیں۔ ان کا مجموعہ کیا ہے؟ اور تینوں اندرونی زاویوں کا؟")},
    "limit_per_day": 3, "max_attempts": 2},
   {"id": "s11_unit_test", "type": "explain",
    "character": say("encouraging", "Test time! Five questions from the whole Constructions unit. Take your time!",
                     "ٹیسٹ کا وقت! تعمیرات کے پورے باب سے پانچ سوال۔ آرام سے کریں!"),
    "text": T("This short test has questions on perpendicular bisectors, constructing and bisecting angles, and real-life angle problems.",
              "اس چھوٹے ٹیسٹ میں عمودی ناصف، زاویے بنانے اور ان کی تنصیف، اور زاویوں کے عملی سوالات ہیں۔")},
   dict(number_question(
     "u1_kite",
     T("Test 1: In a kite frame, the long stick is the perpendicular bisector of the cross stick. The cross stick is 60 cm long. How far is it, in cm, from the crossing point to each end of the cross stick?",
       "ٹیسٹ 1: پتنگ کے ڈھانچے میں لمبی تیلی آڑی تیلی کا عمودی ناصف ہے۔ آڑی تیلی 60 سینٹی میٹر لمبی ہے۔ ملنے کے نقطے سے آڑی تیلی کے ہر سرے تک کتنے سینٹی میٹر ہیں؟"),
     U1,
     T("A bisector cuts the stick into two equal halves.", "ناصف تیلی کو دو برابر آدھے حصوں میں کاٹتا ہے۔"),
     T("Right! 60 ÷ 2 = 30 cm.", "درست! 60 ÷ 2 = 30 سینٹی میٹر"),
     T("The perpendicular bisector cuts it in half: 60 ÷ 2 = 30 cm.", "عمودی ناصف اسے آدھا کرتا ہے: 60 ÷ 2 = 30 سینٹی میٹر"),
     common_wrong=[wrong(60, "60 cm is the whole stick. Bisect means cut in half: 30 cm.", "60 سینٹی میٹر پوری تیلی ہے۔ تنصیف کا مطلب آدھا کرنا: 30"),
                   wrong(90, "90 is the angle at the crossing. The length to each end is 60 ÷ 2 = 30 cm.", "90 ملنے کی جگہ کا زاویہ ہے۔ ہر سرے تک لمبائی 60 ÷ 2 = 30 سینٹی میٹر")],
     skill=CO_BISECTORS), figure=FU1),
   number_question(
     "u2_bisect",
     T("Test 2: Ayesha constructs a 90° angle with her compass and then bisects it. How big is each of the two new angles?", "ٹیسٹ 2: عائشہ پرکار سے 90° کا زاویہ بناتی ہے اور پھر اس کی تنصیف کرتی ہے۔ دونوں نئے زاویوں میں سے ہر ایک کتنا ہے؟"),
     U2,
     T("Bisecting cuts an angle into two equal halves.", "تنصیف زاویے کو دو برابر حصوں میں کاٹتی ہے۔"),
     T("Right! 90 ÷ 2 = 45°.", "درست! 90 ÷ 2 = 45°"),
     T("90 ÷ 2 = 45°.", "90 ÷ 2 = 45°"),
     common_wrong=[wrong(180, "Bisecting halves an angle, it doesn't double it: 45°.", "تنصیف زاویے کو آدھا کرتی ہے، دگنا نہیں: 45°")],
     skill=CO_ANGLES),
   number_question(
     "u3_equilateral",
     T("Test 3: To construct a 60° angle, we draw two arcs with the same compass width. This makes an equilateral triangle. How big is each angle of an equilateral triangle?",
       "ٹیسٹ 3: 60° کا زاویہ بنانے کے لیے ہم پرکار کی ایک ہی چوڑائی سے دو قوسیں لگاتے ہیں۔ اس سے متساوی الاضلاع مثلث بنتی ہے۔ متساوی الاضلاع مثلث کا ہر زاویہ کتنا ہے؟"),
     U3,
     T("Three equal angles share 180°.", "تین برابر زاویے 180° بانٹتے ہیں۔"),
     T("Right! 180 ÷ 3 = 60°.", "درست! 180 ÷ 3 = 60°"),
     T("All three angles are equal: 180 ÷ 3 = 60°.", "تینوں زاویے برابر ہیں: 180 ÷ 3 = 60°"),
     common_wrong=[wrong(120, "That used 360°. A triangle has 180°: 180 ÷ 3 = 60°.", "اس میں 360° لیا۔ مثلث میں 180° ہیں: 180 ÷ 3 = 60°", "triangle_is_360")],
     skill=CO_ANGLES),
   {"id": "u4_check", "type": "choice", "question_type": "apply", "skill": CO_WORD_PROBLEMS,
    "prompt": T("Test 4: Zainab wants to cut a triangle from card. Which three angles can she use?", "ٹیسٹ 4: زینب گتے سے ایک مثلث کاٹنا چاہتی ہے۔ وہ کون سے تین زاویے استعمال کر سکتی ہے؟"),
    "options": [
      opt("equal", "60°, 60°, 60°", "60°، 60°، 60°", True,
          "Yes! 60 + 60 + 60 = 180°: an equilateral triangle.", "جی ہاں! 60 + 60 + 60 = 180°: متساوی الاضلاع مثلث۔"),
      opt("two_right", "90°, 90°, 30°", "90°، 90°، 30°", False,
          "These add up to 210°, more than 180°. Two right angles can't fit in one triangle.", "ان کا مجموعہ 210° ہے، 180° سے زیادہ۔ ایک مثلث میں دو قائمہ زاویے نہیں آ سکتے۔"),
      opt("too_big", "100°, 50°, 40°", "100°، 50°، 40°", False,
          "These add up to 190°. A triangle needs exactly 180°.", "ان کا مجموعہ 190° ہے۔ مثلث کے لیے بالکل 180° چاہیے۔"),
    ]},
   dict(number_question(
     "u5_carpenter",
     T("Test 5: A carpenter cuts the ends of two wooden strips at 45° and joins them to make the corner of a photo frame. What angle does the corner make?",
       "ٹیسٹ 5: ایک بڑھئی لکڑی کی دو پٹیوں کے سرے 45° پر کاٹ کر جوڑتا ہے اور فوٹو فریم کا کونا بناتا ہے۔ کونا کتنے درجے کا بنتا ہے؟"),
     U5,
     T("The two 45° parts sit side by side at the corner.", "دونوں 45° والے حصے کونے پر ساتھ ساتھ ہیں۔"),
     T("Right! 45 + 45 = 90°, a right angle, just right for a frame.", "درست! 45 + 45 = 90°، قائمہ زاویہ، فریم کے لیے بالکل ٹھیک۔"),
     T("45 + 45 = 90°.", "45 + 45 = 90°"),
     common_wrong=[wrong(45, "That is one strip. The corner has both: 45 + 45 = 90°.", "یہ ایک پٹی ہے۔ کونے میں دونوں ہیں: 45 + 45 = 90°"),
                   wrong(135, "The corner is made of the two 45° cuts only: 45 + 45 = 90°.", "کونا صرف دو 45° کے کٹوں سے بنتا ہے: 45 + 45 = 90°")],
     skill=CO_WORD_PROBLEMS), figure=FU5),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Constructions unit complete! Now you can build kites, frames and ramps with the right angles.",
                     "تعمیرات کا باب مکمل! اب آپ صحیح زاویوں کے ساتھ پتنگ، فریم اور ڈھلوان بنا سکتے ہیں۔"),
    "text": T("Line 180°, point 360°, triangle 180°. The exterior angle of a triangle equals the two opposite interior angles added, not the angle next to it. Equilateral: 60° each. Isosceles: the base angles are equal, so use the same number twice. Three angles make a triangle only if they add up to 180°.",
              "لکیر 180°، نقطہ 360°، مثلث 180°۔ مثلث کا بیرونی زاویہ سامنے والے دو اندرونی زاویوں کے جوڑ کے برابر ہے، ساتھ والے زاویے کے نہیں۔ متساوی الاضلاع: ہر زاویہ 60°۔ متساوی الساقین: قاعدے والے زاویے برابر، تو وہی عدد دو بار لیں۔ تین زاویے مثلث تب بناتے ہیں جب ان کا مجموعہ 180° ہو۔"),
    "points": [T("Triangle: 180°, not 360°.", "مثلث: 180°، نہ کہ 360°۔"),
               T("Exterior angle = two opposite angles added.", "بیرونی زاویہ = سامنے والے دو زاویوں کا جوڑ۔")]},
 ],
 "review_questions": [
   {"id": "r_point", "type": "apply", "skill": SKILL, "step": number_question(
     "r_point",
     T("In a floor pattern, four angles meet at the centre: 110°, 95°, 85° and x. What is x?", "فرش کے ایک نقش میں مرکز پر چار زاویے ملتے ہیں: 110°، 95°، 85° اور x۔ x کتنا ہے؟"),
     R1,
     T("Around a point: 360 − 110 − 95 − 85.", "نقطے کے گرد: 360 − 110 − 95 − 85"),
     T("Right! 70°.", "درست! 70°"),
     T("110 + 95 + 85 = 290, and 360 − 290 = 70°.", "110 + 95 + 85 = 290، اور 360 − 290 = 70°"),
     common_wrong=[wrong(290, "290 is the known angles. Take it from 360: 70°.", "290 معلوم زاویے ہیں۔ 360 سے نفی کریں: 70°")],
     qtype=None)},
   {"id": "r_kite", "type": "apply", "skill": SKILL, "step": number_question(
     "r_kite",
     T("A kite's sticks cross at 90°. One small triangle inside the kite has angles of 90° and 35°. What is its third angle?", "پتنگ کی تیلیاں 90° پر ملتی ہیں۔ پتنگ کے اندر ایک چھوٹی مثلث کے دو زاویے 90° اور 35° ہیں۔ تیسرا زاویہ کتنا ہے؟"),
     R2,
     T("180 − 90 − 35.", "180 − 90 − 35"),
     T("Right! 55°.", "درست! 55°"),
     T("180 − 90 − 35 = 55°.", "180 − 90 − 35 = 55°"),
     common_wrong=[wrong(145, "Don't forget the 90°: 180 − 90 − 35 = 55°.", "90° نہ بھولیں: 180 − 90 − 35 = 55°")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Constructions unit (PCTB Mathematics 6, Sub-domain 10, 10.4). No textbook text or exercises were used.",
   "This is the last lesson of the unit: the unit test (u1 to u5) covers perpendicular bisectors, constructing and bisecting angles, and real-life angle problems.",
   "The figures are drawn from computed coordinates so the drawn angles roughly match the numbers; students should still work from the numbers, not measure the screen.",
   "Urdu terms to check: بیرونی زاویہ (exterior angle), اندرونی زاویہ (interior angle), متساوی الساقین مثلث (isosceles triangle), متساوی الاضلاع مثلث (equilateral triangle), عمودی ناصف (perpendicular bisector), تنصیف (bisecting), ڈھلوان (ramp), بڑھئی (carpenter).",
   "The numbers and figures were worked out in content/sources/g6-maths-19/construction_problems.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)
