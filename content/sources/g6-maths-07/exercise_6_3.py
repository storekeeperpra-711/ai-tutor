"""Practice set for Exercise 6.3 of the book: turn statements about ages and
prices into expressions, count the terms, name coefficients and constants, and
group like terms. The questions are new; only the kinds of question follow
the book."""
from common import (T, say, nq, aq, ch, practice_lesson, practice_intro, write, show, m,
                    collect, value, EX_SKILL, ALG_VARIABLES, ALG_TERMS, ALG_LIKE_TERMS)
import figs

SKILL = EX_SKILL["6.3"]


def coefficient(terms, letter):
    return next(c for c, v in terms if v == letter)


def constant(terms):
    return next((c for c, v in terms if not v), 0)


# q1: Hina is x years old, her brother is 4 years older
Q1 = [(1, "x"), (4, "")]
assert value("x + 4", x=11) == 15 and value("4x", x=11) != 15 and value("x - 4", x=11) != 15
# q2: 3 notebooks at Rs n and 1 pen at Rs 15
Q2 = [(3, "n"), (15, "")]
assert value("3n + 15", n=20) == 75 and value("18n", n=20) != 75 and value("n + 18", n=20) != 75
# q3: number of terms in 5a - 2b + 7 - c
E3 = [(5, "a"), (-2, "b"), (7, ""), (-1, "c")]
Q3 = len(E3)
assert Q3 == 4 and len([t for t in E3 if t[1]]) == 3 and show(E3) == "5a − 2b + 7 − c"
# q5: coefficient of y in 9x - 4y + 3
E5 = [(9, "x"), (-4, "y"), (3, "")]
Q5 = coefficient(E5, "y")
assert Q5 == -4 and show(E5) == "9x − 4y + 3"
# q6: constant term in 8p + 2q - 11
E6 = [(8, "p"), (2, "q"), (-11, "")]
Q6 = constant(E6)
assert Q6 == -11 and show(E6) == "8p + 2q − 11"
# q8: 4a + 3b + 2a + b
E8 = [(4, "a"), (3, "b"), (2, "a"), (1, "b")]
Q8 = list(collect(*E8))
assert Q8 == [(6, "a"), (4, "b")] and show(E8) == "4a + 3b + 2a + b"
Q8_WRONG1 = [(6, "a"), (3, "b")]
Q8_WRONG2 = [(10, "a")]
assert collect(*Q8_WRONG1) != collect(*Q8) and sum(c for c, _ in E8) == 10
# q9: how many terms are like 3x in 3x + 2y - x + 5 + 7x
E9 = [(3, "x"), (2, "y"), (-1, "x"), (5, ""), (7, "x")]
Q9 = len([t for t in E9 if t[1] == "x"])
assert Q9 == 3 and len([t for t in E9 if t[1] == "x" and abs(t[0]) != 1]) == 2 and show(E9) == "3x + 2y − x + 5 + 7x"
# q10: coefficient of b in a + b + 3
E10 = [(1, "a"), (1, "b"), (3, "")]
assert coefficient(E10, "b") == 1
# q12: sum of the coefficients of x in 3x + 2y - x + 7x
Q12 = sum(c for c, v in E9 if v == "x")
assert Q12 == 9
# bank and review
QB = len([(5, "m"), (-2, "n"), (4, "")])
assert QB == 3
R1 = coefficient([(2, "x"), (-7, "z"), (1, "")], "z")
assert R1 == -7
R2 = list(collect((5, "t"), (2, "s"), (-3, "t"), (4, "s")))
assert R2 == [(6, "s"), (2, "t")]

lesson = practice_lesson(
 "6.3", script="exercise_6_3.py",
 title=T("Exercise 6.3 practice: terms and like terms", "مشق 6.3 کی پریکٹس: ارکان اور یکساں ارکان"),
 outcome="Write statements about ages and prices as expressions, count the terms of an expression, name coefficients and constants, and group like terms.",
 prerequisites=[ALG_VARIABLES, ALG_TERMS, ALG_LIKE_TERMS],
 misconceptions=[
   {"id": "times_for_plus", "description": "Writes 'older than' or 'more than' as multiplication, like 4x for x + 4."},
   {"id": "wrong_sign_direction", "description": "Writes 'older than' as taking away, like x − 4."},
   {"id": "counts_letters_only", "description": "Leaves out the constant when counting the terms."},
   {"id": "drops_sign", "description": "Leaves out the minus sign that belongs to a term (−4y has coefficient −4)."},
   {"id": "coefficient_is_constant", "description": "Mixes up the coefficient (the number with the letter) and the constant (the number on its own)."},
   {"id": "lone_letter_zero", "description": "Thinks a letter on its own (x) has coefficient 0 instead of 1, and so leaves it out."},
   {"id": "unlike_joined", "description": "Joins terms with different letters, like 2a and 2b, or adds every coefficient into one letter."},
   {"id": "forgets_lone_letter", "description": "Gives b one instead of two when adding 3b and b."},
 ],
 steps=[
   practice_intro("6.3",
     "Here you turn statements about ages and prices into expressions, count terms, name coefficients and constants, and group like terms.",
     "اس میں آپ عمروں اور قیمتوں کے بیانات کو عبارتوں میں بدلیں گے، ارکان گنیں گے، عددی سر اور مستقل کے نام بتائیں گے، اور یکساں ارکان کو اکٹھا کریں گے۔",
     "Exercise 6.3 is about expressions and their terms. Ready?", "مشق 6.3 عبارتوں اور ان کے ارکان کے بارے میں ہے۔ تیار؟"),
   aq("q1_age", ("Hina is x years old. Her brother is 4 years older than Hina. Write his age as an expression.", "حنا x سال کی ہے۔ اس کا بھائی حنا سے 4 سال بڑا ہے۔ اس کی عمر کو عبارت میں لکھیں۔"), Q1,
      ("Older means more. Start with Hina's age, x.", "بڑا یعنی زیادہ۔ حنا کی عمر x سے شروع کریں۔"),
      ("Right! x + 4.", "درست! x + 4"), ("4 years older than x is x + 4.", "x سے 4 سال بڑا یعنی x + 4"),
      [([(4, "x")], "4x means 4 times x. Older by 4 means add 4: x + 4.", "4x یعنی x کا 4 گنا۔ 4 سال بڑا یعنی 4 جمع: x + 4", "times_for_plus"),
       ([(1, "x"), (-4, "")], "Older means more, so add 4: x + 4.", "بڑا یعنی زیادہ، تو 4 جمع کریں: x + 4", "wrong_sign_direction")], qtype="recall"),
   aq("q2_price", ("A pen costs Rs 15. A notebook costs Rs n. Write the cost of 3 notebooks and 1 pen as an expression.", "ایک قلم 15 روپے کا ہے۔ ایک کاپی n روپے کی ہے۔ 3 کاپیوں اور 1 قلم کی قیمت کو عبارت میں لکھیں۔"), Q2,
      ("3 notebooks cost 3 × n. Then add the pen.", "3 کاپیوں کی قیمت 3 × n ہے۔ پھر قلم کی قیمت جمع کریں۔"),
      ("Right! 3n + 15.", "درست! 3n + 15"), ("3 notebooks cost 3n, and the pen costs 15: 3n + 15.", "3 کاپیوں کی قیمت 3n ہے اور قلم کی 15: 3n + 15"),
      [([(18, "n")], "3n and 15 are unlike terms. They cannot join into 18n: 3n + 15.", "3n اور 15 غیر یکساں ارکان ہیں۔ یہ 18n میں نہیں مل سکتے: 3n + 15", "unlike_joined"),
       ([(1, "n"), (18, "")], "The 3 multiplies n; it is not added to 15: 3n + 15.", "3، n کو ضرب دیتا ہے؛ یہ 15 میں جمع نہیں ہوتا: 3n + 15", "times_for_plus")], qtype="recall"),
   {"id": "s_rule", "type": "explain",
    "character": say("thinking", "Terms are separated by + and −. Each sign belongs to the term after it.", "ارکان + اور − سے الگ ہوتے ہیں۔ ہر علامت اپنے بعد والے رکن کی ہے۔"),
    "text": T(f"In {show(E3)} the terms are 5a, −2b, 7 and −c: four terms, because + and − signs separate them and each sign belongs to the term after it. The number with a letter is the coefficient: −2 is the coefficient of b. A letter alone has coefficient 1 (−c has coefficient −1). The number on its own, 7, is the constant. Like terms have the same letter, so 4a and 2a are like terms; 4a and 2b are not. We group like terms by adding their coefficients.",
              f"{show(E3)} میں ارکان 5a، −2b، 7 اور −c ہیں: چار ارکان، کیونکہ + اور − کی علامتیں انھیں الگ کرتی ہیں اور ہر علامت اپنے بعد والے رکن کی ہوتی ہے۔ حرف کے ساتھ والا عدد عددی سر ہے: b کا عددی سر −2 ہے۔ اکیلے حرف کا عددی سر 1 ہوتا ہے (−c کا عددی سر −1 ہے)۔ اکیلا عدد 7 مستقل ہے۔ یکساں ارکان میں حرف ایک جیسا ہوتا ہے، تو 4a اور 2a یکساں ارکان ہیں؛ 4a اور 2b نہیں۔ یکساں ارکان کو ان کے عددی سر جمع کر کے اکٹھا کرتے ہیں۔"),
   },
   nq("q3_count", (f"How many terms does the expression {show(E3)} have?", f"عبارت {show(E3)} کے کتنے ارکان ہیں؟"), Q3,
      ("Split it at each + and − sign.", "ہر + اور − کی علامت پر اسے الگ کریں۔"),
      ("Right! 5a, −2b, 7 and −c: 4 terms.", "درست! 5a، −2b، 7 اور −c: 4 ارکان"),
      ("The terms are 5a, −2b, 7 and −c. That is 4.", "ارکان 5a، −2b، 7 اور −c ہیں۔ یعنی 4"),
      [(3, "The constant 7 is a term too. Count all four: 5a, −2b, 7, −c.", "مستقل 7 بھی ایک رکن ہے۔ چاروں گنیں: 5a، −2b، 7، −c", "counts_letters_only")], qtype="recall"),
   nq("q5_coefficient", (f"What is the coefficient of y in {show(E5)}?", f"{show(E5)} میں y کا عددی سر کیا ہے؟"), Q5,
      ("The sign in front of the term belongs to it.", "رکن کے آگے کی علامت اسی کی ہوتی ہے۔"),
      ("Right! The term is −4y, so the coefficient is −4.", "درست! رکن −4y ہے، تو عددی سر −4 ہے۔"),
      ("The term is −4y, with its minus sign: coefficient −4.", "رکن −4y ہے، منفی کی علامت کے ساتھ: عددی سر −4"),
      [(4, "Keep the minus sign: the term is −4y, so the coefficient is −4.", "منفی کی علامت رکھیں: رکن −4y ہے، تو عددی سر −4 ہے۔", "drops_sign"),
       (3, "3 is the constant, the number with no letter. The coefficient of y is −4.", "3 مستقل ہے، بغیر حرف کا عدد۔ y کا عددی سر −4 ہے۔", "coefficient_is_constant")]),
   nq("q6_constant", (f"What is the constant term in {show(E6)}?", f"{show(E6)} میں مستقل رکن کون سا ہے؟"), Q6,
      ("The constant is the term with no letter. Keep its sign.", "مستقل وہ رکن ہے جس میں حرف نہیں ہوتا۔ اس کی علامت رکھیں۔"),
      ("Right! The constant term is −11.", "درست! مستقل رکن −11 ہے۔"),
      ("The term with no letter is −11, and its sign stays with it.", "بغیر حرف کا رکن −11 ہے، اور اس کی علامت اس کے ساتھ رہتی ہے۔"),
      [(11, "The minus sign belongs to the term: −11.", "منفی کی علامت رکن کی ہے: −11", "drops_sign"),
       (2, "2 is the coefficient of q. The constant has no letter: −11.", "2، q کا عددی سر ہے۔ مستقل میں حرف نہیں ہوتا: −11", "coefficient_is_constant")]),
   ch("q7_like", ("Which pair are like terms?", "کون سا جوڑا یکساں ارکان کا ہے؟"),
      ("6m and −2m", "6m اور −2m", "Yes! Both have the letter m. The coefficients can differ.", "جی ہاں! دونوں میں حرف m ہے۔ عددی سر مختلف ہو سکتے ہیں۔"),
      [("3m and 3n", "3m اور 3n", "The letters m and n differ, so they are unlike terms, even if the coefficients match.", "حروف m اور n مختلف ہیں، اس لیے یہ غیر یکساں ارکان ہیں، چاہے عددی سر برابر ہوں۔", "unlike_joined"),
       ("5a and 5", "5a اور 5", "5a has a letter and 5 has none. They are unlike terms.", "5a میں حرف ہے اور 5 میں نہیں۔ یہ غیر یکساں ارکان ہیں۔", "unlike_joined"),
       ("2x and 2y", "2x اور 2y", "x and y are different letters: unlike terms.", "x اور y مختلف حروف ہیں: غیر یکساں ارکان۔", "unlike_joined")],
      1, qtype="recall"),
   aq("q8_group", (f"Group the like terms and write the expression in its simplest form: {show(E8)}", f"یکساں ارکان کو اکٹھا کر کے عبارت کو سادہ ترین شکل میں لکھیں: {show(E8)}"), Q8,
      ("Add the a-terms together and the b-terms together. b means 1b.", "a والے ارکان اکٹھے اور b والے ارکان اکٹھے جمع کریں۔ b یعنی 1b"),
      ("Right! 4a + 2a = 6a and 3b + b = 4b: 6a + 4b.", "درست! 4a + 2a = 6a اور 3b + b = 4b: 6a + 4b"),
      ("a-terms: 4a + 2a = 6a. b-terms: 3b + 1b = 4b. So 6a + 4b.", "a والے: 4a + 2a = 6a۔ b والے: 3b + 1b = 4b۔ تو 6a + 4b"),
      [(Q8_WRONG1, "A lone b counts as 1b: 3b + 1b = 4b, so 6a + 4b.", "اکیلا b یعنی 1b: 3b + 1b = 4b، تو 6a + 4b", "forgets_lone_letter"),
       (Q8_WRONG2, "a and b are different letters, so you cannot add them all into 10a. Keep 6a + 4b.", "a اور b مختلف حروف ہیں، اس لیے سب کو 10a میں جمع نہیں کر سکتے۔ 6a + 4b رہنے دیں۔", "unlike_joined")]),
   nq("q9_like_count", (f"How many terms of {show(E9)} are like the term 3x?", f"{show(E9)} کے کتنے ارکان رکن 3x کے یکساں ہیں؟"), Q9,
      ("Look for every term with the letter x. A lone x or −x counts too.", "x والے ہر رکن کو دیکھیں۔ اکیلا x یا −x بھی گنا جاتا ہے۔"),
      ("Right! 3x, −x and 7x: 3 terms.", "درست! 3x، −x اور 7x: 3 ارکان"),
      ("The terms with x are 3x, −x and 7x. That is 3.", "x والے ارکان 3x، −x اور 7x ہیں۔ یعنی 3"),
      [(2, "−x is −1x. It is a like term too: 3.", "−x یعنی −1x۔ یہ بھی یکساں رکن ہے: 3", "lone_letter_zero"),
       (5, "That counts every term. Only those with x are like 3x: 3.", "یہ ہر رکن گنتا ہے۔ صرف x والے 3x کے یکساں ہیں: 3", "unlike_joined")]),
   ch("q10_find_error", ("Bilal says the coefficient of b in a + b + 3 is 0, because no number is written. What went wrong?", "بلال کہتا ہے a + b + 3 میں b کا عددی سر 0 ہے، کیونکہ کوئی عدد لکھا نہیں۔ کیا غلطی ہوئی؟"),
      ("A letter alone has coefficient 1, because b means 1 × b.", "اکیلے حرف کا عددی سر 1 ہوتا ہے، کیونکہ b یعنی 1 × b۔", "Yes! The 1 is not written, but it is there.", "جی ہاں! 1 لکھا نہیں جاتا مگر موجود ہوتا ہے۔"),
      [("Nothing. 0 is right.", "کوئی غلطی نہیں۔ 0 درست ہے۔", "With coefficient 0 the term would vanish: 0 × b = 0. It is 1.", "عددی سر 0 ہو تو رکن غائب ہو جاتا: 0 × b = 0۔ یہ 1 ہے۔", "lone_letter_zero"),
       ("The coefficient is 3, the number in the expression.", "عددی سر 3 ہے، جو عبارت میں لکھا عدد ہے۔", "3 has no letter; it is the constant. The coefficient of b is 1.", "3 کے ساتھ حرف نہیں؛ یہ مستقل ہے۔ b کا عددی سر 1 ہے۔", "coefficient_is_constant")],
      0, qtype="find_error"),
   ch("q11_find_error_like", ("Sana says 2a and 2b are like terms, because both have the coefficient 2. What went wrong?", "ثناء کہتی ہے 2a اور 2b یکساں ارکان ہیں، کیونکہ دونوں کا عددی سر 2 ہے۔ کیا غلطی ہوئی؟"),
      ("Like terms need the same letter. a and b differ, so these are unlike terms.", "یکساں ارکان میں ایک ہی حرف ہونا چاہیے۔ a اور b مختلف ہیں، اس لیے یہ غیر یکساں ارکان ہیں۔", "Yes! The letter must match, not the coefficient.", "جی ہاں! حرف ملنا چاہیے، عددی سر نہیں۔"),
      [("Nothing. Equal coefficients make them like terms.", "کوئی غلطی نہیں۔ برابر عددی سر انھیں یکساں ارکان بناتے ہیں۔", "Try a = 1 and b = 5: 2a = 2 but 2b = 10. They are different kinds.", "a = 1 اور b = 5 لیں: 2a = 2 مگر 2b = 10۔ یہ مختلف قسم کے ہیں۔", "unlike_joined"),
       ("They are like terms because both end in a letter.", "یہ یکساں ارکان ہیں کیونکہ دونوں حرف پر ختم ہوتے ہیں۔", "It must be the same letter. a and b are different.", "حرف ایک ہی ہونا چاہیے۔ a اور b مختلف ہیں۔", "unlike_joined")],
      2, qtype="find_error"),
   nq("q12_sum", (f"In {show(E9)}, add the coefficients of all the terms with x. What is the total?", f"{show(E9)} میں x والے تمام ارکان کے عددی سر جمع کریں۔ کل کیا ہے؟"), Q12,
      ("The coefficients are 3, −1 and 7.", "عددی سر 3، −1 اور 7 ہیں۔"),
      ("Right! 3 − 1 + 7 = 9, so the x-terms group into 9x.", "درست! 3 − 1 + 7 = 9، تو x والے ارکان 9x بنتے ہیں۔"),
      ("3 + (−1) + 7 = 9.", "3 + (−1) + 7 = 9"),
      [(10, "The middle term is −x, so its coefficient is −1: 3 − 1 + 7 = 9.", "درمیان کا رکن −x ہے، تو اس کا عددی سر −1 ہے: 3 − 1 + 7 = 9", "drops_sign"),
       (11, "The term −x counts as −1, not +1 or 0: 3 − 1 + 7 = 9.", "رکن −x کا مطلب −1 ہے، +1 یا 0 نہیں: 3 − 1 + 7 = 9", "lone_letter_zero")]),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! You know the parts of an expression.", "شاباش! آپ عبارت کے حصے جانتے ہیں۔"),
    "text": T("Write statements about ages and prices as expressions: older means add (x + 4), and 3 notebooks at n each cost 3n. Terms are separated by + and −, and each sign stays with the term after it. A coefficient goes with a letter (a letter alone has 1) and a constant is a number alone. Like terms have the same letter; group them by adding their coefficients.",
              "عمروں اور قیمتوں کے بیانات کو عبارت میں لکھیں: بڑا یعنی جمع (x + 4)، اور n روپے کی 3 کاپیاں 3n ہیں۔ ارکان + اور − سے الگ ہوتے ہیں، اور ہر علامت اپنے بعد والے رکن کے ساتھ رہتی ہے۔ عددی سر حرف کے ساتھ ہوتا ہے (اکیلے حرف کا 1) اور مستقل اکیلا عدد ہے۔ یکساں ارکان میں حرف ایک جیسا ہوتا ہے؛ انھیں عددی سر جمع کر کے اکٹھا کریں۔"),
    "points": [T("Count terms by looking at the + and − signs.", "+ اور − کی علامتیں دیکھ کر ارکان گنیں۔"),
               T("Same letter means like terms.", "ایک ہی حرف کا مطلب یکساں ارکان۔")]},
 ],
 bank=[
   {"id": "qb_count", "type": "recall", "step": nq("qb_count", (f"How many terms does {show([(5, 'm'), (-2, 'n'), (4, '')])} have?", f"{show([(5, 'm'), (-2, 'n'), (4, '')])} کے کتنے ارکان ہیں؟"), QB,
      ("Split at each + and − sign.", "ہر + اور − کی علامت پر الگ کریں۔"),
      ("Right! 5m, −2n and 4: 3 terms.", "درست! 5m، −2n اور 4: 3 ارکان"), ("5m, −2n and 4 are 3 terms.", "5m، −2n اور 4 یعنی 3 ارکان"),
      [(2, "The constant 4 is a term too: 3.", "مستقل 4 بھی رکن ہے: 3", "counts_letters_only")], qtype=None)},
   {"id": "qb_group", "type": "apply", "step": aq("qb_group", (f"Group the like terms: {show([(5, 't'), (2, 's'), (-3, 't'), (4, 's')])}", f"یکساں ارکان کو اکٹھا کریں: {show([(5, 't'), (2, 's'), (-3, 't'), (4, 's')])}"), R2,
      ("Collect the t-terms and the s-terms separately.", "t والے اور s والے ارکان الگ الگ اکٹھے کریں۔"),
      ("Right! 5t − 3t = 2t and 2s + 4s = 6s, so 6s + 2t.", "درست! 5t − 3t = 2t اور 2s + 4s = 6s، تو 6s + 2t"), ("t-terms: 5 − 3 = 2. s-terms: 2 + 4 = 6.", "t والے: 5 − 3 = 2۔ s والے: 2 + 4 = 6"),
      [([(8, "t"), (6, "s")], "The −3t is taken away: 5t − 3t = 2t.", "−3t تفریق ہوتا ہے: 5t − 3t = 2t", "drops_sign")], qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": ch("qb_find_error",
      ("Usman says 5x − 3 has three terms: 5, x and 3. What went wrong?", "عثمان کہتا ہے 5x − 3 کے تین ارکان ہیں: 5، x اور 3۔ کیا غلطی ہوئی؟"),
      ("5x is one term. The terms are 5x and −3: two terms.", "5x ایک رکن ہے۔ ارکان 5x اور −3 ہیں: دو ارکان۔", "Yes! Terms are split only by + and − signs.", "جی ہاں! ارکان صرف + اور − سے الگ ہوتے ہیں۔"),
      [("Nothing. Three terms is right.", "کوئی غلطی نہیں۔ تین ارکان درست ہیں۔", "5x means 5 × x: one term. 5x − 3 has two terms.", "5x یعنی 5 × x: ایک رکن۔ 5x − 3 کے دو ارکان ہیں۔", "coefficient_is_constant"),
       ("It has one term, 5x − 3.", "اس کا ایک رکن ہے، 5x − 3۔", "The − sign splits it into two terms: 5x and −3.", "− کی علامت اسے دو ارکان میں بانٹتی ہے: 5x اور −3", "unlike_joined")],
      0, qtype=None)},
 ],
 review=[
   {"id": "r_coefficient", "type": "recall", "step": nq("r_coefficient", (f"What is the coefficient of z in {show([(2, 'x'), (-7, 'z'), (1, '')])}?", f"{show([(2, 'x'), (-7, 'z'), (1, '')])} میں z کا عددی سر کیا ہے؟"), R1,
      ("Keep the sign of the term.", "رکن کی علامت رکھیں۔"),
      ("Right! −7.", "درست! −7"), ("The term is −7z: coefficient −7.", "رکن −7z ہے: عددی سر −7"),
      [(7, "Keep the minus sign: −7.", "منفی کی علامت رکھیں: −7", "drops_sign")], qtype=None)},
   {"id": "r_age", "type": "apply", "step": aq("r_age", ("Ali is y years old. His sister is 3 years younger. Write her age as an expression.", "علی y سال کا ہے۔ اس کی بہن اس سے 3 سال چھوٹی ہے۔ اس کی عمر کو عبارت میں لکھیں۔"), [(1, "y"), (-3, "")],
      ("Younger means less. Start with y.", "چھوٹی یعنی کم۔ y سے شروع کریں۔"),
      ("Right! y − 3.", "درست! y − 3"), ("3 years younger than y is y − 3.", "y سے 3 سال چھوٹی یعنی y − 3"),
      [([(1, "y"), (3, "")], "Younger means less, so take away 3: y − 3.", "چھوٹی یعنی کم، تو 3 تفریق کریں: y − 3", "wrong_sign_direction")], qtype=None)},
 ],
 glossary=[T("Term", "رکن"), T("Coefficient", "عددی سر"), T("Constant", "مستقل"), T("Like terms", "یکساں ارکان"), T("Unlike terms", "غیر یکساں ارکان")],
 flashcards=[
   {"id": "f_terms", "front": T("How do you count the terms?", "ارکان کیسے گنتے ہیں؟"),
    "back": T("Split at each + and − sign. The sign stays with the term after it.", "ہر + اور − کی علامت پر الگ کریں۔ علامت اپنے بعد والے رکن کے ساتھ رہتی ہے۔")},
   {"id": "f_like", "front": T("Which terms are like terms?", "کون سے ارکان یکساں ہوتے ہیں؟"),
    "back": T("Terms with the same letter, like 4a and −2a. Add their coefficients.", "ایک ہی حرف والے ارکان، جیسے 4a اور −2a۔ ان کے عددی سر جمع کریں۔")},
 ],
 home_task={"id": "h_terms_at_home", "text": T(
   "Pick two things you buy for the family, with a price for one of each. Write the cost of a few of each as an expression with letters (for example 20a + 15b). Name its terms, coefficients and like terms.",
   "دو چیزیں چنیں جو گھر والوں کے لیے خریدی جاتی ہیں اور ہر ایک کی ایک کی قیمت لکھیں۔ ہر ایک کی چند عدد کی قیمت حروف والی عبارت میں لکھیں (مثلاً 20a + 15b)۔ اس کے ارکان، عددی سر اور یکساں ارکان بتائیں۔")},
 notes=["Covers writing statements as expressions (q1, q2), counting terms (q3), coefficients and constants (q5, q6, q10, q12), like and unlike terms (q7, q9, q11) and grouping like terms (q8).",
        "Each wrong answer is a real mistake: older written as times or minus, the constant left out of the count, the minus sign dropped, coefficient and constant mixed up, a lone letter taken as zero, and unlike terms joined.",
        "Urdu terms to check: رکن / ارکان (term), عددی سر (coefficient), مستقل (constant), یکساں ارکان / غیر یکساں ارکان (like / unlike terms), عبارت (expression). No new Urdu term was invented here."],
 minutes=17,
)

figs.attach(lesson, {
    "q3_count": figs.term_boxes(["5a", "−2b", "7", "−c"], "The expression 5a minus 2b plus 7 minus c cut into four boxes: 5a, minus 2b, 7 and minus c.", "عبارت 5a − 2b + 7 − c چار خانوں میں: 5a، −2b، 7 اور −c۔"),
})
write(lesson)
