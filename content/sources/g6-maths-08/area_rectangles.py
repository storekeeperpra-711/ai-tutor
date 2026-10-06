from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, PA_PERIMETER, PA_AREA)

SKILL = PA_AREA


def rect_p(length, width):
    return 2 * (length + width)


# s2
assert rect_p(6, 3) == 18
# s4: 4 by 3, counted as 3 rows of 4
S4 = sum(4 for _ in range(3))
assert S4 == 4 * 3 == 12 and rect_p(4, 3) == 14 and 4 + 3 == 7
# s5: rug 6 by 4
S5 = 6 * 4
assert S5 == 24 and rect_p(6, 4) == 20
# s6: square side 9
S6 = 9 * 9
assert S6 == 81 and 4 * 9 == 36 and 9 * 2 == 18
# s7: area 40, length 8
S7 = 40 // 8
assert S7 == 5 and 8 * S7 == 40 and 40 - 8 == 32
# s8: same perimeter, different area
assert rect_p(7, 3) == rect_p(5, 5) == 20
S8 = 5 * 5 - 7 * 3
assert S8 == 4
# s9: 5 by 3
assert 5 * 3 == 15 and rect_p(5, 3) == 16
# s11: 8 m by 6 m floor, 1 m² tiles
S11 = 8 * 6
assert S11 == 48 and rect_p(8, 6) == 28
# question bank and review
QB = 12 * 5
assert QB == 60 and rect_p(12, 5) == 34
assert 4 * 4 == 16
R1 = 9 * 7
assert R1 == 63 and rect_p(9, 7) == 32
R2 = 10 * 10
assert R2 == 100 and 4 * 10 == 40


lesson = {
 "id": "g6-maths-08-area-of-rectangles",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Find the area of rectangles and squares in square units, and a missing side from the area.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Area of rectangles and squares", "مستطیل اور مربع کا رقبہ"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": PA_PERIMETER}],
 "misconceptions": [
   {"id": "perimeter_for_area", "description": "Adds the sides (the perimeter) when the area is asked."},
   {"id": "area_wrong_units", "description": "Writes area in cm or m instead of square units (cm², m²)."},
   {"id": "same_perimeter_same_area", "description": "Thinks shapes with the same perimeter must have the same area."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_units", "type": "recall", "step": {
     "id": "qb_units", "type": "choice",
     "prompt": T("Which unit is right for the area of a page?", "کسی صفحے کے رقبے کے لیے کون سی اکائی درست ہے؟"),
     "options": [
       opt("cm2", "cm² (square centimetres)", "مربع سینٹی میٹر (cm²)", True, "Yes! Area counts squares, so it uses square units.", "جی ہاں! رقبہ مربع گنتا ہے، اس لیے مربع اکائیاں۔"),
       opt("cm", "cm", "سینٹی میٹر", False, "cm measures a length. Area counts squares: cm².", "سینٹی میٹر لمبائی ناپتا ہے۔ رقبہ مربع گنتا ہے: cm²", "area_wrong_units"),
       opt("kg", "kg", "کلوگرام", False, "kg measures weight. Area uses square units: cm².", "کلوگرام وزن ناپتا ہے۔ رقبے کی اکائی مربع ہے: cm²"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("Find the area of a rectangle 12 cm long and 5 cm wide, in cm².", "12 سینٹی میٹر لمبی اور 5 سینٹی میٹر چوڑی مستطیل کا رقبہ مربع سینٹی میٹر میں معلوم کریں۔"),
     QB,
     T("Area = length × width.", "رقبہ = لمبائی × چوڑائی"),
     T("Right! 60 cm².", "درست! 60 مربع سینٹی میٹر"),
     T("12 × 5 = 60 cm².", "12 × 5 = 60 مربع سینٹی میٹر"),
     common_wrong=[wrong(34, "34 cm is the perimeter. Area = 12 × 5 = 60 cm².", "34 سینٹی میٹر احاطہ ہے۔ رقبہ = 12 × 5 = 60 مربع سینٹی میٹر", "perimeter_for_area"),
                   wrong(17, "Multiply, don't add: 12 × 5 = 60.", "جمع نہیں، ضرب: 12 × 5 = 60", "perimeter_for_area")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Talha writes: 'The area of a square with 4 cm sides is 16 cm.' What went wrong?", "طلحہ لکھتا ہے: '4 سینٹی میٹر ضلع والے مربع کا رقبہ 16 سینٹی میٹر ہے۔' کیا غلطی ہوئی؟"),
     "options": [
       opt("units", "The unit: area is 16 cm², square centimetres.", "اکائی: رقبہ 16 مربع سینٹی میٹر ہے۔", True,
           "Yes! The number is right; area counts squares, so cm².", "جی ہاں! عدد درست ہے؛ رقبہ مربع گنتا ہے، اس لیے cm²"),
       opt("number", "The number: it should be 8.", "عدد: یہ 8 ہونا چاہیے۔", False,
           "4 × 4 = 16 is right. Only the unit is wrong: cm².", "4 × 4 = 16 درست ہے۔ صرف اکائی غلط ہے: cm²"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "16 cm is a length. Area is 16 cm².", "16 سینٹی میٹر لمبائی ہے۔ رقبہ 16 مربع سینٹی میٹر ہے۔", "area_wrong_units"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_area", "front": T("Area of a rectangle?", "مستطیل کا رقبہ؟"),
    "back": T("Length × width, in square units. 6 m by 4 m: 24 m².", "لمبائی × چوڑائی، مربع اکائیوں میں۔ 6 میٹر ضرب 4 میٹر: 24 مربع میٹر")},
   {"id": "f_square", "front": T("Area of a square?", "مربع کا رقبہ؟"),
    "back": T("Side × side. Side 9 cm: 81 cm².", "ضلع × ضلع۔ ضلع 9 سینٹی میٹر: 81 مربع سینٹی میٹر")},
 ],
 "home_tasks": [{"id": "h_tiles", "text": T(
   "Find a floor or wall with square tiles. Count the tiles along one side and along the other. Multiply to find how many tiles there are, then count a few rows to check.",
   "کوئی فرش یا دیوار ڈھونڈیں جس پر مربع ٹائلیں ہوں۔ ایک طرف کی ٹائلیں اور دوسری طرف کی ٹائلیں گنیں۔ ضرب دے کر کل ٹائلیں نکالیں، پھر کچھ قطاریں گن کر جانچیں۔")}],
 "glossary": [T("Area", "رقبہ"), T("Square centimetre (cm²)", "مربع سینٹی میٹر")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Ammi wants a new rug for the room. Is it the distance around that matters, or the floor it covers?",
                     "امی کمرے کے لیے نیا قالین چاہتی ہیں۔ کیا گرد کا فاصلہ اہم ہے، یا وہ فرش جو قالین ڈھانپے گا؟"),
    "text": T("The space a flat shape covers is its area. First, a quick check on perimeter.", "کوئی چپٹی شکل جتنی جگہ گھیرتی ہے وہ اس کا رقبہ ہے۔ پہلے احاطے کا ایک سوال۔")},
   number_question(
     "s2_foundation",
     T("What is the perimeter of a rectangle 6 cm by 3 cm?", "6 ضرب 3 سینٹی میٹر مستطیل کا احاطہ کیا ہے؟"),
     18,
     T("6 + 3 + 6 + 3.", "6 + 3 + 6 + 3"),
     T("Right! 18 cm.", "درست! 18 سینٹی میٹر"),
     T("2 × (6 + 3) = 18 cm.", "2 × (6 + 3) = 18 سینٹی میٹر"),
     common_wrong=[wrong(9, "That is two sides. All four: 18 cm.", "یہ دو اضلاع ہیں۔ چاروں: 18 سینٹی میٹر")],
     qtype="recall", skill=PA_PERIMETER),
   {"id": "s3_squares", "type": "explain",
    "character": say("happy", "Area counts the little squares inside!", "رقبہ اندر کے چھوٹے مربع گنتا ہے!"),
    "text": T("Cover a rectangle 4 cm long and 3 cm wide with 1 cm squares: 3 rows of 4 squares. That is 4 × 3 = 12 squares, so the area is 12 square centimetres, written 12 cm². Area of a rectangle = length × width. Area of a square = side × side.",
              "4 سینٹی میٹر لمبی اور 3 سینٹی میٹر چوڑی مستطیل کو 1 سینٹی میٹر کے مربعوں سے ڈھانپیں: 4 مربعوں کی 3 قطاریں۔ یعنی 4 × 3 = 12 مربع، اس لیے رقبہ 12 مربع سینٹی میٹر ہے، جسے 12 cm² لکھتے ہیں۔ مستطیل کا رقبہ = لمبائی × چوڑائی۔ مربع کا رقبہ = ضلع × ضلع۔")},
   number_question(
     "s4_count",
     T("So how many 1 cm squares cover the 4 cm by 3 cm rectangle?", "تو 4 ضرب 3 سینٹی میٹر مستطیل کو 1 سینٹی میٹر کے کتنے مربع ڈھانپتے ہیں؟"),
     S4,
     T("3 rows of 4.", "4 کی 3 قطاریں"),
     T("Right! 12 squares: 12 cm².", "درست! 12 مربع: 12 مربع سینٹی میٹر"),
     T("4 × 3 = 12 squares.", "4 × 3 = 12 مربع"),
     common_wrong=[wrong(14, "14 cm is the perimeter, around the edge. Inside: 4 × 3 = 12.", "14 سینٹی میٹر احاطہ ہے، کنارے کے گرد۔ اندر: 4 × 3 = 12", "perimeter_for_area"),
                   wrong(7, "Multiply the rows and columns: 4 × 3 = 12.", "قطاریں اور کالم ضرب دیں: 4 × 3 = 12", "perimeter_for_area")]),
   number_question(
     "s5_rug",
     T("Ammi's rug is 6 m long and 4 m wide. What is its area in m²?", "امی کا قالین 6 میٹر لمبا اور 4 میٹر چوڑا ہے۔ اس کا رقبہ مربع میٹر میں کیا ہے؟"),
     S5,
     T("Length × width.", "لمبائی × چوڑائی"),
     T("Right! 24 m².", "درست! 24 مربع میٹر"),
     T("6 × 4 = 24 m².", "6 × 4 = 24 مربع میٹر"),
     common_wrong=[wrong(20, "20 m is the perimeter. Area = 6 × 4 = 24 m².", "20 میٹر احاطہ ہے۔ رقبہ = 6 × 4 = 24 مربع میٹر", "perimeter_for_area")]),
   number_question(
     "s6_square",
     T("A square has sides of 9 cm. What is its area in cm²?", "ایک مربع کا ضلع 9 سینٹی میٹر ہے۔ اس کا رقبہ مربع سینٹی میٹر میں کیا ہے؟"),
     S6,
     T("Side × side: 9 × 9.", "ضلع × ضلع: 9 × 9"),
     T("Right! 81 cm².", "درست! 81 مربع سینٹی میٹر"),
     T("9 × 9 = 81 cm².", "9 × 9 = 81 مربع سینٹی میٹر"),
     common_wrong=[wrong(36, "36 cm is the perimeter. Area = 9 × 9 = 81 cm².", "36 سینٹی میٹر احاطہ ہے۔ رقبہ = 9 × 9 = 81", "perimeter_for_area"),
                   wrong(18, "That is 9 × 2. Area of a square is 9 × 9 = 81.", "یہ 9 × 2 ہے۔ مربع کا رقبہ 9 × 9 = 81")]),
   number_question(
     "s7_missing",
     T("A rectangle has an area of 40 cm². Its length is 8 cm. How wide is it?", "ایک مستطیل کا رقبہ 40 مربع سینٹی میٹر ہے۔ اس کی لمبائی 8 سینٹی میٹر ہے۔ چوڑائی کتنی ہے؟"),
     S7,
     T("8 × width = 40.", "8 × چوڑائی = 40"),
     T("Right! 5 cm. Check: 8 × 5 = 40.", "درست! 5 سینٹی میٹر۔ جانچ: 8 × 5 = 40"),
     T("40 ÷ 8 = 5 cm.", "40 ÷ 8 = 5 سینٹی میٹر"),
     common_wrong=[wrong(32, "Divide, don't subtract: 40 ÷ 8 = 5.", "گھٹائیں نہیں، تقسیم کریں: 40 ÷ 8 = 5")]),
   number_question(
     "s8_same_perimeter",
     T("A 7 m by 3 m garden and a 5 m by 5 m garden both have a perimeter of 20 m. How many m² bigger is the square garden?", "7 ضرب 3 میٹر اور 5 ضرب 5 میٹر کے دونوں باغیچوں کا احاطہ 20 میٹر ہے۔ مربع باغیچہ کتنے مربع میٹر بڑا ہے؟"),
     S8,
     T("Find both areas: 5 × 5 and 7 × 3.", "دونوں رقبے نکالیں: 5 × 5 اور 7 × 3"),
     T("Right! 25 − 21 = 4 m². Same perimeter, different area!", "درست! 25 − 21 = 4 مربع میٹر۔ احاطہ ایک، رقبہ مختلف!"),
     T("5 × 5 = 25 and 7 × 3 = 21, so 25 − 21 = 4 m².", "5 × 5 = 25 اور 7 × 3 = 21، تو 25 − 21 = 4 مربع میٹر"),
     common_wrong=[wrong(0, "Same perimeter doesn't mean same area: 25 m² and 21 m². Difference: 4.", "ایک احاطے کا مطلب ایک رقبہ نہیں: 25 اور 21 مربع میٹر۔ فرق: 4", "same_perimeter_same_area")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Rabia says the area of a 5 cm by 3 cm rectangle is 16 cm². What went wrong?", "رابعہ کہتی ہے 5 ضرب 3 سینٹی میٹر مستطیل کا رقبہ 16 مربع سینٹی میٹر ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("perimeter", "She found the perimeter. Area = 5 × 3 = 15 cm².", "اس نے احاطہ نکالا۔ رقبہ = 5 × 3 = 15 مربع سینٹی میٹر", True,
          "Yes! 5 + 3 + 5 + 3 = 16 is the distance round. Inside: 15 squares.", "جی ہاں! 5 + 3 + 5 + 3 = 16 گرد کا فاصلہ ہے۔ اندر: 15 مربع۔"),
      opt("eight", "It should be 8 cm².", "یہ 8 مربع سینٹی میٹر ہونا چاہیے۔", False,
          "8 is 5 + 3. Area multiplies: 5 × 3 = 15.", "8 یعنی 5 + 3۔ رقبے میں ضرب: 5 × 3 = 15", "perimeter_for_area"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "16 cm is the perimeter. The area is 5 × 3 = 15 cm².", "16 سینٹی میٹر احاطہ ہے۔ رقبہ 5 × 3 = 15 مربع سینٹی میٹر ہے۔", "perimeter_for_area"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why does length × width give the area of a rectangle? Can you teach me?",
                     "لمبائی × چوڑائی سے مستطیل کا رقبہ کیوں نکلتا ہے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why do we multiply length by width to find the area of a rectangle?",
              "اپنے الفاظ میں بتائیں: مستطیل کا رقبہ نکالنے کے لیے لمبائی کو چوڑائی سے ضرب کیوں دیتے ہیں؟"),
    "key_idea": "Area counts the unit squares inside. The length tells how many squares fit in one row and the width tells how many rows there are, so the total is length × width.",
    "levels": {
      "got_it": "Explains that the rectangle is rows of unit squares: the length gives squares per row, the width gives the number of rows.",
      "partly": "Says area counts squares, without linking rows and columns to the multiplication.",
      "not_yet": "Confuses it with perimeter, or gives no reason."},
    "keywords": [
      ["square", "مربع", "murabba"],
      ["row", "rows", "قطار", "qataar"],
      ["inside", "cover", "اندر", "ڈھانپ"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Rows of squares: squares in a row × number of rows.", "بہت خوب! مربعوں کی قطاریں: ایک قطار کے مربع × قطاروں کی تعداد۔"),
      "partly": T("Good start! Now say how rows and columns of squares give a multiplication.", "اچھی شروعات! اب بتائیں مربعوں کی قطاروں اور کالموں سے ضرب کیسے بنتی ہے۔"),
      "not_yet": T("Picture the 4 by 3 rectangle: 3 rows of 4 squares. How many squares is that?", "4 ضرب 3 کی مستطیل سوچیں: 4 مربعوں کی 3 قطاریں۔ کل کتنے مربع ہوئے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_tiles",
     T("A floor is 8 m long and 6 m wide. Each tile covers 1 m². How many tiles are needed?", "ایک فرش 8 میٹر لمبا اور 6 میٹر چوڑا ہے۔ ہر ٹائل 1 مربع میٹر ڈھانپتی ہے۔ کتنی ٹائلیں چاہییں؟"),
     S11,
     T("The number of tiles is the area: 8 × 6.", "ٹائلوں کی تعداد رقبہ ہے: 8 × 6"),
     T("Right! 48 tiles.", "درست! 48 ٹائلیں"),
     T("8 × 6 = 48 m², so 48 tiles.", "8 × 6 = 48 مربع میٹر، یعنی 48 ٹائلیں"),
     common_wrong=[wrong(28, "28 m is the perimeter. Tiles cover the inside: 8 × 6 = 48.", "28 میٹر احاطہ ہے۔ ٹائلیں اندر ڈھانپتی ہیں: 8 × 6 = 48", "perimeter_for_area"),
                   wrong(14, "Multiply, don't add: 8 × 6 = 48.", "جمع نہیں، ضرب: 8 × 6 = 48")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Now you can measure the inside of a shape!", "اب آپ شکل کا اندر ناپ سکتے ہیں!"),
    "text": T("Area is the space a shape covers, counted in squares. Rectangle: length × width. Square: side × side. Write area in square units: cm², m². Shapes with the same perimeter can have different areas.",
              "رقبہ وہ جگہ ہے جو شکل ڈھانپتی ہے، مربعوں میں گنی جاتی ہے۔ مستطیل: لمبائی × چوڑائی۔ مربع: ضلع × ضلع۔ رقبہ مربع اکائیوں میں لکھیں: مربع سینٹی میٹر، مربع میٹر۔ ایک جیسے احاطے والی شکلوں کا رقبہ مختلف ہو سکتا ہے۔"),
    "points": [T("Perimeter goes around (cm); area covers inside (cm²).", "احاطہ گرد (سینٹی میٹر)؛ رقبہ اندر (مربع سینٹی میٹر)۔"),
               T("Missing side: area ÷ the side you know.", "نامعلوم ضلع: رقبہ ÷ معلوم ضلع۔")]},
 ],
 "review_questions": [
   {"id": "r_rect", "type": "apply", "skill": SKILL, "step": number_question(
     "r_rect",
     T("Find the area of a rectangle 9 cm by 7 cm, in cm².", "9 ضرب 7 سینٹی میٹر مستطیل کا رقبہ مربع سینٹی میٹر میں معلوم کریں۔"),
     R1,
     T("9 × 7.", "9 × 7"),
     T("Right! 63 cm².", "درست! 63 مربع سینٹی میٹر"),
     T("9 × 7 = 63 cm².", "9 × 7 = 63 مربع سینٹی میٹر"),
     common_wrong=[wrong(32, "32 cm is the perimeter. Area: 9 × 7 = 63.", "32 سینٹی میٹر احاطہ ہے۔ رقبہ: 9 × 7 = 63", "perimeter_for_area")],
     qtype=None)},
   {"id": "r_square", "type": "recall", "skill": SKILL, "step": number_question(
     "r_square",
     T("Find the area of a square with 10 m sides, in m².", "10 میٹر ضلع والے مربع کا رقبہ مربع میٹر میں معلوم کریں۔"),
     R2,
     T("10 × 10.", "10 × 10"),
     T("Right! 100 m².", "درست! 100 مربع میٹر"),
     T("10 × 10 = 100 m².", "10 × 10 = 100 مربع میٹر"),
     common_wrong=[wrong(40, "40 m is the perimeter. Area: 10 × 10 = 100.", "40 میٹر احاطہ ہے۔ رقبہ: 10 × 10 = 100", "perimeter_for_area")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Perimeter and Area unit. No textbook text or exercises were used.",
   "Area is introduced by counting unit squares in rows before the formula. Squared paper helps.",
   "Urdu terms to check: رقبہ (area), مربع سینٹی میٹر (square centimetre).",
   "The numbers were worked out in content/sources/g6-maths-08/area_rectangles.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)
