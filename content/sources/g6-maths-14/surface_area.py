from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, AREA_RECTANGLE, SO_VOLUME_CUBE, SO_SURFACE_AREA,
                    cuboid_volume, cuboid_surface)

SKILL = SO_SURFACE_AREA


def cube_surface(s):
    return cuboid_surface(s, s, s)


# s2: rectangle 6 x 4
S2 = 6 * 4
assert S2 == 24
# s4: cube of side 3 (one face 9, volume 27)
S4 = cube_surface(3)
assert S4 == 54 and 3 * 3 == 9 and cuboid_volume(3, 3, 3) == 27
# s5: cuboid 5 x 3 x 2 (three faces 15 + 6 + 10 = 31, volume 30)
S5 = cuboid_surface(5, 3, 2)
assert S5 == 62 and 5 * 3 + 3 * 2 + 5 * 2 == 31 and cuboid_volume(5, 3, 2) == 30
# s7: box 10 x 6 x 4 (half 124, volume 240)
S7 = cuboid_surface(10, 6, 4)
assert S7 == 248 and 10 * 6 + 6 * 4 + 10 * 4 == 124 and cuboid_volume(10, 6, 4) == 240
# s8: cube of side 5 (volume 125, one face 25)
S8 = cube_surface(5)
assert S8 == 150 and cuboid_volume(5, 5, 5) == 125
# s9: cuboid 4 x 3 x 2: 12 + 6 + 8 = 26 is only half
assert cuboid_surface(4, 3, 2) == 52 and 4 * 3 + 3 * 2 + 4 * 2 == 26
# s11: gift box, cube of side 10 cm
S11 = cube_surface(10)
assert S11 == 600 and cuboid_volume(10, 10, 10) == 1000
# question bank and review
QB = cuboid_surface(6, 4, 3)
assert QB == 108 and 6 * 4 + 4 * 3 + 6 * 3 == 54 and cuboid_volume(6, 4, 3) == 72
assert cube_surface(2) == 24 and cuboid_volume(2, 2, 2) == 8
R1 = cube_surface(4)
assert R1 == 96 and cuboid_volume(4, 4, 4) == 64
R2 = cuboid_surface(8, 5, 2)
assert R2 == 132 and 8 * 5 + 5 * 2 + 8 * 2 == 66 and cuboid_volume(8, 5, 2) == 80

# ---------- figures ----------
from figs import (figure, box_items, box_fig, cube_fig, cube_alt, net_items, label, line, circle, cm, with_figures, TALL)


def gift_fig(side, labels):
    """A cube gift box with a ribbon round it and a bow on top."""
    items, b = box_items(side, side, side, labels=labels, max_w=170, max_h=150)
    m = side / 2
    ribbon = [line(b.p(m, 0, 0), b.p(m, 0, side)), line(b.p(m, 0, side), b.p(m, side, side)),
              line(b.p(0, m, side), b.p(side, m, side)), line(b.p(side, m, side), b.p(side, m, 0))]
    bx, by = b.p(m, m, side)
    bow = [circle((bx - 8, by - 6), 7), circle((bx + 8, by - 6), 7)]
    items[3:3] = ribbon + bow
    en, ur = cube_alt(side, "Bano's gift box, a cube,", "بانو کا تحفے کا ڈبہ، ایک مکعب،") if labels else (
        "Bano's gift box, a cube, drawn in 3-D: its front, its shaded top and its shaded right side. The hidden edges at the back are dashed.",
        "بانو کا تحفے کا ڈبہ، ایک مکعب، تین رخی (3-D) شکل میں: سامنے، اوپر اور دائیں رخ پر رنگ۔ پیچھے کے چھپے ہوئے کنارے ڈیش والی لکیروں سے ہیں۔")
    return figure(en + " A ribbon goes round it, with a bow on top.", ur + " اس کے گرد ایک ربن ہے، اور اوپر ربن کی گانٹھ۔", items)


def net_size(l, w, h, max_w=280, max_h=170):
    return min(max_w / (2 * l + 2 * w), max_h / (2 * w + h))


RULE_DIMS = (5, 3, 2)


def rule_net():
    l, w, h = RULE_DIMS
    items = net_items(l, w, h, net_size(l, w, h), texts={"lw": "l×b", "lh": "l×h", "wh": "b×h"})
    return figure(
        "The net of a cuboid: the box opened out flat into 6 rectangles. In the middle row are four faces: a side marked b×h, the front marked l×h, "
        "the other side marked b×h and the back marked l×h. Above and below the front are the top and the bottom, both shaded and marked l×b. "
        "So the faces come in 3 pairs of equal rectangles.",
        "مستطیلی ڈبے کا جال (net): ڈبہ کھول کر چپٹا کیا گیا، 6 مستطیلیں۔ درمیانی قطار میں چار سطحیں ہیں: ایک پہلو جس پر b×h لکھا ہے، سامنے والی جس پر l×h، "
        "دوسرا پہلو b×h اور پیچھے والی l×h۔ سامنے والی کے اوپر اور نیچے اوپر اور نیچے کی سطحیں ہیں، دونوں رنگی ہوئی اور ان پر l×b لکھا ہے۔ "
        "تو سطحیں برابر مستطیلوں کے 3 جوڑوں میں ہیں۔ (l لمبائی، b چوڑائی، h اونچائی)",
        items)


def cube_net(side):
    sc = net_size(side, side, side, max_h=150)
    items = net_items(side, side, side, sc, cell=1)
    # The side length under the bottom face.
    items.append(label((side * sc * 1.5, side * sc * 3 + 4 + TALL / 2), cm(side)))
    return figure(
        f"The net of a cube with {side} cm sides: 6 equal squares laid flat in a cross, 4 in a row with one above and one below the second square. "
        f"Each square is split into 1 cm squares, {side} rows of {side}. The bottom square's side is labelled {side} cm.",
        f"{side} سینٹی میٹر اضلاع والے مکعب کا جال (net): 6 برابر مربع صلیب کی شکل میں چپٹے رکھے ہیں، 4 ایک قطار میں اور دوسرے مربع کے اوپر اور نیچے ایک ایک۔ "
        f"ہر مربع 1 سینٹی میٹر کے خانوں میں بٹا ہے، {side} کی {side} قطاریں۔ نیچے والے مربع کے ضلع پر {side} سینٹی میٹر لکھا ہے۔",
        items)


def error_net(l, w, h):
    lw, lh, wh = l * w, l * h, w * h
    items = net_items(l, w, h, net_size(l, w, h), texts={"lw": str(lw), "lh": str(lh), "wh": str(wh)})
    return figure(
        f"The net of the {l} cm by {w} cm by {h} cm cuboid: 6 rectangles laid flat, each with its area in cm² written on it. "
        f"The top and bottom (shaded) are {lw} each, the front and back are {lh} each, and the two sides are {wh} each.",
        f"{l} × {w} × {h} سینٹی میٹر کے مستطیلی ڈبے کا جال (net): 6 مستطیلیں چپٹی رکھی ہیں، ہر ایک پر اس کا رقبہ مربع سینٹی میٹر میں لکھا ہے۔ "
        f"اوپر اور نیچے (رنگی ہوئی) {lw}، {lw} ہیں، آگے اور پیچھے {lh}، {lh} ہیں، اور دونوں پہلو {wh}، {wh} ہیں۔",
        items)


FIGS = {
    "s1_hook": gift_fig(10, labels=False),
    "s3_rule": rule_net(),
    "s4_cube3": cube_net(3),
    "s5_cuboid": box_fig(5, 3, 2, "A cuboid", "ایک مستطیلی ڈبہ", max_s=40),
    "s7_shoe_box": box_fig(10, 6, 4, "A shoe box", "جوتوں کا ڈبہ"),
    "s8_cube5": cube_fig(5, "A dice, a cube,", "ایک پانسہ، یعنی مکعب،", max_w=150, max_h=130),
    "s9_find_error": error_net(4, 3, 2),
    "s11_gift_box": gift_fig(10, labels=True),
    "qb_apply": box_fig(6, 4, 3, max_s=34),
    "qb_find_error": cube_fig(2, max_w=130, max_h=110),
    "r_cube4": cube_fig(4, max_w=150, max_h=130),
    "r_cuboid": box_fig(8, 5, 2),
}


lesson = {
 "id": "g6-maths-14-surface-area",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Find the surface area of a cube and a cuboid by adding the areas of their six faces.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Surface area", "سطحی رقبہ"),
 "estimated_minutes": 15,
 "prerequisites": [{"skill": SO_VOLUME_CUBE}, {"skill": AREA_RECTANGLE}],
 "misconceptions": [
   {"id": "volume_mixup", "description": "Finds the volume (l × b × h) when the surface area is asked."},
   {"id": "half_faces", "description": "Adds only three faces and forgets each face has an equal opposite face."},
   {"id": "one_face", "description": "Gives the area of one face as the surface area."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_rule", "type": "recall", "step": {
     "id": "qb_rule", "type": "choice",
     "prompt": T("What is the surface area of a cube?", "مکعب کا سطحی رقبہ کیا ہے؟"),
     "options": [
       opt("six_faces", "6 × side × side", "6 × ضلع × ضلع", True,
           "Yes! A cube has 6 equal square faces.", "جی ہاں! مکعب کی 6 برابر مربع سطحیں ہیں۔"),
       opt("volume", "side × side × side", "ضلع × ضلع × ضلع", False,
           "That is the volume. Surface area adds the 6 faces: 6 × side × side.", "یہ حجم ہے۔ سطحی رقبہ 6 سطحیں جمع کرتا ہے: 6 × ضلع × ضلع", "volume_mixup"),
       opt("one_face", "side × side", "ضلع × ضلع", False,
           "That is one face. There are 6 faces.", "یہ ایک سطح ہے۔ 6 سطحیں ہیں۔", "one_face"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("A box is 6 cm long, 4 cm wide and 3 cm high. What is its surface area, in cm²?", "ایک ڈبہ 6 سینٹی میٹر لمبا، 4 سینٹی میٹر چوڑا اور 3 سینٹی میٹر اونچا ہے۔ اس کا سطحی رقبہ کتنے مربع سینٹی میٹر ہے؟"),
     QB,
     T("Add 6 × 4, 4 × 3 and 6 × 3, then double.", "6 × 4، 4 × 3 اور 6 × 3 جمع کریں، پھر دگنا کریں۔"),
     T("Right! 2 × 54 = 108 cm².", "درست! 2 × 54 = 108 مربع سینٹی میٹر"),
     T("24 + 12 + 18 = 54, and 2 × 54 = 108.", "24 + 12 + 18 = 54، اور 2 × 54 = 108"),
     common_wrong=[wrong(54, "That is only 3 faces. Double it: 108.", "یہ صرف 3 سطحیں ہیں۔ دگنا کریں: 108", "half_faces"),
                   wrong(72, "That is the volume. Add the faces: 108.", "یہ حجم ہے۔ سطحیں جمع کریں: 108", "volume_mixup")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("A cube has 2 cm sides. Sara says its surface area is 2 × 2 × 2 = 8 cm². What is wrong?", "ایک مکعب کے اضلاع 2 سینٹی میٹر ہیں۔ سارہ کہتی ہے اس کا سطحی رقبہ 2 × 2 × 2 = 8 مربع سینٹی میٹر ہے۔ کیا غلطی ہے؟"),
     "options": [
       opt("volume", "She found the volume. Surface area = 6 × 2 × 2 = 24 cm².", "اس نے حجم نکالا۔ سطحی رقبہ = 6 × 2 × 2 = 24 مربع سینٹی میٹر", True,
           "Yes! Each face is 4 cm², and there are 6 faces.", "جی ہاں! ہر سطح 4 مربع سینٹی میٹر ہے، اور 6 سطحیں ہیں۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "2 × 2 × 2 is the volume. Add the 6 faces: 24 cm².", "2 × 2 × 2 حجم ہے۔ 6 سطحیں جمع کریں: 24 مربع سینٹی میٹر", "volume_mixup"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_cube", "front": T("Surface area of a cube?", "مکعب کا سطحی رقبہ؟"),
    "back": T("6 × side × side.", "6 × ضلع × ضلع")},
   {"id": "f_cuboid", "front": T("Surface area of a cuboid?", "مستطیلی ڈبے کا سطحی رقبہ؟"),
    "back": T("2 × (l×b + b×h + l×h).", "2 × (ل×چ + چ×ا + ل×ا)")},
 ],
 "home_tasks": [{"id": "h_box", "text": T(
   "Take an empty box at home (a tea or toothpaste box). Measure its length, width and height, and find how much paper would cover it.",
   "گھر میں ایک خالی ڈبہ لیں (چائے یا ٹوتھ پیسٹ کا)۔ اس کی لمبائی، چوڑائی اور اونچائی ناپیں، اور معلوم کریں کہ اسے ڈھانپنے کے لیے کتنا کاغذ چاہیے۔")}],
 "glossary": [T("Surface area", "سطحی رقبہ"), T("Face", "سطح"), T("Cuboid", "مستطیلی ڈبہ")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Bano wants to wrap a gift box in paper. How much paper does she need?",
                     "بانو تحفے کا ڈبہ کاغذ میں لپیٹنا چاہتی ہے۔ اسے کتنا کاغذ چاہیے؟"),
    "text": T("The paper covers every face of the box. The total area of all the faces is the surface area. First, a quick area check.", "کاغذ ڈبے کی ہر سطح ڈھانپتا ہے۔ تمام سطحوں کا کل رقبہ سطحی رقبہ ہے۔ پہلے رقبے کا ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("A rectangle is 6 cm long and 4 cm wide. What is its area, in cm²?", "ایک مستطیل 6 سینٹی میٹر لمبی اور 4 سینٹی میٹر چوڑی ہے۔ اس کا رقبہ کتنے مربع سینٹی میٹر ہے؟"),
     S2,
     T("Length × width.", "لمبائی × چوڑائی"),
     T("Right! 24 cm².", "درست! 24 مربع سینٹی میٹر"),
     T("6 × 4 = 24.", "6 × 4 = 24"),
     common_wrong=[wrong(20, "That is the perimeter. Area = 6 × 4 = 24.", "یہ احاطہ ہے۔ رقبہ = 6 × 4 = 24"),
                   wrong(10, "Multiply, don't add: 6 × 4 = 24.", "جمع نہیں، ضرب: 6 × 4 = 24")],
     qtype="recall", skill=AREA_RECTANGLE),
   {"id": "s3_rule", "type": "explain",
    "character": say("happy", "Every face has a twin on the opposite side!", "ہر سطح کا ایک جڑواں سامنے والی طرف ہوتا ہے!"),
    "text": T("A cuboid has 6 faces in 3 pairs: top and bottom (l × b), front and back (l × h), and two sides (b × h). Surface area = 2 × (l×b + b×h + l×h). A cube has 6 equal square faces, so its surface area = 6 × side × side. Surface area is in cm², not cm³.",
              "مستطیلی ڈبے کی 6 سطحیں 3 جوڑوں میں ہیں: اوپر اور نیچے (ل × چ)، آگے اور پیچھے (ل × ا)، اور دو پہلو (چ × ا)۔ سطحی رقبہ = 2 × (ل×چ + چ×ا + ل×ا)۔ مکعب کی 6 برابر مربع سطحیں ہیں، تو اس کا سطحی رقبہ = 6 × ضلع × ضلع۔ سطحی رقبہ مربع سینٹی میٹر میں ہوتا ہے، مکعب سینٹی میٹر میں نہیں۔")},
   number_question(
     "s4_cube3",
     T("A cube has sides of 3 cm. What is its surface area, in cm²?", "ایک مکعب کے اضلاع 3 سینٹی میٹر ہیں۔ اس کا سطحی رقبہ کتنے مربع سینٹی میٹر ہے؟"),
     S4,
     T("One face is 3 × 3. How many faces?", "ایک سطح 3 × 3 ہے۔ کتنی سطحیں ہیں؟"),
     T("Right! 6 × 9 = 54 cm².", "درست! 6 × 9 = 54 مربع سینٹی میٹر"),
     T("One face is 9 cm², and 6 × 9 = 54.", "ایک سطح 9 مربع سینٹی میٹر ہے، اور 6 × 9 = 54"),
     common_wrong=[wrong(9, "That is one face. There are 6: 54.", "یہ ایک سطح ہے۔ 6 سطحیں ہیں: 54", "one_face"),
                   wrong(27, "That is the volume. Add the 6 faces: 54.", "یہ حجم ہے۔ 6 سطحیں جمع کریں: 54", "volume_mixup")]),
   number_question(
     "s5_cuboid",
     T("A cuboid is 5 cm long, 3 cm wide and 2 cm high. What is its surface area, in cm²?", "ایک مستطیلی ڈبہ 5 سینٹی میٹر لمبا، 3 سینٹی میٹر چوڑا اور 2 سینٹی میٹر اونچا ہے۔ اس کا سطحی رقبہ کتنے مربع سینٹی میٹر ہے؟"),
     S5,
     T("5 × 3, 3 × 2 and 5 × 2. Add them, then double.", "5 × 3، 3 × 2 اور 5 × 2۔ جمع کریں، پھر دگنا کریں۔"),
     T("Right! 2 × 31 = 62 cm².", "درست! 2 × 31 = 62 مربع سینٹی میٹر"),
     T("15 + 6 + 10 = 31, and 2 × 31 = 62.", "15 + 6 + 10 = 31، اور 2 × 31 = 62"),
     common_wrong=[wrong(31, "That is 3 faces. Each has a twin, so double: 62.", "یہ 3 سطحیں ہیں۔ ہر ایک کا جڑواں ہے، تو دگنا: 62", "half_faces"),
                   wrong(30, "That is the volume. Add the faces: 62.", "یہ حجم ہے۔ سطحیں جمع کریں: 62", "volume_mixup")]),
   {"id": "s6_unit", "type": "choice",
    "prompt": T("Which unit do we use for surface area?", "سطحی رقبے کے لیے کون سی اکائی استعمال ہوتی ہے؟"),
    "options": [
      opt("cm2", "cm²", "مربع سینٹی میٹر", True, "Yes! It is an area, so square units.", "جی ہاں! یہ رقبہ ہے، تو مربع اکائیاں۔"),
      opt("cm3", "cm³", "مکعب سینٹی میٹر", False, "cm³ is for volume. Surface area is an area: cm².", "مکعب سینٹی میٹر حجم کے لیے ہے۔ سطحی رقبہ رقبہ ہے: مربع سینٹی میٹر", "volume_mixup"),
      opt("cm", "cm", "سینٹی میٹر", False, "cm is for length. Area is in cm².", "سینٹی میٹر لمبائی کے لیے ہے۔ رقبہ مربع سینٹی میٹر میں ہے۔"),
    ]},
   number_question(
     "s7_shoe_box",
     T("A shoe box is 10 cm long, 6 cm wide and 4 cm high. How much card is needed to make it, in cm²?", "جوتوں کا ڈبہ 10 سینٹی میٹر لمبا، 6 سینٹی میٹر چوڑا اور 4 سینٹی میٹر اونچا ہے۔ اسے بنانے کے لیے کتنے مربع سینٹی میٹر گتا چاہیے؟"),
     S7,
     T("10 × 6, 6 × 4 and 10 × 4. Add, then double.", "10 × 6، 6 × 4 اور 10 × 4۔ جمع کریں، پھر دگنا کریں۔"),
     T("Right! 2 × 124 = 248 cm².", "درست! 2 × 124 = 248 مربع سینٹی میٹر"),
     T("60 + 24 + 40 = 124, and 2 × 124 = 248.", "60 + 24 + 40 = 124، اور 2 × 124 = 248"),
     common_wrong=[wrong(124, "That covers only 3 faces. Double it: 248.", "یہ صرف 3 سطحیں ڈھانپتا ہے۔ دگنا کریں: 248", "half_faces"),
                   wrong(240, "That is the volume. Add the faces: 248.", "یہ حجم ہے۔ سطحیں جمع کریں: 248", "volume_mixup")]),
   number_question(
     "s8_cube5",
     T("A dice is a cube with 5 cm sides. What is its surface area, in cm²?", "ایک پانسہ 5 سینٹی میٹر اضلاع والا مکعب ہے۔ اس کا سطحی رقبہ کتنے مربع سینٹی میٹر ہے؟"),
     S8,
     T("6 × 5 × 5.", "6 × 5 × 5"),
     T("Right! 6 × 25 = 150 cm².", "درست! 6 × 25 = 150 مربع سینٹی میٹر"),
     T("One face is 25 cm², and 6 × 25 = 150.", "ایک سطح 25 مربع سینٹی میٹر ہے، اور 6 × 25 = 150"),
     common_wrong=[wrong(125, "That is the volume. 6 × 25 = 150.", "یہ حجم ہے۔ 6 × 25 = 150", "volume_mixup"),
                   wrong(25, "That is one face. 6 × 25 = 150.", "یہ ایک سطح ہے۔ 6 × 25 = 150", "one_face")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("A cuboid is 4 cm × 3 cm × 2 cm. Hina says its surface area is 12 + 6 + 8 = 26 cm². What went wrong?", "ایک مستطیلی ڈبہ 4 × 3 × 2 سینٹی میٹر ہے۔ حنا کہتی ہے اس کا سطحی رقبہ 12 + 6 + 8 = 26 مربع سینٹی میٹر ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("double", "She added only 3 faces. Double it: 52 cm².", "اس نے صرف 3 سطحیں جمع کیں۔ دگنا کریں: 52 مربع سینٹی میٹر", True,
          "Yes! Each face has an equal face opposite it.", "جی ہاں! ہر سطح کے سامنے ایک برابر سطح ہوتی ہے۔"),
      opt("multiply", "She should multiply: 4 × 3 × 2 = 24.", "اسے ضرب دینی چاہیے: 4 × 3 × 2 = 24", False,
          "4 × 3 × 2 is the volume. She needs all 6 faces: 52.", "4 × 3 × 2 حجم ہے۔ اسے تمام 6 سطحیں چاہییں: 52", "volume_mixup"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "That is 3 faces. The box has 6: 52.", "یہ 3 سطحیں ہیں۔ ڈبے کی 6 ہیں: 52", "half_faces"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why do we multiply by 2 at the end for a cuboid? Can you teach me?",
                     "مستطیلی ڈبے کے لیے آخر میں 2 سے ضرب کیوں دیتے ہیں؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why is the surface area of a cuboid 2 × (l×b + b×h + l×h)?", "اپنے الفاظ میں بتائیں: مستطیلی ڈبے کا سطحی رقبہ 2 × (ل×چ + چ×ا + ل×ا) کیوں ہے؟"),
    "key_idea": "A cuboid has 6 faces in 3 pairs. The two faces in each pair are the same size (top and bottom, front and back, two sides), so we add three different faces and double.",
    "levels": {
      "got_it": "Says there are 6 faces in 3 equal pairs, so 3 faces are added and doubled.",
      "partly": "Says there are 6 faces, without saying they come in equal pairs.",
      "not_yet": "Gives no reason."},
    "keywords": [
      ["pair", "twin", "opposite", "جوڑ", "سامنے"],
      ["6", "six", "چھ"],
      ["face", "سطح"]],
    "fallback_feedback": {
      "got_it": T("Well explained! 3 pairs of equal faces.", "بہت خوب! برابر سطحوں کے 3 جوڑے۔"),
      "partly": T("Good start! Now say which faces are the same size.", "اچھی شروعات! اب بتائیں کون سی سطحیں برابر ہیں۔"),
      "not_yet": T("Look at a box. Is the top the same as the bottom? What about front and back?", "ایک ڈبہ دیکھیں۔ کیا اوپر والی سطح نیچے والی جیسی ہے؟ آگے اور پیچھے والی؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_gift_box",
     T("Bano's gift box is a cube with 10 cm sides. How much paper covers it exactly, in cm²?", "بانو کا تحفے کا ڈبہ 10 سینٹی میٹر اضلاع والا مکعب ہے۔ اسے ٹھیک ٹھیک ڈھانپنے کے لیے کتنے مربع سینٹی میٹر کاغذ چاہیے؟"),
     S11,
     T("6 × 10 × 10.", "6 × 10 × 10"),
     T("Right! 6 × 100 = 600 cm².", "درست! 6 × 100 = 600 مربع سینٹی میٹر"),
     T("One face is 100 cm², and 6 × 100 = 600.", "ایک سطح 100 مربع سینٹی میٹر ہے، اور 6 × 100 = 600"),
     common_wrong=[wrong(1000, "That is the volume. Paper covers the faces: 600.", "یہ حجم ہے۔ کاغذ سطحیں ڈھانپتا ہے: 600", "volume_mixup"),
                   wrong(100, "That is one face. There are 6: 600.", "یہ ایک سطح ہے۔ 6 سطحیں ہیں: 600", "one_face")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Six faces, three pairs. You can wrap any box now!", "چھ سطحیں، تین جوڑے۔ اب آپ کوئی بھی ڈبہ لپیٹ سکتے ہیں!"),
    "text": T("Surface area is the total area of all the faces, in cm². Cuboid: 2 × (l×b + b×h + l×h). Cube: 6 × side × side.",
              "سطحی رقبہ تمام سطحوں کا کل رقبہ ہے، مربع سینٹی میٹر میں۔ مستطیلی ڈبہ: 2 × (ل×چ + چ×ا + ل×ا)۔ مکعب: 6 × ضلع × ضلع۔"),
    "points": [T("Cuboid: add 3 faces, then double.", "مستطیلی ڈبہ: 3 سطحیں جمع کریں، پھر دگنا۔"),
               T("Cube: 6 × side × side.", "مکعب: 6 × ضلع × ضلع۔")]},
 ],
 "review_questions": [
   {"id": "r_cube4", "type": "apply", "skill": SKILL, "step": number_question(
     "r_cube4",
     T("A cube has sides of 4 cm. What is its surface area, in cm²?", "ایک مکعب کے اضلاع 4 سینٹی میٹر ہیں۔ اس کا سطحی رقبہ کتنے مربع سینٹی میٹر ہے؟"),
     R1,
     T("6 × 4 × 4.", "6 × 4 × 4"),
     T("Right! 6 × 16 = 96 cm².", "درست! 6 × 16 = 96 مربع سینٹی میٹر"),
     T("One face is 16 cm², and 6 × 16 = 96.", "ایک سطح 16 مربع سینٹی میٹر ہے، اور 6 × 16 = 96"),
     common_wrong=[wrong(64, "That is the volume. 6 × 16 = 96.", "یہ حجم ہے۔ 6 × 16 = 96", "volume_mixup"),
                   wrong(16, "That is one face. 6 × 16 = 96.", "یہ ایک سطح ہے۔ 6 × 16 = 96", "one_face")],
     qtype=None)},
   {"id": "r_cuboid", "type": "apply", "skill": SKILL, "step": number_question(
     "r_cuboid",
     T("A box is 8 cm long, 5 cm wide and 2 cm high. What is its surface area, in cm²?", "ایک ڈبہ 8 سینٹی میٹر لمبا، 5 سینٹی میٹر چوڑا اور 2 سینٹی میٹر اونچا ہے۔ اس کا سطحی رقبہ کتنے مربع سینٹی میٹر ہے؟"),
     R2,
     T("8 × 5, 5 × 2 and 8 × 2. Add, then double.", "8 × 5، 5 × 2 اور 8 × 2۔ جمع کریں، پھر دگنا کریں۔"),
     T("Right! 2 × 66 = 132 cm².", "درست! 2 × 66 = 132 مربع سینٹی میٹر"),
     T("40 + 10 + 16 = 66, and 2 × 66 = 132.", "40 + 10 + 16 = 66، اور 2 × 66 = 132"),
     common_wrong=[wrong(66, "That is 3 faces. Double it: 132.", "یہ 3 سطحیں ہیں۔ دگنا کریں: 132", "half_faces"),
                   wrong(80, "That is the volume. Add the faces: 132.", "یہ حجم ہے۔ سطحیں جمع کریں: 132", "volume_mixup")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Solids unit. No textbook text or exercises were used.",
   "Opening a real box flat (its net) helps children see the 3 pairs of equal faces.",
   "Urdu terms to check: سطحی رقبہ (surface area), مستطیلی ڈبہ (cuboid), ل/چ/ا for length, breadth and height.",
   "The numbers were worked out in content/sources/g6-maths-14/surface_area.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(with_figures(lesson, FIGS))
