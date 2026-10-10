"""Practice set for Exercise 6.2 of the book: write sentences in symbols, say
whether a statement is true or false, fill in missing values, and pick out
constants and variables. The questions are new; only the kinds of question
follow the book."""
from common import (T, say, nq, aq, ch, practice_lesson, practice_intro, write, show, m,
                    EX_SKILL, ALG_VARIABLES, value)
import figs

SKILL = EX_SKILL["6.2"]

# q4: a number n increased by 9
Q4 = [(1, "n"), (9, "")]
assert show(Q4) == "n + 9" and value("n + 9", n=10) == 19
# q5: 5 less than a number k
Q5 = [(1, "k"), (-5, "")]
Q5_WRONG = [(5, ""), (-1, "k")]
assert show(Q5) == "k − 5" and value("k - 5", k=8) == 3 and value("5 - k", k=8) == -3
# q6: 7 times a number y, and 2 added
Q6 = [(7, "y"), (2, "")]
assert value("7y + 2", y=3) == 23
assert value("9y", y=3) != 23 and value("7 + 2y", y=3) != 23
# q7: when y = 4, the value of 3y
Q7 = value("3y", y=4)
assert Q7 == 12 and int("34") != Q7
# q8: 3m = 15 for m = 12 is false (m = 5)
assert 3 * 12 != 15 and 3 * 5 == 15 and [m_ for m_ in range(1, 30) if 3 * m_ == 15] == [5]
# q9: n pencils at Rs 12 each, n = 5
Q9 = value("12n", n=5)
assert Q9 == 60 and 12 + 5 == 17 and int("125") != Q9
# q10: 5 more than x written as 5x
assert value("x + 5", x=2) != value("5x", x=2)
# q12: 20 minus a number is 13
Q12 = [x for x in range(0, 40) if 20 - x == 13]
assert Q12 == [7]
Q12 = Q12[0]
assert 20 + 13 == 33 and 20 - 13 == Q12
# bank
QB_Y = value("y + 8", y=6)
assert QB_Y == 14 and int("68") != QB_Y
R1 = value("2a + 1", a=7)
assert R1 == 15 and int("27") + 1 != R1
R2 = [x for x in range(0, 30) if x + 9 == 15]
assert R2 == [6]
R2 = R2[0]

lesson = practice_lesson(
 "6.2", script="exercise_6_2.py",
 title=T("Exercise 6.2 practice: letters for numbers", "مشق 6.2 کی پریکٹس: اعداد کی جگہ حروف"),
 outcome="Write sentences in symbols with a letter for the unknown number, decide whether a statement is true or false, fill in missing values, and tell constants from variables.",
 prerequisites=[ALG_VARIABLES],
 misconceptions=[
   {"id": "constant_is_variable", "description": "Takes a quantity that never changes (days in a week) for a variable, or a changing one for a constant."},
   {"id": "times_for_plus", "description": "Writes 'more than' as multiplication, like 5x for 5 more than x."},
   {"id": "less_than_reversed", "description": "Writes 5 less than k as 5 − k instead of k − 5."},
   {"id": "joins_digits", "description": "Reads 3y with y = 4 as 34 instead of 3 × 4."},
   {"id": "wrong_operation", "description": "Adds when a number was taken away, or the other way round, when finding a missing value."},
   {"id": "letter_fixed", "description": "Thinks a letter always stands for one fixed number."},
   {"id": "one_value_true", "description": "Calls a statement with a letter true because it works for one number, without testing the number given."},
 ],
 steps=[
   practice_intro("6.2",
     "Here you write sentences in symbols, decide whether a statement is true or false, fill in missing values, and pick out constants and variables.",
     "اس میں آپ جملوں کو علامتوں میں لکھیں گے، فیصلہ کریں گے کہ بیان درست ہے یا غلط، غائب قیمتیں بھریں گے، اور مستقل اور متغیر پہچانیں گے۔",
     "Exercise 6.2 is about using letters for numbers. Ready?", "مشق 6.2 اعداد کی جگہ حروف کے بارے میں ہے۔ تیار؟"),
   ch("q1_constant", ("Which of these is a constant (its value never changes)?", "ان میں سے کون سا مستقل ہے (اس کی قیمت کبھی نہیں بدلتی)؟"),
      ("The number of days in a week", "ہفتے کے دنوں کی تعداد", "Yes! A week always has 7 days.", "جی ہاں! ہفتے میں ہمیشہ 7 دن ہوتے ہیں۔"),
      [("The temperature of Murree each hour", "مری کا ہر گھنٹے کا درجہ حرارت", "It changes through the day, so it is a variable.", "یہ دن بھر بدلتا رہتا ہے، اس لیے یہ متغیر ہے۔", "constant_is_variable"),
       ("The price of tomatoes each week", "ہر ہفتے ٹماٹر کی قیمت", "Prices go up and down, so this is a variable.", "قیمتیں اوپر نیچے ہوتی ہیں، اس لیے یہ متغیر ہے۔", "constant_is_variable"),
       ("The age of a child each year", "بچے کی عمر ہر سال", "Age grows every year, so it is a variable.", "عمر ہر سال بڑھتی ہے، اس لیے یہ متغیر ہے۔", "constant_is_variable")],
      0, qtype="recall"),
   ch("q2_variable", ("In the rule \"a notebook costs Rs 30, so n notebooks cost 30n rupees\", which part is the variable?", "اصول \"ایک کاپی 30 روپے کی ہے، تو n کاپیوں کی قیمت 30n روپے ہے\" میں متغیر کون سا ہے؟"),
      ("n, the number of notebooks", "n، کاپیوں کی تعداد", "Yes! n can be 1, 2, 3 ... so it is the variable.", "جی ہاں! n، 1، 2، 3 ... ہو سکتا ہے، اس لیے یہ متغیر ہے۔"),
      [("30, the price of one notebook", "30، ایک کاپی کی قیمت", "30 stays the same for every n, so it is a constant.", "30 ہر n کے لیے ایک جیسا رہتا ہے، اس لیے یہ مستقل ہے۔", "constant_is_variable"),
       ("Both 30 and n", "30 اور n دونوں", "Only n changes. 30 is a constant.", "صرف n بدلتا ہے۔ 30 مستقل ہے۔", "constant_is_variable")],
      2, qtype="recall"),
   {"id": "s_rule", "type": "explain",
    "character": say("thinking", "A letter stands for a number. A constant never changes; a variable can.", "حرف ایک عدد کی جگہ آتا ہے۔ مستقل کبھی نہیں بدلتا؛ متغیر بدل سکتا ہے۔"),
    "text": T("We use a letter for a number we do not know yet, or that can change. A letter whose value can change is a variable. A number that always stays the same is a constant. \"A number n increased by 9\" is n + 9. \"5 less than k\" is k − 5, because we start from k. \"7 times y, then 2 added\" is 7y + 2. A statement with a letter is true only for some values: n + 2 = 9 is true when n = 7.",
              "جس عدد کو ہم نہیں جانتے یا جو بدل سکتا ہے اس کی جگہ حرف لکھتے ہیں۔ جس حرف کی قیمت بدل سکتی ہے وہ متغیر ہے۔ جو عدد ہمیشہ ایک جیسا رہے وہ مستقل ہے۔ \"عدد n میں 9 کا اضافہ\" n + 9 ہے۔ \"k سے 5 کم\" k − 5 ہے، کیونکہ ہم k سے شروع کرتے ہیں۔ \"y کا 7 گنا، پھر 2 جمع\" 7y + 2 ہے۔ حرف والا بیان صرف کچھ قیمتوں کے لیے درست ہوتا ہے: n + 2 = 9 اس وقت درست ہے جب n = 7 ہو۔")},
   aq("q4_symbols", ("Write in symbols: a number n increased by 9.", "علامتوں میں لکھیں: عدد n میں 9 کا اضافہ۔"), Q4,
      ("Start with n and add 9.", "n سے شروع کریں اور 9 جمع کریں۔"),
      ("Right! n + 9.", "درست! n + 9"), ("Increased by 9 means plus 9: n + 9.", "9 کا اضافہ یعنی 9 جمع: n + 9"),
      [([(9, "n")], "9n means 9 times n. Increased by 9 is n + 9.", "9n یعنی n کا 9 گنا۔ 9 کا اضافہ n + 9 ہے۔", "times_for_plus")], qtype="recall"),
   aq("q5_less", ("Write in symbols: 5 less than a number k.", "علامتوں میں لکھیں: عدد k سے 5 کم۔"), Q5,
      ("Start from k, then take away 5.", "k سے شروع کریں، پھر 5 تفریق کریں۔"),
      ("Right! k − 5.", "درست! k − 5"), ("5 less than k is k − 5.", "k سے 5 کم یعنی k − 5"),
      [(Q5_WRONG, "5 − k starts from 5. We start from k: k − 5.", "5 − k، 5 سے شروع ہوتا ہے۔ ہم k سے شروع کرتے ہیں: k − 5", "less_than_reversed"),
       ([(5, "k")], "5k means 5 times k. Less than means take away: k − 5.", "5k یعنی k کا 5 گنا۔ کم کا مطلب تفریق ہے: k − 5", "times_for_plus")]),
   aq("q6_times_plus", ("Write in symbols: 7 times a number y, and then 2 added.", "علامتوں میں لکھیں: عدد y کا 7 گنا، اور پھر 2 جمع۔"), Q6,
      ("7 times y is 7y. Then add 2.", "y کا 7 گنا 7y ہے۔ پھر 2 جمع کریں۔"),
      ("Right! 7y + 2.", "درست! 7y + 2"), ("7 times y is 7y, and 2 more is 7y + 2.", "y کا 7 گنا 7y ہے، اور 2 مزید 7y + 2 ہے۔"),
      [([(9, "y")], "7y and 2 are unlike terms (different kinds). They cannot join into 9y: 7y + 2.", "7y اور 2 غیر یکساں ارکان ہیں۔ یہ 9y میں نہیں مل سکتے: 7y + 2", "times_for_plus"),
       ([(7, ""), (2, "y")], "The 7 multiplies y, not the 2: 7y + 2.", "7، y کو ضرب دیتا ہے، 2 کو نہیں: 7y + 2", "times_for_plus")]),
   nq("q7_value", ("Fill in the missing value: when y = 4, the value of 3y is __.", "غائب قیمت بھریں: جب y = 4 ہو تو 3y کی قیمت __ ہے۔"), Q7,
      ("3y means 3 × y.", "3y یعنی 3 × y"),
      ("Right! 3 × 4 = 12.", "درست! 3 × 4 = 12"), ("3y is 3 × 4 = 12.", "3y یعنی 3 × 4 = 12"),
      [(34, "3y is 3 times y, not the digits 3 and 4 side by side: 12.", "3y یعنی y کا 3 گنا، 3 اور 4 کے ہندسے ساتھ ساتھ نہیں: 12", "joins_digits")]),
   ch("q8_true_false", ("Is the statement \"3m = 15 when m = 12\" true or false?", "کیا بیان \"3m = 15 جب m = 12\" درست ہے یا غلط؟"),
      ("False. 3 × 12 = 36, not 15. (It is true when m = 5.)", "غلط۔ 3 × 12 = 36، 15 نہیں۔ (یہ m = 5 کے لیے درست ہے۔)", "Yes! Put the value in and check both sides.", "جی ہاں! قیمت رکھیں اور دونوں طرف جانچیں۔"),
      [("True, because 3m = 15 is a true equation.", "درست، کیونکہ 3m = 15 درست مساوات ہے۔", "It is true only for one value, m = 5. For m = 12 the left side is 36.", "یہ صرف ایک قیمت m = 5 کے لیے درست ہے۔ m = 12 کے لیے بایاں طرف 36 ہے۔", "one_value_true"),
       ("True, because 3 + 12 = 15.", "درست، کیونکہ 3 + 12 = 15۔", "3m means 3 times m, not 3 plus m. 3 × 12 = 36.", "3m یعنی m کا 3 گنا، 3 جمع m نہیں۔ 3 × 12 = 36", "times_for_plus")],
      0, qtype="apply"),
   nq("q9_cost", ("A pencil costs Rs 12, so n pencils cost 12n rupees. What is the cost when n = 5?", "ایک پنسل 12 روپے کی ہے، تو n پنسلوں کی قیمت 12n روپے ہے۔ n = 5 ہو تو قیمت کیا ہے؟"), Q9,
      ("12n means 12 × n.", "12n یعنی 12 × n"),
      ("Right! 12 × 5 = 60 rupees.", "درست! 12 × 5 = 60 روپے"), ("12 × 5 = 60.", "12 × 5 = 60"),
      [(17, "12n is 12 times n, not 12 plus n: 60.", "12n یعنی n کا 12 گنا، 12 جمع n نہیں: 60", "times_for_plus"),
       (125, "12n with n = 5 is 12 × 5, not the digits 12 and 5 together: 60.", "n = 5 کے ساتھ 12n یعنی 12 × 5، ہندسے 12 اور 5 ساتھ ساتھ نہیں: 60", "joins_digits")]),
   ch("q10_find_error", ("Zara writes \"5 more than a number x\" as 5x. What went wrong?", "زارہ \"عدد x سے 5 زیادہ\" کو 5x لکھتی ہے۔ کیا غلطی ہوئی؟"),
      ("5x means 5 times x. 5 more than x is x + 5.", "5x یعنی x کا 5 گنا۔ x سے 5 زیادہ x + 5 ہے۔", "Yes! More than means add, not multiply.", "جی ہاں! زیادہ کا مطلب جمع ہے، ضرب نہیں۔"),
      [("Nothing. 5x is the right way to write it.", "کوئی غلطی نہیں۔ 5x اسے لکھنے کا صحیح طریقہ ہے۔", "When x = 2, 5x = 10 but 5 more than 2 is 7. So 5x is wrong.", "جب x = 2 ہو تو 5x = 10 ہے مگر 2 سے 5 زیادہ 7 ہے۔ اس لیے 5x غلط ہے۔", "times_for_plus"),
       ("She should write x − 5.", "اسے x − 5 لکھنا چاہیے۔", "Minus means less than. 5 more than x is x + 5.", "منفی کا مطلب کم ہے۔ x سے 5 زیادہ x + 5 ہے۔", "less_than_reversed")],
      1, qtype="find_error"),
   ch("q11_find_error_letter", ("Hamza says the letter n must be 5 in every question, because n was 5 in the last one. What went wrong?", "حمزہ کہتا ہے کہ ہر سوال میں حرف n کو 5 ہونا چاہیے، کیونکہ پچھلے سوال میں n برابر 5 تھا۔ کیا غلطی ہوئی؟"),
      ("A letter is a variable. It can stand for a different number in each question.", "حرف متغیر ہے۔ یہ ہر سوال میں مختلف عدد کی جگہ آ سکتا ہے۔", "Yes! The question tells you what the letter stands for.", "جی ہاں! سوال بتاتا ہے کہ حرف کس عدد کی جگہ ہے۔"),
      [("Nothing. n always means 5.", "کوئی غلطی نہیں۔ n کا مطلب ہمیشہ 5 ہے۔", "n is not fixed. In n + 2 it can be 1, 7, 20 ...", "n مقرر نہیں ہے۔ n + 2 میں یہ 1، 7، 20 ... ہو سکتا ہے۔", "letter_fixed"),
       ("He should use x instead, because x is always 5.", "اسے x استعمال کرنا چاہیے، کیونکہ x ہمیشہ 5 ہے۔", "No letter is fixed. Any letter can stand for different numbers.", "کوئی حرف مقرر نہیں۔ ہر حرف مختلف اعداد کی جگہ آ سکتا ہے۔", "letter_fixed")],
      2, qtype="find_error"),
   nq("q12_missing", ("20 minus a number is 13. Fill in the missing number: 20 − __ = 13.", "20 منفی ایک عدد برابر 13 ہے۔ غائب عدد بھریں: 20 − __ = 13۔"), Q12,
      ("What do you take away from 20 to leave 13?", "20 میں سے کیا تفریق کریں کہ 13 بچے؟"),
      ("Right! 20 − 7 = 13.", "درست! 20 − 7 = 13"), ("20 − 13 = 7, and 20 − 7 = 13.", "20 − 13 = 7، اور 20 − 7 = 13"),
      [(33, "20 + 13 is 33, but we take away. 20 − 7 = 13.", "20 + 13، 33 ہے مگر ہم تفریق کرتے ہیں۔ 20 − 7 = 13", "wrong_operation")]),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! You used letters for numbers.", "شاباش! آپ نے اعداد کی جگہ حروف استعمال کیے۔"),
    "text": T("A letter that can change is a variable; a number that stays the same is a constant. More than means add (x + 5), less than means take away from the number named (k − 5), and 3y means 3 times y. To test a statement, put the value in for the letter and check both sides.",
              "جو حرف بدل سکتا ہے وہ متغیر ہے؛ جو عدد ایک جیسا رہے وہ مستقل ہے۔ زیادہ کا مطلب جمع (x + 5)، کم کا مطلب جس عدد کا نام لیا ہو اس میں سے تفریق (k − 5)، اور 3y کا مطلب y کا 3 گنا ہے۔ بیان کو جانچنے کے لیے حرف کی جگہ قیمت رکھیں اور دونوں طرف دیکھیں۔"),
    "points": [T("Ask: can this value change? Then it is a variable.", "پوچھیں: کیا یہ قیمت بدل سکتی ہے؟ تب یہ متغیر ہے۔"),
               T("Test a symbol sentence with a small number.", "علامتوں والے جملے کو چھوٹے عدد سے جانچیں۔")]},
 ],
 bank=[
   {"id": "qb_variable", "type": "recall", "step": ch("qb_variable", ("Which of these is a variable?", "ان میں سے کون سا متغیر ہے؟"),
      ("The number of students present in a class each day", "جماعت میں روزانہ حاضر طلبہ کی تعداد", "Yes! It can be different every day.", "جی ہاں! یہ ہر روز مختلف ہو سکتی ہے۔"),
      [("The number of months in a year", "سال کے مہینوں کی تعداد", "A year always has 12 months: a constant.", "سال میں ہمیشہ 12 مہینے ہوتے ہیں: مستقل۔", "constant_is_variable"),
       ("The number of sides of a triangle", "تکون کے اضلاع کی تعداد", "A triangle always has 3 sides: a constant.", "تکون کے ہمیشہ 3 اضلاع ہوتے ہیں: مستقل۔", "constant_is_variable")],
      0, qtype=None)},
   {"id": "qb_value", "type": "apply", "step": nq("qb_value", ("Fill in the missing value: when y = 6, the value of y + 8 is __.", "غائب قیمت بھریں: جب y = 6 ہو تو y + 8 کی قیمت __ ہے۔"), QB_Y,
      ("Put 6 in place of y.", "y کی جگہ 6 رکھیں۔"),
      ("Right! 6 + 8 = 14.", "درست! 6 + 8 = 14"), ("6 + 8 = 14.", "6 + 8 = 14"),
      [(68, "y + 8 means 6 plus 8, not the digits 6 and 8 together: 14.", "y + 8 یعنی 6 جمع 8، ہندسے 6 اور 8 ساتھ ساتھ نہیں: 14", "joins_digits")], qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": ch("qb_find_error",
      ("Ali writes \"3 less than a number p\" as 3 − p. What went wrong?", "علی \"عدد p سے 3 کم\" کو 3 − p لکھتا ہے۔ کیا غلطی ہوئی؟"),
      ("It should be p − 3, because we start from p and take away 3.", "یہ p − 3 ہونا چاہیے، کیونکہ ہم p سے شروع کر کے 3 تفریق کرتے ہیں۔", "Yes! 3 − p starts from 3.", "جی ہاں! 3 − p، 3 سے شروع ہوتا ہے۔"),
      [("Nothing. 3 − p is correct.", "کوئی غلطی نہیں۔ 3 − p درست ہے۔", "When p = 10, 3 less than p is 7, but 3 − 10 is −7.", "جب p = 10 ہو تو p سے 3 کم 7 ہے مگر 3 − 10 برابر −7 ہے۔", "less_than_reversed"),
       ("It should be 3p.", "یہ 3p ہونا چاہیے۔", "3p means 3 times p. Less than means take away: p − 3.", "3p یعنی p کا 3 گنا۔ کم کا مطلب تفریق ہے: p − 3", "times_for_plus")],
      0, qtype=None)},
 ],
 review=[
   {"id": "r_value", "type": "recall", "step": nq("r_value", ("What is the value of 2a + 1 when a = 7?", "جب a = 7 ہو تو 2a + 1 کی قیمت کیا ہے؟"), R1,
      ("2a means 2 × a. Then add 1.", "2a یعنی 2 × a۔ پھر 1 جمع کریں۔"),
      ("Right! 2 × 7 + 1 = 15.", "درست! 2 × 7 + 1 = 15"), ("2 × 7 = 14, and 14 + 1 = 15.", "2 × 7 = 14، اور 14 + 1 = 15"),
      [(28, "2a with a = 7 is 14, not 27. Then add 1: 15.", "a = 7 کے ساتھ 2a برابر 14 ہے، 27 نہیں۔ پھر 1 جمع کریں: 15", "joins_digits")], qtype=None)},
   {"id": "r_missing", "type": "apply", "step": nq("r_missing", ("Fill in the missing number: __ + 9 = 15.", "غائب عدد بھریں: __ + 9 = 15۔"), R2,
      ("What must be added to 9 to make 15?", "9 میں کیا جمع کریں کہ 15 بنے؟"),
      ("Right! 6 + 9 = 15.", "درست! 6 + 9 = 15"), ("15 − 9 = 6, so 6 + 9 = 15.", "15 − 9 = 6، تو 6 + 9 = 15"),
      [(24, "15 + 9 is 24, but we need the number that makes 15: 6.", "15 + 9، 24 ہے مگر ہمیں وہ عدد چاہیے جس سے 15 بنے: 6", "wrong_operation")], qtype=None)},
 ],
 glossary=[T("Variable", "متغیر"), T("Constant", "مستقل"), T("Expression", "عبارت"), T("True and false", "درست اور غلط")],
 flashcards=[
   {"id": "f_const_var", "front": T("Constant or variable?", "مستقل یا متغیر؟"),
    "back": T("A constant never changes (7 days in a week). A variable can change (n, the number of pens).", "مستقل کبھی نہیں بدلتا (ہفتے کے 7 دن)۔ متغیر بدل سکتا ہے (n، قلموں کی تعداد)۔")},
   {"id": "f_less", "front": T("How do you write 5 less than k?", "k سے 5 کم کیسے لکھتے ہیں؟"),
    "back": T("k − 5. Start from k, then take away 5.", "k − 5۔ k سے شروع کریں، پھر 5 تفریق کریں۔")},
 ],
 home_task={"id": "h_letters_at_home", "text": T(
   "Find two things at home that never change (a constant) and two that change (a variable). Then write one rule with a letter, like \"x oranges cost 20x rupees\", and test it for x = 3.",
   "گھر میں دو چیزیں ڈھونڈیں جو کبھی نہیں بدلتیں (مستقل) اور دو جو بدلتی ہیں (متغیر)۔ پھر حرف کے ساتھ ایک اصول لکھیں، جیسے \"x سنگترے 20x روپے کے ہیں\"، اور اسے x = 3 کے لیے جانچیں۔")},
 notes=["Covers constants and variables (q1, q2), writing sentences in symbols (q4, q5, q6, q10), true and false (q8), filling in missing values (q7, q9, q12) and find-the-error questions (q10, q11).",
        "Each wrong answer is a real mistake: more than written as times, less than written the wrong way round, 3y read as 34, a plus where a minus is needed, and a letter taken as one fixed number.",
        "Urdu terms to check: متغیر (variable), مستقل (constant), عبارت (expression), اضافہ (increase), مساوات (equation). No new Urdu term was invented here."],
 minutes=16,
)

figs.attach(lesson, {})
write(lesson)
