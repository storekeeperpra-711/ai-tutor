"""Practice set for Exercise 6.5 of the book: remove brackets and simplify, and
evaluate expressions for given values. The questions are new; only the kinds of
question follow the book."""
from common import (T, say, nq, aq, ch, practice_lesson, practice_intro, write, show,
                    collect, negate, value, EX_SKILL, ALG_LIKE_TERMS, ALG_ADD_SUBTRACT, ALG_SUBSTITUTION)
import figs

SKILL = EX_SKILL["6.5"]


def plus(a, b):
    """a + (b): the bracket opens with no change."""
    return list(collect(*a, *b))


def minus(a, b):
    """a - (b): every sign in the bracket changes."""
    return list(collect(*a, *negate(*b)))


def keep_signs(a, b):
    """The common slip: a - (b) opened by changing only the first sign."""
    (c, v), *rest = b
    return list(collect(*a, (-c, v), *rest))


def evaluate(terms, **values):
    return sum(c * (values[v] if v else 1) for c, v in terms)


# q1: 25 - (8 + 3)
Q1 = 25 - (8 + 3)
assert Q1 == 14 and 25 - 8 + 3 == 20
# q2: 7x + (3x - 2)
A2, B2 = [(7, "x")], [(3, "x"), (-2, "")]
Q2 = plus(A2, B2)
assert Q2 == [(10, "x"), (-2, "")]
# q3: 9a - (2a + 5)
A3, B3 = [(9, "a")], [(2, "a"), (5, "")]
Q3 = minus(A3, B3)
assert Q3 == [(7, "a"), (-5, "")] and keep_signs(A3, B3) == [(7, "a"), (5, "")]
# q4: 5x - (x - 4)
A4, B4 = [(5, "x")], [(1, "x"), (-4, "")]
Q4 = minus(A4, B4)
assert Q4 == [(4, "x"), (4, "")] and [(4, "x"), (-4, "")] != Q4
assert evaluate(Q4, x=3) == evaluate(A4, x=3) - evaluate(B4, x=3) == 16
# q5: 20 - {6 + (9 - 4)}
Q5 = 20 - (6 + (9 - 4))
assert Q5 == 9 and 20 - 6 + 9 - 4 == 19 and 20 - (6 + 9) - 4 == 1
# q6: 6y - (y - 3) + 2y
Q6 = list(collect((6, "y"), *negate((1, "y"), (-3, "")), (2, "y")))
assert Q6 == [(7, "y"), (3, "")]
Q6_WRONG = list(collect((6, "y"), (1, "y"), (-3, ""), (2, "y")))
assert Q6_WRONG == [(9, "y"), (-3, "")] and Q6_WRONG != Q6
for v in range(1, 6):
    assert evaluate(Q6, y=v) == 6 * v - (v - 3) + 2 * v
# q7: 5a + 3 when a = 4
Q7 = value("5a + 3", a=4)
assert Q7 == 23 and int("54") + 3 == 57
# q8: 7 - 2b when b = 3
Q8 = value("7 - 2b", b=3)
assert Q8 == 1 and (7 - 2) * 3 == 15
# q9: 4p - q + 6 when p = 5, q = 8
Q9 = 4 * 5 - 8 + 6
assert Q9 == 18 and 4 * 5 + 8 + 6 == 34
# q10: (6m + 5) - (2m + 1) then m = 3
A10, B10 = [(6, "m"), (5, "")], [(2, "m"), (1, "")]
S10 = minus(A10, B10)
Q10 = evaluate(S10, m=3)
assert S10 == [(4, "m"), (4, "")] and Q10 == 16 == evaluate(A10, m=3) - evaluate(B10, m=3)
assert evaluate(keep_signs(A10, B10), m=3) != Q10 and evaluate([(4, "m"), (6, "")], m=3) == 18
# q11: 9 - (3 + k) is 6 - k, not 9 - 3 + k
Q11 = minus([(9, "")], [(3, ""), (1, "k")])
assert Q11 == [(-1, "k"), (6, "")] and keep_signs([(9, "")], [(3, ""), (1, "k")]) != Q11
# q12: 3x + 2 when x = 5
Q12 = value("3x + 2", x=5)
assert Q12 == 17 and int("35") + 2 == 37
# bank and review
QB = 30 - (12 + 5)
assert QB == 13 and 30 - 12 + 5 == 23
QBE = value("8c - 5", c=3)
assert QBE == 19 and int("83") - 5 == 78
R1 = minus([(8, "b")], [(3, "b"), (2, "")])
assert R1 == [(5, "b"), (-2, "")]
R2 = evaluate([(2, "u"), (3, "v")], u=4, v=5)
assert R2 == 23 and int("24") + int("35") == 59

lesson = practice_lesson(
 "6.5", script="exercise_6_5.py",
 title=T("Exercise 6.5 practice: brackets and values", "مشق 6.5 کی پریکٹس: بریکٹیں اور قیمتیں"),
 outcome="Remove brackets and simplify expressions, and find the value of an expression for given values of the letters.",
 prerequisites=[ALG_LIKE_TERMS, ALG_ADD_SUBTRACT, ALG_SUBSTITUTION],
 misconceptions=[
   {"id": "sign_not_changed", "description": "Opens a bracket after a minus sign without changing the signs inside it."},
   {"id": "first_term_only", "description": "Changes only the first sign inside a bracket that follows a minus."},
   {"id": "brackets_ignored", "description": "Ignores the brackets and works from left to right."},
   {"id": "outer_first", "description": "Works out the outside bracket before the inside one."},
   {"id": "joins_digits", "description": "Reads 5a with a = 4 as 54 instead of 5 × 4."},
   {"id": "minus_sign_lost", "description": "Treats a minus in front of a letter term as a plus when putting in values."},
   {"id": "subtract_before_multiply", "description": "Subtracts before multiplying, against BODMAS."},
 ],
 steps=[
   practice_intro("6.5",
     "Here you remove brackets and simplify, and find the value of an expression for given values of the letters.",
     "اس میں آپ بریکٹیں ہٹا کر عبارت کو مختصر کریں گے، اور حروف کی دی گئی قیمتوں کے لیے عبارت کی قیمت معلوم کریں گے۔",
     "Exercise 6.5 is about brackets and values. Ready?", "مشق 6.5 بریکٹوں اور قیمتوں کے بارے میں ہے۔ تیار؟"),
   nq("q1_number", ("Work out: 25 − (8 + 3)", "حل کریں: 25 − (8 + 3)"), Q1,
      ("Do the bracket first.", "پہلے بریکٹ حل کریں۔"),
      ("Right! (8 + 3) = 11, and 25 − 11 = 14.", "درست! (8 + 3) = 11، اور 25 − 11 = 14"),
      ("The bracket is 11. 25 − 11 = 14.", "بریکٹ 11 ہے۔ 25 − 11 = 14"),
      [(20, "25 − 8 + 3 takes away only 8 and adds 3. The whole bracket is taken away: 14.", "25 − 8 + 3 صرف 8 تفریق کرتا ہے اور 3 جمع کرتا ہے۔ پوری بریکٹ تفریق ہوتی ہے: 14", "sign_not_changed")], qtype="recall"),
   aq("q2_plus_bracket", (f"Remove the brackets and simplify: {show(A2)} + ({show(B2)})", f"بریکٹ ہٹا کر مختصر کریں: {show(A2)} + ({show(B2)})"), Q2,
      ("A plus in front of a bracket changes nothing inside.", "بریکٹ کے آگے جمع ہو تو اندر کچھ نہیں بدلتا۔"),
      ("Right! 7x + 3x − 2 = 10x − 2.", "درست! 7x + 3x − 2 = 10x − 2"),
      ("The bracket opens as it is: 7x + 3x − 2 = 10x − 2.", "بریکٹ جوں کی توں کھلتی ہے: 7x + 3x − 2 = 10x − 2"),
      [([(10, "x"), (2, "")], "The −2 keeps its minus sign: 10x − 2.", "−2 اپنی منفی کی علامت رکھتا ہے: 10x − 2", "sign_not_changed")], qtype="recall"),
   {"id": "s_rule", "type": "explain",
    "character": say("thinking", "A plus before a bracket changes nothing. A minus changes EVERY sign inside!", "بریکٹ کے آگے جمع ہو تو کچھ نہیں بدلتا۔ منفی ہو تو اندر کی ہر علامت بدلتی ہے!"),
    "text": T("To remove a bracket with + in front, write the terms as they are: 7x + (3x − 2) = 7x + 3x − 2. With − in front, change every sign inside: 9a − (2a + 5) = 9a − 2a − 5 = 7a − 5. With brackets inside brackets, work from the inside out, following BODMAS. To evaluate an expression, put the numbers in for the letters: 5a + 3 with a = 4 is 5 × 4 + 3 = 23. Multiply before you add or subtract, and keep the minus signs.",
              "جس بریکٹ کے آگے + ہو اسے ہٹانے کے لیے ارکان جیسے ہیں ویسے لکھیں: 7x + (3x − 2) = 7x + 3x − 2۔ آگے − ہو تو اندر کی ہر علامت بدلیں: 9a − (2a + 5) = 9a − 2a − 5 = 7a − 5۔ بریکٹ کے اندر بریکٹ ہو تو اندر سے باہر کی طرف حل کریں، BODMAS کے مطابق۔ عبارت کی قیمت معلوم کرنے کے لیے حروف کی جگہ اعداد رکھیں: a = 4 کے ساتھ 5a + 3 برابر 5 × 4 + 3 = 23 ہے۔ جمع یا تفریق سے پہلے ضرب دیں، اور منفی کی علامتیں رکھیں۔")},
   aq("q3_minus_bracket", (f"Remove the brackets and simplify: {show(A3)} − ({show(B3)})", f"بریکٹ ہٹا کر مختصر کریں: {show(A3)} − ({show(B3)})"), Q3,
      ("A minus in front changes the sign of 2a AND of 5.", "آگے منفی ہو تو 2a اور 5 دونوں کی علامت بدلتی ہے۔"),
      ("Right! 9a − 2a − 5 = 7a − 5.", "درست! 9a − 2a − 5 = 7a − 5"),
      ("9a − 2a − 5 = 7a − 5.", "9a − 2a − 5 = 7a − 5"),
      [(keep_signs(A3, B3), "The 5 is taken away too, so it becomes −5: 7a − 5.", "5 بھی تفریق ہوتا ہے، اس لیے یہ −5 بنتا ہے: 7a − 5", "first_term_only")]),
   aq("q4_minus_negative", (f"Remove the brackets and simplify: {show(A4)} − ({show(B4)})", f"بریکٹ ہٹا کر مختصر کریں: {show(A4)} − ({show(B4)})"), Q4,
      ("The signs inside are + for x and − for 4. Change both.", "اندر x کی علامت + اور 4 کی − ہے۔ دونوں بدلیں۔"),
      ("Right! 5x − x + 4 = 4x + 4.", "درست! 5x − x + 4 = 4x + 4"),
      ("−(−4) becomes +4: 5x − x + 4 = 4x + 4.", "−(−4) بن جاتا ہے +4: 5x − x + 4 = 4x + 4"),
      [([(4, "x"), (-4, "")], "Taking away −4 gives +4, not −4: 4x + 4.", "−4 کو تفریق کرنے سے +4 ملتا ہے، −4 نہیں: 4x + 4", "first_term_only")]),
   nq("q5_nested", ("Work out: 20 − {6 + (9 − 4)}", "حل کریں: 20 − {6 + (9 − 4)}"), Q5,
      ("Start with the inside bracket ( ), then the { }.", "اندر کی بریکٹ ( ) سے شروع کریں، پھر { }۔"),
      ("Right! (9 − 4) = 5, then {6 + 5} = 11, and 20 − 11 = 9.", "درست! (9 − 4) = 5، پھر {6 + 5} = 11، اور 20 − 11 = 9"),
      ("Inside first: 9 − 4 = 5. Then 6 + 5 = 11. Then 20 − 11 = 9.", "پہلے اندر: 9 − 4 = 5۔ پھر 6 + 5 = 11۔ پھر 20 − 11 = 9"),
      [(19, "That drops the brackets and the signs. Work from the inside: 20 − 11 = 9.", "یہ بریکٹیں اور علامتیں چھوڑ دیتا ہے۔ اندر سے حل کریں: 20 − 11 = 9", "brackets_ignored"),
       (1, "That does the outside bracket first: 20 − 15 − 4. Work from the inside out: 9.", "یہ باہر کی بریکٹ پہلے حل کرتا ہے: 20 − 15 − 4۔ اندر سے باہر حل کریں: 9", "outer_first")]),
   aq("q6_three_parts", ("Remove the brackets and simplify: 6y − (y − 3) + 2y", "بریکٹ ہٹا کر مختصر کریں: 6y − (y − 3) + 2y"), Q6,
      ("−(y − 3) becomes −y + 3. Then collect the y-terms.", "−(y − 3) بن جاتا ہے −y + 3۔ پھر y والے ارکان اکٹھے کریں۔"),
      ("Right! 6y − y + 3 + 2y = 7y + 3.", "درست! 6y − y + 3 + 2y = 7y + 3"),
      ("6y − y + 3 + 2y: the y-terms make 7y, plus 3. So 7y + 3.", "6y − y + 3 + 2y: y والے ارکان 7y بنتے ہیں، جمع 3۔ تو 7y + 3"),
      [(Q6_WRONG, "The minus changes the signs inside: −y and +3. That gives 7y + 3.", "منفی اندر کی علامتیں بدلتا ہے: −y اور +3۔ یوں 7y + 3 ملتا ہے۔", "sign_not_changed")]),
   nq("q7_evaluate", ("Find the value of 5a + 3 when a = 4.", "جب a = 4 ہو تو 5a + 3 کی قیمت معلوم کریں۔"), Q7,
      ("5a means 5 × a.", "5a یعنی 5 × a"),
      ("Right! 5 × 4 + 3 = 23.", "درست! 5 × 4 + 3 = 23"), ("5 × 4 = 20, and 20 + 3 = 23.", "5 × 4 = 20، اور 20 + 3 = 23"),
      [(57, "5a is 5 × 4 = 20, not 54. Then 20 + 3 = 23.", "5a یعنی 5 × 4 = 20، 54 نہیں۔ پھر 20 + 3 = 23", "joins_digits")]),
   nq("q8_evaluate_minus", ("Find the value of 7 − 2b when b = 3.", "جب b = 3 ہو تو 7 − 2b کی قیمت معلوم کریں۔"), Q8,
      ("Multiply first: 2b = 2 × 3. Then subtract.", "پہلے ضرب دیں: 2b = 2 × 3۔ پھر تفریق کریں۔"),
      ("Right! 7 − 6 = 1.", "درست! 7 − 6 = 1"), ("2 × 3 = 6, and 7 − 6 = 1.", "2 × 3 = 6، اور 7 − 6 = 1"),
      [(15, "That subtracts first: (7 − 2) × 3. Multiply first: 7 − 6 = 1.", "یہ پہلے تفریق کرتا ہے: (7 − 2) × 3۔ پہلے ضرب دیں: 7 − 6 = 1", "subtract_before_multiply")]),
   nq("q9_two_letters", ("Find the value of 4p − q + 6 when p = 5 and q = 8.", "جب p = 5 اور q = 8 ہو تو 4p − q + 6 کی قیمت معلوم کریں۔"), Q9,
      ("4p = 20. The minus sign in front of q stays.", "4p = 20۔ q کے آگے منفی کی علامت رہتی ہے۔"),
      ("Right! 20 − 8 + 6 = 18.", "درست! 20 − 8 + 6 = 18"), ("4 × 5 = 20, then 20 − 8 = 12, then 12 + 6 = 18.", "4 × 5 = 20، پھر 20 − 8 = 12، پھر 12 + 6 = 18"),
      [(34, "q is taken away, not added: 20 − 8 + 6 = 18.", "q تفریق ہوتا ہے، جمع نہیں: 20 − 8 + 6 = 18", "minus_sign_lost")]),
   nq("q10_simplify_then_value", (f"Simplify ({show(A10)}) − ({show(B10)}), then find its value when m = 3.", f"({show(A10)}) − ({show(B10)}) کو مختصر کریں، پھر m = 3 کے لیے اس کی قیمت معلوم کریں۔"), Q10,
      ("The simplified form is 4m + 4. Put m = 3 in.", "مختصر شکل 4m + 4 ہے۔ m = 3 رکھیں۔"),
      ("Right! 6m − 2m = 4m and 5 − 1 = 4, so 4m + 4. With m = 3: 12 + 4 = 16.", "درست! 6m − 2m = 4m اور 5 − 1 = 4، تو 4m + 4۔ m = 3 کے ساتھ: 12 + 4 = 16"),
      ("4m + 4 with m = 3 is 4 × 3 + 4 = 16.", "m = 3 کے ساتھ 4m + 4 برابر 4 × 3 + 4 = 16 ہے۔"),
      [(18, "That keeps +1 inside the bracket: 4m + 6. Taking away 1 gives 5 − 1 = 4, so 4m + 4: 16.", "یہ بریکٹ کے اندر +1 رکھتا ہے: 4m + 6۔ 1 کو تفریق کرنے سے 5 − 1 = 4 ملتا ہے، تو 4m + 4: 16", "first_term_only")]),
   ch("q11_find_error", ("Hira writes 9 − (3 + k) = 9 − 3 + k. What went wrong?", "ہیرا 9 − (3 + k) = 9 − 3 + k لکھتی ہے۔ کیا غلطی ہوئی؟"),
      ("The minus must change both signs: 9 − 3 − k = 6 − k.", "منفی دونوں علامتیں بدلتا ہے: 9 − 3 − k = 6 − k", "Yes! Test k = 1: 9 − 4 = 5 and 6 − 1 = 5.", "جی ہاں! k = 1 لیں: 9 − 4 = 5 اور 6 − 1 = 5"),
      [("Nothing. She opened it correctly.", "کوئی غلطی نہیں۔ اس نے صحیح کھولا۔", "With k = 1: 9 − (3 + 1) = 5 but 9 − 3 + 1 = 7. They differ.", "k = 1 کے ساتھ: 9 − (3 + 1) = 5 مگر 9 − 3 + 1 = 7۔ یہ مختلف ہیں۔", "first_term_only"),
       ("She should add 9 and 3 first.", "اسے پہلے 9 اور 3 جمع کرنے چاہییں۔", "9 and 3 are not added: the bracket is taken away from 9.", "9 اور 3 جمع نہیں ہوتے: بریکٹ 9 میں سے تفریق ہوتی ہے۔", "brackets_ignored")],
      1, qtype="find_error"),
   ch("q12_find_error_value", ("Faisal finds the value of 3x + 2 when x = 5 and writes 37. What went wrong?", "فیصل x = 5 کے لیے 3x + 2 کی قیمت معلوم کر کے 37 لکھتا ہے۔ کیا غلطی ہوئی؟"),
      ("He read 3x as 35. It is 3 × 5 = 15, so the value is 15 + 2 = 17.", "اس نے 3x کو 35 پڑھا۔ یہ 3 × 5 = 15 ہے، تو قیمت 15 + 2 = 17 ہے۔", "Yes! A number next to a letter means multiply.", "جی ہاں! حرف کے ساتھ لکھے عدد کا مطلب ضرب ہے۔"),
      [("Nothing. 37 is right.", "کوئی غلطی نہیں۔ 37 درست ہے۔", "3x is 3 times x, not the digits 3 and 5. The value is 17.", "3x یعنی x کا 3 گنا، ہندسے 3 اور 5 نہیں۔ قیمت 17 ہے۔", "joins_digits"),
       ("He should subtract 2, not add it.", "اسے 2 جمع نہیں بلکہ تفریق کرنا چاہیے۔", "The expression has + 2. The mistake is in 3x.", "عبارت میں + 2 ہے۔ غلطی 3x میں ہے۔", "joins_digits")],
      0, qtype="find_error"),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! You handled brackets and values.", "شاباش! آپ نے بریکٹیں اور قیمتیں سنبھال لیں۔"),
    "text": T("A plus before a bracket changes nothing inside it. A minus before a bracket changes every sign inside. With brackets in brackets, work from the inside out. To find a value, put the numbers in for the letters, multiply first, and keep every minus sign.",
              "بریکٹ کے آگے جمع ہو تو اس کے اندر کچھ نہیں بدلتا۔ آگے منفی ہو تو اندر کی ہر علامت بدلتی ہے۔ بریکٹ کے اندر بریکٹ ہو تو اندر سے باہر حل کریں۔ قیمت معلوم کرنے کے لیے حروف کی جگہ اعداد رکھیں، پہلے ضرب دیں، اور ہر منفی کی علامت رکھیں۔"),
    "points": [T("Test an answer by putting in a small number.", "جواب کو چھوٹا عدد رکھ کر جانچیں۔"),
               T("Multiply before you add or subtract.", "جمع یا تفریق سے پہلے ضرب دیں۔")]},
 ],
 bank=[
   {"id": "qb_number", "type": "recall", "step": nq("qb_number", ("Work out: 30 − (12 + 5)", "حل کریں: 30 − (12 + 5)"), QB,
      ("Do the bracket first.", "پہلے بریکٹ حل کریں۔"),
      ("Right! 30 − 17 = 13.", "درست! 30 − 17 = 13"), ("The bracket is 17. 30 − 17 = 13.", "بریکٹ 17 ہے۔ 30 − 17 = 13"),
      [(23, "The whole bracket is taken away: 30 − 17 = 13.", "پوری بریکٹ تفریق ہوتی ہے: 30 − 17 = 13", "sign_not_changed")], qtype=None)},
   {"id": "qb_value", "type": "apply", "step": nq("qb_value", ("Find the value of 8c − 5 when c = 3.", "جب c = 3 ہو تو 8c − 5 کی قیمت معلوم کریں۔"), QBE,
      ("8c means 8 × c.", "8c یعنی 8 × c"),
      ("Right! 24 − 5 = 19.", "درست! 24 − 5 = 19"), ("8 × 3 = 24, and 24 − 5 = 19.", "8 × 3 = 24، اور 24 − 5 = 19"),
      [(78, "8c is 8 × 3 = 24, not 83. Then 24 − 5 = 19.", "8c یعنی 8 × 3 = 24، 83 نہیں۔ پھر 24 − 5 = 19", "joins_digits")], qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": ch("qb_find_error",
      ("Omar writes 8x − (x + 4) = 7x + 4. What went wrong?", "عمر 8x − (x + 4) = 7x + 4 لکھتا ہے۔ کیا غلطی ہوئی؟"),
      ("The minus changes the 4 as well: 8x − x − 4 = 7x − 4.", "منفی 4 کو بھی بدلتا ہے: 8x − x − 4 = 7x − 4", "Yes! Every sign inside the bracket changes.", "جی ہاں! بریکٹ کے اندر کی ہر علامت بدلتی ہے۔"),
      [("Nothing. 7x + 4 is right.", "کوئی غلطی نہیں۔ 7x + 4 درست ہے۔", "With x = 1: 8 − 5 = 3 but 7 + 4 = 11. It is 7x − 4.", "x = 1 کے ساتھ: 8 − 5 = 3 مگر 7 + 4 = 11۔ یہ 7x − 4 ہے۔", "first_term_only"),
       ("It should be 9x − 4.", "یہ 9x − 4 ہونا چاہیے۔", "8x − x is 7x, not 9x.", "8x − x برابر 7x ہے، 9x نہیں۔", "first_term_only")],
      0, qtype=None)},
 ],
 review=[
   {"id": "r_simplify", "type": "recall", "step": aq("r_simplify", (f"Remove the brackets and simplify: {show([(8, 'b')])} − ({show([(3, 'b'), (2, '')])})", f"بریکٹ ہٹا کر مختصر کریں: {show([(8, 'b')])} − ({show([(3, 'b'), (2, '')])})"), R1,
      ("Change both signs inside the bracket.", "بریکٹ کے اندر دونوں علامتیں بدلیں۔"),
      ("Right! 8b − 3b − 2 = 5b − 2.", "درست! 8b − 3b − 2 = 5b − 2"), ("8b − 3b − 2 = 5b − 2.", "8b − 3b − 2 = 5b − 2"),
      [(keep_signs([(8, "b")], [(3, "b"), (2, "")]), "The 2 is taken away too: 5b − 2.", "2 بھی تفریق ہوتا ہے: 5b − 2", "first_term_only")], qtype=None)},
   {"id": "r_value", "type": "apply", "step": nq("r_value", ("Find the value of 2u + 3v when u = 4 and v = 5.", "جب u = 4 اور v = 5 ہو تو 2u + 3v کی قیمت معلوم کریں۔"), R2,
      ("2 × 4 and 3 × 5.", "2 × 4 اور 3 × 5"),
      ("Right! 8 + 15 = 23.", "درست! 8 + 15 = 23"), ("2 × 4 = 8, 3 × 5 = 15, and 8 + 15 = 23.", "2 × 4 = 8، 3 × 5 = 15، اور 8 + 15 = 23"),
      [(59, "2u is 2 × 4 = 8, not 24. 8 + 15 = 23.", "2u یعنی 2 × 4 = 8، ہندسے ساتھ ساتھ نہیں۔ 8 + 15 = 23", "joins_digits")], qtype=None)},
 ],
 glossary=[T("Bracket", "بریکٹ (قوسین)"), T("Simplify", "مختصر کرنا"), T("Value of an expression", "عبارت کی قیمت"), T("Substitute", "قیمت رکھنا"), T("BODMAS", "BODMAS")],
 flashcards=[
   {"id": "f_minus_bracket", "front": T("What does a minus before a bracket do?", "بریکٹ کے آگے منفی کیا کرتا ہے؟"),
    "back": T("It changes every sign inside: 9 − (3 + k) = 9 − 3 − k.", "یہ اندر کی ہر علامت بدل دیتا ہے: 9 − (3 + k) = 9 − 3 − k")},
   {"id": "f_value", "front": T("How do you find the value of 5a + 3 when a = 4?", "جب a = 4 ہو تو 5a + 3 کی قیمت کیسے معلوم کرتے ہیں؟"),
    "back": T("Put 4 for a: 5 × 4 + 3 = 23. Multiply first.", "a کی جگہ 4 رکھیں: 5 × 4 + 3 = 23۔ پہلے ضرب دیں۔")},
 ],
 home_task={"id": "h_brackets_at_home", "text": T(
   "You have Rs 100. You buy 3 things costing Rs 20, Rs 15 and Rs 10. Write what is left as 100 − (20 + 15 + 10) and also as 100 − 20 − 15 − 10. Check that both give the same answer.",
   "آپ کے پاس 100 روپے ہیں۔ آپ 20، 15 اور 10 روپے کی تین چیزیں خریدتے ہیں۔ جو بچا اسے 100 − (20 + 15 + 10) اور 100 − 20 − 15 − 10 دونوں طرح لکھیں۔ جانچیں کہ دونوں کا جواب ایک ہی ہے۔")},
 notes=["Covers removing brackets after a plus and after a minus (q1 to q4, q6), brackets inside brackets with BODMAS (q5), and finding the value of an expression for given numbers (q7 to q10, q12) and a find-the-error question on each (q11, q12).",
        "Each wrong answer is a real mistake: the signs inside a bracket left unchanged, only the first sign changed, brackets ignored or worked outside first, 5a read as 54, a minus lost when putting in values, and subtracting before multiplying.",
        "Urdu terms to check: بریکٹ (قوسین) (bracket), مختصر کرنا (simplify), عبارت کی قیمت (value of an expression), قیمت رکھنا (substitute). No new Urdu term was invented here."],
 minutes=18,
)

figs.attach(lesson, {})
write(lesson)
