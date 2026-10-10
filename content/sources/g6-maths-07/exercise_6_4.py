"""Practice set for Exercise 6.4 of the book: add and subtract algebraic
expressions (horizontal and vertical methods), and write the perimeter of a
shape as an expression. The questions are new; only the kinds of question
follow the book."""
from common import (T, say, nq, aq, ch, practice_lesson, practice_intro, write, show,
                    collect, negate, value, EX_SKILL, ALG_LIKE_TERMS, ALG_ADD_SUBTRACT, ALG_SUBSTITUTION)
import figs

SKILL = EX_SKILL["6.4"]


def add(a, b):
    return list(collect(*a, *b))


def sub(a, b):
    """a minus b: every sign in b changes."""
    return list(collect(*a, *negate(*b)))


def wrong_sub(a, b):
    """The common slip: only the first term of b is taken away."""
    (c, v), *rest = b
    return list(collect(*a, (-c, v), *rest))


# q1
A1, B1 = [(3, "x"), (5, "")], [(2, "x"), (4, "")]
Q1 = add(A1, B1)
assert Q1 == [(5, "x"), (9, "")]
# q2
A2, B2 = [(6, "a"), (-2, "b")], [(1, "a"), (5, "b")]
Q2 = add(A2, B2)
assert Q2 == [(7, "a"), (3, "b")]
# q3
A3, B3 = [(9, "m"), (7, "")], [(4, "m"), (2, "")]
Q3 = sub(A3, B3)
assert Q3 == [(5, "m"), (5, "")] and wrong_sub(A3, B3) == [(5, "m"), (9, "")]
# q4: subtract 5p - 3 from 8p + 1
A4, B4 = [(8, "p"), (1, "")], [(5, "p"), (-3, "")]
Q4 = sub(A4, B4)
assert Q4 == [(3, "p"), (4, "")] and wrong_sub(A4, B4) == [(3, "p"), (-2, "")]
assert sub(B4, A4) != Q4
# q5: from 10a + 4b take away 6a + b
A5, B5 = [(10, "a"), (4, "b")], [(6, "a"), (1, "b")]
Q5 = sub(A5, B5)
assert Q5 == [(4, "a"), (3, "b")] and wrong_sub(A5, B5) == [(4, "a"), (5, "b")]
# q6: triangle with sides 2x + 1, 3x + 2, x + 4
SIDES6 = [[(2, "x"), (1, "")], [(3, "x"), (2, "")], [(1, "x"), (4, "")]]
Q6 = list(collect(*[t for s in SIDES6 for t in s]))
assert Q6 == [(6, "x"), (7, "")]
Q6_WRONG = [(9, "x")]
# q7: the perimeter at x = 3
Q7 = value("6x + 7", x=3)
assert Q7 == sum(value(f"{s[0][0]}x + {s[1][0]}", x=3) for s in SIDES6) == 25
assert int("63") + 7 == 70 and 6 + 3 + 7 == 16
# q8: rectangle with length 5n + 3 and breadth 2n + 1
L8, W8 = [(5, "n"), (3, "")], [(2, "n"), (1, "")]
Q8 = list(collect(*L8, *W8, *L8, *W8))
assert Q8 == [(14, "n"), (8, "")]
Q8_WRONG = list(collect(*L8, *W8))
assert Q8_WRONG == [(7, "n"), (4, "")]
# q9: the rectangle at n = 2
Q9 = value("14n + 8", n=2)
assert Q9 == 2 * (value("5n + 3", n=2) + value("2n + 1", n=2)) == 36 and 36 // 2 == 18
# q10: (7y + 9) - (3y + 4)
A10, B10 = [(7, "y"), (9, "")], [(3, "y"), (4, "")]
assert sub(A10, B10) == [(4, "y"), (5, "")] and wrong_sub(A10, B10) == [(4, "y"), (13, "")]
# q11: 5m + 2 and 3m + 4
A11, B11 = [(5, "m"), (2, "")], [(3, "m"), (4, "")]
assert add(A11, B11) == [(8, "m"), (6, "")] and 5 + 2 + 3 + 4 == 14
# check each result by substitution
for a, b in ((A1, B1), (A2, B2), (A11, B11)):
    for v in range(1, 6):
        e = lambda t: sum(c * (v if var else 1) for c, var in t)
        assert e(add(a, b)) == e(a) + e(b)
for a, b in ((A3, B3), (A4, B4), (A5, B5), (A10, B10)):
    for v in range(1, 6):
        e = lambda t: sum(c * (v if var else 1) for c, var in t)
        assert e(sub(a, b)) == e(a) - e(b)
# bank and review
QB = add([(2, "k"), (6, "")], [(5, "k"), (1, "")])
assert QB == [(7, "k"), (7, "")]
QBS = sub([(9, "d"), (8, "")], [(4, "d"), (3, "")])
assert QBS == [(5, "d"), (5, "")]
R1 = add([(3, "x"), (4, "y")], [(2, "x"), (-1, "y")])
assert R1 == [(5, "x"), (3, "y")]
SQ = [(3, "s")]
R2 = list(collect(*SQ, *SQ, *SQ, *SQ))
assert R2 == [(12, "s")]

lesson = practice_lesson(
 "6.4", script="exercise_6_4.py",
 title=T("Exercise 6.4 practice: adding and subtracting", "مشق 6.4 کی پریکٹس: جمع اور تفریق"),
 outcome="Add and subtract algebraic expressions by the horizontal and the vertical method, and write the perimeter of a shape as an expression.",
 prerequisites=[ALG_LIKE_TERMS, ALG_ADD_SUBTRACT, ALG_SUBSTITUTION],
 misconceptions=[
   {"id": "first_term_only", "description": "When subtracting a bracket, changes the sign of only the first term inside it."},
   {"id": "unlike_joined", "description": "Adds terms with different letters, or all the numbers, into one term."},
   {"id": "subtract_reversed", "description": "Subtracts in the wrong order when asked to take one expression from another."},
   {"id": "perimeter_missing_sides", "description": "Adds only some of the sides when finding a perimeter."},
   {"id": "joins_digits", "description": "Reads 6x with x = 3 as 63 instead of 6 × 3."},
   {"id": "adds_letter", "description": "Adds the value of the letter instead of multiplying by the coefficient."},
   {"id": "half_perimeter", "description": "Gives the length plus the breadth as the perimeter of a rectangle."},
 ],
 steps=[
   practice_intro("6.4",
     "Here you add and subtract expressions, by the horizontal and the vertical method, and write the perimeter of a shape as an expression.",
     "اس میں آپ عبارتوں کو جمع اور تفریق کریں گے، افقی اور عمودی طریقے سے، اور کسی شکل کا احاطہ عبارت کی صورت میں لکھیں گے۔",
     "Exercise 6.4 is about adding and subtracting expressions. Ready?", "مشق 6.4 عبارتوں کو جمع اور تفریق کرنے کے بارے میں ہے۔ تیار؟"),
   aq("q1_add", (f"Add: ({show(A1)}) + ({show(B1)})", f"جمع کریں: ({show(A1)}) + ({show(B1)})"), Q1,
      ("Add the x-terms together and the numbers together.", "x والے ارکان اکٹھے اور اعداد اکٹھے جمع کریں۔"),
      ("Right! 3x + 2x = 5x and 5 + 4 = 9: 5x + 9.", "درست! 3x + 2x = 5x اور 5 + 4 = 9: 5x + 9"),
      ("x-terms: 3x + 2x = 5x. Numbers: 5 + 4 = 9. So 5x + 9.", "x والے: 3x + 2x = 5x۔ اعداد: 5 + 4 = 9۔ تو 5x + 9"),
      [([(14, "x")], "x-terms and numbers are unlike terms, so they stay apart: 5x + 9.", "x والے ارکان اور اعداد غیر یکساں ارکان ہیں، اس لیے الگ رہتے ہیں: 5x + 9", "unlike_joined")], qtype="recall"),
   aq("q2_add_two", (f"Add: ({show(A2)}) + ({show(B2)})", f"جمع کریں: ({show(A2)}) + ({show(B2)})"), Q2,
      ("Group the a-terms, then the b-terms. a means 1a.", "a والے ارکان، پھر b والے ارکان اکٹھے کریں۔ a یعنی 1a"),
      ("Right! 6a + a = 7a and −2b + 5b = 3b: 7a + 3b.", "درست! 6a + a = 7a اور −2b + 5b = 3b: 7a + 3b"),
      ("a-terms: 6a + 1a = 7a. b-terms: −2b + 5b = 3b. So 7a + 3b.", "a والے: 6a + 1a = 7a۔ b والے: −2b + 5b = 3b۔ تو 7a + 3b"),
      [([(7, "a"), (-7, "b")], "−2b + 5b is 3b, not −7b. Add a minus and a plus by finding the difference: 3b.", "−2b + 5b برابر 3b ہے، −7b نہیں۔ منفی اور مثبت جمع کرنے کے لیے فرق نکالیں: 3b", "unlike_joined")], qtype="recall"),
   {"id": "s_rule", "type": "explain",
    "character": say("thinking", "Adding: collect like terms. Subtracting: change every sign in the second bracket first!", "جمع: یکساں ارکان اکٹھے کریں۔ تفریق: پہلے دوسری بریکٹ کی ہر علامت بدلیں!"),
    "text": T("To add expressions, group the like terms and add their coefficients: (3x + 5) + (2x + 4) = 5x + 9. In the vertical method we write the expressions under each other with like terms in the same column; in the horizontal method we write them on one line. To subtract an expression, change the sign of EVERY term in it, then add: (9m + 7) − (4m + 2) = 9m + 7 − 4m − 2 = 5m + 5. The perimeter of a shape is the sum of all its sides, so it is an expression too.",
              "عبارتیں جمع کرنے کے لیے یکساں ارکان اکٹھے کریں اور ان کے عددی سر جمع کریں: (3x + 5) + (2x + 4) = 5x + 9۔ عمودی طریقے میں عبارتیں ایک کے نیچے ایک لکھتے ہیں اور یکساں ارکان ایک ہی ستون میں رکھتے ہیں؛ افقی طریقے میں انھیں ایک ہی سطر میں لکھتے ہیں۔ کسی عبارت کو تفریق کرنے کے لیے اس کے ہر رکن کی علامت بدلیں، پھر جمع کریں: (9m + 7) − (4m + 2) = 9m + 7 − 4m − 2 = 5m + 5۔ شکل کا احاطہ اس کے تمام اضلاع کا مجموعہ ہے، اس لیے یہ بھی عبارت ہے۔")},
   aq("q3_subtract", (f"Subtract: ({show(A3)}) − ({show(B3)})", f"تفریق کریں: ({show(A3)}) − ({show(B3)})"), Q3,
      ("Change the sign of both terms in the second bracket, then collect.", "دوسری بریکٹ کے دونوں ارکان کی علامت بدلیں، پھر اکٹھا کریں۔"),
      ("Right! 9m − 4m = 5m and 7 − 2 = 5: 5m + 5.", "درست! 9m − 4m = 5m اور 7 − 2 = 5: 5m + 5"),
      ("9m + 7 − 4m − 2 = 5m + 5.", "9m + 7 − 4m − 2 = 5m + 5"),
      [(wrong_sub(A3, B3), "The 2 is taken away too: 7 − 2 = 5, so 5m + 5.", "2 بھی تفریق ہوتا ہے: 7 − 2 = 5، تو 5m + 5", "first_term_only")]),
   aq("q4_subtract_from", (f"Subtract {show(B4)} from {show(A4)}.", f"{show(A4)} میں سے {show(B4)} تفریق کریں۔"), Q4,
      ("Write the one you start from first: (8p + 1) − (5p − 3). Change both signs in the second bracket.", "جس سے شروع کر رہے ہیں اسے پہلے لکھیں: (8p + 1) − (5p − 3)۔ دوسری بریکٹ کی دونوں علامتیں بدلیں۔"),
      ("Right! 8p + 1 − 5p + 3 = 3p + 4.", "درست! 8p + 1 − 5p + 3 = 3p + 4"),
      ("(8p + 1) − (5p − 3) = 8p + 1 − 5p + 3 = 3p + 4.", "(8p + 1) − (5p − 3) = 8p + 1 − 5p + 3 = 3p + 4"),
      [(wrong_sub(A4, B4), "Taking away −3 gives +3, not −3: 3p + 4.", "−3 تفریق کرنے سے +3 ملتا ہے، −3 نہیں: 3p + 4", "first_term_only"),
       (sub(B4, A4), "That subtracts the other way round. Start from 8p + 1: 3p + 4.", "یہ الٹی طرف سے تفریق ہے۔ 8p + 1 سے شروع کریں: 3p + 4", "subtract_reversed")]),
   aq("q5_take_away", (f"Take away {show(B5)} from {show(A5)}.", f"{show(A5)} میں سے {show(B5)} نکالیں۔"), Q5,
      ("Both terms of 6a + b are taken away. b means 1b.", "6a + b کے دونوں ارکان نکالے جاتے ہیں۔ b یعنی 1b"),
      ("Right! 10a − 6a = 4a and 4b − b = 3b: 4a + 3b.", "درست! 10a − 6a = 4a اور 4b − b = 3b: 4a + 3b"),
      ("10a + 4b − 6a − b = 4a + 3b.", "10a + 4b − 6a − b = 4a + 3b"),
      [(wrong_sub(A5, B5), "The b is taken away too: 4b − b = 3b, so 4a + 3b.", "b بھی نکالا جاتا ہے: 4b − b = 3b، تو 4a + 3b", "first_term_only")]),
   aq("q6_perimeter", (f"The sides of a triangle are {show(SIDES6[0])}, {show(SIDES6[1])} and {show(SIDES6[2])} (in cm). Write its perimeter as an expression.", f"ایک تکون کے اضلاع {show(SIDES6[0])}، {show(SIDES6[1])} اور {show(SIDES6[2])} (سینٹی میٹر میں) ہیں۔ اس کا احاطہ عبارت کی صورت میں لکھیں۔"), Q6,
      ("Add all three sides, then collect the like terms.", "تینوں اضلاع جمع کریں، پھر یکساں ارکان اکٹھے کریں۔"),
      ("Right! 6x + 7.", "درست! 6x + 7"),
      ("2x + 3x + x = 6x and 1 + 2 + 4 = 7. So 6x + 7.", "2x + 3x + x = 6x اور 1 + 2 + 4 = 7۔ تو 6x + 7"),
      [(Q6_WRONG, "Only the x-terms can be added together: 6x. The numbers add to 7: 6x + 7.", "صرف x والے ارکان آپس میں جمع ہوتے ہیں: 6x۔ اعداد کا مجموعہ 7 ہے: 6x + 7", "unlike_joined")]),
   nq("q7_perimeter_value", ("Using 6x + 7 for the perimeter, find it when x = 3.", "احاطے کے لیے 6x + 7 استعمال کریں اور x = 3 ہو تو اس کی قیمت معلوم کریں۔"), Q7,
      ("6x means 6 × x.", "6x یعنی 6 × x"),
      ("Right! 6 × 3 + 7 = 25 cm.", "درست! 6 × 3 + 7 = 25 سینٹی میٹر"),
      ("6 × 3 = 18, and 18 + 7 = 25.", "6 × 3 = 18، اور 18 + 7 = 25"),
      [(70, "6x is 6 × 3, not 63. Then 18 + 7 = 25.", "6x یعنی 6 × 3، 63 نہیں۔ پھر 18 + 7 = 25", "joins_digits"),
       (16, "6x means 6 times x, not 6 + x. 18 + 7 = 25.", "6x یعنی x کا 6 گنا، 6 + x نہیں۔ 18 + 7 = 25", "adds_letter")]),
   aq("q8_rectangle", (f"A rectangle has length {show(L8)} and breadth {show(W8)} (in cm). Write its perimeter by adding all four sides.", f"ایک مستطیل کی لمبائی {show(L8)} اور چوڑائی {show(W8)} (سینٹی میٹر میں) ہے۔ چاروں اضلاع جمع کر کے اس کا احاطہ لکھیں۔"), Q8,
      ("A rectangle has two lengths and two breadths.", "مستطیل کی دو لمبائیاں اور دو چوڑائیاں ہوتی ہیں۔"),
      ("Right! 14n + 8.", "درست! 14n + 8"),
      ("(5n + 3) + (2n + 1) + (5n + 3) + (2n + 1) = 14n + 8.", "(5n + 3) + (2n + 1) + (5n + 3) + (2n + 1) = 14n + 8"),
      [(Q8_WRONG, "That is only length + breadth. The perimeter has all four sides: 14n + 8.", "یہ صرف لمبائی + چوڑائی ہے۔ احاطے میں چاروں اضلاع ہوتے ہیں: 14n + 8", "perimeter_missing_sides")]),
   nq("q9_rect_value", ("Using 14n + 8 for the perimeter, find it when n = 2.", "احاطے کے لیے 14n + 8 استعمال کریں اور n = 2 ہو تو اس کی قیمت معلوم کریں۔"), Q9,
      ("Put n = 2 in.", "n = 2 رکھیں۔"),
      ("Right! 14 × 2 + 8 = 36 cm.", "درست! 14 × 2 + 8 = 36 سینٹی میٹر"),
      ("14 × 2 = 28, and 28 + 8 = 36.", "14 × 2 = 28، اور 28 + 8 = 36"),
      [(18, "That is half: length + breadth. The perimeter is 36.", "یہ آدھا ہے: لمبائی + چوڑائی۔ احاطہ 36 ہے۔", "half_perimeter")]),
   ch("q10_find_error", (f"Hamid works out ({show(A10)}) − ({show(B10)}) as 7y + 9 − 3y + 4 = 4y + 13. What went wrong?", f"حامد ({show(A10)}) − ({show(B10)}) کو 7y + 9 − 3y + 4 = 4y + 13 حل کرتا ہے۔ کیا غلطی ہوئی؟"),
      ("He changed only the first sign. The 4 is taken away too: 7y + 9 − 3y − 4 = 4y + 5.", "اس نے صرف پہلی علامت بدلی۔ 4 بھی تفریق ہوتا ہے: 7y + 9 − 3y − 4 = 4y + 5", "Yes! Change every sign in the second bracket.", "جی ہاں! دوسری بریکٹ کی ہر علامت بدلیں۔"),
      [("Nothing. 4y + 13 is right.", "کوئی غلطی نہیں۔ 4y + 13 درست ہے۔", "Test y = 1: (7 + 9) − (3 + 4) = 9, but 4 + 13 = 17.", "y = 1 لیں: (7 + 9) − (3 + 4) = 9، مگر 4 + 13 = 17", "first_term_only"),
       ("He should add the brackets instead.", "اسے بریکٹیں جمع کرنی چاہییں۔", "The question says subtract. The mistake is the sign of the 4.", "سوال میں تفریق کہی گئی ہے۔ غلطی 4 کی علامت میں ہے۔", "subtract_reversed")],
      0, qtype="find_error"),
   ch("q11_find_error_add", (f"Saad adds ({show(A11)}) and ({show(B11)}) and gets 14m, because 5 + 2 + 3 + 4 = 14. What went wrong?", f"سعد ({show(A11)}) اور ({show(B11)}) کو جمع کر کے 14m لکھتا ہے، کیونکہ 5 + 2 + 3 + 4 = 14۔ کیا غلطی ہوئی؟"),
      ("He added numbers and m-terms together. The answer is 8m + 6.", "اس نے اعداد اور m والے ارکان کو ملا دیا۔ جواب 8m + 6 ہے۔", "Yes! Only like terms can be added together.", "جی ہاں! صرف یکساں ارکان آپس میں جمع ہو سکتے ہیں۔"),
      [("Nothing. All the numbers can be added.", "کوئی غلطی نہیں۔ تمام اعداد جمع ہو سکتے ہیں۔", "Test m = 2: the sum is (10 + 2) + (6 + 4) = 22, but 14m = 28. The answer is 8m + 6.", "m = 2 لیں: مجموعہ (10 + 2) + (6 + 4) = 22 ہے، مگر 14m = 28۔ جواب 8m + 6 ہے۔", "unlike_joined"),
       ("He should multiply instead of adding.", "اسے جمع کی جگہ ضرب دینی چاہیے۔", "The question says add. The mistake is joining unlike terms.", "سوال میں جمع کہا گیا ہے۔ غلطی غیر یکساں ارکان کو ملانا ہے۔", "unlike_joined")],
      2, qtype="find_error"),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! You added and subtracted expressions.", "شاباش! آپ نے عبارتیں جمع اور تفریق کیں۔"),
    "text": T("Add expressions by grouping like terms. To subtract, change every sign in the second expression, then group. Take one expression from another by starting with the one you take from. A perimeter is all the sides added; a rectangle has two lengths and two breadths. Check an answer by putting in a small number.",
              "عبارتیں جمع کرنے کے لیے یکساں ارکان اکٹھے کریں۔ تفریق کے لیے دوسری عبارت کی ہر علامت بدلیں، پھر اکٹھا کریں۔ ایک عبارت میں سے دوسری نکالتے وقت اس سے شروع کریں جس میں سے نکال رہے ہیں۔ احاطہ تمام اضلاع کا مجموعہ ہے؛ مستطیل کی دو لمبائیاں اور دو چوڑائیاں ہوتی ہیں۔ جواب کو چھوٹا عدد رکھ کر جانچیں۔"),
    "points": [T("Change every sign in the bracket you subtract.", "جس بریکٹ کو تفریق کر رہے ہیں اس کی ہر علامت بدلیں۔"),
               T("Only like terms join together.", "صرف یکساں ارکان آپس میں ملتے ہیں۔")]},
 ],
 bank=[
   {"id": "qb_add", "type": "recall", "step": aq("qb_add", (f"Add: ({show([(2, 'k'), (6, '')])}) + ({show([(5, 'k'), (1, '')])})", f"جمع کریں: ({show([(2, 'k'), (6, '')])}) + ({show([(5, 'k'), (1, '')])})"), QB,
      ("Add the k-terms and the numbers separately.", "k والے ارکان اور اعداد الگ الگ جمع کریں۔"),
      ("Right! 7k + 7.", "درست! 7k + 7"), ("2k + 5k = 7k and 6 + 1 = 7.", "2k + 5k = 7k اور 6 + 1 = 7"),
      [([(14, "k")], "k-terms and numbers are unlike terms: 7k + 7.", "k والے ارکان اور اعداد غیر یکساں ارکان ہیں: 7k + 7", "unlike_joined")], qtype=None)},
   {"id": "qb_subtract", "type": "apply", "step": aq("qb_subtract", (f"Subtract: ({show([(9, 'd'), (8, '')])}) − ({show([(4, 'd'), (3, '')])})", f"تفریق کریں: ({show([(9, 'd'), (8, '')])}) − ({show([(4, 'd'), (3, '')])})"), QBS,
      ("Change both signs in the second bracket.", "دوسری بریکٹ کی دونوں علامتیں بدلیں۔"),
      ("Right! 5d + 5.", "درست! 5d + 5"), ("9d + 8 − 4d − 3 = 5d + 5.", "9d + 8 − 4d − 3 = 5d + 5"),
      [(wrong_sub([(9, "d"), (8, "")], [(4, "d"), (3, "")]), "The 3 is taken away too: 8 − 3 = 5.", "3 بھی تفریق ہوتا ہے: 8 − 3 = 5", "first_term_only")], qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": ch("qb_find_error",
      ("Mina says the perimeter of a square with side 3s is 3s + 3s = 6s. What went wrong?", "مینا کہتی ہے کہ ضلع 3s والے مربع کا احاطہ 3s + 3s = 6s ہے۔ کیا غلطی ہوئی؟"),
      ("A square has four sides, so the perimeter is 3s + 3s + 3s + 3s = 12s.", "مربع کے چار اضلاع ہوتے ہیں، اس لیے احاطہ 3s + 3s + 3s + 3s = 12s ہے۔", "Yes! Add all four sides.", "جی ہاں! چاروں اضلاع جمع کریں۔"),
      [("Nothing. 6s is right.", "کوئی غلطی نہیں۔ 6s درست ہے۔", "6s is only two sides. A square has four.", "6s صرف دو اضلاع ہیں۔ مربع کے چار ہوتے ہیں۔", "perimeter_missing_sides"),
       ("It should be 3s × 3s.", "یہ 3s × 3s ہونا چاہیے۔", "Perimeter is the sum of the sides, not a product.", "احاطہ اضلاع کا مجموعہ ہے، حاصل ضرب نہیں۔", "perimeter_missing_sides")],
      0, qtype=None)},
 ],
 review=[
   {"id": "r_add", "type": "recall", "step": aq("r_add", (f"Add: ({show([(3, 'x'), (4, 'y')])}) + ({show([(2, 'x'), (-1, 'y')])})", f"جمع کریں: ({show([(3, 'x'), (4, 'y')])}) + ({show([(2, 'x'), (-1, 'y')])})"), R1,
      ("Add the x-terms and the y-terms. −y means −1y.", "x والے اور y والے ارکان جمع کریں۔ −y یعنی −1y"),
      ("Right! 5x + 3y.", "درست! 5x + 3y"), ("3x + 2x = 5x and 4y − y = 3y.", "3x + 2x = 5x اور 4y − y = 3y"),
      [([(5, "x"), (5, "y")], "−y takes one y away: 4y − y = 3y.", "−y ایک y کم کرتا ہے: 4y − y = 3y", "unlike_joined")], qtype=None)},
   {"id": "r_square", "type": "apply", "step": aq("r_square", ("Each side of a square is 3s. Write its perimeter as an expression.", "ایک مربع کا ہر ضلع 3s ہے۔ اس کا احاطہ عبارت کی صورت میں لکھیں۔"), R2,
      ("Add the four equal sides.", "چار برابر اضلاع جمع کریں۔"),
      ("Right! 12s.", "درست! 12s"), ("3s + 3s + 3s + 3s = 12s.", "3s + 3s + 3s + 3s = 12s"),
      [([(6, "s")], "A square has four sides, not two: 12s.", "مربع کے چار اضلاع ہوتے ہیں، دو نہیں: 12s", "perimeter_missing_sides")], qtype=None)},
 ],
 glossary=[T("Add", "جمع کرنا"), T("Subtract", "تفریق کرنا"), T("Like terms", "یکساں ارکان"), T("Perimeter", "احاطہ"), T("Vertical method", "عمودی طریقہ"), T("Horizontal method", "افقی طریقہ")],
 flashcards=[
   {"id": "f_subtract", "front": T("How do you subtract an expression?", "عبارت کو تفریق کیسے کرتے ہیں؟"),
    "back": T("Change the sign of every term in it, then collect like terms.", "اس کے ہر رکن کی علامت بدلیں، پھر یکساں ارکان اکٹھے کریں۔")},
   {"id": "f_perimeter", "front": T("Perimeter as an expression?", "احاطہ بطور عبارت؟"),
    "back": T("Add all the sides, then group the like terms.", "تمام اضلاع جمع کریں، پھر یکساں ارکان اکٹھے کریں۔")},
 ],
 home_task={"id": "h_perimeter_at_home", "text": T(
   "Measure the sides of a book cover or a table in hand spans. Call the length of one span s and write each side as a multiple of s. Then write the perimeter as an expression.",
   "کسی کتاب کے سرورق یا میز کے اضلاع بالشت سے ناپیں۔ ایک بالشت کی لمبائی کو s کہیں اور ہر ضلع کو s کے ضرب کی صورت میں لکھیں۔ پھر احاطہ عبارت کی صورت میں لکھیں۔")},
 notes=["Covers adding expressions (q1, q2, q11), subtracting them, also with 'from' and 'take away' (q3, q4, q5, q10), and the perimeter of a triangle and a rectangle as an expression and its value (q6 to q9). The vertical method is described in the explanation; answers are typed on one line.",
        "Each wrong answer is a real mistake: only the first sign changed, unlike terms joined, subtracting the wrong way round, sides left out of a perimeter, 6x read as 63, and the length plus breadth given as the perimeter.",
        "Urdu terms to check: جمع کرنا / تفریق کرنا (add / subtract), یکساں ارکان / غیر یکساں ارکان (like / unlike terms), احاطہ (perimeter), عمودی طریقہ / افقی طریقہ (vertical / horizontal method), بریکٹ (bracket). The vertical and horizontal method names are NEW Urdu terms invented here; please check them."],
 minutes=18,
)

figs.attach(lesson, {
    "q6_perimeter": figs.triangle_sides([show(SIDES6[0]), show(SIDES6[2]), show(SIDES6[1])], "A triangle with sides 2x + 1 on the left, x + 4 on the right and 3x + 2 along the bottom.", "ایک تکون جس کا بایاں ضلع 2x + 1، دایاں ضلع x + 4 اور نچلا ضلع 3x + 2 ہے۔"),
})
write(lesson)
