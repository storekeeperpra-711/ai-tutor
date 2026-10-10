"""Practice set for Exercise 10.1 of the book: drawing a line segment, the
perpendicular bisector of a segment, and a perpendicular to a line from a point
on it and from a point off it. The app cannot check a real drawing, so the
questions are about the steps and what they give. The questions are new; only
the kinds of question follow the book."""
import math

from common import (T, say, nq, ch, practice_lesson, practice_intro, write, EX_SKILL, CO_BISECTORS)
from figs import (fig, with_fig, label, dot, seg, arc_toward, crossings, right_mark, r1)

SKILL = EX_SKILL["10.1"]
RIGHT = 90

# q3: perpendicular bisector of AB = 18 cm meets AB at its midpoint M
AB3 = 18
Q3 = AB3 // 2
assert Q3 == 9 and 2 * Q3 == AB3 and AB3 * 2 == 36
# q4: smallest whole-number compass opening for AB = 12 cm: more than half of AB
AB4 = 12
Q4 = AB4 // 2 + 1
assert Q4 == 7 and Q4 > AB4 / 2 and (Q4 - 1) <= AB4 / 2
# q7: O is on the line; arcs from O cut it at C and D, 3 cm from O on each side
OC = 3
Q7 = 2 * OC
assert Q7 == 6 and OC + OC + OC == 9
# q8: Q on the perpendicular bisector is as far from A as from B
QA = 13
Q8 = QA
assert Q8 == 13 and 2 * QA == 26
# q9: a strip of cloth 24 cm long is folded end to end; the crease is its perpendicular bisector's midpoint
STRIP = 24
Q9 = STRIP // 2
assert Q9 == 12 and 2 * STRIP == 48 and STRIP // 4 == 6
# bank and review
QB1 = RIGHT
QB2 = 30 // 2
assert QB2 == 15 and 30 * 2 == 60
QB3 = 9
R1 = 26 // 2
assert R1 == 13 and 26 * 2 == 52
R2 = 2 * 8
assert R2 == 16 and 8 // 2 == 4

# figure: arcs from A and B cross at P and Q; PQ meets AB at M
A, B, RAD = (30, 35), (70, 35), 28
P, Q = crossings(A, B, RAD)
assert abs(P[0] - 50) < 0.01 and P[1] < 35 < Q[1]
assert math.isclose(math.dist(A, P), math.dist(B, P)) and math.isclose(math.dist(A, P), RAD)
F_PB = fig(100, 70,
    "Line segment AB with its midpoint M. Dashed compass arcs from A and from B, both with the same opening, cross above AB at P and below AB at Q. A dashed line joins P and Q and cuts AB at M, with a small square showing a right angle.",
    "قطعۂ خط AB اور اس کا درمیانی نقطہ M۔ A اور B سے پرکار کی ایک ہی کھلاؤ والی ڈیش قوسیں AB کے اوپر P پر اور نیچے Q پر ملتی ہیں۔ ڈیش والی لکیر P اور Q کو ملاتی ہے اور AB کو M پر کاٹتی ہے، اور ایک چھوٹا چوکور خانہ قائمہ زاویہ دکھاتا ہے۔",
    [seg(A, B), arc_toward(A, P, RAD), arc_toward(A, Q, RAD), arc_toward(B, P, RAD), arc_toward(B, Q, RAD),
     seg((50, 8), (50, 62), dashed=True), *right_mark(50, 35),
     dot(A), dot(B), dot(P), dot(Q), dot((50, 35)),
     label((24, 35), "A"), label((76, 35), "B"), label((56, 12), "P"), label((56, 58), "Q"), label((45, 41), "M")])

# figure: P above line l; arcs from P cut l at C and D (the first step only)
OP, LY, OR = (50, 24), 42, 22
dx = math.sqrt(OR ** 2 - (LY - OP[1]) ** 2)
C, D = (OP[0] - dx, LY), (OP[0] + dx, LY)
assert math.isclose(math.dist(OP, C), OR) and math.isclose(math.dist(OP, D), OR)
F_OFF = fig(100, 60,
    "A straight line l with a point P above it. Two dashed arcs drawn from P cut the line at C on the left and D on the right. PC and PD are equal.",
    "سیدھی لکیر l اور اس کے اوپر نقطہ P۔ P سے لگی دو ڈیش قوسیں لکیر کو بائیں طرف C پر اور دائیں طرف D پر کاٹتی ہیں۔ PC اور PD برابر ہیں۔",
    [seg((5, LY), (95, LY)), arc_toward(OP, C, OR, 24), arc_toward(OP, D, OR, 24),
     dot(OP), dot(C), dot(D),
     label((56, 20), "P"), label((C[0] - 3, LY + 7), "C"), label((D[0] + 3, LY + 7), "D"), label((92, LY - 6), "l")])

# figure: O on line l; arcs from O cut l at C and D, OC = OD
OO = (50, 40)
C2, D2 = (OO[0] - 22, 40), (OO[0] + 22, 40)
F_ON = fig(100, 66,
    "A straight line l with a point O on it. Two dashed arcs drawn from O cut the line at C on the left and D on the right, the same distance from O on each side.",
    "سیدھی لکیر l اور اس پر نقطہ O۔ O سے لگی دو ڈیش قوسیں لکیر کو بائیں طرف C پر اور دائیں طرف D پر کاٹتی ہیں، O سے دونوں طرف ایک جتنے فاصلے پر۔",
    [seg((5, 40), (95, 40)), arc_toward(OO, C2, 22, 70), arc_toward(OO, D2, 22, 70),
     dot(OO), dot(C2), dot(D2),
     label((50, 47), "O"), label((C2[0], 47), "C"), label((D2[0], 47), "D"), label((92, 34), "l")])

# figure: too-small opening (arcs stop short of each other)
SA, SB, SMALL = (25, 30), (75, 30), 15
assert SMALL < math.dist(SA, SB) / 2
F_SMALL = fig(100, 60,
    "Line segment AB. A short dashed arc is drawn from A and another from B, but the compass was opened less than half of AB, so the two arcs stop before the middle and do not cross.",
    "قطعۂ خط AB۔ A سے ایک چھوٹی ڈیش قوس اور B سے دوسری قوس لگائی گئی، لیکن پرکار AB کے آدھے سے کم کھولا گیا، اس لیے دونوں قوسیں درمیان سے پہلے رک جاتی ہیں اور ایک دوسرے کو نہیں کاٹتیں۔",
    [seg(SA, SB),
     {"kind": "arc", "center": list(SA), "radius": SMALL, "start": 300, "sweep": 120, "style": "dashed"},
     {"kind": "arc", "center": list(SB), "radius": SMALL, "start": 120, "sweep": 120, "style": "dashed"},
     dot(SA), dot(SB), label((19, 30), "A"), label((81, 30), "B"), label((50, 22), "?")])

lesson = practice_lesson(
 "10.1", script="exercise_10_1.py",
 title=T("Exercise 10.1 practice: segments and perpendiculars", "مشق 10.1 کی پریکٹس: قطعۂ خط اور عمود"),
 outcome="Draw a line segment, construct the perpendicular bisector of a segment, and construct a perpendicular to a line from a point on it and from a point outside it, knowing the steps and what they give.",
 prerequisites=[CO_BISECTORS],
 misconceptions=[
   {"id": "bisector_is_perpendicular", "description": "Thinks a bisector always meets the segment at 90°, or that a perpendicular always cuts the segment in half."},
   {"id": "half_not_taken", "description": "Gives the whole length of AB, or double it, when the length of half of AB is asked."},
   {"id": "small_opening", "description": "Opens the compass to half of AB or less, so the arcs touch or miss each other."},
   {"id": "different_openings", "description": "Uses a different compass opening for the arc from A and the arc from B."},
   {"id": "steps_out_of_order", "description": "Puts the steps of a construction in the wrong order, such as joining the crossing points before drawing the arcs."},
   {"id": "same_side", "description": "Cuts the line at two points on the same side of O when drawing a perpendicular at a point on the line."},
   {"id": "tool_mix", "description": "Uses the protractor or the compass for a job that belongs to the ruler, or the other way round."},
 ],
 steps=[
   practice_intro("10.1",
     "Here you practise the steps for drawing a segment, a perpendicular bisector and a perpendicular, and what each one gives. You will not draw today; you will think like someone holding the compass.",
     "اس میں آپ قطعۂ خط، عمودی ناصف اور عمود بنانے کے قدم اور ان کا نتیجہ دہرائیں گے۔ آج آپ ڈرائنگ نہیں کریں گے؛ پرکار ہاتھ میں پکڑنے والے کی طرح سوچیں گے۔",
     "Exercise 10.1 is about drawing with ruler and compass. Ready?", "مشق 10.1 پیمانے اور پرکار سے ڈرائنگ کے بارے میں ہے۔ تیار؟"),
   ch("q1_tool", ("Which tool do you use to draw a line segment exactly 7 cm long?", "7 سینٹی میٹر لمبا قطعۂ خط ٹھیک ناپ کر بنانے کے لیے کون سا اوزار استعمال ہوتا ہے؟"),
      ("A ruler and a sharp pencil", "پیمانہ اور تیز پنسل", "Yes! The ruler measures the length and guides the pencil.", "جی ہاں! پیمانہ لمبائی ناپتا ہے اور پنسل کو سیدھا رکھتا ہے۔"),
      [("A protractor", "زاویہ پیما", "A protractor measures angles, not lengths.", "زاویہ پیما زاویے ناپتا ہے، لمبائی نہیں۔", "tool_mix"),
       ("A compass opened by guessing", "اندازے سے کھولا ہوا پرکار", "A guess will not give exactly 7 cm. Set the opening on the ruler first.", "اندازے سے ٹھیک 7 سینٹی میٹر نہیں بنے گا۔ پہلے پرکار کو پیمانے پر کھولیں۔", "tool_mix"),
       ("Only your eyes", "صرف آنکھوں کا اندازہ", "Estimating by eye is not exact. We measure.", "آنکھ کے اندازے سے ٹھیک ناپ نہیں بنتی۔ ہم ناپتے ہیں۔", "tool_mix")],
      0, qtype="recall"),
   ch("q2_pb", ("Which sentence describes the perpendicular bisector of a segment AB?", "کون سا جملہ قطعۂ خط AB کے عمودی ناصف کو بیان کرتا ہے؟"),
      ("It cuts AB into two equal parts and meets it at 90°.", "یہ AB کو دو برابر حصوں میں کاٹتا ہے اور اس سے 90° پر ملتا ہے۔", "Yes! Two equal halves and a right angle: that is what makes it a perpendicular bisector.", "جی ہاں! دو برابر آدھے اور قائمہ زاویہ: یہی اسے عمودی ناصف بناتا ہے۔"),
      [("It cuts AB into two equal parts, at any angle.", "یہ AB کو دو برابر حصوں میں کاٹتا ہے، کسی بھی زاویے پر۔", "That is only a bisector. A perpendicular bisector also meets AB at 90°.", "یہ صرف ناصف ہے۔ عمودی ناصف AB سے 90° پر بھی ملتا ہے۔", "bisector_is_perpendicular"),
       ("It meets AB at 90° at any point along it.", "یہ AB سے 90° پر ملتا ہے، اس کے کسی بھی نقطے پر۔", "That is only a perpendicular. A perpendicular bisector must pass through the middle of AB.", "یہ صرف عمود ہے۔ عمودی ناصف AB کے بیچ سے گزرنا چاہیے۔", "bisector_is_perpendicular"),
       ("It runs alongside AB and never meets it.", "یہ AB کے ساتھ ساتھ چلتا ہے اور اسے کبھی نہیں کاٹتا۔", "A perpendicular bisector crosses AB.", "عمودی ناصف AB کو کاٹتا ہے۔", "bisector_is_perpendicular")],
      2, qtype="recall"),
   with_fig({"id": "s_idea", "type": "explain",
    "character": say("thinking", "Same opening, from both ends. That is the secret.", "دونوں سروں سے ایک ہی کھلاؤ۔ یہی راز ہے۔"),
    "text": T("To bisect AB at right angles: (1) draw AB with the ruler; (2) open the compass more than half of AB; (3) with the point on A, draw arcs above and below AB; (4) keep the same opening, point on B, draw arcs that cross the first ones at P and Q; (5) join P and Q. PQ cuts AB at its midpoint M and makes 90° with it. To draw a perpendicular from a point O on a line, first mark C and D on the line, the same distance from O on each side, then bisect CD. From a point P off the line, draw an arc from P that cuts the line at C and D, then bisect CD.",
              "AB کو قائمہ زاویے پر دو برابر حصوں میں بانٹنے کے لیے: (1) پیمانے سے AB کھینچیں؛ (2) پرکار AB کے آدھے سے زیادہ کھولیں؛ (3) نوک A پر رکھ کر AB کے اوپر اور نیچے قوسیں لگائیں؛ (4) وہی کھلاؤ رکھ کر نوک B پر رکھیں اور قوسیں لگائیں جو پہلی قوسوں کو P اور Q پر کاٹیں؛ (5) P اور Q کو ملا دیں۔ PQ، AB کو اس کے درمیانی نقطے M پر کاٹتا ہے اور اس سے 90° بناتا ہے۔ لکیر پر دیے ہوئے نقطے O سے عمود بنانے کے لیے پہلے لکیر پر C اور D لگائیں جو O سے دونوں طرف برابر فاصلے پر ہوں، پھر CD کی تنصیف کریں۔ لکیر سے باہر نقطے P سے P سے قوس لگائیں جو لکیر کو C اور D پر کاٹے، پھر CD کی تنصیف کریں۔")}, F_PB),
   nq("q3_half", ("The perpendicular bisector of a segment AB, 18 cm long, meets AB at M. How long is AM, in cm?", "18 سینٹی میٹر لمبے قطعۂ خط AB کا عمودی ناصف AB کو M پر ملتا ہے۔ AM کتنے سینٹی میٹر ہے؟"), Q3,
      ("M is the midpoint, so AM is half of AB.", "M درمیانی نقطہ ہے، تو AM، AB کا آدھا ہے۔"),
      ("Right! 18 ÷ 2 = 9 cm.", "درست! 18 ÷ 2 = 9 سینٹی میٹر"), ("The bisector cuts AB into two equal parts: 18 ÷ 2 = 9.", "ناصف AB کو دو برابر حصوں میں کاٹتا ہے: 18 ÷ 2 = 9"),
      [(18, "18 cm is the whole of AB. AM is only half: 9.", "18 سینٹی میٹر پورا AB ہے۔ AM صرف آدھا ہے: 9", "half_not_taken"),
       (36, "That doubles AB. Halve it: 9.", "یہ AB کا دگنا ہے۔ آدھا کریں: 9", "half_not_taken"),
       (90, "90 is the angle, in degrees. The length AM is 9 cm.", "90 زاویہ ہے، درجوں میں۔ AM کی لمبائی 9 سینٹی میٹر ہے۔", "bisector_is_perpendicular")], qtype="recall"),
   with_fig(nq("q4_opening", ("To bisect AB, 12 cm long, the compass must be opened more than half of AB. What is the smallest whole number of cm you can open it to?", "12 سینٹی میٹر لمبے AB کی تنصیف کے لیے پرکار AB کے آدھے سے زیادہ کھولنا ضروری ہے۔ آپ اسے کم از کم کتنے پورے سینٹی میٹر پر کھول سکتے ہیں؟"), Q4,
      ("Half of AB is 6 cm. The opening must be bigger than that.", "AB کا آدھا 6 سینٹی میٹر ہے۔ کھلاؤ اس سے بڑا ہونا چاہیے۔"),
      ("Right! More than 6 cm, so the smallest whole number is 7 cm.", "درست! 6 سینٹی میٹر سے زیادہ، تو سب سے چھوٹا پورا عدد 7 سینٹی میٹر ہے۔"), ("Half of 12 is 6, and the opening must be more than 6, so 7.", "12 کا آدھا 6 ہے، اور کھلاؤ 6 سے زیادہ ہونا چاہیے، تو 7"),
      [(6, "With exactly half the arcs only touch at M. They must cross, so use more than 6: 7.", "ٹھیک آدھے پر قوسیں صرف M پر چھوتی ہیں۔ انہیں کاٹنا چاہیے، تو 6 سے زیادہ لیں: 7", "small_opening"),
       (12, "12 cm would work, but it is not the smallest. More than 6: 7.", "12 سینٹی میٹر بھی چلے گا، لیکن سب سے چھوٹا نہیں۔ 6 سے زیادہ: 7", "small_opening")]), F_SMALL),
   ch("q5_order", ("Hira bisects AB. Her steps are mixed up: X) join P and Q; Y) draw arcs above and below AB from A, then from B, with the same opening; Z) draw AB with the ruler. What is the right order?", "حرا AB کی تنصیف کرتی ہے۔ اس کے قدم الٹ پلٹ ہو گئے ہیں: X) P اور Q کو ملائیں؛ Y) A سے پھر B سے ایک ہی کھلاؤ کے ساتھ AB کے اوپر اور نیچے قوسیں لگائیں؛ Z) پیمانے سے AB کھینچیں۔ صحیح ترتیب کیا ہے؟"),
      ("Z, then Y, then X", "Z، پھر Y، پھر X", "Yes! Segment first, then arcs from both ends, then join the crossings.", "جی ہاں! پہلے قطعۂ خط، پھر دونوں سروں سے قوسیں، پھر قوسوں کے ملاپ کو ملائیں۔"),
      [("X, then Y, then Z", "X، پھر Y، پھر Z", "You cannot join P and Q before the arcs and AB exist.", "قوسوں اور AB کے بنے بغیر P اور Q کو نہیں ملا سکتے۔", "steps_out_of_order"),
       ("Y, then Z, then X", "Y، پھر Z، پھر X", "The arcs are drawn from A and B, so AB must be drawn first.", "قوسیں A اور B سے لگتی ہیں، تو پہلے AB کھینچنا ہوگا۔", "steps_out_of_order"),
       ("Z, then X, then Y", "Z، پھر X، پھر Y", "P and Q come from the arcs, so the arcs come before joining.", "P اور Q قوسوں سے بنتے ہیں، تو ملانے سے پہلے قوسیں آتی ہیں۔", "steps_out_of_order")],
      1, qtype="apply"),
   with_fig(ch("q6_next", ("P is a point above the line l. An arc from P has cut l at C and D. What is the next step to draw the perpendicular from P to l?", "P لکیر l کے اوپر ایک نقطہ ہے۔ P سے لگی قوس نے l کو C اور D پر کاٹ دیا ہے۔ P سے l پر عمود بنانے کا اگلا قدم کیا ہے؟"),
      ("From C and from D, with the same opening, draw arcs that cross below l; then join P to where they cross.", "C سے اور D سے ایک ہی کھلاؤ کے ساتھ ایسی قوسیں لگائیں جو l کے نیچے ملیں؛ پھر P کو ان کے ملاپ سے ملائیں۔", "Yes! That bisects CD, and the bisector of CD passes through P at 90° to l.", "جی ہاں! اس سے CD کی تنصیف ہوتی ہے، اور CD کا ناصف P سے گزرتا ہے اور l سے 90° بناتا ہے۔"),
      [("Join C to D and stop.", "C کو D سے ملائیں اور رک جائیں۔", "CD lies along l. It is not the perpendicular.", "CD تو l پر ہی ہے۔ یہ عمود نہیں۔", "steps_out_of_order"),
       ("Draw one more arc from P with a bigger opening.", "P سے بڑے کھلاؤ کی ایک اور قوس لگائیں۔", "Another arc from P does not give a direction at 90° to l.", "P سے ایک اور قوس l پر 90° کی سمت نہیں دیتی۔", "steps_out_of_order"),
       ("Join P to C.", "P کو C سے ملائیں۔", "PC is a slanted line, not a perpendicular.", "PC ترچھی لکیر ہے، عمود نہیں۔", "bisector_is_perpendicular")],
      3, qtype="apply"), F_OFF),
   with_fig(nq("q7_cd", ("O is a point on line l. Arcs from O cut the line at C and D, each 3 cm from O, one on each side. How long is CD, in cm?", "O لکیر l پر ایک نقطہ ہے۔ O سے لگی قوسیں لکیر کو C اور D پر کاٹتی ہیں، دونوں O سے 3 سینٹی میٹر دور، ایک ایک طرف۔ CD کتنے سینٹی میٹر ہے؟"), Q7,
      ("C is 3 cm on one side and D is 3 cm on the other.", "C ایک طرف 3 سینٹی میٹر اور D دوسری طرف 3 سینٹی میٹر ہے۔"),
      ("Right! 3 + 3 = 6 cm, and O is the middle of CD, so the perpendicular at O bisects CD.", "درست! 3 + 3 = 6 سینٹی میٹر، اور O، CD کا بیچ ہے، تو O پر عمود CD کی تنصیف کرتا ہے۔"), ("Add both sides: 3 + 3 = 6.", "دونوں طرف جمع کریں: 3 + 3 = 6"),
      [(3, "3 cm is only OC. CD is OC plus OD: 6.", "3 سینٹی میٹر صرف OC ہے۔ CD = OC + OD: 6", "half_not_taken"),
       (9, "That adds 3 three times. CD = 3 + 3 = 6.", "یہ 3 کو تین بار جمع کرتا ہے۔ CD = 3 + 3 = 6", "half_not_taken")], qtype="apply"), F_ON),
   nq("q8_equal", ("Point Q lies on the perpendicular bisector of AB. QA is 13 cm. How long is QB, in cm?", "نقطہ Q، AB کے عمودی ناصف پر ہے۔ QA 13 سینٹی میٹر ہے۔ QB کتنے سینٹی میٹر ہے؟"), Q8,
      ("Every point on the perpendicular bisector is the same distance from A and from B.", "عمودی ناصف کا ہر نقطہ A اور B سے برابر فاصلے پر ہوتا ہے۔"),
      ("Right! QB = QA = 13 cm.", "درست! QB = QA = 13 سینٹی میٹر"), ("The arcs from A and B had the same opening, so QA = QB = 13.", "A اور B کی قوسوں کا کھلاؤ برابر تھا، تو QA = QB = 13"),
      [(26, "That adds QA and QB. QB is just equal to QA: 13.", "یہ QA اور QB کو جمع کرتا ہے۔ QB صرف QA کے برابر ہے: 13", "different_openings"),
       (90, "90 is the angle in degrees. The distance QB is 13 cm.", "90 زاویہ ہے، درجوں میں۔ فاصلہ QB 13 سینٹی میٹر ہے۔", "bisector_is_perpendicular")]),
   nq("q9_cloth", ("A tailor folds a strip of cloth 24 cm long so that its two ends meet, and presses the crease. How far is the crease from each end, in cm?", "ایک درزی 24 سینٹی میٹر لمبی کپڑے کی پٹی کو اس طرح موڑتا ہے کہ اس کے دونوں سرے مل جائیں، اور تہہ دباتا ہے۔ تہہ ہر سرے سے کتنے سینٹی میٹر دور ہے؟"), Q9,
      ("The crease is at the middle of the strip: half of 24.", "تہہ پٹی کے بیچ میں ہے: 24 کا آدھا۔"),
      ("Right! 24 ÷ 2 = 12 cm. The crease is like the perpendicular bisector of the strip.", "درست! 24 ÷ 2 = 12 سینٹی میٹر۔ تہہ پٹی کے عمودی ناصف جیسی ہے۔"), ("Both ends meet at the crease, so each is half the length away: 12.", "دونوں سرے تہہ پر ملتے ہیں، تو ہر ایک آدھی لمبائی دور ہے: 12"),
      [(24, "24 cm is the whole strip. Halve it: 12.", "24 سینٹی میٹر پوری پٹی ہے۔ آدھا کریں: 12", "half_not_taken"),
       (6, "That halves twice. One halving: 12.", "یہ دو بار آدھا کرتا ہے۔ ایک بار آدھا کریں: 12", "half_not_taken"),
       (48, "That doubles the strip. Halve it: 12.", "یہ پٹی کو دگنا کرتا ہے۔ آدھا کریں: 12", "half_not_taken")]),
   ch("q10_find_error", ("Ali bisects AB. He draws the arc from A with an opening of 5 cm and the arc from B with an opening of 7 cm, both more than half of AB. Then he joins the crossings. What went wrong?", "علی AB کی تنصیف کرتا ہے۔ وہ A سے قوس 5 سینٹی میٹر کھلاؤ سے اور B سے قوس 7 سینٹی میٹر کھلاؤ سے لگاتا ہے، دونوں AB کے آدھے سے زیادہ۔ پھر وہ ملاپ کے نقطوں کو ملاتا ہے۔ کیا غلطی ہوئی؟"),
      ("The two arcs must have the same opening. With different openings the line does not pass through the middle of AB.", "دونوں قوسوں کا کھلاؤ ایک جیسا ہونا چاہیے۔ مختلف کھلاؤ سے لکیر AB کے بیچ سے نہیں گزرتی۔", "Yes! Equal openings make P and Q equally far from A and B.", "جی ہاں! برابر کھلاؤ سے P اور Q، A اور B سے برابر دور ہوتے ہیں۔"),
      [("Nothing. Any opening more than half of AB works for each arc.", "کوئی غلطی نہیں۔ ہر قوس کے لیے AB کے آدھے سے زیادہ کوئی بھی کھلاؤ چلتا ہے۔", "Each opening must be more than half, but the two must also be equal.", "ہر کھلاؤ آدھے سے زیادہ ہو، لیکن دونوں برابر بھی ہوں۔", "different_openings"),
       ("He should have used a protractor for the arcs.", "اسے قوسوں کے لیے زاویہ پیما استعمال کرنا چاہیے تھا۔", "Arcs are drawn with the compass.", "قوسیں پرکار سے لگتی ہیں۔", "tool_mix"),
       ("He should have joined A to B after the arcs.", "اسے قوسوں کے بعد A کو B سے ملانا چاہیے تھا۔", "AB is already drawn first. The problem is the unequal openings.", "AB پہلے ہی کھینچا جاتا ہے۔ مسئلہ غیر برابر کھلاؤ کا ہے۔", "steps_out_of_order")],
      0, qtype="find_error"),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! You know the steps and what they give.", "شاباش! آپ کو قدم اور ان کا نتیجہ آتا ہے۔"),
    "text": T("Ruler: lengths and straight lines. Compass: arcs. Perpendicular bisector: open the compass more than half of AB, use the same opening from A and from B, and join the two crossings. It cuts AB into two equal halves at M and makes 90°, and every point on it is equally far from A and B. For a perpendicular from a point on or off a line, make C and D on the line, then bisect CD.",
              "پیمانہ: لمبائی اور سیدھی لکیریں۔ پرکار: قوسیں۔ عمودی ناصف: پرکار AB کے آدھے سے زیادہ کھولیں، A اور B سے ایک ہی کھلاؤ رکھیں، اور دونوں ملاپ کے نقطے ملا دیں۔ یہ AB کو M پر دو برابر آدھوں میں کاٹتا ہے اور 90° بناتا ہے، اور اس کا ہر نقطہ A اور B سے برابر دور ہوتا ہے۔ لکیر پر یا لکیر سے باہر نقطے سے عمود کے لیے لکیر پر C اور D بنائیں، پھر CD کی تنصیف کریں۔"),
    "points": [T("Same compass opening from both ends.", "دونوں سروں سے پرکار کا ایک ہی کھلاؤ۔"),
               T("The opening must be more than half of AB.", "کھلاؤ AB کے آدھے سے زیادہ ہو۔")]},
 ],
 bank=[
   {"id": "qb_right_angle", "type": "recall", "step": nq("qb_right_angle", ("At what angle, in degrees, does a perpendicular meet the line?", "عمود لکیر سے کتنے درجے کے زاویے پر ملتا ہے؟"), QB1,
      ("Perpendicular lines make a right angle.", "عمود لکیریں قائمہ زاویہ بناتی ہیں۔"),
      ("Right! 90°.", "درست! 90°"), ("A right angle is 90°.", "قائمہ زاویہ 90° کا ہوتا ہے۔"),
      [(180, "180° is a straight line. A perpendicular makes 90°.", "180° سیدھی لکیر ہے۔ عمود 90° بناتا ہے۔", "bisector_is_perpendicular")], qtype=None)},
   {"id": "qb_half_rope", "type": "apply", "step": nq("qb_half_rope", ("The perpendicular bisector of a segment 30 cm long meets it at M. How long is the part from one end to M, in cm?", "30 سینٹی میٹر لمبے قطعۂ خط کا عمودی ناصف اسے M پر ملتا ہے۔ ایک سرے سے M تک حصہ کتنے سینٹی میٹر ہے؟"), QB2,
      ("M is in the middle: half of 30.", "M بیچ میں ہے: 30 کا آدھا۔"),
      ("Right! 30 ÷ 2 = 15 cm.", "درست! 30 ÷ 2 = 15 سینٹی میٹر"), ("Two equal halves: 15.", "دو برابر آدھے: 15"),
      [(30, "30 cm is the whole segment. Half: 15.", "30 سینٹی میٹر پورا قطعۂ خط ہے۔ آدھا: 15", "half_not_taken"),
       (60, "That doubles it. Halve it: 15.", "یہ دگنا کرتا ہے۔ آدھا کریں: 15", "half_not_taken")], qtype=None)},
   {"id": "qb_equal_dist", "type": "apply", "step": nq("qb_equal_dist", ("A point X is on the perpendicular bisector of AB. XB is 9 cm. How long is XA, in cm?", "نقطہ X، AB کے عمودی ناصف پر ہے۔ XB 9 سینٹی میٹر ہے۔ XA کتنے سینٹی میٹر ہے؟"), QB3,
      ("X is equally far from A and from B.", "X، A اور B سے برابر دور ہے۔"),
      ("Right! XA = XB = 9 cm.", "درست! XA = XB = 9 سینٹی میٹر"), ("Equal distances: 9.", "برابر فاصلے: 9"),
      [(18, "That doubles XB. XA is equal to XB: 9.", "یہ XB کو دگنا کرتا ہے۔ XA، XB کے برابر ہے: 9", "different_openings")], qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": ch("qb_find_error", ("Sara draws a perpendicular at a point O on a line. She marks C and D on the line both on the right of O, then bisects CD. What went wrong?", "سارہ لکیر پر نقطہ O سے عمود بناتی ہے۔ وہ لکیر پر C اور D دونوں O کے دائیں طرف لگاتی ہے، پھر CD کی تنصیف کرتی ہے۔ کیا غلطی ہوئی؟"),
      ("C and D must be on opposite sides of O, the same distance from it, so that O is the middle of CD.", "C اور D، O کے الگ الگ طرف اور اس سے برابر فاصلے پر ہونے چاہییں، تاکہ O، CD کا بیچ ہو۔", "Yes! Then the bisector of CD passes through O.", "جی ہاں! تب CD کا ناصف O سے گزرتا ہے۔"),
      [("Nothing. Both points can be on the same side.", "کوئی غلطی نہیں۔ دونوں نقطے ایک ہی طرف ہو سکتے ہیں۔", "Then the middle of CD is not O, so the line misses O.", "تب CD کا بیچ O نہیں، تو لکیر O سے نہیں گزرتی۔", "same_side"),
       ("She should bisect CD with a ruler only.", "اسے CD کی تنصیف صرف پیمانے سے کرنی چاہیے تھی۔", "Bisecting needs the compass arcs.", "تنصیف کے لیے پرکار کی قوسیں چاہییں۔", "tool_mix")],
      0, qtype=None)},
 ],
 review=[
   {"id": "r_half", "type": "apply", "step": nq("r_half", ("A segment is 26 cm long. Its perpendicular bisector meets it at M. How long is one half, in cm?", "ایک قطعۂ خط 26 سینٹی میٹر لمبا ہے۔ اس کا عمودی ناصف اسے M پر ملتا ہے۔ ایک آدھا حصہ کتنے سینٹی میٹر ہے؟"), R1,
      ("Half of 26.", "26 کا آدھا۔"),
      ("Right! 26 ÷ 2 = 13 cm.", "درست! 26 ÷ 2 = 13 سینٹی میٹر"), ("Two equal parts: 13.", "دو برابر حصے: 13"),
      [(26, "26 cm is the whole segment. Half: 13.", "26 سینٹی میٹر پورا قطعۂ خط ہے۔ آدھا: 13", "half_not_taken"),
       (52, "That doubles it. Halve it: 13.", "یہ دگنا کرتا ہے۔ آدھا کریں: 13", "half_not_taken")], qtype=None)},
   {"id": "r_cd", "type": "apply", "step": nq("r_cd", ("O is on a line. C and D are on the line, 8 cm from O on each side. How long is CD, in cm?", "O ایک لکیر پر ہے۔ C اور D لکیر پر O سے دونوں طرف 8 سینٹی میٹر دور ہیں۔ CD کتنے سینٹی میٹر ہے؟"), R2,
      ("One side plus the other side.", "ایک طرف جمع دوسری طرف۔"),
      ("Right! 8 + 8 = 16 cm.", "درست! 8 + 8 = 16 سینٹی میٹر"), ("OC + OD = 8 + 8 = 16.", "OC + OD = 8 + 8 = 16"),
      [(8, "8 cm is only OC. CD = 8 + 8: 16.", "8 سینٹی میٹر صرف OC ہے۔ CD = 8 + 8: 16", "half_not_taken"),
       (4, "That halves 8. CD is both sides added: 16.", "یہ 8 کو آدھا کرتا ہے۔ CD دونوں طرف جمع کر کے: 16", "half_not_taken")], qtype=None)},
 ],
 glossary=[T("Line segment", "قطعۂ خط"), T("Perpendicular bisector", "عمودی ناصف"), T("Perpendicular", "عمود"), T("Midpoint", "درمیانی نقطہ"),
           T("Compass", "پرکار"), T("Arc", "قوس"), T("Ruler", "پیمانہ"), T("Protractor", "زاویہ پیما")],
 flashcards=[
   {"id": "f_pb", "front": T("What is special about every point on the perpendicular bisector of AB?", "AB کے عمودی ناصف کے ہر نقطے میں کیا خاص بات ہے؟"),
    "back": T("It is the same distance from A and from B.", "وہ A اور B سے برابر فاصلے پر ہے۔")},
   {"id": "f_opening", "front": T("How far must the compass be opened to bisect AB?", "AB کی تنصیف کے لیے پرکار کتنا کھولنا چاہیے؟"),
    "back": T("More than half of AB, the same for both arcs.", "AB کے آدھے سے زیادہ، دونوں قوسوں کے لیے ایک جتنا۔")},
 ],
 home_task={"id": "h_draw", "text": T(
   "With a ruler and compass (or a string and pencil) draw a segment 8 cm long and construct its perpendicular bisector. Measure the two halves and the angle. Then draw a line, mark a point on it and another off it, and construct a perpendicular from each.",
   "پیمانے اور پرکار (یا دھاگے اور پنسل) سے 8 سینٹی میٹر لمبا قطعۂ خط بنائیں اور اس کا عمودی ناصف بنائیں۔ دونوں آدھے حصے اور زاویہ ناپیں۔ پھر ایک لکیر بنائیں، اس پر ایک نقطہ اور اس سے باہر ایک نقطہ لگائیں، اور ہر ایک سے عمود بنائیں۔")},
 notes=["Covers the tool for a given length (q1), the meaning of a perpendicular bisector (q2, q8), the length of half a segment (q3, q9), the compass opening (q4), the order of steps (q5, q6) and the perpendicular at a point on a line (q7, q10).",
        "Each wrong answer is a real mistake: a bisector taken to always meet at 90°, the whole length given for half, an opening of exactly half of AB, different openings for the two arcs, steps in the wrong order, and C and D on the same side of O.",
        "Urdu terms to check: قطعۂ خط, عمودی ناصف, عمود, درمیانی نقطہ, پرکار, قوس, پیمانہ and زاویہ پیما, all as in the existing Constructions lessons. کھلاؤ (compass opening) is used in the existing lessons as well; کپڑے کی پٹی (strip of cloth) and تہہ (crease) are new, so a teacher should confirm them."],
 minutes=16,
)

write(lesson)
