from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, SO_VOLUME_CUBOID, SO_VOLUME_CUBE, cuboid_volume)

SKILL = SO_VOLUME_CUBE
CM3_PER_LITRE = 1000


def cube_volume(s):
    return cuboid_volume(s, s, s)


# s2: cuboid 3 x 2 x 5
S2 = cuboid_volume(3, 2, 5)
assert S2 == 30
# s4: cube of side 3 cm (3 x 3 = 9 is one face; 3 x 3 = 9; 3 + 3 + 3 = 9)
S4 = cube_volume(3)
assert S4 == 27 and 3 * 3 == 9
# s5: cube of side 10 cm
S5 = cube_volume(10)
assert S5 == 1000 == CM3_PER_LITRE
# s7: tank 50 x 20 x 30 cm, in litres
S7 = cuboid_volume(50, 20, 30) / CM3_PER_LITRE
assert cuboid_volume(50, 20, 30) == 30000 and S7 == 30
# s8: cube of side 5 cm
S8 = cube_volume(5)
assert S8 == 125 and 5 * 5 == 25
# s9: cube of side 4 is 64, not one face 16
assert cube_volume(4) == 64 and 4 * 4 == 16
# s11: water tank 100 x 50 x 40 cm, in litres
S11 = cuboid_volume(100, 50, 40) / CM3_PER_LITRE
assert cuboid_volume(100, 50, 40) == 200000 and S11 == 200
# question bank and review
QB = cube_volume(6)
assert QB == 216 and 6 * 6 == 36
assert 2000 / CM3_PER_LITRE == 2
R1 = cube_volume(2)
assert R1 == 8 and 2 * 3 == 6
R2 = 5000 // CM3_PER_LITRE
assert R2 == 5

lesson = {
 "id": "g6-maths-14-volume-cube",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Find the volume of a cube, and change cubic centimetres to litres (1000 cm³ = 1 litre).", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Volume of a cube, and litres", "مکعب کا حجم اور لیٹر"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": SO_VOLUME_CUBOID}],
 "misconceptions": [
   {"id": "face_area", "description": "Gives the area of one face (side × side) as the volume."},
   {"id": "times_three", "description": "Multiplies the side by 3 instead of side × side × side."},
   {"id": "litre_100", "description": "Thinks 100 cm³ (not 1000 cm³) make 1 litre."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_litre", "type": "recall", "step": {
     "id": "qb_litre", "type": "choice",
     "prompt": T("How many cm³ make 1 litre?", "1 لیٹر میں کتنے مکعب سینٹی میٹر ہوتے ہیں؟"),
     "options": [
       opt("thousand", "1000 cm³", "1000 مکعب سینٹی میٹر", True,
           "Yes! A 10 cm cube holds exactly 1 litre.", "جی ہاں! 10 سینٹی میٹر کا مکعب ٹھیک 1 لیٹر رکھتا ہے۔"),
       opt("hundred", "100 cm³", "100 مکعب سینٹی میٹر", False,
           "It is 1000 cm³: a 10 × 10 × 10 cube.", "یہ 1000 مکعب سینٹی میٹر ہے: 10 × 10 × 10 کا مکعب۔", "litre_100"),
       opt("ten", "10 cm³", "10 مکعب سینٹی میٹر", False,
           "Much more: 1000 cm³.", "اس سے بہت زیادہ: 1000 مکعب سینٹی میٹر۔", "litre_100"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("A cube has sides of 6 cm. What is its volume, in cm³?", "ایک مکعب کے اضلاع 6 سینٹی میٹر ہیں۔ اس کا حجم کتنے مکعب سینٹی میٹر ہے؟"),
     QB,
     T("6 × 6 × 6.", "6 × 6 × 6"),
     T("Right! 216 cm³.", "درست! 216 مکعب سینٹی میٹر"),
     T("6 × 6 = 36, 36 × 6 = 216.", "6 × 6 = 36، 36 × 6 = 216"),
     common_wrong=[wrong(36, "That is one face. Multiply by 6 again: 216.", "یہ ایک سطح ہے۔ پھر 6 سے ضرب دیں: 216", "face_area"),
                   wrong(18, "Not 6 × 3. It is 6 × 6 × 6 = 216.", "6 × 3 نہیں۔ یہ 6 × 6 × 6 = 216 ہے۔", "times_three")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("A jug holds 2000 cm³ of water. Rida says that is 20 litres. What is wrong?", "ایک جگ میں 2000 مکعب سینٹی میٹر پانی آتا ہے۔ ردا کہتی ہے یہ 20 لیٹر ہے۔ کیا غلطی ہے؟"),
     "options": [
       opt("thousand", "1 litre is 1000 cm³, so 2000 cm³ is 2 litres.", "1 لیٹر 1000 مکعب سینٹی میٹر ہے، تو 2000 مکعب سینٹی میٹر 2 لیٹر ہے۔", True,
           "Yes! Divide by 1000, not 100.", "جی ہاں! 1000 سے تقسیم کریں، 100 سے نہیں۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "She divided by 100. Divide by 1000: 2 litres.", "اس نے 100 سے تقسیم کیا۔ 1000 سے تقسیم کریں: 2 لیٹر", "litre_100"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_cube", "front": T("Volume of a cube?", "مکعب کا حجم؟"),
    "back": T("Side × side × side.", "ضلع × ضلع × ضلع")},
   {"id": "f_litre", "front": T("1 litre?", "1 لیٹر؟"),
    "back": T("1000 cm³ (a 10 cm cube).", "1000 مکعب سینٹی میٹر (10 سینٹی میٹر کا مکعب)")},
 ],
 "home_tasks": [{"id": "h_bottle", "text": T(
   "Find a 1.5 litre water bottle at home. How many cm³ of water does it hold? (Hint: 1 litre = 1000 cm³.)",
   "گھر میں 1.5 لیٹر کی پانی کی بوتل ڈھونڈیں۔ اس میں کتنے مکعب سینٹی میٹر پانی آتا ہے؟ (اشارہ: 1 لیٹر = 1000 مکعب سینٹی میٹر)")}],
 "glossary": [T("Cube", "مکعب"), T("Litre", "لیٹر"), T("Capacity", "گنجائش")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "A milk carton says 1 litre. How big a box would hold exactly that much?",
                     "دودھ کے ڈبے پر 1 لیٹر لکھا ہے۔ کتنا بڑا ڈبہ ٹھیک اتنا رکھے گا؟"),
    "text": T("Today we find the volume of a cube and change cm³ to litres. First, a quick volume check.", "آج ہم مکعب کا حجم نکالیں گے اور مکعب سینٹی میٹر کو لیٹر میں بدلیں گے۔ پہلے حجم کا ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("A box is 3 cm long, 2 cm wide and 5 cm high. What is its volume, in cm³?", "ایک ڈبہ 3 سینٹی میٹر لمبا، 2 سینٹی میٹر چوڑا اور 5 سینٹی میٹر اونچا ہے۔ اس کا حجم کتنے مکعب سینٹی میٹر ہے؟"),
     S2,
     T("Length × breadth × height.", "لمبائی × چوڑائی × اونچائی"),
     T("Right! 30 cm³.", "درست! 30 مکعب سینٹی میٹر"),
     T("3 × 2 × 5 = 30.", "3 × 2 × 5 = 30"),
     common_wrong=[wrong(10, "Multiply, don't add: 3 × 2 × 5 = 30.", "جمع نہیں، ضرب: 3 × 2 × 5 = 30")],
     qtype="recall", skill=SO_VOLUME_CUBOID),
   {"id": "s3_rule", "type": "explain",
    "character": say("happy", "A cube's length, breadth and height are all the same side!", "مکعب کی لمبائی، چوڑائی اور اونچائی سب ایک ہی ضلع ہیں!"),
    "text": T("In a cube, length, breadth and height are equal, so volume = side × side × side. A cube with 10 cm sides has volume 10 × 10 × 10 = 1000 cm³, and that holds exactly 1 litre. So 1 litre = 1000 cm³. To change cm³ to litres, divide by 1000.",
              "مکعب میں لمبائی، چوڑائی اور اونچائی برابر ہوتی ہیں، تو حجم = ضلع × ضلع × ضلع۔ 10 سینٹی میٹر اضلاع والے مکعب کا حجم 10 × 10 × 10 = 1000 مکعب سینٹی میٹر ہے، اور اس میں ٹھیک 1 لیٹر آتا ہے۔ تو 1 لیٹر = 1000 مکعب سینٹی میٹر۔ مکعب سینٹی میٹر کو لیٹر میں بدلنے کے لیے 1000 سے تقسیم کریں۔")},
   number_question(
     "s4_cube3",
     T("A cube has sides of 3 cm. What is its volume, in cm³?", "ایک مکعب کے اضلاع 3 سینٹی میٹر ہیں۔ اس کا حجم کتنے مکعب سینٹی میٹر ہے؟"),
     S4,
     T("3 × 3 × 3.", "3 × 3 × 3"),
     T("Right! 27 cm³.", "درست! 27 مکعب سینٹی میٹر"),
     T("3 × 3 = 9, 9 × 3 = 27.", "3 × 3 = 9، 9 × 3 = 27"),
     common_wrong=[wrong(9, "That is one face, or 3 × 3. Multiply by 3 again: 27.", "یہ ایک سطح ہے یعنی 3 × 3۔ پھر 3 سے ضرب دیں: 27", "face_area")]),
   number_question(
     "s5_cube10",
     T("A cube has sides of 10 cm. What is its volume, in cm³?", "ایک مکعب کے اضلاع 10 سینٹی میٹر ہیں۔ اس کا حجم کتنے مکعب سینٹی میٹر ہے؟"),
     S5,
     T("10 × 10 × 10.", "10 × 10 × 10"),
     T("Right! 1000 cm³, which is 1 litre.", "درست! 1000 مکعب سینٹی میٹر، یعنی 1 لیٹر"),
     T("10 × 10 × 10 = 1000.", "10 × 10 × 10 = 1000"),
     common_wrong=[wrong(100, "That is one face. 10 × 10 × 10 = 1000.", "یہ ایک سطح ہے۔ 10 × 10 × 10 = 1000", "face_area"),
                   wrong(30, "Not 10 × 3. It is 10 × 10 × 10 = 1000.", "10 × 3 نہیں۔ یہ 10 × 10 × 10 = 1000 ہے۔", "times_three")]),
   {"id": "s6_litre", "type": "choice",
    "prompt": T("How many cm³ make 1 litre?", "1 لیٹر میں کتنے مکعب سینٹی میٹر ہوتے ہیں؟"),
    "options": [
      opt("thousand", "1000", "1000", True, "Yes! A 10 cm cube.", "جی ہاں! 10 سینٹی میٹر کا مکعب۔"),
      opt("hundred", "100", "100", False, "That is too few: 1 litre = 1000 cm³.", "یہ بہت کم ہے: 1 لیٹر = 1000 مکعب سینٹی میٹر", "litre_100"),
      opt("ten_thousand", "10000", "10000", False, "That is 10 litres. 1 litre = 1000 cm³.", "یہ 10 لیٹر ہے۔ 1 لیٹر = 1000 مکعب سینٹی میٹر"),
    ]},
   number_question(
     "s7_tank",
     T("A fish tank is 50 cm long, 20 cm wide and 30 cm high. How many litres of water does it hold?", "مچھلیوں کی ٹینکی 50 سینٹی میٹر لمبی، 20 سینٹی میٹر چوڑی اور 30 سینٹی میٹر اونچی ہے۔ اس میں کتنے لیٹر پانی آتا ہے؟"),
     S7,
     T("Find the volume in cm³, then ÷ 1000.", "پہلے مکعب سینٹی میٹر میں حجم نکالیں، پھر ÷ 1000"),
     T("Right! 30000 cm³ = 30 litres.", "درست! 30000 مکعب سینٹی میٹر = 30 لیٹر"),
     T("50 × 20 × 30 = 30000. 30000 ÷ 1000 = 30.", "50 × 20 × 30 = 30000۔ 30000 ÷ 1000 = 30"),
     common_wrong=[wrong(30000, "That is in cm³. Divide by 1000: 30 litres.", "یہ مکعب سینٹی میٹر میں ہے۔ 1000 سے تقسیم کریں: 30 لیٹر"),
                   wrong(300, "1 litre is 1000 cm³, not 100: 30 litres.", "1 لیٹر 1000 مکعب سینٹی میٹر ہے، 100 نہیں: 30 لیٹر", "litre_100")]),
   number_question(
     "s8_cube5",
     T("A wooden block is a cube with 5 cm sides. What is its volume, in cm³?", "لکڑی کا ایک ٹکڑا 5 سینٹی میٹر اضلاع والا مکعب ہے۔ اس کا حجم کتنے مکعب سینٹی میٹر ہے؟"),
     S8,
     T("5 × 5 × 5.", "5 × 5 × 5"),
     T("Right! 125 cm³.", "درست! 125 مکعب سینٹی میٹر"),
     T("5 × 5 = 25, 25 × 5 = 125.", "5 × 5 = 25، 25 × 5 = 125"),
     common_wrong=[wrong(25, "That is one face. Multiply by 5 again: 125.", "یہ ایک سطح ہے۔ پھر 5 سے ضرب دیں: 125", "face_area"),
                   wrong(15, "Not 5 × 3. It is 5 × 5 × 5 = 125.", "5 × 3 نہیں۔ یہ 5 × 5 × 5 = 125 ہے۔", "times_three")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("A cube has 4 cm sides. Usman says its volume is 4 × 4 = 16 cm³. What went wrong?", "ایک مکعب کے اضلاع 4 سینٹی میٹر ہیں۔ عثمان کہتا ہے اس کا حجم 4 × 4 = 16 مکعب سینٹی میٹر ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("third", "He found one face. Volume = 4 × 4 × 4 = 64 cm³.", "اس نے ایک سطح نکالی۔ حجم = 4 × 4 × 4 = 64 مکعب سینٹی میٹر", True,
          "Yes! 16 cubes make one layer, and there are 4 layers.", "جی ہاں! 16 مکعب ایک تہہ بناتے ہیں، اور 4 تہیں ہیں۔"),
      opt("times3", "It should be 4 × 3 = 12.", "یہ 4 × 3 = 12 ہونا چاہیے۔", False,
          "Not × 3. Multiply the side three times: 4 × 4 × 4 = 64.", "× 3 نہیں۔ ضلع کو تین بار ضرب دیں: 4 × 4 × 4 = 64", "times_three"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "4 × 4 is the area of one face. The cube is 4 layers high: 64.", "4 × 4 ایک سطح کا رقبہ ہے۔ مکعب 4 تہیں اونچا ہے: 64", "face_area"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why does a 10 cm cube hold 1000 small cubes, not 100? Can you teach me?",
                     "10 سینٹی میٹر کے مکعب میں 1000 چھوٹے مکعب کیوں آتے ہیں، 100 کیوں نہیں؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why do 1000 one-centimetre cubes fit in a 10 cm cube?", "اپنے الفاظ میں بتائیں: 10 سینٹی میٹر کے مکعب میں 1 سینٹی میٹر کے 1000 مکعب کیوں آتے ہیں؟"),
    "key_idea": "The bottom layer is 10 by 10, so it holds 100 small cubes. The cube is 10 cm high, so there are 10 such layers: 10 × 100 = 1000.",
    "levels": {
      "got_it": "Says one layer is 10 × 10 = 100 cubes, and there are 10 layers, so 1000.",
      "partly": "Says 10 × 10 × 10, without explaining layers.",
      "not_yet": "Gives no reason."},
    "keywords": [
      ["layer", "تہہ", "تہیں"],
      ["100", "hundred", "سو"],
      ["10", "ten", "دس"]],
    "fallback_feedback": {
      "got_it": T("Well explained! 100 cubes in each layer, 10 layers.", "بہت خوب! ہر تہہ میں 100 مکعب، 10 تہیں۔"),
      "partly": T("Good start! Now say how many cubes are in one layer.", "اچھی شروعات! اب بتائیں ایک تہہ میں کتنے مکعب ہیں۔"),
      "not_yet": T("How many small cubes cover the 10 cm by 10 cm bottom? How many layers fit?", "10 × 10 سینٹی میٹر کی تہہ کتنے چھوٹے مکعب ڈھانپتے ہیں؟ کتنی تہیں آتی ہیں؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_water_tank",
     T("A water tank on a roof is 100 cm long, 50 cm wide and 40 cm high. How many litres does it hold?", "چھت پر پانی کی ٹینکی 100 سینٹی میٹر لمبی، 50 سینٹی میٹر چوڑی اور 40 سینٹی میٹر اونچی ہے۔ اس میں کتنے لیٹر آتے ہیں؟"),
     S11,
     T("Volume in cm³, then ÷ 1000.", "مکعب سینٹی میٹر میں حجم، پھر ÷ 1000"),
     T("Right! 200000 cm³ = 200 litres.", "درست! 200000 مکعب سینٹی میٹر = 200 لیٹر"),
     T("100 × 50 × 40 = 200000. 200000 ÷ 1000 = 200.", "100 × 50 × 40 = 200000۔ 200000 ÷ 1000 = 200"),
     common_wrong=[wrong(2000, "1 litre is 1000 cm³, not 100: 200 litres.", "1 لیٹر 1000 مکعب سینٹی میٹر ہے، 100 نہیں: 200 لیٹر", "litre_100"),
                   wrong(200000, "That is in cm³. Divide by 1000: 200 litres.", "یہ مکعب سینٹی میٹر میں ہے۔ 1000 سے تقسیم کریں: 200 لیٹر")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Side times side times side, and 1000 cm³ make a litre!", "ضلع ضرب ضلع ضرب ضلع، اور 1000 مکعب سینٹی میٹر ایک لیٹر!"),
    "text": T("Volume of a cube = side × side × side. 1 litre = 1000 cm³, so to change cm³ to litres, divide by 1000.",
              "مکعب کا حجم = ضلع × ضلع × ضلع۔ 1 لیٹر = 1000 مکعب سینٹی میٹر، تو مکعب سینٹی میٹر کو لیٹر میں بدلنے کے لیے 1000 سے تقسیم کریں۔"),
    "points": [T("Cube: side × side × side.", "مکعب: ضلع × ضلع × ضلع۔"),
               T("1000 cm³ = 1 litre.", "1000 مکعب سینٹی میٹر = 1 لیٹر۔")]},
 ],
 "review_questions": [
   {"id": "r_cube2", "type": "apply", "skill": SKILL, "step": number_question(
     "r_cube2",
     T("A cube has sides of 2 cm. What is its volume, in cm³?", "ایک مکعب کے اضلاع 2 سینٹی میٹر ہیں۔ اس کا حجم کتنے مکعب سینٹی میٹر ہے؟"),
     R1,
     T("2 × 2 × 2.", "2 × 2 × 2"),
     T("Right! 8 cm³.", "درست! 8 مکعب سینٹی میٹر"),
     T("2 × 2 × 2 = 8.", "2 × 2 × 2 = 8"),
     common_wrong=[wrong(6, "Not 2 × 3. It is 2 × 2 × 2 = 8.", "2 × 3 نہیں۔ یہ 2 × 2 × 2 = 8 ہے۔", "times_three"),
                   wrong(4, "That is one face. 2 × 2 × 2 = 8.", "یہ ایک سطح ہے۔ 2 × 2 × 2 = 8", "face_area")],
     qtype=None)},
   {"id": "r_litres", "type": "apply", "skill": SKILL, "step": number_question(
     "r_litres",
     T("A bucket holds 5000 cm³ of water. How many litres is that?", "ایک بالٹی میں 5000 مکعب سینٹی میٹر پانی آتا ہے۔ یہ کتنے لیٹر ہے؟"),
     R2,
     T("Divide by 1000.", "1000 سے تقسیم کریں۔"),
     T("Right! 5 litres.", "درست! 5 لیٹر"),
     T("5000 ÷ 1000 = 5.", "5000 ÷ 1000 = 5"),
     common_wrong=[wrong(50, "1 litre is 1000 cm³, not 100: 5 litres.", "1 لیٹر 1000 مکعب سینٹی میٹر ہے، 100 نہیں: 5 لیٹر", "litre_100")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Solids unit. No textbook text or exercises were used.",
   "The 10 cm cube links cm³ to the litre, which children see on milk and water bottles.",
   "Urdu terms to check: ضلع (side), لیٹر (litre), گنجائش (capacity).",
   "The numbers were worked out in content/sources/g6-maths-14/volume_cube.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)
