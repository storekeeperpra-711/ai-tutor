"""Practice set for Exercise 4.4 of the book: change between the 12-hour and
24-hour clock, and elapsed-time and arrival-time problems. The questions are
new; only the kinds of question follow the book."""
from common import (T, say, nq, tq, ch, practice_lesson, practice_intro, write, EX_SKILL, TIME_CLOCK)

SKILL = EX_SKILL["4.4"]


def to_24(h, m, half):
    """12-hour time to 24-hour text: to_24(3, 20, 'pm') is '15:20'."""
    assert 1 <= h <= 12 and 0 <= m < 60 and half in ("am", "pm")
    return f"{h % 12 + (12 if half == 'pm' else 0):02d}:{m:02d}"


def to_12(text):
    hour, m = (int(x) for x in text.split(":"))
    return f"{hour % 12 or 12}:{m:02d} {'p.m.' if hour >= 12 else 'a.m.'}"


def mins(text):
    hour, m = (int(x) for x in text.split(":"))
    return hour * 60 + m


def clock(total):
    """Minutes since midnight (wrapping past 24:00) as 24-hour text."""
    total %= 24 * 60
    return f"{total // 60:02d}:{total % 60:02d}"


def gap(start, end):
    """Minutes from start to end, going past midnight if needed."""
    return (mins(end) - mins(start)) % (24 * 60)


# q1
Q1 = to_24(3, 20, "pm")
assert Q1 == "15:20"
# q2: 21:05 is 9:05 p.m.
assert to_12("21:05") == "9:05 p.m." and to_12("09:05") == "9:05 a.m."
# q3
Q3 = to_24(8, 50, "am")
assert Q3 == "08:50"
# q4: 12:30 a.m. is just after midnight
Q4 = to_24(12, 30, "am")
assert Q4 == "00:30" and to_24(12, 30, "pm") == "12:30"
# q5: 12:15 p.m. is just after noon
Q5 = to_24(12, 15, "pm")
assert Q5 == "12:15" and to_24(12, 15, "am") == "00:15"
# q6: 23:55
assert to_12("23:55") == "11:55 p.m." and to_12("11:55") == "11:55 a.m." and to_12("01:55") == "1:55 a.m."
# q7: 09:15 to 13:05 in minutes (digit subtraction 1305 - 915 = 390)
Q7 = gap("09:15", "13:05")
assert Q7 == 230 and 1305 - 915 == 390 and divmod(Q7, 60) == (3, 50)
# q8: leaves 10:40, journey 2 h 35 min
Q8 = clock(mins("10:40") + 2 * 60 + 35)
assert Q8 == "13:15" and 10 * 60 + 40 + 155 == 795
# q9: arrives 17:10 after 3 h 45 min, so left at
Q9 = clock(mins("17:10") - (3 * 60 + 45))
assert Q9 == "13:25" and clock(mins("17:10") + 3 * 60 + 45) == "20:55"
# q10: film starts 22:30, lasts 2 h 50 min
Q10 = clock(mins("22:30") + 2 * 60 + 50)
assert Q10 == "01:20" and 22 * 60 + 30 + 170 == 1520
# q11: 21:50 to 06:10 next day, in minutes
Q11 = gap("21:50", "06:10")
assert Q11 == 500 and divmod(Q11, 60) == (8, 20) and abs(mins("06:10") - mins("21:50")) == 940
# q12: a 40-minute lesson starts at 1:35 p.m.
Q12 = clock(mins(to_24(1, 35, "pm")) + 40)
assert Q12 == "14:15" and to_24(2, 15, "am") == "02:15"
# q13 (find error): 5:30 p.m.
assert to_24(5, 30, "pm") == "17:30" and to_24(5, 30, "am") == "05:30"
# bank and review
QB_REC = to_24(6, 45, "pm")
assert QB_REC == "18:45"
QB_APP = gap("08:20", "11:05")
assert QB_APP == 165
R_REC = to_24(10, 5, "pm")
assert R_REC == "22:05"
R_APP = clock(mins("15:50") + 45)
assert R_APP == "16:35"

lesson = practice_lesson(
 "4.4", script="exercise_4_4.py",
 title=T("Exercise 4.4 practice: time and the 24-hour clock", "مشق 4.4 کی پریکٹس: وقت اور 24 گھنٹے کی گھڑی"),
 outcome="Change times between the 12-hour and 24-hour clock, and find elapsed times and arrival times, including across noon and midnight.",
 prerequisites=[TIME_CLOCK],
 misconceptions=[
   {"id": "noon_midnight", "description": "Gets 12 a.m. and 12 p.m. wrong when changing to the 24-hour clock."},
   {"id": "pm_not_added", "description": "Forgets to add 12 to an afternoon or evening hour (or subtracts 12 from a morning hour)."},
   {"id": "base_100", "description": "Treats minutes as if there were 100 in an hour, so carries or borrows wrongly."},
   {"id": "digit_subtract", "description": "Subtracts the four digits of two clock times as ordinary numbers."},
   {"id": "midnight_wrap", "description": "Does not wrap past 24:00, writing 25:20 instead of 01:20."},
   {"id": "wrong_operation", "description": "Adds the journey time to the arrival time, or subtracts it from the start time."},
 ],
 steps=[
   practice_intro("4.4",
     "Here you change times between the 12-hour and the 24-hour clock and work out how long things take and when they end.",
     "اس میں آپ وقت کو 12 گھنٹے اور 24 گھنٹے کی گھڑی میں بدلیں گے اور معلوم کریں گے کہ چیزوں میں کتنا وقت لگتا ہے اور وہ کب ختم ہوتی ہیں۔",
     "Exercise 4.4 is about time. Ready?", "مشق 4.4 وقت کے بارے میں ہے۔ تیار؟"),
   tq("q1_pm", ("Write 3:20 p.m. on the 24-hour clock (like 15:20).", "3:20 p.m. کو 24 گھنٹے کی گھڑی میں لکھیں (جیسے 15:20)۔"), Q1,
      ("For p.m. times add 12 to the hour.", "p.m. کے اوقات میں گھنٹے میں 12 جمع کریں۔"),
      ("Right! 3 + 12 = 15, so 15:20.", "درست! 3 + 12 = 15، اس لیے 15:20"),
      ("p.m. means after noon: 3 + 12 = 15. The minutes stay the same: 15:20.", "p.m. کا مطلب دوپہر کے بعد: 3 + 12 = 15۔ منٹ وہی رہتے ہیں: 15:20"),
      [("03:20", "03:20 is in the early morning. For p.m. add 12 to the hour: 15:20.", "03:20 صبح سویرے کا وقت ہے۔ p.m. کے لیے گھنٹے میں 12 جمع کریں: 15:20", "pm_not_added")],
      qtype="recall"),
   ch("q2_to_12", ("21:05 on the 24-hour clock is which time on the 12-hour clock?", "24 گھنٹے کی گھڑی کا 21:05، 12 گھنٹے کی گھڑی میں کون سا وقت ہے؟"),
      ("9:05 p.m.", "9:05 p.m.", "Yes! 21 − 12 = 9, and it is after noon, so p.m.", "جی ہاں! 21 − 12 = 9 اور یہ دوپہر کے بعد ہے، اس لیے p.m."),
      [("9:05 a.m.", "9:05 a.m.", "21:00 is in the evening, so it is p.m., not a.m.", "21:00 شام کا وقت ہے، اس لیے a.m. نہیں، p.m. ہے۔", "pm_not_added"),
       ("1:05 p.m.", "1:05 p.m.", "Take 12 away from 21: 21 − 12 = 9, not 1.", "21 میں سے 12 گھٹائیں: 21 − 12 = 9، 1 نہیں۔"),
       ("12:05 p.m.", "12:05 p.m.", "12:05 p.m. is just after noon. Take 12 away from 21: 9:05 p.m.", "12:05 p.m. دوپہر کے فوراً بعد کا وقت ہے۔ 21 میں سے 12 گھٹائیں: 9:05 p.m.", "noon_midnight")],
      2, qtype="recall"),
   {"id": "s_rules", "type": "explain",
    "character": say("thinking", "a.m. is before noon. p.m. is after noon. Add or take away 12.", "a.m. دوپہر سے پہلے، p.m. دوپہر کے بعد۔ 12 جمع یا کم کریں۔"),
    "text": T("The 12-hour clock uses a.m. (ante meridiem, before noon) and p.m. (post meridiem, after noon). The 24-hour clock counts the hours from 00:00 (midnight) to 23:59. For p.m. times add 12 to the hour: 3:20 p.m. = 15:20. For a.m. times keep the hour: 8:50 a.m. = 08:50. Take care at 12: 12:30 a.m. is 00:30, but 12:15 p.m. is 12:15. To change back, take away 12 from hours above 12. An hour has 60 minutes, so when you add or take away, carry or borrow 60, not 100. If a time goes past 24:00, take away 24 hours.",
              "12 گھنٹے کی گھڑی میں a.m. (دوپہر سے پہلے) اور p.m. (دوپہر کے بعد) استعمال ہوتا ہے۔ 24 گھنٹے کی گھڑی گھنٹے 00:00 (آدھی رات) سے 23:59 تک گنتی ہے۔ p.m. کے اوقات میں گھنٹے میں 12 جمع کریں: 3:20 p.m. = 15:20۔ a.m. کے اوقات میں گھنٹہ وہی رکھیں: 8:50 a.m. = 08:50۔ 12 بجے احتیاط کریں: 12:30 a.m. یعنی 00:30، مگر 12:15 p.m. یعنی 12:15۔ واپس بدلنے کے لیے 12 سے بڑے گھنٹوں میں سے 12 گھٹائیں۔ ایک گھنٹے میں 60 منٹ ہیں، اس لیے جمع یا تفریق میں 60 کا حاصل یا ادھار لیں، 100 کا نہیں۔ اگر وقت 24:00 سے آگے نکلے تو 24 گھنٹے گھٹائیں۔")},
   tq("q3_am", ("Write 8:50 a.m. on the 24-hour clock.", "8:50 a.m. کو 24 گھنٹے کی گھڑی میں لکھیں۔"), Q3,
      ("a.m. times keep the same hour. Write the hour with two digits.", "a.m. کے اوقات میں گھنٹہ وہی رہتا ہے۔ گھنٹہ دو ہندسوں میں لکھیں۔"),
      ("Right! 08:50.", "درست! 08:50"),
      ("It is before noon, so nothing is added: 08:50.", "یہ دوپہر سے پہلے کا وقت ہے، اس لیے کچھ جمع نہیں ہوتا: 08:50"),
      [("20:50", "That adds 12. 8:50 a.m. is a morning time, so it stays 08:50.", "یہ 12 جمع کرتا ہے۔ 8:50 a.m. صبح کا وقت ہے، اس لیے 08:50 ہی رہتا ہے۔", "pm_not_added")]),
   tq("q4_midnight", ("Write 12:30 a.m. (half an hour after midnight) on the 24-hour clock.", "12:30 a.m. (آدھی رات کے آدھے گھنٹے بعد) کو 24 گھنٹے کی گھڑی میں لکھیں۔"), Q4,
      ("The 24-hour day starts at 00:00, midnight.", "24 گھنٹے کا دن 00:00، یعنی آدھی رات سے شروع ہوتا ہے۔"),
      ("Right! Midnight is 00:00, so half an hour later is 00:30.", "درست! آدھی رات 00:00 ہے، اس لیے آدھے گھنٹے بعد 00:30 ہے۔"),
      ("12 a.m. is midnight, which is 00 on the 24-hour clock: 00:30.", "12 a.m. آدھی رات ہے، جو 24 گھنٹے کی گھڑی میں 00 ہے: 00:30"),
      [("12:30", "12:30 is half an hour after noon. After midnight it is 00:30.", "12:30 دوپہر کے آدھے گھنٹے بعد ہے۔ آدھی رات کے بعد یہ 00:30 ہے۔", "noon_midnight")]),
   tq("q5_noon", ("Write 12:15 p.m. (a quarter of an hour after noon) on the 24-hour clock.", "12:15 p.m. (دوپہر کے پندرہ منٹ بعد) کو 24 گھنٹے کی گھڑی میں لکھیں۔"), Q5,
      ("Noon is 12:00 on both clocks.", "دوپہر دونوں گھڑیوں میں 12:00 ہے۔"),
      ("Right! Noon is 12:00, so 12:15 stays 12:15.", "درست! دوپہر 12:00 ہے، اس لیے 12:15 وہی رہتا ہے۔"),
      ("After noon the hour is 12, so we do not add 12: 12:15.", "دوپہر کے بعد گھنٹہ 12 ہی ہے، اس لیے 12 جمع نہیں کرتے: 12:15"),
      [("00:15", "00:15 is just after midnight. A quarter of an hour after noon is 12:15.", "00:15 آدھی رات کے فوراً بعد ہے۔ دوپہر کے پندرہ منٹ بعد 12:15 ہے۔", "noon_midnight"),
       ("24:15", "The 24-hour clock has no 24:15. After noon it is 12:15.", "24 گھنٹے کی گھڑی میں 24:15 نہیں ہوتا۔ دوپہر کے بعد 12:15 ہے۔", "noon_midnight")]),
   ch("q6_back", ("A train leaves at 23:55. Which is the same time on the 12-hour clock?", "ایک ٹرین 23:55 پر چلتی ہے۔ 12 گھنٹے کی گھڑی میں یہی وقت کون سا ہے؟"),
      ("11:55 p.m.", "11:55 p.m.", "Yes! 23 − 12 = 11, five minutes before midnight.", "جی ہاں! 23 − 12 = 11، آدھی رات سے پانچ منٹ پہلے۔"),
      [("11:55 a.m.", "11:55 a.m.", "That is five minutes before noon. 23:55 is at night, so p.m.", "یہ دوپہر سے پانچ منٹ پہلے ہے۔ 23:55 رات کا وقت ہے، اس لیے p.m.", "pm_not_added"),
       ("1:55 a.m.", "1:55 a.m.", "That is early morning. Take 12 away from 23: 11:55 p.m.", "یہ صبح سویرے کا وقت ہے۔ 23 میں سے 12 گھٹائیں: 11:55 p.m.", "noon_midnight"),
       ("3:55 p.m.", "3:55 p.m.", "Take 12 away from 23, not 20: 11:55 p.m.", "23 میں سے 12 گھٹائیں، 20 نہیں: 11:55 p.m.")],
      0),
   nq("q7_elapsed", ("A bus leaves at 09:15 and arrives at 13:05. How many minutes does the journey take?", "ایک بس 09:15 پر چلتی ہے اور 13:05 پر پہنچتی ہے۔ سفر میں کتنے منٹ لگتے ہیں؟"), Q7,
      ("From 09:15 to 12:15 is 3 hours. Then count to 13:05.", "09:15 سے 12:15 تک 3 گھنٹے ہیں۔ پھر 13:05 تک گنیں۔"),
      ("Right! 3 hours 50 minutes = 180 + 50 = 230 minutes.", "درست! 3 گھنٹے 50 منٹ = 180 + 50 = 230 منٹ"),
      ("09:15 to 13:15 is 4 hours, but we stop 10 minutes early at 13:05: 3 h 50 min = 230 minutes.", "09:15 سے 13:15 تک 4 گھنٹے ہیں، مگر ہم 10 منٹ پہلے 13:05 پر رک جاتے ہیں: 3 گھنٹے 50 منٹ = 230 منٹ۔"),
      [(390, "That subtracts 915 from 1305 as ordinary numbers. Minutes go up to 60, not 100: 230.", "یہ 1305 میں سے 915 کو عام اعداد کی طرح گھٹاتا ہے۔ منٹ 60 تک جاتے ہیں، 100 تک نہیں: 230", "digit_subtract")]),
   tq("q8_arrival", ("A coach leaves at 10:40 and the journey takes 2 hours 35 minutes. At what time does it arrive? (24-hour clock)", "ایک کوچ 10:40 پر چلتی ہے اور سفر میں 2 گھنٹے 35 منٹ لگتے ہیں۔ یہ کس وقت پہنچتی ہے؟ (24 گھنٹے کی گھڑی)"), Q8,
      ("Add the hours first: 12:40. Then add 35 minutes.", "پہلے گھنٹے جمع کریں: 12:40۔ پھر 35 منٹ جمع کریں۔"),
      ("Right! 12:40 plus 35 minutes is 13:15.", "درست! 12:40 میں 35 منٹ جمع کریں تو 13:15 بنتا ہے۔"),
      ("40 + 35 = 75 minutes = 1 hour 15 minutes. 12 + 1 = 13, so 13:15.", "40 + 35 = 75 منٹ = 1 گھنٹہ 15 منٹ۔ 12 + 1 = 13، اس لیے 13:15"),
      [("12:75", "There are only 60 minutes in an hour. 75 minutes is 1 hour 15 minutes: 13:15.", "ایک گھنٹے میں صرف 60 منٹ ہوتے ہیں۔ 75 منٹ یعنی 1 گھنٹہ 15 منٹ: 13:15", "base_100"),
       ("12:15", "You forgot to carry the extra hour from 75 minutes: 13:15.", "آپ 75 منٹ کا اضافی گھنٹہ جمع کرنا بھول گئے: 13:15", "base_100")]),
   tq("q9_start", ("A train arrives at 17:10 after a journey of 3 hours 45 minutes. At what time did it leave? (24-hour clock)", "ایک ٹرین 3 گھنٹے 45 منٹ کے سفر کے بعد 17:10 پر پہنچتی ہے۔ وہ کس وقت چلی تھی؟ (24 گھنٹے کی گھڑی)"), Q9,
      ("Take away the hours first: 14:10. Then take away 45 minutes.", "پہلے گھنٹے گھٹائیں: 14:10۔ پھر 45 منٹ گھٹائیں۔"),
      ("Right! 14:10 minus 45 minutes is 13:25.", "درست! 14:10 میں سے 45 منٹ گھٹائیں تو 13:25 بنتا ہے۔"),
      ("14:10 is the same as 13:70. Take away 45 minutes: 13:25.", "14:10 دراصل 13:70 ہے۔ 45 منٹ گھٹائیں: 13:25"),
      [("13:35", "That takes 10 minutes away from 45 and ignores the borrowed hour. 13:70 − 45 minutes is 13:25.", "یہ 45 میں سے 10 گھٹاتا ہے اور ادھار کا گھنٹہ نظر انداز کرتا ہے۔ 13:70 − 45 منٹ یعنی 13:25", "base_100"),
       ("20:55", "That adds the journey time. The train left before it arrived: 13:25.", "یہ سفر کا وقت جمع کرتا ہے۔ ٹرین پہنچنے سے پہلے چلی تھی: 13:25", "wrong_operation")]),
   tq("q10_midnight", ("A film starts at 22:30 and lasts 2 hours 50 minutes. At what time does it end? (24-hour clock)", "ایک فلم 22:30 پر شروع ہوتی ہے اور 2 گھنٹے 50 منٹ چلتی ہے۔ یہ کس وقت ختم ہوتی ہے؟ (24 گھنٹے کی گھڑی)"), Q10,
      ("22:30 plus 2 hours is 24:30. A new day starts at 00:00.", "22:30 میں 2 گھنٹے جمع کریں تو 24:30 بنتا ہے۔ نیا دن 00:00 سے شروع ہوتا ہے۔"),
      ("Right! 22:30 + 2 h 50 min = 25:20, which is 01:20 the next day.", "درست! 22:30 + 2 گھنٹے 50 منٹ = 25:20، یعنی اگلے دن 01:20۔"),
      ("22:30 + 2:50 = 25:20. Take away 24 hours: 01:20 the next morning.", "22:30 + 2:50 = 25:20۔ 24 گھنٹے گھٹائیں: اگلی صبح 01:20"),
      [("25:20", "The clock stops at 23:59. Take away 24 hours from 25:20: 01:20.", "گھڑی 23:59 پر رک جاتی ہے۔ 25:20 میں سے 24 گھنٹے گھٹائیں: 01:20", "midnight_wrap")]),
   nq("q11_overnight", ("A night train leaves at 21:50 and arrives at 06:10 the next morning. How many minutes does the journey take?", "ایک رات کی ٹرین 21:50 پر چلتی ہے اور اگلی صبح 06:10 پر پہنچتی ہے۔ سفر میں کتنے منٹ لگتے ہیں؟"), Q11,
      ("21:50 to midnight is 2 hours 10 minutes. Then midnight to 06:10.", "21:50 سے آدھی رات تک 2 گھنٹے 10 منٹ ہیں۔ پھر آدھی رات سے 06:10 تک۔"),
      ("Right! 2 h 10 min + 6 h 10 min = 8 h 20 min = 500 minutes.", "درست! 2 گھنٹے 10 منٹ + 6 گھنٹے 10 منٹ = 8 گھنٹے 20 منٹ = 500 منٹ۔"),
      ("21:50 to 24:00 is 130 minutes. 00:00 to 06:10 is 370 minutes. Total: 500 minutes.", "21:50 سے 24:00 تک 130 منٹ ہیں۔ 00:00 سے 06:10 تک 370 منٹ ہیں۔ کل: 500 منٹ۔"),
      [(940, "That takes 21:50 from 06:10 without going through midnight. Count past midnight: 500.", "یہ آدھی رات سے گزرے بغیر 06:10 اور 21:50 کا فرق لیتا ہے۔ آدھی رات سے آگے گنیں: 500", "midnight_wrap")]),
   tq("q12_lesson", ("A 40-minute lesson starts at 1:35 p.m. At what time does it end? (24-hour clock)", "40 منٹ کا سبق 1:35 p.m. پر شروع ہوتا ہے۔ یہ کس وقت ختم ہوتا ہے؟ (24 گھنٹے کی گھڑی)"), Q12,
      ("1:35 p.m. is 13:35. Then add 40 minutes.", "1:35 p.m. یعنی 13:35۔ پھر 40 منٹ جمع کریں۔"),
      ("Right! 13:35 + 40 minutes = 14:15.", "درست! 13:35 + 40 منٹ = 14:15"),
      ("13:35 + 25 minutes = 14:00, and 15 more minutes: 14:15.", "13:35 + 25 منٹ = 14:00 اور 15 منٹ مزید: 14:15"),
      [("13:75", "There are only 60 minutes in an hour. 13:75 is 14:15.", "ایک گھنٹے میں صرف 60 منٹ ہوتے ہیں۔ 13:75 یعنی 14:15", "base_100"),
       ("02:15", "That is 2:15 a.m. The lesson is in the afternoon: 14:15.", "یہ 2:15 a.m. ہے۔ سبق دوپہر کو ہے: 14:15", "pm_not_added")]),
   ch("q13_find_error", ("Rafay writes 5:30 p.m. as 05:30 on the 24-hour clock. What went wrong?", "رافع 5:30 p.m. کو 24 گھنٹے کی گھڑی میں 05:30 لکھتا ہے۔ کیا غلطی ہوئی؟"),
      ("It is p.m., so 12 must be added to the hour: 17:30.", "یہ p.m. ہے، اس لیے گھنٹے میں 12 جمع کرنا ہے: 17:30", "Yes! 05:30 is half past five in the morning.", "جی ہاں! 05:30 صبح ساڑھے پانچ بجے ہیں۔"),
      [("Nothing. 05:30 is correct for 5:30 p.m.", "کوئی غلطی نہیں۔ 5:30 p.m. کے لیے 05:30 درست ہے۔", "05:30 is 5:30 a.m. The p.m. time needs 12 added: 17:30.", "05:30 تو 5:30 a.m. ہے۔ p.m. وقت میں 12 جمع کرنا ہے: 17:30", "pm_not_added"),
       ("He should have written 15:30.", "اسے 15:30 لکھنا چاہیے تھا۔", "15:30 is 3:30 p.m. Add 12 to 5: 17:30.", "15:30 تو 3:30 p.m. ہے۔ 5 میں 12 جمع کریں: 17:30")],
      0, qtype="find_error"),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! You worked with time.", "شاباش! آپ نے وقت پر کام کیا۔"),
    "text": T("On the 24-hour clock add 12 to p.m. hours and keep a.m. hours, but 12:xx a.m. is 00:xx and 12:xx p.m. stays 12:xx. To find an elapsed time, count to the next hour first, then add the rest. To find an arrival time, add the journey time; to find a start time, take it away. An hour has 60 minutes, and past 24:00 the day starts again.",
              "24 گھنٹے کی گھڑی میں p.m. کے گھنٹوں میں 12 جمع کریں اور a.m. کے گھنٹے وہی رکھیں، مگر 12:xx a.m. یعنی 00:xx اور 12:xx p.m. یعنی 12:xx رہتا ہے۔ گزرا ہوا وقت معلوم کرنے کے لیے پہلے اگلے گھنٹے تک گنیں، پھر باقی جمع کریں۔ پہنچنے کا وقت معلوم کرنے کے لیے سفر کا وقت جمع کریں؛ چلنے کا وقت معلوم کرنے کے لیے گھٹائیں۔ ایک گھنٹے میں 60 منٹ ہیں، اور 24:00 کے بعد دن دوبارہ شروع ہوتا ہے۔"),
    "points": [T("Write minutes with two digits, like 08:05.", "منٹ دو ہندسوں میں لکھیں، جیسے 08:05۔"),
               T("Check: does the answer make sense for morning or evening?", "جانچیں: کیا جواب صبح یا شام کے لحاظ سے درست لگتا ہے؟")]},
 ],
 bank=[
   {"id": "qb_to_24", "type": "recall", "step": tq("qb_to_24", ("Write 6:45 p.m. on the 24-hour clock.", "6:45 p.m. کو 24 گھنٹے کی گھڑی میں لکھیں۔"), QB_REC,
      ("Add 12 to the hour.", "گھنٹے میں 12 جمع کریں۔"),
      ("Right! 6 + 12 = 18, so 18:45.", "درست! 6 + 12 = 18، اس لیے 18:45"), ("p.m.: 6 + 12 = 18. The minutes stay: 18:45.", "p.m.: 6 + 12 = 18۔ منٹ وہی رہتے ہیں: 18:45"),
      [("06:45", "That is a morning time. For p.m. add 12: 18:45.", "یہ صبح کا وقت ہے۔ p.m. کے لیے 12 جمع کریں: 18:45", "pm_not_added")], qtype=None)},
   {"id": "qb_elapsed", "type": "apply", "step": nq("qb_elapsed", ("A class starts at 08:20 and ends at 11:05. How many minutes is the class?", "ایک جماعت 08:20 پر شروع ہوتی ہے اور 11:05 پر ختم ہوتی ہے۔ جماعت کتنے منٹ کی ہے؟"), QB_APP,
      ("08:20 to 10:20 is 2 hours. Then count to 11:05.", "08:20 سے 10:20 تک 2 گھنٹے ہیں۔ پھر 11:05 تک گنیں۔"),
      ("Right! 2 h 45 min = 165 minutes.", "درست! 2 گھنٹے 45 منٹ = 165 منٹ"), ("10:20 to 11:05 is 45 minutes, so 120 + 45 = 165.", "10:20 سے 11:05 تک 45 منٹ ہیں، اس لیے 120 + 45 = 165"),
      [(285, "That subtracts 820 from 1105 as ordinary numbers. Minutes go up to 60: 165.", "یہ 1105 میں سے 820 کو عام اعداد کی طرح گھٹاتا ہے۔ منٹ 60 تک جاتے ہیں: 165", "digit_subtract")], qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": ch("qb_find_error",
      ("Maha says 12:20 a.m. is 12:20 on the 24-hour clock. What went wrong?", "مہا کہتی ہے 12:20 a.m. 24 گھنٹے کی گھڑی میں 12:20 ہے۔ کیا غلطی ہوئی؟"),
      ("12 a.m. is midnight, so 12:20 a.m. is 00:20.", "12 a.m. آدھی رات ہے، اس لیے 12:20 a.m. یعنی 00:20", "Yes! 12:20 on the 24-hour clock is 20 minutes after noon.", "جی ہاں! 24 گھنٹے کی گھڑی میں 12:20 دوپہر کے 20 منٹ بعد ہے۔"),
      [("Nothing. a.m. times do not change.", "کوئی غلطی نہیں۔ a.m. کے اوقات نہیں بدلتے۔", "They do not change, except at 12: 12 a.m. is midnight, 00.", "یہ نہیں بدلتے، سوائے 12 بجے کے: 12 a.m. آدھی رات ہے، یعنی 00۔", "noon_midnight"),
       ("It should be 24:20.", "یہ 24:20 ہونا چاہیے۔", "The 24-hour clock goes 23:59 then 00:00. There is no 24:20.", "24 گھنٹے کی گھڑی 23:59 کے بعد 00:00 پر آتی ہے۔ 24:20 نہیں ہوتا۔", "midnight_wrap")],
      0, qtype=None)},
 ],
 review=[
   {"id": "r_to_24", "type": "recall", "step": tq("r_to_24", ("Write 10:05 p.m. on the 24-hour clock.", "10:05 p.m. کو 24 گھنٹے کی گھڑی میں لکھیں۔"), R_REC,
      ("Add 12 to the hour.", "گھنٹے میں 12 جمع کریں۔"),
      ("Right! 22:05.", "درست! 22:05"), ("10 + 12 = 22, minutes stay: 22:05.", "10 + 12 = 22، منٹ وہی رہتے ہیں: 22:05"),
      [("10:05", "That is the morning time. For p.m. add 12: 22:05.", "یہ صبح کا وقت ہے۔ p.m. کے لیے 12 جمع کریں: 22:05", "pm_not_added")], qtype=None)},
   {"id": "r_arrive", "type": "apply", "step": tq("r_arrive", ("A bus leaves at 15:50 and the journey takes 45 minutes. At what time does it arrive?", "ایک بس 15:50 پر چلتی ہے اور سفر میں 45 منٹ لگتے ہیں۔ یہ کس وقت پہنچتی ہے؟"), R_APP,
      ("15:50 + 10 minutes = 16:00. How many minutes are left?", "15:50 + 10 منٹ = 16:00۔ کتنے منٹ باقی ہیں؟"),
      ("Right! 16:35.", "درست! 16:35"), ("15:50 + 10 min = 16:00, then 35 more minutes: 16:35.", "15:50 + 10 منٹ = 16:00، پھر 35 منٹ مزید: 16:35"),
      [("15:95", "There are only 60 minutes in an hour. 15:95 is 16:35.", "ایک گھنٹے میں صرف 60 منٹ ہوتے ہیں۔ 15:95 یعنی 16:35", "base_100")], qtype=None)},
 ],
 glossary=[T("a.m. (ante meridiem)", "اے ایم (دوپہر سے پہلے)"), T("p.m. (post meridiem)", "پی ایم (دوپہر کے بعد)"), T("24-hour clock", "24 گھنٹے کی گھڑی"), T("Midnight", "آدھی رات"), T("Noon", "دوپہر")],
 flashcards=[
   {"id": "f_pm", "front": T("How do you change a p.m. time to the 24-hour clock?", "p.m. وقت کو 24 گھنٹے کی گھڑی میں کیسے بدلتے ہیں؟"),
    "back": T("Add 12 to the hour: 3:20 p.m. = 15:20. (12:15 p.m. stays 12:15.)", "گھنٹے میں 12 جمع کریں: 3:20 p.m. = 15:20۔ (12:15 p.m. وہی 12:15 رہتا ہے۔)")},
   {"id": "f_midnight", "front": T("What is 12:30 a.m. on the 24-hour clock?", "24 گھنٹے کی گھڑی میں 12:30 a.m. کیا ہے؟"),
    "back": T("00:30. Midnight is 00:00.", "00:30۔ آدھی رات 00:00 ہے۔")},
 ],
 home_task={"id": "h_timetable", "text": T(
   "Write your own school day timetable (when you wake up, leave home, and each lesson starts) on the 24-hour clock. Then work out how long it is from leaving home until the last lesson ends.",
   "اپنے اسکول کے دن کا ٹائم ٹیبل (جاگنا، گھر سے نکلنا، ہر سبق کا آغاز) 24 گھنٹے کی گھڑی میں لکھیں۔ پھر گھر سے نکلنے سے آخری سبق ختم ہونے تک کا وقت معلوم کریں۔")},
 notes=["Covers changing to the 24-hour clock (q1, q3, q4, q5), changing back (q2, q6), elapsed time (q7, q11), arrival and start times (q8, q9, q12), a time that passes midnight (q10, q11) and a find-the-error question (q13).",
        "Each wrong answer is a real mistake: forgetting to add 12, mixing up 12 a.m. and 12 p.m., treating minutes as 100 to an hour, subtracting clock digits as ordinary numbers and not wrapping past 24:00.",
        "Urdu terms to check: اے ایم / پی ایم (a.m. / p.m.), 24 گھنٹے کی گھڑی (24-hour clock), آدھی رات / دوپہر (midnight / noon)."],
 minutes=18,
)

write(lesson)
