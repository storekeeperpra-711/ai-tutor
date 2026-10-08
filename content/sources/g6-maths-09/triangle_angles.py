import math

from common import (T, opt, say, wrong, number_question, kind_of, write,
                    REF, REVIEW, AN_TYPES, AN_LINE, AN_TRIANGLE)


# ---- figure helpers (the same small block is copied into each Angles script) ----
# Angles are in degrees, measured anticlockwise from +x like in a maths book;
# the app's screen y goes down, so the helpers flip them.
def pt(x, y):
    return [round(x, 1), round(y, 1)]


def ray_end(v, deg, length):
    r = math.radians(deg)
    return pt(v[0] + length * math.cos(r), v[1] - length * math.sin(r))


def arc(center, radius, a0, a1, dashed=False):
    """Arc from a0° to a1° (anticlockwise), in the app's clockwise screen terms."""
    item = {"kind": "arc", "center": center, "radius": radius,
            "start": round((-a1) % 360, 1), "sweep": round(a1 - a0, 1)}
    if dashed:
        item["style"] = "dashed"
    return item


def line(a, b, dashed=False):
    item = {"kind": "line", "from": a, "to": b}
    if dashed:
        item["style"] = "dashed"
    return item


def label(at, text):
    return {"kind": "label", "at": at, "text": text}


def dot(at):
    return {"kind": "point", "at": at}


def square(v, a0, size=6):
    """The little square that marks a right angle between a0° and a0 + 90°."""
    p, q = ray_end(v, a0, size), ray_end(v, a0 + 90, size)
    c = pt(p[0] + q[0] - v[0], p[1] + q[1] - v[1])
    return [line(p, c), line(c, q)]


def mark(v, a0, a1, text=None, r=10, dist=None, arc_only=False):
    """Mark the angle from a0° to a1° at vertex v: a square for exactly 90°
    (unless arc_only, when the square would give the answer away), an arc
    otherwise, and its label on the middle direction."""
    items = square(v, a0) if a1 - a0 == 90 and not arc_only else [arc(v, r, a0, a1)]
    if text:
        half = math.radians(min((a1 - a0) / 2, 90))
        d = dist or max(r + 11, min(8 / math.sin(half), 40))
        items.append(label(ray_end(v, (a0 + a1) / 2, d), text))
    return items


def figure(width, height, alt, items):
    """Check the drawing fits the box (as tools/validate_lessons.py does)."""
    assert len(items) <= 60, len(items)
    margin = 0.025 * max(width, height)
    for it in items:
        reach = it.get("radius", 0)
        for x, y in [*it.get("points", []), *(it[k] for k in ("from", "to", "center", "at") if k in it)]:
            assert reach <= x <= width - reach and reach <= y <= height - reach, (it, width, height)
            if it["kind"] == "label":
                assert margin <= x <= width - margin and margin <= y <= height - margin, (it, width, height)
    return {"width": width, "height": height, "alt": alt, "items": items}


def fan(v, rays, marks, arm=40):
    """Rays from one vertex v (two rays at 0° and 180° make a straight line),
    with marked angles: marks are (a0, a1, text) or (a0, a1, text, dist).
    Neighbouring arcs get different radii so each angle can be seen."""
    items = [line(v, ray_end(v, d, arm)) for d in rays] + [dot(v)]
    radii = [9 + 5 * (i % 2) for i in range(len(marks))]
    if len(marks) % 2 and marks[-1][1] - marks[0][0] == 360:
        radii[-1] = 19      # all the way round: the last arc also touches the first
    for m, r in zip(marks, radii):
        items += mark(v, m[0], m[1], m[2], r=r, dist=m[3] if len(m) > 3 else None)
    return items


def parts_text(texts):
    """Words for the marked angles, for the alt text: '130°' and a missing one."""
    en, ur = [], []
    for t in texts:
        if t == "?":
            en.append("a missing angle marked ?")
            ur.append("ایک نامعلوم زاویہ جس پر ? لکھا ہے")
        elif t.endswith("°"):
            en.append(t)
            ur.append(t)
        else:
            en.append(f"an angle marked {t}")
            ur.append(f"ایک زاویہ جس پر {t} لکھا ہے")

    def join(xs, comma, also):
        return xs[0] if len(xs) == 1 else comma.join(xs[:-1]) + also + xs[-1]
    return join(en, ", ", " and "), join(ur, "، ", " اور ")


def on_line(rays, texts):
    """A straight line with rays from a point on it at the given angles
    (measured from the right end); the angles between them, right to left,
    are marked with texts."""
    edges = [0, *rays, 180]
    assert len(texts) == len(edges) - 1
    v = pt(60, 50)
    items = fan(v, [0, 180, *rays], [(a, b, t) for a, b, t in zip(edges, edges[1:], texts)], arm=50)
    en, ur = parts_text(texts)
    if len(rays) == 1:
        alt = T(f"A straight line with a point on it. A ray from the point splits the straight angle into {en}.",
                f"ایک سیدھی لکیر پر ایک نقطہ۔ اس نقطے سے ایک شعاع سیدھے زاویے کو ان حصوں میں بانٹتی ہے: {ur}۔")
    else:
        alt = T(f"A straight line with a point on it. {len(rays)} rays from the point split the straight angle into {en}.",
                f"ایک سیدھی لکیر پر ایک نقطہ۔ اس نقطے سے {len(rays)} شعاعیں سیدھے زاویے کو ان حصوں میں بانٹتی ہیں: {ur}۔")
    return figure(120, 66, alt, items)


def attach(lesson, figures):
    """Put each figure on the step with that id (steps, question bank, review)."""
    steps = [*lesson["steps"], *(q["step"] for qs in lesson["question_bank"].values() for q in qs),
             *(q["step"] for q in lesson.get("review_questions", []))]
    for step in steps:
        if step["id"] in figures:
            step["figure"] = figures.pop(step["id"])
    assert not figures, figures

SKILL = AN_TRIANGLE
SUM = 180


def third(a, b):
    c = SUM - a - b
    assert c > 0, (a, b)
    return c


def base_angle(top):
    """Each of the two equal angles of an isosceles triangle."""
    assert (SUM - top) % 2 == 0, top
    return (SUM - top) // 2


# s2: three angles on a line
S2 = SUM - 50 - 60
assert S2 == 70
# s4
S4 = third(50, 60)
assert S4 == 70 and 360 - 110 == 250 and 50 + 60 == 110
# s5: right-angled triangle
S5 = third(90, 35)
assert S5 == 55 and SUM - 35 == 145
# s6: equilateral
S6 = SUM // 3
assert S6 == 60 and 3 * S6 == SUM and 360 // 3 == 120
# s7: isosceles, top 40
S7 = base_angle(40)
assert S7 == 70 and S7 + S7 + 40 == SUM and SUM - 40 == 140
# s8: two right angles leave nothing for the third angle
assert SUM - 90 - 90 == 0
# s9: 65 and 45
assert third(65, 45) == 70 and 360 - 65 - 45 == 250
# s10: two obtuse angles are already more than 180
assert 91 + 91 > SUM
# s11: isosceles, base angles 65 each
S11 = SUM - 65 - 65
assert S11 == 50 and SUM - 65 == 115
# question bank and review
QB = third(90, 28)
assert QB == 62 and SUM - 28 == 152
assert third(100, 30) == 50 and kind_of(100) == "obtuse"
R1 = third(100, 30)
R2 = base_angle(80)
assert R2 == 50 and SUM - 80 == 100


# ---- figures -------------------------------------------------------------
def deg(n):
    return f"{n}°"


def triangle_items(a, b, texts, box, ticks=(), fill=True, dists=(None, None, None)):
    """A triangle drawn to scale with angle a° at the bottom left, b° at the
    bottom right and the third angle at the top, fitted into box = (x0, y0, w, h).
    texts label the three angles (left, right, top); a 90° angle gets a square.
    ticks: sides to mark equal, from "left" (left to top), "right" (right to top), "base"."""
    c = 180 - a - b
    assert c > 0
    side = math.sin(math.radians(b)) / math.sin(math.radians(c))     # bottom left to top, base 1
    raw = [(0, 0), (1, 0), (side * math.cos(math.radians(a)), side * math.sin(math.radians(a)))]
    x0, y0, w, h = box
    pad = 15
    lo, hi = min(x for x, _ in raw), max(x for x, _ in raw)
    top = max(y for _, y in raw)
    s = min((w - 2 * pad) / (hi - lo), (h - 2 * pad) / top)
    ox = x0 + (w - s * (hi - lo)) / 2 - s * lo
    oy = y0 + (h + s * top) / 2
    L, R, P = (pt(ox + s * x, oy - s * y) for x, y in raw)
    items = [{"kind": "polygon", "points": [L, R, P], "fill": fill}]
    items += mark(L, 0, a, texts[0], r=10, dist=dists[0])
    items += mark(R, 180 - b, 180, texts[1], r=10, dist=dists[1])
    items += mark(P, 180 + a, 360 - b, texts[2], r=10, dist=dists[2])
    ends = {"left": (L, P), "right": (R, P), "base": (L, R)}
    for name in ticks:
        p, q = ends[name]
        m = ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
        d = math.dist(p, q)
        ux, uy = (q[1] - p[1]) / d, -(q[0] - p[0]) / d       # across the side
        items.append(line(pt(m[0] - 3 * ux, m[1] - 3 * uy), pt(m[0] + 3 * ux, m[1] + 3 * uy)))
    return items


def triangle(a, b, texts, ticks=(), alt=None, size=(120, 90)):
    if alt is None:
        en, ur = parts_text(texts)
        alt = T(f"A triangle with its three angles marked: {en}."
                + (" A small square marks the right angle." if 90 in (a, b) else "")
                + (" Small marks on two sides show they are equal." if len(ticks) == 2 else "")
                + (" Small marks on all three sides show they are equal." if len(ticks) == 3 else ""),
                f"ایک مثلث جس کے تینوں زاویے دکھائے گئے ہیں: {ur}۔"
                + (" ایک چھوٹا مربع قائمہ زاویہ دکھاتا ہے۔" if 90 in (a, b) else "")
                + (" دو اضلاع پر چھوٹے نشان دکھاتے ہیں کہ وہ برابر ہیں۔" if len(ticks) == 2 else "")
                + (" تینوں اضلاع پر چھوٹے نشان دکھاتے ہیں کہ وہ برابر ہیں۔" if len(ticks) == 3 else ""))
    w, h = size
    return figure(w, h, alt, triangle_items(a, b, texts, (0, 0, w, h), ticks))


# s1: the three corners of a triangle fit together on a straight line
HOOK = (50, 60)
HOOK_C = third(*HOOK)
torn = (triangle_items(HOOK[0], HOOK[1], ["a", "b", "c"], (0, 0, 104, 92))
        + fan(pt(150, 70), [0, 180, HOOK[0], HOOK[0] + HOOK[1]],
              [(0, HOOK[0], "a"), (HOOK[0], HOOK[0] + HOOK[1], "b"), (HOOK[0] + HOOK[1], 180, "c")], arm=42))
# s3: one triangle with all three angles, numbers not used in the questions
RULE = (40, 80)
assert third(*RULE) == 60

FIGS = {
  "s1_hook": figure(200, 92, T(
    f"Left: a triangle with its corners marked a, b and c. Right: the same three corners put side by side at one point on a straight line, a then b then c, filling the straight angle with no gap.",
    f"بائیں: ایک مثلث جس کے کونوں پر a، b اور c لکھا ہے۔ دائیں: یہی تینوں کونے سیدھی لکیر کے ایک نقطے پر ساتھ ساتھ رکھے ہیں، پہلے a پھر b پھر c، اور سیدھا زاویہ بغیر خالی جگہ کے بھر جاتا ہے۔"),
    torn),
  "s2_foundation": on_line([50, 50 + 60], ["50°", "60°", "?"]),
  "s3_rule": triangle(*RULE, [deg(RULE[0]), deg(RULE[1]), deg(third(*RULE))]),
  "s4_third": triangle(50, 60, ["50°", "60°", "?"]),
  "s5_right": triangle(90, 35, ["90°", "35°", "?"]),
  "s6_equilateral": triangle(S6, S6, ["x", "x", "x"], ticks=("left", "right", "base")),
  "s7_isosceles": triangle(S7, S7, ["x", "x", "40°"], ticks=("left", "right")),
  "s9_find_error": triangle(65, 45, ["65°", "45°", "?"]),
  "s11_top": triangle(65, 65, ["65°", "65°", "?"], ticks=("left", "right")),
  "qb_apply": triangle(90, 28, ["90°", "28°", "?"]),
  "r_third": triangle(100, 30, ["100°", "30°", "?"]),
  "r_iso": triangle(R2, R2, ["x", "x", "80°"], ticks=("left", "right")),
}


lesson = {
 "id": "g6-maths-09-angles-in-a-triangle",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Use the fact that the angles of a triangle add up to 180° to find a missing angle, including in right-angled, equilateral and isosceles triangles.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Angles in a triangle", "مثلث کے زاویے"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": AN_LINE}, {"skill": AN_TYPES}],
 "misconceptions": [
   {"id": "triangle_is_360", "description": "Uses 360° as the total for a triangle."},
   {"id": "forgets_right_angle", "description": "Leaves the right angle (90°) out of the sum in a right-angled triangle."},
   {"id": "isosceles_no_halve", "description": "Finds 180° minus the top angle but forgets to share it between the two equal angles."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_sum", "type": "recall", "step": {
     "id": "qb_sum", "type": "choice",
     "prompt": T("The three angles inside any triangle add up to how many degrees?", "کسی بھی مثلث کے تینوں اندرونی زاویوں کا مجموعہ کتنے درجے ہوتا ہے؟"),
     "options": [
       opt("half", "180°", "180°", True, "Yes! Always 180°, whatever the triangle.", "جی ہاں! ہمیشہ 180°، مثلث جیسا بھی ہو۔"),
       opt("full", "360°", "360°", False, "360° is a full turn. A triangle's angles make 180°.", "360° پورا چکر ہے۔ مثلث کے زاویے 180° بناتے ہیں۔", "triangle_is_360"),
       opt("depends", "It depends on the triangle.", "مثلث پر منحصر ہے۔", False, "It is always 180°, for every triangle.", "یہ ہر مثلث کے لیے ہمیشہ 180° ہے۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("A right-angled triangle has one angle of 28°. What is the third angle?", "ایک قائمہ الزاویہ مثلث کا ایک زاویہ 28° ہے۔ تیسرا زاویہ کتنا ہے؟"),
     QB,
     T("The right angle is 90°. Then 180 − 90 − 28.", "قائمہ زاویہ 90° ہے۔ پھر 180 − 90 − 28"),
     T("Right! 62°.", "درست! 62°"),
     T("180 − 90 − 28 = 62°.", "180 − 90 − 28 = 62°"),
     common_wrong=[wrong(152, "Don't forget the right angle: 180 − 90 − 28 = 62°.", "قائمہ زاویہ نہ بھولیں: 180 − 90 − 28 = 62°", "forgets_right_angle")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("A triangle has angles of 100° and 30°. Rabia says the third angle is 360 − 100 − 30 = 230°. What went wrong?",
                 "ایک مثلث کے دو زاویے 100° اور 30° ہیں۔ رابعہ کہتی ہے تیسرا زاویہ 360 − 100 − 30 = 230° ہے۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("sum", "A triangle's angles add up to 180°. 180 − 100 − 30 = 50°.", "مثلث کے زاویوں کا مجموعہ 180° ہے۔ 180 − 100 − 30 = 50°", True,
           "Yes! 360° is for angles around a point.", "جی ہاں! 360° نقطے کے گرد زاویوں کے لیے ہے۔"),
       opt("add", "She should add: 100 + 30 = 130°.", "اسے جمع کرنا چاہیے: 100 + 30 = 130°", False,
           "Take the two angles from 180°: 50°.", "دونوں زاویے 180° سے نفی کریں: 50°"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "230° can't fit inside a triangle! 180 − 100 − 30 = 50°.", "230° مثلث کے اندر نہیں آ سکتا! 180 − 100 − 30 = 50°", "triangle_is_360"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_sum", "front": T("Angles in a triangle add up to?", "مثلث کے زاویوں کا مجموعہ؟"),
    "back": T("180°. If two are 50° and 60°, the third is 70°.", "180°۔ اگر دو زاویے 50° اور 60° ہوں تو تیسرا 70°۔")},
   {"id": "f_special", "front": T("Equilateral and isosceles triangles?", "متساوی الاضلاع اور متساوی الساقین مثلث؟"),
    "back": T("Equilateral: all three angles are 60°. Isosceles: two angles are equal.", "متساوی الاضلاع: تینوں زاویے 60°۔ متساوی الساقین: دو زاویے برابر۔")},
 ],
 "home_tasks": [{"id": "h_tear", "text": T(
   "Draw any triangle on paper and cut it out. Tear off the three corners and put their points together side by side. They make a straight line, 180°! Try it with a different triangle.",
   "کاغذ پر کوئی بھی مثلث بنا کر کاٹیں۔ تینوں کونے پھاڑ کر ان کی نوکیں ساتھ ساتھ ملائیں۔ یہ سیدھی لکیر، 180°، بناتے ہیں! کسی اور مثلث کے ساتھ بھی آزمائیں۔")}],
 "glossary": [T("Triangle", "مثلث"), T("Right-angled triangle", "قائمہ الزاویہ مثلث"),
              T("Equilateral triangle", "متساوی الاضلاع مثلث"), T("Isosceles triangle", "متساوی الساقین مثلث")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Tear the three corners off a paper triangle and put them side by side. They make a straight line! Every time!",
                     "کاغذ کے مثلث کے تینوں کونے پھاڑ کر ساتھ ساتھ رکھیں۔ یہ سیدھی لکیر بناتے ہیں! ہر بار!"),
    "text": T("Today we find missing angles inside triangles. First, a quick check.", "آج ہم مثلث کے اندر نامعلوم زاویے نکالیں گے۔ پہلے ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("Three angles sit on a straight line: 50°, 60° and a missing one. What is the missing angle?", "سیدھی لکیر پر تین زاویے ہیں: 50°، 60° اور ایک نامعلوم۔ نامعلوم زاویہ کتنا ہے؟"),
     S2,
     T("A straight line is 180°.", "سیدھی لکیر 180° ہے۔"),
     T("Right! 70°.", "درست! 70°"),
     T("180 − 50 − 60 = 70°.", "180 − 50 − 60 = 70°"),
     common_wrong=[wrong(250, "Use 180° for a line: 70°.", "لکیر کے لیے 180° لیں: 70°")],
     qtype="recall", skill=AN_LINE),
   {"id": "s3_rule", "type": "explain",
    "character": say("happy", "The three corners make a straight line, so a triangle's angles add up to 180°!",
                     "تینوں کونے سیدھی لکیر بناتے ہیں، اس لیے مثلث کے زاویوں کا مجموعہ 180° ہے!"),
    "text": T("The three angles inside any triangle add up to 180°. To find a missing angle, take the other two away from 180°. In a right-angled triangle one angle is 90°. In an equilateral triangle all three angles are equal. In an isosceles triangle two angles are equal.",
              "کسی بھی مثلث کے تینوں اندرونی زاویوں کا مجموعہ 180° ہے۔ نامعلوم زاویے کے لیے باقی دو کو 180° سے نفی کریں۔ قائمہ الزاویہ مثلث میں ایک زاویہ 90° ہوتا ہے۔ متساوی الاضلاع مثلث میں تینوں زاویے برابر ہوتے ہیں۔ متساوی الساقین مثلث میں دو زاویے برابر ہوتے ہیں۔")},
   number_question(
     "s4_third",
     T("A triangle has angles of 50° and 60°. What is the third angle?", "ایک مثلث کے دو زاویے 50° اور 60° ہیں۔ تیسرا زاویہ کتنا ہے؟"),
     S4,
     T("180 − 50 − 60.", "180 − 50 − 60"),
     T("Right! 70°. Same as the line: the corners make a straight line!", "درست! 70°۔ لکیر والا ہی جواب: کونے سیدھی لکیر بناتے ہیں!"),
     T("50 + 60 = 110, and 180 − 110 = 70°.", "50 + 60 = 110، اور 180 − 110 = 70°"),
     common_wrong=[wrong(250, "That used 360°. A triangle is 180°: 70°.", "اس میں 360° لیا۔ مثلث 180° ہے: 70°", "triangle_is_360"),
                   wrong(110, "110 is the two angles added. Take it from 180: 70°.", "110 دونوں زاویوں کا مجموعہ ہے۔ 180 سے نفی کریں: 70°")]),
   number_question(
     "s5_right",
     T("A right-angled triangle has one angle of 35°. What is the third angle?", "ایک قائمہ الزاویہ مثلث کا ایک زاویہ 35° ہے۔ تیسرا زاویہ کتنا ہے؟"),
     S5,
     T("One angle is the right angle, 90°.", "ایک زاویہ قائمہ، 90°، ہے۔"),
     T("Right! 55°.", "درست! 55°"),
     T("180 − 90 − 35 = 55°.", "180 − 90 − 35 = 55°"),
     common_wrong=[wrong(145, "Don't forget the right angle: 180 − 90 − 35 = 55°.", "قائمہ زاویہ نہ بھولیں: 180 − 90 − 35 = 55°", "forgets_right_angle")]),
   number_question(
     "s6_equilateral",
     T("All three angles of an equilateral triangle are equal. How big is each one?", "متساوی الاضلاع مثلث کے تینوں زاویے برابر ہیں۔ ہر ایک کتنا بڑا ہے؟"),
     S6,
     T("Share 180° between three.", "180° کو تین میں بانٹیں۔"),
     T("Right! 60° each.", "درست! ہر ایک 60°"),
     T("180 ÷ 3 = 60°.", "180 ÷ 3 = 60°"),
     common_wrong=[wrong(120, "That used 360°. A triangle is 180°: 180 ÷ 3 = 60°.", "اس میں 360° لیا۔ مثلث 180° ہے: 180 ÷ 3 = 60°", "triangle_is_360")]),
   number_question(
     "s7_isosceles",
     T("An isosceles triangle has a top angle of 40°. The other two angles are equal. How big is each of them?", "ایک متساوی الساقین مثلث کا اوپر والا زاویہ 40° ہے۔ باقی دو زاویے برابر ہیں۔ ہر ایک کتنا ہے؟"),
     S7,
     T("180 − 40 = 140. Share it between the two equal angles.", "180 − 40 = 140۔ اسے دونوں برابر زاویوں میں بانٹیں۔"),
     T("Right! 70° each. Check: 70 + 70 + 40 = 180.", "درست! ہر ایک 70°۔ جانچ: 70 + 70 + 40 = 180"),
     T("180 − 40 = 140, and 140 ÷ 2 = 70°.", "180 − 40 = 140، اور 140 ÷ 2 = 70°"),
     common_wrong=[wrong(140, "That is both equal angles together. Each is 140 ÷ 2 = 70°.", "یہ دونوں برابر زاویے مل کر ہیں۔ ہر ایک 140 ÷ 2 = 70°", "isosceles_no_halve")]),
   {"id": "s8_two_right", "type": "choice", "question_type": "apply",
    "prompt": T("Can a triangle have two right angles?", "کیا ایک مثلث میں دو قائمہ زاویے ہو سکتے ہیں؟"),
    "options": [
      opt("no", "No. 90 + 90 = 180, leaving 0° for the third angle.", "نہیں۔ 90 + 90 = 180، تیسرے زاویے کے لیے 0° بچتا ہے۔", True,
          "Yes! A triangle needs three real angles, so two right angles is impossible.", "جی ہاں! مثلث کو تین اصل زاویے چاہییں، اس لیے دو قائمہ زاویے ناممکن ہیں۔"),
      opt("yes", "Yes, if it is big enough.", "ہاں، اگر وہ کافی بڑا ہو۔", False,
          "Size doesn't change the angles. 90 + 90 = 180 already, so nothing is left.", "سائز سے زاویے نہیں بدلتے۔ 90 + 90 = 180 پہلے ہی، کچھ نہیں بچتا۔"),
    ]},
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("A triangle has angles of 65° and 45°. Faisal says the third angle is 360 − 65 − 45 = 250°. What went wrong?",
                "ایک مثلث کے دو زاویے 65° اور 45° ہیں۔ فیصل کہتا ہے تیسرا زاویہ 360 − 65 − 45 = 250° ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("sum", "A triangle's angles add up to 180°. 180 − 65 − 45 = 70°.", "مثلث کے زاویوں کا مجموعہ 180° ہے۔ 180 − 65 − 45 = 70°", True,
          "Yes! An angle inside a triangle is always less than 180°.", "جی ہاں! مثلث کا اندرونی زاویہ ہمیشہ 180° سے کم ہوتا ہے۔"),
      opt("add", "He should add: 65 + 45 = 110°.", "اسے جمع کرنا چاہیے: 65 + 45 = 110°", False,
          "Take the two angles from 180°: 70°.", "دونوں زاویے 180° سے نفی کریں: 70°"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "250° can't fit inside a triangle. 180 − 65 − 45 = 70°.", "250° مثلث کے اندر نہیں آ سکتا۔ 180 − 65 − 45 = 70°", "triangle_is_360"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Can a triangle have two obtuse angles? Why or why not? Can you teach me?",
                     "کیا ایک مثلث میں دو منفرجہ زاویے ہو سکتے ہیں؟ کیوں یا کیوں نہیں؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why can't a triangle have two obtuse angles?",
              "اپنے الفاظ میں بتائیں: ایک مثلث میں دو منفرجہ زاویے کیوں نہیں ہو سکتے؟"),
    "key_idea": "Each obtuse angle is more than 90°, so two of them add up to more than 180°. But all three angles of a triangle add up to exactly 180°, so there would be nothing left for the third angle.",
    "levels": {
      "got_it": "Says two obtuse angles are more than 180° together, but the triangle's angles must add up to 180°.",
      "partly": "Mentions 180° or that obtuse angles are big, without putting the two together.",
      "not_yet": "Says yes, or gives no reason."},
    "keywords": [
      ["180", "straight", "سیدھی"],
      ["90", "more", "bigger", "obtuse", "زیادہ", "منفرجہ"],
      ["nothing", "left", "third", "کچھ نہیں", "تیسرا", "باقی"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Two obtuse angles already pass 180°, so there is no room for a third.", "بہت خوب! دو منفرجہ زاویے پہلے ہی 180° سے آگے ہیں، تیسرے کی جگہ نہیں۔"),
      "partly": T("Good start! Now add two angles bigger than 90°. Is that more or less than 180°?", "اچھی شروعات! اب 90° سے بڑے دو زاویے جمع کریں۔ کیا یہ 180° سے زیادہ ہے یا کم؟"),
      "not_yet": T("Obtuse angles are more than 90°. What do two of them make together? What must a triangle's angles add up to?", "منفرجہ زاویے 90° سے زیادہ ہوتے ہیں۔ دو مل کر کتنے بنتے ہیں؟ مثلث کے زاویوں کا مجموعہ کتنا ہونا چاہیے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_top",
     T("An isosceles triangle has two equal angles of 65° each. What is the third angle?", "ایک متساوی الساقین مثلث کے دو برابر زاویے 65° کے ہیں۔ تیسرا زاویہ کتنا ہے؟"),
     S11,
     T("Both 65° angles count: 180 − 65 − 65.", "دونوں 65° زاویے شمار کریں: 180 − 65 − 65"),
     T("Right! 50°.", "درست! 50°"),
     T("65 + 65 = 130, and 180 − 130 = 50°.", "65 + 65 = 130، اور 180 − 130 = 50°"),
     common_wrong=[wrong(115, "There are two 65° angles. 180 − 65 − 65 = 50°.", "65° کے دو زاویے ہیں۔ 180 − 65 − 65 = 50°")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Triangle angles mastered! They always make 180°.", "مثلث کے زاویے آ گئے! یہ ہمیشہ 180° بناتے ہیں۔"),
    "text": T("The angles inside a triangle add up to 180°. A right-angled triangle has one 90° angle. An equilateral triangle has three 60° angles. An isosceles triangle has two equal angles: take the third from 180° and halve what is left.",
              "مثلث کے اندرونی زاویوں کا مجموعہ 180° ہے۔ قائمہ الزاویہ مثلث میں ایک زاویہ 90° ہے۔ متساوی الاضلاع مثلث میں تینوں زاویے 60° ہیں۔ متساوی الساقین مثلث میں دو زاویے برابر ہیں: تیسرا 180° سے نفی کریں اور باقی کا آدھا کریں۔"),
    "points": [T("Triangle: 180°.", "مثلث: 180°۔"),
               T("Equilateral: 60°, 60°, 60°.", "متساوی الاضلاع: 60°، 60°، 60°۔")]},
 ],
 "review_questions": [
   {"id": "r_third", "type": "apply", "skill": SKILL, "step": number_question(
     "r_third",
     T("A triangle has angles of 100° and 30°. What is the third angle?", "ایک مثلث کے دو زاویے 100° اور 30° ہیں۔ تیسرا زاویہ کتنا ہے؟"),
     R1,
     T("180 − 100 − 30.", "180 − 100 − 30"),
     T("Right! 50°.", "درست! 50°"),
     T("180 − 130 = 50°.", "180 − 130 = 50°"),
     common_wrong=[wrong(230, "Use 180° for a triangle: 50°.", "مثلث کے لیے 180° لیں: 50°", "triangle_is_360")],
     qtype=None)},
   {"id": "r_iso", "type": "apply", "skill": SKILL, "step": number_question(
     "r_iso",
     T("An isosceles triangle has a top angle of 80°. How big is each of the two equal angles?", "ایک متساوی الساقین مثلث کا اوپر والا زاویہ 80° ہے۔ دونوں برابر زاویوں میں سے ہر ایک کتنا ہے؟"),
     R2,
     T("180 − 80, then halve.", "180 − 80، پھر آدھا"),
     T("Right! 50° each.", "درست! ہر ایک 50°"),
     T("180 − 80 = 100, and 100 ÷ 2 = 50°.", "180 − 80 = 100، اور 100 ÷ 2 = 50°"),
     common_wrong=[wrong(100, "Share it between the two angles: 100 ÷ 2 = 50°.", "اسے دونوں زاویوں میں بانٹیں: 100 ÷ 2 = 50°", "isosceles_no_halve")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Angles unit. No textbook text or exercises were used.",
   "Tearing the corners off a paper triangle (s1 and the home task) shows the 180° rule instead of just stating it. s2 and s4 use the same numbers on purpose, so children see the link with angles on a line.",
   "Urdu terms to check: قائمہ الزاویہ مثلث (right-angled triangle), متساوی الاضلاع (equilateral), متساوی الساقین (isosceles).",
   "The numbers were worked out in content/sources/g6-maths-09/triangle_angles.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
attach(lesson, FIGS)
write(lesson)
