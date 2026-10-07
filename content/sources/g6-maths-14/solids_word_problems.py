from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, SO_PARTS, SO_VOLUME_CUBOID, SO_VOLUME_CUBE, SO_SURFACE_AREA, SO_WORD_PROBLEMS,
                    cuboid_volume, cuboid_surface)

SKILL = SO_WORD_PROBLEMS
CM3_PER_LITRE = 1000

# s2: surface area of a cube of side 2 (volume 8)
S2 = cuboid_surface(2, 2, 2)
assert S2 == 24 and cuboid_volume(2, 2, 2) == 8
# s4: toy box 20 x 10 x 5 (adding gives 35)
S4 = cuboid_volume(20, 10, 5)
assert S4 == 1000 and 20 + 10 + 5 == 35
# s5: tank 80 x 50 x 50 in litres
S5 = cuboid_volume(80, 50, 50) / CM3_PER_LITRE
assert cuboid_volume(80, 50, 50) == 200000 and S5 == 200
# s7: 2 cm cubes in a 10 x 6 x 4 box: 5 x 3 x 2 = 30 (240 / 2 = 120)
S7 = cuboid_volume(10, 6, 4) / cuboid_volume(2, 2, 2)
assert S7 == 30 == (10 // 2) * (6 // 2) * (4 // 2) and cuboid_volume(10, 6, 4) / 2 == 120
# s8: open box (no lid), cube of side 30: 5 faces (all 6 = 5400)
S8 = 5 * 30 * 30
assert S8 == 4500 and cuboid_surface(30, 30, 30) == 5400
# unit test
U1 = 12
assert U1 != 8 and U1 != 6  # edges, not corners or faces
U2 = cuboid_volume(7, 4, 3)
assert U2 == 84 and 7 + 4 + 3 == 14
U3 = 3000 // CM3_PER_LITRE
assert U3 == 3
U4 = cuboid_surface(5, 4, 2)
assert U4 == 76 and 5 * 4 + 4 * 2 + 5 * 2 == 38 and cuboid_volume(5, 4, 2) == 40
U5 = 12 * 250 // CM3_PER_LITRE
assert 12 * 250 == 3000 and U5 == 3
# question bank and review
QB = cuboid_volume(30, 20, 10) / CM3_PER_LITRE
assert cuboid_volume(30, 20, 10) == 6000 and QB == 6
R1 = cuboid_volume(4, 3, 2)
assert R1 == 24 and 4 + 3 + 2 == 9
R2 = cuboid_surface(3, 3, 3)
assert R2 == 54 and cuboid_volume(3, 3, 3) == 27

lesson = {
 "id": "g6-maths-14-solids-word-problems",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Solve real-life problems on volume, capacity and surface area, choosing which one the problem needs.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Solids word problems", "ٹھوس اشکال کے عملی سوال"),
 "estimated_minutes": 18,
 "prerequisites": [{"skill": SO_SURFACE_AREA}, {"skill": SO_VOLUME_CUBE}, {"skill": SO_VOLUME_CUBOID}, {"skill": SO_PARTS}],
 "misconceptions": [
   {"id": "volume_or_area", "description": "Finds surface area when the problem asks how much a box holds, or volume when it asks how much covers it."},
   {"id": "litre_100", "description": "Thinks 100 cm³ (not 1000 cm³) make 1 litre."},
   {"id": "counts_lid", "description": "Counts all 6 faces for an open box with no lid."},
   {"id": "adds_sides", "description": "Adds length, breadth and height instead of multiplying them."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_which", "type": "recall", "step": {
     "id": "qb_which", "type": "choice",
     "prompt": T("To find how much water a tank holds, what do we find?", "یہ معلوم کرنے کے لیے کہ ٹینکی میں کتنا پانی آتا ہے، ہم کیا نکالتے ہیں؟"),
     "options": [
       opt("volume", "Its volume", "اس کا حجم", True,
           "Yes! Volume is the space inside.", "جی ہاں! حجم اندر کی جگہ ہے۔"),
       opt("surface", "Its surface area", "اس کا سطحی رقبہ", False,
           "Surface area is the outside cover. What it holds is the volume.", "سطحی رقبہ باہر کا غلاف ہے۔ جو اس میں آتا ہے وہ حجم ہے۔", "volume_or_area"),
       opt("edges", "The number of edges", "کناروں کی تعداد", False,
           "Edges don't tell how much it holds. Find the volume.", "کنارے نہیں بتاتے کہ اس میں کتنا آتا ہے۔ حجم نکالیں۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("A box is 30 cm long, 20 cm wide and 10 cm high. How many litres of rice does it hold?", "ایک ڈبہ 30 سینٹی میٹر لمبا، 20 سینٹی میٹر چوڑا اور 10 سینٹی میٹر اونچا ہے۔ اس میں کتنے لیٹر چاول آتے ہیں؟"),
     QB,
     T("Volume in cm³, then ÷ 1000.", "مکعب سینٹی میٹر میں حجم، پھر ÷ 1000"),
     T("Right! 6000 cm³ = 6 litres.", "درست! 6000 مکعب سینٹی میٹر = 6 لیٹر"),
     T("30 × 20 × 10 = 6000, and 6000 ÷ 1000 = 6.", "30 × 20 × 10 = 6000، اور 6000 ÷ 1000 = 6"),
     common_wrong=[wrong(60, "1 litre is 1000 cm³, not 100: 6 litres.", "1 لیٹر 1000 مکعب سینٹی میٹر ہے، 100 نہیں: 6 لیٹر", "litre_100"),
                   wrong(6000, "That is in cm³. Divide by 1000: 6 litres.", "یہ مکعب سینٹی میٹر میں ہے۔ 1000 سے تقسیم کریں: 6 لیٹر")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Kamran wants to know how much paint covers a box. He finds l × b × h. What is wrong?", "کامران جاننا چاہتا ہے کہ ایک ڈبے پر کتنا رنگ لگے گا۔ وہ ل × چ × ا نکالتا ہے۔ کیا غلطی ہے؟"),
     "options": [
       opt("surface", "Paint covers the faces, so he needs the surface area.", "رنگ سطحوں پر لگتا ہے، تو اسے سطحی رقبہ چاہیے۔", True,
           "Yes! l × b × h is the space inside, not the outside.", "جی ہاں! ل × چ × ا اندر کی جگہ ہے، باہر نہیں۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "l × b × h is the volume. Paint needs the surface area.", "ل × چ × ا حجم ہے۔ رنگ کے لیے سطحی رقبہ چاہیے۔", "volume_or_area"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_holds", "front": T("How much a box holds?", "ڈبے میں کتنا آتا ہے؟"),
    "back": T("Volume (cm³ or litres).", "حجم (مکعب سینٹی میٹر یا لیٹر)")},
   {"id": "f_covers", "front": T("How much covers a box?", "ڈبے کو کتنا ڈھانپتا ہے؟"),
    "back": T("Surface area (cm²).", "سطحی رقبہ (مربع سینٹی میٹر)")},
 ],
 "home_tasks": [{"id": "h_room", "text": T(
   "Think of your school bag or a cupboard at home. Name one question about it that needs volume, and one that needs surface area.",
   "اپنے سکول بیگ یا گھر کی الماری کے بارے میں سوچیں۔ اس کے بارے میں ایک سوال بتائیں جس کے لیے حجم چاہیے، اور ایک جس کے لیے سطحی رقبہ۔")}],
 "glossary": [T("Volume", "حجم"), T("Surface area", "سطحی رقبہ"), T("Capacity", "گنجائش")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Filling a tank or painting a box? One needs volume, one needs surface area!",
                     "ٹینکی بھرنی ہے یا ڈبہ رنگنا ہے؟ ایک کے لیے حجم چاہیے، ایک کے لیے سطحی رقبہ!"),
    "text": T("Today we solve real problems with boxes and tanks. First decide: does it ask what fits inside (volume) or what covers the outside (surface area)? First, a quick check.", "آج ہم ڈبوں اور ٹینکیوں کے اصل سوال حل کریں گے۔ پہلے فیصلہ کریں: کیا سوال اندر آنے والی چیز (حجم) پوچھتا ہے یا باہر ڈھانپنے والی (سطحی رقبہ)؟ پہلے ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("A cube has 2 cm sides. What is its surface area, in cm²?", "ایک مکعب کے اضلاع 2 سینٹی میٹر ہیں۔ اس کا سطحی رقبہ کتنے مربع سینٹی میٹر ہے؟"),
     S2,
     T("6 × 2 × 2.", "6 × 2 × 2"),
     T("Right! 6 × 4 = 24 cm².", "درست! 6 × 4 = 24 مربع سینٹی میٹر"),
     T("One face is 4 cm², and 6 × 4 = 24.", "ایک سطح 4 مربع سینٹی میٹر ہے، اور 6 × 4 = 24"),
     common_wrong=[wrong(8, "That is the volume. 6 × 4 = 24.", "یہ حجم ہے۔ 6 × 4 = 24", "volume_or_area")],
     qtype="recall", skill=SO_SURFACE_AREA),
   {"id": "s3_rule", "type": "explain",
    "character": say("happy", "Inside means volume. Outside means surface area. Easy!", "اندر یعنی حجم۔ باہر یعنی سطحی رقبہ۔ آسان!"),
    "text": T("Holds, fills, fits inside: find the volume (l × b × h), in cm³, then ÷ 1000 for litres. Covers, paints, wraps: find the surface area, in cm². An open box with no lid has only 5 faces.",
              "رکھتا ہے، بھرتا ہے، اندر آتا ہے: حجم نکالیں (ل × چ × ا)، مکعب سینٹی میٹر میں، پھر لیٹر کے لیے ÷ 1000۔ ڈھانپتا ہے، رنگتا ہے، لپیٹتا ہے: سطحی رقبہ نکالیں، مربع سینٹی میٹر میں۔ بغیر ڈھکن کے کھلے ڈبے کی صرف 5 سطحیں ہوتی ہیں۔")},
   number_question(
     "s4_toy_box",
     T("A toy box is 20 cm long, 10 cm wide and 5 cm high. What is its volume, in cm³?", "کھلونوں کا ڈبہ 20 سینٹی میٹر لمبا، 10 سینٹی میٹر چوڑا اور 5 سینٹی میٹر اونچا ہے۔ اس کا حجم کتنے مکعب سینٹی میٹر ہے؟"),
     S4,
     T("20 × 10 × 5.", "20 × 10 × 5"),
     T("Right! 1000 cm³, that is 1 litre.", "درست! 1000 مکعب سینٹی میٹر، یعنی 1 لیٹر"),
     T("20 × 10 = 200, and 200 × 5 = 1000.", "20 × 10 = 200، اور 200 × 5 = 1000"),
     common_wrong=[wrong(35, "Multiply, don't add: 20 × 10 × 5 = 1000.", "جمع نہیں، ضرب: 20 × 10 × 5 = 1000", "adds_sides"),
                   wrong(200, "That is the bottom only. × 5 high: 1000.", "یہ صرف نچلی سطح ہے۔ × 5 اونچائی: 1000")]),
   number_question(
     "s5_tank",
     T("A water tank is 80 cm long, 50 cm wide and 50 cm high. How many litres does it hold?", "پانی کی ٹینکی 80 سینٹی میٹر لمبی، 50 سینٹی میٹر چوڑی اور 50 سینٹی میٹر اونچی ہے۔ اس میں کتنے لیٹر آتے ہیں؟"),
     S5,
     T("Volume in cm³, then ÷ 1000.", "مکعب سینٹی میٹر میں حجم، پھر ÷ 1000"),
     T("Right! 200000 cm³ = 200 litres.", "درست! 200000 مکعب سینٹی میٹر = 200 لیٹر"),
     T("80 × 50 × 50 = 200000, and 200000 ÷ 1000 = 200.", "80 × 50 × 50 = 200000، اور 200000 ÷ 1000 = 200"),
     common_wrong=[wrong(2000, "1 litre is 1000 cm³, not 100: 200 litres.", "1 لیٹر 1000 مکعب سینٹی میٹر ہے، 100 نہیں: 200 لیٹر", "litre_100"),
                   wrong(200000, "That is in cm³. Divide by 1000: 200 litres.", "یہ مکعب سینٹی میٹر میں ہے۔ 1000 سے تقسیم کریں: 200 لیٹر")]),
   {"id": "s6_which", "type": "choice",
    "prompt": T("Ali wants to cover his book box with brown paper. What should he find?", "علی اپنی کتابوں کے ڈبے پر خاکی کاغذ چڑھانا چاہتا ہے۔ اسے کیا نکالنا چاہیے؟"),
    "options": [
      opt("surface", "The surface area", "سطحی رقبہ", True, "Yes! Paper covers the outside faces.", "جی ہاں! کاغذ باہر کی سطحیں ڈھانپتا ہے۔"),
      opt("volume", "The volume", "حجم", False, "Volume is what fits inside. Paper covers the outside: surface area.", "حجم وہ ہے جو اندر آتا ہے۔ کاغذ باہر ڈھانپتا ہے: سطحی رقبہ", "volume_or_area"),
    ]},
   number_question(
     "s7_small_cubes",
     T("How many 2 cm cubes fit in a box 10 cm long, 6 cm wide and 4 cm high?", "10 سینٹی میٹر لمبے، 6 سینٹی میٹر چوڑے اور 4 سینٹی میٹر اونچے ڈبے میں 2 سینٹی میٹر کے کتنے مکعب آئیں گے؟"),
     S7,
     T("How many fit along each side? 10 ÷ 2, 6 ÷ 2, 4 ÷ 2.", "ہر طرف کتنے آئیں گے؟ 10 ÷ 2، 6 ÷ 2، 4 ÷ 2"),
     T("Right! 5 × 3 × 2 = 30 cubes.", "درست! 5 × 3 × 2 = 30 مکعب"),
     T("5 along, 3 across, 2 up: 5 × 3 × 2 = 30. (Or 240 ÷ 8 = 30.)", "5 لمبائی میں، 3 چوڑائی میں، 2 اوپر: 5 × 3 × 2 = 30۔ (یا 240 ÷ 8 = 30)"),
     common_wrong=[wrong(120, "Each cube is 2 × 2 × 2 = 8 cm³, not 2. 240 ÷ 8 = 30.", "ہر مکعب 2 × 2 × 2 = 8 مکعب سینٹی میٹر ہے، 2 نہیں۔ 240 ÷ 8 = 30"),
                   wrong(240, "240 is the volume in cm³. Each cube is 8 cm³: 30.", "240 مکعب سینٹی میٹر میں حجم ہے۔ ہر مکعب 8 مکعب سینٹی میٹر ہے: 30")]),
   number_question(
     "s8_open_box",
     T("A box with no lid is a cube with 30 cm sides. How much paint covers the outside of it, in cm²?", "بغیر ڈھکن کا ایک ڈبہ 30 سینٹی میٹر اضلاع والا مکعب ہے۔ اس کے باہر کتنے مربع سینٹی میٹر رنگ لگے گا؟"),
     S8,
     T("No lid: only 5 faces of 30 × 30.", "ڈھکن نہیں: 30 × 30 کی صرف 5 سطحیں۔"),
     T("Right! 5 × 900 = 4500 cm².", "درست! 5 × 900 = 4500 مربع سینٹی میٹر"),
     T("One face is 900 cm², and 5 × 900 = 4500.", "ایک سطح 900 مربع سینٹی میٹر ہے، اور 5 × 900 = 4500"),
     common_wrong=[wrong(5400, "There is no lid, so 5 faces, not 6: 4500.", "ڈھکن نہیں، تو 6 نہیں 5 سطحیں: 4500", "counts_lid"),
                   wrong(27000, "That is the volume. Paint covers 5 faces: 4500.", "یہ حجم ہے۔ رنگ 5 سطحوں پر لگتا ہے: 4500", "volume_or_area")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Bilal wants to know how much water a tank holds. He adds up the areas of its 6 faces. What went wrong?", "بلال جاننا چاہتا ہے کہ ٹینکی میں کتنا پانی آتا ہے۔ وہ اس کی 6 سطحوں کے رقبے جمع کرتا ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("volume", "Water fills the inside, so he needs the volume.", "پانی اندر بھرتا ہے، تو اسے حجم چاہیے۔", True,
          "Yes! l × b × h, then ÷ 1000 for litres.", "جی ہاں! ل × چ × ا، پھر لیٹر کے لیے ÷ 1000"),
      opt("five", "He should add only 5 faces.", "اسے صرف 5 سطحیں جمع کرنی چاہییں۔", False,
          "Faces give the outside. Water needs the inside: volume.", "سطحیں باہر بتاتی ہیں۔ پانی کے لیے اندر چاہیے: حجم", "volume_or_area"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "Adding faces gives the surface area. Water needs the volume.", "سطحیں جمع کرنے سے سطحی رقبہ ملتا ہے۔ پانی کے لیے حجم چاہیے۔", "volume_or_area"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "How do you know when to use volume and when to use surface area? Can you teach me?",
                     "آپ کو کیسے پتا چلتا ہے کہ کب حجم اور کب سطحی رقبہ استعمال کرنا ہے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: when do we find volume, and when do we find surface area? Give an example of each.", "اپنے الفاظ میں بتائیں: ہم کب حجم نکالتے ہیں اور کب سطحی رقبہ؟ ہر ایک کی ایک مثال دیں۔"),
    "key_idea": "Volume is the space inside, used for filling or holding (water in a tank). Surface area is the total area of the outside faces, used for covering or painting (wrapping a box).",
    "levels": {
      "got_it": "Says volume is for filling or the inside, surface area is for covering or the outside, with an example of each.",
      "partly": "Explains one of the two, or gives no examples.",
      "not_yet": "Gives no reason."},
    "keywords": [
      ["inside", "fill", "hold", "اندر", "بھر"],
      ["outside", "cover", "paint", "wrap", "باہر", "ڈھانپ", "رنگ"],
      ["volume", "حجم"],
      ["surface", "سطح"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Inside is volume, outside is surface area.", "بہت خوب! اندر حجم ہے، باہر سطحی رقبہ۔"),
      "partly": T("Good start! Now explain the other one too, with an example.", "اچھی شروعات! اب دوسرے کی بھی مثال کے ساتھ وضاحت کریں۔"),
      "not_yet": T("Think of filling a bucket with water and painting a box. Which needs the inside?", "بالٹی میں پانی بھرنے اور ڈبہ رنگنے کا سوچیں۔ کس کے لیے اندر کی جگہ چاہیے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   {"id": "s11_unit_test", "type": "explain",
    "character": say("encouraging", "Test time! Five questions from the whole Solids unit. You can do it!",
                     "ٹیسٹ کا وقت! ٹھوس اشکال کے پورے باب سے پانچ سوال۔ آپ کر سکتے ہیں!"),
    "text": T("This short test has questions on faces and edges, volume, litres, surface area and a real-life problem. Take your time.",
              "اس چھوٹے ٹیسٹ میں سطحوں اور کناروں، حجم، لیٹر، سطحی رقبے اور ایک اصل زندگی کے سوال ہیں۔ آرام سے کریں۔")},
   number_question(
     "u1_edges",
     T("Test 1: How many edges does a cuboid have?", "ٹیسٹ 1: مستطیلی ڈبے کے کتنے کنارے ہوتے ہیں؟"),
     U1,
     T("4 on top, 4 at the bottom, 4 standing up.", "4 اوپر، 4 نیچے، 4 کھڑے۔"),
     T("Right! 12 edges.", "درست! 12 کنارے"),
     T("4 + 4 + 4 = 12.", "4 + 4 + 4 = 12"),
     common_wrong=[wrong(8, "8 is the corners. Edges: 4 + 4 + 4 = 12.", "8 کونے ہیں۔ کنارے: 4 + 4 + 4 = 12"),
                   wrong(6, "6 is the faces. Edges: 12.", "6 سطحیں ہیں۔ کنارے: 12")],
     qtype="recall", skill=SO_PARTS),
   number_question(
     "u2_volume",
     T("Test 2: A box is 7 cm long, 4 cm wide and 3 cm high. What is its volume, in cm³?", "ٹیسٹ 2: ایک ڈبہ 7 سینٹی میٹر لمبا، 4 سینٹی میٹر چوڑا اور 3 سینٹی میٹر اونچا ہے۔ اس کا حجم کتنے مکعب سینٹی میٹر ہے؟"),
     U2,
     T("7 × 4 × 3.", "7 × 4 × 3"),
     T("Right! 84 cm³.", "درست! 84 مکعب سینٹی میٹر"),
     T("7 × 4 = 28, and 28 × 3 = 84.", "7 × 4 = 28، اور 28 × 3 = 84"),
     common_wrong=[wrong(14, "Multiply, don't add: 7 × 4 × 3 = 84.", "جمع نہیں، ضرب: 7 × 4 × 3 = 84", "adds_sides")],
     qtype="apply", skill=SO_VOLUME_CUBOID),
   number_question(
     "u3_litres",
     T("Test 3: A jug holds 3000 cm³. How many litres is that?", "ٹیسٹ 3: ایک جگ میں 3000 مکعب سینٹی میٹر آتا ہے۔ یہ کتنے لیٹر ہے؟"),
     U3,
     T("Divide by 1000.", "1000 سے تقسیم کریں۔"),
     T("Right! 3 litres.", "درست! 3 لیٹر"),
     T("3000 ÷ 1000 = 3.", "3000 ÷ 1000 = 3"),
     common_wrong=[wrong(30, "1 litre is 1000 cm³, not 100: 3 litres.", "1 لیٹر 1000 مکعب سینٹی میٹر ہے، 100 نہیں: 3 لیٹر", "litre_100")],
     qtype="apply", skill=SO_VOLUME_CUBE),
   number_question(
     "u4_surface",
     T("Test 4: A box is 5 cm long, 4 cm wide and 2 cm high. What is its surface area, in cm²?", "ٹیسٹ 4: ایک ڈبہ 5 سینٹی میٹر لمبا، 4 سینٹی میٹر چوڑا اور 2 سینٹی میٹر اونچا ہے۔ اس کا سطحی رقبہ کتنے مربع سینٹی میٹر ہے؟"),
     U4,
     T("5 × 4, 4 × 2 and 5 × 2. Add, then double.", "5 × 4، 4 × 2 اور 5 × 2۔ جمع کریں، پھر دگنا کریں۔"),
     T("Right! 2 × 38 = 76 cm².", "درست! 2 × 38 = 76 مربع سینٹی میٹر"),
     T("20 + 8 + 10 = 38, and 2 × 38 = 76.", "20 + 8 + 10 = 38، اور 2 × 38 = 76"),
     common_wrong=[wrong(38, "That is 3 faces. Double it: 76.", "یہ 3 سطحیں ہیں۔ دگنا کریں: 76"),
                   wrong(40, "That is the volume. Add the faces: 76.", "یہ حجم ہے۔ سطحیں جمع کریں: 76", "volume_or_area")],
     qtype="apply", skill=SO_SURFACE_AREA),
   number_question(
     "u5_juice",
     T("Test 5: A carton has 12 juice packs. Each pack holds 250 cm³. How many litres of juice are in the carton?", "ٹیسٹ 5: ایک کارٹن میں جوس کے 12 ڈبے ہیں۔ ہر ڈبے میں 250 مکعب سینٹی میٹر جوس ہے۔ کارٹن میں کل کتنے لیٹر جوس ہے؟"),
     U5,
     T("12 × 250 first, then ÷ 1000.", "پہلے 12 × 250، پھر ÷ 1000"),
     T("Right! 3000 cm³ = 3 litres.", "درست! 3000 مکعب سینٹی میٹر = 3 لیٹر"),
     T("12 × 250 = 3000, and 3000 ÷ 1000 = 3.", "12 × 250 = 3000، اور 3000 ÷ 1000 = 3"),
     common_wrong=[wrong(30, "1 litre is 1000 cm³, not 100: 3 litres.", "1 لیٹر 1000 مکعب سینٹی میٹر ہے، 100 نہیں: 3 لیٹر", "litre_100"),
                   wrong(3000, "That is in cm³. Divide by 1000: 3 litres.", "یہ مکعب سینٹی میٹر میں ہے۔ 1000 سے تقسیم کریں: 3 لیٹر")],
     qtype="apply"),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Solids unit complete! Inside is volume, outside is surface area.", "ٹھوس اشکال کا باب مکمل! اندر حجم ہے، باہر سطحی رقبہ۔"),
    "text": T("First decide what the problem asks. Filling or holding: volume, in cm³ or litres (÷ 1000). Covering or painting: surface area, in cm². Check for a missing lid.",
              "پہلے فیصلہ کریں کہ سوال کیا پوچھتا ہے۔ بھرنا یا رکھنا: حجم، مکعب سینٹی میٹر یا لیٹر میں (÷ 1000)۔ ڈھانپنا یا رنگنا: سطحی رقبہ، مربع سینٹی میٹر میں۔ ڈھکن نہ ہو تو دھیان رکھیں۔"),
    "points": [T("Holds or fills: volume.", "رکھتا یا بھرتا: حجم۔"),
               T("Covers or paints: surface area.", "ڈھانپتا یا رنگتا: سطحی رقبہ۔")]},
 ],
 "review_questions": [
   {"id": "r_cubes", "type": "apply", "skill": SKILL, "step": number_question(
     "r_cubes",
     T("How many 1 cm cubes fill a box 4 cm long, 3 cm wide and 2 cm high?", "4 سینٹی میٹر لمبے، 3 سینٹی میٹر چوڑے اور 2 سینٹی میٹر اونچے ڈبے کو 1 سینٹی میٹر کے کتنے مکعب بھریں گے؟"),
     R1,
     T("4 × 3 × 2.", "4 × 3 × 2"),
     T("Right! 24 cubes.", "درست! 24 مکعب"),
     T("4 × 3 = 12 in a layer, 2 layers: 24.", "ایک تہہ میں 4 × 3 = 12، 2 تہیں: 24"),
     common_wrong=[wrong(9, "Multiply, don't add: 4 × 3 × 2 = 24.", "جمع نہیں، ضرب: 4 × 3 × 2 = 24", "adds_sides"),
                   wrong(12, "That is one layer. There are 2 layers: 24.", "یہ ایک تہہ ہے۔ 2 تہیں ہیں: 24")],
     qtype=None)},
   {"id": "r_paint", "type": "apply", "skill": SKILL, "step": number_question(
     "r_paint",
     T("Zara paints all 6 faces of a wooden cube with 3 cm sides. How many cm² does she paint?", "زارا 3 سینٹی میٹر اضلاع والے لکڑی کے مکعب کی تمام 6 سطحیں رنگتی ہے۔ وہ کتنے مربع سینٹی میٹر رنگتی ہے؟"),
     R2,
     T("6 × 3 × 3.", "6 × 3 × 3"),
     T("Right! 6 × 9 = 54 cm².", "درست! 6 × 9 = 54 مربع سینٹی میٹر"),
     T("One face is 9 cm², and 6 × 9 = 54.", "ایک سطح 9 مربع سینٹی میٹر ہے، اور 6 × 9 = 54"),
     common_wrong=[wrong(27, "That is the volume. Paint covers faces: 54.", "یہ حجم ہے۔ رنگ سطحوں پر لگتا ہے: 54", "volume_or_area")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Solids unit. No textbook text or exercises were used.",
   "The key skill is deciding between volume (inside: holds, fills) and surface area (outside: covers, paints).",
   "The five-question unit test at the end covers every lesson of the unit.",
   "The numbers were worked out in content/sources/g6-maths-14/solids_word_problems.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)
