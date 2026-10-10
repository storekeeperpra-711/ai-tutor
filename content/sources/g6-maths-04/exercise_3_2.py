"""Practice set for Exercise 3.2 of the book: multiply and divide integers
by the sign rules, fill in missing integers, verify the commutative,
associative and distributive laws of multiplication, and word problems about
savings and temperature change. The questions are new; only the kinds of
question follow the book."""
from common import (T, say, nq, ch, practice_lesson, practice_intro, write, EX_SKILL,
                    INT_MULTIPLY, INT_LAWS, INT_WORD_PROBLEMS)

SKILL = EX_SKILL["3.2"]

# q1, q2: sign rules
Q1 = -6 * 7
assert Q1 == -42
Q2 = -8 * -5
assert Q2 == 40
# q3, q4: division
Q3 = 48 // -6
assert 48 % 6 == 0 and Q3 == -8 and Q3 * -6 == 48
Q4 = -72 // -9
assert 72 % 9 == 0 and Q4 == 8 and Q4 * -9 == -72
# q5: -7 x [] = 56
Q5 = 56 // -7
assert Q5 == -8 and -7 * Q5 == 56
# q6: [] / 4 = -9
Q6 = -9 * 4
assert Q6 == -36 and Q6 // 4 == -9 and -9 + 4 == -5
# q7: commutative law of multiplication
assert -3 * 8 == 8 * -3 and (-3 * 8) * 2 == -3 * (8 * 2)
assert -3 * (8 + 2) == -3 * 8 + -3 * 2 and -3 * 1 == -3
# q8: associative
Q8_L = (-2 * 5) * -3
Q8_R = -2 * (5 * -3)
assert Q8_L == Q8_R == 30 and -30 != 30
# q9: distributive
Q9 = -4 * (6 + -9)
assert Q9 == 12 and -4 * 6 + -4 * -9 == 12 and -4 * 6 + -9 == -33 and -12 != 12
# q10: division by zero
assert 0 // 5 == 0 and 0 // -5 == 0 and 5 * 0 == 0
try:
    5 // 0
    raise AssertionError("5 / 0 should fail")
except ZeroDivisionError:
    pass
# q11: temperature falls 3 degrees an hour for 5 hours from 4
Q11 = 4 + 5 * -3
assert Q11 == -11 and 5 * -3 == -15 and 4 + 15 == 19
# q12: savings Rs 1000, spends Rs 85 a day for 9 days
Q12 = 1000 + 9 * -85
assert Q12 == 235 and 9 * 85 == 765 and 1000 + 765 == 1765
# q13 (find error): (-12) / (-3)
assert -12 // -3 == 4 and -12 // 3 == -4
# bank and review
QB_REC = -9 * -6
assert QB_REC == 54
QB_APP = -96 // 8
assert -96 % 8 == 0 and QB_APP == -12
assert 6 * (4 + -3) == 6 and 6 * 4 + -3 == 21 and 6 * 4 + 6 * -3 == 6
R_REC = -11 * 4
assert R_REC == -44
R_APP = 7 * -5
assert R_APP == -35 and R_APP // -5 == 7

lesson = practice_lesson(
 "3.2", script="exercise_3_2.py",
 title=T("Exercise 3.2 practice: multiplying and dividing integers", "مشق 3.2 کی پریکٹس: صحیح اعداد کا ضرب اور تقسیم"),
 outcome="Multiply and divide two-digit like and unlike integers, verify the commutative, associative and distributive laws, and solve word problems about integers.",
 prerequisites=[INT_MULTIPLY, INT_LAWS, INT_WORD_PROBLEMS],
 misconceptions=[
   {"id": "neg_neg", "description": "Thinks a negative times a negative is negative, or a negative divided by a negative is negative."},
   {"id": "pos_only", "description": "Thinks the product or quotient is always positive and drops the minus sign."},
   {"id": "blank_sign", "description": "Finds the missing integer's digits but not its sign, or uses the wrong operation to undo."},
   {"id": "distribute_one", "description": "Multiplies only the first term inside the bracket: a × (b + c) = a × b + c."},
   {"id": "zero_division", "description": "Thinks a number divided by zero is 0 or the number itself."},
   {"id": "stops_early", "description": "Finds a middle result but does not finish the problem."},
 ],
 steps=[
   practice_intro("3.2",
     "Here you multiply and divide integers with the sign rules, fill in missing integers, check the laws of multiplication, and solve savings and temperature problems.",
     "اس میں آپ علامتوں کے اصول سے صحیح اعداد کا ضرب اور تقسیم کریں گے، گم شدہ صحیح اعداد بھریں گے، ضرب کے قوانین جانچیں گے، اور بچت اور درجہ حرارت کے سوال حل کریں گے۔",
     "Exercise 3.2 is about multiplying and dividing integers. Ready?",
     "مشق 3.2 صحیح اعداد کے ضرب اور تقسیم کے بارے میں ہے۔ تیار؟"),
   nq("q1_unlike", ("Find (−6) × 7.", "(−6) × 7 معلوم کریں۔"), Q1,
      ("Multiply 6 × 7. Unlike signs give a negative answer.", "6 × 7 کریں۔ مخالف علامتوں کا جواب منفی ہوتا ہے۔"),
      ("Right! 6 × 7 = 42 and the signs differ: −42.", "درست! 6 × 7 = 42 اور علامتیں مختلف ہیں: −42"),
      ("Unlike signs give a negative product: (−6) × 7 = −42.", "مخالف علامتوں کا حاصل ضرب منفی ہوتا ہے: (−6) × 7 = −42"),
      [(42, "One factor is negative and one positive, so the product is negative: −42.", "ایک جز منفی اور ایک مثبت ہے، اس لیے حاصل ضرب منفی ہے: −42", "pos_only")],
      qtype="recall"),
   nq("q2_like", ("Find (−8) × (−5).", "(−8) × (−5) معلوم کریں۔"), Q2,
      ("Like signs (both negative) give a positive answer.", "ایک جیسی علامتوں (دونوں منفی) کا جواب مثبت ہوتا ہے۔"),
      ("Right! 8 × 5 = 40, and two negatives make a positive.", "درست! 8 × 5 = 40، اور دو منفی مل کر مثبت بنتے ہیں۔"),
      ("Like signs give a positive product: (−8) × (−5) = 40.", "ایک جیسی علامتوں کا حاصل ضرب مثبت ہوتا ہے: (−8) × (−5) = 40"),
      [(-40, "Both numbers are negative, so the product is positive: 40.", "دونوں اعداد منفی ہیں، اس لیے حاصل ضرب مثبت ہے: 40", "neg_neg")],
      qtype="recall"),
   {"id": "s_rules", "type": "explain",
    "character": say("thinking", "Same signs give plus. Different signs give minus.", "ایک جیسی علامتیں پلس۔ مختلف علامتیں مائنس۔"),
    "text": T("The sign rules for multiplying and dividing are the same: (+) × (+) = +, (−) × (−) = +, (+) × (−) = −, (−) × (+) = −. So 48 ÷ (−6) = −8 and (−72) ÷ (−9) = 8. Division by 0 has no answer, it is undefined, but 0 divided by any other integer is 0. Multiplication is commutative, a × b = b × a, associative, (a × b) × c = a × (b × c), and distributive over addition, a × (b + c) = a × b + a × c. The distributive law multiplies every term inside the bracket.",
              "ضرب اور تقسیم کے علامتی اصول ایک جیسے ہیں: (+) × (+) = +، (−) × (−) = +، (+) × (−) = −، (−) × (+) = −۔ اس لیے 48 ÷ (−6) = −8 اور (−72) ÷ (−9) = 8۔ صفر سے تقسیم کا کوئی جواب نہیں، یہ غیر معین ہے، مگر 0 کو کسی اور صحیح عدد پر تقسیم کریں تو 0 ملتا ہے۔ ضرب قانون تبدیلی a × b = b × a، قانون شراکت (a × b) × c = a × (b × c)، اور جمع پر قانون تقسیم a × (b + c) = a × b + a × c مانتا ہے۔ قانون تقسیم بریکٹ کے اندر ہر جز کو ضرب دیتا ہے۔")},
   nq("q3_div", ("Find 48 ÷ (−6).", "48 ÷ (−6) معلوم کریں۔"), Q3,
      ("48 ÷ 6 = 8. Are the signs the same or different?", "48 ÷ 6 = 8۔ علامتیں ایک جیسی ہیں یا مختلف؟"),
      ("Right! Unlike signs: −8. Check: (−8) × (−6) = 48.", "درست! مخالف علامتیں: −8۔ جانچ: (−8) × (−6) = 48"),
      ("48 ÷ 6 = 8 and the signs differ, so the answer is −8.", "48 ÷ 6 = 8 اور علامتیں مختلف ہیں، اس لیے جواب −8 ہے۔"),
      [(8, "The divisor is negative, so the quotient is negative: −8.", "مقسوم علیہ منفی ہے، اس لیے خارج قسمت منفی ہے: −8", "pos_only")]),
   nq("q4_div_like", ("Find (−72) ÷ (−9).", "(−72) ÷ (−9) معلوم کریں۔"), Q4,
      ("72 ÷ 9 = 8. Both numbers are negative.", "72 ÷ 9 = 8۔ دونوں اعداد منفی ہیں۔"),
      ("Right! Like signs give a positive quotient: 8.", "درست! ایک جیسی علامتوں کا خارج قسمت مثبت ہے: 8"),
      ("72 ÷ 9 = 8 and both are negative, so the answer is 8.", "72 ÷ 9 = 8 اور دونوں منفی ہیں، اس لیے جواب 8 ہے۔"),
      [(-8, "Dividing a negative by a negative gives a positive: 8.", "منفی کو منفی پر تقسیم کرنے سے مثبت ملتا ہے: 8", "neg_neg")]),
   nq("q5_blank", ("Fill in the blank with an integer: (−7) × □ = 56.", "خالی جگہ میں صحیح عدد لکھیں: (−7) × □ = 56"), Q5,
      ("Divide: 56 ÷ (−7). The product is positive and −7 is negative, so the missing sign is negative.", "تقسیم کریں: 56 ÷ (−7)۔ حاصل ضرب مثبت ہے اور −7 منفی ہے، اس لیے گم شدہ علامت منفی ہے۔"),
      ("Right! (−7) × (−8) = 56.", "درست! (−7) × (−8) = 56"),
      ("56 ÷ (−7) = −8. Check: (−7) × (−8) = 56.", "56 ÷ (−7) = −8۔ جانچ: (−7) × (−8) = 56"),
      [(8, "(−7) × 8 = −56, not 56. The missing integer is −8.", "(−7) × 8 = −56، 56 نہیں۔ گم شدہ صحیح عدد −8 ہے۔", "blank_sign")]),
   nq("q6_blank_div", ("Fill in the blank with an integer: □ ÷ 4 = −9.", "خالی جگہ میں صحیح عدد لکھیں: □ ÷ 4 = −9"), Q6,
      ("To undo dividing by 4, multiply by 4.", "4 سے تقسیم کو ختم کرنے کے لیے 4 سے ضرب دیں۔"),
      ("Right! (−36) ÷ 4 = −9.", "درست! (−36) ÷ 4 = −9"),
      ("□ = (−9) × 4 = −36. Check: (−36) ÷ 4 = −9.", "□ = (−9) × 4 = −36۔ جانچ: (−36) ÷ 4 = −9"),
      [(36, "36 ÷ 4 = 9, not −9. The blank must be negative: −36.", "36 ÷ 4 = 9، −9 نہیں۔ خالی جگہ منفی ہونی چاہیے: −36", "blank_sign"),
       (-5, "That adds −9 and 4. To undo a division, multiply: −36.", "یہ −9 اور 4 کو جمع کرتا ہے۔ تقسیم الٹنے کے لیے ضرب دیں: −36", "blank_sign")]),
   ch("q7_commutative", ("Which equation shows the commutative law of multiplication?", "کون سی مساوات ضرب کا قانون تبدیلی دکھاتی ہے؟"),
      ("(−3) × 8 = 8 × (−3)", "(−3) × 8 = 8 × (−3)", "Yes! Swapping the two numbers gives the same product, −24.", "جی ہاں! دونوں اعداد بدلنے سے وہی حاصل ضرب −24 ملتا ہے۔"),
      [("((−3) × 8) × 2 = (−3) × (8 × 2)", "((−3) × 8) × 2 = (−3) × (8 × 2)", "The order stays and only the grouping changes. That is the associative law.", "ترتیب وہی ہے اور صرف بریکٹ بدلے۔ یہ قانون شراکت ہے۔"),
       ("(−3) × (8 + 2) = (−3) × 8 + (−3) × 2", "(−3) × (8 + 2) = (−3) × 8 + (−3) × 2", "Here the multiplication is spread over an addition. That is the distributive law.", "یہاں ضرب جمع پر پھیلائی گئی ہے۔ یہ قانون تقسیم ہے۔"),
       ("(−3) × 1 = −3", "(−3) × 1 = −3", "Multiplying by 1 changes nothing. That is the multiplicative identity.", "1 سے ضرب دینے سے کچھ نہیں بدلتا۔ یہ ضربی ذاتی عدد ہے۔")],
      0),
   nq("q8_associative", ("Check the associative law for −2, 5 and −3. Work out ((−2) × 5) × (−3). It must equal (−2) × (5 × (−3)). What is the value?", "−2، 5 اور −3 کے لیے قانون شراکت جانچیں۔ ((−2) × 5) × (−3) معلوم کریں۔ یہ (−2) × (5 × (−3)) کے برابر ہونا چاہیے۔ قیمت کیا ہے؟"), Q8_L,
      ("Left side: (−2) × 5 = −10, then (−10) × (−3).", "بایاں طرف: (−2) × 5 = −10، پھر (−10) × (−3)"),
      ("Right! Both sides are 30: (−10) × (−3) = 30 and (−2) × (−15) = 30.", "درست! دونوں طرف 30 ہے: (−10) × (−3) = 30 اور (−2) × (−15) = 30"),
      ("L.H.S. = (−10) × (−3) = 30. R.H.S. = (−2) × (−15) = 30. They are equal.", "L.H.S. = (−10) × (−3) = 30۔ R.H.S. = (−2) × (−15) = 30۔ دونوں برابر ہیں۔"),
      [(-30, "Two negative factors (−10 and −3) give a positive product: 30.", "دو منفی اجزا (−10 اور −3) کا حاصل ضرب مثبت ہے: 30", "neg_neg")]),
   nq("q9_distributive", ("Use the distributive law to find (−4) × (6 + (−9)).", "قانون تقسیم سے (−4) × (6 + (−9)) معلوم کریں۔"), Q9,
      ("(−4) × 6 + (−4) × (−9). Multiply both terms.", "(−4) × 6 + (−4) × (−9)۔ دونوں اجزا کو ضرب دیں۔"),
      ("Right! −24 + 36 = 12.", "درست! −24 + 36 = 12"),
      ("(−4) × 6 = −24 and (−4) × (−9) = 36, so −24 + 36 = 12. Check: 6 + (−9) = −3 and (−4) × (−3) = 12.", "(−4) × 6 = −24 اور (−4) × (−9) = 36، اس لیے −24 + 36 = 12۔ جانچ: 6 + (−9) = −3 اور (−4) × (−3) = 12"),
      [(-33, "That multiplies only 6 by −4. Multiply both terms: −24 + 36 = 12.", "یہ صرف 6 کو −4 سے ضرب دیتا ہے۔ دونوں اجزا کو ضرب دیں: −24 + 36 = 12", "distribute_one"),
       (-12, "(−4) × (−9) is positive 36, so the total is 12.", "(−4) × (−9) مثبت 36 ہے، اس لیے کل 12 ہے۔", "neg_neg")]),
   ch("q10_zero", ("Which of these is undefined (has no answer)?", "ان میں سے کون غیر معین ہے (جواب نہیں رکھتا)؟"),
      ("5 ÷ 0", "5 ÷ 0", "Yes! No number times 0 gives 5, so 5 ÷ 0 is undefined.", "جی ہاں! کوئی عدد 0 سے ضرب ہو کر 5 نہیں دیتا، اس لیے 5 ÷ 0 غیر معین ہے۔"),
      [("0 ÷ 5", "0 ÷ 5", "0 ÷ 5 = 0, because 0 × 5 = 0.", "0 ÷ 5 = 0، کیونکہ 0 × 5 = 0"),
       ("5 × 0", "5 × 0", "5 × 0 = 0. Multiplying by 0 is fine.", "5 × 0 = 0۔ صفر سے ضرب کوئی مسئلہ نہیں۔"),
       ("0 ÷ (−5)", "0 ÷ (−5)", "0 ÷ (−5) = 0. Dividing 0 by any non-zero integer gives 0.", "0 ÷ (−5) = 0۔ 0 کو کسی غیر صفر صحیح عدد پر تقسیم کرنے سے 0 ملتا ہے۔", "zero_division")],
      1),
   nq("q11_temperature", ("At 10 pm the temperature is 4 degrees. It falls 3 degrees every hour for 5 hours. What is the temperature then?", "رات 10 بجے درجہ حرارت 4 ڈگری ہے۔ ہر گھنٹے میں 3 ڈگری گرتا ہے، 5 گھنٹے تک۔ تب درجہ حرارت کیا ہوگا؟"), Q11,
      ("The change is 5 × (−3). Then add it to 4.", "تبدیلی 5 × (−3) ہے۔ پھر اسے 4 میں جمع کریں۔"),
      ("Right! 4 + (−15) = −11 degrees.", "درست! 4 + (−15) = −11 ڈگری"),
      ("The total change is 5 × (−3) = −15, so 4 + (−15) = −11.", "کل تبدیلی 5 × (−3) = −15 ہے، اس لیے 4 + (−15) = −11"),
      [(-15, "That is only the change. The temperature started at 4: 4 + (−15) = −11.", "یہ صرف تبدیلی ہے۔ درجہ حرارت 4 سے شروع ہوا تھا: 4 + (−15) = −11", "stops_early"),
       (19, "A fall is negative, so the change is −15 and not +15: −11.", "گرنا منفی ہے، اس لیے تبدیلی +15 نہیں −15 ہے: −11", "pos_only")]),
   nq("q12_savings", ("Hamza has Rs 1000 saved. He spends Rs 85 every day for 9 days. How many rupees does he have left?", "حمزہ کے پاس 1000 روپے بچت ہے۔ وہ 9 دن تک ہر روز 85 روپے خرچ کرتا ہے۔ اس کے پاس کتنے روپے بچتے ہیں؟"), Q12,
      ("The spending is 9 × 85. Subtract it from 1000 (or add 9 × (−85)).", "خرچ 9 × 85 ہے۔ اسے 1000 میں سے گھٹائیں (یا 9 × (−85) جمع کریں)۔"),
      ("Right! 1000 + 9 × (−85) = 1000 − 765 = 235.", "درست! 1000 + 9 × (−85) = 1000 − 765 = 235"),
      ("9 × 85 = 765 spent, so 1000 − 765 = Rs 235 are left.", "9 × 85 = 765 خرچ ہوئے، اس لیے 1000 − 765 = 235 روپے بچتے ہیں۔"),
      [(765, "That is the amount spent. The money left is 1000 − 765 = 235.", "یہ خرچ کی گئی رقم ہے۔ بچی ہوئی رقم 1000 − 765 = 235 ہے۔", "stops_early"),
       (1765, "Spending takes money away, so subtract: 1000 − 765 = 235.", "خرچ سے رقم کم ہوتی ہے، اس لیے گھٹائیں: 1000 − 765 = 235", "pos_only")]),
   ch("q13_find_error", ("Aiman says (−12) ÷ (−3) = −4, because there are two minus signs and she keeps one. What went wrong?", "ایمن کہتی ہے (−12) ÷ (−3) = −4، کیونکہ دو منفی علامتیں ہیں اور وہ ایک رکھتی ہے۔ کیا غلطی ہوئی؟"),
      ("Like signs give a positive quotient: (−12) ÷ (−3) = 4. Check: 4 × (−3) = −12.", "ایک جیسی علامتوں کا خارج قسمت مثبت ہے: (−12) ÷ (−3) = 4۔ جانچ: 4 × (−3) = −12", "Yes! A negative divided by a negative is positive.", "جی ہاں! منفی کو منفی پر تقسیم کریں تو مثبت ملتا ہے۔"),
      [("Nothing. Her answer is correct.", "کوئی غلطی نہیں۔ اس کا جواب ٹھیک ہے۔", "Check: (−4) × (−3) = 12, not −12. So −4 is wrong.", "جانچ: (−4) × (−3) = 12، −12 نہیں۔ اس لیے −4 غلط ہے۔", "neg_neg"),
       ("The digits are wrong: 12 ÷ 3 = 6.", "ہندسے غلط ہیں: 12 ÷ 3 = 6", "12 ÷ 3 is 4, so the digits are right. Only the sign is wrong.", "12 ÷ 3 تو 4 ہے، اس لیے ہندسے درست ہیں۔ صرف علامت غلط ہے۔")],
      2, qtype="find_error"),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! You multiplied and divided integers.", "شاباش! آپ نے صحیح اعداد کا ضرب اور تقسیم کیا۔"),
    "text": T("Same signs give a positive answer and different signs give a negative answer, for both multiplication and division. Multiplication is commutative, associative and distributive over addition, and in the distributive law every term in the bracket is multiplied. Dividing by 0 is undefined. Check a division by multiplying back.",
              "ضرب اور تقسیم دونوں میں ایک جیسی علامتیں مثبت اور مختلف علامتیں منفی جواب دیتی ہیں۔ ضرب قانون تبدیلی، قانون شراکت اور جمع پر قانون تقسیم مانتا ہے، اور قانون تقسیم میں بریکٹ کے ہر جز کو ضرب دی جاتی ہے۔ صفر سے تقسیم غیر معین ہے۔ تقسیم کو واپس ضرب دے کر جانچیں۔"),
    "points": [T("(−) × (−) = + and (−) ÷ (−) = +.", "(−) × (−) = + اور (−) ÷ (−) = +"),
               T("0 ÷ 5 = 0 but 5 ÷ 0 is undefined.", "0 ÷ 5 = 0 مگر 5 ÷ 0 غیر معین ہے۔")]},
 ],
 bank=[
   {"id": "qb_mul", "type": "recall", "step": nq("qb_mul", ("Find (−9) × (−6).", "(−9) × (−6) معلوم کریں۔"), QB_REC,
      ("Same signs give a positive product.", "ایک جیسی علامتوں کا حاصل ضرب مثبت ہے۔"),
      ("Right! 54.", "درست! 54"), ("9 × 6 = 54 and both are negative: 54.", "9 × 6 = 54 اور دونوں منفی ہیں: 54"),
      [(-54, "Two negatives give a positive: 54.", "دو منفی مل کر مثبت دیتے ہیں: 54", "neg_neg")], qtype=None)},
   {"id": "qb_div", "type": "apply", "step": nq("qb_div", ("Find (−96) ÷ 8.", "(−96) ÷ 8 معلوم کریں۔"), QB_APP,
      ("96 ÷ 8 = 12. Are the signs the same?", "96 ÷ 8 = 12۔ کیا علامتیں ایک جیسی ہیں؟"),
      ("Right! −12.", "درست! −12"), ("96 ÷ 8 = 12 and the signs differ: −12.", "96 ÷ 8 = 12 اور علامتیں مختلف ہیں: −12"),
      [(12, "A negative divided by a positive is negative: −12.", "منفی کو مثبت پر تقسیم کریں تو منفی ملتا ہے: −12", "pos_only")], qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": ch("qb_find_error",
      ("Imran works out 6 × (4 + (−3)) as 6 × 4 + (−3) = 21. What went wrong?", "عمران 6 × (4 + (−3)) کو 6 × 4 + (−3) = 21 لکھ کر حل کرتا ہے۔ کیا غلطی ہوئی؟"),
      ("He multiplied only 4. Both terms must be multiplied: 6 × 4 + 6 × (−3) = 24 − 18 = 6.", "اس نے صرف 4 کو ضرب دی۔ دونوں اجزا کو ضرب دینا ہے: 6 × 4 + 6 × (−3) = 24 − 18 = 6", "Yes! Check: 4 + (−3) = 1 and 6 × 1 = 6.", "جی ہاں! جانچ: 4 + (−3) = 1 اور 6 × 1 = 6"),
      [("Nothing. 21 is correct.", "کوئی غلطی نہیں۔ 21 درست ہے۔", "6 × 1 = 6, so 21 cannot be right.", "6 × 1 = 6، اس لیے 21 درست نہیں ہو سکتا۔", "distribute_one"),
       ("He should have added 6 to the bracket.", "اسے بریکٹ میں 6 جمع کرنا چاہیے تھا۔", "The distributive law multiplies; it does not add.", "قانون تقسیم ضرب دیتا ہے، جمع نہیں کرتا۔")],
      0, qtype=None)},
 ],
 review=[
   {"id": "r_mul", "type": "recall", "step": nq("r_mul", ("Find (−11) × 4.", "(−11) × 4 معلوم کریں۔"), R_REC,
      ("Unlike signs give a negative product.", "مخالف علامتوں کا حاصل ضرب منفی ہے۔"),
      ("Right! −44.", "درست! −44"), ("11 × 4 = 44, unlike signs: −44.", "11 × 4 = 44، مخالف علامتیں: −44"),
      [(44, "One factor is negative, so the product is negative: −44.", "ایک جز منفی ہے، اس لیے حاصل ضرب منفی ہے: −44", "pos_only")], qtype=None)},
   {"id": "r_blank", "type": "apply", "step": nq("r_blank", ("Fill in the blank: □ ÷ (−5) = 7.", "خالی جگہ بھریں: □ ÷ (−5) = 7"), R_APP,
      ("Undo the division: multiply 7 by −5.", "تقسیم الٹیں: 7 کو −5 سے ضرب دیں۔"),
      ("Right! (−35) ÷ (−5) = 7.", "درست! (−35) ÷ (−5) = 7"), ("□ = 7 × (−5) = −35. Check: (−35) ÷ (−5) = 7.", "□ = 7 × (−5) = −35۔ جانچ: (−35) ÷ (−5) = 7"),
      [(35, "35 ÷ (−5) = −7, not 7. The blank is −35.", "35 ÷ (−5) = −7، 7 نہیں۔ خالی جگہ −35 ہے۔", "blank_sign")], qtype=None)},
 ],
 glossary=[T("Product", "حاصل ضرب"), T("Quotient", "خارج قسمت"), T("Distributive law", "قانون تقسیم"), T("Undefined", "غیر معین"), T("Multiplicative identity", "ضربی ذاتی عدد")],
 flashcards=[
   {"id": "f_signs", "front": T("What is (−8) × (−5)?", "(−8) × (−5) کیا ہے؟"),
    "back": T("40. Like signs give a positive product.", "40۔ ایک جیسی علامتوں کا حاصل ضرب مثبت ہوتا ہے۔")},
   {"id": "f_zero", "front": T("What is 5 ÷ 0? And 0 ÷ 5?", "5 ÷ 0 کیا ہے؟ اور 0 ÷ 5؟"),
    "back": T("5 ÷ 0 is undefined. 0 ÷ 5 = 0.", "5 ÷ 0 غیر معین ہے۔ 0 ÷ 5 = 0")},
 ],
 home_task={"id": "h_savings", "text": T(
   "Imagine you spend Rs 40 every day for 6 days from Rs 500. Write the change as 6 × (−40), find the money left, and check it by adding back. Then make up a similar problem about a temperature that falls every hour.",
   "فرض کریں آپ 500 روپے میں سے 6 دن تک ہر روز 40 روپے خرچ کرتے ہیں۔ تبدیلی 6 × (−40) لکھیں، بچی ہوئی رقم معلوم کریں، اور واپس جمع کر کے جانچیں۔ پھر ہر گھنٹے گرتے درجہ حرارت کا ایسا ہی ایک سوال خود بنائیں۔")},
 notes=["Covers the sign rules for multiplication (q1, q2) and division (q3, q4, q13), missing integers (q5, q6), the commutative, associative and distributive laws (q7, q8, q9), division by zero (q10) and savings and temperature word problems (q11, q12).",
        "Each wrong answer is a real mistake: a negative times a negative taken as negative, dropping the minus sign, multiplying only the first term in the distributive law, or stopping before the last step.",
        "Urdu terms to check: حاصل ضرب (product), خارج قسمت (quotient), قانون تقسیم (distributive law), غیر معین (undefined), ضربی ذاتی عدد (multiplicative identity)."],
 minutes=18,
)

write(lesson)
