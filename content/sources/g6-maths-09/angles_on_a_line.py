import math

from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, AN_TYPES, AN_LINE)


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

SKILL = AN_LINE
LINE, POINT = 180, 360


def missing(total, *known):
    m = total - sum(known)
    assert 0 < m < total, (total, known)
    return m


# s4: a line split into 130 and ?
S4 = missing(LINE, 130)
assert S4 == 50 and POINT - 130 == 230
# s5: three angles on a line
S5 = missing(LINE, 40, 75)
assert S5 == 65 and 40 + 75 == 115 and POINT - 115 == 245
# s6: around a point
S6 = missing(POINT, 100, 150)
assert S6 == 110 and 100 + 150 == 250
# s7: four equal angles around a point
S7 = POINT // 4
assert S7 == 90 and 4 * S7 == POINT and LINE // 4 == 45
# s8: x + x + 40 on a line
S8 = missing(LINE, 40) // 2
assert S8 == 70 and S8 + S8 + 40 == LINE and missing(LINE, 40) == 140
# s9: 70 on a line; 290 uses the full turn by mistake
assert missing(LINE, 70) == 110 and POINT - 70 == 290
# s11: four angles around a point, one is a right angle
S11 = missing(POINT, 90, 120, 85)
assert S11 == 65 and missing(POINT, 120, 85) == 155
# question bank and review
QB = missing(LINE, 75)
assert QB == 105 and POINT - 75 == 285
R1 = missing(LINE, 145)
assert R1 == 35 and POINT - 145 == 215
R2 = missing(POINT, 200, 95)
assert R2 == 65 and 200 + 95 == 295


# ---- figures -------------------------------------------------------------
def at_point(rays, texts):
    """Rays from a point; the angles between them, going round, marked with texts."""
    edges = [*rays, rays[0] + POINT]
    assert len(texts) == len(rays)
    items = fan(pt(50, 50), rays, [(a, b, t) for a, b, t in zip(edges, edges[1:], texts)])
    en, ur = parts_text(texts)
    alt = T(f"{len(rays)} rays come out of one point. The angles between them, all the way round, are {en}.",
            f"ایک نقطے سے {len(rays)} شعاعیں نکلتی ہیں۔ ان کے درمیان پورے گرد زاویے یہ ہیں: {ur}۔")
    return figure(100, 100, alt, items)


def roti(cuts):
    c = pt(50, 50)
    items = [{"kind": "circle", "center": c, "radius": 42, "fill": True}]
    items += [line(c, ray_end(c, d, 42)) for d in cuts] + [dot(c)]
    return items


ROTI_CUTS = [20, 110, 170, 250, 315]
assert sorted(ROTI_CUTS) == ROTI_CUTS and ROTI_CUTS[-1] - ROTI_CUTS[0] < POINT


def deg(n):
    return f"{n}°"


# s3: one worked example of each total, numbers not used in the questions
EX_LINE = 60
EX_POINT = [10, 110, 250]
assert [b - a for a, b in zip(EX_POINT, EX_POINT[1:] + [EX_POINT[0] + POINT])] == [100, 140, 120]
rules = (fan(pt(48, 66), [0, LINE, EX_LINE], [(0, EX_LINE, deg(EX_LINE)), (EX_LINE, LINE, deg(LINE - EX_LINE))], arm=42)
         + fan(pt(140, 46), EX_POINT, [(10, 110, "100°"), (110, 250, "140°"), (250, 370, "120°")], arm=38))

FIGS = {
  "s1_hook": figure(100, 100, T(
    f"A round roti cut from the middle into {len(ROTI_CUTS)} slices of different sizes. All the slice corners meet at the centre.",
    f"ایک گول روٹی درمیان سے {len(ROTI_CUTS)} مختلف سائز کے ٹکڑوں میں کٹی ہوئی ہے۔ سب ٹکڑوں کے کونے مرکز پر ملتے ہیں۔"),
    roti(ROTI_CUTS)),
  "s3_rules": figure(184, 90, T(
    f"Left: a straight line split by a ray into {EX_LINE}° and {LINE - EX_LINE}°, which make 180°. Right: three rays from a point make angles of 100°, 140° and 120°, which make 360°.",
    f"بائیں: ایک سیدھی لکیر جسے ایک شعاع {EX_LINE}° اور {LINE - EX_LINE}° میں بانٹتی ہے، جو مل کر 180° ہیں۔ دائیں: ایک نقطے سے تین شعاعیں 100°، 140° اور 120° کے زاویے بناتی ہیں، جو مل کر 360° ہیں۔"),
    rules),
  "s4_line": on_line([S4], ["?", "130°"]),
  "s5_three": on_line([40, 40 + 75], ["40°", "75°", "?"]),
  "s6_point": at_point([0, 100, 100 + 150], ["100°", "150°", "?"]),
  "s8_two_equal": on_line([40, 40 + S8], ["40°", "x", "x"]),
  "s9_find_error": on_line([70], ["70°", "?"]),
  "s11_four": at_point([0, 90, 90 + 120, 90 + 120 + 85], ["90°", "120°", "85°", "?"]),
  "qb_apply": on_line([75], ["75°", "?"]),
  "qb_find_error": at_point([0, 120, 120 + 140], ["120°", "140°", "?"]),
  "r_line": on_line([R1], ["?", "145°"]),
  "r_point": at_point([0, 200, 200 + 95], ["200°", "95°", "?"]),
}


lesson = {
 "id": "g6-maths-09-angles-on-a-line",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Find missing angles using: angles on a straight line add up to 180°, and angles around a point add up to 360°.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Angles on a line and around a point", "سیدھی لکیر پر اور نقطے کے گرد زاویے"),
 "estimated_minutes": 13,
 "prerequisites": [{"skill": AN_TYPES}],
 "misconceptions": [
   {"id": "line_is_360", "description": "Uses 360° for angles on a straight line."},
   {"id": "point_is_180", "description": "Uses 180° for angles around a point."},
   {"id": "adds_known", "description": "Adds the known angles instead of taking them away from the total."},
   {"id": "forgets_an_angle", "description": "Leaves one known angle (often the right angle) out of the sum."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_point", "type": "recall", "step": {
     "id": "qb_point", "type": "choice",
     "prompt": T("The angles around a point add up to how many degrees?", "نقطے کے گرد زاویوں کا مجموعہ کتنے درجے ہوتا ہے؟"),
     "options": [
       opt("full", "360°", "360°", True, "Yes! Around a point is a full turn, 360°.", "جی ہاں! نقطے کے گرد پورا چکر ہے، 360°۔"),
       opt("half", "180°", "180°", False, "180° is a straight line, half a turn. Around a point is 360°.", "180° سیدھی لکیر، آدھا چکر ہے۔ نقطے کے گرد 360°۔", "point_is_180"),
       opt("quarter", "90°", "90°", False, "90° is a quarter turn. All the way around is 360°.", "90° چوتھائی چکر ہے۔ پورا گرد 360°۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("Two angles sit on a straight line. One is 75°. What is the other, in degrees?", "سیدھی لکیر پر دو زاویے ہیں۔ ایک 75° ہے۔ دوسرا کتنے درجے ہے؟"),
     QB,
     T("180 − 75.", "180 − 75"),
     T("Right! 105°.", "درست! 105°"),
     T("180 − 75 = 105°.", "180 − 75 = 105°"),
     common_wrong=[wrong(285, "That used 360°. A straight line is 180°: 180 − 75 = 105.", "اس میں 360° لیا۔ سیدھی لکیر 180° ہے: 180 − 75 = 105", "line_is_360")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Three angles meet at a point: 120°, 140° and a missing one. Zara says the missing angle is 180 − 120 − 140. What went wrong?",
                 "ایک نقطے پر تین زاویے ملتے ہیں: 120°، 140° اور ایک نامعلوم۔ زارا کہتی ہے نامعلوم زاویہ 180 − 120 − 140 ہے۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("full", "Around a point is 360°, not 180°. 360 − 120 − 140 = 100°.", "نقطے کے گرد 360° ہے، 180° نہیں۔ 360 − 120 − 140 = 100°", True,
           "Yes! 180° is only for a straight line.", "جی ہاں! 180° صرف سیدھی لکیر کے لیے ہے۔"),
       opt("add", "She should add: 120 + 140 = 260°.", "اسے جمع کرنا چاہیے: 120 + 140 = 260°", False,
           "Take the known angles away from 360°: 100°.", "معلوم زاویے 360° سے نفی کریں: 100°", "adds_known"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "180 − 120 − 140 is less than zero! Around a point use 360°: 100°.", "180 − 120 − 140 صفر سے کم ہے! نقطے کے گرد 360° لیں: 100°", "point_is_180"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_line", "front": T("Angles on a straight line add up to?", "سیدھی لکیر پر زاویوں کا مجموعہ؟"),
    "back": T("180°. If one is 130°, the other is 50°.", "180°۔ اگر ایک 130° ہے تو دوسرا 50°۔")},
   {"id": "f_point", "front": T("Angles around a point add up to?", "نقطے کے گرد زاویوں کا مجموعہ؟"),
    "back": T("360°, a full turn.", "360°، پورا چکر۔")},
 ],
 "home_tasks": [{"id": "h_roti", "text": T(
   "Cut a roti or a paper circle into 4 pieces from the middle (not all the same size). The angles at the middle add up to 360°. Lay two pieces with straight edges together on a line: those angles make 180°.",
   "روٹی یا کاغذ کے دائرے کو درمیان سے 4 ٹکڑوں میں کاٹیں (سب برابر نہ ہوں)۔ درمیان کے زاویوں کا مجموعہ 360° ہے۔ سیدھے کناروں والے دو ٹکڑے ایک لکیر پر رکھیں: وہ زاویے 180° بناتے ہیں۔")}],
 "glossary": [T("Straight line", "سیدھی لکیر"), T("Point", "نقطہ"), T("Full turn", "پورا چکر"), T("Missing angle", "نامعلوم زاویہ")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Cut a roti into slices from the middle. All the slice corners together make a full turn! How many degrees is that?",
                     "روٹی کو درمیان سے ٹکڑوں میں کاٹیں۔ سب ٹکڑوں کے کونے مل کر پورا چکر بناتے ہیں! یہ کتنے درجے ہے؟"),
    "text": T("Today we find missing angles on a straight line and around a point. First, a quick check.",
              "آج ہم سیدھی لکیر پر اور نقطے کے گرد نامعلوم زاویے نکالیں گے۔ پہلے ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("How many degrees is a straight angle?", "مستقیم زاویہ کتنے درجے کا ہوتا ہے؟"),
     LINE,
     T("Half of a full turn.", "پورے چکر کا آدھا"),
     T("Right! 180°.", "درست! 180°"),
     T("A straight angle is 180°.", "مستقیم زاویہ 180° ہے۔"),
     common_wrong=[wrong(90, "90° is a right angle. A straight angle is two of them: 180°.", "90° قائمہ زاویہ ہے۔ مستقیم ان میں سے دو ہے: 180°"),
                   wrong(360, "360° is a full turn. A straight angle is half: 180°.", "360° پورا چکر ہے۔ مستقیم آدھا ہے: 180°")],
     qtype="recall", skill=AN_TYPES),
   {"id": "s3_rules", "type": "explain",
    "character": say("happy", "Two numbers to remember: 180 for a line, 360 for a point!", "دو عدد یاد رکھیں: لکیر کے لیے 180، نقطے کے لیے 360!"),
    "text": T("Angles that sit together on a straight line add up to 180°. Angles that go all the way around a point add up to 360°. To find a missing angle, take the known angles away from 180° or 360°.",
              "سیدھی لکیر پر ساتھ ساتھ زاویوں کا مجموعہ 180° ہوتا ہے۔ نقطے کے پورے گرد زاویوں کا مجموعہ 360° ہوتا ہے۔ نامعلوم زاویہ نکالنے کے لیے معلوم زاویے 180° یا 360° سے نفی کریں۔")},
   number_question(
     "s4_line",
     T("A straight line is split into two angles. One is 130°. What is the other, in degrees?", "ایک سیدھی لکیر دو زاویوں میں تقسیم ہے۔ ایک 130° ہے۔ دوسرا کتنے درجے ہے؟"),
     S4,
     T("180 − 130.", "180 − 130"),
     T("Right! 50°. Check: 130 + 50 = 180.", "درست! 50°۔ جانچ: 130 + 50 = 180"),
     T("180 − 130 = 50°.", "180 − 130 = 50°"),
     common_wrong=[wrong(230, "That used 360°. A straight line is 180°: 50°.", "اس میں 360° لیا۔ سیدھی لکیر 180° ہے: 50°", "line_is_360")]),
   number_question(
     "s5_three",
     T("Three angles sit on a straight line: 40°, 75° and a missing one. What is the missing angle?", "سیدھی لکیر پر تین زاویے ہیں: 40°، 75° اور ایک نامعلوم۔ نامعلوم زاویہ کتنا ہے؟"),
     S5,
     T("40 + 75 = 115. Then 180 − 115.", "40 + 75 = 115۔ پھر 180 − 115"),
     T("Right! 65°.", "درست! 65°"),
     T("180 − 115 = 65°.", "180 − 115 = 65°"),
     common_wrong=[wrong(115, "115 is the two known angles. Take it from 180: 65°.", "115 دو معلوم زاویے ہیں۔ 180 سے نفی کریں: 65°", "adds_known"),
                   wrong(245, "That used 360°. On a line use 180°: 65°.", "اس میں 360° لیا۔ لکیر پر 180° لیں: 65°", "line_is_360")]),
   number_question(
     "s6_point",
     T("Three angles meet around a point: 100°, 150° and a missing one. What is the missing angle?", "ایک نقطے کے گرد تین زاویے ملتے ہیں: 100°، 150° اور ایک نامعلوم۔ نامعلوم زاویہ کتنا ہے؟"),
     S6,
     T("Around a point: 360 − 100 − 150.", "نقطے کے گرد: 360 − 100 − 150"),
     T("Right! 110°.", "درست! 110°"),
     T("100 + 150 = 250, and 360 − 250 = 110°.", "100 + 150 = 250، اور 360 − 250 = 110°"),
     common_wrong=[wrong(250, "250 is the two known angles. Take it from 360: 110°.", "250 دو معلوم زاویے ہیں۔ 360 سے نفی کریں: 110°", "adds_known")]),
   number_question(
     "s7_equal",
     T("Four equal angles meet around a point. How big is each one?", "ایک نقطے کے گرد چار برابر زاویے ملتے ہیں۔ ہر ایک کتنا بڑا ہے؟"),
     S7,
     T("360 ÷ 4.", "360 ÷ 4"),
     T("Right! 90°: four right angles, like a plus sign.", "درست! 90°: چار قائمہ زاویے، جمع کے نشان کی طرح۔"),
     T("360 ÷ 4 = 90°.", "360 ÷ 4 = 90°"),
     common_wrong=[wrong(45, "That used 180°. Around a point is 360°: 360 ÷ 4 = 90°.", "اس میں 180° لیا۔ نقطے کے گرد 360° ہے: 360 ÷ 4 = 90°", "point_is_180")]),
   number_question(
     "s8_two_equal",
     T("On a straight line there is a 40° angle and two equal angles. How big is each equal angle?", "سیدھی لکیر پر ایک 40° کا زاویہ اور دو برابر زاویے ہیں۔ ہر برابر زاویہ کتنا ہے؟"),
     S8,
     T("180 − 40 = 140. Share it between two.", "180 − 40 = 140۔ اسے دو میں بانٹیں۔"),
     T("Right! 70°. Check: 70 + 70 + 40 = 180.", "درست! 70°۔ جانچ: 70 + 70 + 40 = 180"),
     T("180 − 40 = 140, and 140 ÷ 2 = 70°.", "180 − 40 = 140، اور 140 ÷ 2 = 70°"),
     common_wrong=[wrong(140, "That is both equal angles together. Each is 140 ÷ 2 = 70°.", "یہ دونوں برابر زاویے مل کر ہیں۔ ہر ایک 140 ÷ 2 = 70°")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Two angles sit on a straight line. One is 70°. Usman says the other is 360 − 70 = 290°. What went wrong?",
                "سیدھی لکیر پر دو زاویے ہیں۔ ایک 70° ہے۔ عثمان کہتا ہے دوسرا 360 − 70 = 290° ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("line", "A straight line is 180°. 180 − 70 = 110°.", "سیدھی لکیر 180° ہے۔ 180 − 70 = 110°", True,
          "Yes! 360° is for a full turn around a point.", "جی ہاں! 360° نقطے کے گرد پورے چکر کے لیے ہے۔"),
      opt("add", "He should add: 70 + 70 = 140°.", "اسے جمع کرنا چاہیے: 70 + 70 = 140°", False,
          "The two angles needn't be equal. 180 − 70 = 110°.", "دونوں زاویوں کا برابر ہونا ضروری نہیں۔ 180 − 70 = 110°"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "290° is more than a straight line! 180 − 70 = 110°.", "290° تو سیدھی لکیر سے بھی زیادہ ہے! 180 − 70 = 110°", "line_is_360"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why do the angles on a straight line always add up to 180°? Can you teach me?",
                     "سیدھی لکیر پر زاویوں کا مجموعہ ہمیشہ 180° کیوں ہوتا ہے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why do angles on a straight line add up to 180°?",
              "اپنے الفاظ میں بتائیں: سیدھی لکیر پر زاویوں کا مجموعہ 180° کیوں ہوتا ہے؟"),
    "key_idea": "A straight line is half a turn, a straight angle of 180°. The angles on it just split that half turn into parts, so together they still make 180°.",
    "levels": {
      "got_it": "Says a straight line is a straight angle or half a turn (180°), and the angles on it are parts of it.",
      "partly": "Says a straight line is 180° without saying the angles are its parts, or the reverse.",
      "not_yet": "Gives no reason, or says it is just the rule."},
    "keywords": [
      ["half", "straight angle", "آدھا", "مستقیم", "aadha"],
      ["turn", "360", "چکر", "chakkar"],
      ["parts", "split", "together", "حصے", "مل کر", "hissay"]],
    "fallback_feedback": {
      "got_it": T("Well explained! The angles are just parts of one straight angle, 180°.", "بہت خوب! یہ زاویے ایک مستقیم زاویے، 180°، کے حصے ہیں۔"),
      "partly": T("Good start! Now say how the angles on the line are parts of the straight angle.", "اچھی شروعات! اب بتائیں لکیر کے زاویے مستقیم زاویے کے حصے کیسے ہیں۔"),
      "not_yet": T("A straight line is half a turn. How many degrees is half of 360°? The angles share that.", "سیدھی لکیر آدھا چکر ہے۔ 360° کا آدھا کتنا ہے؟ زاویے اسی کو بانٹتے ہیں۔")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_four",
     T("Four angles meet around a point: a right angle (90°), 120°, 85° and a missing one. What is the missing angle?",
       "ایک نقطے کے گرد چار زاویے ملتے ہیں: ایک قائمہ زاویہ (90°)، 120°، 85° اور ایک نامعلوم۔ نامعلوم زاویہ کتنا ہے؟"),
     S11,
     T("90 + 120 + 85 = 295. Then 360 − 295.", "90 + 120 + 85 = 295۔ پھر 360 − 295"),
     T("Right! 65°.", "درست! 65°"),
     T("360 − 295 = 65°.", "360 − 295 = 65°"),
     common_wrong=[wrong(155, "Don't forget the right angle: 360 − 90 − 120 − 85 = 65°.", "قائمہ زاویہ نہ بھولیں: 360 − 90 − 120 − 85 = 65°", "forgets_an_angle")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "180 for a line, 360 for a point. Well done!", "لکیر کے لیے 180، نقطے کے لیے 360۔ شاباش!"),
    "text": T("Angles on a straight line add up to 180°. Angles around a point add up to 360°. To find a missing angle, add the known ones and take the sum away from 180° or 360°. Check by adding them all back up.",
              "سیدھی لکیر پر زاویوں کا مجموعہ 180° ہے۔ نقطے کے گرد زاویوں کا مجموعہ 360° ہے۔ نامعلوم زاویے کے لیے معلوم زاویے جمع کریں اور 180° یا 360° سے نفی کریں۔ سب کو دوبارہ جمع کر کے جانچیں۔"),
    "points": [T("Straight line: 180°.", "سیدھی لکیر: 180°۔"),
               T("Around a point: 360°.", "نقطے کے گرد: 360°۔")]},
 ],
 "review_questions": [
   {"id": "r_line", "type": "apply", "skill": SKILL, "step": number_question(
     "r_line",
     T("Two angles sit on a straight line. One is 145°. What is the other?", "سیدھی لکیر پر دو زاویے ہیں۔ ایک 145° ہے۔ دوسرا کتنا ہے؟"),
     R1,
     T("180 − 145.", "180 − 145"),
     T("Right! 35°.", "درست! 35°"),
     T("180 − 145 = 35°.", "180 − 145 = 35°"),
     common_wrong=[wrong(215, "Use 180° for a line: 35°.", "لکیر کے لیے 180° لیں: 35°", "line_is_360")],
     qtype=None)},
   {"id": "r_point", "type": "apply", "skill": SKILL, "step": number_question(
     "r_point",
     T("Three angles meet around a point: 200°, 95° and a missing one. What is the missing angle?", "ایک نقطے کے گرد تین زاویے ہیں: 200°، 95° اور ایک نامعلوم۔ نامعلوم زاویہ کتنا ہے؟"),
     R2,
     T("360 − 200 − 95.", "360 − 200 − 95"),
     T("Right! 65°.", "درست! 65°"),
     T("200 + 95 = 295, and 360 − 295 = 65°.", "200 + 95 = 295، اور 360 − 295 = 65°"),
     common_wrong=[wrong(295, "Take the known angles from 360: 65°.", "معلوم زاویے 360 سے نفی کریں: 65°", "adds_known")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Angles unit. No textbook text or exercises were used.",
   "The two totals are tied to turns: a straight line is half a turn (180°), all the way round is a full turn (360°). The most common slip is using the wrong total, so several wrong answers catch it.",
   "Urdu terms to check: سیدھی لکیر (straight line), نقطہ (point), پورا چکر (full turn), نامعلوم زاویہ (missing angle).",
   "The numbers were worked out in content/sources/g6-maths-09/angles_on_a_line.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
attach(lesson, FIGS)
write(lesson)
