"""Practice set for Exercise 6.1 of the book: state the rule of a number
sequence and continue it, including sequences that go down through zero and
sequences that add the last two terms (Fibonacci type). The questions are new;
only the kinds of question follow the book."""
from common import (T, say, nq, ch, practice_lesson, practice_intro, write, m,
                    EX_SKILL, ALG_SEQUENCES, value)
import figs

SKILL = EX_SKILL["6.1"]


def run(first, step, count):
    return [first + step * k for k in range(count)]


def times(first, factor, count):
    return [first * factor ** k for k in range(count)]


def fib(a, b, count):
    out = [a, b]
    while len(out) < count:
        out.append(out[-1] + out[-2])
    return out


def seq(xs):
    return ", ".join(m(x) for x in xs)


def gaps(xs):
    return [b - a for a, b in zip(xs, xs[1:])]


# q1: 7, 12, 17, 22 adds 5
Q1 = run(7, 5, 4)
assert gaps(Q1) == [5, 5, 5]
# q2: 4, 11, 18, 25, ... next term (adding 4 again: 29)
Q2S = run(4, 7, 4)
Q2 = Q2S[-1] + 7
assert gaps(Q2S) == [7, 7, 7] and Q2 == 32 and Q2S[-1] + 4 == 29
# q3: 90, 81, 72, 63, ... goes down by 9
Q3S = run(90, -9, 4)
Q3 = Q3S[-1] - 9
assert gaps(Q3S) == [-9, -9, -9] and Q3 == 54 and Q3S[-1] + 9 == 72
# q5: 3, 6, 12, 24 doubles
Q5 = times(3, 2, 4)
assert Q5 == [3, 6, 12, 24] and gaps(Q5) == [3, 6, 12]
# q6: 2, 3, 5, 8, 13 each term is the sum of the two before
Q6S = fib(2, 3, 5)
Q6 = Q6S[-1] + Q6S[-2]
assert Q6S == [2, 3, 5, 8, 13] and Q6 == 21 and Q6S[-1] + 5 == 18 and Q6S[-1] * 2 == 26
assert all(Q6S[k] == Q6S[k - 1] + Q6S[k - 2] for k in range(2, 5))
# q7: 6, 10, __, 18, 22 (adds 4)
Q7S = run(6, 4, 5)
Q7 = Q7S[2]
assert Q7S == [6, 10, 14, 18, 22] and Q7 == 14 and 10 + 2 == 12
# q8: 10, 6, 2, -2, -6, next term -10
Q8S = run(10, -4, 5)
Q8 = Q8S[-1] - 4
assert Q8S == [10, 6, 2, -2, -6] and Q8 == -10 and Q8S[-1] + 4 == -2
# q9: 6th term of 4n - 3
Q9 = value("4n − 3", n=6)
assert Q9 == 21 and 4 * 6 == 24 and int("46") - 3 == 43
# q10: 2, 6, 18, 54 multiplies by 3
Q10S = times(2, 3, 4)
assert Q10S == [2, 6, 18, 54] and gaps(Q10S) == [4, 12, 36] and Q10S[-1] * 3 == 162
# q11: 1, 1, 2, 3, 5 next is 8
Q11S = fib(1, 1, 5)
Q11 = Q11S[-1] + Q11S[-2]
assert Q11S == [1, 1, 2, 3, 5] and Q11 == 8 and Q11S[-1] + 2 == 7
# bank and review
QB1 = run(100, -10, 4)
assert QB1 == [100, 90, 80, 70] and gaps(QB1) == [-10] * 3
QB2S = fib(3, 4, 5)
QB2 = QB2S[-1] + QB2S[-2]
assert QB2S == [3, 4, 7, 11, 18] and QB2 == 29
R1 = run(25, 6, 5)[-1]
assert R1 == 49 and gaps(run(25, 6, 5)) == [6] * 4
R2 = run(8, -3, 5)[-1]
assert R2 == -4 and run(8, -3, 5) == [8, 5, 2, -1, -4]

lesson = practice_lesson(
 "6.1", script="exercise_6_1.py",
 title=T("Exercise 6.1 practice: number patterns", "مشق 6.1 کی پریکٹس: اعداد کے نمونے"),
 outcome="State the rule of a number sequence and continue it, including sequences that go down, pass through zero or add the last two terms.",
 prerequisites=[ALG_SEQUENCES],
 misconceptions=[
   {"id": "always_add", "description": "Assumes every pattern adds the same number, even when it multiplies or the gap grows."},
   {"id": "wrong_direction", "description": "Adds when the pattern goes down, or subtracts when it goes up."},
   {"id": "first_gap_only", "description": "Finds the rule from the first two terms only, without checking the rest."},
   {"id": "fib_gap", "description": "Continues a sequence that adds the last two terms by adding the same gap each time."},
   {"id": "negative_step", "description": "Slips when the terms pass through zero into negative numbers."},
   {"id": "joins_digits", "description": "Reads 4n with n = 6 as 46 instead of 4 × 6."},
   {"id": "forgets_constant", "description": "Leaves out the number added or taken away in a rule like 4n − 3."},
 ],
 steps=[
   practice_intro("6.1",
     "Here you state the rule of a number sequence and continue it, including sequences that go down and sequences where each term is the sum of the two before.",
     "اس میں آپ اعداد کے سلسلے کا اصول بتائیں گے اور اسے آگے بڑھائیں گے، ان سلسلوں کو بھی جو نیچے جاتے ہیں اور ان کو بھی جن میں ہر رکن پچھلے دو ارکان کا مجموعہ ہوتا ہے۔",
     "Exercise 6.1 is about patterns. Ready?", "مشق 6.1 نمونوں کے بارے میں ہے۔ تیار؟"),
   ch("q1_rule", (f"What is the rule of the pattern {seq(Q1)}, …?", f"نمونے {seq(Q1)}، … کا اصول کیا ہے؟"),
      ("Add 5 each time", "ہر بار 5 جمع کریں", "Yes! 12 − 7 = 5, 17 − 12 = 5, 22 − 17 = 5.", "جی ہاں! 12 − 7 = 5، 17 − 12 = 5، 22 − 17 = 5"),
      [("Add 7 each time", "ہر بار 7 جمع کریں", "7 is the first term. The gap between terms is 5.", "7 پہلا رکن ہے۔ ارکان کے درمیان فرق 5 ہے۔", "first_gap_only"),
       ("Multiply by 2 each time", "ہر بار 2 سے ضرب دیں", "7 × 2 = 14, not 12. The terms go up by the same number: 5.", "7 × 2 = 14، 12 نہیں۔ ارکان ایک ہی عدد سے بڑھتے ہیں: 5", "always_add"),
       ("Subtract 5 each time", "ہر بار 5 تفریق کریں", "The terms get bigger, so we add 5.", "ارکان بڑے ہو رہے ہیں، اس لیے 5 جمع کرتے ہیں۔", "wrong_direction")],
      0, qtype="recall"),
   nq("q2_next", (f"Write the next term of the pattern {seq(Q2S)}, …", f"نمونے {seq(Q2S)}، … کا اگلا رکن لکھیں۔"), Q2,
      ("Find the gap between two neighbours first.", "پہلے دو برابر کے ارکان کا فرق معلوم کریں۔"),
      ("Right! The rule is add 7: 25 + 7 = 32.", "درست! اصول 7 جمع کرنا ہے: 25 + 7 = 32"),
      ("The gap is 7 each time, so 25 + 7 = 32.", "فرق ہر بار 7 ہے، تو 25 + 7 = 32"),
      [(29, "4 is the first term, not the gap. The gap is 7: 32.", "4 پہلا رکن ہے، فرق نہیں۔ فرق 7 ہے: 32", "first_gap_only")], qtype="recall"),
   {"id": "s_rule", "type": "explain",
    "character": say("thinking", "Find how the terms change. Then check the rule on every pair!", "دیکھیں ارکان کیسے بدلتے ہیں۔ پھر اصول ہر جوڑے پر جانچیں!"),
    "text": T("A pattern (sequence) follows a rule. Some rules add the same number each time. Some subtract, so the terms go down and may pass through zero into negative numbers. Some multiply, like doubling. Some use the terms before: in 1, 1, 2, 3, 5, 8 every term is the sum of the two terms before it (a Fibonacci-type sequence). To find the rule, look at the gaps. Then test the rule on every pair of neighbours, not only the first two.",
              "نمونہ (سلسلہ) کسی اصول پر چلتا ہے۔ کچھ اصول ہر بار ایک ہی عدد جمع کرتے ہیں۔ کچھ تفریق کرتے ہیں، تو ارکان نیچے جاتے ہیں اور صفر سے گزر کر منفی اعداد میں پہنچ سکتے ہیں۔ کچھ ضرب دیتے ہیں، جیسے دگنا کرنا۔ کچھ پچھلے ارکان استعمال کرتے ہیں: 1، 1، 2، 3، 5، 8 میں ہر رکن اپنے سے پہلے دو ارکان کا مجموعہ ہے (فبوناچی قسم کا سلسلہ)۔ اصول معلوم کرنے کے لیے فرق دیکھیں۔ پھر اصول کو صرف پہلے دو پر نہیں بلکہ ہر جوڑے پر جانچیں۔")},
   nq("q3_down", (f"Write the next term of the pattern {seq(Q3S)}, …", f"نمونے {seq(Q3S)}، … کا اگلا رکن لکھیں۔"), Q3,
      ("The terms are getting smaller. By how much?", "ارکان چھوٹے ہو رہے ہیں۔ کتنے سے؟"),
      ("Right! The rule is subtract 9: 63 − 9 = 54.", "درست! اصول 9 تفریق کرنا ہے: 63 − 9 = 54"),
      ("The terms go down by 9 each time, so 63 − 9 = 54.", "ارکان ہر بار 9 کم ہوتے ہیں، تو 63 − 9 = 54"),
      [(72, "The pattern goes down, not up: 63 − 9 = 54.", "نمونہ نیچے جا رہا ہے، اوپر نہیں: 63 − 9 = 54", "wrong_direction")]),
   ch("q5_double", (f"What is the rule of the pattern {seq(Q5)}, …?", f"نمونے {seq(Q5)}، … کا اصول کیا ہے؟"),
      ("Multiply by 2 each time", "ہر بار 2 سے ضرب دیں", "Yes! 3 × 2 = 6, 6 × 2 = 12, 12 × 2 = 24.", "جی ہاں! 3 × 2 = 6، 6 × 2 = 12، 12 × 2 = 24"),
      [("Add 3 each time", "ہر بار 3 جمع کریں", "3 + 3 = 6 works, but 6 + 3 = 9, not 12. Test every pair.", "3 + 3 = 6 درست ہے مگر 6 + 3 = 9، 12 نہیں۔ ہر جوڑے کو جانچیں۔", "first_gap_only"),
       ("Add 6 each time", "ہر بار 6 جمع کریں", "3 + 6 = 9, not 6. The gaps are 3, 6, 12: they are not equal.", "3 + 6 = 9، 6 نہیں۔ فرق 3، 6، 12 ہیں: برابر نہیں۔", "always_add"),
       ("Add the two terms before", "پچھلے دو ارکان جمع کریں", "3 + 6 = 9, not 12. Each term is double the one before.", "3 + 6 = 9، 12 نہیں۔ ہر رکن پچھلے کا دگنا ہے۔", "fib_gap")],
      2),
   nq("q6_fib", (f"In the pattern {seq(Q6S)}, … each term is the sum of the two terms before it. Write the next term.", f"نمونے {seq(Q6S)}، … میں ہر رکن اپنے سے پہلے دو ارکان کا مجموعہ ہے۔ اگلا رکن لکھیں۔"), Q6,
      ("Add the last two terms.", "آخری دو ارکان جمع کریں۔"),
      ("Right! 8 + 13 = 21.", "درست! 8 + 13 = 21"),
      ("The last two terms are 8 and 13, and 8 + 13 = 21.", "آخری دو ارکان 8 اور 13 ہیں، اور 8 + 13 = 21"),
      [(18, "13 + 5 uses a gap. This pattern adds the last two terms, 8 + 13: 21.", "13 + 5 فرق کا استعمال ہے۔ یہ نمونہ آخری دو ارکان 8 + 13 جمع کرتا ہے: 21", "fib_gap"),
       (26, "That doubles 13. Add the last two terms, 8 + 13: 21.", "یہ 13 کو دگنا کرتا ہے۔ آخری دو ارکان 8 + 13 جمع کریں: 21", "fib_gap")]),
   nq("q7_missing", (f"One term is missing: 6, 10, __, 18, 22. Write the missing term.", "ایک رکن غائب ہے: 6، 10، __، 18، 22۔ غائب رکن لکھیں۔"), Q7,
      ("Find the gap from the terms you can see, then fill the middle.", "نظر آنے والے ارکان سے فرق معلوم کریں، پھر درمیان کو بھریں۔"),
      ("Right! The rule is add 4: 10 + 4 = 14, and 14 + 4 = 18.", "درست! اصول 4 جمع کرنا ہے: 10 + 4 = 14، اور 14 + 4 = 18"),
      ("The gap is 4: 10 + 4 = 14, and 14 + 4 = 18 fits.", "فرق 4 ہے: 10 + 4 = 14، اور 14 + 4 = 18 ٹھیک بیٹھتا ہے۔"),
      [(12, "10 + 2 does not reach 18 in the next step. The gap is 4: 14.", "10 + 2 اگلے قدم میں 18 تک نہیں پہنچتا۔ فرق 4 ہے: 14", "first_gap_only")]),
   nq("q8_negative", (f"The terms of a pattern go {seq(Q8S)}, … Write the next term.", f"ایک نمونے کے ارکان {seq(Q8S)}، … ہیں۔ اگلا رکن لکھیں۔"), Q8,
      ("The terms go down by 4 each time, even below zero.", "ارکان ہر بار 4 کم ہوتے ہیں، صفر سے نیچے بھی۔"),
      ("Right! −6 − 4 = −10.", "درست! −6 − 4 = −10"),
      ("The rule is subtract 4: −6 − 4 = −10.", "اصول 4 تفریق کرنا ہے: −6 − 4 = −10"),
      [(-2, "−2 comes before −6. The terms keep going down: −10.", "−2، −6 سے پہلے آتا ہے۔ ارکان نیچے جاتے رہتے ہیں: −10", "negative_step")]),
   nq("q9_nth", ("The rule for the nth term of a pattern is 4n − 3. What is the 6th term (n = 6)?", "ایک نمونے کے n ویں رکن کا اصول 4n − 3 ہے۔ چھٹا رکن (n = 6) کیا ہے؟"), Q9,
      ("4n means 4 × n. Put n = 6, then take away 3.", "4n یعنی 4 × n۔ n = 6 رکھیں، پھر 3 تفریق کریں۔"),
      ("Right! 4 × 6 − 3 = 21.", "درست! 4 × 6 − 3 = 21"),
      ("4 × 6 = 24, and 24 − 3 = 21.", "4 × 6 = 24، اور 24 − 3 = 21"),
      [(24, "That forgets to take away 3: 24 − 3 = 21.", "اس میں 3 تفریق کرنا بھول گئے: 24 − 3 = 21", "forgets_constant"),
       (43, "4n with n = 6 is 4 × 6 = 24, not 46. Then 24 − 3 = 21.", "n = 6 کے ساتھ 4n یعنی 4 × 6 = 24، 46 نہیں۔ پھر 24 − 3 = 21", "joins_digits")]),
   ch("q10_find_error", (f"Imran says the rule of {seq(Q10S)}, … is \"add 4\", because 6 − 2 = 4. What went wrong?", f"عمران کہتا ہے کہ {seq(Q10S)}، … کا اصول \"4 جمع کریں\" ہے، کیونکہ 6 − 2 = 4۔ کیا غلطی ہوئی؟"),
      ("He tested only the first pair. The gaps are 4, 12, 36; the rule is multiply by 3.", "اس نے صرف پہلا جوڑا جانچا۔ فرق 4، 12، 36 ہیں؛ اصول 3 سے ضرب دینا ہے۔", "Yes! A rule must fit every pair of neighbours.", "جی ہاں! اصول ہر برابر کے جوڑے پر پورا اترنا چاہیے۔"),
      [("Nothing. The first gap is 4, so the rule is add 4.", "کوئی غلطی نہیں۔ پہلا فرق 4 ہے، تو اصول 4 جمع کرنا ہے۔", "6 + 4 = 10, not 18. The rule must fit every pair.", "6 + 4 = 10، 18 نہیں۔ اصول ہر جوڑے پر پورا اترنا چاہیے۔", "first_gap_only"),
       ("He should subtract 4, because the terms are even.", "اسے 4 تفریق کرنا چاہیے، کیونکہ ارکان جفت ہیں۔", "The terms go up, so subtracting is wrong.", "ارکان بڑھ رہے ہیں، اس لیے تفریق غلط ہے۔", "wrong_direction")],
      0, qtype="find_error"),
   ch("q11_find_error_fib", (f"Amna continues {seq(Q11S)}, … (each term is the sum of the two before) with 7, because 3 + 2 = 5, so she adds 2. What went wrong?", f"آمنہ {seq(Q11S)}، … کو (ہر رکن پچھلے دو کا مجموعہ ہے) 7 سے آگے بڑھاتی ہے، کیونکہ 3 + 2 = 5، تو وہ 2 جمع کرتی ہے۔ کیا غلطی ہوئی؟"),
      ("She added a gap. The rule adds the last two terms: 3 + 5 = 8.", "اس نے فرق جمع کیا۔ اصول آخری دو ارکان جمع کرتا ہے: 3 + 5 = 8", "Yes! In this kind of pattern the gap changes every time.", "جی ہاں! اس قسم کے نمونے میں فرق ہر بار بدلتا ہے۔"),
      [("Nothing. 5 + 2 = 7 is right.", "کوئی غلطی نہیں۔ 5 + 2 = 7 درست ہے۔", "The rule is 'add the last two terms', so 3 + 5 = 8.", "اصول 'آخری دو ارکان جمع کریں' ہے، تو 3 + 5 = 8", "fib_gap"),
       ("She should multiply 5 by 2: 10.", "اسے 5 کو 2 سے ضرب دینا چاہیے: 10", "Doubling does not fit 1, 1, 2, 3, 5. Add the last two: 8.", "دگنا کرنا 1، 1، 2، 3، 5 پر پورا نہیں اترتا۔ آخری دو جمع کریں: 8", "fib_gap")],
      1, qtype="find_error"),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! You found the rules of patterns.", "شاباش! آپ نے نمونوں کے اصول ڈھونڈ لیے۔"),
    "text": T("To continue a pattern, find its rule from the gaps and check it on every pair. A pattern can add, subtract (and pass through zero), multiply, or add the last two terms. For a rule like 4n − 3, put in the position for n, multiply, then add or take away.",
              "نمونے کو آگے بڑھانے کے لیے فرق سے اس کا اصول معلوم کریں اور ہر جوڑے پر جانچیں۔ نمونہ جمع، تفریق (اور صفر سے گزرنا)، ضرب، یا آخری دو ارکان کو جمع کر سکتا ہے۔ 4n − 3 جیسے اصول میں n کی جگہ مقام رکھیں، ضرب دیں، پھر جمع یا تفریق کریں۔"),
    "points": [T("Check the rule on every pair of neighbours.", "اصول کو ہر برابر کے جوڑے پر جانچیں۔"),
               T("If the terms go down, subtract; they may pass below zero.", "اگر ارکان نیچے جائیں تو تفریق کریں؛ وہ صفر سے نیچے بھی جا سکتے ہیں۔")]},
 ],
 bank=[
   {"id": "qb_rule", "type": "recall", "step": ch("qb_rule", (f"What is the rule of the pattern {seq(QB1)}, …?", f"نمونے {seq(QB1)}، … کا اصول کیا ہے؟"),
      ("Subtract 10 each time", "ہر بار 10 تفریق کریں", "Yes! The terms go down by 10.", "جی ہاں! ارکان 10، 10 کم ہوتے ہیں۔"),
      [("Add 10 each time", "ہر بار 10 جمع کریں", "The terms get smaller, so we subtract.", "ارکان چھوٹے ہو رہے ہیں، اس لیے تفریق کرتے ہیں۔", "wrong_direction"),
       ("Divide by 10 each time", "ہر بار 10 سے تقسیم کریں", "100 ÷ 10 = 10, not 90. The terms go down by the same number: 10.", "100 ÷ 10 = 10، 90 نہیں۔ ارکان ایک ہی عدد سے کم ہوتے ہیں: 10", "always_add")],
      0, qtype=None)},
   {"id": "qb_fib", "type": "apply", "step": nq("qb_fib", (f"Each term of {seq(QB2S)}, … is the sum of the two terms before it. Write the next term.", f"{seq(QB2S)}، … کا ہر رکن اپنے سے پہلے دو ارکان کا مجموعہ ہے۔ اگلا رکن لکھیں۔"), QB2,
      ("Add the last two terms.", "آخری دو ارکان جمع کریں۔"),
      ("Right! 11 + 18 = 29.", "درست! 11 + 18 = 29"), ("The last two terms are 11 and 18: 11 + 18 = 29.", "آخری دو ارکان 11 اور 18 ہیں: 11 + 18 = 29"),
      [(25, "18 + 7 uses a gap. Add the last two terms, 11 + 18: 29.", "18 + 7 فرق کا استعمال ہے۔ آخری دو ارکان 11 + 18 جمع کریں: 29", "fib_gap")], qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": ch("qb_find_error",
      ("Sana continues 20, 17, 14, 11, … with 14, because the terms go 20, 17, 14. What went wrong?", "ثناء 20، 17، 14، 11، … کو 14 سے آگے بڑھاتی ہے، کیونکہ ارکان 20، 17، 14 ہیں۔ کیا غلطی ہوئی؟"),
      ("The terms keep going down by 3, so the next term is 11 − 3 = 8.", "ارکان 3، 3 کم ہوتے جاتے ہیں، اس لیے اگلا رکن 11 − 3 = 8 ہے۔", "Yes! The pattern does not go back up.", "جی ہاں! نمونہ واپس اوپر نہیں جاتا۔"),
      [("Nothing. The pattern repeats.", "کوئی غلطی نہیں۔ نمونہ دہراتا ہے۔", "There is no repeat: each term is 3 less than the one before.", "کوئی دہراؤ نہیں: ہر رکن پچھلے سے 3 کم ہے۔", "wrong_direction"),
       ("She should add 3: 14.", "اسے 3 جمع کرنا چاہیے: 14", "The pattern goes down, so subtract 3: 8.", "نمونہ نیچے جاتا ہے، اس لیے 3 تفریق کریں: 8", "wrong_direction")],
      0, qtype=None)},
 ],
 review=[
   {"id": "r_add", "type": "recall", "step": nq("r_add", (f"Write the 5th term of the pattern that starts at 25 and adds 6 each time: {seq(run(25, 6, 3))}, …", f"اس نمونے کا پانچواں رکن لکھیں جو 25 سے شروع ہو کر ہر بار 6 جمع کرتا ہے: {seq(run(25, 6, 3))}، …"), R1,
      ("Keep adding 6: 37, 43, …", "6 جمع کرتے جائیں: 37، 43، …"),
      ("Right! 25, 31, 37, 43, 49.", "درست! 25، 31، 37، 43، 49"), ("Add 6 twice more after 37: 43, then 49.", "37 کے بعد دو بار مزید 6 جمع کریں: 43، پھر 49"),
      [(43, "That is the 4th term. One more step: 49.", "یہ چوتھا رکن ہے۔ ایک قدم اور: 49", "first_gap_only")], qtype=None)},
   {"id": "r_down", "type": "apply", "step": nq("r_down", (f"The pattern {seq(run(8, -3, 4))}, … subtracts 3 each time. Write the 5th term.", f"نمونہ {seq(run(8, -3, 4))}، … ہر بار 3 تفریق کرتا ہے۔ پانچواں رکن لکھیں۔"), R2,
      ("−1 minus 3 goes further below zero.", "−1 منفی 3 صفر سے اور نیچے جاتا ہے۔"),
      ("Right! −1 − 3 = −4.", "درست! −1 − 3 = −4"), ("Subtract 3 from −1: −4.", "−1 میں سے 3 تفریق کریں: −4"),
      [(-2, "−1 − 3 is −4, not −2. Count 3 steps down from −1.", "−1 − 3 یعنی −4، −2 نہیں۔ −1 سے 3 قدم نیچے گنیں۔", "negative_step")], qtype=None)},
 ],
 glossary=[T("Pattern", "نمونہ"), T("Sequence", "سلسلہ"), T("Term", "رکن"), T("Rule", "اصول"), T("Fibonacci-type sequence", "فبوناچی قسم کا سلسلہ")],
 flashcards=[
   {"id": "f_rule", "front": T("How do you find the rule of a pattern?", "نمونے کا اصول کیسے معلوم کرتے ہیں؟"),
    "back": T("Look at the gap between neighbours, then check it on every pair.", "برابر کے ارکان کا فرق دیکھیں، پھر ہر جوڑے پر جانچیں۔")},
   {"id": "f_fib", "front": T("What is a Fibonacci-type sequence?", "فبوناچی قسم کا سلسلہ کیا ہے؟"),
    "back": T("Each term is the sum of the two terms before it: 1, 1, 2, 3, 5, 8.", "ہر رکن اپنے سے پہلے دو ارکان کا مجموعہ ہوتا ہے: 1، 1، 2، 3، 5، 8")},
 ],
 home_task={"id": "h_patterns_at_home", "text": T(
   "Make up three number patterns of your own: one that adds, one that goes down below zero, and one that doubles. Write the first five terms of each and ask someone at home to find the rule.",
   "اپنے تین نمونے بنائیں: ایک جو جمع کرے، ایک جو صفر سے نیچے جائے، اور ایک جو دگنا کرے۔ ہر ایک کے پہلے پانچ ارکان لکھیں اور گھر میں کسی سے اصول ڈھونڈنے کو کہیں۔")},
 notes=["Covers stating the rule of a pattern (q1, q5, q10), continuing it by adding (q2, q7), subtracting and passing below zero (q3, q8), multiplying (q5), sequences that add the last two terms (q6, q11) and the rule of the nth term (q9).",
        "Each wrong answer is a real mistake: the first term taken as the gap, adding when the pattern goes down, a gap used on a Fibonacci-type sequence, a slip below zero, 4n read as 46, and a forgotten constant.",
        "Urdu terms to check: نمونہ / سلسلہ (pattern / sequence), رکن (term), اصول (rule). NEW Urdu term invented here: فبوناچی قسم کا سلسلہ (Fibonacci-type sequence); please check it."],
 minutes=15,
)

figs.attach(lesson, {
    "q2_next": figs.number_cards([str(x) for x in Q2S], f"Four number cards: {seq(Q2S)}, with a jump of +7 between neighbours.", f"چار نمبر کارڈ: {seq(Q2S)}، برابر کے کارڈوں کے درمیان +7 کی چھلانگ۔", jumps=["+7", "+7", "+7"]),
    "q3_down": figs.number_cards([str(x) for x in Q3S], f"Four number cards: {seq(Q3S)}, with a jump of −9 between neighbours.", f"چار نمبر کارڈ: {seq(Q3S)}، برابر کے کارڈوں کے درمیان −9 کی چھلانگ۔", jumps=["−9", "−9", "−9"]),
})
write(lesson)
