from common import (T, opt, say, wrong, number_question, text_question, write,
                    expr_forms, BOOK, REVIEW, ALG_VARIABLES, ALG_TERMS)

SKILL = ALG_TERMS

# Each expression as (coefficient, letter) pairs; a constant has no letter.
E4 = [(4, "a"), (2, "b"), (-6, ""), (1, "c")]   # 4a + 2b − 6 + c
E5 = [(7, "x"), (9, "y"), (-2, "")]             # 7x + 9y − 2
E6 = [(3, "m"), (-8, ""), (2, "n")]             # 3m − 8 + 2n
E7 = [(1, "a"), (1, "b"), (6, "")]              # a + b + 6
E8 = [(12, ""), (-5, "x")]                      # 12 − 5x
E9 = [(4, "p"), (9, "")]                        # 4p + 9
QB = [(6, "p"), (-1, "q"), (4, "")]             # 6p − q + 4
R1 = [(2, "x"), (3, "y"), (-1, "z"), (7, "")]   # 2x + 3y − z + 7
R2 = [(11, ""), (4, "m")]                       # 11 + 4m


def coefficient(terms, letter):
    return next(c for c, v in terms if v == letter)


def constant(terms):
    return next(c for c, v in terms if not v)


S2 = expr_forms((1, "x"), (3, ""))
assert S2 == ["3+x", "x+3"]
S4 = len(E4)
assert S4 == 4
S5 = coefficient(E5, "y")
assert S5 == 9
assert constant(E6) == -8
S7 = coefficient(E7, "b")
assert S7 == 1
S8 = coefficient(E8, "x")
assert S8 == -5
assert coefficient(E9, "p") == 4 and constant(E9) == 9
S11 = 2 + 5   # 2n + 5n = 7n
assert S11 == 7
QBA = coefficient(QB, "q")
assert QBA == -1
R1A = len(R1)
assert R1A == 4
R2A = coefficient(R2, "m")
assert R2A == 4

lesson = {
 "id": "g6-maths-07-terms-and-coefficients",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Name the terms, variables, coefficients and constant of an algebraic expression.", "textbook": f"{BOOK}, Terms, coefficients and constants"}],
 "skills": [SKILL],
 "title": T("Terms, coefficients and constants", "ارکان، عددی سر اور مستقل"),
 "estimated_minutes": 13,
 "prerequisites": [{"skill": ALG_VARIABLES}],
 "misconceptions": [
   {"id": "coefficient_is_constant", "description": "Mixes up the coefficient (the number with the letter) and the constant (the number on its own)."},
   {"id": "lone_letter_zero", "description": "Thinks a letter on its own (b) has coefficient 0 instead of 1."},
   {"id": "drops_sign", "description": "Leaves out the minus sign that belongs to a term (−5x has coefficient −5)."},
   {"id": "splits_terms", "description": "Splits a term like 5x into two terms, 5 and x."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_name", "type": "recall", "step": {
     "id": "qb_name", "type": "choice",
     "prompt": T("In the term 8k, the 8 is called the …", "رکن 8k میں 8 کو کہتے ہیں …"),
     "options": [
       opt("coefficient", "coefficient", "عددی سر", True, "Yes! The number multiplying the letter.", "جی ہاں! وہ عدد جو حرف سے ضرب ہوتا ہے۔"),
       opt("constant", "constant", "مستقل", False, "A constant has no letter. 8 here multiplies k: coefficient.", "مستقل کے ساتھ حرف نہیں ہوتا۔ یہاں 8، k سے ضرب ہے: عددی سر۔", "coefficient_is_constant"),
       opt("variable", "variable", "متغیر", False, "The variable is the letter, k. 8 is the coefficient.", "متغیر حرف k ہے۔ 8 عددی سر ہے۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("What is the coefficient of q in 6p − q + 4?", "6p − q + 4 میں q کا عددی سر کیا ہے؟"),
     QBA,
     T("−q means −1 × q.", "−q یعنی −1 × q"),
     T("Right! −q is −1q, so the coefficient is −1.", "درست! −q یعنی −1q، تو عددی سر −1 ہے۔"),
     T("The term is −q = −1q: coefficient −1.", "رکن −q = −1q ہے: عددی سر −1"),
     common_wrong=[wrong(1, "Keep the minus sign with the term: −q has coefficient −1.", "منفی کی علامت رکن کے ساتھ رکھیں: −q کا عددی سر −1 ہے۔", "drops_sign"),
                   wrong(0, "A letter on its own counts once: −q = −1q.", "اکیلا حرف ایک بار گنا جاتا ہے: −q = −1q", "lone_letter_zero")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Usman says 5x − 3 has three terms: 5, x and 3. What is wrong?", "عثمان کہتا ہے 5x − 3 کے تین ارکان ہیں: 5، x اور 3۔ کیا غلطی ہے؟"),
     "options": [
       opt("two_terms", "5x is one term. The terms are 5x and −3: two terms.", "5x ایک رکن ہے۔ ارکان 5x اور −3 ہیں: دو ارکان۔", True,
           "Yes! Terms are split by + and − signs only.", "جی ہاں! ارکان صرف + اور − سے الگ ہوتے ہیں۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "5x means 5 × x: one term. 5x − 3 has two terms.", "5x یعنی 5 × x: ایک رکن۔ 5x − 3 کے دو ارکان ہیں۔", "splits_terms"),
       opt("one", "It has one term.", "اس کا ایک رکن ہے۔", False,
           "The − sign splits it into two terms: 5x and −3.", "− کی علامت اسے دو ارکان میں بانٹتی ہے: 5x اور −3"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_parts", "front": T("In 5x + 3y − 7?", "5x + 3y − 7 میں؟"),
    "back": T("Terms 5x, 3y, −7. Coefficient of x is 5, of y is 3. Constant −7.", "ارکان 5x، 3y، −7۔ x کا عددی سر 5، y کا 3۔ مستقل −7")},
   {"id": "f_one", "front": T("Coefficient of b in a + b?", "a + b میں b کا عددی سر؟"),
    "back": T("1, because b means 1b.", "1، کیونکہ b یعنی 1b")},
 ],
 "home_tasks": [{"id": "h_shop", "text": T(
   "A shopkeeper charges Rs 10 for each pen and Rs 25 for a bag, so x pens cost 10x + 25. Ask someone at home to make up a price rule like this. Name its coefficient and constant.",
   "دکاندار ہر قلم کے 10 روپے اور تھیلے کے 25 روپے لیتا ہے، تو x قلم 10x + 25 کے ہیں۔ گھر میں کسی سے ایسا ایک قیمت کا اصول بنوائیں۔ اس کا عددی سر اور مستقل بتائیں۔")}],
 "glossary": [T("Term", "رکن"), T("Variable", "متغیر"), T("Coefficient", "عددی سر"), T("Constant", "مستقل")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "5x + 3y − 7 looks like a puzzle. Let's name every piece of it!",
                     "5x + 3y − 7 ایک پہیلی لگتی ہے۔ آئیں اس کے ہر ٹکڑے کا نام رکھیں!"),
    "text": T("Today we learn the names of the parts of an expression: terms, variables, coefficients and constants. First, write an expression.", "آج ہم عبارت کے حصوں کے نام سیکھیں گے: ارکان، متغیر، عددی سر اور مستقل۔ پہلے ایک عبارت لکھیں۔")},
   text_question(
     "s2_foundation",
     T("Ali has x marbles. He gets 3 more. Write how many he has now.", "علی کے پاس x کنچے ہیں۔ اسے 3 اور ملتے ہیں۔ لکھیں اب اس کے پاس کتنے ہیں۔"),
     S2[1],
     T("Start with x, then add 3.", "x سے شروع کریں، پھر 3 جمع کریں۔"),
     T("Right! x + 3.", "درست! x + 3"),
     T("x marbles and 3 more: x + 3.", "x کنچے اور 3 مزید: x + 3"),
     accept=[S2[0]],
     common_wrong=[wrong("3x", "3x means 3 times x. He gets 3 MORE: x + 3.", "3x یعنی x کا تین گنا۔ اسے 3 مزید ملتے ہیں: x + 3")],
     qtype="recall", skill=ALG_VARIABLES),
   {"id": "s3_rule", "type": "explain",
    "character": say("happy", "The letter is the variable, its number is the coefficient, and a lonely number is the constant!", "حرف متغیر ہے، اس کا عدد عددی سر، اور اکیلا عدد مستقل!"),
    "text": T("In 5x + 3y − 7 the terms are 5x, 3y and −7; + and − signs separate them, and each sign belongs to the term after it. x and y are variables. The number in front of a variable is its coefficient: 5 is the coefficient of x, 3 of y. A term with no letter, −7, is the constant. A letter on its own has coefficient 1: b means 1b, and −b means −1b.",
              "5x + 3y − 7 میں ارکان 5x، 3y اور −7 ہیں؛ + اور − کی علامات انہیں الگ کرتی ہیں، اور ہر علامت اپنے بعد والے رکن کی ہوتی ہے۔ x اور y متغیر ہیں۔ متغیر سے پہلے کا عدد اس کا عددی سر ہے: 5، x کا عددی سر ہے، 3، y کا۔ بغیر حرف والا رکن، −7، مستقل ہے۔ اکیلے حرف کا عددی سر 1 ہوتا ہے: b یعنی 1b، اور −b یعنی −1b۔")},
   number_question(
     "s4_count",
     T("How many terms does 4a + 2b − 6 + c have?", "4a + 2b − 6 + c کے کتنے ارکان ہیں؟"),
     S4,
     T("Count the parts between + and − signs.", "+ اور − کے درمیان حصے گنیں۔"),
     T("Right! 4a, 2b, −6 and c: 4 terms.", "درست! 4a، 2b، −6 اور c: 4 ارکان"),
     T("The terms are 4a, 2b, −6 and c: 4.", "ارکان 4a، 2b، −6 اور c ہیں: 4"),
     common_wrong=[wrong(3, "Don't forget c on the end: it is a term too. 4 terms.", "آخر میں c نہ بھولیں: یہ بھی رکن ہے۔ 4 ارکان")]),
   number_question(
     "s5_coefficient",
     T("What is the coefficient of y in 7x + 9y − 2?", "7x + 9y − 2 میں y کا عددی سر کیا ہے؟"),
     S5,
     T("Which number is with y?", "y کے ساتھ کون سا عدد ہے؟"),
     T("Right! 9.", "درست! 9"),
     T("The term with y is 9y, so the coefficient is 9.", "y والا رکن 9y ہے، تو عددی سر 9"),
     common_wrong=[wrong(7, "7 goes with x. The coefficient of y is 9.", "7، x کے ساتھ ہے۔ y کا عددی سر 9 ہے۔"),
                   wrong(-2, "−2 has no letter: it is the constant. y's coefficient is 9.", "−2 کے ساتھ حرف نہیں: یہ مستقل ہے۔ y کا عددی سر 9", "coefficient_is_constant")]),
   {"id": "s6_constant", "type": "choice",
    "prompt": T("What is the constant in 3m − 8 + 2n?", "3m − 8 + 2n میں مستقل کیا ہے؟"),
    "options": [
      opt("minus_eight", "−8", "−8", True, "Yes! It has no letter, and the minus sign belongs to it.", "جی ہاں! اس کے ساتھ حرف نہیں، اور منفی علامت اسی کی ہے۔"),
      opt("eight", "8", "8", False, "The sign in front belongs to the term: −8.", "سامنے کی علامت رکن کی ہوتی ہے: −8", "drops_sign"),
      opt("three", "3", "3", False, "3 is the coefficient of m. The constant has no letter: −8.", "3، m کا عددی سر ہے۔ مستقل کے ساتھ حرف نہیں: −8", "coefficient_is_constant"),
    ]},
   number_question(
     "s7_lone_letter",
     T("What is the coefficient of b in a + b + 6?", "a + b + 6 میں b کا عددی سر کیا ہے؟"),
     S7,
     T("b on its own means 1 × b.", "اکیلا b یعنی 1 × b"),
     T("Right! b = 1b, so 1.", "درست! b = 1b، تو 1"),
     T("A letter on its own has coefficient 1.", "اکیلے حرف کا عددی سر 1 ہوتا ہے۔"),
     common_wrong=[wrong(0, "b is there once, so 1b: coefficient 1.", "b ایک بار ہے، یعنی 1b: عددی سر 1", "lone_letter_zero"),
                   wrong(6, "6 has no letter: it is the constant. b's coefficient is 1.", "6 کے ساتھ حرف نہیں: یہ مستقل ہے۔ b کا عددی سر 1", "coefficient_is_constant")]),
   number_question(
     "s8_negative",
     T("What is the coefficient of x in 12 − 5x?", "12 − 5x میں x کا عددی سر کیا ہے؟"),
     S8,
     T("The sign in front of 5x belongs to it.", "5x سے پہلے کی علامت اسی کی ہے۔"),
     T("Right! −5.", "درست! −5"),
     T("The term is −5x, so the coefficient is −5.", "رکن −5x ہے، تو عددی سر −5"),
     common_wrong=[wrong(5, "Keep the sign: the term is −5x, so −5.", "علامت ساتھ رکھیں: رکن −5x ہے، تو −5", "drops_sign"),
                   wrong(12, "12 is the constant. x's coefficient is −5.", "12 مستقل ہے۔ x کا عددی سر −5", "coefficient_is_constant")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("In 4p + 9, Bilal says the coefficient of p is 9. What is wrong?", "4p + 9 میں بلال کہتا ہے کہ p کا عددی سر 9 ہے۔ کیا غلطی ہے؟"),
    "options": [
      opt("four", "The coefficient is 4, the number with p. 9 is the constant.", "عددی سر 4 ہے، p کے ساتھ والا عدد۔ 9 مستقل ہے۔", True,
          "Yes! Coefficient goes with the letter; constant stands alone.", "جی ہاں! عددی سر حرف کے ساتھ؛ مستقل اکیلا۔"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "9 has no letter, so it is the constant. p's coefficient is 4.", "9 کے ساتھ حرف نہیں، تو یہ مستقل ہے۔ p کا عددی سر 4", "coefficient_is_constant"),
      opt("thirteen", "It is 13, because 4 + 9 = 13.", "یہ 13 ہے، کیونکہ 4 + 9 = 13", False,
          "4p and 9 are different terms; they are not added. p's coefficient is 4.", "4p اور 9 مختلف ارکان ہیں؛ جمع نہیں ہوتے۔ p کا عددی سر 4"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "The shopkeeper's price rule is 10x + 25. What do the 10 and the 25 mean? Teach me!",
                     "دکاندار کا قیمت کا اصول 10x + 25 ہے۔ 10 اور 25 کا کیا مطلب ہے؟ مجھے سکھائیں!"),
    "task": T("x pens and one bag cost 10x + 25 rupees. Which is the coefficient and which is the constant? What does each mean in the shop?", "x قلم اور ایک تھیلا 10x + 25 روپے کے ہیں۔ عددی سر کون سا ہے اور مستقل کون سا؟ دکان میں ہر ایک کا کیا مطلب ہے؟"),
    "key_idea": "10 is the coefficient of x: each pen costs Rs 10, so it is multiplied by the number of pens. 25 is the constant: the bag costs Rs 25 however many pens you buy.",
    "levels": {
      "got_it": "Says 10 is the coefficient (price of each pen, multiplied by x) and 25 is the constant (the bag, which doesn't change).",
      "partly": "Names the coefficient and constant correctly but doesn't say what they mean, or the other way round.",
      "not_yet": "Mixes them up or gives no reason."},
    "keywords": [
      ["coefficient", "عددی سر"],
      ["constant", "مستقل"],
      ["each pen", "per pen", "ہر قلم"],
      ["bag", "تھیلا"]],
    "fallback_feedback": {
      "got_it": T("Well explained! 10 per pen, 25 for the bag.", "بہت خوب! ہر قلم کے 10، تھیلے کے 25۔"),
      "partly": T("Good start! Now say what 10 and 25 mean in the shop.", "اچھی شروعات! اب بتائیں دکان میں 10 اور 25 کا کیا مطلب ہے۔"),
      "not_yet": T("Which number goes with x? Which one stays the same?", "کون سا عدد x کے ساتھ ہے؟ کون سا ویسا ہی رہتا ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_combine",
     T("2n + 5n can be written as one term. What is its coefficient?", "2n + 5n کو ایک رکن میں لکھا جا سکتا ہے۔ اس کا عددی سر کیا ہے؟"),
     S11,
     T("2 n's and 5 more n's.", "2 n اور 5 مزید n"),
     T("Right! 2n + 5n = 7n, coefficient 7.", "درست! 2n + 5n = 7n، عددی سر 7"),
     T("Like terms add their coefficients: 2 + 5 = 7, so 7n.", "یکساں ارکان کے عددی سر جمع ہوتے ہیں: 2 + 5 = 7، تو 7n"),
     common_wrong=[wrong(10, "Add the coefficients, don't multiply: 2 + 5 = 7.", "عددی سر جمع کریں، ضرب نہیں: 2 + 5 = 7")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Terms, variables, coefficients, constants. You can name every part now!", "ارکان، متغیر، عددی سر، مستقل۔ اب آپ ہر حصے کا نام لے سکتے ہیں!"),
    "text": T("Terms are separated by + and − signs, and each sign belongs to the term after it. The letter is the variable; the number with it is the coefficient; a number on its own is the constant. A lone letter has coefficient 1 (or −1).",
              "ارکان + اور − سے الگ ہوتے ہیں، اور ہر علامت اپنے بعد والے رکن کی ہوتی ہے۔ حرف متغیر ہے؛ اس کے ساتھ کا عدد عددی سر؛ اکیلا عدد مستقل۔ اکیلے حرف کا عددی سر 1 (یا −1) ہوتا ہے۔"),
    "points": [T("5x: coefficient 5, variable x.", "5x: عددی سر 5، متغیر x"),
               T("−7 alone: the constant.", "اکیلا −7: مستقل")]},
 ],
 "review_questions": [
   {"id": "r_terms", "type": "apply", "skill": SKILL, "step": number_question(
     "r_terms",
     T("How many terms does 2x + 3y − z + 7 have?", "2x + 3y − z + 7 کے کتنے ارکان ہیں؟"),
     R1A,
     T("Split at every + and − sign.", "ہر + اور − پر الگ کریں۔"),
     T("Right! 2x, 3y, −z and 7: 4.", "درست! 2x، 3y، −z اور 7: 4"),
     T("The terms are 2x, 3y, −z and 7.", "ارکان 2x، 3y، −z اور 7 ہیں۔"),
     common_wrong=[wrong(3, "−z is a term too: 4 terms.", "−z بھی رکن ہے: 4 ارکان")],
     qtype=None)},
   {"id": "r_coefficient", "type": "apply", "skill": SKILL, "step": number_question(
     "r_coefficient",
     T("What is the coefficient of m in 11 + 4m?", "11 + 4m میں m کا عددی سر کیا ہے؟"),
     R2A,
     T("Which number is with m?", "m کے ساتھ کون سا عدد ہے؟"),
     T("Right! 4.", "درست! 4"),
     T("The term is 4m, so the coefficient is 4. 11 is the constant.", "رکن 4m ہے، تو عددی سر 4۔ 11 مستقل ہے۔"),
     common_wrong=[wrong(11, "11 has no letter: it is the constant. m's coefficient is 4.", "11 کے ساتھ حرف نہیں: یہ مستقل ہے۔ m کا عددی سر 4", "coefficient_is_constant")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh after matching the app with PCTB Mathematics 6 (Sub-domain 6, terms, coefficients and constants). No textbook text or exercises were used.",
   "Negative coefficients (−5x, −q) use the integers taught in the Integers unit.",
   "Urdu terms to check: رکن / ارکان (term / terms), متغیر (variable), عددی سر (coefficient), مستقل (constant).",
   "The numbers were worked out in content/sources/g6-maths-07/terms_and_coefficients.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)
