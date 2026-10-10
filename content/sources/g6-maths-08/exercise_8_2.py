"""Practice set for Exercise 8.2 of the book: altitudes, and the area of
parallelograms, trapeziums and triangles, including finding a missing base or
height. The questions are new; only the kinds of question follow the book."""
from common import (T, say, nq, ch, practice_lesson, practice_intro, write, EX_SKILL,
                    PA_AREA, PA_TRIANGLE, PA_PARALLELOGRAM, PA_COMPOUND, PA_WORD_PROBLEMS)

SKILL = EX_SKILL["8.2"]


def para(b, h):
    return b * h


def tri2(b, h):
    """Twice the area of a triangle (so it stays a whole number for checks)."""
    return b * h


def trap2(a, b, h):
    """Twice the area of a trapezium."""
    return (a + b) * h


# q2: parallelogram base 12, height 7, slanting side 9
Q2 = para(12, 7)
assert Q2 == 84 and 12 * 9 == 108 and 12 + 7 == 19
# q3: triangle base 14, height 9
assert tri2(14, 9) % 2 == 0
Q3 = tri2(14, 9) // 2
assert Q3 == 63 and 14 * 9 == 126
# q4: trapezium parallel sides 10 and 16, height 6
assert trap2(10, 16, 6) % 2 == 0
Q4 = trap2(10, 16, 6) // 2
assert Q4 == 78 and 26 * 6 == 156 and 10 * 16 == 160 and (10 + 16) // 2 == 13
# q5: triangle area 60, base 12 -> height
Q5 = 2 * 60 // 12
assert Q5 == 10 and 12 * 10 // 2 == 60 and 60 // 12 == 5 and 60 * 12 == 720
# q6: parallelogram area 96, height 8 -> base
Q6 = 96 // 8
assert Q6 == 12 and para(12, 8) == 96 and 96 - 8 == 88 and 96 * 8 == 768
# q7: trapezium area 54, height 6, one parallel side 7 -> other
SUM7 = 2 * 54 // 6
Q7 = SUM7 - 7
assert SUM7 == 18 and Q7 == 11 and trap2(7, 11, 6) // 2 == 54 and 54 // 6 == 9 and 9 - 7 == 2
# q8 (find error): parallelogram base 10, slanting 6, height 5
assert para(10, 5) == 50 and 10 * 6 == 60
# q9 (find error): triangle base 8, height 5
assert tri2(8, 5) // 2 == 20 and 8 * 5 == 40
# q10: right-angled triangle with legs 9 and 12, hypotenuse 15
Q10 = tri2(9, 12) // 2
assert Q10 == 54 and 9 * 12 == 108 and 9 * 12 * 15 == 1620 and 9 + 12 + 15 == 36 and 9 ** 2 + 12 ** 2 == 15 ** 2
# q11: rectangle 10 by 6 and triangle on the same base and height
Q11 = 10 * 6 - tri2(10, 6) // 2
assert Q11 == 30 and 10 * 6 == 60
# q12: sort shapes (one pair of parallel sides)
# bank and review
QB1 = para(15, 4)
assert QB1 == 60 and 15 * 5 == 75
QB2 = tri2(16, 5) // 2
assert QB2 == 40 and 16 * 5 == 80
QB3 = trap2(8, 12, 5) // 2
assert QB3 == 50 and 20 * 5 == 100
R1 = tri2(9, 8) // 2
assert R1 == 36 and 72 == 9 * 8
R2 = 70 // 7
assert R2 == 10 and para(10, 7) == 70 and 70 - 7 == 63

lesson = practice_lesson(
 "8.2", script="exercise_8_2.py",
 title=T("Exercise 8.2 practice: parallelograms, trapeziums and triangles", "مشق 8.2 کی پریکٹس: متوازی الاضلاع، ذوزنقہ اور مثلث"),
 outcome="Mark the altitude of a figure, find the area of parallelograms, trapeziums and triangles, and find a missing base or height.",
 prerequisites=[PA_AREA, PA_TRIANGLE, PA_PARALLELOGRAM, PA_COMPOUND, PA_WORD_PROBLEMS],
 misconceptions=[
   {"id": "slant_for_height", "description": "Uses the slanting side instead of the perpendicular height."},
   {"id": "forgets_half", "description": "Gives base × height for a triangle, without halving."},
   {"id": "trapezium_product", "description": "Multiplies the two parallel sides, or forgets to halve, in the area of a trapezium."},
   {"id": "wrong_inverse", "description": "Subtracts or multiplies instead of dividing to find a missing base or height."},
   {"id": "missing_side_half", "description": "Forgets that a triangle's area is half of base × height when finding the height, and divides the area by the base only."},
   {"id": "stops_early", "description": "Stops after finding the sum of the parallel sides and gives it as the missing side."},
   {"id": "perimeter_for_area", "description": "Adds the sides instead of finding the area."},
 ],
 steps=[
   practice_intro("8.2",
     "Here you mark altitudes, find the area of a parallelogram, a trapezium and a triangle, and find a missing base or height.",
     "اس میں آپ ارتفاع نشان کریں گے، متوازی الاضلاع، ذوزنقہ اور مثلث کا رقبہ نکالیں گے، اور گمشدہ قاعدہ یا اونچائی معلوم کریں گے۔",
     "Exercise 8.2 is about altitudes and areas. Ready?", "مشق 8.2 ارتفاع اور رقبوں کے بارے میں ہے۔ تیار؟"),
   ch("q1_altitude", ("What is the altitude (height) of a parallelogram?", "متوازی الاضلاع کا ارتفاع (اونچائی) کیا ہے؟"),
      ("The perpendicular distance between the base and the opposite side", "قاعدے اور مخالف ضلع کے درمیان عمودی فاصلہ", "Yes! It makes a right angle with the base.", "جی ہاں! یہ قاعدے کے ساتھ زاویہ قائمہ بناتا ہے۔"),
      [("The length of the slanting side", "ترچھے ضلع کی لمبائی", "The slanting side is longer than the height. Height meets the base at a right angle.", "ترچھا ضلع اونچائی سے لمبا ہوتا ہے۔ اونچائی قاعدے سے زاویہ قائمہ پر ملتی ہے۔", "slant_for_height"),
       ("The sum of all the sides", "تمام اضلاع کا مجموعہ", "That is the perimeter.", "یہ احاطہ ہے۔", "perimeter_for_area"),
       ("The longest side", "سب سے لمبا ضلع", "The height need not be a side at all.", "اونچائی کا کسی ضلع ہونا ضروری نہیں۔", "slant_for_height")],
      2, qtype="recall"),
   nq("q2_parallelogram", ("A parallelogram has a base of 12 cm, a slanting side of 9 cm and a height of 7 cm. What is its area, in cm²?", "ایک متوازی الاضلاع کا قاعدہ 12 سینٹی میٹر، ترچھا ضلع 9 سینٹی میٹر اور اونچائی 7 سینٹی میٹر ہے۔ اس کا رقبہ کتنے مربع سینٹی میٹر ہے؟"), Q2,
      ("Area = base × height. The slanting side is not used.", "رقبہ = قاعدہ × اونچائی۔ ترچھا ضلع استعمال نہیں ہوتا۔"),
      ("Right! 12 × 7 = 84 cm².", "درست! 12 × 7 = 84 مربع سینٹی میٹر"), ("Base × height = 12 × 7 = 84 cm².", "قاعدہ × اونچائی = 12 × 7 = 84 مربع سینٹی میٹر"),
      [(108, "That uses the slanting side, 9. Use the height, 7: 84.", "یہ ترچھا ضلع، 9، استعمال کرتا ہے۔ اونچائی، 7، لیں: 84", "slant_for_height"),
       (19, "That adds 12 and 7. Multiply: 84.", "یہ 12 اور 7 جمع کرتا ہے۔ ضرب دیں: 84", "perimeter_for_area")], qtype="recall"),
   nq("q3_triangle", ("A triangle has a base of 14 cm and a height of 9 cm. What is its area, in cm²?", "ایک مثلث کا قاعدہ 14 سینٹی میٹر اور اونچائی 9 سینٹی میٹر ہے۔ اس کا رقبہ کتنے مربع سینٹی میٹر ہے؟"), Q3,
      ("Area of a triangle = ½ × base × height.", "مثلث کا رقبہ = ½ × قاعدہ × اونچائی"),
      ("Right! ½ × 14 × 9 = 63 cm².", "درست! ½ × 14 × 9 = 63 مربع سینٹی میٹر"), ("14 × 9 = 126, half of that is 63.", "14 × 9 = 126، اس کا آدھا 63 ہے۔"),
      [(126, "That is base × height, the area of the whole parallelogram. A triangle is half: 63.", "یہ قاعدہ × اونچائی ہے، پورے متوازی الاضلاع کا رقبہ۔ مثلث اس کا آدھا ہے: 63", "forgets_half")], qtype="recall"),
   {"id": "s_idea", "type": "explain",
    "character": say("thinking", "The height must meet the base at a right angle. The slanting side is not the height!", "اونچائی قاعدے سے زاویہ قائمہ پر ملتی ہے۔ ترچھا ضلع اونچائی نہیں!"),
    "text": T("The altitude (height) is the perpendicular distance from the base to the opposite side or corner. Parallelogram: area = base × height. Triangle: area = ½ × base × height. Trapezium: area = ½ × (sum of the parallel sides) × height. To find a missing base or height, put the numbers in the formula and undo it: for a triangle, height = 2 × area ÷ base.",
              "ارتفاع (اونچائی) قاعدے سے مخالف ضلع یا کونے تک عمودی فاصلہ ہے۔ متوازی الاضلاع: رقبہ = قاعدہ × اونچائی۔ مثلث: رقبہ = ½ × قاعدہ × اونچائی۔ ذوزنقہ: رقبہ = ½ × (متوازی اضلاع کا مجموعہ) × اونچائی۔ گمشدہ قاعدہ یا اونچائی معلوم کرنے کے لیے عدد کلیے میں رکھیں اور اسے الٹ دیں: مثلث کے لیے اونچائی = 2 × رقبہ ÷ قاعدہ۔")},
   nq("q4_trapezium", ("A trapezium has parallel sides of 10 cm and 16 cm, and a height of 6 cm. What is its area, in cm²?", "ایک ذوزنقہ کے متوازی اضلاع 10 سینٹی میٹر اور 16 سینٹی میٹر ہیں اور اونچائی 6 سینٹی میٹر ہے۔ اس کا رقبہ کتنے مربع سینٹی میٹر ہے؟"), Q4,
      ("½ × (10 + 16) × 6.", "½ × (10 + 16) × 6"),
      ("Right! ½ × 26 × 6 = 78 cm².", "درست! ½ × 26 × 6 = 78 مربع سینٹی میٹر"), ("10 + 16 = 26, 26 × 6 = 156, half is 78.", "10 + 16 = 26، 26 × 6 = 156، اس کا آدھا 78"),
      [(156, "You forgot the half. Half of 156 is 78.", "آپ آدھا کرنا بھول گئے۔ 156 کا آدھا 78 ہے۔", "forgets_half"),
       (160, "That multiplies the two parallel sides. Add them, then × height ÷ 2: 78.", "یہ دونوں متوازی اضلاع کو ضرب دیتا ہے۔ انہیں جمع کریں، پھر × اونچائی ÷ 2: 78", "trapezium_product")]),
   nq("q5_missing_height", ("A triangle has an area of 60 cm² and a base of 12 cm. What is its height, in cm?", "ایک مثلث کا رقبہ 60 مربع سینٹی میٹر اور قاعدہ 12 سینٹی میٹر ہے۔ اس کی اونچائی کتنے سینٹی میٹر ہے؟"), Q5,
      ("Double the area, 120, then divide by the base.", "رقبے کو دگنا کریں، 120، پھر قاعدے سے تقسیم کریں۔"),
      ("Right! 2 × 60 ÷ 12 = 10 cm. Check: ½ × 12 × 10 = 60.", "درست! 2 × 60 ÷ 12 = 10 سینٹی میٹر۔ جانچ: ½ × 12 × 10 = 60"),
      ("120 ÷ 12 = 10.", "120 ÷ 12 = 10"),
      [(5, "60 ÷ 12 forgets the half. The area is only half of base × height, so double 60 first: 10.", "60 ÷ 12 آدھے کو بھول جاتا ہے۔ رقبہ قاعدہ × اونچائی کا صرف آدھا ہے، پہلے 60 کو دگنا کریں: 10", "missing_side_half"),
       (720, "That multiplies. Undo the formula by dividing: 10.", "یہ ضرب دیتا ہے۔ کلیے کو تقسیم سے الٹیں: 10", "wrong_inverse")]),
   nq("q6_missing_base", ("A parallelogram has an area of 96 m² and a height of 8 m. What is its base, in metres?", "ایک متوازی الاضلاع کا رقبہ 96 مربع میٹر اور اونچائی 8 میٹر ہے۔ اس کا قاعدہ کتنے میٹر ہے؟"), Q6,
      ("Area = base × height, so base = area ÷ height.", "رقبہ = قاعدہ × اونچائی، تو قاعدہ = رقبہ ÷ اونچائی"),
      ("Right! 96 ÷ 8 = 12 m.", "درست! 96 ÷ 8 = 12 میٹر"), ("96 ÷ 8 = 12, and 12 × 8 = 96.", "96 ÷ 8 = 12، اور 12 × 8 = 96"),
      [(88, "That takes 8 away. Undo × 8 by dividing: 12.", "یہ 8 تفریق کرتا ہے۔ × 8 کو تقسیم سے ختم کریں: 12", "wrong_inverse"),
       (768, "That multiplies. Divide: 12.", "یہ ضرب دیتا ہے۔ تقسیم کریں: 12", "wrong_inverse")]),
   nq("q7_missing_side", ("A trapezium has an area of 54 cm² and a height of 6 cm. One parallel side is 7 cm. How long is the other parallel side, in cm?", "ایک ذوزنقہ کا رقبہ 54 مربع سینٹی میٹر اور اونچائی 6 سینٹی میٹر ہے۔ ایک متوازی ضلع 7 سینٹی میٹر ہے۔ دوسرا متوازی ضلع کتنے سینٹی میٹر ہے؟"), Q7,
      ("Double the area and divide by the height to get the sum of the parallel sides. Then take 7 away.", "رقبے کو دگنا کریں اور اونچائی سے تقسیم کریں تو متوازی اضلاع کا مجموعہ ملے گا۔ پھر 7 تفریق کریں۔"),
      ("Right! 2 × 54 ÷ 6 = 18, and 18 − 7 = 11 cm.", "درست! 2 × 54 ÷ 6 = 18، اور 18 − 7 = 11 سینٹی میٹر"),
      ("The two parallel sides add up to 108 ÷ 6 = 18. The other is 18 − 7 = 11.", "دونوں متوازی اضلاع کا مجموعہ 108 ÷ 6 = 18 ہے۔ دوسرا 18 − 7 = 11 ہے۔"),
      [(18, "18 cm is the two parallel sides together. Take the 7 cm one away: 11.", "18 سینٹی میٹر دونوں متوازی اضلاع کا مجموعہ ہے۔ 7 سینٹی میٹر والا تفریق کریں: 11", "stops_early"),
       (2, "54 ÷ 6 = 9 forgets the half. The sum is 18, so the other side is 11.", "54 ÷ 6 = 9 آدھے کو بھول جاتا ہے۔ مجموعہ 18 ہے، تو دوسرا ضلع 11 ہے۔", "missing_side_half")]),
   ch("q8_find_error", ("A parallelogram has a base of 10 cm, a slanting side of 6 cm and a height of 5 cm. Wasim says its area is 10 × 6 = 60 cm². What went wrong?", "ایک متوازی الاضلاع کا قاعدہ 10 سینٹی میٹر، ترچھا ضلع 6 سینٹی میٹر اور اونچائی 5 سینٹی میٹر ہے۔ وسیم کہتا ہے اس کا رقبہ 10 × 6 = 60 مربع سینٹی میٹر ہے۔ کیا غلطی ہوئی؟"),
      ("He used the slanting side. With the height, the area is 10 × 5 = 50 cm².", "اس نے ترچھا ضلع استعمال کیا۔ اونچائی سے رقبہ 10 × 5 = 50 مربع سینٹی میٹر ہے۔", "Yes! Always use the height that makes a right angle with the base.", "جی ہاں! ہمیشہ وہ اونچائی لیں جو قاعدے کے ساتھ زاویہ قائمہ بنائے۔"),
      [("Nothing. 60 cm² is right.", "کوئی غلطی نہیں۔ 60 مربع سینٹی میٹر درست ہے۔", "6 cm is the slanting side, not the height.", "6 سینٹی میٹر ترچھا ضلع ہے، اونچائی نہیں۔", "slant_for_height"),
       ("He should have halved it: 30 cm².", "اسے آدھا کرنا چاہیے تھا: 30 مربع سینٹی میٹر۔", "A parallelogram is not halved. That is for a triangle.", "متوازی الاضلاع آدھا نہیں ہوتا۔ یہ مثلث کے لیے ہے۔", "forgets_half")],
      1, qtype="find_error"),
   ch("q9_find_error_triangle", ("Hiba says a triangle with base 8 cm and height 5 cm has an area of 8 × 5 = 40 cm². What went wrong?", "ہبہ کہتی ہے 8 سینٹی میٹر قاعدے اور 5 سینٹی میٹر اونچائی والے مثلث کا رقبہ 8 × 5 = 40 مربع سینٹی میٹر ہے۔ کیا غلطی ہوئی؟"),
      ("She forgot the half. The area is ½ × 8 × 5 = 20 cm².", "وہ آدھا کرنا بھول گئی۔ رقبہ ½ × 8 × 5 = 20 مربع سینٹی میٹر ہے۔", "Yes! A triangle is half of the rectangle on the same base and height.", "جی ہاں! مثلث اسی قاعدے اور اونچائی کی مستطیل کا آدھا ہوتا ہے۔"),
      [("Nothing. 40 cm² is right.", "کوئی غلطی نہیں۔ 40 مربع سینٹی میٹر درست ہے۔", "8 × 5 = 40 is the rectangle's area. The triangle is half of it.", "8 × 5 = 40 مستطیل کا رقبہ ہے۔ مثلث اس کا آدھا ہے۔", "forgets_half"),
       ("She should have added: 8 + 5 = 13 cm².", "اسے جمع کرنا چاہیے تھا: 8 + 5 = 13 مربع سینٹی میٹر۔", "Area is not found by adding.", "رقبہ جمع کر کے نہیں نکلتا۔", "perimeter_for_area")],
      0, qtype="find_error"),
   nq("q10_right_triangle", ("A right-angled triangle has two short sides (legs) of 9 cm and 12 cm, and a long side of 15 cm. What is its area, in cm²? (One leg is the base and the other is the height.)", "ایک قائمہ زاویہ مثلث کے دو چھوٹے اضلاع 9 سینٹی میٹر اور 12 سینٹی میٹر ہیں، اور لمبا ضلع 15 سینٹی میٹر ہے۔ اس کا رقبہ کتنے مربع سینٹی میٹر ہے؟ (ایک چھوٹا ضلع قاعدہ ہے اور دوسرا اونچائی۔)"), Q10,
      ("In a right-angled triangle the two short sides make the right angle, so one is the base and the other the height.", "قائمہ زاویہ مثلث میں دونوں چھوٹے اضلاع زاویہ قائمہ بناتے ہیں، تو ایک قاعدہ اور دوسرا اونچائی ہے۔"),
      ("Right! ½ × 9 × 12 = 54 cm².", "درست! ½ × 9 × 12 = 54 مربع سینٹی میٹر"), ("9 × 12 = 108, half is 54. The 15 cm side is not needed.", "9 × 12 = 108، اس کا آدھا 54۔ 15 سینٹی میٹر والا ضلع درکار نہیں۔"),
      [(108, "You forgot the half: 54.", "آپ آدھا کرنا بھول گئے: 54", "forgets_half"),
       (36, "That adds the three sides, the perimeter. The area is ½ × 9 × 12 = 54.", "یہ تینوں اضلاع جمع کرتا ہے، یعنی احاطہ۔ رقبہ ½ × 9 × 12 = 54 ہے۔", "perimeter_for_area")]),
   nq("q11_compare", ("A rectangle is 10 cm by 6 cm. A triangle has the same base, 10 cm, and the same height, 6 cm. How many cm² bigger is the area of the rectangle than the area of the triangle?", "ایک مستطیل 10 ضرب 6 سینٹی میٹر ہے۔ ایک مثلث کا قاعدہ وہی 10 سینٹی میٹر اور اونچائی وہی 6 سینٹی میٹر ہے۔ مستطیل کا رقبہ مثلث کے رقبے سے کتنے مربع سینٹی میٹر زیادہ ہے؟"), Q11,
      ("Find both areas, then subtract.", "دونوں رقبے نکالیں، پھر تفریق کریں۔"),
      ("Right! 60 − 30 = 30 cm².", "درست! 60 − 30 = 30 مربع سینٹی میٹر"), ("Rectangle 60, triangle ½ × 60 = 30, difference 30.", "مستطیل 60، مثلث ½ × 60 = 30، فرق 30"),
      [(60, "60 cm² is the rectangle's area. Subtract the triangle's 30: 30.", "60 مربع سینٹی میٹر مستطیل کا رقبہ ہے۔ مثلث کا 30 تفریق کریں: 30", "forgets_half"),
       (0, "The triangle is only half the rectangle, so they are not equal. The difference is 30.", "مثلث مستطیل کا صرف آدھا ہے، اس لیے برابر نہیں۔ فرق 30 ہے۔", "forgets_half")]),
   ch("q12_trapezium", ("Which shape has exactly one pair of parallel sides?", "کس شکل میں بالکل ایک جوڑی متوازی اضلاع ہوتی ہے؟"),
      ("A trapezium", "ذوزنقہ", "Yes! Only the two parallel sides are used in its area, with the height.", "جی ہاں! اس کے رقبے میں صرف دونوں متوازی اضلاع اور اونچائی استعمال ہوتی ہیں۔"),
      [("A parallelogram", "متوازی الاضلاع", "A parallelogram has two pairs of parallel sides.", "متوازی الاضلاع میں متوازی اضلاع کی دو جوڑیاں ہوتی ہیں۔"),
       ("A rectangle", "مستطیل", "A rectangle has two pairs of parallel sides.", "مستطیل میں متوازی اضلاع کی دو جوڑیاں ہوتی ہیں۔"),
       ("A triangle", "مثلث", "A triangle has no parallel sides.", "مثلث میں کوئی متوازی اضلاع نہیں ہوتے۔")],
      3, qtype="recall"),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! You know the areas of these shapes.", "شاباش! آپ ان اشکال کے رقبے جانتے ہیں۔"),
    "text": T("Use the perpendicular height, never the slanting side. Parallelogram: base × height. Triangle: ½ × base × height. Trapezium: ½ × (sum of the parallel sides) × height. For a missing base or height, divide the area by the other measurement, and for a triangle or trapezium double the area first.",
              "عمودی اونچائی لیں، کبھی ترچھا ضلع نہیں۔ متوازی الاضلاع: قاعدہ × اونچائی۔ مثلث: ½ × قاعدہ × اونچائی۔ ذوزنقہ: ½ × (متوازی اضلاع کا مجموعہ) × اونچائی۔ گمشدہ قاعدہ یا اونچائی کے لیے رقبے کو دوسری پیمائش سے تقسیم کریں، اور مثلث یا ذوزنقہ میں پہلے رقبے کو دگنا کریں۔"),
    "points": [T("Height meets the base at a right angle.", "اونچائی قاعدے سے زاویہ قائمہ پر ملتی ہے۔"),
               T("A triangle is half of base × height.", "مثلث قاعدہ × اونچائی کا آدھا ہے۔")]},
 ],
 bank=[
   {"id": "qb_para", "type": "recall", "step": nq("qb_para", ("A parallelogram has base 15 cm and height 4 cm. What is its area, in cm²?", "ایک متوازی الاضلاع کا قاعدہ 15 سینٹی میٹر اور اونچائی 4 سینٹی میٹر ہے۔ اس کا رقبہ کتنے مربع سینٹی میٹر ہے؟"), QB1,
      ("Base × height.", "قاعدہ × اونچائی"),
      ("Right! 15 × 4 = 60 cm².", "درست! 15 × 4 = 60 مربع سینٹی میٹر"), ("15 × 4 = 60.", "15 × 4 = 60"),
      [(19, "That adds. Multiply: 60.", "یہ جمع کرتا ہے۔ ضرب دیں: 60", "perimeter_for_area")], qtype=None)},
   {"id": "qb_tri", "type": "apply", "step": nq("qb_tri", ("A triangle has a base of 16 cm and a height of 5 cm. What is its area, in cm²?", "ایک مثلث کا قاعدہ 16 سینٹی میٹر اور اونچائی 5 سینٹی میٹر ہے۔ اس کا رقبہ کتنے مربع سینٹی میٹر ہے؟"), QB2,
      ("½ × 16 × 5.", "½ × 16 × 5"),
      ("Right! 40 cm².", "درست! 40 مربع سینٹی میٹر"), ("16 × 5 = 80, half is 40.", "16 × 5 = 80، آدھا 40"),
      [(80, "You forgot the half: 40.", "آپ آدھا کرنا بھول گئے: 40", "forgets_half")], qtype=None)},
   {"id": "qb_trap", "type": "apply", "step": nq("qb_trap", ("A trapezium has parallel sides of 8 cm and 12 cm and a height of 5 cm. What is its area, in cm²?", "ایک ذوزنقہ کے متوازی اضلاع 8 سینٹی میٹر اور 12 سینٹی میٹر ہیں اور اونچائی 5 سینٹی میٹر ہے۔ اس کا رقبہ کتنے مربع سینٹی میٹر ہے؟"), QB3,
      ("½ × (8 + 12) × 5.", "½ × (8 + 12) × 5"),
      ("Right! 50 cm².", "درست! 50 مربع سینٹی میٹر"), ("20 × 5 = 100, half is 50.", "20 × 5 = 100، آدھا 50"),
      [(100, "You forgot the half: 50.", "آپ آدھا کرنا بھول گئے: 50", "forgets_half")], qtype=None)},
 ],
 review=[
   {"id": "r_tri", "type": "apply", "step": nq("r_tri", ("A triangle has base 9 cm and height 8 cm. What is its area, in cm²?", "ایک مثلث کا قاعدہ 9 سینٹی میٹر اور اونچائی 8 سینٹی میٹر ہے۔ اس کا رقبہ کتنے مربع سینٹی میٹر ہے؟"), R1,
      ("½ × 9 × 8.", "½ × 9 × 8"),
      ("Right! 36 cm².", "درست! 36 مربع سینٹی میٹر"), ("9 × 8 = 72, half is 36.", "9 × 8 = 72، آدھا 36"),
      [(72, "You forgot the half: 36.", "آپ آدھا کرنا بھول گئے: 36", "forgets_half")], qtype=None)},
   {"id": "r_base", "type": "apply", "step": nq("r_base", ("A parallelogram has an area of 70 cm² and a height of 7 cm. What is its base, in cm?", "ایک متوازی الاضلاع کا رقبہ 70 مربع سینٹی میٹر اور اونچائی 7 سینٹی میٹر ہے۔ اس کا قاعدہ کتنے سینٹی میٹر ہے؟"), R2,
      ("Divide the area by the height.", "رقبے کو اونچائی سے تقسیم کریں۔"),
      ("Right! 70 ÷ 7 = 10 cm.", "درست! 70 ÷ 7 = 10 سینٹی میٹر"), ("70 ÷ 7 = 10.", "70 ÷ 7 = 10"),
      [(63, "That takes 7 away. Divide: 10.", "یہ 7 تفریق کرتا ہے۔ تقسیم کریں: 10", "wrong_inverse")], qtype=None)},
 ],
 glossary=[T("Altitude (height)", "ارتفاع (اونچائی)"), T("Base", "قاعدہ"), T("Parallelogram", "متوازی الاضلاع"),
           T("Trapezium", "ذوزنقہ"), T("Triangle", "مثلث"), T("Parallel sides", "متوازی اضلاع"), T("Slanting side", "ترچھا ضلع")],
 flashcards=[
   {"id": "f_formulas", "front": T("Area of a parallelogram, a triangle and a trapezium?", "متوازی الاضلاع، مثلث اور ذوزنقہ کا رقبہ؟"),
    "back": T("Parallelogram: base × height. Triangle: ½ × base × height. Trapezium: ½ × (sum of parallel sides) × height.", "متوازی الاضلاع: قاعدہ × اونچائی۔ مثلث: ½ × قاعدہ × اونچائی۔ ذوزنقہ: ½ × (متوازی اضلاع کا مجموعہ) × اونچائی۔")},
   {"id": "f_height", "front": T("Which line is the height?", "اونچائی کون سی لکیر ہے؟"),
    "back": T("The one that meets the base at a right angle, not the slanting side.", "جو قاعدے سے زاویہ قائمہ پر ملے، ترچھا ضلع نہیں۔")},
 ],
 home_task={"id": "h_cut_paper", "text": T(
   "Draw a rectangle on paper, 10 cm by 6 cm, and cut it out. Draw one diagonal and cut along it. You get two triangles. Find the area of one triangle with ½ × base × height, and check that it is half the rectangle.",
   "کاغذ پر 10 ضرب 6 سینٹی میٹر کی مستطیل بنا کر کاٹ لیں۔ ایک وتر کھینچ کر اس کے ساتھ کاٹیں۔ آپ کو دو مثلث ملیں گے۔ ایک مثلث کا رقبہ ½ × قاعدہ × اونچائی سے نکالیں اور دیکھیں کہ یہ مستطیل کا آدھا ہے۔")},
 notes=["Covers the altitude (q1, q8), the area of a parallelogram (q2, q6, q8), a triangle (q3, q5, q9, q10, q11) and a trapezium (q4, q7, q12), and finding a missing base or height (q5-q7).",
        "Each wrong answer is a real mistake: the slanting side used for the height, the half forgotten, the parallel sides multiplied, and a missing side found by subtracting or multiplying.",
        "Urdu terms to check: ارتفاع (altitude), اونچائی (height), قاعدہ (base), متوازی الاضلاع (parallelogram), ذوزنقہ (trapezium), ترچھا ضلع (slanting side), all from the existing lessons. وتر (diagonal) in the home task is a common Urdu school word but is new to the lessons, so a teacher should confirm it."],
 minutes=17,
)

write(lesson)
