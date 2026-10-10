"""Practice set for Exercise 1.3 of the book: HCF by prime factorisation
and by long division, and word problems about equal rows, packs and
tiles. The questions are new; only the kinds of question follow the book."""
from math import gcd, lcm

from common import (T, opt, say, wrong, number_question, choice_question, practice_lesson,
                    practice_intro, write, factors, prime_factors, EX_SKILL, FM_HCF, FM_PRIMES, FM_WORD_PROBLEMS)
from figs import attach, venn, floor_figure, bars_figure

SKILL = EX_SKILL["1.3"]


def long_division(a, b):
    """The steps of the long division method: [(dividend, divisor, quotient, remainder)]."""
    a, b = max(a, b), min(a, b)
    steps = []
    while b:
        steps.append((a, b, a // b, a % b))
        a, b = b, a % b
    return steps


def steps_en(steps):
    return "; ".join(f"{a} ÷ {b} = {q} remainder {r}" for a, b, q, r in steps)


def steps_ur(steps):
    return "؛ ".join(f"{a} ÷ {b} = {q} باقی {r}" for a, b, q, r in steps)


def split_primes(a, b):
    pa, pb = prime_factors(a), prime_factors(b)
    both, rest_b = [], list(pb)
    for p in pa:
        if p in rest_b:
            both.append(p)
            rest_b.remove(p)
    rest_a = list(pa)
    for p in both:
        rest_a.remove(p)
    return rest_a, both, rest_b


# q1: HCF of 16 and 40 by listing
Q1 = gcd(16, 40)
assert Q1 == 8 and factors(16) == [1, 2, 4, 8, 16] and lcm(16, 40) == 80
assert [f for f in factors(16) if 40 % f == 0] == [1, 2, 4, 8]
# q2: 60 = 2² × 3 × 5 and 84 = 2² × 3 × 7
Q2 = gcd(60, 84)
assert prime_factors(60) == [2, 2, 3, 5] and prime_factors(84) == [2, 2, 3, 7]
assert Q2 == 2 * 2 * 3 == 12 and lcm(60, 84) == 420 and 2 * 2 * 3 * 5 * 7 == 420
RA2, BOTH2, RB2 = split_primes(60, 84)
assert (RA2, BOTH2, RB2) == ([5], [2, 2, 3], [7])
# q3: HCF of 72 and 108
Q3 = gcd(72, 108)
assert prime_factors(72) == [2, 2, 2, 3, 3] and prime_factors(108) == [2, 2, 3, 3, 3]
assert Q3 == 36 == 2 * 2 * 3 * 3 and lcm(72, 108) == 216 and 108 % 12 == 0 and 72 % 12 == 0
# q4: HCF of 24, 36 and 60
Q4 = gcd(gcd(24, 36), 60)
assert Q4 == 12 and gcd(24, 36) == 12 and gcd(36, 60) == 12 and lcm(lcm(24, 36), 60) == 360
# s_long: worked example, 45 and 75
EX = long_division(75, 45)
assert EX == [(75, 45, 1, 30), (45, 30, 1, 15), (30, 15, 2, 0)] and gcd(45, 75) == 15
# q5, q6: 156 and 204
L5 = long_division(204, 156)
assert L5 == [(204, 156, 1, 48), (156, 48, 3, 12), (48, 12, 4, 0)]
Q5 = L5[0][3]
Q6 = L5[-1][1]
assert Q5 == 48 and Q6 == 12 == gcd(156, 204) and 204 - 156 == 48
# q7: 299 and 391 (prime factors are hard to see, long division is quick)
L7 = long_division(391, 299)
Q7 = L7[-1][1]
assert L7 == [(391, 299, 1, 92), (299, 92, 3, 23), (92, 23, 4, 0)] and Q7 == 23 == gcd(391, 299)
assert prime_factors(391) == [17, 23] and prime_factors(299) == [13, 23]
# q8, q9: 54 mango and 72 guava trees in rows of one kind, all rows the same length
Q8 = gcd(54, 72)
Q9 = 54 // Q8 + 72 // Q8
assert Q8 == 18 and Q9 == 3 + 4 == 7 and lcm(54, 72) == 216
# q10, q11: 84 red and 126 blue pencils in identical packs
Q10 = gcd(84, 126)
Q11 = 84 // Q10 + 126 // Q10
assert Q10 == 42 and Q11 == 2 + 3 == 5 and lcm(84, 126) == 252 and 84 + 126 == 210
# q12: floor 360 cm by 450 cm, largest square tile
Q12 = gcd(360, 450)
assert Q12 == 90 and (360 // Q12) * (450 // Q12) == 4 * 5 == 20 and lcm(360, 450) == 1800
# find error: 80 and 112, stops at the first remainder
FE = long_division(112, 80)
assert FE == [(112, 80, 1, 32), (80, 32, 2, 16), (32, 16, 2, 0)] and gcd(80, 112) == 16
# question bank
QB_REC = gcd(27, 45)
assert QB_REC == 9 and lcm(27, 45) == 135
QB_L = long_division(252, 189)
QB_APP = QB_L[-1][1]
assert QB_L == [(252, 189, 1, 63), (189, 63, 3, 0)] and QB_APP == 63 == gcd(189, 252)
assert 2 * 2 * 2 * 3 == 24 and gcd(24, 40) == 8 and prime_factors(24) == [2, 2, 2, 3] and prime_factors(40) == [2, 2, 2, 5]
# review
R1 = gcd(48, 80)
assert R1 == 16 and lcm(48, 80) == 240
R2 = gcd(35, 56)
assert R2 == 7 and 35 // R2 + 56 // R2 == 13


lesson = practice_lesson(
 "1.3", script="exercise_1_3.py",
 title=T("Exercise 1.3 practice: HCF", "مشق 1.3 کی پریکٹس: عاد اعظم"),
 outcome="Find the HCF of two or three numbers by prime factorisation and by the long division method, and use it to solve problems about equal rows, packs and tiles.",
 prerequisites=[FM_HCF, FM_PRIMES, FM_WORD_PROBLEMS],
 misconceptions=[
   {"id": "hcf_lcm_swap", "description": "Gives a common multiple (often the LCM) instead of the HCF."},
   {"id": "not_highest", "description": "Gives a common factor that is not the highest."},
   {"id": "all_primes", "description": "Multiplies all the prime factors of both numbers instead of only the shared ones."},
   {"id": "first_remainder", "description": "In the long division method, stops at the first remainder instead of dividing until the remainder is 0."},
   {"id": "stops_early", "description": "Finds the HCF but does not answer the question asked (number of rows, pencils in a pack, number of tiles)."},
 ],
 steps=[
   practice_intro("1.3",
     "Here you find the HCF by prime factorisation and by long division, then solve problems about rows, packs and tiles.",
     "اس میں آپ مفرد اجزائے ضربی اور لمبی تقسیم سے عاد اعظم معلوم کریں گے، پھر قطاروں، پیکٹوں اور ٹائلوں کے سوال حل کریں گے۔",
     "Exercise 1.3 is about the HCF. Remember: the highest number that divides both!",
     "مشق 1.3 عاد اعظم کے بارے میں ہے۔ یاد رکھیں: سب سے بڑا عدد جو دونوں کو تقسیم کرے!"),
   number_question(
     "q1_listing",
     T("Find the HCF of 16 and 40.", "16 اور 40 کا عاد اعظم معلوم کریں۔"),
     Q1,
     T("List the factors of 16. Which is the biggest one that also divides 40?", "16 کے اجزائے ضربی لکھیں۔ ان میں سب سے بڑا کون سا ہے جو 40 کو بھی تقسیم کرے؟"),
     T("Right! HCF = 8.", "درست! عاد اعظم = 8"),
     T("Factors of 16: 1, 2, 4, 8, 16. 16 does not divide 40, but 8 does. HCF = 8.", "16 کے اجزائے ضربی: 1، 2، 4، 8، 16۔ 16، 40 کو تقسیم نہیں کرتا، مگر 8 کرتا ہے۔ عاد اعظم = 8"),
     common_wrong=[wrong(80, "80 is the LCM. The HCF divides both numbers, so it can't be bigger than 16.", "80 ذو اضعاف اقل ہے۔ عاد اعظم دونوں اعداد کو تقسیم کرتا ہے، اس لیے 16 سے بڑا نہیں ہو سکتا۔", "hcf_lcm_swap"),
                   wrong(4, "4 is a common factor, but 8 is higher.", "4 مشترک جزو ضربی ہے، مگر 8 بڑا ہے۔", "not_highest")],
     qtype="recall"),
   choice_question(
     "q2_shared_primes",
     T("60 = 2 × 2 × 3 × 5 and 84 = 2 × 2 × 3 × 7. What is their HCF?", "60 = 2 × 2 × 3 × 5 اور 84 = 2 × 2 × 3 × 7۔ ان کا عاد اعظم کیا ہے؟"),
     [opt("n12", "12", "12", True, "Yes! The shared primes are 2, 2 and 3: 2 × 2 × 3 = 12.", "جی ہاں! مشترک مفرد اعداد 2، 2 اور 3 ہیں: 2 × 2 × 3 = 12"),
      opt("n420", "420", "420", False, "420 = 2 × 2 × 3 × 5 × 7 uses every prime: that is the LCM. Take only the shared ones.", "420 = 2 × 2 × 3 × 5 × 7 میں سب مفرد اعداد ہیں: یہ ذو اضعاف اقل ہے۔ صرف مشترک لیں۔", "all_primes"),
      opt("n4", "4", "4", False, "4 = 2 × 2 is a common factor, but 3 is shared too: 2 × 2 × 3 = 12.", "4 = 2 × 2 مشترک جزو ضربی ہے، مگر 3 بھی مشترک ہے: 2 × 2 × 3 = 12", "not_highest"),
      opt("n35", "35", "35", False, "5 and 7 are the primes that are NOT shared. Multiply the shared ones: 2 × 2 × 3 = 12.", "5 اور 7 وہ مفرد اعداد ہیں جو مشترک نہیں۔ مشترک کو ضرب دیں: 2 × 2 × 3 = 12")],
     qtype="recall"),
   number_question(
     "q3_primes",
     T("Find the HCF of 72 and 108 by prime factorisation.", "مفرد اجزائے ضربی سے 72 اور 108 کا عاد اعظم معلوم کریں۔"),
     Q3,
     T("72 = 2 × 2 × 2 × 3 × 3 and 108 = 2 × 2 × 3 × 3 × 3. Which primes do they share?", "72 = 2 × 2 × 2 × 3 × 3 اور 108 = 2 × 2 × 3 × 3 × 3۔ کون سے مفرد اعداد مشترک ہیں؟"),
     T("Right! Shared: 2 × 2 × 3 × 3 = 36.", "درست! مشترک: 2 × 2 × 3 × 3 = 36"),
     T("Both have two 2s and two 3s: HCF = 2 × 2 × 3 × 3 = 36.", "دونوں میں دو 2 اور دو 3 ہیں: عاد اعظم = 2 × 2 × 3 × 3 = 36"),
     common_wrong=[wrong(216, "216 is the LCM. The HCF uses only the shared primes: 36.", "216 ذو اضعاف اقل ہے۔ عاد اعظم میں صرف مشترک مفرد اعداد آتے ہیں: 36", "hcf_lcm_swap"),
                   wrong(12, "12 divides both, but 36 is higher. Both share two 3s, not one.", "12 دونوں کو تقسیم کرتا ہے، مگر 36 بڑا ہے۔ دونوں میں دو 3 مشترک ہیں، ایک نہیں۔", "not_highest")]),
   number_question(
     "q4_three",
     T("Find the HCF of 24, 36 and 60.", "24، 36 اور 60 کا عاد اعظم معلوم کریں۔"),
     Q4,
     T("24 = 2 × 2 × 2 × 3, 36 = 2 × 2 × 3 × 3, 60 = 2 × 2 × 3 × 5. Which primes are in all three?", "24 = 2 × 2 × 2 × 3، 36 = 2 × 2 × 3 × 3، 60 = 2 × 2 × 3 × 5۔ کون سے مفرد اعداد تینوں میں ہیں؟"),
     T("Right! All three share 2 × 2 × 3 = 12.", "درست! تینوں میں 2 × 2 × 3 = 12 مشترک ہے۔"),
     T("All three have two 2s and one 3, so HCF = 2 × 2 × 3 = 12.", "تینوں میں دو 2 اور ایک 3 ہے، اس لیے عاد اعظم = 2 × 2 × 3 = 12"),
     common_wrong=[wrong(360, "360 is the LCM. The HCF divides all three, so it is no bigger than 24.", "360 ذو اضعاف اقل ہے۔ عاد اعظم تینوں کو تقسیم کرتا ہے، اس لیے 24 سے بڑا نہیں۔", "hcf_lcm_swap"),
                   wrong(6, "6 divides all three, but 12 is higher.", "6 تینوں کو تقسیم کرتا ہے، مگر 12 بڑا ہے۔", "not_highest")]),
   {"id": "s_long", "type": "explain",
    "character": say("talking", "Now the book's second way: the long division method. It is quick for big numbers.",
                     "اب کتاب کا دوسرا طریقہ: لمبی تقسیم کا طریقہ۔ بڑے اعداد کے لیے یہ جلدی ہوتا ہے۔"),
    "text": T(f"Long division method: divide the bigger number by the smaller. Then divide the last divisor by the remainder. Keep going until the remainder is 0. The last divisor is the HCF. For 45 and 75: {steps_en(EX)}. So the HCF is 15.",
              f"لمبی تقسیم کا طریقہ: بڑے عدد کو چھوٹے سے تقسیم کریں۔ پھر پچھلے مقسوم علیہ کو باقی سے تقسیم کریں۔ یہ تب تک کریں جب تک باقی 0 نہ ہو جائے۔ آخری مقسوم علیہ عاد اعظم ہے۔ 45 اور 75 کے لیے: {steps_ur(EX)}۔ اس لیے عاد اعظم 15 ہے۔")},
   number_question(
     "q5_first_remainder",
     T("Use long division to find the HCF of 156 and 204. First step: 204 ÷ 156 = 1 remainder ?. What is the remainder?", "لمبی تقسیم سے 156 اور 204 کا عاد اعظم معلوم کریں۔ پہلا قدم: 204 ÷ 156 = 1 باقی ?۔ باقی کیا ہے؟"),
     Q5,
     T("156 goes into 204 once. What is left over? 204 − 156.", "156، 204 میں ایک بار جاتا ہے۔ کتنا بچا؟ 204 − 156"),
     T("Right! 204 − 156 = 48.", "درست! 204 − 156 = 48"),
     T("204 − 156 × 1 = 48, so the remainder is 48.", "204 − 156 × 1 = 48، اس لیے باقی 48 ہے۔"),
     common_wrong=[wrong(156, "156 is the divisor. The remainder is what is left: 204 − 156 = 48.", "156 مقسوم علیہ ہے۔ باقی وہ ہے جو بچ جائے: 204 − 156 = 48")]),
   number_question(
     "q6_finish",
     T("Now carry on: divide 156 by 48, then the divisor by the new remainder, until the remainder is 0. What is the HCF of 156 and 204?", "اب آگے کریں: 156 کو 48 سے تقسیم کریں، پھر مقسوم علیہ کو نئے باقی سے، یہاں تک کہ باقی 0 ہو جائے۔ 156 اور 204 کا عاد اعظم کیا ہے؟"),
     Q6,
     T("156 ÷ 48 = 3 remainder 12. Now divide 48 by 12.", "156 ÷ 48 = 3 باقی 12۔ اب 48 کو 12 سے تقسیم کریں۔"),
     T("Right! 48 ÷ 12 = 4 remainder 0, so the HCF is 12.", "درست! 48 ÷ 12 = 4 باقی 0، اس لیے عاد اعظم 12 ہے۔"),
     T(f"{steps_en(L5)}. The last divisor is 12, so the HCF is 12.", f"{steps_ur(L5)}۔ آخری مقسوم علیہ 12 ہے، اس لیے عاد اعظم 12 ہے۔"),
     common_wrong=[wrong(48, "48 is only the first remainder. Keep dividing until the remainder is 0: the HCF is 12.", "48 صرف پہلا باقی ہے۔ باقی 0 ہونے تک تقسیم کرتے رہیں: عاد اعظم 12 ہے۔", "first_remainder"),
                   wrong(3, "3 is a quotient. The HCF is the last divisor: 12.", "3 خارج قسمت ہے۔ عاد اعظم آخری مقسوم علیہ ہے: 12")]),
   number_question(
     "q7_long_3digit",
     T("Find the HCF of 299 and 391 by the long division method.", "لمبی تقسیم کے طریقے سے 299 اور 391 کا عاد اعظم معلوم کریں۔"),
     Q7,
     T("391 ÷ 299 = 1 remainder 92. Then divide 299 by 92.", "391 ÷ 299 = 1 باقی 92۔ پھر 299 کو 92 سے تقسیم کریں۔"),
     T("Right! HCF = 23.", "درست! عاد اعظم = 23"),
     T(f"{steps_en(L7)}. The last divisor is 23.", f"{steps_ur(L7)}۔ آخری مقسوم علیہ 23 ہے۔"),
     common_wrong=[wrong(92, "92 is the first remainder. Keep going: 299 ÷ 92 leaves 23, and 92 ÷ 23 leaves 0.", "92 پہلا باقی ہے۔ آگے کریں: 299 ÷ 92 سے 23 بچتا ہے، اور 92 ÷ 23 سے 0", "first_remainder"),
                   wrong(1, "299 and 391 do share a factor. Keep dividing: the HCF is 23.", "299 اور 391 کا ایک مشترک جزو ضربی ہے۔ تقسیم کرتے رہیں: عاد اعظم 23 ہے۔")]),
   number_question(
     "q8_rows",
     T("A gardener plants 54 mango trees and 72 guava trees in rows. Each row has only one kind of tree, and all rows have the same number of trees. What is the largest number of trees in a row?", "ایک مالی 54 آم اور 72 امرود کے درخت قطاروں میں لگاتا ہے۔ ہر قطار میں صرف ایک قسم کے درخت ہیں، اور سب قطاروں میں درخت برابر ہیں۔ ایک قطار میں زیادہ سے زیادہ کتنے درخت ہو سکتے ہیں؟"),
     Q8,
     T("The number in a row must divide 54 and 72. Find the HCF.", "ایک قطار کی تعداد 54 اور 72 دونوں کو تقسیم کرے۔ عاد اعظم معلوم کریں۔"),
     T("Right! HCF of 54 and 72 = 18.", "درست! 54 اور 72 کا عاد اعظم = 18"),
     T("54 = 2 × 3 × 3 × 3 and 72 = 2 × 2 × 2 × 3 × 3. Shared: 2 × 3 × 3 = 18.", "54 = 2 × 3 × 3 × 3 اور 72 = 2 × 2 × 2 × 3 × 3۔ مشترک: 2 × 3 × 3 = 18"),
     common_wrong=[wrong(216, "216 is the LCM. A row can't have more trees than the gardener has. Use the HCF: 18.", "216 ذو اضعاف اقل ہے۔ قطار میں مالی کے درختوں سے زیادہ نہیں ہو سکتے۔ عاد اعظم لیں: 18", "hcf_lcm_swap"),
                   wrong(9, "Rows of 9 work, but rows of 18 are longer.", "9 کی قطاریں بن سکتی ہیں، مگر 18 کی قطاریں لمبی ہیں۔", "not_highest")]),
   number_question(
     "q9_how_many_rows",
     T("With 18 trees in each row, how many rows are there altogether?", "ہر قطار میں 18 درخت ہوں تو کل کتنی قطاریں ہوں گی؟"),
     Q9,
     T("Mango rows: 54 ÷ 18. Guava rows: 72 ÷ 18. Add them.", "آم کی قطاریں: 54 ÷ 18۔ امرود کی قطاریں: 72 ÷ 18۔ دونوں جمع کریں۔"),
     T("Right! 3 mango rows and 4 guava rows make 7.", "درست! آم کی 3 اور امرود کی 4 قطاریں، کل 7"),
     T("54 ÷ 18 = 3 and 72 ÷ 18 = 4, so 3 + 4 = 7 rows.", "54 ÷ 18 = 3 اور 72 ÷ 18 = 4، اس لیے 3 + 4 = 7 قطاریں۔"),
     common_wrong=[wrong(18, "18 is the number of trees in a row. Count the rows: 3 + 4 = 7.", "18 ایک قطار کے درخت ہیں۔ قطاریں گنیں: 3 + 4 = 7", "stops_early"),
                   wrong(4, "That is only the guava rows. Add the 3 mango rows: 7.", "یہ صرف امرود کی قطاریں ہیں۔ آم کی 3 قطاریں جمع کریں: 7")]),
   number_question(
     "q10_packs",
     T("A shopkeeper has 84 red pencils and 126 blue pencils. He makes identical packs, each with both colours, and no pencil is left over. What is the greatest number of packs he can make?", "ایک دکاندار کے پاس 84 سرخ اور 126 نیلی پنسلیں ہیں۔ وہ ایک جیسے پیکٹ بناتا ہے جن میں دونوں رنگ ہوں، اور کوئی پنسل نہ بچے۔ زیادہ سے زیادہ کتنے پیکٹ بن سکتے ہیں؟"),
     Q10,
     T("The number of packs must divide 84 and 126. Try the long division method.", "پیکٹوں کی تعداد 84 اور 126 دونوں کو تقسیم کرے۔ لمبی تقسیم کا طریقہ آزمائیں۔"),
     T("Right! HCF = 42 packs.", "درست! عاد اعظم = 42 پیکٹ"),
     T(f"{steps_en(long_division(126, 84))}. HCF = 42, so 42 packs.", f"{steps_ur(long_division(126, 84))}۔ عاد اعظم = 42، اس لیے 42 پیکٹ۔"),
     common_wrong=[wrong(252, "252 is the LCM. There are only 210 pencils, so there can't be 252 packs. Use the HCF: 42.", "252 ذو اضعاف اقل ہے۔ کل 210 پنسلیں ہیں، اس لیے 252 پیکٹ نہیں بن سکتے۔ عاد اعظم لیں: 42", "hcf_lcm_swap"),
                   wrong(21, "21 packs work, but 42 is more.", "21 پیکٹ بن سکتے ہیں، مگر 42 زیادہ ہیں۔", "not_highest")]),
   number_question(
     "q11_pencils_in_pack",
     T("With 42 packs, how many pencils are in each pack?", "42 پیکٹ ہوں تو ہر پیکٹ میں کتنی پنسلیں ہوں گی؟"),
     Q11,
     T("Red in a pack: 84 ÷ 42. Blue in a pack: 126 ÷ 42.", "ایک پیکٹ میں سرخ: 84 ÷ 42۔ نیلی: 126 ÷ 42"),
     T("Right! 2 red + 3 blue = 5 pencils.", "درست! 2 سرخ + 3 نیلی = 5 پنسلیں"),
     T("84 ÷ 42 = 2 red and 126 ÷ 42 = 3 blue, so 5 pencils in each pack.", "84 ÷ 42 = 2 سرخ اور 126 ÷ 42 = 3 نیلی، اس لیے ہر پیکٹ میں 5 پنسلیں۔"),
     common_wrong=[wrong(42, "42 is the number of packs. In each pack: 2 red and 3 blue, so 5.", "42 پیکٹوں کی تعداد ہے۔ ہر پیکٹ میں: 2 سرخ اور 3 نیلی، یعنی 5", "stops_early"),
                   wrong(2, "That is only the red pencils. Add the 3 blue ones: 5.", "یہ صرف سرخ پنسلیں ہیں۔ 3 نیلی جمع کریں: 5")]),
   number_question(
     "q12_tiles",
     T("A floor is 360 cm wide and 450 cm long. It is covered with equal square tiles, with no cutting. What is the side of the largest tile that can be used, in cm?", "ایک فرش 360 سینٹی میٹر چوڑا اور 450 سینٹی میٹر لمبا ہے۔ اسے برابر مربع ٹائلوں سے ڈھانپا جاتا ہے، کوئی ٹائل کاٹی نہیں جاتی۔ سب سے بڑی ٹائل کا ضلع کتنے سینٹی میٹر ہو سکتا ہے؟"),
     Q12,
     T("The tile's side must divide 360 and 450 exactly. Find the HCF.", "ٹائل کا ضلع 360 اور 450 دونوں کو پورا تقسیم کرے۔ عاد اعظم معلوم کریں۔"),
     T("Right! 90 cm tiles: 4 across and 5 along, 20 tiles in all.", "درست! 90 سینٹی میٹر کی ٹائلیں: چوڑائی میں 4 اور لمبائی میں 5، کل 20 ٹائلیں۔"),
     T(f"{steps_en(long_division(450, 360))}. HCF = 90, so the tiles are 90 cm.", f"{steps_ur(long_division(450, 360))}۔ عاد اعظم = 90، اس لیے ٹائلیں 90 سینٹی میٹر کی ہیں۔"),
     common_wrong=[wrong(1800, "1800 is the LCM, bigger than the floor! The tile must fit into both sides: HCF = 90.", "1800 ذو اضعاف اقل ہے، فرش سے بھی بڑا! ٹائل دونوں اضلاع میں پوری آئے: عاد اعظم = 90", "hcf_lcm_swap"),
                   wrong(45, "45 cm tiles fit, but 90 cm tiles are bigger.", "45 سینٹی میٹر کی ٹائلیں آ جاتی ہیں، مگر 90 سینٹی میٹر کی بڑی ہیں۔", "not_highest")]),
   choice_question(
     "q13_find_error",
     T("Mehak finds the HCF of 80 and 112 by long division. She writes 112 ÷ 80 = 1 remainder 32 and says the HCF is 32. What went wrong?", "مہک لمبی تقسیم سے 80 اور 112 کا عاد اعظم معلوم کرتی ہے۔ وہ لکھتی ہے 112 ÷ 80 = 1 باقی 32 اور کہتی ہے عاد اعظم 32 ہے۔ کیا غلطی ہوئی؟"),
     [opt("keep_going", "She stopped too early. 80 ÷ 32 = 2 remainder 16, then 32 ÷ 16 = 2 remainder 0, so the HCF is 16.", "وہ جلدی رک گئی۔ 80 ÷ 32 = 2 باقی 16، پھر 32 ÷ 16 = 2 باقی 0، اس لیے عاد اعظم 16 ہے۔", True,
          "Yes! Keep dividing until the remainder is 0. 32 does not even divide 80.", "جی ہاں! باقی 0 ہونے تک تقسیم کرتے رہیں۔ 32 تو 80 کو تقسیم بھی نہیں کرتا۔"),
      opt("quotient", "The HCF is the quotient, 1.", "عاد اعظم خارج قسمت ہے، یعنی 1", False,
          "The quotient is not the HCF. Keep dividing until the remainder is 0; the last divisor, 16, is the HCF.", "خارج قسمت عاد اعظم نہیں۔ باقی 0 ہونے تک تقسیم کریں؛ آخری مقسوم علیہ، 16، عاد اعظم ہے۔"),
      opt("nothing", "Nothing. The HCF is 32.", "کوئی غلطی نہیں۔ عاد اعظم 32 ہے۔", False,
          "80 ÷ 32 is not exact, so 32 can't be the HCF. Carry on: the HCF is 16.", "80 ÷ 32 پورا تقسیم نہیں ہوتا، اس لیے 32 عاد اعظم نہیں ہو سکتا۔ آگے کریں: عاد اعظم 16 ہے۔", "first_remainder")],
     qtype="find_error"),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! You know two ways to find the HCF now.", "شاباش! اب آپ عاد اعظم معلوم کرنے کے دو طریقے جانتے ہیں۔"),
    "text": T("HCF by prime factorisation: multiply the primes the numbers share. HCF by long division: divide, then divide the divisor by the remainder, until the remainder is 0; the last divisor is the HCF. In word problems, the HCF gives the largest equal rows, packs or tiles.",
              "مفرد اجزائے ضربی سے عاد اعظم: جو مفرد اعداد مشترک ہوں انہیں ضرب دیں۔ لمبی تقسیم سے عاد اعظم: تقسیم کریں، پھر مقسوم علیہ کو باقی سے تقسیم کریں، یہاں تک کہ باقی 0 ہو؛ آخری مقسوم علیہ عاد اعظم ہے۔ سوالات میں عاد اعظم سب سے بڑی برابر قطاریں، پیکٹ یا ٹائلیں بتاتا ہے۔"),
    "points": [T("The HCF is never bigger than the smallest number.", "عاد اعظم سب سے چھوٹے عدد سے بڑا نہیں ہوتا۔"),
               T("After finding the HCF, answer the question asked: how many rows, pencils or tiles.", "عاد اعظم نکالنے کے بعد اصل سوال کا جواب دیں: کتنی قطاریں، پنسلیں یا ٹائلیں۔")]},
 ],
 bank=[
   {"id": "qb_hcf", "type": "recall", "step": number_question(
     "qb_hcf",
     T("Find the HCF of 27 and 45.", "27 اور 45 کا عاد اعظم معلوم کریں۔"),
     QB_REC,
     T("27 = 3 × 3 × 3 and 45 = 3 × 3 × 5.", "27 = 3 × 3 × 3 اور 45 = 3 × 3 × 5"),
     T("Right! Shared: 3 × 3 = 9.", "درست! مشترک: 3 × 3 = 9"),
     T("Both share two 3s: HCF = 9.", "دونوں میں دو 3 مشترک ہیں: عاد اعظم = 9"),
     common_wrong=[wrong(135, "135 is the LCM. Take only the shared primes: 9.", "135 ذو اضعاف اقل ہے۔ صرف مشترک مفرد اعداد لیں: 9", "hcf_lcm_swap"),
                   wrong(3, "3 is a common factor, but 9 is higher.", "3 مشترک جزو ضربی ہے، مگر 9 بڑا ہے۔", "not_highest")],
     qtype=None)},
   {"id": "qb_long", "type": "apply", "step": number_question(
     "qb_long",
     T("Find the HCF of 189 and 252 by the long division method.", "لمبی تقسیم کے طریقے سے 189 اور 252 کا عاد اعظم معلوم کریں۔"),
     QB_APP,
     T("252 ÷ 189 = 1 remainder 63. Now divide 189 by 63.", "252 ÷ 189 = 1 باقی 63۔ اب 189 کو 63 سے تقسیم کریں۔"),
     T("Right! 189 ÷ 63 = 3 remainder 0, so the HCF is 63.", "درست! 189 ÷ 63 = 3 باقی 0، اس لیے عاد اعظم 63 ہے۔"),
     T(f"{steps_en(QB_L)}. The last divisor is 63.", f"{steps_ur(QB_L)}۔ آخری مقسوم علیہ 63 ہے۔"),
     common_wrong=[wrong(3, "3 is the quotient. The HCF is the last divisor: 63.", "3 خارج قسمت ہے۔ عاد اعظم آخری مقسوم علیہ ہے: 63")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": choice_question(
     "qb_find_error",
     T("24 = 2 × 2 × 2 × 3 and 40 = 2 × 2 × 2 × 5. Danish says the HCF is 2 × 2 × 2 × 3 × 5 = 120. What went wrong?", "24 = 2 × 2 × 2 × 3 اور 40 = 2 × 2 × 2 × 5۔ دانش کہتا ہے عاد اعظم 2 × 2 × 2 × 3 × 5 = 120 ہے۔ کیا غلطی ہوئی؟"),
     [opt("shared_only", "He used every prime. Only the shared ones count: 2 × 2 × 2 = 8.", "اس نے سب مفرد اعداد لے لیے۔ صرف مشترک گنے جاتے ہیں: 2 × 2 × 2 = 8", True,
          "Yes! 120 is the LCM. The HCF is 8.", "جی ہاں! 120 ذو اضعاف اقل ہے۔ عاد اعظم 8 ہے۔"),
      opt("add", "He should add the primes.", "اسے مفرد اعداد جمع کرنے تھے۔", False,
          "We multiply primes, but only the shared ones: 2 × 2 × 2 = 8.", "ہم مفرد اعداد ضرب دیتے ہیں، مگر صرف مشترک: 2 × 2 × 2 = 8"),
      opt("nothing", "Nothing. The HCF is 120.", "کوئی غلطی نہیں۔ عاد اعظم 120 ہے۔", False,
          "120 is bigger than 24 and 40, so it can't divide them. The HCF is 8.", "120، 24 اور 40 سے بڑا ہے، اس لیے انہیں تقسیم نہیں کر سکتا۔ عاد اعظم 8 ہے۔", "all_primes")],
     qtype=None)},
 ],
 review=[
   {"id": "r_hcf", "type": "recall", "step": number_question(
     "r_hcf",
     T("Find the HCF of 48 and 80.", "48 اور 80 کا عاد اعظم معلوم کریں۔"),
     R1,
     T("48 = 2⁴ × 3 and 80 = 2⁴ × 5.", "48 = 2⁴ × 3 اور 80 = 2⁴ × 5"),
     T("Right! HCF = 2⁴ = 16.", "درست! عاد اعظم = 2⁴ = 16"),
     T("Both share four 2s: 2 × 2 × 2 × 2 = 16.", "دونوں میں چار 2 مشترک ہیں: 2 × 2 × 2 × 2 = 16"),
     common_wrong=[wrong(240, "240 is the LCM. The HCF is 16.", "240 ذو اضعاف اقل ہے۔ عاد اعظم 16 ہے۔", "hcf_lcm_swap"),
                   wrong(8, "8 divides both, but 16 is higher.", "8 دونوں کو تقسیم کرتا ہے، مگر 16 بڑا ہے۔", "not_highest")],
     qtype=None)},
   {"id": "r_rows", "type": "apply", "step": number_question(
     "r_rows",
     T("35 boys and 56 girls stand in rows of the same length, each row only boys or only girls. What is the longest a row can be?", "35 لڑکے اور 56 لڑکیاں برابر لمبائی کی قطاروں میں کھڑے ہیں، ہر قطار میں صرف لڑکے یا صرف لڑکیاں۔ ایک قطار زیادہ سے زیادہ کتنی لمبی ہو سکتی ہے؟"),
     R2,
     T("Find the HCF of 35 and 56.", "35 اور 56 کا عاد اعظم معلوم کریں۔"),
     T("Right! Rows of 7: 5 rows of boys and 8 of girls.", "درست! 7 کی قطاریں: لڑکوں کی 5 اور لڑکیوں کی 8"),
     T("35 = 5 × 7 and 56 = 8 × 7, so the HCF is 7.", "35 = 5 × 7 اور 56 = 8 × 7، اس لیے عاد اعظم 7 ہے۔"),
     common_wrong=[wrong(280, "280 is the LCM. A row can't be longer than 35. Use the HCF: 7.", "280 ذو اضعاف اقل ہے۔ قطار 35 سے لمبی نہیں ہو سکتی۔ عاد اعظم لیں: 7", "hcf_lcm_swap")],
     qtype=None)},
 ],
 glossary=[T("Highest common factor (HCF)", "عاد اعظم"), T("Long division method", "لمبی تقسیم کا طریقہ"),
           T("Remainder", "باقی"), T("Divisor", "مقسوم علیہ"), T("Quotient", "خارج قسمت")],
 flashcards=[
   {"id": "f_long", "front": T("How does the long division method find the HCF?", "لمبی تقسیم کا طریقہ عاد اعظم کیسے معلوم کرتا ہے؟"),
    "back": T("Divide the bigger number by the smaller, then the divisor by the remainder, until the remainder is 0. The last divisor is the HCF.", "بڑے عدد کو چھوٹے سے تقسیم کریں، پھر مقسوم علیہ کو باقی سے، یہاں تک کہ باقی 0 ہو۔ آخری مقسوم علیہ عاد اعظم ہے۔")},
   {"id": "f_when_hcf", "front": T("Which word problems need the HCF?", "کن سوالات میں عاد اعظم چاہیے؟"),
    "back": T("Sharing or cutting into the LARGEST equal rows, packs, pieces or tiles with nothing left over.", "جب چیزوں کو سب سے بڑی برابر قطاروں، پیکٹوں، ٹکڑوں یا ٹائلوں میں بانٹنا ہو اور کچھ نہ بچے۔")},
 ],
 home_task={"id": "h_packs", "text": T(
   "Count two kinds of things at home, such as spoons and forks, or red and blue pens. What is the greatest number of identical sets you could make with nothing left over? Check your answer with the long division method.",
   "گھر میں دو قسم کی چیزیں گنیں، جیسے چمچ اور کانٹے، یا سرخ اور نیلے قلم۔ زیادہ سے زیادہ کتنے ایک جیسے سیٹ بن سکتے ہیں کہ کچھ نہ بچے؟ لمبی تقسیم کے طریقے سے اپنا جواب جانچیں۔")},
 notes=["Covers HCF by listing and prime factorisation (q1 to q4), the long division method (s_long, q5 to q7), and word problems about rows (q8, q9), packs (q10, q11) and tiles (q12).",
        "The long division method is not taught in the unit's HCF lesson, so s_long shows it once before q5.",
        "Urdu terms to check: لمبی تقسیم کا طریقہ (long division method), مقسوم علیہ (divisor), خارج قسمت (quotient), باقی (remainder)."],
 minutes=20,
)

attach(lesson, {
    "q2_shared_primes": venn(RA2, BOTH2, RB2, (60, 84),
        "Two overlapping circles for the prime factors. Left circle, 60: 2 × 2 × 3 × 5. Right circle, 84: 2 × 2 × 3 × 7. The shared primes 2, 2 and 3 are in the middle. Only in 60: 5. Only in 84: 7.",
        "مفرد اجزائے ضربی کے دو ایک دوسرے پر چڑھے دائرے۔ بائیں دائرہ، 60: 2 × 2 × 3 × 5۔ دائیں دائرہ، 84: 2 × 2 × 3 × 7۔ مشترک مفرد اعداد 2، 2 اور 3 درمیان میں ہیں۔ صرف 60 میں: 5۔ صرف 84 میں: 7۔"),
    "q10_packs": bars_figure([84, 126],
        "Two bars, one for the red pencils (84) and a longer one for the blue pencils (126), with the numbers written after them.",
        "دو پٹیاں، ایک سرخ پنسلوں کی (84) اور ایک لمبی نیلی پنسلوں کی (126)، ساتھ اعداد لکھے ہیں۔"),
    "q12_tiles": floor_figure(360, 450,
        "A rectangle for the floor, 450 across and 360 down, drawn to scale.",
        "فرش کا ایک مستطیل، 450 چوڑائی میں اور 360 اونچائی میں، پیمانے کے مطابق۔"),
})
write(lesson)
