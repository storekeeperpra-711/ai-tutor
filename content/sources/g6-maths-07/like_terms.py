from common import (T, opt, say, wrong, number_question, text_question, write, value,
                    REF, REVIEW, ALG_SUBSTITUTION, ALG_LIKE_TERMS)

SKILL = ALG_LIKE_TERMS


def same(left, right, /, **ranges):
    """Two expressions give the same value for many numbers."""
    names = list(ranges)
    import itertools
    for vals in itertools.product(*ranges.values()):
        v = dict(zip(names, vals))
        if value(left, **v) != value(right, **v):
            return False
    return True


R = range(-5, 6)
# s2
assert value("2x + 3", x=5) == 13
# s4, s5
assert same("4x + 3x", "7x", x=R) and not same("4x + 3x", "12x", x=R)
assert same("9m - 4m", "5m", m=R) and not same("9m - 4m", "13m", m=R)
# s7
assert same("3x + 4 + 4x", "7x + 4", x=R) and not same("3x + 4 + 4x", "11x", x=R)
# s8
assert same("2a + 3b + 4a + b", "6a + 4b", a=R, b=R) and not same("2a + 3b + 4a + b", "6a + 3b", a=R, b=R)
# s9, s10: 3a + 2b is not 5ab
assert not same("3a + 2b", "5*a*b", a=R, b=R)
# s11
S11 = value("7x + 4", x=2)
assert S11 == value("3x + 4 + 4x", x=2) == 18
# question bank and review
assert same("5p + 2 + p", "6p + 2", p=R) and not same("5p + 2 + p", "8p", p=R)
assert same("6n - n", "5n", n=R)
assert same("8k - 3k", "5k", k=R) and same("a + a + a", "3a", a=R)


lesson = {
 "id": "g6-maths-07-like-terms",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Recognise like terms and simplify expressions by collecting them.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Collecting like terms", "یکساں رقوم جمع کرنا"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": ALG_SUBSTITUTION}],
 "misconceptions": [
   {"id": "joins_unlike", "description": "Combines unlike terms: 3a + 2b = 5ab, or 3x + 4 = 7x."},
   {"id": "drops_letter", "description": "Adds the numbers and drops the letter: 3a + 2a = 5."},
   {"id": "multiplies_terms", "description": "Multiplies instead of adding: 4x + 3x = 12x."},
   {"id": "forgets_one", "description": "Forgets that a letter on its own means 1 of it: b counted as 0b."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_like", "type": "recall", "step": {
     "id": "qb_like", "type": "choice",
     "prompt": T("Which two are like terms?", "کون سی دو یکساں رقوم ہیں؟"),
     "options": [
       opt("same", "3y and 7y", "3y اور 7y", True, "Yes! Same letter, so they can be added: 10y.", "جی ہاں! ایک ہی حرف، اس لیے جمع ہو سکتی ہیں: 10y"),
       opt("diff", "3y and 7x", "3y اور 7x", False, "Different letters are unlike terms. 3y and 7y are alike.", "مختلف حروف یکساں رقوم نہیں۔ 3y اور 7y یکساں ہیں۔", "joins_unlike"),
       opt("num", "3y and 7", "3y اور 7", False, "7 has no letter, so it is not like 3y. 3y and 7y are alike.", "7 میں حرف نہیں، اس لیے یہ 3y جیسی نہیں۔ 3y اور 7y یکساں ہیں۔", "joins_unlike"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": text_question(
     "qb_apply",
     T("Simplify 5p + 2 + p.", "5p + 2 + p کو مختصر کریں۔"),
     "6p + 2",
     T("p on its own is 1p. Collect the p terms; the 2 stays.", "اکیلا p یعنی 1p۔ p والی رقوم جمع کریں؛ 2 ویسے ہی رہے گا۔"),
     T("Right! 6p + 2.", "درست! 6p + 2"),
     T("5p + p = 6p, and the 2 stays: 6p + 2.", "5p + p = 6p، اور 2 ویسے ہی: 6p + 2"),
     accept=["2 + 6p"],
     common_wrong=[wrong("8p", "2 has no letter, so it can't join the p terms: 6p + 2.", "2 میں حرف نہیں، اس لیے p والی رقوم سے نہیں ملتا: 6p + 2", "joins_unlike"),
                   wrong("5p + 2", "Don't forget the last p (that's 1p): 6p + 2.", "آخری p نہ بھولیں (یہ 1p ہے): 6p + 2", "forgets_one")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Noor says 6n − n = 6. What went wrong?", "نور کہتی ہے 6n − n = 6۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("right", "n is 1n, so 6n − 1n = 5n.", "n یعنی 1n، تو 6n − 1n = 5n", True,
           "Yes! 6 lots of n take away 1 lot of n leaves 5n.", "جی ہاں! n کے 6 میں سے 1 گھٹائیں تو 5n بچتے ہیں۔"),
       opt("nothing", "Nothing. The n's cancel.", "کوئی غلطی نہیں۔ n کٹ جاتے ہیں۔", False,
           "Try n = 2: 6 × 2 − 2 = 10, not 6. The answer is 5n.", "n = 2 رکھیں: 6 × 2 − 2 = 10، نہ کہ 6۔ جواب 5n ہے۔", "drops_letter"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_like", "front": T("What are like terms?", "یکساں رقوم کیا ہیں؟"),
    "back": T("Terms with the same letter, like 3a and 2a. Add their numbers: 3a + 2a = 5a.", "ایک ہی حرف والی رقوم، جیسے 3a اور 2a۔ ان کے اعداد جمع کریں: 3a + 2a = 5a")},
   {"id": "f_unlike", "front": T("Can 3a + 2b be simplified?", "کیا 3a + 2b مختصر ہو سکتا ہے؟"),
    "back": T("No. Different letters are unlike terms, so it stays 3a + 2b (never 5ab).", "نہیں۔ مختلف حروف یکساں رقوم نہیں، اس لیے یہ 3a + 2b ہی رہے گا (5ab کبھی نہیں)۔")},
 ],
 "home_tasks": [{"id": "h_fruit", "text": T(
   "Put some mangoes (m) and bananas (b) in two groups, for example 3m + 2b and 4m + 1b. Join the groups. How many of each do you have? Write it as an expression.",
   "کچھ آم (m) اور کیلے (b) دو گروہوں میں رکھیں، مثلاً 3m + 2b اور 4m + 1b۔ دونوں گروہ ملائیں۔ ہر ایک کتنے ہیں؟ اسے عبارت کی شکل میں لکھیں۔")}],
 "glossary": [T("Term", "رقم"), T("Like terms", "یکساں رقوم"), T("Simplify", "مختصر کرنا")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "3 apples and 2 apples make 5 apples. But what do 3 apples and 2 bananas make?",
                     "3 سیب اور 2 سیب مل کر 5 سیب۔ مگر 3 سیب اور 2 کیلے مل کر کیا بنتے ہیں؟"),
    "text": T("Today we tidy up expressions by joining the parts that are alike. First, a quick check.", "آج ہم عبارتوں کے یکساں حصے ملا کر انہیں مختصر کریں گے۔ پہلے ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("Find the value of 2x + 3 when x = 5.", "جب x = 5 ہو تو 2x + 3 کی قیمت معلوم کریں۔"),
     13,
     T("2 × 5 first, then add 3.", "پہلے 2 × 5، پھر 3 جمع۔"),
     T("Right! 10 + 3 = 13.", "درست! 10 + 3 = 13"),
     T("2 × 5 = 10, then 10 + 3 = 13.", "2 × 5 = 10، پھر 10 + 3 = 13"),
     common_wrong=[wrong(28, "2x is 2 × x, not 25. 10 + 3 = 13.", "2x یعنی 2 × x، نہ کہ 25۔ 10 + 3 = 13")],
     qtype="recall", skill=ALG_SUBSTITUTION),
   {"id": "s3_like", "type": "explain",
    "character": say("happy", "Same letter? Join them! Different letters? Leave them!", "ایک ہی حرف؟ ملا دیں! مختلف حروف؟ رہنے دیں!"),
    "text": T("Each part of an expression is a term. Terms with the same letter are like terms: 3a + 2a = 5a, just like 3 apples + 2 apples. Terms with different letters are unlike: 3a + 2b stays as it is. A letter on its own, like b, means 1b.",
              "عبارت کا ہر حصہ ایک رقم ہے۔ ایک ہی حرف والی رقوم یکساں رقوم ہیں: 3a + 2a = 5a، جیسے 3 سیب + 2 سیب۔ مختلف حروف والی رقوم یکساں نہیں: 3a + 2b ویسے ہی رہتا ہے۔ اکیلا حرف، جیسے b، یعنی 1b۔")},
   text_question(
     "s4_add",
     T("Simplify 4x + 3x.", "4x + 3x کو مختصر کریں۔"),
     "7x",
     T("4 x's and 3 more x's.", "4 x اور 3 مزید x"),
     T("Right! 7x.", "درست! 7x"),
     T("4x + 3x = 7x.", "4x + 3x = 7x"),
     accept=["7*x", "x7"],
     common_wrong=[wrong("7", "Keep the letter: 7 x's, so 7x.", "حرف رکھیں: 7 x، یعنی 7x", "drops_letter"),
                   wrong("12x", "Add, don't multiply: 4 + 3 = 7, so 7x.", "ضرب نہیں، جمع کریں: 4 + 3 = 7، یعنی 7x", "multiplies_terms")]),
   text_question(
     "s5_subtract",
     T("Simplify 9m − 4m.", "9m − 4m کو مختصر کریں۔"),
     "5m",
     T("9 m's take away 4 m's.", "9 m میں سے 4 m گھٹائیں۔"),
     T("Right! 5m.", "درست! 5m"),
     T("9 − 4 = 5, so 5m.", "9 − 4 = 5، یعنی 5m"),
     accept=["5*m", "m5"],
     common_wrong=[wrong("5", "Keep the letter: 5m.", "حرف رکھیں: 5m", "drops_letter"),
                   wrong("13m", "It's minus: 9 − 4 = 5, so 5m.", "یہ تفریق ہے: 9 − 4 = 5، یعنی 5m")]),
   {"id": "s6_which", "type": "choice", "question_type": "recall",
    "prompt": T("Which expression can be made shorter?", "کون سی عبارت مختصر ہو سکتی ہے؟"),
    "options": [
      opt("like", "2a + 5a", "2a + 5a", True, "Yes! Same letter: 2a + 5a = 7a.", "جی ہاں! ایک ہی حرف: 2a + 5a = 7a"),
      opt("unlike", "2a + 5b", "2a + 5b", False, "Different letters can't be joined. 2a + 5a can: 7a.", "مختلف حروف نہیں ملتے۔ 2a + 5a مل سکتے ہیں: 7a", "joins_unlike"),
      opt("number", "2a + 5", "2a + 5", False, "5 has no letter, so it can't join 2a. 2a + 5a can: 7a.", "5 میں حرف نہیں، اس لیے 2a سے نہیں ملتا۔ 2a + 5a مل سکتے ہیں: 7a", "joins_unlike"),
    ]},
   text_question(
     "s7_with_number",
     T("Simplify 3x + 4 + 4x.", "3x + 4 + 4x کو مختصر کریں۔"),
     "7x + 4",
     T("Join the x terms. The 4 has no letter, so it stays.", "x والی رقوم ملائیں۔ 4 میں حرف نہیں، وہ ویسے ہی رہے گا۔"),
     T("Right! 7x + 4.", "درست! 7x + 4"),
     T("3x + 4x = 7x, and the 4 stays: 7x + 4.", "3x + 4x = 7x، اور 4 ویسے ہی: 7x + 4"),
     accept=["4 + 7x"],
     common_wrong=[wrong("11x", "4 has no letter, so it can't join the x terms: 7x + 4.", "4 میں حرف نہیں، اس لیے x والی رقوم سے نہیں ملتا: 7x + 4", "joins_unlike"),
                   wrong("11", "Only the x terms join, and keep the letter: 7x + 4.", "صرف x والی رقوم ملتی ہیں، اور حرف رکھیں: 7x + 4", "drops_letter")]),
   text_question(
     "s8_two_letters",
     T("Simplify 2a + 3b + 4a + b.", "2a + 3b + 4a + b کو مختصر کریں۔"),
     "6a + 4b",
     T("a's together, b's together. b on its own is 1b.", "a ایک ساتھ، b ایک ساتھ۔ اکیلا b یعنی 1b"),
     T("Right! 6a + 4b.", "درست! 6a + 4b"),
     T("2a + 4a = 6a and 3b + 1b = 4b: 6a + 4b.", "2a + 4a = 6a اور 3b + 1b = 4b: 6a + 4b"),
     accept=["4b + 6a"],
     common_wrong=[wrong("6a + 3b", "The last b counts as 1b: 3b + 1b = 4b.", "آخری b کو 1b گنیں: 3b + 1b = 4b", "forgets_one"),
                   wrong("10ab", "a's and b's are unlike, so they stay apart: 6a + 4b.", "a اور b یکساں نہیں، اس لیے الگ رہتے ہیں: 6a + 4b", "joins_unlike")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Kamran simplifies 3a + 2b to 5ab. What went wrong?", "کامران 3a + 2b کو 5ab بنا دیتا ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("unlike", "a and b are unlike terms, so it stays 3a + 2b.", "a اور b یکساں رقوم نہیں، اس لیے یہ 3a + 2b ہی رہے گا۔", True,
          "Yes! Like 3 apples and 2 bananas: you can't call them 5 'apple-bananas'.", "جی ہاں! جیسے 3 سیب اور 2 کیلے: انہیں 5 'سیب کیلے' نہیں کہہ سکتے۔"),
      opt("five", "It should be 5a.", "یہ 5a ہونا چاہیے۔", False,
          "The b's aren't a's. It stays 3a + 2b.", "b کو a نہیں بنا سکتے۔ یہ 3a + 2b ہی رہے گا۔", "joins_unlike"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "Try a = 1, b = 1: 3 + 2 = 5, but 5ab = 5. Try a = 2, b = 1: 8, but 5ab = 10. Not the same!", "a = 1، b = 1 پر 3 + 2 = 5 اور 5ab = 5۔ a = 2، b = 1 پر 8، مگر 5ab = 10۔ برابر نہیں!", "joins_unlike"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why can we join 3a + 2a but not 3a + 2b? Can you teach me?",
                     "ہم 3a + 2a کو کیوں ملا سکتے ہیں مگر 3a + 2b کو کیوں نہیں؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why does 3a + 2a make 5a, but 3a + 2b can't be made shorter?",
              "اپنے الفاظ میں بتائیں: 3a + 2a کیوں 5a بنتا ہے، مگر 3a + 2b کیوں مختصر نہیں ہو سکتا؟"),
    "key_idea": "a and b can stand for different numbers. 3a + 2a is 5 lots of the same thing, but a and b are different things (like apples and bananas), so they can't be counted together.",
    "levels": {
      "got_it": "Explains that like terms are the same kind of thing (same letter, same number) so they can be counted together, while a and b are different.",
      "partly": "Says the letters must be the same, without saying why.",
      "not_yet": "Says 3a + 2b is 5ab, or gives no reason."},
    "keywords": [
      ["same", "like", "ایک", "یکساں", "same letter"],
      ["different", "unlike", "مختلف", "alag"],
      ["apple", "banana", "سیب", "کیلے", "thing", "چیز"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Same letter, same kind of thing; different letters, different things.", "بہت خوب! ایک حرف، ایک جیسی چیز؛ مختلف حروف، مختلف چیزیں۔"),
      "partly": T("Good start! Now say why: what could a and b stand for?", "اچھی شروعات! اب وجہ بتائیں: a اور b کس کی جگہ ہو سکتے ہیں؟"),
      "not_yet": T("Think of 3 apples and 2 bananas. Is that 5 apples? Is it 5 bananas?", "3 سیب اور 2 کیلے سوچیں۔ کیا یہ 5 سیب ہیں؟ کیا 5 کیلے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_check",
     T("We said 3x + 4 + 4x = 7x + 4. Check it: what is 7x + 4 when x = 2? (3x + 4 + 4x gives the same.)", "ہم نے کہا 3x + 4 + 4x = 7x + 4۔ جانچیں: x = 2 پر 7x + 4 کتنا ہے؟ (3x + 4 + 4x کا جواب بھی یہی ہوگا۔)"),
     S11,
     T("7 × 2 first, then add 4.", "پہلے 7 × 2، پھر 4 جمع۔"),
     T("Right! 18. And 6 + 4 + 8 = 18 too. Same!", "درست! 18۔ اور 6 + 4 + 8 بھی 18۔ برابر!"),
     T("7 × 2 + 4 = 14 + 4 = 18.", "7 × 2 + 4 = 14 + 4 = 18"),
     common_wrong=[wrong(22, "Multiply first: 7 × 2 = 14, then + 4 = 18.", "پہلے ضرب: 7 × 2 = 14، پھر + 4 = 18"),
                   wrong(76, "7x is 7 × x, not 72. 14 + 4 = 18.", "7x یعنی 7 × x، نہ کہ 72۔ 14 + 4 = 18")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Your expressions are neat and tidy now!", "اب آپ کی عبارتیں صاف ستھری ہیں!"),
    "text": T("Like terms have the same letter. Add or take away their numbers and keep the letter: 4x + 3x = 7x. Unlike terms, and plain numbers, stay apart: 3x + 4 + 4x = 7x + 4. A letter on its own means 1 of it.",
              "یکساں رقوم میں ایک ہی حرف ہوتا ہے۔ ان کے اعداد جمع یا تفریق کریں اور حرف رکھیں: 4x + 3x = 7x۔ غیر یکساں رقوم اور خالی اعداد الگ رہتے ہیں: 3x + 4 + 4x = 7x + 4۔ اکیلا حرف یعنی اس کا 1۔"),
    "points": [T("3a + 2b is never 5ab.", "3a + 2b کبھی 5ab نہیں ہوتا۔"),
               T("Check by putting in a number: both forms give the same value.", "کوئی عدد رکھ کر جانچیں: دونوں شکلوں کی قیمت برابر آتی ہے۔")]},
 ],
 "review_questions": [
   {"id": "r_subtract", "type": "apply", "skill": SKILL, "step": text_question(
     "r_subtract",
     T("Simplify 8k − 3k.", "8k − 3k کو مختصر کریں۔"),
     "5k",
     T("8 − 3, and keep the k.", "8 − 3، اور k رکھیں۔"),
     T("Right! 5k.", "درست! 5k"),
     T("8 − 3 = 5, so 5k.", "8 − 3 = 5، یعنی 5k"),
     accept=["5*k", "k5"],
     common_wrong=[wrong("5", "Keep the letter: 5k.", "حرف رکھیں: 5k", "drops_letter")],
     qtype=None)},
   {"id": "r_repeat", "type": "recall", "skill": SKILL, "step": text_question(
     "r_repeat",
     T("Simplify a + a + a.", "a + a + a کو مختصر کریں۔"),
     "3a",
     T("How many a's are there?", "کتنے a ہیں؟"),
     T("Right! 3a.", "درست! 3a"),
     T("Three a's: 3a.", "تین a: 3a"),
     accept=["3*a", "a3"],
     common_wrong=[wrong("aaa", "Three a's added is 3a.", "تین a جمع کریں تو 3a"),
                   wrong("3", "Keep the letter: 3a.", "حرف رکھیں: 3a", "drops_letter")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Introduction to Algebra unit. No textbook text or exercises were used.",
   "Answers are typed and checked as text, accepting other orders (4 + 7x). The script checks every simplification by putting in many numbers.",
   "This lesson's skill (maths.algebra.expressions_basic) is the warm-up skill of the Grade 9 linear equations lesson.",
   "Urdu terms to check: رقم (term), یکساں رقوم (like terms), مختصر کرنا (simplify).",
   "The numbers were worked out in content/sources/g6-maths-07/like_terms.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
# ---------- pictures ----------
from common import expr
from figs import (attach, figure, tiles_figure, tiles_en, tiles_ur, strip_figure, mango, banana,
                  label, expr_text, W)


def shows(terms, written):
    """The tiles drawn are the expression in the step."""
    assert expr(*terms).replace(" ", "") == written.replace(" ", ""), (terms, written)
    return terms


def fruit():
    """3 apples + 2 apples = 5 apples; 3 apples + 2 bananas = ?"""
    items = []
    y1, y2 = 26, 76
    xs = [40 + i * 22 for i in range(3)]
    items += [mango(x, y1) for x in xs] + [label((118, y1), "+")]
    items += [mango(140 + i * 22, y1) for i in range(2)] + [label((190, y1), "=")]
    items += [mango(214 + i * 18, y1) for i in range(5)]
    items += [mango(x, y2) for x in xs] + [label((118, y2), "+")]
    for i in range(2):
        items += banana(148 + i * 30, y2 + 4)
    items += [label((206, y2), "="), label((230, y2), "?")]
    return figure(W, 100,
        "Top row: 3 apples (shaded circles) plus 2 apples equals 5 apples. Bottom row: 3 apples plus 2 bananas (curved shapes) equals a question mark.",
        "اوپر کی قطار: 3 سیب (رنگے دائرے) جمع 2 سیب برابر 5 سیب۔ نیچے کی قطار: 3 سیب جمع 2 کیلے (مڑی ہوئی شکلیں) برابر سوالیہ نشان۔",
        items)


def tiles(rows, letters, en, ur, **kw):
    return tiles_figure(rows, letters, f"{en} {tiles_en(letters)}", f"{ur} {tiles_ur(letters)}", **kw)


def one_row(terms, letters, written):
    shows(terms, written)
    return tiles([[("terms", terms)]], letters,
        f"Algebra tiles for {expr_text(terms)}, each group named above it",
        f"{expr_text(terms)} کی الجبرا ٹائلیں، ہر گروہ کا نام اس کے اوپر")


def two_groups(a, op, b, letters, written):
    shows([a, (b[0] if op == "+" else -b[0], b[1])], written)
    return tiles([[("terms", [a]), ("op", op), ("terms", [b])]], letters,
        f"Algebra tiles: a group for {expr_text([a])}, then {op}, then a group for {expr_text([b])}",
        f"الجبرا ٹائلیں: {expr_text([a])} کا گروہ، پھر {op}، پھر {expr_text([b])} کا گروہ")


A3, B3 = 3, 2                              # s3: 3a + 2a = 5a, 3a + 2b stays
assert same(f"{A3}a + {B3}a", f"{A3 + B3}a", a=R)
S7 = shows([(3, "x"), (4, ""), (4, "x")], "3x + 4 + 4x")
S7_DONE = [(7, "x"), (4, "")]
assert same(expr(*S7), expr(*S7_DONE), x=R)

attach(lesson, {
    "s1_hook": fruit(),
    "s2_foundation": strip_figure([("bags", 2, "x"), ("text", "+"), ("marbles", 3), ("text", "x=5")],
        "2 bags marked x, a plus sign and 3 marbles, which is 2x + 3. Beside them: x=5, each bag holds 5 marbles.",
        "2 تھیلے جن پر x لکھا ہے، جمع کا نشان اور 3 کنچے، یعنی 2x + 3۔ ساتھ میں: x=5، ہر تھیلے میں 5 کنچے ہیں۔"),
    "s3_like": tiles([[("terms", [(A3, "a")]), ("op", "+"), ("terms", [(B3, "a")]), ("op", "="), ("terms", [(A3 + B3, "a")])],
                      [("terms", [(A3, "a")]), ("op", "+"), ("terms", [(B3, "b")])]], ("a", "b"),
        "Top row: 3 a-tiles plus 2 a-tiles make 5 a-tiles, so 3a + 2a = 5a. Bottom row: 3 a-tiles and 2 b-tiles are different tiles, so 3a + 2b stays as it is.",
        "اوپر کی قطار: 3 ٹائلیں a جمع 2 ٹائلیں a مل کر 5 ٹائلیں a، یعنی 3a + 2a = 5a۔ نیچے کی قطار: 3 ٹائلیں a اور 2 ٹائلیں b مختلف ہیں، اس لیے 3a + 2b ویسا ہی رہتا ہے۔"),
    "s4_add": two_groups((4, "x"), "+", (3, "x"), ("x",), "4x + 3x"),
    "s5_subtract": two_groups((9, "m"), "−", (4, "m"), ("m",), "9m - 4m"),
    "s7_with_number": one_row(S7, ("x",), "3x + 4 + 4x"),
    "s8_two_letters": one_row([(2, "a"), (3, "b"), (4, "a"), (1, "b")], ("a", "b"), "2a + 3b + 4a + b"),
    "s9_find_error": one_row([(3, "a"), (2, "b")], ("a", "b"), "3a + 2b"),
    "s12_summary": tiles([[("terms", S7)], [("terms", S7_DONE)]], ("x",),
        "Top row: algebra tiles for 3x + 4 + 4x. An arrow points down. Bottom row: the x-tiles put together make 7x, and the 4 small squares stay apart: 7x + 4.",
        "اوپر کی قطار: 3x + 4 + 4x کی الجبرا ٹائلیں۔ نیچے کی طرف تیر۔ نیچے کی قطار: x والی ٹائلیں اکٹھی ہو کر 7x، اور 4 چھوٹے مربعے الگ رہتے ہیں: 7x + 4۔",
        between="arrow"),
    "qb_apply": one_row([(5, "p"), (2, ""), (1, "p")], ("p",), "5p + 2 + p"),
    "qb_find_error": one_row([(6, "n"), (-1, "n")], ("n",), "6n - n"),
    "r_subtract": one_row([(8, "k"), (-3, "k")], ("k",), "8k - 3k"),
    "r_repeat": one_row([(1, "a"), (1, "a"), (1, "a")], ("a",), "a + a + a"),
})
write(lesson)
