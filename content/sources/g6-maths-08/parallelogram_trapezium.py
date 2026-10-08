from fractions import Fraction as F

from common import (T, opt, say, wrong, number_question, write,
                    BOOK, REVIEW, PA_TRIANGLE, PA_PARALLELOGRAM)

SKILL = PA_PARALLELOGRAM


def tri(base, height):
    a = F(base * height, 2)
    assert a.denominator == 1, (base, height)
    return int(a)


def para(base, height):
    return base * height


def trap(a, b, height):
    t = F((a + b) * height, 2)
    assert t.denominator == 1, (a, b, height)
    return int(t)


# s2: triangle base 10, height 6
S2 = tri(10, 6)
assert S2 == 30 and 10 * 6 == 60
# s4: parallelogram base 9, height 5, slanting side 7
S4 = para(9, 5)
assert S4 == 45 and para(9, 7) == 63 and 2 * (9 + 7) == 32
# s5: parallelogram area 48 m², base 8 m -> height
S5 = 48 // 8
assert S5 == 6 and para(8, S5) == 48 and 48 // 2 // 8 == 3
# s6: two copies of a trapezium with parallel sides 6 and 10 make a parallelogram
S6 = 6 + 10
assert S6 == 16 and 10 - 6 == 4
# s7: trapezium parallel sides 6 and 10, height 4
S7 = trap(6, 10, 4)
assert S7 == 32 and (6 + 10) * 4 == 64 and 10 * 4 == 40 and para(S6, 4) == 2 * S7
# s8: trapezium parallel sides 5 m and 9 m, height 6 m, slanting sides 7 m
S8 = trap(5, 9, 6)
assert S8 == 42 and (5 + 9) * 6 == 84 and trap(5, 9, 7) == 49
# s9: parallel sides 8 and 12, height 5
S9 = trap(8, 12, 5)
assert S9 == 50 and (8 + 12) * 5 == 100 and 12 * 5 == 60
# s11: parallelogram tile base 15, height 8, slanting side 10
S11 = para(15, 8)
assert S11 == 120 and para(15, 10) == 150 and tri(15, 8) == 60
# question bank
QB = trap(4, 10, 6)
assert QB == 42 and (4 + 10) * 6 == 84 and 10 * 6 == 60
QB_ERR = para(12, 6)
assert QB_ERR == 72 and para(12, 8) == 96
# review
R1 = para(11, 4)
assert R1 == 44 and tri(11, 4) == 22
R2 = trap(3, 7, 8)
assert R2 == 40 and (3 + 7) * 8 == 80 and 7 * 8 == 56


lesson = {
 "id": "g6-maths-08-parallelogram-and-trapezium",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Find the area of a parallelogram as base × perpendicular height, and of a trapezium as ½ × (sum of the parallel sides) × height.", "textbook": BOOK}],
 "skills": [SKILL],
 "title": T("Area of a parallelogram and a trapezium", "متوازی الاضلاع اور ذوزنقہ کا رقبہ"),
 "estimated_minutes": 15,
 "prerequisites": [{"skill": PA_TRIANGLE}],
 "misconceptions": [
   {"id": "slant_height", "description": "Multiplies by the slanting side instead of the perpendicular height."},
   {"id": "trap_forgets_half", "description": "Adds the parallel sides and multiplies by the height, forgetting to halve."},
   {"id": "one_parallel_side", "description": "Uses only one of the parallel sides of a trapezium instead of their sum."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_formula", "type": "recall", "step": {
     "id": "qb_formula", "type": "choice",
     "prompt": T("What is the area of a parallelogram?", "متوازی الاضلاع کا رقبہ کیا ہوتا ہے؟"),
     "options": [
       opt("base_height", "Base × perpendicular height", "قاعدہ × عمودی اونچائی", True,
           "Yes! Move a triangle from one end to the other and it becomes a rectangle.", "جی ہاں! ایک سرے سے مثلث کاٹ کر دوسرے سرے پر لگائیں تو مستطیل بن جاتی ہے۔"),
       opt("base_slant", "Base × slanting side", "قاعدہ × ترچھا ضلع", False,
           "The slanting side is longer than the height. Use the straight-up height.", "ترچھا ضلع اونچائی سے لمبا ہے۔ سیدھی اوپر والی اونچائی لیں۔", "slant_height"),
       opt("half", "Half of base × height", "قاعدہ × اونچائی کا آدھا", False,
           "That is a triangle. A parallelogram is a whole rectangle's worth: base × height.", "یہ مثلث کا ہے۔ متوازی الاضلاع پوری مستطیل جتنا ہے: قاعدہ × اونچائی۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("A trapezium has parallel sides of 4 cm and 10 cm, and a height of 6 cm. What is its area in cm²?",
       "ایک ذوزنقہ کے متوازی اضلاع 4 اور 10 سینٹی میٹر ہیں، اور اونچائی 6 سینٹی میٹر ہے۔ اس کا رقبہ کتنے مربع سینٹی میٹر ہے؟"),
     QB,
     T("Add the parallel sides, multiply by the height, then halve.", "متوازی اضلاع جمع کریں، اونچائی سے ضرب دیں، پھر آدھا کریں۔"),
     T("Right! 42 cm².", "درست! 42 مربع سینٹی میٹر"),
     T("4 + 10 = 14, 14 × 6 = 84, half is 42 cm².", "4 + 10 = 14، 14 × 6 = 84، آدھا 42"),
     common_wrong=[wrong(84, "Don't forget to halve: 84 ÷ 2 = 42.", "آدھا کرنا نہ بھولیں: 84 ÷ 2 = 42", "trap_forgets_half"),
                   wrong(60, "Use both parallel sides: ½ × (4 + 10) × 6 = 42.", "دونوں متوازی اضلاع لیں: ½ × (4 + 10) × 6 = 42", "one_parallel_side")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("A parallelogram has base 12 cm, height 6 cm and slanting sides of 8 cm. Bilal says its area is 12 × 8 = 96 cm². What went wrong?",
                 "ایک متوازی الاضلاع کا قاعدہ 12، اونچائی 6 اور ترچھے اضلاع 8 سینٹی میٹر ہیں۔ بلال کہتا ہے رقبہ 12 × 8 = 96 ہے۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("height", "He used the slanting side. Use the height: 12 × 6 = 72 cm².", "اس نے ترچھا ضلع لیا۔ اونچائی لیں: 12 × 6 = 72", True,
           "Yes! The height goes straight up from the base, at a right angle.", "جی ہاں! اونچائی قاعدے سے سیدھی اوپر، زاویہ قائمہ پر جاتی ہے۔"),
       opt("half", "He forgot to halve: 48 cm².", "وہ آدھا کرنا بھول گیا: 48", False,
           "A parallelogram is not halved. The mistake is the slanting side: 12 × 6 = 72.", "متوازی الاضلاع آدھا نہیں ہوتا۔ غلطی ترچھا ضلع ہے: 12 × 6 = 72"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "8 cm is the slanting side, not the height. 12 × 6 = 72 cm².", "8 ترچھا ضلع ہے، اونچائی نہیں۔ 12 × 6 = 72", "slant_height"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_para", "front": T("Area of a parallelogram?", "متوازی الاضلاع کا رقبہ؟"),
    "back": T("Base × perpendicular height. Base 9, height 5: 45 cm².", "قاعدہ × عمودی اونچائی۔ قاعدہ 9، اونچائی 5: 45 مربع سینٹی میٹر")},
   {"id": "f_trap", "front": T("Area of a trapezium?", "ذوزنقہ کا رقبہ؟"),
    "back": T("½ × (sum of the parallel sides) × height. Sides 6 and 10, height 4: 32 cm².", "½ × (متوازی اضلاع کا مجموعہ) × اونچائی۔ اضلاع 6 اور 10، اونچائی 4: 32 مربع سینٹی میٹر")},
 ],
 "home_tasks": [{"id": "h_cut", "text": T(
   "Draw a parallelogram on paper and measure its base and height. Cut a triangle off one end and stick it on the other end. Is it a rectangle now? Work out its area both ways.",
   "کاغذ پر ایک متوازی الاضلاع بنائیں اور اس کا قاعدہ اور اونچائی ناپیں۔ ایک سرے سے مثلث کاٹ کر دوسرے سرے پر لگائیں۔ کیا اب یہ مستطیل ہے؟ دونوں طریقوں سے رقبہ نکالیں۔")}],
 "glossary": [T("Parallelogram", "متوازی الاضلاع"), T("Trapezium", "ذوزنقہ"), T("Parallel sides", "متوازی اضلاع"),
              T("Base", "قاعدہ"), T("Height", "اونچائی (ارتفاع)"), T("Slanting side", "ترچھا ضلع")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "A parallelogram looks like a rectangle pushed sideways. Does pushing it change its area?",
                     "متوازی الاضلاع ایسی مستطیل لگتی ہے جسے ایک طرف دھکیل دیا گیا ہو۔ کیا دھکیلنے سے رقبہ بدلتا ہے؟"),
    "text": T("Today we find the area of a parallelogram and a trapezium, using rectangles and triangles. First, a quick check.",
              "آج ہم مستطیل اور مثلث کی مدد سے متوازی الاضلاع اور ذوزنقہ کا رقبہ نکالیں گے۔ پہلے ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("A triangle has a base of 10 cm and a height of 6 cm. What is its area in cm²?", "ایک مثلث کا قاعدہ 10 اور اونچائی 6 سینٹی میٹر ہے۔ اس کا رقبہ کیا ہے؟"),
     S2,
     T("½ × base × height.", "½ × قاعدہ × اونچائی"),
     T("Right! 30 cm².", "درست! 30 مربع سینٹی میٹر"),
     T("10 × 6 = 60, half is 30 cm².", "10 × 6 = 60، آدھا 30"),
     common_wrong=[wrong(60, "That is the rectangle. A triangle is half: 30.", "یہ مستطیل ہے۔ مثلث آدھا ہے: 30")],
     qtype="recall", skill=PA_TRIANGLE),
   {"id": "s3_shapes", "type": "explain",
    "character": say("happy", "Cut, move, and it's a rectangle!", "کاٹیں، کھسکائیں، اور مستطیل بن گئی!"),
    "text": T("A parallelogram has two pairs of parallel sides. Cut a triangle off one end and move it to the other end: it becomes a rectangle. So area of a parallelogram = base × height. A trapezium has one pair of parallel sides. Two copies, one turned upside down, fit together into a parallelogram whose base is the two parallel sides added. So area of a trapezium = ½ × (sum of the parallel sides) × height. The height always goes straight across between the parallel sides, at a right angle. It is not the slanting side.",
              "متوازی الاضلاع کے دو جوڑے متوازی اضلاع ہوتے ہیں۔ ایک سرے سے مثلث کاٹ کر دوسرے سرے پر لگائیں: یہ مستطیل بن جاتی ہے۔ اس لیے متوازی الاضلاع کا رقبہ = قاعدہ × اونچائی۔ ذوزنقہ کا ایک جوڑا متوازی اضلاع کا ہوتا ہے۔ اس کی دو کاپیاں، ایک الٹی کر کے، جوڑیں تو متوازی الاضلاع بنتا ہے جس کا قاعدہ دونوں متوازی اضلاع کا مجموعہ ہے۔ اس لیے ذوزنقہ کا رقبہ = ½ × (متوازی اضلاع کا مجموعہ) × اونچائی۔ اونچائی ہمیشہ متوازی اضلاع کے درمیان زاویہ قائمہ پر سیدھی ہوتی ہے۔ یہ ترچھا ضلع نہیں۔")},
   number_question(
     "s4_para",
     T("A parallelogram has a base of 9 cm, a height of 5 cm and slanting sides of 7 cm. What is its area in cm²?",
       "ایک متوازی الاضلاع کا قاعدہ 9، اونچائی 5 اور ترچھے اضلاع 7 سینٹی میٹر ہیں۔ اس کا رقبہ کیا ہے؟"),
     S4,
     T("Base × height. Use 5, not 7.", "قاعدہ × اونچائی۔ 5 لیں، 7 نہیں۔"),
     T("Right! 9 × 5 = 45 cm².", "درست! 9 × 5 = 45 مربع سینٹی میٹر"),
     T("9 × 5 = 45 cm². The 7 cm sides are not needed.", "9 × 5 = 45۔ 7 والے اضلاع نہیں چاہییں۔"),
     common_wrong=[wrong(63, "7 cm is the slanting side. Use the height: 9 × 5 = 45.", "7 ترچھا ضلع ہے۔ اونچائی لیں: 9 × 5 = 45", "slant_height"),
                   wrong(32, "32 cm is the perimeter. Area: 9 × 5 = 45.", "32 سینٹی میٹر احاطہ ہے۔ رقبہ: 9 × 5 = 45")]),
   number_question(
     "s5_missing_height",
     T("A parallelogram-shaped field has an area of 48 m² and a base of 8 m. What is its height in m?",
       "ایک متوازی الاضلاع شکل کے کھیت کا رقبہ 48 مربع میٹر اور قاعدہ 8 میٹر ہے۔ اس کی اونچائی کتنے میٹر ہے؟"),
     S5,
     T("Base × height = 48, so height = 48 ÷ 8.", "قاعدہ × اونچائی = 48، تو اونچائی = 48 ÷ 8"),
     T("Right! 6 m. Check: 8 × 6 = 48.", "درست! 6 میٹر۔ جانچ: 8 × 6 = 48"),
     T("48 ÷ 8 = 6 m.", "48 ÷ 8 = 6 میٹر"),
     common_wrong=[wrong(3, "Check: 8 × 3 = 24, not 48. A parallelogram has no ½: 48 ÷ 8 = 6.", "جانچیں: 8 × 3 = 24، نہ کہ 48۔ متوازی الاضلاع میں ½ نہیں: 48 ÷ 8 = 6")]),
   number_question(
     "s6_two_copies",
     T("Two copies of a trapezium with parallel sides of 6 cm and 10 cm are joined, one upside down, to make a parallelogram. What is the base of the parallelogram in cm?",
       "6 اور 10 سینٹی میٹر متوازی اضلاع والے ذوزنقہ کی دو کاپیاں، ایک الٹی کر کے، جوڑ کر متوازی الاضلاع بنایا گیا۔ اس متوازی الاضلاع کا قاعدہ کتنے سینٹی میٹر ہے؟"),
     S6,
     T("Along the bottom, the short side of one copy meets the long side of the other.", "نیچے ایک کاپی کا چھوٹا ضلع دوسری کے لمبے ضلع سے ملتا ہے۔"),
     T("Right! 6 + 10 = 16 cm. That is why we add the parallel sides.", "درست! 6 + 10 = 16۔ اسی لیے ہم متوازی اضلاع جمع کرتے ہیں۔"),
     T("The base is 6 + 10 = 16 cm.", "قاعدہ 6 + 10 = 16 سینٹی میٹر ہے۔"),
     common_wrong=[wrong(10, "The bottom has one side from each copy: 6 + 10 = 16.", "نیچے ہر کاپی کا ایک ضلع ہے: 6 + 10 = 16", "one_parallel_side"),
                   wrong(4, "Add, don't take away: 6 + 10 = 16.", "جمع کریں، تفریق نہیں: 6 + 10 = 16")]),
   number_question(
     "s7_trap",
     T("That trapezium has parallel sides of 6 cm and 10 cm, and a height of 4 cm. What is its area in cm²?",
       "اس ذوزنقہ کے متوازی اضلاع 6 اور 10 سینٹی میٹر ہیں، اور اونچائی 4 سینٹی میٹر۔ اس کا رقبہ کیا ہے؟"),
     S7,
     T("½ × (6 + 10) × 4.", "½ × (6 + 10) × 4"),
     T("Right! 16 × 4 = 64, half is 32 cm².", "درست! 16 × 4 = 64، آدھا 32 مربع سینٹی میٹر"),
     T("6 + 10 = 16, 16 × 4 = 64, half is 32 cm².", "6 + 10 = 16، 16 × 4 = 64، آدھا 32"),
     common_wrong=[wrong(64, "That is the whole parallelogram of two copies. One trapezium is half: 32.", "یہ دو کاپیوں کا پورا متوازی الاضلاع ہے۔ ایک ذوزنقہ آدھا ہے: 32", "trap_forgets_half"),
                   wrong(40, "Use both parallel sides: ½ × (6 + 10) × 4 = 32.", "دونوں متوازی اضلاع لیں: ½ × (6 + 10) × 4 = 32", "one_parallel_side")]),
   number_question(
     "s8_trap_slant",
     T("A trapezium-shaped garden has parallel sides of 5 m and 9 m, a height of 6 m, and slanting sides of 7 m. What is its area in m²?",
       "ایک ذوزنقہ شکل کے باغ کے متوازی اضلاع 5 اور 9 میٹر، اونچائی 6 میٹر اور ترچھے اضلاع 7 میٹر ہیں۔ اس کا رقبہ کتنے مربع میٹر ہے؟"),
     S8,
     T("½ × (5 + 9) × 6. The 7 m sides are not needed.", "½ × (5 + 9) × 6۔ 7 میٹر والے اضلاع نہیں چاہییں۔"),
     T("Right! 14 × 6 = 84, half is 42 m².", "درست! 14 × 6 = 84، آدھا 42 مربع میٹر"),
     T("5 + 9 = 14, 14 × 6 = 84, half is 42 m².", "5 + 9 = 14، 14 × 6 = 84، آدھا 42"),
     common_wrong=[wrong(84, "Halve it: 84 ÷ 2 = 42.", "آدھا کریں: 84 ÷ 2 = 42", "trap_forgets_half"),
                   wrong(49, "7 m is the slanting side. Use the height 6: ½ × 14 × 6 = 42.", "7 ترچھا ضلع ہے۔ اونچائی 6 لیں: ½ × 14 × 6 = 42", "slant_height")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Hina says a trapezium with parallel sides 8 cm and 12 cm and height 5 cm has an area of (8 + 12) × 5 = 100 cm². What went wrong?",
                "حنا کہتی ہے 8 اور 12 سینٹی میٹر متوازی اضلاع اور 5 اونچائی والے ذوزنقہ کا رقبہ (8 + 12) × 5 = 100 ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("half", "She forgot to halve. ½ × 20 × 5 = 50 cm².", "وہ آدھا کرنا بھول گئی۔ ½ × 20 × 5 = 50", True,
          "Yes! 100 is two trapeziums together; one is half.", "جی ہاں! 100 دو ذوزنقہ مل کر ہیں؛ ایک آدھا ہے۔"),
      opt("long_side", "She should use only the longer side: 12 × 5 = 60 cm².", "اسے صرف لمبا ضلع لینا چاہیے: 12 × 5 = 60", False,
          "Both parallel sides count. ½ × (8 + 12) × 5 = 50.", "دونوں متوازی اضلاع گنے جاتے ہیں۔ ½ × (8 + 12) × 5 = 50", "one_parallel_side"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "(8 + 12) × 5 is two trapeziums. Halve it: 50 cm².", "(8 + 12) × 5 دو ذوزنقہ ہیں۔ آدھا کریں: 50", "trap_forgets_half"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why is a parallelogram's area just base × height, like a rectangle? Can you teach me?",
                     "متوازی الاضلاع کا رقبہ مستطیل کی طرح صرف قاعدہ × اونچائی کیوں ہے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why is the area of a parallelogram base × height?",
              "اپنے الفاظ میں بتائیں: متوازی الاضلاع کا رقبہ قاعدہ × اونچائی کیوں ہوتا ہے؟"),
    "key_idea": "Cutting a triangle off one end and moving it to the other end turns the parallelogram into a rectangle with the same base and height, and nothing is lost or added.",
    "levels": {
      "got_it": "Explains cutting a triangle off one end and moving it to the other to make a rectangle of the same base and height, with the same area.",
      "partly": "Says it becomes a rectangle, without saying how or why the area stays the same.",
      "not_yet": "Gives no reason, or says it is just the rule."},
    "keywords": [
      ["rectangle", "مستطیل", "mustateel"],
      ["cut", "move", "triangle", "کاٹ", "مثلث", "کھسکا"],
      ["same", "height", "برابر", "وہی", "اونچائی"]],
    "fallback_feedback": {
      "got_it": T("Well explained! The cut triangle moves across and a rectangle appears, with the same area.", "بہت خوب! کٹا ہوا مثلث دوسری طرف جاتا ہے اور اتنے ہی رقبے کی مستطیل بن جاتی ہے۔"),
      "partly": T("Good start! Now say how it becomes a rectangle, and why the area stays the same.", "اچھی شروعات! اب بتائیں یہ مستطیل کیسے بنتی ہے، اور رقبہ وہی کیوں رہتا ہے۔"),
      "not_yet": T("Imagine cutting a triangle off one end of the parallelogram and sliding it to the other end. What shape do you get?", "سوچیں کہ متوازی الاضلاع کے ایک سرے سے مثلث کاٹ کر دوسرے سرے پر لگا دیں۔ کون سی شکل بنتی ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_tile",
     T("A floor tile is a parallelogram with a base of 15 cm, a height of 8 cm and slanting sides of 10 cm. What is its area in cm²?",
       "فرش کی ایک ٹائل متوازی الاضلاع ہے جس کا قاعدہ 15، اونچائی 8 اور ترچھے اضلاع 10 سینٹی میٹر ہیں۔ اس کا رقبہ کیا ہے؟"),
     S11,
     T("Base × height. Which number is the height?", "قاعدہ × اونچائی۔ اونچائی کون سا عدد ہے؟"),
     T("Right! 15 × 8 = 120 cm².", "درست! 15 × 8 = 120 مربع سینٹی میٹر"),
     T("15 × 8 = 120 cm². The 10 cm sides are slanting.", "15 × 8 = 120۔ 10 والے اضلاع ترچھے ہیں۔"),
     common_wrong=[wrong(150, "10 cm is the slanting side. Use the height: 15 × 8 = 120.", "10 ترچھا ضلع ہے۔ اونچائی لیں: 15 × 8 = 120", "slant_height"),
                   wrong(60, "A parallelogram is not halved: 15 × 8 = 120.", "متوازی الاضلاع آدھا نہیں ہوتا: 15 × 8 = 120")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Parallelograms and trapeziums done!", "متوازی الاضلاع اور ذوزنقہ مکمل!"),
    "text": T("Area of a parallelogram = base × height. Area of a trapezium = ½ × (sum of the parallel sides) × height. The height is straight across at a right angle; never use the slanting side. To find a missing height of a parallelogram, divide the area by the base.",
              "متوازی الاضلاع کا رقبہ = قاعدہ × اونچائی۔ ذوزنقہ کا رقبہ = ½ × (متوازی اضلاع کا مجموعہ) × اونچائی۔ اونچائی زاویہ قائمہ پر سیدھی ہوتی ہے؛ ترچھا ضلع کبھی نہ لیں۔ متوازی الاضلاع کی نامعلوم اونچائی کے لیے رقبے کو قاعدے سے تقسیم کریں۔"),
    "points": [T("A parallelogram is a rectangle with one triangle moved.", "متوازی الاضلاع ایک مستطیل ہے جس کا ایک مثلث کھسکا دیا گیا ہو۔"),
               T("A trapezium is half of a parallelogram: add both parallel sides, then halve.", "ذوزنقہ متوازی الاضلاع کا آدھا ہے: دونوں متوازی اضلاع جمع کریں، پھر آدھا کریں۔")]},
 ],
 "review_questions": [
   {"id": "r_para", "type": "apply", "skill": SKILL, "step": number_question(
     "r_para",
     T("Find the area of a parallelogram with base 11 m and height 4 m, in m².", "11 میٹر قاعدے اور 4 میٹر اونچائی والے متوازی الاضلاع کا رقبہ معلوم کریں۔"),
     R1,
     T("Base × height.", "قاعدہ × اونچائی"),
     T("Right! 44 m².", "درست! 44 مربع میٹر"),
     T("11 × 4 = 44 m².", "11 × 4 = 44"),
     common_wrong=[wrong(22, "A parallelogram is not halved: 11 × 4 = 44.", "متوازی الاضلاع آدھا نہیں ہوتا: 11 × 4 = 44")],
     qtype=None)},
   {"id": "r_trap", "type": "apply", "skill": SKILL, "step": number_question(
     "r_trap",
     T("Find the area of a trapezium with parallel sides 3 cm and 7 cm and height 8 cm, in cm².", "3 اور 7 سینٹی میٹر متوازی اضلاع اور 8 سینٹی میٹر اونچائی والے ذوزنقہ کا رقبہ معلوم کریں۔"),
     R2,
     T("½ × (3 + 7) × 8.", "½ × (3 + 7) × 8"),
     T("Right! 40 cm².", "درست! 40 مربع سینٹی میٹر"),
     T("3 + 7 = 10, 10 × 8 = 80, half is 40.", "3 + 7 = 10، 10 × 8 = 80، آدھا 40"),
     common_wrong=[wrong(80, "Halve it: 40.", "آدھا کریں: 40", "trap_forgets_half"),
                   wrong(56, "Use both parallel sides: ½ × (3 + 7) × 8 = 40.", "دونوں متوازی اضلاع لیں: ½ × (3 + 7) × 8 = 40", "one_parallel_side")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh to fill a gap in the Perimeter and Area unit. No textbook text or exercises were used.",
   "Lessons have no pictures, so every shape is described in words, giving the base, the height and the slanting side so the child must choose the height. Drawing the shapes on paper or cutting them out helps.",
   "The parallelogram is shown as a rectangle with a triangle moved from one end to the other; the trapezium as half of a parallelogram made from two copies (s6).",
   "Urdu terms to check: متوازی الاضلاع (parallelogram), ذوزنقہ (trapezium), متوازی اضلاع (parallel sides), قاعدہ (base), اونچائی / ارتفاع (height), ترچھا ضلع (slanting side), زاویہ قائمہ (right angle).",
   "The numbers were worked out in content/sources/g6-maths-08/parallelogram_trapezium.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)
