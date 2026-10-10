"""Practice set for Exercise 9.2 of the book: parallel, intersecting and
perpendicular lines, and the angles a transversal makes. The questions are
new; only the kinds of question follow the book."""
from common import (T, say, nq, ch, practice_lesson, practice_intro, write, EX_SKILL,
                    SY_LINES, AN_LINE, AN_PAIRS)
from figs import (fig, with_fig, seg, poly, label, dot, transversal_figure, theta_for, corner_size, LINE)

SKILL = EX_SKILL["9.2"]


def fig_for(given_corner, given, unknown_line, unknown_corner, letter, given_line="l"):
    """A picture of parallel lines l and m with a transversal, the given angle
    marked on given_line and the unknown on unknown_line. Returns (figure, answer)."""
    th = theta_for(given_corner, given)
    answer = corner_size(th, unknown_corner)
    return transversal_figure(th, [(given_line, given_corner, f"{given}°"), (unknown_line, unknown_corner, letter)]), answer


# q4: l top-right and m top-right are corresponding angles
Q4_FIG = transversal_figure(65, [("l", "tr", "a"), ("m", "tr", "b")])
assert corner_size(65, "tr") == corner_size(65, "tr") == 65
# q5: vertically opposite at l: top-left 138 -> bottom-right
Q5_FIG, Q5 = fig_for("tl", 138, "l", "br", "x")
assert Q5 == 138 and LINE - 138 == 42
# q6: corresponding: l top-right 72 -> m top-right
Q6_FIG, Q6 = fig_for("tr", 72, "m", "tr", "x")
assert Q6 == 72 and LINE - 72 == 108
# q7: alternate: l bottom-right 118 -> m top-left
Q7_FIG, Q7 = fig_for("br", 118, "m", "tl", "x")
assert Q7 == 118 and LINE - 118 == 62
# q8: co-interior: l bottom-left 112 -> m top-left
Q8_FIG, Q8 = fig_for("bl", 112, "m", "tl", "x")
assert Q8 == 68 and Q8 + 112 == LINE and 360 - 112 == 248
# q9: two steps: l top-right 64 -> m top-right 64 -> m bottom-right
Q9_FIG, Q9 = fig_for("tr", 64, "m", "br", "x")
assert Q9 == 116 and corner_size(theta_for("tr", 64), "tr") == 64 and 90 - 64 == 26
# q10: x and x + 30 on a straight line
Q10 = (LINE - 30) // 2
assert Q10 == 75 and Q10 + (Q10 + 30) == LINE and Q10 + 30 == 105 and (LINE - 30) % 2 == 0
Q10_FIG = transversal_figure(Q10, [("l", "tr", "x"), ("l", "br", "x+30")])
assert corner_size(Q10, "tr") == Q10 and corner_size(Q10, "br") == Q10 + 30
# q11 (find error): co-interior 70 and x -> x = 110, not 70
Q11_FIG, Q11 = fig_for("bl", 70, "m", "tl", "x")
assert Q11 == 110 and Q11 + 70 == LINE
# q12 (find error): corresponding angles 70 and 75 differ, so the lines are not parallel
assert 70 != 75
# perpendicular lines: 4 right angles; the 4 angles add to 360
Q3 = 360 // 90
assert Q3 == 4 and 4 * 90 == 360
# bank and review
QB1 = LINE
QB2_FIG, QB2 = fig_for("tl", 134, "m", "tl", "x")
assert QB2 == 134
QB3_FIG, QB3 = fig_for("bl", 47, "m", "tr", "x")
assert QB3 == 47
R1_FIG, R1 = fig_for("tl", 41, "l", "br", "x")
assert R1 == 41
R2_FIG, R2 = fig_for("bl", 100, "m", "tl", "x")
assert R2 == 80 and R2 + 100 == LINE

F_PERP = fig(120, 80,
    "Two straight lines p and q cross at one point. One goes across and one goes straight up and down. A small square in the corner where they meet marks a right angle.",
    "دو سیدھی لکیریں p اور q ایک نقطے پر ملتی ہیں۔ ایک افقی ہے اور ایک سیدھی اوپر نیچے۔ ملنے کی جگہ کونے میں چھوٹا مربع قائمہ زاویہ دکھاتا ہے۔",
    [seg((12, 40), (108, 40)), seg((60, 6), (60, 74)),
     poly([(60, 40), (67, 40), (67, 33), (60, 33)]), dot((60, 40)), label((104, 34), "p"), label((66, 10), "q")])

lesson = practice_lesson(
 "9.2", script="exercise_9_2.py",
 title=T("Exercise 9.2 practice: lines and transversals", "مشق 9.2 کی پریکٹس: لکیریں اور قاطع"),
 outcome="Tell parallel, intersecting and perpendicular lines apart, name the angles a transversal makes and find unknown angles.",
 prerequisites=[SY_LINES, AN_LINE, AN_PAIRS],
 misconceptions=[
   {"id": "parallel_perp_mix", "description": "Mixes up parallel lines (never meet) and perpendicular lines (meet at 90°)."},
   {"id": "cointerior_equal", "description": "Thinks co-interior angles are equal instead of adding to 180°."},
   {"id": "alternate_supplementary", "description": "Thinks alternate or corresponding angles add to 180° instead of being equal."},
   {"id": "stops_after_one_step", "description": "Stops after the first step of a two-step angle problem and gives that angle."},
   {"id": "opposite_supplementary", "description": "Gives 180° minus the angle for a vertically opposite angle."},
   {"id": "equal_without_parallel", "description": "Thinks the angle rules hold for any two lines, even when they are not parallel."},
   {"id": "half_not_found", "description": "Does not use the 180° of a straight line to set up and solve the unknown."},
 ],
 steps=[
   practice_intro("9.2",
     "Here you tell parallel, intersecting and perpendicular lines apart, name the angles a transversal makes, and find unknown angles.",
     "اس میں آپ متوازی، قطع کرنے والی اور عمودی لکیروں میں فرق کریں گے، قاطع سے بننے والے زاویوں کے نام بتائیں گے، اور نامعلوم زاویے نکالیں گے۔",
     "Exercise 9.2 is about lines and angles. Ready?", "مشق 9.2 لکیروں اور زاویوں کے بارے میں ہے۔ تیار؟"),
   ch("q1_parallel", ("Two lines on a page never meet, however far they are drawn. What are they called?", "کاغذ پر دو لکیریں کتنی ہی بڑھائی جائیں کبھی نہیں ملتیں۔ انہیں کیا کہتے ہیں؟"),
      ("Parallel lines", "متوازی لکیریں", "Yes! Parallel lines stay the same distance apart and never meet.", "جی ہاں! متوازی لکیریں ہمیشہ ایک جتنے فاصلے پر رہتی ہیں اور کبھی نہیں ملتیں۔"),
      [("Perpendicular lines", "عمودی لکیریں", "Perpendicular lines do meet, at a right angle.", "عمودی لکیریں ملتی ہیں، قائمہ زاویے پر۔", "parallel_perp_mix"),
       ("Intersecting lines", "قطع کرنے والی لکیریں", "Intersecting lines cross each other at a point.", "قطع کرنے والی لکیریں ایک نقطے پر ایک دوسرے کو کاٹتی ہیں۔", "parallel_perp_mix"),
       ("A transversal", "قاطع", "A transversal is a line that cuts across other lines.", "قاطع وہ لکیر ہے جو دوسری لکیروں کو کاٹتی ہے۔", "parallel_perp_mix")],
      2, qtype="recall"),
   ch("q2_perp", ("Two lines are perpendicular. At what angle do they meet?", "دو لکیریں عمودی ہیں۔ وہ کس زاویے پر ملتی ہیں؟"),
      ("90°", "90°", "Yes! Perpendicular lines meet at a right angle, 90°.", "جی ہاں! عمودی لکیریں قائمہ زاویے، 90° پر ملتی ہیں۔"),
      [("180°", "180°", "180° is a straight line, not a corner.", "180° سیدھی لکیر ہے، کونا نہیں۔", "parallel_perp_mix"),
       ("45°", "45°", "45° is half a right angle.", "45° قائمہ زاویے کا آدھا ہے۔", "parallel_perp_mix"),
       ("0°", "0°", "Lines that never meet are parallel. Perpendicular lines meet at 90°.", "جو لکیریں نہیں ملتیں وہ متوازی ہیں۔ عمودی لکیریں 90° پر ملتی ہیں۔", "parallel_perp_mix")],
      0, qtype="recall"),
   with_fig(nq("q3_right_angles", ("Lines p and q are perpendicular. How many right angles do they make at the point where they cross?", "لکیریں p اور q عمودی ہیں۔ جہاں وہ ملتی ہیں وہاں کتنے قائمہ زاویے بنتے ہیں؟"), Q3,
      ("Count the four corners round the crossing.", "ملنے کی جگہ کے گرد چاروں کونے گنیں۔"),
      ("Right! All 4 angles are 90° (4 × 90° = 360°).", "درست! چاروں زاویے 90° ہیں (4 × 90° = 360°)۔"), ("If one angle is 90°, the others are 90° too: 4.", "اگر ایک زاویہ 90° ہے تو باقی بھی 90° ہیں: 4"),
      [(1, "The square mark shows one, but each of the 4 corners is a right angle: 4.", "مربع کا نشان ایک دکھاتا ہے، مگر چاروں کونے قائمہ زاویے ہیں: 4", "parallel_perp_mix"),
       (2, "Count all four corners round the crossing: 4.", "ملنے کی جگہ کے گرد چاروں کونے گنیں: 4", "parallel_perp_mix")], qtype="recall"), F_PERP),
   with_fig(ch("q4_name", ("Parallel lines l and m are cut by a transversal. Angles a and b are in the same place at each crossing. What are they called?", "متوازی لکیریں l اور m ایک قاطع سے کٹتی ہیں۔ زاویے a اور b ہر ملاپ پر ایک ہی جگہ ہیں۔ انہیں کیا کہتے ہیں؟"),
      ("Corresponding angles", "متناظرہ زاویے", "Yes! Same position at the two crossings: corresponding angles.", "جی ہاں! دونوں ملاپ پر ایک ہی جگہ: متناظرہ زاویے۔"),
      [("Alternate angles", "متبادلہ زاویے", "Alternate angles are on opposite sides of the transversal, between the lines.", "متبادلہ زاویے قاطع کے مخالف رخوں پر، لکیروں کے درمیان ہوتے ہیں۔", "alternate_supplementary"),
       ("Co-interior angles", "ہم اندرونی زاویے", "Co-interior angles are between the lines, on the same side.", "ہم اندرونی زاویے لکیروں کے درمیان، ایک ہی رخ پر ہوتے ہیں۔", "cointerior_equal"),
       ("Vertically opposite angles", "راسی زاویے", "Vertically opposite angles are across one crossing, not two.", "راسی زاویے ایک ہی ملاپ پر آمنے سامنے ہوتے ہیں، دو پر نہیں۔", "opposite_supplementary")],
      3, qtype="recall"), Q4_FIG),
   with_fig(nq("q5_opposite", ("Two lines cross. One of the angles is 138°. What is the angle opposite to it (x)?", "دو لکیریں ایک دوسرے کو کاٹتی ہیں۔ ایک زاویہ 138° ہے۔ اس کے سامنے والا زاویہ (x) کتنا ہے؟"), Q5,
      ("Vertically opposite angles are equal.", "راسی زاویے برابر ہوتے ہیں۔"),
      ("Right! Opposite angles are equal: x = 138°.", "درست! سامنے والے زاویے برابر ہیں: x = 138°"), ("They are vertically opposite, so x = 138°.", "یہ راسی زاویے ہیں، تو x = 138°"),
      [(42, "42° is the angle next to it (180° − 138°). The opposite angle is equal: 138°.", "42° اس کے ساتھ والا زاویہ ہے (180° − 138°)۔ سامنے والا برابر ہے: 138°", "opposite_supplementary"),
       (222, "That is 360° − 138°. The opposite angle is equal: 138°.", "یہ 360° − 138° ہے۔ سامنے والا زاویہ برابر ہے: 138°", "opposite_supplementary")], qtype="recall"), Q5_FIG),
   {"id": "s_idea", "type": "explain",
    "character": say("thinking", "Parallel lines make equal angles, or angles that add to 180°.", "متوازی لکیریں برابر زاویے بناتی ہیں، یا ایسے زاویے جن کا مجموعہ 180° ہوتا ہے۔"),
    "text": T("When a transversal cuts two PARALLEL lines: corresponding angles are equal; alternate angles are equal; co-interior angles add up to 180°. Vertically opposite angles are always equal, even for lines that are not parallel. Angles side by side on a straight line add up to 180°. Two lines that cross at 90° are perpendicular; all four angles there are 90°.",
              "جب قاطع دو متوازی لکیروں کو کاٹے: متناظرہ زاویے برابر ہوتے ہیں؛ متبادلہ زاویے برابر ہوتے ہیں؛ ہم اندرونی زاویوں کا مجموعہ 180° ہوتا ہے۔ راسی زاویے ہمیشہ برابر ہوتے ہیں، چاہے لکیریں متوازی نہ ہوں۔ سیدھی لکیر پر ساتھ ساتھ زاویوں کا مجموعہ 180° ہوتا ہے۔ جو دو لکیریں 90° پر ملیں وہ عمودی ہیں؛ وہاں چاروں زاویے 90° ہوتے ہیں۔")},
   with_fig(nq("q6_corresponding", ("Lines l and m are parallel. The angle marked 72° is on line l; angle x is its corresponding angle on line m. Find x.", "لکیریں l اور m متوازی ہیں۔ 72° والا زاویہ لکیر l پر ہے؛ زاویہ x لکیر m پر اس کا متناظرہ زاویہ ہے۔ x نکالیں۔"), Q6,
      ("Corresponding angles between parallel lines are equal.", "متوازی لکیروں کے درمیان متناظرہ زاویے برابر ہوتے ہیں۔"),
      ("Right! x = 72°.", "درست! x = 72°"), ("Same position at the two crossings, so equal: 72°.", "دونوں ملاپ پر ایک ہی جگہ، تو برابر: 72°"),
      [(108, "108° is 180° − 72°. Corresponding angles are equal, not supplementary: 72°.", "108° ہے 180° − 72°۔ متناظرہ زاویے برابر ہوتے ہیں، تکمیلی نہیں: 72°", "alternate_supplementary")]), Q6_FIG),
   with_fig(nq("q7_alternate", ("Lines l and m are parallel. The angle marked 118° and angle x are alternate angles. Find x.", "لکیریں l اور m متوازی ہیں۔ 118° والا زاویہ اور زاویہ x متبادلہ زاویے ہیں۔ x نکالیں۔"), Q7,
      ("Alternate angles between parallel lines are equal.", "متوازی لکیروں کے درمیان متبادلہ زاویے برابر ہوتے ہیں۔"),
      ("Right! x = 118°.", "درست! x = 118°"), ("They form a Z shape, so they are equal: 118°.", "یہ Z کی شکل بناتے ہیں، تو برابر ہیں: 118°"),
      [(62, "62° is 180° − 118°. Alternate angles are equal: 118°.", "62° ہے 180° − 118°۔ متبادلہ زاویے برابر ہوتے ہیں: 118°", "alternate_supplementary")]), Q7_FIG),
   with_fig(nq("q8_cointerior", ("Lines l and m are parallel. The angle marked 112° and angle x are co-interior angles. Find x.", "لکیریں l اور m متوازی ہیں۔ 112° والا زاویہ اور زاویہ x ہم اندرونی زاویے ہیں۔ x نکالیں۔"), Q8,
      ("Co-interior angles between parallel lines add up to 180°.", "متوازی لکیروں کے درمیان ہم اندرونی زاویوں کا مجموعہ 180° ہوتا ہے۔"),
      ("Right! x = 180° − 112° = 68°.", "درست! x = 180° − 112° = 68°"), ("112° + x = 180°, so x = 68°.", "112° + x = 180°، تو x = 68°"),
      [(112, "That makes them equal. Co-interior angles add up to 180°: 68°.", "یہ انہیں برابر بناتا ہے۔ ہم اندرونی زاویوں کا مجموعہ 180° ہے: 68°", "cointerior_equal"),
       (248, "That is 360° − 112°. Co-interior angles add up to 180°: 68°.", "یہ 360° − 112° ہے۔ ہم اندرونی زاویوں کا مجموعہ 180° ہے: 68°", "cointerior_equal")]), Q8_FIG),
   with_fig(nq("q9_two_steps", ("Lines l and m are parallel. The angle on l marked 64° has a corresponding angle on m. Angle x on m is next to that corresponding angle, on a straight line. Find x.", "لکیریں l اور m متوازی ہیں۔ لکیر l پر 64° والے زاویے کا متناظرہ زاویہ m پر ہے۔ m پر زاویہ x اس متناظرہ زاویے کے ساتھ سیدھی لکیر پر ہے۔ x نکالیں۔"), Q9,
      ("First the corresponding angle (64°). Then the straight line: 180° − 64°.", "پہلے متناظرہ زاویہ (64°)۔ پھر سیدھی لکیر: 180° − 64°"),
      ("Right! The corresponding angle is 64°, so x = 180° − 64° = 116°.", "درست! متناظرہ زاویہ 64° ہے، تو x = 180° − 64° = 116°"), ("Step 1: 64°. Step 2: 180° − 64° = 116°.", "مرحلہ 1: 64°۔ مرحلہ 2: 180° − 64° = 116°"),
      [(64, "That is only the first step. x is next to it on a straight line: 116°.", "یہ صرف پہلا مرحلہ ہے۔ x اس کے ساتھ سیدھی لکیر پر ہے: 116°", "stops_after_one_step"),
       (26, "26° is 90° − 64°. Angles on a straight line add up to 180°: 116°.", "26° ہے 90° − 64°۔ سیدھی لکیر پر زاویوں کا مجموعہ 180° ہوتا ہے: 116°", "half_not_found")]), Q9_FIG),
   with_fig(nq("q10_equation", ("The two angles x and (x + 30) in the picture are side by side on a straight line. Find x.", "تصویر میں دو زاویے x اور (x + 30) سیدھی لکیر پر ساتھ ساتھ ہیں۔ x نکالیں۔"), Q10,
      ("x + (x + 30) = 180. So 2x + 30 = 180.", "x + (x + 30) = 180۔ تو 2x + 30 = 180"),
      ("Right! 2x = 150, so x = 75°. Check: 75° + 105° = 180°.", "درست! 2x = 150، تو x = 75°۔ جانچ: 75° + 105° = 180°"), ("2x = 180 − 30 = 150, and 150 ÷ 2 = 75.", "2x = 180 − 30 = 150، اور 150 ÷ 2 = 75"),
      [(105, "105° is the other angle, x + 30. The question asks for x: 75°.", "105° دوسرا زاویہ x + 30 ہے۔ سوال x پوچھتا ہے: 75°", "half_not_found"),
       (150, "150 is 2x. Divide by 2: x = 75°.", "150، 2x ہے۔ 2 سے تقسیم کریں: x = 75°", "half_not_found")]), Q10_FIG),
   with_fig(ch("q11_find_error", ("Sara says: \"Lines l and m are parallel. The angles 70° and x are co-interior, so x = 70°.\" What went wrong?", "سارہ کہتی ہے: \"لکیریں l اور m متوازی ہیں۔ 70° اور x ہم اندرونی زاویے ہیں، تو x = 70°۔\" کیا غلطی ہوئی؟"),
      ("Co-interior angles add up to 180°, so x = 180° − 70° = 110°.", "ہم اندرونی زاویوں کا مجموعہ 180° ہوتا ہے، تو x = 180° − 70° = 110°۔", "Yes! Co-interior angles are not equal; they are supplementary.", "جی ہاں! ہم اندرونی زاویے برابر نہیں ہوتے؛ ان کا مجموعہ 180° ہوتا ہے۔"),
      [("Nothing. Co-interior angles are equal.", "کوئی غلطی نہیں۔ ہم اندرونی زاویے برابر ہوتے ہیں۔", "That is the rule for alternate and corresponding angles, not co-interior.", "یہ متبادلہ اور متناظرہ زاویوں کا اصول ہے، ہم اندرونی کا نہیں۔", "cointerior_equal"),
       ("x should be 20°, because 90° − 70° = 20°.", "x کو 20° ہونا چاہیے، کیونکہ 90° − 70° = 20°۔", "The total is 180°, not 90°.", "مجموعہ 180° ہے، 90° نہیں۔", "half_not_found")],
      0, qtype="find_error"), Q11_FIG),
   ch("q12_find_error_parallel", ("Bilal draws a transversal across two lines and measures a pair of corresponding angles: 70° and 75°. He says the lines are parallel. What went wrong?", "بلال دو لکیروں پر ایک قاطع کھینچتا ہے اور متناظرہ زاویوں کا ایک جوڑا ناپتا ہے: 70° اور 75°۔ وہ کہتا ہے لکیریں متوازی ہیں۔ کیا غلطی ہوئی؟"),
      ("For parallel lines, corresponding angles must be equal. 70° and 75° are not equal, so the lines are not parallel.", "متوازی لکیروں کے متناظرہ زاویے برابر ہونے چاہییں۔ 70° اور 75° برابر نہیں، تو لکیریں متوازی نہیں۔", "Yes! Equal corresponding angles show parallel lines; unequal ones show they are not.", "جی ہاں! برابر متناظرہ زاویے متوازی لکیریں بتاتے ہیں؛ غیر برابر بتاتے ہیں کہ نہیں ہیں۔"),
      [("Nothing. The angles are close enough, so the lines are parallel.", "کوئی غلطی نہیں۔ زاویے کافی قریب ہیں، تو لکیریں متوازی ہیں۔", "5° is a real difference. Parallel lines need exactly equal angles.", "5° کا فرق اصلی فرق ہے۔ متوازی لکیروں کے زاویے بالکل برابر ہوتے ہیں۔", "equal_without_parallel"),
       ("The angles should add up to 180°, so 70° + 75° = 145° is wrong.", "زاویوں کا مجموعہ 180° ہونا چاہیے، تو 70° + 75° = 145° غلط ہے۔", "Corresponding angles are equal, not supplementary.", "متناظرہ زاویے برابر ہوتے ہیں، تکمیلی نہیں۔", "alternate_supplementary")],
      1, qtype="find_error"),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! You can find angles made by a transversal.", "شاباش! آپ قاطع سے بننے والے زاویے نکال سکتے ہیں۔"),
    "text": T("Parallel lines never meet. Perpendicular lines meet at 90°. A transversal cuts across other lines. Between PARALLEL lines: corresponding angles are equal, alternate angles are equal, co-interior angles add up to 180°. Vertically opposite angles are always equal. Angles on a straight line add up to 180°. For an unknown with x, write the equation and solve it.",
              "متوازی لکیریں کبھی نہیں ملتیں۔ عمودی لکیریں 90° پر ملتی ہیں۔ قاطع دوسری لکیروں کو کاٹتا ہے۔ متوازی لکیروں کے درمیان: متناظرہ زاویے برابر، متبادلہ زاویے برابر، ہم اندرونی زاویوں کا مجموعہ 180°۔ راسی زاویے ہمیشہ برابر ہوتے ہیں۔ سیدھی لکیر پر زاویوں کا مجموعہ 180° ہوتا ہے۔ x والے نامعلوم کے لیے مساوات لکھیں اور حل کریں۔"),
    "points": [T("Equal: corresponding, alternate, vertically opposite.", "برابر: متناظرہ، متبادلہ، راسی۔"),
               T("Add to 180°: co-interior, and angles on a straight line.", "مجموعہ 180°: ہم اندرونی، اور سیدھی لکیر پر زاویے۔")]},
 ],
 bank=[
   {"id": "qb_cointerior_total", "type": "recall", "step": nq("qb_cointerior_total", ("Co-interior angles between parallel lines add up to how many degrees?", "متوازی لکیروں کے درمیان ہم اندرونی زاویوں کا مجموعہ کتنے ڈگری ہوتا ہے؟"), QB1,
      ("They fill a straight line.", "وہ سیدھی لکیر بھرتے ہیں۔"),
      ("Right! 180°.", "درست! 180°"), ("A straight line is 180°.", "سیدھی لکیر 180° ہوتی ہے۔"),
      [(90, "90° is a right angle. Co-interior angles add up to 180°.", "90° قائمہ زاویہ ہے۔ ہم اندرونی زاویوں کا مجموعہ 180° ہے۔", "half_not_found"),
       (360, "360° is a full turn. Co-interior angles add up to 180°.", "360° پورا چکر ہے۔ ہم اندرونی زاویوں کا مجموعہ 180° ہے۔", "half_not_found")], qtype=None)},
   {"id": "qb_corresponding", "type": "apply", "step": with_fig(nq("qb_corresponding", ("Lines l and m are parallel. The angle on l is 134°. Find its corresponding angle x on m.", "لکیریں l اور m متوازی ہیں۔ l پر زاویہ 134° ہے۔ m پر اس کا متناظرہ زاویہ x نکالیں۔"), QB2,
      ("Corresponding angles are equal.", "متناظرہ زاویے برابر ہوتے ہیں۔"),
      ("Right! x = 134°.", "درست! x = 134°"), ("Same position, so equal: 134°.", "ایک ہی جگہ، تو برابر: 134°"),
      [(46, "46° is 180° − 134°. Corresponding angles are equal: 134°.", "46° ہے 180° − 134°۔ متناظرہ زاویے برابر ہیں: 134°", "alternate_supplementary")], qtype=None), QB2_FIG)},
   {"id": "qb_alternate", "type": "apply", "step": with_fig(nq("qb_alternate", ("Lines l and m are parallel. The angle on l is 47°. Find its alternate angle x on m.", "لکیریں l اور m متوازی ہیں۔ l پر زاویہ 47° ہے۔ m پر اس کا متبادلہ زاویہ x نکالیں۔"), QB3,
      ("Alternate angles are equal.", "متبادلہ زاویے برابر ہوتے ہیں۔"),
      ("Right! x = 47°.", "درست! x = 47°"), ("A Z shape: the two angles are equal: 47°.", "Z کی شکل: دونوں زاویے برابر ہیں: 47°"),
      [(133, "133° is 180° − 47°. Alternate angles are equal: 47°.", "133° ہے 180° − 47°۔ متبادلہ زاویے برابر ہیں: 47°", "alternate_supplementary")], qtype=None), QB3_FIG)},
   {"id": "qb_find_error", "type": "find_error", "step": ch("qb_find_error", ("Omar says vertically opposite angles add up to 180°. What went wrong?", "عمر کہتا ہے راسی زاویوں کا مجموعہ 180° ہوتا ہے۔ کیا غلطی ہوئی؟"),
      ("Vertically opposite angles are equal. It is the angles side by side on a straight line that add up to 180°.", "راسی زاویے برابر ہوتے ہیں۔ سیدھی لکیر پر ساتھ ساتھ زاویوں کا مجموعہ 180° ہوتا ہے۔", "Yes! Opposite means equal.", "جی ہاں! سامنے والے برابر ہوتے ہیں۔"),
      [("Nothing. Opposite angles add up to 180°.", "کوئی غلطی نہیں۔ سامنے والے زاویوں کا مجموعہ 180° ہوتا ہے۔", "Opposite angles are equal.", "سامنے والے زاویے برابر ہوتے ہیں۔", "opposite_supplementary"),
       ("They add up to 90°.", "ان کا مجموعہ 90° ہوتا ہے۔", "They are equal, not a total of 90°.", "وہ برابر ہوتے ہیں، ان کا مجموعہ 90° نہیں۔", "opposite_supplementary")],
      0, qtype=None)},
 ],
 review=[
   {"id": "r_opposite", "type": "apply", "step": with_fig(nq("r_opposite", ("Two lines cross. One angle is 41°. Find the angle x opposite to it.", "دو لکیریں ایک دوسرے کو کاٹتی ہیں۔ ایک زاویہ 41° ہے۔ اس کے سامنے والا زاویہ x نکالیں۔"), R1,
      ("Vertically opposite angles are equal.", "راسی زاویے برابر ہوتے ہیں۔"),
      ("Right! x = 41°.", "درست! x = 41°"), ("Opposite angles are equal: 41°.", "سامنے والے زاویے برابر ہیں: 41°"),
      [(139, "139° is 180° − 41°. The opposite angle is equal: 41°.", "139° ہے 180° − 41°۔ سامنے والا زاویہ برابر ہے: 41°", "opposite_supplementary")], qtype=None), R1_FIG)},
   {"id": "r_cointerior", "type": "apply", "step": with_fig(nq("r_cointerior", ("Lines l and m are parallel. Co-interior angles are 100° and x. Find x.", "لکیریں l اور m متوازی ہیں۔ ہم اندرونی زاویے 100° اور x ہیں۔ x نکالیں۔"), R2,
      ("100° + x = 180°.", "100° + x = 180°"),
      ("Right! x = 80°.", "درست! x = 80°"), ("180° − 100° = 80°.", "180° − 100° = 80°"),
      [(100, "That makes them equal. Co-interior angles add up to 180°: 80°.", "یہ انہیں برابر بناتا ہے۔ ہم اندرونی زاویوں کا مجموعہ 180° ہے: 80°", "cointerior_equal")], qtype=None), R2_FIG)},
 ],
 glossary=[T("Parallel lines", "متوازی لکیریں"), T("Perpendicular lines", "عمودی لکیریں"), T("Intersecting lines", "قطع کرنے والی لکیریں"),
           T("Transversal", "قاطع"), T("Corresponding angles", "متناظرہ زاویے"), T("Alternate angles", "متبادلہ زاویے"),
           T("Co-interior angles", "ہم اندرونی زاویے"), T("Vertically opposite angles", "راسی زاویے")],
 flashcards=[
   {"id": "f_rules", "front": T("Which angles are equal between parallel lines?", "متوازی لکیروں کے درمیان کون سے زاویے برابر ہوتے ہیں؟"),
    "back": T("Corresponding and alternate angles (and vertically opposite angles always).", "متناظرہ اور متبادلہ زاویے (اور راسی زاویے ہمیشہ)۔")},
   {"id": "f_cointerior", "front": T("What do co-interior angles add up to?", "ہم اندرونی زاویوں کا مجموعہ کتنا ہوتا ہے؟"),
    "back": T("180°, when the lines are parallel.", "180°، جب لکیریں متوازی ہوں۔")},
 ],
 home_task={"id": "h_lines", "text": T(
   "Look for parallel lines (rails, window bars) and perpendicular lines (corners of a door) at home. Draw two parallel lines and a transversal in your notebook. Measure one angle with a protractor and work out the other seven. Then measure them to check.",
   "گھر میں متوازی لکیریں (پٹریاں، کھڑکی کی سلاخیں) اور عمودی لکیریں (دروازے کے کونے) ڈھونڈیں۔ اپنی کاپی میں دو متوازی لکیریں اور ایک قاطع کھینچیں۔ ایک زاویہ چاند کی مدد سے ناپیں اور باقی سات حساب سے نکالیں۔ پھر ناپ کر جانچیں۔")},
 notes=["Covers naming parallel, intersecting and perpendicular lines (q1 to q3), naming the pairs of angles a transversal makes (q4), finding vertically opposite, corresponding, alternate and co-interior angles (q5 to q8), a two-step problem (q9), an equation from a straight line (q10) and two find-the-error questions (q11, q12).",
        "Each wrong answer is a real mistake: co-interior angles taken as equal, equal angles taken as adding to 180°, 180° minus the angle for a vertically opposite angle, stopping after the first step, and using the angle rules for lines that are not parallel.",
        "Urdu terms to check: متوازی لکیریں, عمودی لکیریں, قطع کرنے والی لکیریں, قاطع, متناظرہ, متبادلہ, ہم اندرونی, راسی زاویے, all as in the existing lesson on parallel lines and the transversal. No new terms."],
 minutes=18,
)

write(lesson)
