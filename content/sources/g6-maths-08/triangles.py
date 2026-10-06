from fractions import Fraction as F

from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, PA_AREA, PA_COMPOUND, PA_TRIANGLE)

SKILL = PA_TRIANGLE


def tri(base, height):
    a = F(base * height, 2)
    assert a.denominator == 1, (base, height)
    return int(a)


# s2
assert 8 * 6 == 48
# s4: right triangle 8 by 6 is half a rectangle
S4 = tri(8, 6)
assert S4 == 24 and 8 * 6 == 48 and 8 + 6 == 14
# s5
S5 = tri(10, 7)
assert S5 == 35 and 10 * 7 == 70
# s6: base 12, height 5, slanted side 13 (a 5-12-13 right triangle)
assert 5 ** 2 + 12 ** 2 == 13 ** 2
S6 = tri(12, 5)
assert S6 == 30 and tri(12, 13) == 78 and 12 * 5 == 60
# s7: area 24, base 8 -> height
S7 = 2 * 24 // 8
assert S7 == 6 and tri(8, S7) == 24 and 24 // 8 == 3
# s8: kite of two triangles, each base 10 height 4
S8 = 2 * tri(10, 4)
assert S8 == 40 and tri(10, 4) == 20
# s9: base 6 height 4
assert tri(6, 4) == 12 and 6 * 4 == 24
# s11: house = 6 by 4 wall + roof triangle base 6 height 3
S11 = 6 * 4 + tri(6, 3)
assert S11 == 33 and tri(6, 3) == 9 and 6 * 4 + 6 * 3 == 42
# question bank and review
QB = tri(9, 4)
assert QB == 18 and 9 * 4 == 36
R1 = tri(14, 3)
assert R1 == 21 and 14 * 3 == 42
R2 = tri(5, 6)
assert R2 == 15 and 5 * 6 == 30


lesson = {
 "id": "g6-maths-08-area-of-triangles",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Find the area of a triangle as half of base × height, using the perpendicular height.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Area of triangles", "مثلث کا رقبہ"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": PA_AREA}, {"skill": PA_COMPOUND}],
 "misconceptions": [
   {"id": "forgets_half", "description": "Multiplies base by height and forgets to halve."},
   {"id": "slant_height", "description": "Uses the slanted side instead of the perpendicular height."},
   {"id": "missing_height_no_double", "description": "Finds a missing height by area ÷ base, forgetting to double the area first."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_formula", "type": "recall", "step": {
     "id": "qb_formula", "type": "choice",
     "prompt": T("What is the area of a triangle?", "مثلث کا رقبہ کیا ہوتا ہے؟"),
     "options": [
       opt("half", "Half of base × height", "قاعدہ × اونچائی کا آدھا", True, "Yes! A triangle is half of a rectangle.", "جی ہاں! مثلث مستطیل کا آدھا ہے۔"),
       opt("full", "Base × height", "قاعدہ × اونچائی", False, "That is the whole rectangle. A triangle is half of it.", "یہ پوری مستطیل ہے۔ مثلث اس کا آدھا ہے۔", "forgets_half"),
       opt("sides", "All three sides added", "تینوں اضلاع کا مجموعہ", False, "That is the perimeter. Area: half of base × height.", "یہ احاطہ ہے۔ رقبہ: قاعدہ × اونچائی کا آدھا۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("A triangle has a base of 9 cm and a height of 4 cm. What is its area in cm²?", "ایک مثلث کا قاعدہ 9 سینٹی میٹر اور اونچائی 4 سینٹی میٹر ہے۔ اس کا رقبہ کیا ہے؟"),
     QB,
     T("9 × 4, then halve.", "9 × 4، پھر آدھا۔"),
     T("Right! 18 cm².", "درست! 18 مربع سینٹی میٹر"),
     T("9 × 4 = 36, half is 18 cm².", "9 × 4 = 36، آدھا 18"),
     common_wrong=[wrong(36, "Don't forget to halve: 36 ÷ 2 = 18.", "آدھا کرنا نہ بھولیں: 36 ÷ 2 = 18", "forgets_half")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("A triangle has base 12 cm, height 5 cm and a slanted side of 13 cm. Saad says its area is ½ × 12 × 13 = 78 cm². What went wrong?", "ایک مثلث کا قاعدہ 12، اونچائی 5 اور ترچھا ضلع 13 سینٹی میٹر ہے۔ سعد کہتا ہے رقبہ ½ × 12 × 13 = 78 ہے۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("height", "He used the slanted side. Use the height: ½ × 12 × 5 = 30 cm².", "اس نے ترچھا ضلع لیا۔ اونچائی لیں: ½ × 12 × 5 = 30", True,
           "Yes! The height goes straight up from the base, at a right angle.", "جی ہاں! اونچائی قاعدے سے سیدھی اوپر، زاویہ قائمہ پر جاتی ہے۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "The slanted side isn't the height. ½ × 12 × 5 = 30 cm².", "ترچھا ضلع اونچائی نہیں۔ ½ × 12 × 5 = 30", "slant_height"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_tri", "front": T("Area of a triangle?", "مثلث کا رقبہ؟"),
    "back": T("½ × base × height. Base 8, height 6: 24 cm².", "½ × قاعدہ × اونچائی۔ قاعدہ 8، اونچائی 6: 24 مربع سینٹی میٹر")},
   {"id": "f_height", "front": T("What is the height of a triangle?", "مثلث کی اونچائی کیا ہے؟"),
    "back": T("The straight-up distance from the base to the top corner, at a right angle to the base. Not the slanted side.", "قاعدے سے اوپر کے کونے تک سیدھا فاصلہ، قاعدے پر زاویہ قائمہ بناتا ہوا۔ ترچھا ضلع نہیں۔")},
 ],
 "home_tasks": [{"id": "h_fold", "text": T(
   "Take a rectangular piece of paper and measure it. Fold or cut it along a diagonal. Are the two triangles the same? Work out the area of one triangle.",
   "مستطیل کاغذ لیں اور ناپیں۔ اسے ترچھی لکیر (وتر) پر موڑیں یا کاٹیں۔ کیا دونوں مثلث ایک جیسے ہیں؟ ایک مثلث کا رقبہ نکالیں۔")}],
 "glossary": [T("Triangle", "مثلث"), T("Base", "قاعدہ"), T("Height", "اونچائی"), T("Right angle", "زاویہ قائمہ")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Cut a rectangle corner to corner. What do you get? Two triangles! So what is the area of one?",
                     "مستطیل کو ایک کونے سے دوسرے کونے تک کاٹیں۔ کیا ملا؟ دو مثلث! تو ایک کا رقبہ کیا ہوگا؟"),
    "text": T("Today we find the area of triangles using what we know about rectangles. First, a quick check.", "آج ہم مستطیل کی مدد سے مثلث کا رقبہ نکالیں گے۔ پہلے ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("What is the area of a rectangle 8 cm by 6 cm, in cm²?", "8 ضرب 6 سینٹی میٹر مستطیل کا رقبہ کیا ہے؟"),
     48,
     T("Length × width.", "لمبائی × چوڑائی"),
     T("Right! 48 cm².", "درست! 48 مربع سینٹی میٹر"),
     T("8 × 6 = 48 cm².", "8 × 6 = 48"),
     common_wrong=[wrong(28, "28 cm is the perimeter. Area: 8 × 6 = 48.", "28 سینٹی میٹر احاطہ ہے۔ رقبہ: 8 × 6 = 48")],
     qtype="recall", skill=PA_AREA),
   {"id": "s3_half", "type": "explain",
    "character": say("happy", "A triangle is half a rectangle!", "مثلث آدھی مستطیل ہے!"),
    "text": T("Cutting an 8 cm by 6 cm rectangle corner to corner makes two equal triangles. Each is half of 48 cm². So the area of a triangle = ½ × base × height. The height must go straight up from the base, at a right angle, to the top corner. It is not the slanted side.",
              "8 ضرب 6 سینٹی میٹر کی مستطیل کو کونے سے کونے تک کاٹنے سے دو برابر مثلث بنتے ہیں۔ ہر ایک 48 کا آدھا ہے۔ اس لیے مثلث کا رقبہ = ½ × قاعدہ × اونچائی۔ اونچائی قاعدے سے سیدھی اوپر، زاویہ قائمہ پر، اوپر کے کونے تک جاتی ہے۔ یہ ترچھا ضلع نہیں۔")},
   number_question(
     "s4_half_rect",
     T("So what is the area of one of those triangles, with base 8 cm and height 6 cm?", "تو ان میں سے ایک مثلث کا رقبہ کیا ہے، جس کا قاعدہ 8 اور اونچائی 6 سینٹی میٹر ہے؟"),
     S4,
     T("Half of 8 × 6.", "8 × 6 کا آدھا"),
     T("Right! 24 cm².", "درست! 24 مربع سینٹی میٹر"),
     T("8 × 6 = 48, half is 24 cm².", "8 × 6 = 48، آدھا 24"),
     common_wrong=[wrong(48, "That is the whole rectangle. One triangle is half: 24.", "یہ پوری مستطیل ہے۔ ایک مثلث آدھا ہے: 24", "forgets_half"),
                   wrong(14, "Multiply, then halve: 8 × 6 ÷ 2 = 24.", "ضرب دیں، پھر آدھا: 8 × 6 ÷ 2 = 24")]),
   number_question(
     "s5_any",
     T("A triangle has a base of 10 cm and a height of 7 cm. What is its area in cm²?", "ایک مثلث کا قاعدہ 10 اور اونچائی 7 سینٹی میٹر ہے۔ رقبہ کیا ہے؟"),
     S5,
     T("½ × 10 × 7.", "½ × 10 × 7"),
     T("Right! 35 cm².", "درست! 35 مربع سینٹی میٹر"),
     T("10 × 7 = 70, half is 35 cm².", "10 × 7 = 70، آدھا 35"),
     common_wrong=[wrong(70, "Don't forget to halve: 70 ÷ 2 = 35.", "آدھا کرنا نہ بھولیں: 70 ÷ 2 = 35", "forgets_half")]),
   number_question(
     "s6_slant",
     T("A triangle has a base of 12 cm, a height of 5 cm, and a slanted side of 13 cm. What is its area in cm²?", "ایک مثلث کا قاعدہ 12، اونچائی 5 اور ترچھا ضلع 13 سینٹی میٹر ہے۔ رقبہ کیا ہے؟"),
     S6,
     T("Use the height (5), not the slanted side.", "اونچائی (5) لیں، ترچھا ضلع نہیں۔"),
     T("Right! ½ × 12 × 5 = 30 cm².", "درست! ½ × 12 × 5 = 30"),
     T("12 × 5 = 60, half is 30 cm². The 13 cm side isn't needed.", "12 × 5 = 60، آدھا 30۔ 13 والا ضلع نہیں چاہیے۔"),
     common_wrong=[wrong(78, "13 cm is the slanted side. Use the height: ½ × 12 × 5 = 30.", "13 ترچھا ضلع ہے۔ اونچائی لیں: ½ × 12 × 5 = 30", "slant_height"),
                   wrong(60, "Halve it: 60 ÷ 2 = 30.", "آدھا کریں: 60 ÷ 2 = 30", "forgets_half")]),
   number_question(
     "s7_missing_height",
     T("A triangle has an area of 24 cm² and a base of 8 cm. What is its height?", "ایک مثلث کا رقبہ 24 مربع سینٹی میٹر اور قاعدہ 8 سینٹی میٹر ہے۔ اونچائی کتنی ہے؟"),
     S7,
     T("Base × height is double the area: 48. Then 48 ÷ 8.", "قاعدہ × اونچائی رقبے کا دگنا ہے: 48۔ پھر 48 ÷ 8"),
     T("Right! 6 cm. Check: ½ × 8 × 6 = 24.", "درست! 6 سینٹی میٹر۔ جانچ: ½ × 8 × 6 = 24"),
     T("24 × 2 = 48, and 48 ÷ 8 = 6 cm.", "24 × 2 = 48، اور 48 ÷ 8 = 6"),
     common_wrong=[wrong(3, "Check: ½ × 8 × 3 = 12, not 24. Double the area first: 48 ÷ 8 = 6.", "جانچیں: ½ × 8 × 3 = 12، نہ کہ 24۔ پہلے رقبہ دگنا کریں: 48 ÷ 8 = 6", "missing_height_no_double")]),
   number_question(
     "s8_kite",
     T("A kite is made of two equal triangles, each with a base of 10 cm and a height of 4 cm. What is the area of the kite in cm²?", "ایک پتنگ دو برابر مثلثوں سے بنی ہے، ہر ایک کا قاعدہ 10 اور اونچائی 4 سینٹی میٹر۔ پتنگ کا رقبہ کیا ہے؟"),
     S8,
     T("One triangle is ½ × 10 × 4. There are two.", "ایک مثلث ½ × 10 × 4۔ دو ہیں۔"),
     T("Right! 20 + 20 = 40 cm².", "درست! 20 + 20 = 40 مربع سینٹی میٹر"),
     T("Each triangle is 20 cm², so the kite is 40 cm².", "ہر مثلث 20، تو پتنگ 40 مربع سینٹی میٹر"),
     common_wrong=[wrong(20, "That is one triangle. The kite has two: 40.", "یہ ایک مثلث ہے۔ پتنگ میں دو ہیں: 40"),
                   wrong(80, "Each triangle is half of 10 × 4 = 20. Two make 40.", "ہر مثلث 10 × 4 کا آدھا = 20۔ دو مل کر 40", "forgets_half")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Asad says a triangle with base 6 cm and height 4 cm has an area of 24 cm². What went wrong?", "اسد کہتا ہے 6 قاعدے اور 4 اونچائی والے مثلث کا رقبہ 24 مربع سینٹی میٹر ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("half", "He forgot to halve. ½ × 6 × 4 = 12 cm².", "وہ آدھا کرنا بھول گیا۔ ½ × 6 × 4 = 12", True,
          "Yes! 24 is the whole rectangle; the triangle is half.", "جی ہاں! 24 پوری مستطیل ہے؛ مثلث آدھا ہے۔"),
      opt("ten", "It should be 10 cm².", "یہ 10 ہونا چاہیے۔", False,
          "10 is 6 + 4. Area: ½ × 6 × 4 = 12.", "10 یعنی 6 + 4۔ رقبہ: ½ × 6 × 4 = 12"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "6 × 4 is the rectangle. A triangle is half of it: 12 cm².", "6 × 4 مستطیل ہے۔ مثلث اس کا آدھا: 12", "forgets_half"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why is there a ½ in the triangle area formula? Can you teach me?",
                     "مثلث کے رقبے کے قاعدے میں ½ کیوں ہے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why is the area of a triangle half of base × height?",
              "اپنے الفاظ میں بتائیں: مثلث کا رقبہ قاعدہ × اونچائی کا آدھا کیوں ہوتا ہے؟"),
    "key_idea": "Base × height is the area of a rectangle around the triangle. A diagonal cuts that rectangle into two equal triangles, so one triangle is half of it.",
    "levels": {
      "got_it": "Explains that base × height is a rectangle, and the triangle is half of it because two equal triangles make the rectangle.",
      "partly": "Says the triangle is half a rectangle, without saying why or which rectangle.",
      "not_yet": "Gives no reason, or says the ½ is just part of the rule."},
    "keywords": [
      ["rectangle", "مستطیل", "mustateel"],
      ["half", "two", "آدھا", "دو", "aadha"],
      ["diagonal", "cut", "corner", "کاٹ", "کونے", "وتر"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Two equal triangles make the rectangle, so one is half.", "بہت خوب! دو برابر مثلث مل کر مستطیل بناتے ہیں، اس لیے ایک آدھا ہے۔"),
      "partly": T("Good start! Now say which rectangle, and why exactly half.", "اچھی شروعات! اب بتائیں کون سی مستطیل، اور بالکل آدھا کیوں۔"),
      "not_yet": T("Remember cutting the rectangle corner to corner. How many triangles did you get? Were they the same?", "مستطیل کو کونے سے کونے تک کاٹنا یاد کریں۔ کتنے مثلث بنے؟ کیا وہ ایک جیسے تھے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_house",
     T("A drawing of a house is a 6 cm by 4 cm rectangle with a triangle roof on top: base 6 cm, height 3 cm. What is the total area in cm²?", "گھر کی تصویر 6 ضرب 4 سینٹی میٹر کی مستطیل اور اوپر مثلث چھت سے بنی ہے: قاعدہ 6، اونچائی 3 سینٹی میٹر۔ کل رقبہ کیا ہے؟"),
     S11,
     T("Rectangle 6 × 4, plus triangle ½ × 6 × 3.", "مستطیل 6 × 4، جمع مثلث ½ × 6 × 3"),
     T("Right! 24 + 9 = 33 cm².", "درست! 24 + 9 = 33 مربع سینٹی میٹر"),
     T("6 × 4 = 24 and ½ × 6 × 3 = 9, so 33 cm².", "6 × 4 = 24 اور ½ × 6 × 3 = 9، تو 33"),
     common_wrong=[wrong(42, "Halve the roof: ½ × 6 × 3 = 9, so 24 + 9 = 33.", "چھت آدھی کریں: ½ × 6 × 3 = 9، تو 24 + 9 = 33", "forgets_half"),
                   wrong(24, "Add the roof too: 24 + 9 = 33.", "چھت بھی جمع کریں: 24 + 9 = 33")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Triangles done!", "مثلث مکمل!"),
    "text": T("Area of a triangle = ½ × base × height. The height goes straight up from the base at a right angle; never use the slanted side. To find a missing height, double the area and divide by the base.",
              "مثلث کا رقبہ = ½ × قاعدہ × اونچائی۔ اونچائی قاعدے سے زاویہ قائمہ پر سیدھی اوپر جاتی ہے؛ ترچھا ضلع کبھی نہ لیں۔ نامعلوم اونچائی کے لیے رقبہ دگنا کر کے قاعدے سے تقسیم کریں۔"),
    "points": [T("A triangle is half a rectangle.", "مثلث آدھی مستطیل ہے۔"),
               T("Don't forget the ½.", "½ نہ بھولیں۔")]},
 ],
 "review_questions": [
   {"id": "r_tri", "type": "apply", "skill": SKILL, "step": number_question(
     "r_tri",
     T("Find the area of a triangle with base 14 cm and height 3 cm, in cm².", "14 قاعدے اور 3 اونچائی والے مثلث کا رقبہ معلوم کریں۔"),
     R1,
     T("½ × 14 × 3.", "½ × 14 × 3"),
     T("Right! 21 cm².", "درست! 21 مربع سینٹی میٹر"),
     T("14 × 3 = 42, half is 21.", "14 × 3 = 42، آدھا 21"),
     common_wrong=[wrong(42, "Halve it: 21.", "آدھا کریں: 21", "forgets_half")],
     qtype=None)},
   {"id": "r_tri2", "type": "recall", "skill": SKILL, "step": number_question(
     "r_tri2",
     T("Find the area of a triangle with base 5 m and height 6 m, in m².", "5 میٹر قاعدے اور 6 میٹر اونچائی والے مثلث کا رقبہ معلوم کریں۔"),
     R2,
     T("½ × 5 × 6.", "½ × 5 × 6"),
     T("Right! 15 m².", "درست! 15 مربع میٹر"),
     T("5 × 6 = 30, half is 15.", "5 × 6 = 30، آدھا 15"),
     common_wrong=[wrong(30, "Halve it: 15.", "آدھا کریں: 15", "forgets_half")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Perimeter and Area unit. No textbook text or exercises were used.",
   "The formula is shown as half of a rectangle; cutting a paper rectangle along a diagonal makes it concrete. The 5-12-13 triangle in s6 checks that children use the height, not the slanted side.",
   "Urdu terms to check: مثلث (triangle), قاعدہ (base), اونچائی (height), زاویہ قائمہ (right angle).",
   "The numbers were worked out in content/sources/g6-maths-08/triangles.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)
