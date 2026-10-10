"""Practice set for Exercise 11.3 of the book: reading pie charts given in
percentages, working out quantities, and finding sector angles (value / total x 360).
The app cannot check a drawing, so the questions are about reading and working out.
The questions are new; only the kinds of question follow the book."""
from fractions import Fraction as F

from common import (T, say, nq, ch, practice_lesson, practice_intro, write, EX_SKILL,
                    DH_PIE_CHARTS, DH_TABLES)
from figs import pie_chart, with_fig

SKILL = EX_SKILL["11.3"]
FULL = 360


def angle(value, total):
    """Sector angle = value / total x 360, which must be a whole number here."""
    a = F(value, total) * FULL
    assert a.denominator == 1, (value, total)
    return int(a)


def percent_of(p, total):
    v = F(p, 100) * total
    assert v.denominator == 1
    return int(v)


# pie chart 1: how 200 pupils come to school, in percent
TOTAL = 200
SLICES = [("W", 40), ("B", 25), ("C", 20), ("V", 15)]      # walk, bus, cycle, van
assert sum(p for _, p in SLICES) == 100
ANG = [angle(p, 100) for _, p in SLICES]
assert ANG == [144, 90, 72, 54] and sum(ANG) == FULL
PIE1 = pie_chart([(a, n, f"{p}%") for a, (n, p) in zip(ANG, SLICES)],
    "A pie chart of how 200 pupils come to school. W (walk) 40 percent, B (bus) 25 percent, C (cycle) 20 percent and V (van) 15 percent.",
    "200 طلبہ کے سکول آنے کے طریقوں کا دائری نقشہ۔ W (پیدل) 40 فیصد، B (بس) 25 فیصد، C (سائیکل) 20 فیصد اور V (وین) 15 فیصد۔")
Q3 = percent_of(40, TOTAL)
assert Q3 == 80 and 40 != 80 and percent_of(20, TOTAL) == 40
Q4 = 25 + 20
assert Q4 == 45 and 100 - Q4 == 55
Q5_KNOWN = [35, 30, 10]
Q5 = 100 - sum(Q5_KNOWN)
assert Q5 == 25 and sum(Q5_KNOWN) == 75
Q5_ANG = [angle(p, 100) for p in Q5_KNOWN + [Q5]]
assert Q5_ANG == [126, 108, 36, 90] and sum(Q5_ANG) == FULL
PIE5 = pie_chart([(a, n, f"{p}%") for a, n, p in zip(Q5_ANG, "RGBY", Q5_KNOWN + ["?"])],
    "A pie chart with four sectors R, G, B and Y. R is 35 percent, G is 30 percent and B is 10 percent. The sector Y is marked with a question mark.",
    "چار ٹکڑوں R، G، B اور Y کا دائری نقشہ۔ R کے 35 فیصد، G کے 30 فیصد اور B کے 10 فیصد ہیں۔ ٹکڑے Y پر سوالیہ نشان ہے۔")
# angles from numbers
Q6_V, Q6_T = 30, 120
Q6 = angle(Q6_V, Q6_T)
assert Q6 == 90 and F(Q6_V, Q6_T) * 100 == 25 and Q6_V != Q6
Q7_V, Q7_T = 15, 90
Q7 = angle(Q7_V, Q7_T)
assert Q7 == 60 and Q7_V != Q7
# percentage from an angle
Q8_A = 72
Q8 = F(Q8_A, FULL) * 100
assert Q8 == 20 and Q8_A != Q8
# quantity from an angle
Q9_A, Q9_T = 90, 240
Q9 = F(Q9_A, FULL) * Q9_T
assert Q9 == 60 and Q9_T // 10 == 24
Q9 = int(Q9)
# which angles can make one pie chart
OKSET = [120, 100, 80, 60]
assert sum(OKSET) == FULL
BAD1, BAD2, BAD3 = [120, 100, 80, 50], [150, 100, 80, 40], [100, 100, 100, 100]
assert sum(BAD1) == 350 and sum(BAD2) == 370 and sum(BAD3) == 400
# find the error: 20 out of 80 pupils
E_V, E_T = 20, 80
E_RIGHT = angle(E_V, E_T)
assert E_RIGHT == 90 and F(E_V, E_T) * 100 == 25
# bank / review
QB_V, QB_T = 10, 40
QB = angle(QB_V, QB_T)
assert QB == 90
QB_HALF = angle(1, 2)
assert QB_HALF == 180 and angle(1, 4) == 90
R1_V, R1_T = 25, 100
R1 = angle(R1_V, R1_T)
assert R1 == 90
R2_P, R2_T = 30, 60
R2 = percent_of(R2_P, R2_T)
assert R2 == 18

lesson = practice_lesson(
 "11.3", script="exercise_11_3.py",
 title=T("Exercise 11.3 practice: pie charts", "مشق 11.3 کی پریکٹس: دائری نقشے"),
 outcome="Read a pie chart given in percentages, work out quantities from it, and find a sector angle as value / total x 360.",
 prerequisites=[DH_PIE_CHARTS, DH_TABLES],
 misconceptions=[
   {"id": "pie_total_wrong", "description": "Thinks the whole pie is 100 degrees, or that the sectors add up to something other than 360 degrees (or 100 percent)."},
   {"id": "percent_as_number", "description": "Gives the percentage as the number of people, or the angle as the number of people."},
   {"id": "angle_times_100", "description": "Finds the sector angle as value / total x 100 instead of x 360."},
   {"id": "angle_is_value", "description": "Gives the value itself as the angle, without dividing by the total and multiplying by 360."},
   {"id": "missing_not_taken", "description": "Does not take the known sectors away from the whole to find the missing one."},
   {"id": "pie_parts_not_added", "description": "Gives only one sector when two sectors are asked for together."},
 ],
 steps=[
   practice_intro("11.3",
     "Here you practise reading a pie chart, finding quantities from percentages and angles, and working out sector angles. You only read and calculate; the drawing is for your notebook.",
     "اس میں آپ دائری نقشہ پڑھنا، فیصد اور زاویوں سے مقداریں نکالنا اور ٹکڑوں کے زاویے نکالنا دہرائیں گے۔ آپ صرف پڑھیں گے اور حساب کریں گے؛ بنانا کاپی میں کریں۔",
     "Exercise 11.3 is about pie charts. Ready?", "مشق 11.3 دائری نقشوں کے بارے میں ہے۔ تیار؟"),
   ch("q1_whole", ("All the sectors of a pie chart together make a whole circle. How many degrees is that?", "دائری نقشے کے سب ٹکڑے مل کر پورا دائرہ بناتے ہیں۔ یہ کتنے درجے کا ہے؟"),
      ("360°", "360°", "Yes! A full turn is 360°, and the percentages add up to 100.", "جی ہاں! پورا چکر 360° ہے، اور فیصد کا مجموعہ 100 ہے۔"),
      [("100°", "100°", "100 is the total of the percentages. The circle is 360°.", "100 فیصد کا مجموعہ ہے۔ دائرہ 360° کا ہے۔", "pie_total_wrong"),
       ("180°", "180°", "180° is only half a circle, a straight line.", "180° صرف آدھا دائرہ ہے، سیدھی لکیر۔", "pie_total_wrong")],
      0, qtype="recall"),
   {"id": "s_idea", "type": "explain",
    "character": say("thinking", "A sector is a share of 360°. Divide by the total, then multiply by 360.", "ٹکڑا 360° کا ایک حصہ ہے۔ کل سے تقسیم کریں، پھر 360 سے ضرب دیں۔"),
    "text": T("The sectors of a pie chart make 100% and 360°. To find a quantity from a percentage: percentage ÷ 100 × total. To find a sector angle: value ÷ total × 360°. To find a percentage from an angle: angle ÷ 360 × 100. A missing sector is what is left of 100% (or 360°) after the known sectors are taken away.",
              "دائری نقشے کے ٹکڑے مل کر 100 فیصد اور 360° بناتے ہیں۔ فیصد سے مقدار نکالنے کے لیے: فیصد ÷ 100 × کل۔ ٹکڑے کا زاویہ نکالنے کے لیے: قیمت ÷ کل × 360°۔ زاویے سے فیصد نکالنے کے لیے: زاویہ ÷ 360 × 100۔ غائب ٹکڑا وہ ہے جو معلوم ٹکڑے نکالنے کے بعد 100 فیصد (یا 360°) میں سے بچے۔")},
   with_fig(ch("q2_largest", ("The pie chart shows how 200 pupils come to school: W is walk, B is bus, C is cycle and V is van. Which way is the most common?", "دائری نقشہ دکھاتا ہے کہ 200 طلبہ سکول کیسے آتے ہیں: W پیدل، B بس، C سائیکل اور V وین۔ کون سا طریقہ سب سے زیادہ ہے؟"),
      ("walking (W, 40%)", "پیدل (W، 40٪)", "Yes! The biggest sector is the biggest share.", "جی ہاں! سب سے بڑا ٹکڑا سب سے بڑا حصہ ہے۔"),
      [("bus (B, 25%)", "بس (B، 25٪)", "The bus is 25%, less than 40%.", "بس 25٪ ہے، 40٪ سے کم۔", "percent_as_number"),
       ("cycle (C, 20%)", "سائیکل (C، 20٪)", "Cycle is 20%, less than 40%.", "سائیکل 20٪ ہے، 40٪ سے کم۔", "percent_as_number"),
       ("van (V, 15%)", "وین (V، 15٪)", "The van is the smallest sector.", "وین سب سے چھوٹا ٹکڑا ہے۔", "percent_as_number")],
      0, qtype="recall"), PIE1),
   with_fig(nq("q3_quantity", ("How many of the 200 pupils walk to school?", "200 میں سے کتنے طلبہ پیدل سکول آتے ہیں؟"), Q3,
      ("40% of 200: 40 ÷ 100 × 200.", "200 کا 40٪: 40 ÷ 100 × 200"),
      ("Right! 40 ÷ 100 × 200 = 80 pupils.", "درست! 40 ÷ 100 × 200 = 80 طلبہ"), ("10% of 200 is 20, so 40% is 4 × 20 = 80.", "200 کا 10٪ 20 ہے، تو 40٪ یعنی 4 × 20 = 80"),
      [(40, "40 is the percentage, not the number of pupils. Take 40% of 200: 80.", "40 فیصد ہے، طلبہ کی تعداد نہیں۔ 200 کا 40٪ لیں: 80", "percent_as_number"),
       (144, "144° is the sector's angle. The number of pupils is 40% of 200: 80.", "144° ٹکڑے کا زاویہ ہے۔ طلبہ کی تعداد 200 کا 40٪ ہے: 80", "percent_as_number")]), PIE1),
   with_fig(nq("q4_two", ("What percentage of the pupils come by bus (B) or by cycle (C) together?", "کتنے فیصد طلبہ بس (B) یا سائیکل (C) سے آتے ہیں، دونوں ملا کر؟"), Q4,
      ("Add the two sectors.", "دونوں ٹکڑے جمع کریں۔"),
      ("Right! 25% + 20% = 45%.", "درست! 25٪ + 20٪ = 45٪"), ("25 + 20 = 45.", "25 + 20 = 45"),
      [(25, "25 is only the bus. Add the cycle too: 45.", "25 صرف بس ہے۔ سائیکل بھی جمع کریں: 45", "pie_parts_not_added"),
       (55, "55 is what is left over (walk and van). Bus and cycle together: 45.", "55 بچا ہوا ہے (پیدل اور وین)۔ بس اور سائیکل ملا کر: 45", "pie_parts_not_added")]), PIE1),
   with_fig(nq("q5_missing", ("The pie chart has four sectors R, G, B and Y. R is 35%, G is 30% and B is 10%. What percentage is the sector Y?", "دائری نقشے میں چار ٹکڑے R، G، B اور Y ہیں۔ R کا 35٪، G کا 30٪ اور B کا 10٪ ہے۔ ٹکڑا Y کتنے فیصد ہے؟"), Q5,
      ("The sectors make 100%. Take the known ones away.", "ٹکڑے مل کر 100٪ بنتے ہیں۔ معلوم ٹکڑے گھٹائیں۔"),
      ("Right! 35 + 30 + 10 = 75, and 100 − 75 = 25%.", "درست! 35 + 30 + 10 = 75، اور 100 − 75 = 25٪"), ("100 − 35 − 30 − 10 = 25.", "100 − 35 − 30 − 10 = 25"),
      [(75, "75 is the three known sectors added. Y is what is left of 100: 25.", "75 تین معلوم ٹکڑوں کا مجموعہ ہے۔ Y وہ ہے جو 100 میں سے بچے: 25", "missing_not_taken"),
       (65, "65 takes away only R from 100. Take away all three: 25.", "65 میں 100 میں سے صرف R گھٹایا گیا ہے۔ تینوں گھٹائیں: 25", "missing_not_taken")]), PIE5),
   nq("q6_angle", (f"In a class of {Q6_T} pupils, {Q6_V} like cricket best. What is the angle of the cricket sector in a pie chart, in degrees?", f"{Q6_T} طلبہ کی جماعت میں {Q6_V} کو کرکٹ سب سے زیادہ پسند ہے۔ دائری نقشے میں کرکٹ کے ٹکڑے کا زاویہ درجوں میں کتنا ہے؟"), Q6,
      ("Angle = value ÷ total × 360.", "زاویہ = قیمت ÷ کل × 360"),
      ("Right! 30 ÷ 120 × 360 = 90°.", "درست! 30 ÷ 120 × 360 = 90°"), ("30 ÷ 120 = 1/4, and 1/4 of 360 is 90.", "30 ÷ 120 = 1/4، اور 360 کا 1/4 یعنی 90"),
      [(25, "25 is the percentage (30 ÷ 120 × 100). For the angle multiply by 360: 90.", "25 فیصد ہے (30 ÷ 120 × 100)۔ زاویے کے لیے 360 سے ضرب دیں: 90", "angle_times_100"),
       (30, "30 is the number of pupils. The angle is 30 ÷ 120 × 360 = 90.", "30 طلبہ کی تعداد ہے۔ زاویہ 30 ÷ 120 × 360 = 90 ہے۔", "angle_is_value")]),
   nq("q7_angle2", (f"A jar has {Q7_T} sweets, and {Q7_V} of them are mints. What is the angle of the mint sector in a pie chart, in degrees?", f"ایک مرتبان میں {Q7_T} ٹافیاں ہیں، اور ان میں سے {Q7_V} پودینے کی ہیں۔ دائری نقشے میں پودینے کے ٹکڑے کا زاویہ درجوں میں کتنا ہے؟"), Q7,
      ("15 ÷ 90 × 360.", "15 ÷ 90 × 360"),
      ("Right! 15 ÷ 90 = 1/6, and 360 ÷ 6 = 60°.", "درست! 15 ÷ 90 = 1/6، اور 360 ÷ 6 = 60°"), ("15 ÷ 90 × 360 = 60.", "15 ÷ 90 × 360 = 60"),
      [(15, "15 is the number of mints. The angle is 15 ÷ 90 × 360 = 60.", "15 پودینے کی ٹافیوں کی تعداد ہے۔ زاویہ 15 ÷ 90 × 360 = 60 ہے۔", "angle_is_value"),
       (17, "17 is about 15 ÷ 90 × 100. Multiply by 360 instead: 60.", "17 تقریباً 15 ÷ 90 × 100 ہے۔ اس کی جگہ 360 سے ضرب دیں: 60", "angle_times_100")]),
   nq("q8_percent", (f"A sector of a pie chart has an angle of {Q8_A}°. What percentage of the whole is it?", f"دائری نقشے کے ایک ٹکڑے کا زاویہ {Q8_A}° ہے۔ یہ پورے کا کتنے فیصد ہے؟"), int(Q8),
      ("72 ÷ 360 × 100.", "72 ÷ 360 × 100"),
      ("Right! 72 ÷ 360 = 1/5, which is 20%.", "درست! 72 ÷ 360 = 1/5، یعنی 20٪"), ("72 ÷ 360 = 0.2, and 0.2 × 100 = 20.", "72 ÷ 360 = 0.2، اور 0.2 × 100 = 20"),
      [(72, "72 is the angle itself. Divide by 360 and multiply by 100: 20.", "72 خود زاویہ ہے۔ 360 سے تقسیم کریں اور 100 سے ضرب دیں: 20", "pie_total_wrong"),
       (5, "5 is 360 ÷ 72, the other way up. 72 ÷ 360 × 100 = 20.", "5 یعنی 360 ÷ 72، الٹا۔ 72 ÷ 360 × 100 = 20", "pie_total_wrong")]),
   nq("q9_from_angle", (f"A pie chart shows {Q9_T} people. A sector has an angle of {Q9_A}°. How many people does it stand for?", f"ایک دائری نقشہ {Q9_T} لوگ دکھاتا ہے۔ ایک ٹکڑے کا زاویہ {Q9_A}° ہے۔ یہ کتنے لوگوں کو ظاہر کرتا ہے؟"), Q9,
      ("90 ÷ 360 × 240.", "90 ÷ 360 × 240"),
      ("Right! 90 ÷ 360 = 1/4, and 1/4 of 240 is 60.", "درست! 90 ÷ 360 = 1/4، اور 240 کا 1/4 یعنی 60"), ("240 ÷ 4 = 60.", "240 ÷ 4 = 60"),
      [(90, "90 is the angle. The number of people is 90 ÷ 360 × 240 = 60.", "90 زاویہ ہے۔ لوگوں کی تعداد 90 ÷ 360 × 240 = 60 ہے۔", "percent_as_number"),
       (24, "24 is 240 ÷ 10. A quarter of 240 is 60.", "24 یعنی 240 ÷ 10۔ 240 کا چوتھائی 60 ہے۔", "percent_as_number")]),
   ch("q10_which", ("Which set of sector angles can belong to one pie chart?", "سیکٹر کے زاویوں کا کون سا مجموعہ ایک ہی دائری نقشے کا ہو سکتا ہے؟"),
      ("120°, 100°, 80°, 60°", "120°، 100°، 80°، 60°", "Yes! 120 + 100 + 80 + 60 = 360.", "جی ہاں! 120 + 100 + 80 + 60 = 360"),
      [("120°, 100°, 80°, 50°", "120°، 100°، 80°، 50°", "These add up to 350°, not 360°.", "یہ 350° بنتے ہیں، 360° نہیں۔", "pie_total_wrong"),
       ("150°, 100°, 80°, 40°", "150°، 100°، 80°، 40°", "These add up to 370°, too much.", "یہ 370° بنتے ہیں، بہت زیادہ۔", "pie_total_wrong"),
       ("100°, 100°, 100°, 100°", "100°، 100°، 100°، 100°", "These add up to 400°.", "یہ 400° بنتے ہیں۔", "pie_total_wrong")],
      2, qtype="apply"),
   ch("q11_find_error", ("Aziz says: 20 of 80 pupils like football, so its sector angle is 20 ÷ 80 × 100 = 25°. What went wrong?", "عزیز کہتا ہے: 80 میں سے 20 طلبہ کو فٹ بال پسند ہے، تو اس ٹکڑے کا زاویہ 20 ÷ 80 × 100 = 25° ہے۔ کیا غلطی ہوئی؟"),
      ("He multiplied by 100. For an angle multiply by 360: 20 ÷ 80 × 360 = 90°.", "اس نے 100 سے ضرب دی۔ زاویے کے لیے 360 سے ضرب دیں: 20 ÷ 80 × 360 = 90°", "Yes! × 100 gives a percentage (25%). × 360 gives the angle (90°).", "جی ہاں! × 100 فیصد دیتا ہے (25٪)۔ × 360 زاویہ دیتا ہے (90°)۔"),
      [("Nothing. 25° is right.", "کوئی غلطی نہیں۔ 25° ٹھیک ہے۔", "25 is the percentage. A quarter of the circle is 90°.", "25 فیصد ہے۔ دائرے کا چوتھائی 90° ہے۔", "angle_times_100"),
       ("He should have divided 80 by 20 and multiplied by 360.", "اسے 80 کو 20 سے تقسیم کر کے 360 سے ضرب دینی چاہیے تھی۔", "That is upside down. It would give 1440°. Use 20 ÷ 80.", "یہ الٹا ہے۔ اس سے 1440° آئے گا۔ 20 ÷ 80 لیں۔", "angle_times_100")],
      1, qtype="find_error"),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! You can work with pie charts.", "شاباش! آپ دائری نقشوں کے ساتھ کام کر سکتے ہیں۔"),
    "text": T("A pie chart is 100% and 360°. Quantity = percentage ÷ 100 × total. Sector angle = value ÷ total × 360°. Percentage = angle ÷ 360 × 100. A missing sector is what is left after the known ones are taken away. Check: the angles must add up to 360°.",
              "دائری نقشہ 100٪ اور 360° ہے۔ مقدار = فیصد ÷ 100 × کل۔ ٹکڑے کا زاویہ = قیمت ÷ کل × 360°۔ فیصد = زاویہ ÷ 360 × 100۔ غائب ٹکڑا وہ ہے جو معلوم ٹکڑے نکالنے کے بعد بچے۔ جانچ: زاویوں کا مجموعہ 360° ہونا چاہیے۔"),
    "points": [T("Angle: ÷ total × 360. Percentage: × 100.", "زاویہ: ÷ کل × 360۔ فیصد: × 100۔"),
               T("The angles add up to 360°.", "زاویوں کا مجموعہ 360° ہوتا ہے۔")]},
 ],
 bank=[
   {"id": "qb_recall", "type": "recall", "step": ch("qb_recall", ("What do all the percentages of a pie chart add up to?", "دائری نقشے کے تمام فیصد کا مجموعہ کتنا ہوتا ہے؟"),
      ("100%", "100٪", "Yes! The whole pie is 100%.", "جی ہاں! پورا دائرہ 100٪ ہے۔"),
      [("360%", "360٪", "360 is for degrees. Percentages add up to 100.", "360 درجوں کا ہے۔ فیصد کا مجموعہ 100 ہے۔", "pie_total_wrong"),
       ("50%", "50٪", "50% is half. The whole is 100%.", "50٪ آدھا ہے۔ پورا 100٪ ہے۔", "pie_total_wrong")],
      1, qtype=None)},
   {"id": "qb_angle", "type": "apply", "step": nq("qb_angle", (f"{QB_V} of {QB_T} pupils walk to school. What is the angle of the walking sector in a pie chart, in degrees?", f"{QB_T} میں سے {QB_V} طلبہ پیدل سکول آتے ہیں۔ دائری نقشے میں پیدل والے ٹکڑے کا زاویہ درجوں میں کتنا ہے؟"), QB,
      ("10 ÷ 40 × 360.", "10 ÷ 40 × 360"),
      ("Right! 10 ÷ 40 = 1/4, and 1/4 of 360 is 90°.", "درست! 10 ÷ 40 = 1/4، اور 360 کا 1/4 یعنی 90°"), ("360 ÷ 4 = 90.", "360 ÷ 4 = 90"),
      [(25, "25 is the percentage. Multiply by 360 for the angle: 90.", "25 فیصد ہے۔ زاویے کے لیے 360 سے ضرب دیں: 90", "angle_times_100"),
       (10, "10 is the number of pupils. The angle is 10 ÷ 40 × 360 = 90.", "10 طلبہ کی تعداد ہے۔ زاویہ 10 ÷ 40 × 360 = 90 ہے۔", "angle_is_value")], qtype=None)},
   {"id": "qb_half", "type": "apply", "step": nq("qb_half", ("Half of the people in a pie chart like tea. What is the angle of the tea sector, in degrees?", "دائری نقشے میں آدھے لوگوں کو چائے پسند ہے۔ چائے کے ٹکڑے کا زاویہ درجوں میں کتنا ہے؟"), QB_HALF,
      ("Half of 360.", "360 کا آدھا۔"),
      ("Right! 360 ÷ 2 = 180°.", "درست! 360 ÷ 2 = 180°"), ("Half the circle is a straight line, 180°.", "آدھا دائرہ سیدھی لکیر ہے، 180°"),
      [(50, "50 is the percentage. Half of 360 is 180.", "50 فیصد ہے۔ 360 کا آدھا 180 ہے۔", "angle_times_100"),
       (90, "90° is a quarter of the circle. Half is 180.", "90° دائرے کا چوتھائی ہے۔ آدھا 180 ہے۔", "pie_total_wrong")], qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": ch("qb_find_error", ("A pie chart has the angles 90°, 120° and 100°. Mehr says the fourth sector is 40°. What went wrong?", "ایک دائری نقشے میں زاویے 90°، 120° اور 100° ہیں۔ مہر کہتی ہے چوتھا ٹکڑا 40° ہے۔ کیا غلطی ہوئی؟"),
      ("She should take the three angles from 360°: 360 − 310 = 50°, not 40°.", "اسے تینوں زاویے 360° میں سے گھٹانے چاہییں: 360 − 310 = 50°، 40° نہیں۔", "Yes! 90 + 120 + 100 = 310, and 360 − 310 = 50.", "جی ہاں! 90 + 120 + 100 = 310، اور 360 − 310 = 50"),
      [("Nothing. 40° is right.", "کوئی غلطی نہیں۔ 40° ٹھیک ہے۔", "With 40° the angles add up to 350°, not 360°.", "40° کے ساتھ زاویوں کا مجموعہ 350° ہوتا ہے، 360° نہیں۔", "missing_not_taken"),
       ("She should take them from 180°.", "اسے انہیں 180° میں سے گھٹانا چاہیے۔", "A pie chart is a full circle, 360°.", "دائری نقشہ پورا دائرہ ہے، 360°۔", "pie_total_wrong")],
      0, qtype=None)},
 ],
 review=[
   {"id": "r_angle", "type": "apply", "step": nq("r_angle", (f"In a pie chart of {R1_T} people, {R1_V} chose rice. What is the angle of the rice sector, in degrees?", f"{R1_T} لوگوں کے دائری نقشے میں {R1_V} نے چاول چنے۔ چاول کے ٹکڑے کا زاویہ درجوں میں کتنا ہے؟"), R1,
      ("25 ÷ 100 × 360.", "25 ÷ 100 × 360"),
      ("Right! 25 ÷ 100 = 1/4, and 1/4 of 360 is 90°.", "درست! 25 ÷ 100 = 1/4، اور 360 کا 1/4 یعنی 90°"), ("360 ÷ 4 = 90.", "360 ÷ 4 = 90"),
      [(25, "25 is the number of people. The angle is 25 ÷ 100 × 360 = 90.", "25 لوگوں کی تعداد ہے۔ زاویہ 25 ÷ 100 × 360 = 90 ہے۔", "angle_is_value")], qtype=None)},
   {"id": "r_quantity", "type": "apply", "step": nq("r_quantity", (f"{R2_T} pupils are in a pie chart, and the reading sector is {R2_P}%. How many pupils is that?", f"دائری نقشے میں {R2_T} طلبہ ہیں، اور مطالعے کا ٹکڑا {R2_P}٪ ہے۔ یہ کتنے طلبہ ہیں؟"), R2,
      ("30 ÷ 100 × 60.", "30 ÷ 100 × 60"),
      ("Right! 30 ÷ 100 × 60 = 18 pupils.", "درست! 30 ÷ 100 × 60 = 18 طلبہ"), ("10% of 60 is 6, so 30% is 18.", "60 کا 10٪ یعنی 6، تو 30٪ یعنی 18"),
      [(30, "30 is the percentage, not the number of pupils: 18.", "30 فیصد ہے، طلبہ کی تعداد نہیں: 18", "percent_as_number")], qtype=None)},
 ],
 glossary=[T("Pie chart", "دائری نقشہ (پائی چارٹ)"), T("Slice", "ٹکڑا"), T("Angle", "زاویہ"), T("Degree", "درجہ"), T("Percentage", "فیصد"), T("Total", "کل")],
 flashcards=[
   {"id": "f_angle", "front": T("How do you find a sector angle?", "ٹکڑے کا زاویہ کیسے نکالتے ہیں؟"),
    "back": T("Angle = value ÷ total × 360°.", "زاویہ = قیمت ÷ کل × 360°")},
   {"id": "f_whole", "front": T("What do the sectors of a pie chart add up to?", "دائری نقشے کے ٹکڑوں کا مجموعہ کتنا ہے؟"),
    "back": T("360° and 100%.", "360° اور 100٪")},
 ],
 home_task={"id": "h_pie", "text": T(
   "Ask 20 classmates which fruit they like best (three or four fruits). Work out each sector angle with value ÷ total × 360°, check that the angles add up to 360°, and draw the pie chart in your notebook with a protractor.",
   "اپنے 20 ہم جماعتوں سے پوچھیں کہ انہیں کون سا پھل سب سے زیادہ پسند ہے (تین یا چار پھل)۔ ہر ٹکڑے کا زاویہ قیمت ÷ کل × 360° سے نکالیں، جانچیں کہ زاویوں کا مجموعہ 360° ہے، اور کاپی میں زاویہ پیما سے دائری نقشہ بنائیں۔")},
 notes=["Covers the whole circle (q1, qb_recall, q10), reading a pie chart in percentages (q2 to q4), a missing sector (q5, qb_find_error), the sector angle value ÷ total × 360 (q6, q7, qb_angle, qb_half, r_angle, q11), and a percentage or a quantity from an angle (q8, q9, r_quantity).",
        "Each wrong answer is a real mistake: multiplying by 100 instead of 360, giving the value as the angle, giving the percentage as the number of people, and not taking the known sectors from the whole.",
        "The app cannot check a drawing, so these questions are about reading and calculating; drawing the chart with a protractor is the home task. Figure labels are letters and numbers; the step text says what each letter stands for.",
        "Urdu terms to check: دائری نقشہ (پائی چارٹ), ٹکڑا, زاویہ, درجہ and کل, all as in the existing Data Handling lessons. فیصد (percentage, written ٪) is the term used in the existing percentage lessons. No new Urdu terms were added."],
 minutes=18,
)
write(lesson)
