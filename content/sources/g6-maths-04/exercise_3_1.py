"""Practice set for Exercise 3.1 of the book: add and subtract integers,
verify the commutative and associative laws of addition, find a missing
integer, and word problems about distance. The questions are new; only the
kinds of question follow the book."""
from common import (T, say, wrong, signed, nq, ch, choice_question, practice_lesson, practice_intro,
                    write, EX_SKILL, INT_ADD, INT_SUBTRACT, INT_LAWS, INT_WORD_PROBLEMS)

SKILL = EX_SKILL["3.1"]

# q1: like integers
Q1 = -6 + -5
assert Q1 == -11 and 6 + 5 == 11 and -6 - 5 == -11
# q2: start at 3, move 8 left
Q2 = 3 + -8
assert Q2 == -5 and 8 - 3 == 5 and 3 + 8 == 11
# q3: unlike integers, the bigger absolute value decides the sign
Q3 = 12 + -20
assert Q3 == -8 and abs(-20) > abs(12) and 20 - 12 == 8 and 12 + 20 == 32
# q4: a small number minus a bigger one
Q4 = 5 - 9
assert Q4 == -4 and 9 - 5 == 4 and 5 + 9 == 14
# q5: subtracting a negative
Q5 = 7 - -6
assert Q5 == 13 and 7 - 6 == 1 and -(7 + 6) == -13
# q6
Q6 = -8 - -15
assert Q6 == 7 and -8 - 15 == -23 and 8 - 15 == -7
# q7: commutative law of addition (the statement that is true for every a, b)
A7, B7, C7 = -4, 9, 2
assert A7 + B7 == B7 + A7                              # commutative
assert (A7 + B7) + C7 == A7 + (B7 + C7)               # associative
assert A7 + 0 == A7 and 4 + -4 == 0                    # identity, inverse
# q8: both sides of the associative law
A8, B8, C8 = -3, 8, -6
Q8_L = (A8 + B8) + C8
Q8_R = A8 + (B8 + C8)
assert Q8_L == Q8_R == -1 and A8 + B8 + C8 == -1 and 3 + 8 + 6 == 17
# q9: x + 9 = 4
Q9 = 4 - 9
assert Q9 == -5 and Q9 + 9 == 4 and 4 + 9 == 13
# q10: x - (-4) = -10
Q10 = -10 + -4
assert Q10 == -14 and Q10 - -4 == -10 and -10 + 4 == -6
# q11: fall in temperature from 9 to -12
Q11 = 9 - -12
assert Q11 == 21 and 12 - 9 == 3
# q12: account balance
Q12 = -450 + 1200 - 300
assert Q12 == 450 and 450 + 1200 - 300 == 1350 and -450 + 1200 == 750
# q13 (find error): 4 - 9
assert 4 - 9 == -5 and 9 - 4 == 5 and 4 - 9 != 9 - 4
# bank and review
QB_REC = -7 + -9
assert QB_REC == -16
QB_APP = 15 - 23
assert QB_APP == -8 and 23 - 15 == 8
assert 8 - -3 == 11 and 8 - 3 == 5
R_REC = -12 + -8
assert R_REC == -20
R_APP = -2 - 7
assert R_APP == -9 and -2 + 7 == 5 and 2 + 7 == 9

lesson = practice_lesson(
 "3.1", script="exercise_3_1.py",
 title=T("Exercise 3.1 practice: adding and subtracting integers", "مشق 3.1 کی پریکٹس: صحیح اعداد کا جمع اور تفریق"),
 outcome="Add and subtract two-digit like and unlike integers, verify the commutative and associative laws of addition, and solve word problems about integers.",
 prerequisites=[INT_ADD, INT_SUBTRACT, INT_LAWS, INT_WORD_PROBLEMS],
 misconceptions=[
   {"id": "sign_lost", "description": "Drops the minus sign from an answer, or adds the digits and forgets the sign."},
   {"id": "small_minus_big", "description": "Turns 5 − 9 into 9 − 5, as if subtraction could be done in either order."},
   {"id": "double_neg", "description": "Treats subtracting a negative number as subtracting a positive one."},
   {"id": "unlike_added", "description": "Adds the digits of unlike integers instead of finding the difference."},
   {"id": "wrong_inverse", "description": "Solves x + 9 = 4 or x − (−4) = −10 with the wrong operation or sign."},
   {"id": "stops_early", "description": "Finds a middle result but does not finish the problem."},
 ],
 steps=[
   practice_intro("3.1",
     "Here you add and subtract integers on the number line and without it, check the laws of addition, find a missing integer, and solve distance problems.",
     "اس میں آپ عددی خط پر اور اس کے بغیر صحیح اعداد جمع اور تفریق کریں گے، جمع کے قوانین جانچیں گے، گم شدہ صحیح عدد معلوم کریں گے، اور فاصلے کے سوال حل کریں گے۔",
     "Exercise 3.1 is about adding and subtracting integers. Ready?",
     "مشق 3.1 صحیح اعداد کے جمع اور تفریق کے بارے میں ہے۔ تیار؟"),
   nq("q1_like", ("Find (−6) + (−5).", "(−6) + (−5) معلوم کریں۔"), Q1,
      ("Two negative numbers: add the digits and keep the minus sign.", "دو منفی اعداد: ہندسے جمع کریں اور منفی علامت رکھیں۔"),
      ("Right! 6 + 5 = 11, so the sum is −11.", "درست! 6 + 5 = 11، اس لیے مجموعہ −11 ہے۔"),
      ("Both numbers are negative, so the sum is negative: −11.", "دونوں اعداد منفی ہیں، اس لیے مجموعہ منفی ہے: −11"),
      [(11, "Like negative numbers add up to a negative number: −11.", "ملتے جلتے منفی اعداد کا مجموعہ منفی ہوتا ہے: −11", "sign_lost")],
      qtype="recall"),
   nq("q2_line", ("Start at 3 on the number line and move 8 steps to the left. Which integer do you reach? (This is 3 + (−8).)", "عددی خط پر 3 سے شروع کریں اور 8 قدم بائیں جائیں۔ آپ کس صحیح عدد پر پہنچتے ہیں؟ (یہ 3 + (−8) ہے۔)"), Q2,
      ("3 steps reach 0. How many steps are left?", "3 قدم میں 0 پر پہنچتے ہیں۔ کتنے قدم باقی ہیں؟"),
      ("Right! 3 steps get to 0 and 5 more go past it: −5.", "درست! 3 قدم سے 0 پر اور 5 قدم مزید آگے: −5"),
      ("3 + (−8): 3 steps to 0, then 5 more to the left, so −5.", "3 + (−8): 3 قدم 0 تک، پھر 5 قدم مزید بائیں، اس لیے −5"),
      [(5, "You went past 0, so the answer is negative: −5.", "آپ 0 سے آگے گئے، اس لیے جواب منفی ہے: −5", "sign_lost"),
       (11, "Moving left subtracts. 3 and −8 are unlike, so find the difference, not the sum.", "بائیں جانا گھٹانا ہے۔ 3 اور −8 مخالف علامت کے ہیں، اس لیے مجموعہ نہیں فرق نکالیں۔", "unlike_added")],
      qtype="recall"),
   {"id": "s_rules", "type": "explain",
    "character": say("thinking", "Unlike signs? Subtract the digits and keep the sign of the bigger one.", "مخالف علامتیں؟ ہندسے گھٹائیں اور بڑے ہندسوں والی علامت رکھیں۔"),
    "text": T("Like integers (same signs): add the digits and keep the sign: (−6) + (−5) = −11. Unlike integers (different signs): subtract the smaller digits from the bigger and keep the sign of the integer with the bigger digits: 12 + (−20) = −8. To subtract an integer, add its opposite: 7 − (−6) = 7 + 6 = 13. The commutative law says a + b = b + a. The associative law says (a + b) + c = a + (b + c). Subtraction obeys neither: 4 − 9 is not 9 − 4.",
              "ملتی جلتی علامت والے صحیح اعداد: ہندسے جمع کریں اور علامت وہی رکھیں: (−6) + (−5) = −11۔ مخالف علامت والے صحیح اعداد: چھوٹے ہندسے بڑے ہندسوں سے گھٹائیں اور بڑے ہندسوں والے عدد کی علامت رکھیں: 12 + (−20) = −8۔ کسی صحیح عدد کو گھٹانے کے لیے اس کا مخالف جمع کریں: 7 − (−6) = 7 + 6 = 13۔ تبدیلی کا قانون کہتا ہے a + b = b + a۔ شراکت کا قانون کہتا ہے (a + b) + c = a + (b + c)۔ تفریق ان دونوں کو نہیں مانتی: 4 − 9، 9 − 4 کے برابر نہیں۔")},
   nq("q3_unlike", ("Find 12 + (−20).", "12 + (−20) معلوم کریں۔"), Q3,
      ("Unlike signs: find 20 − 12, then use the sign of the bigger digits.", "مخالف علامتیں: 20 − 12 نکالیں، پھر بڑے ہندسوں والی علامت لگائیں۔"),
      ("Right! 20 − 12 = 8 and 20 is the negative one: −8.", "درست! 20 − 12 = 8 اور 20 منفی ہے: −8"),
      ("20 − 12 = 8, and the bigger digits belong to −20, so the answer is −8.", "20 − 12 = 8، اور بڑے ہندسے −20 کے ہیں، اس لیے جواب −8 ہے۔"),
      [(8, "−20 is farther from 0 than 12, so the answer is negative: −8.", "−20، 12 سے 0 سے زیادہ دور ہے، اس لیے جواب منفی ہے: −8", "sign_lost"),
       (32, "The signs are different, so subtract the digits: 20 − 12 = 8, with a minus sign.", "علامتیں مختلف ہیں، اس لیے ہندسے گھٹائیں: 20 − 12 = 8، منفی علامت کے ساتھ۔", "unlike_added")]),
   nq("q4_small_minus_big", ("Find 5 − 9.", "5 − 9 معلوم کریں۔"), Q4,
      ("Start at 5 and move 9 steps to the left.", "5 سے شروع کریں اور 9 قدم بائیں جائیں۔"),
      ("Right! 5 steps reach 0 and 4 more go past it: −4.", "درست! 5 قدم سے 0 پر اور 4 قدم مزید آگے: −4"),
      ("5 − 9 = 5 + (−9) = −4.", "5 − 9 = 5 + (−9) = −4"),
      [(4, "9 − 5 is 4, but we need 5 − 9. Going 9 steps left from 5 passes 0: −4.", "9 − 5 تو 4 ہے، مگر ہمیں 5 − 9 چاہیے۔ 5 سے 9 قدم بائیں جانا 0 سے آگے لے جاتا ہے: −4", "small_minus_big"),
       (14, "That adds. We subtract: 5 − 9 = −4.", "یہ جمع ہے۔ ہمیں تفریق کرنی ہے: 5 − 9 = −4", "unlike_added")]),
   nq("q5_sub_neg", ("Find 7 − (−6).", "7 − (−6) معلوم کریں۔"), Q5,
      ("Subtracting −6 is the same as adding its opposite, 6.", "−6 کو گھٹانا اس کے مخالف 6 کو جمع کرنے کے برابر ہے۔"),
      ("Right! 7 − (−6) = 7 + 6 = 13.", "درست! 7 − (−6) = 7 + 6 = 13"),
      ("Subtracting a negative number is adding the positive: 7 + 6 = 13.", "منفی عدد کو گھٹانا مثبت جمع کرنا ہے: 7 + 6 = 13"),
      [(1, "That treats it as 7 − 6. Two minus signs together make a plus: 7 + 6 = 13.", "یہ 7 − 6 کی طرح ہے۔ دو منفی علامتیں مل کر جمع بنتی ہیں: 7 + 6 = 13", "double_neg"),
       (-13, "7 + 6 is positive, so the answer is 13.", "7 + 6 مثبت ہے، اس لیے جواب 13 ہے۔", "sign_lost")]),
   nq("q6_sub_neg2", ("Find (−8) − (−15).", "(−8) − (−15) معلوم کریں۔"), Q6,
      ("Change the subtraction to adding the opposite: −8 + 15.", "تفریق کو مخالف کے جمع میں بدلیں: −8 + 15"),
      ("Right! −8 + 15 = 7.", "درست! −8 + 15 = 7"),
      ("(−8) − (−15) = −8 + 15. The bigger digits are positive, so 15 − 8 = 7.", "(−8) − (−15) = −8 + 15۔ بڑے ہندسے مثبت ہیں، اس لیے 15 − 8 = 7"),
      [(-23, "That is (−8) − 15. Subtracting −15 means adding 15: 7.", "یہ (−8) − 15 ہے۔ −15 کو گھٹانے کا مطلب 15 جمع کرنا ہے: 7", "double_neg"),
       (-7, "15 is bigger than 8 and positive, so the answer is positive: 7.", "15، 8 سے بڑا اور مثبت ہے، اس لیے جواب مثبت ہے: 7", "sign_lost")]),
   ch("q7_commutative", ("Which equation shows the commutative law of addition?", "کون سی مساوات جمع کا قانون تبدیلی دکھاتی ہے؟"),
      ("(−4) + 9 = 9 + (−4)", "(−4) + 9 = 9 + (−4)", "Yes! The order of the two numbers is swapped and the sum stays 5.", "جی ہاں! دونوں اعداد کی ترتیب بدلی اور مجموعہ 5 ہی رہا۔"),
      [("((−4) + 9) + 2 = (−4) + (9 + 2)", "((−4) + 9) + 2 = (−4) + (9 + 2)", "Here the numbers stay in order and only the grouping changes. That is the associative law.", "یہاں اعداد کی ترتیب وہی ہے اور صرف بریکٹ بدلے۔ یہ شراکت کا قانون ہے۔"),
       ("(−4) + 0 = −4", "(−4) + 0 = −4", "Adding 0 changes nothing. That is the additive identity, not the commutative law.", "0 جمع کرنے سے کچھ نہیں بدلتا۔ یہ جمعی ذاتی عدد ہے، قانون تبدیلی نہیں۔"),
       ("4 + (−4) = 0", "4 + (−4) = 0", "A number plus its opposite is 0. That is the additive inverse.", "عدد اور اس کے مخالف کا مجموعہ 0 ہوتا ہے۔ یہ جمعی معکوس ہے۔")],
      2),
   nq("q8_associative", ("Check the associative law for −3, 8 and −6. Work out (−3 + 8) + (−6). It must equal −3 + (8 + (−6)). What is the value?", "−3، 8 اور −6 کے لیے شراکت کا قانون جانچیں۔ (−3 + 8) + (−6) معلوم کریں۔ یہ −3 + (8 + (−6)) کے برابر ہونا چاہیے۔ قیمت کیا ہے؟"), Q8_L,
      ("Left side: −3 + 8 = 5, then 5 + (−6). Right side: 8 + (−6) = 2, then −3 + 2.", "بایاں طرف: −3 + 8 = 5، پھر 5 + (−6)۔ دایاں طرف: 8 + (−6) = 2، پھر −3 + 2"),
      ("Right! Both sides are −1, so the law holds.", "درست! دونوں طرف −1 ہے، اس لیے قانون ٹھیک ہے۔"),
      ("L.H.S. = 5 + (−6) = −1 and R.H.S. = −3 + 2 = −1. Both are −1.", "L.H.S. = 5 + (−6) = −1 اور R.H.S. = −3 + 2 = −1۔ دونوں −1 ہیں۔"),
      [(1, "5 + (−6) goes one step past 0, so it is −1, not 1.", "5 + (−6) 0 سے ایک قدم آگے جاتا ہے، اس لیے یہ −1 ہے، 1 نہیں۔", "sign_lost"),
       (-17, "That adds all the digits. The signs differ, so subtract: −1.", "یہ سب ہندسے جمع کرتا ہے۔ علامتیں مختلف ہیں، اس لیے تفریق کریں: −1", "unlike_added")]),
   nq("q9_missing", ("Find the integer x if x + 9 = 4.", "وہ صحیح عدد x معلوم کریں جس کے لیے x + 9 = 4 ہو۔"), Q9,
      ("What must you add to 9 to get 4? Or: x = 4 − 9.", "9 میں کیا جمع کریں تو 4 بنے؟ یا: x = 4 − 9"),
      ("Right! −5 + 9 = 4.", "درست! −5 + 9 = 4"),
      ("x = 4 − 9 = −5. Check: −5 + 9 = 4.", "x = 4 − 9 = −5۔ جانچ: −5 + 9 = 4"),
      [(5, "5 + 9 is 14, not 4. x = 4 − 9 = −5.", "5 + 9 تو 14 ہے، 4 نہیں۔ x = 4 − 9 = −5", "wrong_inverse"),
       (13, "That adds 4 and 9. To undo + 9 we subtract 9: −5.", "یہ 4 اور 9 کو جمع کرتا ہے۔ + 9 کو ختم کرنے کے لیے 9 گھٹائیں: −5", "wrong_inverse")]),
   nq("q10_missing_sub", ("Find the integer x if x − (−4) = −10.", "وہ صحیح عدد x معلوم کریں جس کے لیے x − (−4) = −10 ہو۔"), Q10,
      ("x − (−4) is x + 4. So x + 4 = −10.", "x − (−4) دراصل x + 4 ہے۔ اس لیے x + 4 = −10"),
      ("Right! −14 − (−4) = −14 + 4 = −10.", "درست! −14 − (−4) = −14 + 4 = −10"),
      ("x + 4 = −10, so x = −10 − 4 = −14.", "x + 4 = −10، اس لیے x = −10 − 4 = −14"),
      [(-6, "That is −10 + 4. To undo + 4 we subtract 4: −14.", "یہ −10 + 4 ہے۔ + 4 کو ختم کرنے کے لیے 4 گھٹائیں: −14", "wrong_inverse"),
       (14, "Check: 14 − (−4) = 18, not −10. The answer is −14.", "جانچ: 14 − (−4) = 18، −10 نہیں۔ جواب −14 ہے۔", "sign_lost")]),
   nq("q11_fall", ("At noon the temperature is 9 degrees. At midnight it is −12 degrees. By how many degrees did it fall?", "دوپہر کو درجہ حرارت 9 ڈگری ہے۔ آدھی رات کو −12 ڈگری ہے۔ درجہ حرارت کتنے ڈگری گرا؟"), Q11,
      ("Fall = noon − midnight = 9 − (−12). Or count 9 steps down to 0, then 12 more.", "گرنا = دوپہر − آدھی رات = 9 − (−12)۔ یا 0 تک 9 قدم نیچے، پھر 12 مزید گنیں۔"),
      ("Right! 9 + 12 = 21 degrees.", "درست! 9 + 12 = 21 ڈگری"),
      ("The numbers are on opposite sides of 0: 9 steps to 0 and 12 more, so 21 degrees.", "اعداد 0 کی مخالف طرف ہیں: 0 تک 9 قدم اور 12 مزید، اس لیے 21 ڈگری۔"),
      [(3, "That is 12 − 9. The temperatures are on different sides of 0, so add: 21.", "یہ 12 − 9 ہے۔ درجہ حرارت 0 کی مختلف طرف ہیں، اس لیے جمع کریں: 21", "unlike_added"),
       (-21, "A fall of 21 degrees is a distance, so the number of degrees is 21.", "21 ڈگری کا گرنا فاصلہ ہے، اس لیے ڈگریوں کی تعداد 21 ہے۔", "sign_lost")]),
   nq("q12_account", ("Imran's shop account shows −450 rupees (he owes Rs 450). He deposits Rs 1200 and then withdraws Rs 300. What is the balance in rupees?", "عمران کی دکان کے کھاتے میں −450 روپے ہیں (اس پر 450 روپے واجب ہیں)۔ وہ 1200 روپے جمع کرواتا ہے اور پھر 300 روپے نکلواتا ہے۔ بیلنس کتنے روپے ہے؟"), Q12,
      ("−450 + 1200 first, then take away 300.", "پہلے −450 + 1200، پھر 300 گھٹائیں۔"),
      ("Right! −450 + 1200 = 750, and 750 − 300 = 450.", "درست! −450 + 1200 = 750، اور 750 − 300 = 450"),
      ("−450 + 1200 = 750, then 750 − 300 = 450 rupees.", "−450 + 1200 = 750، پھر 750 − 300 = 450 روپے۔"),
      [(750, "That stops after the deposit. Take away the Rs 300 withdrawal too: 450.", "یہ جمع کے بعد رک گیا۔ 300 روپے نکلوانا بھی گھٹائیں: 450", "stops_early"),
       (1350, "That ignores the minus sign on 450. He owed that money, so subtract it: 450.", "یہ 450 کی منفی علامت نظر انداز کرتا ہے۔ یہ رقم واجب تھی، اس لیے اسے گھٹائیں: 450", "sign_lost")]),
   ch("q13_find_error", ("Hira works out 4 − 9 and writes 5, because 9 − 4 = 5. What went wrong?", "ہیرا 4 − 9 معلوم کرتی ہے اور 5 لکھتی ہے، کیونکہ 9 − 4 = 5۔ کیا غلطی ہوئی؟"),
      ("Subtraction cannot be swapped. 4 − 9 = −5, and 9 − 4 = 5 is a different question.", "تفریق میں ترتیب نہیں بدل سکتے۔ 4 − 9 = −5، اور 9 − 4 = 5 الگ سوال ہے۔", "Yes! 4 − 9 goes past 0 on the number line, so it is negative.", "جی ہاں! 4 − 9 عددی خط پر 0 سے آگے جاتا ہے، اس لیے منفی ہے۔"),
      [("Nothing. Subtraction obeys the commutative law.", "کوئی غلطی نہیں۔ تفریق قانون تبدیلی کو مانتی ہے۔", "The commutative law works for addition only. 4 − 9 and 9 − 4 are different.", "قانون تبدیلی صرف جمع کے لیے ہے۔ 4 − 9 اور 9 − 4 مختلف ہیں۔", "small_minus_big"),
       ("She should have added: 4 + 9 = 13.", "اسے جمع کرنا چاہیے تھا: 4 + 9 = 13", "The question asks for a subtraction, so adding is a different problem.", "سوال تفریق کا ہے، جمع الگ مسئلہ ہے۔", "unlike_added")],
      1, qtype="find_error"),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! You added and subtracted integers.", "شاباش! آپ نے صحیح اعداد جمع اور تفریق کیے۔"),
    "text": T("Like signs: add and keep the sign. Unlike signs: subtract and keep the sign of the bigger digits. To subtract, add the opposite. Addition is commutative and associative, but subtraction is not: 4 − 9 = −5 while 9 − 4 = 5. To find a missing integer, undo the operation.",
              "ایک جیسی علامتیں: جمع کریں اور علامت رکھیں۔ مخالف علامتیں: تفریق کریں اور بڑے ہندسوں والی علامت رکھیں۔ تفریق کے لیے مخالف جمع کریں۔ جمع تبدیلی اور شراکت کے قوانین مانتا ہے، تفریق نہیں: 4 − 9 = −5 جبکہ 9 − 4 = 5۔ گم شدہ صحیح عدد کے لیے عمل کو الٹ دیں۔"),
    "points": [T("Subtracting a negative number is adding a positive one.", "منفی عدد کو گھٹانا مثبت عدد کو جمع کرنا ہے۔"),
               T("A distance between points on opposite sides of 0 is found by adding.", "0 کی مخالف طرف کے نقطوں کا فاصلہ جمع کر کے ملتا ہے۔")]},
 ],
 bank=[
   {"id": "qb_like", "type": "recall", "step": nq("qb_like", ("Find (−7) + (−9).", "(−7) + (−9) معلوم کریں۔"), QB_REC,
      ("Add the digits and keep the minus sign.", "ہندسے جمع کریں اور منفی علامت رکھیں۔"),
      ("Right! −16.", "درست! −16"), ("7 + 9 = 16, both negative: −16.", "7 + 9 = 16، دونوں منفی: −16"),
      [(16, "Like negative numbers give a negative sum: −16.", "منفی اعداد کا مجموعہ منفی ہوتا ہے: −16", "sign_lost")], qtype=None)},
   {"id": "qb_sub", "type": "apply", "step": nq("qb_sub", ("Find 15 − 23.", "15 − 23 معلوم کریں۔"), QB_APP,
      ("Start at 15 and go 23 steps left. You pass 0.", "15 سے شروع کریں اور 23 قدم بائیں جائیں۔ آپ 0 سے آگے نکل جائیں گے۔"),
      ("Right! −8.", "درست! −8"), ("15 − 23 = 15 + (−23) = −8.", "15 − 23 = 15 + (−23) = −8"),
      [(8, "23 − 15 is 8, but 15 − 23 is negative: −8.", "23 − 15 تو 8 ہے، مگر 15 − 23 منفی ہے: −8", "small_minus_big"),
       (38, "That adds. We subtract: −8.", "یہ جمع ہے۔ ہمیں تفریق کرنی ہے: −8", "unlike_added")], qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": ch("qb_find_error",
      ("Zain says 8 − (−3) = 5. What went wrong?", "زین کہتا ہے 8 − (−3) = 5۔ کیا غلطی ہوئی؟"),
      ("Subtracting −3 is adding 3, so 8 − (−3) = 8 + 3 = 11.", "−3 کو گھٹانا 3 جمع کرنا ہے، اس لیے 8 − (−3) = 8 + 3 = 11", "Yes! Two minus signs make a plus.", "جی ہاں! دو منفی علامتیں مل کر جمع بنتی ہیں۔"),
      [("Nothing. 8 − (−3) = 8 − 3 = 5.", "کوئی غلطی نہیں۔ 8 − (−3) = 8 − 3 = 5", "He ignored the minus sign inside the bracket.", "اس نے بریکٹ کے اندر کی منفی علامت نظر انداز کر دی۔", "double_neg"),
       ("The answer should be −5.", "جواب −5 ہونا چاہیے۔", "8 + 3 is positive, so the answer is not −5.", "8 + 3 مثبت ہے، اس لیے جواب −5 نہیں۔", "sign_lost")],
      0, qtype=None)},
 ],
 review=[
   {"id": "r_like", "type": "recall", "step": nq("r_like", ("Find (−12) + (−8).", "(−12) + (−8) معلوم کریں۔"), R_REC,
      ("Same signs: add and keep the sign.", "ایک جیسی علامتیں: جمع کریں اور علامت رکھیں۔"),
      ("Right! −20.", "درست! −20"), ("12 + 8 = 20, negative: −20.", "12 + 8 = 20، منفی: −20"),
      [(20, "Both are negative, so the sum is negative: −20.", "دونوں منفی ہیں، اس لیے مجموعہ منفی ہے: −20", "sign_lost")], qtype=None)},
   {"id": "r_sub", "type": "apply", "step": nq("r_sub", ("Find (−2) − 7.", "(−2) − 7 معلوم کریں۔"), R_APP,
      ("Both steps go left: −2 − 7.", "دونوں قدم بائیں جاتے ہیں: −2 − 7"),
      ("Right! −9.", "درست! −9"), ("From −2, go 7 more to the left: −9.", "−2 سے 7 قدم مزید بائیں: −9"),
      [(5, "That is −2 + 7. We subtract 7, which moves left: −9.", "یہ −2 + 7 ہے۔ ہم 7 گھٹا رہے ہیں، جو بائیں لے جاتا ہے: −9", "double_neg")], qtype=None)},
 ],
 glossary=[T("Like integers", "ملتے جلتے صحیح اعداد"), T("Unlike integers", "مخالف صحیح اعداد"), T("Commutative law", "قانون تبدیلی"), T("Associative law", "قانون شراکت"), T("Additive inverse", "جمعی معکوس")],
 flashcards=[
   {"id": "f_sub", "front": T("How do you subtract an integer?", "صحیح عدد کو کیسے گھٹاتے ہیں؟"),
    "back": T("Add its opposite: 7 − (−6) = 7 + 6 = 13.", "اس کا مخالف جمع کریں: 7 − (−6) = 7 + 6 = 13")},
   {"id": "f_unlike", "front": T("What is 12 + (−20)?", "12 + (−20) کیا ہے؟"),
    "back": T("−8. Subtract 20 − 12 and keep the sign of the bigger digits.", "−8۔ 20 − 12 کریں اور بڑے ہندسوں کی علامت رکھیں۔")},
 ],
 home_task={"id": "h_thermo", "text": T(
   "Write today's morning and night temperatures as integers (for a cold place use a negative number, such as −3). Work out the change from one to the other in two ways: with a number line and with subtraction.",
   "آج صبح اور رات کے درجہ حرارت صحیح اعداد کے طور پر لکھیں (ٹھنڈی جگہ کے لیے منفی عدد، جیسے −3)۔ ایک سے دوسرے تک کی تبدیلی دو طریقوں سے معلوم کریں: عددی خط سے اور تفریق سے۔")},
 notes=["Covers adding like and unlike integers (q1, q2, q3), subtracting (q4, q5, q6), the commutative and associative laws of addition (q7, q8, q13), finding a missing integer (q9, q10) and distance word problems (q11, q12).",
        "Each wrong answer is a real mistake: dropping the sign, swapping the order of a subtraction, treating − (−6) as − 6, or adding the digits of unlike integers.",
        "Urdu terms to check: قانون تبدیلی / قانون شراکت (commutative / associative law), ملتے جلتے / مخالف صحیح اعداد (like / unlike integers), جمعی معکوس (additive inverse)."],
 minutes=18,
)

write(lesson)
