"""Practice set for Exercise 10.2 of the book: bisecting angles and building
30, 45, 60, 75, 90, 105, 120 and 150 degrees with a compass. The app cannot check
a real drawing, so the questions are about which step gives which angle. The
questions are new; only the kinds of question follow the book."""
import math

from common import (T, say, nq, ch, practice_lesson, practice_intro, write, EX_SKILL, CO_ANGLES, AN_TYPES)
from figs import (fig, with_fig, label, dot, seg, at_angle, angle_arc, rays_fig, r1)

SKILL = EX_SKILL["10.2"]

# How each angle is made from the basic angle 60 (arcs of one radius make an equilateral triangle).
BASIC = 60
assert math.isclose(math.dist((0, 0), (1, 0)), math.dist((0, 0), (math.cos(math.radians(BASIC)), math.sin(math.radians(BASIC)))))
def mid(a, b):
    assert (a + b) % 2 == 0
    return (a + b) // 2
BUILD = {
    60: BASIC, 120: BASIC + BASIC, 30: mid(0, BASIC), 90: mid(BASIC, 120), 45: mid(0, 90),
    75: mid(BASIC, 90), 105: mid(90, 120), 150: mid(120, 180),
}
assert sorted(BUILD) == [30, 45, 60, 75, 90, 105, 120, 150] and all(k == v for k, v in BUILD.items())

# q3: bisect an 80 degree angle
Q3 = 80 // 2
assert Q3 == 40 and 80 * 2 == 160
# q4: bisect 60, then bisect the 30 again
Q4 = 60 // 2 // 2
assert Q4 == 15 and 60 // 2 == 30
# q5: halfway between the 90 and 120 degree rays
Q5 = (90 + 120) // 2
assert Q5 == 105 and 90 + 120 == 210 and 120 - 90 == 30 and (120 - 90) // 2 == 15
# q7: bisect between the 120 degree ray and the straight line (180)
Q7 = (120 + 180) // 2
assert Q7 == 150 and 120 // 2 == 60 and 120 + 180 == 300 and 180 - 150 == 30
# q9: arc from O cuts arms at P, Q; angle POQ = 70; R is on the bisector
POQ = 70
Q9 = POQ // 2
assert Q9 == 35 and POQ // 2 + POQ // 2 == POQ and 2 * POQ == 140
# q10: three 60 steps in a row from the base arm
Q10 = 3 * BASIC
assert Q10 == 180 and 2 * BASIC == 120 and 6 * BASIC == 360
# bank and review
QB1 = BASIC
QB2 = 50 // 2
assert QB2 == 25 and 50 * 2 == 100
QB3 = mid(60, 120)
assert QB3 == 90 and 60 + 120 == 180
R1 = 150 // 2
assert R1 == 75 and 150 * 2 == 300
R2 = mid(30, 60)
assert R2 == 45 and 30 + 60 == 90

# figure: an 80 degree angle with its bisector
O3, L3 = (28, 64), 48
F_BI = fig(125, 80,
    "An angle of 80 degrees at point O, with a dashed line from O that splits it into two equal parts. The two parts are each marked with a question mark.",
    "نقطہ O پر 80 درجے کا زاویہ، اور O سے ایک ڈیش لکیر جو اسے دو برابر حصوں میں بانٹتی ہے۔ دونوں حصوں پر سوالیہ نشان ہے۔",
    [seg(O3, at_angle(O3, L3, 0)), seg(O3, at_angle(O3, L3, 80)), seg(O3, at_angle(O3, L3, 40), dashed=True), dot(O3),
     angle_arc(O3, 0, 80, 12), label(at_angle(O3, 22, 20), "?"), label(at_angle(O3, 22, 60), "?"), label((O3[0] - 9, O3[1] + 8), "O"),
     label(at_angle(O3, L3 + 6, 80), "80°")])

# figure: rays at 90 and 120 degrees on one base arm, with the ray in between dashed
F_MID = rays_fig(130, 80, (65, 68), 52, [(90, "90°"), (105, "?"), (120, "120°")],
    "A base arm going right from a point O. Three rays leave O: one straight up marked 90 degrees, one at 120 degrees marked 120 degrees, and a dashed ray between them marked with a question mark.",
    "نقطہ O سے دائیں طرف ایک بنیادی بازو۔ O سے تین شعاعیں نکلتی ہیں: ایک سیدھی اوپر جس پر 90° لکھا ہے، ایک 120° پر جس پر 120° لکھا ہے، اور دونوں کے بیچ ایک ڈیش شعاع جس پر سوالیہ نشان ہے۔",
    dashed=(105,))

# figure: the basic angle 60 with arcs
O6 = (30, 62)
F_60 = rays_fig(125, 80, O6, 60, [(60, "60°")],
    "A base arm going right from O and a ray at 60 degrees to it, marked 60 degrees. This basic angle comes from an equilateral triangle of compass arcs.",
    "O سے دائیں طرف ایک بنیادی بازو اور اس کے ساتھ 60° پر ایک شعاع جس پر 60° لکھا ہے۔ یہ بنیادی زاویہ پرکار کی قوسوں کے مساوی الاضلاع مثلث سے بنتا ہے۔",
    arcs=[(0, 60, 14)])

lesson = practice_lesson(
 "10.2", script="exercise_10_2.py",
 title=T("Exercise 10.2 practice: bisecting and building angles", "مشق 10.2 کی پریکٹس: زاویوں کی تنصیف اور تعمیر"),
 outcome="Bisect an angle with a compass and build the angles 30°, 45°, 60°, 75°, 90°, 105°, 120° and 150° from the basic angle 60°, knowing which step gives which angle.",
 prerequisites=[CO_ANGLES, AN_TYPES],
 misconceptions=[
   {"id": "bisect_not_half", "description": "Divides by 3 or doubles when asked for the angle after bisecting, instead of halving."},
   {"id": "add_not_mid", "description": "Adds the two angles instead of going halfway between them when a ray is made between two rays."},
   {"id": "gap_not_angle", "description": "Gives the half of the gap between two rays instead of the angle the new ray makes with the base arm."},
   {"id": "wrong_start_angle", "description": "Bisects the wrong angle, for example bisects 60° to get 45°, or 120° to get 75°."},
   {"id": "steps_out_of_order", "description": "Puts the steps of bisecting an angle in the wrong order."},
   {"id": "basic_angle_mix", "description": "Thinks the angle from three equal arcs is 90° or 30° rather than 60°."},
 ],
 steps=[
   practice_intro("10.2",
     "Here you practise bisecting angles and building 30°, 45°, 60°, 75°, 90°, 105°, 120° and 150°. You will work out which step gives which angle.",
     "اس میں آپ زاویوں کی تنصیف اور 30°، 45°، 60°، 75°، 90°، 105°، 120° اور 150° کی تعمیر دہرائیں گے۔ آپ سوچیں گے کہ کون سا قدم کون سا زاویہ دیتا ہے۔",
     "Exercise 10.2 is about angles. Ready?", "مشق 10.2 زاویوں کے بارے میں ہے۔ تیار؟"),
   with_fig(ch("q1_basic", ("Equal compass arcs make an equilateral triangle. What is the basic angle you build first?", "برابر پرکار کی قوسیں مساوی الاضلاع مثلث بناتی ہیں۔ سب سے پہلے کون سا بنیادی زاویہ بنتا ہے؟"),
      ("60°", "60°", "Yes! Every angle of an equilateral triangle is 60°.", "جی ہاں! مساوی الاضلاع مثلث کا ہر زاویہ 60° ہوتا ہے۔"),
      [("30°", "30°", "30° comes later, by bisecting the 60°.", "30° بعد میں 60° کی تنصیف سے ملتا ہے۔", "basic_angle_mix"),
       ("90°", "90°", "90° comes by bisecting the angle between 60° and 120°.", "90° 60° اور 120° کے بیچ کی تنصیف سے ملتا ہے۔", "basic_angle_mix"),
       ("45°", "45°", "45° comes by bisecting 90°.", "45° 90° کی تنصیف سے ملتا ہے۔", "basic_angle_mix")],
      1, qtype="recall"), F_60),
   ch("q2_bisect", ("To bisect an angle means to:", "زاویے کی تنصیف کرنے کا مطلب ہے:"),
      ("cut it into two equal parts", "اسے دو برابر حصوں میں کاٹنا", "Yes! The bisector leaves two equal angles.", "جی ہاں! ناصف دو برابر زاویے چھوڑتا ہے۔"),
      [("cut it into three equal parts", "اسے تین برابر حصوں میں کاٹنا", "Three parts is a trisection. Bisect means two.", "تین حصے تثلیث ہے۔ تنصیف کا مطلب دو ہے۔", "bisect_not_half"),
       ("make it twice as big", "اسے دگنا بڑا کرنا", "Making it twice as big is the opposite of halving.", "دگنا بڑا کرنا آدھا کرنے کا الٹ ہے۔", "bisect_not_half"),
       ("make it a right angle", "اسے قائمہ زاویہ بنانا", "Bisecting does not change it to 90°. It halves whatever angle you have.", "تنصیف اسے 90° نہیں بناتی۔ جو بھی زاویہ ہو اسے آدھا کرتی ہے۔", "bisect_not_half")],
      0, qtype="recall"),
   {"id": "s_idea", "type": "explain",
    "character": say("thinking", "Start with 60° and halve or add. Every other angle follows.", "60° سے شروع کریں اور آدھا کریں یا جمع کریں۔ باقی سب زاویے اسی سے بنتے ہیں۔"),
    "text": T("To bisect an angle: draw an arc from the vertex that cuts both arms; from those two points draw equal arcs that cross; join the vertex to the crossing. Build from 60°: 30° = bisect 60°. 120° = two steps of 60°. 90° = bisect the angle between 60° and 120°. 45° = bisect 90°. 75° = halfway between 60° and 90°. 105° = halfway between 90° and 120°. 150° = halfway between 120° and the straight line, 180°.",
              "زاویے کی تنصیف کے لیے: راس سے ایسی قوس لگائیں جو دونوں بازو کاٹے؛ ان دو نقطوں سے برابر قوسیں لگائیں جو ایک دوسرے کو کاٹیں؛ راس کو ملاپ سے ملائیں۔ 60° سے بنائیں: 30° = 60° کی تنصیف۔ 120° = 60° کے دو قدم۔ 90° = 60° اور 120° کے بیچ کی تنصیف۔ 45° = 90° کی تنصیف۔ 75° = 60° اور 90° کے بیچ۔ 105° = 90° اور 120° کے بیچ۔ 150° = 120° اور سیدھی لکیر 180° کے بیچ۔")},
   with_fig(nq("q3_half", ("The bisector of an 80° angle is drawn, as in the picture. How big is each of the two parts, in degrees?", "تصویر کی طرح 80° کے زاویے کا ناصف کھینچا گیا ہے۔ دونوں حصوں میں سے ہر ایک کتنے درجے کا ہے؟"), Q3,
      ("Two equal parts: halve 80.", "دو برابر حصے: 80 کو آدھا کریں۔"),
      ("Right! 80 ÷ 2 = 40°.", "درست! 80 ÷ 2 = 40°"), ("A bisector halves the angle: 40.", "ناصف زاویے کو آدھا کرتا ہے: 40"),
      [(80, "80° is the whole angle. Each part is half: 40.", "80° پورا زاویہ ہے۔ ہر حصہ آدھا ہے: 40", "bisect_not_half"),
       (160, "That doubles it. Halve it: 40.", "یہ دگنا کرتا ہے۔ آدھا کریں: 40", "bisect_not_half")], qtype="recall"), F_BI),
   nq("q4_twice", ("Mina builds 60°, bisects it, then bisects the new angle again. How big is the smallest angle now, in degrees?", "مینا 60° بناتی ہے، اس کی تنصیف کرتی ہے، پھر نئے زاویے کی دوبارہ تنصیف کرتی ہے۔ اب سب سے چھوٹا زاویہ کتنے درجے کا ہے؟"), Q4,
      ("60 halved, then halved again.", "60 کا آدھا، پھر دوبارہ آدھا۔"),
      ("Right! 60 → 30 → 15°.", "درست! 60 ← 30 ← 15°"), ("60 ÷ 2 = 30, and 30 ÷ 2 = 15.", "60 ÷ 2 = 30، اور 30 ÷ 2 = 15"),
      [(30, "30° is after one bisection. She bisected twice: 15.", "30° ایک تنصیف کے بعد ہے۔ اس نے دو بار تنصیف کی: 15", "bisect_not_half"),
       (120, "That doubles 60. Bisecting halves: 15 after two bisections.", "یہ 60 کو دگنا کرتا ہے۔ تنصیف آدھا کرتی ہے: دو تنصیفوں کے بعد 15", "bisect_not_half")]),
   with_fig(nq("q5_105", ("A ray is made halfway between the 90° ray and the 120° ray, as in the picture. What angle does it make with the base arm, in degrees?", "تصویر کی طرح 90° کی شعاع اور 120° کی شعاع کے ٹھیک بیچ میں ایک شعاع بنائی گئی ہے۔ وہ بنیادی بازو کے ساتھ کتنے درجے کا زاویہ بناتی ہے؟"), Q5,
      ("Halfway between 90 and 120. Find the middle number.", "90 اور 120 کے ٹھیک بیچ میں۔ درمیانی عدد نکالیں۔"),
      ("Right! (90 + 120) ÷ 2 = 105°.", "درست! (90 + 120) ÷ 2 = 105°"), ("The gap is 30°, half is 15°, and 90 + 15 = 105.", "فاصلہ 30° ہے، آدھا 15° ہے، اور 90 + 15 = 105"),
      [(210, "210 is 90 + 120. Halfway means half of that: 105.", "210 یعنی 90 + 120۔ بیچ کا مطلب اس کا آدھا ہے: 105", "add_not_mid"),
       (15, "15° is half the gap. Measure from the base arm: 90 + 15 = 105.", "15° فاصلے کا آدھا ہے۔ بنیادی بازو سے ناپیں: 90 + 15 = 105", "gap_not_angle"),
       (30, "30° is the whole gap between the rays. Halfway from the base: 105.", "30° دونوں شعاعوں کے بیچ کا پورا فاصلہ ہے۔ بنیاد سے آدھے راستے پر: 105", "gap_not_angle")]), F_MID),
   ch("q6_which", ("Which step gives a 45° angle?", "کون سا قدم 45° کا زاویہ دیتا ہے؟"),
      ("Bisect a 90° angle", "90° کے زاویے کی تنصیف", "Yes! 90 ÷ 2 = 45°.", "جی ہاں! 90 ÷ 2 = 45°"),
      [("Bisect a 60° angle", "60° کے زاویے کی تنصیف", "That gives 30°.", "اس سے 30° ملتا ہے۔", "wrong_start_angle"),
       ("Bisect a 120° angle", "120° کے زاویے کی تنصیف", "That gives 60°.", "اس سے 60° ملتا ہے۔", "wrong_start_angle"),
       ("Make two 60° steps", "60° کے دو قدم بنانا", "That gives 120°.", "اس سے 120° ملتا ہے۔", "wrong_start_angle")],
      2, qtype="apply"),
   nq("q7_150", ("Aziz makes a 120° ray, then bisects the angle between his 120° ray and the straight line (180°). What angle does the new ray make with the base arm, in degrees?", "عزیز 120° کی شعاع بناتا ہے، پھر اپنی 120° کی شعاع اور سیدھی لکیر (180°) کے بیچ کے زاویے کی تنصیف کرتا ہے۔ نئی شعاع بنیادی بازو کے ساتھ کتنے درجے کا زاویہ بناتی ہے؟"), Q7,
      ("Halfway between 120 and 180.", "120 اور 180 کے ٹھیک بیچ میں۔"),
      ("Right! (120 + 180) ÷ 2 = 150°.", "درست! (120 + 180) ÷ 2 = 150°"), ("The gap is 60°, half is 30°, and 120 + 30 = 150.", "فاصلہ 60° ہے، آدھا 30° ہے، اور 120 + 30 = 150"),
      [(60, "60° is half of 120°, or the gap. The ray is 150° from the base arm.", "60° 120° کا آدھا یا فاصلہ ہے۔ شعاع بنیادی بازو سے 150° پر ہے۔", "gap_not_angle"),
       (300, "300 is 120 + 180. Halfway means half of that: 150.", "300 یعنی 120 + 180۔ بیچ کا مطلب اس کا آدھا ہے: 150", "add_not_mid"),
       (30, "30° is half the gap. From the base arm: 120 + 30 = 150.", "30° فاصلے کا آدھا ہے۔ بنیادی بازو سے: 120 + 30 = 150", "gap_not_angle")]),
   ch("q8_order", ("Hamza bisects an angle. His steps are mixed up: X) join the vertex to where the arcs cross; Y) draw equal arcs from the two cut points so that they cross; Z) draw an arc from the vertex that cuts both arms. What is the right order?", "حمزہ ایک زاویے کی تنصیف کرتا ہے۔ اس کے قدم الٹ پلٹ ہو گئے ہیں: X) راس کو قوسوں کے ملاپ سے ملائیں؛ Y) کٹے ہوئے دو نقطوں سے برابر قوسیں لگائیں جو ایک دوسرے کو کاٹیں؛ Z) راس سے قوس لگائیں جو دونوں بازو کاٹے۔ صحیح ترتیب کیا ہے؟"),
      ("Z, then Y, then X", "Z، پھر Y، پھر X", "Yes! Cut the arms, cross the arcs, then join.", "جی ہاں! بازو کاٹیں، قوسیں ملائیں، پھر جوڑیں۔"),
      [("X, then Z, then Y", "X، پھر Z، پھر Y", "You cannot join to the crossing before it exists.", "ملاپ بننے سے پہلے اس سے جوڑ نہیں سکتے۔", "steps_out_of_order"),
       ("Y, then Z, then X", "Y، پھر Z، پھر X", "The equal arcs start from the points cut on the arms, so Z comes first.", "برابر قوسیں بازوؤں پر کٹے نقطوں سے لگتی ہیں، تو Z پہلے آتا ہے۔", "steps_out_of_order"),
       ("Z, then X, then Y", "Z، پھر X، پھر Y", "X needs the crossing from Y.", "X کو Y کا ملاپ چاہیے۔", "steps_out_of_order")],
      0, qtype="apply"),
   nq("q9_bisector_ray", ("The arc from O cuts the arms at P and Q, and angle POQ is 70°. The line from O through the crossing R of the equal arcs bisects the angle. How big is angle POR, in degrees?", "O سے لگی قوس بازوؤں کو P اور Q پر کاٹتی ہے، اور زاویہ POQ 70° ہے۔ برابر قوسوں کے ملاپ R سے گزرنے والی O کی لکیر زاویے کی تنصیف کرتی ہے۔ زاویہ POR کتنے درجے کا ہے؟"), Q9,
      ("OR bisects angle POQ.", "OR زاویہ POQ کی تنصیف کرتی ہے۔"),
      ("Right! 70 ÷ 2 = 35°.", "درست! 70 ÷ 2 = 35°"), ("Half of 70 is 35.", "70 کا آدھا 35 ہے۔"),
      [(70, "70° is the whole angle POQ. POR is half: 35.", "70° پورا زاویہ POQ ہے۔ POR آدھا ہے: 35", "bisect_not_half"),
       (140, "That doubles 70. Halve it: 35.", "یہ 70 کو دگنا کرتا ہے۔ آدھا کریں: 35", "bisect_not_half")]),
   nq("q10_three_steps", ("Kashif makes three 60° steps in a row from the base arm, one after the other. What angle does his last ray make with the base arm, in degrees?", "کاشف بنیادی بازو سے لگاتار تین 60° کے قدم بناتا ہے۔ اس کی آخری شعاع بنیادی بازو کے ساتھ کتنے درجے کا زاویہ بناتی ہے؟"), Q10,
      ("Three steps of 60°.", "60° کے تین قدم۔"),
      ("Right! 3 × 60 = 180°. The last ray is in line with the base arm: a straight line.", "درست! 3 × 60 = 180°۔ آخری شعاع بنیادی بازو کی سیدھ میں ہے: سیدھی لکیر۔"), ("60 + 60 + 60 = 180.", "60 + 60 + 60 = 180"),
      [(120, "120° is two steps. He made three: 180.", "120° دو قدم ہیں۔ اس نے تین بنائے: 180", "basic_angle_mix"),
       (360, "360° would be six steps. Three steps: 180.", "360° چھ قدم ہوں گے۔ تین قدم: 180", "basic_angle_mix")]),
   ch("q11_find_error", ("Zain says: to make a 75° angle, I bisect the 60° angle. What went wrong?", "زین کہتا ہے: 75° کا زاویہ بنانے کے لیے میں 60° کے زاویے کی تنصیف کرتا ہوں۔ کیا غلطی ہوئی؟"),
      ("Bisecting 60° gives 30°. For 75° you bisect the angle between the 60° and 90° rays.", "60° کی تنصیف سے 30° ملتا ہے۔ 75° کے لیے 60° اور 90° کی شعاعوں کے بیچ کے زاویے کی تنصیف کرتے ہیں۔", "Yes! (60 + 90) ÷ 2 = 75.", "جی ہاں! (60 + 90) ÷ 2 = 75"),
      [("Nothing. Bisecting 60° gives 75°.", "کوئی غلطی نہیں۔ 60° کی تنصیف سے 75° ملتا ہے۔", "Half of 60° is 30°, not 75°.", "60° کا آدھا 30° ہے، 75° نہیں۔", "wrong_start_angle"),
       ("He should bisect the 120° angle.", "اسے 120° کے زاویے کی تنصیف کرنی چاہیے۔", "That gives 60°.", "اس سے 60° ملتا ہے۔", "wrong_start_angle")],
      1, qtype="find_error"),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! One basic angle makes a whole family.", "شاباش! ایک بنیادی زاویے سے پورا خاندان بنتا ہے۔"),
    "text": T("Bisecting halves an angle: 80° gives 40°. Basic angle 60°. 30° = bisect 60°; 120° = 60° twice; 90° = halfway between 60° and 120°; 45° = bisect 90°; 75° = halfway between 60° and 90°; 105° = halfway between 90° and 120°; 150° = halfway between 120° and 180°. Halfway means add the two angles and halve, measured from the base arm.",
              "تنصیف زاویے کو آدھا کرتی ہے: 80° سے 40°۔ بنیادی زاویہ 60°۔ 30° = 60° کی تنصیف؛ 120° = 60° دو بار؛ 90° = 60° اور 120° کے بیچ؛ 45° = 90° کی تنصیف؛ 75° = 60° اور 90° کے بیچ؛ 105° = 90° اور 120° کے بیچ؛ 150° = 120° اور 180° کے بیچ۔ بیچ کا مطلب دونوں زاویے جمع کر کے آدھا کرنا ہے، بنیادی بازو سے ناپتے ہوئے۔"),
    "points": [T("Bisect means halve: two equal parts.", "تنصیف یعنی آدھا کرنا: دو برابر حصے۔"),
               T("Halfway: add the two angles, then halve.", "بیچ میں: دونوں زاویے جمع کریں، پھر آدھا کریں۔")]},
 ],
 bank=[
   {"id": "qb_basic", "type": "recall", "step": nq("qb_basic", ("How many degrees is each angle of an equilateral triangle, the basic angle of compass constructions?", "مساوی الاضلاع مثلث کا ہر زاویہ کتنے درجے کا ہے، یعنی پرکار کی تعمیرات کا بنیادی زاویہ؟"), QB1,
      ("Three equal angles add up to 180°.", "تین برابر زاویوں کا مجموعہ 180° ہے۔"),
      ("Right! 60°.", "درست! 60°"), ("180 ÷ 3 = 60.", "180 ÷ 3 = 60"),
      [(90, "90° is a right angle. The basic angle is 60°.", "90° قائمہ زاویہ ہے۔ بنیادی زاویہ 60° ہے۔", "basic_angle_mix"),
       (30, "30° is half of the basic angle.", "30° بنیادی زاویے کا آدھا ہے۔", "basic_angle_mix")], qtype=None)},
   {"id": "qb_bisect_50", "type": "apply", "step": nq("qb_bisect_50", ("A 50° angle is bisected. How big is each part, in degrees?", "50° کے زاویے کی تنصیف کی گئی۔ ہر حصہ کتنے درجے کا ہے؟"), QB2,
      ("Halve 50.", "50 کو آدھا کریں۔"),
      ("Right! 50 ÷ 2 = 25°.", "درست! 50 ÷ 2 = 25°"), ("Two equal parts of 25°.", "25° کے دو برابر حصے۔"),
      [(50, "50° is the whole angle. Each part is half: 25.", "50° پورا زاویہ ہے۔ ہر حصہ آدھا ہے: 25", "bisect_not_half"),
       (100, "That doubles it. Halve it: 25.", "یہ دگنا کرتا ہے۔ آدھا کریں: 25", "bisect_not_half")], qtype=None)},
   {"id": "qb_mid", "type": "apply", "step": nq("qb_mid", ("A ray is made halfway between the 60° ray and the 120° ray. What angle does it make with the base arm, in degrees?", "60° کی شعاع اور 120° کی شعاع کے ٹھیک بیچ میں شعاع بنائی گئی۔ وہ بنیادی بازو کے ساتھ کتنے درجے کا زاویہ بناتی ہے؟"), QB3,
      ("Halfway between 60 and 120.", "60 اور 120 کے ٹھیک بیچ میں۔"),
      ("Right! (60 + 120) ÷ 2 = 90°.", "درست! (60 + 120) ÷ 2 = 90°"), ("The gap is 60°, half is 30°, and 60 + 30 = 90.", "فاصلہ 60° ہے، آدھا 30° ہے، اور 60 + 30 = 90"),
      [(180, "180 is 60 + 120. Halfway means half of that: 90.", "180 یعنی 60 + 120۔ بیچ کا مطلب اس کا آدھا ہے: 90", "add_not_mid"),
       (30, "30° is half the gap. From the base arm: 60 + 30 = 90.", "30° فاصلے کا آدھا ہے۔ بنیادی بازو سے: 60 + 30 = 90", "gap_not_angle")], qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": ch("qb_find_error", ("Hina bisects a 40° angle and says one part is 20° and the other part is 40°. What went wrong?", "حنا 40° کے زاویے کی تنصیف کرتی ہے اور کہتی ہے ایک حصہ 20° اور دوسرا حصہ 40° ہے۔ کیا غلطی ہوئی؟"),
      ("A bisector makes two equal parts. Both parts are 20°.", "ناصف دو برابر حصے بناتا ہے۔ دونوں حصے 20° کے ہیں۔", "Yes! 20° + 20° = 40°.", "جی ہاں! 20° + 20° = 40°"),
      [("Nothing. A bisector can make unequal parts.", "کوئی غلطی نہیں۔ ناصف غیر برابر حصے بھی بنا سکتا ہے۔", "Bisect means equal parts.", "تنصیف کا مطلب برابر حصے ہے۔", "bisect_not_half"),
       ("Both parts should be 40°.", "دونوں حصے 40° کے ہونے چاہییں۔", "The two parts add up to the whole angle, 40°.", "دونوں حصوں کا مجموعہ پورا زاویہ، 40°، ہوتا ہے۔", "bisect_not_half")],
      0, qtype=None)},
 ],
 review=[
   {"id": "r_bisect_150", "type": "apply", "step": nq("r_bisect_150", ("A 150° angle is bisected. How big is each part, in degrees?", "150° کے زاویے کی تنصیف کی گئی۔ ہر حصہ کتنے درجے کا ہے؟"), R1,
      ("Halve 150.", "150 کو آدھا کریں۔"),
      ("Right! 150 ÷ 2 = 75°.", "درست! 150 ÷ 2 = 75°"), ("Two equal parts: 75.", "دو برابر حصے: 75"),
      [(150, "150° is the whole angle. Each part is half: 75.", "150° پورا زاویہ ہے۔ ہر حصہ آدھا ہے: 75", "bisect_not_half"),
       (300, "That doubles it. Halve it: 75.", "یہ دگنا کرتا ہے۔ آدھا کریں: 75", "bisect_not_half")], qtype=None)},
   {"id": "r_mid_45", "type": "apply", "step": nq("r_mid_45", ("A ray is made halfway between the 30° ray and the 60° ray. What angle does it make with the base arm, in degrees?", "30° کی شعاع اور 60° کی شعاع کے ٹھیک بیچ میں شعاع بنائی گئی۔ وہ بنیادی بازو کے ساتھ کتنے درجے کا زاویہ بناتی ہے؟"), R2,
      ("Halfway between 30 and 60.", "30 اور 60 کے ٹھیک بیچ میں۔"),
      ("Right! (30 + 60) ÷ 2 = 45°.", "درست! (30 + 60) ÷ 2 = 45°"), ("The gap is 30°, half is 15°, and 30 + 15 = 45.", "فاصلہ 30° ہے، آدھا 15° ہے، اور 30 + 15 = 45"),
      [(90, "90 is 30 + 60. Halfway means half of that: 45.", "90 یعنی 30 + 60۔ بیچ کا مطلب اس کا آدھا ہے: 45", "add_not_mid"),
       (15, "15° is half the gap. From the base arm: 30 + 15 = 45.", "15° فاصلے کا آدھا ہے۔ بنیادی بازو سے: 30 + 15 = 45", "gap_not_angle")], qtype=None)},
 ],
 glossary=[T("Bisect", "تنصیف کرنا"), T("Angle bisector", "ناصف زاویہ"), T("Compass", "پرکار"), T("Arc", "قوس"), T("Vertex", "راس"),
           T("Arm", "بازو"), T("Equilateral triangle", "مساوی الاضلاع مثلث"), T("Basic angle", "بنیادی زاویہ")],
 flashcards=[
   {"id": "f_75", "front": T("How do you build 75° and 105°?", "75° اور 105° کیسے بنتے ہیں؟"),
    "back": T("75° is halfway between 60° and 90°; 105° is halfway between 90° and 120°.", "75°، 60° اور 90° کے بیچ ہے؛ 105°، 90° اور 120° کے بیچ۔")},
   {"id": "f_150", "front": T("How do you build 150°?", "150° کیسے بنتا ہے؟"),
    "back": T("Halfway between 120° and the straight line, 180°.", "120° اور سیدھی لکیر، 180°، کے بیچ۔")},
 ],
 home_task={"id": "h_angles", "text": T(
   "With ruler and compass, construct 60° and then bisect it to get 30°. Then build 90°, 45° and 150°. Check each angle with a protractor and write how far off you were.",
   "پیمانے اور پرکار سے 60° بنائیں اور اس کی تنصیف کر کے 30° بنائیں۔ پھر 90°، 45° اور 150° بنائیں۔ ہر زاویہ زاویہ پیما سے جانچیں اور لکھیں کہ کتنا فرق تھا۔")},
 notes=["Covers the basic angle 60° (q1), what bisect means (q2, q3, q9), bisecting twice (q4), going halfway between two rays for 75°, 105° and 150° (q5, q7, q11), which step gives 45° (q6), the order of steps (q8) and three 60° steps making a straight line (q10).",
        "Each wrong answer is a real mistake: dividing by 3 or doubling instead of halving, adding the two angles instead of going halfway, giving half the gap instead of the angle from the base arm, and bisecting the wrong angle.",
        "Urdu terms to check: تنصیف کرنا, ناصف زاویہ, پرکار, قوس, راس, بازو, مساوی الاضلاع مثلث and بنیادی زاویہ, all as in the existing Constructions lessons. تثلیث (trisection, in a wrong-answer feedback) is new, so a teacher should confirm it."],
 minutes=16,
)

write(lesson)
