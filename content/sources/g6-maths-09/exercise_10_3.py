"""Practice set for Exercise 10.3 of the book: finding unknown angles on a
straight line and in a triangle, checking whether angles make a straight line,
and the angles of an equilateral triangle. The questions are new; only the
kinds of question follow the book."""
from common import (T, say, nq, ch, practice_lesson, practice_intro, write, EX_SKILL,
                    AN_TYPES, AN_LINE, AN_PAIRS, AN_TRIANGLE)
from figs import fig, with_fig, line_fig, tri_fig

SKILL = EX_SKILL["10.3"]
LINE, TRI = 180, 180

# q3: one angle 115 on a straight line
A3 = 115
Q3 = LINE - A3
assert Q3 == 65 and A3 + Q3 == LINE and 360 - A3 == 245 and 90 - 25 == 65
# q4: three angles on a line, 35, x and 85
A4, B4 = 35, 85
Q4 = LINE - A4 - B4
assert Q4 == 60 and A4 + Q4 + B4 == LINE and LINE - A4 == 145 and 360 - A4 - B4 == 240
# q5: triangle with 52 and 71
A5, B5 = 52, 71
Q5 = TRI - A5 - B5
assert Q5 == 57 and A5 + B5 + Q5 == TRI and A5 + B5 == 123 and 360 - A5 - B5 == 237
# q6: which sets of angles can sit side by side on a straight line
SETS = {"a": (95, 85), "b": (100, 70), "c": (120, 70), "d": (130, 60, 40)}
OK = [k for k, v in SETS.items() if sum(v) == LINE]
assert OK == ["a"] and sum(SETS["b"]) == 170 and sum(SETS["c"]) == 190 and sum(SETS["d"]) == 230
# q7: equilateral triangle: all three angles are equal
Q7 = TRI // 3
assert Q7 == 60 and 3 * Q7 == TRI
# q8: bisect one angle of an equilateral triangle
Q8 = Q7 // 2
assert Q8 == 30 and Q7 * 2 == 120
# q9: isosceles triangle, apex 40, two equal base angles
APEX = 40
Q9 = (TRI - APEX) // 2
assert Q9 == 70 and 2 * Q9 + APEX == TRI and TRI - APEX == 140 and (TRI - APEX) % 2 == 0
# q10: right-angled triangle with an acute angle 28
Q10 = TRI - 90 - 28
assert Q10 == 62 and 90 - 28 == 62 and 28 + 62 == 90
# q11: x and x + 30 on a straight line; the larger angle
X11 = (LINE - 30) // 2
Q11 = X11 + 30
assert X11 == 75 and Q11 == 105 and X11 + Q11 == LINE and (LINE - 30) % 2 == 0 and 2 * X11 + 30 == LINE
# q12: exterior angle 125 and one opposite interior angle 50
EXT, OPP = 125, 50
Q12 = EXT - OPP
assert Q12 == 75 and OPP + Q12 == EXT and LINE - EXT == 55 and OPP + Q12 + (LINE - EXT) == TRI
# bank and review
QB1 = TRI
QB2 = LINE - 140
assert QB2 == 40 and 140 + QB2 == LINE
QB3 = TRI - 90 - 35
assert QB3 == 55 and 90 + 35 + QB3 == TRI
R1 = LINE - 72 - 44
assert R1 == 64 and 72 + 44 + R1 == LINE and 72 + 44 == 116
R2 = TRI - 66 - 66
assert R2 == 48 and 66 + 66 + R2 == TRI

F_Q3 = line_fig([Q3], ["x", "115°"],
    "A straight line with a point O on it and a ray from O. The angle on the right of the ray is marked x and the angle on the left, up to the end of the line, is marked 115 degrees.",
    "ایک سیدھی لکیر جس پر نقطہ O ہے اور O سے ایک شعاع۔ شعاع کے دائیں طرف کا زاویہ x اور بائیں طرف کا، لکیر کے سرے تک، 115° لکھا ہے۔")
F_Q4 = line_fig([A4, A4 + Q4], ["35°", "x", "85°"],
    "A straight line with a point O on it and two rays from O that split the line into three angles. From the right they are marked 35 degrees, x and 85 degrees.",
    "ایک سیدھی لکیر جس پر نقطہ O ہے اور O سے دو شعاعیں جو لکیر کو تین زاویوں میں بانٹتی ہیں۔ دائیں سے بائیں یہ 35°، x اور 85° ہیں۔")
F_Q5 = tri_fig(A5, B5, [f"{A5}°", f"{B5}°", "x"],
    "A triangle ABC with the angle at A marked 52 degrees, the angle at B marked 71 degrees and the angle at C marked x.",
    "مثلث ABC جس میں A پر زاویہ 52°، B پر زاویہ 71° اور C پر زاویہ x لکھا ہے۔")
F_Q9 = tri_fig(Q9, Q9, ["x", "x", f"{APEX}°"],
    "An isosceles triangle ABC with two equal sides. The angle at the top, C, is marked 40 degrees. The two equal angles at the base, A and B, are each marked x.",
    "متساوی الساقین مثلث ABC جس کے دو ضلع برابر ہیں۔ اوپر C کا زاویہ 40° ہے۔ قاعدے کے دو برابر زاویوں، A اور B، پر x لکھا ہے۔")
F_Q10 = tri_fig(28, 62, ["28°", "x", "90°"],
    "A right-angled triangle ABC. The angle at A is marked 28 degrees, the angle at B is marked x, and the angle at C is marked 90 degrees.",
    "قائمہ الزاویہ مثلث ABC۔ A پر زاویہ 28° ہے، B پر زاویہ x ہے، اور C پر زاویہ 90° ہے۔")
F_Q11 = line_fig([X11], ["x", "x+30°"],
    "A straight line with a point O on it and a ray from O. The angle on the right of the ray is marked x and the angle on the left is marked x plus 30 degrees.",
    "ایک سیدھی لکیر جس پر نقطہ O ہے اور O سے ایک شعاع۔ شعاع کے دائیں طرف کا زاویہ x اور بائیں طرف کا زاویہ x جمع 30° لکھا ہے۔")

lesson = practice_lesson(
 "10.3", script="exercise_10_3.py",
 title=T("Exercise 10.3 practice: finding unknown angles", "مشق 10.3 کی پریکٹس: نامعلوم زاویے نکالنا"),
 outcome="Find unknown angles on a straight line and in a triangle, check whether angles make a straight line, and use the angles of an equilateral, isosceles and right-angled triangle.",
 prerequisites=[AN_TYPES, AN_LINE, AN_PAIRS, AN_TRIANGLE],
 misconceptions=[
   {"id": "use_360", "description": "Uses 360° for angles on a straight line or in a triangle instead of 180°."},
   {"id": "use_90", "description": "Uses 90° as the total for angles on a straight line, or for the three angles of a triangle."},
   {"id": "stops_at_sum", "description": "Adds the known angles and gives that sum as the answer, without taking it away from 180°."},
   {"id": "forgets_one", "description": "Takes away only one of the known angles from 180° when there are two or more."},
   {"id": "isosceles_halving", "description": "Gives 180° minus the apex angle for each base angle of an isosceles triangle, without halving."},
   {"id": "equation_value", "description": "Gives x when the angle (x + 30)° is asked, or the other way round."},
   {"id": "exterior_supp", "description": "Gives 180° minus the exterior angle where the exterior angle minus the opposite angle is needed."},
 ],
 steps=[
   practice_intro("10.3",
     "Here you find unknown angles on a straight line and in a triangle, and check whether angles make a straight line.",
     "اس میں آپ سیدھی لکیر پر اور مثلث میں نامعلوم زاویے نکالیں گے، اور جانچیں گے کہ زاویے سیدھی لکیر بناتے ہیں یا نہیں۔",
     "Exercise 10.3 is about unknown angles. Ready?", "مشق 10.3 نامعلوم زاویوں کے بارے میں ہے۔ تیار؟"),
   nq("q1_line_total", ("How many degrees do all the angles on a straight line at one point add up to?", "ایک نقطے پر سیدھی لکیر کے سب زاویوں کا مجموعہ کتنے درجے ہوتا ہے؟"), LINE,
      ("A straight angle.", "مستقیم زاویہ۔"),
      ("Right! 180°.", "درست! 180°"), ("A straight line is a straight angle of 180°.", "سیدھی لکیر 180° کا مستقیم زاویہ ہے۔"),
      [(360, "360° is a full turn. A straight line is half of it: 180°.", "360° پورا چکر ہے۔ سیدھی لکیر اس کا آدھا ہے: 180°", "use_360"),
       (90, "90° is a right angle, only half of a straight line: 180°.", "90° قائمہ زاویہ ہے، سیدھی لکیر کا صرف آدھا: 180°", "use_90")], qtype="recall"),
   nq("q2_tri_total", ("How many degrees do the three angles of any triangle add up to?", "کسی بھی مثلث کے تین زاویوں کا مجموعہ کتنے درجے ہوتا ہے؟"), TRI,
      ("The same as a straight line.", "سیدھی لکیر جتنا۔"),
      ("Right! 180°.", "درست! 180°"), ("Any triangle: 180°.", "کوئی بھی مثلث: 180°"),
      [(360, "360° is for a four-sided shape. A triangle: 180°.", "360° چار اضلاع والی شکل کا ہے۔ مثلث: 180°", "use_360"),
       (90, "90° is one right angle. Three angles of a triangle: 180°.", "90° ایک قائمہ زاویہ ہے۔ مثلث کے تین زاویے: 180°", "use_90")], qtype="recall"),
   {"id": "s_idea", "type": "explain",
    "character": say("thinking", "Add the angles you know, then take the sum away from 180°.", "جو زاویے معلوم ہیں انہیں جمع کریں، پھر مجموعہ 180° میں سے گھٹائیں۔"),
    "text": T("Angles on a straight line add up to 180°. The three angles of a triangle add up to 180°. To find an unknown angle: add the angles you know, then 180° minus that sum. An equilateral triangle has three equal angles of 60°. An isosceles triangle has two equal angles. In a right-angled triangle the other two angles add up to 90°. An exterior angle of a triangle equals the sum of the two opposite interior angles.",
              "سیدھی لکیر پر زاویوں کا مجموعہ 180° ہوتا ہے۔ مثلث کے تین زاویوں کا مجموعہ 180° ہوتا ہے۔ نامعلوم زاویہ نکالنے کے لیے: معلوم زاویے جمع کریں، پھر 180° میں سے وہ مجموعہ گھٹائیں۔ مساوی الاضلاع مثلث کے تینوں زاویے برابر، 60° کے، ہوتے ہیں۔ متساوی الساقین مثلث کے دو زاویے برابر ہوتے ہیں۔ قائمہ الزاویہ مثلث میں باقی دو زاویوں کا مجموعہ 90° ہوتا ہے۔ مثلث کا بیرونی زاویہ دو مخالف اندرونی زاویوں کے مجموعے کے برابر ہوتا ہے۔")},
   with_fig(nq("q3_line", ("On the straight line in the picture one angle is 115°. Find x, in degrees.", "تصویر کی سیدھی لکیر پر ایک زاویہ 115° ہے۔ x کتنے درجے کا ہے؟"), Q3,
      ("x + 115 = 180.", "x + 115 = 180"),
      ("Right! 180 − 115 = 65°.", "درست! 180 − 115 = 65°"), ("The two angles add up to 180°: 65.", "دونوں زاویوں کا مجموعہ 180° ہے: 65"),
      [(245, "That is 360 − 115. A straight line adds to 180°: 65.", "یہ 360 − 115 ہے۔ سیدھی لکیر کا مجموعہ 180° ہے: 65", "use_360"),
       (115, "115° is the other angle. x = 180 − 115 = 65.", "115° دوسرا زاویہ ہے۔ x = 180 − 115 = 65", "stops_at_sum"),
       (25, "That is 90 − 65. The total on a line is 180°: x = 65.", "یہ 90 − 65 ہے۔ لکیر پر مجموعہ 180° ہے: x = 65", "use_90")], qtype="recall"), F_Q3),
   with_fig(nq("q4_three", ("Three angles sit side by side on a straight line: 35°, x and 85°. Find x, in degrees.", "ایک سیدھی لکیر پر تین زاویے ساتھ ساتھ ہیں: 35°، x اور 85°۔ x کتنے درجے کا ہے؟"), Q4,
      ("35 + x + 85 = 180.", "35 + x + 85 = 180"),
      ("Right! 35 + 85 = 120, and 180 − 120 = 60°.", "درست! 35 + 85 = 120، اور 180 − 120 = 60°"), ("Add the known angles, then take away from 180: 60.", "معلوم زاویے جمع کریں، پھر 180 میں سے گھٹائیں: 60"),
      [(145, "That takes away only 35. Take away 35 and 85: 60.", "اس میں صرف 35 گھٹایا۔ 35 اور 85 دونوں گھٹائیں: 60", "forgets_one"),
       (120, "120° is 35 + 85. x is what is left of 180: 60.", "120° یعنی 35 + 85۔ x وہ ہے جو 180 میں سے بچے: 60", "stops_at_sum"),
       (240, "That uses 360. A straight line is 180°: 60.", "اس میں 360 استعمال ہوا۔ سیدھی لکیر 180° ہے: 60", "use_360")]), F_Q4),
   with_fig(nq("q5_triangle", ("In the triangle, two angles are 52° and 71°. Find the third angle x, in degrees.", "مثلث میں دو زاویے 52° اور 71° ہیں۔ تیسرا زاویہ x کتنے درجے کا ہے؟"), Q5,
      ("52 + 71 + x = 180.", "52 + 71 + x = 180"),
      ("Right! 52 + 71 = 123, and 180 − 123 = 57°.", "درست! 52 + 71 = 123، اور 180 − 123 = 57°"), ("The three angles add up to 180°: 57.", "تین زاویوں کا مجموعہ 180° ہے: 57"),
      [(123, "123° is 52 + 71. x is what is left of 180: 57.", "123° یعنی 52 + 71۔ x وہ ہے جو 180 میں سے بچے: 57", "stops_at_sum"),
       (237, "That is 360 − 123. A triangle adds to 180°: 57.", "یہ 360 − 123 ہے۔ مثلث کا مجموعہ 180° ہے: 57", "use_360"),
       (128, "That takes away only 52. Take away 52 and 71: 57.", "اس میں صرف 52 گھٹایا۔ 52 اور 71 دونوں گھٹائیں: 57", "forgets_one")], qtype="recall"), F_Q5),
   ch("q6_straight", ("Which pair of angles, placed side by side, makes a straight line?", "کون سے دو زاویے، ساتھ ساتھ رکھنے پر، سیدھی لکیر بناتے ہیں؟"),
      ("95° and 85°", "95° اور 85°", "Yes! 95 + 85 = 180, so together they make a straight line.", "جی ہاں! 95 + 85 = 180، تو مل کر سیدھی لکیر بناتے ہیں۔"),
      [("100° and 70°", "100° اور 70°", "100 + 70 = 170. That is 10° short of 180°.", "100 + 70 = 170۔ یہ 180° سے 10° کم ہے۔", "stops_at_sum"),
       ("120° and 70°", "120° اور 70°", "120 + 70 = 190. That is 10° more than 180°.", "120 + 70 = 190۔ یہ 180° سے 10° زیادہ ہے۔", "stops_at_sum"),
       ("130°, 60° and 40°", "130°، 60° اور 40°", "130 + 60 + 40 = 230, not 180.", "130 + 60 + 40 = 230، 180 نہیں۔", "stops_at_sum")],
      3, qtype="apply"),
   nq("q7_equilateral", ("All three angles of an equilateral triangle are equal. How big is each one, in degrees?", "مساوی الاضلاع مثلث کے تینوں زاویے برابر ہیں۔ ہر ایک کتنے درجے کا ہے؟"), Q7,
      ("Share 180° equally among 3 angles.", "180° کو 3 زاویوں میں برابر بانٹیں۔"),
      ("Right! 180 ÷ 3 = 60°.", "درست! 180 ÷ 3 = 60°"), ("3 equal angles that add to 180°: 60 each.", "180° مجموعے والے 3 برابر زاویے: ہر ایک 60°"),
      [(90, "90° is a right angle. Divide 180 by 3: 60.", "90° قائمہ زاویہ ہے۔ 180 کو 3 سے تقسیم کریں: 60", "use_90"),
       (120, "That is 360 ÷ 3. A triangle adds to 180°: 60.", "یہ 360 ÷ 3 ہے۔ مثلث کا مجموعہ 180° ہے: 60", "use_360")], qtype="recall"),
   nq("q8_bisect_tri", ("The angle bisector from one corner of an equilateral triangle cuts that corner's angle into two equal parts. How big is each part, in degrees?", "مساوی الاضلاع مثلث کے ایک کونے کا ناصف زاویہ اس کونے کے زاویے کو دو برابر حصوں میں کاٹتا ہے۔ ہر حصہ کتنے درجے کا ہے؟"), Q8,
      ("The corner angle is 60°. Halve it.", "کونے کا زاویہ 60° ہے۔ اسے آدھا کریں۔"),
      ("Right! 60 ÷ 2 = 30°.", "درست! 60 ÷ 2 = 30°"), ("Each corner is 60°, and half of it is 30°.", "ہر کونا 60° کا ہے، اور اس کا آدھا 30° ہے۔"),
      [(60, "60° is the whole corner angle. Each part is half: 30.", "60° پورے کونے کا زاویہ ہے۔ ہر حصہ آدھا ہے: 30", "stops_at_sum"),
       (90, "A corner of an equilateral triangle is 60°, not 90°. Half is 30.", "مساوی الاضلاع مثلث کا کونا 60° کا ہوتا ہے، 90° کا نہیں۔ آدھا 30° ہے۔", "use_90")]),
   with_fig(nq("q9_isosceles", ("An isosceles triangle has the angle 40° at the top. The two equal angles at the base are each x. Find x, in degrees.", "ایک متساوی الساقین مثلث کے اوپر کا زاویہ 40° ہے۔ قاعدے کے دو برابر زاویے ہر ایک x ہیں۔ x کتنے درجے کا ہے؟"), Q9,
      ("The two base angles share what is left of 180°. 180 − 40 = 140.", "قاعدے کے دونوں زاویے 180° میں سے بچا ہوا بانٹتے ہیں۔ 180 − 40 = 140"),
      ("Right! 140 ÷ 2 = 70°.", "درست! 140 ÷ 2 = 70°"), ("2x + 40 = 180, so 2x = 140 and x = 70.", "2x + 40 = 180، تو 2x = 140 اور x = 70"),
      [(140, "140° is both base angles together. Each one is half: 70.", "140° قاعدے کے دونوں زاویے ملا کر ہیں۔ ہر ایک آدھا ہے: 70", "isosceles_halving"),
       (40, "40° is the top angle. The base angles are 70° each.", "40° اوپر کا زاویہ ہے۔ قاعدے کے زاویے ہر ایک 70° ہیں۔", "stops_at_sum"),
       (50, "That is 90 − 40. The three angles add to 180°: x = 70.", "یہ 90 − 40 ہے۔ تین زاویوں کا مجموعہ 180° ہے: x = 70", "use_90")]), F_Q9),
   with_fig(nq("q10_right", ("In a right-angled triangle one angle is 90° and another is 28°. Find the third angle x, in degrees.", "ایک قائمہ الزاویہ مثلث میں ایک زاویہ 90° اور دوسرا 28° ہے۔ تیسرا زاویہ x کتنے درجے کا ہے؟"), Q10,
      ("The other two angles add up to 90°.", "باقی دو زاویوں کا مجموعہ 90° ہے۔"),
      ("Right! 180 − 90 − 28 = 62°.", "درست! 180 − 90 − 28 = 62°"), ("28 + x = 90, so x = 62.", "28 + x = 90، تو x = 62"),
      [(152, "That is 180 − 28. Also take away the 90°: 62.", "یہ 180 − 28 ہے۔ 90° بھی گھٹائیں: 62", "forgets_one"),
       (118, "That is 90 + 28. x is what is left of 180: 62.", "یہ 90 + 28 ہے۔ x وہ ہے جو 180 میں سے بچے: 62", "stops_at_sum")]), F_Q10),
   with_fig(nq("q11_algebra", ("The angles x° and (x + 30)° sit side by side on a straight line. Find the larger angle, in degrees.", "x° اور (x + 30)° کے زاویے ایک سیدھی لکیر پر ساتھ ساتھ ہیں۔ بڑا زاویہ کتنے درجے کا ہے؟"), Q11,
      ("x + x + 30 = 180. Find x first, then the larger angle.", "x + x + 30 = 180۔ پہلے x نکالیں، پھر بڑا زاویہ۔"),
      ("Right! 2x = 150, x = 75, and the larger angle is 75 + 30 = 105°.", "درست! 2x = 150، x = 75، اور بڑا زاویہ 75 + 30 = 105°"), ("x = 75 is the smaller angle. The larger is x + 30 = 105.", "x = 75 چھوٹا زاویہ ہے۔ بڑا x + 30 = 105 ہے۔"),
      [(75, "75 is x, the smaller angle. The larger one is x + 30: 105.", "75، x ہے، یعنی چھوٹا زاویہ۔ بڑا x + 30 ہے: 105", "equation_value"),
       (150, "150 is 180 − 30. Solve 2x + 30 = 180 first: the larger angle is 105.", "150 یعنی 180 − 30۔ پہلے 2x + 30 = 180 حل کریں: بڑا زاویہ 105 ہے۔", "stops_at_sum")]), F_Q11),
   nq("q12_exterior", ("One side of a triangle is extended. The exterior angle is 125°, and one of the two opposite interior angles is 50°. Find the other opposite interior angle, in degrees.", "ایک مثلث کا ایک ضلع بڑھایا گیا ہے۔ بیرونی زاویہ 125° ہے، اور دو مخالف اندرونی زاویوں میں سے ایک 50° ہے۔ دوسرا مخالف اندرونی زاویہ کتنے درجے کا ہے؟"), Q12,
      ("Exterior angle = the sum of the two opposite interior angles.", "بیرونی زاویہ = دو مخالف اندرونی زاویوں کا مجموعہ"),
      ("Right! 125 − 50 = 75°.", "درست! 125 − 50 = 75°"), ("50 + x = 125, so x = 75.", "50 + x = 125، تو x = 75"),
      [(55, "55° is 180 − 125, the interior angle next to the exterior one. The other opposite angle is 125 − 50 = 75.", "55° یعنی 180 − 125، بیرونی زاویے کے ساتھ والا اندرونی زاویہ۔ دوسرا مخالف زاویہ 125 − 50 = 75 ہے۔", "exterior_supp"),
       (130, "That is 180 − 50. Use exterior angle − 50: 75.", "یہ 180 − 50 ہے۔ بیرونی زاویہ − 50 استعمال کریں: 75", "exterior_supp")]),
   ch("q13_find_error", ("Imran finds the third angle of a triangle with angles 60° and 80°. He writes 360 − 140 = 220°. What went wrong?", "عمران ایک مثلث کا تیسرا زاویہ نکالتا ہے جس کے دو زاویے 60° اور 80° ہیں۔ وہ لکھتا ہے 360 − 140 = 220°۔ کیا غلطی ہوئی؟"),
      ("The angles of a triangle add up to 180°, not 360°. The third angle is 180 − 140 = 40°.", "مثلث کے زاویوں کا مجموعہ 180° ہوتا ہے، 360° نہیں۔ تیسرا زاویہ 180 − 140 = 40° ہے۔", "Yes! 60 + 80 + 40 = 180.", "جی ہاں! 60 + 80 + 40 = 180"),
      [("Nothing. 220° is correct.", "کوئی غلطی نہیں۔ 220° درست ہے۔", "A triangle angle cannot be bigger than 180°, and 220° would break the 180° total.", "مثلث کا زاویہ 180° سے بڑا نہیں ہو سکتا، اور 220° سے 180° کا مجموعہ ٹوٹ جاتا ہے۔", "use_360"),
       ("He should add 60 and 80 and stop: 140°.", "اسے 60 اور 80 جمع کر کے رک جانا چاہیے: 140°۔", "140° is the two known angles together. The third angle is what is left of 180°: 40.", "140° معلوم دو زاویے ملا کر ہیں۔ تیسرا زاویہ وہ ہے جو 180° میں سے بچے: 40", "stops_at_sum")],
      0, qtype="find_error"),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! Add what you know, take it from 180°.", "شاباش! جو معلوم ہے جمع کریں اور 180° میں سے گھٹائیں۔"),
    "text": T("Angles on a straight line add up to 180°, and so do the three angles of a triangle. Unknown angle = 180° minus the sum of the known angles. Equilateral triangle: 60° each. Isosceles: two equal angles, so the base angles are (180° − apex) ÷ 2. Right-angled: the other two add up to 90°. Exterior angle = sum of the two opposite interior angles. Solve for x first when the angle is written with x, then give the angle asked.",
              "سیدھی لکیر پر زاویوں کا مجموعہ 180° ہوتا ہے، اور مثلث کے تین زاویوں کا بھی۔ نامعلوم زاویہ = 180° منفی معلوم زاویوں کا مجموعہ۔ مساوی الاضلاع مثلث: ہر زاویہ 60°۔ متساوی الساقین: دو زاویے برابر، تو قاعدے کا زاویہ (180° − راسی زاویہ) ÷ 2۔ قائمہ الزاویہ: باقی دو کا مجموعہ 90°۔ بیرونی زاویہ = دو مخالف اندرونی زاویوں کا مجموعہ۔ جب زاویہ x کے ساتھ لکھا ہو تو پہلے x نکالیں، پھر پوچھا گیا زاویہ بتائیں۔"),
    "points": [T("Add the known angles, then 180° minus the sum.", "معلوم زاویے جمع کریں، پھر 180° منفی مجموعہ۔"),
               T("Straight line: 180°. Triangle: 180°.", "سیدھی لکیر: 180°۔ مثلث: 180°۔")]},
 ],
 bank=[
   {"id": "qb_tri_total", "type": "recall", "step": nq("qb_tri_total", ("What do the three angles of a triangle add up to, in degrees?", "مثلث کے تین زاویوں کا مجموعہ کتنے درجے ہے؟"), QB1,
      ("Same as a straight line.", "سیدھی لکیر جتنا۔"),
      ("Right! 180°.", "درست! 180°"), ("Any triangle: 180°.", "کوئی بھی مثلث: 180°"),
      [(360, "360° is a full turn. A triangle: 180°.", "360° پورا چکر ہے۔ مثلث: 180°", "use_360")], qtype=None)},
   {"id": "qb_line", "type": "apply", "step": nq("qb_line", ("Two angles are on a straight line. One is 140°. Find the other, in degrees.", "ایک سیدھی لکیر پر دو زاویے ہیں۔ ایک 140° کا ہے۔ دوسرا کتنے درجے کا ہے؟"), QB2,
      ("The two add up to 180°.", "دونوں کا مجموعہ 180° ہے۔"),
      ("Right! 180 − 140 = 40°.", "درست! 180 − 140 = 40°"), ("140 + x = 180, so x = 40.", "140 + x = 180، تو x = 40"),
      [(220, "That is 360 − 140. A straight line is 180°: 40.", "یہ 360 − 140 ہے۔ سیدھی لکیر 180° ہے: 40", "use_360"),
       (140, "140° is the angle we already know. The other is 40.", "140° معلوم زاویہ ہے۔ دوسرا 40° ہے۔", "stops_at_sum")], qtype=None)},
   {"id": "qb_right_tri", "type": "apply", "step": nq("qb_right_tri", ("A right-angled triangle has an angle of 35°. Find its third angle, in degrees.", "ایک قائمہ الزاویہ مثلث میں ایک زاویہ 35° کا ہے۔ اس کا تیسرا زاویہ کتنے درجے کا ہے؟"), QB3,
      ("180 − 90 − 35.", "180 − 90 − 35"),
      ("Right! 180 − 90 − 35 = 55°.", "درست! 180 − 90 − 35 = 55°"), ("The two acute angles add up to 90°: 35 + 55.", "دونوں حادہ زاویوں کا مجموعہ 90° ہے: 35 + 55"),
      [(145, "That is 180 − 35. Also take away the 90°: 55.", "یہ 180 − 35 ہے۔ 90° بھی گھٹائیں: 55", "forgets_one"),
       (125, "That is 90 + 35. The third angle is 90 − 35 = 55.", "یہ 90 + 35 ہے۔ تیسرا زاویہ 90 − 35 = 55 ہے۔", "stops_at_sum")], qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": ch("qb_find_error", ("Rida says the third angle of a triangle with angles 90° and 40° is 90 + 40 = 130°. What went wrong?", "رِدا کہتی ہے ایک مثلث کا تیسرا زاویہ، جس کے دو زاویے 90° اور 40° ہیں، 90 + 40 = 130° ہے۔ کیا غلطی ہوئی؟"),
      ("130° is the sum of the two known angles. The third angle is 180 − 130 = 50°.", "130° دو معلوم زاویوں کا مجموعہ ہے۔ تیسرا زاویہ 180 − 130 = 50° ہے۔", "Yes! 90 + 40 + 50 = 180.", "جی ہاں! 90 + 40 + 50 = 180"),
      [("Nothing. 130° is the third angle.", "کوئی غلطی نہیں۔ 130° تیسرا زاویہ ہے۔", "She stopped before taking the sum away from 180°.", "وہ مجموعے کو 180° سے گھٹانے سے پہلے رک گئی۔", "stops_at_sum"),
       ("The sum should be taken from 360°: 230°.", "مجموعہ 360° میں سے گھٹانا چاہیے: 230°۔", "A triangle adds to 180°, not 360°.", "مثلث کا مجموعہ 180° ہوتا ہے، 360° نہیں۔", "use_360")],
      0, qtype=None)},
 ],
 review=[
   {"id": "r_line_three", "type": "apply", "step": nq("r_line_three", ("Three angles on a straight line are 72°, 44° and x. Find x, in degrees.", "ایک سیدھی لکیر پر تین زاویے 72°، 44° اور x ہیں۔ x کتنے درجے کا ہے؟"), R1,
      ("72 + 44 + x = 180.", "72 + 44 + x = 180"),
      ("Right! 72 + 44 = 116, and 180 − 116 = 64°.", "درست! 72 + 44 = 116، اور 180 − 116 = 64°"), ("Take 116 away from 180: 64.", "180 میں سے 116 گھٹائیں: 64"),
      [(116, "116° is 72 + 44. x is what is left of 180: 64.", "116° یعنی 72 + 44۔ x وہ ہے جو 180 میں سے بچے: 64", "stops_at_sum"),
       (108, "That takes away only 72. Take away 72 and 44: 64.", "اس میں صرف 72 گھٹایا۔ 72 اور 44 دونوں گھٹائیں: 64", "forgets_one")], qtype=None)},
   {"id": "r_iso", "type": "apply", "step": nq("r_iso", ("An isosceles triangle has two equal angles of 66°. Find the third angle, in degrees.", "ایک متساوی الساقین مثلث کے دو برابر زاویے 66° کے ہیں۔ تیسرا زاویہ کتنے درجے کا ہے؟"), R2,
      ("66 + 66 + x = 180.", "66 + 66 + x = 180"),
      ("Right! 66 + 66 = 132, and 180 − 132 = 48°.", "درست! 66 + 66 = 132، اور 180 − 132 = 48°"), ("Take 132 away from 180: 48.", "180 میں سے 132 گھٹائیں: 48"),
      [(132, "132° is the two equal angles together. The third is 48.", "132° دو برابر زاویے ملا کر ہیں۔ تیسرا 48° ہے۔", "stops_at_sum"),
       (114, "That is 180 − 66. Take away both 66° angles: 48.", "یہ 180 − 66 ہے۔ دونوں 66° کے زاویے گھٹائیں: 48", "forgets_one")], qtype=None)},
 ],
 glossary=[T("Straight line", "سیدھی لکیر"), T("Triangle", "مثلث"), T("Equilateral triangle", "مساوی الاضلاع مثلث"), T("Isosceles triangle", "متساوی الساقین مثلث"),
           T("Right-angled triangle", "قائمہ الزاویہ مثلث"), T("Exterior angle", "بیرونی زاویہ"), T("Interior angle", "اندرونی زاویہ"), T("Unknown angle", "نامعلوم زاویہ")],
 flashcards=[
   {"id": "f_totals", "front": T("What do angles on a straight line and angles in a triangle add up to?", "سیدھی لکیر کے زاویوں اور مثلث کے زاویوں کا مجموعہ کتنا ہوتا ہے؟"),
    "back": T("Both add up to 180°.", "دونوں کا مجموعہ 180° ہوتا ہے۔")},
   {"id": "f_iso", "front": T("How do you find a base angle of an isosceles triangle from its top angle?", "متساوی الساقین مثلث کے اوپر کے زاویے سے قاعدے کا زاویہ کیسے نکالتے ہیں؟"),
    "back": T("(180° − top angle) ÷ 2.", "(180° − اوپر کا زاویہ) ÷ 2")},
 ],
 home_task={"id": "h_angles", "text": T(
   "Draw any triangle, measure its three angles with a protractor and add them. Do this for two more triangles. Then draw a straight line with a ray from a point on it, measure both angles and add them. Write what you notice.",
   "کوئی سا بھی مثلث بنائیں، اس کے تینوں زاویے زاویہ پیما سے ناپیں اور جمع کریں۔ دو اور مثلثوں کے ساتھ بھی کریں۔ پھر ایک سیدھی لکیر بنائیں اور اس کے ایک نقطے سے ایک شعاع نکالیں، دونوں زاویے ناپیں اور جمع کریں۔ جو بات نظر آئے لکھیں۔")},
 notes=["Covers the totals of 180° on a straight line and in a triangle (q1, q2), finding an unknown angle with one or two known angles (q3, q4, q5), checking whether angles make a straight line (q6), equilateral, isosceles and right-angled triangles (q7 to q10), an angle written with x (q11) and the exterior angle (q12).",
        "Each wrong answer is a real mistake: using 360° or 90° for the total, stopping at the sum of the known angles, taking away only one known angle, not halving for the base angles of an isosceles triangle, and giving x when the angle (x + 30)° is asked.",
        "Urdu terms to check: سیدھی لکیر, مثلث, مساوی الاضلاع مثلث, متساوی الساقین مثلث, قائمہ الزاویہ مثلث, بیرونی زاویہ, اندرونی زاویہ and نامعلوم زاویہ, all as in the existing Angles and Constructions lessons. راسی زاویہ (apex angle, in the summary) is new, so a teacher should confirm it."],
 minutes=18,
)

write(lesson)
