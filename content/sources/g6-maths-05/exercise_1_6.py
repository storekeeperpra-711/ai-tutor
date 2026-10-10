"""Practice set for Exercise 1.6 of the book: pick out perfect squares and
find squares of numbers, including negative numbers. The questions are
new; only the kinds of question follow the book."""
from math import isqrt

from common import (T, opt, say, wrong, number_question, choice_question, practice_lesson,
                    practice_intro, write, prime_factors, EX_SKILL, FM_INDEX)
from figs import attach, floor_figure

SKILL = EX_SKILL["1.6"]


def is_square(n):
    return n >= 0 and isqrt(n) ** 2 == n


# q1: 8²
Q1 = 8 ** 2
assert Q1 == 64 and 8 * 2 == 16 and 8 + 8 == 16
# q2: which is a perfect square: 50, 63, 121, 140
Q2_OPTS = (50, 63, 121, 140)
assert [n for n in Q2_OPTS if is_square(n)] == [121] and 121 == 11 * 11
assert 7 * 7 < 50 < 8 * 8 and 7 * 7 < 63 < 8 * 8 and 11 * 11 < 140 < 12 * 12
# q3: perfect squares from 1 to 100
SQ100 = [n for n in range(1, 101) if is_square(n)]
Q3 = len(SQ100)
assert SQ100 == [k * k for k in range(1, 11)] and Q3 == 10
# q4: 15²
Q4 = 15 ** 2
assert Q4 == 225 and 15 * 2 == 30 and 10 * 10 + 5 * 5 == 125
# s_negative: (−5)² = 25
assert (-5) ** 2 == 25 and -(5 ** 2) == -25
# q5: (−6)²
Q5 = (-6) ** 2
assert Q5 == 36 and -(6 ** 2) == -36 and -6 * 2 == -12
# q6: (−9)²
assert (-9) ** 2 == 81 and -(9 ** 2) == -81 and -9 * 2 == -18
# q7: 20²
Q7 = 20 ** 2
assert Q7 == 400 and 20 * 2 == 40 and 2 * 2 * 10 == 40
# q8: which positive number squared gives 144
Q8 = isqrt(144)
assert Q8 == 12 and Q8 ** 2 == 144 and 144 // 2 == 72
# q9: is 180 a perfect square
assert prime_factors(180) == [2, 2, 3, 3, 5] and not is_square(180) and 13 ** 2 < 180 < 14 ** 2
# q10: 324 = 2² × 3⁴
assert 324 == 2 ** 2 * 3 ** 4 and prime_factors(324) == [2, 2, 3, 3, 3, 3]
Q10 = 2 * 3 ** 2
assert Q10 == 18 and Q10 ** 2 == 324 and 324 // 2 == 162
# q11: square garden, side 13 m
Q11 = 13 ** 2
assert Q11 == 169 and 13 * 4 == 52 and 13 * 2 == 26
# q12: (−1)² + (−2)² + (−3)²
Q12 = (-1) ** 2 + (-2) ** 2 + (-3) ** 2
assert Q12 == 14 and -(1 + 4 + 9) == -14 and (-1 - 2 - 3) ** 2 == 36
# find error: (−7)² is not −49
assert (-7) ** 2 == 49 and -(7 ** 2) == -49
# question bank
QB_REC = 11 ** 2
assert QB_REC == 121 and 11 * 2 == 22
QB_APP = (-12) ** 2
assert QB_APP == 144 and -(12 ** 2) == -144
assert 6 ** 2 == 36 and 6 * 2 == 12
# review
R1 = 14 ** 2
assert R1 == 196 and 14 * 2 == 28
R2_OPTS = (48, 72, 81, 90)
assert [n for n in R2_OPTS if is_square(n)] == [81]


lesson = practice_lesson(
 "1.6", script="exercise_1_6.py",
 title=T("Exercise 1.6 practice: square numbers", "مشق 1.6 کی پریکٹس: مربع اعداد"),
 outcome="Find the squares of numbers up to 2 digits, including negative numbers, and tell whether a number is a perfect square.",
 prerequisites=[FM_INDEX],
 misconceptions=[
   {"id": "times_two", "description": "Doubles the number instead of squaring it: 8² = 16."},
   {"id": "negative_square", "description": "Thinks the square of a negative number is negative: (−7)² = −49."},
   {"id": "half_root", "description": "Halves a number to find what was squared: 144 = 72²."},
 ],
 steps=[
   practice_intro("1.6",
     "Here you find squares of numbers, including negative numbers, and pick out perfect squares.",
     "اس میں آپ اعداد کے مربع معلوم کریں گے، منفی اعداد کے بھی، اور مکمل مربع اعداد پہچانیں گے۔",
     "Exercise 1.6 is about squares. A number times itself!",
     "مشق 1.6 مربع کے بارے میں ہے۔ عدد کو خود سے ضرب!"),
   number_question(
     "q1_square",
     T("Find 8².", "8² معلوم کریں۔"),
     Q1,
     T("8² means 8 × 8.", "8² کا مطلب 8 × 8 ہے۔"),
     T("Right! 8 × 8 = 64.", "درست! 8 × 8 = 64"),
     T("8² = 8 × 8 = 64.", "8² = 8 × 8 = 64"),
     common_wrong=[wrong(16, "That is 8 × 2. Squaring means 8 × 8 = 64.", "یہ 8 × 2 ہے۔ مربع کا مطلب 8 × 8 = 64", "times_two")],
     qtype="recall"),
   choice_question(
     "q2_which_square",
     T("Which of these is a perfect square?", "ان میں سے کون سا مکمل مربع عدد ہے؟"),
     [opt("n50", "50", "50", False, "7² = 49 and 8² = 64, so 50 is between two squares.", "7² = 49 اور 8² = 64، اس لیے 50 دو مربعوں کے بیچ میں ہے۔"),
      opt("n63", "63", "63", False, "7² = 49 and 8² = 64. 63 is just under 64, but not a square.", "7² = 49 اور 8² = 64۔ 63، 64 سے ذرا کم ہے، مگر مربع نہیں۔"),
      opt("n121", "121", "121", True, "Yes! 11 × 11 = 121.", "جی ہاں! 11 × 11 = 121"),
      opt("n140", "140", "140", False, "11² = 121 and 12² = 144, so 140 is not a square.", "11² = 121 اور 12² = 144، اس لیے 140 مربع نہیں۔")],
     qtype="recall"),
   number_question(
     "q3_count",
     T("How many perfect squares are there from 1 to 100?", "1 سے 100 تک کتنے مکمل مربع اعداد ہیں؟"),
     Q3,
     T("1² = 1, 2² = 4, 3² = 9 ... Which is the last square that is not more than 100?", "1² = 1، 2² = 4، 3² = 9 ... آخری مربع کون سا ہے جو 100 سے زیادہ نہ ہو؟"),
     T("Right! 1², 2², ... 10²: ten squares.", "درست! 1²، 2²، ... 10²: دس مربع۔"),
     T("1, 4, 9, 16, 25, 36, 49, 64, 81, 100: these are 1² to 10², so there are 10.", "1، 4، 9، 16، 25، 36، 49، 64، 81، 100: یہ 1² سے 10² تک ہیں، اس لیے 10 ہیں۔"),
     common_wrong=[wrong(9, "Don't forget 100 = 10². There are 10.", "100 = 10² کو نہ بھولیں۔ کل 10 ہیں۔"),
                   wrong(50, "Only a few numbers are squares. They are 1², 2², ... 10²: 10 of them.", "صرف چند اعداد مربع ہوتے ہیں۔ یہ 1²، 2²، ... 10² ہیں: کل 10", "half_root")]),
   number_question(
     "q4_fifteen",
     T("Find 15².", "15² معلوم کریں۔"),
     Q4,
     T("15 × 15 = 15 × 10 + 15 × 5.", "15 × 15 = 15 × 10 + 15 × 5"),
     T("Right! 150 + 75 = 225.", "درست! 150 + 75 = 225"),
     T("15 × 10 = 150 and 15 × 5 = 75, so 15² = 225.", "15 × 10 = 150 اور 15 × 5 = 75، اس لیے 15² = 225"),
     common_wrong=[wrong(30, "That is 15 × 2. Squaring means 15 × 15 = 225.", "یہ 15 × 2 ہے۔ مربع کا مطلب 15 × 15 = 225", "times_two"),
                   wrong(125, "That is 10² + 5². Multiply the whole number: 15 × 15 = 225.", "یہ 10² + 5² ہے۔ پورے عدد کو ضرب دیں: 15 × 15 = 225")]),
   {"id": "s_negative", "type": "explain",
    "character": say("thinking", "What about a negative number times itself? Let's see.",
                     "منفی عدد کو خود سے ضرب دیں تو کیا ہوتا ہے؟ آئیں دیکھیں۔"),
    "text": T("(−5)² means (−5) × (−5). A negative times a negative is positive, so (−5)² = 25. The square of any number, positive or negative, is never negative. Be careful with brackets: (−5)² = 25, but −5² means −(5 × 5) = −25.",
              "(−5)² کا مطلب (−5) × (−5) ہے۔ منفی ضرب منفی مثبت ہوتا ہے، اس لیے (−5)² = 25۔ کسی بھی عدد کا مربع، مثبت ہو یا منفی، کبھی منفی نہیں ہوتا۔ قوسین کا خیال رکھیں: (−5)² = 25، مگر −5² کا مطلب −(5 × 5) = −25")},
   number_question(
     "q5_negative",
     T("Find (−6)².", "(−6)² معلوم کریں۔"),
     Q5,
     T("(−6) × (−6). Negative times negative is positive.", "(−6) × (−6)۔ منفی ضرب منفی مثبت ہوتا ہے۔"),
     T("Right! (−6) × (−6) = 36.", "درست! (−6) × (−6) = 36"),
     T("(−6)² = (−6) × (−6) = 36, a positive number.", "(−6)² = (−6) × (−6) = 36، ایک مثبت عدد۔"),
     common_wrong=[wrong(-36, "A negative times a negative is positive: (−6) × (−6) = 36.", "منفی ضرب منفی مثبت ہوتا ہے: (−6) × (−6) = 36", "negative_square"),
                   wrong(-12, "That is −6 × 2. Squaring means (−6) × (−6) = 36.", "یہ −6 × 2 ہے۔ مربع کا مطلب (−6) × (−6) = 36", "times_two")]),
   choice_question(
     "q6_negative_choice",
     T("What is (−9)²?", "(−9)² کیا ہے؟"),
     [opt("p81", "81", "81", True, "Yes! (−9) × (−9) = 81.", "جی ہاں! (−9) × (−9) = 81"),
      opt("m81", "−81", "−81", False, "Two negatives multiplied make a positive: (−9) × (−9) = 81.", "دو منفی اعداد کا حاصل ضرب مثبت ہوتا ہے: (−9) × (−9) = 81", "negative_square"),
      opt("m18", "−18", "−18", False, "That is −9 × 2. Square means (−9) × (−9) = 81.", "یہ −9 × 2 ہے۔ مربع کا مطلب (−9) × (−9) = 81", "times_two"),
      opt("p18", "18", "18", False, "18 is 9 × 2. Square means (−9) × (−9) = 81.", "18، 9 × 2 ہے۔ مربع کا مطلب (−9) × (−9) = 81", "times_two")]),
   number_question(
     "q7_twenty",
     T("Find the square of 20.", "20 کا مربع معلوم کریں۔"),
     Q7,
     T("20 × 20 = 2 × 2 × 10 × 10.", "20 × 20 = 2 × 2 × 10 × 10"),
     T("Right! 20² = 400.", "درست! 20² = 400"),
     T("20 × 20 = 4 × 100 = 400.", "20 × 20 = 4 × 100 = 400"),
     common_wrong=[wrong(40, "That is 20 × 2. Square means 20 × 20 = 400.", "یہ 20 × 2 ہے۔ مربع کا مطلب 20 × 20 = 400", "times_two")]),
   number_question(
     "q8_root",
     T("Which positive number, multiplied by itself, gives 144?", "کون سا مثبت عدد خود سے ضرب ہو کر 144 دیتا ہے؟"),
     Q8,
     T("10 × 10 = 100 is too small. Try a little bigger.", "10 × 10 = 100 بہت کم ہے۔ تھوڑا بڑا آزمائیں۔"),
     T("Right! 12 × 12 = 144.", "درست! 12 × 12 = 144"),
     T("11 × 11 = 121 and 12 × 12 = 144, so the number is 12.", "11 × 11 = 121 اور 12 × 12 = 144، اس لیے عدد 12 ہے۔"),
     common_wrong=[wrong(72, "72 × 72 is much more than 144. 144 ÷ 2 = 72 halves it; we need 12 × 12 = 144.", "72 × 72، 144 سے بہت زیادہ ہے۔ 144 ÷ 2 = 72 تو آدھا ہے؛ ہمیں 12 × 12 = 144 چاہیے۔", "half_root")]),
   choice_question(
     "q9_is_square",
     T("180 = 2 × 2 × 3 × 3 × 5. Is 180 a perfect square?", "180 = 2 × 2 × 3 × 3 × 5۔ کیا 180 مکمل مربع عدد ہے؟"),
     [opt("no", "No, because the 5 has no partner to pair with.", "نہیں، کیونکہ 5 کا کوئی جوڑا نہیں۔", True,
          "Yes! In a perfect square every prime comes in pairs. 13² = 169 and 14² = 196, so 180 is between them.", "جی ہاں! مکمل مربع میں ہر مفرد عدد جوڑوں میں آتا ہے۔ 13² = 169 اور 14² = 196، اس لیے 180 ان کے بیچ میں ہے۔"),
      opt("yes_even", "Yes, because 180 is even.", "ہاں، کیونکہ 180 جفت ہے۔", False,
          "Being even doesn't make a square: 2, 8 and 180 are even but not squares. The 5 has no partner.", "جفت ہونے سے مربع نہیں بنتا: 2، 8 اور 180 جفت ہیں مگر مربع نہیں۔ 5 کا کوئی جوڑا نہیں۔"),
      opt("yes_pairs", "Yes, because it has two 2s.", "ہاں، کیونکہ اس میں دو 2 ہیں۔", False,
          "The 2s and 3s pair up, but the 5 is alone, so 180 is not a square.", "2 اور 3 کے جوڑے بن جاتے ہیں، مگر 5 اکیلا ہے، اس لیے 180 مربع نہیں۔")]),
   number_question(
     "q10_from_primes",
     T("324 = 2² × 3⁴, and 324 is a perfect square. Which number squared gives 324?", "324 = 2² × 3⁴، اور 324 مکمل مربع عدد ہے۔ کس عدد کا مربع 324 ہے؟"),
     Q10,
     T("Split the primes into two equal groups: 2 × 3 × 3 and 2 × 3 × 3.", "مفرد اعداد کو دو برابر حصوں میں بانٹیں: 2 × 3 × 3 اور 2 × 3 × 3"),
     T("Right! 2 × 3 × 3 = 18, and 18 × 18 = 324.", "درست! 2 × 3 × 3 = 18، اور 18 × 18 = 324"),
     T("324 = (2 × 3 × 3) × (2 × 3 × 3) = 18 × 18, so the number is 18.", "324 = (2 × 3 × 3) × (2 × 3 × 3) = 18 × 18، اس لیے عدد 18 ہے۔"),
     common_wrong=[wrong(162, "162 is half of 324. We need a number times itself: 18 × 18 = 324.", "162، 324 کا آدھا ہے۔ ہمیں عدد ضرب خود چاہیے: 18 × 18 = 324", "half_root")]),
   number_question(
     "q11_garden",
     T("A square garden has sides of 13 m. What is its area in square metres?", "ایک مربع باغ کا ہر ضلع 13 میٹر ہے۔ اس کا رقبہ کتنے مربع میٹر ہے؟"),
     Q11,
     T("Area of a square = side × side = 13².", "مربع کا رقبہ = ضلع × ضلع = 13²"),
     T("Right! 13 × 13 = 169 square metres.", "درست! 13 × 13 = 169 مربع میٹر"),
     T("13² = 13 × 13 = 169.", "13² = 13 × 13 = 169"),
     common_wrong=[wrong(52, "52 = 4 × 13 is the distance round the garden. The area is 13 × 13 = 169.", "52 = 4 × 13 باغ کا گھیر ہے۔ رقبہ 13 × 13 = 169 ہے۔"),
                   wrong(26, "That is 13 × 2. The area is 13 × 13 = 169.", "یہ 13 × 2 ہے۔ رقبہ 13 × 13 = 169 ہے۔", "times_two")]),
   number_question(
     "q12_sum_negatives",
     T("Work out (−1)² + (−2)² + (−3)².", "(−1)² + (−2)² + (−3)² معلوم کریں۔"),
     Q12,
     T("Square each one first. Each square is positive.", "پہلے ہر ایک کا مربع نکالیں۔ ہر مربع مثبت ہے۔"),
     T("Right! 1 + 4 + 9 = 14.", "درست! 1 + 4 + 9 = 14"),
     T("(−1)² = 1, (−2)² = 4, (−3)² = 9, and 1 + 4 + 9 = 14.", "(−1)² = 1، (−2)² = 4، (−3)² = 9، اور 1 + 4 + 9 = 14"),
     common_wrong=[wrong(-14, "Each square is positive: 1 + 4 + 9 = 14.", "ہر مربع مثبت ہے: 1 + 4 + 9 = 14", "negative_square"),
                   wrong(36, "Square each number on its own, then add: 1 + 4 + 9 = 14.", "ہر عدد کا الگ مربع نکالیں، پھر جمع کریں: 1 + 4 + 9 = 14")]),
   choice_question(
     "q13_find_error",
     T("Rabia says (−7)² = −49 because the number is negative. What went wrong?", "رابعہ کہتی ہے (−7)² = −49 کیونکہ عدد منفی ہے۔ کیا غلطی ہوئی؟"),
     [opt("positive", "(−7) × (−7) is negative times negative, which is positive: 49.", "(−7) × (−7) منفی ضرب منفی ہے، جو مثبت ہوتا ہے: 49", True,
          "Yes! The square of any number is never negative.", "جی ہاں! کسی بھی عدد کا مربع کبھی منفی نہیں ہوتا۔"),
      opt("fourteen", "It should be −14.", "یہ −14 ہونا چاہیے۔", False,
          "−14 is −7 × 2. Squaring means (−7) × (−7) = 49.", "−14، −7 × 2 ہے۔ مربع کا مطلب (−7) × (−7) = 49", "times_two"),
      opt("nothing", "Nothing. (−7)² = −49.", "کوئی غلطی نہیں۔ (−7)² = −49", False,
          "(−7) × (−7): two negatives make a positive, so 49.", "(−7) × (−7): دو منفی مل کر مثبت بناتے ہیں، اس لیے 49", "negative_square")],
     qtype="find_error"),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! You have squared big, small and negative numbers.", "شاباش! آپ نے بڑے، چھوٹے اور منفی اعداد کے مربع نکال لیے۔"),
    "text": T("The square of a number is the number times itself: 15² = 15 × 15 = 225. A perfect square is the square of a whole number, like 1, 4, 9, 16 ... 100, 121, 144. The square of a negative number is positive: (−6)² = 36. In a perfect square, the prime factors come in pairs.",
              "کسی عدد کا مربع وہ عدد ضرب خود ہے: 15² = 15 × 15 = 225۔ مکمل مربع کسی پورے عدد کا مربع ہوتا ہے، جیسے 1، 4، 9، 16 ... 100، 121، 144۔ منفی عدد کا مربع مثبت ہوتا ہے: (−6)² = 36۔ مکمل مربع میں مفرد اجزائے ضربی جوڑوں میں آتے ہیں۔"),
    "points": [T("8² means 8 × 8, not 8 × 2.", "8² کا مطلب 8 × 8 ہے، 8 × 2 نہیں۔"),
               T("(−5)² = 25, but −5² = −25.", "(−5)² = 25، مگر −5² = −25")]},
 ],
 bank=[
   {"id": "qb_square", "type": "recall", "step": number_question(
     "qb_square",
     T("Find 11².", "11² معلوم کریں۔"),
     QB_REC,
     T("11 × 11.", "11 × 11"),
     T("Right! 11 × 11 = 121.", "درست! 11 × 11 = 121"),
     T("11² = 11 × 11 = 121.", "11² = 11 × 11 = 121"),
     common_wrong=[wrong(22, "That is 11 × 2. Square means 11 × 11 = 121.", "یہ 11 × 2 ہے۔ مربع کا مطلب 11 × 11 = 121", "times_two")],
     qtype=None)},
   {"id": "qb_negative", "type": "apply", "step": number_question(
     "qb_negative",
     T("Find (−12)².", "(−12)² معلوم کریں۔"),
     QB_APP,
     T("(−12) × (−12). Negative times negative is positive.", "(−12) × (−12)۔ منفی ضرب منفی مثبت ہوتا ہے۔"),
     T("Right! 144.", "درست! 144"),
     T("(−12) × (−12) = 144.", "(−12) × (−12) = 144"),
     common_wrong=[wrong(-144, "Two negatives multiplied make a positive: 144.", "دو منفی اعداد کا حاصل ضرب مثبت ہوتا ہے: 144", "negative_square")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": choice_question(
     "qb_find_error",
     T("Hassan says 6² = 12. What went wrong?", "حسن کہتا ہے 6² = 12۔ کیا غلطی ہوئی؟"),
     [opt("times", "He did 6 × 2. 6² means 6 × 6 = 36.", "اس نے 6 × 2 کیا۔ 6² کا مطلب 6 × 6 = 36", True,
          "Yes! The 2 tells you how many 6s to multiply.", "جی ہاں! 2 بتاتا ہے کہ کتنے 6 ضرب کرنے ہیں۔"),
      opt("add", "He should add 6 + 6.", "اسے 6 + 6 جمع کرنا تھا۔", False,
          "6 + 6 is also 12. Square means multiply: 6 × 6 = 36.", "6 + 6 بھی 12 ہے۔ مربع کا مطلب ضرب: 6 × 6 = 36"),
      opt("nothing", "Nothing. 6² = 12.", "کوئی غلطی نہیں۔ 6² = 12", False,
          "6² = 6 × 6 = 36.", "6² = 6 × 6 = 36", "times_two")],
     qtype=None)},
 ],
 review=[
   {"id": "r_square", "type": "recall", "step": number_question(
     "r_square",
     T("Find 14².", "14² معلوم کریں۔"),
     R1,
     T("14 × 14 = 14 × 10 + 14 × 4.", "14 × 14 = 14 × 10 + 14 × 4"),
     T("Right! 140 + 56 = 196.", "درست! 140 + 56 = 196"),
     T("14 × 10 = 140 and 14 × 4 = 56, so 14² = 196.", "14 × 10 = 140 اور 14 × 4 = 56، اس لیے 14² = 196"),
     common_wrong=[wrong(28, "That is 14 × 2. Square means 14 × 14 = 196.", "یہ 14 × 2 ہے۔ مربع کا مطلب 14 × 14 = 196", "times_two")],
     qtype=None)},
   {"id": "r_which", "type": "apply", "step": choice_question(
     "r_which",
     T("Which of these is a perfect square?", "ان میں سے کون سا مکمل مربع عدد ہے؟"),
     [opt("n48", "48", "48", False, "6² = 36 and 7² = 49, so 48 is not a square.", "6² = 36 اور 7² = 49، اس لیے 48 مربع نہیں۔"),
      opt("n72", "72", "72", False, "8² = 64 and 9² = 81, so 72 is not a square.", "8² = 64 اور 9² = 81، اس لیے 72 مربع نہیں۔"),
      opt("n81", "81", "81", True, "Yes! 9 × 9 = 81.", "جی ہاں! 9 × 9 = 81"),
      opt("n90", "90", "90", False, "9² = 81 and 10² = 100, so 90 is not a square.", "9² = 81 اور 10² = 100، اس لیے 90 مربع نہیں۔")],
     qtype=None)},
 ],
 glossary=[T("Square number", "مربع عدد"), T("Perfect square", "مکمل مربع"), T("Negative number", "منفی عدد"), T("Index (power)", "قوت")],
 flashcards=[
   {"id": "f_negative", "front": T("What is (−8)²?", "(−8)² کیا ہے؟"),
    "back": T("64. (−8) × (−8): negative times negative is positive.", "64۔ (−8) × (−8): منفی ضرب منفی مثبت ہے۔")},
   {"id": "f_pairs", "front": T("How can prime factors show a perfect square?", "مفرد اجزائے ضربی سے مکمل مربع کیسے پہچانیں؟"),
    "back": T("Every prime comes in pairs. 36 = 2 × 2 × 3 × 3 is a square; 180 = 2 × 2 × 3 × 3 × 5 is not.", "ہر مفرد عدد جوڑوں میں ہو۔ 36 = 2 × 2 × 3 × 3 مربع ہے؛ 180 = 2 × 2 × 3 × 3 × 5 نہیں۔")},
 ],
 home_task={"id": "h_tiles", "text": T(
   "Find a square floor tile, a chessboard or a square cloth at home. Count how many small squares are in one row, then work out how many there are altogether as a square number.",
   "گھر میں فرش کی کوئی مربع ٹائل، شطرنج کی بساط یا مربع کپڑا ڈھونڈیں۔ ایک قطار کے چھوٹے مربع گنیں، پھر مربع عدد کی مدد سے معلوم کریں کہ کل کتنے ہیں۔")},
 notes=["Covers squares of numbers (q1, q4, q7, q11), perfect squares (q2, q3, q8 to q10) and squares of negative numbers (s_negative, q5, q6, q12, q13).",
        "Negative numbers come in the next chapter of the book (Integers); s_negative explains in one line why (−5)² is positive.",
        "Urdu terms to check: مکمل مربع (perfect square), منفی عدد (negative number)."],
 minutes=16,
)

attach(lesson, {
    "q11_garden": floor_figure(13, 13,
        "A square garden with each side 13, drawn to scale.",
        "ایک مربع باغ جس کا ہر ضلع 13 ہے، پیمانے کے مطابق۔"),
})
write(lesson)
