from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, AREA_RECTANGLE, SO_PARTS, SO_VOLUME_CUBOID, cuboid_volume)

SKILL = SO_VOLUME_CUBOID

# s2: area of a 5 cm by 3 cm rectangle
S2 = 5 * 3
assert S2 == 15
# s4: 4 x 3 x 2 (adding gives 9)
S4 = cuboid_volume(4, 3, 2)
assert S4 == 24 and 4 + 3 + 2 == 9
# s5: matchbox 5 x 3 x 2 (only the base gives 15)
S5 = cuboid_volume(5, 3, 2)
assert S5 == 30 and 5 * 3 == 15
# s7: brick 20 x 10 x 5
S7 = cuboid_volume(20, 10, 5)
assert S7 == 1000
# s8: base area 12 cm2, height 5 cm
S8 = 12 * 5
assert S8 == 60
# s9: 4 + 3 + 2 = 9 is wrong; 4 x 3 x 2 = 24
assert cuboid_volume(4, 3, 2) == 24
# s11: a 10 x 6 x 4 box filled with 1 cm cubes
S11 = cuboid_volume(10, 6, 4)
assert S11 == 240 and 10 * 6 == 60
# question bank and review
QB = cuboid_volume(6, 2, 3)
assert QB == 36 and 6 + 2 + 3 == 11
R1 = cuboid_volume(8, 5, 2)
assert R1 == 80
R2 = 20 * 3
assert R2 == 60

# ---------- figures ----------
from figs import (Box, fit, figure, row, box_items, box_fig, box_alt, label, line, poly, cm, shift, extent,
                  with_figures)


def grid_box(l, d, h, en="A box", ur="ایک ڈبہ", **kw):
    """A box with its faces split into 1 cm squares: the 1 cm cubes that fill it."""
    return box_fig(l, d, h, en, ur, grid=1, **kw)


def layers_fig(l, d, h):
    """Left: one layer of l × d cubes on the bottom. Right: h such layers."""
    layer, _ = box_items(l, d, 1, grid=1, max_w=100, max_h=100, max_s=26, texts=(cm(l), cm(d), None))
    full, _ = box_items(l, d, h, grid=1, max_w=100, max_h=100, max_s=26)
    return figure(
        f"Two boxes made of 1 cm cubes, drawn in 3-D. Left: one layer, {l} cubes long and {d} cubes wide, so {l} × {d} = {l * d} cubes cover the bottom. "
        f"Right: the full box, {l} cm long, {d} cm wide and {h} cm high, which is {h} such layers stacked up: {l * d} × {h} = {l * d * h} cubes. "
        f"Hidden edges at the back are dashed.",
        f"1 سینٹی میٹر کے مکعبوں سے بنے دو ڈبے، تین رخی (3-D) شکل میں۔ بائیں: ایک تہہ، {l} مکعب لمبی اور {d} مکعب چوڑی، تو {l} × {d} = {l * d} مکعب تہہ ڈھانپتے ہیں۔ "
        f"دائیں: پورا ڈبہ، {l} سینٹی میٹر لمبا، {d} سینٹی میٹر چوڑا اور {h} سینٹی میٹر اونچا، جو ایسی {h} تہیں اوپر تلے ہیں: {l * d} × {h} = {l * d * h} مکعب۔ "
        f"پیچھے کے چھپے ہوئے کنارے ڈیش والی لکیروں سے ہیں۔",
        row([layer, full], gap=20))


def base_fig(area, h, l, d):
    """A box h cm high standing above its bottom face, drawn apart and
    shaded, with the area of the bottom written on it. l and d only set
    the shape of the bottom; they are not labelled."""
    items, b = box_items(l, d, h, max_w=170, max_h=110, texts=(None, None, cm(h)))
    gap = 26
    base = [b.p(0, 0, 0), b.p(l, 0, 0), b.p(l, d, 0), b.p(0, d, 0)]
    base = [(x, y + gap + b.s * d * 0.25) for x, y in base]
    items.append(poly(base, fill=True))
    for i in (0, l):
        top = b.p(i, 0, 0)
        items.append(line((top[0], top[1] + 4), (top[0], base[0][1] - 4 if i == 0 else base[1][1] - 4), dashed=True))
    cx = sum(x for x, _ in base) / 4
    cy = sum(y for _, y in base) / 4
    items.append(label((cx, cy), f"{area}cm²"))
    return figure(
        f"A box drawn in 3-D, {h} cm high (labelled on its left edge). Its bottom face is drawn again just below it as a shaded flat shape, "
        f"joined to it by dashed lines, with its area, {area} cm², written on it. Hidden edges at the back of the box are dashed.",
        f"ایک ڈبہ تین رخی (3-D) شکل میں، {h} سینٹی میٹر اونچا (بائیں کنارے پر لکھا ہے)۔ اس کی نچلی سطح (تہہ) نیچے الگ سے ایک رنگی ہوئی چپٹی شکل میں بنی ہے، "
        f"ڈیش والی لکیروں سے جڑی، اور اس پر اس کا رقبہ {area} مربع سینٹی میٹر لکھا ہے۔ ڈبے کے پیچھے کے چھپے ہوئے کنارے ڈیش والی لکیروں سے ہیں۔",
        items)


F_HOOK = figure(
    "A box filled with 1 cm sugar cubes, drawn in 3-D: the lines on its front, top and side show the rows of small cubes inside. Hidden edges at the back are dashed.",
    "1 سینٹی میٹر کے چینی کے ٹکڑوں سے بھرا ڈبہ، تین رخی (3-D) شکل میں: سامنے، اوپر اور پہلو پر لکیریں اندر چھوٹے مکعبوں کی قطاریں دکھاتی ہیں۔ پیچھے کے چھپے ہوئے کنارے ڈیش والی لکیروں سے ہیں۔",
    box_items(4, 3, 2, labels=False, grid=1, max_s=40)[0])

FIGS = {
    "s1_hook": F_HOOK,
    "s3_rule": layers_fig(4, 3, 2),
    "s4_first": grid_box(4, 3, 2, max_s=40),
    "s5_matchbox": box_fig(5, 3, 2, "A matchbox", "ماچس کی ڈبیا", max_s=40),
    "s7_brick": box_fig(20, 10, 5, "A brick", "ایک اینٹ"),
    "s8_base": base_fig(S8 // 5, 5, 4, 3),
    "s9_find_error": grid_box(4, 3, 2, max_s=40),
    "s11_sugar": grid_box(10, 6, 4),
    "qb_apply": box_fig(6, 2, 3, max_s=30),
    "qb_find_error": grid_box(5, 4, 3, "A tin box", "ٹین کا ڈبہ", max_s=32),
    "r_box": box_fig(8, 5, 2),
    "r_base": base_fig(20, R2 // 20, 5, 4),
}


lesson = {
 "id": "g6-maths-14-volume-cuboid",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Find the volume of a cuboid as length × breadth × height, in cubic centimetres.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Volume of a cuboid", "مکعب نما کا حجم"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": SO_PARTS}, {"skill": AREA_RECTANGLE}],
 "misconceptions": [
   {"id": "adds_lengths", "description": "Adds the length, breadth and height instead of multiplying them."},
   {"id": "area_only", "description": "Finds only the area of the base and forgets the height."},
   {"id": "square_units", "description": "Writes volume in cm or cm² instead of cm³."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_units", "type": "recall", "step": {
     "id": "qb_units", "type": "choice",
     "prompt": T("Which unit is used for volume?", "حجم کے لیے کون سی اکائی استعمال ہوتی ہے؟"),
     "options": [
       opt("cm3", "cm³ (cubic centimetres)", "مکعب سینٹی میٹر (cm³)", True,
           "Yes! Volume counts 1 cm cubes.", "جی ہاں! حجم 1 سینٹی میٹر کے مکعب گنتا ہے۔"),
       opt("cm2", "cm² (square centimetres)", "مربع سینٹی میٹر (cm²)", False,
           "cm² is for area. Volume is in cm³.", "cm² رقبے کے لیے ہے۔ حجم cm³ میں ہوتا ہے۔", "square_units"),
       opt("cm", "cm", "سینٹی میٹر", False,
           "cm measures length. Volume is in cm³.", "سینٹی میٹر لمبائی ناپتا ہے۔ حجم cm³ میں ہوتا ہے۔", "square_units"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("A box is 6 cm long, 2 cm wide and 3 cm high. What is its volume, in cm³?", "ایک ڈبہ 6 سینٹی میٹر لمبا، 2 سینٹی میٹر چوڑا اور 3 سینٹی میٹر اونچا ہے۔ اس کا حجم کتنے مکعب سینٹی میٹر ہے؟"),
     QB,
     T("Length × breadth × height.", "لمبائی × چوڑائی × اونچائی"),
     T("Right! 36 cm³.", "درست! 36 مکعب سینٹی میٹر"),
     T("6 × 2 × 3 = 36.", "6 × 2 × 3 = 36"),
     common_wrong=[wrong(11, "Multiply, don't add: 6 × 2 × 3 = 36.", "جمع نہیں، ضرب: 6 × 2 × 3 = 36", "adds_lengths"),
                   wrong(12, "That is only the base. Multiply by the height too: 36.", "یہ صرف تہہ ہے۔ اونچائی سے بھی ضرب دیں: 36", "area_only")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("A tin box is 5 cm by 4 cm by 3 cm. Asad says its volume is 5 × 4 = 20 cm³. What is wrong?", "ٹین کا ڈبہ 5 × 4 × 3 سینٹی میٹر ہے۔ اسد کہتا ہے اس کا حجم 5 × 4 = 20 مکعب سینٹی میٹر ہے۔ کیا غلطی ہے؟"),
     "options": [
       opt("height", "He forgot the height: 5 × 4 × 3 = 60 cm³.", "وہ اونچائی بھول گیا: 5 × 4 × 3 = 60 مکعب سینٹی میٹر", True,
           "Yes! 20 cubes cover the base, and there are 3 layers.", "جی ہاں! 20 مکعب تہہ ڈھانپتے ہیں، اور 3 تہیں ہیں۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "5 × 4 is the area of the base. Multiply by the height, 3: 60.", "5 × 4 تہہ کا رقبہ ہے۔ اونچائی 3 سے ضرب دیں: 60", "area_only"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_volume", "front": T("Volume of a cuboid?", "مکعب نما کا حجم؟"),
    "back": T("Length × breadth × height, in cm³.", "لمبائی × چوڑائی × اونچائی، مکعب سینٹی میٹر میں۔")},
   {"id": "f_layers", "front": T("Another way?", "دوسرا طریقہ؟"),
    "back": T("Area of the base × height (number of layers).", "تہہ کا رقبہ × اونچائی (تہوں کی تعداد)۔")},
 ],
 "home_tasks": [{"id": "h_box", "text": T(
   "Find a box at home, like a tea box or a shoe box. Measure its length, breadth and height with a ruler, to the nearest centimetre, and work out its volume.",
   "گھر میں کوئی ڈبہ ڈھونڈیں، جیسے چائے کا ڈبہ یا جوتوں کا ڈبہ۔ فٹے سے اس کی لمبائی، چوڑائی اور اونچائی قریب ترین سینٹی میٹر تک ناپیں اور اس کا حجم نکالیں۔")}],
 "glossary": [T("Volume", "حجم"), T("Cubic centimetre (cm³)", "مکعب سینٹی میٹر"), T("Height", "اونچائی")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "How many sugar cubes fit in a box? That's the box's volume!",
                     "ایک ڈبے میں چینی کے کتنے ٹکڑے آئیں گے؟ یہی ڈبے کا حجم ہے!"),
    "text": T("Today we find how much space is inside a box. First, a quick area check.", "آج ہم معلوم کریں گے کہ ڈبے کے اندر کتنی جگہ ہے۔ پہلے رقبے کا ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("A rectangle is 5 cm by 3 cm. What is its area, in cm²?", "ایک مستطیل 5 × 3 سینٹی میٹر ہے۔ اس کا رقبہ کتنے مربع سینٹی میٹر ہے؟"),
     S2,
     T("Length × width.", "لمبائی × چوڑائی"),
     T("Right! 15 cm².", "درست! 15 مربع سینٹی میٹر"),
     T("5 × 3 = 15.", "5 × 3 = 15"),
     common_wrong=[wrong(16, "16 is the perimeter. Area = 5 × 3 = 15.", "16 احاطہ ہے۔ رقبہ = 5 × 3 = 15")],
     qtype="recall", skill=AREA_RECTANGLE),
   {"id": "s3_rule", "type": "explain",
    "character": say("happy", "Cover the bottom with cubes, then stack layers up to the top!", "تہہ کو مکعبوں سے ڈھانپیں، پھر اوپر تک تہیں رکھیں!"),
    "text": T("Volume is the space inside a solid. We count it in 1 cm cubes, called cubic centimetres (cm³). For a box 4 cm long and 3 cm wide, 4 × 3 = 12 cubes cover the bottom. If it is 2 cm high, there are 2 layers: 12 × 2 = 24 cm³. So volume = length × breadth × height.",
              "حجم کسی ٹھوس کے اندر کی جگہ ہے۔ ہم اسے 1 سینٹی میٹر کے مکعبوں میں گنتے ہیں، جنہیں مکعب سینٹی میٹر (cm³) کہتے ہیں۔ 4 سینٹی میٹر لمبے اور 3 سینٹی میٹر چوڑے ڈبے کی تہہ 4 × 3 = 12 مکعب ڈھانپتے ہیں۔ اگر یہ 2 سینٹی میٹر اونچا ہے تو 2 تہیں ہیں: 12 × 2 = 24 مکعب سینٹی میٹر۔ تو حجم = لمبائی × چوڑائی × اونچائی۔")},
   number_question(
     "s4_first",
     T("A box is 4 cm long, 3 cm wide and 2 cm high. What is its volume, in cm³?", "ایک ڈبہ 4 سینٹی میٹر لمبا، 3 سینٹی میٹر چوڑا اور 2 سینٹی میٹر اونچا ہے۔ اس کا حجم کتنے مکعب سینٹی میٹر ہے؟"),
     S4,
     T("4 × 3 × 2.", "4 × 3 × 2"),
     T("Right! 24 cm³.", "درست! 24 مکعب سینٹی میٹر"),
     T("4 × 3 = 12, 12 × 2 = 24.", "4 × 3 = 12، 12 × 2 = 24"),
     common_wrong=[wrong(9, "Multiply, don't add: 4 × 3 × 2 = 24.", "جمع نہیں، ضرب: 4 × 3 × 2 = 24", "adds_lengths"),
                   wrong(12, "That covers only the bottom. There are 2 layers: 24.", "یہ صرف تہہ ڈھانپتا ہے۔ 2 تہیں ہیں: 24", "area_only")]),
   number_question(
     "s5_matchbox",
     T("A matchbox is 5 cm long, 3 cm wide and 2 cm high. What is its volume, in cm³?", "ماچس کی ڈبیا 5 سینٹی میٹر لمبی، 3 سینٹی میٹر چوڑی اور 2 سینٹی میٹر اونچی ہے۔ اس کا حجم کتنے مکعب سینٹی میٹر ہے؟"),
     S5,
     T("5 × 3 × 2.", "5 × 3 × 2"),
     T("Right! 30 cm³.", "درست! 30 مکعب سینٹی میٹر"),
     T("5 × 3 = 15, 15 × 2 = 30.", "5 × 3 = 15، 15 × 2 = 30"),
     common_wrong=[wrong(15, "That is only the base. Multiply by the height, 2: 30.", "یہ صرف تہہ ہے۔ اونچائی 2 سے ضرب دیں: 30", "area_only"),
                   wrong(10, "Multiply all three: 5 × 3 × 2 = 30.", "تینوں کو ضرب دیں: 5 × 3 × 2 = 30", "adds_lengths")]),
   {"id": "s6_unit", "type": "choice",
    "prompt": T("The volume of a box is 30 ___. Which unit fits?", "ایک ڈبے کا حجم 30 ___ ہے۔ کون سی اکائی درست ہے؟"),
    "options": [
      opt("cm3", "cm³", "مکعب سینٹی میٹر (cm³)", True, "Yes! Volume is in cubic units.", "جی ہاں! حجم مکعب اکائیوں میں ہوتا ہے۔"),
      opt("cm2", "cm²", "مربع سینٹی میٹر (cm²)", False, "cm² is for area. Volume is cm³.", "cm² رقبے کے لیے ہے۔ حجم cm³ ہے۔", "square_units"),
      opt("cm", "cm", "سینٹی میٹر", False, "cm is for length. Volume is cm³.", "سینٹی میٹر لمبائی کے لیے ہے۔ حجم cm³ ہے۔", "square_units"),
    ]},
   number_question(
     "s7_brick",
     T("A brick is 20 cm long, 10 cm wide and 5 cm high. What is its volume, in cm³?", "ایک اینٹ 20 سینٹی میٹر لمبی، 10 سینٹی میٹر چوڑی اور 5 سینٹی میٹر اونچی ہے۔ اس کا حجم کتنے مکعب سینٹی میٹر ہے؟"),
     S7,
     T("20 × 10 = 200, then × 5.", "20 × 10 = 200، پھر × 5"),
     T("Right! 1000 cm³.", "درست! 1000 مکعب سینٹی میٹر"),
     T("20 × 10 × 5 = 1000.", "20 × 10 × 5 = 1000"),
     common_wrong=[wrong(35, "Multiply, don't add: 20 × 10 × 5 = 1000.", "جمع نہیں، ضرب: 20 × 10 × 5 = 1000", "adds_lengths"),
                   wrong(200, "That is only the base. Multiply by the height, 5: 1000.", "یہ صرف تہہ ہے۔ اونچائی 5 سے ضرب دیں: 1000", "area_only")]),
   number_question(
     "s8_base",
     T("The bottom of a box has an area of 12 cm². The box is 5 cm high. What is its volume, in cm³?", "ایک ڈبے کی تہہ کا رقبہ 12 مربع سینٹی میٹر ہے۔ ڈبہ 5 سینٹی میٹر اونچا ہے۔ اس کا حجم کتنے مکعب سینٹی میٹر ہے؟"),
     S8,
     T("Base area × height.", "تہہ کا رقبہ × اونچائی"),
     T("Right! 12 × 5 = 60 cm³.", "درست! 12 × 5 = 60 مکعب سینٹی میٹر"),
     T("12 cubes per layer, 5 layers: 60.", "ہر تہہ میں 12 مکعب، 5 تہیں: 60"),
     common_wrong=[wrong(17, "Multiply, don't add: 12 × 5 = 60.", "جمع نہیں، ضرب: 12 × 5 = 60", "adds_lengths")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("A box is 4 cm by 3 cm by 2 cm. Maria says its volume is 4 + 3 + 2 = 9 cm³. What went wrong?", "ایک ڈبہ 4 × 3 × 2 سینٹی میٹر ہے۔ ماریہ کہتی ہے اس کا حجم 4 + 3 + 2 = 9 مکعب سینٹی میٹر ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("multiply", "She added. She should multiply: 4 × 3 × 2 = 24 cm³.", "اس نے جمع کیا۔ اسے ضرب دینی چاہیے: 4 × 3 × 2 = 24 مکعب سینٹی میٹر", True,
          "Yes! 12 cubes per layer, 2 layers.", "جی ہاں! ہر تہہ میں 12 مکعب، 2 تہیں۔"),
      opt("units", "Only the unit is wrong.", "صرف اکائی غلط ہے۔", False,
          "The unit is right. The working is wrong: multiply to get 24.", "اکائی درست ہے۔ حل غلط ہے: ضرب سے 24 آتا ہے۔"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "Adding gives the total length of three edges, not the space inside. 24 cm³.", "جمع سے تین کناروں کی لمبائی آتی ہے، اندر کی جگہ نہیں۔ 24 مکعب سینٹی میٹر", "adds_lengths"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why do we multiply all three lengths to get the volume? Can you teach me?",
                     "حجم نکالنے کے لیے تینوں لمبائیوں کو ضرب کیوں دیتے ہیں؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why is the volume of a 4 cm × 3 cm × 2 cm box equal to 4 × 3 × 2?", "اپنے الفاظ میں بتائیں: 4 × 3 × 2 سینٹی میٹر کے ڈبے کا حجم 4 × 3 × 2 کیوں ہے؟"),
    "key_idea": "4 × 3 = 12 one-centimetre cubes cover the bottom of the box in one layer. The box is 2 cm high, so there are 2 such layers. 12 × 2 = 24 cubes fill the box.",
    "levels": {
      "got_it": "Says 4 × 3 cubes make one layer covering the bottom, and the height tells how many layers, so multiply again.",
      "partly": "Mentions layers or cubes, without linking both lengths of the base and the height.",
      "not_yet": "Gives no reason."},
    "keywords": [
      ["layer", "تہہ", "تہیں"],
      ["cube", "مکعب"],
      ["bottom", "base", "height", "نیچے", "اونچائی"]],
    "fallback_feedback": {
      "got_it": T("Well explained! One layer of 12 cubes, 2 layers high.", "بہت خوب! 12 مکعبوں کی ایک تہہ، 2 تہیں اونچی۔"),
      "partly": T("Good start! Now say how many cubes are in one layer, and how many layers there are.", "اچھی شروعات! اب بتائیں ایک تہہ میں کتنے مکعب ہیں، اور کتنی تہیں ہیں۔"),
      "not_yet": T("Imagine filling the box with sugar cubes. How many cover the bottom? How many layers fit?", "سوچیں ڈبے کو چینی کے ٹکڑوں سے بھر رہے ہیں۔ تہہ میں کتنے آتے ہیں؟ کتنی تہیں آتی ہیں؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_sugar",
     T("A box is 10 cm long, 6 cm wide and 4 cm high. How many 1 cm sugar cubes fill it?", "ایک ڈبہ 10 سینٹی میٹر لمبا، 6 سینٹی میٹر چوڑا اور 4 سینٹی میٹر اونچا ہے۔ 1 سینٹی میٹر کے چینی کے کتنے ٹکڑے اس میں آئیں گے؟"),
     S11,
     T("10 × 6 cubes per layer, 4 layers.", "ہر تہہ میں 10 × 6 مکعب، 4 تہیں۔"),
     T("Right! 60 × 4 = 240 sugar cubes.", "درست! 60 × 4 = 240 ٹکڑے"),
     T("10 × 6 = 60, 60 × 4 = 240.", "10 × 6 = 60، 60 × 4 = 240"),
     common_wrong=[wrong(60, "That fills only one layer. 4 layers: 240.", "یہ صرف ایک تہہ بھرتا ہے۔ 4 تہیں: 240", "area_only"),
                   wrong(20, "Multiply, don't add: 10 × 6 × 4 = 240.", "جمع نہیں، ضرب: 10 × 6 × 4 = 240", "adds_lengths")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Length times breadth times height. You can measure the space inside any box!", "لمبائی ضرب چوڑائی ضرب اونچائی۔ اب آپ کسی بھی ڈبے کے اندر کی جگہ ناپ سکتے ہیں!"),
    "text": T("Volume is the space inside a solid, measured in cm³. Volume of a cuboid = length × breadth × height, which is the same as the area of the base × the height.",
              "حجم کسی ٹھوس کے اندر کی جگہ ہے، جو مکعب سینٹی میٹر میں ناپی جاتی ہے۔ مکعب نما کا حجم = لمبائی × چوڑائی × اونچائی، جو تہہ کے رقبے × اونچائی کے برابر ہے۔"),
    "points": [T("V = l × b × h.", "حجم = لمبائی × چوڑائی × اونچائی"),
               T("Volume is in cm³.", "حجم مکعب سینٹی میٹر میں۔")]},
 ],
 "review_questions": [
   {"id": "r_box", "type": "apply", "skill": SKILL, "step": number_question(
     "r_box",
     T("A box is 8 cm long, 5 cm wide and 2 cm high. What is its volume, in cm³?", "ایک ڈبہ 8 سینٹی میٹر لمبا، 5 سینٹی میٹر چوڑا اور 2 سینٹی میٹر اونچا ہے۔ اس کا حجم کتنے مکعب سینٹی میٹر ہے؟"),
     R1,
     T("8 × 5 × 2.", "8 × 5 × 2"),
     T("Right! 80 cm³.", "درست! 80 مکعب سینٹی میٹر"),
     T("8 × 5 = 40, 40 × 2 = 80.", "8 × 5 = 40، 40 × 2 = 80"),
     common_wrong=[wrong(15, "Multiply, don't add: 8 × 5 × 2 = 80.", "جمع نہیں، ضرب: 8 × 5 × 2 = 80", "adds_lengths")],
     qtype=None)},
   {"id": "r_base", "type": "apply", "skill": SKILL, "step": number_question(
     "r_base",
     T("The bottom of a tank has an area of 20 cm². It is 3 cm high. What is its volume, in cm³?", "ایک ٹینکی کی تہہ کا رقبہ 20 مربع سینٹی میٹر ہے۔ یہ 3 سینٹی میٹر اونچی ہے۔ اس کا حجم کتنے مکعب سینٹی میٹر ہے؟"),
     R2,
     T("Base area × height.", "تہہ کا رقبہ × اونچائی"),
     T("Right! 60 cm³.", "درست! 60 مکعب سینٹی میٹر"),
     T("20 × 3 = 60.", "20 × 3 = 60"),
     common_wrong=[wrong(23, "Multiply, don't add: 20 × 3 = 60.", "جمع نہیں، ضرب: 20 × 3 = 60", "adds_lengths")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Solids unit. No textbook text or exercises were used.",
   "Volume is built from layers of 1 cm cubes before the formula, so the formula has a meaning.",
   "Urdu terms to check: حجم (volume), مکعب سینٹی میٹر (cubic centimetre), تہہ (base/layer).",
   "The numbers were worked out in content/sources/g6-maths-14/volume_cuboid.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(with_figures(lesson, FIGS))
