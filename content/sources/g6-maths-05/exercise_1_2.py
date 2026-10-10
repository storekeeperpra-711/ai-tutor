"""Practice set for Exercise 1.2 of the book: complete factor trees, move
between expanded form and index notation, find prime factors by the
division and factor tree methods, and "who am I" puzzles. The questions are
new; only the kinds of question follow the book."""
from math import prod

from common import (T, opt, say, wrong, number_question, choice_question, practice_lesson,
                    practice_intro, write, is_prime, prime_factors, EX_SKILL, FM_PRIMES, FM_INDEX)
from figs import attach, tree_figure, tree_fig, ladder, division_ladder, ladder_rows

SKILL = EX_SKILL["1.2"]

SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")


def index_form(n):
    """180 -> '2² × 3² × 5' (an index of 1 is not written)."""
    ps = prime_factors(n)
    parts = []
    for p in sorted(set(ps)):
        k = ps.count(p)
        parts.append(str(p) + (str(k).translate(SUP) if k > 1 else ""))
    return " × ".join(parts)


def expanded(n):
    return " × ".join(str(p) for p in prime_factors(n))


# q1: factor tree for 126 with 63 = ? × 7
Q1 = 63 // 7
assert 126 == 2 * 63 and Q1 == 9 and Q1 == 3 * 3 and 63 - 7 == 56
T126 = (126, (2,), (63, ("?", (3,), (3,)), (7,)))
# q2: 5 × 5 × 5 × 5 = 5^?
Q2 = [5, 5, 5, 5].count(5)
assert Q2 == 4 and 5 ** Q2 == 625
# q3: 2 × 2 × 2 × 5 × 5 in index notation
assert index_form(2 * 2 * 2 * 5 * 5) == "2³ × 5²" and 2 ** 3 * 5 ** 2 == 200
assert 3 ** 2 * 2 ** 5 == 288 != 200 and 2 ** 2 * 5 ** 3 == 500 != 200 and 2 ** 3 + 5 ** 2 == 33
# q4: the value of 2⁴ × 3
Q4 = 2 ** 4 * 3
assert Q4 == 48 and 2 * 4 * 3 == 24
# q5: 7² × 11 in expanded form
assert 7 ** 2 * 11 == 7 * 7 * 11 == 539 and 7 * 2 * 11 == 154 and 7 * 11 * 11 == 847
# s_division: the division method for 150
D150 = [2, 3, 5, 5]
R150 = ladder_rows([150], D150)
assert R150 == [[150], [75], [25], [5], [1]] and prod(D150) == 150 and all(is_prime(d) for d in D150)
# q6: the division method for 156, last prime hidden
D156 = prime_factors(156)
R156 = ladder_rows([156], D156)
assert D156 == [2, 2, 3, 13] and R156 == [[156], [78], [39], [13], [1]]
Q6 = R156[3][0]
assert Q6 == 13 and is_prime(Q6) and 39 - 3 == 36
assert index_form(156) == "2² × 3 × 13"
# q7: 180 in index notation
assert index_form(180) == "2² × 3² × 5" and 2 ** 2 * 3 * 5 == 60 and 2 * 3 ** 2 * 5 == 90 and 4 * 9 * 5 == 180
# q8: 360 = 2³ × 3² × p
Q8 = 360 // (2 ** 3 * 3 ** 2)
assert Q8 == 5 and is_prime(Q8) and index_form(360) == "2³ × 3² × 5"
Q8_TIMES = 360 // ((2 * 3) * (3 * 2))
assert Q8_TIMES == 10
# q9: factor tree for 264 stopped at 33
T264 = ladder(264, stop=33)
assert T264 == (264, (2,), (132, (2,), (66, (2,), (33,))))
Q9 = max(prime_factors(264))
assert prime_factors(264) == [2, 2, 2, 3, 11] and Q9 == 11 and not is_prime(33)
# q10: between 40 and 50, prime factors only 2 and 3 (both used)
Q10_ALL = [n for n in range(41, 50) if set(prime_factors(n)) == {2, 3}]
assert Q10_ALL == [48]
Q10 = Q10_ALL[0]
assert index_form(Q10) == "2⁴ × 3" and index_form(42) == "2 × 3 × 7"
# q11: 2² × 7²
Q11 = 2 ** 2 * 7 ** 2
assert Q11 == 196 and 2 * 2 * 7 * 2 == 56 and 2 * 2 * 7 == 28
# q12: a prime factor of 91 bigger than 10
Q12_ALL = [p for p in set(prime_factors(91)) if p > 10]
assert prime_factors(91) == [7, 13] and Q12_ALL == [13]
Q12 = Q12_ALL[0]
# find error: 3 × 3 × 3 × 3 × 7 written as 4³ × 7
assert 3 ** 4 * 7 == 567 and 4 ** 3 * 7 == 448 and index_form(567) == "3⁴ × 7"
# question bank
assert index_form(98) == "2 × 7²"
QB = prime_factors(98).count(7)
assert QB == 2
assert 120 == 4 * 5 * 6 and not is_prime(4) and not is_prime(6) and index_form(120) == "2³ × 3 × 5"
# review
R1 = 2 ** 3 * 3 * 5
assert R1 == 120 and 2 * 3 * 3 * 5 == 90
assert 5 ** 3 == 125 and index_form(125) == "5³"


lesson = practice_lesson(
 "1.2", script="exercise_1_2.py",
 title=T("Exercise 1.2 practice: prime factors and index notation", "مشق 1.2 کی پریکٹس: مفرد اجزائے ضربی اور قوت کی شکل"),
 outcome="Complete factor trees, find prime factors by the division and factor tree methods, and move between expanded form and index notation.",
 prerequisites=[FM_PRIMES, FM_INDEX],
 misconceptions=[
   {"id": "stops_early", "description": "Stops a factor tree or the division method before every factor is prime: 264 = 2 × 2 × 2 × 33."},
   {"id": "not_prime_factors", "description": "Writes a product with composite numbers as the prime factorisation: 120 = 4 × 5 × 6."},
   {"id": "swap_base_index", "description": "Swaps the base and the index: writes 3 × 3 × 3 × 3 as 4³."},
   {"id": "times_index", "description": "Multiplies the base by the index: 2⁴ = 2 × 4."},
 ],
 steps=[
   practice_intro("1.2",
     "Here you complete factor trees, write numbers as products of primes, and change between expanded form (2 × 2 × 3) and index notation (2² × 3).",
     "اس میں آپ اجزائے ضربی کے درخت مکمل کریں گے، اعداد کو مفرد اعداد کے حاصل ضرب کی شکل میں لکھیں گے، اور پھیلی ہوئی شکل (2 × 2 × 3) اور قوت کی شکل (2² × 3) میں بدلیں گے۔",
     "Exercise 1.2 is all about prime factors. Let's break some numbers into primes!",
     "مشق 1.2 مفرد اجزائے ضربی کے بارے میں ہے۔ آئیں کچھ اعداد کو مفرد اعداد میں توڑیں!"),
   number_question(
     "q1_tree_gap",
     T("In this factor tree, 126 = 2 × 63, and 63 splits into ? and 7. What is the missing number?", "اس اجزائے ضربی کے درخت میں 126 = 2 × 63، اور 63 کے دو حصے ? اور 7 ہیں۔ غائب عدد کیا ہے؟"),
     Q1,
     T("? × 7 = 63. Which number times 7 makes 63?", "? × 7 = 63۔ کس عدد کو 7 سے ضرب دیں تو 63 بنتا ہے؟"),
     T("Right! 9 × 7 = 63, and 9 splits again into 3 × 3.", "درست! 9 × 7 = 63، اور 9 پھر 3 × 3 میں ٹوٹتا ہے۔"),
     T("63 ÷ 7 = 9. The tree also shows 9 = 3 × 3.", "63 ÷ 7 = 9۔ درخت یہ بھی دکھاتا ہے کہ 9 = 3 × 3"),
     common_wrong=[wrong(56, "That is 63 − 7. In a factor tree the two parts multiply: ? × 7 = 63.", "یہ 63 − 7 ہے۔ اجزائے ضربی کے درخت میں دونوں حصے ضرب ہوتے ہیں: ? × 7 = 63"),
                   wrong(3, "3 × 7 = 21, not 63. The missing number is 3 × 3 = 9.", "3 × 7 = 21، نہ کہ 63۔ غائب عدد 3 × 3 = 9 ہے۔")],
     qtype="recall"),
   number_question(
     "q2_index",
     T("Write 5 × 5 × 5 × 5 in index notation. 5 to the power of what?", "5 × 5 × 5 × 5 کو قوت کی شکل میں لکھیں۔ 5 کی قوت کیا ہوگی؟"),
     Q2,
     T("The index counts how many 5s are multiplied.", "قوت گنتی ہے کہ کتنے 5 ضرب ہو رہے ہیں۔"),
     T("Right! 5 × 5 × 5 × 5 = 5⁴.", "درست! 5 × 5 × 5 × 5 = 5⁴"),
     T("There are four 5s, so it is 5⁴.", "اس میں چار 5 ہیں، اس لیے یہ 5⁴ ہے۔"),
     common_wrong=[wrong(5, "5 is the base, the number being multiplied. Count how many 5s: 4.", "5 اساس ہے، یعنی جو عدد ضرب ہو رہا ہے۔ گنیں کتنے 5 ہیں: 4", "swap_base_index")],
     qtype="recall"),
   choice_question(
     "q3_to_index",
     T("Which shows 2 × 2 × 2 × 5 × 5 in index notation?", "کون سا 2 × 2 × 2 × 5 × 5 کو قوت کی شکل میں دکھاتا ہے؟"),
     [opt("right", "2³ × 5²", "2³ × 5²", True, "Yes! Three 2s and two 5s.", "جی ہاں! تین 2 اور دو 5"),
      opt("swap", "3² × 2⁵", "3² × 2⁵", False, "The base is the number multiplied and the index is how many times: three 2s is 2³.", "اساس وہ عدد ہے جو ضرب ہو رہا ہے اور قوت بتاتی ہے کتنی بار: تین 2 یعنی 2³", "swap_base_index"),
      opt("counts", "2² × 5³", "2² × 5³", False, "Count again: there are three 2s and two 5s, so 2³ × 5².", "دوبارہ گنیں: تین 2 اور دو 5 ہیں، اس لیے 2³ × 5²"),
      opt("plus", "2³ + 5²", "2³ + 5²", False, "The numbers are multiplied, so use ×, not +.", "اعداد ضرب ہو رہے ہیں، اس لیے × لگائیں، + نہیں۔")]),
   number_question(
     "q4_value",
     T("Write 2⁴ × 3 in expanded form and find its value.", "2⁴ × 3 کو پھیلی ہوئی شکل میں لکھیں اور اس کی قیمت معلوم کریں۔"),
     Q4,
     T("2⁴ = 2 × 2 × 2 × 2. Multiply that by 3.", "2⁴ = 2 × 2 × 2 × 2۔ اسے 3 سے ضرب دیں۔"),
     T("Right! 2 × 2 × 2 × 2 × 3 = 16 × 3 = 48.", "درست! 2 × 2 × 2 × 2 × 3 = 16 × 3 = 48"),
     T("2⁴ = 2 × 2 × 2 × 2 = 16, and 16 × 3 = 48.", "2⁴ = 2 × 2 × 2 × 2 = 16، اور 16 × 3 = 48"),
     common_wrong=[wrong(24, "2⁴ is not 2 × 4. It is 2 × 2 × 2 × 2 = 16, so 16 × 3 = 48.", "2⁴ کا مطلب 2 × 4 نہیں۔ یہ 2 × 2 × 2 × 2 = 16 ہے، اس لیے 16 × 3 = 48", "times_index")]),
   choice_question(
     "q5_to_expanded",
     T("Which shows 7² × 11 in expanded form?", "کون سا 7² × 11 کو پھیلی ہوئی شکل میں دکھاتا ہے؟"),
     [opt("right", "7 × 7 × 11", "7 × 7 × 11", True, "Yes! 7² means 7 × 7.", "جی ہاں! 7² کا مطلب 7 × 7 ہے۔"),
      opt("times", "7 × 2 × 11", "7 × 2 × 11", False, "7² is 7 × 7, not 7 × 2.", "7²، 7 × 7 ہے، 7 × 2 نہیں۔", "times_index"),
      opt("eleven", "7 × 11 × 11", "7 × 11 × 11", False, "The index 2 belongs to the 7, so there are two 7s and one 11.", "قوت 2، 7 کی ہے، اس لیے دو 7 اور ایک 11 ہے۔"),
      opt("swap", "2 × 2 × 11", "2 × 2 × 11", False, "The base is 7, so multiply 7 by itself: 7 × 7 × 11.", "اساس 7 ہے، اس لیے 7 کو خود سے ضرب دیں: 7 × 7 × 11", "swap_base_index")],
     qtype="recall"),
   {"id": "s_division", "type": "explain",
    "character": say("talking", "The book shows two ways to find prime factors. Here is the division method.",
                     "کتاب مفرد اجزائے ضربی معلوم کرنے کے دو طریقے بتاتی ہے۔ یہ تقسیم کا طریقہ ہے۔"),
    "text": T("Division method: divide by the smallest prime that goes in exactly, write the answer underneath, and keep going until you reach 1. For 150: ÷ 2 gives 75, ÷ 3 gives 25, ÷ 5 gives 5, ÷ 5 gives 1. The primes on the left are the prime factors: 150 = 2 × 3 × 5 × 5 = 2 × 3 × 5².",
              "تقسیم کا طریقہ: سب سے چھوٹے مفرد عدد سے تقسیم کریں جو پورا تقسیم کرے، جواب نیچے لکھیں، اور 1 تک پہنچنے تک یہی کرتے رہیں۔ 150 کے لیے: 2 سے تقسیم پر 75، 3 سے 25، 5 سے 5، اور 5 سے 1۔ بائیں طرف کے مفرد اعداد ہی مفرد اجزائے ضربی ہیں: 150 = 2 × 3 × 5 × 5 = 2 × 3 × 5²")},
   number_question(
     "q6_division",
     T("Finish the division method for 156: 156 ÷ 2 = 78, 78 ÷ 2 = 39, 39 ÷ 3 = ?. What number goes in the gap?", "156 کے لیے تقسیم کا طریقہ مکمل کریں: 156 ÷ 2 = 78، 78 ÷ 2 = 39، 39 ÷ 3 = ?۔ خالی جگہ میں کون سا عدد آئے گا؟"),
     Q6,
     T("Work out 39 ÷ 3.", "39 ÷ 3 کریں۔"),
     T(f"Right! 13 is prime, so the last step is ÷ 13. 156 = {index_form(156)}.", f"درست! 13 مفرد ہے، اس لیے آخری قدم 13 سے تقسیم ہے۔ 156 = {index_form(156)}"),
     T(f"39 ÷ 3 = 13, and 13 ÷ 13 = 1. So 156 = 2 × 2 × 3 × 13 = {index_form(156)}.", f"39 ÷ 3 = 13، اور 13 ÷ 13 = 1۔ اس لیے 156 = 2 × 2 × 3 × 13 = {index_form(156)}"),
     common_wrong=[wrong(36, "That is 39 − 3. Divide: 39 ÷ 3 = 13.", "یہ 39 − 3 ہے۔ تقسیم کریں: 39 ÷ 3 = 13")]),
   choice_question(
     "q7_index_180",
     T("Which is the prime factorisation of 180 in index notation?", "180 کے مفرد اجزائے ضربی قوت کی شکل میں کون سے ہیں؟"),
     [opt("right", "2² × 3² × 5", "2² × 3² × 5", True, "Yes! 180 = 2 × 2 × 3 × 3 × 5.", "جی ہاں! 180 = 2 × 2 × 3 × 3 × 5"),
      opt("sixty", "2² × 3 × 5", "2² × 3 × 5", False, "That is 4 × 3 × 5 = 60. One 3 is missing.", "یہ 4 × 3 × 5 = 60 ہے۔ ایک 3 رہ گیا ہے۔"),
      opt("ninety", "2 × 3² × 5", "2 × 3² × 5", False, "That is 2 × 9 × 5 = 90. One 2 is missing.", "یہ 2 × 9 × 5 = 90 ہے۔ ایک 2 رہ گیا ہے۔"),
      opt("composite", "4 × 9 × 5", "4 × 9 × 5", False, "4 × 9 × 5 is 180, but 4 and 9 are not prime. Break them: 2² × 3² × 5.", "4 × 9 × 5 = 180 ہے، مگر 4 اور 9 مفرد نہیں۔ انہیں توڑیں: 2² × 3² × 5", "not_prime_factors")]),
   number_question(
     "q8_missing_prime",
     T("360 = 2³ × 3² × p, where p is a prime. Find p.", "360 = 2³ × 3² × p، جہاں p مفرد عدد ہے۔ p معلوم کریں۔"),
     Q8,
     T("2³ × 3² = 8 × 9 = 72. Divide 360 by 72.", "2³ × 3² = 8 × 9 = 72۔ 360 کو 72 سے تقسیم کریں۔"),
     T("Right! 360 ÷ 72 = 5, so 360 = 2³ × 3² × 5.", "درست! 360 ÷ 72 = 5، اس لیے 360 = 2³ × 3² × 5"),
     T("2³ = 8 and 3² = 9, so 8 × 9 = 72 and 360 ÷ 72 = 5.", "2³ = 8 اور 3² = 9، اس لیے 8 × 9 = 72 اور 360 ÷ 72 = 5"),
     common_wrong=[wrong(Q8_TIMES, "2³ is 8 (not 6) and 3² is 9 (not 6). 360 ÷ 72 = 5.", "2³ = 8 ہے (6 نہیں) اور 3² = 9 ہے (6 نہیں)۔ 360 ÷ 72 = 5", "times_index")]),
   number_question(
     "q9_tree_264",
     T("Mehwish starts a factor tree for 264: 264 = 2 × 132, 132 = 2 × 66, 66 = 2 × 33. Finish it. What is the biggest prime factor of 264?", "مہوش 264 کا اجزائے ضربی کا درخت شروع کرتی ہے: 264 = 2 × 132، 132 = 2 × 66، 66 = 2 × 33۔ اسے مکمل کریں۔ 264 کا سب سے بڑا مفرد جزو ضربی کیا ہے؟"),
     Q9,
     T("33 is not prime yet. Split it into two factors.", "33 ابھی مفرد نہیں۔ اسے دو اجزائے ضربی میں توڑیں۔"),
     T(f"Right! 33 = 3 × 11, so 264 = {index_form(264)}.", f"درست! 33 = 3 × 11، اس لیے 264 = {index_form(264)}"),
     T(f"33 = 3 × 11, and both are prime. So 264 = {expanded(264)} = {index_form(264)}, and the biggest prime factor is 11.", f"33 = 3 × 11، اور دونوں مفرد ہیں۔ اس لیے 264 = {expanded(264)} = {index_form(264)}، اور سب سے بڑا مفرد جزو ضربی 11 ہے۔"),
     common_wrong=[wrong(33, "33 = 3 × 11, so it is not prime. Keep splitting.", "33 = 3 × 11، اس لیے یہ مفرد نہیں۔ توڑتے رہیں۔", "stops_early"),
                   wrong(132, "132 is a factor of 264, but it is not prime.", "132، 264 کا جزو ضربی ہے، مگر مفرد نہیں۔", "stops_early")]),
   number_question(
     "q10_who_am_i",
     T("Who am I? I am between 40 and 50. My only prime factors are 2 and 3, and I need both of them.", "میں کون ہوں؟ میں 40 اور 50 کے درمیان ہوں۔ میرے مفرد اجزائے ضربی صرف 2 اور 3 ہیں، اور دونوں چاہییں۔"),
     Q10,
     T("Try the numbers 41 to 49 one by one. Break each into primes.", "41 سے 49 تک کے اعداد ایک ایک کر کے آزمائیں۔ ہر ایک کو مفرد اعداد میں توڑیں۔"),
     T(f"Right! 48 = {expanded(48)} = {index_form(48)}.", f"درست! 48 = {expanded(48)} = {index_form(48)}"),
     T(f"48 = {index_form(48)}. The others don't work: 42 = 2 × 3 × 7 has a 7, 45 = 3² × 5 has a 5, 44 = 2² × 11 has an 11.", f"48 = {index_form(48)}۔ باقی نہیں چلتے: 42 = 2 × 3 × 7 میں 7 ہے، 45 = 3² × 5 میں 5 ہے، 44 = 2² × 11 میں 11 ہے۔"),
     common_wrong=[wrong(42, "42 = 2 × 3 × 7 also has the prime 7.", "42 = 2 × 3 × 7 میں مفرد عدد 7 بھی ہے۔"),
                   wrong(45, "45 = 3 × 3 × 5 has a 5 and no 2.", "45 = 3 × 3 × 5 میں 5 ہے اور 2 نہیں۔")]),
   number_question(
     "q11_who_am_i_index",
     T("Who am I? In index notation I am 2² × 7².", "میں کون ہوں؟ قوت کی شکل میں میں 2² × 7² ہوں۔"),
     Q11,
     T("2² = 4 and 7² = 49. Multiply them.", "2² = 4 اور 7² = 49۔ انہیں ضرب دیں۔"),
     T("Right! 4 × 49 = 196.", "درست! 4 × 49 = 196"),
     T("2 × 2 × 7 × 7 = 4 × 49 = 196.", "2 × 2 × 7 × 7 = 4 × 49 = 196"),
     common_wrong=[wrong(56, "7² is 7 × 7 = 49, not 7 × 2. So 4 × 49 = 196.", "7² کا مطلب 7 × 7 = 49 ہے، 7 × 2 نہیں۔ اس لیے 4 × 49 = 196", "times_index"),
                   wrong(28, "That is 2 × 2 × 7. There are two 7s: 2 × 2 × 7 × 7 = 196.", "یہ 2 × 2 × 7 ہے۔ دو 7 ہیں: 2 × 2 × 7 × 7 = 196")]),
   number_question(
     "q12_who_am_i_prime",
     T("Who am I? I am a prime number, I am a factor of 91, and I am bigger than 10.", "میں کون ہوں؟ میں مفرد عدد ہوں، 91 کا جزو ضربی ہوں، اور 10 سے بڑا ہوں۔"),
     Q12,
     T("Break 91 into primes. Try dividing by 7.", "91 کو مفرد اعداد میں توڑیں۔ 7 سے تقسیم کر کے دیکھیں۔"),
     T("Right! 91 = 7 × 13, and 13 is the prime bigger than 10.", "درست! 91 = 7 × 13، اور 13 وہ مفرد عدد ہے جو 10 سے بڑا ہے۔"),
     T("91 = 7 × 13. 7 is smaller than 10, so the answer is 13.", "91 = 7 × 13۔ 7، 10 سے چھوٹا ہے، اس لیے جواب 13 ہے۔"),
     common_wrong=[wrong(7, "7 is a prime factor of 91, but it is not bigger than 10.", "7، 91 کا مفرد جزو ضربی ہے، مگر 10 سے بڑا نہیں۔"),
                   wrong(91, "91 = 7 × 13, so 91 is not prime.", "91 = 7 × 13، اس لیے 91 مفرد نہیں۔")]),
   choice_question(
     "q13_find_error",
     T("Zoya writes 3 × 3 × 3 × 3 × 7 = 4³ × 7. What went wrong?", "زویا لکھتی ہے 3 × 3 × 3 × 3 × 7 = 4³ × 7۔ کیا غلطی ہوئی؟"),
     [opt("swap", "She swapped base and index. Four 3s is 3⁴, so it is 3⁴ × 7.", "اس نے اساس اور قوت الٹ دیے۔ چار 3 یعنی 3⁴، اس لیے 3⁴ × 7", True,
          "Yes! The base is the number multiplied (3) and the index is how many times (4).", "جی ہاں! اساس وہ عدد ہے جو ضرب ہو رہا ہے (3) اور قوت بتاتی ہے کتنی بار (4)۔"),
      opt("times", "It should be 3 × 4 × 7.", "یہ 3 × 4 × 7 ہونا چاہیے۔", False,
          "3 × 4 means one 3 times 4. Four 3s multiplied is 3⁴, so 3⁴ × 7.", "3 × 4 کا مطلب ایک 3 ضرب 4 ہے۔ چار 3 کا حاصل ضرب 3⁴ ہے، اس لیے 3⁴ × 7", "times_index"),
      opt("nothing", "Nothing. 4³ × 7 is right.", "کوئی غلطی نہیں۔ 4³ × 7 درست ہے۔", False,
          "4³ = 4 × 4 × 4 = 64, but 3 × 3 × 3 × 3 = 81. The right form is 3⁴ × 7.", "4³ = 4 × 4 × 4 = 64، مگر 3 × 3 × 3 × 3 = 81۔ درست شکل 3⁴ × 7 ہے۔", "swap_base_index")],
     qtype="find_error"),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Great work! You can break numbers into primes both ways now.", "بہت خوب! اب آپ اعداد کو دونوں طریقوں سے مفرد اعداد میں توڑ سکتے ہیں۔"),
    "text": T("Factor tree: split a number into two factors and keep splitting until every branch ends in a prime. Division method: keep dividing by primes until you reach 1. Then write the primes in index notation: 2 × 2 × 3 × 3 × 5 = 2² × 3² × 5.",
              "اجزائے ضربی کا درخت: عدد کو دو اجزائے ضربی میں توڑیں اور توڑتے رہیں یہاں تک کہ ہر شاخ مفرد عدد پر ختم ہو۔ تقسیم کا طریقہ: 1 تک پہنچنے تک مفرد اعداد سے تقسیم کرتے رہیں۔ پھر مفرد اعداد کو قوت کی شکل میں لکھیں: 2 × 2 × 3 × 3 × 5 = 2² × 3² × 5"),
    "points": [T("In 3⁴ the base is 3 and the index is 4: 3⁴ = 3 × 3 × 3 × 3.", "3⁴ میں اساس 3 اور قوت 4 ہے: 3⁴ = 3 × 3 × 3 × 3"),
               T("Check your answer by multiplying the primes back together.", "مفرد اعداد کو واپس ضرب دے کر اپنا جواب جانچیں۔")]},
 ],
 bank=[
   {"id": "qb_base", "type": "recall", "step": choice_question(
     "qb_base",
     T("In 6³, what is the 6 called?", "6³ میں 6 کو کیا کہتے ہیں؟"),
     [opt("base", "The base", "اساس", True, "Yes! The base is the number multiplied: 6³ = 6 × 6 × 6.", "جی ہاں! اساس وہ عدد ہے جو ضرب ہوتا ہے: 6³ = 6 × 6 × 6"),
      opt("index", "The index", "قوت", False, "The index is the small 3: how many 6s are multiplied.", "قوت چھوٹا 3 ہے: کتنے 6 ضرب ہو رہے ہیں۔", "swap_base_index"),
      opt("factor_tree", "A factor tree", "اجزائے ضربی کا درخت", False, "A factor tree is a way to find prime factors. In 6³, 6 is the base.", "اجزائے ضربی کا درخت مفرد اجزائے ضربی معلوم کرنے کا طریقہ ہے۔ 6³ میں 6 اساس ہے۔")],
     qtype=None)},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("98 = 2 × 7ⁿ. Break 98 into primes and find n.", "98 = 2 × 7ⁿ۔ 98 کو مفرد اعداد میں توڑیں اور n معلوم کریں۔"),
     QB,
     T("98 ÷ 2 = 49. How many 7s make 49?", "98 ÷ 2 = 49۔ کتنے 7 مل کر 49 بناتے ہیں؟"),
     T("Right! 98 = 2 × 7 × 7 = 2 × 7².", "درست! 98 = 2 × 7 × 7 = 2 × 7²"),
     T("98 = 2 × 49 = 2 × 7 × 7, so n = 2.", "98 = 2 × 49 = 2 × 7 × 7، اس لیے n = 2"),
     common_wrong=[wrong(7, "7 is the base. Count the 7s: 49 = 7 × 7, so n = 2.", "7 اساس ہے۔ 7 گنیں: 49 = 7 × 7، اس لیے n = 2", "swap_base_index")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": choice_question(
     "qb_find_error",
     T("Kamran says the prime factorisation of 120 is 4 × 5 × 6. What went wrong?", "کامران کہتا ہے 120 کے مفرد اجزائے ضربی 4 × 5 × 6 ہیں۔ کیا غلطی ہوئی؟"),
     [opt("not_prime", "4 and 6 are not prime. Break them: 120 = 2³ × 3 × 5.", "4 اور 6 مفرد نہیں۔ انہیں توڑیں: 120 = 2³ × 3 × 5", True,
          "Yes! 4 = 2 × 2 and 6 = 2 × 3, so 120 = 2 × 2 × 2 × 3 × 5.", "جی ہاں! 4 = 2 × 2 اور 6 = 2 × 3، اس لیے 120 = 2 × 2 × 2 × 3 × 5"),
      opt("wrong_product", "4 × 5 × 6 is not 120.", "4 × 5 × 6، 120 نہیں ہے۔", False,
          "4 × 5 × 6 is 120. The problem is that 4 and 6 are not prime.", "4 × 5 × 6 = 120 ہی ہے۔ مسئلہ یہ ہے کہ 4 اور 6 مفرد نہیں۔"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "Every factor must be prime. 4 = 2 × 2 and 6 = 2 × 3, so 120 = 2³ × 3 × 5.", "ہر جزو ضربی مفرد ہونا چاہیے۔ 4 = 2 × 2 اور 6 = 2 × 3، اس لیے 120 = 2³ × 3 × 5", "not_prime_factors")],
     qtype=None)},
 ],
 review=[
   {"id": "r_value", "type": "apply", "step": number_question(
     "r_value",
     T("Which number is 2³ × 3 × 5?", "2³ × 3 × 5 کون سا عدد ہے؟"),
     R1,
     T("2³ = 8. Then 8 × 3 × 5.", "2³ = 8۔ پھر 8 × 3 × 5"),
     T("Right! 8 × 15 = 120.", "درست! 8 × 15 = 120"),
     T("2³ = 2 × 2 × 2 = 8, and 8 × 3 × 5 = 120.", "2³ = 2 × 2 × 2 = 8، اور 8 × 3 × 5 = 120"),
     common_wrong=[wrong(90, "2³ is 8, not 2 × 3 = 6. 8 × 3 × 5 = 120.", "2³ = 8 ہے، 2 × 3 = 6 نہیں۔ 8 × 3 × 5 = 120", "times_index")],
     qtype=None)},
   {"id": "r_index", "type": "recall", "step": choice_question(
     "r_index",
     T("Which is 5 × 5 × 5 in index notation?", "5 × 5 × 5 قوت کی شکل میں کیا ہے؟"),
     [opt("right", "5³", "5³", True, "Yes! Three 5s.", "جی ہاں! تین 5"),
      opt("swap", "3⁵", "3⁵", False, "The base is 5 and the index is 3: 5³.", "اساس 5 اور قوت 3 ہے: 5³", "swap_base_index"),
      opt("times", "5 × 3", "5 × 3", False, "5 × 3 = 15, but 5 × 5 × 5 = 125. Write 5³.", "5 × 3 = 15، مگر 5 × 5 × 5 = 125۔ 5³ لکھیں۔", "times_index")],
     qtype=None)},
 ],
 glossary=[T("Factor tree", "اجزائے ضربی کا درخت"), T("Prime factor", "مفرد جزو ضربی"), T("Division method", "تقسیم کا طریقہ"),
           T("Index notation", "قوت کی شکل"), T("Expanded form", "پھیلی ہوئی شکل"), T("Base", "اساس"), T("Index (power)", "قوت")],
 flashcards=[
   {"id": "f_division", "front": T("How does the division method find prime factors?", "تقسیم کا طریقہ مفرد اجزائے ضربی کیسے معلوم کرتا ہے؟"),
    "back": T("Keep dividing by the smallest prime that goes in exactly until you reach 1. 150: ÷ 2, ÷ 3, ÷ 5, ÷ 5, so 150 = 2 × 3 × 5².", "1 تک پہنچنے تک سب سے چھوٹے مفرد عدد سے تقسیم کرتے رہیں جو پورا تقسیم کرے۔ 150: 2، 3، 5، 5 سے تقسیم، اس لیے 150 = 2 × 3 × 5²")},
   {"id": "f_expanded", "front": T("Expanded form and index notation of 72?", "72 کی پھیلی ہوئی شکل اور قوت کی شکل؟"),
    "back": T("Expanded: 2 × 2 × 2 × 3 × 3. Index notation: 2³ × 3².", "پھیلی ہوئی: 2 × 2 × 2 × 3 × 3۔ قوت کی شکل: 2³ × 3²")},
 ],
 home_task={"id": "h_riddle", "text": T(
   "Make up your own \"Who am I?\" riddle using prime factors, like \"I am between 30 and 40 and my prime factors are 2 and 3.\" Ask a family member or friend to solve it.",
   "مفرد اجزائے ضربی سے اپنی \"میں کون ہوں؟\" پہیلی بنائیں، جیسے \"میں 30 اور 40 کے درمیان ہوں اور میرے مفرد اجزائے ضربی 2 اور 3 ہیں۔\" گھر کے کسی فرد یا دوست سے حل کروائیں۔")},
 notes=["Covers completing factor trees (q1, q9), index notation and expanded form (q2 to q5, q7, q8, q11), the division method (s_division, q6) and who-am-I riddles (q10 to q12).",
        "The division method is not taught in the unit's lessons, so s_division shows it once before q6.",
        "Urdu terms to check: پھیلی ہوئی شکل (expanded form), تقسیم کا طریقہ (division method)."],
 minutes=18,
)

attach(lesson, {
    "q1_tree_gap": tree_figure(T126,
        "A factor tree for 126: 126 splits into 2 and 63; 63 splits into a question mark and 7; the question mark splits into 3 and 3. The primes at the ends of the branches are circled.",
        "126 کا اجزائے ضربی کا درخت: 126 سے 2 اور 63؛ 63 سے سوالیہ نشان اور 7؛ سوالیہ نشان سے 3 اور 3۔ شاخوں کے آخر میں مفرد اعداد کے گرد دائرہ ہے۔"),
    "s_division": division_ladder(D150, R150,
        "The division method for 150, set out in steps. On the left the primes 2, 3, 5, 5; on the right 150, then 75, 25, 5 and finally 1.",
        "150 کے لیے تقسیم کا طریقہ قدم بہ قدم۔ بائیں طرف مفرد اعداد 2، 3، 5، 5؛ دائیں طرف 150، پھر 75، 25، 5 اور آخر میں 1۔"),
    "q6_division": division_ladder(D156[:3], R156[:4],
        "The division method for 156. On the left the primes 2, 2, 3; on the right 156, then 78, 39, and a question mark under 39.",
        "156 کے لیے تقسیم کا طریقہ۔ بائیں طرف مفرد اعداد 2، 2، 3؛ دائیں طرف 156، پھر 78، 39، اور 39 کے نیچے سوالیہ نشان۔",
        hide={(3, 0)}),
    "q9_tree_264": tree_fig(T264, " 33 at the end is not split yet.", " آخر میں 33 ابھی توڑا نہیں گیا۔"),
    "qb_find_error": tree_figure((120, (4, (2,), (2,)), (30, (5,), (6, (2,), (3,)))),
        "A factor tree for 120: 120 splits into 4 and 30; 4 into 2 and 2; 30 into 5 and 6; 6 into 2 and 3. The primes at the ends of the branches are circled.",
        "120 کا اجزائے ضربی کا درخت: 120 سے 4 اور 30؛ 4 سے 2 اور 2؛ 30 سے 5 اور 6؛ 6 سے 2 اور 3۔ شاخوں کے آخر میں مفرد اعداد کے گرد دائرہ ہے۔"),
})
write(lesson)
