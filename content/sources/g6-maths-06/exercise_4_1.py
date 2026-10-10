"""Practice set for Exercise 4.1 of the book: write and simplify ratios, change
between fractions and ratios, share an amount in a ratio, and join two ratios
into a continued ratio. The questions are new; only the kinds of question
follow the book."""
from math import gcd
from common import (T, say, nq, rq, ch, practice_lesson, practice_intro, write, share, join, simplest,
                    EX_SKILL, RATIO_MEANING, RATIO_EQUIVALENT, RATIO_SHARE, RATIO_CONTINUED)

SKILL = EX_SKILL["4.1"]

# q1: 12 boys to 18 girls
Q1 = simplest(12, 18)
assert Q1 == (2, 3) and simplest(18, 12) == (3, 2) and gcd(12, 18) == 6
# q2: consequent of 5 : 8
Q2 = 8
assert Q2 != 5
# q3: ratio 3 : 7 as a fraction is 3/7 (not 3/10)
assert 3 + 7 == 10
# q4: simplify 36 : 48
Q4 = simplest(36, 48)
assert Q4 == (3, 4) and gcd(36, 48) == 12 and simplest(6, 8) == (3, 4) and (6, 8) != Q4
# q5: 2 m to 50 cm
Q5 = simplest(2 * 100, 50)
assert Q5 == (4, 1) and simplest(2, 50) == (1, 25)
# q6: 3/8 of a book read, so 5/8 not read
Q6 = (3, 8 - 3)
assert Q6 == (3, 5) and (Q6[1], Q6[0]) == (5, 3)
# q7: 5 : 9 = 35 : ?
Q7 = 9 * (35 // 5)
assert 35 % 5 == 0 and Q7 == 63 and 9 + 35 - 5 == 39
# q8: Rs 1,200 in the ratio 3 : 5, larger share
S8 = share(1200, (3, 5))
Q8 = max(S8)
assert S8 == [450, 750] and Q8 == 750 and 1200 // 8 == 150 and 1200 // 5 == 240
# q9: 360 sweets, Ali : Sara = 4 : 5, Ali's share
S9 = share(360, (4, 5))
Q9 = S9[0]
assert S9 == [160, 200] and 360 // 2 == 180
# q10: two brothers, total age 45 years, ratio 4 : 5, older one
S10 = share(45, (4, 5))
Q10 = S10[1]
assert S10 == [20, 25] and Q10 == 25
# q11: A : B = 2 : 3 and B : C = 6 : 7
Q11 = join((2, 3), (6, 7))
assert Q11 == (4, 6, 7) and (2, 6, 7) != Q11
# q12: Rs 2,400 in the ratio 2 : 3 : 5, largest share
S12 = share(2400, (2, 3, 5))
Q12 = max(S12)
assert S12 == [480, 720, 1200] and Q12 == 1200 and 2400 // 3 == 800
# q13 (find error): 12 : 18 divided by 6 and by 3
assert 12 // 6 == 2 and 18 // 3 == 6 and simplest(12, 18) == (2, 3)
assert 2 * 18 != 6 * 12 and 12 * 3 == 18 * 2
# bank and review
QB_REC = simplest(20, 35)
assert QB_REC == (4, 7)
QB_APP = share(280, (3, 4))[1]
assert QB_APP == 160 and 280 // 7 == 40
R_REC = simplest(15, 40)
assert R_REC == (3, 8)
R_APP = share(900, (1, 2))[0]
assert R_APP == 300 and 900 // 2 == 450


def r(a, b):
    return f"{a} : {b}"


lesson = practice_lesson(
 "4.1", script="exercise_4_1.py",
 title=T("Exercise 4.1 practice: ratios", "مشق 4.1 کی پریکٹس: نسبت"),
 outcome="Write a ratio in its simplest form, change between fractions and ratios, find a missing term of an equivalent ratio, share a quantity in a ratio and join two ratios into a continued ratio.",
 prerequisites=[RATIO_MEANING, RATIO_EQUIVALENT, RATIO_SHARE, RATIO_CONTINUED],
 misconceptions=[
   {"id": "order_swapped", "description": "Writes the ratio the wrong way round, putting the second quantity first."},
   {"id": "not_simplest", "description": "Stops before the ratio is in its lowest terms."},
   {"id": "one_term_divided", "description": "Divides only one term of a ratio, or the two terms by different numbers."},
   {"id": "units_mixed", "description": "Compares quantities in different units without changing them to the same unit."},
   {"id": "part_whole", "description": "Treats a ratio of part to part as part to whole (3 : 7 as 3/7 of the total, or 3/8 as 3 : 8)."},
   {"id": "equal_share", "description": "Shares equally whatever the ratio is."},
   {"id": "one_part", "description": "Gives the value of one part instead of the share asked for."},
   {"id": "added_not_scaled", "description": "Adds the same number to both terms instead of multiplying them by the same number."},
 ],
 steps=[
   practice_intro("4.1",
     "Here you write ratios in the simplest form, change fractions into ratios, share money in a ratio and join two ratios into a continued ratio.",
     "اس میں آپ نسبتیں سادہ ترین صورت میں لکھیں گے، کسر کو نسبت میں بدلیں گے، رقم کو نسبت سے تقسیم کریں گے اور دو نسبتوں سے مسلسل نسبت بنائیں گے۔",
     "Exercise 4.1 is about ratios. Ready?", "مشق 4.1 نسبت کے بارے میں ہے۔ تیار؟"),
   rq("q1_simplest", ("A class has 12 boys and 18 girls. Write the ratio of boys to girls in its simplest form (like 2:3).", "ایک جماعت میں 12 لڑکے اور 18 لڑکیاں ہیں۔ لڑکوں اور لڑکیوں کی نسبت سادہ ترین صورت میں لکھیں (جیسے 2:3)۔"), Q1,
      ("Write 12 : 18, then divide both terms by 6.", "12 : 18 لکھیں، پھر دونوں اجزا کو 6 سے تقسیم کریں۔"),
      ("Right! 12 : 18 = 2 : 3.", "درست! 12 : 18 = 2 : 3"),
      ("Boys first: 12 : 18. Divide both by 6 to get 2 : 3.", "پہلے لڑکے: 12 : 18۔ دونوں کو 6 سے تقسیم کریں تو 2 : 3 ملتا ہے۔"),
      [("3:2", "The question asks boys to girls, so boys come first: 2 : 3.", "سوال لڑکوں اور لڑکیوں کی نسبت مانگتا ہے، اس لیے لڑکے پہلے: 2 : 3", "order_swapped"),
       ("12:18", "That is the ratio, but not yet in its simplest form. Divide both terms by 6.", "یہ نسبت ہے مگر ابھی سادہ ترین صورت میں نہیں۔ دونوں اجزا کو 6 سے تقسیم کریں۔", "not_simplest")],
      qtype="recall"),
   nq("q2_consequent", ("In the ratio 5 : 8, which number is the consequent (the second term)?", "نسبت 5 : 8 میں تالی (دوسرا جز) کون سا عدد ہے؟"), Q2,
      ("The antecedent is the first term. The consequent is the other one.", "مقدم پہلا جز ہے۔ تالی دوسرا جز ہے۔"),
      ("Right! In 5 : 8, 5 is the antecedent and 8 is the consequent.", "درست! 5 : 8 میں 5 مقدم اور 8 تالی ہے۔"),
      ("The first term (5) is the antecedent. The second term (8) is the consequent.", "پہلا جز (5) مقدم ہے۔ دوسرا جز (8) تالی ہے۔"),
      [(5, "5 is the first term, the antecedent. The consequent is the second term: 8.", "5 پہلا جز ہے، یعنی مقدم۔ تالی دوسرا جز ہے: 8", "order_swapped")],
      qtype="recall"),
   {"id": "s_rules", "type": "explain",
    "character": say("thinking", "Divide both terms by the same number. A ratio has no units.", "دونوں اجزا کو ایک ہی عدد سے تقسیم کریں۔ نسبت کی کوئی اکائی نہیں ہوتی۔"),
    "text": T("A ratio compares two quantities of the same kind in the same unit: 12 boys to 18 girls is 12 : 18. To simplify it, divide both terms by the same number until no number divides both: 12 : 18 = 2 : 3. To change a fraction of a whole into a ratio, use the part and the rest: if 3/8 is read, 5/8 is not read, so the ratio is 3 : 5. To share in a ratio, add the parts, find the value of one part, and multiply: 3 : 5 has 8 parts. For a continued ratio, make the common quantity the same in both ratios first.",
              "نسبت ایک ہی قسم اور ایک ہی اکائی کی دو مقداروں کا موازنہ ہے: 12 لڑکے اور 18 لڑکیاں یعنی 12 : 18۔ اسے سادہ کرنے کے لیے دونوں اجزا کو ایک ہی عدد سے تقسیم کریں جب تک کوئی عدد دونوں کو تقسیم نہ کر سکے: 12 : 18 = 2 : 3۔ کسی کل کی کسر کو نسبت بنانے کے لیے حصہ اور باقی لیں: اگر 3/8 پڑھا ہے تو 5/8 نہیں پڑھا، اس لیے نسبت 3 : 5 ہے۔ نسبت سے تقسیم کے لیے حصے جمع کریں، ایک حصے کی قیمت نکالیں اور ضرب دیں: 3 : 5 میں 8 حصے ہیں۔ مسلسل نسبت کے لیے پہلے دونوں نسبتوں میں مشترک مقدار کو برابر کریں۔")},
   ch("q3_fraction", ("A ratio is 3 : 7. Which fraction is the ratio written in fraction form?", "نسبت 3 : 7 ہے۔ کسر کی صورت میں یہ نسبت کون سی ہے؟"),
      ("3/7", "3/7", "Yes! The ratio 3 : 7 in fraction form is 3/7.", "جی ہاں! نسبت 3 : 7 کسر کی صورت میں 3/7 ہے۔"),
      [("3/10", "3/10", "3/10 compares 3 with the total of both parts. The fraction form of 3 : 7 is 3/7.", "3/10 میں 3 کا موازنہ کل سے ہے۔ 3 : 7 کی کسری صورت 3/7 ہے۔", "part_whole"),
       ("7/3", "7/3", "That puts the terms the wrong way round.", "اس میں اجزا الٹے ہیں۔", "order_swapped"),
       ("4/7", "4/7", "That subtracts the terms. The fraction form just writes 3 over 7.", "یہ اجزا کو گھٹاتا ہے۔ کسری صورت میں بس 3 کو 7 پر لکھا جاتا ہے۔")],
      3, qtype="recall"),
   rq("q4_simplify", ("Write 36 : 48 in its simplest form.", "36 : 48 کو سادہ ترین صورت میں لکھیں۔"), Q4,
      ("The biggest number that divides 36 and 48 is 12.", "36 اور 48 کو تقسیم کرنے والا سب سے بڑا عدد 12 ہے۔"),
      ("Right! 36 ÷ 12 = 3 and 48 ÷ 12 = 4.", "درست! 36 ÷ 12 = 3 اور 48 ÷ 12 = 4"),
      ("Divide both terms by 12: 3 : 4.", "دونوں اجزا کو 12 سے تقسیم کریں: 3 : 4"),
      [("6:8", "6 : 8 can still be divided by 2. Keep going: 3 : 4.", "6 : 8 کو ابھی 2 سے تقسیم کیا جا سکتا ہے۔ جاری رکھیں: 3 : 4", "not_simplest"),
       ("4:3", "The order stays the same: 36 first, so 3 : 4.", "ترتیب وہی رہتی ہے: 36 پہلے، اس لیے 3 : 4", "order_swapped")]),
   rq("q5_units", ("Find the ratio of 2 metres to 50 centimetres in its simplest form.", "2 میٹر اور 50 سینٹی میٹر کی نسبت سادہ ترین صورت میں معلوم کریں۔"), Q5,
      ("Change 2 m to centimetres first. 1 m = 100 cm.", "پہلے 2 میٹر کو سینٹی میٹر میں بدلیں۔ 1 میٹر = 100 سینٹی میٹر"),
      ("Right! 200 cm : 50 cm = 4 : 1.", "درست! 200 سینٹی میٹر : 50 سینٹی میٹر = 4 : 1"),
      ("2 m = 200 cm, so the ratio is 200 : 50. Divide by 50 to get 4 : 1.", "2 میٹر = 200 سینٹی میٹر، اس لیے نسبت 200 : 50 ہے۔ 50 سے تقسیم کریں تو 4 : 1 ملتا ہے۔")
      , [("1:25", "That compares 2 with 50 in different units. Change both to centimetres: 4 : 1.", "یہ 2 اور 50 کو مختلف اکائیوں میں موازنہ کرتا ہے۔ دونوں کو سینٹی میٹر میں بدلیں: 4 : 1", "units_mixed"),
          ("200:50", "That is right but not yet in its simplest form. Divide by 50: 4 : 1.", "یہ درست ہے مگر ابھی سادہ ترین صورت میں نہیں۔ 50 سے تقسیم کریں: 4 : 1", "not_simplest")]),
   rq("q6_read", ("Aisha has read 3/8 of a story book. Write the ratio of the part she has read to the part she has not read.", "عائشہ نے کہانی کی کتاب کا 3/8 حصہ پڑھ لیا ہے۔ پڑھے ہوئے حصے اور نہ پڑھے ہوئے حصے کی نسبت لکھیں۔"), Q6,
      ("If 3 of 8 equal parts are read, how many of the 8 parts are not read?", "اگر 8 برابر حصوں میں سے 3 پڑھ لیے ہیں تو 8 میں سے کتنے حصے نہیں پڑھے؟"),
      ("Right! 3 parts read and 5 parts not read: 3 : 5.", "درست! 3 حصے پڑھے اور 5 نہیں پڑھے: 3 : 5"),
      ("The book has 8 equal parts: 3 are read and 8 − 3 = 5 are not. The ratio is 3 : 5.", "کتاب کے 8 برابر حصے ہیں: 3 پڑھے ہیں اور 8 − 3 = 5 نہیں پڑھے۔ نسبت 3 : 5 ہے۔"),
      [("3:8", "That compares the part read to the whole book. We need read to not read: 3 : 5.", "یہ پڑھے ہوئے حصے کا پوری کتاب سے موازنہ ہے۔ ہمیں پڑھے اور نہ پڑھے کا چاہیے: 3 : 5", "part_whole"),
       ("5:3", "The question asks read first: 3 : 5.", "سوال میں پڑھا ہوا پہلے ہے: 3 : 5", "order_swapped")]),
   nq("q7_missing", ("Find the missing number: 5 : 9 = 35 : □", "گم شدہ عدد معلوم کریں: 5 : 9 = 35 : □"), Q7,
      ("5 became 35. What did you multiply by? Do the same to 9.", "5 سے 35 بنا۔ آپ نے کس سے ضرب دی؟ 9 کے ساتھ بھی یہی کریں۔"),
      ("Right! 5 × 7 = 35 and 9 × 7 = 63.", "درست! 5 × 7 = 35 اور 9 × 7 = 63"),
      ("Both terms are multiplied by 7: 9 × 7 = 63.", "دونوں اجزا کو 7 سے ضرب دی گئی: 9 × 7 = 63"),
      [(39, "That adds 30 to both terms. A ratio stays the same when you multiply both terms by the same number: 63.", "یہ دونوں اجزا میں 30 جمع کرتا ہے۔ نسبت تب برقرار رہتی ہے جب دونوں کو ایک ہی عدد سے ضرب دیں: 63", "added_not_scaled")]),
   nq("q8_share2", ("Rs 1,200 is shared between two friends in the ratio 3 : 5. How many rupees does the friend with the bigger share get?", "1,200 روپے دو دوستوں میں 3 : 5 کی نسبت سے تقسیم ہوتے ہیں۔ بڑے حصے والے دوست کو کتنے روپے ملتے ہیں؟"), Q8,
      ("3 + 5 = 8 parts. Find one part, then multiply by 5.", "3 + 5 = 8 حصے۔ ایک حصہ نکالیں، پھر 5 سے ضرب دیں۔"),
      ("Right! One part is 150 and 5 × 150 = 750.", "درست! ایک حصہ 150 ہے اور 5 × 150 = 750"),
      ("1200 ÷ 8 = 150 for one part. The bigger share is 5 parts: 750 rupees.", "1200 ÷ 8 = 150 ایک حصہ ہے۔ بڑا حصہ 5 حصے ہیں: 750 روپے۔"),
      [(150, "That is the value of one part. The bigger share has 5 parts: 750.", "یہ ایک حصے کی قیمت ہے۔ بڑے حصے میں 5 حصے ہیں: 750", "one_part"),
       (600, "That shares equally. The ratio is 3 : 5, so the shares are not equal: 750.", "یہ برابر تقسیم ہے۔ نسبت 3 : 5 ہے، اس لیے حصے برابر نہیں: 750", "equal_share")]),
   nq("q9_share_sweets", ("There are 360 sweets to share between Ali and Sara in the ratio 4 : 5. How many sweets does Ali get?", "360 مٹھائیاں علی اور سارہ میں 4 : 5 کی نسبت سے تقسیم کرنی ہیں۔ علی کو کتنی مٹھائیاں ملتی ہیں؟"), Q9,
      ("4 + 5 = 9 parts. Ali has 4 of them.", "4 + 5 = 9 حصے۔ علی کے پاس ان میں سے 4 ہیں۔"),
      ("Right! One part is 40, and 4 × 40 = 160.", "درست! ایک حصہ 40 ہے اور 4 × 40 = 160"),
      ("360 ÷ 9 = 40 for one part. Ali gets 4 parts: 160 sweets.", "360 ÷ 9 = 40 ایک حصہ ہے۔ علی کو 4 حصے ملتے ہیں: 160 مٹھائیاں۔"),
      [(200, "That is Sara's share (5 parts). Ali has 4 parts: 160.", "یہ سارہ کا حصہ ہے (5 حصے)۔ علی کے 4 حصے ہیں: 160", "order_swapped"),
       (180, "That shares equally. The ratio is 4 : 5: 160.", "یہ برابر تقسیم ہے۔ نسبت 4 : 5 ہے: 160", "equal_share")]),
   nq("q10_ages", ("Two brothers' ages add up to 45 years and are in the ratio 4 : 5. How old is the older brother?", "دو بھائیوں کی عمروں کا مجموعہ 45 سال ہے اور ان کی نسبت 4 : 5 ہے۔ بڑے بھائی کی عمر کتنی ہے؟"), Q10,
      ("4 + 5 = 9 parts make 45 years. How much is one part?", "4 + 5 = 9 حصے مل کر 45 سال بنتے ہیں۔ ایک حصہ کتنا ہے؟"),
      ("Right! One part is 5 years, and the older brother has 5 parts: 25 years.", "درست! ایک حصہ 5 سال ہے اور بڑے بھائی کے 5 حصے ہیں: 25 سال"),
      ("45 ÷ 9 = 5 years a part. The older brother has the bigger ratio number: 5 × 5 = 25.", "45 ÷ 9 = 5 سال فی حصہ۔ بڑے بھائی کا نسبتی عدد بڑا ہے: 5 × 5 = 25"),
      [(20, "That is the younger brother (4 parts). The older one has 5 parts: 25.", "یہ چھوٹا بھائی ہے (4 حصے)۔ بڑے کے 5 حصے ہیں: 25", "order_swapped"),
       (5, "That is one part. The older brother has 5 parts: 25.", "یہ ایک حصہ ہے۔ بڑے بھائی کے 5 حصے ہیں: 25", "one_part")]),
   rq("q11_continued", ("Hina : Zoya = 2 : 3 and Zoya : Maria = 6 : 7. Write Hina : Zoya : Maria as a continued ratio (like 2:3:4).", "حنا : زویا = 2 : 3 اور زویا : ماریہ = 6 : 7۔ حنا : زویا : ماریہ مسلسل نسبت کی صورت میں لکھیں (جیسے 2:3:4)۔"), Q11,
      ("Zoya is 3 in the first ratio and 6 in the second. Make both 6 first.", "زویا پہلی نسبت میں 3 اور دوسری میں 6 ہے۔ پہلے دونوں کو 6 بنائیں۔"),
      ("Right! 2 : 3 = 4 : 6, so Hina : Zoya : Maria = 4 : 6 : 7.", "درست! 2 : 3 = 4 : 6، اس لیے حنا : زویا : ماریہ = 4 : 6 : 7"),
      ("Multiply 2 : 3 by 2 to get 4 : 6. Now Zoya is 6 in both, so the continued ratio is 4 : 6 : 7.", "2 : 3 کو 2 سے ضرب دیں تو 4 : 6 ملتا ہے۔ اب زویا دونوں میں 6 ہے، اس لیے مسلسل نسبت 4 : 6 : 7 ہے۔"),
      [("2:6:7", "Zoya must have the same number in both ratios. Change 2 : 3 to 4 : 6 first: 4 : 6 : 7.", "زویا کا عدد دونوں نسبتوں میں ایک جیسا ہونا چاہیے۔ پہلے 2 : 3 کو 4 : 6 بنائیں: 4 : 6 : 7", "one_term_divided")]),
   nq("q12_share3", ("Rs 2,400 is shared among three children in the ratio 2 : 3 : 5. How many rupees does the child with the biggest share get?", "2,400 روپے تین بچوں میں 2 : 3 : 5 کی نسبت سے تقسیم ہوتے ہیں۔ سب سے بڑے حصے والے بچے کو کتنے روپے ملتے ہیں؟"), Q12,
      ("2 + 3 + 5 = 10 parts. The biggest share is 5 parts.", "2 + 3 + 5 = 10 حصے۔ سب سے بڑا حصہ 5 حصے ہیں۔"),
      ("Right! One part is 240 and 5 × 240 = 1200.", "درست! ایک حصہ 240 ہے اور 5 × 240 = 1200"),
      ("2400 ÷ 10 = 240 for one part. The biggest share is 5 parts: 1200 rupees.", "2400 ÷ 10 = 240 ایک حصہ ہے۔ سب سے بڑا حصہ 5 حصے ہیں: 1200 روپے۔"),
      [(800, "That shares equally among three. The ratio is 2 : 3 : 5: 1200.", "یہ تین میں برابر تقسیم ہے۔ نسبت 2 : 3 : 5 ہے: 1200", "equal_share"),
       (240, "That is one part. The biggest share has 5 parts: 1200.", "یہ ایک حصہ ہے۔ سب سے بڑے حصے میں 5 حصے ہیں: 1200", "one_part")]),
   ch("q13_find_error", ("Bilal simplifies 12 : 18 by dividing 12 by 6 and 18 by 3. He gets 2 : 6. What went wrong?", "بلال 12 : 18 کو سادہ کرتا ہے: 12 کو 6 سے اور 18 کو 3 سے تقسیم کرتا ہے۔ اسے 2 : 6 ملتا ہے۔ کیا غلطی ہوئی؟"),
      ("He must divide both terms by the same number. Dividing both by 6 gives 2 : 3.", "اسے دونوں اجزا کو ایک ہی عدد سے تقسیم کرنا چاہیے۔ دونوں کو 6 سے تقسیم کرنے پر 2 : 3 ملتا ہے۔", "Yes! 12 ÷ 6 = 2 and 18 ÷ 6 = 3.", "جی ہاں! 12 ÷ 6 = 2 اور 18 ÷ 6 = 3"),
      [("Nothing. 2 : 6 is the simplest form of 12 : 18.", "کوئی غلطی نہیں۔ 2 : 6، 12 : 18 کی سادہ ترین صورت ہے۔", "2 : 6 is a different ratio. 12 : 18 is 2 to 3, but 2 : 6 is 1 to 3.", "2 : 6 ایک اور نسبت ہے۔ 12 : 18 یعنی 2 : 3، مگر 2 : 6 یعنی 1 : 3", "one_term_divided"),
       ("He should have added 6 to both terms.", "اسے دونوں اجزا میں 6 جمع کرنا چاہیے تھا۔", "Adding changes the ratio. Equivalent ratios come from multiplying or dividing both terms.", "جمع کرنے سے نسبت بدل جاتی ہے۔ ہم نسبتیں دونوں اجزا کو ضرب یا تقسیم دے کر بناتے ہیں۔", "added_not_scaled")],
      0, qtype="find_error"),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! You worked with ratios.", "شاباش! آپ نے نسبتوں پر کام کیا۔"),
    "text": T("Write a ratio in the order asked, in the same unit, and divide both terms by the same number to simplify. A fraction of a whole gives a ratio of the part to the rest. To share in a ratio, add the parts, find one part, then multiply. For a continued ratio, make the common quantity equal first.",
              "نسبت اسی ترتیب سے اور ایک ہی اکائی میں لکھیں، اور سادہ کرنے کے لیے دونوں اجزا کو ایک ہی عدد سے تقسیم کریں۔ کل کی کسر سے حصے اور باقی کی نسبت ملتی ہے۔ نسبت سے تقسیم کے لیے حصے جمع کریں، ایک حصہ نکالیں، پھر ضرب دیں۔ مسلسل نسبت کے لیے پہلے مشترک مقدار کو برابر کریں۔"),
    "points": [T("Check a share: the parts must add up to the total.", "حصے کو جانچیں: حصوں کا مجموعہ کل کے برابر ہونا چاہیے۔"),
               T("A ratio has no unit.", "نسبت کی کوئی اکائی نہیں ہوتی۔")]},
 ],
 bank=[
   {"id": "qb_simplify", "type": "recall", "step": rq("qb_simplify", ("Write 20 : 35 in its simplest form.", "20 : 35 کو سادہ ترین صورت میں لکھیں۔"), QB_REC,
      ("Both 20 and 35 divide by 5.", "20 اور 35 دونوں 5 سے تقسیم ہوتے ہیں۔"),
      ("Right! 4 : 7.", "درست! 4 : 7"), ("20 ÷ 5 = 4 and 35 ÷ 5 = 7: 4 : 7.", "20 ÷ 5 = 4 اور 35 ÷ 5 = 7: 4 : 7"),
      [("7:4", "Keep the order: 20 first, so 4 : 7.", "ترتیب وہی رکھیں: 20 پہلے، اس لیے 4 : 7", "order_swapped")], qtype=None)},
   {"id": "qb_share", "type": "apply", "step": nq("qb_share", ("Divide 280 sweets between two children in the ratio 3 : 4. How many does the second child get?", "280 مٹھائیاں دو بچوں میں 3 : 4 کی نسبت سے تقسیم کریں۔ دوسرے بچے کو کتنی ملتی ہیں؟"), QB_APP,
      ("3 + 4 = 7 parts. The second child has 4 of them.", "3 + 4 = 7 حصے۔ دوسرے بچے کے 4 حصے ہیں۔"),
      ("Right! One part is 40, so 4 × 40 = 160.", "درست! ایک حصہ 40 ہے، اس لیے 4 × 40 = 160"), ("280 ÷ 7 = 40 and 4 × 40 = 160.", "280 ÷ 7 = 40 اور 4 × 40 = 160"),
      [(120, "That is the first child's share (3 parts). The second has 4 parts: 160.", "یہ پہلے بچے کا حصہ ہے (3 حصے)۔ دوسرے کے 4 حصے ہیں: 160", "order_swapped"),
       (140, "That shares equally. The ratio is 3 : 4: 160.", "یہ برابر تقسیم ہے۔ نسبت 3 : 4 ہے: 160", "equal_share")], qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": ch("qb_find_error",
      ("Rani says the ratio 3 : 5 means the first person gets 3/5 of the money. What went wrong?", "رانی کہتی ہے نسبت 3 : 5 کا مطلب ہے پہلے شخص کو رقم کا 3/5 ملتا ہے۔ کیا غلطی ہوئی؟"),
      ("There are 3 + 5 = 8 parts, so the first person gets 3/8 of the money.", "کل 3 + 5 = 8 حصے ہیں، اس لیے پہلے شخص کو رقم کا 3/8 ملتا ہے۔", "Yes! The total is the sum of the parts.", "جی ہاں! کل حصوں کا مجموعہ ہے۔"),
      [("Nothing. 3/5 is right.", "کوئی غلطی نہیں۔ 3/5 درست ہے۔", "5 is only the second person's parts, not the total.", "5 صرف دوسرے شخص کے حصے ہیں، کل نہیں۔", "part_whole"),
       ("It should be 5/3.", "یہ 5/3 ہونا چاہیے۔", "5/3 is more than 1 whole, which cannot be a share.", "5/3 ایک پورے سے زیادہ ہے، یہ حصہ نہیں ہو سکتا۔", "order_swapped")],
      0, qtype=None)},
 ],
 review=[
   {"id": "r_simplify", "type": "recall", "step": rq("r_simplify", ("Write 15 : 40 in its simplest form.", "15 : 40 کو سادہ ترین صورت میں لکھیں۔"), R_REC,
      ("Both 15 and 40 divide by 5.", "15 اور 40 دونوں 5 سے تقسیم ہوتے ہیں۔"),
      ("Right! 3 : 8.", "درست! 3 : 8"), ("15 ÷ 5 = 3 and 40 ÷ 5 = 8.", "15 ÷ 5 = 3 اور 40 ÷ 5 = 8"),
      [("8:3", "Keep the order: 3 : 8.", "ترتیب وہی رکھیں: 3 : 8", "order_swapped")], qtype=None)},
   {"id": "r_share", "type": "apply", "step": nq("r_share", ("Share Rs 900 in the ratio 1 : 2. How much is the smaller share?", "900 روپے 1 : 2 کی نسبت سے تقسیم کریں۔ چھوٹا حصہ کتنا ہے؟"), R_APP,
      ("1 + 2 = 3 parts.", "1 + 2 = 3 حصے۔"),
      ("Right! 900 ÷ 3 = 300.", "درست! 900 ÷ 3 = 300"), ("One part is 300 and the smaller share is 1 part: 300.", "ایک حصہ 300 ہے اور چھوٹا حصہ 1 حصہ ہے: 300"),
      [(450, "That shares equally. The ratio is 1 : 2: 300.", "یہ برابر تقسیم ہے۔ نسبت 1 : 2 ہے: 300", "equal_share")], qtype=None)},
 ],
 glossary=[T("Ratio", "نسبت"), T("Antecedent", "مقدم"), T("Consequent", "تالی"), T("Equivalent ratio", "مساوی نسبت"), T("Continued ratio", "مسلسل نسبت")],
 flashcards=[
   {"id": "f_share", "front": T("How do you share an amount in a ratio?", "رقم کو نسبت سے کیسے تقسیم کرتے ہیں؟"),
    "back": T("Add the parts, divide the amount by the sum to get one part, then multiply by each term.", "حصے جمع کریں، رقم کو مجموعے سے تقسیم کر کے ایک حصہ نکالیں، پھر ہر جز سے ضرب دیں۔")},
   {"id": "f_continued", "front": T("How do you join A : B and B : C?", "A : B اور B : C کو کیسے جوڑتے ہیں؟"),
    "back": T("Make B the same number in both ratios first, then write A : B : C.", "پہلے دونوں نسبتوں میں B کو ایک ہی عدد بنائیں، پھر A : B : C لکھیں۔")},
 ],
 home_task={"id": "h_family", "text": T(
   "Count the boys and girls (or men and women) in your family and your neighbours' families. Write the ratio of boys to girls in its simplest form for each. Which family has the biggest ratio?",
   "اپنے خاندان اور پڑوسیوں کے خاندانوں میں لڑکوں اور لڑکیوں (یا مردوں اور عورتوں) کو گنیں۔ ہر ایک کے لیے لڑکوں اور لڑکیوں کی نسبت سادہ ترین صورت میں لکھیں۔ کس خاندان میں نسبت سب سے بڑی ہے؟")},
 notes=["Covers writing and simplifying a ratio (q1, q4, q5), antecedent and consequent (q2), fraction form and fraction to ratio (q3, q6), a missing term of an equivalent ratio (q7), sharing in a ratio (q8, q9, q10, q12), a continued ratio (q11) and a find-the-error question (q13).",
        "Each wrong answer is a real mistake: the ratio written backwards, an unfinished simplification, units mixed, a part-to-part ratio read as part-to-whole, an equal share, one part instead of a share, and adding instead of multiplying.",
        "Urdu terms to check: مقدم / تالی (antecedent / consequent), مساوی نسبت (equivalent ratio), مسلسل نسبت (continued ratio)."],
 minutes=18,
)

write(lesson)
