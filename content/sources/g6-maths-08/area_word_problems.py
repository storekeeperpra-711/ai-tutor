from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, PA_PERIMETER, PA_AREA, PA_COMPOUND, PA_TRIANGLE, PA_WORD_PROBLEMS)

SKILL = PA_WORD_PROBLEMS


def rect_p(length, width):
    return 2 * (length + width)


# s2
assert 10 * 6 // 2 == 30
# s5: fence 20 by 15 at Rs 50 a metre
S5 = rect_p(20, 15) * 50
assert rect_p(20, 15) == 70 and S5 == 3500 and 20 * 15 * 50 == 15000 and (20 + 15) * 50 == 1750
# s6: carpet 5 by 4 at Rs 300 a square metre
S6 = 5 * 4 * 300
assert S6 == 6000 and rect_p(5, 4) * 300 == 5400
# s7: wall 4 by 3, a litre covers 6 m²
S7 = 4 * 3 // 6
assert S7 == 2 and 4 * 3 % 6 == 0 and 4 * 3 == 12
# s8: square field, perimeter 64
side = 64 // 4
S8 = side * side
assert side == 16 and S8 == 256
# u1 to u5
U1 = rect_p(11, 4)
assert U1 == 30 and 11 * 4 == 44
U2 = 12 * 12
assert U2 == 144 and 4 * 12 == 48
U3 = 9 * 6 - 2 * 3
assert U3 == 48 and 9 * 6 + 2 * 3 == 60
U4 = 16 * 5 // 2
assert U4 == 40 and 16 * 5 == 80
U5 = rect_p(15, 10)
assert U5 == 50 and 15 * 10 == 150
# question bank and review
QB = 4 * 25
assert QB == 100 and 25 * 25 == 625
R1 = 6 * 3 * 200
assert R1 == 3600 and rect_p(6, 3) * 200 == 3600  # same number, so no perimeter wrong answer here
R2 = rect_p(2, 1)
assert R2 == 6 and 2 * 1 == 2


lesson = {
 "id": "g6-maths-08-area-word-problems",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Solve real-life problems by deciding whether perimeter or area is needed, including costs.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Perimeter and area word problems", "احاطے اور رقبے کے سوالات"),
 "estimated_minutes": 16,
 "prerequisites": [{"skill": PA_TRIANGLE}, {"skill": PA_PERIMETER}, {"skill": PA_AREA}, {"skill": PA_COMPOUND}],
 "misconceptions": [
   {"id": "wrong_measure", "description": "Uses area for an edge job (fencing, border) or perimeter for a covering job (carpet, paint)."},
   {"id": "stops_early", "description": "Finds the perimeter or area but not the cost or amount the question asks for."},
   {"id": "two_sides_only", "description": "Adds only two sides of a rectangle for the perimeter."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_which", "type": "recall", "step": {
     "id": "qb_which", "type": "choice",
     "prompt": T("To find how much paint covers a wall, which do you need?", "دیوار پر کتنا رنگ لگے گا، یہ جاننے کے لیے کیا چاہیے؟"),
     "options": [
       opt("area", "The area of the wall", "دیوار کا رقبہ", True, "Yes! Paint covers the whole surface.", "جی ہاں! رنگ پوری سطح ڈھانپتا ہے۔"),
       opt("perimeter", "The perimeter of the wall", "دیوار کا احاطہ", False, "Perimeter is only the edge. Paint covers the inside: area.", "احاطہ صرف کنارہ ہے۔ رنگ اندر ڈھانپتا ہے: رقبہ۔", "wrong_measure"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("A square plot has 25 m sides. How many metres of wire fence go all the way round?", "ایک مربع پلاٹ کا ہر ضلع 25 میٹر ہے۔ چاروں طرف کتنے میٹر تار کی باڑ لگے گی؟"),
     QB,
     T("Fence goes around: perimeter = 4 × 25.", "باڑ گرد لگتی ہے: احاطہ = 4 × 25"),
     T("Right! 100 m.", "درست! 100 میٹر"),
     T("4 × 25 = 100 m.", "4 × 25 = 100 میٹر"),
     common_wrong=[wrong(625, "625 m² is the area. A fence goes around: 100 m.", "625 مربع میٹر رقبہ ہے۔ باڑ گرد لگتی ہے: 100 میٹر", "wrong_measure")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("To fence a 20 m by 15 m field, Javed works out 20 × 15 = 300 m of fence. What went wrong?", "20 ضرب 15 میٹر کے میدان کی باڑ کے لیے جاوید 20 × 15 = 300 میٹر نکالتا ہے۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("perimeter", "A fence needs the perimeter: 2 × (20 + 15) = 70 m.", "باڑ کے لیے احاطہ چاہیے: 2 × (20 + 15) = 70 میٹر", True,
           "Yes! 300 m² is the area of the field, not the fence.", "جی ہاں! 300 مربع میٹر میدان کا رقبہ ہے، باڑ نہیں۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "The fence goes around the edge: 70 m. 300 is the area.", "باڑ کنارے کے گرد لگتی ہے: 70 میٹر۔ 300 رقبہ ہے۔", "wrong_measure"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_which", "front": T("Perimeter or area?", "احاطہ یا رقبہ؟"),
    "back": T("Around the edge (fence, border, lace): perimeter. Covering (carpet, paint, tiles, grass): area.", "کنارے کے گرد (باڑ، بارڈر، لیس): احاطہ۔ ڈھانپنا (قالین، رنگ، ٹائل، گھاس): رقبہ۔")},
 ],
 "home_tasks": [{"id": "h_cost", "text": T(
   "Measure a room or courtyard at home. Work out how many metres of border it would need and how many square metres of carpet. Ask at a shop what one metre of border and one square metre of carpet cost, and find the totals.",
   "گھر کا کوئی کمرہ یا صحن ناپیں۔ معلوم کریں کتنے میٹر بارڈر اور کتنے مربع میٹر قالین لگے گا۔ دکان سے ایک میٹر بارڈر اور ایک مربع میٹر قالین کی قیمت پوچھیں، اور کل خرچ نکالیں۔")}],
 "glossary": [T("Perimeter", "احاطہ"), T("Area", "رقبہ"), T("Cost per metre", "فی میٹر قیمت")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Fence, carpet, paint, tiles: some jobs go around the edge, some cover the inside. Which is which?",
                     "باڑ، قالین، رنگ، ٹائلیں: کچھ کام کنارے کے گرد ہوتے ہیں، کچھ اندر ڈھانپتے ہیں۔ کون سا کیا ہے؟"),
    "text": T("Today we solve real problems with perimeter and area, including costs. First, a quick check.", "آج ہم احاطے اور رقبے کے اصل سوال حل کریں گے، خرچ سمیت۔ پہلے ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("What is the area of a triangle with base 10 cm and height 6 cm, in cm²?", "10 قاعدے اور 6 اونچائی والے مثلث کا رقبہ کیا ہے؟"),
     30,
     T("½ × 10 × 6.", "½ × 10 × 6"),
     T("Right! 30 cm².", "درست! 30 مربع سینٹی میٹر"),
     T("10 × 6 = 60, half is 30.", "10 × 6 = 60، آدھا 30"),
     common_wrong=[wrong(60, "Halve it: 30.", "آدھا کریں: 30")],
     qtype="recall", skill=PA_TRIANGLE),
   {"id": "s3_which", "type": "explain",
    "character": say("thinking", "Ask: does it go around, or cover?", "پوچھیں: یہ گرد جاتا ہے، یا ڈھانپتا ہے؟"),
    "text": T("Around the edge (fence, border, lace, skirting): use the perimeter, in m or cm. Covering the inside (carpet, paint, tiles, grass): use the area, in m² or cm². For a cost, multiply the amount by the price of one metre or one square metre.",
              "کنارے کے گرد (باڑ، بارڈر، لیس): احاطہ لیں، میٹر یا سینٹی میٹر میں۔ اندر ڈھانپنا (قالین، رنگ، ٹائلیں، گھاس): رقبہ لیں، مربع میٹر یا مربع سینٹی میٹر میں۔ خرچ کے لیے مقدار کو ایک میٹر یا ایک مربع میٹر کی قیمت سے ضرب دیں۔")},
   {"id": "s4_choose", "type": "choice", "question_type": "apply",
    "prompt": T("Nani wants lace sewn all round the edge of a tablecloth. Which does she need?", "نانی میز پوش کے چاروں کناروں پر لیس لگوانا چاہتی ہیں۔ انہیں کیا چاہیے؟"),
    "options": [
      opt("perimeter", "The perimeter", "احاطہ", True, "Yes! Lace goes around the edge.", "جی ہاں! لیس کنارے کے گرد لگتی ہے۔"),
      opt("area", "The area", "رقبہ", False, "Lace only goes on the edge, not over the cloth: perimeter.", "لیس صرف کنارے پر لگتی ہے، پورے کپڑے پر نہیں: احاطہ۔", "wrong_measure"),
    ]},
   number_question(
     "s5_fence_cost",
     T("A field is 20 m long and 15 m wide. Fencing costs Rs 50 a metre. How much does it cost to fence all the way round?", "ایک میدان 20 میٹر لمبا اور 15 میٹر چوڑا ہے۔ باڑ 50 روپے فی میٹر ہے۔ چاروں طرف باڑ پر کتنا خرچ آئے گا؟"),
     S5,
     T("Perimeter first: 2 × (20 + 15). Then × 50.", "پہلے احاطہ: 2 × (20 + 15)۔ پھر × 50"),
     T("Right! 70 m × Rs 50 = Rs 3500.", "درست! 70 میٹر × 50 روپے = 3500 روپے"),
     T("Perimeter = 70 m, so 70 × 50 = Rs 3500.", "احاطہ = 70 میٹر، تو 70 × 50 = 3500 روپے"),
     common_wrong=[wrong(15000, "That used the area. A fence goes around: 70 m × 50 = 3500.", "یہ رقبے سے نکلا۔ باڑ گرد لگتی ہے: 70 × 50 = 3500", "wrong_measure"),
                   wrong(1750, "That is only two sides. All four: 70 m × 50 = 3500.", "یہ صرف دو اضلاع ہیں۔ چاروں: 70 × 50 = 3500", "two_sides_only"),
                   wrong(70, "70 m is the fence. Now the cost: 70 × 50 = 3500.", "70 میٹر باڑ ہے۔ اب خرچ: 70 × 50 = 3500", "stops_early")]),
   number_question(
     "s6_carpet_cost",
     T("A room is 5 m by 4 m. Carpet costs Rs 300 a square metre. How much does carpet for the whole floor cost?", "ایک کمرہ 5 ضرب 4 میٹر ہے۔ قالین 300 روپے فی مربع میٹر ہے۔ پورے فرش کے قالین پر کتنا خرچ آئے گا؟"),
     S6,
     T("Area first: 5 × 4. Then × 300.", "پہلے رقبہ: 5 × 4۔ پھر × 300"),
     T("Right! 20 m² × Rs 300 = Rs 6000.", "درست! 20 مربع میٹر × 300 = 6000 روپے"),
     T("Area = 20 m², so 20 × 300 = Rs 6000.", "رقبہ = 20 مربع میٹر، تو 20 × 300 = 6000 روپے"),
     common_wrong=[wrong(5400, "That used the perimeter. Carpet covers the floor: 20 m² × 300 = 6000.", "یہ احاطے سے نکلا۔ قالین فرش ڈھانپتا ہے: 20 × 300 = 6000", "wrong_measure"),
                   wrong(20, "20 m² is the area. Now the cost: 20 × 300 = 6000.", "20 مربع میٹر رقبہ ہے۔ اب خرچ: 20 × 300 = 6000", "stops_early")]),
   number_question(
     "s7_paint",
     T("A wall is 4 m wide and 3 m high. One tin of paint covers 6 m². How many tins are needed?", "ایک دیوار 4 میٹر چوڑی اور 3 میٹر اونچی ہے۔ رنگ کا ایک ڈبہ 6 مربع میٹر ڈھانپتا ہے۔ کتنے ڈبے چاہییں؟"),
     S7,
     T("Area: 4 × 3 = 12 m². Each tin covers 6 m².", "رقبہ: 4 × 3 = 12 مربع میٹر۔ ہر ڈبہ 6 مربع میٹر۔"),
     T("Right! 12 ÷ 6 = 2 tins.", "درست! 12 ÷ 6 = 2 ڈبے"),
     T("4 × 3 = 12 m², and 12 ÷ 6 = 2 tins.", "4 × 3 = 12، اور 12 ÷ 6 = 2 ڈبے"),
     common_wrong=[wrong(12, "12 m² is the wall. Each tin covers 6: 12 ÷ 6 = 2.", "12 مربع میٹر دیوار ہے۔ ہر ڈبہ 6: 12 ÷ 6 = 2", "stops_early")]),
   number_question(
     "s8_square_field",
     T("A square field has a perimeter of 64 m. What is its area in m²?", "ایک مربع میدان کا احاطہ 64 میٹر ہے۔ اس کا رقبہ کیا ہے؟"),
     S8,
     T("Side = 64 ÷ 4. Then side × side.", "ضلع = 64 ÷ 4۔ پھر ضلع × ضلع"),
     T("Right! Side 16 m, area 16 × 16 = 256 m².", "درست! ضلع 16 میٹر، رقبہ 16 × 16 = 256"),
     T("64 ÷ 4 = 16 m, and 16 × 16 = 256 m².", "64 ÷ 4 = 16 میٹر، اور 16 × 16 = 256"),
     common_wrong=[wrong(16, "16 m is one side. Area: 16 × 16 = 256 m².", "16 میٹر ایک ضلع ہے۔ رقبہ: 16 × 16 = 256", "stops_early"),
                   wrong(64, "64 m is the perimeter. Area: 16 × 16 = 256 m².", "64 میٹر احاطہ ہے۔ رقبہ: 16 × 16 = 256", "wrong_measure")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("To find how many m² of grass seed a 9 m by 6 m lawn needs, Laiba works out 2 × (9 + 6) = 30. What went wrong?", "9 ضرب 6 میٹر کے لان کے لیے کتنے مربع میٹر گھاس کا بیج چاہیے، اس کے لیے لائبہ 2 × (9 + 6) = 30 نکالتی ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("area", "Grass covers the lawn: area = 9 × 6 = 54 m².", "گھاس لان ڈھانپتی ہے: رقبہ = 9 × 6 = 54 مربع میٹر", True,
          "Yes! 30 m is the perimeter, the distance around.", "جی ہاں! 30 میٹر احاطہ ہے، گرد کا فاصلہ۔"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "That is the edge. Seed covers the whole lawn: 9 × 6 = 54 m².", "یہ کنارہ ہے۔ بیج پورا لان ڈھانپتا ہے: 9 × 6 = 54", "wrong_measure"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "How do you decide if a problem needs perimeter or area? Can you teach me?",
                     "آپ کیسے فیصلہ کرتے ہیں کہ سوال میں احاطہ چاہیے یا رقبہ؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: how do you know whether a problem needs the perimeter or the area? Give an example of each.",
              "اپنے الفاظ میں بتائیں: آپ کیسے جانتے ہیں کہ سوال میں احاطہ چاہیے یا رقبہ؟ ہر ایک کی مثال دیں۔"),
    "key_idea": "If the thing goes along the edge (fence, border, lace), use perimeter. If it covers the surface (carpet, paint, grass, tiles), use area.",
    "levels": {
      "got_it": "Links perimeter to things along the edge and area to things covering the surface, with an example of each.",
      "partly": "Describes one correctly, or both without examples.",
      "not_yet": "Mixes them up or gives no rule."},
    "keywords": [
      ["edge", "around", "fence", "کنارہ", "گرد", "باڑ"],
      ["cover", "inside", "carpet", "paint", "ڈھانپ", "قالین", "رنگ"],
      ["perimeter", "area", "احاطہ", "رقبہ"]],
    "fallback_feedback": {
      "got_it": T("Great rule! Around the edge: perimeter. Covering: area.", "بہت اچھا اصول! کنارے کے گرد: احاطہ۔ ڈھانپنا: رقبہ۔"),
      "partly": T("Good start! Now give the other one, with an example.", "اچھی شروعات! اب دوسرا بتائیں، مثال کے ساتھ۔"),
      "not_yet": T("Think of a fence and a carpet. Which goes around the room, and which covers the floor?", "باڑ اور قالین سوچیں۔ کون گرد جاتا ہے، اور کون فرش ڈھانپتا ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   {"id": "s11_unit_test", "type": "explain",
    "character": say("encouraging", "Test time! Five questions from the whole Perimeter and area unit. You can do it!",
                     "ٹیسٹ کا وقت! احاطے اور رقبے کے پورے باب سے پانچ سوال۔ آپ کر سکتے ہیں!"),
    "text": T("This short test has questions on perimeter, area of rectangles, compound shapes, triangles and a real-life problem. Take your time.",
              "اس چھوٹے ٹیسٹ میں احاطہ، مستطیل کا رقبہ، مرکب شکلیں، مثلث اور ایک اصل زندگی کا سوال ہے۔ آرام سے کریں۔")},
   number_question(
     "u1_perimeter",
     T("Test 1: Find the perimeter of a rectangle 11 cm by 4 cm.", "ٹیسٹ 1: 11 ضرب 4 سینٹی میٹر مستطیل کا احاطہ معلوم کریں۔"),
     U1,
     T("2 × (11 + 4).", "2 × (11 + 4)"),
     T("Right! 30 cm.", "درست! 30 سینٹی میٹر"),
     T("2 × 15 = 30 cm.", "2 × 15 = 30"),
     common_wrong=[wrong(44, "11 × 4 is the area. Perimeter: 30 cm.", "11 × 4 رقبہ ہے۔ احاطہ: 30"),
                   wrong(15, "That is two sides. All four: 30 cm.", "یہ دو اضلاع ہیں۔ چاروں: 30")],
     qtype="recall", skill=PA_PERIMETER),
   number_question(
     "u2_area",
     T("Test 2: Find the area of a square with 12 cm sides, in cm².", "ٹیسٹ 2: 12 سینٹی میٹر ضلع والے مربع کا رقبہ معلوم کریں۔"),
     U2,
     T("12 × 12.", "12 × 12"),
     T("Right! 144 cm².", "درست! 144 مربع سینٹی میٹر"),
     T("12 × 12 = 144 cm².", "12 × 12 = 144"),
     common_wrong=[wrong(48, "48 cm is the perimeter. Area: 12 × 12 = 144.", "48 سینٹی میٹر احاطہ ہے۔ رقبہ: 144")],
     qtype="apply", skill=PA_AREA),
   number_question(
     "u3_compound",
     T("Test 3: A 9 m by 6 m yard has a 2 m by 3 m shed in it. What area is left, in m²?", "ٹیسٹ 3: 9 ضرب 6 میٹر کے احاطے میں 2 ضرب 3 میٹر کا کمرہ ہے۔ کتنا رقبہ بچا؟"),
     U3,
     T("54 take away 6.", "54 منفی 6"),
     T("Right! 48 m².", "درست! 48 مربع میٹر"),
     T("9 × 6 = 54, shed 2 × 3 = 6, so 48 m².", "9 × 6 = 54، کمرہ 2 × 3 = 6، تو 48"),
     common_wrong=[wrong(60, "Take the shed away, don't add it: 54 − 6 = 48.", "کمرہ گھٹائیں، جمع نہیں: 54 − 6 = 48")],
     qtype="apply", skill=PA_COMPOUND),
   number_question(
     "u4_triangle",
     T("Test 4: Find the area of a triangle with base 16 cm and height 5 cm, in cm².", "ٹیسٹ 4: 16 قاعدے اور 5 اونچائی والے مثلث کا رقبہ معلوم کریں۔"),
     U4,
     T("½ × 16 × 5.", "½ × 16 × 5"),
     T("Right! 40 cm².", "درست! 40 مربع سینٹی میٹر"),
     T("16 × 5 = 80, half is 40.", "16 × 5 = 80، آدھا 40"),
     common_wrong=[wrong(80, "Halve it: 40.", "آدھا کریں: 40")],
     qtype="apply", skill=PA_TRIANGLE),
   number_question(
     "u5_ribbon",
     T("Test 5: Zoya puts ribbon all round the edge of a card 15 cm by 10 cm. How many cm of ribbon does she need?", "ٹیسٹ 5: زویا 15 ضرب 10 سینٹی میٹر کارڈ کے چاروں کناروں پر ربن لگاتی ہے۔ کتنے سینٹی میٹر ربن چاہیے؟"),
     U5,
     T("Ribbon goes around: perimeter.", "ربن گرد لگتا ہے: احاطہ۔"),
     T("Right! 50 cm.", "درست! 50 سینٹی میٹر"),
     T("2 × (15 + 10) = 50 cm.", "2 × (15 + 10) = 50"),
     common_wrong=[wrong(150, "150 cm² is the area. Ribbon goes around: 50 cm.", "150 رقبہ ہے۔ ربن گرد لگتا ہے: 50", "wrong_measure")],
     qtype="apply"),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "You finished the Perimeter and area unit! Well done!", "آپ نے احاطے اور رقبے کا باب مکمل کر لیا! شاباش!"),
    "text": T("Around the edge (fence, border, ribbon): perimeter. Covering (carpet, paint, grass, tiles): area. For costs or tins, finish the job: multiply by the price, or divide by what one tin covers.",
              "کنارے کے گرد (باڑ، بارڈر، ربن): احاطہ۔ ڈھانپنا (قالین، رنگ، گھاس، ٹائلیں): رقبہ۔ خرچ یا ڈبوں کے لیے کام پورا کریں: قیمت سے ضرب دیں، یا ایک ڈبے کی مقدار سے تقسیم کریں۔"),
    "points": [T("Perimeter in m; area in m².", "احاطہ میٹر میں؛ رقبہ مربع میٹر میں۔"),
               T("Answer the question asked: the cost, not just the area.", "وہی جواب دیں جو پوچھا گیا: خرچ، صرف رقبہ نہیں۔")]},
 ],
 "review_questions": [
   {"id": "r_carpet", "type": "apply", "skill": SKILL, "step": number_question(
     "r_carpet",
     T("Carpet costs Rs 200 a square metre. How much does it cost to carpet a 6 m by 3 m room?", "قالین 200 روپے فی مربع میٹر ہے۔ 6 ضرب 3 میٹر کمرے کے قالین پر کتنا خرچ آئے گا؟"),
     R1,
     T("Area 6 × 3, then × 200.", "رقبہ 6 × 3، پھر × 200"),
     T("Right! 18 m² × 200 = Rs 3600.", "درست! 18 × 200 = 3600 روپے"),
     T("6 × 3 = 18 m², and 18 × 200 = Rs 3600.", "6 × 3 = 18، اور 18 × 200 = 3600"),
     common_wrong=[wrong(18, "18 m² is the area. Now the cost: 18 × 200 = 3600.", "18 مربع میٹر رقبہ ہے۔ اب خرچ: 3600", "stops_early")],
     qtype=None)},
   {"id": "r_lace", "type": "recall", "skill": SKILL, "step": number_question(
     "r_lace",
     T("A tablecloth is 2 m by 1 m. How many metres of lace go all round its edge?", "ایک میز پوش 2 ضرب 1 میٹر ہے۔ اس کے چاروں کناروں پر کتنے میٹر لیس لگے گی؟"),
     R2,
     T("Perimeter: 2 × (2 + 1).", "احاطہ: 2 × (2 + 1)"),
     T("Right! 6 m.", "درست! 6 میٹر"),
     T("2 × 3 = 6 m.", "2 × 3 = 6 میٹر"),
     common_wrong=[wrong(2, "2 m² is the area. Lace goes around: 6 m.", "2 مربع میٹر رقبہ ہے۔ لیس گرد لگتی ہے: 6 میٹر", "wrong_measure"),
                   wrong(3, "That is two sides. All four: 6 m.", "یہ دو اضلاع ہیں۔ چاروں: 6 میٹر", "two_sides_only")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Perimeter and Area unit. No textbook text or exercises were used.",
   "The main idea is choosing perimeter (along the edge) or area (covering), then finishing the problem (cost, number of tins).",
   "Steps u1 to u5 are a short unit test; each is tagged with the skill of the lesson it comes from.",
   "The numbers were worked out in content/sources/g6-maths-08/area_word_problems.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)
