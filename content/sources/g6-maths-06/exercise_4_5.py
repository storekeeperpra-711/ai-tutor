"""Practice set for Exercise 4.5 of the book: speed, distance and time, and
changing between km/h and m/s. The questions are new; only the kinds of
question follow the book."""
from fractions import Fraction as F
from common import (T, say, nq, ch, practice_lesson, practice_intro, write, EX_SKILL, RATIO_RATE, RATIO_SPEED)

SKILL = EX_SKILL["4.5"]


def whole(x):
    x = F(x)
    assert x.denominator == 1, x
    return int(x)


def kmh_to_ms(v):
    """km/h to m/s: x 1000 m, / 3600 s, the same as x 5/18."""
    return whole(F(v) * 5 / 18)


def ms_to_kmh(v):
    return whole(F(v) * 18 / 5)


# q1: 180 km in 3 hours
Q1 = whole(F(180, 3))
assert Q1 == 60 and 180 * 3 == 540
# q2: 72 km/h in m/s
Q2 = kmh_to_ms(72)
assert Q2 == 20 and 72 * 1000 / 3600 == 20 and F(72) * 18 / 5 == F(1296, 5) and float(F(1296, 5)) == 259.2
# q3: 15 m/s in km/h
Q3 = ms_to_kmh(15)
assert Q3 == 54 and 15 * 3600 / 1000 == 54 and 15 * 18 == 270
# q4: 48 km/h for 5 hours
Q4 = 48 * 5
assert Q4 == 240 and 48 / 5 == 9.6
# q5: 300 km at 75 km/h
Q5 = whole(F(300, 75))
assert Q5 == 4 and 300 * 75 == 22500
# q6: 90 km/h in m/s
Q6 = kmh_to_ms(90)
assert Q6 == 25 and 90 * 18 // 5 == 324
# q7: 8 m/s for 2 minutes
Q7 = 8 * (2 * 60)
assert Q7 == 960 and 8 * 2 == 16
# q8: 100 m in 20 s, then in km/h
S8 = whole(F(100, 20))
Q8 = ms_to_kmh(S8)
assert S8 == 5 and Q8 == 18 and S8 * 18 == 90
# q9: 25 m/s against a limit of 80 km/h
V9 = ms_to_kmh(25)
assert V9 == 90 and V9 > 80 and 25 < 80
# q10: average speed, 90 km in 2 h then 210 km in 3 h
Q10 = whole(F(90 + 210, 2 + 3))
assert Q10 == 60 and F(90, 2) == 45 and F(210, 3) == 70 and F(45 + 70, 2) == F(115, 2) and float(F(115, 2)) == 57.5
# q11: minutes to cover 45 km at 90 km/h
T11_H = F(45, 90)
Q11 = whole(T11_H * 60)
assert T11_H == F(1, 2) and Q11 == 30 and F(90, 45) == 2
# q12: sound at 340 m/s for 3 s
Q12 = 340 * 3
assert Q12 == 1020 and 340 + 3 == 343
# q13 (find error): 54 km/h to m/s
assert kmh_to_ms(54) == 15 and F(54) * 18 / 5 == F(972, 5)
# bank and review
QB_REC = whole(F(150, 2))
assert QB_REC == 75
QB_APP = kmh_to_ms(36)
assert QB_APP == 10 and F(36) * 18 / 5 == F(648, 5) and float(F(648, 5)) == 129.6
R_REC = whole(F(240, 4))
assert R_REC == 60
R_APP = ms_to_kmh(10)
assert R_APP == 36

lesson = practice_lesson(
 "4.5", script="exercise_4_5.py",
 title=T("Exercise 4.5 practice: speed, distance and time", "مشق 4.5 کی پریکٹس: رفتار، فاصلہ اور وقت"),
 outcome="Find speed, distance and time, change a speed between km/h and m/s, and solve speed-limit and average-speed problems.",
 prerequisites=[RATIO_RATE, RATIO_SPEED],
 misconceptions=[
   {"id": "speed_times", "description": "Multiplies the distance and the time to find a speed, or divides the speed and time to find a distance."},
   {"id": "wrong_factor", "description": "Multiplies by 18/5 when changing km/h to m/s, or by 5/18 when changing m/s to km/h."},
   {"id": "half_conversion", "description": "Multiplies by 18 or by 5 only, without dividing by the other number."},
   {"id": "units_mixed", "description": "Uses minutes with metres per second, or hours with metres, without changing the unit of time."},
   {"id": "mean_of_speeds", "description": "Finds an average speed by averaging the speeds instead of using total distance over total time."},
   {"id": "stops_early", "description": "Finds a speed in m/s and does not change it to km/h as asked."},
   {"id": "time_unit", "description": "Gives the time in hours when minutes are asked for."},
   {"id": "compare_units", "description": "Compares a speed in m/s with a limit in km/h without changing units."},
 ],
 steps=[
   practice_intro("4.5",
     "Here you find speed, distance and time, change speeds between kilometres per hour and metres per second, and solve speed-limit and average-speed problems.",
     "اس میں آپ رفتار، فاصلہ اور وقت معلوم کریں گے، رفتار کو کلومیٹر فی گھنٹہ اور میٹر فی سیکنڈ میں بدلیں گے اور رفتار کی حد اور اوسط رفتار کے سوال حل کریں گے۔",
     "Exercise 4.5 is about speed. Ready?", "مشق 4.5 رفتار کے بارے میں ہے۔ تیار؟"),
   nq("q1_speed", ("A train covers 180 km in 3 hours. What is its speed in km per hour?", "ایک ٹرین 3 گھنٹے میں 180 کلومیٹر طے کرتی ہے۔ اس کی رفتار کلومیٹر فی گھنٹہ میں کیا ہے؟"), Q1,
      ("Speed = distance travelled ÷ time taken.", "رفتار = طے کیا گیا فاصلہ ÷ لگا ہوا وقت"),
      ("Right! 180 ÷ 3 = 60 km/h.", "درست! 180 ÷ 3 = 60 کلومیٹر فی گھنٹہ"),
      ("Speed = 180 km ÷ 3 h = 60 km/h.", "رفتار = 180 کلومیٹر ÷ 3 گھنٹے = 60 کلومیٹر فی گھنٹہ"),
      [(540, "That multiplies. Speed is distance divided by time: 60.", "یہ ضرب ہے۔ رفتار فاصلے کو وقت سے تقسیم کرنے سے ملتی ہے: 60", "speed_times")],
      qtype="recall"),
   nq("q2_kmh_to_ms", ("Change 72 km/h to metres per second.", "72 کلومیٹر فی گھنٹہ کو میٹر فی سیکنڈ میں بدلیں۔"), Q2,
      ("km/h to m/s: multiply by 5/18. 72 ÷ 18 = 4, then × 5.", "کلومیٹر فی گھنٹہ سے میٹر فی سیکنڈ: 5/18 سے ضرب دیں۔ 72 ÷ 18 = 4، پھر × 5"),
      ("Right! 72 × 5/18 = 20 m/s.", "درست! 72 × 5/18 = 20 میٹر فی سیکنڈ"),
      ("1 km = 1000 m and 1 h = 3600 s, so multiply by 5/18: 72 × 5 ÷ 18 = 20 m/s.", "1 کلومیٹر = 1000 میٹر اور 1 گھنٹہ = 3600 سیکنڈ، اس لیے 5/18 سے ضرب دیں: 72 × 5 ÷ 18 = 20 میٹر فی سیکنڈ"),
      [(259.2, "That multiplies by 18/5, which changes m/s to km/h. For km/h to m/s multiply by 5/18: 20.", "یہ 18/5 سے ضرب دیتا ہے، جو میٹر فی سیکنڈ کو کلومیٹر فی گھنٹہ بناتا ہے۔ کلومیٹر فی گھنٹہ سے میٹر فی سیکنڈ کے لیے 5/18 سے ضرب دیں: 20", "wrong_factor")],
      qtype="recall"),
   nq("q3_ms_to_kmh", ("Change 15 m/s to kilometres per hour.", "15 میٹر فی سیکنڈ کو کلومیٹر فی گھنٹہ میں بدلیں۔"), Q3,
      ("m/s to km/h: multiply by 18/5. 15 ÷ 5 = 3, then × 18.", "میٹر فی سیکنڈ سے کلومیٹر فی گھنٹہ: 18/5 سے ضرب دیں۔ 15 ÷ 5 = 3، پھر × 18"),
      ("Right! 15 × 18/5 = 54 km/h.", "درست! 15 × 18/5 = 54 کلومیٹر فی گھنٹہ"),
      ("Multiply by 18/5: 15 ÷ 5 = 3 and 3 × 18 = 54 km/h.", "18/5 سے ضرب دیں: 15 ÷ 5 = 3 اور 3 × 18 = 54 کلومیٹر فی گھنٹہ"),
      [(270, "That multiplies by 18 but forgets to divide by 5: 54.", "یہ 18 سے ضرب دیتا ہے مگر 5 سے تقسیم کرنا بھول جاتا ہے: 54", "half_conversion")],
      qtype="recall"),
   {"id": "s_rules", "type": "explain",
    "character": say("thinking", "km/h to m/s: × 5/18. m/s to km/h: × 18/5.", "کلومیٹر فی گھنٹہ سے میٹر فی سیکنڈ: × 5/18۔ میٹر فی سیکنڈ سے کلومیٹر فی گھنٹہ: × 18/5"),
    "text": T("Speed = distance travelled ÷ time taken, so distance = speed × time and time = distance ÷ speed. Speed is measured in km/h or m/s. Since 1 km = 1000 m and 1 hour = 3600 seconds, 1 km/h = 1000/3600 = 5/18 m/s. To change km/h to m/s multiply by 5/18: 72 km/h = 72 × 5/18 = 20 m/s. To change m/s to km/h multiply by 18/5: 15 m/s = 54 km/h. For an average speed over a whole journey, use total distance ÷ total time.",
              "رفتار = طے کیا گیا فاصلہ ÷ لگا ہوا وقت، اس لیے فاصلہ = رفتار × وقت اور وقت = فاصلہ ÷ رفتار۔ رفتار کلومیٹر فی گھنٹہ یا میٹر فی سیکنڈ میں ناپی جاتی ہے۔ چونکہ 1 کلومیٹر = 1000 میٹر اور 1 گھنٹہ = 3600 سیکنڈ، اس لیے 1 کلومیٹر فی گھنٹہ = 1000/3600 = 5/18 میٹر فی سیکنڈ۔ کلومیٹر فی گھنٹہ کو میٹر فی سیکنڈ بنانے کے لیے 5/18 سے ضرب دیں: 72 کلومیٹر فی گھنٹہ = 72 × 5/18 = 20 میٹر فی سیکنڈ۔ میٹر فی سیکنڈ کو کلومیٹر فی گھنٹہ بنانے کے لیے 18/5 سے ضرب دیں: 15 میٹر فی سیکنڈ = 54 کلومیٹر فی گھنٹہ۔ پورے سفر کی اوسط رفتار کے لیے کل فاصلہ ÷ کل وقت لیں۔")},
   nq("q4_distance", ("A bus travels at 48 km/h for 5 hours. How far does it go, in km?", "ایک بس 48 کلومیٹر فی گھنٹہ کی رفتار سے 5 گھنٹے چلتی ہے۔ وہ کتنے کلومیٹر جاتی ہے؟"), Q4,
      ("Distance = speed × time.", "فاصلہ = رفتار × وقت"),
      ("Right! 48 × 5 = 240 km.", "درست! 48 × 5 = 240 کلومیٹر"),
      ("48 km each hour for 5 hours: 48 × 5 = 240 km.", "5 گھنٹے تک ہر گھنٹے 48 کلومیٹر: 48 × 5 = 240 کلومیٹر"),
      [(9.6, "That divides. To find a distance multiply speed by time: 240.", "یہ تقسیم ہے۔ فاصلہ معلوم کرنے کے لیے رفتار کو وقت سے ضرب دیں: 240", "speed_times")]),
   nq("q5_time", ("A van drives 300 km at 75 km/h. How many hours does it take?", "ایک وین 75 کلومیٹر فی گھنٹہ کی رفتار سے 300 کلومیٹر چلتی ہے۔ اس میں کتنے گھنٹے لگتے ہیں؟"), Q5,
      ("Time = distance ÷ speed.", "وقت = فاصلہ ÷ رفتار"),
      ("Right! 300 ÷ 75 = 4 hours.", "درست! 300 ÷ 75 = 4 گھنٹے"),
      ("Time = 300 ÷ 75 = 4 hours.", "وقت = 300 ÷ 75 = 4 گھنٹے"),
      [(22500, "That multiplies 300 by 75. Time is distance divided by speed: 4.", "یہ 300 کو 75 سے ضرب دیتا ہے۔ وقت فاصلے کو رفتار سے تقسیم کرنے سے ملتا ہے: 4", "speed_times")]),
   nq("q6_kmh_to_ms2", ("A motorbike goes at 90 km/h. What is its speed in m/s?", "ایک موٹر بائیک 90 کلومیٹر فی گھنٹہ کی رفتار سے چلتی ہے۔ اس کی رفتار میٹر فی سیکنڈ میں کیا ہے؟"), Q6,
      ("Multiply by 5/18: 90 ÷ 18 = 5, then × 5.", "5/18 سے ضرب دیں: 90 ÷ 18 = 5، پھر × 5"),
      ("Right! 90 × 5/18 = 25 m/s.", "درست! 90 × 5/18 = 25 میٹر فی سیکنڈ"),
      ("90 × 5 ÷ 18 = 25 m/s.", "90 × 5 ÷ 18 = 25 میٹر فی سیکنڈ"),
      [(324, "That multiplies by 18/5. A speed in m/s is smaller than the same speed in km/h, so multiply by 5/18: 25.", "یہ 18/5 سے ضرب دیتا ہے۔ میٹر فی سیکنڈ کی رفتار کلومیٹر فی گھنٹہ سے چھوٹی ہوتی ہے، اس لیے 5/18 سے ضرب دیں: 25", "wrong_factor")]),
   nq("q7_ms_minutes", ("A cyclist rides at 8 m/s for 2 minutes. How many metres does the cyclist cover?", "ایک سائیکل سوار 8 میٹر فی سیکنڈ کی رفتار سے 2 منٹ چلتا ہے۔ وہ کتنے میٹر طے کرتا ہے؟"), Q7,
      ("The speed is per second, so change 2 minutes to seconds first.", "رفتار فی سیکنڈ ہے، اس لیے پہلے 2 منٹ کو سیکنڈ میں بدلیں۔"),
      ("Right! 2 minutes = 120 seconds and 8 × 120 = 960 m.", "درست! 2 منٹ = 120 سیکنڈ اور 8 × 120 = 960 میٹر"),
      ("2 × 60 = 120 seconds. Distance = 8 × 120 = 960 m.", "2 × 60 = 120 سیکنڈ۔ فاصلہ = 8 × 120 = 960 میٹر"),
      [(16, "That multiplies 8 by 2 minutes, but the speed is in metres per second. Use 120 seconds: 960.", "یہ 8 کو 2 منٹ سے ضرب دیتا ہے، مگر رفتار میٹر فی سیکنڈ میں ہے۔ 120 سیکنڈ لیں: 960", "units_mixed")]),
   nq("q8_two_steps", ("A runner covers 100 m in 20 seconds. What is the speed in km/h?", "ایک دوڑنے والا 20 سیکنڈ میں 100 میٹر طے کرتا ہے۔ اس کی رفتار کلومیٹر فی گھنٹہ میں کیا ہے؟"), Q8,
      ("First find the speed in m/s: 100 ÷ 20. Then multiply by 18/5.", "پہلے میٹر فی سیکنڈ میں رفتار نکالیں: 100 ÷ 20۔ پھر 18/5 سے ضرب دیں۔"),
      ("Right! 5 m/s × 18/5 = 18 km/h.", "درست! 5 میٹر فی سیکنڈ × 18/5 = 18 کلومیٹر فی گھنٹہ"),
      ("100 ÷ 20 = 5 m/s. Then 5 × 18 ÷ 5 = 18 km/h.", "100 ÷ 20 = 5 میٹر فی سیکنڈ۔ پھر 5 × 18 ÷ 5 = 18 کلومیٹر فی گھنٹہ"),
      [(5, "That is the speed in m/s. The question asks for km/h: 18.", "یہ میٹر فی سیکنڈ میں رفتار ہے۔ سوال کلومیٹر فی گھنٹہ مانگتا ہے: 18", "stops_early"),
       (90, "That multiplies by 18 and forgets to divide by 5: 18.", "یہ 18 سے ضرب دیتا ہے اور 5 سے تقسیم کرنا بھول جاتا ہے: 18", "half_conversion")]),
   ch("q9_limit", ("The speed limit on a road is 80 km/h. A car passes a camera at 25 m/s. Is the car over the limit?", "ایک سڑک پر رفتار کی حد 80 کلومیٹر فی گھنٹہ ہے۔ ایک کار کیمرے کے پاس سے 25 میٹر فی سیکنڈ کی رفتار سے گزرتی ہے۔ کیا کار حد سے زیادہ تیز ہے؟"),
      ("Yes, 25 m/s is 90 km/h", "جی ہاں، 25 میٹر فی سیکنڈ یعنی 90 کلومیٹر فی گھنٹہ", "Right! 25 × 18/5 = 90 km/h, which is more than 80.", "درست! 25 × 18/5 = 90 کلومیٹر فی گھنٹہ، جو 80 سے زیادہ ہے۔"),
      [("No, because 25 is less than 80", "نہیں، کیونکہ 25، 80 سے کم ہے", "25 is in m/s and 80 is in km/h. Change them to the same unit first.", "25 میٹر فی سیکنڈ میں ہے اور 80 کلومیٹر فی گھنٹہ میں۔ پہلے دونوں کو ایک ہی اکائی میں بدلیں۔", "compare_units"),
       ("No, 25 m/s is 70 km/h", "نہیں، 25 میٹر فی سیکنڈ یعنی 70 کلومیٹر فی گھنٹہ", "25 × 18/5 = 90, not 70.", "25 × 18/5 = 90، 70 نہیں۔", "wrong_factor")],
      1),
   nq("q10_average", ("A car travels 90 km in the first 2 hours and 210 km in the next 3 hours. What is its average speed for the whole journey, in km/h?", "ایک کار پہلے 2 گھنٹے میں 90 کلومیٹر اور اگلے 3 گھنٹے میں 210 کلومیٹر چلتی ہے۔ پورے سفر کی اوسط رفتار کلومیٹر فی گھنٹہ میں کیا ہے؟"), Q10,
      ("Average speed = total distance ÷ total time.", "اوسط رفتار = کل فاصلہ ÷ کل وقت"),
      ("Right! 300 km in 5 hours is 60 km/h.", "درست! 5 گھنٹے میں 300 کلومیٹر یعنی 60 کلومیٹر فی گھنٹہ"),
      ("Total distance 90 + 210 = 300 km and total time 2 + 3 = 5 h. 300 ÷ 5 = 60 km/h.", "کل فاصلہ 90 + 210 = 300 کلومیٹر اور کل وقت 2 + 3 = 5 گھنٹے۔ 300 ÷ 5 = 60 کلومیٹر فی گھنٹہ"),
      [(57.5, "That averages the two speeds (45 and 70). Use the total distance over the total time: 60.", "یہ دونوں رفتاروں (45 اور 70) کا اوسط لیتا ہے۔ کل فاصلہ کل وقت پر تقسیم کریں: 60", "mean_of_speeds")]),
   nq("q11_minutes", ("A train runs at 90 km/h. How many minutes does it take to cover 45 km?", "ایک ٹرین 90 کلومیٹر فی گھنٹہ کی رفتار سے چلتی ہے۔ 45 کلومیٹر طے کرنے میں کتنے منٹ لگتے ہیں؟"), Q11,
      ("Time = 45 ÷ 90 hours. Change the hours to minutes.", "وقت = 45 ÷ 90 گھنٹے۔ گھنٹوں کو منٹ میں بدلیں۔"),
      ("Right! Half an hour is 30 minutes.", "درست! آدھا گھنٹہ 30 منٹ ہے۔"),
      ("45 ÷ 90 = 1/2 hour, and 1/2 × 60 = 30 minutes.", "45 ÷ 90 = 1/2 گھنٹہ اور 1/2 × 60 = 30 منٹ"),
      [(0.5, "That is the time in hours. The question asks for minutes: 30.", "یہ گھنٹوں میں وقت ہے۔ سوال منٹ مانگتا ہے: 30", "time_unit"),
       (2, "That divides 90 by 45. Time is distance divided by speed: 30 minutes.", "یہ 90 کو 45 سے تقسیم کرتا ہے۔ وقت فاصلہ تقسیم رفتار ہے: 30 منٹ", "speed_times")]),
   nq("q12_sound", ("Sound travels about 340 metres every second. How far does it travel in 3 seconds, in metres?", "آواز تقریباً 340 میٹر فی سیکنڈ کی رفتار سے چلتی ہے۔ 3 سیکنڈ میں وہ کتنے میٹر چلتی ہے؟"), Q12,
      ("Distance = speed × time.", "فاصلہ = رفتار × وقت"),
      ("Right! 340 × 3 = 1,020 m.", "درست! 340 × 3 = 1,020 میٹر"),
      ("340 m each second for 3 seconds: 1,020 m.", "3 سیکنڈ تک ہر سیکنڈ 340 میٹر: 1,020 میٹر"),
      [(343, "That adds. Multiply the speed by the time: 1,020.", "یہ جمع ہے۔ رفتار کو وقت سے ضرب دیں: 1,020", "speed_times")]),
   ch("q13_find_error", ("Zara changes 54 km/h to m/s by multiplying by 18/5. What went wrong?", "زارا 54 کلومیٹر فی گھنٹہ کو 18/5 سے ضرب دے کر میٹر فی سیکنڈ میں بدلتی ہے۔ کیا غلطی ہوئی؟"),
      ("To change km/h to m/s, multiply by 5/18: 54 × 5/18 = 15 m/s.", "کلومیٹر فی گھنٹہ سے میٹر فی سیکنڈ کے لیے 5/18 سے ضرب دیں: 54 × 5/18 = 15 میٹر فی سیکنڈ۔", "Yes! 18/5 changes m/s to km/h, the other way round.", "جی ہاں! 18/5 میٹر فی سیکنڈ کو کلومیٹر فی گھنٹہ بناتا ہے، یعنی الٹ سمت میں۔"),
      [("Nothing. 18/5 is the right number.", "کوئی غلطی نہیں۔ 18/5 درست عدد ہے۔", "A car at 54 km/h does not go at 194 metres in a second. Multiply by 5/18: 15.", "54 کلومیٹر فی گھنٹہ کی کار ایک سیکنڈ میں 194 میٹر نہیں چلتی۔ 5/18 سے ضرب دیں: 15", "wrong_factor"),
       ("She should divide by 1000 only.", "اسے صرف 1000 سے تقسیم کرنا چاہیے تھا۔", "That changes metres to kilometres but ignores that hours become seconds: multiply by 5/18.", "یہ میٹر کو کلومیٹر بناتا ہے مگر گھنٹوں کے سیکنڈ بننے کو نظر انداز کرتا ہے: 5/18 سے ضرب دیں۔", "half_conversion")],
      0, qtype="find_error"),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! You worked with speed.", "شاباش! آپ نے رفتار پر کام کیا۔"),
    "text": T("Speed = distance ÷ time, distance = speed × time, time = distance ÷ speed. To change km/h to m/s multiply by 5/18; to change m/s to km/h multiply by 18/5. Use the same unit before you compare speeds or combine distances with times. Average speed is total distance ÷ total time, not the average of the speeds.",
              "رفتار = فاصلہ ÷ وقت، فاصلہ = رفتار × وقت، وقت = فاصلہ ÷ رفتار۔ کلومیٹر فی گھنٹہ کو میٹر فی سیکنڈ بنانے کے لیے 5/18 سے ضرب دیں؛ میٹر فی سیکنڈ کو کلومیٹر فی گھنٹہ بنانے کے لیے 18/5 سے ضرب دیں۔ رفتاروں کا موازنہ کرنے یا فاصلے اور وقت ملانے سے پہلے ایک ہی اکائی لیں۔ اوسط رفتار کل فاصلہ ÷ کل وقت ہے، رفتاروں کا اوسط نہیں۔"),
    "points": [T("m/s numbers are smaller than km/h numbers for the same speed.", "ایک ہی رفتار کے لیے میٹر فی سیکنڈ کا عدد کلومیٹر فی گھنٹہ سے چھوٹا ہوتا ہے۔"),
               T("Check the unit the question asks for.", "دیکھیں سوال کس اکائی میں جواب مانگتا ہے۔")]},
 ],
 bank=[
   {"id": "qb_speed", "type": "recall", "step": nq("qb_speed", ("A cyclist rides 150 km in 2 hours. What is the speed in km/h?", "ایک سائیکل سوار 2 گھنٹے میں 150 کلومیٹر چلتا ہے۔ رفتار کلومیٹر فی گھنٹہ میں کیا ہے؟"), QB_REC,
      ("Speed = distance ÷ time.", "رفتار = فاصلہ ÷ وقت"),
      ("Right! 150 ÷ 2 = 75.", "درست! 150 ÷ 2 = 75"), ("150 km in 2 h is 75 km each hour.", "2 گھنٹے میں 150 کلومیٹر یعنی ہر گھنٹے 75 کلومیٹر۔"),
      [(300, "That multiplies. Speed is distance divided by time: 75.", "یہ ضرب ہے۔ رفتار فاصلے کو وقت سے تقسیم کرنے سے ملتی ہے: 75", "speed_times")], qtype=None)},
   {"id": "qb_convert", "type": "apply", "step": nq("qb_convert", ("Change 36 km/h to m/s.", "36 کلومیٹر فی گھنٹہ کو میٹر فی سیکنڈ میں بدلیں۔"), QB_APP,
      ("Multiply by 5/18: 36 ÷ 18 = 2, then × 5.", "5/18 سے ضرب دیں: 36 ÷ 18 = 2، پھر × 5"),
      ("Right! 10 m/s.", "درست! 10 میٹر فی سیکنڈ"), ("36 × 5 ÷ 18 = 10 m/s.", "36 × 5 ÷ 18 = 10 میٹر فی سیکنڈ"),
      [(129.6, "That multiplies by 18/5. For km/h to m/s multiply by 5/18: 10.", "یہ 18/5 سے ضرب دیتا ہے۔ کلومیٹر فی گھنٹہ سے میٹر فی سیکنڈ کے لیے 5/18 سے ضرب دیں: 10", "wrong_factor")], qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": ch("qb_find_error",
      ("Umer says a car going 40 m/s is slower than a car going 100 km/h because 40 is less than 100. What went wrong?", "عمر کہتا ہے 40 میٹر فی سیکنڈ کی کار 100 کلومیٹر فی گھنٹہ کی کار سے سست ہے کیونکہ 40، 100 سے کم ہے۔ کیا غلطی ہوئی؟"),
      ("The speeds are in different units. 40 m/s is 144 km/h, which is faster.", "رفتاریں مختلف اکائیوں میں ہیں۔ 40 میٹر فی سیکنڈ یعنی 144 کلومیٹر فی گھنٹہ، جو تیز ہے۔", "Yes! Change to the same unit before comparing.", "جی ہاں! موازنے سے پہلے ایک ہی اکائی میں بدلیں۔"),
      [("Nothing. 40 is less than 100.", "کوئی غلطی نہیں۔ 40، 100 سے کم ہے۔", "You cannot compare numbers in different units.", "مختلف اکائیوں کے اعداد کا موازنہ نہیں ہو سکتا۔", "compare_units"),
       ("They are equal speeds.", "دونوں کی رفتار برابر ہے۔", "40 m/s is 144 km/h, not 100 km/h.", "40 میٹر فی سیکنڈ یعنی 144 کلومیٹر فی گھنٹہ، 100 نہیں۔", "wrong_factor")],
      0, qtype=None)},
 ],
 review=[
   {"id": "r_speed", "type": "recall", "step": nq("r_speed", ("A car covers 240 km in 4 hours. What is its speed in km/h?", "ایک کار 4 گھنٹے میں 240 کلومیٹر طے کرتی ہے۔ اس کی رفتار کلومیٹر فی گھنٹہ میں کیا ہے؟"), R_REC,
      ("Divide the distance by the time.", "فاصلے کو وقت سے تقسیم کریں۔"),
      ("Right! 240 ÷ 4 = 60.", "درست! 240 ÷ 4 = 60"), ("240 ÷ 4 = 60 km/h.", "240 ÷ 4 = 60 کلومیٹر فی گھنٹہ"),
      [(960, "That multiplies. Divide: 60.", "یہ ضرب ہے۔ تقسیم کریں: 60", "speed_times")], qtype=None)},
   {"id": "r_convert", "type": "apply", "step": nq("r_convert", ("Change 10 m/s to km/h.", "10 میٹر فی سیکنڈ کو کلومیٹر فی گھنٹہ میں بدلیں۔"), R_APP,
      ("Multiply by 18/5: 10 ÷ 5 = 2, then × 18.", "18/5 سے ضرب دیں: 10 ÷ 5 = 2، پھر × 18"),
      ("Right! 36 km/h.", "درست! 36 کلومیٹر فی گھنٹہ"), ("10 × 18 ÷ 5 = 36 km/h.", "10 × 18 ÷ 5 = 36 کلومیٹر فی گھنٹہ"),
      [(180, "That multiplies by 18 and forgets to divide by 5: 36.", "یہ 18 سے ضرب دیتا ہے اور 5 سے تقسیم کرنا بھول جاتا ہے: 36", "half_conversion")], qtype=None)},
 ],
 glossary=[T("Speed", "رفتار"), T("Distance", "فاصلہ"), T("Kilometres per hour (km/h)", "کلومیٹر فی گھنٹہ"), T("Metres per second (m/s)", "میٹر فی سیکنڈ"), T("Average speed", "اوسط رفتار")],
 flashcards=[
   {"id": "f_convert", "front": T("How do you change km/h to m/s, and m/s to km/h?", "کلومیٹر فی گھنٹہ سے میٹر فی سیکنڈ اور اس کے الٹ کیسے بدلتے ہیں؟"),
    "back": T("km/h to m/s: × 5/18. m/s to km/h: × 18/5.", "کلومیٹر فی گھنٹہ سے میٹر فی سیکنڈ: × 5/18۔ میٹر فی سیکنڈ سے کلومیٹر فی گھنٹہ: × 18/5۔")},
   {"id": "f_average", "front": T("How do you find an average speed?", "اوسط رفتار کیسے نکالتے ہیں؟"),
    "back": T("Total distance ÷ total time.", "کل فاصلہ ÷ کل وقت۔")},
 ],
 home_task={"id": "h_walk", "text": T(
   "Walk 100 steps at your normal pace and time yourself with a clock or phone. Estimate the distance (a step is about 0.6 m) and work out your speed in m/s and in km/h.",
   "اپنی عام رفتار سے 100 قدم چلیں اور گھڑی یا فون سے وقت نوٹ کریں۔ فاصلے کا اندازہ لگائیں (ایک قدم تقریباً 0.6 میٹر) اور اپنی رفتار میٹر فی سیکنڈ اور کلومیٹر فی گھنٹہ میں نکالیں۔")},
 notes=["Covers speed from distance and time (q1), changing between km/h and m/s (q2, q3, q6, q8), distance and time from speed (q4, q5, q7, q11, q12), a speed-limit problem (q9), average speed (q10) and a find-the-error question (q13).",
        "Each wrong answer is a real mistake: multiplying instead of dividing, using 18/5 and 5/18 the wrong way round, half a conversion, minutes with metres per second, and averaging speeds instead of using total distance over total time.",
        "Urdu terms to check: رفتار (speed), فاصلہ (distance), اوسط رفتار (average speed), کلومیٹر فی گھنٹہ / میٹر فی سیکنڈ (km/h / m/s)."],
 minutes=20,
)

write(lesson)
