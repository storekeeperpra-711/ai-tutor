"""Chapter 8 test (Surface Area and Volume), set out like the book's review
exercise and a board paper: multiple choice, short questions, then longer
problems. The questions are new; only the kinds of question follow the book."""
from common import (T, say, nq, ch, write, book_ref, REVIEW, CHAPTER_8_TEST, CH8_PREREQS,
                    cuboid_volume, cuboid_surface)

SKILL = CHAPTER_8_TEST


def vol(l, b, h):
    return int(cuboid_volume(l, b, h))


def surf(l, b, h):
    return int(cuboid_surface(l, b, h))


def mcq(id, en, ur, right, wrongs, pos):
    return ch(id, ("MCQ: " + en, "کثیر انتخابی: " + ur), right, wrongs, pos, qtype="exam_style")


def short(id, en, ur, answer, hint, good, bad, wrongs=()):
    return nq(id, ("Short question: " + en, "مختصر سوال: " + ur), answer, hint, good, bad, wrongs, qtype="exam_style")


def long_q(id, en, ur, answer, hint, good, bad, wrongs=()):
    return nq(id, ("Long question: " + en, "تفصیلی سوال: " + ur), answer, hint, good, bad, wrongs, qtype="exam_style")


# MCQs
assert vol(2, 2, 2) == 8   # unit of volume is cubic
M2 = 11 * 11
assert M2 == 121 and 4 * 11 == 44 and 2 * 11 == 22
M3 = 2 * (18 + 7)
assert M3 == 50 and 18 * 7 == 126 and 18 + 7 == 25
M4 = 10 * 8 // 2
assert M4 == 40 and 80 // 1 == 80 and 10 + 8 == 18
M5 = surf(3, 3, 3)
assert M5 == 54 and vol(3, 3, 3) == 27 and 9 * 3 == 27 and 6 * 3 == 18
M6 = vol(6, 5, 4)
assert M6 == 120 and 6 + 5 + 4 == 15 and surf(6, 5, 4) == 148
# short questions
S1 = (9 + 15) * 5 // 2
assert (9 + 15) * 5 % 2 == 0 and S1 == 60 and 9 * 15 == 135 and 24 * 5 == 120
S2 = 105 // 15
assert S2 == 7 and 15 * 7 == 105 and 105 - 15 == 90 and 105 * 15 == 1575
S3 = (30 + 2 * 2) * (20 + 2 * 2) - 30 * 20
assert S3 == 216 and 34 * 24 == 816 and 30 * 20 == 600 and (30 + 2) * (20 + 2) - 600 == 104
S4_CM3 = vol(100, 60, 50)
S4 = S4_CM3 // 1000
assert S4_CM3 == 300000 and S4 == 300 and S4_CM3 % 1000 == 0 and S4_CM3 // 100 == 3000
# long questions
L1P = 2 * (36 + 24)
L1 = L1P * 45
assert L1P == 120 and L1 == 5400 and 36 * 24 * 45 == 38880 and L1P // 2 * 45 == 2700
L2A = 14 * 9 - 6 * 4
L2 = L2A * 40
assert L2A == 102 and L2 == 4080 and 14 * 9 == 126 and 14 * 9 + 6 * 4 == 150 and 126 * 40 == 5040
L3A = surf(2, 1, 1)
L3 = L3A * 60
assert L3A == 10 and L3 == 600 and vol(2, 1, 1) == 2 and 2 * 60 == 120 and (2 * 1 + 1 * 1 + 2 * 1) * 60 == 300
L4_CM3 = vol(150, 100, 80)
L4_L = L4_CM3 // 1000
L4 = L4_L // 20
assert L4_CM3 == 1200000 and L4_L == 1200 and L4 == 60 and L4_L % 20 == 0 and L4_CM3 // 20 == 60000
# question bank and review
QB1 = 2 * (12 + 5)
assert QB1 == 34 and 12 * 5 == 60
QB2 = 12 * 7 // 2
assert QB2 == 42 and 12 * 7 == 84
QB3 = vol(5, 4, 3)
assert QB3 == 60 and surf(5, 4, 3) == 94
R1 = 8 * 8
assert R1 == 64 and 4 * 8 == 32
R2 = surf(5, 5, 5)
assert R2 == 150 and vol(5, 5, 5) == 125

lesson = {
 "id": "g6-maths-14-chapter-8-test",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Answer exam-style questions on the whole of chapter 8: perimeter and area of rectangles, squares, triangles, parallelograms and trapeziums, paths and shaded regions, and the surface area and volume of cubes and cuboids.",
                      "textbook": book_ref("Review Exercise 8")}],
 "skills": [SKILL],
 "title": T("Chapter 8 test: Surface area and volume", "باب 8 کا ٹیسٹ: سطحی رقبہ اور حجم"),
 "estimated_minutes": 25,
 "prerequisites": [{"skill": s} for s in CH8_PREREQS],
 "misconceptions": [
   {"id": "perimeter_for_area", "description": "Gives the perimeter when the area is asked, or the other way round, or adds the sides for an area."},
   {"id": "forgets_half", "description": "Gives base × height for a triangle (or the sum × height for a trapezium) without halving."},
   {"id": "path_not_subtracted", "description": "Gives the area of the whole shape (field and path) as the area of the path, or adds the path width only once."},
   {"id": "volume_for_surface", "description": "Gives the volume when the surface area is asked, or the other way round."},
   {"id": "unit_mix", "description": "Gives cm3 as litres, uses a wrong unit, or mixes metres and centimetres."},
   {"id": "cost_uses_wrong_measure", "description": "Uses the area or volume instead of the perimeter or surface area for a cost."},
   {"id": "wrong_inverse", "description": "Multiplies or subtracts instead of dividing to find a missing measurement."},
   {"id": "answer_is_other_quantity", "description": "Stops at a middle step, such as the volume in cm3, and gives it as the answer."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["exam_style"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_exam_perimeter", "type": "exam_style", "step": nq(
     "qb_exam_perimeter", ("Find the perimeter, in cm, of a rectangle 12 cm long and 5 cm wide.", "12 سینٹی میٹر لمبی اور 5 سینٹی میٹر چوڑی مستطیل کا احاطہ سینٹی میٹر میں نکالیں۔"), QB1,
     ("2 × (12 + 5).", "2 × (12 + 5)"),
     ("Correct: 2 × 17 = 34 cm.", "درست: 2 × 17 = 34 سینٹی میٹر"), ("12 + 5 + 12 + 5 = 34.", "12 + 5 + 12 + 5 = 34"),
     [(60, "That is the area. The perimeter is 34 cm.", "یہ رقبہ ہے۔ احاطہ 34 سینٹی میٹر ہے۔", "perimeter_for_area")], qtype=None)},
   {"id": "qb_exam_triangle", "type": "exam_style", "step": nq(
     "qb_exam_triangle", ("Find the area, in cm², of a triangle with base 12 cm and height 7 cm.", "12 سینٹی میٹر قاعدے اور 7 سینٹی میٹر اونچائی والے مثلث کا رقبہ مربع سینٹی میٹر میں نکالیں۔"), QB2,
     ("½ × base × height.", "½ × قاعدہ × اونچائی"),
     ("Correct: ½ × 12 × 7 = 42 cm².", "درست: ½ × 12 × 7 = 42 مربع سینٹی میٹر"), ("12 × 7 = 84, half is 42.", "12 × 7 = 84، آدھا 42"),
     [(84, "You forgot the half: 42.", "آپ آدھا کرنا بھول گئے: 42", "forgets_half")], qtype=None)},
   {"id": "qb_exam_volume", "type": "exam_style", "step": nq(
     "qb_exam_volume", ("Find the volume, in cm³, of a cuboid 5 cm by 4 cm by 3 cm.", "5 ضرب 4 ضرب 3 سینٹی میٹر مستطیلی ڈبے کا حجم مکعب سینٹی میٹر میں نکالیں۔"), QB3,
     ("ℓ × b × h.", "ℓ × b × h"),
     ("Correct: 5 × 4 × 3 = 60 cm³.", "درست: 5 × 4 × 3 = 60 مکعب سینٹی میٹر"), ("5 × 4 = 20, 20 × 3 = 60.", "5 × 4 = 20، 20 × 3 = 60"),
     [(94, "That is the surface area. The volume is 60 cm³.", "یہ سطحی رقبہ ہے۔ حجم 60 مکعب سینٹی میٹر ہے۔", "volume_for_surface")], qtype=None)},
 ]},
 "home_tasks": [{"id": "h_paper", "text": T(
   "Do Review Exercise 8 in your maths book in your notebook, setting out the working the way this test's answers do: write the formula, put in the numbers, work out the answer with its unit. Ask your teacher to check it.",
   "اپنی ریاضی کی کتاب کی اعادی مشق 8 اپنی کاپی میں حل کریں، اور کام اس ٹیسٹ کے جوابات کی طرح لکھیں: کلیہ لکھیں، اعداد رکھیں، اور جواب اکائی کے ساتھ نکالیں۔ اپنے استاد سے جانچ کروائیں۔")}],
 "glossary": [T("Multiple choice", "کثیر انتخابی"), T("Short question", "مختصر سوال"), T("Long question", "تفصیلی سوال"),
              T("Model answer", "نمونہ جواب"), T("Review exercise", "اعادی مشق")],
 "steps": [
   {"id": "s1_paper", "type": "explain",
    "character": say("encouraging", "This is a test of the whole chapter, like the book's review exercise. Read each question carefully!",
                     "یہ پورے باب کا ٹیسٹ ہے، کتاب کی اعادی مشق کی طرح۔ ہر سوال غور سے پڑھیں!"),
    "text": T("This test goes with Review Exercise 8 of your maths book (PCTB Mathematics 6). It has three parts, like an exam paper: multiple choice questions (choose one answer), short questions (a few lines of working), and longer problems (full working in your notebook, then the final answer). The questions are new, not the book's. Write the unit with every answer in your notebook: cm, cm², cm³ or litres.",
              "یہ ٹیسٹ آپ کی ریاضی کی کتاب (پنجاب ٹیکسٹ بک بورڈ، ریاضی 6) کی اعادی مشق 8 کے ساتھ ہے۔ اس کے تین حصے ہیں، امتحانی پرچے کی طرح: کثیر انتخابی سوال (ایک جواب چنیں)، مختصر سوال (چند سطروں کا کام)، اور تفصیلی سوالات (کاپی میں پورا کام، پھر آخری جواب)۔ سوال نئے ہیں، کتاب کے نہیں۔ اپنی کاپی میں ہر جواب کے ساتھ اکائی لکھیں: سینٹی میٹر، مربع سینٹی میٹر، مکعب سینٹی میٹر یا لیٹر۔")},
   mcq("m1_unit", "In which unit is the volume of a box measured?", "ڈبے کا حجم کس اکائی میں ناپا جاتا ہے؟",
       ("cm³", "cm³", "Correct: volume uses cubic units.", "درست: حجم مکعب اکائیوں میں ہوتا ہے۔"),
       [("cm", "cm", "cm measures a length or a perimeter.", "سینٹی میٹر لمبائی یا احاطہ ناپتا ہے۔", "unit_mix"),
        ("cm²", "cm²", "cm² measures an area or a surface.", "مربع سینٹی میٹر رقبہ یا سطح ناپتا ہے۔", "unit_mix"),
        ("kg", "kg", "kg measures mass, not space.", "کلوگرام کمیت ناپتا ہے، جگہ نہیں۔", "unit_mix")], 0),
   mcq("m2_square", "The area of a square of side 11 m is:", "11 میٹر ضلع کے مربع کا رقبہ ہے:",
       ("121 m²", "121 m²", "Correct: 11 × 11 = 121.", "درست: 11 × 11 = 121"),
       [("44 m²", "44 m²", "44 is the perimeter, 4 × 11, and it is in metres.", "44 احاطہ ہے، 4 × 11، اور میٹر میں ہے۔", "perimeter_for_area"),
        ("22 m²", "22 m²", "That is 2 × 11. Multiply the side by itself.", "یہ 2 × 11 ہے۔ ضلع کو اسی سے ضرب دیں۔", "perimeter_for_area"),
        ("121 m", "121 m", "The number is right, but area is in square metres.", "عدد درست ہے، مگر رقبہ مربع میٹر میں ہوتا ہے۔", "unit_mix")], 2),
   mcq("m3_perimeter", "The perimeter of a rectangle 18 cm long and 7 cm wide is:", "18 سینٹی میٹر لمبی اور 7 سینٹی میٹر چوڑی مستطیل کا احاطہ ہے:",
       ("50 cm", "50 cm", "Correct: 2 × (18 + 7) = 50.", "درست: 2 × (18 + 7) = 50"),
       [("126 cm²", "126 cm²", "That is the area.", "یہ رقبہ ہے۔", "perimeter_for_area"),
        ("25 cm", "25 cm", "That is only length plus width. Double it.", "یہ صرف لمبائی جمع چوڑائی ہے۔ دگنا کریں۔", "perimeter_for_area"),
        ("32 cm", "32 cm", "That is 18 + 7 + 7. All four sides: 50.", "یہ 18 + 7 + 7 ہے۔ چاروں اضلاع: 50", "perimeter_for_area")], 1),
   mcq("m4_triangle", "The area of a triangle with base 10 cm and height 8 cm is:", "10 سینٹی میٹر قاعدے اور 8 سینٹی میٹر اونچائی والے مثلث کا رقبہ ہے:",
       ("40 cm²", "40 cm²", "Correct: ½ × 10 × 8 = 40.", "درست: ½ × 10 × 8 = 40"),
       [("80 cm²", "80 cm²", "You forgot the half.", "آپ آدھا کرنا بھول گئے۔", "forgets_half"),
        ("18 cm²", "18 cm²", "That adds the base and height. Multiply and halve.", "یہ قاعدہ اور اونچائی جمع کرتا ہے۔ ضرب دیں اور آدھا کریں۔", "perimeter_for_area"),
        ("20 cm²", "20 cm²", "Half of 40 is too small. ½ × 10 × 8 = 40.", "40 کا آدھا بہت چھوٹا ہے۔ ½ × 10 × 8 = 40", "forgets_half")], 3),
   mcq("m5_cube", "The surface area of a cube of side 3 cm is:", "3 سینٹی میٹر ضلع کے مکعب کا سطحی رقبہ ہے:",
       ("54 cm²", "54 cm²", "Correct: 6 × 3 × 3 = 54.", "درست: 6 × 3 × 3 = 54"),
       [("27 cm²", "27 cm²", "27 is the volume (in cm³).", "27 حجم ہے (مکعب سینٹی میٹر میں)۔", "volume_for_surface"),
        ("9 cm²", "9 cm²", "That is one face. A cube has six.", "یہ ایک سطح ہے۔ مکعب کی چھ ہوتی ہیں۔", "volume_for_surface"),
        ("18 cm²", "18 cm²", "That is 6 × 3. Each face is 3 × 3: 54.", "یہ 6 × 3 ہے۔ ہر سطح 3 × 3 ہے: 54", "volume_for_surface")], 1),
   mcq("m6_volume", "The volume of a cuboid 6 cm by 5 cm by 4 cm is:", "6 ضرب 5 ضرب 4 سینٹی میٹر مستطیلی ڈبے کا حجم ہے:",
       ("120 cm³", "120 cm³", "Correct: 6 × 5 × 4 = 120.", "درست: 6 × 5 × 4 = 120"),
       [("15 cm³", "15 cm³", "That adds the lengths. Multiply.", "یہ لمبائیاں جمع کرتا ہے۔ ضرب دیں۔", "volume_for_surface"),
        ("148 cm³", "148 cm³", "That is the surface area, and in cm².", "یہ سطحی رقبہ ہے، اور مربع سینٹی میٹر میں۔", "volume_for_surface"),
        ("30 cm³", "30 cm³", "That is only the 6 × 5 face. Multiply by 4: 120.", "یہ صرف 6 × 5 والی سطح ہے۔ 4 سے ضرب دیں: 120", "volume_for_surface")], 2),
   {"id": "s_short", "type": "explain",
    "text": T("Short questions. Work each one out in your notebook, then type the answer.",
              "مختصر سوال۔ ہر ایک اپنی کاپی میں حل کریں، پھر جواب لکھیں۔")},
   short("q1_trapezium", "A trapezium has parallel sides of 9 cm and 15 cm and a height of 5 cm. Find its area, in cm².", "ایک ذوزنقہ کے متوازی اضلاع 9 سینٹی میٹر اور 15 سینٹی میٹر ہیں اور اونچائی 5 سینٹی میٹر ہے۔ اس کا رقبہ مربع سینٹی میٹر میں نکالیں۔", S1,
      ("½ × (9 + 15) × 5.", "½ × (9 + 15) × 5"),
      ("Correct: ½ × 24 × 5 = 60 cm².", "درست: ½ × 24 × 5 = 60 مربع سینٹی میٹر"),
      ("Model answer: area = ½ × (9 + 15) × 5 = ½ × 24 × 5 = 60 cm².", "نمونہ جواب: رقبہ = ½ × (9 + 15) × 5 = ½ × 24 × 5 = 60 مربع سینٹی میٹر"),
      [(120, "You forgot the half: 60.", "آپ آدھا کرنا بھول گئے: 60", "forgets_half"),
       (135, "That multiplies the two parallel sides. Add them: 60.", "یہ دونوں متوازی اضلاع کو ضرب دیتا ہے۔ انہیں جمع کریں: 60", "forgets_half")]),
   short("q2_parallelogram", "A parallelogram has an area of 105 cm² and a base of 15 cm. Find its height, in cm.", "ایک متوازی الاضلاع کا رقبہ 105 مربع سینٹی میٹر اور قاعدہ 15 سینٹی میٹر ہے۔ اس کی اونچائی سینٹی میٹر میں نکالیں۔", S2,
      ("Height = area ÷ base.", "اونچائی = رقبہ ÷ قاعدہ"),
      ("Correct: 105 ÷ 15 = 7 cm.", "درست: 105 ÷ 15 = 7 سینٹی میٹر"),
      ("Model answer: area = base × height, so height = 105 ÷ 15 = 7 cm. Check: 15 × 7 = 105.", "نمونہ جواب: رقبہ = قاعدہ × اونچائی، تو اونچائی = 105 ÷ 15 = 7 سینٹی میٹر۔ جانچ: 15 × 7 = 105"),
      [(90, "That takes 15 away. Undo × 15 by dividing: 7.", "یہ 15 تفریق کرتا ہے۔ × 15 کو تقسیم سے ختم کریں: 7", "wrong_inverse"),
       (1575, "That multiplies. Divide: 7.", "یہ ضرب دیتا ہے۔ تقسیم کریں: 7", "wrong_inverse")]),
   short("q3_path", "A field is 30 m by 20 m. A path 2 m wide goes all round it, outside. Find the area of the path, in m².", "ایک کھیت 30 ضرب 20 میٹر ہے۔ اس کے باہر چاروں طرف 2 میٹر چوڑا راستہ ہے۔ راستے کا رقبہ مربع میٹر میں نکالیں۔", S3,
      ("The field with the path is 34 m by 24 m. Take the field away.", "راستے سمیت کھیت 34 ضرب 24 میٹر ہے۔ کھیت کو تفریق کریں۔"),
      ("Correct: 34 × 24 = 816, and 816 − 600 = 216 m².", "درست: 34 × 24 = 816، اور 816 − 600 = 216 مربع میٹر"),
      ("Model answer: outer 34 × 24 = 816 m², field 30 × 20 = 600 m², path = 816 − 600 = 216 m².", "نمونہ جواب: باہر کا حصہ 34 × 24 = 816 مربع میٹر، کھیت 30 × 20 = 600 مربع میٹر، راستہ = 816 − 600 = 216 مربع میٹر"),
      [(816, "That is the field and the path together. Take away the field, 600: 216.", "یہ کھیت اور راستہ دونوں ہیں۔ کھیت، 600، تفریق کریں: 216", "path_not_subtracted"),
       (104, "That adds only 2 m to the length and the width. The path is 2 m wide at both ends, so add 4 m: 216.", "یہ لمبائی اور چوڑائی میں صرف 2 میٹر جمع کرتا ہے۔ راستہ دونوں سروں پر 2 میٹر چوڑا ہے، 4 میٹر جمع کریں: 216", "path_not_subtracted")]),
   short("q4_litres", "A tank is 100 cm long, 60 cm wide and 50 cm high. How many litres of water does it hold when full? (1 litre = 1000 cm³)", "ایک ٹینکی 100 سینٹی میٹر لمبی، 60 سینٹی میٹر چوڑی اور 50 سینٹی میٹر اونچی ہے۔ بھری ہوئی ہو تو اس میں کتنے لیٹر پانی آتا ہے؟ (1 لیٹر = 1000 مکعب سینٹی میٹر)", S4,
      ("Volume in cm³, then divide by 1000.", "حجم مکعب سینٹی میٹر میں، پھر 1000 سے تقسیم کریں۔"),
      ("Correct: 300,000 cm³ ÷ 1000 = 300 litres.", "درست: 300,000 مکعب سینٹی میٹر ÷ 1000 = 300 لیٹر"),
      ("Model answer: V = 100 × 60 × 50 = 300,000 cm³ = 300,000 ÷ 1000 = 300 litres.", "نمونہ جواب: V = 100 × 60 × 50 = 300,000 مکعب سینٹی میٹر = 300,000 ÷ 1000 = 300 لیٹر"),
      [(300000, "That is the volume in cm³. Divide by 1000 for litres: 300.", "یہ حجم مکعب سینٹی میٹر میں ہے۔ لیٹر کے لیے 1000 سے تقسیم کریں: 300", "answer_is_other_quantity"),
       (3000, "That divides by 100. One litre is 1000 cm³: 300.", "یہ 100 سے تقسیم کرتا ہے۔ ایک لیٹر 1000 مکعب سینٹی میٹر ہے: 300", "unit_mix")]),
   {"id": "s_long", "type": "explain",
    "text": T("Longer problems. Write the formula and full working in your notebook, then type the final answer.",
              "تفصیلی سوالات۔ اپنی کاپی میں کلیہ اور پورا کام لکھیں، پھر آخری جواب لکھیں۔")},
   long_q("l1_fence", "A rectangular plot is 36 m long and 24 m wide. A fence is built right round it. The fence costs Rs 45 for each metre. Find the total cost of the fence, in rupees.", "ایک مستطیل پلاٹ 36 میٹر لمبا اور 24 میٹر چوڑا ہے۔ اس کے گرد باڑ بنائی جاتی ہے۔ باڑ کی قیمت فی میٹر 45 روپے ہے۔ باڑ کی کل لاگت روپوں میں نکالیں۔", L1,
      ("Perimeter first, then × 45.", "پہلے احاطہ، پھر × 45"),
      ("Correct: perimeter 120 m, cost 120 × 45 = Rs 5,400.", "درست: احاطہ 120 میٹر، لاگت 120 × 45 = 5,400 روپے"),
      ("Model answer: P = 2 × (36 + 24) = 120 m. Cost = 120 × 45 = Rs 5,400.", "نمونہ جواب: P = 2 × (36 + 24) = 120 میٹر۔ لاگت = 120 × 45 = 5,400 روپے"),
      [(38880, "That uses the area, 864 m². A fence goes round the edge: the perimeter, 120 m, so 5,400.", "یہ رقبہ، 864 مربع میٹر، استعمال کرتا ہے۔ باڑ کنارے کے گرد لگتی ہے: احاطہ، 120 میٹر، یعنی 5,400", "cost_uses_wrong_measure"),
       (2700, "That is half the perimeter. The fence goes right round: 120 m, so 5,400.", "یہ آدھا احاطہ ہے۔ باڑ پورے گرد لگتی ہے: 120 میٹر، یعنی 5,400", "cost_uses_wrong_measure"),
       (120, "120 m is the length of fence. Multiply by Rs 45: 5,400.", "120 میٹر باڑ کی لمبائی ہے۔ 45 روپے سے ضرب دیں: 5,400", "answer_is_other_quantity")]),
   long_q("l2_tiles", "A floor is a rectangle 14 m by 9 m with a rectangular corner, 6 m by 4 m, cut out of it (the floor is L-shaped). Tiles cost Rs 40 for each square metre. Find the cost of tiling the floor, in rupees.", "ایک فرش 14 ضرب 9 میٹر کی مستطیل ہے جس کے ایک کونے سے 6 ضرب 4 میٹر کی مستطیل کاٹ دی گئی ہے (فرش L شکل کا ہے)۔ ٹائل کی قیمت فی مربع میٹر 40 روپے ہے۔ فرش پر ٹائل لگانے کی لاگت روپوں میں نکالیں۔", L2,
      ("Area of the floor = whole rectangle − the corner. Then × 40.", "فرش کا رقبہ = پوری مستطیل − کونا۔ پھر × 40"),
      ("Correct: 126 − 24 = 102 m², and 102 × 40 = Rs 4,080.", "درست: 126 − 24 = 102 مربع میٹر، اور 102 × 40 = 4,080 روپے"),
      ("Model answer: area = 14 × 9 − 6 × 4 = 126 − 24 = 102 m². Cost = 102 × 40 = Rs 4,080.", "نمونہ جواب: رقبہ = 14 × 9 − 6 × 4 = 126 − 24 = 102 مربع میٹر۔ لاگت = 102 × 40 = 4,080 روپے"),
      [(5040, "That tiles the whole 14 by 9 rectangle, with the corner. Take the corner away: 102 m², so 4,080.", "یہ پوری 14 ضرب 9 مستطیل، کونے سمیت، ٹائل کرتا ہے۔ کونا تفریق کریں: 102 مربع میٹر، یعنی 4,080", "path_not_subtracted"),
       (102, "102 m² is the area. Multiply by Rs 40: 4,080.", "102 مربع میٹر رقبہ ہے۔ 40 روپے سے ضرب دیں: 4,080", "answer_is_other_quantity")]),
   long_q("l3_box", "A closed wooden box in the shape of a cuboid is 2 m long, 1 m wide and 1 m high. The outside of the box is painted. The paint costs Rs 60 for each square metre. Find the cost of the paint, in rupees.", "لکڑی کا ایک بند ڈبہ مستطیلی شکل کا ہے جو 2 میٹر لمبا، 1 میٹر چوڑا اور 1 میٹر اونچا ہے۔ ڈبے کا باہر کا حصہ رنگا جاتا ہے۔ رنگ کی قیمت فی مربع میٹر 60 روپے ہے۔ رنگ کی لاگت روپوں میں نکالیں۔", L3,
      ("Surface area = 2 × (2×1 + 1×1 + 2×1). Then × 60.", "سطحی رقبہ = 2 × (2×1 + 1×1 + 2×1)۔ پھر × 60"),
      ("Correct: surface area 10 m², cost 10 × 60 = Rs 600.", "درست: سطحی رقبہ 10 مربع میٹر، لاگت 10 × 60 = 600 روپے"),
      ("Model answer: S = 2 × (2 + 1 + 2) = 10 m². Cost = 10 × 60 = Rs 600.", "نمونہ جواب: S = 2 × (2 + 1 + 2) = 10 مربع میٹر۔ لاگت = 10 × 60 = 600 روپے"),
      [(120, "That uses the volume, 2 m³. Paint covers the outside: 10 m², so 600.", "یہ حجم، 2 مکعب میٹر، استعمال کرتا ہے۔ رنگ باہر کو ڈھانپتا ہے: 10 مربع میٹر، یعنی 600", "cost_uses_wrong_measure"),
       (300, "That is only three faces (5 m²). A closed box has six: 10 m², so 600.", "یہ صرف تین سطحیں ہیں (5 مربع میٹر)۔ بند ڈبے کی چھ ہوتی ہیں: 10 مربع میٹر، یعنی 600", "volume_for_surface")]),
   long_q("l4_buckets", "A tank is 150 cm long, 100 cm wide and 80 cm high. Water is poured into the empty tank from a bucket that holds 20 litres. How many buckets fill the tank exactly? (1 litre = 1000 cm³)", "ایک ٹینکی 150 سینٹی میٹر لمبی، 100 سینٹی میٹر چوڑی اور 80 سینٹی میٹر اونچی ہے۔ ایک خالی ٹینکی میں 20 لیٹر کی بالٹی سے پانی ڈالا جاتا ہے۔ ٹینکی کتنی بالٹیوں سے پوری بھرتی ہے؟ (1 لیٹر = 1000 مکعب سینٹی میٹر)", L4,
      ("Volume in cm³ → litres → divide by 20.", "حجم مکعب سینٹی میٹر میں → لیٹر → 20 سے تقسیم"),
      ("Correct: 1,200,000 cm³ = 1200 litres, and 1200 ÷ 20 = 60 buckets.", "درست: 1,200,000 مکعب سینٹی میٹر = 1200 لیٹر، اور 1200 ÷ 20 = 60 بالٹیاں"),
      ("Model answer: V = 150 × 100 × 80 = 1,200,000 cm³ = 1200 litres. Buckets = 1200 ÷ 20 = 60.", "نمونہ جواب: V = 150 × 100 × 80 = 1,200,000 مکعب سینٹی میٹر = 1200 لیٹر۔ بالٹیاں = 1200 ÷ 20 = 60"),
      [(1200, "1200 is the capacity in litres. Divide by 20 litres per bucket: 60.", "1200 گنجائش لیٹر میں ہے۔ فی بالٹی 20 لیٹر سے تقسیم کریں: 60", "answer_is_other_quantity"),
       (60000, "That divides the volume in cm³ by 20 without changing to litres. 1200 litres ÷ 20 = 60.", "یہ حجم کو مکعب سینٹی میٹر میں 20 سے تقسیم کرتا ہے، لیٹر بنائے بغیر۔ 1200 لیٹر ÷ 20 = 60", "unit_mix")]),
   {"id": "s_end_summary", "type": "summary",
    "character": say("celebrating", "You finished the chapter 8 test. Well done!", "آپ نے باب 8 کا ٹیسٹ مکمل کر لیا۔ شاباش!"),
    "text": T("In the exam: perimeter goes round the edge (cm, m) and is used for fencing; area covers the inside (cm², m²). Triangle: ½ × base × height. Parallelogram: base × height. Trapezium: ½ × (sum of the parallel sides) × height. A path is the big shape minus the small one. Cuboid: V = ℓ × b × h, S = 2 × (ℓb + bh + hℓ); cube: V = ℓ³, S = 6ℓ². Paint and wrapping use the surface area; litres come from volume ÷ 1000. Write the unit with every answer.",
              "امتحان میں: احاطہ کنارے کے گرد ہوتا ہے (سینٹی میٹر، میٹر) اور باڑ کے لیے استعمال ہوتا ہے؛ رقبہ اندر کی جگہ ہے (مربع سینٹی میٹر، مربع میٹر)۔ مثلث: ½ × قاعدہ × اونچائی۔ متوازی الاضلاع: قاعدہ × اونچائی۔ ذوزنقہ: ½ × (متوازی اضلاع کا مجموعہ) × اونچائی۔ راستہ بڑی شکل منفی چھوٹی شکل ہے۔ مستطیلی ڈبہ: V = ℓ × b × h، S = 2 × (ℓb + bh + hℓ)؛ مکعب: V = ℓ³، S = 6ℓ²۔ رنگ اور لپیٹنا سطحی رقبہ استعمال کرتے ہیں؛ لیٹر حجم ÷ 1000 سے ملتے ہیں۔ ہر جواب کے ساتھ اکائی لکھیں۔"),
    "points": [T("Formula, numbers, answer with its unit.", "کلیہ، اعداد، اکائی کے ساتھ جواب۔"),
               T("Fence: perimeter. Paint: surface area. Water: volume.", "باڑ: احاطہ۔ رنگ: سطحی رقبہ۔ پانی: حجم۔")]},
 ],
 "review_questions": [
   {"id": "r_exam_square", "type": "exam_style", "skill": SKILL, "step": nq(
     "r_exam_square", ("Find the area, in cm², of a square of side 8 cm.", "8 سینٹی میٹر ضلع کے مربع کا رقبہ مربع سینٹی میٹر میں نکالیں۔"), R1,
     ("Side × side.", "ضلع × ضلع"),
     ("Correct: 8 × 8 = 64 cm².", "درست: 8 × 8 = 64 مربع سینٹی میٹر"), ("8 × 8 = 64.", "8 × 8 = 64"),
     [(32, "That is the perimeter, 4 × 8. The area is 64.", "یہ احاطہ ہے، 4 × 8۔ رقبہ 64 ہے۔", "perimeter_for_area")], qtype=None)},
   {"id": "r_exam_cube", "type": "exam_style", "skill": SKILL, "step": nq(
     "r_exam_cube", ("Find the surface area, in cm², of a cube of side 5 cm.", "5 سینٹی میٹر ضلع کے مکعب کا سطحی رقبہ مربع سینٹی میٹر میں نکالیں۔"), R2,
     ("Six faces, each 5 × 5.", "چھ سطحیں، ہر ایک 5 × 5"),
     ("Correct: 6 × 25 = 150 cm².", "درست: 6 × 25 = 150 مربع سینٹی میٹر"), ("6 × 25 = 150.", "6 × 25 = 150"),
     [(125, "That is the volume. Surface area: 150.", "یہ حجم ہے۔ سطحی رقبہ: 150", "volume_for_surface")], qtype=None)},
 ],
 "teacher_notes": [
   "A chapter test to use with Review Exercise 8 of the PCTB Mathematics 6 book, in the style of a paper: multiple choice, short questions, then longer problems. Only the kinds of question come from the book; every question, number and story here is new, because the book may not be copied.",
   "It has its own skill (maths.solids.chapter_8_test), with the skills of the Perimeter and area unit and the Solids unit as prerequisites, and is mastered with exam_style questions, like the chapter 5, 6 and 7 tests.",
   "Urdu terms to check: کثیر انتخابی (multiple choice), مختصر سوال / تفصیلی سوال (short / long question), نمونہ جواب (model answer), اعادی مشق (review exercise), all as in the earlier chapter tests; احاطہ, رقبہ, سطحی رقبہ, حجم, ذوزنقہ, مستطیلی ڈبہ and the other measurement words come from the existing lessons. No new Urdu term was invented here.",
   "The numbers were worked out in content/sources/g6-maths-14/chapter_8_test.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}

write(lesson)
