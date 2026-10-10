"""Practice set for Exercise 8.3 of the book: surface area and volume of cubes
and cuboids, missing dimensions, tank capacity, the cost of wrapping or
painting, and unit conversions. The questions are new; only the kinds of
question follow the book."""
from common import (T, say, nq, ch, practice_lesson, practice_intro, write, EX_SKILL, CH8_PREREQS,
                    SO_PARTS, SO_VOLUME_CUBOID, SO_VOLUME_CUBE, SO_SURFACE_AREA, SO_WORD_PROBLEMS,
                    cuboid_volume, cuboid_surface)

SKILL = EX_SKILL["8.3"]


def vol(l, b, h):
    return int(cuboid_volume(l, b, h))


def surf(l, b, h):
    return int(cuboid_surface(l, b, h))


# q2: cube of side 7 cm
Q2 = vol(7, 7, 7)
assert Q2 == 343 and 7 * 3 == 21 and 7 * 7 == 49
# q3: cube of side 5 cm, surface area
Q3 = surf(5, 5, 5)
assert Q3 == 150 and vol(5, 5, 5) == 125 and 5 * 5 == 25 and 4 * 25 == 100
# q4: cuboid 9 by 4 by 3, surface area
Q4 = surf(9, 4, 3)
assert Q4 == 150 and 9 * 4 + 4 * 3 + 9 * 3 == 75 and vol(9, 4, 3) == 108
# q5: missing height, V = 240, l = 10, b = 6
Q5 = 240 // (10 * 6)
assert Q5 == 4 and vol(10, 6, Q5) == 240 and 240 - 10 - 6 == 224 and 240 // 10 == 24
# q6: tank 80 cm by 50 cm by 40 cm, litres
Q6_CM3 = vol(80, 50, 40)
Q6 = Q6_CM3 // 1000
assert Q6_CM3 == 160000 and Q6 == 160 and Q6_CM3 // 10000 == 16 and 160000 % 1000 == 0
# q7: closed cube-shaped box of side 2 m painted outside at Rs 25 a m2
Q7_AREA = surf(2, 2, 2)
Q7 = Q7_AREA * 25
assert Q7_AREA == 24 and Q7 == 600 and vol(2, 2, 2) * 25 == 200 and 4 * 25 == 100
# q8: 1 m by 50 cm by 20 cm in cm3
Q8 = vol(100, 50, 20)
assert Q8 == 100000 and vol(1, 50, 20) == 1000 and vol(1, 50, 20) * 100 == 100000
# q9 (find error): cuboid 5 by 3 by 2, surface area is not 30
assert vol(5, 3, 2) == 30 and surf(5, 3, 2) == 62
# q10 (find error): volume unit
assert vol(3, 3, 3) == 27
# q11: 2 cm cubes in a 10 by 6 by 4 box
Q11 = vol(10, 6, 4) // vol(2, 2, 2)
assert Q11 == 30 and vol(10, 6, 4) == 240 and vol(2, 2, 2) == 8 and (10 // 2) * (6 // 2) * (4 // 2) == 30
# q12: open tank (no lid) 6 m by 4 m by 3 m, metal sheet needed
Q12 = surf(6, 4, 3) - 6 * 4
assert Q12 == 84 and surf(6, 4, 3) == 108 and 6 * 4 + 2 * 6 * 3 + 2 * 4 * 3 == 84
# bank and review
QB1 = surf(6, 4, 3)
assert QB1 == 108 and vol(6, 4, 3) == 72
QB2 = vol(10, 5, 4)
assert QB2 == 200 and 10 + 5 + 4 == 19
QB3 = vol(50, 40, 30) // 1000
assert QB3 == 60 and vol(50, 40, 30) == 60000
R1 = surf(4, 4, 4)
assert R1 == 96 and vol(4, 4, 4) == 64
R2 = 360 // (9 * 5)
assert R2 == 8 and vol(9, 5, R2) == 360

lesson = practice_lesson(
 "8.3", script="exercise_8_3.py",
 title=T("Exercise 8.3 practice: cubes and cuboids", "مشق 8.3 کی پریکٹس: مکعب اور مستطیلی ڈبے"),
 outcome="Find the surface area and volume of cubes and cuboids, a missing dimension, the capacity of a tank, the cost of wrapping or painting, and change between units.",
 prerequisites=[SO_PARTS, SO_VOLUME_CUBOID, SO_VOLUME_CUBE, SO_SURFACE_AREA, SO_WORD_PROBLEMS],
 misconceptions=[
   {"id": "volume_for_surface", "description": "Gives the volume when the surface area is asked, or multiplies the three lengths for the surface area."},
   {"id": "half_the_faces", "description": "Adds only three faces (one of each kind) and forgets to double."},
   {"id": "adds_dimensions", "description": "Adds the three lengths instead of multiplying them, or takes the side three times."},
   {"id": "unit_mix", "description": "Gives cm3 as litres or cm2 as cm3, or mixes metres and centimetres."},
   {"id": "cost_uses_volume", "description": "Uses the volume instead of the surface area for the cost of painting or wrapping."},
   {"id": "wrong_inverse", "description": "Subtracts or divides by the wrong thing to find a missing dimension."},
   {"id": "lid_forgotten", "description": "Counts all six faces of a tank that has no lid."},
   {"id": "volume_not_count", "description": "Gives the volume of the big box as the number of small cubes inside it."},
 ],
 steps=[
   practice_intro("8.3",
     "Here you find the surface area and volume of cubes and cuboids, a missing dimension, the capacity of a tank, the cost of painting or wrapping, and change between units.",
     "اس میں آپ مکعب اور مستطیلی ڈبوں کا سطحی رقبہ اور حجم، گمشدہ پیمائش، ٹینکی کی گنجائش، رنگ یا لپیٹنے کی لاگت، اور اکائیوں کی تبدیلی نکالیں گے۔",
     "Exercise 8.3 is about cubes and cuboids. Ready?", "مشق 8.3 مکعب اور مستطیلی ڈبوں کے بارے میں ہے۔ تیار؟"),
   ch("q1_formula", ("Which is the formula for the surface area of a cube of side ℓ?", "ℓ ضلع والے مکعب کے سطحی رقبے کا کلیہ کون سا ہے؟"),
      ("S = 6 × ℓ × ℓ", "S = 6 × ℓ × ℓ", "Yes! A cube has 6 equal square faces, each ℓ × ℓ.", "جی ہاں! مکعب کی 6 برابر مربع سطحیں ہوتی ہیں، ہر ایک ℓ × ℓ۔"),
      [("S = ℓ × ℓ × ℓ", "S = ℓ × ℓ × ℓ", "That is the volume.", "یہ حجم ہے۔", "volume_for_surface"),
       ("S = 4 × ℓ × ℓ", "S = 4 × ℓ × ℓ", "A cube has 6 faces, not 4.", "مکعب کی 6 سطحیں ہوتی ہیں، 4 نہیں۔", "half_the_faces"),
       ("S = 3 × ℓ", "S = 3 × ℓ", "That adds up three edges. Surface area is about faces.", "یہ تین کنارے جمع کرتا ہے۔ سطحی رقبہ سطحوں کے بارے میں ہے۔", "adds_dimensions")],
      0, qtype="recall"),
   nq("q2_volume_cube", ("A cube has a side of 7 cm. What is its volume, in cm³?", "ایک مکعب کا ضلع 7 سینٹی میٹر ہے۔ اس کا حجم کتنے مکعب سینٹی میٹر ہے؟"), Q2,
      ("Volume of a cube = side × side × side.", "مکعب کا حجم = ضلع × ضلع × ضلع"),
      ("Right! 7 × 7 × 7 = 343 cm³.", "درست! 7 × 7 × 7 = 343 مکعب سینٹی میٹر"), ("7 × 7 = 49 and 49 × 7 = 343.", "7 × 7 = 49 اور 49 × 7 = 343"),
      [(21, "That adds the three sides. Multiply them: 343.", "یہ تین اضلاع جمع کرتا ہے۔ انہیں ضرب دیں: 343", "adds_dimensions"),
       (49, "That is one face, 7 × 7. Multiply by 7 once more: 343.", "یہ ایک سطح ہے، 7 × 7۔ ایک بار اور 7 سے ضرب دیں: 343", "adds_dimensions")], qtype="recall"),
   nq("q3_surface_cube", ("A cube has a side of 5 cm. What is its surface area, in cm²?", "ایک مکعب کا ضلع 5 سینٹی میٹر ہے۔ اس کا سطحی رقبہ کتنے مربع سینٹی میٹر ہے؟"), Q3,
      ("One face is 5 × 5. A cube has 6 faces.", "ایک سطح 5 × 5 ہے۔ مکعب کی 6 سطحیں ہوتی ہیں۔"),
      ("Right! 6 × 25 = 150 cm².", "درست! 6 × 25 = 150 مربع سینٹی میٹر"), ("One face is 25 cm², and 6 × 25 = 150.", "ایک سطح 25 مربع سینٹی میٹر ہے، اور 6 × 25 = 150"),
      [(125, "That is the volume, in cm³. Surface area is 6 faces: 150.", "یہ حجم ہے، مکعب سینٹی میٹر میں۔ سطحی رقبہ 6 سطحیں ہے: 150", "volume_for_surface"),
       (25, "That is only one face. Multiply by 6: 150.", "یہ صرف ایک سطح ہے۔ 6 سے ضرب دیں: 150", "half_the_faces"),
       (100, "That counts 4 faces. A cube has 6: 150.", "یہ 4 سطحیں گنتا ہے۔ مکعب کی 6 ہوتی ہیں: 150", "half_the_faces")], qtype="recall"),
   {"id": "s_idea", "type": "explain",
    "character": say("thinking", "Surface area is the outside, in square units. Volume is the space inside, in cubic units.", "سطحی رقبہ باہر کی سطح ہے، مربع اکائیوں میں۔ حجم اندر کی جگہ ہے، مکعب اکائیوں میں۔"),
    "text": T("Cuboid: volume V = ℓ × b × h; surface area S = 2 × (ℓb + bh + hℓ). Cube: V = ℓ × ℓ × ℓ; S = 6 × ℓ × ℓ. Surface area is in cm² or m²; volume is in cm³ or m³. 1 litre = 1000 cm³. Painting or wrapping a box covers its surface, so its cost uses the surface area. Before multiplying, put all the lengths in the same unit. A missing dimension is found by dividing the volume by the other lengths.",
              "مستطیلی ڈبہ: حجم V = ℓ × b × h؛ سطحی رقبہ S = 2 × (ℓb + bh + hℓ)۔ مکعب: V = ℓ × ℓ × ℓ؛ S = 6 × ℓ × ℓ۔ سطحی رقبہ مربع سینٹی میٹر یا مربع میٹر میں ہوتا ہے؛ حجم مکعب سینٹی میٹر یا مکعب میٹر میں۔ 1 لیٹر = 1000 مکعب سینٹی میٹر۔ ڈبے پر رنگ یا کاغذ لپیٹنا اس کی سطح کو ڈھانپتا ہے، اس لیے لاگت سطحی رقبے سے نکلتی ہے۔ ضرب دینے سے پہلے تمام لمبائیاں ایک ہی اکائی میں کریں۔ گمشدہ پیمائش حجم کو باقی لمبائیوں سے تقسیم کر کے ملتی ہے۔")},
   nq("q4_surface_cuboid", ("A cuboid is 9 cm long, 4 cm wide and 3 cm high. What is its surface area, in cm²?", "ایک مستطیلی ڈبہ 9 سینٹی میٹر لمبا، 4 سینٹی میٹر چوڑا اور 3 سینٹی میٹر اونچا ہے۔ اس کا سطحی رقبہ کتنے مربع سینٹی میٹر ہے؟"), Q4,
      ("Add the three different faces: 9×4, 4×3 and 9×3. Then double.", "تین مختلف سطحیں جمع کریں: 9×4، 4×3 اور 9×3۔ پھر دگنا کریں۔"),
      ("Right! 2 × (36 + 12 + 27) = 150 cm².", "درست! 2 × (36 + 12 + 27) = 150 مربع سینٹی میٹر"), ("36 + 12 + 27 = 75, and 2 × 75 = 150.", "36 + 12 + 27 = 75، اور 2 × 75 = 150"),
      [(75, "That is only three faces. A cuboid has 6, in pairs: double it: 150.", "یہ صرف تین سطحیں ہیں۔ مستطیلی ڈبے کی 6 ہوتی ہیں، جوڑوں میں: دگنا کریں: 150", "half_the_faces"),
       (108, "That is the volume, 9 × 4 × 3. Surface area adds the faces: 150.", "یہ حجم ہے، 9 × 4 × 3۔ سطحی رقبہ سطحیں جمع کرتا ہے: 150", "volume_for_surface")]),
   nq("q5_missing", ("A cuboid has a volume of 240 cm³. It is 10 cm long and 6 cm wide. What is its height, in cm?", "ایک مستطیلی ڈبے کا حجم 240 مکعب سینٹی میٹر ہے۔ وہ 10 سینٹی میٹر لمبا اور 6 سینٹی میٹر چوڑا ہے۔ اس کی اونچائی کتنے سینٹی میٹر ہے؟"), Q5,
      ("Volume = ℓ × b × h, so h = volume ÷ (ℓ × b).", "حجم = ℓ × b × h، تو h = حجم ÷ (ℓ × b)"),
      ("Right! 240 ÷ 60 = 4 cm. Check: 10 × 6 × 4 = 240.", "درست! 240 ÷ 60 = 4 سینٹی میٹر۔ جانچ: 10 × 6 × 4 = 240"), ("10 × 6 = 60, and 240 ÷ 60 = 4.", "10 × 6 = 60، اور 240 ÷ 60 = 4"),
      [(24, "That divides by 10 only. Divide by 6 as well: 4.", "یہ صرف 10 سے تقسیم کرتا ہے۔ 6 سے بھی تقسیم کریں: 4", "wrong_inverse"),
       (224, "That takes 10 and 6 away. Undo the multiplying by dividing by 10 × 6 = 60: 4.", "یہ 10 اور 6 تفریق کرتا ہے۔ ضرب کو 10 × 6 = 60 سے تقسیم کر کے ختم کریں: 4", "wrong_inverse")]),
   nq("q6_tank", ("A water tank is 80 cm long, 50 cm wide and 40 cm high. How many litres of water does it hold when full? (1 litre = 1000 cm³)", "پانی کی ایک ٹینکی 80 سینٹی میٹر لمبی، 50 سینٹی میٹر چوڑی اور 40 سینٹی میٹر اونچی ہے۔ بھری ہوئی ہو تو اس میں کتنے لیٹر پانی آتا ہے؟ (1 لیٹر = 1000 مکعب سینٹی میٹر)"), Q6,
      ("Find the volume in cm³ first, then divide by 1000.", "پہلے حجم مکعب سینٹی میٹر میں نکالیں، پھر 1000 سے تقسیم کریں۔"),
      ("Right! 160,000 cm³ ÷ 1000 = 160 litres.", "درست! 160,000 مکعب سینٹی میٹر ÷ 1000 = 160 لیٹر"),
      ("80 × 50 × 40 = 160,000 cm³, and 160,000 ÷ 1000 = 160 litres.", "80 × 50 × 40 = 160,000 مکعب سینٹی میٹر، اور 160,000 ÷ 1000 = 160 لیٹر"),
      [(160000, "That is the volume in cm³. Change to litres by dividing by 1000: 160.", "یہ حجم مکعب سینٹی میٹر میں ہے۔ 1000 سے تقسیم کر کے لیٹر بنائیں: 160", "unit_mix"),
       (16, "That divides by 10,000. 1 litre is 1000 cm³: 160.", "یہ 10,000 سے تقسیم کرتا ہے۔ 1 لیٹر 1000 مکعب سینٹی میٹر ہے: 160", "unit_mix")]),
   nq("q7_paint", ("A closed box in the shape of a cube has a side of 2 m. The outside is painted, and the paint costs Rs 25 for each square metre. What is the cost, in rupees?", "ایک بند ڈبہ مکعب کی شکل کا ہے اور اس کا ضلع 2 میٹر ہے۔ اس کا باہر کا حصہ رنگا جاتا ہے، اور رنگ کی قیمت فی مربع میٹر 25 روپے ہے۔ لاگت کتنے روپے ہے؟"), Q7,
      ("Paint covers the surface. Find the surface area first.", "رنگ سطح کو ڈھانپتا ہے۔ پہلے سطحی رقبہ نکالیں۔"),
      ("Right! Surface area 6 × 4 = 24 m², and 24 × 25 = Rs 600.", "درست! سطحی رقبہ 6 × 4 = 24 مربع میٹر، اور 24 × 25 = 600 روپے"),
      ("One face is 2 × 2 = 4 m², all six 24 m². 24 × 25 = 600.", "ایک سطح 2 × 2 = 4 مربع میٹر، چھ سطحیں 24 مربع میٹر۔ 24 × 25 = 600"),
      [(200, "That uses the volume, 8 m³. Paint covers the outside: 24 m², so Rs 600.", "یہ حجم، 8 مکعب میٹر، استعمال کرتا ہے۔ رنگ باہر کو ڈھانپتا ہے: 24 مربع میٹر، یعنی 600 روپے", "cost_uses_volume"),
       (100, "That paints only one face. All 6 faces: Rs 600.", "یہ صرف ایک سطح رنگتا ہے۔ تمام 6 سطحیں: 600 روپے", "half_the_faces"),
       (24, "24 m² is the area to paint. Multiply by Rs 25: 600.", "24 مربع میٹر رنگنے کا رقبہ ہے۔ 25 روپے سے ضرب دیں: 600", "unit_mix")]),
   nq("q8_units", ("A box is 1 m long, 50 cm wide and 20 cm high. What is its volume, in cm³?", "ایک ڈبہ 1 میٹر لمبا، 50 سینٹی میٹر چوڑا اور 20 سینٹی میٹر اونچا ہے۔ اس کا حجم کتنے مکعب سینٹی میٹر ہے؟"), Q8,
      ("Change 1 m to 100 cm first, so all three are in cm.", "پہلے 1 میٹر کو 100 سینٹی میٹر بنائیں، تاکہ تینوں سینٹی میٹر میں ہوں۔"),
      ("Right! 100 × 50 × 20 = 100,000 cm³.", "درست! 100 × 50 × 20 = 100,000 مکعب سینٹی میٹر"), ("100 × 50 = 5000, and 5000 × 20 = 100,000.", "100 × 50 = 5000، اور 5000 × 20 = 100,000"),
      [(1000, "That multiplies 1 × 50 × 20 and mixes metres with centimetres. Use 100 cm for 1 m: 100,000.", "یہ 1 × 50 × 20 ضرب دیتا ہے اور میٹر کو سینٹی میٹر سے ملاتا ہے۔ 1 میٹر کی جگہ 100 سینٹی میٹر لیں: 100,000", "unit_mix"),
       (170, "That adds 100 + 50 + 20. Multiply: 100,000.", "یہ 100 + 50 + 20 جمع کرتا ہے۔ ضرب دیں: 100,000", "adds_dimensions")]),
   ch("q9_find_error", ("A cuboid is 5 cm by 3 cm by 2 cm. Zoya finds the surface area as 5 × 3 × 2 = 30 cm². What went wrong?", "ایک مستطیلی ڈبہ 5 ضرب 3 ضرب 2 سینٹی میٹر ہے۔ زویا سطحی رقبہ 5 × 3 × 2 = 30 مربع سینٹی میٹر نکالتی ہے۔ کیا غلطی ہوئی؟"),
      ("She found the volume. The surface area is 2 × (15 + 6 + 10) = 62 cm².", "اس نے حجم نکالا۔ سطحی رقبہ 2 × (15 + 6 + 10) = 62 مربع سینٹی میٹر ہے۔", "Yes! 30 is the volume (in cm³). The surface area adds the six faces.", "جی ہاں! 30 حجم ہے (مکعب سینٹی میٹر میں)۔ سطحی رقبہ چھ سطحیں جمع کرتا ہے۔"),
      [("Nothing. 30 cm² is right.", "کوئی غلطی نہیں۔ 30 مربع سینٹی میٹر درست ہے۔", "Multiplying all three lengths gives the volume, not the surface.", "تینوں لمبائیاں ضرب دینے سے حجم ملتا ہے، سطح نہیں۔", "volume_for_surface"),
       ("She should add 5 + 3 + 2 = 10 cm².", "اسے 5 + 3 + 2 = 10 مربع سینٹی میٹر جمع کرنا چاہیے تھا۔", "Adding the lengths gives neither the surface nor the volume.", "لمبائیاں جمع کرنے سے نہ سطحی رقبہ ملتا ہے نہ حجم۔", "adds_dimensions")],
      1, qtype="find_error"),
   ch("q10_find_error_unit", ("Imran says the volume of a cube of side 3 cm is 27 cm². What went wrong?", "عمران کہتا ہے 3 سینٹی میٹر ضلع کے مکعب کا حجم 27 مربع سینٹی میٹر ہے۔ کیا غلطی ہوئی؟"),
      ("The number is right, but volume is in cubic units: 27 cm³.", "عدد درست ہے، مگر حجم مکعب اکائیوں میں ہوتا ہے: 27 مکعب سینٹی میٹر۔", "Yes! cm² is for areas. Volume is cm³.", "جی ہاں! مربع سینٹی میٹر رقبوں کے لیے ہے۔ حجم مکعب سینٹی میٹر میں ہوتا ہے۔"),
      [("The number is wrong. It should be 9.", "عدد غلط ہے۔ یہ 9 ہونا چاہیے۔", "3 × 3 × 3 = 27. 9 is one face.", "3 × 3 × 3 = 27۔ 9 ایک سطح ہے۔", "adds_dimensions"),
       ("Nothing. cm² is right for volume.", "کوئی غلطی نہیں۔ حجم کے لیے مربع سینٹی میٹر درست ہے۔", "Square units measure surfaces; volume needs cubic units.", "مربع اکائیاں سطح ناپتی ہیں؛ حجم کو مکعب اکائیاں چاہئیں۔", "unit_mix")],
      0, qtype="find_error"),
   nq("q11_cubes_in_box", ("A box is 10 cm long, 6 cm wide and 4 cm high. How many small cubes of side 2 cm fit inside it exactly?", "ایک ڈبہ 10 سینٹی میٹر لمبا، 6 سینٹی میٹر چوڑا اور 4 سینٹی میٹر اونچا ہے۔ 2 سینٹی میٹر ضلع کے کتنے چھوٹے مکعب اس میں پوری طرح سما جاتے ہیں؟"), Q11,
      ("Divide the volume of the box by the volume of one small cube.", "ڈبے کے حجم کو ایک چھوٹے مکعب کے حجم سے تقسیم کریں۔"),
      ("Right! 240 ÷ 8 = 30 cubes.", "درست! 240 ÷ 8 = 30 مکعب"), ("Box 240 cm³, one cube 8 cm³, and 240 ÷ 8 = 30.", "ڈبہ 240 مکعب سینٹی میٹر، ایک مکعب 8 مکعب سینٹی میٹر، اور 240 ÷ 8 = 30"),
      [(240, "That is the volume of the box, not the number of cubes. Divide by 8: 30.", "یہ ڈبے کا حجم ہے، مکعبوں کی تعداد نہیں۔ 8 سے تقسیم کریں: 30", "volume_not_count"),
       (120, "That divides by 2, the side. Divide by the cube's volume, 8: 30.", "یہ 2 سے تقسیم کرتا ہے، ضلع سے۔ مکعب کے حجم، 8، سے تقسیم کریں: 30", "volume_not_count")]),
   nq("q12_open_tank", ("A tank with no lid is 6 m long, 4 m wide and 3 m high. How many m² of metal sheet are needed to make it (the bottom and the four sides)?", "ایک ٹینکی بغیر ڈھکن کی ہے جو 6 میٹر لمبی، 4 میٹر چوڑی اور 3 میٹر اونچی ہے۔ اسے بنانے کے لیے کتنے مربع میٹر دھات کی چادر چاہیے (تہہ اور چار اطراف)؟"), Q12,
      ("Find all 6 faces, then take away the lid (6 × 4).", "چھ سطحیں نکالیں، پھر ڈھکن (6 × 4) تفریق کریں۔"),
      ("Right! 108 − 24 = 84 m².", "درست! 108 − 24 = 84 مربع میٹر"), ("The bottom is 24, the long sides 2 × 18 = 36, the short sides 2 × 12 = 24. Total 84 m².", "تہہ 24، لمبے اطراف 2 × 18 = 36، چھوٹے اطراف 2 × 12 = 24۔ کل 84 مربع میٹر"),
      [(108, "That counts the lid too. There is no lid: 84.", "یہ ڈھکن بھی گنتا ہے۔ ڈھکن نہیں ہے: 84", "lid_forgotten"),
       (72, "That is the volume, 6 × 4 × 3. Metal sheet is a surface: 84.", "یہ حجم ہے، 6 × 4 × 3۔ دھات کی چادر سطح ہے: 84", "volume_for_surface")]),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! You can find both surface area and volume.", "شاباش! آپ سطحی رقبہ اور حجم دونوں نکال سکتے ہیں۔"),
    "text": T("Surface area (outside, cm² or m²): cuboid 2 × (ℓb + bh + hℓ), cube 6 × ℓ × ℓ. Volume (inside, cm³ or m³): ℓ × b × h, cube ℓ × ℓ × ℓ. 1 litre = 1000 cm³. Paint and wrapping cost use the surface area; a tank's water uses the volume. Change all lengths to the same unit first. For a missing dimension, divide the volume by the other lengths. For a tank with no lid, take the lid away.",
              "سطحی رقبہ (باہر، مربع سینٹی میٹر یا مربع میٹر): مستطیلی ڈبہ 2 × (ℓb + bh + hℓ)، مکعب 6 × ℓ × ℓ۔ حجم (اندر، مکعب سینٹی میٹر یا مکعب میٹر): ℓ × b × h، مکعب ℓ × ℓ × ℓ۔ 1 لیٹر = 1000 مکعب سینٹی میٹر۔ رنگ اور لپیٹنے کی لاگت سطحی رقبے سے نکلتی ہے؛ ٹینکی کا پانی حجم سے۔ پہلے تمام لمبائیاں ایک ہی اکائی میں کریں۔ گمشدہ پیمائش کے لیے حجم کو باقی لمبائیوں سے تقسیم کریں۔ بغیر ڈھکن کی ٹینکی میں ڈھکن تفریق کریں۔"),
    "points": [T("Outside: surface area, cm². Inside: volume, cm³.", "باہر: سطحی رقبہ، مربع سینٹی میٹر۔ اندر: حجم، مکعب سینٹی میٹر۔"),
               T("Same unit for every length before you multiply.", "ضرب دینے سے پہلے ہر لمبائی ایک ہی اکائی میں کریں۔")]},
 ],
 bank=[
   {"id": "qb_surface", "type": "recall", "step": nq("qb_surface", ("What is the surface area of a cuboid 6 cm by 4 cm by 3 cm, in cm²?", "6 ضرب 4 ضرب 3 سینٹی میٹر مستطیلی ڈبے کا سطحی رقبہ کتنے مربع سینٹی میٹر ہے؟"), QB1,
      ("2 × (6×4 + 4×3 + 6×3).", "2 × (6×4 + 4×3 + 6×3)"),
      ("Right! 2 × 54 = 108 cm².", "درست! 2 × 54 = 108 مربع سینٹی میٹر"), ("24 + 12 + 18 = 54, and 2 × 54 = 108.", "24 + 12 + 18 = 54، اور 2 × 54 = 108"),
      [(54, "That is three faces only. Double it: 108.", "یہ صرف تین سطحیں ہیں۔ دگنا کریں: 108", "half_the_faces"),
       (72, "That is the volume. Surface area: 108.", "یہ حجم ہے۔ سطحی رقبہ: 108", "volume_for_surface")], qtype=None)},
   {"id": "qb_volume", "type": "recall", "step": nq("qb_volume", ("What is the volume of a cuboid 10 cm by 5 cm by 4 cm, in cm³?", "10 ضرب 5 ضرب 4 سینٹی میٹر مستطیلی ڈبے کا حجم کتنے مکعب سینٹی میٹر ہے؟"), QB2,
      ("ℓ × b × h.", "ℓ × b × h"),
      ("Right! 10 × 5 × 4 = 200 cm³.", "درست! 10 × 5 × 4 = 200 مکعب سینٹی میٹر"), ("10 × 5 = 50, 50 × 4 = 200.", "10 × 5 = 50، 50 × 4 = 200"),
      [(19, "That adds the lengths. Multiply: 200.", "یہ لمبائیاں جمع کرتا ہے۔ ضرب دیں: 200", "adds_dimensions")], qtype=None)},
   {"id": "qb_litres", "type": "apply", "step": nq("qb_litres", ("A tank is 50 cm long, 40 cm wide and 30 cm high. How many litres does it hold? (1 litre = 1000 cm³)", "ایک ٹینکی 50 سینٹی میٹر لمبی، 40 سینٹی میٹر چوڑی اور 30 سینٹی میٹر اونچی ہے۔ اس میں کتنے لیٹر آتے ہیں؟ (1 لیٹر = 1000 مکعب سینٹی میٹر)"), QB3,
      ("Volume in cm³, then ÷ 1000.", "حجم مکعب سینٹی میٹر میں، پھر ÷ 1000"),
      ("Right! 60,000 ÷ 1000 = 60 litres.", "درست! 60,000 ÷ 1000 = 60 لیٹر"), ("50 × 40 × 30 = 60,000 cm³, so 60 litres.", "50 × 40 × 30 = 60,000 مکعب سینٹی میٹر، تو 60 لیٹر"),
      [(60000, "That is in cm³. Divide by 1000 for litres: 60.", "یہ مکعب سینٹی میٹر میں ہے۔ لیٹر کے لیے 1000 سے تقسیم کریں: 60", "unit_mix")], qtype=None)},
 ],
 review=[
   {"id": "r_cube_surface", "type": "apply", "step": nq("r_cube_surface", ("What is the surface area of a cube of side 4 cm, in cm²?", "4 سینٹی میٹر ضلع کے مکعب کا سطحی رقبہ کتنے مربع سینٹی میٹر ہے؟"), R1,
      ("6 × 4 × 4.", "6 × 4 × 4"),
      ("Right! 6 × 16 = 96 cm².", "درست! 6 × 16 = 96 مربع سینٹی میٹر"), ("One face 16, six faces 96.", "ایک سطح 16، چھ سطحیں 96"),
      [(64, "That is the volume. Surface area is 96.", "یہ حجم ہے۔ سطحی رقبہ 96 ہے۔", "volume_for_surface")], qtype=None)},
   {"id": "r_height", "type": "apply", "step": nq("r_height", ("A cuboid has a volume of 360 cm³, a length of 9 cm and a width of 5 cm. What is its height, in cm?", "ایک مستطیلی ڈبے کا حجم 360 مکعب سینٹی میٹر، لمبائی 9 سینٹی میٹر اور چوڑائی 5 سینٹی میٹر ہے۔ اس کی اونچائی کتنے سینٹی میٹر ہے؟"), R2,
      ("360 ÷ (9 × 5).", "360 ÷ (9 × 5)"),
      ("Right! 360 ÷ 45 = 8 cm.", "درست! 360 ÷ 45 = 8 سینٹی میٹر"), ("9 × 5 = 45, 360 ÷ 45 = 8.", "9 × 5 = 45، 360 ÷ 45 = 8"),
      [(40, "That divides by 9 only. Divide by 5 as well: 8.", "یہ صرف 9 سے تقسیم کرتا ہے۔ 5 سے بھی تقسیم کریں: 8", "wrong_inverse")], qtype=None)},
 ],
 glossary=[T("Surface area", "سطحی رقبہ"), T("Volume", "حجم"), T("Cube", "مکعب"), T("Cuboid", "مستطیلی ڈبہ"),
           T("Litre", "لیٹر"), T("Cubic centimetre (cm³)", "مکعب سینٹی میٹر"), T("Capacity", "گنجائش")],
 flashcards=[
   {"id": "f_formulas", "front": T("Surface area and volume of a cuboid?", "مستطیلی ڈبے کا سطحی رقبہ اور حجم؟"),
    "back": T("S = 2 × (ℓb + bh + hℓ) in cm²; V = ℓ × b × h in cm³.", "S = 2 × (ℓb + bh + hℓ) مربع سینٹی میٹر میں؛ V = ℓ × b × h مکعب سینٹی میٹر میں۔")},
   {"id": "f_litre", "front": T("How many cm³ is one litre?", "ایک لیٹر کتنے مکعب سینٹی میٹر ہے؟"),
    "back": T("1000 cm³. So divide cm³ by 1000 to get litres.", "1000 مکعب سینٹی میٹر۔ لیٹر کے لیے مکعب سینٹی میٹر کو 1000 سے تقسیم کریں۔")},
 ],
 home_task={"id": "h_box", "text": T(
   "Find a box at home, such as a matchbox or a cereal box. Measure its length, breadth and height in cm. Work out its volume and its surface area, with the right units, and say which one tells you how much paper it needs to be wrapped.",
   "گھر میں کوئی ڈبہ ڈھونڈیں، جیسے ماچس کی ڈبیا یا اناج کا ڈبہ۔ اس کی لمبائی، چوڑائی اور اونچائی سینٹی میٹر میں ناپیں۔ اس کا حجم اور سطحی رقبہ صحیح اکائیوں کے ساتھ نکالیں، اور بتائیں کہ لپیٹنے کے لیے کاغذ کتنا چاہیے یہ کون سا بتاتا ہے۔")},
 notes=["Covers the volume of a cube (q2) and cuboid (q8, q11), surface area of a cube (q3) and cuboid (q4, q9, q12), a missing dimension (q5), the capacity of a tank in litres (q6), the cost of painting (q7) and changing between units (q6, q8, q10).",
        "Each wrong answer is a real mistake: the volume given for the surface area, one or three faces instead of six, lengths added, cm³ given as litres, metres mixed with centimetres, the volume used for the cost of paint, and the lid counted for a tank without one.",
        "Urdu terms to check: سطحی رقبہ (surface area), حجم (volume), مکعب (cube), مستطیلی ڈبہ (cuboid), گنجائش (capacity), لیٹر, مکعب سینٹی میٹر, all from the existing lessons. ڈھکن (lid) is already used in the Solids lessons. دھات کی چادر (metal sheet) is new, so a teacher should confirm it."],
 minutes=18,
)

write(lesson)
