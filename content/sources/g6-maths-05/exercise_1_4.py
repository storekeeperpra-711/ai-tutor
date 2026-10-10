"""Practice set for Exercise 1.4 of the book: LCM by prime factorisation
and by the division method, and "when do they meet again" word problems
(jumps, buses, traffic lights, bells). The questions are new; only the
kinds of question follow the book."""
from math import gcd, lcm

from common import (T, opt, say, wrong, number_question, choice_question, practice_lesson,
                    practice_intro, write, prime_factors, EX_SKILL, FM_LCM, FM_WORD_PROBLEMS)
from figs import attach, division_ladder, ladder_rows, multiples_rows

SKILL = EX_SKILL["1.4"]


def lcm_of(*ns):
    out = 1
    for n in ns:
        out = lcm(out, n)
    return out


def ladder_divisors(ns):
    """Divide by the smallest prime that divides at least one number, until all are 1."""
    ds, row = [], list(ns)
    while any(v > 1 for v in row):
        d = min(p for v in row if v > 1 for p in prime_factors(v))
        ds.append(d)
        row = [v // d if v % d == 0 else v for v in row]
    return ds


def clock(start_h, start_m, minutes):
    total = start_h * 60 + start_m + minutes
    return f"{total // 60 % 12 or 12}:{total % 60:02d}"


# q1: LCM of 8 and 12 by listing
Q1 = lcm(8, 12)
assert Q1 == 24 and 8 * 12 == 96 and gcd(8, 12) == 4
# q2: 2³ × 3 and 2 × 3² × 5
A2, B2 = 2 ** 3 * 3, 2 * 3 ** 2 * 5
Q2 = lcm(A2, B2)
assert (A2, B2) == (24, 90) and Q2 == 2 ** 3 * 3 ** 2 * 5 == 360 and gcd(A2, B2) == 6
assert 2 ** 4 * 3 ** 3 * 5 == 2160 and A2 * B2 == 2160
# q3: LCM of 18 and 30 by prime factorisation
Q3 = lcm(18, 30)
assert prime_factors(18) == [2, 3, 3] and prime_factors(30) == [2, 3, 5]
assert Q3 == 2 * 3 * 3 * 5 == 90 and gcd(18, 30) == 6 and 18 * 30 == 540
# s_division: worked example, 12 and 15
D_EX = ladder_divisors([12, 15])
R_EX = ladder_rows([12, 15], D_EX)
assert D_EX == [2, 2, 3, 5] and R_EX == [[12, 15], [6, 15], [3, 15], [1, 5], [1, 1]] and lcm(12, 15) == 60
# q4: division method for 16, 20 and 24
D4 = ladder_divisors([16, 20, 24])
R4 = ladder_rows([16, 20, 24], D4)
Q4 = lcm_of(16, 20, 24)
assert D4 == [2, 2, 2, 2, 3, 5] and Q4 == 240 == 2 ** 4 * 3 * 5
assert R4 == [[16, 20, 24], [8, 10, 12], [4, 5, 6], [2, 5, 3], [1, 5, 3], [1, 5, 1], [1, 1, 1]]
assert 16 * 20 * 24 == 7680 and gcd(gcd(16, 20), 24) == 4
# q5: LCM of 9, 12 and 15
Q5 = lcm_of(9, 12, 15)
assert Q5 == 180 and 9 * 12 * 15 == 1620 and gcd(gcd(9, 12), 15) == 3
# q6: hops of 4 and 10 from 0
Q6 = lcm(4, 10)
assert Q6 == 20 and 4 * 10 == 40 and gcd(4, 10) == 2
# q7, q8: buses every 25 and 35 minutes, both at 7:00
Q7 = lcm(25, 35)
assert Q7 == 175 and gcd(25, 35) == 5 and 25 * 35 == 875
Q8_TIME = clock(7, 0, Q7)
assert [clock(7, 0, 25 * k) for k in (1, 2, 3)] == ["7:25", "7:50", "8:15"] and [clock(7, 0, 35 * k) for k in (1, 2)] == ["7:35", "8:10"]
assert 60 % 25 and 60 % 35
assert Q8_TIME == "9:55" and clock(7, 0, 5) == "7:05" and clock(7, 0, 60 + 75) == "9:15" and clock(7, 0, 60) == "8:00"
# q9: traffic lights change every 40, 60 and 90 seconds
Q9_SECONDS = lcm_of(40, 60, 90)
Q9 = Q9_SECONDS // 60
assert Q9_SECONDS == 360 and Q9 == 6 and gcd(gcd(40, 60), 90) == 10
# q10: bells every 12, 18 and 20 minutes, together at 8:00
Q10_MIN = lcm_of(12, 18, 20)
Q10 = Q10_MIN // 60
assert Q10_MIN == 180 and Q10 == 3 and clock(8, 0, Q10_MIN) == "11:00"
# q11: sweets shared equally among 8, 12 or 18 children
Q11 = lcm_of(8, 12, 18)
assert Q11 == 72 and all(Q11 % n == 0 for n in (8, 12, 18)) and 8 * 12 * 18 == 1728
# find error: LCM of 12 and 16 is not 192
assert lcm(12, 16) == 48 and 12 * 16 == 192 and gcd(12, 16) == 4
# question bank
QB_REC = lcm(6, 15)
assert QB_REC == 30 and gcd(6, 15) == 3 and 6 * 15 == 90
QB_APP = lcm(45, 60)
assert QB_APP == 180 and gcd(45, 60) == 15
assert lcm(10, 14) == 70 and gcd(10, 14) == 2
# review
R1 = lcm(14, 21)
assert R1 == 42 and gcd(14, 21) == 7 and 14 * 21 == 294
R2 = lcm(6, 8)
assert R2 == 24 and 6 * 8 == 48


lesson = practice_lesson(
 "1.4", script="exercise_1_4.py",
 title=T("Exercise 1.4 practice: LCM", "مشق 1.4 کی پریکٹس: ذو اضعاف اقل"),
 outcome="Find the LCM of two or three numbers by prime factorisation and by the division method, and use it to find when repeating events happen together again.",
 prerequisites=[FM_LCM, FM_WORD_PROBLEMS],
 misconceptions=[
   {"id": "lcm_hcf_swap", "description": "Gives a common factor (often the HCF) instead of the LCM."},
   {"id": "always_multiply", "description": "Always multiplies the numbers: the LCM of 12 and 16 is 192, which is a common multiple but not the lowest."},
   {"id": "shared_primes_only", "description": "Multiplies only the shared prime factors, which gives the HCF."},
   {"id": "stops_early", "description": "Finds the LCM but does not answer the question asked (the time, or minutes instead of hours)."},
 ],
 steps=[
   practice_intro("1.4",
     "Here you find the LCM by prime factorisation and by the division method, then solve \"when do they meet again\" problems.",
     "اس میں آپ مفرد اجزائے ضربی اور تقسیم کے طریقے سے ذو اضعاف اقل معلوم کریں گے، پھر \"دوبارہ کب ساتھ ہوں گے\" والے سوال حل کریں گے۔",
     "Exercise 1.4 is about the LCM: the lowest number that both numbers divide into.",
     "مشق 1.4 ذو اضعاف اقل کے بارے میں ہے: سب سے چھوٹا عدد جسے دونوں اعداد تقسیم کریں۔"),
   number_question(
     "q1_listing",
     T("Find the LCM of 8 and 12.", "8 اور 12 کا ذو اضعاف اقل معلوم کریں۔"),
     Q1,
     T("Multiples of 12: 12, 24, 36 ... Which is the first one that 8 divides?", "12 کے اضعاف: 12، 24، 36 ... پہلا کون سا ہے جسے 8 تقسیم کرے؟"),
     T("Right! LCM = 24.", "درست! ذو اضعاف اقل = 24"),
     T("12 ÷ 8 is not exact, but 24 ÷ 8 = 3. So the LCM is 24.", "12 ÷ 8 پورا تقسیم نہیں ہوتا، مگر 24 ÷ 8 = 3۔ اس لیے ذو اضعاف اقل 24 ہے۔"),
     common_wrong=[wrong(96, "96 = 8 × 12 is a common multiple, but 24 is lower.", "96 = 8 × 12 مشترک ضعف ہے، مگر 24 چھوٹا ہے۔", "always_multiply"),
                   wrong(4, "4 is the HCF. The LCM is a multiple of both: 24.", "4 عاد اعظم ہے۔ ذو اضعاف اقل دونوں کا ضعف ہے: 24", "lcm_hcf_swap")],
     qtype="recall"),
   choice_question(
     "q2_index",
     T("24 = 2³ × 3 and 90 = 2 × 3² × 5. What is their LCM?", "24 = 2³ × 3 اور 90 = 2 × 3² × 5۔ ان کا ذو اضعاف اقل کیا ہے؟"),
     [opt("right", "2³ × 3² × 5 = 360", "2³ × 3² × 5 = 360", True,
          "Yes! Take each prime with its highest index: 2³, 3² and 5.", "جی ہاں! ہر مفرد عدد کی سب سے بڑی قوت لیں: 2³، 3² اور 5"),
      opt("hcf", "2 × 3 = 6", "2 × 3 = 6", False,
          "2 × 3 uses only the shared primes: that is the HCF. Take every prime with its highest index.", "2 × 3 میں صرف مشترک مفرد اعداد ہیں: یہ عاد اعظم ہے۔ ہر مفرد عدد کی سب سے بڑی قوت لیں۔", "shared_primes_only"),
      opt("all", "2⁴ × 3³ × 5 = 2160", "2⁴ × 3³ × 5 = 2160", False,
          "That multiplies the two numbers together. The LCM takes each prime once, with its highest index: 2³ × 3² × 5.", "یہ دونوں اعداد کا حاصل ضرب ہے۔ ذو اضعاف اقل میں ہر مفرد عدد ایک بار، سب سے بڑی قوت کے ساتھ: 2³ × 3² × 5", "always_multiply"),
      opt("low", "2 × 3 × 5 = 30", "2 × 3 × 5 = 30", False,
          "24 does not divide 30. Use the highest index of each prime: 2³ × 3² × 5.", "24، 30 کو تقسیم نہیں کرتا۔ ہر مفرد عدد کی سب سے بڑی قوت لیں: 2³ × 3² × 5")],
     qtype="recall"),
   number_question(
     "q3_primes",
     T("Find the LCM of 18 and 30 by prime factorisation.", "مفرد اجزائے ضربی سے 18 اور 30 کا ذو اضعاف اقل معلوم کریں۔"),
     Q3,
     T("18 = 2 × 3 × 3 and 30 = 2 × 3 × 5. Take each prime the most times it appears in either.", "18 = 2 × 3 × 3 اور 30 = 2 × 3 × 5۔ ہر مفرد عدد اتنی بار لیں جتنی بار وہ کسی ایک میں سب سے زیادہ آئے۔"),
     T("Right! 2 × 3 × 3 × 5 = 90.", "درست! 2 × 3 × 3 × 5 = 90"),
     T("One 2, two 3s (from 18) and one 5: 2 × 3 × 3 × 5 = 90.", "ایک 2، دو 3 (18 سے) اور ایک 5: 2 × 3 × 3 × 5 = 90"),
     common_wrong=[wrong(540, "540 = 18 × 30 is a common multiple, but 90 is lower.", "540 = 18 × 30 مشترک ضعف ہے، مگر 90 چھوٹا ہے۔", "always_multiply"),
                   wrong(6, "6 is the HCF (only the shared primes). The LCM is 90.", "6 عاد اعظم ہے (صرف مشترک مفرد اعداد)۔ ذو اضعاف اقل 90 ہے۔", "shared_primes_only")]),
   {"id": "s_division", "type": "explain",
    "character": say("talking", "The book also finds the LCM by the division method. Here is how it works.",
                     "کتاب ذو اضعاف اقل تقسیم کے طریقے سے بھی معلوم کرتی ہے۔ یہ ایسے ہوتا ہے۔"),
    "text": T("Division method: write the numbers in a row. Divide by a prime that goes into at least one of them; a number it doesn't divide is copied down as it is. Keep going until every number is 1. The LCM is all the divisors multiplied. For 12 and 15: divide by 2, 2, 3 and 5, so LCM = 2 × 2 × 3 × 5 = 60.",
              "تقسیم کا طریقہ: اعداد ایک قطار میں لکھیں۔ ایسے مفرد عدد سے تقسیم کریں جو کم از کم ایک کو تقسیم کرے؛ جو عدد تقسیم نہ ہو اسے ویسے ہی نیچے لکھ دیں۔ یہ تب تک کریں جب تک ہر عدد 1 نہ ہو جائے۔ سب تقسیم کرنے والے اعداد کا حاصل ضرب ذو اضعاف اقل ہے۔ 12 اور 15 کے لیے: 2، 2، 3 اور 5 سے تقسیم، اس لیے ذو اضعاف اقل = 2 × 2 × 3 × 5 = 60")},
   number_question(
     "q4_division",
     T("Use the division method to find the LCM of 16, 20 and 24.", "تقسیم کے طریقے سے 16، 20 اور 24 کا ذو اضعاف اقل معلوم کریں۔"),
     Q4,
     T("Divide by 2 while you can, then by 3 and 5. Multiply all the divisors.", "جب تک ہو سکے 2 سے تقسیم کریں، پھر 3 اور 5 سے۔ سب تقسیم کرنے والے اعداد ضرب دیں۔"),
     T("Right! 2 × 2 × 2 × 2 × 3 × 5 = 240.", "درست! 2 × 2 × 2 × 2 × 3 × 5 = 240"),
     T("The divisors are 2, 2, 2, 2, 3 and 5. LCM = 2⁴ × 3 × 5 = 240.", "تقسیم کرنے والے اعداد 2، 2، 2، 2، 3 اور 5 ہیں۔ ذو اضعاف اقل = 2⁴ × 3 × 5 = 240"),
     common_wrong=[wrong(7680, "7680 = 16 × 20 × 24 is a common multiple, but far from the lowest: 240.", "7680 = 16 × 20 × 24 مشترک ضعف ہے، مگر سب سے چھوٹا نہیں: 240", "always_multiply"),
                   wrong(4, "4 is the HCF. The LCM is the divisors multiplied: 240.", "4 عاد اعظم ہے۔ ذو اضعاف اقل تقسیم کرنے والے اعداد کا حاصل ضرب ہے: 240", "lcm_hcf_swap")]),
   number_question(
     "q5_three",
     T("Find the LCM of 9, 12 and 15.", "9، 12 اور 15 کا ذو اضعاف اقل معلوم کریں۔"),
     Q5,
     T("9 = 3 × 3, 12 = 2 × 2 × 3, 15 = 3 × 5. Take two 2s, two 3s and one 5.", "9 = 3 × 3، 12 = 2 × 2 × 3، 15 = 3 × 5۔ دو 2، دو 3 اور ایک 5 لیں۔"),
     T("Right! 2 × 2 × 3 × 3 × 5 = 180.", "درست! 2 × 2 × 3 × 3 × 5 = 180"),
     T("LCM = 2 × 2 × 3 × 3 × 5 = 180. Check: 180 ÷ 9 = 20, 180 ÷ 12 = 15, 180 ÷ 15 = 12.", "ذو اضعاف اقل = 2 × 2 × 3 × 3 × 5 = 180۔ جانچ: 180 ÷ 9 = 20، 180 ÷ 12 = 15، 180 ÷ 15 = 12"),
     common_wrong=[wrong(1620, "1620 = 9 × 12 × 15 is a common multiple, but 180 is lower.", "1620 = 9 × 12 × 15 مشترک ضعف ہے، مگر 180 چھوٹا ہے۔", "always_multiply"),
                   wrong(3, "3 is the HCF. The LCM is 180.", "3 عاد اعظم ہے۔ ذو اضعاف اقل 180 ہے۔", "lcm_hcf_swap")]),
   number_question(
     "q6_hops",
     T("Ayan hops along a number line from 0 in jumps of 4. Bela starts at 0 too and jumps 10 at a time. What is the first number after 0 that both land on?", "ایان عددی لکیر پر 0 سے 4، 4 کی چھلانگیں لگاتا ہے۔ بیلا بھی 0 سے شروع کرتی ہے اور 10، 10 کی چھلانگیں لگاتی ہے۔ 0 کے بعد پہلا عدد کون سا ہے جس پر دونوں پہنچیں؟"),
     Q6,
     T("Ayan lands on 4, 8, 12, 16, 20 ... Bela on 10, 20 ...", "ایان 4، 8، 12، 16، 20 ... پر آتا ہے۔ بیلا 10، 20 ... پر"),
     T("Right! LCM of 4 and 10 = 20.", "درست! 4 اور 10 کا ذو اضعاف اقل = 20"),
     T("20 is the first number in both lists: the LCM of 4 and 10.", "20 دونوں فہرستوں کا پہلا مشترک عدد ہے: 4 اور 10 کا ذو اضعاف اقل۔"),
     common_wrong=[wrong(40, "Both land on 40, but they meet earlier, at 20.", "دونوں 40 پر آتے ہیں، مگر پہلے 20 پر مل جاتے ہیں۔", "always_multiply"),
                   wrong(2, "2 is the HCF. Neither of them lands on 2.", "2 عاد اعظم ہے۔ دونوں میں سے کوئی 2 پر نہیں آتا۔", "lcm_hcf_swap")]),
   number_question(
     "q7_buses",
     T("Bus A leaves the stop every 25 minutes and bus B every 35 minutes. Both leave together at 7:00 in the morning. After how many minutes do they leave together again?", "بس A ہر 25 منٹ بعد اور بس B ہر 35 منٹ بعد اڈے سے چلتی ہے۔ صبح 7 بجے دونوں ساتھ چلیں۔ کتنے منٹ بعد دونوں دوبارہ ساتھ چلیں گی؟"),
     Q7,
     T("25 = 5 × 5 and 35 = 5 × 7. Find the LCM.", "25 = 5 × 5 اور 35 = 5 × 7۔ ذو اضعاف اقل معلوم کریں۔"),
     T("Right! 5 × 5 × 7 = 175 minutes.", "درست! 5 × 5 × 7 = 175 منٹ"),
     T("LCM = 5 × 5 × 7 = 175. They leave together again after 175 minutes.", "ذو اضعاف اقل = 5 × 5 × 7 = 175۔ دونوں 175 منٹ بعد دوبارہ ساتھ چلیں گی۔"),
     common_wrong=[wrong(5, "5 is the HCF. After 5 minutes neither bus has left again.", "5 عاد اعظم ہے۔ 5 منٹ بعد کوئی بس دوبارہ نہیں چلی۔", "lcm_hcf_swap"),
                   wrong(875, "875 = 25 × 35 is a common multiple, but they meet earlier, at 175.", "875 = 25 × 35 مشترک ضعف ہے، مگر وہ پہلے، 175 پر مل جاتی ہیں۔", "always_multiply")]),
   choice_question(
     "q8_bus_time",
     T("So at what time do the two buses leave together again?", "تو دونوں بسیں دوبارہ کس وقت ساتھ چلیں گی؟"),
     [opt("right", Q8_TIME, Q8_TIME, True, "Yes! 175 minutes = 2 hours 55 minutes, and 7:00 + 2:55 = 9:55.", "جی ہاں! 175 منٹ = 2 گھنٹے 55 منٹ، اور 7:00 + 2:55 = 9:55"),
      opt("hcf", clock(7, 0, 5), clock(7, 0, 5), False, "That is 5 minutes later, the HCF. They meet after 175 minutes: 9:55.", "یہ 5 منٹ بعد ہے، یعنی عاد اعظم۔ وہ 175 منٹ بعد ملیں گی: 9:55", "lcm_hcf_swap"),
      opt("hundred", clock(7, 0, 60 + 75), clock(7, 0, 60 + 75), False, "175 minutes is not 1 hour 75 minutes. 175 = 120 + 55, so 2 hours 55 minutes: 9:55.", "175 منٹ، 1 گھنٹہ 75 منٹ نہیں۔ 175 = 120 + 55، یعنی 2 گھنٹے 55 منٹ: 9:55"),
      opt("one_hour", clock(7, 0, 60), clock(7, 0, 60), False, "At 8:00 neither bus leaves: bus A leaves at 7:25, 7:50, 8:15 and bus B at 7:35, 8:10. They meet at 9:55.", "8 بجے کوئی بس نہیں چلتی: بس A 7:25، 7:50، 8:15 پر اور بس B 7:35، 8:10 پر چلتی ہے۔ وہ 9:55 پر ملیں گی۔")]),
   number_question(
     "q9_lights",
     T("Three traffic lights change every 40, 60 and 90 seconds. They change together now. After how many MINUTES will they change together again?", "تین ٹریفک بتیاں ہر 40، 60 اور 90 سیکنڈ بعد بدلتی ہیں۔ ابھی تینوں ساتھ بدلی ہیں۔ کتنے منٹ بعد دوبارہ ساتھ بدلیں گی؟"),
     Q9,
     T("First find the LCM of 40, 60 and 90 in seconds. Then divide by 60.", "پہلے 40، 60 اور 90 کا ذو اضعاف اقل سیکنڈوں میں نکالیں۔ پھر 60 سے تقسیم کریں۔"),
     T("Right! 360 seconds = 6 minutes.", "درست! 360 سیکنڈ = 6 منٹ"),
     T("LCM of 40, 60 and 90 = 360 seconds, and 360 ÷ 60 = 6 minutes.", "40، 60 اور 90 کا ذو اضعاف اقل = 360 سیکنڈ، اور 360 ÷ 60 = 6 منٹ"),
     common_wrong=[wrong(Q9_SECONDS, "360 is in seconds. The question asks for minutes: 360 ÷ 60 = 6.", "360 سیکنڈ ہیں۔ سوال منٹ پوچھتا ہے: 360 ÷ 60 = 6", "stops_early"),
                   wrong(10, "10 seconds is the HCF. The lights meet after 360 seconds, which is 6 minutes.", "10 سیکنڈ عاد اعظم ہے۔ بتیاں 360 سیکنڈ بعد ملتی ہیں، یعنی 6 منٹ۔", "lcm_hcf_swap")]),
   number_question(
     "q10_bells",
     T("Three bells ring every 12, 18 and 20 minutes. They ring together at 8:00. After how many HOURS will they ring together again?", "تین گھنٹیاں ہر 12، 18 اور 20 منٹ بعد بجتی ہیں۔ 8 بجے تینوں ساتھ بجیں۔ کتنے گھنٹے بعد دوبارہ ساتھ بجیں گی؟"),
     Q10,
     T("12 = 2² × 3, 18 = 2 × 3², 20 = 2² × 5. Find the LCM in minutes, then change to hours.", "12 = 2² × 3، 18 = 2 × 3²، 20 = 2² × 5۔ ذو اضعاف اقل منٹوں میں نکالیں، پھر گھنٹوں میں بدلیں۔"),
     T("Right! 180 minutes = 3 hours, so at 11:00.", "درست! 180 منٹ = 3 گھنٹے، یعنی 11 بجے۔"),
     T("LCM = 2² × 3² × 5 = 180 minutes = 3 hours. They ring together at 11:00.", "ذو اضعاف اقل = 2² × 3² × 5 = 180 منٹ = 3 گھنٹے۔ وہ 11 بجے ساتھ بجیں گی۔"),
     common_wrong=[wrong(Q10_MIN, "180 is in minutes. In hours: 180 ÷ 60 = 3.", "180 منٹ ہیں۔ گھنٹوں میں: 180 ÷ 60 = 3", "stops_early"),
                   wrong(11, "11:00 is the time they ring together. The question asks how many hours after 8:00: 3.", "11 بجے وہ وقت ہے جب وہ ساتھ بجیں گی۔ سوال پوچھتا ہے 8 بجے کے کتنے گھنٹے بعد: 3")]),
   number_question(
     "q11_sweets",
     T("A box of sweets can be shared equally among 8 children, or among 12, or among 18, with none left over. What is the smallest number of sweets the box can hold?", "مٹھائی کا ایک ڈبہ 8 بچوں میں، یا 12 میں، یا 18 میں برابر بانٹا جا سکتا ہے، کچھ نہیں بچتا۔ ڈبے میں کم از کم کتنی مٹھائیاں ہو سکتی ہیں؟"),
     Q11,
     T("The number must be a multiple of 8, 12 and 18. Find the LCM.", "تعداد 8، 12 اور 18 تینوں کا ضعف ہو۔ ذو اضعاف اقل معلوم کریں۔"),
     T("Right! 72 = 8 × 9 = 12 × 6 = 18 × 4.", "درست! 72 = 8 × 9 = 12 × 6 = 18 × 4"),
     T("8 = 2³, 12 = 2² × 3, 18 = 2 × 3². LCM = 2³ × 3² = 72.", "8 = 2³، 12 = 2² × 3، 18 = 2 × 3²۔ ذو اضعاف اقل = 2³ × 3² = 72"),
     common_wrong=[wrong(2, "2 is the HCF: 2 sweets can't be shared among 8 children. Use the LCM: 72.", "2 عاد اعظم ہے: 2 مٹھائیاں 8 بچوں میں نہیں بٹ سکتیں۔ ذو اضعاف اقل لیں: 72", "lcm_hcf_swap"),
                   wrong(144, "144 works, but 72 is smaller and works too.", "144 چل جاتا ہے، مگر 72 چھوٹا ہے اور وہ بھی چلتا ہے۔")]),
   choice_question(
     "q12_find_error",
     T("Kashif says the LCM of 12 and 16 is 12 × 16 = 192. What went wrong?", "کاشف کہتا ہے 12 اور 16 کا ذو اضعاف اقل 12 × 16 = 192 ہے۔ کیا غلطی ہوئی؟"),
     [opt("not_lowest", "192 is a common multiple but not the lowest. 48 is: 48 ÷ 12 = 4 and 48 ÷ 16 = 3.", "192 مشترک ضعف ہے مگر سب سے چھوٹا نہیں۔ 48 ہے: 48 ÷ 12 = 4 اور 48 ÷ 16 = 3", True,
          "Yes! Multiplying only gives the LCM when the HCF is 1. Here the HCF is 4, so 192 ÷ 4 = 48.", "جی ہاں! ضرب سے ذو اضعاف اقل صرف تب ملتا ہے جب عاد اعظم 1 ہو۔ یہاں عاد اعظم 4 ہے، اس لیے 192 ÷ 4 = 48"),
      opt("hcf", "He should find the HCF, 4.", "اسے عاد اعظم، 4، نکالنا تھا۔", False,
          "The question asks for the LCM. It is 48, not 192 and not 4.", "سوال ذو اضعاف اقل پوچھتا ہے۔ یہ 48 ہے، نہ 192 نہ 4۔", "lcm_hcf_swap"),
      opt("nothing", "Nothing. The LCM is 192.", "کوئی غلطی نہیں۔ ذو اضعاف اقل 192 ہے۔", False,
          "Check 48: 48 ÷ 12 = 4 and 48 ÷ 16 = 3. 48 is a smaller common multiple.", "48 جانچیں: 48 ÷ 12 = 4 اور 48 ÷ 16 = 3۔ 48 ایک چھوٹا مشترک ضعف ہے۔", "always_multiply")],
     qtype="find_error"),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Brilliant! Buses, bells and lights all meet at the LCM.", "زبردست! بسیں، گھنٹیاں اور بتیاں سب ذو اضعاف اقل پر ملتی ہیں۔"),
    "text": T("LCM by prime factorisation: take every prime with its highest index. LCM by division: divide by primes until every number is 1, then multiply the divisors. When things repeat every so often, they happen together again after the LCM.",
              "مفرد اجزائے ضربی سے ذو اضعاف اقل: ہر مفرد عدد اس کی سب سے بڑی قوت کے ساتھ لیں۔ تقسیم کے طریقے سے: مفرد اعداد سے تقسیم کریں یہاں تک کہ ہر عدد 1 ہو جائے، پھر تقسیم کرنے والے اعداد ضرب دیں۔ جب چیزیں وقفے وقفے سے ہوں، تو وہ ذو اضعاف اقل کے بعد دوبارہ ساتھ ہوتی ہیں۔"),
    "points": [T("The LCM is never smaller than the biggest number.", "ذو اضعاف اقل سب سے بڑے عدد سے چھوٹا نہیں ہوتا۔"),
               T("Check the units: change seconds to minutes or minutes to hours if the question asks.", "اکائیاں دیکھیں: اگر سوال کہے تو سیکنڈ کو منٹ یا منٹ کو گھنٹے میں بدلیں۔")]},
 ],
 bank=[
   {"id": "qb_lcm", "type": "recall", "step": number_question(
     "qb_lcm",
     T("Find the LCM of 6 and 15.", "6 اور 15 کا ذو اضعاف اقل معلوم کریں۔"),
     QB_REC,
     T("Multiples of 15: 15, 30, 45 ... Which does 6 divide?", "15 کے اضعاف: 15، 30، 45 ... ان میں سے کسے 6 تقسیم کرتا ہے؟"),
     T("Right! LCM = 30.", "درست! ذو اضعاف اقل = 30"),
     T("15 ÷ 6 is not exact, but 30 ÷ 6 = 5. LCM = 30.", "15 ÷ 6 پورا تقسیم نہیں ہوتا، مگر 30 ÷ 6 = 5۔ ذو اضعاف اقل = 30"),
     common_wrong=[wrong(90, "90 = 6 × 15 is a common multiple, but 30 is lower.", "90 = 6 × 15 مشترک ضعف ہے، مگر 30 چھوٹا ہے۔", "always_multiply"),
                   wrong(3, "3 is the HCF. The LCM is 30.", "3 عاد اعظم ہے۔ ذو اضعاف اقل 30 ہے۔", "lcm_hcf_swap")],
     qtype=None)},
   {"id": "qb_meet", "type": "apply", "step": number_question(
     "qb_meet",
     T("Two runners go round a track. One takes 45 seconds a lap, the other 60 seconds. They start together. After how many seconds are they at the start together again?", "دو دوڑنے والے ایک ٹریک کے چکر لگاتے ہیں۔ ایک کو ایک چکر میں 45 سیکنڈ لگتے ہیں، دوسرے کو 60 سیکنڈ۔ دونوں ساتھ شروع کرتے ہیں۔ کتنے سیکنڈ بعد دونوں دوبارہ ساتھ شروع کی جگہ پر ہوں گے؟"),
     QB_APP,
     T("45 = 3² × 5 and 60 = 2² × 3 × 5. Find the LCM.", "45 = 3² × 5 اور 60 = 2² × 3 × 5۔ ذو اضعاف اقل معلوم کریں۔"),
     T("Right! 2² × 3² × 5 = 180 seconds.", "درست! 2² × 3² × 5 = 180 سیکنڈ"),
     T("LCM = 2² × 3² × 5 = 180. The first runner has done 4 laps and the second 3.", "ذو اضعاف اقل = 2² × 3² × 5 = 180۔ پہلے نے 4 چکر لگائے اور دوسرے نے 3"),
     common_wrong=[wrong(15, "15 is the HCF. After 15 seconds no one has finished a lap.", "15 عاد اعظم ہے۔ 15 سیکنڈ بعد کسی کا چکر پورا نہیں ہوا۔", "lcm_hcf_swap")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": choice_question(
     "qb_find_error",
     T("10 = 2 × 5 and 14 = 2 × 7. Nida says the LCM is 2, because 2 is the prime they share. What went wrong?", "10 = 2 × 5 اور 14 = 2 × 7۔ ندا کہتی ہے ذو اضعاف اقل 2 ہے، کیونکہ 2 مشترک مفرد عدد ہے۔ کیا غلطی ہوئی؟"),
     [opt("all_primes", "The LCM uses every prime: 2 × 5 × 7 = 70. The shared prime gives the HCF.", "ذو اضعاف اقل میں سب مفرد اعداد آتے ہیں: 2 × 5 × 7 = 70۔ مشترک مفرد عدد عاد اعظم دیتا ہے۔", True,
          "Yes! 70 ÷ 10 = 7 and 70 ÷ 14 = 5.", "جی ہاں! 70 ÷ 10 = 7 اور 70 ÷ 14 = 5"),
      opt("multiply", "The LCM is 10 × 14 = 140.", "ذو اضعاف اقل 10 × 14 = 140 ہے۔", False,
          "140 is a common multiple, but 70 is lower.", "140 مشترک ضعف ہے، مگر 70 چھوٹا ہے۔", "always_multiply"),
      opt("nothing", "Nothing. The LCM is 2.", "کوئی غلطی نہیں۔ ذو اضعاف اقل 2 ہے۔", False,
          "The LCM can't be smaller than 14. Use every prime: 2 × 5 × 7 = 70.", "ذو اضعاف اقل 14 سے چھوٹا نہیں ہو سکتا۔ سب مفرد اعداد لیں: 2 × 5 × 7 = 70", "shared_primes_only")],
     qtype=None)},
 ],
 review=[
   {"id": "r_lcm", "type": "recall", "step": number_question(
     "r_lcm",
     T("Find the LCM of 14 and 21.", "14 اور 21 کا ذو اضعاف اقل معلوم کریں۔"),
     R1,
     T("14 = 2 × 7 and 21 = 3 × 7.", "14 = 2 × 7 اور 21 = 3 × 7"),
     T("Right! 2 × 3 × 7 = 42.", "درست! 2 × 3 × 7 = 42"),
     T("LCM = 2 × 3 × 7 = 42.", "ذو اضعاف اقل = 2 × 3 × 7 = 42"),
     common_wrong=[wrong(294, "294 = 14 × 21 is a common multiple, but 42 is lower.", "294 = 14 × 21 مشترک ضعف ہے، مگر 42 چھوٹا ہے۔", "always_multiply"),
                   wrong(7, "7 is the HCF. The LCM is 42.", "7 عاد اعظم ہے۔ ذو اضعاف اقل 42 ہے۔", "lcm_hcf_swap")],
     qtype=None)},
   {"id": "r_lamps", "type": "apply", "step": number_question(
     "r_lamps",
     T("Two lamps blink every 6 and every 8 seconds. They blink together now. After how many seconds will they blink together again?", "دو چراغ ہر 6 اور ہر 8 سیکنڈ بعد جلتے ہیں۔ ابھی دونوں ساتھ جلے ہیں۔ کتنے سیکنڈ بعد دوبارہ ساتھ جلیں گے؟"),
     R2,
     T("Find the LCM of 6 and 8.", "6 اور 8 کا ذو اضعاف اقل معلوم کریں۔"),
     T("Right! 24 seconds.", "درست! 24 سیکنڈ"),
     T("Multiples of 8: 8, 16, 24. 24 ÷ 6 = 4, so 24 seconds.", "8 کے اضعاف: 8، 16، 24۔ 24 ÷ 6 = 4، اس لیے 24 سیکنڈ۔"),
     common_wrong=[wrong(48, "48 = 6 × 8 works, but they meet earlier, at 24.", "48 = 6 × 8 بھی چلتا ہے، مگر وہ پہلے، 24 پر مل جاتے ہیں۔", "always_multiply")],
     qtype=None)},
 ],
 glossary=[T("Lowest common multiple (LCM)", "ذو اضعاف اقل"), T("Common multiple", "مشترک ضعف"), T("Division method", "تقسیم کا طریقہ")],
 flashcards=[
   {"id": "f_division", "front": T("How does the division method find the LCM?", "تقسیم کا طریقہ ذو اضعاف اقل کیسے معلوم کرتا ہے؟"),
    "back": T("Divide the numbers by primes, copying down any number that doesn't divide, until all are 1. Multiply the divisors. 12 and 15: 2 × 2 × 3 × 5 = 60.", "اعداد کو مفرد اعداد سے تقسیم کریں، جو تقسیم نہ ہو اسے ویسے ہی نیچے لکھیں، یہاں تک کہ سب 1 ہو جائیں۔ تقسیم کرنے والے اعداد ضرب دیں۔ 12 اور 15: 2 × 2 × 3 × 5 = 60")},
   {"id": "f_meet", "front": T("Two things repeat every 25 and 35 minutes. When do they happen together again?", "دو چیزیں ہر 25 اور 35 منٹ بعد ہوتی ہیں۔ دوبارہ کب ساتھ ہوں گی؟"),
    "back": T("After the LCM: 175 minutes.", "ذو اضعاف اقل کے بعد: 175 منٹ۔")},
 ],
 home_task={"id": "h_timetable", "text": T(
   "Think of two things that repeat, like a wall clock that chimes every hour and a TV advert that comes every 20 minutes. Make up the times, then find when they happen together again.",
   "دو ایسی چیزیں سوچیں جو بار بار ہوں، جیسے دیوار کی گھڑی کا ہر گھنٹے بجنا اور کسی ٹی وی اشتہار کا ہر 20 منٹ بعد آنا۔ وقت خود بنائیں، پھر معلوم کریں کہ وہ دوبارہ کب ساتھ ہوں گی۔")},
 notes=["Covers LCM by listing and prime factorisation (q1 to q3, q5), the division method (s_division, q4), and when-do-they-meet-again problems with jumps (q6), buses (q7, q8), traffic lights (q9), bells (q10) and sharing (q11).",
        "The division method for the LCM is not taught in the unit's LCM lesson, so s_division shows it once before q4.",
        "Urdu terms to check: تقسیم کا طریقہ (division method), ٹریفک بتیاں (traffic lights)."],
 minutes=20,
)

attach(lesson, {
    "s_division": division_ladder(D_EX, R_EX,
        "The division method for 12 and 15. On the left the primes 2, 2, 3, 5. The rows are 12 and 15; 6 and 15; 3 and 15; 1 and 5; and finally 1 and 1. A number that a prime does not divide is copied down.",
        "12 اور 15 کے لیے تقسیم کا طریقہ۔ بائیں طرف مفرد اعداد 2، 2، 3، 5۔ قطاریں: 12 اور 15؛ 6 اور 15؛ 3 اور 15؛ 1 اور 5؛ اور آخر میں 1 اور 1۔ جو عدد تقسیم نہ ہو اسے ویسے ہی نیچے لکھا گیا ہے۔"),
    "q4_division": division_ladder(D4[:2], R4[:3],
        "The start of the division method for 16, 20 and 24. Divided by 2: 8, 10, 12. Divided by 2 again: 4, 5, 6.",
        "16، 20 اور 24 کے لیے تقسیم کے طریقے کا آغاز۔ 2 سے تقسیم: 8، 10، 12۔ پھر 2 سے تقسیم: 4، 5، 6۔"),
    "q6_hops": multiples_rows(4, 10, 40,
        "Two number lines from 0 to 40. Top: Ayan's jumps of 4 landing on 4, 8, 12 ... 40. Bottom: Bela's jumps of 10 landing on 10, 20, 30, 40.",
        "0 سے 40 تک دو عددی لکیریں۔ اوپر: ایان کی 4 کی چھلانگیں جو 4، 8، 12 ... 40 پر آتی ہیں۔ نیچے: بیلا کی 10 کی چھلانگیں جو 10، 20، 30، 40 پر آتی ہیں۔", ring=False),
})
write(lesson)
