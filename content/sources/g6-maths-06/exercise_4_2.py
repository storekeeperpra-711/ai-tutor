"""Practice set for Exercise 4.2 of the book: rates (pay per hour, cost per kg,
call charges, kilometres per hour) and distance = rate x time. The questions
are new; only the kinds of question follow the book."""
from common import (T, say, nq, ch, practice_lesson, practice_intro, write,
                    EX_SKILL, RATIO_RATE, UNITARY)

SKILL = EX_SKILL["4.2"]


def per(amount, units):
    """The amount for one unit; the division must be exact."""
    r, rest = divmod(amount, units)
    assert rest == 0, (amount, units)
    return r


# q1: 6 notebooks for Rs 270
Q1 = per(270, 6)
assert Q1 == 45 and 270 * 6 == 1620
# q2: which is a rate (different units)? "Rs 60 for 3 kg"
# q3: Rs 2,400 for 8 hours
Q3 = per(2400, 8)
assert Q3 == 300 and 2400 * 8 == 19200
# q4: 12 kg of flour for Rs 1,440
Q4 = per(1440, 12)
assert Q4 == 120 and 1440 * 12 == 17280
# q5: 5 kg of apples at Rs 180 a kilogram
Q5 = 180 * 5
assert Q5 == 900 and 180 // 5 == 36
# q6: a call at Rs 4 a minute for 18 minutes
Q6 = 4 * 18
assert Q6 == 72 and 18 // 4 == 4
# q7: 45 km in 3 hours
Q7 = per(45, 3)
assert Q7 == 15 and 45 * 3 == 135
# q8: walks at 4 km/h for 3 hours
Q8 = 4 * 3
assert Q8 == 12 and 4 + 3 == 7
# q9: car at 65 km/h for 4 hours
Q9 = 65 * 4
assert Q9 == 260 and 65 + 4 == 69
# q10: 5 kg for Rs 600 or 8 kg for Rs 880
R10_A, R10_B = per(600, 5), per(880, 8)
assert (R10_A, R10_B) == (120, 110) and R10_B < R10_A and 880 > 600
# q11: tank fills at 15 litres a minute: 180 litres
Q11 = per(180, 15)
assert Q11 == 12 and 180 * 15 == 2700
# q12: types 120 words in 4 minutes; words in 15 minutes
Q12 = per(120, 4) * 15
assert Q12 == 450 and 120 * 15 == 1800 and per(120, 4) == 30
# q13 (find error): 150 km in 3 h is 50 km/h, not 450
assert per(150, 3) == 50 and 150 * 3 == 450
# bank and review
QB_REC = per(840, 7)
assert QB_REC == 120
QB_APP = 55 * 3
assert QB_APP == 165 and 55 + 3 == 58
R_REC = per(360, 9)
assert R_REC == 40
R_APP = 12 * 7
assert R_APP == 84 and 12 + 7 == 19

lesson = practice_lesson(
 "4.2", script="exercise_4_2.py",
 title=T("Exercise 4.2 practice: rate", "مشق 4.2 کی پریکٹس: شرح"),
 outcome="Find a unit rate from two quantities in different units, use a rate to find the cost or the distance, compare two rates and solve rate problems.",
 prerequisites=[RATIO_RATE, UNITARY],
 misconceptions=[
   {"id": "rate_times", "description": "Multiplies the two quantities when finding a rate instead of dividing."},
   {"id": "rate_divides", "description": "Divides by the rate when the total is wanted, instead of multiplying."},
   {"id": "rate_adds", "description": "Adds the rate and the time instead of multiplying them."},
   {"id": "wrong_way_round", "description": "Divides the units the wrong way round, so the rate is for the other quantity."},
   {"id": "compare_totals", "description": "Compares the total prices without looking at how much each buys."},
   {"id": "rate_unit", "description": "Does not see that a rate compares two different units."},
   {"id": "stops_early", "description": "Finds the rate but does not use it to finish the problem."},
 ],
 steps=[
   practice_intro("4.2",
     "Here you find unit rates such as pay per hour or cost per kilogram, use a rate to find a total or a distance, and compare two rates.",
     "اس میں آپ فی گھنٹہ اجرت یا فی کلوگرام قیمت جیسی اکائی شرح معلوم کریں گے، شرح سے کل رقم یا فاصلہ نکالیں گے اور دو شرحوں کا موازنہ کریں گے۔",
     "Exercise 4.2 is about rate. Ready?", "مشق 4.2 شرح کے بارے میں ہے۔ تیار؟"),
   nq("q1_unit_rate", ("6 notebooks cost Rs 270. What is the rate in rupees per notebook?", "6 کاپیوں کی قیمت 270 روپے ہے۔ فی کاپی شرح کتنے روپے ہے؟"), Q1,
      ("Rate per notebook = cost ÷ number of notebooks.", "فی کاپی شرح = قیمت ÷ کاپیوں کی تعداد"),
      ("Right! 270 ÷ 6 = 45 rupees per notebook.", "درست! 270 ÷ 6 = 45 روپے فی کاپی"),
      ("Divide the cost by the number of notebooks: 270 ÷ 6 = 45.", "قیمت کو کاپیوں کی تعداد سے تقسیم کریں: 270 ÷ 6 = 45"),
      [(1620, "That multiplies. A rate per notebook comes from dividing: 45.", "یہ ضرب ہے۔ فی کاپی شرح تقسیم سے ملتی ہے: 45", "rate_times")],
      qtype="recall"),
   ch("q2_which_rate", ("Which of these is a rate?", "ان میں سے کون سی ایک شرح ہے؟"),
      ("Rs 60 for 3 kg of sugar", "3 کلوگرام چینی کے 60 روپے", "Yes! A rate compares two quantities in different units: rupees and kilograms.", "جی ہاں! شرح دو مختلف اکائیوں کی مقداروں کا موازنہ ہے: روپے اور کلوگرام۔"),
      [("4 boys to 5 girls", "4 لڑکے اور 5 لڑکیاں", "Boys and girls are counted in the same kind of unit (children), so this is a ratio.", "لڑکے اور لڑکیاں ایک ہی طرح کی اکائی (بچے) میں گنے جاتے ہیں، اس لیے یہ نسبت ہے۔", "rate_unit"),
       ("8 cm to 12 cm", "8 سینٹی میٹر اور 12 سینٹی میٹر", "Both are in centimetres, so this is a ratio.", "دونوں سینٹی میٹر میں ہیں، اس لیے یہ نسبت ہے۔", "rate_unit"),
       ("3 : 4", "3 : 4", "This has no units. A rate compares different units, like rupees and kilograms.", "اس میں اکائیاں نہیں ہیں۔ شرح مختلف اکائیوں کا موازنہ کرتی ہے، جیسے روپے اور کلوگرام۔", "rate_unit")],
      1, qtype="recall"),
   {"id": "s_rules", "type": "explain",
    "character": say("thinking", "A rate compares different units. Divide to find the rate for one.", "شرح مختلف اکائیوں کا موازنہ ہے۔ ایک کی شرح کے لیے تقسیم کریں۔"),
    "text": T("A rate is a special kind of ratio in which the two terms are in different units, such as rupees and hours. The unit rate is the amount for one: Rs 2,400 for 8 hours is 2,400 ÷ 8 = Rs 300 per hour. To find a total, multiply the rate by the number of units: 5 kg at Rs 180 per kg costs 5 × 180 = Rs 900. Distance = rate × time: 4 km/h for 3 hours is 12 km. To compare, find the rate for one of each.",
              "شرح ایک خاص طرح کی نسبت ہے جس کے دونوں اجزا مختلف اکائیوں میں ہوتے ہیں، جیسے روپے اور گھنٹے۔ اکائی شرح ایک کی مقدار ہے: 8 گھنٹے کے 2,400 روپے یعنی 2,400 ÷ 8 = 300 روپے فی گھنٹہ۔ کل معلوم کرنے کے لیے شرح کو اکائیوں کی تعداد سے ضرب دیں: 180 روپے فی کلوگرام کے حساب سے 5 کلوگرام کی قیمت 5 × 180 = 900 روپے۔ فاصلہ = شرح × وقت: 4 کلومیٹر فی گھنٹہ سے 3 گھنٹے میں 12 کلومیٹر۔ موازنے کے لیے دونوں کی ایک ایک کی شرح نکالیں۔")},
   nq("q3_pay", ("Nadeem earns Rs 2,400 for working 8 hours. How many rupees does he earn per hour?", "ندیم 8 گھنٹے کام کرنے کے 2,400 روپے کماتا ہے۔ وہ فی گھنٹہ کتنے روپے کماتا ہے؟"), Q3,
      ("Pay per hour = total pay ÷ hours.", "فی گھنٹہ اجرت = کل اجرت ÷ گھنٹے"),
      ("Right! 2400 ÷ 8 = 300.", "درست! 2400 ÷ 8 = 300"),
      ("2400 ÷ 8 = 300 rupees per hour.", "2400 ÷ 8 = 300 روپے فی گھنٹہ"),
      [(19200, "That multiplies 2400 by 8. To find the pay for one hour we divide: 300.", "یہ 2400 کو 8 سے ضرب دیتا ہے۔ ایک گھنٹے کی اجرت کے لیے تقسیم کریں: 300", "rate_times")]),
   nq("q4_flour", ("12 kg of flour cost Rs 1,440. What is the cost of 1 kg of flour in rupees?", "12 کلوگرام آٹے کی قیمت 1,440 روپے ہے۔ 1 کلوگرام آٹے کی قیمت کتنے روپے ہے؟"), Q4,
      ("Cost of 1 kg = total cost ÷ kilograms.", "1 کلوگرام کی قیمت = کل قیمت ÷ کلوگرام"),
      ("Right! 1440 ÷ 12 = 120.", "درست! 1440 ÷ 12 = 120"),
      ("1440 ÷ 12 = 120 rupees per kg.", "1440 ÷ 12 = 120 روپے فی کلوگرام"),
      [(17280, "That multiplies. For the cost of one kilogram, divide: 120.", "یہ ضرب ہے۔ ایک کلوگرام کی قیمت کے لیے تقسیم کریں: 120", "rate_times")]),
   nq("q5_total_cost", ("Apples cost Rs 180 per kilogram. How much do 5 kilograms cost, in rupees?", "سیب 180 روپے فی کلوگرام ہیں۔ 5 کلوگرام کی قیمت کتنے روپے ہے؟"), Q5,
      ("Cost = rate × number of kilograms.", "قیمت = شرح × کلوگرام"),
      ("Right! 180 × 5 = 900.", "درست! 180 × 5 = 900"),
      ("Each kilogram costs 180, so 5 kilograms cost 180 × 5 = 900 rupees.", "ہر کلوگرام 180 روپے کا ہے، اس لیے 5 کلوگرام 180 × 5 = 900 روپے کے ہیں۔"),
      [(36, "That divides. We know the price of one kilogram and want the price of 5, so multiply: 900.", "یہ تقسیم ہے۔ ہمیں ایک کلوگرام کی قیمت معلوم ہے اور 5 کی چاہیے، اس لیے ضرب دیں: 900", "rate_divides")]),
   nq("q6_call", ("A phone call costs Rs 4 per minute. What is the charge for an 18-minute call, in rupees?", "ایک فون کال 4 روپے فی منٹ ہے۔ 18 منٹ کی کال کا خرچ کتنے روپے ہے؟"), Q6,
      ("Charge = rate per minute × minutes.", "خرچ = فی منٹ شرح × منٹ"),
      ("Right! 4 × 18 = 72.", "درست! 4 × 18 = 72"),
      ("4 rupees for each of 18 minutes: 4 × 18 = 72.", "18 منٹ میں سے ہر ایک کے 4 روپے: 4 × 18 = 72"),
      [(4, "That divides 18 by 4. Multiply the rate by the minutes: 72.", "یہ 18 کو 4 سے تقسیم کرتا ہے۔ شرح کو منٹ سے ضرب دیں: 72", "rate_divides")]),
   nq("q7_speed", ("A cyclist rides 45 km in 3 hours. What is the rate in km per hour?", "ایک سائیکل سوار 3 گھنٹے میں 45 کلومیٹر چلتا ہے۔ کلومیٹر فی گھنٹہ شرح کیا ہے؟"), Q7,
      ("Rate per hour = distance ÷ hours.", "فی گھنٹہ شرح = فاصلہ ÷ گھنٹے"),
      ("Right! 45 ÷ 3 = 15 km per hour.", "درست! 45 ÷ 3 = 15 کلومیٹر فی گھنٹہ"),
      ("Distance for one hour: 45 ÷ 3 = 15 km.", "ایک گھنٹے کا فاصلہ: 45 ÷ 3 = 15 کلومیٹر"),
      [(135, "That multiplies. The distance for one hour comes from dividing: 15.", "یہ ضرب ہے۔ ایک گھنٹے کا فاصلہ تقسیم سے ملتا ہے: 15", "rate_times")]),
   nq("q8_walk", ("Imran walks at 4 km per hour. How far does he walk in 3 hours? Answer in km.", "عمران 4 کلومیٹر فی گھنٹہ کی رفتار سے چلتا ہے۔ وہ 3 گھنٹے میں کتنا فاصلہ طے کرتا ہے؟ جواب کلومیٹر میں دیں۔"), Q8,
      ("Distance = rate × time.", "فاصلہ = شرح × وقت"),
      ("Right! 4 × 3 = 12 km.", "درست! 4 × 3 = 12 کلومیٹر"),
      ("He covers 4 km every hour for 3 hours: 4 × 3 = 12 km.", "وہ 3 گھنٹے تک ہر گھنٹے 4 کلومیٹر چلتا ہے: 4 × 3 = 12 کلومیٹر"),
      [(7, "That adds the rate and the time. Multiply them: 12.", "یہ شرح اور وقت کو جمع کرتا ہے۔ انہیں ضرب دیں: 12", "rate_adds")]),
   nq("q9_car", ("A car travels at 65 km per hour for 4 hours. How many kilometres does it cover?", "ایک کار 65 کلومیٹر فی گھنٹہ کی رفتار سے 4 گھنٹے چلتی ہے۔ وہ کتنے کلومیٹر طے کرتی ہے؟"), Q9,
      ("Distance = rate × time.", "فاصلہ = شرح × وقت"),
      ("Right! 65 × 4 = 260 km.", "درست! 65 × 4 = 260 کلومیٹر"),
      ("65 km in each of 4 hours: 65 × 4 = 260 km.", "4 گھنٹوں میں سے ہر ایک میں 65 کلومیٹر: 65 × 4 = 260 کلومیٹر"),
      [(69, "That adds 65 and 4. Multiply: 260.", "یہ 65 اور 4 کو جمع کرتا ہے۔ ضرب دیں: 260", "rate_adds")]),
   ch("q10_compare", ("Shop A sells 5 kg of rice for Rs 600. Shop B sells 8 kg of the same rice for Rs 880. Which shop is cheaper per kilogram?", "دکان A میں 5 کلوگرام چاول 600 روپے کے ہیں۔ دکان B میں وہی چاول 8 کلوگرام 880 روپے کے ہیں۔ فی کلوگرام کون سی دکان سستی ہے؟"),
      ("Shop B: Rs 110 per kg, against Rs 120 per kg in shop A", "دکان B: 110 روپے فی کلوگرام، جبکہ دکان A میں 120 روپے فی کلوگرام", "Yes! 600 ÷ 5 = 120 and 880 ÷ 8 = 110, so B is cheaper per kilogram.", "جی ہاں! 600 ÷ 5 = 120 اور 880 ÷ 8 = 110، اس لیے B فی کلوگرام سستی ہے۔"),
      [("Shop A, because Rs 600 is less than Rs 880", "دکان A، کیونکہ 600 روپے 880 سے کم ہیں", "The shops sell different amounts of rice, so compare the price of 1 kg in each.", "دکانیں مختلف مقدار بیچ رہی ہیں، اس لیے دونوں میں 1 کلوگرام کی قیمت کا موازنہ کریں۔", "compare_totals"),
       ("They cost the same per kilogram", "فی کلوگرام دونوں کی قیمت برابر ہے", "600 ÷ 5 = 120 but 880 ÷ 8 = 110. They are not the same.", "600 ÷ 5 = 120 مگر 880 ÷ 8 = 110۔ یہ برابر نہیں۔")],
      0),
   nq("q11_tank", ("A tap fills a tank at 15 litres per minute. How many minutes does it take to put in 180 litres?", "ایک نل ٹینکی کو 15 لیٹر فی منٹ کی شرح سے بھرتا ہے۔ 180 لیٹر بھرنے میں کتنے منٹ لگیں گے؟"), Q11,
      ("How many 15-litre amounts are in 180 litres?", "180 لیٹر میں 15 لیٹر کتنی بار آتے ہیں؟"),
      ("Right! 180 ÷ 15 = 12 minutes.", "درست! 180 ÷ 15 = 12 منٹ"),
      ("Time = total ÷ rate = 180 ÷ 15 = 12 minutes.", "وقت = کل ÷ شرح = 180 ÷ 15 = 12 منٹ"),
      [(2700, "That multiplies 180 by 15. We want the number of minutes, so divide: 12.", "یہ 180 کو 15 سے ضرب دیتا ہے۔ ہمیں منٹ چاہییں، اس لیے تقسیم کریں: 12", "rate_divides")]),
   nq("q12_typist", ("A typist types 120 words in 4 minutes. At the same rate, how many words can she type in 15 minutes?", "ایک ٹائپسٹ 4 منٹ میں 120 الفاظ ٹائپ کرتی ہے۔ اسی شرح سے وہ 15 منٹ میں کتنے الفاظ ٹائپ کرے گی؟"), Q12,
      ("First find the words in 1 minute.", "پہلے 1 منٹ میں الفاظ معلوم کریں۔"),
      ("Right! 30 words a minute and 30 × 15 = 450.", "درست! 30 الفاظ فی منٹ اور 30 × 15 = 450"),
      ("120 ÷ 4 = 30 words per minute. In 15 minutes: 30 × 15 = 450.", "120 ÷ 4 = 30 الفاظ فی منٹ۔ 15 منٹ میں: 30 × 15 = 450"),
      [(30, "That is only the rate for one minute. Multiply by 15 minutes: 450.", "یہ صرف ایک منٹ کی شرح ہے۔ 15 منٹ سے ضرب دیں: 450", "stops_early"),
       (1800, "That multiplies 120 by 15. The 120 words took 4 minutes, so use 30 words per minute: 450.", "یہ 120 کو 15 سے ضرب دیتا ہے۔ 120 الفاظ 4 منٹ میں لکھے گئے، اس لیے 30 الفاظ فی منٹ لیں: 450", "wrong_way_round")]),
   ch("q13_find_error", ("Sana drives 150 km in 3 hours and says her rate is 150 × 3 = 450 km per hour. What went wrong?", "ثناء 3 گھنٹے میں 150 کلومیٹر چلتی ہے اور کہتی ہے اس کی شرح 150 × 3 = 450 کلومیٹر فی گھنٹہ ہے۔ کیا غلطی ہوئی؟"),
      ("A rate per hour is found by dividing: 150 ÷ 3 = 50 km per hour.", "فی گھنٹہ شرح تقسیم سے ملتی ہے: 150 ÷ 3 = 50 کلومیٹر فی گھنٹہ۔", "Yes! She cannot drive 450 km in 3 hours at 50 km per hour: 50 × 3 = 150.", "جی ہاں! 50 کلومیٹر فی گھنٹہ سے 3 گھنٹے میں 150 کلومیٹر بنتے ہیں: 50 × 3 = 150"),
      [("Nothing. Multiplying gives the rate.", "کوئی غلطی نہیں۔ ضرب سے شرح ملتی ہے۔", "Multiplying gives the total distance for a given rate and time, not the rate.", "ضرب سے دی گئی شرح اور وقت کا کل فاصلہ ملتا ہے، شرح نہیں۔", "rate_times"),
       ("She should have added 150 + 3.", "اسے 150 + 3 جمع کرنا چاہیے تھا۔", "Adding kilometres and hours makes no sense. Divide the distance by the time.", "کلومیٹر اور گھنٹے جمع کرنے کا کوئی مطلب نہیں۔ فاصلے کو وقت سے تقسیم کریں۔", "rate_adds")],
      0, qtype="find_error"),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! You worked with rates.", "شاباش! آپ نے شرحوں پر کام کیا۔"),
    "text": T("A rate compares quantities in different units. To find the rate for one unit, divide. To find a total (a cost or a distance), multiply the rate by the number of units or the time. To find the number of units or the time, divide the total by the rate. To compare two rates, find the price or the distance for one unit of each.",
              "شرح مختلف اکائیوں کی مقداروں کا موازنہ ہے۔ ایک اکائی کی شرح کے لیے تقسیم کریں۔ کل (قیمت یا فاصلہ) کے لیے شرح کو اکائیوں کی تعداد یا وقت سے ضرب دیں۔ اکائیوں کی تعداد یا وقت کے لیے کل کو شرح سے تقسیم کریں۔ دو شرحوں کے موازنے کے لیے دونوں کی ایک اکائی کی قیمت یا فاصلہ نکالیں۔"),
    "points": [T("Always write the unit of a rate: Rs per kg, km per hour.", "شرح کی اکائی ہمیشہ لکھیں: روپے فی کلوگرام، کلومیٹر فی گھنٹہ۔"),
               T("Distance = rate × time.", "فاصلہ = شرح × وقت")]},
 ],
 bank=[
   {"id": "qb_rate", "type": "recall", "step": nq("qb_rate", ("7 kg of sugar cost Rs 840. What is the cost of 1 kg in rupees?", "7 کلوگرام چینی کی قیمت 840 روپے ہے۔ 1 کلوگرام کی قیمت کتنے روپے ہے؟"), QB_REC,
      ("Divide the cost by the kilograms.", "قیمت کو کلوگرام سے تقسیم کریں۔"),
      ("Right! 840 ÷ 7 = 120.", "درست! 840 ÷ 7 = 120"), ("840 ÷ 7 = 120 rupees per kg.", "840 ÷ 7 = 120 روپے فی کلوگرام"),
      [(5880, "That multiplies. The cost of one kilogram comes from dividing: 120.", "یہ ضرب ہے۔ ایک کلوگرام کی قیمت تقسیم سے ملتی ہے: 120", "rate_times")], qtype=None)},
   {"id": "qb_distance", "type": "apply", "step": nq("qb_distance", ("A bus travels at 55 km per hour for 3 hours. How many kilometres is that?", "ایک بس 55 کلومیٹر فی گھنٹہ کی رفتار سے 3 گھنٹے چلتی ہے۔ یہ کتنے کلومیٹر ہوئے؟"), QB_APP,
      ("Distance = rate × time.", "فاصلہ = شرح × وقت"),
      ("Right! 55 × 3 = 165 km.", "درست! 55 × 3 = 165 کلومیٹر"), ("55 km each hour for 3 hours: 165 km.", "3 گھنٹے تک ہر گھنٹے 55 کلومیٹر: 165 کلومیٹر"),
      [(58, "That adds 55 and 3. Multiply them: 165.", "یہ 55 اور 3 کو جمع کرتا ہے۔ انہیں ضرب دیں: 165", "rate_adds")], qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": ch("qb_find_error",
      ("Fatima says 4 : 5 and Rs 20 for 5 kg are both rates. What went wrong?", "فاطمہ کہتی ہے 4 : 5 اور 5 کلوگرام کے 20 روپے دونوں شرحیں ہیں۔ کیا غلطی ہوئی؟"),
      ("Only Rs 20 for 5 kg is a rate. 4 : 5 compares two numbers with no different units.", "صرف 5 کلوگرام کے 20 روپے شرح ہے۔ 4 : 5 دو اعداد کا موازنہ ہے جن کی اکائیاں مختلف نہیں۔", "Yes! A rate needs two different units.", "جی ہاں! شرح کے لیے دو مختلف اکائیاں چاہییں۔"),
      [("Nothing. Both are rates.", "کوئی غلطی نہیں۔ دونوں شرحیں ہیں۔", "A ratio like 4 : 5 has no different units, so it is not a rate.", "4 : 5 جیسی نسبت میں مختلف اکائیاں نہیں ہوتیں، اس لیے یہ شرح نہیں۔", "rate_unit"),
       ("Neither is a rate.", "کوئی بھی شرح نہیں۔", "Rs 20 for 5 kg compares rupees with kilograms, so it is a rate.", "5 کلوگرام کے 20 روپے روپوں کا کلوگرام سے موازنہ ہے، اس لیے یہ شرح ہے۔", "rate_unit")],
      0, qtype=None)},
 ],
 review=[
   {"id": "r_rate", "type": "recall", "step": nq("r_rate", ("A worker earns Rs 360 in 9 hours. What is the pay per hour in rupees?", "ایک مزدور 9 گھنٹے میں 360 روپے کماتا ہے۔ فی گھنٹہ اجرت کتنے روپے ہے؟"), R_REC,
      ("Divide the pay by the hours.", "اجرت کو گھنٹوں سے تقسیم کریں۔"),
      ("Right! 360 ÷ 9 = 40.", "درست! 360 ÷ 9 = 40"), ("360 ÷ 9 = 40 rupees an hour.", "360 ÷ 9 = 40 روپے فی گھنٹہ"),
      [(3240, "That multiplies. Divide to find the pay for one hour: 40.", "یہ ضرب ہے۔ ایک گھنٹے کی اجرت کے لیے تقسیم کریں: 40", "rate_times")], qtype=None)},
   {"id": "r_cost", "type": "apply", "step": nq("r_cost", ("Ribbon costs Rs 12 per metre. How much do 7 metres cost, in rupees?", "فیتہ 12 روپے فی میٹر ہے۔ 7 میٹر کی قیمت کتنے روپے ہے؟"), R_APP,
      ("Cost = rate × metres.", "قیمت = شرح × میٹر"),
      ("Right! 12 × 7 = 84.", "درست! 12 × 7 = 84"), ("12 rupees for each of 7 metres: 84.", "7 میٹر میں سے ہر ایک کے 12 روپے: 84"),
      [(19, "That adds. Multiply the rate by the metres: 84.", "یہ جمع ہے۔ شرح کو میٹر سے ضرب دیں: 84", "rate_adds")], qtype=None)},
 ],
 glossary=[T("Rate", "شرح"), T("Unit rate", "اکائی شرح"), T("Per", "فی"), T("Kilometres per hour", "کلومیٹر فی گھنٹہ"), T("Distance", "فاصلہ")],
 flashcards=[
   {"id": "f_rate", "front": T("What is a rate?", "شرح کیا ہے؟"),
    "back": T("A ratio of two quantities in different units, like Rs 60 for 3 kg.", "مختلف اکائیوں کی دو مقداروں کی نسبت، جیسے 3 کلوگرام کے 60 روپے۔")},
   {"id": "f_dist", "front": T("How do you find a distance from a rate?", "شرح سے فاصلہ کیسے نکالتے ہیں؟"),
    "back": T("Distance = rate × time: 4 km/h for 3 hours is 12 km.", "فاصلہ = شرح × وقت: 4 کلومیٹر فی گھنٹہ سے 3 گھنٹے میں 12 کلومیٹر۔")},
 ],
 home_task={"id": "h_prices", "text": T(
   "Look at two sizes of the same product in a shop (for example 1 kg and 5 kg of rice). Write the price of each and work out the price of 1 kg in each. Which size is the better buy?",
   "دکان میں ایک ہی چیز کی دو مقداریں دیکھیں (مثلاً 1 کلوگرام اور 5 کلوگرام چاول)۔ ہر ایک کی قیمت لکھیں اور دونوں میں 1 کلوگرام کی قیمت نکالیں۔ کون سی مقدار بہتر خریداری ہے؟")},
 notes=["Covers the unit rate (q1, q3, q4, q7), what a rate is (q2), total cost and distance from a rate (q5, q6, q8, q9), comparing two rates (q10), finding the time (q11), a two-step rate problem (q12) and a find-the-error question (q13).",
        "Each wrong answer is a real mistake: multiplying when the rate is wanted, dividing when the total is wanted, adding a rate and a time, comparing totals instead of rates, and stopping after the rate.",
        "Urdu terms to check: شرح (rate), اکائی شرح (unit rate), فی (per)."],
 minutes=18,
)

write(lesson)
