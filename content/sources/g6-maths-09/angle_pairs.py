import math

from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, AN_TYPES, AN_LINE, AN_PAIRS)


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

SKILL = AN_PAIRS
CORNER, LINE = 90, 180


def complement(a):
    assert 0 < a < CORNER, a
    return CORNER - a


def supplement(a):
    assert 0 < a < LINE, a
    return LINE - a


def pair_kind(a, b):
    if a + b == CORNER:
        return "comp"
    if a + b == LINE:
        return "supp"
    return "neither"


# s2
S2 = LINE - 150
assert S2 == 30
# s4, s5
S4 = complement(30)
assert S4 == 60 and supplement(30) == 150
S5 = supplement(65)
assert S5 == 115 and complement(65) == 25
# s6, s7
assert pair_kind(35, 55) == "comp" and pair_kind(110, 70) == "supp"
# s8: an angle equal to its own complement
S8 = CORNER // 2
assert complement(S8) == S8 == 45
# s9: complement of 40 is 50, not 140
assert complement(40) == 50 and supplement(40) == 140
# s11: supplement is 100 -> angle 80 -> complement 10
S11_ANGLE = LINE - 100
S11 = complement(S11_ANGLE)
assert S11_ANGLE == 80 and S11 == 10
# s10: an obtuse angle has no complement
assert all(CORNER - a <= 0 for a in range(91, 180))
# question bank and review
QB = supplement(128)
assert QB == 52 and 360 - 128 == 232
assert supplement(120) == 60
R1 = complement(72)
assert R1 == 18 and supplement(72) == 108
R2 = supplement(45)
assert R2 == 135 and complement(45) == 45


def pair_question(id, a, b, *, qtype="apply"):
    right = pair_kind(a, b)
    s = a + b
    step = {"id": id, "type": "choice"}
    if qtype:
        step["question_type"] = qtype
    step["prompt"] = T(f"Are {a}° and {b}° complementary, supplementary or neither?",
                       f"کیا {a}° اور {b}° متمم ہیں، مکمل ہیں یا کوئی نہیں؟")
    why = T(f"{a} + {b} = {s}.", f"{a} + {b} = {s}۔")
    step["options"] = [
        opt("comp", "Complementary", "متمم", right == "comp",
            f"{why['en']} " + ("Yes! They make 90°." if right == "comp" else "Complementary angles make 90°."),
            f"{why['ur']} " + ("جی ہاں! یہ 90° بناتے ہیں۔" if right == "comp" else "متمم زاویے 90° بناتے ہیں۔"),
            None if right == "comp" else "mixes_up_pairs"),
        opt("supp", "Supplementary", "مکمل", right == "supp",
            f"{why['en']} " + ("Yes! They make 180°." if right == "supp" else "Supplementary angles make 180°."),
            f"{why['ur']} " + ("جی ہاں! یہ 180° بناتے ہیں۔" if right == "supp" else "مکمل زاویے 180° بناتے ہیں۔"),
            None if right == "supp" else "mixes_up_pairs"),
        opt("neither", "Neither", "کوئی نہیں", right == "neither",
            f"{why['en']} " + ("Yes! That is neither 90° nor 180°." if right == "neither" else "Look at the total again."),
            f"{why['ur']} " + ("جی ہاں! یہ نہ 90° ہے نہ 180°۔" if right == "neither" else "مجموعہ دوبارہ دیکھیں۔")),
    ]
    return step



# ---- figures -------------------------------------------------------------
def deg(n):
    return f"{n}°"


def corner_items(v, split, texts, arm):
    """A right-angle corner (arms at 0° and 90°) split by a ray at split°."""
    return fan(v, [0, CORNER, split], [(0, split, texts[0]), (split, CORNER, texts[1])], arm=arm)


def in_corner(split, texts):
    en, ur = parts_text(texts)
    alt = T(f"A square corner, a right angle of 90°: one arm goes right and one goes straight up. A ray from the corner splits it into {en}.",
            f"ایک چوکور کونا، 90° کا قائمہ زاویہ: ایک بازو دائیں اور ایک سیدھا اوپر جاتا ہے۔ کونے سے ایک شعاع اسے ان حصوں میں بانٹتی ہے: {ur}۔")
    return figure(90, 90, alt, corner_items(pt(16, 74), split, texts, 66))


def past_corner(a):
    """An obtuse angle with a dashed ray at 90°: it is already past the corner."""
    assert CORNER < a < LINE
    v = pt(60, 64)
    items = [line(v, ray_end(v, CORNER, 50), dashed=True), label(ray_end(v, CORNER, 57), "90°")]
    items += fan(v, [0, a], [], arm=50) + mark(v, 0, a, deg(a), r=14, dist=26)
    alt = T(f"An angle of {a}° marked with an arc. A dashed ray straight up shows 90°: the {a}° arm has already gone past it.",
            f"{a}° کا زاویہ جو ایک قوس سے دکھایا گیا ہے۔ سیدھی اوپر ایک ڈیش والی شعاع 90° دکھاتی ہے: {a}° والا بازو اس سے آگے نکل چکا ہے۔")
    return figure(120, 80, alt, items)


def wedge(v, a0, a1, length):
    return {"kind": "polygon", "points": [v, ray_end(v, a0, length), ray_end(v, a1, length)], "fill": True}


# s1: two puzzle pieces, 30° and 60°, lying apart
HOOK = (30, 60)
assert sum(HOOK) == CORNER
p1, p2 = pt(16, 58), pt(72, 58)
hook = [wedge(p1, 0, HOOK[0], 48), *mark(p1, 0, HOOK[0], deg(HOOK[0]), r=14),
        wedge(p2, 0, HOOK[1], 44), *mark(p2, 0, HOOK[1], deg(HOOK[1]), r=12)]

# s3: the same 30° as part of a corner and as part of a straight line
EX = 30
pairs = (corner_items(pt(16, 76), EX, [deg(EX), deg(complement(EX))], 58)
         + fan(pt(146, 76), [0, LINE, EX], [(0, EX, deg(EX)), (EX, LINE, deg(supplement(EX)))], arm=50))

FIGS = {
  "s1_hook": figure(120, 72, T(
    f"Two shaded angle pieces lying apart, like puzzle pieces: one of {HOOK[0]}° and one of {HOOK[1]}°.",
    f"دو سایہ دار زاویے کے ٹکڑے الگ الگ پڑے ہیں، پہیلی کے ٹکڑوں کی طرح: ایک {HOOK[0]}° کا اور ایک {HOOK[1]}° کا۔"),
    hook),
  "s2_foundation": on_line([S2], ["?", "150°"]),
  "s3_pairs": figure(200, 92, T(
    f"Left: a square corner, 90°, split by a ray into {EX}° and {complement(EX)}°: complementary angles. Right: a straight line, 180°, split by a ray into {EX}° and {supplement(EX)}°: supplementary angles.",
    f"بائیں: ایک چوکور کونا، 90°، جسے ایک شعاع {EX}° اور {complement(EX)}° میں بانٹتی ہے: متمم زاویے۔ دائیں: ایک سیدھی لکیر، 180°، جسے ایک شعاع {EX}° اور {supplement(EX)}° میں بانٹتی ہے: مکمل زاویے۔"),
    pairs),
  "s4_complement": in_corner(30, ["30°", "?"]),
  "s5_supplement": on_line([65], ["65°", "?"]),
  "s8_self": in_corner(S8, ["x", "x"]),
  "s9_find_error": in_corner(40, ["40°", "?"]),
  "s10_explain_why": past_corner(100),
  "s11_two_step": on_line([S11_ANGLE], ["?", "100°"]),
  "qb_apply": on_line([QB], ["?", "128°"]),
  "qb_find_error": past_corner(120),
  "r_comp": in_corner(72, ["72°", "?"]),
  "r_supp": on_line([45], ["45°", "?"]),
}


lesson = {
 "id": "g6-maths-09-complementary-supplementary",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Recognise complementary angles (sum 90°) and supplementary angles (sum 180°), and find a missing complement or supplement.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Complementary and supplementary angles", "متمم اور مکمل زاویے"),
 "estimated_minutes": 13,
 "prerequisites": [{"skill": AN_LINE}, {"skill": AN_TYPES}],
 "misconceptions": [
   {"id": "mixes_up_pairs", "description": "Mixes up complementary (90°) and supplementary (180°)."},
   {"id": "complement_from_180", "description": "Finds a complement by taking the angle from 180° instead of 90°."},
   {"id": "supplement_from_90", "description": "Finds a supplement by taking the angle from 90° instead of 180°."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_comp", "type": "recall", "step": {
     "id": "qb_comp", "type": "choice",
     "prompt": T("Complementary angles add up to how many degrees?", "متمم زاویوں کا مجموعہ کتنے درجے ہوتا ہے؟"),
     "options": [
       opt("ninety", "90°", "90°", True, "Yes! Complementary angles make a corner, 90°.", "جی ہاں! متمم زاویے کونا، 90°، بناتے ہیں۔"),
       opt("oneeighty", "180°", "180°", False, "180° is for supplementary angles. Complementary make 90°.", "180° مکمل زاویوں کے لیے ہے۔ متمم 90° بناتے ہیں۔", "mixes_up_pairs"),
       opt("threesixty", "360°", "360°", False, "360° is a full turn. Complementary angles make 90°.", "360° پورا چکر ہے۔ متمم زاویے 90° بناتے ہیں۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("What is the supplement of 128°?", "128° کا مکمل زاویہ کیا ہے؟"),
     QB,
     T("Supplementary angles make 180°: 180 − 128.", "مکمل زاویے 180° بناتے ہیں: 180 − 128"),
     T("Right! 52°.", "درست! 52°"),
     T("180 − 128 = 52°.", "180 − 128 = 52°"),
     common_wrong=[wrong(232, "Supplementary is 180°, not 360°: 180 − 128 = 52°.", "مکمل 180° ہے، 360° نہیں: 180 − 128 = 52°")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Kamran says the complement of 120° is 60°. What went wrong?", "کامران کہتا ہے 120° کا متمم 60° ہے۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("none", "120° is more than 90°, so it has no complement. 60° is its supplement.", "120° تو 90° سے زیادہ ہے، اس لیے اس کا کوئی متمم نہیں۔ 60° اس کا مکمل زاویہ ہے۔", True,
           "Yes! Only acute angles have a complement.", "جی ہاں! صرف حادہ زاویوں کا متمم ہوتا ہے۔"),
       opt("thirty", "The complement is 30°.", "متمم 30° ہے۔", False,
           "120 + 30 is 150, not 90. 120° has no complement.", "120 + 30 = 150، نہ کہ 90۔ 120° کا کوئی متمم نہیں۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "120 + 60 = 180, so 60° is the supplement, not the complement.", "120 + 60 = 180، اس لیے 60° مکمل ہے، متمم نہیں۔", "mixes_up_pairs"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_comp", "front": T("Complementary angles?", "متمم زاویے؟"),
    "back": T("Two angles that add up to 90°, like 30° and 60°. Think C for Corner.", "دو زاویے جن کا مجموعہ 90° ہو، جیسے 30° اور 60°۔ C یعنی Corner (کونا) یاد رکھیں۔")},
   {"id": "f_supp", "front": T("Supplementary angles?", "مکمل زاویے؟"),
    "back": T("Two angles that add up to 180°, like 65° and 115°. Think S for Straight.", "دو زاویے جن کا مجموعہ 180° ہو، جیسے 65° اور 115°۔ S یعنی Straight (سیدھی) یاد رکھیں۔")},
 ],
 "home_tasks": [{"id": "h_corner", "text": T(
   "Put a ruler across the corner of a book so it makes two angles in the corner. Those two angles are complementary: together they make 90°. Then lay the ruler across a straight edge: the two angles are supplementary.",
   "کتاب کے کونے پر رولر ترچھا رکھیں تاکہ کونے میں دو زاویے بنیں۔ یہ دونوں متمم ہیں: مل کر 90° بناتے ہیں۔ پھر رولر کو سیدھے کنارے پر رکھیں: دونوں زاویے مکمل ہیں۔")}],
 "glossary": [T("Complementary angles", "متمم زاویے"), T("Supplementary angles", "مکمل زاویے"), T("Complement", "متمم"), T("Supplement", "مکمل زاویہ")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Some angles come in pairs that fit together perfectly, like two puzzle pieces. Let's find out how!",
                     "کچھ زاویے جوڑوں میں آتے ہیں جو پہیلی کے دو ٹکڑوں کی طرح بالکل جڑ جاتے ہیں۔ آئیں دیکھیں کیسے!"),
    "text": T("Today we meet two special pairs of angles. First, a quick check.", "آج ہم زاویوں کے دو خاص جوڑوں سے ملیں گے۔ پہلے ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("Two angles sit on a straight line. One is 150°. What is the other?", "سیدھی لکیر پر دو زاویے ہیں۔ ایک 150° ہے۔ دوسرا کتنا ہے؟"),
     S2,
     T("A straight line is 180°.", "سیدھی لکیر 180° ہے۔"),
     T("Right! 30°.", "درست! 30°"),
     T("180 − 150 = 30°.", "180 − 150 = 30°"),
     common_wrong=[wrong(210, "Use 180° for a line: 30°.", "لکیر کے لیے 180° لیں: 30°")],
     qtype="recall", skill=AN_LINE),
   {"id": "s3_pairs", "type": "explain",
    "character": say("happy", "C for Corner, 90°. S for Straight, 180°!", "C یعنی کونا، 90°۔ S یعنی سیدھی لکیر، 180°!"),
    "text": T("Two angles are complementary if they add up to 90°: together they fill a corner. Two angles are supplementary if they add up to 180°: together they make a straight line. The complement of 30° is 90 − 30 = 60°. The supplement of 30° is 180 − 30 = 150°.",
              "دو زاویے متمم ہیں اگر ان کا مجموعہ 90° ہو: مل کر کونا بھرتے ہیں۔ دو زاویے مکمل ہیں اگر ان کا مجموعہ 180° ہو: مل کر سیدھی لکیر بناتے ہیں۔ 30° کا متمم 90 − 30 = 60° ہے۔ 30° کا مکمل زاویہ 180 − 30 = 150° ہے۔")},
   number_question(
     "s4_complement",
     T("What is the complement of 30°?", "30° کا متمم کیا ہے؟"),
     S4,
     T("Complementary angles make 90°.", "متمم زاویے 90° بناتے ہیں۔"),
     T("Right! 60°. 30 + 60 = 90.", "درست! 60°۔ 30 + 60 = 90"),
     T("90 − 30 = 60°.", "90 − 30 = 60°"),
     common_wrong=[wrong(150, "150° is the supplement (180°). The complement uses 90°: 60°.", "150° مکمل زاویہ ہے (180°)۔ متمم میں 90° لیں: 60°", "complement_from_180")]),
   number_question(
     "s5_supplement",
     T("What is the supplement of 65°?", "65° کا مکمل زاویہ کیا ہے؟"),
     S5,
     T("Supplementary angles make 180°.", "مکمل زاویے 180° بناتے ہیں۔"),
     T("Right! 115°. 65 + 115 = 180.", "درست! 115°۔ 65 + 115 = 180"),
     T("180 − 65 = 115°.", "180 − 65 = 115°"),
     common_wrong=[wrong(25, "25° is the complement (90°). The supplement uses 180°: 115°.", "25° متمم ہے (90°)۔ مکمل میں 180° لیں: 115°", "supplement_from_90")]),
   pair_question("s6_which", 35, 55),
   pair_question("s7_which", 110, 70),
   number_question(
     "s8_self",
     T("An angle is equal to its own complement. How big is it?", "ایک زاویہ اپنے متمم کے برابر ہے۔ یہ کتنا بڑا ہے؟"),
     S8,
     T("Two equal angles make 90°.", "دو برابر زاویے 90° بناتے ہیں۔"),
     T("Right! 45° + 45° = 90°.", "درست! 45° + 45° = 90°"),
     T("90 ÷ 2 = 45°.", "90 ÷ 2 = 45°"),
     common_wrong=[wrong(90, "90° with its complement would make more than 90°. Half of 90: 45°.", "90° اور اس کا متمم 90° سے زیادہ ہو جائے گا۔ 90 کا آدھا: 45°")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Ayesha says the complement of 40° is 140°. What went wrong?", "عائشہ کہتی ہے 40° کا متمم 140° ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("ninety", "Complementary means 90°. 90 − 40 = 50°.", "متمم کا مطلب 90°۔ 90 − 40 = 50°", True,
          "Yes! 140° is the supplement, using 180°.", "جی ہاں! 140° مکمل زاویہ ہے، 180° سے۔"),
      opt("bigger", "It should be bigger, 320°.", "یہ بڑا ہونا چاہیے، 320°۔", False,
          "320° uses 360°. The complement uses 90°: 50°.", "320° میں 360° لیا۔ متمم میں 90° لیں: 50°"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "40 + 140 = 180, so 140° is the supplement. The complement is 50°.", "40 + 140 = 180، اس لیے 140° مکمل ہے۔ متمم 50° ہے۔", "complement_from_180"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Can a 100° angle have a complement? Why or why not? Can you teach me?",
                     "کیا 100° کے زاویے کا متمم ہو سکتا ہے؟ کیوں یا کیوں نہیں؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why does an obtuse angle, like 100°, have no complement?",
              "اپنے الفاظ میں بتائیں: منفرجہ زاویے، جیسے 100°، کا کوئی متمم کیوں نہیں ہوتا؟"),
    "key_idea": "Complementary angles add up to 90°. An obtuse angle is already more than 90°, so there is nothing left to add: no angle can make the total 90°.",
    "levels": {
      "got_it": "Says complements add to 90° and the obtuse angle is already more than 90°, so nothing is left.",
      "partly": "Says 100° is more than 90° without linking it to the 90° total, or the reverse.",
      "not_yet": "Gives a number like 80° or −10°, or no reason."},
    "keywords": [
      ["90", "corner", "کونا", "kona"],
      ["more", "bigger", "already", "زیادہ", "بڑا", "zyada"],
      ["nothing", "no angle", "left", "کچھ نہیں", "باقی"]],
    "fallback_feedback": {
      "got_it": T("Well explained! 100° is already past 90°, so no angle can be added to make 90°.", "بہت خوب! 100° پہلے ہی 90° سے آگے ہے، اس لیے کوئی زاویہ جمع کر کے 90° نہیں بن سکتا۔"),
      "partly": T("Good start! Now say what complementary angles must add up to.", "اچھی شروعات! اب بتائیں متمم زاویوں کا مجموعہ کتنا ہونا چاہیے۔"),
      "not_yet": T("Complementary angles add up to 90°. Is 100° more or less than 90°?", "متمم زاویوں کا مجموعہ 90° ہوتا ہے۔ کیا 100°، 90° سے زیادہ ہے یا کم؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_two_step",
     T("The supplement of an angle is 100°. What is the complement of the same angle?", "ایک زاویے کا مکمل زاویہ 100° ہے۔ اسی زاویے کا متمم کیا ہے؟"),
     S11,
     T("First find the angle: 180 − 100. Then take it from 90.", "پہلے زاویہ نکالیں: 180 − 100۔ پھر اسے 90 سے نفی کریں۔"),
     T("Right! The angle is 80°, so its complement is 10°.", "درست! زاویہ 80° ہے، اس لیے اس کا متمم 10° ہے۔"),
     T("180 − 100 = 80°, and 90 − 80 = 10°.", "180 − 100 = 80°، اور 90 − 80 = 10°"),
     common_wrong=[wrong(S11_ANGLE, "80° is the angle itself. Its complement is 90 − 80 = 10°.", "80° تو خود زاویہ ہے۔ اس کا متمم 90 − 80 = 10° ہے۔")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "You know your angle pairs now!", "اب آپ زاویوں کے جوڑے جانتے ہیں!"),
    "text": T("Complementary angles add up to 90° (C for Corner). Supplementary angles add up to 180° (S for Straight). To find a complement, take the angle from 90°; to find a supplement, take it from 180°. Only acute angles have a complement.",
              "متمم زاویوں کا مجموعہ 90° ہے (C یعنی کونا)۔ مکمل زاویوں کا مجموعہ 180° ہے (S یعنی سیدھی لکیر)۔ متمم کے لیے زاویہ 90° سے نفی کریں؛ مکمل کے لیے 180° سے۔ صرف حادہ زاویوں کا متمم ہوتا ہے۔"),
    "points": [T("Complementary: 90°.", "متمم: 90°۔"),
               T("Supplementary: 180°.", "مکمل: 180°۔")]},
 ],
 "review_questions": [
   {"id": "r_comp", "type": "apply", "skill": SKILL, "step": number_question(
     "r_comp",
     T("What is the complement of 72°?", "72° کا متمم کیا ہے؟"),
     R1,
     T("90 − 72.", "90 − 72"),
     T("Right! 18°.", "درست! 18°"),
     T("90 − 72 = 18°.", "90 − 72 = 18°"),
     common_wrong=[wrong(108, "108° is the supplement. The complement: 90 − 72 = 18°.", "108° مکمل ہے۔ متمم: 90 − 72 = 18°", "complement_from_180")],
     qtype=None)},
   {"id": "r_supp", "type": "apply", "skill": SKILL, "step": number_question(
     "r_supp",
     T("What is the supplement of 45°?", "45° کا مکمل زاویہ کیا ہے؟"),
     R2,
     T("180 − 45.", "180 − 45"),
     T("Right! 135°.", "درست! 135°"),
     T("180 − 45 = 135°.", "180 − 45 = 135°"),
     common_wrong=[wrong(45, "45° is the complement. The supplement: 180 − 45 = 135°.", "45° متمم ہے۔ مکمل: 180 − 45 = 135°", "supplement_from_90")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Angles unit. No textbook text or exercises were used.",
   "\"C for Corner, S for Straight\" helps children keep 90° and 180° apart; most wrong answers in this lesson catch that mix-up.",
   "Urdu terms to check: متمم (complementary) and مکمل زاویے (supplementary). Some books use other words; please confirm the PCTB ones.",
   "The numbers were worked out in content/sources/g6-maths-09/angle_pairs.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
attach(lesson, FIGS)
write(lesson)
