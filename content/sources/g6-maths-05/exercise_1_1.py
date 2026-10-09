"""Practice set for Exercise 1.1 of the book: list factors and multiples,
pick out primes, odd composite numbers and the even prime. The questions
are new; only the kinds of question follow the book."""
from common import (T, opt, say, wrong, number_question, choice_question, practice_lesson,
                    practice_intro, write, factors, is_prime, EX_SKILL, FM_FACTORS, FM_PRIMES)
from figs import attach, arrays_figure, multiples_line, number_grid, en_list, ur_list

SKILL = EX_SKILL["1.1"]


def multiples(n, count):
    return [n * k for k in range(1, count + 1)]


def odd_composites(lo, hi):
    return [n for n in range(lo, hi + 1) if n % 2 == 1 and n > 1 and not is_prime(n)]


# q1: how many factors does 20 have
F20 = factors(20)
Q1 = len(F20)
assert F20 == [1, 2, 4, 5, 10, 20] and Q1 == 6
Q1_NO_ENDS = Q1 - 2          # forgets 1 and 20
assert Q1_NO_ENDS == 4
# q2: all the factors of 30
F30 = factors(30)
assert F30 == [1, 2, 3, 5, 6, 10, 15, 30]
F30_NO_ENDS = F30[1:-1]
F30_NO_PAIR = [f for f in F30 if f not in (5, 6)]
assert 5 * 6 == 30 and F30_NO_PAIR == [1, 2, 3, 10, 15, 30]
M30 = multiples(30, 4)
assert M30 == [30, 60, 90, 120]
# q3: the 6th multiple of 9
Q3 = 9 * 6
assert Q3 == 54 and 9 + 6 == 15 and 9 * 5 == 45
# q4: the first five multiples of 8
M8 = multiples(8, 5)
assert M8 == [8, 16, 24, 32, 40]
M8_LATE = multiples(8, 6)[1:]
assert M8_LATE == [16, 24, 32, 40, 48]
assert factors(8) == [1, 2, 4, 8]
M8_SLIP = [8, 16, 24, 30, 40]
assert any(v % 8 for v in M8_SLIP)
# q5: multiples of 7 between 20 and 60
M7 = [n for n in range(21, 60) if n % 7 == 0]
Q5 = len(M7)
assert M7 == [21, 28, 35, 42, 49, 56] and Q5 == 6
Q5_SUBTRACT = (60 - 20) // 7
assert Q5_SUBTRACT == 5 != Q5
# q6: primes between 20 and 40
P20_40 = [n for n in range(21, 40) if is_prime(n)]
Q6 = len(P20_40)
assert P20_40 == [23, 29, 31, 37] and Q6 == 4
Q6_ODD = len([n for n in range(21, 40) if n % 2])
assert Q6_ODD == 10
# q7: which is prime: 51, 57, 53, 49
Q7_OPTS = (51, 57, 53, 49)
assert [n for n in Q7_OPTS if is_prime(n)] == [53]
assert 51 == 3 * 17 and 57 == 3 * 19 and 49 == 7 * 7
# q8: which is an odd composite: 23, 35, 31, 40
assert odd_composites(23, 23) == [] and odd_composites(31, 31) == [] and odd_composites(35, 35) == [35]
assert 35 == 5 * 7 and 40 % 2 == 0 and not is_prime(40)
# q9: odd composites from 1 to 30
OC30 = odd_composites(1, 30)
Q9 = len(OC30)
assert OC30 == [9, 15, 21, 25, 27] and Q9 == 5
Q9_WITH_ONE = Q9 + 1         # counts 1 as composite
assert Q9_WITH_ONE == 6
# q10: the even prime
EVEN_PRIMES = [n for n in range(1, 200) if n % 2 == 0 and is_prime(n)]
assert EVEN_PRIMES == [2] and not is_prime(1)
# q11: a factor of 48, a multiple of 6, between 20 and 40
Q11_ALL = [n for n in factors(48) if n % 6 == 0 and 20 < n < 40]
assert Q11_ALL == [24]
Q11 = Q11_ALL[0]
assert 48 % 6 == 0 and 48 > 40 and 12 < 20
# q12: twin prime of 59 (the next prime after it)
assert is_prime(59) and is_prime(61) and not is_prime(57) and 57 == 3 * 19
Q12 = 61
assert Q12 - 59 == 2
# find error: 39 is odd but not prime
assert 39 == 3 * 13 and factors(39) == [1, 3, 13, 39] and not is_prime(39)
# question bank
QB_REC = len(factors(45))
assert factors(45) == [1, 3, 5, 9, 15, 45] and QB_REC == 6
QB_APP = len([n for n in range(41, 60) if is_prime(n)])
assert [n for n in range(41, 60) if is_prime(n)] == [41, 43, 47, 53, 59] and QB_APP == 5
QB_ODD = len([n for n in range(41, 60) if n % 2])
assert QB_ODD == 10 and [n for n in range(41, 60) if n % 2 and not is_prime(n)] == [45, 49, 51, 55, 57]
assert 1 not in [n for n in range(1, 10) if is_prime(n)]
# review
R1 = 12 * 7
assert R1 == 84 and 12 + 7 == 19 and 12 * 6 == 72
R2_OPTS = (21, 27, 29, 33)
assert [n for n in R2_OPTS if is_prime(n)] == [29]


lesson = practice_lesson(
 "1.1", script="exercise_1_1.py",
 title=T("Exercise 1.1 practice: factors, multiples and primes", "مشق 1.1 کی پریکٹس: اجزائے ضربی، اضعاف اور مفرد اعداد"),
 outcome="List the factors and multiples of a number, and pick out prime numbers, odd composite numbers and the even prime.",
 prerequisites=[FM_FACTORS, FM_PRIMES],
 misconceptions=[
   {"id": "factor_multiple_swap", "description": "Gives multiples when factors are asked for, or factors when multiples are asked for."},
   {"id": "missing_pairs", "description": "Leaves out factors when listing them, especially 1 and the number itself, or one of a pair."},
   {"id": "adds_for_multiple", "description": "Adds instead of multiplying to find a multiple: the 6th multiple of 9 is 15."},
   {"id": "odd_is_prime", "description": "Thinks every odd number is prime: 39, 51 and 57 are prime."},
   {"id": "one_is_prime", "description": "Thinks 1 is a prime or a composite number; it is neither."},
 ],
 steps=[
   practice_intro("1.1",
     "Here you list factors and multiples, and pick out prime numbers, odd composite numbers and the even prime.",
     "اس میں آپ اجزائے ضربی اور اضعاف لکھیں گے، اور مفرد اعداد، طاق مرکب اعداد اور جفت مفرد عدد چنیں گے۔",
     "Let's practise Exercise 1.1 together. Take your time with each one!",
     "آئیں مل کر مشق 1.1 کی پریکٹس کریں۔ ہر سوال آرام سے کریں!"),
   number_question(
     "q1_count_factors",
     T("How many factors does 20 have?", "20 کے کتنے اجزائے ضربی ہیں؟"),
     Q1,
     T("Find them in pairs: 1 × 20, 2 × 10, 4 × 5.", "جوڑوں میں ڈھونڈیں: 1 × 20، 2 × 10، 4 × 5"),
     T(f"Right! The factors of 20 are {en_list(F20)}.", f"درست! 20 کے اجزائے ضربی {ur_list(F20)} ہیں۔"),
     T(f"The pairs 1 × 20, 2 × 10 and 4 × 5 give {Q1} factors: {en_list(F20)}.", f"جوڑے 1 × 20، 2 × 10 اور 4 × 5 سے {Q1} اجزائے ضربی ملتے ہیں: {ur_list(F20)}"),
     common_wrong=[wrong(Q1_NO_ENDS, "Don't forget 1 and 20 themselves: 1 × 20 is a pair too.", "1 اور خود 20 کو نہ بھولیں: 1 × 20 بھی ایک جوڑا ہے۔", "missing_pairs")],
     qtype="recall"),
   choice_question(
     "q2_list_factors",
     T("Which list shows ALL the factors of 30?", "کون سی فہرست 30 کے سارے اجزائے ضربی دکھاتی ہے؟"),
     [opt("all", en_list(F30), ur_list(F30), True,
          "Yes! The pairs are 1 × 30, 2 × 15, 3 × 10 and 5 × 6.", "جی ہاں! جوڑے 1 × 30، 2 × 15، 3 × 10 اور 5 × 6 ہیں۔"),
      opt("no_ends", en_list(F30_NO_ENDS), ur_list(F30_NO_ENDS), False,
          "1 and 30 are missing. Every number has 1 and itself as factors.", "1 اور 30 غائب ہیں۔ ہر عدد کے اجزائے ضربی میں 1 اور خود وہ عدد ہوتا ہے۔", "missing_pairs"),
      opt("no_pair", en_list(F30_NO_PAIR), ur_list(F30_NO_PAIR), False,
          "The pair 5 × 6 is missing: 5 and 6 are factors of 30 too.", "جوڑا 5 × 6 غائب ہے: 5 اور 6 بھی 30 کے اجزائے ضربی ہیں۔", "missing_pairs"),
      opt("multiples", en_list(M30), ur_list(M30), False,
          "These are multiples of 30. Factors divide 30 exactly, so none is bigger than 30.", "یہ 30 کے اضعاف ہیں۔ اجزائے ضربی 30 کو پورا تقسیم کرتے ہیں، اس لیے کوئی 30 سے بڑا نہیں۔", "factor_multiple_swap")],
     qtype="recall"),
   number_question(
     "q3_sixth_multiple",
     T("What is the 6th multiple of 9?", "9 کا چھٹا ضعف کیا ہے؟"),
     Q3,
     T("Count in 9s six times: 9, 18, 27 ... or work out 9 × 6.", "9، 9 کر کے چھ بار گنیں: 9، 18، 27 ... یا 9 × 6 کریں۔"),
     T("Right! 9 × 6 = 54.", "درست! 9 × 6 = 54"),
     T("9, 18, 27, 36, 45, 54. The 6th multiple is 9 × 6 = 54.", "9، 18، 27، 36، 45، 54۔ چھٹا ضعف 9 × 6 = 54 ہے۔"),
     common_wrong=[wrong(15, "That is 9 + 6. A multiple comes from multiplying: 9 × 6 = 54.", "یہ 9 + 6 ہے۔ ضعف ضرب سے ملتا ہے: 9 × 6 = 54", "adds_for_multiple"),
                   wrong(45, "45 is the 5th multiple. One more jump of 9: 54.", "45 پانچواں ضعف ہے۔ 9 کی ایک اور چھلانگ: 54")]),
   choice_question(
     "q4_first_multiples",
     T("Which list shows the first five multiples of 8?", "کون سی فہرست 8 کے پہلے پانچ اضعاف دکھاتی ہے؟"),
     [opt("right", en_list(M8), ur_list(M8), True,
          "Yes! 8 × 1, 8 × 2, 8 × 3, 8 × 4, 8 × 5.", "جی ہاں! 8 × 1، 8 × 2، 8 × 3، 8 × 4، 8 × 5"),
      opt("late", en_list(M8_LATE), ur_list(M8_LATE), False,
          "The first multiple of 8 is 8 itself (8 × 1). This list starts one too late.", "8 کا پہلا ضعف خود 8 ہے (8 × 1)۔ یہ فہرست ایک قدم دیر سے شروع ہوتی ہے۔"),
      opt("slip", en_list(M8_SLIP), ur_list(M8_SLIP), False,
          "30 is not in the 8 times table: 8 × 4 = 32.", "30، 8 کے پہاڑے میں نہیں: 8 × 4 = 32"),
      opt("factors", en_list(factors(8)), ur_list(factors(8)), False,
          "These are the factors of 8. Multiples are in the 8 times table: 8, 16, 24 ...", "یہ 8 کے اجزائے ضربی ہیں۔ اضعاف 8 کے پہاڑے میں ہوتے ہیں: 8، 16، 24 ...", "factor_multiple_swap")]),
   number_question(
     "q5_multiples_between",
     T("How many multiples of 7 are there between 20 and 60?", "20 اور 60 کے درمیان 7 کے کتنے اضعاف ہیں؟"),
     Q5,
     T("The first one after 20 is 21 = 7 × 3. Keep adding 7 until you pass 60.", "20 کے بعد پہلا 21 = 7 × 3 ہے۔ 60 سے آگے جانے تک 7 جمع کرتے رہیں۔"),
     T(f"Right! {en_list(M7)}.", f"درست! {ur_list(M7)}"),
     T(f"They are {en_list(M7)}: {Q5} multiples. The next one, 63, is past 60.", f"یہ {ur_list(M7)} ہیں: {Q5} اضعاف۔ اگلا، 63، 60 سے آگے ہے۔"),
     common_wrong=[wrong(Q5_SUBTRACT, f"(60 − 20) ÷ 7 misses one. List them: {en_list(M7)}.", f"(60 − 20) ÷ 7 سے ایک رہ جاتا ہے۔ لکھ کر دیکھیں: {ur_list(M7)}")]),
   number_question(
     "q6_count_primes",
     T("How many prime numbers are there between 20 and 40?", "20 اور 40 کے درمیان کتنے مفرد اعداد ہیں؟"),
     Q6,
     T("Only odd numbers can be prime here. Cross out those that 3, 5 or 7 divide.", "یہاں صرف طاق اعداد مفرد ہو سکتے ہیں۔ جنہیں 3، 5 یا 7 تقسیم کرے انہیں کاٹ دیں۔"),
     T(f"Right! {en_list(P20_40)}.", f"درست! {ur_list(P20_40)}"),
     T(f"The primes are {en_list(P20_40)}. 21, 27, 33 and 39 have 3 as a factor, 25 and 35 have 5.", f"مفرد اعداد {ur_list(P20_40)} ہیں۔ 21، 27، 33 اور 39 میں 3 جزو ضربی ہے، 25 اور 35 میں 5۔"),
     common_wrong=[wrong(Q6_ODD, "That counts every odd number. Odd numbers like 21 = 3 × 7 are not prime.", "یہ ہر طاق عدد گن لیا۔ 21 = 3 × 7 جیسے طاق اعداد مفرد نہیں۔", "odd_is_prime")],
     qtype="recall"),
   choice_question(
     "q7_which_prime",
     T("Which of these is a prime number?", "ان میں سے کون سا مفرد عدد ہے؟"),
     [opt("n51", "51", "51", False, "51 = 3 × 17, so it is composite. Add its digits: 5 + 1 = 6, which 3 divides.", "51 = 3 × 17، اس لیے یہ مرکب ہے۔ ہندسے جمع کریں: 5 + 1 = 6، جسے 3 تقسیم کرتا ہے۔", "odd_is_prime"),
      opt("n57", "57", "57", False, "57 = 3 × 19, so it is composite.", "57 = 3 × 19، اس لیے یہ مرکب ہے۔", "odd_is_prime"),
      opt("n53", "53", "53", True, "Yes! No number from 2 to 7 divides 53, so its only factors are 1 and 53.", "جی ہاں! 2 سے 7 تک کوئی عدد 53 کو تقسیم نہیں کرتا، اس لیے اس کے اجزائے ضربی صرف 1 اور 53 ہیں۔"),
      opt("n49", "49", "49", False, "49 = 7 × 7, so it is composite.", "49 = 7 × 7، اس لیے یہ مرکب ہے۔", "odd_is_prime")]),
   choice_question(
     "q8_odd_composite",
     T("Which of these is an odd composite number?", "ان میں سے کون سا طاق مرکب عدد ہے؟"),
     [opt("n23", "23", "23", False, "23 is odd, but it is prime: only 1 and 23 divide it.", "23 طاق ہے، مگر مفرد ہے: اسے صرف 1 اور 23 تقسیم کرتے ہیں۔"),
      opt("n35", "35", "35", True, "Yes! 35 is odd and 35 = 5 × 7, so it has more than two factors.", "جی ہاں! 35 طاق ہے اور 35 = 5 × 7، اس لیے اس کے دو سے زیادہ اجزائے ضربی ہیں۔"),
      opt("n31", "31", "31", False, "31 is odd, but it is prime.", "31 طاق ہے، مگر مفرد ہے۔"),
      opt("n40", "40", "40", False, "40 is composite, but it is even, not odd.", "40 مرکب ہے، مگر جفت ہے، طاق نہیں۔")]),
   number_question(
     "q9_count_odd_composites",
     T("How many odd composite numbers are there from 1 to 30?", "1 سے 30 تک کتنے طاق مرکب اعداد ہیں؟"),
     Q9,
     T("Go through the odd numbers 1, 3, 5 ... 29. Which are not prime? Remember 1 is neither prime nor composite.", "طاق اعداد 1، 3، 5 ... 29 دیکھیں۔ کون سے مفرد نہیں؟ یاد رکھیں 1 نہ مفرد ہے نہ مرکب۔"),
     T(f"Right! {en_list(OC30)}.", f"درست! {ur_list(OC30)}"),
     T(f"They are {en_list(OC30)}: {Q9} numbers. 1 does not count, because it is neither prime nor composite.", f"یہ {ur_list(OC30)} ہیں: {Q9} اعداد۔ 1 نہیں گنا جاتا، کیونکہ یہ نہ مفرد ہے نہ مرکب۔"),
     common_wrong=[wrong(Q9_WITH_ONE, "1 is not composite: it has only one factor. Leave it out.", "1 مرکب نہیں: اس کا صرف ایک جزو ضربی ہے۔ اسے نہ گنیں۔", "one_is_prime")]),
   choice_question(
     "q10_even_prime",
     T("Which of these is the only even prime number?", "ان میں سے کون سا واحد جفت مفرد عدد ہے؟"),
     [opt("two", "2", "2", True, "Yes! 2 has only the factors 1 and 2. Every other even number has 2 as a factor too.", "جی ہاں! 2 کے اجزائے ضربی صرف 1 اور 2 ہیں۔ ہر دوسرے جفت عدد میں 2 بھی جزو ضربی ہوتا ہے۔"),
      opt("one", "1", "1", False, "1 is odd, and it is not prime: it has only one factor.", "1 طاق ہے، اور مفرد نہیں: اس کا صرف ایک جزو ضربی ہے۔", "one_is_prime"),
      opt("four", "4", "4", False, "4 = 2 × 2, so it is composite.", "4 = 2 × 2، اس لیے یہ مرکب ہے۔"),
      opt("ten", "10", "10", False, "10 = 2 × 5, so it is composite.", "10 = 2 × 5، اس لیے یہ مرکب ہے۔")],
     qtype="recall"),
   number_question(
     "q11_who_am_i",
     T("I am a factor of 48 and a multiple of 6. I am between 20 and 40. Who am I?", "میں 48 کا جزو ضربی ہوں اور 6 کا ضعف بھی۔ میں 20 اور 40 کے درمیان ہوں۔ میں کون ہوں؟"),
     Q11,
     T("List the factors of 48 between 20 and 40. Which one is in the 6 times table?", "48 کے وہ اجزائے ضربی لکھیں جو 20 اور 40 کے درمیان ہیں۔ ان میں سے کون 6 کے پہاڑے میں ہے؟"),
     T("Right! 24 × 2 = 48 and 6 × 4 = 24.", "درست! 24 × 2 = 48 اور 6 × 4 = 24"),
     T("The only factor of 48 between 20 and 40 is 24, and 24 = 6 × 4.", "48 کا 20 اور 40 کے درمیان واحد جزو ضربی 24 ہے، اور 24 = 6 × 4"),
     common_wrong=[wrong(48, "48 is a factor of itself, but it is not between 20 and 40.", "48 اپنا جزو ضربی ہے، مگر یہ 20 اور 40 کے درمیان نہیں۔"),
                   wrong(36, "36 is a multiple of 6, but 48 ÷ 36 is not exact.", "36، 6 کا ضعف ہے، مگر 48 ÷ 36 پورا تقسیم نہیں ہوتا۔", "factor_multiple_swap")]),
   number_question(
     "q12_twin_prime",
     T("Twin primes are two prime numbers that differ by 2, like 17 and 19. 59 is prime. Which bigger prime makes a twin pair with it?", "جڑواں مفرد اعداد وہ دو مفرد اعداد ہیں جن کا فرق 2 ہو، جیسے 17 اور 19۔ 59 مفرد ہے۔ کون سا بڑا مفرد عدد اس کے ساتھ جڑواں جوڑا بناتا ہے؟"),
     Q12,
     T("Try 59 + 2. Is it prime? Check 2, 3, 5 and 7.", "59 + 2 آزمائیں۔ کیا یہ مفرد ہے؟ 2، 3، 5 اور 7 سے جانچیں۔"),
     T("Right! 61 is prime, so 59 and 61 are twin primes.", "درست! 61 مفرد ہے، اس لیے 59 اور 61 جڑواں مفرد اعداد ہیں۔"),
     T("59 + 2 = 61, and no number from 2 to 7 divides 61. So 61 is prime.", "59 + 2 = 61، اور 2 سے 7 تک کوئی عدد 61 کو تقسیم نہیں کرتا۔ اس لیے 61 مفرد ہے۔"),
     common_wrong=[wrong(57, "57 is smaller than 59, and 57 = 3 × 19 is not prime. Try 59 + 2.", "57، 59 سے چھوٹا ہے، اور 57 = 3 × 19 مفرد نہیں۔ 59 + 2 آزمائیں۔", "odd_is_prime")]),
   choice_question(
     "q13_find_error",
     T("Areeba says, \"39 is odd, so it must be a prime number.\" What went wrong?", "اریبہ کہتی ہے، \"39 طاق ہے، اس لیے یہ لازماً مفرد عدد ہے۔\" کیا غلطی ہوئی؟"),
     [opt("odd_not_prime", "Odd numbers can be composite: 39 = 3 × 13.", "طاق اعداد مرکب بھی ہو سکتے ہیں: 39 = 3 × 13", True,
          "Yes! 39 has the factors 1, 3, 13 and 39, so it is an odd composite number.", "جی ہاں! 39 کے اجزائے ضربی 1، 3، 13 اور 39 ہیں، اس لیے یہ طاق مرکب عدد ہے۔"),
      opt("even_prime", "Only even numbers can be prime.", "صرف جفت اعداد مفرد ہو سکتے ہیں۔", False,
          "No: 3, 5, 7, 11 ... are odd primes. 2 is the only even prime. 39 = 3 × 13, so it is not prime.", "نہیں: 3، 5، 7، 11 ... طاق مفرد اعداد ہیں۔ 2 واحد جفت مفرد عدد ہے۔ 39 = 3 × 13، اس لیے یہ مفرد نہیں۔"),
      opt("nothing", "Nothing. 39 is prime.", "کوئی غلطی نہیں۔ 39 مفرد ہے۔", False,
          "Try dividing by 3: 39 ÷ 3 = 13. So 39 has more than two factors.", "3 سے تقسیم کر کے دیکھیں: 39 ÷ 3 = 13۔ اس لیے 39 کے دو سے زیادہ اجزائے ضربی ہیں۔", "odd_is_prime")],
     qtype="find_error"),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! You have practised all of Exercise 1.1.", "شاباش! آپ نے مشق 1.1 کی پوری پریکٹس کر لی۔"),
    "text": T("Factors divide a number exactly; find them in pairs and don't forget 1 and the number itself. Multiples are the number times 1, 2, 3 ... A prime has exactly two factors. A composite number has more than two. 1 is neither, and 2 is the only even prime.",
              "اجزائے ضربی عدد کو پورا تقسیم کرتے ہیں؛ انہیں جوڑوں میں ڈھونڈیں اور 1 اور خود عدد کو نہ بھولیں۔ اضعاف عدد کو 1، 2، 3 ... سے ضرب دینے سے ملتے ہیں۔ مفرد عدد کے ٹھیک دو اجزائے ضربی ہوتے ہیں۔ مرکب عدد کے دو سے زیادہ۔ 1 دونوں میں سے کوئی نہیں، اور 2 واحد جفت مفرد عدد ہے۔"),
    "points": [T("Not every odd number is prime: 9, 15, 21, 25 and 27 are odd composites.", "ہر طاق عدد مفرد نہیں: 9، 15، 21، 25 اور 27 طاق مرکب اعداد ہیں۔"),
               T("To test a number for prime, try dividing by 2, 3, 5 and 7.", "عدد مفرد ہے یا نہیں، یہ جانچنے کے لیے 2، 3، 5 اور 7 سے تقسیم کر کے دیکھیں۔")]},
 ],
 bank=[
   {"id": "qb_factors", "type": "recall", "step": number_question(
     "qb_factors",
     T("How many factors does 45 have?", "45 کے کتنے اجزائے ضربی ہیں؟"),
     QB_REC,
     T("Pairs: 1 × 45, 3 × 15, 5 × 9.", "جوڑے: 1 × 45، 3 × 15، 5 × 9"),
     T(f"Right! {en_list(factors(45))}.", f"درست! {ur_list(factors(45))}"),
     T(f"The factors of 45 are {en_list(factors(45))}: {QB_REC} of them.", f"45 کے اجزائے ضربی {ur_list(factors(45))} ہیں: کل {QB_REC}۔"),
     common_wrong=[wrong(QB_REC - 2, "Count 1 and 45 too.", "1 اور 45 بھی گنیں۔", "missing_pairs")],
     qtype=None)},
   {"id": "qb_primes", "type": "apply", "step": number_question(
     "qb_primes",
     T("How many prime numbers are there between 40 and 60?", "40 اور 60 کے درمیان کتنے مفرد اعداد ہیں؟"),
     QB_APP,
     T("Check only the odd numbers. Cross out those that 3, 5 or 7 divide.", "صرف طاق اعداد دیکھیں۔ جنہیں 3، 5 یا 7 تقسیم کرے انہیں کاٹ دیں۔"),
     T("Right! 41, 43, 47, 53 and 59.", "درست! 41، 43، 47، 53 اور 59"),
     T("The primes are 41, 43, 47, 53 and 59. 45, 51 and 57 have 3 as a factor, 49 = 7 × 7, 55 = 5 × 11.", "مفرد اعداد 41، 43، 47، 53 اور 59 ہیں۔ 45، 51 اور 57 میں 3 جزو ضربی ہے، 49 = 7 × 7، 55 = 5 × 11"),
     common_wrong=[wrong(QB_ODD, "That counts every odd number. 45, 49, 51, 55 and 57 are not prime.", "یہ ہر طاق عدد گن لیا۔ 45، 49، 51، 55 اور 57 مفرد نہیں۔", "odd_is_prime")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": choice_question(
     "qb_find_error",
     T("Faraz says, \"1 is the smallest prime number.\" What went wrong?", "فراز کہتا ہے، \"1 سب سے چھوٹا مفرد عدد ہے۔\" کیا غلطی ہوئی؟"),
     [opt("one_factor", "1 has only one factor, so it is not prime. The smallest prime is 2.", "1 کا صرف ایک جزو ضربی ہے، اس لیے یہ مفرد نہیں۔ سب سے چھوٹا مفرد عدد 2 ہے۔", True,
          "Yes! A prime needs exactly two factors. 1 is neither prime nor composite.", "جی ہاں! مفرد عدد کے ٹھیک دو اجزائے ضربی ہونے چاہییں۔ 1 نہ مفرد ہے نہ مرکب۔"),
      opt("three", "The smallest prime is 3, because 2 is even.", "سب سے چھوٹا مفرد عدد 3 ہے، کیونکہ 2 جفت ہے۔", False,
          "2 is even but still prime: its only factors are 1 and 2.", "2 جفت ہے مگر پھر بھی مفرد ہے: اس کے اجزائے ضربی صرف 1 اور 2 ہیں۔"),
      opt("nothing", "Nothing. 1 is prime.", "کوئی غلطی نہیں۔ 1 مفرد ہے۔", False,
          "1 has only one factor. A prime has exactly two.", "1 کا صرف ایک جزو ضربی ہے۔ مفرد عدد کے ٹھیک دو ہوتے ہیں۔", "one_is_prime")],
     qtype=None)},
 ],
 review=[
   {"id": "r_multiple", "type": "apply", "step": number_question(
     "r_multiple",
     T("What is the 7th multiple of 12?", "12 کا ساتواں ضعف کیا ہے؟"),
     R1,
     T("Work out 12 × 7.", "12 × 7 کریں۔"),
     T("Right! 12 × 7 = 84.", "درست! 12 × 7 = 84"),
     T("The 7th multiple is 12 × 7 = 84.", "ساتواں ضعف 12 × 7 = 84 ہے۔"),
     common_wrong=[wrong(19, "That is 12 + 7. Multiply: 12 × 7 = 84.", "یہ 12 + 7 ہے۔ ضرب دیں: 12 × 7 = 84", "adds_for_multiple"),
                   wrong(72, "72 is the 6th multiple. One more 12: 84.", "72 چھٹا ضعف ہے۔ ایک اور 12: 84")],
     qtype=None)},
   {"id": "r_prime", "type": "recall", "step": choice_question(
     "r_prime",
     T("Which of these is a prime number?", "ان میں سے کون سا مفرد عدد ہے؟"),
     [opt("n21", "21", "21", False, "21 = 3 × 7.", "21 = 3 × 7", "odd_is_prime"),
      opt("n27", "27", "27", False, "27 = 3 × 9.", "27 = 3 × 9", "odd_is_prime"),
      opt("n29", "29", "29", True, "Yes! Only 1 and 29 divide 29.", "جی ہاں! 29 کو صرف 1 اور 29 تقسیم کرتے ہیں۔"),
      opt("n33", "33", "33", False, "33 = 3 × 11.", "33 = 3 × 11", "odd_is_prime")],
     qtype=None)},
 ],
 glossary=[T("Factor", "جزو ضربی"), T("Multiple", "ضعف"), T("Prime number", "مفرد عدد"), T("Composite number", "مرکب عدد"),
           T("Odd number", "طاق عدد"), T("Even number", "جفت عدد"), T("Twin primes", "جڑواں مفرد اعداد")],
 flashcards=[
   {"id": "f_odd_composite", "front": T("What is an odd composite number?", "طاق مرکب عدد کیا ہے؟"),
    "back": T("An odd number with more than two factors, like 9, 15, 21, 25 and 35.", "ایسا طاق عدد جس کے دو سے زیادہ اجزائے ضربی ہوں، جیسے 9، 15، 21، 25 اور 35۔")},
   {"id": "f_even_prime", "front": T("Which is the only even prime?", "واحد جفت مفرد عدد کون سا ہے؟"),
    "back": T("2. Every other even number has 2 as a factor, so it has more than two factors.", "2۔ ہر دوسرے جفت عدد میں 2 جزو ضربی ہوتا ہے، اس لیے اس کے دو سے زیادہ اجزائے ضربی ہوتے ہیں۔")},
 ],
 home_task={"id": "h_house_numbers", "text": T(
   "Write down five numbers you see at home or on the street (a house number, a price, a page number). For each, say whether it is prime or composite, and write two of its multiples.",
   "گھر یا گلی میں نظر آنے والے پانچ اعداد لکھیں (مکان نمبر، قیمت، صفحہ نمبر)۔ ہر ایک کے بارے میں بتائیں کہ وہ مفرد ہے یا مرکب، اور اس کے دو اضعاف لکھیں۔")},
 notes=["Covers listing factors and multiples (q1 to q5), primes (q6, q7, q12), odd composites (q8, q9), the even prime (q10) and a who-am-I puzzle (q11).",
        "Urdu terms to check: طاق مرکب عدد (odd composite number), جڑواں مفرد اعداد (twin primes)."],
 minutes=16,
)

attach(lesson, {
    "q3_sixth_multiple": multiples_line(9, 6,
        "A number line from 0 with 6 jumps of 9, numbered 1 to 6 above the jumps. Under the line: 0, 9, 18, 27, 36, 45, and a question mark where the 6th jump lands.",
        "0 سے شروع ہونے والی عددی لکیر جس پر 9 کی 6 چھلانگیں ہیں، اوپر 1 سے 6 تک نمبر۔ لکیر کے نیچے: 0، 9، 18، 27، 36، 45، اور چھٹی چھلانگ کی جگہ سوالیہ نشان۔",
        shown=[0, 9, 18, 27, 36, 45], hide=[Q3]),
    "q6_count_primes": number_grid(20, 39,
        "The numbers 20 to 39 in a grid of 2 rows of 10.",
        "20 سے 39 تک کے اعداد 10، 10 کی 2 قطاروں کے خانوں میں۔"),
    "q9_count_odd_composites": number_grid(1, 30,
        "The numbers 1 to 30 in a grid of 3 rows of 10.",
        "1 سے 30 تک کے اعداد 10، 10 کی 3 قطاروں کے خانوں میں۔"),
    "q13_find_error": arrays_figure(
        [dict(rows=3, cols=13, text="3×13")],
        "39 dots in 3 rows of 13, with 3×13 written under them.",
        "39 نقطے، 13 کی 3 قطاریں، نیچے 3×13 لکھا ہے۔"),
})
write(lesson)
