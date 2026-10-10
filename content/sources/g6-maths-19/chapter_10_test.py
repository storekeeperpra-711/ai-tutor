"""Chapter 10 test (Geometrical Constructions), set out like the book's review
exercise and a board paper: multiple choice, short questions, then longer
problems. The questions are new; only the kinds of question follow the book."""
from common import (T, say, nq, ch, write, book_ref, REVIEW, CHAPTER_10_TEST, CH10_PREREQS)
from figs import fig, with_fig, line_fig, tri_fig

SKILL = CHAPTER_10_TEST
LINE = TRI = 180


def mcq(id, en, ur, right, wrongs, pos):
    return ch(id, ("MCQ: " + en, "کثیر انتخابی: " + ur), right, wrongs, pos, qtype="exam_style")


def short(id, en, ur, answer, hint, good, bad, wrongs=()):
    return nq(id, ("Short question: " + en, "مختصر سوال: " + ur), answer, hint, good, bad, wrongs, qtype="exam_style")


def long_q(id, en, ur, answer, hint, good, bad, wrongs=()):
    return nq(id, ("Long question: " + en, "تفصیلی سوال: " + ur), answer, hint, good, bad, wrongs, qtype="exam_style")


# how the angles are built from 60
def mid(a, b):
    assert (a + b) % 2 == 0
    return (a + b) // 2
assert mid(60, 90) == 75 and mid(90, 120) == 105 and mid(60, 120) == 90 and mid(0, 90) == 45

# MCQs
M2_AB = 14
assert M2_AB / 2 == 7
M4_A = 128
M4 = LINE - M4_A
assert M4 == 52 and M4_A + M4 == LINE and 360 - M4_A == 232
M4_FIG = line_fig([M4], ["x", f"{M4_A}°"],
    "A straight line with a point O on it and a ray from O. The angle on the right of the ray is marked x and the angle on the left is marked 128 degrees.",
    "ایک سیدھی لکیر جس پر نقطہ O ہے اور O سے ایک شعاع۔ شعاع کے دائیں طرف کا زاویہ x اور بائیں طرف کا زاویہ 128° لکھا ہے۔")
M5_A, M5_B = 50, 60
M5 = TRI - M5_A - M5_B
assert M5 == 70 and M5_A + M5_B + M5 == TRI and M5_A + M5_B == 110
M5_FIG = tri_fig(M5_A, M5_B, [f"{M5_A}°", f"{M5_B}°", "x"],
    "A triangle ABC with the angle at A marked 50 degrees, the angle at B marked 60 degrees and the angle at C marked x.",
    "مثلث ABC جس میں A پر زاویہ 50°، B پر زاویہ 60° اور C پر زاویہ x لکھا ہے۔")
# short questions
S1_AB = 46
S1 = S1_AB // 2
assert S1 == 23 and 2 * S1 == S1_AB
S2_ANGLE = 140
S2 = S2_ANGLE // 2 // 2
assert S2 == 35 and S2_ANGLE // 2 == 70 and 4 * S2 == S2_ANGLE
S3_A, S3_B = 48, 77
S3 = LINE - S3_A - S3_B
assert S3 == 55 and S3_A + S3_B + S3 == LINE and S3_A + S3_B == 125
S3_FIG = line_fig([S3_A, S3_A + S3], [f"{S3_A}°", "x", f"{S3_B}°"],
    "A straight line with a point O on it and two rays from O that split the line into three angles. From the right they are marked 48 degrees, x and 77 degrees.",
    "ایک سیدھی لکیر جس پر نقطہ O ہے اور O سے دو شعاعیں جو لکیر کو تین زاویوں میں بانٹتی ہیں۔ دائیں سے بائیں یہ 48°، x اور 77° ہیں۔")
S4_BASE = 55
S4 = TRI - 2 * S4_BASE
assert S4 == 70 and 2 * S4_BASE + S4 == TRI and 2 * S4_BASE == 110
# long questions
# AM = 3x - 4, MB = x + 8: M is the midpoint so they are equal
L1_X = (8 + 4) // 2
assert 3 * L1_X - 4 == L1_X + 8 and L1_X == 6 and (8 + 4) % 2 == 0
L1_HALF = L1_X + 8
L1 = 2 * L1_HALF
assert L1_HALF == 14 and L1 == 28 and 3 * L1_X - 4 == 14
# 45 = bisect 90; 105 = halfway between 90 and 120; angle between the two rays
L2_A, L2_B = mid(0, 90), mid(90, 120)
L2 = L2_B - L2_A
assert (L2_A, L2_B) == (45, 105) and L2 == 60 and L2_A + L2_B == 150 and L2_B - 90 == 15
# x, 2x and 3x on a straight line: the largest
L3_X = LINE // (1 + 2 + 3)
L3 = 3 * L3_X
assert L3_X == 30 and L3 == 90 and L3_X + 2 * L3_X + 3 * L3_X == LINE and 2 * L3_X == 60
L3_FIG = line_fig([L3_X, 3 * L3_X], ["x°", "2x°", "3x°"],
    "A straight line with a point O on it and two rays from O that split the line into three angles. From the right they are marked x, 2x and 3x degrees.",
    "ایک سیدھی لکیر جس پر نقطہ O ہے اور O سے دو شعاعیں جو لکیر کو تین زاویوں میں بانٹتی ہیں۔ دائیں سے بائیں یہ x°، 2x° اور 3x° ہیں۔")
# exterior angle 120 = (2x + 10) + (x + 20)
EXT = 120
L4_X = (EXT - 10 - 20) // 3
assert L4_X == 30 and (EXT - 30) % 3 == 0 and (2 * L4_X + 10) + (L4_X + 20) == EXT
L4_BIG = 2 * L4_X + 10
L4_SMALL = L4_X + 20
L4 = L4_BIG
assert L4 == 70 and L4_SMALL == 50 and L4_BIG + L4_SMALL + (LINE - EXT) == TRI and LINE - EXT == 60
# question bank and review
QB1 = 20 // 2
assert QB1 == 10
QB2 = LINE - 100
assert QB2 == 80
QB3 = TRI // 3
assert QB3 == 60
R1 = 90 // 2
assert R1 == 45
R2 = TRI - 90 - 30
assert R2 == 60

lesson = {
 "id": "g6-maths-19-chapter-10-test",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Answer exam-style questions on the whole of chapter 10: drawing a segment, the perpendicular bisector, perpendiculars from a point, bisecting angles, building 30° to 150° with a compass, and finding unknown angles on a straight line and in a triangle.",
                      "textbook": book_ref("Review Exercise 10")}],
 "skills": [SKILL],
 "title": T("Chapter 10 test: Geometrical Constructions", "باب 10 کا ٹیسٹ: ہندسی تعمیرات"),
 "estimated_minutes": 25,
 "prerequisites": [{"skill": s} for s in CH10_PREREQS],
 "misconceptions": [
   {"id": "bisector_mix", "description": "Mixes up a bisector and a perpendicular bisector, or the half of a segment with the whole segment."},
   {"id": "opening_wrong", "description": "Thinks the compass can be opened to half of AB or less to bisect AB."},
   {"id": "bisect_not_half", "description": "Does not halve when bisecting, or halves only once when two bisections are made."},
   {"id": "add_not_mid", "description": "Adds the two angles instead of going halfway between them, or gives half the gap instead of the angle from the base arm."},
   {"id": "use_360", "description": "Uses 360° or 90° for angles on a straight line or in a triangle instead of 180°."},
   {"id": "stops_at_sum", "description": "Adds the known angles and gives that sum as the answer, or takes away only one of them from 180°."},
   {"id": "equation_wrong", "description": "Sets up or solves the equation for x wrongly, or gives x when the angle is asked."},
   {"id": "answer_is_other_quantity", "description": "Stops at a middle step, such as the value of x, and gives it as the answer."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["exam_style"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_exam_half", "type": "exam_style", "step": nq(
     "qb_exam_half", ("The perpendicular bisector of a segment 20 cm long meets it at M. How long is one half, in cm?", "20 سینٹی میٹر لمبے قطعۂ خط کا عمودی ناصف اسے M پر ملتا ہے۔ ایک آدھا حصہ کتنے سینٹی میٹر ہے؟"), QB1,
     ("M is the midpoint.", "M درمیانی نقطہ ہے۔"),
     ("Correct: 20 ÷ 2 = 10 cm.", "درست: 20 ÷ 2 = 10 سینٹی میٹر"), ("Two equal halves: 10.", "دو برابر آدھے: 10"),
     [(20, "20 cm is the whole segment. Half: 10.", "20 سینٹی میٹر پورا قطعۂ خط ہے۔ آدھا: 10", "bisector_mix")], qtype=None)},
   {"id": "qb_exam_line", "type": "exam_style", "step": nq(
     "qb_exam_line", ("Two angles are on a straight line. One is 100°. Find the other, in degrees.", "ایک سیدھی لکیر پر دو زاویے ہیں۔ ایک 100° کا ہے۔ دوسرا کتنے درجے کا ہے؟"), QB2,
     ("The two add up to 180°.", "دونوں کا مجموعہ 180° ہے۔"),
     ("Correct: 180° − 100° = 80°.", "درست: 180° − 100° = 80°"), ("100 + x = 180, so x = 80.", "100 + x = 180، تو x = 80"),
     [(260, "That is 360 − 100. A straight line is 180°: 80.", "یہ 360 − 100 ہے۔ سیدھی لکیر 180° ہے: 80", "use_360")], qtype=None)},
   {"id": "qb_exam_equilateral", "type": "exam_style", "step": nq(
     "qb_exam_equilateral", ("How big is each angle of an equilateral triangle, in degrees?", "مساوی الاضلاع مثلث کا ہر زاویہ کتنے درجے کا ہے؟"), QB3,
     ("Three equal angles that add up to 180°.", "تین برابر زاویے جن کا مجموعہ 180° ہے۔"),
     ("Correct: 180 ÷ 3 = 60°.", "درست: 180 ÷ 3 = 60°"), ("180 ÷ 3 = 60.", "180 ÷ 3 = 60"),
     [(90, "90° is a right angle. Divide 180 by 3: 60.", "90° قائمہ زاویہ ہے۔ 180 کو 3 سے تقسیم کریں: 60", "use_360")], qtype=None)},
 ]},
 "home_tasks": [{"id": "h_paper", "text": T(
   "Do Review Exercise 10 in your maths book in your notebook, setting out the working the way this test's answers do: write the rule you use, put in the numbers, work out the answer with its unit or degrees. Draw the constructions with ruler and compass. Ask your teacher to check it.",
   "اپنی ریاضی کی کتاب کی اعادی مشق 10 اپنی کاپی میں حل کریں، اور کام اس ٹیسٹ کے جوابات کی طرح لکھیں: جو اصول استعمال کریں وہ لکھیں، اعداد رکھیں، اور جواب اکائی یا ڈگری کے ساتھ نکالیں۔ تعمیرات پیمانے اور پرکار سے بنائیں۔ اپنے استاد سے جانچ کروائیں۔")}],
 "glossary": [T("Multiple choice", "کثیر انتخابی"), T("Short question", "مختصر سوال"), T("Long question", "تفصیلی سوال"),
              T("Model answer", "نمونہ جواب"), T("Review exercise", "اعادی مشق")],
 "steps": [
   {"id": "s1_paper", "type": "explain",
    "character": say("encouraging", "This is a test of the whole chapter, like the book's review exercise. Read each question carefully!",
                     "یہ پورے باب کا ٹیسٹ ہے، کتاب کی اعادی مشق کی طرح۔ ہر سوال غور سے پڑھیں!"),
    "text": T("This test goes with Review Exercise 10 of your maths book (PCTB Mathematics 6). It has three parts, like an exam paper: multiple choice questions (choose one answer), short questions (a few lines of working), and longer problems (full working in your notebook, then the final answer). The questions are new, not the book's. Write the unit with every answer in your notebook: degrees or cm.",
              "یہ ٹیسٹ آپ کی ریاضی کی کتاب (پنجاب ٹیکسٹ بک بورڈ، ریاضی 6) کی اعادی مشق 10 کے ساتھ ہے۔ اس کے تین حصے ہیں، امتحانی پرچے کی طرح: کثیر انتخابی سوال (ایک جواب چنیں)، مختصر سوال (چند سطروں کا کام)، اور تفصیلی سوالات (کاپی میں پورا کام، پھر آخری جواب)۔ سوال نئے ہیں، کتاب کے نہیں۔ اپنی کاپی میں ہر جواب کے ساتھ اکائی لکھیں: ڈگری یا سینٹی میٹر۔")},
   mcq("m1_pb", "Every point on the perpendicular bisector of AB is:", "AB کے عمودی ناصف کا ہر نقطہ:",
       ("the same distance from A and from B", "A اور B سے برابر فاصلے پر ہے", "Correct: the arcs from A and B had the same opening.", "درست: A اور B کی قوسوں کا کھلاؤ برابر تھا۔"),
       [("closer to A than to B", "A کے B سے زیادہ قریب ہے", "The bisector sits exactly in the middle, so no point is closer to one end.", "ناصف ٹھیک بیچ میں ہے، تو کوئی نقطہ کسی ایک سرے کے زیادہ قریب نہیں۔", "bisector_mix"),
        ("at 45° to AB", "AB سے 45° پر ہے", "A perpendicular bisector meets AB at 90°.", "عمودی ناصف AB سے 90° پر ملتا ہے۔", "bisector_mix"),
        ("on the line AB", "لکیر AB پر ہے", "Only M is on AB. The other points lie above and below it.", "صرف M لکیر AB پر ہے۔ باقی نقطے اس کے اوپر اور نیچے ہیں۔", "bisector_mix")], 0),
   mcq("m2_opening", "To bisect AB, 14 cm long, the compass is opened:", "14 سینٹی میٹر لمبے AB کی تنصیف کے لیے پرکار کھولا جاتا ہے:",
       ("more than 7 cm, the same for both arcs", "7 سینٹی میٹر سے زیادہ، دونوں قوسوں کے لیے ایک جتنا", "Correct: more than half of AB, and equal for both arcs.", "درست: AB کے آدھے سے زیادہ، اور دونوں قوسوں کے لیے برابر۔"),
       [("exactly 7 cm", "ٹھیک 7 سینٹی میٹر", "With exactly half the arcs only touch at M and do not cross.", "ٹھیک آدھے پر قوسیں صرف M کو چھوتی ہیں، کاٹتی نہیں۔", "opening_wrong"),
        ("less than 7 cm", "7 سینٹی میٹر سے کم", "The arcs would stop short and never meet.", "قوسیں پہلے رک جائیں گی اور کبھی نہیں ملیں گی۔", "opening_wrong"),
        ("any opening, even 1 cm", "کوئی بھی کھلاؤ، 1 سینٹی میٹر بھی", "A small opening gives arcs that do not meet.", "چھوٹے کھلاؤ سے قوسیں نہیں ملتیں۔", "opening_wrong")], 2),
   mcq("m3_75", "An angle of 75° is built by making a ray:", "75° کا زاویہ بنانے کے لیے شعاع بنائی جاتی ہے:",
       ("halfway between the 60° ray and the 90° ray", "60° اور 90° کی شعاعوں کے ٹھیک بیچ میں", "Correct: (60 + 90) ÷ 2 = 75.", "درست: (60 + 90) ÷ 2 = 75"),
       [("halfway between the 90° ray and the 120° ray", "90° اور 120° کی شعاعوں کے ٹھیک بیچ میں", "That gives 105°.", "اس سے 105° ملتا ہے۔", "add_not_mid"),
        ("by bisecting the 60° angle", "60° کے زاویے کی تنصیف سے", "That gives 30°.", "اس سے 30° ملتا ہے۔", "bisect_not_half"),
        ("by bisecting the 120° angle", "120° کے زاویے کی تنصیف سے", "That gives 60°.", "اس سے 60° ملتا ہے۔", "bisect_not_half")], 1),
   with_fig(mcq("m4_line", "Two angles on a straight line are 128° and x. Then x is:", "ایک سیدھی لکیر پر دو زاویے 128° اور x ہیں۔ تو x ہے:",
       ("52°", "52°", "Correct: 180° − 128° = 52°.", "درست: 180° − 128° = 52°"),
       [("232°", "232°", "That is 360° − 128°. A straight line adds to 180°.", "یہ 360° − 128° ہے۔ سیدھی لکیر کا مجموعہ 180° ہے۔", "use_360"),
        ("128°", "128°", "That is the angle we already know.", "یہ وہ زاویہ ہے جو ہمیں پہلے سے معلوم ہے۔", "stops_at_sum"),
        ("38°", "38°", "That is 90° − 52°. The total on a line is 180°, so x = 52°.", "یہ 90° − 52° ہے۔ لکیر پر مجموعہ 180° ہے، تو x = 52°", "use_360")], 3), M4_FIG),
   with_fig(mcq("m5_triangle", "Two angles of a triangle are 50° and 60°. The third angle x is:", "ایک مثلث کے دو زاویے 50° اور 60° ہیں۔ تیسرا زاویہ x ہے:",
       ("70°", "70°", "Correct: 180° − 110° = 70°.", "درست: 180° − 110° = 70°"),
       [("110°", "110°", "That is 50° + 60°. Take it away from 180°.", "یہ 50° + 60° ہے۔ اسے 180° میں سے گھٹائیں۔", "stops_at_sum"),
        ("250°", "250°", "That is 360° − 110°. A triangle adds to 180°.", "یہ 360° − 110° ہے۔ مثلث کا مجموعہ 180° ہے۔", "use_360"),
        ("130°", "130°", "That is 180° − 50°. Take away both angles.", "یہ 180° − 50° ہے۔ دونوں زاویے گھٹائیں۔", "stops_at_sum")], 1), M5_FIG),
   mcq("m6_105", "Which construction gives 105°?", "کون سی تعمیر 105° دیتی ہے؟",
       ("A ray halfway between the 90° ray and the 120° ray", "90° اور 120° کی شعاعوں کے ٹھیک بیچ میں شعاع", "Correct: (90 + 120) ÷ 2 = 105.", "درست: (90 + 120) ÷ 2 = 105"),
       [("Bisect the 90° angle", "90° کے زاویے کی تنصیف", "That gives 45°.", "اس سے 45° ملتا ہے۔", "bisect_not_half"),
        ("A ray halfway between the 60° ray and the 90° ray", "60° اور 90° کی شعاعوں کے ٹھیک بیچ میں شعاع", "That gives 75°.", "اس سے 75° ملتا ہے۔", "add_not_mid"),
        ("Two steps of 60°", "60° کے دو قدم", "That gives 120°.", "اس سے 120° ملتا ہے۔", "add_not_mid")], 0),
   {"id": "s_short", "type": "explain",
    "text": T("Short questions. Work each one out in your notebook, then type the answer.",
              "مختصر سوال۔ ہر ایک اپنی کاپی میں حل کریں، پھر جواب لکھیں۔")},
   short("q1_half", "The perpendicular bisector of a segment AB, 46 cm long, meets AB at M. Find AM, in cm.", "46 سینٹی میٹر لمبے قطعۂ خط AB کا عمودی ناصف AB کو M پر ملتا ہے۔ AM سینٹی میٹر میں نکالیں۔",
      S1, ("M is the midpoint of AB.", "M، AB کا درمیانی نقطہ ہے۔"),
      ("Correct: 46 ÷ 2 = 23 cm.", "درست: 46 ÷ 2 = 23 سینٹی میٹر"),
      ("Model answer: the perpendicular bisector cuts AB into two equal parts, so AM = 46 ÷ 2 = 23 cm.", "نمونہ جواب: عمودی ناصف AB کو دو برابر حصوں میں کاٹتا ہے، تو AM = 46 ÷ 2 = 23 سینٹی میٹر"),
      [(46, "46 cm is the whole of AB. AM is half: 23.", "46 سینٹی میٹر پورا AB ہے۔ AM آدھا ہے: 23", "bisector_mix"),
       (92, "That doubles AB. Halve it: 23.", "یہ AB کو دگنا کرتا ہے۔ آدھا کریں: 23", "bisector_mix")]),
   short("q2_twice", "A 140° angle is bisected, and then one of the two parts is bisected again. Find the size of the smallest angle, in degrees.", "140° کے زاویے کی تنصیف کی جاتی ہے، پھر اس کے دو حصوں میں سے ایک کی دوبارہ تنصیف کی جاتی ہے۔ سب سے چھوٹے زاویے کا ناپ درجوں میں نکالیں۔",
      S2, ("Halve 140, then halve the answer.", "140 کو آدھا کریں، پھر جواب کو آدھا کریں۔"),
      ("Correct: 140 → 70 → 35°.", "درست: 140 ← 70 ← 35°"),
      ("Model answer: first bisection 140° ÷ 2 = 70°. Second bisection 70° ÷ 2 = 35°.", "نمونہ جواب: پہلی تنصیف 140° ÷ 2 = 70°۔ دوسری تنصیف 70° ÷ 2 = 35°"),
      [(70, "70° is after one bisection. There was a second: 35.", "70° ایک تنصیف کے بعد ہے۔ دوسری بھی ہوئی: 35", "bisect_not_half"),
       (280, "That doubles 140. Bisecting halves: 35.", "یہ 140 کو دگنا کرتا ہے۔ تنصیف آدھا کرتی ہے: 35", "bisect_not_half")]),
   with_fig(short("q3_three_line", "Three angles sit side by side on a straight line: 48°, x and 77°. Find x, in degrees.", "ایک سیدھی لکیر پر تین زاویے ساتھ ساتھ ہیں: 48°، x اور 77°۔ x درجوں میں نکالیں۔",
      S3, ("48 + x + 77 = 180.", "48 + x + 77 = 180"),
      ("Correct: 48 + 77 = 125, and 180 − 125 = 55°.", "درست: 48 + 77 = 125، اور 180 − 125 = 55°"),
      ("Model answer: angles on a straight line add up to 180°. 48 + x + 77 = 180, so x = 180 − 125 = 55°.", "نمونہ جواب: سیدھی لکیر پر زاویوں کا مجموعہ 180° ہوتا ہے۔ 48 + x + 77 = 180، تو x = 180 − 125 = 55°"),
      [(125, "125° is 48 + 77. x is what is left of 180: 55.", "125° یعنی 48 + 77۔ x وہ ہے جو 180 میں سے بچے: 55", "stops_at_sum"),
       (132, "That takes away only 48. Take away 48 and 77: 55.", "اس میں صرف 48 گھٹایا۔ 48 اور 77 دونوں گھٹائیں: 55", "stops_at_sum")]), S3_FIG),
   short("q4_iso", "An isosceles triangle has two equal angles of 55°. Find the third angle, in degrees.", "ایک متساوی الساقین مثلث کے دو برابر زاویے 55° کے ہیں۔ تیسرا زاویہ درجوں میں نکالیں۔",
      S4, ("55 + 55 + x = 180.", "55 + 55 + x = 180"),
      ("Correct: 180 − 110 = 70°.", "درست: 180 − 110 = 70°"),
      ("Model answer: the angles of a triangle add up to 180°. 55 + 55 + x = 180, so x = 180 − 110 = 70°.", "نمونہ جواب: مثلث کے زاویوں کا مجموعہ 180° ہوتا ہے۔ 55 + 55 + x = 180، تو x = 180 − 110 = 70°"),
      [(110, "110° is the two equal angles together. The third is 70.", "110° دو برابر زاویے ملا کر ہیں۔ تیسرا 70° ہے۔", "stops_at_sum"),
       (125, "That is 180 − 55. Take away both 55° angles: 70.", "یہ 180 − 55 ہے۔ دونوں 55° کے زاویے گھٹائیں: 70", "stops_at_sum")]),
   {"id": "s_long", "type": "explain",
    "text": T("Longer problems. Write the rule and full working in your notebook, then type the final answer.",
              "تفصیلی سوالات۔ اپنی کاپی میں اصول اور پورا کام لکھیں، پھر آخری جواب لکھیں۔")},
   long_q("l1_pb_x", "The perpendicular bisector of AB meets AB at M. AM = (3x − 4) cm and MB = (x + 8) cm. Find the length of AB, in cm.", "AB کا عمودی ناصف AB کو M پر ملتا ہے۔ AM = (3x − 4) سینٹی میٹر اور MB = (x + 8) سینٹی میٹر ہے۔ AB کی لمبائی سینٹی میٹر میں نکالیں۔",
      L1, ("M is the midpoint, so AM = MB. Find x, then AB = AM + MB.", "M درمیانی نقطہ ہے، تو AM = MB۔ x نکالیں، پھر AB = AM + MB۔"),
      ("Correct: 2x = 12, x = 6, AM = 14, and AB = 28 cm.", "درست: 2x = 12، x = 6، AM = 14، اور AB = 28 سینٹی میٹر"),
      ("Model answer: AM = MB, so 3x − 4 = x + 8, 2x = 12, x = 6. MB = 6 + 8 = 14 cm, AM = 14 cm. AB = 14 + 14 = 28 cm.", "نمونہ جواب: AM = MB، تو 3x − 4 = x + 8، 2x = 12، x = 6۔ MB = 6 + 8 = 14 سینٹی میٹر، AM = 14 سینٹی میٹر۔ AB = 14 + 14 = 28 سینٹی میٹر"),
      [(6, "6 is x. The question asks for AB: 28.", "6، x ہے۔ سوال AB پوچھتا ہے: 28", "answer_is_other_quantity"),
       (14, "14 cm is only one half. AB is both halves: 28.", "14 سینٹی میٹر صرف ایک آدھا ہے۔ AB دونوں آدھے ہیں: 28", "answer_is_other_quantity")]),
   long_q("l2_between", "On one base arm, Sara builds a ray at 45° by bisecting a right angle, and a ray at 105° by going halfway between the 90° and 120° rays. What angle is there between her two rays, in degrees?", "ایک بنیادی بازو پر سارہ قائمہ زاویے کی تنصیف سے 45° کی شعاع بناتی ہے، اور 90° اور 120° کی شعاعوں کے ٹھیک بیچ میں جا کر 105° کی شعاع بناتی ہے۔ اس کی دونوں شعاعوں کے بیچ کتنے درجے کا زاویہ ہے؟",
      L2, ("Both angles are measured from the base arm. Take the smaller from the larger.", "دونوں زاویے بنیادی بازو سے ناپے گئے ہیں۔ بڑے میں سے چھوٹا گھٹائیں۔"),
      ("Correct: 105° − 45° = 60°.", "درست: 105° − 45° = 60°"),
      ("Model answer: 90° ÷ 2 = 45°, and (90 + 120) ÷ 2 = 105°. Both are measured from the same base arm, so the angle between the rays = 105 − 45 = 60°.", "نمونہ جواب: 90° ÷ 2 = 45°، اور (90 + 120) ÷ 2 = 105°۔ دونوں ایک ہی بنیادی بازو سے ناپے گئے ہیں، تو شعاعوں کے بیچ کا زاویہ = 105 − 45 = 60°"),
      [(150, "150° is 45 + 105. The angle between them is the difference: 60.", "150° یعنی 45 + 105۔ ان کے بیچ کا زاویہ فرق ہے: 60", "add_not_mid"),
       (15, "15° is 105 − 90. Both rays are measured from the base arm: 105 − 45 = 60.", "15° یعنی 105 − 90۔ دونوں شعاعیں بنیادی بازو سے ناپی گئی ہیں: 105 − 45 = 60", "add_not_mid")]),
   with_fig(long_q("l3_xyz", "Three angles on a straight line are x°, 2x° and 3x°. Find the largest angle, in degrees.", "ایک سیدھی لکیر پر تین زاویے x°، 2x° اور 3x° ہیں۔ سب سے بڑا زاویہ درجوں میں نکالیں۔",
      L3, ("x + 2x + 3x = 180. Find x, then 3x.", "x + 2x + 3x = 180۔ x نکالیں، پھر 3x۔"),
      ("Correct: 6x = 180, x = 30, and the largest angle is 3 × 30 = 90°.", "درست: 6x = 180، x = 30، اور سب سے بڑا زاویہ 3 × 30 = 90°"),
      ("Model answer: angles on a straight line add up to 180°, so x + 2x + 3x = 180, 6x = 180, x = 30. The largest angle is 3x = 3 × 30 = 90°.", "نمونہ جواب: سیدھی لکیر پر زاویوں کا مجموعہ 180° ہوتا ہے، تو x + 2x + 3x = 180، 6x = 180، x = 30۔ سب سے بڑا زاویہ 3x = 3 × 30 = 90°"),
      [(30, "30 is x, the smallest angle. The largest is 3x: 90.", "30، x ہے، یعنی سب سے چھوٹا زاویہ۔ سب سے بڑا 3x ہے: 90", "answer_is_other_quantity"),
       (60, "60° is 2x. The largest angle is 3x = 90.", "60° یعنی 2x۔ سب سے بڑا زاویہ 3x = 90 ہے۔", "equation_wrong")]), L3_FIG),
   long_q("l4_exterior", "One side of a triangle is extended. The exterior angle is 120°, and the two opposite interior angles are (2x + 10)° and (x + 20)°. Find the larger of these two interior angles, in degrees.", "ایک مثلث کا ایک ضلع بڑھایا گیا ہے۔ بیرونی زاویہ 120° ہے، اور دو مخالف اندرونی زاویے (2x + 10)° اور (x + 20)° ہیں۔ ان دو اندرونی زاویوں میں سے بڑا درجوں میں نکالیں۔",
      L4, ("Exterior angle = sum of the two opposite interior angles. Solve for x first.", "بیرونی زاویہ = دو مخالف اندرونی زاویوں کا مجموعہ۔ پہلے x نکالیں۔"),
      ("Correct: 3x + 30 = 120, x = 30. The angles are 70° and 50°, so the larger is 70°.", "درست: 3x + 30 = 120، x = 30۔ زاویے 70° اور 50° ہیں، تو بڑا 70° ہے۔"),
      ("Model answer: exterior angle = sum of the opposite interior angles, so (2x + 10) + (x + 20) = 120, 3x + 30 = 120, 3x = 90, x = 30. The angles are 2 × 30 + 10 = 70° and 30 + 20 = 50°. The larger is 70°. Check: 70 + 50 = 120.", "نمونہ جواب: بیرونی زاویہ = مخالف اندرونی زاویوں کا مجموعہ، تو (2x + 10) + (x + 20) = 120، 3x + 30 = 120، 3x = 90، x = 30۔ زاویے 2 × 30 + 10 = 70° اور 30 + 20 = 50° ہیں۔ بڑا 70° ہے۔ جانچ: 70 + 50 = 120"),
      [(30, "30 is x. The question asks for the larger angle: 70.", "30، x ہے۔ سوال بڑا زاویہ پوچھتا ہے: 70", "answer_is_other_quantity"),
       (50, "50° is the smaller angle. The larger is 2x + 10 = 70.", "50° چھوٹا زاویہ ہے۔ بڑا 2x + 10 = 70 ہے۔", "equation_wrong")]),
   {"id": "s_end_summary", "type": "summary",
    "character": say("celebrating", "You finished the chapter 10 test. Well done!", "آپ نے باب 10 کا ٹیسٹ مکمل کر لیا۔ شاباش!"),
    "text": T("In the exam: the perpendicular bisector of AB cuts it into two equal halves at 90°, and its points are equally far from A and B; open the compass more than half of AB, the same for both arcs. Bisecting halves an angle. Build from 60°: 30° (bisect 60°), 90°, 45°, 75°, 105° and 150° by bisecting or going halfway between rays. Angles on a straight line and in a triangle add up to 180°. For x questions, write the equation, solve for x, then answer what is asked.",
              "امتحان میں: AB کا عمودی ناصف اسے 90° پر دو برابر آدھوں میں کاٹتا ہے، اور اس کے نقطے A اور B سے برابر دور ہوتے ہیں؛ پرکار AB کے آدھے سے زیادہ کھولیں، دونوں قوسوں کے لیے ایک جتنا۔ تنصیف زاویے کو آدھا کرتی ہے۔ 60° سے بنائیں: 30° (60° کی تنصیف)، 90°، 45°، 75°، 105° اور 150° تنصیف سے یا شعاعوں کے بیچ میں جا کر۔ سیدھی لکیر پر اور مثلث میں زاویوں کا مجموعہ 180° ہوتا ہے۔ x والے سوالوں میں مساوات لکھیں، x نکالیں، پھر وہ جواب دیں جو پوچھا گیا ہو۔"),
    "points": [T("Rule, numbers, answer with its unit.", "اصول، اعداد، اکائی کے ساتھ جواب۔"),
               T("Equation for x: write it, solve it, then answer the question asked.", "x کی مساوات: لکھیں، حل کریں، پھر پوچھا گیا جواب دیں۔")]},
 ],
 "review_questions": [
   {"id": "r_exam_bisect", "type": "exam_style", "skill": SKILL, "step": nq(
     "r_exam_bisect", ("A right angle is bisected. How big is each part, in degrees?", "قائمہ زاویے کی تنصیف کی گئی۔ ہر حصہ کتنے درجے کا ہے؟"), R1,
     ("Halve 90.", "90 کو آدھا کریں۔"),
     ("Correct: 90 ÷ 2 = 45°.", "درست: 90 ÷ 2 = 45°"), ("Two equal parts: 45.", "دو برابر حصے: 45"),
     [(30, "30° is for bisecting 60°. A right angle halved: 45.", "30° 60° کی تنصیف کا ہے۔ قائمہ زاویے کا آدھا: 45", "bisect_not_half")], qtype=None)},
   {"id": "r_exam_right_tri", "type": "exam_style", "skill": SKILL, "step": nq(
     "r_exam_right_tri", ("A right-angled triangle has an angle of 30°. Find its third angle, in degrees.", "ایک قائمہ الزاویہ مثلث میں ایک زاویہ 30° کا ہے۔ اس کا تیسرا زاویہ کتنے درجے کا ہے؟"), R2,
     ("180 − 90 − 30.", "180 − 90 − 30"),
     ("Correct: 180 − 90 − 30 = 60°.", "درست: 180 − 90 − 30 = 60°"), ("The two acute angles add up to 90°: 30 + 60.", "دونوں حادہ زاویوں کا مجموعہ 90° ہے: 30 + 60"),
     [(150, "That is 180 − 30. Also take away the 90°: 60.", "یہ 180 − 30 ہے۔ 90° بھی گھٹائیں: 60", "stops_at_sum")], qtype=None)},
 ],
 "teacher_notes": [
   "A chapter test to use with Review Exercise 10 of the PCTB Mathematics 6 book, in the style of a paper: multiple choice, short questions, then longer problems. Only the kinds of question come from the book; every question, number and story here is new, because the book may not be copied.",
   "It has its own skill (maths.constructions.chapter_10_test), with the skills of the Constructions unit and the Angles unit as prerequisites, and is mastered with exam_style questions, like the chapter 5 to 9 tests. The app cannot check a real drawing, so the questions are about the steps of the constructions and the angles they give; the drawing is a home task.",
   "Urdu terms to check: کثیر انتخابی (multiple choice), مختصر سوال / تفصیلی سوال (short / long question), نمونہ جواب (model answer), اعادی مشق (review exercise), all as in the earlier chapter tests; the construction and angle words come from the existing lessons. No new Urdu terms were added.",
   "The numbers were worked out in content/sources/g6-maths-19/chapter_10_test.py. Edit the script, not this file.",
 ],
 "review": REVIEW,
}

write(lesson)
