from common import (T, opt, say, wrong, number_question, text_question, write, value,
                    REF, REVIEW, TIMES_TABLES, ALG_VARIABLES)

SKILL = ALG_VARIABLES

# s2
assert 6 * 7 == 42
# s4: n marbles and 4 more
assert value("n + 4", n=7) == value("4 + n", n=7) == 11 and value("4n", n=7) == 28
# s5: 6 eggs in each of b boxes
assert value("6b", b=3) == 18 and value("b + 6", b=3) == 9
# s6: 3 years younger than a
assert value("a - 3", a=12) == 9 and value("3 - a", a=12) == -9
# s8: n = 7 in n + 4
S8 = value("n + 4", n=7)
assert S8 == 11
# s11: 5 pens at p rupees
assert value("5p", p=20) == 100 and value("p + 5", p=20) == 25
# question bank and review
assert value("10 + k", k=2) == value("k + 10", k=2) == 12
assert value("4y", y=5) == 20
R2 = value("m - 8", m=20)
assert R2 == 12


def times_forms(a, b):
    """Other right ways to write a × b, like 6*b and b*6."""
    return [f"{a}*{b}", f"{b}*{a}", f"{b}{a}"]


lesson = {
 "id": "g6-maths-07-letters-for-numbers",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Use letters to stand for unknown numbers and write simple algebraic expressions from words.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Letters for numbers", "اعداد کی جگہ حروف"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": TIMES_TABLES}],
 "misconceptions": [
   {"id": "plus_vs_times", "description": "Writes 4n for 'n and 4 more', or n + 6 for '6 lots of n': mixes up adding and multiplying."},
   {"id": "subtract_order", "description": "Writes 8 − m for '8 less than m': reverses the order of a subtraction."},
   {"id": "letter_is_digit", "description": "Thinks 5x means a number like 53 (5 followed by x), not 5 × x."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_meaning", "type": "recall", "step": {
     "id": "qb_meaning", "type": "choice",
     "prompt": T("What does n + 3 mean?", "n + 3 کا کیا مطلب ہے؟"),
     "options": [
       opt("more", "3 more than n", "n سے 3 زیادہ", True, "Yes! Whatever n is, add 3.", "جی ہاں! n جو بھی ہو، اس میں 3 جمع کریں۔"),
       opt("times", "3 times n", "n کا 3 گنا", False, "3 times n is written 3n. n + 3 means add 3.", "n کا 3 گنا 3n لکھا جاتا ہے۔ n + 3 کا مطلب 3 جمع کرنا ہے۔", "plus_vs_times"),
       opt("less", "3 less than n", "n سے 3 کم", False, "3 less would be n − 3. The + means add.", "3 کم ہو تو n − 3 ہوگا۔ + کا مطلب جمع ہے۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": text_question(
     "qb_apply",
     T("Write an expression for 'k more than 10'.", "'10 سے k زیادہ' کی عبارت لکھیں۔"),
     "10 + k",
     T("Start with 10 and add k.", "10 سے شروع کریں اور k جمع کریں۔"),
     T("Right! 10 + k (or k + 10).", "درست! 10 + k (یا k + 10)"),
     T("k more than 10 is 10 + k. k + 10 is also right.", "10 سے k زیادہ یعنی 10 + k۔ k + 10 بھی درست ہے۔"),
     accept=["k + 10"],
     common_wrong=[wrong("10k", "10k means 10 × k. 'More than' means add: 10 + k.", "10k کا مطلب 10 × k ہے۔ 'زیادہ' کا مطلب جمع: 10 + k", "plus_vs_times")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Hamza writes '6 lots of x' as x + 6. What went wrong?", "حمزہ '6 دفعہ x' کو x + 6 لکھتا ہے۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("times", "6 lots of x means 6 × x, written 6x.", "6 دفعہ x کا مطلب 6 × x ہے، جو 6x لکھا جاتا ہے۔", True,
           "Yes! x + 6 means 6 more than x.", "جی ہاں! x + 6 کا مطلب x سے 6 زیادہ ہے۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "If x = 2, 6 lots of 2 is 12, but x + 6 = 8. It should be 6x.", "اگر x = 2 ہو تو 6 دفعہ 2 = 12، مگر x + 6 = 8۔ یہ 6x ہونا چاہیے۔", "plus_vs_times"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_letter", "front": T("What does a letter mean in algebra?", "الجبرا میں حرف کا کیا مطلب ہے؟"),
    "back": T("It stands for a number we don't know yet, or one that can change. n + 5 is 5 more than n.", "یہ کسی ایسے عدد کی جگہ ہے جو ابھی معلوم نہیں، یا بدل سکتا ہے۔ n + 5 یعنی n سے 5 زیادہ۔")},
   {"id": "f_times", "front": T("What does 3n mean?", "3n کا کیا مطلب ہے؟"),
    "back": T("3 × n. We leave out the × sign and write the number first.", "3 × n۔ ہم × کا نشان نہیں لکھتے اور عدد پہلے لکھتے ہیں۔")},
 ],
 "home_tasks": [{"id": "h_family", "text": T(
   "Pick a family member and call their age a. Write expressions for the ages of 3 other people using a, like a + 25 for a grandparent. Then put in the real age to check.",
   "گھر کے ایک فرد کی عمر کو a کہیں۔ a استعمال کر کے 3 اور لوگوں کی عمر کی عبارتیں لکھیں، جیسے دادا کے لیے a + 25۔ پھر اصل عمر رکھ کر جانچیں۔")}],
 "glossary": [T("Variable", "متغیر"), T("Expression", "الجبری عبارت")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Ali has a bag of marbles but won't say how many. How can we write about a number we don't know?",
                     "علی کے پاس کنچوں کا تھیلا ہے مگر وہ نہیں بتاتا کتنے ہیں۔ جو عدد معلوم نہ ہو، اس کے بارے میں کیسے لکھیں؟"),
    "text": T("Mathematicians use a letter, like n, for a number they don't know yet. First, a quick times-table check.", "ریاضی دان نامعلوم عدد کے لیے کوئی حرف، جیسے n، استعمال کرتے ہیں۔ پہلے پہاڑے کا ایک سوال۔")},
   number_question(
     "s2_foundation",
     T("What is 6 × 7?", "6 × 7 کتنا ہے؟"),
     42,
     T("6 × 7 is the same as 7 × 6.", "6 × 7 وہی ہے جو 7 × 6"),
     T("Right! 42.", "درست! 42"),
     T("6 × 7 = 42.", "6 × 7 = 42"),
     common_wrong=[wrong(13, "That is 6 + 7. Multiply: 42.", "یہ 6 + 7 ہے۔ ضرب دیں: 42")],
     qtype="recall", skill=TIMES_TABLES),
   {"id": "s3_letters", "type": "explain",
    "character": say("happy", "A letter is just a box for a number!", "حرف بس ایک عدد کا ڈبہ ہے!"),
    "text": T("Call Ali's marbles n. If he gets 5 more, he has n + 5. If he loses 2, he has n − 2. If his sister has 3 times as many, she has 3 × n, which we write 3n. These are called expressions.",
              "علی کے کنچوں کو n کہیں۔ اگر اسے 5 اور ملیں تو اس کے پاس n + 5 ہیں۔ اگر 2 گم ہو جائیں تو n − 2۔ اگر بہن کے پاس 3 گنا ہوں تو 3 × n، جسے ہم 3n لکھتے ہیں۔ انہیں الجبری عبارتیں کہتے ہیں۔")},
   text_question(
     "s4_more",
     T("Ali has n marbles. He wins 4 more. Write an expression for how many he has now.", "علی کے پاس n کنچے ہیں۔ وہ 4 اور جیتتا ہے۔ اب اس کے پاس کتنے ہیں، اس کی عبارت لکھیں۔"),
     "n + 4",
     T("Winning more means adding.", "زیادہ جیتنے کا مطلب جمع کرنا ہے۔"),
     T("Right! n + 4.", "درست! n + 4"),
     T("He has n, then 4 more: n + 4.", "اس کے پاس n ہیں، پھر 4 اور: n + 4"),
     accept=["4 + n"],
     common_wrong=[wrong("4n", "4n means 4 × n. Winning 4 more means add: n + 4.", "4n کا مطلب 4 × n ہے۔ 4 اور جیتنے کا مطلب جمع: n + 4", "plus_vs_times")]),
   text_question(
     "s5_times",
     T("A box holds 6 eggs. Write an expression for the eggs in b boxes.", "ایک ڈبے میں 6 انڈے ہیں۔ b ڈبوں کے انڈوں کی عبارت لکھیں۔"),
     "6b",
     T("b boxes of 6 means 6 × b. Leave out the × sign.", "6 کے b ڈبے یعنی 6 × b۔ × کا نشان نہ لکھیں۔"),
     T("Right! 6b.", "درست! 6b"),
     T("6 eggs in each of b boxes: 6 × b = 6b.", "ہر b ڈبے میں 6 انڈے: 6 × b = 6b"),
     accept=times_forms(6, "b"),
     common_wrong=[wrong("b + 6", "b + 6 is 6 more than b. Each box has 6, so multiply: 6b.", "b + 6 یعنی b سے 6 زیادہ۔ ہر ڈبے میں 6 ہیں، اس لیے ضرب: 6b", "plus_vs_times"),
                   wrong("6 + b", "That adds. Each box has 6, so multiply: 6b.", "یہ جمع ہے۔ ہر ڈبے میں 6 ہیں، اس لیے ضرب: 6b", "plus_vs_times")]),
   text_question(
     "s6_less",
     T("Sara is 3 years younger than her brother. Her brother is a years old. Write Sara's age.", "سارہ اپنے بھائی سے 3 سال چھوٹی ہے۔ بھائی کی عمر a سال ہے۔ سارہ کی عمر لکھیں۔"),
     "a - 3",
     T("Younger means take away. Start with the brother's age.", "چھوٹی کا مطلب گھٹانا۔ بھائی کی عمر سے شروع کریں۔"),
     T("Right! a − 3.", "درست! a − 3"),
     T("Start with a and take away 3: a − 3.", "a سے شروع کریں اور 3 گھٹائیں: a − 3"),
     common_wrong=[wrong("3 - a", "Start with the brother's age: a − 3. If a = 12, 3 − 12 makes no sense for an age.", "بھائی کی عمر سے شروع کریں: a − 3۔ اگر a = 12 ہو تو 3 − 12 عمر نہیں ہو سکتی۔", "subtract_order"),
                   wrong("a + 3", "Younger means fewer years: a − 3.", "چھوٹی کا مطلب کم سال: a − 3")]),
   {"id": "s7_meaning", "type": "choice", "question_type": "recall",
    "prompt": T("What does 5x mean?", "5x کا کیا مطلب ہے؟"),
    "options": [
      opt("times", "5 × x", "5 × x", True, "Yes! A number next to a letter means multiply.", "جی ہاں! حرف کے ساتھ لکھا عدد ضرب کا مطلب دیتا ہے۔"),
      opt("plus", "5 + x", "5 + x", False, "That would be written 5 + x. 5x means 5 × x.", "یہ 5 + x لکھا جاتا۔ 5x کا مطلب 5 × x ہے۔", "plus_vs_times"),
      opt("digit", "A number in the fifties, like 53", "پچاس کی دہائی کا عدد، جیسے 53", False, "x is not a digit. 5x means 5 × x.", "x کوئی ہندسہ نہیں۔ 5x کا مطلب 5 × x ہے۔", "letter_is_digit"),
    ]},
   number_question(
     "s8_try",
     T("Ali opens his bag: n = 7. He won 4 more, so he has n + 4. How many marbles is that?", "علی تھیلا کھولتا ہے: n = 7۔ اس نے 4 اور جیتے، تو اس کے پاس n + 4 ہیں۔ یہ کتنے کنچے ہوئے؟"),
     S8,
     T("Put 7 in place of n.", "n کی جگہ 7 رکھیں۔"),
     T("Right! 7 + 4 = 11.", "درست! 7 + 4 = 11"),
     T("n + 4 = 7 + 4 = 11.", "n + 4 = 7 + 4 = 11"),
     common_wrong=[wrong(28, "That is 4 × 7. n + 4 means add: 11.", "یہ 4 × 7 ہے۔ n + 4 کا مطلب جمع: 11", "plus_vs_times"),
                   wrong(74, "n is not a digit. Put 7 in: 7 + 4 = 11.", "n ہندسہ نہیں۔ 7 رکھیں: 7 + 4 = 11", "letter_is_digit")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Bilal writes '8 less than m' as 8 − m. What went wrong?", "بلال '8 کم m سے' کو 8 − m لکھتا ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("order", "Start with m and take 8 away: m − 8.", "m سے شروع کریں اور 8 گھٹائیں: m − 8", True,
          "Yes! If m = 20, 8 less is 12 = 20 − 8, not 8 − 20.", "جی ہاں! اگر m = 20 ہو تو 8 کم یعنی 12 = 20 − 8، نہ کہ 8 − 20"),
      opt("plus", "It should be m + 8.", "یہ m + 8 ہونا چاہیے۔", False,
          "'Less' means take away, so it is m − 8.", "'کم' کا مطلب گھٹانا، اس لیے m − 8", None),
      opt("nothing", "Nothing. 8 − m and m − 8 are the same.", "کوئی غلطی نہیں۔ 8 − m اور m − 8 ایک ہی ہیں۔", False,
          "Order matters in subtraction: 20 − 8 = 12 but 8 − 20 is negative.", "تفریق میں ترتیب اہم ہے: 20 − 8 = 12 مگر 8 − 20 منفی ہے۔", "subtract_order"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why not just guess a number for Ali's marbles? Why is a letter better? Can you teach me?",
                     "علی کے کنچوں کے لیے بس کوئی عدد کیوں نہ سوچ لیں؟ حرف کیوں بہتر ہے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why do we use a letter like n instead of a number when we don't know how many?",
              "اپنے الفاظ میں بتائیں: جب ہمیں معلوم نہ ہو کہ کتنے ہیں تو عدد کی بجائے n جیسا حرف کیوں استعمال کرتے ہیں؟"),
    "key_idea": "A letter stands for any number we don't know yet. An expression like n + 4 is true whatever n turns out to be; a guessed number could be wrong.",
    "levels": {
      "got_it": "Explains that the letter stands for the unknown or changing number, so the expression works whatever the number is.",
      "partly": "Says the letter is the unknown number, without saying why that is better than guessing.",
      "not_yet": "Gives no reason, or thinks the letter is a fixed number or a digit."},
    "keywords": [
      ["unknown", "don't know", "any", "نامعلوم", "معلوم نہیں", "koi bhi"],
      ["stand", "instead", "place", "جگہ", "jagah"],
      ["guess", "wrong", "change", "اندازہ", "غلط", "بدل"]],
    "fallback_feedback": {
      "got_it": T("Well explained! n + 4 is right whatever n is; a guess might be wrong.", "بہت خوب! n + 4 ہر n کے لیے درست ہے؛ اندازہ غلط ہو سکتا ہے۔"),
      "partly": T("Good start! Now say: what goes wrong if we guess 10 and Ali really has 7?", "اچھی شروعات! اب بتائیں: اگر ہم 10 سوچیں اور علی کے پاس اصل میں 7 ہوں تو کیا گڑبڑ ہوگی؟"),
      "not_yet": T("Think: n + 4 works if Ali has 7, 20 or 100 marbles. Does a guess do that?", "سوچیں: n + 4 تب بھی درست ہے جب علی کے پاس 7، 20 یا 100 کنچے ہوں۔ کیا اندازہ ایسا کرتا ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   text_question(
     "s11_cost",
     T("A pen costs p rupees. Write the cost of 5 pens.", "ایک قلم کی قیمت p روپے ہے۔ 5 قلموں کی قیمت لکھیں۔"),
     "5p",
     T("5 pens at p rupees each: 5 × p.", "p روپے والے 5 قلم: 5 × p"),
     T("Right! 5p rupees.", "درست! 5p روپے"),
     T("5 × p = 5p.", "5 × p = 5p"),
     accept=times_forms(5, "p"),
     common_wrong=[wrong("p + 5", "That is 5 rupees more. 5 pens means 5 × p = 5p.", "یہ 5 روپے زیادہ ہے۔ 5 قلم یعنی 5 × p = 5p", "plus_vs_times")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "You can write algebra now!", "اب آپ الجبرا لکھ سکتے ہیں!"),
    "text": T("A letter stands for a number we don't know yet. More: add (n + 5). Less: take away, starting with the letter (n − 2). Lots of: multiply, number first (3n means 3 × n).",
              "حرف کسی نامعلوم عدد کی جگہ ہوتا ہے۔ زیادہ: جمع (n + 5)۔ کم: حرف سے شروع کر کے گھٹائیں (n − 2)۔ گنا: ضرب، عدد پہلے (3n یعنی 3 × n)۔"),
    "points": [T("3n means 3 × n, not a number like 35.", "3n یعنی 3 × n، نہ کہ 35 جیسا عدد۔"),
               T("In subtraction, order matters: m − 8 is not 8 − m.", "تفریق میں ترتیب اہم ہے: m − 8 اور 8 − m برابر نہیں۔")]},
 ],
 "review_questions": [
   {"id": "r_times", "type": "apply", "skill": SKILL, "step": text_question(
     "r_times",
     T("Write an expression for '4 times y'.", "'y کا 4 گنا' کی عبارت لکھیں۔"),
     "4y",
     T("Number first, no × sign.", "عدد پہلے، × کے بغیر۔"),
     T("Right! 4y.", "درست! 4y"),
     T("4 × y = 4y.", "4 × y = 4y"),
     accept=times_forms(4, "y"),
     common_wrong=[wrong("y + 4", "That is 4 more than y. 4 times y is 4y.", "یہ y سے 4 زیادہ ہے۔ y کا 4 گنا 4y ہے۔", "plus_vs_times")],
     qtype=None)},
   {"id": "r_less", "type": "recall", "skill": SKILL, "step": number_question(
     "r_less",
     T("m − 8 means 8 less than m. If m = 20, what is m − 8?", "m − 8 یعنی m سے 8 کم۔ اگر m = 20 ہو تو m − 8 کتنا ہے؟"),
     R2,
     T("20 − 8.", "20 − 8"),
     T("Right! 12.", "درست! 12"),
     T("m − 8 = 20 − 8 = 12.", "m − 8 = 20 − 8 = 12"),
     common_wrong=[wrong(28, "That adds. m − 8 takes 8 away: 12.", "یہ جمع ہے۔ m − 8 میں 8 گھٹاتے ہیں: 12")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Introduction to Algebra unit. No textbook text or exercises were used.",
   "Typed expressions are checked as text: spaces, capitals and the × sign don't matter, and other right orders (4 + n, b6) are accepted.",
   "Urdu terms to check: متغیر (variable), الجبری عبارت (expression).",
   "The numbers were worked out in content/sources/g6-maths-07/letters_for_numbers.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
# ---------- pictures ----------
from figs import (attach, figure, strip, strip_figure, dot_array, bar_model, egg_box, pen,
                  point, line, label, W)

ROWS2, COLS2 = 6, 7                      # s2: 6 × 7
EXTRA4 = 4                               # s4: n + 4
EGGS = 6                                 # s5: 6 eggs in each box
N8, MORE8 = 7, 4                         # s8: n = 7, n + 4
assert value("n + 4", n=N8) == S8 and MORE8 == EXTRA4
AGE_A, YOUNGER = 12, 3                   # s6: a − 3 (drawn for a = 12)
assert value("a - 3", a=AGE_A) == AGE_A - YOUNGER
PENS = 5                                 # s11: 5p
TEN = 10                                 # qb: k more than 10
LOTS = 6                                 # qb_find_error: 6 lots of x
M_R, LESS_R = 20, 8                      # review: m − 8 with m = 20
assert value("m - 8", m=M_R) == R2

MORE3, LESS3, TIMES3 = 5, 2, 3           # s3: n + 5, n − 2, 3n


def three_ways():
    rows = [
        [("bag", "n"), ("text", "+"), ("marbles", MORE3), ("text", "="), ("text", f"n+{MORE3}")],
        [("bag", "n"), ("text", "−"), ("dmarbles", LESS3), ("text", "="), ("text", f"n−{LESS3}")],
        [("bags", TIMES3, "n"), ("text", "="), ("text", f"{TIMES3}n")],
    ]
    items = []
    for i, row in enumerate(rows):
        items += strip(row, 46 + i * 50, gap=12)
    return figure(W, 160,
        f"Three rows, each with a bag of marbles marked n (n is how many marbles are in a bag). Top: a bag plus {MORE3} marbles is n+{MORE3}. Middle: a bag with {LESS3} dashed marbles taken away is n−{LESS3}. Bottom: {TIMES3} bags is {TIMES3}n.",
        f"تین قطاریں، ہر ایک میں کنچوں کا تھیلا جس پر n لکھا ہے (n ایک تھیلے کے کنچوں کی تعداد ہے)۔ اوپر: ایک تھیلا جمع {MORE3} کنچے n+{MORE3} ہے۔ درمیان: ایک تھیلا جس میں سے {LESS3} ڈیش والے کنچے نکالے گئے n−{LESS3} ہے۔ نیچے: {TIMES3} تھیلے {TIMES3}n ہیں۔",
        items)


def egg_boxes():
    items = []
    for i, x in enumerate((50, 116)):
        items += egg_box(x, 14, EGGS)
    items += [point((186, 32)), point((198, 32)), point((210, 32))]
    items += egg_box(222, 14, EGGS)
    items += [line((50, 60), (50, 66)), line((50, 66), (274, 66)), line((274, 66), (274, 60)),
              label((162, 80), "b")]
    return figure(W, 92,
        f"Egg boxes in a row, each holding {EGGS} eggs; dots show that more boxes follow. A bracket under all the boxes is marked b: there are b boxes.",
        f"ایک قطار میں انڈوں کے ڈبے، ہر ایک میں {EGGS} انڈے؛ نقطے بتاتے ہیں کہ اور ڈبے بھی ہیں۔ سب ڈبوں کے نیچے ایک قوس پر b لکھا ہے: کل b ڈبے ہیں۔",
        items)


def pens():
    items = []
    for i in range(PENS):
        items += pen(70 + i * 40, 92, "p")
    return figure(W, 100,
        f"{PENS} pens in a row, each marked p: every pen costs p rupees.",
        f"ایک قطار میں {PENS} قلم، ہر ایک پر p لکھا ہے: ہر قلم p روپے کا ہے۔",
        items)


attach(lesson, {
    "s1_hook": strip_figure([("bag", "n"), ("text", "="), ("text", "?")],
        "A closed bag of marbles marked n, then = ? : we don't know how many marbles are inside, so we call the number n.",
        "کنچوں کا بند تھیلا جس پر n لکھا ہے، پھر = ? : ہمیں نہیں معلوم اندر کتنے کنچے ہیں، اس لیے اس عدد کو n کہتے ہیں۔"),
    "s2_foundation": dot_array(ROWS2, COLS2,
        f"Dots in {ROWS2} rows with {COLS2} dots in each row.",
        f"نقطوں کی {ROWS2} قطاریں، ہر قطار میں {COLS2} نقطے۔"),
    "s3_letters": three_ways(),
    "s4_more": strip_figure([("bag", "n"), ("text", "+"), ("marbles", EXTRA4)],
        f"Ali's bag marked n (the marbles he has), a plus sign and {EXTRA4} more marbles.",
        f"علی کا تھیلا جس پر n لکھا ہے (اس کے کنچے)، جمع کا نشان اور {EXTRA4} مزید کنچے۔"),
    "s5_times": egg_boxes(),
    "s6_less": bar_model([[(AGE_A, "a", False)], [(AGE_A - YOUNGER, None, False), (YOUNGER, str(YOUNGER), True)]],
        f"Two bars. The top bar, B, is the brother's age, a. The bottom bar, S, is Sara's age: it is shorter, and the dashed piece marked {YOUNGER} shows the {YOUNGER} years it is missing.",
        f"دو پٹیاں۔ اوپر والی پٹی B بھائی کی عمر a ہے۔ نیچے والی پٹی S ثنا کی عمر ہے: یہ چھوٹی ہے، اور {YOUNGER} والا ڈیش ٹکڑا وہ {YOUNGER} سال دکھاتا ہے جو اس میں کم ہیں۔",
        names=("B", "S")),
    "s8_try": strip_figure([("text", "n"), ("text", "="), ("marbles", N8, 4), ("text", "+"), ("marbles", MORE8, 4)],
        f"n = {N8}: Ali's {N8} marbles, a plus sign, and the {MORE8} marbles he won.",
        f"n = {N8}: علی کے {N8} کنچے، جمع کا نشان، اور وہ {MORE8} کنچے جو اس نے جیتے۔"),
    "s11_cost": pens(),
    "s12_summary": three_ways(),
    "qb_apply": strip_figure([("marbles", TEN), ("text", "+"), ("bag", "k")],
        f"{TEN} marbles, a plus sign and a bag marked k (k more marbles).",
        f"{TEN} کنچے، جمع کا نشان اور ایک تھیلا جس پر k لکھا ہے (k مزید کنچے)۔"),
    "qb_find_error": strip_figure([("bags", LOTS, "x")],
        f"{LOTS} bags in a row, each marked x: {LOTS} lots of x.",
        f"ایک قطار میں {LOTS} تھیلے، ہر ایک پر x لکھا ہے: x کے {LOTS} گروہ۔"),
    "r_less": bar_model([[(M_R, str(M_R), False)], [(M_R - LESS_R, None, False), (LESS_R, str(LESS_R), True)]],
        f"Two bars. The top bar is m = {M_R}. The bottom bar is m − {LESS_R}: the same length with a dashed piece of {LESS_R} taken away from the end.",
        f"دو پٹیاں۔ اوپر والی پٹی m = {M_R} ہے۔ نیچے والی پٹی m − {LESS_R} ہے: اتنی ہی لمبی، آخر سے {LESS_R} کا ڈیش ٹکڑا نکالا گیا ہے۔"),
})
write(lesson)
