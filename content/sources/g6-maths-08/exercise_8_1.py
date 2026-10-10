"""Practice set for Exercise 8.1 of the book: perimeter and area of squares and
rectangles, L-shaped (composite) shapes, fencing cost, the area of a path
inside or outside a field, and shaded regions.
The questions are new; only the kinds of question follow the book."""
from common import (T, say, nq, ch, practice_lesson, practice_intro, write, EX_SKILL, CH8_PREREQS,
                    PA_PERIMETER, PA_AREA, PA_COMPOUND, PA_PATH, PA_WORD_PROBLEMS)

SKILL = EX_SKILL["8.1"]


def perim(l, b):
    return 2 * (l + b)


def area(l, b):
    return l * b


# q2: field 15 m by 8 m
Q2 = perim(15, 8)
assert Q2 == 46 and area(15, 8) == 120 and 15 + 8 == 23 and 15 + 8 + 15 == 38
# q3: square tile of side 9 cm
Q3 = area(9, 9)
assert Q3 == 81 and perim(9, 9) == 36 and 9 * 2 == 18
# q4: field 40 m by 25 m, fence at Rs 30 a metre
Q4P = perim(40, 25)
Q4 = Q4P * 30
assert Q4P == 130 and Q4 == 3900 and area(40, 25) * 30 == 30000 and (Q4P // 2) * 30 == 1950
# q5: L-shape = 10 x 4 rectangle plus 5 x 3 rectangle
Q5 = area(10, 4) + area(5, 3)
assert Q5 == 55 and area(10, 4) == 40 and area(10, 4 + 3) == 70 and 10 * 4 + 5 * 3 + 10 + 5 != 0
# q6: garden 14 m by 10 m, path 2 m wide outside
Q6 = area(14 + 2 * 2, 10 + 2 * 2) - area(14, 10)
assert Q6 == 112 and area(18, 14) == 252 and area(14, 10) == 140 and 2 * (14 + 10) * 2 == 96
assert area(16, 12) - area(14, 10) == 52   # path 1 m wide would be wrong here
# q7: hall 20 m by 12 m, path 1 m wide inside
Q7 = area(20, 12) - area(20 - 2, 12 - 2)
assert Q7 == 60 and area(18, 10) == 180 and area(20, 12) == 240 and area(19, 11) == 209
assert area(20, 12) - area(19, 11) == 31
# q8: 16 cm by 9 cm with a square hole of side 4 cm
Q8 = area(16, 9) - area(4, 4)
assert Q8 == 128 and area(16, 9) == 144 and area(16, 9) + area(4, 4) == 160 and area(4, 4) == 16
# q9 (find error): area of 7 by 5 is 35, not 24
assert area(7, 5) == 35 and perim(7, 5) == 24
# q10 (find error): path round a 10 m by 6 m garden, 1 m wide
Q10 = area(10 + 2, 6 + 2) - area(10, 6)
assert Q10 == 36 and area(12, 8) == 96 and area(10, 6) == 60
# q11: missing side, area 84 m2, length 12 m
Q11 = 84 // 12
assert Q11 == 7 and 12 * 7 == 84 and 84 - 12 == 72 and 84 * 12 == 1008
# q12: perimeter of a square is 36 m, find area
Q12_SIDE = 36 // 4
Q12 = area(Q12_SIDE, Q12_SIDE)
assert Q12_SIDE == 9 and Q12 == 81 and 36 * 36 == 1296 and 36 // 2 == 18
# bank and review
QB1 = perim(12, 7)
assert QB1 == 38 and area(12, 7) == 84 and 12 + 7 == 19
QB2 = area(11, 11)
assert QB2 == 121 and perim(11, 11) == 44
QB3 = area(9, 6) + area(4, 5)
assert QB3 == 74 and area(9, 6) == 54 and area(4, 5) == 20 and 9 * 6 + 4 * 5 == 74
R1 = perim(30, 20) * 15
assert R1 == 1500 and perim(30, 20) == 100 and area(30, 20) * 15 == 9000
R2 = area(8, 8) - area(2, 2)
assert R2 == 60 and area(8, 8) == 64

lesson = practice_lesson(
 "8.1", script="exercise_8_1.py",
 title=T("Exercise 8.1 practice: perimeter and area", "مشق 8.1 کی پریکٹس: احاطہ اور رقبہ"),
 outcome="Find the perimeter and area of squares, rectangles and shapes made of rectangles, the cost of fencing, the area of a path inside or outside a field, and shaded regions.",
 prerequisites=[PA_PERIMETER, PA_AREA, PA_COMPOUND, PA_PATH, PA_WORD_PROBLEMS],
 misconceptions=[
   {"id": "perimeter_for_area", "description": "Gives the perimeter when the area is asked, or the other way round."},
   {"id": "adds_sides_only", "description": "Adds length and breadth only once, or two sides, when finding the perimeter."},
   {"id": "wrong_units", "description": "Mixes up cm and cm2, or gives the area of the rectangle as the cost."},
   {"id": "path_forgets_both_sides", "description": "Adds the width of a path once instead of twice to each side of the field (or takes it away once, for a path inside)."},
   {"id": "path_not_subtracted", "description": "Gives the area of the whole shape (field and path) as the area of the path."},
   {"id": "shaded_added", "description": "Adds the hole to the big shape instead of taking it away, or gives only the area of the hole."},
   {"id": "wrong_inverse", "description": "Subtracts or multiplies instead of dividing to find a missing side."},
   {"id": "square_perimeter_slip", "description": "Takes the perimeter of a square as its side, or squares the perimeter."},
 ],
 steps=[
   practice_intro("8.1",
     "Here you find the perimeter and area of squares and rectangles, L-shaped figures, the cost of fencing, the area of a path, and shaded parts.",
     "اس میں آپ مربع اور مستطیل کا احاطہ اور رقبہ، L شکل کے اشکال، باڑ کی لاگت، راستے کا رقبہ اور سایہ دار حصے نکالیں گے۔",
     "Exercise 8.1 is about perimeter and area. Ready?", "مشق 8.1 احاطہ اور رقبہ کے بارے میں ہے۔ تیار؟"),
   ch("q1_formula", ("Which is the formula for the perimeter of a rectangle with length ℓ and breadth b?", "لمبائی ℓ اور چوڑائی b والی مستطیل کے احاطے کا کلیہ کون سا ہے؟"),
      ("P = 2 × (ℓ + b)", "P = 2 × (ℓ + b)", "Yes! Add all four sides: two lengths and two breadths.", "جی ہاں! چاروں اضلاع جمع کریں: دو لمبائیاں اور دو چوڑائیاں۔"),
      [("P = ℓ × b", "P = ℓ × b", "That is the area, in square units.", "یہ رقبہ ہے، مربع اکائیوں میں۔", "perimeter_for_area"),
       ("P = ℓ + b", "P = ℓ + b", "That is only two of the four sides.", "یہ چار میں سے صرف دو اضلاع ہیں۔", "adds_sides_only"),
       ("P = 4 × ℓ", "P = 4 × ℓ", "That is for a square. A rectangle has two different lengths.", "یہ مربع کے لیے ہے۔ مستطیل کی دو مختلف لمبائیاں ہوتی ہیں۔", "adds_sides_only")],
      1, qtype="recall"),
   nq("q2_perimeter", ("A rectangular field is 15 m long and 8 m wide. What is its perimeter, in metres?", "ایک مستطیل کھیت 15 میٹر لمبا اور 8 میٹر چوڑا ہے۔ اس کا احاطہ کتنے میٹر ہے؟"), Q2,
      ("Add all four sides, or double the sum of length and width.", "چاروں اضلاع جمع کریں، یا لمبائی اور چوڑائی کے مجموعے کو دگنا کریں۔"),
      ("Right! 2 × (15 + 8) = 46 m.", "درست! 2 × (15 + 8) = 46 میٹر"), ("2 × (15 + 8) = 2 × 23 = 46 m.", "2 × (15 + 8) = 2 × 23 = 46 میٹر"),
      [(120, "That is the area, 15 × 8. The perimeter adds the sides: 46 m.", "یہ رقبہ ہے، 15 × 8۔ احاطہ اضلاع جمع کرتا ہے: 46 میٹر", "perimeter_for_area"),
       (23, "That is only length plus width. Double it: 46 m.", "یہ صرف لمبائی جمع چوڑائی ہے۔ اسے دگنا کریں: 46 میٹر", "adds_sides_only")], qtype="recall"),
   nq("q3_square", ("A square tile has a side of 9 cm. What is its area, in cm²?", "ایک مربع ٹائل کا ضلع 9 سینٹی میٹر ہے۔ اس کا رقبہ کتنے مربع سینٹی میٹر ہے؟"), Q3,
      ("The area of a square is side × side.", "مربع کا رقبہ ضلع × ضلع ہے۔"),
      ("Right! 9 × 9 = 81 cm².", "درست! 9 × 9 = 81 مربع سینٹی میٹر"), ("9 × 9 = 81 cm².", "9 × 9 = 81 مربع سینٹی میٹر"),
      [(36, "That is the perimeter, 4 × 9. The area is 9 × 9 = 81.", "یہ احاطہ ہے، 4 × 9۔ رقبہ 9 × 9 = 81 ہے۔", "perimeter_for_area"),
       (18, "That is 9 × 2. Multiply the side by itself: 81.", "یہ 9 × 2 ہے۔ ضلع کو اسی سے ضرب دیں: 81", "perimeter_for_area")], qtype="recall"),
   {"id": "s_idea", "type": "explain",
    "character": say("thinking", "Perimeter is the way round. Area is the space inside. Ask which one the question wants!", "احاطہ گرد کا فاصلہ ہے۔ رقبہ اندر کی جگہ ہے۔ دیکھیں سوال کون سا مانگتا ہے!"),
    "text": T("Perimeter is the distance round a shape, in cm or m: for a rectangle 2 × (ℓ + b), for a square 4 × side. Area is the space inside, in cm² or m²: ℓ × b, or side × side for a square. For an L-shape, split it into rectangles and add their areas. For a path round a field, find the area of the field with the path, then take away the field. For a shaded region, take the unshaded part away from the whole. Fencing goes round the edge, so its cost uses the perimeter.",
              "احاطہ کسی شکل کے گرد کا فاصلہ ہے، سینٹی میٹر یا میٹر میں: مستطیل کے لیے 2 × (ℓ + b)، مربع کے لیے 4 × ضلع۔ رقبہ اندر کی جگہ ہے، مربع سینٹی میٹر یا مربع میٹر میں: ℓ × b، یا مربع کے لیے ضلع × ضلع۔ L شکل کو مستطیلوں میں بانٹیں اور ان کے رقبے جمع کریں۔ کھیت کے گرد راستے کے لیے کھیت سمیت راستے کا رقبہ نکالیں، پھر کھیت کا رقبہ تفریق کریں۔ سایہ دار حصے کے لیے پوری شکل میں سے بے سایہ حصہ تفریق کریں۔ باڑ کنارے کے گرد لگتی ہے، اس لیے اس کی لاگت احاطے سے نکلتی ہے۔")},
   nq("q4_fence", ("A field is 40 m long and 25 m wide. A fence goes right round it. The fence costs Rs 30 for each metre. What is the total cost, in rupees?", "ایک کھیت 40 میٹر لمبا اور 25 میٹر چوڑا ہے۔ اس کے چاروں طرف باڑ لگتی ہے۔ باڑ کی قیمت فی میٹر 30 روپے ہے۔ کل لاگت کتنے روپے ہے؟"), Q4,
      ("Find the perimeter first, then multiply by Rs 30.", "پہلے احاطہ نکالیں، پھر 30 روپے سے ضرب دیں۔"),
      ("Right! The perimeter is 130 m, and 130 × 30 = Rs 3,900.", "درست! احاطہ 130 میٹر ہے، اور 130 × 30 = 3,900 روپے"),
      ("2 × (40 + 25) = 130 m. Then 130 × 30 = 3,900.", "2 × (40 + 25) = 130 میٹر۔ پھر 130 × 30 = 3,900"),
      [(30000, "That uses the area, 1000 m². A fence goes round the edge, so use the perimeter: 3,900.", "یہ رقبہ 1000 مربع میٹر استعمال کرتا ہے۔ باڑ کنارے کے گرد لگتی ہے، احاطہ لیں: 3,900", "perimeter_for_area"),
       (1950, "That is half the perimeter. The fence goes right round: 130 m, so 3,900.", "یہ آدھا احاطہ ہے۔ باڑ پورے گرد لگتی ہے: 130 میٹر، یعنی 3,900", "adds_sides_only"),
       (130, "130 m is the length of fence. Multiply by Rs 30 for the cost: 3,900.", "130 میٹر باڑ کی لمبائی ہے۔ لاگت کے لیے 30 روپے سے ضرب دیں: 3,900", "wrong_units")]),
   nq("q5_lshape", ("An L-shaped floor is made of one rectangle 10 m by 4 m and another rectangle 5 m by 3 m joined to it, with no overlap. What is the area of the floor, in m²?", "L شکل کا ایک فرش ایک 10 ضرب 4 میٹر مستطیل اور اس سے جڑی ایک 5 ضرب 3 میٹر مستطیل سے بنا ہے، بغیر ایک دوسرے پر چڑھے۔ فرش کا رقبہ کتنے مربع میٹر ہے؟"), Q5,
      ("Find each rectangle's area, then add them.", "ہر مستطیل کا رقبہ نکالیں، پھر جمع کریں۔"),
      ("Right! 40 + 15 = 55 m².", "درست! 40 + 15 = 55 مربع میٹر"), ("10 × 4 = 40 and 5 × 3 = 15. Together 55 m².", "10 × 4 = 40 اور 5 × 3 = 15۔ دونوں مل کر 55 مربع میٹر"),
      [(40, "That is only the big rectangle. Add the small one, 15: 55.", "یہ صرف بڑی مستطیل ہے۔ چھوٹی بھی جمع کریں، 15: 55", "adds_sides_only"),
       (70, "That treats the L as one 10 by 7 rectangle. The L is not full: 40 + 15 = 55.", "یہ L کو ایک 10 ضرب 7 مستطیل سمجھتا ہے۔ L بھرا ہوا نہیں: 40 + 15 = 55", "adds_sides_only")]),
   nq("q6_path_out", ("A garden is 14 m long and 10 m wide. A path 2 m wide goes all round it, outside the garden. What is the area of the path, in m²?", "ایک باغ 14 میٹر لمبا اور 10 میٹر چوڑا ہے۔ باغ کے باہر اس کے چاروں طرف 2 میٹر چوڑا راستہ ہے۔ راستے کا رقبہ کتنے مربع میٹر ہے؟"), Q6,
      ("The garden with its path is 2 m bigger on each side, so add 4 m to the length and to the width. Then take the garden away.", "راستے سمیت باغ ہر طرف 2 میٹر بڑا ہے، اس لیے لمبائی اور چوڑائی میں 4 میٹر جمع کریں۔ پھر باغ کو تفریق کریں۔"),
      ("Right! 18 × 14 = 252, and 252 − 140 = 112 m².", "درست! 18 × 14 = 252، اور 252 − 140 = 112 مربع میٹر"),
      ("Outer 18 m by 14 m = 252 m². Garden 14 × 10 = 140 m². Path = 112 m².", "باہر کی 18 ضرب 14 میٹر = 252 مربع میٹر۔ باغ 14 × 10 = 140 مربع میٹر۔ راستہ = 112 مربع میٹر"),
      [(252, "That is the garden and the path together. Take the garden, 140, away: 112.", "یہ باغ اور راستہ دونوں ہیں۔ باغ، 140، تفریق کریں: 112", "path_not_subtracted"),
       (96, "That is the perimeter of the garden × 2, not an area. Use outer area − garden area: 112.", "یہ باغ کے احاطے کا 2 گنا ہے، رقبہ نہیں۔ باہر کا رقبہ − باغ کا رقبہ لیں: 112", "path_forgets_both_sides"),
       (52, "That adds only 2 m to the length and to the width. The path is 2 m wide at both ends, so add 4 m: 112.", "یہ لمبائی اور چوڑائی میں صرف 2 میٹر جمع کرتا ہے۔ راستہ دونوں سروں پر 2 میٹر چوڑا ہے، 4 میٹر جمع کریں: 112", "path_forgets_both_sides")]),
   nq("q7_path_in", ("A hall is 20 m long and 12 m wide. A path 1 m wide runs round the inside edge of the floor. What is the area of the path, in m²?", "ایک ہال 20 میٹر لمبا اور 12 میٹر چوڑا ہے۔ فرش کے اندرونی کنارے کے گرد 1 میٹر چوڑا راستہ ہے۔ راستے کا رقبہ کتنے مربع میٹر ہے؟"), Q7,
      ("The part left inside the path is 2 m shorter and 2 m narrower. Find it, then take it from the whole floor.", "راستے کے اندر بچنے والا حصہ 2 میٹر چھوٹا اور 2 میٹر تنگ ہے۔ اسے نکالیں، پھر پورے فرش میں سے تفریق کریں۔"),
      ("Right! 240 − 180 = 60 m².", "درست! 240 − 180 = 60 مربع میٹر"),
      ("Inside 18 m by 10 m = 180 m². Whole floor 20 × 12 = 240 m². Path = 60 m².", "اندر کا حصہ 18 ضرب 10 میٹر = 180 مربع میٹر۔ پورا فرش 20 × 12 = 240 مربع میٹر۔ راستہ = 60 مربع میٹر"),
      [(31, "That takes only 1 m off each of the length and the width. The path is on both sides, so take 2 m: 60.", "یہ لمبائی اور چوڑائی سے صرف 1 میٹر کم کرتا ہے۔ راستہ دونوں طرف ہے، 2 میٹر کم کریں: 60", "path_forgets_both_sides"),
       (180, "180 m² is the part inside the path. The path is 240 − 180 = 60.", "180 مربع میٹر راستے کے اندر کا حصہ ہے۔ راستہ 240 − 180 = 60 ہے۔", "path_not_subtracted")]),
   nq("q8_shaded", ("A rectangular sheet is 16 cm by 9 cm. A square hole of side 4 cm is cut out of it. What is the area of the shaded sheet that is left, in cm²?", "ایک مستطیل چادر 16 ضرب 9 سینٹی میٹر ہے۔ اس میں سے 4 سینٹی میٹر ضلع کا مربع سوراخ کاٹ دیا گیا ہے۔ بچ جانے والی سایہ دار چادر کا رقبہ کتنے مربع سینٹی میٹر ہے؟"), Q8,
      ("Whole sheet area, then take away the hole's area.", "پوری چادر کا رقبہ، پھر سوراخ کا رقبہ تفریق کریں۔"),
      ("Right! 144 − 16 = 128 cm².", "درست! 144 − 16 = 128 مربع سینٹی میٹر"), ("16 × 9 = 144, the hole is 4 × 4 = 16, so 144 − 16 = 128 cm².", "16 × 9 = 144، سوراخ 4 × 4 = 16 ہے، تو 144 − 16 = 128 مربع سینٹی میٹر"),
      [(160, "That adds the hole. A hole is cut out, so take it away: 128.", "یہ سوراخ جمع کرتا ہے۔ سوراخ کاٹا گیا ہے، تفریق کریں: 128", "shaded_added"),
       (16, "16 cm² is the hole itself. The sheet that is left is 144 − 16 = 128.", "16 مربع سینٹی میٹر خود سوراخ ہے۔ بچی ہوئی چادر 144 − 16 = 128 ہے۔", "shaded_added"),
       (144, "That is the sheet before the hole was cut. Take away 16: 128.", "یہ سوراخ کاٹنے سے پہلے کی چادر ہے۔ 16 تفریق کریں: 128", "shaded_added")]),
   ch("q9_find_error", ("Hamza says the area of a 7 cm by 5 cm rectangle is 2 × (7 + 5) = 24 cm². What went wrong?", "حمزہ کہتا ہے 7 ضرب 5 سینٹی میٹر مستطیل کا رقبہ 2 × (7 + 5) = 24 مربع سینٹی میٹر ہے۔ کیا غلطی ہوئی؟"),
      ("He found the perimeter. The area is 7 × 5 = 35 cm².", "اس نے احاطہ نکالا۔ رقبہ 7 × 5 = 35 مربع سینٹی میٹر ہے۔", "Yes! 24 cm is the way round; the area is 35 cm².", "جی ہاں! 24 سینٹی میٹر گرد کا فاصلہ ہے؛ رقبہ 35 مربع سینٹی میٹر ہے۔"),
      [("Nothing. 24 cm² is right.", "کوئی غلطی نہیں۔ 24 مربع سینٹی میٹر درست ہے۔", "2 × (7 + 5) is the perimeter, in cm, not an area.", "2 × (7 + 5) احاطہ ہے، سینٹی میٹر میں، رقبہ نہیں۔", "perimeter_for_area"),
       ("He should have added 7 + 5 = 12.", "اسے 7 + 5 = 12 جمع کرنا چاہیے تھا۔", "Adding the sides gives the perimeter, not the area.", "اضلاع جمع کرنے سے احاطہ ملتا ہے، رقبہ نہیں۔", "perimeter_for_area")],
      0, qtype="find_error"),
   ch("q10_find_error_path", ("A path 1 m wide goes round the outside of a garden 10 m by 6 m. Dania works out 12 × 8 = 96 m² and says that is the area of the path. What went wrong?", "10 ضرب 6 میٹر باغ کے باہر گرد 1 میٹر چوڑا راستہ ہے۔ دانیہ 12 × 8 = 96 مربع میٹر نکالتی ہے اور کہتی ہے کہ یہ راستے کا رقبہ ہے۔ کیا غلطی ہوئی؟"),
      ("96 m² is the garden and path together. Take away the garden, 60 m²: the path is 36 m².", "96 مربع میٹر باغ اور راستہ دونوں ہیں۔ باغ، 60 مربع میٹر، تفریق کریں: راستہ 36 مربع میٹر ہے۔", "Yes! The path is 96 − 60 = 36 m².", "جی ہاں! راستہ 96 − 60 = 36 مربع میٹر ہے۔"),
      [("Nothing. 96 m² is the path.", "کوئی غلطی نہیں۔ 96 مربع میٹر راستہ ہے۔", "12 by 8 includes the garden itself.", "12 ضرب 8 میں خود باغ بھی شامل ہے۔", "path_not_subtracted"),
       ("The outer rectangle should be 11 m by 7 m.", "باہر کی مستطیل 11 ضرب 7 میٹر ہونی چاہیے۔", "A path 1 m wide on both ends adds 2 m to each side: 12 by 8 is right. The mistake is not taking the garden away.", "دونوں سروں پر 1 میٹر کا راستہ ہر ضلع میں 2 میٹر جمع کرتا ہے: 12 ضرب 8 درست ہے۔ غلطی باغ کو تفریق نہ کرنا ہے۔", "path_forgets_both_sides")],
      1, qtype="find_error"),
   nq("q11_missing", ("A rectangular plot has an area of 84 m² and a length of 12 m. How wide is it, in metres?", "ایک مستطیل پلاٹ کا رقبہ 84 مربع میٹر اور لمبائی 12 میٹر ہے۔ اس کی چوڑائی کتنے میٹر ہے؟"), Q11,
      ("Area = length × width, so divide the area by the length.", "رقبہ = لمبائی × چوڑائی، تو رقبے کو لمبائی سے تقسیم کریں۔"),
      ("Right! 84 ÷ 12 = 7 m. Check: 12 × 7 = 84.", "درست! 84 ÷ 12 = 7 میٹر۔ جانچ: 12 × 7 = 84"), ("84 ÷ 12 = 7.", "84 ÷ 12 = 7"),
      [(72, "That takes 12 away. Undo × 12 by dividing by 12: 7.", "یہ 12 تفریق کرتا ہے۔ × 12 کو 12 سے تقسیم کر کے ختم کریں: 7", "wrong_inverse"),
       (1008, "That multiplies. Divide: 7.", "یہ ضرب دیتا ہے۔ تقسیم کریں: 7", "wrong_inverse")]),
   nq("q12_square_perimeter", ("The perimeter of a square field is 36 m. What is its area, in m²?", "ایک مربع کھیت کا احاطہ 36 میٹر ہے۔ اس کا رقبہ کتنے مربع میٹر ہے؟"), Q12,
      ("A square has four equal sides. Find one side first.", "مربع کے چار برابر اضلاع ہوتے ہیں۔ پہلے ایک ضلع نکالیں۔"),
      ("Right! Side = 36 ÷ 4 = 9 m, and area = 9 × 9 = 81 m².", "درست! ضلع = 36 ÷ 4 = 9 میٹر، اور رقبہ = 9 × 9 = 81 مربع میٹر"),
      ("36 ÷ 4 = 9, then 9 × 9 = 81.", "36 ÷ 4 = 9، پھر 9 × 9 = 81"),
      [(1296, "That squares the perimeter. Find the side, 9, first: 9 × 9 = 81.", "یہ احاطے کا مربع ہے۔ پہلے ضلع، 9، نکالیں: 9 × 9 = 81", "square_perimeter_slip"),
       (18, "That is 36 ÷ 2, not a side. Divide by 4 to get the side, 9, then multiply 9 × 9: 81.", "یہ 36 ÷ 2 ہے، ضلع نہیں۔ ضلع کے لیے 4 سے تقسیم کریں، 9، پھر 9 × 9: 81", "square_perimeter_slip"),
       (9, "9 m is the side. The area is 9 × 9 = 81.", "9 میٹر ضلع ہے۔ رقبہ 9 × 9 = 81 ہے۔", "perimeter_for_area")]),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! You can tell perimeter from area.", "شاباش! آپ احاطہ اور رقبہ الگ پہچان سکتے ہیں۔"),
    "text": T("Perimeter goes round the edge (cm, m); area covers the inside (cm², m²). Fencing uses the perimeter. For an L-shape, add the rectangles. For a path, take the field away from the field with the path (add the path width twice to each side for a path outside, take it off twice for a path inside). For a shaded region, take the unshaded part away from the whole.",
              "احاطہ کنارے کے گرد ہوتا ہے (سینٹی میٹر، میٹر)؛ رقبہ اندر کی جگہ ہے (مربع سینٹی میٹر، مربع میٹر)۔ باڑ احاطے سے نکلتی ہے۔ L شکل میں مستطیلیں جمع کریں۔ راستے کے لیے راستے سمیت کھیت میں سے کھیت تفریق کریں (باہر کے راستے میں راستے کی چوڑائی ہر ضلع میں دو بار جمع کریں، اندر کے راستے میں دو بار کم کریں)۔ سایہ دار حصے کے لیے پوری شکل میں سے بے سایہ حصہ تفریق کریں۔"),
    "points": [T("Perimeter: the way round. Area: the space inside.", "احاطہ: گرد کا فاصلہ۔ رقبہ: اندر کی جگہ۔"),
               T("A path is the big shape minus the small shape.", "راستہ بڑی شکل منفی چھوٹی شکل ہے۔")]},
 ],
 bank=[
   {"id": "qb_perimeter", "type": "recall", "step": nq("qb_perimeter", ("What is the perimeter of a rectangle 12 cm long and 7 cm wide, in cm?", "12 سینٹی میٹر لمبی اور 7 سینٹی میٹر چوڑی مستطیل کا احاطہ کتنے سینٹی میٹر ہے؟"), QB1,
      ("2 × (12 + 7).", "2 × (12 + 7)"),
      ("Right! 2 × 19 = 38 cm.", "درست! 2 × 19 = 38 سینٹی میٹر"), ("2 × (12 + 7) = 38.", "2 × (12 + 7) = 38"),
      [(84, "That is the area. The perimeter is 38 cm.", "یہ رقبہ ہے۔ احاطہ 38 سینٹی میٹر ہے۔", "perimeter_for_area"),
       (19, "That is only half. Double it: 38.", "یہ صرف آدھا ہے۔ دگنا کریں: 38", "adds_sides_only")], qtype=None)},
   {"id": "qb_square", "type": "recall", "step": nq("qb_square", ("What is the area of a square of side 11 cm, in cm²?", "11 سینٹی میٹر ضلع کے مربع کا رقبہ کتنے مربع سینٹی میٹر ہے؟"), QB2,
      ("Side × side.", "ضلع × ضلع"),
      ("Right! 11 × 11 = 121 cm².", "درست! 11 × 11 = 121 مربع سینٹی میٹر"), ("11 × 11 = 121.", "11 × 11 = 121"),
      [(44, "That is the perimeter. The area is 121 cm².", "یہ احاطہ ہے۔ رقبہ 121 مربع سینٹی میٹر ہے۔", "perimeter_for_area")], qtype=None)},
   {"id": "qb_composite", "type": "apply", "step": nq("qb_composite", ("A shape is made of a 9 m by 6 m rectangle and a 4 m by 5 m rectangle joined side by side with no overlap. What is its area, in m²?", "ایک شکل 9 ضرب 6 میٹر مستطیل اور 4 ضرب 5 میٹر مستطیل کو بغیر چڑھے جوڑ کر بنی ہے۔ اس کا رقبہ کتنے مربع میٹر ہے؟"), QB3,
      ("Area of each rectangle, then add.", "ہر مستطیل کا رقبہ، پھر جمع۔"),
      ("Right! 54 + 20 = 74 m².", "درست! 54 + 20 = 74 مربع میٹر"), ("9 × 6 = 54, 4 × 5 = 20, total 74.", "9 × 6 = 54، 4 × 5 = 20، کل 74"),
      [(54, "That is only the first rectangle. Add the second, 20: 74.", "یہ صرف پہلی مستطیل ہے۔ دوسری، 20، جمع کریں: 74", "adds_sides_only")], qtype=None)},
 ],
 review=[
   {"id": "r_fence", "type": "apply", "step": nq("r_fence", ("A field is 30 m by 20 m. A fence goes round it at Rs 15 a metre. What is the cost, in rupees?", "ایک کھیت 30 ضرب 20 میٹر ہے۔ اس کے گرد باڑ فی میٹر 15 روپے کے حساب سے لگتی ہے۔ لاگت کتنے روپے ہے؟"), R1,
      ("Perimeter first, then × 15.", "پہلے احاطہ، پھر × 15"),
      ("Right! 100 × 15 = Rs 1,500.", "درست! 100 × 15 = 1,500 روپے"), ("2 × (30 + 20) = 100 m; 100 × 15 = 1,500.", "2 × (30 + 20) = 100 میٹر؛ 100 × 15 = 1,500"),
      [(9000, "That uses the area. A fence goes round the edge: perimeter 100, so 1,500.", "یہ رقبہ استعمال کرتا ہے۔ باڑ کنارے کے گرد لگتی ہے: احاطہ 100، یعنی 1,500", "perimeter_for_area")], qtype=None)},
   {"id": "r_shaded", "type": "apply", "step": nq("r_shaded", ("A square of side 8 cm has a square of side 2 cm cut out. What is the area left, in cm²?", "8 سینٹی میٹر ضلع کے مربع میں سے 2 سینٹی میٹر ضلع کا مربع کاٹ دیا گیا۔ باقی رقبہ کتنے مربع سینٹی میٹر ہے؟"), R2,
      ("64 minus the small square.", "64 منفی چھوٹا مربع"),
      ("Right! 64 − 4 = 60 cm².", "درست! 64 − 4 = 60 مربع سینٹی میٹر"), ("8 × 8 = 64 and 2 × 2 = 4, so 60.", "8 × 8 = 64 اور 2 × 2 = 4، تو 60"),
      [(68, "That adds the piece. It is cut out, so take it away: 60.", "یہ ٹکڑا جمع کرتا ہے۔ وہ کاٹا گیا ہے، تفریق کریں: 60", "shaded_added")], qtype=None)},
 ],
 glossary=[T("Perimeter", "احاطہ"), T("Area", "رقبہ"), T("Path", "راستہ"), T("Compound shape", "مرکب شکل"),
           T("Shaded region", "سایہ دار حصہ"), T("Cost per metre", "فی میٹر قیمت")],
 flashcards=[
   {"id": "f_pa", "front": T("Perimeter or area?", "احاطہ یا رقبہ؟"),
    "back": T("Perimeter is the way round (cm, m). Area is the space inside (cm², m²).", "احاطہ گرد کا فاصلہ ہے (سینٹی میٹر، میٹر)۔ رقبہ اندر کی جگہ ہے (مربع سینٹی میٹر، مربع میٹر)۔")},
   {"id": "f_path", "front": T("How do you find the area of a path round a field?", "کھیت کے گرد راستے کا رقبہ کیسے نکالتے ہیں؟"),
    "back": T("Area of the field with the path, minus the area of the field.", "راستے سمیت کھیت کا رقبہ، منفی کھیت کا رقبہ۔")},
 ],
 home_task={"id": "h_room", "text": T(
   "Measure the length and width of a room at home in metres (a rounded number is fine). Find its perimeter and its area. Then work out the area of a path 1 m wide round the inside of the floor.",
   "گھر کے ایک کمرے کی لمبائی اور چوڑائی میٹر میں ناپیں (گول عدد بھی ٹھیک ہے)۔ اس کا احاطہ اور رقبہ نکالیں۔ پھر فرش کے اندر گرد 1 میٹر چوڑے راستے کا رقبہ نکالیں۔")},
 notes=["Covers perimeter and area of squares and rectangles (q1-q3, q11, q12), the cost of fencing (q4), an L-shape split into rectangles (q5), a path outside and inside a field (q6, q7, q10) and a shaded region (q8).",
        "Each wrong answer is a real mistake: the area given for the perimeter, a path width added once instead of twice, the whole shape given for the path, the hole added instead of taken away, and the area used for the cost of a fence.",
        "Urdu terms to check: احاطہ (perimeter), رقبہ (area), راستہ (path), مرکب شکل (compound shape), سایہ دار (shaded), باڑ (fence), all from the existing lessons. سایہ دار حصہ (shaded region) is new as a glossary entry: it joins the existing words سایہ دار and حصہ, so a teacher should confirm it."],
 minutes=17,
)

write(lesson)
