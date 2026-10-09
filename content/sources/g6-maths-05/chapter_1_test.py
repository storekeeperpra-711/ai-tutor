"""Chapter 1 test (Factors and Multiples), set out like the book's review
exercise and a board paper: multiple choice, short questions, then longer
mixed problems. The questions are new; only the kinds of question follow
the book."""
from math import gcd, isqrt, lcm

from common import (T, opt, say, wrong, number_question, choice_question, write, factors, is_prime,
                    prime_factors, book_ref, REVIEW, CHAPTER_TEST, FM_FACTORS, FM_PRIMES,
                    FM_HCF, FM_LCM, FM_INDEX, FM_HCF_LCM, FM_WORD_PROBLEMS)
from figs import attach, bars_figure, en_list, ur_list

SKILL = CHAPTER_TEST


def lcm_of(*ns):
    out = 1
    for n in ns:
        out = lcm(out, n)
    return out


def clock(start_h, start_m, minutes):
    total = start_h * 60 + start_m + minutes
    return f"{total // 60 % 12 or 12}:{total % 60:02d}"


def mcq(id, en, ur, options):
    return choice_question(id, T("MCQ: " + en, "کثیر انتخابی: " + ur), options, qtype="exam_style")


def short(id, en, ur, *args, **kw):
    return number_question(id, T("Short question: " + en, "مختصر سوال: " + ur), *args, qtype="exam_style", **kw)


# MCQs
M1 = (87, 89, 91, 93)
assert [n for n in M1 if is_prime(n)] == [89] and 87 == 3 * 29 and 91 == 7 * 13 and 93 == 3 * 31
assert len(factors(1)) == 1 and is_prime(2) and 9 == 3 * 3 and 15 == 3 * 5
assert gcd(8, 15) == 1 and 8 * 15 == 120
M4 = lcm(14, 35)
assert M4 == 70 and gcd(14, 35) == 7 and 14 * 35 == 490
assert 2 ** 5 == 32 and 2 * 5 == 10 and 5 * 5 == 25 and 2 + 2 + 2 + 2 + 2 == 10
M6 = (196, 96, 160, 216)
assert [n for n in M6 if isqrt(n) ** 2 == n] == [196] and 196 == 14 * 14 and 216 == 6 ** 3
M7 = 864 // 24
assert M7 == 36 and gcd(24, 36) * lcm(24, 36) == 864 and 864 - 24 == 840 and 864 + 24 == 888
assert (-8) ** 2 == 64 and -(8 ** 2) == -64
# short questions
F52 = factors(52)
S1 = len(F52)
assert F52 == [1, 2, 4, 13, 26, 52] and S1 == 6
S2 = 252 // (2 ** 2 * 3 ** 2)
assert S2 == 7 and is_prime(S2) and prime_factors(252) == [2, 2, 3, 3, 7]
assert 252 // ((2 * 2) * (3 * 2)) == 10
S3 = gcd(96, 156)
assert S3 == 12 and lcm(96, 156) == 1248 and prime_factors(96) == [2, 2, 2, 2, 2, 3] and prime_factors(156) == [2, 2, 3, 13]
S4 = lcm_of(15, 20, 36)
assert S4 == 180 and 15 * 20 * 36 == 10800 and gcd(gcd(15, 20), 36) == 1
S5 = 17 ** 2
assert S5 == 289 and 17 * 2 == 34
# long problem 1: ribbons 132 cm and 198 cm cut into the longest equal pieces
L1 = gcd(132, 198)
L1B = 132 // L1 + 198 // L1
assert L1 == 66 and L1B == 2 + 3 == 5 and lcm(132, 198) == 396
# long problem 2: alarms every 8, 12 and 20 minutes, together at 9:00
L2 = lcm_of(8, 12, 20)
L2_TIME = clock(9, 0, L2)
assert L2 == 120 and L2_TIME == "11:00" and gcd(gcd(8, 12), 20) == 4 and clock(9, 0, 4) == "9:04"
assert clock(9, 0, 40) == "9:40" and clock(9, 0, 60 + 20) == "10:20" and 8 * 12 * 20 == 1920
# long problem 3: HCF 8, LCM 240, one number 48
L3 = 8 * 240 // 48
assert L3 == 40 and gcd(48, L3) == 8 and lcm(48, L3) == 240 and 240 // 48 == 5
# long problem 4: a perfect square between 50 and 100 with 3 as a factor
L4_ALL = [n for n in range(51, 100) if isqrt(n) ** 2 == n and n % 3 == 0]
assert L4_ALL == [81] and [n for n in range(51, 100) if isqrt(n) ** 2 == n] == [64, 81]
L4 = L4_ALL[0]
# question bank
QB1 = gcd(126, 210)
assert QB1 == 42 and lcm(126, 210) == 630
QB2 = lcm_of(6, 9, 15)
assert QB2 == 90 and clock(6, 0, QB2) == "7:30"
QB3 = 2 ** 3 * 3 ** 2
assert QB3 == 72 and 2 * 3 * 3 * 2 == 36
# review
R1 = 12 * 360 // 36
assert R1 == 120 and gcd(36, R1) == 12 and lcm(36, R1) == 360
R2 = gcd(64, 80)
R2B = 64 // R2 + 80 // R2
assert R2 == 16 and R2B == 4 + 5 == 9


lesson = {
 "id": "g6-maths-05-chapter-1-test",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Answer exam-style questions on the whole of chapter 1: factors, multiples, primes, prime factorisation and index notation, HCF, LCM, HCF × LCM, and squares.",
                      "textbook": book_ref("Review Exercise 1")}],
 "skills": [SKILL],
 "title": T("Chapter 1 test: Factors and Multiples", "باب 1 کا ٹیسٹ: اجزائے ضربی اور اضعاف"),
 "estimated_minutes": 25,
 "prerequisites": [{"skill": s} for s in (FM_FACTORS, FM_PRIMES, FM_HCF, FM_LCM, FM_INDEX, FM_HCF_LCM, FM_WORD_PROBLEMS)],
 "misconceptions": [
   {"id": "odd_is_prime", "description": "Thinks every odd number is prime."},
   {"id": "one_is_prime", "description": "Thinks 1 is prime or composite; it is neither."},
   {"id": "hcf_lcm_swap", "description": "Gives the LCM when the HCF is asked for, or the other way round."},
   {"id": "always_multiply", "description": "Multiplies the numbers to get the LCM, which is a common multiple but often not the lowest."},
   {"id": "times_index", "description": "Multiplies the base by the index: 2⁵ = 10."},
   {"id": "negative_square", "description": "Thinks the square of a negative number is negative."},
   {"id": "wrong_division", "description": "Divides the wrong numbers when using HCF × LCM = product."},
   {"id": "stops_early", "description": "Finds the HCF or LCM but does not answer the question asked."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["exam_style"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_exam_hcf", "type": "exam_style", "step": number_question(
     "qb_exam_hcf",
     T("Find the HCF of 126 and 210.", "126 اور 210 کا عاد اعظم معلوم کریں۔"),
     QB1,
     T("210 ÷ 126 = 1 remainder 84. Carry on with 126 ÷ 84.", "210 ÷ 126 = 1 باقی 84۔ آگے 126 ÷ 84 کریں۔"),
     T("Correct: HCF = 42.", "درست: عاد اعظم = 42"),
     T("210 ÷ 126 = 1 remainder 84; 126 ÷ 84 = 1 remainder 42; 84 ÷ 42 = 2 remainder 0. HCF = 42.", "210 ÷ 126 = 1 باقی 84؛ 126 ÷ 84 = 1 باقی 42؛ 84 ÷ 42 = 2 باقی 0۔ عاد اعظم = 42"),
     common_wrong=[wrong(630, "630 is the LCM. The HCF is 42.", "630 ذو اضعاف اقل ہے۔ عاد اعظم 42 ہے۔", "hcf_lcm_swap")],
     qtype=None)},
   {"id": "qb_exam_lcm", "type": "exam_style", "step": number_question(
     "qb_exam_lcm",
     T("Three taps drip every 6, 9 and 15 seconds. They drip together now. After how many seconds will they drip together again?", "تین نلکے ہر 6، 9 اور 15 سیکنڈ بعد ٹپکتے ہیں۔ ابھی تینوں ساتھ ٹپکے ہیں۔ کتنے سیکنڈ بعد دوبارہ ساتھ ٹپکیں گے؟"),
     QB2,
     T("Find the LCM of 6, 9 and 15.", "6، 9 اور 15 کا ذو اضعاف اقل معلوم کریں۔"),
     T("Correct: 2 × 3² × 5 = 90 seconds.", "درست: 2 × 3² × 5 = 90 سیکنڈ"),
     T("6 = 2 × 3, 9 = 3², 15 = 3 × 5. LCM = 2 × 3² × 5 = 90 seconds.", "6 = 2 × 3، 9 = 3²، 15 = 3 × 5۔ ذو اضعاف اقل = 2 × 3² × 5 = 90 سیکنڈ"),
     common_wrong=[wrong(3, "3 is the HCF. They drip together after the LCM: 90 seconds.", "3 عاد اعظم ہے۔ وہ ذو اضعاف اقل کے بعد ساتھ ٹپکیں گے: 90 سیکنڈ", "hcf_lcm_swap"),
                   wrong(810, "810 = 6 × 9 × 15 is a common multiple, but 90 is lower.", "810 = 6 × 9 × 15 مشترک ضعف ہے، مگر 90 چھوٹا ہے۔", "always_multiply")],
     qtype=None)},
   {"id": "qb_exam_index", "type": "exam_style", "step": number_question(
     "qb_exam_index",
     T("Which number is 2³ × 3²?", "2³ × 3² کون سا عدد ہے؟"),
     QB3,
     T("2³ = 8 and 3² = 9.", "2³ = 8 اور 3² = 9"),
     T("Correct: 8 × 9 = 72.", "درست: 8 × 9 = 72"),
     T("2³ × 3² = 2 × 2 × 2 × 3 × 3 = 8 × 9 = 72.", "2³ × 3² = 2 × 2 × 2 × 3 × 3 = 8 × 9 = 72"),
     common_wrong=[wrong(36, "2³ is 8, not 2 × 3 = 6, and 3² is 9, not 6. 8 × 9 = 72.", "2³ = 8 ہے، 2 × 3 = 6 نہیں، اور 3² = 9 ہے، 6 نہیں۔ 8 × 9 = 72", "times_index")],
     qtype=None)},
 ]},
 "home_tasks": [{"id": "h_paper", "text": T(
   "Do Review Exercise 1 in your maths book in your notebook, setting out the working the way this test's answers do. Ask your teacher to check it.",
   "اپنی ریاضی کی کتاب کی اعادی مشق 1 اپنی کاپی میں حل کریں، اور کام اس ٹیسٹ کے جوابات کی طرح لکھیں۔ اپنے استاد سے جانچ کروائیں۔")}],
 "glossary": [T("Multiple choice", "کثیر انتخابی"), T("Short question", "مختصر سوال"), T("Long question", "تفصیلی سوال"),
              T("Highest common factor (HCF)", "عاد اعظم"), T("Lowest common multiple (LCM)", "ذو اضعاف اقل")],
 "steps": [
   {"id": "s1_paper", "type": "explain",
    "character": say("encouraging", "This is a test of the whole chapter, like the book's review exercise. Read each question carefully!",
                     "یہ پورے باب کا ٹیسٹ ہے، کتاب کی اعادی مشق کی طرح۔ ہر سوال غور سے پڑھیں!"),
    "text": T("This test goes with Review Exercise 1 of your maths book (PCTB Mathematics 6). It has three parts, like an exam paper: multiple choice questions (choose one answer), short questions (a few lines of working), and longer problems (full working in your notebook). The questions are new, not the book's.",
              "یہ ٹیسٹ آپ کی ریاضی کی کتاب (پنجاب ٹیکسٹ بک بورڈ، ریاضی 6) کی اعادی مشق 1 کے ساتھ ہے۔ اس کے تین حصے ہیں، امتحانی پرچے کی طرح: کثیر انتخابی سوال (ایک جواب چنیں)، مختصر سوال (چند سطروں کا کام)، اور تفصیلی سوال (پورا کام اپنی کاپی میں)۔ سوال نئے ہیں، کتاب والے نہیں۔")},
   mcq("m1_prime", "Which of these is a prime number?", "ان میں سے کون سا مفرد عدد ہے؟", [
     opt("a", "87", "87", False, "87 = 3 × 29 (8 + 7 = 15, which 3 divides).", "87 = 3 × 29 (8 + 7 = 15، جسے 3 تقسیم کرتا ہے)۔", "odd_is_prime"),
     opt("b", "89", "89", True, "Correct: no prime up to 9 divides 89.", "درست: 9 تک کا کوئی مفرد عدد 89 کو تقسیم نہیں کرتا۔"),
     opt("c", "91", "91", False, "91 = 7 × 13.", "91 = 7 × 13", "odd_is_prime"),
     opt("d", "93", "93", False, "93 = 3 × 31.", "93 = 3 × 31", "odd_is_prime"),
   ]),
   mcq("m2_neither", "Which number is neither prime nor composite?", "کون سا عدد نہ مفرد ہے نہ مرکب؟", [
     opt("a", "1", "1", True, "Correct: 1 has only one factor.", "درست: 1 کا صرف ایک جزو ضربی ہے۔"),
     opt("b", "2", "2", False, "2 is prime: its factors are 1 and 2.", "2 مفرد ہے: اس کے اجزائے ضربی 1 اور 2 ہیں۔"),
     opt("c", "9", "9", False, "9 = 3 × 3 is composite.", "9 = 3 × 3 مرکب ہے۔"),
     opt("d", "15", "15", False, "15 = 3 × 5 is composite.", "15 = 3 × 5 مرکب ہے۔"),
   ]),
   mcq("m3_coprime", "The HCF of two co-prime numbers, like 8 and 15, is:", "دو باہم مفرد اعداد کا عاد اعظم، جیسے 8 اور 15، ہوتا ہے:", [
     opt("a", "1", "1", True, "Correct: co-prime numbers share no factor except 1.", "درست: باہم مفرد اعداد میں 1 کے سوا کوئی جزو ضربی مشترک نہیں ہوتا۔"),
     opt("b", "0", "0", False, "0 is never a factor. The HCF is 1.", "0 کبھی جزو ضربی نہیں ہوتا۔ عاد اعظم 1 ہے۔"),
     opt("c", "their product", "ان کا حاصل ضرب", False, "Their product (120) is the LCM, not the HCF.", "ان کا حاصل ضرب (120) ذو اضعاف اقل ہے، عاد اعظم نہیں۔", "hcf_lcm_swap"),
     opt("d", "the smaller number", "چھوٹا عدد", False, "8 does not divide 15. The HCF is 1.", "8، 15 کو تقسیم نہیں کرتا۔ عاد اعظم 1 ہے۔"),
   ]),
   mcq("m4_lcm", "The LCM of 14 and 35 is:", "14 اور 35 کا ذو اضعاف اقل ہے:", [
     opt("a", str(M4), str(M4), True, "Correct: 2 × 5 × 7 = 70.", "درست: 2 × 5 × 7 = 70"),
     opt("b", "7", "7", False, "7 is the HCF.", "7 عاد اعظم ہے۔", "hcf_lcm_swap"),
     opt("c", "490", "490", False, "490 = 14 × 35 is a common multiple, but 70 is lower.", "490 = 14 × 35 مشترک ضعف ہے، مگر 70 چھوٹا ہے۔", "always_multiply"),
     opt("d", "35", "35", False, "14 does not divide 35.", "14، 35 کو تقسیم نہیں کرتا۔"),
   ]),
   mcq("m5_index", "2⁵ means:", "2⁵ کا مطلب ہے:", [
     opt("a", "2 × 2 × 2 × 2 × 2", "2 × 2 × 2 × 2 × 2", True, "Correct: five 2s multiplied, which is 32.", "درست: پانچ 2 کا حاصل ضرب، یعنی 32"),
     opt("b", "2 × 5", "2 × 5", False, "2 × 5 = 10. The index 5 means five 2s multiplied.", "2 × 5 = 10۔ قوت 5 کا مطلب پانچ 2 کا حاصل ضرب۔", "times_index"),
     opt("c", "5 × 5", "5 × 5", False, "That is 5². In 2⁵ the base is 2.", "یہ 5² ہے۔ 2⁵ میں اساس 2 ہے۔"),
     opt("d", "2 + 2 + 2 + 2 + 2", "2 + 2 + 2 + 2 + 2", False, "The 2s are multiplied, not added.", "2 ضرب ہوتے ہیں، جمع نہیں۔"),
   ]),
   mcq("m6_square", "Which of these is a perfect square?", "ان میں سے کون سا مکمل مربع عدد ہے؟", [
     opt("a", "196", "196", True, "Correct: 14 × 14 = 196.", "درست: 14 × 14 = 196"),
     opt("b", "96", "96", False, "9² = 81 and 10² = 100, so 96 is not a square.", "9² = 81 اور 10² = 100، اس لیے 96 مربع نہیں۔"),
     opt("c", "160", "160", False, "12² = 144 and 13² = 169, so 160 is not a square.", "12² = 144 اور 13² = 169، اس لیے 160 مربع نہیں۔"),
     opt("d", "216", "216", False, "216 = 6 × 6 × 6, but it is not a number times itself: 14² = 196 and 15² = 225.", "216 = 6 × 6 × 6، مگر یہ کسی عدد ضرب خود نہیں: 14² = 196 اور 15² = 225"),
   ]),
   mcq("m7_product", "For two numbers, HCF × LCM = 864. One number is 24. The other number is:", "دو اعداد کے لیے عاد اعظم × ذو اضعاف اقل = 864۔ ایک عدد 24 ہے۔ دوسرا عدد ہے:", [
     opt("a", str(M7), str(M7), True, "Correct: 864 ÷ 24 = 36.", "درست: 864 ÷ 24 = 36"),
     opt("b", "840", "840", False, "That is 864 − 24. Divide: 864 ÷ 24 = 36.", "یہ 864 − 24 ہے۔ تقسیم کریں: 864 ÷ 24 = 36", "wrong_division"),
     opt("c", "888", "888", False, "That is 864 + 24. Divide: 864 ÷ 24 = 36.", "یہ 864 + 24 ہے۔ تقسیم کریں: 864 ÷ 24 = 36", "wrong_division"),
     opt("d", "24", "24", False, "24 × 24 = 576, not 864. The other number is 36.", "24 × 24 = 576، 864 نہیں۔ دوسرا عدد 36 ہے۔"),
   ]),
   mcq("m8_negative", "(−8)² is equal to:", "(−8)² برابر ہے:", [
     opt("a", "64", "64", True, "Correct: (−8) × (−8) = 64.", "درست: (−8) × (−8) = 64"),
     opt("b", "−64", "−64", False, "Negative times negative is positive: 64.", "منفی ضرب منفی مثبت ہوتا ہے: 64", "negative_square"),
     opt("c", "−16", "−16", False, "That is −8 × 2. Square means (−8) × (−8) = 64.", "یہ −8 × 2 ہے۔ مربع کا مطلب (−8) × (−8) = 64", "times_index"),
     opt("d", "16", "16", False, "16 = 8 × 2. Square means (−8) × (−8) = 64.", "16 = 8 × 2۔ مربع کا مطلب (−8) × (−8) = 64", "times_index"),
   ]),
   {"id": "s_short", "type": "explain",
    "text": T("Short questions. Work each one out in your notebook, then type the answer.",
              "مختصر سوال۔ ہر ایک اپنی کاپی میں حل کریں، پھر جواب لکھیں۔")},
   short("q1_factors", "Write all the factors of 52. How many factors are there?", "52 کے سارے اجزائے ضربی لکھیں۔ کل کتنے اجزائے ضربی ہیں؟",
     S1,
     T("Find them in pairs: 1 × 52, 2 × 26, 4 × 13.", "جوڑوں میں ڈھونڈیں: 1 × 52، 2 × 26، 4 × 13"),
     T(f"Correct: {en_list(F52)}.", f"درست: {ur_list(F52)}"),
     T(f"Model answer: 52 = 1 × 52 = 2 × 26 = 4 × 13. Factors: {en_list(F52)}, so {S1} factors.", f"نمونہ جواب: 52 = 1 × 52 = 2 × 26 = 4 × 13۔ اجزائے ضربی: {ur_list(F52)}، یعنی {S1}"),
     common_wrong=[wrong(S1 - 2, "Count 1 and 52 as well.", "1 اور 52 بھی گنیں۔")]),
   short("q2_prime_factors", "252 = 2² × 3² × p, where p is a prime. Find p.", "252 = 2² × 3² × p، جہاں p مفرد عدد ہے۔ p معلوم کریں۔",
     S2,
     T("2² × 3² = 4 × 9 = 36. Divide 252 by 36.", "2² × 3² = 4 × 9 = 36۔ 252 کو 36 سے تقسیم کریں۔"),
     T("Correct: p = 7.", "درست: p = 7"),
     T("Model answer: 252 ÷ 2 = 126, ÷ 2 = 63, ÷ 3 = 21, ÷ 3 = 7. So 252 = 2² × 3² × 7 and p = 7.", "نمونہ جواب: 252 ÷ 2 = 126، ÷ 2 = 63، ÷ 3 = 21، ÷ 3 = 7۔ اس لیے 252 = 2² × 3² × 7 اور p = 7"),
     common_wrong=[wrong(10, "2² is 4 and 3² is 9, so 252 ÷ 36 = 7.", "2² = 4 اور 3² = 9، اس لیے 252 ÷ 36 = 7", "times_index")]),
   short("q3_hcf", "Find the HCF of 96 and 156.", "96 اور 156 کا عاد اعظم معلوم کریں۔",
     S3,
     T("96 = 2⁵ × 3 and 156 = 2² × 3 × 13.", "96 = 2⁵ × 3 اور 156 = 2² × 3 × 13"),
     T("Correct: HCF = 2² × 3 = 12.", "درست: عاد اعظم = 2² × 3 = 12"),
     T("Model answer: 96 = 2⁵ × 3, 156 = 2² × 3 × 13. Shared: 2² × 3 = 12.", "نمونہ جواب: 96 = 2⁵ × 3، 156 = 2² × 3 × 13۔ مشترک: 2² × 3 = 12"),
     common_wrong=[wrong(1248, "1248 is the LCM. The HCF is 12.", "1248 ذو اضعاف اقل ہے۔ عاد اعظم 12 ہے۔", "hcf_lcm_swap")]),
   short("q4_lcm", "Find the LCM of 15, 20 and 36.", "15، 20 اور 36 کا ذو اضعاف اقل معلوم کریں۔",
     S4,
     T("15 = 3 × 5, 20 = 2² × 5, 36 = 2² × 3².", "15 = 3 × 5، 20 = 2² × 5، 36 = 2² × 3²"),
     T("Correct: 2² × 3² × 5 = 180.", "درست: 2² × 3² × 5 = 180"),
     T("Model answer: take each prime with its highest index: 2² × 3² × 5 = 180.", "نمونہ جواب: ہر مفرد عدد اس کی سب سے بڑی قوت کے ساتھ: 2² × 3² × 5 = 180"),
     common_wrong=[wrong(1, "1 is the HCF. The LCM is 180.", "1 عاد اعظم ہے۔ ذو اضعاف اقل 180 ہے۔", "hcf_lcm_swap"),
                   wrong(10800, "10800 = 15 × 20 × 36 is a common multiple, but 180 is lower.", "10800 = 15 × 20 × 36 مشترک ضعف ہے، مگر 180 چھوٹا ہے۔", "always_multiply")]),
   short("q5_square", "Find 17².", "17² معلوم کریں۔",
     S5,
     T("17 × 17 = 17 × 10 + 17 × 7.", "17 × 17 = 17 × 10 + 17 × 7"),
     T("Correct: 289.", "درست: 289"),
     T("Model answer: 17 × 10 = 170 and 17 × 7 = 119, so 17² = 289.", "نمونہ جواب: 17 × 10 = 170 اور 17 × 7 = 119، اس لیے 17² = 289"),
     common_wrong=[wrong(34, "That is 17 × 2. 17² = 17 × 17 = 289.", "یہ 17 × 2 ہے۔ 17² = 17 × 17 = 289", "times_index")]),
   {"id": "s_long", "type": "explain",
    "character": say("talking", "Longer problems now. Write every step: what you find, how, and the answer in a sentence.",
                     "اب تفصیلی سوال۔ ہر قدم لکھیں: کیا معلوم کر رہے ہیں، کیسے، اور آخر میں جواب ایک جملے میں۔"),
    "text": T("For each problem, first decide: HCF (sharing into the largest equal parts) or LCM (when things happen together again)? Show the prime factors or the division, then answer the question that was asked.",
              "ہر سوال میں پہلے فیصلہ کریں: عاد اعظم (سب سے بڑے برابر حصوں میں بانٹنا) یا ذو اضعاف اقل (چیزیں دوبارہ کب ساتھ ہوں)؟ مفرد اجزائے ضربی یا تقسیم دکھائیں، پھر وہی جواب دیں جو پوچھا گیا ہے۔")},
   number_question(
     "l1_ribbon",
     T("Long question: Two ribbons are 132 cm and 198 cm long. Both are cut into pieces of the same length, as long as possible, with nothing left over. (a) How long is each piece, in cm?", "تفصیلی سوال: دو فیتے 132 سینٹی میٹر اور 198 سینٹی میٹر لمبے ہیں۔ دونوں کو برابر لمبائی کے ٹکڑوں میں کاٹا جاتا ہے، جتنے لمبے ہو سکیں، اور کچھ نہیں بچتا۔ (الف) ہر ٹکڑا کتنے سینٹی میٹر کا ہے؟"),
     L1,
     T("The piece length divides 132 and 198. Find the HCF.", "ٹکڑے کی لمبائی 132 اور 198 دونوں کو تقسیم کرے۔ عاد اعظم معلوم کریں۔"),
     T("Correct: 66 cm.", "درست: 66 سینٹی میٹر"),
     T("Model answer: 132 = 2² × 3 × 11 and 198 = 2 × 3² × 11. HCF = 2 × 3 × 11 = 66. Each piece is 66 cm.", "نمونہ جواب: 132 = 2² × 3 × 11 اور 198 = 2 × 3² × 11۔ عاد اعظم = 2 × 3 × 11 = 66۔ ہر ٹکڑا 66 سینٹی میٹر کا ہے۔"),
     common_wrong=[wrong(396, "396 is the LCM, longer than both ribbons! Use the HCF: 66.", "396 ذو اضعاف اقل ہے، دونوں فیتوں سے لمبا! عاد اعظم لیں: 66", "hcf_lcm_swap"),
                   wrong(33, "33 cm pieces work, but 66 cm pieces are longer.", "33 سینٹی میٹر کے ٹکڑے بن سکتے ہیں، مگر 66 سینٹی میٹر کے لمبے ہیں۔")],
     qtype="exam_style"),
   number_question(
     "l1_pieces",
     T("(b) How many pieces are there altogether?", "(ب) کل کتنے ٹکڑے ہیں؟"),
     L1B,
     T("132 ÷ 66 and 198 ÷ 66. Add them.", "132 ÷ 66 اور 198 ÷ 66۔ دونوں جمع کریں۔"),
     T("Correct: 2 + 3 = 5 pieces.", "درست: 2 + 3 = 5 ٹکڑے"),
     T("Model answer: 132 ÷ 66 = 2 and 198 ÷ 66 = 3, so there are 2 + 3 = 5 pieces.", "نمونہ جواب: 132 ÷ 66 = 2 اور 198 ÷ 66 = 3، اس لیے کل 2 + 3 = 5 ٹکڑے ہیں۔"),
     common_wrong=[wrong(66, "66 cm is the length of a piece. Count the pieces: 2 + 3 = 5.", "66 سینٹی میٹر ایک ٹکڑے کی لمبائی ہے۔ ٹکڑے گنیں: 2 + 3 = 5", "stops_early")],
     qtype="exam_style"),
   number_question(
     "l2_alarms",
     T("Long question: Three alarms ring every 8, 12 and 20 minutes. They ring together at 9:00. (a) After how many minutes do they next ring together?", "تفصیلی سوال: تین الارم ہر 8، 12 اور 20 منٹ بعد بجتے ہیں۔ 9 بجے تینوں ساتھ بجے۔ (الف) کتنے منٹ بعد اگلی بار ساتھ بجیں گے؟"),
     L2,
     T("8 = 2³, 12 = 2² × 3, 20 = 2² × 5. Find the LCM.", "8 = 2³، 12 = 2² × 3، 20 = 2² × 5۔ ذو اضعاف اقل معلوم کریں۔"),
     T("Correct: 120 minutes.", "درست: 120 منٹ"),
     T("Model answer: LCM = 2³ × 3 × 5 = 120. They ring together after 120 minutes.", "نمونہ جواب: ذو اضعاف اقل = 2³ × 3 × 5 = 120۔ وہ 120 منٹ بعد ساتھ بجیں گے۔"),
     common_wrong=[wrong(4, "4 is the HCF. After 4 minutes no alarm has rung again.", "4 عاد اعظم ہے۔ 4 منٹ بعد کوئی الارم دوبارہ نہیں بجا۔", "hcf_lcm_swap"),
                   wrong(1920, "1920 = 8 × 12 × 20 is a common multiple, but 120 is lower.", "1920 = 8 × 12 × 20 مشترک ضعف ہے، مگر 120 چھوٹا ہے۔", "always_multiply")],
     qtype="exam_style"),
   choice_question(
     "l2_time",
     T("(b) At what time do they next ring together?", "(ب) اگلی بار کس وقت ساتھ بجیں گے؟"),
     [opt("right", L2_TIME, L2_TIME, True, "Correct: 120 minutes = 2 hours after 9:00.", "درست: 120 منٹ = 9 بجے کے 2 گھنٹے بعد۔"),
      opt("hcf", clock(9, 0, 4), clock(9, 0, 4), False, "That adds the HCF, 4 minutes. Add 120 minutes: 11:00.", "اس میں عاد اعظم، 4 منٹ، جمع کیا گیا۔ 120 منٹ جمع کریں: 11:00", "hcf_lcm_swap"),
      opt("forty", clock(9, 0, 40), clock(9, 0, 40), False, "40 is the LCM of 8 and 20 only. All three meet after 120 minutes: 11:00.", "40 صرف 8 اور 20 کا ذو اضعاف اقل ہے۔ تینوں 120 منٹ بعد ملتے ہیں: 11:00"),
      opt("ten", clock(9, 0, 60 + 20), clock(9, 0, 60 + 20), False, "120 minutes is 2 hours, not 1 hour 20 minutes. 9:00 + 2 hours = 11:00.", "120 منٹ، 2 گھنٹے ہیں، 1 گھنٹہ 20 منٹ نہیں۔ 9:00 + 2 گھنٹے = 11:00")],
     qtype="exam_style"),
   number_question(
     "l3_missing",
     T("Long question: The HCF of two numbers is 8 and their LCM is 240. One number is 48. Find the other number.", "تفصیلی سوال: دو اعداد کا عاد اعظم 8 اور ذو اضعاف اقل 240 ہے۔ ایک عدد 48 ہے۔ دوسرا عدد معلوم کریں۔"),
     L3,
     T("HCF × LCM = product of the two numbers. 8 × 240 = 1920.", "عاد اعظم × ذو اضعاف اقل = دونوں اعداد کا حاصل ضرب۔ 8 × 240 = 1920"),
     T("Correct: 1920 ÷ 48 = 40.", "درست: 1920 ÷ 48 = 40"),
     T("Model answer: 48 × other = 8 × 240 = 1920, so other = 1920 ÷ 48 = 40. Check: HCF of 48 and 40 is 8, LCM is 240.", "نمونہ جواب: 48 × دوسرا = 8 × 240 = 1920، اس لیے دوسرا = 1920 ÷ 48 = 40۔ جانچ: 48 اور 40 کا عاد اعظم 8 اور ذو اضعاف اقل 240 ہے۔"),
     common_wrong=[wrong(5, "That is 240 ÷ 48. Find the product first: 1920 ÷ 48 = 40.", "یہ 240 ÷ 48 ہے۔ پہلے حاصل ضرب: 1920 ÷ 48 = 40", "wrong_division"),
                   wrong(240, "That is 1920 ÷ 8, the LCM. Divide by the known number 48: 40.", "یہ 1920 ÷ 8 ہے، یعنی ذو اضعاف اقل۔ معلوم عدد 48 سے تقسیم کریں: 40", "wrong_division")],
     qtype="exam_style"),
   number_question(
     "l4_who_am_i",
     T("Long question: Who am I? I am a perfect square between 50 and 100, and 3 is one of my factors.", "تفصیلی سوال: میں کون ہوں؟ میں 50 اور 100 کے درمیان ایک مکمل مربع عدد ہوں، اور 3 میرا ایک جزو ضربی ہے۔"),
     L4,
     T("List the perfect squares between 50 and 100. Which one does 3 divide?", "50 اور 100 کے درمیان مکمل مربع اعداد لکھیں۔ ان میں سے کسے 3 تقسیم کرتا ہے؟"),
     T("Correct: 81 = 9² and 81 ÷ 3 = 27.", "درست: 81 = 9² اور 81 ÷ 3 = 27"),
     T("Model answer: the perfect squares between 50 and 100 are 64 = 8² and 81 = 9². 64 ÷ 3 is not exact, but 81 ÷ 3 = 27. So I am 81.", "نمونہ جواب: 50 اور 100 کے درمیان مکمل مربع اعداد 64 = 8² اور 81 = 9² ہیں۔ 64 ÷ 3 پورا تقسیم نہیں ہوتا، مگر 81 ÷ 3 = 27۔ اس لیے میں 81 ہوں۔"),
     common_wrong=[wrong(64, "64 is a perfect square, but 3 does not divide it.", "64 مکمل مربع ہے، مگر 3 اسے تقسیم نہیں کرتا۔"),
                   wrong(9, "9 is not between 50 and 100. 9² = 81 is.", "9، 50 اور 100 کے درمیان نہیں۔ 9² = 81 ہے۔")],
     qtype="exam_style"),
   {"id": "s_end_summary", "type": "summary",
    "character": say("celebrating", "You finished the chapter 1 test. Well done!", "آپ نے باب 1 کا ٹیسٹ مکمل کر لیا۔ شاباش!"),
    "text": T("In the exam: break numbers into primes, use the shared primes for the HCF and every prime (highest index) for the LCM, use HCF × LCM = product for a missing number, and remember that the square of a negative number is positive. In word problems, write the answer as a sentence.",
              "امتحان میں: اعداد کو مفرد اعداد میں توڑیں، عاد اعظم کے لیے مشترک مفرد اعداد اور ذو اضعاف اقل کے لیے ہر مفرد عدد (سب سے بڑی قوت) لیں، گمشدہ عدد کے لیے عاد اعظم × ذو اضعاف اقل = حاصل ضرب استعمال کریں، اور یاد رکھیں کہ منفی عدد کا مربع مثبت ہوتا ہے۔ سوالات میں جواب ایک جملے میں لکھیں۔"),
    "points": [T("Check an HCF by dividing: it must go into every number exactly.", "عاد اعظم کو تقسیم سے جانچیں: یہ ہر عدد کو پورا تقسیم کرے۔"),
               T("Check an LCM by dividing: every number must go into it exactly.", "ذو اضعاف اقل کو تقسیم سے جانچیں: ہر عدد اسے پورا تقسیم کرے۔")]},
 ],
 "review_questions": [
   {"id": "r_exam_missing", "type": "exam_style", "skill": SKILL, "step": number_question(
     "r_exam_missing",
     T("Two numbers have HCF 12 and LCM 360. One number is 36. Find the other.", "دو اعداد کا عاد اعظم 12 اور ذو اضعاف اقل 360 ہے۔ ایک عدد 36 ہے۔ دوسرا معلوم کریں۔"),
     R1,
     T("12 × 360 = 4320. Divide by 36.", "12 × 360 = 4320۔ 36 سے تقسیم کریں۔"),
     T("Correct: 4320 ÷ 36 = 120.", "درست: 4320 ÷ 36 = 120"),
     T("12 × 360 = 4320 and 4320 ÷ 36 = 120.", "12 × 360 = 4320 اور 4320 ÷ 36 = 120"),
     common_wrong=[wrong(10, "That is 360 ÷ 36. Use the product: 4320 ÷ 36 = 120.", "یہ 360 ÷ 36 ہے۔ حاصل ضرب استعمال کریں: 4320 ÷ 36 = 120", "wrong_division")],
     qtype=None)},
   {"id": "r_exam_pieces", "type": "exam_style", "skill": SKILL, "step": number_question(
     "r_exam_pieces",
     T("64 apples and 80 oranges are packed in boxes, each box with one kind of fruit and the same number of fruits, as many as possible. How many boxes are needed?", "64 سیب اور 80 مالٹے ڈبوں میں رکھے جاتے ہیں، ہر ڈبے میں ایک قسم کا پھل اور برابر تعداد، جتنی زیادہ ہو سکے۔ کتنے ڈبے چاہییں؟"),
     R2B,
     T("The number in each box is the HCF of 64 and 80. Then count the boxes.", "ہر ڈبے کی تعداد 64 اور 80 کا عاد اعظم ہے۔ پھر ڈبے گنیں۔"),
     T("Correct: 16 in a box, 4 + 5 = 9 boxes.", "درست: ہر ڈبے میں 16، کل 4 + 5 = 9 ڈبے۔"),
     T("HCF of 64 and 80 = 16. 64 ÷ 16 = 4 and 80 ÷ 16 = 5, so 9 boxes.", "64 اور 80 کا عاد اعظم = 16۔ 64 ÷ 16 = 4 اور 80 ÷ 16 = 5، اس لیے 9 ڈبے۔"),
     common_wrong=[wrong(R2, "16 is the number of fruits in each box. Count the boxes: 4 + 5 = 9.", "16 ہر ڈبے میں پھلوں کی تعداد ہے۔ ڈبے گنیں: 4 + 5 = 9", "stops_early")],
     qtype=None)},
 ],
 "teacher_notes": [
   "A chapter test to use with Review Exercise 1 of the PCTB Mathematics 6 book, in the style of a paper: multiple choice, short questions, then longer problems. Only the kinds of question come from the book; every question, number and story here is new, because the book may not be copied.",
   "It has its own skill (maths.factors.chapter_1_test), with the unit's skills as prerequisites, and is mastered with exam_style questions, like g9-maths-05-board-exam-practice.",
   "Urdu terms to check: کثیر انتخابی (multiple choice), مختصر سوال / تفصیلی سوال (short / long question), نمونہ جواب (model answer), اعادی مشق (review exercise), باہم مفرد (co-prime).",
   "The numbers were worked out in content/sources/g6-maths-05/chapter_1_test.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}

attach(lesson, {
    "l1_ribbon": bars_figure([132, 198],
        "Two ribbons drawn as bars: one 132 long and a longer one 198 long, with the lengths written after them.",
        "دو فیتے پٹیوں کی صورت میں: ایک 132 لمبا اور ایک لمبا 198، ساتھ لمبائیاں لکھی ہیں۔"),
})
write(lesson)
