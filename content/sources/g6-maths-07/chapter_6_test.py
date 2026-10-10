"""Chapter 6 test (Algebraic Expressions), set out like the book's review
exercise and a board paper: multiple choice, short questions, then longer
problems. The questions are new; only the kinds of question follow the book."""
from common import (T, say, nq, aq, ch, write, show, m, book_ref, REVIEW, CHAPTER_6_TEST,
                    collect, negate, value, ALG_VARIABLES, ALG_SUBSTITUTION, ALG_LIKE_TERMS,
                    ALG_SEQUENCES, ALG_TERMS, ALG_ADD_SUBTRACT)
import figs

SKILL = CHAPTER_6_TEST


def mcq(id, en, ur, right, wrongs, pos):
    return ch(id, ("MCQ: " + en, "کثیر انتخابی: " + ur), right, wrongs, pos, qtype="exam_style")


def short(id, en, ur, answer, hint, good, bad, wrongs=()):
    return nq(id, ("Short question: " + en, "مختصر سوال: " + ur), answer, hint, good, bad, wrongs, qtype="exam_style")


def long_q(id, en, ur, answer, hint, good, bad, wrongs=()):
    return nq(id, ("Long question: " + en, "تفصیلی سوال: " + ur), answer, hint, good, bad, wrongs, qtype="exam_style")


def short_expr(id, en, ur, terms, hint, good, bad, wrongs=()):
    return aq(id, ("Short question: " + en, "مختصر سوال: " + ur), terms, hint, good, bad, wrongs, qtype="exam_style")


def long_expr(id, en, ur, terms, hint, good, bad, wrongs=()):
    return aq(id, ("Long question: " + en, "تفصیلی سوال: " + ur), terms, hint, good, bad, wrongs, qtype="exam_style")


def plus(a, b):
    return list(collect(*a, *b))


def minus(a, b):
    return list(collect(*a, *negate(*b)))


def first_only(a, b):
    (c, v), *rest = b
    return list(collect(*a, (-c, v), *rest))


def fib(a, b, count):
    out = [a, b]
    while len(out) < count:
        out.append(out[-1] + out[-2])
    return out


def evaluate(terms, **values):
    return sum(c * (values[v] if v else 1) for c, v in terms)


# MCQs
M1 = [(1, "x"), (-5, "")]
assert show(M1) == "x − 5" and show([(5, ""), (-1, "x")]) == "5 − x"
M2 = [(3, "n"), (10, "")]
assert value("3n + 10", n=4) == 22 and value("13n", n=4) != 22 and value("n + 30", n=4) != 22
E3 = [(4, "a"), (-3, "b"), (2, "")]
M3 = len(E3)
assert M3 == 3 and show(E3) == "4a − 3b + 2"
E4 = [(2, ""), (-6, "x")]
M4 = next(c for c, v in E4 if v == "x")
assert M4 == -6 and show(E4) == "2 − 6x"
M6S = [2 + 3 * k for k in range(4)]
M6 = M6S[-1] + 3
assert M6S == [2, 5, 8, 11] and M6 == 14 and M6S[-1] + 2 == 13
A7, B7 = [(4, "x"), (3, "")], [(1, "x"), (2, "")]
M7 = plus(A7, B7)
assert M7 == [(5, "x"), (5, "")]
M8 = value("3a - 2", a=4)
assert M8 == 10 and int("34") - 2 == 32 and 3 + 4 - 2 == 5
# short questions
A1 = [(7, "a"), (2, "b"), (-3, "a"), (1, "b")]
E_S1 = list(collect(*A1))
assert E_S1 == [(4, "a"), (3, "b")] and sum(c for c, _ in A1) == 7
A2, B2 = [(9, "m"), (8, "")], [(2, "m"), (3, "")]
S2 = minus(A2, B2)
assert S2 == [(7, "m"), (5, "")] and first_only(A2, B2) == [(7, "m"), (11, "")]
A3, B3 = [(8, "x")], [(3, "x"), (-5, "")]
S3 = minus(A3, B3)
assert S3 == [(5, "x"), (5, "")] and first_only(A3, B3) == [(5, "x"), (-5, "")]
S4S = [14 - 5 * k for k in range(4)]
S4 = S4S[-1] - 5
assert S4S == [14, 9, 4, -1] and S4 == -6 and S4S[-1] + 5 == 4
S5E = [(6, "p"), (-1, "q"), (5, "")]
S5 = evaluate(S5E, p=3, q=7)
assert S5 == 16 and 6 * 3 + 7 + 5 == 30
# long questions
L1S = fib(4, 7, 7)
L1 = L1S[-1]
assert L1S == [4, 7, 11, 18, 29, 47, 76] and L1 == 76 and L1S[5] == 47
SIDES2 = [[(3, "x"), (2, "")], [(1, "x"), (5, "")], [(2, "x"), (1, "")]]
P2 = list(collect(*[t for s in SIDES2 for t in s]))
assert P2 == [(6, "x"), (8, "")]
L2 = evaluate(P2, x=4)
assert L2 == 32 and sum(evaluate(s, x=4) for s in SIDES2) == 32 and int("64") + 8 == 72
A3L, B3L, C3L = [(5, "a"), (2, "b")], [(2, "a"), (-3, "b")], [(1, "a"), (-1, "b")]
L3 = list(collect(*A3L, *negate(*B3L), *C3L))
assert L3 == [(4, "a"), (4, "b")]
L3_WRONG = list(collect(*A3L, (-2, "a"), (-3, "b"), *C3L))
assert L3_WRONG == [(4, "a"), (-2, "b")]
for a_ in range(1, 5):
    for b_ in range(1, 5):
        assert evaluate(L3, a=a_, b=b_) == evaluate(A3L, a=a_, b=b_) - evaluate(B3L, a=a_, b=b_) + evaluate(C3L, a=a_, b=b_)
LEN4, BR4 = [(4, "n"), (1, "")], [(1, "n"), (3, "")]
P4 = list(collect(*LEN4, *BR4, *LEN4, *BR4))
assert P4 == [(10, "n"), (8, "")]
L4 = evaluate(P4, n=5)
assert L4 == 58 and L4 // 2 == 29 and int("105") + 8 == 113
assert L4 == 2 * (evaluate(LEN4, n=5) + evaluate(BR4, n=5))
# question bank
QB1 = [(1, "x"), (-9, "")]
assert show(QB1) == "x − 9" and value("x - 9", x=20) == 11
QB2 = value("4n + 1", n=6)
assert QB2 == 25 and 4 * 6 + 1 == 25 and int("46") + 1 == 47
QB3 = list(collect((6, "c"), (4, "c"), (-2, "")))
assert QB3 == [(10, "c"), (-2, "")]
# review
R1 = evaluate([(5, "k"), (2, "")], k=3)
assert R1 == 17 and int("53") + 2 == 55
R2S = [100 - 15 * k for k in range(4)]
R2 = R2S[-1] - 15
assert R2S == [100, 85, 70, 55] and R2 == 40

lesson = {
 "id": "g6-maths-07-chapter-6-test",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Answer exam-style questions on the whole of chapter 6: number patterns, letters for numbers, terms, coefficients and constants, like terms, adding and subtracting expressions, brackets, and finding the value of an expression.",
                      "textbook": book_ref("Review Exercise 6")}],
 "skills": [SKILL],
 "title": T("Chapter 6 test: Algebraic expressions", "باب 6 کا ٹیسٹ: الجبری عبارتیں"),
 "estimated_minutes": 25,
 "prerequisites": [{"skill": s} for s in (ALG_SEQUENCES, ALG_VARIABLES, ALG_TERMS, ALG_LIKE_TERMS, ALG_ADD_SUBTRACT, ALG_SUBSTITUTION)],
 "misconceptions": [
   {"id": "always_add", "description": "Assumes every pattern adds the same number, or adds a gap to a sequence that adds the last two terms."},
   {"id": "times_for_plus", "description": "Writes 'more than' or a price plus a cost as multiplication."},
   {"id": "less_than_reversed", "description": "Writes 5 less than x as 5 − x instead of x − 5."},
   {"id": "counts_letters_only", "description": "Leaves out the constant when counting the terms."},
   {"id": "drops_sign", "description": "Leaves out the minus sign that belongs to a term."},
   {"id": "unlike_joined", "description": "Joins terms with different letters, or a letter term and a number, into one term."},
   {"id": "first_term_only", "description": "Changes only the first sign when subtracting an expression or removing a bracket after a minus."},
   {"id": "joins_digits", "description": "Reads 3a with a = 4 as 34 instead of 3 × 4."},
   {"id": "perimeter_missing_sides", "description": "Adds only some of the sides when finding a perimeter."},
   {"id": "stops_early", "description": "Finds a middle result (a term, an expression) but does not answer the question asked."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["exam_style"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_exam_write", "type": "exam_style", "step": aq(
     "qb_exam_write", ("Write 9 less than a number x as an expression.", "عدد x سے 9 کم کو عبارت کی صورت میں لکھیں۔"), QB1,
     ("Start from x and take away 9.", "x سے شروع کریں اور 9 تفریق کریں۔"),
     ("Correct: x − 9.", "درست: x − 9"),
     ("9 less than x is x − 9.", "x سے 9 کم یعنی x − 9"),
     [([(9, ""), (-1, "x")], "9 − x starts from 9. Start from x: x − 9.", "9 − x، 9 سے شروع ہوتا ہے۔ x سے شروع کریں: x − 9", "less_than_reversed")], qtype=None)},
   {"id": "qb_exam_value", "type": "exam_style", "step": nq(
     "qb_exam_value", ("The nth term of a pattern is 4n + 1. What is the 6th term?", "ایک نمونے کے n ویں رکن کا اصول 4n + 1 ہے۔ چھٹا رکن کیا ہے؟"), QB2,
     ("Put n = 6. 4n means 4 × n.", "n = 6 رکھیں۔ 4n یعنی 4 × n"),
     ("Correct: 4 × 6 + 1 = 25.", "درست: 4 × 6 + 1 = 25"),
     ("4 × 6 = 24, and 24 + 1 = 25.", "4 × 6 = 24، اور 24 + 1 = 25"),
     [(47, "4n with n = 6 is 4 × 6 = 24, not 46. Then 25.", "n = 6 کے ساتھ 4n یعنی 4 × 6 = 24، 46 نہیں۔ پھر 25", "joins_digits")], qtype=None)},
   {"id": "qb_exam_group", "type": "exam_style", "step": aq(
     "qb_exam_group", (f"Simplify: {show([(6, 'c'), (4, 'c'), (-2, '')])}", f"مختصر کریں: {show([(6, 'c'), (4, 'c'), (-2, '')])}"), QB3,
     ("Add the c-terms. The −2 has no letter.", "c والے ارکان جمع کریں۔ −2 میں حرف نہیں۔"),
     ("Correct: 10c − 2.", "درست: 10c − 2"),
     ("6c + 4c = 10c, and the −2 stays: 10c − 2.", "6c + 4c = 10c، اور −2 رہتا ہے: 10c − 2"),
     [([(8, "c")], "10c and −2 are unlike terms, so they cannot join: 10c − 2.", "10c اور −2 غیر یکساں ارکان ہیں، اس لیے نہیں مل سکتے: 10c − 2", "unlike_joined")], qtype=None)},
 ]},
 "home_tasks": [{"id": "h_paper", "text": T(
   "Do Review Exercise 6 in your maths book in your notebook, setting out the working the way this test's answers do. Ask your teacher to check it.",
   "اپنی ریاضی کی کتاب کی اعادی مشق 6 اپنی کاپی میں حل کریں، اور کام اس ٹیسٹ کے جوابات کی طرح لکھیں۔ اپنے استاد سے جانچ کروائیں۔")}],
 "glossary": [T("Multiple choice", "کثیر انتخابی"), T("Short question", "مختصر سوال"), T("Long question", "تفصیلی سوال"),
              T("Model answer", "نمونہ جواب"), T("Review exercise", "اعادی مشق")],
 "steps": [
   {"id": "s1_paper", "type": "explain",
    "character": say("encouraging", "This is a test of the whole chapter, like the book's review exercise. Read each question carefully!",
                     "یہ پورے باب کا ٹیسٹ ہے، کتاب کی اعادی مشق کی طرح۔ ہر سوال غور سے پڑھیں!"),
    "text": T("This test goes with Review Exercise 6 of your maths book (PCTB Mathematics 6). It has three parts, like an exam paper: multiple choice questions (choose one answer), short questions (a few lines of working), and longer problems (full working in your notebook). The questions are new, not the book's.",
              "یہ ٹیسٹ آپ کی ریاضی کی کتاب (پنجاب ٹیکسٹ بک بورڈ، ریاضی 6) کی اعادی مشق 6 کے ساتھ ہے۔ اس کے تین حصے ہیں، امتحانی پرچے کی طرح: کثیر انتخابی سوال (ایک جواب چنیں)، مختصر سوال (چند سطروں کا کام)، اور تفصیلی سوال (پورا کام اپنی کاپی میں)۔ سوال نئے ہیں، کتاب والے نہیں۔")},
   mcq("m1_write", "Which expression means \"5 less than a number x\"?", "کون سی عبارت \"عدد x سے 5 کم\" کو ظاہر کرتی ہے؟",
       ("x − 5", "x − 5", "Correct: start from x and take away 5.", "درست: x سے شروع کریں اور 5 تفریق کریں۔"),
       [("5 − x", "5 − x", "That starts from 5. We start from x: x − 5.", "یہ 5 سے شروع ہوتا ہے۔ ہم x سے شروع کرتے ہیں: x − 5", "less_than_reversed"),
        ("5x", "5x", "5x means 5 times x.", "5x یعنی x کا 5 گنا۔", "times_for_plus"),
        ("x + 5", "x + 5", "That is 5 MORE than x.", "یہ x سے 5 زیادہ ہے۔", "less_than_reversed")], 1),
   mcq("m2_price", "A pen costs Rs 10 and a notebook costs Rs n. The cost of 3 notebooks and a pen is:", "ایک قلم 10 روپے کا اور ایک کاپی n روپے کی ہے۔ 3 کاپیوں اور ایک قلم کی قیمت ہے:",
       ("3n + 10", "3n + 10", "Correct: 3 notebooks cost 3n, and the pen costs 10.", "درست: 3 کاپیوں کی قیمت 3n اور قلم کی 10 ہے۔"),
       [("13n", "13n", "3n and 10 are unlike terms. They cannot join.", "3n اور 10 غیر یکساں ارکان ہیں۔ یہ نہیں مل سکتے۔", "unlike_joined"),
        ("n + 30", "n + 30", "The 3 multiplies n; it does not multiply the pen.", "3، n کو ضرب دیتا ہے؛ قلم کو نہیں۔", "times_for_plus"),
        ("3 + n + 10", "3 + n + 10", "3 notebooks cost 3 × n, not 3 + n.", "3 کاپیوں کی قیمت 3 × n ہے، 3 + n نہیں۔", "times_for_plus")], 0),
   mcq("m3_terms", f"The number of terms in {show(E3)} is:", f"{show(E3)} میں ارکان کی تعداد ہے:",
       ("3", "3", "Correct: 4a, −3b and 2.", "درست: 4a، −3b اور 2"),
       [("2", "2", "The constant 2 is a term too.", "مستقل 2 بھی ایک رکن ہے۔", "counts_letters_only"),
        ("5", "5", "4a is one term, not two. Count the groups between the signs.", "4a ایک رکن ہے، دو نہیں۔ علامتوں کے درمیان کے گروہ گنیں۔"),
        ("4", "4", "Do not count the letters and numbers separately. The terms are 4a, −3b and 2.", "حروف اور اعداد الگ الگ نہ گنیں۔ ارکان 4a، −3b اور 2 ہیں۔", "counts_letters_only")], 2),
   mcq("m4_coefficient", f"The coefficient of x in {show(E4)} is:", f"{show(E4)} میں x کا عددی سر ہے:",
       ("−6", "−6", "Correct: the term is −6x.", "درست: رکن −6x ہے۔"),
       [("6", "6", "Keep the minus sign: −6.", "منفی کی علامت رکھیں: −6", "drops_sign"),
        ("2", "2", "2 is the constant, with no letter.", "2 مستقل ہے، بغیر حرف کے۔"),
        ("−4", "−4", "That is 2 − 6. The coefficient is the number with x: −6.", "یہ 2 − 6 ہے۔ عددی سر وہ عدد ہے جو x کے ساتھ ہے: −6")], 0),
   mcq("m5_like", "Which pair are like terms?", "کون سا جوڑا یکساں ارکان کا ہے؟",
       ("7y and −y", "7y اور −y", "Correct: both have the letter y.", "درست: دونوں میں حرف y ہے۔"),
       [("4a and 4b", "4a اور 4b", "The letters differ, so they are unlike terms.", "حروف مختلف ہیں، اس لیے یہ غیر یکساں ارکان ہیں۔", "unlike_joined"),
        ("3x and 3", "3x اور 3", "3 has no letter, so it is unlike 3x.", "3 میں حرف نہیں، اس لیے یہ 3x کے غیر یکساں ہے۔", "unlike_joined"),
        ("2m and 2n", "2m اور 2n", "m and n differ: unlike terms.", "m اور n مختلف ہیں: غیر یکساں ارکان۔", "unlike_joined")], 3),
   mcq("m6_pattern", f"The next term of the pattern {', '.join(map(str, M6S))}, … is:", f"نمونے {', '.join(map(str, M6S))}، … کا اگلا رکن ہے:",
       (str(M6), str(M6), "Correct: the rule is add 3, so 11 + 3 = 14.", "درست: اصول 3 جمع کرنا ہے، تو 11 + 3 = 14"),
       [(str(M6S[-1] + 2), str(M6S[-1] + 2), "The gap is 3, not 2: 14.", "فرق 3 ہے، 2 نہیں: 14", "always_add"),
        (str(M6S[-1] * 2), str(M6S[-1] * 2), "The pattern adds 3; it does not double.", "نمونہ 3 جمع کرتا ہے؛ دگنا نہیں کرتا۔", "always_add"),
        (str(M6S[-1] + 4), str(M6S[-1] + 4), "The gap is 3, not 4: 14.", "فرق 3 ہے، 4 نہیں: 14", "always_add")], 2),
   mcq("m7_add", f"({show(A7)}) + ({show(B7)}) =", f"({show(A7)}) + ({show(B7)}) =",
       (show(M7), show(M7), "Correct: 4x + x = 5x and 3 + 2 = 5.", "درست: 4x + x = 5x اور 3 + 2 = 5"),
       [("5x + 6", "5x + 6", "3 + 2 is 5, not 6.", "3 + 2 برابر 5 ہے، 6 نہیں۔"),
        ("10x", "10x", "Letters and numbers cannot all join into 10x.", "حروف اور اعداد سب مل کر 10x نہیں بن سکتے۔", "unlike_joined"),
        ("4x + 5", "4x + 5", "x means 1x: 4x + 1x = 5x.", "x یعنی 1x: 4x + 1x = 5x", "unlike_joined")], 1),
   mcq("m8_value", "The value of 3a − 2 when a = 4 is:", "جب a = 4 ہو تو 3a − 2 کی قیمت ہے:",
       (str(M8), str(M8), "Correct: 3 × 4 − 2 = 10.", "درست: 3 × 4 − 2 = 10"),
       [("32", "32", "3a is 3 × 4 = 12, not 34.", "3a یعنی 3 × 4 = 12، 34 نہیں۔", "joins_digits"),
        ("5", "5", "3a is 3 times a, not 3 + a.", "3a یعنی a کا 3 گنا، 3 + a نہیں۔", "times_for_plus"),
        ("14", "14", "The − 2 is taken away: 12 − 2 = 10.", "− 2 تفریق ہوتا ہے: 12 − 2 = 10", "drops_sign")], 0),
   {"id": "s_short", "type": "explain",
    "text": T("Short questions. Work each one out in your notebook, then type the answer.",
              "مختصر سوال۔ ہر ایک اپنی کاپی میں حل کریں، پھر جواب لکھیں۔")},
   short_expr("q1_simplify", f"Simplify: {show(A1)}", f"مختصر کریں: {show(A1)}", E_S1,
      ("Group the a-terms and the b-terms separately. b means 1b.", "a والے اور b والے ارکان الگ الگ اکٹھے کریں۔ b یعنی 1b"),
      ("Correct: 4a + 3b.", "درست: 4a + 3b"),
      ("Model answer: 7a − 3a = 4a and 2b + b = 3b. So 4a + 3b.", "نمونہ جواب: 7a − 3a = 4a اور 2b + b = 3b۔ تو 4a + 3b"),
      [([(7, "a")], "a-terms and b-terms are unlike. Do not add them all: 4a + 3b.", "a والے اور b والے ارکان غیر یکساں ہیں۔ سب جمع نہ کریں: 4a + 3b", "unlike_joined"),
       ([(10, "a"), (3, "b")], "The −3a is taken away: 7a − 3a = 4a.", "−3a تفریق ہوتا ہے: 7a − 3a = 4a", "drops_sign")]),
   short_expr("q2_subtract", f"Subtract {show(B2)} from {show(A2)}.", f"{show(A2)} میں سے {show(B2)} تفریق کریں۔", S2,
      ("Write (9m + 8) − (2m + 3) and change both signs in the second bracket.", "(9m + 8) − (2m + 3) لکھیں اور دوسری بریکٹ کی دونوں علامتیں بدلیں۔"),
      ("Correct: 7m + 5.", "درست: 7m + 5"),
      ("Model answer: 9m + 8 − 2m − 3 = 7m + 5.", "نمونہ جواب: 9m + 8 − 2m − 3 = 7m + 5"),
      [(first_only(A2, B2), "The 3 is taken away too: 8 − 3 = 5, so 7m + 5.", "3 بھی تفریق ہوتا ہے: 8 − 3 = 5، تو 7m + 5", "first_term_only")]),
   short_expr("q3_brackets", f"Remove the brackets and simplify: {show(A3)} − ({show(B3)})", f"بریکٹ ہٹا کر مختصر کریں: {show(A3)} − ({show(B3)})", S3,
      ("A minus in front changes both signs inside: 3x becomes −3x and −5 becomes +5.", "آگے منفی ہو تو اندر کی دونوں علامتیں بدلتی ہیں: 3x بنتا ہے −3x اور −5 بنتا ہے +5"),
      ("Correct: 5x + 5.", "درست: 5x + 5"),
      ("Model answer: 8x − 3x + 5 = 5x + 5.", "نمونہ جواب: 8x − 3x + 5 = 5x + 5"),
      [(first_only(A3, B3), "Taking away −5 gives +5: 5x + 5.", "−5 کو تفریق کرنے سے +5 ملتا ہے: 5x + 5", "first_term_only")]),
   short("q4_negative", f"What is the next term of {', '.join(m(x) for x in S4S)}, … ?", f"{', '.join(m(x) for x in S4S)}، … کا اگلا رکن کیا ہے؟", S4,
      ("The terms go down by 5, even below zero.", "ارکان 5، 5 کم ہوتے ہیں، صفر سے نیچے بھی۔"),
      ("Correct: −1 − 5 = −6.", "درست: −1 − 5 = −6"),
      ("Model answer: the rule is subtract 5: 14, 9, 4, −1, −6.", "نمونہ جواب: اصول 5 تفریق کرنا ہے: 14، 9، 4، −1، −6"),
      [(4, "That adds 5. The pattern goes down: −6.", "یہ 5 جمع کرتا ہے۔ نمونہ نیچے جاتا ہے: −6", "always_add")]),
   short("q5_value", f"Find the value of {show(S5E)} when p = 3 and q = 7.", f"جب p = 3 اور q = 7 ہو تو {show(S5E)} کی قیمت معلوم کریں۔", S5,
      ("6p = 18. The minus sign in front of q stays.", "6p = 18۔ q کے آگے منفی کی علامت رہتی ہے۔"),
      ("Correct: 18 − 7 + 5 = 16.", "درست: 18 − 7 + 5 = 16"),
      ("Model answer: 6 × 3 = 18, then 18 − 7 = 11, then 11 + 5 = 16.", "نمونہ جواب: 6 × 3 = 18، پھر 18 − 7 = 11، پھر 11 + 5 = 16"),
      [(30, "q is taken away, not added: 18 − 7 + 5 = 16.", "q تفریق ہوتا ہے، جمع نہیں: 18 − 7 + 5 = 16", "drops_sign")]),
   {"id": "s_long", "type": "explain",
    "text": T("Longer problems. Write full working in your notebook, then type the final answer.",
              "تفصیلی سوالات۔ اپنی کاپی میں پورا کام لکھیں، پھر آخری جواب لکھیں۔")},
   long_q("l1_fib", "The first two terms of a pattern are 4 and 7. Each next term is the sum of the two terms before it. What is the 7th term?", "ایک نمونے کے پہلے دو ارکان 4 اور 7 ہیں۔ ہر اگلا رکن اپنے سے پہلے دو ارکان کا مجموعہ ہے۔ ساتواں رکن کیا ہے؟", L1,
      ("Write the terms one by one: 4, 7, 11, ...", "ارکان ایک ایک کر کے لکھیں: 4، 7، 11، ..."),
      ("Correct: 4, 7, 11, 18, 29, 47, 76.", "درست: 4، 7، 11، 18، 29، 47، 76"),
      ("Model answer: 4 + 7 = 11, 7 + 11 = 18, 11 + 18 = 29, 18 + 29 = 47, 29 + 47 = 76. The 7th term is 76.", "نمونہ جواب: 4 + 7 = 11، 7 + 11 = 18، 11 + 18 = 29، 18 + 29 = 47، 29 + 47 = 76۔ ساتواں رکن 76 ہے۔"),
      [(47, "That is the 6th term. One more step: 29 + 47 = 76.", "یہ چھٹا رکن ہے۔ ایک قدم اور: 29 + 47 = 76", "stops_early"),
       (22, "That adds a gap of 3 each time. This pattern adds the last two terms: 76.", "یہ ہر بار 3 جمع کرتا ہے۔ یہ نمونہ آخری دو ارکان جمع کرتا ہے: 76", "always_add")]),
   long_q("l2_perimeter", f"The sides of a triangle are {show(SIDES2[0])} cm, {show(SIDES2[1])} cm and {show(SIDES2[2])} cm. Write its perimeter as an expression, then find the perimeter in cm when x = 4.", f"ایک تکون کے اضلاع {show(SIDES2[0])} سینٹی میٹر، {show(SIDES2[1])} سینٹی میٹر اور {show(SIDES2[2])} سینٹی میٹر ہیں۔ اس کا احاطہ عبارت میں لکھیں، پھر x = 4 ہو تو احاطہ سینٹی میٹر میں معلوم کریں۔", L2,
      ("Add the three sides: 3x + x + 2x and 2 + 5 + 1. Then put x = 4.", "تینوں اضلاع جمع کریں: 3x + x + 2x اور 2 + 5 + 1۔ پھر x = 4 رکھیں۔"),
      ("Correct: 6x + 8, and 6 × 4 + 8 = 32 cm.", "درست: 6x + 8، اور 6 × 4 + 8 = 32 سینٹی میٹر"),
      ("Model answer: perimeter = 6x + 8. With x = 4: 6 × 4 = 24, and 24 + 8 = 32 cm.", "نمونہ جواب: احاطہ = 6x + 8۔ x = 4 کے ساتھ: 6 × 4 = 24، اور 24 + 8 = 32 سینٹی میٹر"),
      [(72, "6x is 6 × 4 = 24, not 64. Then 24 + 8 = 32.", "6x یعنی 6 × 4 = 24، 64 نہیں۔ پھر 24 + 8 = 32", "joins_digits"),
       (6, "6 is only the coefficient of x. Put x = 4 in: 32.", "6 صرف x کا عددی سر ہے۔ x = 4 رکھیں: 32", "stops_early")]),
   long_expr("l3_mixed", f"Simplify: ({show(A3L)}) − ({show(B3L)}) + ({show(C3L)})", f"مختصر کریں: ({show(A3L)}) − ({show(B3L)}) + ({show(C3L)})", L3,
      ("Change both signs in the middle bracket; the last bracket opens as it is. Then group a-terms and b-terms.", "درمیان کی بریکٹ کی دونوں علامتیں بدلیں؛ آخری بریکٹ جیسی ہے ویسی کھلتی ہے۔ پھر a اور b والے ارکان اکٹھے کریں۔"),
      ("Correct: 4a + 4b.", "درست: 4a + 4b"),
      ("Model answer: 5a + 2b − 2a + 3b + a − b. The a-terms: 5 − 2 + 1 = 4. The b-terms: 2 + 3 − 1 = 4. So 4a + 4b.", "نمونہ جواب: 5a + 2b − 2a + 3b + a − b۔ a والے: 5 − 2 + 1 = 4۔ b والے: 2 + 3 − 1 = 4۔ تو 4a + 4b"),
      [(L3_WRONG, "The −3b in the middle bracket becomes +3b: 2b + 3b − b = 4b.", "درمیان کی بریکٹ کا −3b بن جاتا ہے +3b: 2b + 3b − b = 4b", "first_term_only")]),
   long_q("l4_rectangle", f"A rectangle has length {show(LEN4)} cm and breadth {show(BR4)} cm. Write its perimeter as an expression in n, then find the perimeter in cm when n = 5.", f"ایک مستطیل کی لمبائی {show(LEN4)} سینٹی میٹر اور چوڑائی {show(BR4)} سینٹی میٹر ہے۔ اس کا احاطہ n میں عبارت کی صورت میں لکھیں، پھر n = 5 ہو تو احاطہ سینٹی میٹر میں معلوم کریں۔", L4,
      ("Add two lengths and two breadths: 10n + 8. Then put n = 5.", "دو لمبائیاں اور دو چوڑائیاں جمع کریں: 10n + 8۔ پھر n = 5 رکھیں۔"),
      ("Correct: 10n + 8, and 10 × 5 + 8 = 58 cm.", "درست: 10n + 8، اور 10 × 5 + 8 = 58 سینٹی میٹر"),
      ("Model answer: perimeter = (4n + 1) + (n + 3) + (4n + 1) + (n + 3) = 10n + 8. With n = 5: 50 + 8 = 58 cm.", "نمونہ جواب: احاطہ = (4n + 1) + (n + 3) + (4n + 1) + (n + 3) = 10n + 8۔ n = 5 کے ساتھ: 50 + 8 = 58 سینٹی میٹر"),
      [(29, "That is only length + breadth. The perimeter has all four sides: 58.", "یہ صرف لمبائی + چوڑائی ہے۔ احاطے میں چاروں اضلاع ہوتے ہیں: 58", "perimeter_missing_sides"),
       (113, "10n is 10 × 5 = 50, not 105. Then 50 + 8 = 58.", "10n یعنی 10 × 5 = 50، 105 نہیں۔ پھر 50 + 8 = 58", "joins_digits")]),
   {"id": "s_end_summary", "type": "summary",
    "character": say("celebrating", "You finished the chapter 6 test. Well done!", "آپ نے باب 6 کا ٹیسٹ مکمل کر لیا۔ شاباش!"),
    "text": T("In the exam: find the rule of a pattern by checking every pair of neighbours. Write words as expressions (5 less than x is x − 5). Terms are separated by + and −; the coefficient is the number with the letter; the constant has no letter. Only like terms can be added together. To subtract, change every sign in the second expression, and the same for a bracket after a minus. A perimeter is all the sides added. To find a value, put the numbers in for the letters and multiply first.",
              "امتحان میں: نمونے کا اصول ہر برابر کے جوڑے کو جانچ کر معلوم کریں۔ الفاظ کو عبارت میں لکھیں (x سے 5 کم یعنی x − 5)۔ ارکان + اور − سے الگ ہوتے ہیں؛ عددی سر حرف کے ساتھ والا عدد ہے؛ مستقل میں حرف نہیں ہوتا۔ صرف یکساں ارکان آپس میں جمع ہو سکتے ہیں۔ تفریق کے لیے دوسری عبارت کی ہر علامت بدلیں، اور منفی کے بعد والی بریکٹ کے لیے بھی یہی۔ احاطہ تمام اضلاع کا مجموعہ ہے۔ قیمت معلوم کرنے کے لیے حروف کی جگہ اعداد رکھیں اور پہلے ضرب دیں۔"),
    "points": [T("Check an answer by putting in a small number.", "جواب کو چھوٹا عدد رکھ کر جانچیں۔"),
               T("Write the working, then the final answer with its unit.", "کام لکھیں، پھر آخری جواب اکائی کے ساتھ۔")]},
 ],
 "review_questions": [
   {"id": "r_exam_value", "type": "exam_style", "skill": SKILL, "step": nq(
     "r_exam_value", ("Find the value of 5k + 2 when k = 3.", "جب k = 3 ہو تو 5k + 2 کی قیمت معلوم کریں۔"), R1,
     ("5k means 5 × k.", "5k یعنی 5 × k"),
     ("Correct: 5 × 3 + 2 = 17.", "درست: 5 × 3 + 2 = 17"), ("15 + 2 = 17.", "15 + 2 = 17"),
     [(55, "5k is 5 × 3 = 15, not 53. Then 15 + 2 = 17.", "5k یعنی 5 × 3 = 15، 53 نہیں۔ پھر 15 + 2 = 17", "joins_digits")], qtype=None)},
   {"id": "r_exam_pattern", "type": "exam_style", "skill": SKILL, "step": nq(
     "r_exam_pattern", (f"What is the next term of {', '.join(map(str, R2S))}, … ?", f"{', '.join(map(str, R2S))}، … کا اگلا رکن کیا ہے؟"), R2,
     ("The terms go down by 15.", "ارکان 15، 15 کم ہوتے ہیں۔"),
     ("Correct: 55 − 15 = 40.", "درست: 55 − 15 = 40"), ("The rule is subtract 15: 55 − 15 = 40.", "اصول 15 تفریق کرنا ہے: 55 − 15 = 40"),
     [(70, "The pattern goes down, not up: 40.", "نمونہ نیچے جاتا ہے، اوپر نہیں: 40", "always_add")], qtype=None)},
 ],
 "teacher_notes": [
   "A chapter test to use with Review Exercise 6 of the PCTB Mathematics 6 book, in the style of a paper: multiple choice, short questions, then longer problems. Only the kinds of question come from the book; every question, number and story here is new, because the book may not be copied.",
   "It has its own skill (maths.algebra.chapter_6_test), with the chapter's algebra skills as prerequisites, and is mastered with exam_style questions, like the chapter 5 test.",
   "Urdu terms to check: کثیر انتخابی (multiple choice), مختصر سوال / تفصیلی سوال (short / long question), نمونہ جواب (model answer), اعادی مشق (review exercise), عبارت (expression), رکن (term), عددی سر (coefficient), مستقل (constant), یکساں ارکان (like terms), احاطہ (perimeter). No new Urdu term was invented here.",
   "The numbers were worked out in content/sources/g6-maths-07/chapter_6_test.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}

figs.attach(lesson, {
    "l2_perimeter": figs.triangle_sides([show(SIDES2[0]), show(SIDES2[2]), show(SIDES2[1])], "A triangle with sides 3x + 2 on the left, 2x + 1 on the right and x + 5 along the bottom.", "ایک تکون جس کا بایاں ضلع 3x + 2، دایاں ضلع 2x + 1 اور نچلا ضلع x + 5 ہے۔"),
})
write(lesson)
