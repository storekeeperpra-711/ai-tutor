import math

from common import (T, opt, say, wrong, number_question, kind_of, kind_question, write,
                    REF, REVIEW, AN_TYPES, AN_LINE, AN_PAIRS, AN_TRIANGLE, AN_WORD_PROBLEMS)


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

SKILL = AN_WORD_PROBLEMS
CORNER, LINE, POINT = 90, 180, 360

# s2
S2 = LINE - 90 - 40
assert S2 == 50
# s4: ladder makes 70 with the ground; the wall meets the ground at 90
S4 = LINE - 90 - 70
assert S4 == 20 and LINE - 70 == 110
# s5: roti cut from the middle into 6 equal pieces
S5 = POINT // 6
assert S5 == 60 and LINE // 6 == 30
# s6: a gate opened 75 from the fence line; the angle on the other side of the line
S6 = LINE - 75
assert S6 == 105 and CORNER - 75 == 15
# s7: clock at 4 o'clock
S7 = 4 * (POINT // 12)
assert S7 == 120 and POINT - S7 == 240
# s8: roof truss, isosceles with top 120
S8 = (LINE - 120) // 2
assert S8 == 30 and LINE - 120 == 60
# s9: ramp: ground and ramp make 15 on a straight road, the other side is 165
assert LINE - 15 == 165 and CORNER - 15 == 75
# u1 to u5
assert kind_of(135) == "obtuse"
U2 = LINE - 48
assert U2 == 132 and POINT - 48 == 312
U3 = CORNER - 58
assert U3 == 32 and LINE - 58 == 122
U4 = LINE - 45 - 75
assert U4 == 60 and 45 + 75 == 120
U5 = POINT - 100 - 145
assert U5 == 115 and LINE - 100 - 145 < 0 and 100 + 145 == 245
# question bank and review
QB = LINE - 90 - 55
assert QB == 35 and LINE - 55 == 125
R1 = POINT // 5
assert R1 == 72 and LINE // 5 == 36
R2 = 2 * (POINT // 12)
assert R2 == 60



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

def clock(hour, text="?"):
    """A clock face with the minute hand on 12 and the hour hand on `hour`,
    and the angle between them marked (an arc, never a square: the child works it out)."""
    c, r = pt(50, 50), 44
    items = [{"kind": "circle", "center": c, "radius": r}]
    for h in range(12):
        a = 90 - 30 * h
        items.append(line(ray_end(c, a, r - 5), ray_end(c, a, r)))
    for h in (12, 3, 6, 9):
        items.append(label(ray_end(c, 90 - 30 * h, 34), str(h)))
    hand = 90 - 30 * hour
    items += [line(c, ray_end(c, 90, 24)), line(c, ray_end(c, hand, 18)), dot(c)]
    items += mark(c, hand, 90, text, arc_only=True)
    alt = T(f"A clock face showing {hour} o'clock: the long hand points to 12 and the short hand points to {hour}. The angle between the hands is marked {text}.",
            f"گھڑی {hour} بجا رہی ہے: لمبی سوئی 12 پر اور چھوٹی سوئی {hour} پر ہے۔ سوئیوں کے درمیان زاویے پر {text} لکھا ہے۔")
    return figure(100, 100, alt, items)


def at_point(rays, texts):
    """Rays from a point; the angles between them, going round, marked with texts."""
    edges = [*rays, rays[0] + POINT]
    assert len(texts) == len(rays)
    items = fan(pt(50, 50), rays, [(a, b, t) for a, b, t in zip(edges, edges[1:], texts)])
    en, ur = parts_text(texts)
    alt = T(f"{len(rays)} rays come out of one point. The angles between them, all the way round, are {en}.",
            f"ایک نقطے سے {len(rays)} شعاعیں نکلتی ہیں۔ ان کے درمیان پورے گرد زاویے یہ ہیں: {ur}۔")
    return figure(100, 100, alt, items)


def wheel(n, en, ur, fill=False):
    """A circle cut from the middle into n equal parts; one angle at the middle is marked ?."""
    c = pt(50, 50)
    step = POINT // n
    items = [{"kind": "circle", "center": c, "radius": 42, "fill": fill}]
    items += [line(c, ray_end(c, 90 + i * step, 42)) for i in range(n)] + [dot(c)]
    items += mark(c, 90, 90 + step, "?", r=12, arc_only=True)
    return figure(100, 100, T(en, ur), items)


def leaning(ground, texts, en, ur):
    """Something standing straight up from the ground (on the left), with a
    slanting line from its top to the ground making `ground`° with it."""
    w, h = 110, 120
    # narrow triangle: the square alone marks the right angle, labels kept apart
    items = triangle_items(90, ground, [None, *texts], (0, 0, w - 10, h), fill=False, dists=(None, 19, None))
    foot, far, top = items[0]["points"]
    items += [line(foot, pt(w - 4, foot[1])), line(foot, pt(foot[0], top[1] - 8)) if top[1] > 12 else line(foot, top)]
    return figure(w, h, T(en, ur), items)


# s3: the three totals
totals = (fan(pt(16, 60), [0, CORNER], [(0, CORNER, "90°")], arm=44)
          + fan(pt(112, 60), [0, LINE], [(0, LINE, "180°")], arm=36)
          + [line(pt(180, 40), ray_end(pt(180, 40), 0, 24)), dot(pt(180, 40)), *mark(pt(180, 40), 0, POINT, "360°", r=12, dist=26)])

roof = triangle(S8, S8, ["x", "x", "120°"], ticks=("left", "right"), size=(140, 80), alt=T(
    "A roof frame drawn as a triangle with two equal sloping sides (small marks show they are equal). The top angle is 120°; the two equal angles at the bottom are marked x.",
    "چھت کا ڈھانچہ ایک مثلث کی شکل میں جس کے دو ڈھلوان اضلاع برابر ہیں (چھوٹے نشان دکھاتے ہیں کہ وہ برابر ہیں)۔ اوپر کا زاویہ 120° ہے؛ نیچے کے دونوں برابر زاویوں پر x لکھا ہے۔"))

gate = on_line([75], ["75°", "?"])
gate["alt"] = T("A straight fence drawn as a line, with a gate turning out from a point on it. The angle between the gate and the fence on one side is 75°; on the other side it is marked ?.",
                "ایک سیدھی باڑ لکیر کی صورت میں، جس کے ایک نقطے سے دروازہ کھلتا ہے۔ ایک طرف دروازے اور باڑ کا زاویہ 75° ہے؛ دوسری طرف ? لکھا ہے۔")
ramp = on_line([15], ["15°", "?"])
ramp["alt"] = T("A straight road drawn as a line, with a ramp going up from a point on it at 15°. The angle between the ramp and the road on the other side is marked ?.",
                "ایک سیدھی سڑک لکیر کی صورت میں، جس کے ایک نقطے سے ڈھلوان 15° پر اوپر جاتی ہے۔ دوسری طرف ڈھلوان اور سڑک کے زاویے پر ? لکھا ہے۔")
roundabout = at_point([0, 100, 100 + 145], ["100°", "145°", "?"])
roundabout["alt"] = T("Three roads drawn as rays meeting at a roundabout. The angles between them, all the way round, are 100°, 145° and a missing angle marked ?.",
                      "تین سڑکیں شعاعوں کی صورت میں ایک گول چکر پر ملتی ہیں۔ ان کے درمیان پورے گرد زاویے 100°، 145° اور ایک نامعلوم زاویہ ہیں جس پر ? لکھا ہے۔")

FIGS = {
  "s2_foundation": triangle(90, 40, ["90°", "40°", "?"]),
  "s3_plan": figure(210, 76, T(
    "The three totals. Left: a square corner, a right angle of 90°. Middle: a straight line, a straight angle of 180°. Right: a ray with an arc going all the way round its point, a full turn of 360°.",
    "تین مجموعے۔ بائیں: ایک چوکور کونا، 90° کا قائمہ زاویہ۔ درمیان: ایک سیدھی لکیر، 180° کا مستقیم زاویہ۔ دائیں: ایک شعاع جس کے نقطے کے پورے گرد قوس ہے، 360° کا پورا چکر۔"),
    totals),
  "s4_ladder": leaning(70, ["70°", "?"],
    "A wall standing straight up from the ground, with a ladder leaning from the ground to the wall. The wall meets the ground at a right angle, marked with a square. The ladder makes 70° with the ground. The angle between the ladder and the wall, at the top, is marked ?.",
    "زمین سے سیدھی کھڑی دیوار، اور زمین سے دیوار تک ٹکی سیڑھی۔ دیوار زمین سے قائمہ زاویے پر ملتی ہے، جس پر مربع کا نشان ہے۔ سیڑھی زمین کے ساتھ 70° بناتی ہے۔ اوپر سیڑھی اور دیوار کے زاویے پر ? لکھا ہے۔"),
  "s5_roti": wheel(6,
    "A round roti cut from the middle into 6 equal pieces. The angle of one piece at the middle is marked ?.",
    "ایک گول روٹی درمیان سے 6 برابر ٹکڑوں میں کٹی ہوئی ہے۔ ایک ٹکڑے کے درمیان والے زاویے پر ? لکھا ہے۔", fill=True),
  "s6_gate": gate,
  "s7_clock": clock(4),
  "s8_roof": roof,
  "s9_find_error": ramp,
  "u2_line": on_line([48], ["48°", "?"]),
  "u4_triangle": triangle(45, 75, ["45°", "75°", "?"]),
  "u5_roundabout": roundabout,
  "qb_apply": leaning(55, ["55°", "?"],
    "A pole standing straight up from flat ground, with a rope from its top down to the ground. The pole meets the ground at a right angle, marked with a square. The rope makes 55° with the ground. The angle between the rope and the pole, at the top, is marked ?.",
    "ہموار زمین پر سیدھا کھڑا کھمبا، اور اس کی چوٹی سے زمین تک ایک رسی۔ کھمبا زمین سے قائمہ زاویے پر ملتا ہے، جس پر مربع کا نشان ہے۔ رسی زمین کے ساتھ 55° بناتی ہے۔ اوپر رسی اور کھمبے کے زاویے پر ? لکھا ہے۔"),
  "r_star": wheel(5,
    "A wheel with 5 equal spokes coming out from the middle. The angle between two spokes next to each other is marked ?.",
    "ایک پہیہ جس کے درمیان سے 5 برابر تیلیاں نکلتی ہیں۔ ساتھ والی دو تیلیوں کے درمیان زاویے پر ? لکھا ہے۔"),
  "r_clock": clock(2),
}


lesson = {
 "id": "g6-maths-09-angle-word-problems",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Solve real-life problems with angles on a line, around a point, in a triangle and on a clock, choosing the right total.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Angle word problems", "زاویوں کے عبارتی سوال"),
 "estimated_minutes": 16,
 "prerequisites": [{"skill": AN_TRIANGLE}, {"skill": AN_LINE}, {"skill": AN_PAIRS}, {"skill": AN_TYPES}],
 "misconceptions": [
   {"id": "wrong_total", "description": "Picks the wrong total (90°, 180° or 360°) for the situation."},
   {"id": "forgets_right_angle", "description": "Leaves out a right angle that the story gives in words (a wall meeting the ground)."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_total", "type": "recall", "step": {
     "id": "qb_total", "type": "choice",
     "prompt": T("Slices of a roti meet at the middle. Which total do their angles make?", "روٹی کے ٹکڑے درمیان میں ملتے ہیں۔ ان کے زاویوں کا مجموعہ کیا ہوگا؟"),
     "options": [
       opt("point", "360°, all the way around a point", "360°، نقطے کے پورے گرد", True, "Yes! The slices go all the way round.", "جی ہاں! ٹکڑے پورے گرد جاتے ہیں۔"),
       opt("line", "180°, a straight line", "180°، سیدھی لکیر", False, "The slices go all the way round the middle: 360°.", "ٹکڑے درمیان کے پورے گرد جاتے ہیں: 360°۔", "wrong_total"),
       opt("corner", "90°, a corner", "90°، ایک کونا", False, "The slices go all the way round the middle: 360°.", "ٹکڑے درمیان کے پورے گرد جاتے ہیں: 360°۔", "wrong_total"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("A pole stands straight up from flat ground. A rope from its top to the ground makes 55° with the ground. What angle does the rope make with the pole?",
       "ایک کھمبا ہموار زمین پر سیدھا کھڑا ہے۔ اس کی چوٹی سے زمین تک ایک رسی زمین کے ساتھ 55° بناتی ہے۔ رسی کھمبے کے ساتھ کتنا زاویہ بناتی ہے؟"),
     QB,
     T("Pole, ground and rope make a triangle with a right angle at the bottom.", "کھمبا، زمین اور رسی ایک مثلث بناتے ہیں جس کے نیچے قائمہ زاویہ ہے۔"),
     T("Right! 35°.", "درست! 35°"),
     T("180 − 90 − 55 = 35°.", "180 − 90 − 55 = 35°"),
     common_wrong=[wrong(125, "The pole meets the ground at 90°: 180 − 90 − 55 = 35°.", "کھمبا زمین سے 90° پر ملتا ہے: 180 − 90 − 55 = 35°", "forgets_right_angle")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("A roti is cut from the middle into 4 equal pieces. Hamza says each piece has a 45° angle at the middle. What went wrong?",
                 "ایک روٹی درمیان سے 4 برابر ٹکڑوں میں کاٹی گئی۔ حمزہ کہتا ہے ہر ٹکڑے کا درمیان میں زاویہ 45° ہے۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("point", "Around a point is 360°, so each is 360 ÷ 4 = 90°.", "نقطے کے گرد 360° ہے، اس لیے ہر ایک 360 ÷ 4 = 90°", True,
           "Yes! He shared 180° instead of 360°.", "جی ہاں! اس نے 360° کی بجائے 180° بانٹا۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "4 × 45 is only 180°, half the roti. Each piece is 90°.", "4 × 45 صرف 180° ہے، آدھی روٹی۔ ہر ٹکڑا 90° ہے۔", "wrong_total"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_which", "front": T("Which total?", "کون سا مجموعہ؟"),
    "back": T("Corner: 90°. Straight line or triangle: 180°. All the way round a point: 360°.", "کونا: 90°۔ سیدھی لکیر یا مثلث: 180°۔ نقطے کے پورے گرد: 360°۔")},
   {"id": "f_clock", "front": T("Angle between clock hour marks?", "گھڑی کے گھنٹوں کے نشانوں کے درمیان زاویہ؟"),
    "back": T("30°, because 360 ÷ 12 = 30.", "30°، کیونکہ 360 ÷ 12 = 30")},
 ],
 "home_tasks": [{"id": "h_clock", "text": T(
   "Look at a clock at home at 1, 2, 3 and 4 o'clock (or move the hands yourself). Work out the angle between the hands each time: 30° for every hour mark.",
   "گھر کی گھڑی کو 1، 2، 3 اور 4 بجے دیکھیں (یا خود سوئیاں گھمائیں)۔ ہر بار سوئیوں کا زاویہ نکالیں: ہر گھنٹے کے نشان کے لیے 30°۔")}],
 "glossary": [T("Ladder", "سیڑھی"), T("Clock hands", "گھڑی کی سوئیاں"), T("Roof", "چھت"), T("Total", "مجموعہ")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Angles are everywhere: ladders, clocks, roofs and even rotis! Let's solve some real puzzles.",
                     "زاویے ہر جگہ ہیں: سیڑھیاں، گھڑیاں، چھتیں اور روٹی بھی! آئیں کچھ اصل پہیلیاں حل کریں۔"),
    "text": T("Today we use everything from the Angles unit on real-life problems, then a short unit test. First, a quick check.",
              "آج ہم زاویوں کے پورے باب کو اصل زندگی کے سوالوں پر لگائیں گے، پھر ایک چھوٹا ٹیسٹ۔ پہلے ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("A triangle has angles of 90° and 40°. What is the third angle?", "ایک مثلث کے دو زاویے 90° اور 40° ہیں۔ تیسرا زاویہ کتنا ہے؟"),
     S2,
     T("A triangle is 180°.", "مثلث 180° ہے۔"),
     T("Right! 50°.", "درست! 50°"),
     T("180 − 90 − 40 = 50°.", "180 − 90 − 40 = 50°"),
     common_wrong=[wrong(140, "Don't forget the 90°: 180 − 90 − 40 = 50°.", "90° نہ بھولیں: 180 − 90 − 40 = 50°", "forgets_right_angle")],
     qtype="recall", skill=AN_TRIANGLE),
   {"id": "s3_plan", "type": "explain",
    "character": say("thinking", "First ask: is it a corner, a line, a triangle, or all the way round?",
                     "پہلے پوچھیں: یہ کونا ہے، لکیر ہے، مثلث ہے، یا پورا گرد؟"),
    "text": T("For an angle problem: 1) Picture it, or draw it. 2) Choose the total: a corner is 90°, a straight line or a triangle is 180°, all the way round a point is 360°. 3) Take the known angles away. Watch for right angles hidden in words, like a wall meeting the ground.",
              "زاویے کے سوال کے لیے: 1) تصور کریں یا بنائیں۔ 2) مجموعہ چنیں: کونا 90°، سیدھی لکیر یا مثلث 180°، نقطے کے پورے گرد 360°۔ 3) معلوم زاویے نفی کریں۔ الفاظ میں چھپے قائمہ زاویے دیکھیں، جیسے دیوار کا زمین سے ملنا۔")},
   number_question(
     "s4_ladder",
     T("A ladder leans against a wall. It makes 70° with the ground. The wall stands straight up from the ground. What angle does the ladder make with the wall?",
       "ایک سیڑھی دیوار سے ٹیک لگائے ہے۔ یہ زمین کے ساتھ 70° بناتی ہے۔ دیوار زمین سے سیدھی کھڑی ہے۔ سیڑھی دیوار کے ساتھ کتنا زاویہ بناتی ہے؟"),
     S4,
     T("Ladder, wall and ground make a triangle. The wall meets the ground at 90°.", "سیڑھی، دیوار اور زمین مثلث بناتے ہیں۔ دیوار زمین سے 90° پر ملتی ہے۔"),
     T("Right! 20°.", "درست! 20°"),
     T("180 − 90 − 70 = 20°.", "180 − 90 − 70 = 20°"),
     common_wrong=[wrong(110, "Don't forget the right angle at the wall: 180 − 90 − 70 = 20°.", "دیوار والا قائمہ زاویہ نہ بھولیں: 180 − 90 − 70 = 20°", "forgets_right_angle")]),
   number_question(
     "s5_roti",
     T("Ammi cuts a roti from the middle into 6 equal pieces. What angle does each piece make at the middle?", "امی ایک روٹی درمیان سے 6 برابر ٹکڑوں میں کاٹتی ہیں۔ ہر ٹکڑا درمیان میں کتنا زاویہ بناتا ہے؟"),
     S5,
     T("All the way round the middle is 360°.", "درمیان کے پورے گرد 360° ہے۔"),
     T("Right! 60° each.", "درست! ہر ایک 60°"),
     T("360 ÷ 6 = 60°.", "360 ÷ 6 = 60°"),
     common_wrong=[wrong(30, "That shared 180°. All the way round is 360°: 60°.", "اس میں 180° بانٹا۔ پورا گرد 360° ہے: 60°", "wrong_total")]),
   number_question(
     "s6_gate",
     T("A gate in a straight fence opens 75° from the fence on one side. What angle does it make with the fence on the other side?",
       "سیدھی باڑ میں ایک دروازہ ایک طرف باڑ سے 75° کھلتا ہے۔ دوسری طرف یہ باڑ کے ساتھ کتنا زاویہ بناتا ہے؟"),
     S6,
     T("The fence is a straight line: 180°.", "باڑ سیدھی لکیر ہے: 180°۔"),
     T("Right! 105°.", "درست! 105°"),
     T("180 − 75 = 105°.", "180 − 75 = 105°"),
     common_wrong=[wrong(15, "That used 90°. The fence is a straight line, 180°: 105°.", "اس میں 90° لیا۔ باڑ سیدھی لکیر، 180°، ہے: 105°", "wrong_total")]),
   number_question(
     "s7_clock",
     T("What is the smaller angle between the hands of a clock at 4 o'clock?", "4 بجے گھڑی کی سوئیوں کے درمیان چھوٹا زاویہ کتنا ہے؟"),
     S7,
     T("Each hour mark is 30°.", "ہر گھنٹے کا نشان 30° ہے۔"),
     T("Right! 4 × 30° = 120°.", "درست! 4 × 30° = 120°"),
     T("4 × 30° = 120°.", "4 × 30° = 120°"),
     common_wrong=[wrong(240, "240° is the bigger angle, the other way round. The smaller one is 120°.", "240° بڑا زاویہ ہے، دوسری طرف سے۔ چھوٹا 120° ہے۔"),
                   wrong(40, "Each hour is 30°, not 10°: 4 × 30 = 120°.", "ہر گھنٹہ 30° ہے، 10° نہیں: 4 × 30 = 120°")]),
   number_question(
     "s8_roof",
     T("A roof frame is an isosceles triangle. The angle at the top is 120°. What is each of the two equal angles at the bottom?",
       "چھت کا ڈھانچہ متساوی الساقین مثلث ہے۔ اوپر کا زاویہ 120° ہے۔ نیچے کے دونوں برابر زاویوں میں سے ہر ایک کتنا ہے؟"),
     S8,
     T("180 − 120, then share between two.", "180 − 120، پھر دو میں بانٹیں۔"),
     T("Right! 30° each.", "درست! ہر ایک 30°"),
     T("180 − 120 = 60, and 60 ÷ 2 = 30°.", "180 − 120 = 60، اور 60 ÷ 2 = 30°"),
     common_wrong=[wrong(60, "That is both bottom angles together. Each is 60 ÷ 2 = 30°.", "یہ نیچے کے دونوں زاویے مل کر ہیں۔ ہر ایک 60 ÷ 2 = 30°")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("A ramp goes up from a straight road at 15°. Sara says the angle between the ramp and the road on the other side is 90 − 15 = 75°. What went wrong?",
                "ایک ڈھلوان سیدھی سڑک سے 15° پر اوپر جاتی ہے۔ سارہ کہتی ہے دوسری طرف ڈھلوان اور سڑک کا زاویہ 90 − 15 = 75° ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("line", "The road is a straight line, so use 180°: 180 − 15 = 165°.", "سڑک سیدھی لکیر ہے، اس لیے 180° لیں: 180 − 15 = 165°", True,
          "Yes! There is no corner here, just a straight road.", "جی ہاں! یہاں کوئی کونا نہیں، صرف سیدھی سڑک ہے۔"),
      opt("point", "She should use 360°: 345°.", "اسے 360° لینا چاہیے: 345°", False,
          "The road is a straight line, not a full turn: 165°.", "سڑک سیدھی لکیر ہے، پورا چکر نہیں: 165°", "wrong_total"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "90° is a corner. A straight road is 180°: 165°.", "90° کونا ہے۔ سیدھی سڑک 180° ہے: 165°", "wrong_total"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "How do you know whether to use 90°, 180° or 360°? Can you teach me?",
                     "آپ کو کیسے پتا چلتا ہے کہ 90°، 180° یا 360° لینا ہے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: how do you choose between 90°, 180° and 360° in an angle problem?",
              "اپنے الفاظ میں بتائیں: زاویے کے سوال میں آپ 90°، 180° اور 360° میں سے کیسے چنتے ہیں؟"),
    "key_idea": "Look at what the angles make together: a corner (right angle) is 90°, a straight line or the inside of a triangle is 180°, and angles all the way round a point are 360°.",
    "levels": {
      "got_it": "Links each total to its situation: corner 90°, straight line or triangle 180°, round a point 360°.",
      "partly": "Gets one or two of the situations right.",
      "not_yet": "Gives no way to choose, or mixes them up."},
    "keywords": [
      ["corner", "right angle", "کونا", "قائمہ"],
      ["line", "straight", "triangle", "لکیر", "سیدھی", "مثلث"],
      ["round", "point", "full", "گرد", "نقطہ", "پورا"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Corner 90°, line or triangle 180°, all the way round 360°.", "بہت خوب! کونا 90°، لکیر یا مثلث 180°، پورا گرد 360°۔"),
      "partly": T("Good start! Can you add the other situations? Think of a corner, a line and a full turn.", "اچھی شروعات! کیا آپ باقی صورتیں بھی بتا سکتے ہیں؟ کونا، لکیر اور پورا چکر سوچیں۔"),
      "not_yet": T("Think of a book corner, a straight road and a whole roti. Which total goes with each?", "کتاب کا کونا، سیدھی سڑک اور پوری روٹی سوچیں۔ ہر ایک کے ساتھ کون سا مجموعہ ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   {"id": "s11_unit_test", "type": "explain",
    "character": say("encouraging", "Test time! Five questions from the whole Angles unit. You can do it!",
                     "ٹیسٹ کا وقت! زاویوں کے پورے باب سے پانچ سوال۔ آپ کر سکتے ہیں!"),
    "text": T("This short test has questions on types of angles, angles on a line, angle pairs, triangles and a real-life problem. Take your time.",
              "اس چھوٹے ٹیسٹ میں زاویوں کی اقسام، لکیر پر زاویے، زاویوں کے جوڑے، مثلث اور ایک اصل زندگی کا سوال ہے۔ آرام سے کریں۔")},
   kind_question("u1_kind", 135, T("Test 1: What kind of angle is 135°?", "ٹیسٹ 1: 135° کس قسم کا زاویہ ہے؟"),
                 qtype="recall", skill=AN_TYPES),
   number_question(
     "u2_line",
     T("Test 2: Two angles sit on a straight line. One is 48°. What is the other?", "ٹیسٹ 2: سیدھی لکیر پر دو زاویے ہیں۔ ایک 48° ہے۔ دوسرا کتنا ہے؟"),
     U2,
     T("180 − 48.", "180 − 48"),
     T("Right! 132°.", "درست! 132°"),
     T("180 − 48 = 132°.", "180 − 48 = 132°"),
     common_wrong=[wrong(312, "A line is 180°, not 360°: 132°.", "لکیر 180° ہے، 360° نہیں: 132°", "wrong_total")],
     qtype="apply", skill=AN_LINE),
   number_question(
     "u3_complement",
     T("Test 3: What is the complement of 58°?", "ٹیسٹ 3: 58° کا متمم کیا ہے؟"),
     U3,
     T("Complementary angles make 90°.", "متمم زاویے 90° بناتے ہیں۔"),
     T("Right! 32°.", "درست! 32°"),
     T("90 − 58 = 32°.", "90 − 58 = 32°"),
     common_wrong=[wrong(122, "122° is the supplement. The complement: 90 − 58 = 32°.", "122° مکمل زاویہ ہے۔ متمم: 90 − 58 = 32°", "wrong_total")],
     qtype="apply", skill=AN_PAIRS),
   number_question(
     "u4_triangle",
     T("Test 4: A triangle has angles of 45° and 75°. What is the third angle?", "ٹیسٹ 4: ایک مثلث کے دو زاویے 45° اور 75° ہیں۔ تیسرا زاویہ کتنا ہے؟"),
     U4,
     T("180 − 45 − 75.", "180 − 45 − 75"),
     T("Right! 60°.", "درست! 60°"),
     T("45 + 75 = 120, and 180 − 120 = 60°.", "45 + 75 = 120، اور 180 − 120 = 60°"),
     common_wrong=[wrong(120, "120 is the two angles added. Take it from 180: 60°.", "120 دونوں زاویوں کا مجموعہ ہے۔ 180 سے نفی کریں: 60°")],
     qtype="apply", skill=AN_TRIANGLE),
   number_question(
     "u5_roundabout",
     T("Test 5: Three roads meet at a roundabout. The angles between them are 100°, 145° and a missing one. What is the missing angle?",
       "ٹیسٹ 5: ایک گول چکر پر تین سڑکیں ملتی ہیں۔ ان کے درمیان زاویے 100°، 145° اور ایک نامعلوم ہیں۔ نامعلوم زاویہ کتنا ہے؟"),
     U5,
     T("The roads go all the way round: 360°.", "سڑکیں پورے گرد جاتی ہیں: 360°۔"),
     T("Right! 115°.", "درست! 115°"),
     T("100 + 145 = 245, and 360 − 245 = 115°.", "100 + 145 = 245، اور 360 − 245 = 115°"),
     common_wrong=[wrong(245, "245 is the two angles added. Take it from 360: 115°.", "245 دونوں زاویوں کا مجموعہ ہے۔ 360 سے نفی کریں: 115°")],
     qtype="apply"),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Angles unit complete! You solved real angle puzzles.", "زاویوں کا باب مکمل! آپ نے اصل زاویوں کی پہیلیاں حل کیں۔"),
    "text": T("Picture the problem, choose the total (corner 90°, line or triangle 180°, round a point 360°), then take away the angles you know. Look for right angles hidden in words, and on a clock use 30° for each hour mark.",
              "سوال کا تصور کریں، مجموعہ چنیں (کونا 90°، لکیر یا مثلث 180°، نقطے کے گرد 360°)، پھر معلوم زاویے نفی کریں۔ الفاظ میں چھپے قائمہ زاویے دیکھیں، اور گھڑی پر ہر گھنٹے کے نشان کے لیے 30° لیں۔"),
    "points": [T("Choose the right total first.", "پہلے صحیح مجموعہ چنیں۔"),
               T("Walls and poles stand at 90°.", "دیواریں اور کھمبے 90° پر کھڑے ہوتے ہیں۔")]},
 ],
 "review_questions": [
   {"id": "r_star", "type": "apply", "skill": SKILL, "step": number_question(
     "r_star",
     T("A wheel has 5 equal spokes from the middle. What is the angle between two spokes next to each other?", "ایک پہیے کے درمیان سے 5 برابر تیلیاں نکلتی ہیں۔ ساتھ والی دو تیلیوں کے درمیان زاویہ کتنا ہے؟"),
     R1,
     T("All the way round: 360 ÷ 5.", "پورا گرد: 360 ÷ 5"),
     T("Right! 72°.", "درست! 72°"),
     T("360 ÷ 5 = 72°.", "360 ÷ 5 = 72°"),
     common_wrong=[wrong(36, "That shared 180°. All the way round is 360°: 72°.", "اس میں 180° بانٹا۔ پورا گرد 360° ہے: 72°", "wrong_total")],
     qtype=None)},
   {"id": "r_clock", "type": "apply", "skill": SKILL, "step": number_question(
     "r_clock",
     T("What is the angle between the hands of a clock at 2 o'clock?", "2 بجے گھڑی کی سوئیوں کے درمیان زاویہ کتنا ہے؟"),
     R2,
     T("Each hour mark is 30°.", "ہر گھنٹے کا نشان 30° ہے۔"),
     T("Right! 60°.", "درست! 60°"),
     T("2 × 30° = 60°.", "2 × 30° = 60°"),
     common_wrong=[wrong(2, "2 is the hour. Each hour is 30°: 60°.", "2 گھنٹہ ہے۔ ہر گھنٹہ 30°: 60°")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Angles unit. No textbook text or exercises were used.",
   "Most mistakes in angle word problems come from choosing the wrong total, or missing a right angle given only in words (a wall, a pole). The steps practise both.",
   "The unit test (u1 to u5) has one question per earlier lesson plus a real-life problem. Each is tagged with that lesson's skill, so results feed back into the mastery of earlier lessons.",
   "The numbers were worked out in content/sources/g6-maths-09/angle_word_problems.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
attach(lesson, FIGS)
write(lesson)
