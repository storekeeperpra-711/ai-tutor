"""Chapter 4 test (Rate, Ratio and Percentage), set out like the book's review
exercise and a board paper: multiple choice, short questions, then longer
mixed problems. The questions are new; only the kinds of question follow the
book."""
from fractions import Fraction as F
from math import gcd
from common import (T, say, nq, rq, ch, write, book_ref, share, join, simplest, REVIEW, CHAPTER_4_TEST,
                    RATIO_MEANING, RATIO_EQUIVALENT, RATIO_SHARE, RATIO_CONTINUED, RATIO_RATE, RATIO_SPEED,
                    PC_MEANING, PC_CONVERT, PC_OF_AMOUNT, PC_FIND, PC_CHANGE, TIME_CLOCK)

SKILL = CHAPTER_4_TEST


def mcq(id, en, ur, right, wrongs, pos):
    return ch(id, ("MCQ: " + en, "کثیر انتخابی: " + ur), right, wrongs, pos, qtype="exam_style")


def short(id, en, ur, answer, hint, good, bad, wrongs=()):
    return nq(id, ("Short question: " + en, "مختصر سوال: " + ur), answer, hint, good, bad, wrongs, qtype="exam_style")


def long_q(id, en, ur, answer, hint, good, bad, wrongs=()):
    return nq(id, ("Long question: " + en, "تفصیلی سوال: " + ur), answer, hint, good, bad, wrongs, qtype="exam_style")


def pct(p, amount):
    x = F(p) * F(amount) / 100
    assert x.denominator == 1, (p, amount)
    return int(x)


def mins(text):
    h, m = (int(x) for x in text.split(":"))
    return h * 60 + m


# MCQs
M1 = simplest(45, 60)
assert M1 == (3, 4) and gcd(45, 60) == 15 and simplest(9, 12) == (3, 4)
M2 = F(480, 40)
assert M2 == 12 and 480 + 40 == 520 and 480 * 40 == 19200
M3 = pct(25, 80)
assert M3 == 20 and 80 - 20 == 60 and F(80, 25) == F(16, 5)
M4 = F(18, 24) * 100
assert M4 == 75 and F(18, 100) * 24 == F(108, 25) and 24 - 18 == 6
assert 18 + 6 == 24
M5_H = 6 + 12
assert f"{M5_H}:15" == "18:15" and f"0{6}:15" == "06:15"
M6 = F(36) * 5 / 18
assert M6 == 10 and F(36) * 18 / 5 == F(648, 5) and float(F(648, 5)) == 129.6 and 36 * 1000 == 36000
M7 = 500 + pct(20, 500)
assert M7 == 600 and pct(20, 500) == 100 and 500 - 100 == 400
M8 = share(500, (2, 3))
assert M8 == [200, 300] and max(M8) == 300 and 500 // 5 == 100
# short questions
S1 = simplest(2 * 1000, 500)
assert S1 == (4, 1) and simplest(2, 500) == (1, 250)
S2 = F(96, 8)
assert S2 == 12 and 96 * 8 == 768
S3 = pct(35, 600)
assert S3 == 210 and 600 - 210 == 390 and 600 // 35 == 17
S4 = mins("17:10") - mins("14:25")
assert S4 == 165 and divmod(S4, 60) == (2, 45) and 1710 - 1425 == 285
S5 = F(108) * 5 / 18
assert S5 == 30 and F(108) * 18 / 5 == F(1944, 5) and float(F(1944, 5)) == 388.8
# long questions
L1_RATIO = join((3, 4), (2, 3))
assert L1_RATIO == (3, 4, 6)
L1 = max(share(3900, L1_RATIO))
assert share(3900, L1_RATIO) == [900, 1200, 1800] and L1 == 1800 and 3900 // 3 == 1300
L2_UP = 24000 + pct(10, 24000)
L2 = L2_UP - pct(10, L2_UP)
assert L2_UP == 26400 and L2 == 23760 and L2 != 24000 and 24000 - 2400 == 21600
L3_TIME = mins("07:50") + 3 * 60 + 40
assert f"{L3_TIME // 60:02d}:{L3_TIME % 60:02d}" == "11:30"
L3 = F(198) / (F(3 * 60 + 40, 60))
assert L3 == 54 and F(198, 3) == 66 and F(198, 11) == 18
L4_PAY = 350 * 8 * 6
L4 = L4_PAY + pct(10, L4_PAY)
assert L4_PAY == 16800 and L4 == 18480 and L4_PAY + 10 == 16810 and 350 * 8 == 2800
# question bank
QB1 = simplest(24, 40)
assert QB1 == (3, 5)
QB2 = F(36, 9) * 7
assert QB2 == 28 and 36 * 7 == 252
QB3 = 800 + pct(25, 800)
assert QB3 == 1000 and pct(25, 800) == 200
# review
R1 = F(60, 4)
assert R1 == 15 and 60 * 4 == 240
R2 = F(45, 300) * 100
assert R2 == 15 and F(300, 45) * 100 != 15

lesson = {
 "id": "g6-maths-06-chapter-4-test",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Answer exam-style questions on the whole of chapter 4: ratio, continued ratio, rate, percentage and its increase and decrease, time, and speed, distance and time.",
                      "textbook": book_ref("Review Exercise 4")}],
 "skills": [SKILL],
 "title": T("Chapter 4 test: Rate, Ratio and Percentage", "باب 4 کا ٹیسٹ: شرح، نسبت اور فیصد"),
 "estimated_minutes": 25,
 "prerequisites": [{"skill": s} for s in (RATIO_MEANING, RATIO_EQUIVALENT, RATIO_SHARE, RATIO_CONTINUED, RATIO_RATE, RATIO_SPEED,
                                         PC_MEANING, PC_CONVERT, PC_OF_AMOUNT, PC_FIND, PC_CHANGE, TIME_CLOCK)],
 "misconceptions": [
   {"id": "order_swapped", "description": "Writes a ratio the wrong way round, or gives the smaller share when the larger is asked."},
   {"id": "not_simplest", "description": "Stops before a ratio is in its lowest terms."},
   {"id": "units_mixed", "description": "Compares quantities in different units without changing them."},
   {"id": "equal_share", "description": "Shares equally whatever the ratio is, or gives the value of one part."},
   {"id": "rate_times", "description": "Multiplies when a rate is wanted, or divides when a total is wanted."},
   {"id": "pc_not_divided", "description": "Forgets to divide by 100 when finding a percentage of a quantity, or finds the rest instead."},
   {"id": "pc_change_only", "description": "Gives the change instead of the new price."},
   {"id": "pc_wrong_base", "description": "Takes a second percentage change of the original price instead of the changed price."},
   {"id": "pm_not_added", "description": "Forgets to add 12 to a p.m. hour on the 24-hour clock."},
   {"id": "base_100", "description": "Treats an hour as 100 minutes, or subtracts clock digits as ordinary numbers."},
   {"id": "wrong_factor", "description": "Uses 18/5 and 5/18 the wrong way round when changing units of speed."},
   {"id": "stops_early", "description": "Finds a middle result but does not answer the question asked."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["exam_style"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_exam_ratio", "type": "exam_style", "step": rq(
     "qb_exam_ratio", ("Write 24 : 40 in its simplest form.", "24 : 40 کو سادہ ترین صورت میں لکھیں۔"), QB1,
     ("Both 24 and 40 divide by 8.", "24 اور 40 دونوں 8 سے تقسیم ہوتے ہیں۔"),
     ("Correct: 3 : 5.", "درست: 3 : 5"),
     ("24 ÷ 8 = 3 and 40 ÷ 8 = 5.", "24 ÷ 8 = 3 اور 40 ÷ 8 = 5"),
     [("5:3", "Keep the order: 3 : 5.", "ترتیب وہی رکھیں: 3 : 5", "order_swapped")], qtype=None)},
   {"id": "qb_exam_rate", "type": "exam_style", "step": nq(
     "qb_exam_rate", ("9 pencils cost Rs 36. What do 7 pencils cost, in rupees?", "9 پنسلوں کی قیمت 36 روپے ہے۔ 7 پنسلوں کی قیمت کتنے روپے ہے؟"), int(QB2),
     ("Find the cost of 1 pencil first.", "پہلے 1 پنسل کی قیمت نکالیں۔"),
     ("Correct: Rs 4 each and 4 × 7 = 28.", "درست: 4 روپے فی پنسل اور 4 × 7 = 28"),
     ("36 ÷ 9 = 4 rupees a pencil. 7 pencils: 4 × 7 = 28.", "36 ÷ 9 = 4 روپے فی پنسل۔ 7 پنسلیں: 4 × 7 = 28"),
     [(252, "That multiplies 36 by 7. Find the cost of one pencil first: 28.", "یہ 36 کو 7 سے ضرب دیتا ہے۔ پہلے ایک پنسل کی قیمت نکالیں: 28", "rate_times")], qtype=None)},
   {"id": "qb_exam_percent", "type": "exam_style", "step": nq(
     "qb_exam_percent", ("A price of Rs 800 is increased by 25%. What is the new price in rupees?", "800 روپے کی قیمت میں 25% اضافہ ہوتا ہے۔ نئی قیمت کتنے روپے ہے؟"), QB3,
     ("25% of 800 is 200. Add it to 800.", "800 کا 25% یعنی 200۔ اسے 800 میں جمع کریں۔"),
     ("Correct: 800 + 200 = 1,000.", "درست: 800 + 200 = 1,000"),
     ("The rise is 25/100 × 800 = 200, so the new price is 1,000.", "اضافہ 25/100 × 800 = 200 ہے، اس لیے نئی قیمت 1,000 ہے۔"),
     [(200, "That is only the rise. Add it to 800: 1,000.", "یہ صرف اضافہ ہے۔ اسے 800 میں جمع کریں: 1,000", "pc_change_only")], qtype=None)},
 ]},
 "home_tasks": [{"id": "h_paper", "text": T(
   "Do Review Exercise 4 in your maths book in your notebook, setting out the working the way this test's answers do. Ask your teacher to check it.",
   "اپنی ریاضی کی کتاب کی اعادی مشق 4 اپنی کاپی میں حل کریں، اور کام اس ٹیسٹ کے جوابات کی طرح لکھیں۔ اپنے استاد سے جانچ کروائیں۔")}],
 "glossary": [T("Multiple choice", "کثیر انتخابی"), T("Short question", "مختصر سوال"), T("Long question", "تفصیلی سوال"),
              T("Model answer", "نمونہ جواب"), T("Review exercise", "اعادی مشق")],
 "steps": [
   {"id": "s1_paper", "type": "explain",
    "character": say("encouraging", "This is a test of the whole chapter, like the book's review exercise. Read each question carefully!",
                     "یہ پورے باب کا ٹیسٹ ہے، کتاب کی اعادی مشق کی طرح۔ ہر سوال غور سے پڑھیں!"),
    "text": T("This test goes with Review Exercise 4 of your maths book (PCTB Mathematics 6). It has three parts, like an exam paper: multiple choice questions (choose one answer), short questions (a few lines of working), and longer problems (full working in your notebook). The questions are new, not the book's.",
              "یہ ٹیسٹ آپ کی ریاضی کی کتاب (پنجاب ٹیکسٹ بک بورڈ، ریاضی 6) کی اعادی مشق 4 کے ساتھ ہے۔ اس کے تین حصے ہیں، امتحانی پرچے کی طرح: کثیر انتخابی سوال (ایک جواب چنیں)، مختصر سوال (چند سطروں کا کام)، اور تفصیلی سوال (پورا کام اپنی کاپی میں)۔ سوال نئے ہیں، کتاب والے نہیں۔")},
   mcq("m1_ratio", "The simplest form of the ratio 45 : 60 is:", "نسبت 45 : 60 کی سادہ ترین صورت ہے:",
       ("3 : 4", "3 : 4", "Correct: divide both terms by 15.", "درست: دونوں اجزا کو 15 سے تقسیم کریں۔"),
       [("4 : 3", "4 : 3", "The order is 45 first, so the answer is 3 : 4.", "ترتیب میں 45 پہلے ہے، اس لیے جواب 3 : 4 ہے۔", "order_swapped"),
        ("9 : 12", "9 : 12", "9 : 12 can still be divided by 3. The simplest form is 3 : 4.", "9 : 12 کو ابھی 3 سے تقسیم کیا جا سکتا ہے۔ سادہ ترین صورت 3 : 4 ہے۔", "not_simplest"),
        ("15 : 20", "15 : 20", "15 : 20 can still be divided by 5. The simplest form is 3 : 4.", "15 : 20 کو ابھی 5 سے تقسیم کیا جا سکتا ہے۔ سادہ ترین صورت 3 : 4 ہے۔", "not_simplest")], 0),
   mcq("m2_rate", "A car uses 40 litres of petrol for 480 km. The rate is:", "ایک کار 480 کلومیٹر کے لیے 40 لیٹر پیٹرول استعمال کرتی ہے۔ شرح ہے:",
       ("12 km per litre", "12 کلومیٹر فی لیٹر", "Correct: 480 ÷ 40 = 12.", "درست: 480 ÷ 40 = 12"),
       [("520 km per litre", "520 کلومیٹر فی لیٹر", "That adds 480 and 40. A rate is found by dividing.", "یہ 480 اور 40 کو جمع کرتا ہے۔ شرح تقسیم سے ملتی ہے۔", "rate_times"),
        ("19,200 km per litre", "19,200 کلومیٹر فی لیٹر", "That multiplies. Divide the distance by the litres.", "یہ ضرب ہے۔ فاصلے کو لیٹر سے تقسیم کریں۔", "rate_times"),
        ("12 litres per km", "12 لیٹر فی کلومیٹر", "That has the units the wrong way round. The car covers 12 km for each litre.", "اس میں اکائیاں الٹی ہیں۔ کار ہر لیٹر پر 12 کلومیٹر چلتی ہے۔", "units_mixed")], 2),
   mcq("m3_percent_of", "25% of 80 is:", "80 کا 25% ہے:",
       ("20", "20", "Correct: 25/100 × 80 = 20.", "درست: 25/100 × 80 = 20"),
       [("60", "60", "That is the rest (80 − 20). We want 25% itself.", "یہ باقی ہے (80 − 20)۔ ہمیں خود 25% چاہیے۔", "pc_not_divided"),
        ("25", "25", "That is the percentage itself, not 25% of 80.", "یہ خود فیصد ہے، 80 کا 25% نہیں۔", "pc_not_divided"),
        ("3.2", "3.2", "That divides 80 by 25. Multiply 80 by 25/100: 20.", "یہ 80 کو 25 سے تقسیم کرتا ہے۔ 80 کو 25/100 سے ضرب دیں: 20", "pc_not_divided")], 3),
   mcq("m4_as_percent", "18 out of 24 expressed as a percentage is:", "24 میں سے 18 فیصد کی صورت میں ہے:",
       ("75%", "75%", "Correct: 18/24 = 3/4 = 75%.", "درست: 18/24 = 3/4 = 75%"),
       [("25%", "25%", "That is the part left out (6 out of 24). 18 out of 24 is 75%.", "یہ چھوڑا ہوا حصہ ہے (24 میں سے 6)۔ 24 میں سے 18 یعنی 75%", "pc_not_divided"),
        ("18%", "18%", "18 out of 24 is not 18 out of 100. Divide 18 by 24 and multiply by 100: 75%.", "24 میں سے 18، 100 میں سے 18 نہیں ہوتا۔ 18 کو 24 سے تقسیم کر کے 100 سے ضرب دیں: 75%", "pc_not_divided"),
        ("133%", "133%", "That divides 24 by 18. The part is 18, the whole is 24: 75%.", "یہ 24 کو 18 سے تقسیم کرتا ہے۔ جزو 18 ہے، کل 24 ہے: 75%", "pc_wrong_base")], 1),
   mcq("m5_clock", "6:15 p.m. on the 24-hour clock is:", "6:15 p.m. 24 گھنٹے کی گھڑی میں ہے:",
       ("18:15", "18:15", "Correct: 6 + 12 = 18.", "درست: 6 + 12 = 18"),
       [("06:15", "06:15", "That is 6:15 in the morning. Add 12 for p.m.", "یہ صبح کے 6:15 ہیں۔ p.m. کے لیے 12 جمع کریں۔", "pm_not_added"),
        ("16:15", "16:15", "That is 4:15 p.m. Add 12 to 6, not 10.", "یہ 4:15 p.m. ہے۔ 6 میں 12 جمع کریں، 10 نہیں۔"),
        ("18:50", "18:50", "A quarter of an hour is 15 minutes, not 50.", "ایک چوتھائی گھنٹہ 15 منٹ ہے، 50 نہیں۔", "base_100")], 0),
   mcq("m6_speed_unit", "A speed of 36 km/h is the same as:", "36 کلومیٹر فی گھنٹہ کی رفتار برابر ہے:",
       ("10 m/s", "10 میٹر فی سیکنڈ", "Correct: 36 × 5/18 = 10.", "درست: 36 × 5/18 = 10"),
       [("129.6 m/s", "129.6 میٹر فی سیکنڈ", "That multiplies by 18/5, which changes m/s to km/h. Multiply by 5/18.", "یہ 18/5 سے ضرب دیتا ہے جو میٹر فی سیکنڈ کو کلومیٹر فی گھنٹہ بناتا ہے۔ 5/18 سے ضرب دیں۔", "wrong_factor"),
        ("36,000 m/s", "36,000 میٹر فی سیکنڈ", "That changes kilometres to metres but ignores the hour. Also divide by 3600: 10 m/s.", "یہ کلومیٹر کو میٹر بناتا ہے مگر گھنٹے کو نظر انداز کرتا ہے۔ 3600 سے بھی تقسیم کریں: 10 میٹر فی سیکنڈ", "wrong_factor"),
        ("100 m/s", "100 میٹر فی سیکنڈ", "36 km/h is not that fast. Multiply by 5/18: 10 m/s.", "36 کلومیٹر فی گھنٹہ اتنا تیز نہیں۔ 5/18 سے ضرب دیں: 10 میٹر فی سیکنڈ", "wrong_factor")], 1),
   mcq("m7_increase", "A price of Rs 500 is increased by 20%. The new price is:", "500 روپے کی قیمت میں 20% اضافہ ہوتا ہے۔ نئی قیمت ہے:",
       ("Rs 600", "600 روپے", "Correct: 20% of 500 is 100, and 500 + 100 = 600.", "درست: 500 کا 20% یعنی 100 اور 500 + 100 = 600"),
       [("Rs 100", "100 روپے", "That is only the increase. Add it to 500.", "یہ صرف اضافہ ہے۔ اسے 500 میں جمع کریں۔", "pc_change_only"),
        ("Rs 520", "520 روپے", "That adds 20 rupees. Add 20% of 500, which is 100.", "یہ 20 روپے جمع کرتا ہے۔ 500 کا 20% جمع کریں، یعنی 100۔", "pc_not_divided"),
        ("Rs 400", "400 روپے", "An increase is added, not subtracted.", "اضافہ جمع کیا جاتا ہے، گھٹایا نہیں جاتا۔", "pc_change_only")], 2),
   mcq("m8_share", "Rs 500 is shared in the ratio 2 : 3. The larger share is:", "500 روپے 2 : 3 کی نسبت سے تقسیم ہوتے ہیں۔ بڑا حصہ ہے:",
       ("Rs 300", "300 روپے", "Correct: 5 parts, Rs 100 a part, and 3 × 100 = 300.", "درست: 5 حصے، 100 روپے فی حصہ، اور 3 × 100 = 300"),
       [("Rs 200", "200 روپے", "That is the smaller share (2 parts).", "یہ چھوٹا حصہ ہے (2 حصے)۔", "order_swapped"),
        ("Rs 100", "100 روپے", "That is the value of one part.", "یہ ایک حصے کی قیمت ہے۔", "equal_share"),
        ("Rs 250", "250 روپے", "That shares equally. The ratio is 2 : 3, so the shares differ.", "یہ برابر تقسیم ہے۔ نسبت 2 : 3 ہے، اس لیے حصے مختلف ہیں۔", "equal_share")], 3),
   {"id": "s_short", "type": "explain",
    "text": T("Short questions. Work each one out in your notebook, then type the answer.",
              "مختصر سوال۔ ہر ایک اپنی کاپی میں حل کریں، پھر جواب لکھیں۔")},
   rq("q1_units", ("Short question: Write the ratio of 2 kg to 500 g in its simplest form (like 3:1).", "مختصر سوال: 2 کلوگرام اور 500 گرام کی نسبت سادہ ترین صورت میں لکھیں (جیسے 3:1)۔"), S1,
     ("Change 2 kg to grams first.", "پہلے 2 کلوگرام کو گرام میں بدلیں۔"),
     ("Correct: 2000 : 500 = 4 : 1.", "درست: 2000 : 500 = 4 : 1"),
     ("Model answer: 2 kg = 2000 g. 2000 : 500, divided by 500, is 4 : 1.", "نمونہ جواب: 2 کلوگرام = 2000 گرام۔ 2000 : 500 کو 500 سے تقسیم کریں تو 4 : 1 ملتا ہے۔"),
     [("2:500", "The two quantities must be in the same unit. Use grams for both: 4 : 1.", "دونوں مقداریں ایک ہی اکائی میں ہونی چاہییں۔ دونوں کو گرام میں لیں: 4 : 1", "units_mixed"),
      ("1:4", "The order is 2 kg first, so 4 : 1.", "ترتیب میں 2 کلوگرام پہلے ہے، اس لیے 4 : 1", "order_swapped")], qtype="exam_style"),
   short("q2_rate", "8 pens cost Rs 96. How many rupees does one pen cost?", "8 قلموں کی قیمت 96 روپے ہے۔ ایک قلم کی قیمت کتنے روپے ہے؟", int(S2),
     ("Cost of one = total cost ÷ number of pens.", "ایک کی قیمت = کل قیمت ÷ قلموں کی تعداد"),
     ("Correct: 96 ÷ 8 = 12.", "درست: 96 ÷ 8 = 12"),
     ("Model answer: 96 ÷ 8 = 12 rupees per pen.", "نمونہ جواب: 96 ÷ 8 = 12 روپے فی قلم۔"),
     [(768, "That multiplies. For the cost of one pen divide: 12.", "یہ ضرب ہے۔ ایک قلم کی قیمت کے لیے تقسیم کریں: 12", "rate_times")]),
   short("q3_percent", "Find 35% of 600.", "600 کا 35% معلوم کریں۔", S3,
     ("10% of 600 is 60. Build 35% from 10% three times and 5% once.", "600 کا 10% یعنی 60۔ 35% کو 10% تین بار اور 5% ایک بار سے بنائیں۔"),
     ("Correct: 180 + 30 = 210.", "درست: 180 + 30 = 210"),
     ("Model answer: 35/100 × 600 = 210.", "نمونہ جواب: 35/100 × 600 = 210"),
     [(390, "That is the rest (600 − 210). 35% of 600 is 210.", "یہ باقی ہے (600 − 210)۔ 600 کا 35% ہے 210", "pc_not_divided"),
      (21000, "That multiplies by 35 and forgets to divide by 100: 210.", "یہ 35 سے ضرب دیتا ہے اور 100 سے تقسیم کرنا بھول جاتا ہے: 210", "pc_not_divided")]),
   short("q4_elapsed", "A programme starts at 14:25 and ends at 17:10. How many minutes does it last?", "ایک پروگرام 14:25 پر شروع ہو کر 17:10 پر ختم ہوتا ہے۔ یہ کتنے منٹ چلتا ہے؟", S4,
     ("14:25 to 17:25 is 3 hours. You stop 15 minutes early.", "14:25 سے 17:25 تک 3 گھنٹے ہیں۔ آپ 15 منٹ پہلے رک جاتے ہیں۔"),
     ("Correct: 2 h 45 min = 165 minutes.", "درست: 2 گھنٹے 45 منٹ = 165 منٹ"),
     ("Model answer: 14:25 to 17:10 is 2 hours 45 minutes = 120 + 45 = 165 minutes.", "نمونہ جواب: 14:25 سے 17:10 تک 2 گھنٹے 45 منٹ = 120 + 45 = 165 منٹ"),
     [(285, "That subtracts 1425 from 1710 as ordinary numbers. Minutes go up to 60: 165.", "یہ 1710 میں سے 1425 کو عام اعداد کی طرح گھٹاتا ہے۔ منٹ 60 تک جاتے ہیں: 165", "base_100")]),
   short("q5_convert", "Change 108 km/h to metres per second.", "108 کلومیٹر فی گھنٹہ کو میٹر فی سیکنڈ میں بدلیں۔", int(S5),
     ("Multiply by 5/18. 108 ÷ 18 = 6.", "5/18 سے ضرب دیں۔ 108 ÷ 18 = 6"),
     ("Correct: 6 × 5 = 30 m/s.", "درست: 6 × 5 = 30 میٹر فی سیکنڈ"),
     ("Model answer: 108 × 5/18 = 30 m/s.", "نمونہ جواب: 108 × 5/18 = 30 میٹر فی سیکنڈ۔"),
     [(388.8, "That multiplies by 18/5. For km/h to m/s multiply by 5/18: 30.", "یہ 18/5 سے ضرب دیتا ہے۔ کلومیٹر فی گھنٹہ سے میٹر فی سیکنڈ کے لیے 5/18 سے ضرب دیں: 30", "wrong_factor")]),
   {"id": "s_long", "type": "explain",
    "text": T("Longer problems. Write full working in your notebook, then type the final answer.",
              "تفصیلی سوالات۔ اپنی کاپی میں پورا کام لکھیں، پھر آخری جواب لکھیں۔")},
   long_q("l1_continued", "Aslam : Bilal = 3 : 4 and Bilal : Chand = 2 : 3. Rs 3,900 is shared among the three in the ratio Aslam : Bilal : Chand. How many rupees does the one with the largest share get?", "اسلم : بلال = 3 : 4 اور بلال : چاند = 2 : 3۔ 3,900 روپے تینوں میں اسلم : بلال : چاند کی نسبت سے تقسیم ہوتے ہیں۔ سب سے بڑے حصے والے کو کتنے روپے ملتے ہیں؟", L1,
     ("Make Bilal 4 in both ratios: 2 : 3 = 4 : 6. Then 3 : 4 : 6.", "دونوں نسبتوں میں بلال کو 4 بنائیں: 2 : 3 = 4 : 6۔ پھر 3 : 4 : 6"),
     ("Correct: 13 parts, Rs 300 a part, and 6 × 300 = 1,800.", "درست: 13 حصے، 300 روپے فی حصہ، اور 6 × 300 = 1,800"),
     ("Model answer: 2 : 3 = 4 : 6, so the continued ratio is 3 : 4 : 6. 3 + 4 + 6 = 13 parts. 3900 ÷ 13 = 300. Chand gets 6 × 300 = 1,800 rupees.", "نمونہ جواب: 2 : 3 = 4 : 6، اس لیے مسلسل نسبت 3 : 4 : 6 ہے۔ 3 + 4 + 6 = 13 حصے۔ 3900 ÷ 13 = 300۔ چاند کو 6 × 300 = 1,800 روپے ملتے ہیں۔"),
     [(1300, "That shares equally among three. The ratio is 3 : 4 : 6: 1,800.", "یہ تین میں برابر تقسیم ہے۔ نسبت 3 : 4 : 6 ہے: 1,800", "equal_share"),
      (300, "That is the value of one part. The largest share has 6 parts: 1,800.", "یہ ایک حصے کی قیمت ہے۔ سب سے بڑے حصے میں 6 حصے ہیں: 1,800", "equal_share")]),
   long_q("l2_two_changes", "A phone costs Rs 24,000. Its price first rises by 10%. Then the new price falls by 10%. What is the final price in rupees?", "ایک فون کی قیمت 24,000 روپے ہے۔ اس کی قیمت پہلے 10% بڑھتی ہے۔ پھر نئی قیمت 10% کم ہو جاتی ہے۔ آخری قیمت کتنے روپے ہے؟", L2,
     ("After the rise, find 10% of the new price, not of 24,000.", "اضافے کے بعد 24,000 کا نہیں، نئی قیمت کا 10% نکالیں۔"),
     ("Correct: 26,400 − 2,640 = 23,760.", "درست: 26,400 − 2,640 = 23,760"),
     ("Model answer: 10% of 24,000 = 2,400, so the price is 26,400. 10% of 26,400 = 2,640. 26,400 − 2,640 = 23,760 rupees.", "نمونہ جواب: 24,000 کا 10% = 2,400، اس لیے قیمت 26,400 ہے۔ 26,400 کا 10% = 2,640۔ 26,400 − 2,640 = 23,760 روپے۔"),
     [(24000, "The fall is 10% of the higher price, 26,400, so it is more than the rise: 23,760.", "کمی زیادہ قیمت 26,400 کا 10% ہے، اس لیے یہ اضافے سے زیادہ ہے: 23,760", "pc_wrong_base"),
      (26400, "That stops after the rise. Now take 10% off: 23,760.", "یہ اضافے کے بعد رک گیا۔ اب 10% کم کریں: 23,760", "stops_early")]),
   long_q("l3_bus_speed", "A bus leaves at 07:50 and reaches its destination 3 hours 40 minutes later, after covering 198 km. What is its average speed in km/h?", "ایک بس 07:50 پر چلتی ہے اور 198 کلومیٹر طے کر کے 3 گھنٹے 40 منٹ بعد منزل پر پہنچتی ہے۔ اس کی اوسط رفتار کلومیٹر فی گھنٹہ میں کیا ہے؟", int(L3),
     ("3 hours 40 minutes is 3 2/3 hours = 11/3 hours. Divide 198 by that.", "3 گھنٹے 40 منٹ یعنی 3 2/3 گھنٹے = 11/3 گھنٹے۔ 198 کو اس سے تقسیم کریں۔"),
     ("Correct: 198 ÷ 11/3 = 54 km/h.", "درست: 198 ÷ 11/3 = 54 کلومیٹر فی گھنٹہ"),
     ("Model answer: 40 minutes = 2/3 hour, so the time is 11/3 hours. Speed = 198 ÷ 11/3 = 198 × 3 ÷ 11 = 54 km/h. (The bus arrives at 11:30.)", "نمونہ جواب: 40 منٹ = 2/3 گھنٹہ، اس لیے وقت 11/3 گھنٹے ہے۔ رفتار = 198 ÷ 11/3 = 198 × 3 ÷ 11 = 54 کلومیٹر فی گھنٹہ۔ (بس 11:30 پر پہنچتی ہے۔)"),
     [(66, "That uses 3 hours and ignores the 40 minutes. The time is 3 2/3 hours: 54.", "یہ 3 گھنٹے لیتا ہے اور 40 منٹ نظر انداز کرتا ہے۔ وقت 3 2/3 گھنٹے ہے: 54", "base_100"),
      (18, "That divides 198 by 11. The time is 11/3 hours, so multiply by 3 as well: 54.", "یہ 198 کو 11 سے تقسیم کرتا ہے۔ وقت 11/3 گھنٹے ہے، اس لیے 3 سے بھی ضرب دیں: 54", "stops_early")]),
   long_q("l4_wages", "A worker earns Rs 350 per hour. He works 8 hours a day for 6 days and then gets a bonus of 10% of what he has earned. How many rupees does he receive altogether?", "ایک مزدور 350 روپے فی گھنٹہ کماتا ہے۔ وہ روزانہ 8 گھنٹے 6 دن کام کرتا ہے اور پھر اپنی کمائی کا 10% بونس پاتا ہے۔ اسے کل کتنے روپے ملتے ہیں؟", int(L4),
     ("Pay = 350 × 8 × 6. Then add 10% of it.", "اجرت = 350 × 8 × 6۔ پھر اس کا 10% جمع کریں۔"),
     ("Correct: 16,800 + 1,680 = 18,480.", "درست: 16,800 + 1,680 = 18,480"),
     ("Model answer: 8 × 6 = 48 hours, 48 × 350 = 16,800. Bonus = 10% of 16,800 = 1,680. Total = 18,480 rupees.", "نمونہ جواب: 8 × 6 = 48 گھنٹے، 48 × 350 = 16,800۔ بونس = 16,800 کا 10% = 1,680۔ کل = 18,480 روپے۔"),
     [(16800, "That is the pay before the bonus. Add the bonus: 18,480.", "یہ بونس سے پہلے کی اجرت ہے۔ بونس جمع کریں: 18,480", "stops_early"),
      (16810, "The bonus is 10% of 16,800, which is 1,680, not 10 rupees: 18,480.", "بونس 16,800 کا 10% یعنی 1,680 ہے، 10 روپے نہیں: 18,480", "pc_not_divided")]),
   {"id": "s_end_summary", "type": "summary",
    "character": say("celebrating", "You finished the chapter 4 test. Well done!", "آپ نے باب 4 کا ٹیسٹ مکمل کر لیا۔ شاباش!"),
    "text": T("In the exam: put a ratio in the same unit and divide both terms by the same number; share by adding the parts and finding one part; join two ratios by making the common quantity equal. A rate divides one quantity by the other in different units. A percentage is out of 100: multiply to find a percentage of a quantity, divide and multiply by 100 for a percentage of another, and add or subtract for an increase or decrease. On the 24-hour clock add 12 to p.m. hours and use 60 minutes to an hour. Speed = distance ÷ time; km/h to m/s is × 5/18, m/s to km/h is × 18/5.",
              "امتحان میں: نسبت کو ایک ہی اکائی میں رکھیں اور دونوں اجزا کو ایک ہی عدد سے تقسیم کریں؛ حصے جمع کر کے اور ایک حصہ نکال کر تقسیم کریں؛ دو نسبتوں کو جوڑنے کے لیے مشترک مقدار برابر کریں۔ شرح مختلف اکائیوں کی ایک مقدار کو دوسری سے تقسیم کرتی ہے۔ فیصد سو میں سے ہوتا ہے: کسی مقدار کا فیصد نکالنے کے لیے ضرب دیں، دوسری کا فیصد معلوم کرنے کے لیے تقسیم کر کے 100 سے ضرب دیں، اور اضافے یا کمی کے لیے جمع یا تفریق کریں۔ 24 گھنٹے کی گھڑی میں p.m. کے گھنٹوں میں 12 جمع کریں اور ایک گھنٹے میں 60 منٹ لیں۔ رفتار = فاصلہ ÷ وقت؛ کلومیٹر فی گھنٹہ سے میٹر فی سیکنڈ × 5/18، میٹر فی سیکنڈ سے کلومیٹر فی گھنٹہ × 18/5۔"),
    "points": [T("In a two-step percentage problem, the second percentage is taken of the new value.", "دو مرحلوں کے فیصد سوال میں دوسرا فیصد نئی قیمت کا لیا جاتا ہے۔"),
               T("Write the unit with each answer: Rs, km/h, minutes.", "ہر جواب کے ساتھ اکائی لکھیں: روپے، کلومیٹر فی گھنٹہ، منٹ۔")]},
 ],
 "review_questions": [
   {"id": "r_exam_rate", "type": "exam_style", "skill": SKILL, "step": nq(
     "r_exam_rate", ("A tap fills 60 litres in 4 minutes. How many litres does it fill in 1 minute?", "ایک نل 4 منٹ میں 60 لیٹر بھرتا ہے۔ یہ 1 منٹ میں کتنے لیٹر بھرتا ہے؟"), int(R1),
     ("Divide the litres by the minutes.", "لیٹر کو منٹ سے تقسیم کریں۔"),
     ("Correct: 15.", "درست: 15"), ("60 ÷ 4 = 15 litres per minute.", "60 ÷ 4 = 15 لیٹر فی منٹ"),
     [(240, "That multiplies. Divide to find the amount for one minute: 15.", "یہ ضرب ہے۔ ایک منٹ کی مقدار کے لیے تقسیم کریں: 15", "rate_times")], qtype=None)},
   {"id": "r_exam_percent", "type": "exam_style", "skill": SKILL, "step": nq(
     "r_exam_percent", ("Out of 300 students, 45 are absent. What percentage is absent?", "300 طلبہ میں سے 45 غیر حاضر ہیں۔ کتنے فیصد غیر حاضر ہیں؟"), int(R2),
     ("Divide 45 by 300, then multiply by 100.", "45 کو 300 سے تقسیم کریں، پھر 100 سے ضرب دیں۔"),
     ("Correct: 15%.", "درست: 15%"), ("45/300 × 100 = 15%.", "45/300 × 100 = 15%"),
     [(255, "That is the number present. We want the percentage absent: 15.", "یہ حاضر طلبہ کی تعداد ہے۔ ہمیں غیر حاضر کا فیصد چاہیے: 15", "pc_not_divided")], qtype=None)},
 ],
 "teacher_notes": [
   "A chapter test to use with Review Exercise 4 of the PCTB Mathematics 6 book, in the style of a paper: multiple choice, short questions, then longer problems. Only the kinds of question come from the book; every question, number and story here is new, because the book may not be copied.",
   "It has its own skill (maths.ratio.chapter_4_test), with the chapter's ratio, percentage, time and speed skills as prerequisites, and is mastered with exam_style questions, like g9-maths-05-board-exam-practice.",
   "Urdu terms to check: کثیر انتخابی (multiple choice), مختصر سوال / تفصیلی سوال (short / long question), نمونہ جواب (model answer), اعادی مشق (review exercise), مسلسل نسبت (continued ratio), فیصد (percentage), رفتار (speed).",
   "The numbers were worked out in content/sources/g6-maths-06/chapter_4_test.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}

write(lesson)
