import math

from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, AN_TYPES, CO_BISECTORS, CO_ANGLES)

SKILL = CO_ANGLES
BASIC = 60          # the angle the compass gives us directly (equilateral triangle)
RIGHT, LINE = 90, 180


def half(a):
    assert a % 2 == 0, a
    return a // 2


def between(a, b):
    """Bisecting the gap between two rays at a° and b° gives the ray halfway."""
    assert a < b and (a + b) % 2 == 0, (a, b)
    return (a + b) // 2


# ---- numbers -------------------------------------------------------------
# s2: a 120° angle is obtuse
S2 = 2 * BASIC
assert S2 == 120 and 90 < S2 < 180
# s4: half of 84°
S4 = half(84)
assert S4 == 42 and 2 * 84 == 168
# s5: the arc construction gives 60°
S5 = BASIC
assert S5 == 180 // 3          # each angle of an equilateral triangle
# s6: bisect 60°
S6 = half(BASIC)
assert S6 == 30 and 2 * BASIC == 120
# s7: bisecting 90° gives 45°
assert half(RIGHT) == 45 and half(BASIC) == 30 and half(2 * BASIC) == 60 and half(30) == 15
# s8: 60°, 120°, bisect between them → 90°, then bisect between 60° and 90° → 75°
NINETY = between(BASIC, 2 * BASIC)
assert NINETY == RIGHT
S8 = between(BASIC, NINETY)
assert S8 == 75 and (NINETY - BASIC) // 2 == 15 and BASIC + NINETY == 150
# s9: Bilal halves 90° and says 30°
assert half(RIGHT) == 45 and RIGHT // 3 == 30
# s11: ordering (no numbers)
# question bank: 105° between 90° and 120°; doubling 35°
QB = between(RIGHT, 2 * BASIC)
assert QB == 105 and (2 * BASIC - RIGHT) // 2 == 15 and RIGHT + 2 * BASIC == 210
# review: 150° between 120° and the straight line; copy 40° next to itself
R1 = between(2 * BASIC, LINE)
assert R1 == 150 and (LINE - 2 * BASIC) // 2 == 30
R2 = 40 + 40
assert R2 == 80 and half(40) == 20


# ---- figures -------------------------------------------------------------
def pt(x, y):
    return [round(x, 1), round(y, 1)]


def ray_end(v, deg, length):
    """End of a ray from v at deg° measured anticlockwise from +x (screen y goes down)."""
    r = math.radians(deg)
    return pt(v[0] + length * math.cos(r), v[1] - length * math.sin(r))


def arc(center, radius, a0, a1, dashed=False):
    """Arc from a0° to a1° (anticlockwise, maths style), turned into the app's clockwise screen terms."""
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


def figure(width, height, alt, items):
    for it in items:
        reach = it.get("radius", 0)
        for x, y in [*it.get("points", []), *(it[k] for k in ("from", "to", "center", "at") if k in it)]:
            assert reach <= x <= width - reach and reach <= y <= height - reach, (it, width, height)
    return {"width": width, "height": height, "alt": alt, "items": items}


def angle_marks(v, a0, a1, text, r=12, gap=10):
    mid = (a0 + a1) / 2
    return [arc(v, r, a0, a1), label(ray_end(v, mid, r + gap), text)]


def plain_angle(deg, text, alt, extra_rays=(), bisect=False):
    """Two arms with an angle mark. extra_rays: (deg, dashed, label) drawn from the vertex too."""
    wide = deg > 90 or any(d > 90 for d, _, _ in extra_rays)
    w, h = (130, 80) if wide else (110, 80)
    v = pt(65, 68) if wide else pt(22, 68)
    # short enough that a ray's label (7 past its end) stays well inside the box
    arm = 52
    items = [line(v, ray_end(v, 0, arm)), line(v, ray_end(v, deg, arm)), dot(v)]
    if bisect:
        items.append(line(v, ray_end(v, deg / 2, arm), dashed=True))
    for d, dashed, lab in extra_rays:
        items.append(line(v, ray_end(v, d, arm), dashed=dashed))
        if lab:
            items.append(label(ray_end(v, d, arm + 7), lab))
    if text and bisect:
        # keep the label off the dashed bisector
        items += [arc(v, 12, 0, deg), label(ray_end(v, deg * 0.75, 24), text)]
    elif text:
        items += angle_marks(v, 0, deg, text)
    return figure(w, h, alt, items)


def bisect_figure(deg, alt, text=None, r1=30, r2=24):
    """Compass bisection: arc from O cutting both arms at P and Q, equal arcs
    from P and Q crossing at R, dashed bisector OR."""
    assert r2 > r1 * math.sin(math.radians(deg / 2)), "the two arcs must cross"
    w, h = 125, 102
    o = pt(32, 70)
    p, q = ray_end(o, 0, r1), ray_end(o, deg, r1)
    gap = r1 * math.sin(math.radians(deg / 2))
    dist_r = r1 * math.cos(math.radians(deg / 2)) + math.sqrt(r2 ** 2 - gap ** 2)
    r = ray_end(o, deg / 2, dist_r)
    assert abs(math.dist(p, r) - r2) < 0.3 and abs(math.dist(q, r) - r2) < 0.3

    def toward(a, b):
        return math.degrees(math.atan2(-(b[1] - a[1]), b[0] - a[0]))

    tp, tq = toward(p, r), toward(q, r)
    items = [
        line(o, ray_end(o, 0, 85)), line(o, ray_end(o, deg, 62)), dot(o),
        arc(o, r1, -6, deg + 6, dashed=True),
        dot(p), dot(q),
        arc(p, r2, tp - 18, tp + 18, dashed=True),
        arc(q, r2, tq - 18, tq + 18, dashed=True),
        dot(r),
        line(o, ray_end(o, deg / 2, dist_r + 18), dashed=True),
        label(pt(o[0] - 7, o[1] + 6), "O"),
        label(pt(p[0] + 2, p[1] + 8), "P"),
        label(ray_end(q, deg + 90, 7), "Q"),
        label(ray_end(r, deg / 2 - 90, 7), "R"),
    ]
    if text:
        items.append(arc(o, 11, 0, deg))
        items.append(label(ray_end(o, deg / 4, 21), text))
    return figure(w, h, alt, items)


def sixty_figure(alt, triangle=False):
    """60° from an equilateral triangle: arc from O cuts OA at P, the same arc
    from P cuts the first arc at Q, OQ makes 60° with OA."""
    w, h, rad = 140, 100, 40
    o = pt(42, 60)
    p = ray_end(o, 0, rad)
    q = ray_end(o, 60, rad)
    assert abs(math.dist(p, q) - rad) < 0.2
    items = [
        line(o, ray_end(o, 0, 90)), dot(o),
        arc(o, rad, -6, 75, dashed=True),
        dot(p),
        arc(p, rad, 105, 135, dashed=True),
        dot(q),
        line(o, ray_end(o, 60, 56)),
        label(pt(o[0] - 7, o[1] + 6), "O"),
        label(pt(p[0] + 3, p[1] + 8), "P"),
        label(pt(q[0] - 7, q[1] - 4), "Q"),
        label(ray_end(o, 0, 92), "A"),
    ]
    items += angle_marks(o, 0, 60, "60°", r=12, gap=10)
    if triangle:
        items.append({"kind": "polygon", "points": [o, p, q], "style": "dashed"})
    return figure(w, h, alt, items)


FAN = plain_angle(
    120, "120°",
    T("A base arm going right from a point O. From O, a ray at 60° to the base, a dashed ray straight up at 90°, and a ray at 120°. Labels 60°, 90° and 120° sit at the ends of the rays.",
      "نقطہ O سے دائیں طرف ایک بنیادی بازو۔ O سے بنیاد کے ساتھ 60° پر ایک شعاع، 90° پر سیدھی اوپر ایک ڈیش والی شعاع، اور 120° پر ایک شعاع۔ شعاعوں کے سروں پر 60°، 90° اور 120° لکھا ہے۔"),
    extra_rays=[(60, False, "60°"), (90, True, "90°")])
# the 120° mark label would clash with the ray labels; keep only the arc and the end labels
FAN["items"] = [it for it in FAN["items"] if not (it["kind"] == "label" and it["text"] == "120°" and it["at"][1] > 40)]
FAN["items"].append(label(ray_end([65, 68], 120, 62), "120°"))
assert sum(1 for it in FAN["items"] if it["kind"] == "label" and it["text"] == "120°") == 1


lesson = {
 "id": "g6-maths-19-constructing-angles",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Bisect a given angle with a compass, and construct angles of 60°, 30°, 120°, 90°, 45°, 75°, 105° and 150° with a ruler and compass.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Bisecting and constructing angles", "زاویوں کی تنصیف اور زاویے بنانا"),
 "estimated_minutes": 15,
 "prerequisites": [{"skill": CO_BISECTORS}, {"skill": AN_TYPES}],
 "misconceptions": [
   {"id": "half_right_is_30", "description": "Thinks bisecting a right angle (90°) gives 30° instead of 45°."},
   {"id": "changes_width", "description": "Changes the compass width between the two equal arcs, so the crossing point is off the bisector."},
   {"id": "doubles_not_halves", "description": "Adds or doubles instead of halving: says bisecting 60° gives 120°."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_basic", "type": "recall", "step": {
     "id": "qb_basic", "type": "choice",
     "prompt": T("With only a ruler and compass, which angle do we make first, using arcs of the same width that form an equilateral triangle?",
                 "صرف رولر اور پرکار سے، ہم سب سے پہلے کون سا زاویہ بناتے ہیں، ایک ہی چوڑائی کی قوسوں سے جو مساوی الاضلاع مثلث بناتی ہیں؟"),
     "options": [
       opt("sixty", "60°", "60°", True, "Yes! 60° is the basic angle. The others come from it.", "جی ہاں! 60° بنیادی زاویہ ہے۔ باقی اسی سے بنتے ہیں۔"),
       opt("ninety", "90°", "90°", False, "90° comes later, by bisecting between 60° and 120°. The first one is 60°.", "90° بعد میں آتا ہے، 60° اور 120° کے درمیان تنصیف سے۔ پہلا 60° ہے۔"),
       opt("fortyfive", "45°", "45°", False, "45° is half of 90°, so it needs 90° first. We start with 60°.", "45° تو 90° کا آدھا ہے، پہلے 90° چاہیے۔ ہم 60° سے شروع کرتے ہیں۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("Sana makes 90° and 120° on the same base arm, then bisects the gap between those two rays. What angle does the new ray make with the base?",
       "ثنا ایک ہی بنیادی بازو پر 90° اور 120° بناتی ہے، پھر ان دونوں شعاعوں کے درمیان فاصلے کی تنصیف کرتی ہے۔ نئی شعاع بنیاد کے ساتھ کتنا زاویہ بناتی ہے؟"),
     QB,
     T("Halfway between 90 and 120.", "90 اور 120 کا درمیان۔"),
     T("Right! 105°.", "درست! 105°"),
     T("The gap is 30°, half is 15°, and 90 + 15 = 105°.", "فاصلہ 30° ہے، آدھا 15° ہے، اور 90 + 15 = 105°"),
     common_wrong=[wrong(15, "15° is only half the gap. Add it to 90°: 105°.", "15° صرف فاصلے کا آدھا ہے۔ اسے 90° میں جمع کریں: 105°"),
                   wrong(210, "That added 90 and 120. Bisecting goes halfway between them: 105°.", "اس میں 90 اور 120 جمع کیے۔ تنصیف دونوں کے بیچ میں جاتی ہے: 105°", "doubles_not_halves")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Hamza bisects an angle. He draws the arc from P with his compass open 4 cm, then opens it to 6 cm for the arc from Q. His line misses the middle. What went wrong?",
                 "حمزہ ایک زاویے کی تنصیف کرتا ہے۔ وہ P سے قوس پرکار 4 سینٹی میٹر کھول کر لگاتا ہے، پھر Q سے قوس کے لیے 6 سینٹی میٹر کھول لیتا ہے۔ اس کی لکیر درمیان سے ہٹ جاتی ہے۔ کیا غلطی ہوئی؟"),
     "figure": bisect_figure(
       70, T("An angle at O with arms through P and Q. A dashed arc from O cuts both arms. Two dashed arcs from P and Q cross at R, and a dashed line from O through R splits the angle.",
             "O پر ایک زاویہ جس کے بازو P اور Q سے گزرتے ہیں۔ O سے ایک ڈیش والی قوس دونوں بازوؤں کو کاٹتی ہے۔ P اور Q سے دو ڈیش والی قوسیں R پر ملتی ہیں، اور O سے R تک ڈیش والی لکیر زاویے کو تقسیم کرتی ہے۔")),
     "options": [
       opt("width", "The arcs from P and Q must use the same compass width.", "P اور Q سے قوسیں ایک ہی پرکار چوڑائی سے لگنی چاہییں۔", True,
           "Yes! Equal arcs put the crossing exactly in the middle.", "جی ہاں! برابر قوسیں ملاپ کو بالکل درمیان میں لاتی ہیں۔"),
       opt("first_arc", "The first arc from O should be bigger.", "O سے پہلی قوس بڑی ہونی چاہیے۔", False,
           "The first arc can be any size. The problem is the two different widths, 4 cm and 6 cm.", "پہلی قوس کسی بھی سائز کی ہو سکتی ہے۔ مسئلہ دو مختلف چوڑائیاں ہیں، 4 اور 6 سینٹی میٹر۔", "changes_width"),
       opt("nothing", "Nothing; any widths work.", "کوئی غلطی نہیں؛ کوئی بھی چوڑائی چلتی ہے۔", False,
           "With different widths the crossing slides towards one arm. Keep the width the same.", "مختلف چوڑائی سے ملاپ ایک بازو کی طرف کھسک جاتا ہے۔ چوڑائی ایک جیسی رکھیں۔", "changes_width"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_bisect", "front": T("How do you bisect an angle with a compass?", "پرکار سے زاویے کی تنصیف کیسے کرتے ہیں؟"),
    "back": T("Arc from the vertex cutting both arms; equal arcs from those two points; join the vertex to where they cross.",
              "راس سے قوس جو دونوں بازو کاٹے؛ ان دو نقطوں سے برابر قوسیں؛ راس کو ان کے ملاپ سے ملائیں۔")},
   {"id": "f_family", "front": T("How do you get 30°, 90° and 45° from 60°?", "60° سے 30°، 90° اور 45° کیسے بنتے ہیں؟"),
    "back": T("Bisect 60° for 30°. Bisect between 60° and 120° for 90°. Bisect 90° for 45°.",
              "60° کی تنصیف سے 30°۔ 60° اور 120° کے درمیان تنصیف سے 90°۔ 90° کی تنصیف سے 45°۔")},
 ],
 "home_tasks": [{"id": "h_construct", "text": T(
   "On paper, use a ruler and compass to construct 60°, then 90°, then 45°. Measure each with a protractor. If you have no protractor, fold a paper corner neatly in half twice to make a right angle and check your 90° against it, then fold that corner once more to check 45°.",
   "کاغذ پر رولر اور پرکار سے پہلے 60°، پھر 90°، پھر 45° بنائیں۔ ہر ایک کو چاند (پروٹریکٹر) سے ناپیں۔ اگر چاند نہیں ہے تو کاغذ کو دو بار احتیاط سے تہہ کر کے قائمہ زاویہ بنائیں اور اپنے 90° کو اس سے جانچیں، پھر اس کونے کو ایک بار اور تہہ کر کے 45° جانچیں۔")}],
 "glossary": [T("Bisect", "تنصیف کرنا"), T("Angle bisector", "ناصف زاویہ"), T("Compass", "پرکار"), T("Arc", "قوس"),
              T("Vertex", "راس"), T("Arm", "بازو"), T("Equilateral triangle", "مساوی الاضلاع مثلث")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Ali's kite frame needs a stick exactly in the middle of an angle. No protractor! Can a compass find the middle?",
                     "علی کی پتنگ کے ڈھانچے میں زاویے کے بالکل درمیان ایک تیلی لگانی ہے۔ چاند نہیں ہے! کیا پرکار درمیان ڈھونڈ سکتا ہے؟"),
    "text": T("Today we split angles exactly in half and build angles like 60°, 90° and 45° with only a ruler and a compass. First, a quick check.",
              "آج ہم زاویوں کو بالکل آدھا کریں گے اور صرف رولر اور پرکار سے 60°، 90° اور 45° جیسے زاویے بنائیں گے۔ پہلے ایک چھوٹا سا سوال۔")},
   {"id": "s2_foundation", "type": "choice", "question_type": "recall", "skill": AN_TYPES,
    "prompt": T("What kind of angle is this 120° angle?", "یہ 120° کا زاویہ کس قسم کا ہے؟"),
    "figure": plain_angle(
      S2, "120°",
      T("Two arms meet at a point. One arm goes right; the other goes up and to the left. The angle between them is marked 120°.",
        "دو بازو ایک نقطے پر ملتے ہیں۔ ایک بازو دائیں جاتا ہے؛ دوسرا اوپر بائیں طرف۔ ان کے درمیان زاویے پر 120° لکھا ہے۔")),
    "options": [
      opt("obtuse", "Obtuse", "منفرجہ", True, "Yes! 120° is between 90° and 180°.", "جی ہاں! 120°، 90° اور 180° کے درمیان ہے۔"),
      opt("acute", "Acute", "حادہ", False, "Acute angles are less than 90°. 120° is bigger, so it is obtuse.", "حادہ زاویہ 90° سے کم ہوتا ہے۔ 120° بڑا ہے، اس لیے منفرجہ ہے۔"),
      opt("right", "Right", "قائمہ", False, "A right angle is exactly 90°. 120° is more, so it is obtuse.", "قائمہ زاویہ بالکل 90° ہوتا ہے۔ 120° زیادہ ہے، اس لیے منفرجہ ہے۔"),
    ]},
   {"id": "s3_bisect", "type": "explain",
    "character": say("happy", "Keep the compass width the same for the two middle arcs. That is the whole trick!",
                     "درمیان والی دونوں قوسوں کے لیے پرکار کی چوڑائی ایک جیسی رکھیں۔ یہی سارا راز ہے!"),
    "figure": bisect_figure(
      70, T("An angle at vertex O. A dashed arc drawn from O cuts one arm at P and the other at Q. Two dashed arcs of the same width, one from P and one from Q, cross at R. A dashed line from O through R splits the angle into two equal parts.",
            "راس O پر ایک زاویہ۔ O سے لگائی گئی ڈیش والی قوس ایک بازو کو P پر اور دوسرے کو Q پر کاٹتی ہے۔ ایک ہی چوڑائی کی دو ڈیش والی قوسیں، ایک P سے اور ایک Q سے، R پر ملتی ہیں۔ O سے R تک ڈیش والی لکیر زاویے کو دو برابر حصوں میں بانٹتی ہے۔")),
    "text": T("To bisect an angle means to split it into two equal angles. 1) Put the compass point on the vertex O and draw an arc that cuts both arms, at P and Q. 2) From P, draw an arc inside the angle. Without changing the width, draw an arc from Q that crosses it at R. 3) Join O to R. OR is the angle bisector: each half is exactly half the angle. Using the same idea we can also copy an angle onto another line, or put a copy next to it to double it.",
              "زاویے کی تنصیف کا مطلب ہے اسے دو برابر زاویوں میں بانٹنا۔ 1) پرکار کی نوک راس O پر رکھیں اور ایسی قوس لگائیں جو دونوں بازوؤں کو P اور Q پر کاٹے۔ 2) P سے زاویے کے اندر ایک قوس لگائیں۔ چوڑائی بدلے بغیر Q سے قوس لگائیں جو اسے R پر کاٹے۔ 3) O کو R سے ملائیں۔ OR ناصف زاویہ ہے: ہر حصہ زاویے کا بالکل آدھا ہے۔ اسی طریقے سے ہم کسی زاویے کی نقل دوسری لکیر پر بنا سکتے ہیں، یا ساتھ میں نقل لگا کر اسے دگنا کر سکتے ہیں۔")},
   {**number_question(
     "s4_half",
     T("Ali's kite frame has an angle of 84° at the top. He bisects it to fix the middle stick. How big is each half, in degrees?",
       "علی کی پتنگ کے ڈھانچے کے اوپر 84° کا زاویہ ہے۔ وہ درمیان والی تیلی لگانے کے لیے اس کی تنصیف کرتا ہے۔ ہر آدھا حصہ کتنے درجے کا ہے؟"),
     S4,
     T("Bisect means split into two equal parts: 84 ÷ 2.", "تنصیف کا مطلب دو برابر حصے: 84 ÷ 2"),
     T("Right! 42°. Check: 42 + 42 = 84.", "درست! 42°۔ جانچ: 42 + 42 = 84"),
     T("84 ÷ 2 = 42°.", "84 ÷ 2 = 42°"),
     common_wrong=[wrong(168, "168° is double. Bisecting halves the angle: 84 ÷ 2 = 42°.", "168° تو دگنا ہے۔ تنصیف زاویے کو آدھا کرتی ہے: 84 ÷ 2 = 42°", "doubles_not_halves")]),
    "figure": plain_angle(
      84, "84°",
      T("An angle of 84° at the top of a kite frame, drawn as two arms from a point, with a dashed line from the point splitting it into two equal parts.",
        "پتنگ کے ڈھانچے کے اوپر 84° کا زاویہ، ایک نقطے سے دو بازو، اور نقطے سے ایک ڈیش والی لکیر جو اسے دو برابر حصوں میں بانٹتی ہے۔"),
      bisect=True)},
   {**number_question(
     "s5_sixty",
     T("Draw a line OA. With the compass point on O, draw an arc cutting OA at P. Keep the same width, put the point on P and draw an arc cutting the first arc at Q. O, P and Q make an equilateral triangle. How many degrees is angle AOQ?",
       "ایک لکیر OA بنائیں۔ پرکار کی نوک O پر رکھ کر قوس لگائیں جو OA کو P پر کاٹے۔ وہی چوڑائی رکھیں، نوک P پر رکھیں اور قوس لگائیں جو پہلی قوس کو Q پر کاٹے۔ O، P اور Q مساوی الاضلاع مثلث بناتے ہیں۔ زاویہ AOQ کتنے درجے کا ہے؟"),
     S5,
     T("All three sides are one compass width, so all three angles are equal. They share 180°.", "تینوں اضلاع ایک پرکار چوڑائی کے ہیں، اس لیے تینوں زاویے برابر ہیں۔ وہ 180° بانٹتے ہیں۔"),
     T("Right! 60°: 180 ÷ 3. This is our basic angle.", "درست! 60°: 180 ÷ 3۔ یہ ہمارا بنیادی زاویہ ہے۔"),
     T("An equilateral triangle has three equal angles: 180 ÷ 3 = 60°.", "مساوی الاضلاع مثلث کے تین برابر زاویے ہیں: 180 ÷ 3 = 60°"),
     common_wrong=[wrong(90, "It is not a right angle. The triangle's three equal angles make 180°: each is 60°.", "یہ قائمہ زاویہ نہیں۔ مثلث کے تین برابر زاویے 180° بناتے ہیں: ہر ایک 60°۔"),
                   wrong(45, "45° needs a 90° first. Here each angle of the equilateral triangle is 180 ÷ 3 = 60°.", "45° کے لیے پہلے 90° چاہیے۔ یہاں مساوی الاضلاع مثلث کا ہر زاویہ 180 ÷ 3 = 60° ہے۔")]),
    "figure": sixty_figure(
      T("A line from O to A. A dashed arc from O cuts it at P. A dashed arc of the same width from P cuts the first arc at Q. The ray OQ is drawn, and the angle between OA and OQ is marked 60°.",
        "O سے A تک ایک لکیر۔ O سے ڈیش والی قوس اسے P پر کاٹتی ہے۔ P سے اسی چوڑائی کی ڈیش والی قوس پہلی قوس کو Q پر کاٹتی ہے۔ شعاع OQ بنی ہے، اور OA اور OQ کے درمیان زاویے پر 60° لکھا ہے۔"))},
   {**number_question(
     "s6_thirty",
     T("Zainab makes a 60° angle with her compass, then bisects it. What angle does each half make?",
       "زینب پرکار سے 60° کا زاویہ بناتی ہے، پھر اس کی تنصیف کرتی ہے۔ ہر آدھا حصہ کتنا زاویہ بناتا ہے؟"),
     S6,
     T("Half of 60.", "60 کا آدھا"),
     T("Right! 30°.", "درست! 30°"),
     T("60 ÷ 2 = 30°.", "60 ÷ 2 = 30°"),
     common_wrong=[wrong(120, "120° is two 60° steps. Bisecting halves: 60 ÷ 2 = 30°.", "120° تو 60° کے دو قدم ہیں۔ تنصیف آدھا کرتی ہے: 60 ÷ 2 = 30°", "doubles_not_halves")]),
    "figure": plain_angle(
      60, "60°",
      T("An angle of 60° made of two arms from a point, with a dashed line from the point splitting it into two equal parts.",
        "دو بازوؤں سے بنا 60° کا زاویہ، اور نقطے سے ایک ڈیش والی لکیر جو اسے دو برابر حصوں میں بانٹتی ہے۔"),
      bisect=True)},
   {"id": "s7_which", "type": "choice", "question_type": "apply",
    "prompt": T("On one base arm we have made rays at 60°, 90° and 120°. Which bisection gives 45°?",
                "ایک بنیادی بازو پر ہم نے 60°، 90° اور 120° پر شعاعیں بنائی ہیں۔ کون سی تنصیف سے 45° ملتا ہے؟"),
    "figure": FAN,
    "options": [
      opt("ninety", "Bisect the 90° angle", "90° کے زاویے کی تنصیف", True,
          "Yes! 90 ÷ 2 = 45°.", "جی ہاں! 90 ÷ 2 = 45°"),
      opt("sixty", "Bisect the 60° angle", "60° کے زاویے کی تنصیف", False,
          "Half of 60° is 30°. For 45° bisect 90°.", "60° کا آدھا 30° ہے۔ 45° کے لیے 90° کی تنصیف کریں۔"),
      opt("onetwenty", "Bisect the 120° angle", "120° کے زاویے کی تنصیف", False,
          "Half of 120° is 60°. For 45° bisect 90°.", "120° کا آدھا 60° ہے۔ 45° کے لیے 90° کی تنصیف کریں۔"),
      opt("between", "Bisect between 60° and 120°", "60° اور 120° کے درمیان تنصیف", False,
          "That gives 90°. Bisect that 90° to get 45°.", "اس سے 90° ملتا ہے۔ 45° کے لیے اس 90° کی تنصیف کریں۔"),
    ]},
   {**number_question(
     "s8_steps",
     T("Kashif builds an angle in steps on one base arm: make 60°, make another 60° to reach 120°, bisect between 60° and 120°, then bisect between 60° and that new ray. What angle does the last ray make with the base arm?",
       "کاشف ایک بنیادی بازو پر قدم بہ قدم زاویہ بناتا ہے: 60° بنائیں، ایک اور 60° بنا کر 120° تک پہنچیں، 60° اور 120° کے درمیان تنصیف کریں، پھر 60° اور اس نئی شعاع کے درمیان تنصیف کریں۔ آخری شعاع بنیادی بازو کے ساتھ کتنا زاویہ بناتی ہے؟"),
     S8,
     T("Between 60° and 120° is 90°. Then go halfway between 60° and 90°.", "60° اور 120° کا درمیان 90° ہے۔ پھر 60° اور 90° کے بیچ میں جائیں۔"),
     T("Right! 75°. The gap 60° to 90° is 30°, half is 15°, and 60 + 15 = 75.", "درست! 75°۔ 60° سے 90° تک فاصلہ 30° ہے، آدھا 15° ہے، اور 60 + 15 = 75"),
     T("First ray: 90°. Halfway between 60° and 90°: 60 + 15 = 75°.", "پہلی نئی شعاع: 90°۔ 60° اور 90° کا درمیان: 60 + 15 = 75°"),
     common_wrong=[wrong(15, "15° is half the gap between 60° and 90°. Measure from the base: 60 + 15 = 75°.", "15° تو 60° اور 90° کے فاصلے کا آدھا ہے۔ بنیاد سے ناپیں: 60 + 15 = 75°"),
                   wrong(150, "That added 60 and 90. Bisecting goes halfway between them: 75°.", "اس میں 60 اور 90 جمع کیے۔ تنصیف دونوں کے بیچ میں جاتی ہے: 75°", "doubles_not_halves")]),
    "figure": plain_angle(
      60, None,
      T("A base arm going right from a point. A ray at 60° labelled 60°, a ray straight up labelled 90°, and a dashed ray halfway between them labelled with a question mark.",
        "ایک نقطے سے دائیں طرف بنیادی بازو۔ 60° پر ایک شعاع جس پر 60° لکھا ہے، سیدھی اوپر ایک شعاع جس پر 90° لکھا ہے، اور ان کے بیچ میں ایک ڈیش والی شعاع جس پر سوالیہ نشان ہے۔"),
      extra_rays=[(60, False, "60°"), (90, False, "90°"), (75, True, "?")])},
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Bilal constructs a right angle and bisects it. He says each half is 30°. What went wrong?",
                "بلال قائمہ زاویہ بناتا ہے اور اس کی تنصیف کرتا ہے۔ وہ کہتا ہے ہر آدھا 30° ہے۔ کیا غلطی ہوئی؟"),
    "figure": plain_angle(
      RIGHT, "90°",
      T("A right angle marked 90°, with a dashed line from the corner splitting it into two equal parts.",
        "ایک قائمہ زاویہ جس پر 90° لکھا ہے، اور کونے سے ایک ڈیش والی لکیر جو اسے دو برابر حصوں میں بانٹتی ہے۔"),
      bisect=True),
    "options": [
      opt("half", "Bisecting splits it into two: 90 ÷ 2 = 45°.", "تنصیف دو حصے کرتی ہے: 90 ÷ 2 = 45°", True,
          "Yes! Bisect means two equal parts, so 45° each.", "جی ہاں! تنصیف یعنی دو برابر حصے، تو ہر ایک 45°۔"),
      opt("third", "Nothing; 90 ÷ 3 = 30°.", "کوئی غلطی نہیں؛ 90 ÷ 3 = 30°", False,
          "Dividing by 3 makes three parts. Bisecting makes two: 45°.", "3 سے تقسیم تین حصے بناتی ہے۔ تنصیف دو بناتی ہے: 45°", "half_right_is_30"),
      opt("double", "Each half should be 180°.", "ہر آدھا 180° ہونا چاہیے۔", False,
          "180° doubles the angle. Half of 90° is 45°.", "180° تو زاویے کو دگنا کرتا ہے۔ 90° کا آدھا 45° ہے۔", "doubles_not_halves"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Two arcs of the same width always give exactly 60°. Why does that work? Can you teach me?",
                     "ایک ہی چوڑائی کی دو قوسیں ہمیشہ بالکل 60° دیتی ہیں۔ ایسا کیوں ہوتا ہے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "figure": sixty_figure(
      T("A line from O to A. A dashed arc from O cuts it at P. A dashed arc of the same width from P cuts the first arc at Q. The ray OQ makes a 60° angle with OA, and a dashed triangle joins O, P and Q.",
        "O سے A تک ایک لکیر۔ O سے ڈیش والی قوس اسے P پر کاٹتی ہے۔ P سے اسی چوڑائی کی ڈیش والی قوس پہلی قوس کو Q پر کاٹتی ہے۔ شعاع OQ، OA کے ساتھ 60° کا زاویہ بناتی ہے، اور ڈیش والی مثلث O، P اور Q کو ملاتی ہے۔"),
      triangle=True),
    "task": T("In your own words: why does this compass construction make an angle of exactly 60°?",
              "اپنے الفاظ میں بتائیں: پرکار کی یہ بناوٹ بالکل 60° کا زاویہ کیوں بناتی ہے؟"),
    "key_idea": "OP, OQ and PQ are all one compass width, so triangle OPQ is equilateral. Its three angles are equal and add up to 180°, so each is 60°.",
    "levels": {
      "got_it": "Says the three sides are equal (same compass width) so the triangle is equilateral, and its equal angles share 180° to make 60° each.",
      "partly": "Says the triangle is equilateral or the sides are equal, but not why that makes 60° (or the reverse).",
      "not_yet": "Gives no reason, or only repeats the steps."},
    "keywords": [
      ["equal", "same width", "equilateral", "برابر", "مساوی", "barabar"],
      ["triangle", "مثلث", "musallas"],
      ["180", "three", "تین", "teen"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Equal sides make equal angles, and 180 ÷ 3 = 60°.", "بہت خوب! برابر اضلاع برابر زاویے بناتے ہیں، اور 180 ÷ 3 = 60°۔"),
      "partly": T("Good start! Now say how the three equal angles share the triangle's 180°.", "اچھی شروعات! اب بتائیں تین برابر زاویے مثلث کے 180° کیسے بانٹتے ہیں۔"),
      "not_yet": T("Look at OP, OQ and PQ: all drawn with one compass width. What kind of triangle is that?", "OP، OQ اور PQ دیکھیں: سب ایک پرکار چوڑائی سے بنے ہیں۔ یہ کون سی مثلث ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   {"id": "s11_order", "type": "choice", "question_type": "apply",
    "prompt": T("Hira wants to bisect an angle. Her steps are mixed up: X) join the vertex to where the arcs cross; Y) draw an arc from the vertex cutting both arms; Z) from the two cut points, draw equal arcs that cross. What is the right order?",
                "حرا ایک زاویے کی تنصیف کرنا چاہتی ہے۔ اس کے قدم الٹ پلٹ ہو گئے ہیں: X) راس کو قوسوں کے ملاپ سے ملائیں؛ Y) راس سے قوس لگائیں جو دونوں بازو کاٹے؛ Z) کٹے ہوئے دو نقطوں سے برابر قوسیں لگائیں جو ایک دوسرے کو کاٹیں۔ صحیح ترتیب کیا ہے؟"),
    "figure": bisect_figure(
      50, T("An angle at O. A dashed arc from O cuts the arms at P and Q. Equal dashed arcs from P and Q cross at R, and a dashed line joins O to R.",
            "O پر ایک زاویہ۔ O سے ڈیش والی قوس بازوؤں کو P اور Q پر کاٹتی ہے۔ P اور Q سے برابر ڈیش والی قوسیں R پر ملتی ہیں، اور ڈیش والی لکیر O کو R سے ملاتی ہے۔")),
    "options": [
      opt("yzx", "Y, Z, X", "Y، Z، X", True,
          "Yes! Arc from the vertex, equal arcs, then join.", "جی ہاں! راس سے قوس، برابر قوسیں، پھر ملائیں۔"),
      opt("zyx", "Z, Y, X", "Z، Y، X", False,
          "The cut points come from the first arc, so Y comes first: Y, Z, X.", "کٹے ہوئے نقطے پہلی قوس سے بنتے ہیں، اس لیے Y پہلے: Y، Z، X"),
      opt("xyz", "X, Y, Z", "X، Y، Z", False,
          "You can't join to the crossing before the arcs exist. Y, Z, X.", "قوسیں بننے سے پہلے ملاپ سے نہیں ملا سکتے۔ Y، Z، X"),
    ]},
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "One basic angle, 60°, and bisecting gives a whole family of angles. Shabash!",
                     "ایک بنیادی زاویہ، 60°، اور تنصیف سے زاویوں کا پورا خاندان بن جاتا ہے۔ شاباش!"),
    "figure": FAN,
    "text": T("To bisect an angle: arc from the vertex cutting both arms, equal arcs from those two points, then join the vertex to the crossing. The basic angle is 60°, from an equilateral triangle of arcs. From it: 30° (bisect 60°), 120° (two 60° steps), 90° (bisect between 60° and 120°), 45° (bisect 90°), 75° (between 60° and 90°), 105° (between 90° and 120°) and 150° (between 120° and the straight line). Copy an angle next to itself to double it.",
              "زاویے کی تنصیف: راس سے قوس جو دونوں بازو کاٹے، ان دو نقطوں سے برابر قوسیں، پھر راس کو ملاپ سے ملائیں۔ بنیادی زاویہ 60° ہے، قوسوں کی مساوی الاضلاع مثلث سے۔ اس سے: 30° (60° کی تنصیف)، 120° (60° کے دو قدم)، 90° (60° اور 120° کے درمیان تنصیف)، 45° (90° کی تنصیف)، 75° (60° اور 90° کے درمیان)، 105° (90° اور 120° کے درمیان) اور 150° (120° اور سیدھی لکیر کے درمیان)۔ کسی زاویے کو دگنا کرنے کے لیے اس کی نقل ساتھ لگائیں۔"),
    "points": [T("Bisecting halves an angle; keep the compass width the same.", "تنصیف زاویے کو آدھا کرتی ہے؛ پرکار کی چوڑائی ایک جیسی رکھیں۔"),
               T("60° is the basic angle; the rest come from it.", "60° بنیادی زاویہ ہے؛ باقی اسی سے بنتے ہیں۔")]},
 ],
 "review_questions": [
   {"id": "r_150", "type": "apply", "skill": SKILL, "step": number_question(
     "r_150",
     T("Make 120° on a straight line, then bisect between the 120° ray and the rest of the straight line (180°). What angle does the new ray make with the base?",
       "ایک سیدھی لکیر پر 120° بنائیں، پھر 120° والی شعاع اور سیدھی لکیر کے باقی حصے (180°) کے درمیان تنصیف کریں۔ نئی شعاع بنیاد کے ساتھ کتنا زاویہ بناتی ہے؟"),
     R1,
     T("Halfway between 120 and 180.", "120 اور 180 کا درمیان۔"),
     T("Right! 150°.", "درست! 150°"),
     T("The gap is 60°, half is 30°, and 120 + 30 = 150°.", "فاصلہ 60° ہے، آدھا 30° ہے، اور 120 + 30 = 150°"),
     common_wrong=[wrong(30, "30° is only half the gap. Add it to 120°: 150°.", "30° صرف فاصلے کا آدھا ہے۔ اسے 120° میں جمع کریں: 150°")],
     qtype=None)},
   {"id": "r_double", "type": "apply", "skill": SKILL, "step": number_question(
     "r_double",
     T("Nida copies a 40° angle with her compass and places the copy right next to it, sharing one arm. How big is the whole angle now?",
       "ندا پرکار سے 40° کے زاویے کی نقل بناتی ہے اور نقل کو ایک بازو مشترک رکھ کر بالکل ساتھ لگا دیتی ہے۔ اب پورا زاویہ کتنا ہے؟"),
     R2,
     T("Two 40° angles side by side.", "دو 40° کے زاویے ساتھ ساتھ۔"),
     T("Right! 80°: copying next to itself doubles the angle.", "درست! 80°: ساتھ نقل لگانے سے زاویہ دگنا ہو جاتا ہے۔"),
     T("40 + 40 = 80°.", "40 + 40 = 80°"),
     common_wrong=[wrong(20, "That halved it. A copy placed alongside doubles it: 80°.", "یہ تو آدھا ہو گیا۔ ساتھ لگی نقل دگنا کرتی ہے: 80°")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Geometrical Constructions unit. No textbook text or exercises were used.",
   "Every angle here comes from one basic angle, 60°, made from an equilateral triangle of equal compass arcs, plus bisection. Ask students to say which two rays they bisect between: 90° is between 60° and 120°, 75° between 60° and 90°, 105° between 90° and 120°, 150° between 120° and 180°.",
   "The most common construction slip is changing the compass width between the two equal arcs; the second is calling half of 90° '30°'. Watch real constructions on paper and check them with a protractor or a folded paper corner.",
   "Copying an angle: draw an arc across the given angle and the same arc from the new vertex; set the compass to the chord between the two cut points and transfer it. Placing the copy next to the original doubles the angle.",
   "Urdu terms to check: تنصیف (bisect), ناصف زاویہ (angle bisector), پرکار (compass), قوس (arc), راس (vertex), بازو (arm), چاند/پروٹریکٹر (protractor), مساوی الاضلاع مثلث (equilateral triangle).",
   "The numbers and figure coordinates were worked out in content/sources/g6-maths-19/constructing_angles.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)
