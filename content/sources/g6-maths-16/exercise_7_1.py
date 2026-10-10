"""Practice set for Exercise 7.1 of the book: turn sentences into equations and
equations back into sentences, and sort items into equations and expressions.
The questions are new; only the kinds of question follow the book."""
from common import (T, say, nq, eq_q, ch, practice_lesson, practice_intro, write, m, solves, solve,
                    EX_SKILL, EQ_RECOGNISE, EQ_FORMING, ALG_VARIABLES, ALG_SUBSTITUTION)

SKILL = EX_SKILL["7.1"]


def is_equation(text):
    return "=" in text


def one_letter(text):
    return {c for c in text if c.isalpha()}


# q1: which one is an equation
Q1_RIGHT, Q1_WRONG = "5y − 2 = 13", ["5y − 2", "5y", "y − 2 + 13"]
assert is_equation(Q1_RIGHT) and not any(is_equation(w) for w in Q1_WRONG)
# q2: m + 6 = 21 (Mariam's marbles, m = 15)
assert solve("m + 6 = 21", "m") == 15 and not solves("m - 6 = 21", m=15) and not solves("6m = 21", m=15)
# q3: 4 times n is 36
assert solve("4n = 36", "n") == 9 and not solves("n + 4 = 36", n=9) and not solves("n ÷ 4 = 36", n=9)
# q4: 5 less than x is 12 (x = 17)
assert solves("x − 5 = 12", x=17) and not solves("5 − x = 12", x=17)
assert not solves("x + 5 = 12", x=17) and not solves("5x = 12", x=17)
# q5: 3n + 2 = 14 has n = 4
assert solves("3n + 2 = 14", n=4) and not solves("3(n + 2) = 14", n=4) and not solves("n + 3 + 2 = 14", n=4)
# q6: how many of the items are expressions
ITEMS6 = ["2x + 1", "5a = 20", "7 − y", "3m + 4 = 19", "9b"]
Q6 = len([t for t in ITEMS6 if not is_equation(t)])
assert Q6 == 3 and len([t for t in ITEMS6 if is_equation(t)]) == 2
# q7: x + 6 = 15
Q7 = solve("x + 6 = 15")
assert Q7 == 9 and 15 + 6 == 21
# q8: algebraic equation has a letter and an = sign; 7 + 5 = 12 is arithmetic
assert not one_letter("7 + 5 = 12") and one_letter("x + 5 = 12") and is_equation("x + 5 = 12")
# q10: x − 7 = 15 (x = 22); 7 − x = 15 gives x = −8
assert solve("x − 7 = 15") == 22 and solve("7 − x = 15") == -8
# q11: how many of these arithmetic sentences are true
SUMS = [(5, "+", 3, 8), (6, "+", 2, 9), (10, "−", 4, 6), (7, "×", 2, 15)]
OPS = {"+": lambda a, b: a + b, "−": lambda a, b: a - b, "×": lambda a, b: a * b}
Q11 = len([1 for a, o, b, c in SUMS if OPS[o](a, b) == c])
assert Q11 == 2
# q12: b + 5 = 17 (Bilal is 12)
assert solve("b + 5 = 17", "b") == 12 and not solves("b − 5 = 17", b=12) and not solves("5b = 17", b=12)
# bank and review
QB = solve("x + 8 = 20")
assert QB == 12 and 20 + 8 == 28
R1 = solve("x − 4 = 10")
assert R1 == 14 and 10 - 4 == 6

lesson = practice_lesson(
 "7.1", script="exercise_7_1.py",
 title=T("Exercise 7.1 practice: equations and expressions", "مشق 7.1 کی پریکٹس: مساوات اور الجبری جملے"),
 outcome="Turn sentences into algebraic equations and back, and sort items into equations and expressions.",
 prerequisites=[EQ_RECOGNISE, EQ_FORMING, ALG_VARIABLES, ALG_SUBSTITUTION],
 misconceptions=[
   {"id": "letter_means_equation", "description": "Thinks anything with a letter is an equation, even with no = sign."},
   {"id": "times_for_plus", "description": "Writes 'more than' or 'increased by' as multiplication, like 6m = 21 for m + 6 = 21."},
   {"id": "wrong_operation", "description": "Writes 'increased by' as taking away, or 'times' as adding."},
   {"id": "less_than_reversed", "description": "Writes '5 less than x' as 5 − x instead of x − 5."},
   {"id": "brackets_wrong", "description": "Puts brackets where the words don't need them, like 3(n + 2) for 'three times a number, plus 2'."},
   {"id": "arithmetic_is_algebraic", "description": "Calls 7 + 5 = 12 an algebraic equation, although it has no letter."},
   {"id": "wrong_inverse", "description": "Finds the unknown by adding when the equation takes away, or the other way round."},
 ],
 steps=[
   practice_intro("7.1",
     "Here you turn sentences into equations and equations back into sentences, and sort things into equations and expressions.",
     "اس میں آپ جملوں کو مساوات میں اور مساوات کو جملوں میں بدلیں گے، اور چیزوں کو مساوات اور الجبری جملوں میں الگ کریں گے۔",
     "Exercise 7.1 is about equations. Ready?", "مشق 7.1 مساوات کے بارے میں ہے۔ تیار؟"),
   ch("q1_which", ("Which of these is an equation?", "ان میں سے کون سی مساوات ہے؟"),
      (Q1_RIGHT, Q1_RIGHT, "Yes! It has an = sign: it says two sides are equal.", "جی ہاں! اس میں = کا نشان ہے: یہ بتاتی ہے کہ دونوں طرف برابر ہیں۔"),
      [(Q1_WRONG[0], Q1_WRONG[0], "No = sign, so this is an expression, not an equation.", "= کا نشان نہیں، اس لیے یہ الجبری جملہ ہے، مساوات نہیں۔", "letter_means_equation"),
       (Q1_WRONG[1], Q1_WRONG[1], "A letter with a number is an expression. An equation needs the = sign.", "حرف اور عدد الجبری جملہ ہیں۔ مساوات کے لیے = کا نشان چاہیے۔", "letter_means_equation"),
       (Q1_WRONG[2], Q1_WRONG[2], "Still no = sign: an expression.", "پھر بھی = کا نشان نہیں: الجبری جملہ۔", "letter_means_equation")],
      2, qtype="recall"),
   eq_q("q2_marbles", ("Mariam has m marbles. She wins 6 more and now has 21. Write this as an equation.", "مریم کے پاس m کنچے ہیں۔ وہ 6 اور جیت لیتی ہے اور اب اس کے پاس 21 ہیں۔ اسے مساوات کی صورت میں لکھیں۔"),
        ["m + 6 = 21", "6 + m = 21", "21 = m + 6", "21 = 6 + m"], {"m": 15},
        ("Winning more means adding. Start with m, add 6, and say it equals 21.", "مزید جیتنا یعنی جمع۔ m سے شروع کریں، 6 جمع کریں، اور لکھیں کہ یہ 21 کے برابر ہے۔"),
        ("Right! m + 6 = 21.", "درست! m + 6 = 21"), ("She had m, got 6 more, and has 21: m + 6 = 21.", "اس کے پاس m تھے، 6 اور ملے، اب 21 ہیں: m + 6 = 21"),
        [("m − 6 = 21", "Winning marbles is adding, not taking away: m + 6 = 21.", "کنچے جیتنا جمع ہے، تفریق نہیں: m + 6 = 21", "wrong_operation"),
         ("6m = 21", "6m means 6 times m. She gets 6 more: m + 6 = 21.", "6m یعنی m کا 6 گنا۔ اسے 6 اور ملے: m + 6 = 21", "times_for_plus")], qtype="recall"),
   eq_q("q3_times", ("Write as an equation: 4 times a number n is 36.", "مساوات لکھیں: عدد n کا 4 گنا 36 ہے۔"),
        ["4n = 36", "4 × n = 36", "36 = 4n"], {"n": 9},
        ("4 times n is 4n. 'Is' becomes =.", "n کا 4 گنا یعنی 4n۔ 'ہے' کی جگہ = لکھیں۔"),
        ("Right! 4n = 36.", "درست! 4n = 36"), ("4 times n is 4n, and 'is' is =: 4n = 36.", "n کا 4 گنا 4n ہے اور 'ہے' کا مطلب =: 4n = 36"),
        [("n + 4 = 36", "'Times' means multiply: 4n, not n + 4.", "'گنا' یعنی ضرب: 4n، n + 4 نہیں۔", "wrong_operation"),
         ("n ÷ 4 = 36", "4 times n is 4 × n, not n ÷ 4: 4n = 36.", "n کا 4 گنا 4 × n ہے، n ÷ 4 نہیں: 4n = 36", "wrong_operation")], qtype="recall"),
   {"id": "s_idea", "type": "explain",
    "character": say("thinking", "An equation has an = sign. An expression does not. That is the whole difference!", "مساوات میں = کا نشان ہوتا ہے۔ الجبری جملے میں نہیں۔ بس یہی فرق ہے!"),
    "text": T("An expression like 3x + 2 is only a way of writing a number. An equation like 3x + 2 = 14 says that two sides are equal. We can ask 'which x makes it true?' and the answer is the solution (x = 4). When an equation has only numbers, like 7 + 5 = 12, it is an arithmetic equation; with a letter it is an algebraic equation. To turn words into an equation, write each part in symbols and let 'is' become =.",
              "3x + 2 جیسا الجبری جملہ صرف ایک عدد لکھنے کا طریقہ ہے۔ 3x + 2 = 14 جیسی مساوات بتاتی ہے کہ دونوں طرف برابر ہیں۔ ہم پوچھ سکتے ہیں 'کون سا x اسے درست بناتا ہے؟' اور جواب حل ہے (x = 4)۔ جب مساوات میں صرف اعداد ہوں، جیسے 7 + 5 = 12، تو وہ حسابی مساوات ہے؛ حرف ہو تو الجبری مساوات۔ الفاظ کو مساوات بنانے کے لیے ہر حصہ علامتوں میں لکھیں اور 'ہے' کو = بنا دیں۔")},
   ch("q4_less", ("Which equation says '5 less than a number x is 12'?", "کون سی مساوات کہتی ہے 'عدد x سے 5 کم 12 ہے'؟"),
      ("x − 5 = 12", "x − 5 = 12", "Yes! Start from x and take away 5.", "جی ہاں! x سے شروع کریں اور 5 تفریق کریں۔"),
      [("5 − x = 12", "5 − x = 12", "That starts from 5. '5 less than x' starts from x: x − 5.", "یہ 5 سے شروع ہوتا ہے۔ 'x سے 5 کم' x سے شروع ہوتا ہے: x − 5", "less_than_reversed"),
       ("x + 5 = 12", "x + 5 = 12", "That is 5 MORE than x.", "یہ x سے 5 زیادہ ہے۔", "wrong_operation"),
       ("5x = 12", "5x = 12", "5x means 5 times x.", "5x یعنی x کا 5 گنا۔", "times_for_plus")],
      0),
   ch("q5_back", ("Which sentence matches the equation 3n + 2 = 14?", "کون سا جملہ مساوات 3n + 2 = 14 سے ملتا ہے؟"),
      ("Three times a number, plus 2, is 14.", "ایک عدد کا تین گنا، جمع 2، 14 ہے۔", "Yes! 3n is three times n, then add 2.", "جی ہاں! 3n یعنی n کا تین گنا، پھر 2 جمع۔"),
      [("Three times (a number plus 2) is 14.", "تین گنا (عدد جمع 2) 14 ہے۔", "That would need brackets: 3(n + 2). Here only the 3n is multiplied.", "اس کے لیے قوسین چاہیے: 3(n + 2)۔ یہاں صرف 3n ضرب ہوتا ہے۔", "brackets_wrong"),
       ("A number plus 3 plus 2 is 14.", "عدد جمع 3 جمع 2، 14 ہے۔", "3n is 3 times n, not n + 3.", "3n یعنی n کا 3 گنا، n + 3 نہیں۔", "times_for_plus"),
       ("Three more than a number is 14.", "عدد سے تین زیادہ 14 ہے۔", "That is n + 3 = 14. We have 3n + 2.", "یہ n + 3 = 14 ہے۔ ہمارے پاس 3n + 2 ہے۔", "times_for_plus")],
      1),
   nq("q6_sort", (f"Sort these into equations and expressions: {', '.join(ITEMS6)}. How many of them are expressions?", f"ان کو مساوات اور الجبری جملوں میں الگ کریں: {', '.join(ITEMS6)}۔ ان میں سے کتنے الجبری جملے ہیں؟"), Q6,
      ("An item with an = sign is an equation. The others are expressions.", "جس میں = کا نشان ہو وہ مساوات ہے۔ باقی الجبری جملے ہیں۔"),
      ("Right! 2x + 1, 7 − y and 9b have no = sign: 3 expressions.", "درست! 2x + 1، 7 − y اور 9b میں = کا نشان نہیں: 3 الجبری جملے"),
      ("5a = 20 and 3m + 4 = 19 are equations. The other 3 are expressions.", "5a = 20 اور 3m + 4 = 19 مساواتیں ہیں۔ باقی 3 الجبری جملے ہیں۔"),
      [(2, "2 is the number of equations (the ones with =). Count the others: 3.", "2 مساواتوں کی تعداد ہے (جن میں = ہے)۔ باقی گنیں: 3", "letter_means_equation"),
       (5, "Only the items with no = sign are expressions: 3.", "صرف وہ جن میں = کا نشان نہیں الجبری جملے ہیں: 3", "letter_means_equation")]),
   nq("q7_true", ("For which value of x is the equation x + 6 = 15 true?", "x کی کس قیمت کے لیے مساوات x + 6 = 15 درست ہے؟"), Q7,
      ("Which number plus 6 makes 15? Take 6 away from 15.", "کون سا عدد جمع 6، 15 بناتا ہے؟ 15 میں سے 6 تفریق کریں۔"),
      ("Right! 9 + 6 = 15, so x = 9.", "درست! 9 + 6 = 15، تو x = 9"), ("15 − 6 = 9, and 9 + 6 = 15.", "15 − 6 = 9، اور 9 + 6 = 15"),
      [(21, "That adds 6 to 15. To undo + 6, take 6 away: 9.", "یہ 15 میں 6 جمع کرتا ہے۔ + 6 کو ختم کرنے کے لیے 6 تفریق کریں: 9", "wrong_inverse")]),
   ch("q8_kind", ("Which one is an algebraic equation (not an arithmetic equation)?", "ان میں سے کون سی الجبری مساوات ہے (حسابی مساوات نہیں)؟"),
      ("x + 5 = 12", "x + 5 = 12", "Yes! It has a letter and an = sign.", "جی ہاں! اس میں حرف بھی ہے اور = کا نشان بھی۔"),
      [("7 + 5 = 12", "7 + 5 = 12", "It has only numbers: an arithmetic equation.", "اس میں صرف اعداد ہیں: حسابی مساوات۔", "arithmetic_is_algebraic"),
       ("x + 5", "x + 5", "No = sign: an expression.", "= کا نشان نہیں: الجبری جملہ۔", "letter_means_equation"),
       ("7 + 5", "7 + 5", "Only numbers and no = sign: just a sum.", "صرف اعداد اور = نہیں: صرف ایک جمع۔")],
      3, qtype="recall"),
   ch("q9_find_error", ("Zara says 4a + 3 is an equation, because it has a letter and numbers. What went wrong?", "ثناء کہتی ہے 4a + 3 مساوات ہے، کیونکہ اس میں حرف اور اعداد ہیں۔ کیا غلطی ہوئی؟"),
      ("An equation needs an = sign. 4a + 3 has none, so it is an expression.", "مساوات کے لیے = کا نشان چاہیے۔ 4a + 3 میں نہیں، اس لیے یہ الجبری جملہ ہے۔", "Yes! A letter alone does not make an equation.", "جی ہاں! صرف حرف مساوات نہیں بناتا۔"),
      [("Nothing. A letter with numbers is an equation.", "کوئی غلطی نہیں۔ حرف اور اعداد مساوات ہیں۔", "An expression like 4a + 3 is just a number written with a letter. It says nothing is equal to anything.", "4a + 3 جیسا الجبری جملہ ایک عدد کو حرف سے لکھنا ہے۔ یہ کسی چیز کے برابر ہونے کا نہیں کہتا۔", "letter_means_equation"),
       ("It is an equation, but 4a should be 4 + a.", "یہ مساوات ہے، مگر 4a کو 4 + a ہونا چاہیے۔", "4a means 4 times a, and the sentence still has no = sign.", "4a یعنی a کا 4 گنا، اور جملے میں پھر بھی = نہیں۔", "letter_means_equation")],
      0, qtype="find_error"),
   ch("q10_find_error_less", (f"Sana writes '7 less than a number x equals 15' as 7 − x = 15. What went wrong?", "ثناء '7 کم عدد x برابر 15' کو 7 − x = 15 لکھتی ہے۔ کیا غلطی ہوئی؟"),
      ("'7 less than x' starts from x. It is x − 7 = 15.", "'x سے 7 کم' x سے شروع ہوتا ہے۔ یہ x − 7 = 15 ہے۔", "Yes! With x − 7 = 15, x = 22. With 7 − x = 15 you would get x = −8.", "جی ہاں! x − 7 = 15 سے x = 22 ہے۔ 7 − x = 15 سے x = −8 آتا۔"),
      [("Nothing. 7 − x = 15 is right.", "کوئی غلطی نہیں۔ 7 − x = 15 درست ہے۔", "7 − x starts from 7. 'Less than x' means we start from x.", "7 − x، 7 سے شروع ہوتا ہے۔ 'x سے کم' کا مطلب ہے x سے شروع کرنا۔", "less_than_reversed"),
       ("It should be 7x = 15.", "یہ 7x = 15 ہونا چاہیے۔", "7x means 7 times x. 'Less than' means take away.", "7x یعنی x کا 7 گنا۔ 'کم' کا مطلب تفریق ہے۔", "times_for_plus")],
      1, qtype="find_error"),
   nq("q11_true_false", ("How many of these arithmetic sentences are true: " + "; ".join(f"{a} {o} {b} = {c}" for a, o, b, c in SUMS) + "?",
                         "ان میں سے کتنے حسابی جملے درست ہیں: " + "؛ ".join(f"{a} {o} {b} = {c}" for a, o, b, c in SUMS) + "؟"), Q11,
      ("Work out the left side of each one and compare it with the right.", "ہر ایک کی بائیں طرف نکالیں اور دائیں سے ملائیں۔"),
      ("Right! 5 + 3 = 8 and 10 − 4 = 6 are true.", "درست! 5 + 3 = 8 اور 10 − 4 = 6 درست ہیں۔"),
      ("6 + 2 is 8, not 9, and 7 × 2 is 14, not 15. Only 2 are true.", "6 + 2 برابر 8 ہے، 9 نہیں، اور 7 × 2 برابر 14 ہے، 15 نہیں۔ صرف 2 درست ہیں۔"),
      [(4, "Check each one: 6 + 2 = 8 and 7 × 2 = 14 are not true.", "ہر ایک جانچیں: 6 + 2 = 8 اور 7 × 2 = 14 ہیں، یعنی یہ درست نہیں۔", "arithmetic_is_algebraic"),
       (3, "7 × 2 = 14, so '7 × 2 = 15' is false. Also 6 + 2 = 8, not 9.", "7 × 2 = 14، تو '7 × 2 = 15' غلط ہے۔ نیز 6 + 2 = 8، 9 نہیں۔", "arithmetic_is_algebraic")]),
   eq_q("q12_age", ("Bilal is b years old now. In 5 years' time he will be 17. Write an equation.", "بلال اب b سال کا ہے۔ 5 سال بعد وہ 17 سال کا ہو گا۔ مساوات لکھیں۔"),
        ["b + 5 = 17", "5 + b = 17", "17 = b + 5"], {"b": 12},
        ("In 5 years means add 5 to his age now.", "5 سال بعد یعنی اس کی اب کی عمر میں 5 جمع کریں۔"),
        ("Right! b + 5 = 17.", "درست! b + 5 = 17"), ("His age in 5 years is b + 5, and that is 17.", "5 سال بعد اس کی عمر b + 5 ہے، اور وہ 17 ہے۔"),
        [("b − 5 = 17", "Later means older: add 5, not take away: b + 5 = 17.", "بعد کا مطلب بڑا: 5 جمع کریں، تفریق نہیں: b + 5 = 17", "wrong_operation"),
         ("5b = 17", "5b means 5 times b. We add 5 years: b + 5 = 17.", "5b یعنی b کا 5 گنا۔ ہم 5 سال جمع کرتے ہیں: b + 5 = 17", "times_for_plus")]),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! You can tell and write equations.", "شاباش! آپ مساوات پہچان اور لکھ سکتے ہیں۔"),
    "text": T("An equation has an = sign and says two sides are equal; an expression has none. With only numbers it is an arithmetic equation; with a letter it is an algebraic equation. To write one from words, put each part in symbols and let 'is' become =: 'm and 6 more is 21' is m + 6 = 21, and '5 less than x is 12' is x − 5 = 12.",
              "مساوات میں = کا نشان ہوتا ہے اور وہ بتاتی ہے کہ دونوں طرف برابر ہیں؛ الجبری جملے میں نہیں۔ صرف اعداد ہوں تو حسابی مساوات، حرف ہو تو الجبری مساوات۔ الفاظ سے مساوات لکھنے کے لیے ہر حصہ علامتوں میں لکھیں اور 'ہے' کو = بنائیں: 'm اور 6 زیادہ 21 ہے' یعنی m + 6 = 21، اور 'x سے 5 کم 12 ہے' یعنی x − 5 = 12۔"),
    "points": [T("Look for the = sign first.", "پہلے = کا نشان دیکھیں۔"),
               T("'Less than' starts from the number named last.", "'سے کم' میں آخر میں آنے والے عدد سے شروع کریں۔")]},
 ],
 bank=[
   {"id": "qb_sign", "type": "recall", "step": ch("qb_sign", ("What does an equation have that an expression does not?", "مساوات میں ایسا کیا ہوتا ہے جو الجبری جملے میں نہیں ہوتا؟"),
      ("An = sign", "= کا نشان", "Yes! It says the two sides are equal.", "جی ہاں! یہ بتاتا ہے کہ دونوں طرف برابر ہیں۔"),
      [("A letter", "ایک حرف", "Expressions have letters too, like 3x + 5.", "الجبری جملوں میں بھی حرف ہوتے ہیں، جیسے 3x + 5۔", "letter_means_equation"),
       ("A number", "ایک عدد", "Both have numbers. The = sign makes an equation.", "دونوں میں اعداد ہوتے ہیں۔ = کا نشان مساوات بناتا ہے۔")],
      0, qtype=None)},
   {"id": "qb_value", "type": "apply", "step": nq("qb_value", ("For which value of x is x + 8 = 20 true?", "x کی کس قیمت کے لیے x + 8 = 20 درست ہے؟"), QB,
      ("Take 8 away from 20.", "20 میں سے 8 تفریق کریں۔"),
      ("Right! 12 + 8 = 20.", "درست! 12 + 8 = 20"), ("20 − 8 = 12.", "20 − 8 = 12"),
      [(28, "That adds 8 to 20. Undo + 8 by taking 8 away: 12.", "یہ 20 میں 8 جمع کرتا ہے۔ + 8 کو 8 تفریق کر کے ختم کریں: 12", "wrong_inverse")], qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": ch("qb_find_error",
      ("Usman says 'a number times 3 is 21' is n + 3 = 21. What went wrong?", "عثمان کہتا ہے 'ایک عدد کا 3 گنا 21 ہے' کو n + 3 = 21 لکھتے ہیں۔ کیا غلطی ہوئی؟"),
      ("'Times' means multiply. It is 3n = 21.", "'گنا' یعنی ضرب۔ یہ 3n = 21 ہے۔", "Yes! 3 times a number is 3n.", "جی ہاں! عدد کا 3 گنا 3n ہے۔"),
      [("Nothing. n + 3 = 21 is right.", "کوئی غلطی نہیں۔ n + 3 = 21 درست ہے۔", "n + 3 means 3 MORE than n. Times is multiply: 3n.", "n + 3 یعنی n سے 3 زیادہ۔ گنا ضرب ہے: 3n", "wrong_operation"),
       ("It should be n − 3 = 21.", "یہ n − 3 = 21 ہونا چاہیے۔", "'Times' is not taking away. It is 3n = 21.", "'گنا' تفریق نہیں۔ یہ 3n = 21 ہے۔", "wrong_operation")],
      2, qtype=None)},
 ],
 review=[
   {"id": "r_value", "type": "apply", "step": nq("r_value", ("For which value of x is x − 4 = 10 true?", "x کی کس قیمت کے لیے x − 4 = 10 درست ہے؟"), R1,
      ("Add 4 to 10.", "10 میں 4 جمع کریں۔"),
      ("Right! 14 − 4 = 10.", "درست! 14 − 4 = 10"), ("10 + 4 = 14.", "10 + 4 = 14"),
      [(6, "That takes 4 from 10. To undo − 4, add 4: 14.", "یہ 10 میں سے 4 تفریق کرتا ہے۔ − 4 کو ختم کرنے کے لیے 4 جمع کریں: 14", "wrong_inverse")], qtype=None)},
   {"id": "r_kind", "type": "recall", "step": ch("r_kind", ("Is 7a + 2 an equation or an expression?", "کیا 7a + 2 مساوات ہے یا الجبری جملہ؟"),
      ("An expression, because it has no = sign.", "الجبری جملہ، کیونکہ اس میں = کا نشان نہیں۔", "Yes! No = sign.", "جی ہاں! = کا نشان نہیں۔"),
      [("An equation, because it has a letter.", "مساوات، کیونکہ اس میں حرف ہے۔", "A letter does not make an equation. You need =.", "حرف سے مساوات نہیں بنتی۔ = چاہیے۔", "letter_means_equation"),
       ("An equation, because it has a + sign.", "مساوات، کیونکہ اس میں + کا نشان ہے۔", "+ is for adding. Only = makes an equation.", "+ جمع کے لیے ہے۔ مساوات صرف = سے بنتی ہے۔", "letter_means_equation")],
      1, qtype=None)},
 ],
 glossary=[T("Equation", "مساوات"), T("Expression", "الجبری جملہ"), T("Arithmetic equation", "حسابی مساوات"),
           T("Algebraic equation", "الجبری مساوات"), T("Solution", "حل")],
 flashcards=[
   {"id": "f_sign", "front": T("Equation or expression?", "مساوات یا الجبری جملہ؟"),
    "back": T("An equation has an = sign: 3x + 2 = 14. An expression does not: 3x + 2.", "مساوات میں = کا نشان ہوتا ہے: 3x + 2 = 14۔ الجبری جملے میں نہیں: 3x + 2")},
   {"id": "f_words", "front": T("How do you write '5 less than x is 12'?", "'x سے 5 کم 12 ہے' کیسے لکھتے ہیں؟"),
    "back": T("x − 5 = 12. Start from x, take away 5, and 'is' becomes =.", "x − 5 = 12۔ x سے شروع کریں، 5 تفریق کریں، اور 'ہے' کو = بنائیں۔")},
 ],
 home_task={"id": "h_eq_at_home", "text": T(
   "Write three sentences about things at home that use a number, like 'my brother is 3 years older than me and is 14'. Turn each into an equation with a letter. Then write one expression that is NOT an equation.",
   "گھر کی باتوں کے بارے میں تین جملے لکھیں جن میں ایک عدد ہو، جیسے 'میرا بھائی مجھ سے 3 سال بڑا ہے اور 14 سال کا ہے'۔ ہر ایک کو حرف والی مساوات میں بدلیں۔ پھر ایک ایسا الجبری جملہ لکھیں جو مساوات نہ ہو۔")},
 notes=["Covers telling equations from expressions (q1, q6, q8, q9), turning sentences into equations (q2, q3, q4, q12), turning an equation back into a sentence (q5), and checking which value makes an equation true (q7, q11).",
        "Each wrong answer is a real mistake: more written as times, a word problem turned the wrong way (5 − x), brackets added by habit, a letter taken to make an equation, and the unknown found by the wrong inverse.",
        "Urdu terms to check: مساوات (equation), الجبری جملہ (expression), حسابی مساوات (arithmetic equation), حل (solution). الجبری مساوات (algebraic equation) is new: it joins the existing words الجبری and مساوات, so a teacher should confirm it."],
 minutes=16,
)

write(lesson)
