"""Chapter 3 test (Laws of Integers), set out like the book's review exercise
and a board paper: multiple choice, short questions, then longer mixed
problems. The questions are new; only the kinds of question follow the book."""
from fractions import Fraction as F
from common import (T, say, wrong, nq, ch, write, book_ref, REVIEW, CHAPTER_3_TEST, INT_ADD, INT_SUBTRACT,
                    INT_MULTIPLY, INT_LAWS, SM_ORDER, SM_BRACKETS, SM_FRACTIONS_DECIMALS)

SKILL = CHAPTER_3_TEST


def mcq(id, en, ur, right, wrongs, pos):
    return ch(id, ("MCQ: " + en, "کثیر انتخابی: " + ur), right, wrongs, pos, qtype="exam_style")


def short(id, en, ur, answer, hint, good, bad, wrongs=()):
    return nq(id, ("Short question: " + en, "مختصر سوال: " + ur), answer, hint, good, bad, wrongs, qtype="exam_style")


def long_q(id, en, ur, answer, hint, good, bad, wrongs=()):
    return nq(id, ("Long question: " + en, "تفصیلی سوال: " + ur), answer, hint, good, bad, wrongs, qtype="exam_style")


# MCQs
M1 = -9 + -6
assert M1 == -15 and 9 + 6 == 15 and -9 - 6 == -15 and -9 + 6 == -3
M2 = 7 - -5
assert M2 == 12 and 7 - 5 == 2 and -7 - 5 == -12
M3 = -8 * -7
assert M3 == 56
M4 = -54 // 9
assert -54 % 9 == 0 and M4 == -6
assert 5 + -3 == -3 + 5            # commutative law of addition
assert (5 + -3) + 2 == 5 + (-3 + 2)  # associative law (different statement)
assert 5 * 0 == 0                   # not a law
M7 = 9 - 2 * 3 + 4
assert M7 == 7 and (9 - 2) * 3 + 4 == 25 and 9 - 2 * (3 + 4) == -5 and (9 - 2) * (3 + 4) == 49
assert -3 * (4 + 5) == -3 * 4 + -3 * 5 == -27
# short questions
S1 = -23 + 9
assert S1 == -14 and 23 + 9 == 32 and 23 - 9 == 14
S2 = -18 - -6
assert S2 == -12 and -18 - 6 == -24 and -18 + 6 == -12
S3 = -13 * -4
assert S3 == 52
S4 = -63 // -7
assert -63 % 7 == 0 and S4 == 9 and -7 * S4 == -63 and -7 * -9 == 63
S5 = 40 - 4 * (6 - 1)
assert S5 == 20 and (40 - 4) * (6 - 1) == 180 and 40 - 4 * 6 - 1 == 15
# long questions
L1 = 3 + 5 * -4 + 7
assert L1 == -10 and 5 * -4 == -20 and 3 + 20 + 7 == 30 and 3 + -20 == -17
L2_L = (-2 * 7) * -5
L2_R = -2 * (7 * -5)
assert L2_L == L2_R == 70 and -70 != 70
L3 = F(11, 2) + 2 * (F(9, 2) - (F(6, 5) + F(4, 5)))
assert L3 == F(21, 2) and float(L3) == 10.5 and (F(11, 2) + 2) * (F(9, 2) - 2) == F(75, 4)
L4 = (8 * 18 + 4 * 5) - 12 * 15
assert L4 == -16 and 8 * 18 + 4 * 5 == 164 and 12 * 15 == 180 and 164 != 180
# question bank
QB1 = -17 + -26
assert QB1 == -43
QB2 = -144 // 12
assert 144 % 12 == 0 and QB2 == -12
QB3 = 36 // (2 + 4) + 5 * 2
assert 36 % 6 == 0 and QB3 == 16 and 36 // 2 + 4 + 5 * 2 == 32
# review
R1 = 14 - 30
assert R1 == -16 and 30 - 14 == 16
R2 = 4 * (6 + -9)
assert R2 == -12 and 4 * 6 + -9 == 15

lesson = {
 "id": "g6-maths-04-chapter-3-test",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Answer exam-style questions on the whole of chapter 3: adding, subtracting, multiplying and dividing integers, the commutative, associative and distributive laws, and the BODMAS rule.",
                      "textbook": book_ref("Review Exercise 3")}],
 "skills": [SKILL],
 "title": T("Chapter 3 test: Laws of Integers", "باب 3 کا ٹیسٹ: صحیح اعداد کے قوانین"),
 "estimated_minutes": 25,
 "prerequisites": [{"skill": s} for s in (INT_ADD, INT_SUBTRACT, INT_MULTIPLY, INT_LAWS, SM_ORDER, SM_BRACKETS, SM_FRACTIONS_DECIMALS)],
 "misconceptions": [
   {"id": "sign_lost", "description": "Drops the minus sign from an answer, or adds the digits and forgets the sign."},
   {"id": "double_neg", "description": "Treats subtracting a negative number as subtracting a positive one."},
   {"id": "neg_neg", "description": "Thinks a negative times a negative is negative."},
   {"id": "pos_only", "description": "Gives a positive product or quotient for unlike signs."},
   {"id": "law_mixed", "description": "Mixes up the commutative, associative and distributive laws."},
   {"id": "zero_division", "description": "Thinks a number divided by zero is 0."},
   {"id": "left_to_right", "description": "Works strictly left to right and ignores BODMAS."},
   {"id": "skips_brackets", "description": "Ignores the brackets, or multiplies only the first term inside them."},
   {"id": "stops_early", "description": "Finds a middle result but does not answer the question asked."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["exam_style"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_exam_add", "type": "exam_style", "step": nq(
     "qb_exam_add", ("Find (−17) + (−26).", "(−17) + (−26) معلوم کریں۔"), QB1,
     ("Same signs: add the digits and keep the minus sign.", "ایک جیسی علامتیں: ہندسے جمع کریں اور منفی علامت رکھیں۔"),
     ("Correct: 17 + 26 = 43, so −43.", "درست: 17 + 26 = 43، اس لیے −43"),
     ("Both are negative, so the sum is negative: −43.", "دونوں منفی ہیں، اس لیے مجموعہ منفی ہے: −43"),
     [(43, "Like negative numbers add up to a negative number: −43.", "منفی اعداد کا مجموعہ منفی ہوتا ہے: −43", "sign_lost")], qtype=None)},
   {"id": "qb_exam_div", "type": "exam_style", "step": nq(
     "qb_exam_div", ("Find (−144) ÷ 12.", "(−144) ÷ 12 معلوم کریں۔"), QB2,
     ("144 ÷ 12 = 12. Are the signs the same?", "144 ÷ 12 = 12۔ کیا علامتیں ایک جیسی ہیں؟"),
     ("Correct: unlike signs, −12.", "درست: مخالف علامتیں، −12"),
     ("144 ÷ 12 = 12 and the signs differ, so −12.", "144 ÷ 12 = 12 اور علامتیں مختلف ہیں، اس لیے −12"),
     [(12, "A negative divided by a positive is negative: −12.", "منفی کو مثبت پر تقسیم کریں تو منفی ملتا ہے: −12", "pos_only")], qtype=None)},
   {"id": "qb_exam_bodmas", "type": "exam_style", "step": nq(
     "qb_exam_bodmas", (f"Simplify 36 ÷ (2 + 4) + 5 × 2.", "36 ÷ (2 + 4) + 5 × 2 سادہ کریں۔"), QB3,
     ("Bracket first, then divide and multiply, then add.", "پہلے بریکٹ، پھر تقسیم اور ضرب، پھر جمع۔"),
     ("Correct: 6 + 10 = 16.", "درست: 6 + 10 = 16"),
     ("Bracket: 2 + 4 = 6. Then 36 ÷ 6 = 6 and 5 × 2 = 10. 6 + 10 = 16.", "بریکٹ: 2 + 4 = 6۔ پھر 36 ÷ 6 = 6 اور 5 × 2 = 10۔ 6 + 10 = 16"),
     [(32, "That ignores the bracket and divides 36 by 2 only. The answer is 16.", "یہ بریکٹ نظر انداز کر کے 36 کو صرف 2 سے تقسیم کرتا ہے۔ جواب 16 ہے۔", "skips_brackets")], qtype=None)},
 ]},
 "home_tasks": [{"id": "h_paper", "text": T(
   "Do Review Exercise 3 in your maths book in your notebook, setting out the working the way this test's answers do. Ask your teacher to check it.",
   "اپنی ریاضی کی کتاب کی اعادی مشق 3 اپنی کاپی میں حل کریں، اور کام اس ٹیسٹ کے جوابات کی طرح لکھیں۔ اپنے استاد سے جانچ کروائیں۔")}],
 "glossary": [T("Multiple choice", "کثیر انتخابی"), T("Short question", "مختصر سوال"), T("Long question", "تفصیلی سوال"),
              T("Distributive law", "قانون تقسیم"), T("BODMAS", "بوڈ ماس")],
 "steps": [
   {"id": "s1_paper", "type": "explain",
    "character": say("encouraging", "This is a test of the whole chapter, like the book's review exercise. Read each question carefully!",
                     "یہ پورے باب کا ٹیسٹ ہے، کتاب کی اعادی مشق کی طرح۔ ہر سوال غور سے پڑھیں!"),
    "text": T("This test goes with Review Exercise 3 of your maths book (PCTB Mathematics 6). It has three parts, like an exam paper: multiple choice questions (choose one answer), short questions (a few lines of working), and longer problems (full working in your notebook). The questions are new, not the book's.",
              "یہ ٹیسٹ آپ کی ریاضی کی کتاب (پنجاب ٹیکسٹ بک بورڈ، ریاضی 6) کی اعادی مشق 3 کے ساتھ ہے۔ اس کے تین حصے ہیں، امتحانی پرچے کی طرح: کثیر انتخابی سوال (ایک جواب چنیں)، مختصر سوال (چند سطروں کا کام)، اور تفصیلی سوال (پورا کام اپنی کاپی میں)۔ سوال نئے ہیں، کتاب والے نہیں۔")},
   mcq("m1_add", "(−9) + (−6) is equal to:", "(−9) + (−6) برابر ہے:",
       ("−15", "−15", "Correct: 9 + 6 = 15 and both are negative.", "درست: 9 + 6 = 15 اور دونوں منفی ہیں۔"),
       [("15", "15", "Two negative numbers give a negative sum.", "دو منفی اعداد کا مجموعہ منفی ہوتا ہے۔", "sign_lost"),
        ("−3", "−3", "That is (−9) + 6. Here both numbers are negative, so add the digits.", "یہ (−9) + 6 ہے۔ یہاں دونوں منفی ہیں، اس لیے ہندسے جمع کریں۔"),
        ("3", "3", "That is 9 − 6. Add the digits instead and keep the minus sign.", "یہ 9 − 6 ہے۔ ہندسے جمع کریں اور منفی علامت رکھیں۔")], 0),
   mcq("m2_sub", "7 − (−5) is equal to:", "7 − (−5) برابر ہے:",
       ("12", "12", "Correct: subtracting −5 is adding 5.", "درست: −5 کو گھٹانا 5 جمع کرنا ہے۔"),
       [("2", "2", "That is 7 − 5. The bracket has a minus sign too, so it becomes + 5.", "یہ 7 − 5 ہے۔ بریکٹ میں بھی منفی علامت ہے، اس لیے یہ + 5 بنتا ہے۔", "double_neg"),
        ("−12", "−12", "7 + 5 is positive.", "7 + 5 مثبت ہے۔", "sign_lost"),
        ("−2", "−2", "Subtracting −5 moves right, not left, so it cannot be −2.", "−5 کو گھٹانا دائیں لے جاتا ہے، بائیں نہیں، اس لیے یہ −2 نہیں ہو سکتا۔")], 2),
   mcq("m3_mul", "(−8) × (−7) is equal to:", "(−8) × (−7) برابر ہے:",
       ("56", "56", "Correct: like signs give a positive product.", "درست: ایک جیسی علامتوں کا حاصل ضرب مثبت ہے۔"),
       [("−56", "−56", "Two negative factors give a positive product.", "دو منفی اجزا کا حاصل ضرب مثبت ہے۔", "neg_neg"),
        ("−15", "−15", "That adds the numbers. We multiply.", "یہ اعداد جمع کرتا ہے۔ ہمیں ضرب کرنی ہے۔"),
        ("15", "15", "That adds the digits of 8 and 7. We multiply: 56.", "یہ 8 اور 7 کے ہندسے جمع کرتا ہے۔ ہمیں ضرب کرنی ہے: 56")], 1),
   mcq("m4_div", "(−54) ÷ 9 is equal to:", "(−54) ÷ 9 برابر ہے:",
       ("−6", "−6", "Correct: 54 ÷ 9 = 6 and the signs differ.", "درست: 54 ÷ 9 = 6 اور علامتیں مختلف ہیں۔"),
       [("6", "6", "Unlike signs give a negative quotient.", "مخالف علامتوں کا خارج قسمت منفی ہوتا ہے۔", "pos_only"),
        ("−45", "−45", "That subtracts 9 from −54. We divide.", "یہ −54 میں سے 9 گھٹاتا ہے۔ ہمیں تقسیم کرنی ہے۔"),
        ("−486", "−486", "That multiplies. We divide.", "یہ ضرب کرتا ہے۔ ہمیں تقسیم کرنی ہے۔")], 3),
   mcq("m5_law", "5 + (−3) = (−3) + 5 is an example of the:", "5 + (−3) = (−3) + 5 کس کی مثال ہے:",
       ("commutative law of addition", "جمع کا قانون تبدیلی", "Correct: the two numbers swap places and the sum is the same.", "درست: دونوں اعداد جگہ بدلتے ہیں اور مجموعہ وہی رہتا ہے۔"),
       [("associative law of addition", "جمع کا قانون شراکت", "The associative law changes the brackets, not the order of the numbers.", "قانون شراکت بریکٹ بدلتا ہے، اعداد کی ترتیب نہیں۔", "law_mixed"),
        ("distributive law", "قانون تقسیم", "The distributive law needs multiplication over a bracket with addition.", "قانون تقسیم میں جمع والے بریکٹ پر ضرب ہوتی ہے۔", "law_mixed"),
        ("additive identity", "جمعی ذاتی عدد", "The additive identity is about adding 0.", "جمعی ذاتی عدد 0 جمع کرنے کے بارے میں ہے۔", "law_mixed")], 2),
   mcq("m6_zero", "Which statement is true?", "کون سا بیان درست ہے؟",
       ("0 ÷ (−9) = 0", "0 ÷ (−9) = 0", "Correct: 0 divided by a non-zero integer is 0.", "درست: 0 کو غیر صفر صحیح عدد پر تقسیم کریں تو 0 ملتا ہے۔"),
       [("(−9) ÷ 0 = 0", "(−9) ÷ 0 = 0", "Division by 0 is undefined; there is no answer.", "صفر سے تقسیم غیر معین ہے؛ اس کا کوئی جواب نہیں۔", "zero_division"),
        ("(−9) ÷ 0 = −9", "(−9) ÷ 0 = −9", "Division by 0 is undefined; the answer is not the number itself.", "صفر سے تقسیم غیر معین ہے؛ جواب عدد خود نہیں ہوتا۔", "zero_division"),
        ("(−9) × (−9) = −81", "(−9) × (−9) = −81", "Two negatives give a positive: 81.", "دو منفی مل کر مثبت دیتے ہیں: 81", "neg_neg")], 0),
   mcq("m7_bodmas", "The value of 9 − 2 × 3 + 4 is:", "9 − 2 × 3 + 4 کی قیمت ہے:",
       (str(M7), str(M7), "Correct: 2 × 3 = 6, then 9 − 6 + 4 = 7.", "درست: 2 × 3 = 6، پھر 9 − 6 + 4 = 7"),
       [("25", "25", "That works left to right: 9 − 2 = 7, then × 3, then + 4. BODMAS multiplies first.", "یہ بائیں سے دائیں چلتا ہے: 9 − 2 = 7، پھر × 3، پھر + 4۔ بوڈ ماس پہلے ضرب کرتا ہے۔", "left_to_right"),
        ("−5", "−5", "That treats 3 + 4 as a bracket. There is no bracket here.", "یہ 3 + 4 کو بریکٹ سمجھتا ہے۔ یہاں بریکٹ نہیں ہے۔", "skips_brackets"),
        ("49", "49", "That adds before multiplying. Multiplication comes first.", "یہ ضرب سے پہلے جمع کرتا ہے۔ ضرب پہلے آتی ہے۔", "left_to_right")], 1),
   mcq("m8_distributive", "(−3) × (4 + 5) = (−3) × 4 + (−3) × 5 is an example of the:", "(−3) × (4 + 5) = (−3) × 4 + (−3) × 5 کس کی مثال ہے:",
       ("distributive law", "قانون تقسیم", "Correct: −3 is multiplied by each term in the bracket. Both sides are −27.", "درست: −3 بریکٹ کے ہر جز سے ضرب ہوا۔ دونوں طرف −27 ہے۔"),
       [("commutative law of multiplication", "ضرب کا قانون تبدیلی", "The commutative law swaps two numbers; nothing is swapped here.", "قانون تبدیلی دو اعداد کی جگہ بدلتا ہے؛ یہاں کچھ نہیں بدلا۔", "law_mixed"),
        ("associative law of multiplication", "ضرب کا قانون شراکت", "The associative law regroups three factors; here there is an addition.", "قانون شراکت تین اجزا کی گروہ بندی بدلتا ہے؛ یہاں جمع ہے۔", "law_mixed"),
        ("multiplicative identity", "ضربی ذاتی عدد", "The multiplicative identity is about multiplying by 1.", "ضربی ذاتی عدد 1 سے ضرب کے بارے میں ہے۔", "law_mixed")], 3),
   {"id": "s_short", "type": "explain",
    "text": T("Short questions. Work each one out in your notebook, then type the answer.",
              "مختصر سوال۔ ہر ایک اپنی کاپی میں حل کریں، پھر جواب لکھیں۔")},
   short("q1_unlike", "Find (−23) + 9.", "(−23) + 9 معلوم کریں۔", S1,
     ("Unlike signs: find 23 − 9 and use the sign of the bigger digits.", "مخالف علامتیں: 23 − 9 نکالیں اور بڑے ہندسوں کی علامت لگائیں۔"),
     ("Correct: −14.", "درست: −14"),
     ("Model answer: 23 − 9 = 14, and 23 is the negative one, so −14.", "نمونہ جواب: 23 − 9 = 14، اور 23 منفی ہے، اس لیے −14"),
     [(32, "The signs differ, so subtract the digits: 14, with a minus sign: −14.", "علامتیں مختلف ہیں، اس لیے ہندسے گھٹائیں: 14، منفی علامت کے ساتھ: −14", "sign_lost"),
      (14, "−23 is farther from 0 than 9, so the answer is negative: −14.", "−23، 9 سے 0 سے زیادہ دور ہے، اس لیے جواب منفی ہے: −14", "sign_lost")]),
   short("q2_sub", "Find (−18) − (−6).", "(−18) − (−6) معلوم کریں۔", S2,
     ("Subtracting −6 is adding 6.", "−6 کو گھٹانا 6 جمع کرنا ہے۔"),
     ("Correct: −18 + 6 = −12.", "درست: −18 + 6 = −12"),
     ("Model answer: (−18) − (−6) = −18 + 6 = −12.", "نمونہ جواب: (−18) − (−6) = −18 + 6 = −12"),
     [(-24, "That is (−18) − 6. Subtracting −6 means adding 6: −12.", "یہ (−18) − 6 ہے۔ −6 کو گھٹانے کا مطلب 6 جمع کرنا ہے: −12", "double_neg")]),
   short("q3_mul", "Find (−13) × (−4).", "(−13) × (−4) معلوم کریں۔", S3,
     ("13 × 4 = 52. Are the signs the same?", "13 × 4 = 52۔ کیا علامتیں ایک جیسی ہیں؟"),
     ("Correct: 52.", "درست: 52"),
     ("Model answer: 13 × 4 = 52, and like signs give a positive product: 52.", "نمونہ جواب: 13 × 4 = 52، اور ایک جیسی علامتوں کا حاصل ضرب مثبت ہے: 52"),
     [(-52, "Two negative factors give a positive product: 52.", "دو منفی اجزا کا حاصل ضرب مثبت ہے: 52", "neg_neg")]),
   short("q4_blank", "Fill in the blank with an integer: (−7) × □ = −63.", "خالی جگہ میں صحیح عدد لکھیں: (−7) × □ = −63", S4,
     ("Divide: (−63) ÷ (−7). The product is negative and −7 is negative, so the missing integer is positive.", "تقسیم کریں: (−63) ÷ (−7)۔ حاصل ضرب منفی ہے اور −7 منفی ہے، اس لیے گم شدہ عدد مثبت ہے۔"),
     ("Correct: 9.", "درست: 9"),
     ("Model answer: (−63) ÷ (−7) = 9. Check: (−7) × 9 = −63.", "نمونہ جواب: (−63) ÷ (−7) = 9۔ جانچ: (−7) × 9 = −63"),
     [(-9, "Check: (−7) × (−9) = 63, not −63. The missing integer is 9.", "جانچ: (−7) × (−9) = 63، −63 نہیں۔ گم شدہ صحیح عدد 9 ہے۔", "neg_neg")]),
   short("q5_bodmas", "Simplify 40 − 4 × (6 − 1).", "40 − 4 × (6 − 1) سادہ کریں۔", S5,
     ("Bracket first, then multiply, then subtract.", "پہلے بریکٹ، پھر ضرب، پھر تفریق۔"),
     ("Correct: 40 − 20 = 20.", "درست: 40 − 20 = 20"),
     ("Model answer: (6 − 1) = 5, 4 × 5 = 20, and 40 − 20 = 20.", "نمونہ جواب: (6 − 1) = 5، 4 × 5 = 20، اور 40 − 20 = 20"),
     [(180, "That subtracts 40 − 4 first. Multiplication comes before subtraction: 20.", "یہ پہلے 40 − 4 کرتا ہے۔ ضرب تفریق سے پہلے آتی ہے: 20", "left_to_right"),
      (15, "The bracket (6 − 1) has to be worked out as a whole: 5. Then 4 × 5 = 20 and 40 − 20 = 20.", "بریکٹ (6 − 1) کو پورا حل کرنا ہے: 5۔ پھر 4 × 5 = 20 اور 40 − 20 = 20", "skips_brackets")]),
   {"id": "s_long", "type": "explain",
    "text": T("Longer problems. Write full working in your notebook, then type the final answer.",
              "تفصیلی سوالات۔ اپنی کاپی میں پورا کام لکھیں، پھر آخری جواب لکھیں۔")},
   long_q("l1_temperature", "At 6 pm the temperature is 3 degrees. It falls 4 degrees every hour for 5 hours, and then rises 7 degrees. What is the temperature at the end?", "شام 6 بجے درجہ حرارت 3 ڈگری ہے۔ یہ 5 گھنٹے تک ہر گھنٹے 4 ڈگری گرتا ہے، پھر 7 ڈگری بڑھتا ہے۔ آخر میں درجہ حرارت کیا ہے؟", L1,
     ("The fall is 5 × (−4). Then add the rise of 7 to 3 + that.", "گرنا 5 × (−4) ہے۔ پھر 3 + اس میں 7 کا اضافہ جمع کریں۔"),
     ("Correct: 3 + (−20) + 7 = −10.", "درست: 3 + (−20) + 7 = −10"),
     ("Model answer: 5 × (−4) = −20. Then 3 + (−20) = −17, and −17 + 7 = −10 degrees.", "نمونہ جواب: 5 × (−4) = −20۔ پھر 3 + (−20) = −17، اور −17 + 7 = −10 ڈگری۔"),
     [(-17, "That stops before the rise of 7: −17 + 7 = −10.", "یہ 7 کے اضافے سے پہلے رک گیا: −17 + 7 = −10", "stops_early"),
      (30, "A fall is negative, so the change is −20, not +20: −10.", "گرنا منفی ہے، اس لیے تبدیلی +20 نہیں −20 ہے: −10", "pos_only")]),
   long_q("l2_associative", "Verify the associative law of multiplication for −2, 7 and −5. Work out ((−2) × 7) × (−5). It must equal (−2) × (7 × (−5)). What is the value?", "−2، 7 اور −5 کے لیے ضرب کا قانون شراکت جانچیں۔ ((−2) × 7) × (−5) معلوم کریں۔ یہ (−2) × (7 × (−5)) کے برابر ہونا چاہیے۔ قیمت کیا ہے؟", L2_L,
     ("L.H.S.: (−2) × 7 = −14, then (−14) × (−5). R.H.S.: 7 × (−5) = −35, then (−2) × (−35).", "L.H.S.: (−2) × 7 = −14، پھر (−14) × (−5)۔ R.H.S.: 7 × (−5) = −35، پھر (−2) × (−35)"),
     ("Correct: both sides are 70.", "درست: دونوں طرف 70 ہے۔"),
     ("Model answer: L.H.S. = (−14) × (−5) = 70. R.H.S. = (−2) × (−35) = 70. L.H.S. = R.H.S., so the law holds.", "نمونہ جواب: L.H.S. = (−14) × (−5) = 70۔ R.H.S. = (−2) × (−35) = 70۔ L.H.S. = R.H.S.، اس لیے قانون ٹھیک ہے۔"),
     [(-70, "Each side multiplies two negative numbers at the end, so the product is positive: 70.", "ہر طرف آخر میں دو منفی اعداد ضرب ہوتے ہیں، اس لیے حاصل ضرب مثبت ہے: 70", "neg_neg")]),
   long_q("l3_decimals", "Simplify 5.5 + 2 × {4.5 − (1.2 + 0.8)}.", "5.5 + 2 × {4.5 − (1.2 + 0.8)} سادہ کریں۔", L3,
     ("Innermost bracket first: 1.2 + 0.8. Then { }, then multiply, then add.", "سب سے اندر کا بریکٹ پہلے: 1.2 + 0.8۔ پھر { }، پھر ضرب، پھر جمع۔"),
     ("Correct: (1.2 + 0.8) = 2, {4.5 − 2} = 2.5, 2 × 2.5 = 5, 5.5 + 5 = 10.5.", "درست: (1.2 + 0.8) = 2، {4.5 − 2} = 2.5، 2 × 2.5 = 5، 5.5 + 5 = 10.5"),
     ("Model answer: 1.2 + 0.8 = 2; 4.5 − 2 = 2.5; 2 × 2.5 = 5; 5.5 + 5 = 10.5.", "نمونہ جواب: 1.2 + 0.8 = 2؛ 4.5 − 2 = 2.5؛ 2 × 2.5 = 5؛ 5.5 + 5 = 10.5"),
     [(18.75, "That adds 5.5 + 2 before multiplying. Multiplication comes first: 10.5.", "یہ ضرب سے پہلے 5.5 + 2 کرتا ہے۔ ضرب پہلے آتی ہے: 10.5", "left_to_right"),
      (5, "That is the value of 2 × {…} only. Add 5.5 at the end: 10.5.", "یہ صرف 2 × {…} کی قیمت ہے۔ آخر میں 5.5 جمع کریں: 10.5", "stops_early")]),
   long_q("l4_pens", "A shopkeeper buys 12 pens at Rs 15 each. He sells 8 of them at Rs 18 each and the other 4 at Rs 5 each. Write his gain as a positive integer and his loss as a negative integer. What is the result?", "ایک دکاندار 15 روپے فی قلم کے حساب سے 12 قلم خریدتا ہے۔ وہ ان میں سے 8 قلم 18 روپے فی قلم اور باقی 4 قلم 5 روپے فی قلم بیچتا ہے۔ نفع مثبت صحیح عدد اور نقصان منفی صحیح عدد لکھیں۔ نتیجہ کیا ہے؟", L4,
     ("Money in = 8 × 18 + 4 × 5. Money out = 12 × 15. Result = money in − money out.", "آمدنی = 8 × 18 + 4 × 5۔ خرچ = 12 × 15۔ نتیجہ = آمدنی − خرچ"),
     ("Correct: 164 − 180 = −16, a loss of Rs 16.", "درست: 164 − 180 = −16، یعنی 16 روپے کا نقصان۔"),
     ("Model answer: sold for 8 × 18 + 4 × 5 = 144 + 20 = 164. Cost 12 × 15 = 180. 164 − 180 = −16, a loss of Rs 16.", "نمونہ جواب: فروخت 8 × 18 + 4 × 5 = 144 + 20 = 164۔ لاگت 12 × 15 = 180۔ 164 − 180 = −16، یعنی 16 روپے کا نقصان۔"),
     [(16, "He received less than he paid, so it is a loss, written as −16.", "اسے ادا کردہ رقم سے کم ملی، اس لیے یہ نقصان ہے، یعنی −16", "sign_lost"),
      (164, "That is only the money received. Subtract the cost of 180: −16.", "یہ صرف وصول شدہ رقم ہے۔ لاگت 180 گھٹائیں: −16", "stops_early")]),
   {"id": "s_end_summary", "type": "summary",
    "character": say("celebrating", "You finished the chapter 3 test. Well done!", "آپ نے باب 3 کا ٹیسٹ مکمل کر لیا۔ شاباش!"),
    "text": T("In the exam: like signs add and unlike signs subtract; to subtract, add the opposite; in multiplying and dividing, like signs give plus and unlike signs give minus; addition and multiplication are commutative and associative, multiplication is distributive over addition, and nothing can be divided by 0. For mixed expressions use BODMAS: brackets from the inside out, then multiply and divide, then add and subtract.",
              "امتحان میں: ایک جیسی علامتیں جمع اور مخالف علامتیں تفریق کرتی ہیں؛ تفریق کے لیے مخالف جمع کریں؛ ضرب اور تقسیم میں ایک جیسی علامتیں پلس اور مخالف علامتیں مائنس دیتی ہیں؛ جمع اور ضرب تبدیلی اور شراکت کے قوانین مانتے ہیں، ضرب جمع پر تقسیم کا قانون مانتی ہے، اور کسی عدد کو 0 سے تقسیم نہیں کر سکتے۔ ملی جلی عبارتوں کے لیے بوڈ ماس: بریکٹ اندر سے باہر، پھر ضرب اور تقسیم، پھر جمع اور تفریق۔"),
    "points": [T("Check a division by multiplying back.", "تقسیم کو واپس ضرب دے کر جانچیں۔"),
               T("In a word problem, write the whole calculation first, then simplify it.", "لفظی سوال میں پہلے پورا حساب لکھیں، پھر سادہ کریں۔")]},
 ],
 "review_questions": [
   {"id": "r_exam_sub", "type": "exam_style", "skill": SKILL, "step": nq(
     "r_exam_sub", ("Find 14 − 30.", "14 − 30 معلوم کریں۔"), R1,
     ("Start at 14 and go 30 steps to the left.", "14 سے شروع کریں اور 30 قدم بائیں جائیں۔"),
     ("Correct: −16.", "درست: −16"), ("14 − 30 = −(30 − 14) = −16.", "14 − 30 = −(30 − 14) = −16"),
     [(16, "30 − 14 is 16, but 14 − 30 is negative: −16.", "30 − 14 تو 16 ہے، مگر 14 − 30 منفی ہے: −16", "sign_lost")], qtype=None)},
   {"id": "r_exam_dist", "type": "exam_style", "skill": SKILL, "step": nq(
     "r_exam_dist", ("Use the distributive law to find 4 × (6 + (−9)).", "قانون تقسیم سے 4 × (6 + (−9)) معلوم کریں۔"), R2,
     ("4 × 6 + 4 × (−9). Multiply both terms.", "4 × 6 + 4 × (−9)۔ دونوں اجزا کو ضرب دیں۔"),
     ("Correct: 24 − 36 = −12.", "درست: 24 − 36 = −12"), ("4 × 6 = 24 and 4 × (−9) = −36, so 24 − 36 = −12.", "4 × 6 = 24 اور 4 × (−9) = −36، اس لیے 24 − 36 = −12"),
     [(15, "That multiplies only 6. Multiply both terms: −12.", "یہ صرف 6 کو ضرب دیتا ہے۔ دونوں اجزا کو ضرب دیں: −12", "skips_brackets")], qtype=None)},
 ],
 "teacher_notes": [
   "A chapter test to use with Review Exercise 3 of the PCTB Mathematics 6 book, in the style of a paper: multiple choice, short questions, then longer problems. Only the kinds of question come from the book; every question, number and story here is new, because the book may not be copied.",
   "It has its own skill (maths.integers.chapter_3_test), with the chapter's integer and simplification skills as prerequisites, and is mastered with exam_style questions, like g9-maths-05-board-exam-practice.",
   "Urdu terms to check: کثیر انتخابی (multiple choice), مختصر سوال / تفصیلی سوال (short / long question), نمونہ جواب (model answer), اعادی مشق (review exercise), قانون تبدیلی / قانون شراکت / قانون تقسیم (commutative / associative / distributive law), غیر معین (undefined), بوڈ ماس (BODMAS).",
   "The numbers were worked out in content/sources/g6-maths-04/chapter_3_test.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}

write(lesson)
