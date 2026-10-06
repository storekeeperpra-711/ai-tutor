from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, TIMES_TABLES, PA_PERIMETER)

SKILL = PA_PERIMETER


def rect_p(length, width):
    return 2 * (length + width)


# s2
assert 7 * 4 == 28
# s4: garden 8 by 5
S4 = rect_p(8, 5)
assert S4 == 26 == 8 + 5 + 8 + 5 and 8 + 5 == 13 and 8 * 5 == 40
# s5: square side 7
S5 = 4 * 7
assert S5 == 28 and 7 * 7 == 49
# s6: triangle 5, 6, 9
S6 = 5 + 6 + 9
assert S6 == 20
# s7: regular hexagon side 4
S7 = 6 * 4
assert S7 == 24 and 4 * 4 == 16
# s8: perimeter 30, length 9: width?
S8 = 30 // 2 - 9
assert S8 == 6 and rect_p(9, S8) == 30 and 30 - 9 == 21
# s9: 6 by 4
assert rect_p(6, 4) == 20 and 6 + 4 == 10
# s11: square with perimeter 36
S11 = 36 // 4
assert S11 == 9 and 4 * S11 == 36 and 36 - 4 == 32
# question bank and review
QB = rect_p(12, 3)
assert QB == 30 and 12 + 3 == 15 and 12 * 3 == 36
assert 4 * 5 == 20 and 5 * 5 == 25
R1 = rect_p(10, 4)
assert R1 == 28 and 10 * 4 == 40
R2 = 4 * 6
assert R2 == 24 and 6 * 6 == 36


lesson = {
 "id": "g6-maths-08-perimeter",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Find the perimeter of rectangles, squares and other polygons, and a missing side from the perimeter.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Perimeter", "احاطہ"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": TIMES_TABLES}],
 "misconceptions": [
   {"id": "two_sides_only", "description": "Adds only the two sides given (length + width) instead of all four."},
   {"id": "area_for_perimeter", "description": "Multiplies length by width (the area) when the perimeter is asked."},
   {"id": "missing_side_subtract", "description": "Finds a missing side by taking one side from the whole perimeter, forgetting there are two of each."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_meaning", "type": "recall", "step": {
     "id": "qb_meaning", "type": "choice",
     "prompt": T("What is the perimeter of a shape?", "کسی شکل کا احاطہ کیا ہوتا ہے؟"),
     "options": [
       opt("around", "The distance all the way around its edge.", "اس کے کنارے کے گرد پورا فاصلہ۔", True, "Yes! Add up the lengths of all the sides.", "جی ہاں! تمام اضلاع کی لمبائیاں جمع کریں۔"),
       opt("inside", "The space inside it.", "اس کے اندر کی جگہ۔", False, "That is the area. Perimeter is the distance around.", "یہ رقبہ ہے۔ احاطہ گرد کا فاصلہ ہے۔", "area_for_perimeter"),
       opt("long", "Its longest side.", "اس کا سب سے لمبا ضلع۔", False, "Perimeter uses every side, all the way around.", "احاطے میں ہر ضلع آتا ہے، پورے گرد۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("Find the perimeter of a rectangle 12 cm long and 3 cm wide.", "12 سینٹی میٹر لمبی اور 3 سینٹی میٹر چوڑی مستطیل کا احاطہ معلوم کریں۔"),
     QB,
     T("Add all four sides: 12 + 3 + 12 + 3.", "چاروں اضلاع جمع کریں: 12 + 3 + 12 + 3"),
     T("Right! 30 cm.", "درست! 30 سینٹی میٹر"),
     T("2 × (12 + 3) = 2 × 15 = 30 cm.", "2 × (12 + 3) = 2 × 15 = 30 سینٹی میٹر"),
     common_wrong=[wrong(15, "That is two sides. A rectangle has four: 30 cm.", "یہ دو اضلاع ہیں۔ مستطیل کے چار ہیں: 30 سینٹی میٹر", "two_sides_only"),
                   wrong(36, "12 × 3 is the area. Perimeter adds the sides: 30 cm.", "12 × 3 رقبہ ہے۔ احاطے میں اضلاع جمع ہوتے ہیں: 30 سینٹی میٹر", "area_for_perimeter")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Maryam says a square with 5 cm sides has a perimeter of 25 cm. What went wrong?", "مریم کہتی ہے 5 سینٹی میٹر ضلع والے مربع کا احاطہ 25 سینٹی میٹر ہے۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("area", "She found the area. Perimeter = 4 × 5 = 20 cm.", "اس نے رقبہ نکالا۔ احاطہ = 4 × 5 = 20 سینٹی میٹر", True,
           "Yes! 5 × 5 is the area. Around the edge is 5 + 5 + 5 + 5 = 20.", "جی ہاں! 5 × 5 رقبہ ہے۔ کنارے کے گرد 5 + 5 + 5 + 5 = 20"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "Add the four sides: 5 + 5 + 5 + 5 = 20 cm. 25 is the area.", "چاروں اضلاع جمع کریں: 5 + 5 + 5 + 5 = 20 سینٹی میٹر۔ 25 رقبہ ہے۔", "area_for_perimeter"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_rect", "front": T("Perimeter of a rectangle?", "مستطیل کا احاطہ؟"),
    "back": T("Add all four sides, or 2 × (length + width). 8 m by 5 m: 26 m.", "چاروں اضلاع جمع کریں، یا 2 × (لمبائی + چوڑائی)۔ 8 میٹر ضرب 5 میٹر: 26 میٹر")},
   {"id": "f_square", "front": T("Perimeter of a square?", "مربع کا احاطہ؟"),
    "back": T("4 × side. Side 7 cm: 28 cm.", "4 × ضلع۔ ضلع 7 سینٹی میٹر: 28 سینٹی میٹر")},
 ],
 "home_tasks": [{"id": "h_measure", "text": T(
   "With a ruler or a piece of string, measure the sides of a book, a table top and a door. Work out the perimeter of each. Which is the biggest?",
   "فٹے یا دھاگے سے کسی کتاب، میز کی سطح اور دروازے کے اضلاع ناپیں۔ ہر ایک کا احاطہ نکالیں۔ سب سے بڑا کون سا ہے؟")}],
 "glossary": [T("Perimeter", "احاطہ"), T("Rectangle", "مستطیل"), T("Square", "مربع")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Dada's vegetable garden is 8 m long and 5 m wide. How much fence does he need to go all the way round?",
                     "دادا کا سبزیوں کا باغیچہ 8 میٹر لمبا اور 5 میٹر چوڑا ہے۔ چاروں طرف باڑ کے لیے کتنی تار چاہیے؟"),
    "text": T("The distance around a shape is called its perimeter. First, a quick times-table check.", "کسی شکل کے گرد کے فاصلے کو اس کا احاطہ کہتے ہیں۔ پہلے پہاڑے کا ایک سوال۔")},
   number_question(
     "s2_foundation",
     T("What is 7 × 4?", "7 × 4 کتنا ہے؟"),
     28,
     T("Four sevens: 7, 14, 21 ...", "چار دفعہ سات: 7، 14، 21 ..."),
     T("Right! 28.", "درست! 28"),
     T("7 × 4 = 28.", "7 × 4 = 28"),
     common_wrong=[wrong(11, "That is 7 + 4. Multiply: 28.", "یہ 7 + 4 ہے۔ ضرب دیں: 28")],
     qtype="recall", skill=TIMES_TABLES),
   {"id": "s3_around", "type": "explain",
    "character": say("happy", "Walk all the way round and add every side!", "پورا چکر لگائیں اور ہر ضلع جمع کریں!"),
    "text": T("Perimeter = the lengths of all the sides added together. A rectangle has two lengths and two widths, so perimeter = length + width + length + width = 2 × (length + width). A square has four equal sides, so perimeter = 4 × side.",
              "احاطہ = تمام اضلاع کی لمبائیوں کا مجموعہ۔ مستطیل کی دو لمبائیاں اور دو چوڑائیاں ہوتی ہیں، اس لیے احاطہ = لمبائی + چوڑائی + لمبائی + چوڑائی = 2 × (لمبائی + چوڑائی)۔ مربع کے چار برابر اضلاع ہیں، اس لیے احاطہ = 4 × ضلع۔")},
   number_question(
     "s4_garden",
     T("Dada's garden is 8 m long and 5 m wide. How many metres of fence go all the way round?", "دادا کا باغیچہ 8 میٹر لمبا اور 5 میٹر چوڑا ہے۔ چاروں طرف کتنے میٹر باڑ لگے گی؟"),
     S4,
     T("8 + 5 + 8 + 5.", "8 + 5 + 8 + 5"),
     T("Right! 26 m of fence.", "درست! 26 میٹر باڑ"),
     T("2 × (8 + 5) = 2 × 13 = 26 m.", "2 × (8 + 5) = 2 × 13 = 26 میٹر"),
     common_wrong=[wrong(13, "That covers only two sides. Go all the way round: 26 m.", "یہ صرف دو اضلاع ہیں۔ پورا چکر: 26 میٹر", "two_sides_only"),
                   wrong(40, "8 × 5 is the area. Fence goes around: 26 m.", "8 × 5 رقبہ ہے۔ باڑ گرد لگتی ہے: 26 میٹر", "area_for_perimeter")]),
   number_question(
     "s5_square",
     T("A square tile has sides of 7 cm. What is its perimeter?", "ایک مربع ٹائل کا ہر ضلع 7 سینٹی میٹر ہے۔ اس کا احاطہ کیا ہے؟"),
     S5,
     T("Four equal sides: 4 × 7.", "چار برابر اضلاع: 4 × 7"),
     T("Right! 28 cm.", "درست! 28 سینٹی میٹر"),
     T("4 × 7 = 28 cm.", "4 × 7 = 28 سینٹی میٹر"),
     common_wrong=[wrong(49, "7 × 7 is the area. Perimeter: 4 × 7 = 28 cm.", "7 × 7 رقبہ ہے۔ احاطہ: 4 × 7 = 28 سینٹی میٹر", "area_for_perimeter"),
                   wrong(14, "A square has four sides, not two: 28 cm.", "مربع کے دو نہیں، چار اضلاع ہیں: 28 سینٹی میٹر", "two_sides_only")]),
   number_question(
     "s6_triangle",
     T("A triangle has sides of 5 cm, 6 cm and 9 cm. What is its perimeter?", "ایک مثلث کے اضلاع 5، 6 اور 9 سینٹی میٹر ہیں۔ اس کا احاطہ کیا ہے؟"),
     S6,
     T("Add the three sides.", "تینوں اضلاع جمع کریں۔"),
     T("Right! 20 cm.", "درست! 20 سینٹی میٹر"),
     T("5 + 6 + 9 = 20 cm.", "5 + 6 + 9 = 20 سینٹی میٹر"),
     common_wrong=[wrong(270, "Perimeter adds, it doesn't multiply: 5 + 6 + 9 = 20.", "احاطے میں ضرب نہیں، جمع: 5 + 6 + 9 = 20")]),
   number_question(
     "s7_hexagon",
     T("A regular hexagon has 6 equal sides of 4 cm. What is its perimeter?", "ایک باقاعدہ مسدس کے 6 برابر اضلاع 4 سینٹی میٹر کے ہیں۔ اس کا احاطہ کیا ہے؟"),
     S7,
     T("6 sides of 4 cm: 6 × 4.", "4 سینٹی میٹر کے 6 اضلاع: 6 × 4"),
     T("Right! 24 cm.", "درست! 24 سینٹی میٹر"),
     T("6 × 4 = 24 cm.", "6 × 4 = 24 سینٹی میٹر"),
     common_wrong=[wrong(16, "A hexagon has 6 sides, not 4: 6 × 4 = 24.", "مسدس کے 4 نہیں، 6 اضلاع ہیں: 6 × 4 = 24")]),
   number_question(
     "s8_missing",
     T("A rectangle has a perimeter of 30 cm. Its length is 9 cm. How wide is it?", "ایک مستطیل کا احاطہ 30 سینٹی میٹر ہے۔ اس کی لمبائی 9 سینٹی میٹر ہے۔ چوڑائی کتنی ہے؟"),
     S8,
     T("Half the perimeter is one length + one width: 15 cm.", "آدھا احاطہ = ایک لمبائی + ایک چوڑائی: 15 سینٹی میٹر"),
     T("Right! 6 cm. Check: 9 + 6 + 9 + 6 = 30.", "درست! 6 سینٹی میٹر۔ جانچ: 9 + 6 + 9 + 6 = 30"),
     T("30 ÷ 2 = 15, and 15 − 9 = 6 cm.", "30 ÷ 2 = 15، اور 15 − 9 = 6 سینٹی میٹر"),
     common_wrong=[wrong(21, "There are two lengths: 30 ÷ 2 = 15, then 15 − 9 = 6.", "دو لمبائیاں ہیں: 30 ÷ 2 = 15، پھر 15 − 9 = 6", "missing_side_subtract"),
                   wrong(12, "Take away both lengths: 30 − 9 − 9 = 12 is two widths. One width: 6.", "دونوں لمبائیاں گھٹائیں: 30 − 9 − 9 = 12 دو چوڑائیاں ہیں۔ ایک چوڑائی: 6")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Ayan says a rectangle 6 cm by 4 cm has a perimeter of 10 cm. What went wrong?", "ایان کہتا ہے 6 ضرب 4 سینٹی میٹر کی مستطیل کا احاطہ 10 سینٹی میٹر ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("two", "He added only two sides. All four: 20 cm.", "اس نے صرف دو اضلاع جمع کیے۔ چاروں: 20 سینٹی میٹر", True,
          "Yes! 6 + 4 + 6 + 4 = 20.", "جی ہاں! 6 + 4 + 6 + 4 = 20"),
      opt("area", "It should be 24 cm, 6 × 4.", "یہ 24 سینٹی میٹر ہونا چاہیے، 6 × 4", False,
          "6 × 4 is the area. Perimeter: 6 + 4 + 6 + 4 = 20.", "6 × 4 رقبہ ہے۔ احاطہ: 6 + 4 + 6 + 4 = 20", "area_for_perimeter"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "A rectangle has four sides: 6 + 4 + 6 + 4 = 20 cm.", "مستطیل کے چار اضلاع ہیں: 6 + 4 + 6 + 4 = 20 سینٹی میٹر", "two_sides_only"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why is a rectangle's perimeter 2 × (length + width)? Can you teach me?",
                     "مستطیل کا احاطہ 2 × (لمبائی + چوڑائی) کیوں ہوتا ہے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why can we find a rectangle's perimeter with 2 × (length + width)?",
              "اپنے الفاظ میں بتائیں: مستطیل کا احاطہ 2 × (لمبائی + چوڑائی) سے کیوں نکل آتا ہے؟"),
    "key_idea": "A rectangle has two equal lengths and two equal widths. Going round once means one length + one width, twice. So perimeter = 2 × (length + width).",
    "levels": {
      "got_it": "Explains that opposite sides are equal, so there are two lengths and two widths, which is 2 × (length + width).",
      "partly": "Says you add the sides, without explaining where the 2 comes from.",
      "not_yet": "Confuses it with area, or gives no reason."},
    "keywords": [
      ["two", "twice", "دو", "do"],
      ["opposite", "equal", "same", "برابر", "آمنے سامنے"],
      ["length", "width", "لمبائی", "چوڑائی"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Two lengths and two widths make 2 × (length + width).", "بہت خوب! دو لمبائیاں اور دو چوڑائیاں مل کر 2 × (لمبائی + چوڑائی)۔"),
      "partly": T("Good start! Now say why we multiply by 2: how many lengths does a rectangle have?", "اچھی شروعات! اب بتائیں 2 سے ضرب کیوں: مستطیل کی کتنی لمبائیاں ہیں؟"),
      "not_yet": T("Walk round Dada's garden: 8, 5, 8, 5. Which numbers repeat?", "دادا کے باغیچے کا چکر لگائیں: 8، 5، 8، 5۔ کون سے اعداد دہرائے گئے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_square_side",
     T("A square has a perimeter of 36 cm. How long is each side?", "ایک مربع کا احاطہ 36 سینٹی میٹر ہے۔ ہر ضلع کتنا لمبا ہے؟"),
     S11,
     T("4 equal sides make 36: 36 ÷ 4.", "4 برابر اضلاع مل کر 36: 36 ÷ 4"),
     T("Right! 9 cm. Check: 4 × 9 = 36.", "درست! 9 سینٹی میٹر۔ جانچ: 4 × 9 = 36"),
     T("36 ÷ 4 = 9 cm.", "36 ÷ 4 = 9 سینٹی میٹر"),
     common_wrong=[wrong(6, "6 × 6 = 36 is the area of a 6 cm square. Perimeter ÷ 4: 9 cm.", "6 × 6 = 36 تو 6 سینٹی میٹر مربع کا رقبہ ہے۔ احاطہ ÷ 4: 9 سینٹی میٹر", "area_for_perimeter"),
                   wrong(32, "Divide by 4, don't subtract: 36 ÷ 4 = 9.", "4 سے تقسیم کریں، گھٹائیں نہیں: 36 ÷ 4 = 9")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "You can measure all the way round now!", "اب آپ پورا گرد ناپ سکتے ہیں!"),
    "text": T("Perimeter is the distance around a shape: add all its sides. Rectangle: 2 × (length + width). Square: 4 × side. To find a missing side of a rectangle, halve the perimeter, then take away the side you know.",
              "احاطہ کسی شکل کے گرد کا فاصلہ ہے: تمام اضلاع جمع کریں۔ مستطیل: 2 × (لمبائی + چوڑائی)۔ مربع: 4 × ضلع۔ مستطیل کا نامعلوم ضلع نکالنے کے لیے احاطہ آدھا کریں، پھر معلوم ضلع گھٹائیں۔"),
    "points": [T("Count every side, not just two.", "ہر ضلع گنیں، صرف دو نہیں۔"),
               T("Perimeter is in cm or m, not cm².", "احاطہ سینٹی میٹر یا میٹر میں ہوتا ہے، مربع سینٹی میٹر میں نہیں۔")]},
 ],
 "review_questions": [
   {"id": "r_rect", "type": "apply", "skill": SKILL, "step": number_question(
     "r_rect",
     T("Find the perimeter of a rectangle 10 m long and 4 m wide.", "10 میٹر لمبی اور 4 میٹر چوڑی مستطیل کا احاطہ معلوم کریں۔"),
     R1,
     T("2 × (10 + 4).", "2 × (10 + 4)"),
     T("Right! 28 m.", "درست! 28 میٹر"),
     T("2 × 14 = 28 m.", "2 × 14 = 28 میٹر"),
     common_wrong=[wrong(14, "That is two sides. All four: 28 m.", "یہ دو اضلاع ہیں۔ چاروں: 28 میٹر", "two_sides_only"),
                   wrong(40, "10 × 4 is the area. Perimeter: 28 m.", "10 × 4 رقبہ ہے۔ احاطہ: 28 میٹر", "area_for_perimeter")],
     qtype=None)},
   {"id": "r_square", "type": "recall", "skill": SKILL, "step": number_question(
     "r_square",
     T("Find the perimeter of a square with 6 cm sides.", "6 سینٹی میٹر ضلع والے مربع کا احاطہ معلوم کریں۔"),
     R2,
     T("4 × 6.", "4 × 6"),
     T("Right! 24 cm.", "درست! 24 سینٹی میٹر"),
     T("4 × 6 = 24 cm.", "4 × 6 = 24 سینٹی میٹر"),
     common_wrong=[wrong(36, "6 × 6 is the area. Perimeter: 4 × 6 = 24.", "6 × 6 رقبہ ہے۔ احاطہ: 4 × 6 = 24", "area_for_perimeter")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Perimeter and Area unit. No textbook text or exercises were used.",
   "There are no pictures yet: every shape is described in words. A drawing of each shape on the board helps.",
   "Urdu terms to check: احاطہ (perimeter), مستطیل (rectangle), مربع (square), مسدس (hexagon).",
   "The numbers were worked out in content/sources/g6-maths-08/perimeter.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)
