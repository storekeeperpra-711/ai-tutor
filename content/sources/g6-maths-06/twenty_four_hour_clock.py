from common import (T, opt, say, wrong, number_question, write,
                    BOOK, REVIEW, TIMES_TABLES)

SKILL = "maths.time.clock_24"


def to_24(h, m, half):
    """12-hour time to 24-hour time: to_24(3, 45, 'pm') is '15:45'."""
    assert 1 <= h <= 12 and 0 <= m < 60 and half in ("am", "pm")
    hour = h % 12 + (12 if half == "pm" else 0)
    return f"{hour:02d}:{m:02d}"


def to_12(text):
    """'19:30' to (7, 30, 'pm')."""
    hour, m = (int(x) for x in text.split(":"))
    return (hour % 12 or 12, m, "pm" if hour >= 12 else "am")


def minutes_between(start, end):
    (h1, m1), (h2, m2) = ((int(x) for x in t.split(":")) for t in (start, end))
    return (h2 * 60 + m2) - (h1 * 60 + m1)


def accepted(text):
    """Other ways a child may type the same time: 9:10, 0910, 09.10."""
    hour, m = text.split(":")
    forms = {f"{hour}{m}", f"{hour}.{m}", f"{int(hour)}:{m}", f"{int(hour)}.{m}"}
    return sorted(forms - {text})


def time_question(id, prompt, expected, hint, good, bad, *, common_wrong=(), qtype="apply", skill=None):
    step = {"id": id, "type": "text_check"}
    if qtype:
        step["question_type"] = qtype
    if skill:
        step["skill"] = skill
    step.update({
        "prompt": prompt, "checker": "text", "expected": expected,
        "accept": accepted(expected),
        "hint": hint, "feedback_correct": good, "feedback_wrong": bad,
    })
    if common_wrong:
        right = {expected, *step["accept"]}
        assert all(w["answer"] not in right for w in common_wrong), id
        step["common_wrong"] = list(common_wrong)
    return step


# s2: minutes in 3 hours (100 minutes an hour: 300)
S2 = 3 * 60
assert S2 == 180
S4 = to_24(3, 45, "pm")
assert S4 == "15:45"
S5 = to_24(9, 10, "am")
assert S5 == "09:10" and "9:10" in accepted(S5)
assert to_12("19:30") == (7, 30, "pm")
S7 = to_24(12, 20, "am")
assert S7 == "00:20"
# s8: 08:30 to 13:15 (taking 830 from 1315 gives 485)
S8 = minutes_between("08:30", "13:15")
assert S8 == 285 and 1315 - 830 == 485
assert to_12("14:00") == (2, 0, "pm")
S11 = to_24(11, 5, "pm")
assert S11 == "23:05"
QB = to_24(6, 40, "pm")
assert QB == "18:40"
assert to_12("17:00") == (5, 0, "pm")
R1 = to_24(4, 25, "pm")
assert R1 == "16:25"
R2 = minutes_between("09:45", "11:15")
assert R2 == 90 and 1115 - 945 == 170

lesson = {
 "id": "g6-maths-06-24-hour-clock",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Change times between the 12-hour and 24-hour clock, and find how long something takes.", "textbook": f"{BOOK}, Time: 12-hour and 24-hour clock"}],
 "skills": [SKILL],
 "title": T("The 24-hour clock", "24 گھنٹے والی گھڑی"),
 "estimated_minutes": 13,
 "prerequisites": [{"skill": TIMES_TABLES}],
 "misconceptions": [
   {"id": "forgets_twelve", "description": "Leaves pm times as they are instead of adding 12 hours."},
   {"id": "subtracts_ten", "description": "Takes 10 away (not 12) to change a 24-hour time to pm."},
   {"id": "midnight_twelve", "description": "Writes times just after midnight as 12:xx or 24:xx instead of 00:xx."},
   {"id": "subtracts_as_numbers", "description": "Subtracts times like ordinary numbers (1315 − 830), forgetting an hour has 60 minutes."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_midnight", "type": "recall", "step": {
     "id": "qb_midnight", "type": "choice",
     "prompt": T("On the 24-hour clock, 00:00 is …", "24 گھنٹے والی گھڑی پر 00:00 ہے …"),
     "options": [
       opt("midnight", "midnight", "آدھی رات", True, "Yes! The day starts at 00:00.", "جی ہاں! دن 00:00 سے شروع ہوتا ہے۔"),
       opt("noon", "noon (12 in the day)", "دوپہر 12 بجے", False, "Noon is 12:00. 00:00 is midnight.", "دوپہر 12:00 ہے۔ 00:00 آدھی رات ہے۔"),
       opt("broken", "a time that doesn't exist", "ایسا وقت جو ہوتا ہی نہیں", False, "00:00 is real: it is midnight, when the day starts.", "00:00 اصل وقت ہے: آدھی رات، جب دن شروع ہوتا ہے۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": time_question(
     "qb_apply",
     T("Write 6:40 pm on the 24-hour clock.", "شام 6:40 کو 24 گھنٹے والی گھڑی میں لکھیں۔"),
     QB,
     T("pm: add 12 to the hours.", "pm: گھنٹوں میں 12 جمع کریں۔"),
     T("Right! 6 + 12 = 18, so 18:40.", "درست! 6 + 12 = 18، تو 18:40"),
     T("6:40 pm is 6 + 12 = 18 hours: 18:40.", "شام 6:40 یعنی 6 + 12 = 18 گھنٹے: 18:40"),
     common_wrong=[wrong("6:40", "That is still the 12-hour time. Add 12 for pm: 18:40.", "یہ ابھی 12 گھنٹے والا وقت ہے۔ pm کے لیے 12 جمع کریں: 18:40", "forgets_twelve")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Ayesha reads 17:00 on a timetable. She says it is 5 am. What is wrong?", "عائشہ ٹائم ٹیبل پر 17:00 پڑھتی ہے۔ وہ کہتی ہے یہ صبح 5 بجے ہیں۔ کیا غلطی ہے؟"),
     "options": [
       opt("pm", "17 is after 12, so it is 5 pm (17 − 12 = 5).", "17، 12 کے بعد ہے، تو یہ شام 5 بجے ہیں (17 − 12 = 5)", True,
           "Yes! Hours 13 to 23 are pm.", "جی ہاں! 13 سے 23 تک کے گھنٹے pm ہیں۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "5 am is 05:00. 17:00 is in the afternoon: 5 pm.", "صبح 5 بجے 05:00 ہے۔ 17:00 سہ پہر ہے: شام 5 بجے۔"),
       opt("seven", "It is 7 pm.", "یہ شام 7 بجے ہیں۔", False,
           "Take 12 away, not 10: 17 − 12 = 5 pm.", "10 نہیں، 12 تفریق کریں: 17 − 12 = شام 5 بجے", "subtracts_ten"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_pm", "front": T("pm to 24-hour?", "pm سے 24 گھنٹے؟"),
    "back": T("Add 12 to the hours: 3:45 pm = 15:45. (12 noon stays 12:00.)", "گھنٹوں میں 12 جمع کریں: شام 3:45 = 15:45۔ (دوپہر 12 بجے 12:00 ہی رہتا ہے۔)")},
   {"id": "f_midnight", "front": T("Just after midnight?", "آدھی رات کے فوراً بعد؟"),
    "back": T("Hours start again at 00: 12:20 am = 00:20.", "گھنٹے دوبارہ 00 سے شروع: رات 12:20 = 00:20")},
 ],
 "home_tasks": [{"id": "h_day", "text": T(
   "Write 5 times from your day (waking up, school, lunch, dinner, sleep) on the 24-hour clock.",
   "اپنے دن کے 5 وقت (جاگنا، اسکول، دوپہر کا کھانا، رات کا کھانا، سونا) 24 گھنٹے والی گھڑی میں لکھیں۔")}],
 "glossary": [T("24-hour clock", "24 گھنٹے والی گھڑی"), T("Midnight", "آدھی رات"), T("Noon", "دوپہر"), T("Timetable", "ٹائم ٹیبل (اوقاتِ کار)")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "The train ticket says 15:45. But clocks only go up to 12! What time is that?",
                     "ٹرین کے ٹکٹ پر 15:45 لکھا ہے۔ مگر گھڑی تو صرف 12 تک جاتی ہے! یہ کیا وقت ہے؟"),
    "text": T("Today we learn the 24-hour clock that trains, buses and airports use. First, hours and minutes.", "آج ہم 24 گھنٹے والی گھڑی سیکھیں گے جو ٹرینیں، بسیں اور ہوائی اڈے استعمال کرتے ہیں۔ پہلے گھنٹے اور منٹ۔")},
   number_question(
     "s2_foundation",
     T("How many minutes are there in 3 hours?", "3 گھنٹوں میں کتنے منٹ ہیں؟"),
     S2,
     T("1 hour = 60 minutes.", "1 گھنٹہ = 60 منٹ"),
     T("Right! 3 × 60 = 180.", "درست! 3 × 60 = 180"),
     T("Each hour has 60 minutes: 3 × 60 = 180.", "ہر گھنٹے میں 60 منٹ: 3 × 60 = 180"),
     common_wrong=[wrong(300, "An hour has 60 minutes, not 100: 3 × 60 = 180.", "گھنٹے میں 60 منٹ ہیں، 100 نہیں: 3 × 60 = 180", "subtracts_as_numbers")],
     qtype="recall", skill=TIMES_TABLES),
   {"id": "s3_rule", "type": "explain",
    "character": say("happy", "Morning times stay the same. Afternoon and night: add 12 to the hours!", "صبح کے وقت ویسے ہی رہتے ہیں۔ دوپہر اور رات: گھنٹوں میں 12 جمع کریں!"),
    "text": T("The 24-hour clock counts the hours from midnight, 00:00, to 23:59. It always uses four digits. Morning (am) times keep their hours: 9:10 am = 09:10. For afternoon and night (pm), add 12 to the hours: 3:45 pm = 15:45. 12 noon is 12:00, and just after midnight the hours start at 00: 12:20 am = 00:20. To go back, take 12 away from hours 13 to 23: 19:30 = 7:30 pm.",
              "24 گھنٹے والی گھڑی آدھی رات 00:00 سے 23:59 تک گھنٹے گنتی ہے۔ اس میں ہمیشہ چار ہندسے ہوتے ہیں۔ صبح (am) کے وقت کے گھنٹے وہی رہتے ہیں: صبح 9:10 = 09:10۔ دوپہر اور رات (pm) کے لیے گھنٹوں میں 12 جمع کریں: شام 3:45 = 15:45۔ دوپہر 12 بجے 12:00 ہے، اور آدھی رات کے فوراً بعد گھنٹے 00 سے شروع ہوتے ہیں: رات 12:20 = 00:20۔ واپس بدلنے کے لیے 13 سے 23 تک کے گھنٹوں میں سے 12 تفریق کریں: 19:30 = شام 7:30۔")},
   time_question(
     "s4_pm",
     T("Write 3:45 pm on the 24-hour clock.", "سہ پہر 3:45 کو 24 گھنٹے والی گھڑی میں لکھیں۔"),
     S4,
     T("pm: add 12 to the 3.", "pm: 3 میں 12 جمع کریں۔"),
     T("Right! 3 + 12 = 15, so 15:45.", "درست! 3 + 12 = 15، تو 15:45"),
     T("3:45 pm: 3 + 12 = 15 hours, so 15:45.", "سہ پہر 3:45: 3 + 12 = 15 گھنٹے، تو 15:45"),
     common_wrong=[wrong("3:45", "pm times need 12 added: 15:45.", "pm کے وقت میں 12 جمع کرنے ہیں: 15:45", "forgets_twelve"),
                   wrong("03:45", "03:45 is a quarter to four in the early morning. pm: 15:45.", "03:45 تو صبح سویرے کا وقت ہے۔ pm: 15:45", "forgets_twelve")]),
   time_question(
     "s5_am",
     T("Write 9:10 am on the 24-hour clock.", "صبح 9:10 کو 24 گھنٹے والی گھڑی میں لکھیں۔"),
     S5,
     T("Morning: the hours stay the same. Use four digits.", "صبح: گھنٹے وہی رہتے ہیں۔ چار ہندسے لکھیں۔"),
     T("Right! 09:10.", "درست! 09:10"),
     T("Morning times keep their hours: 09:10.", "صبح کے وقت کے گھنٹے وہی رہتے ہیں: 09:10"),
     common_wrong=[wrong("21:10", "Only pm times get 12 added. 9:10 am is 09:10.", "صرف pm کے وقت میں 12 جمع ہوتے ہیں۔ صبح 9:10 یعنی 09:10")]),
   {"id": "s6_back", "type": "choice",
    "prompt": T("A bus leaves at 19:30. What time is that on the 12-hour clock?", "ایک بس 19:30 پر روانہ ہوتی ہے۔ 12 گھنٹے والی گھڑی میں یہ کیا وقت ہے؟"),
    "options": [
      opt("seven_pm", "7:30 pm", "شام 7:30", True, "Yes! 19 − 12 = 7, in the evening.", "جی ہاں! 19 − 12 = 7، شام کو۔"),
      opt("nine_pm", "9:30 pm", "رات 9:30", False, "Take 12 away, not 10: 19 − 12 = 7:30 pm.", "10 نہیں، 12 تفریق کریں: 19 − 12 = شام 7:30", "subtracts_ten"),
      opt("seven_am", "7:30 am", "صبح 7:30", False, "Hours after 12 are pm: 7:30 pm.", "12 کے بعد کے گھنٹے pm ہیں: شام 7:30"),
    ]},
   time_question(
     "s7_midnight",
     T("A train leaves at 12:20 am, just after midnight. Write it on the 24-hour clock.", "ایک ٹرین رات 12:20 پر، آدھی رات کے فوراً بعد، روانہ ہوتی ہے۔ اسے 24 گھنٹے والی گھڑی میں لکھیں۔"),
     S7,
     T("After midnight the hours start at 00.", "آدھی رات کے بعد گھنٹے 00 سے شروع ہوتے ہیں۔"),
     T("Right! 00:20.", "درست! 00:20"),
     T("Just after midnight the hour is 00: 00:20.", "آدھی رات کے فوراً بعد گھنٹہ 00 ہے: 00:20"),
     common_wrong=[wrong("12:20", "12:20 is twenty past noon. After midnight: 00:20.", "12:20 دوپہر کا وقت ہے۔ آدھی رات کے بعد: 00:20", "midnight_twelve"),
                   wrong("24:20", "The clock stops at 23:59 and starts again at 00:00: 00:20.", "گھڑی 23:59 پر رکتی ہے اور 00:00 سے دوبارہ شروع ہوتی ہے: 00:20", "midnight_twelve")]),
   number_question(
     "s8_journey",
     T("A train leaves Lahore at 08:30 and reaches Rawalpindi at 13:15. How many minutes is the journey?", "ایک ٹرین 08:30 پر لاہور سے چلتی ہے اور 13:15 پر راولپنڈی پہنچتی ہے۔ سفر کتنے منٹ کا ہے؟"),
     S8,
     T("08:30 to 13:00 is 4 h 30 min. Then 15 more minutes.", "08:30 سے 13:00 تک 4 گھنٹے 30 منٹ۔ پھر 15 منٹ اور۔"),
     T("Right! 4 hours 45 minutes = 285 minutes.", "درست! 4 گھنٹے 45 منٹ = 285 منٹ"),
     T("08:30 to 13:00 = 270 minutes, plus 15 = 285.", "08:30 سے 13:00 = 270 منٹ، جمع 15 = 285"),
     common_wrong=[wrong(485, "Times can't be taken away like ordinary numbers: an hour is 60 minutes. 285.", "وقت عام اعداد کی طرح تفریق نہیں ہوتا: گھنٹہ 60 منٹ کا ہے۔ 285", "subtracts_as_numbers")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Usman sees 14:00 on a clock. He takes 10 away and says it is 4 pm. What is wrong?", "عثمان گھڑی پر 14:00 دیکھتا ہے۔ وہ 10 تفریق کر کے کہتا ہے کہ شام 4 بجے ہیں۔ کیا غلطی ہے؟"),
    "options": [
      opt("twelve", "Take 12 away, not 10: 14 − 12 = 2 pm.", "10 نہیں، 12 تفریق کریں: 14 − 12 = دوپہر 2 بجے", True,
          "Yes! The 12-hour clock starts again after 12.", "جی ہاں! 12 گھنٹے والی گھڑی 12 کے بعد دوبارہ شروع ہوتی ہے۔"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "4 pm is 16:00. 14:00 is 2 pm.", "شام 4 بجے 16:00 ہے۔ 14:00 دوپہر 2 بجے ہیں۔", "subtracts_ten"),
      opt("am", "It is 2 am.", "رات 2 بجے ہیں۔", False,
          "2 am is 02:00. 14:00 is in the afternoon: 2 pm.", "رات 2 بجے 02:00 ہے۔ 14:00 دوپہر ہے: 2 بجے۔"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why do trains and airports use 24 hours? Can you teach me how to change 8:15 pm?",
                     "ٹرینیں اور ہوائی اڈے 24 گھنٹے کیوں استعمال کرتے ہیں؟ کیا آپ مجھے شام 8:15 بدلنا سکھا سکتے ہیں؟"),
    "task": T("Explain how to write 8:15 pm on the 24-hour clock, and why a timetable might use the 24-hour clock.", "بتائیں کہ شام 8:15 کو 24 گھنٹے والی گھڑی میں کیسے لکھیں، اور ٹائم ٹیبل 24 گھنٹے والی گھڑی کیوں استعمال کر سکتا ہے۔"),
    "key_idea": "8:15 pm is in the evening, so add 12 to the hours: 8 + 12 = 20, giving 20:15. The 24-hour clock gives every time of day its own number, so nobody mixes up morning and evening (08:15 and 20:15).",
    "levels": {
      "got_it": "Adds 12 to get 20:15 and says the 24-hour clock stops am/pm mix-ups (each time has one number).",
      "partly": "Gives 20:15 without a reason for timetables, or gives the reason without the time.",
      "not_yet": "Gives no reason."},
    "keywords": [
      ["20:15", "2015", "20.15"],
      ["12", "twelve", "بارہ"],
      ["am", "pm", "morning", "evening", "صبح", "شام"],
      ["mix", "confus", "الجھن", "غلط"]],
    "fallback_feedback": {
      "got_it": T("Well explained! 20:15, and no am/pm mix-ups.", "بہت خوب! 20:15، اور صبح شام کی الجھن نہیں۔"),
      "partly": T("Good start! Now say why one number for each time helps.", "اچھی شروعات! اب بتائیں کہ ہر وقت کا ایک عدد کیوں مددگار ہے۔"),
      "not_yet": T("pm: add 12 to the 8. What could go wrong with 8:15 on a ticket?", "pm: 8 میں 12 جمع کریں۔ ٹکٹ پر صرف 8:15 ہو تو کیا گڑبڑ ہو سکتی ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   time_question(
     "s11_night",
     T("The last bus leaves at 11:05 pm. Write it on the 24-hour clock.", "آخری بس رات 11:05 پر روانہ ہوتی ہے۔ اسے 24 گھنٹے والی گھڑی میں لکھیں۔"),
     S11,
     T("pm: add 12 to the 11.", "pm: 11 میں 12 جمع کریں۔"),
     T("Right! 23:05.", "درست! 23:05"),
     T("11 + 12 = 23, so 23:05.", "11 + 12 = 23، تو 23:05"),
     common_wrong=[wrong("11:05", "pm: add 12 to the hours. 23:05.", "pm: گھنٹوں میں 12 جمع کریں۔ 23:05", "forgets_twelve")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Now you can read any train or bus timetable!", "اب آپ کوئی بھی ٹرین یا بس کا ٹائم ٹیبل پڑھ سکتے ہیں!"),
    "text": T("The 24-hour clock runs from 00:00 (midnight) to 23:59. Morning times keep their hours (09:10). For pm, add 12 (15:45). To go back, take 12 away from hours 13 to 23. To find how long a journey takes, count hours and minutes; don't subtract the times like ordinary numbers.",
              "24 گھنٹے والی گھڑی 00:00 (آدھی رات) سے 23:59 تک چلتی ہے۔ صبح کے وقت کے گھنٹے وہی رہتے ہیں (09:10)۔ pm کے لیے 12 جمع کریں (15:45)۔ واپس بدلنے کے لیے 13 سے 23 تک کے گھنٹوں سے 12 تفریق کریں۔ سفر کا وقت نکالنے کے لیے گھنٹے اور منٹ گنیں؛ اوقات کو عام اعداد کی طرح تفریق نہ کریں۔"),
    "points": [T("pm: add 12.", "pm: 12 جمع کریں۔"),
               T("Midnight is 00:00.", "آدھی رات 00:00 ہے۔")]},
 ],
 "review_questions": [
   {"id": "r_convert", "type": "apply", "skill": SKILL, "step": time_question(
     "r_convert",
     T("Write 4:25 pm on the 24-hour clock.", "سہ پہر 4:25 کو 24 گھنٹے والی گھڑی میں لکھیں۔"),
     R1,
     T("pm: add 12.", "pm: 12 جمع کریں۔"),
     T("Right! 16:25.", "درست! 16:25"),
     T("4 + 12 = 16, so 16:25.", "4 + 12 = 16، تو 16:25"),
     common_wrong=[wrong("4:25", "Add 12 for pm: 16:25.", "pm کے لیے 12 جمع کریں: 16:25", "forgets_twelve")],
     qtype=None)},
   {"id": "r_minutes", "type": "apply", "skill": SKILL, "step": number_question(
     "r_minutes",
     T("A class starts at 09:45 and ends at 11:15. How many minutes long is it?", "ایک کلاس 09:45 پر شروع ہو کر 11:15 پر ختم ہوتی ہے۔ یہ کتنے منٹ کی ہے؟"),
     R2,
     T("09:45 to 10:00 is 15 minutes; 10:00 to 11:15 is 75.", "09:45 سے 10:00 تک 15 منٹ؛ 10:00 سے 11:15 تک 75"),
     T("Right! 90 minutes.", "درست! 90 منٹ"),
     T("15 + 75 = 90 minutes.", "15 + 75 = 90 منٹ"),
     common_wrong=[wrong(170, "1115 − 945 treats the time like a number. Count: 15 + 75 = 90.", "1115 − 945 وقت کو عدد سمجھتا ہے۔ گنیں: 15 + 75 = 90", "subtracts_as_numbers")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh after matching the app with PCTB Mathematics 6 (Sub-domain 4 includes the 12-hour and 24-hour clock). No textbook text or exercises were used.",
   "Typed times accept 15:45, 1545 and 15.45; a morning time also accepts one hour digit (9:10 for 09:10).",
   "Urdu terms to check: 24 گھنٹے والی گھڑی، آدھی رات (midnight)، دوپہر (noon)، ٹائم ٹیبل.",
   "The numbers were worked out in content/sources/g6-maths-06/twenty_four_hour_clock.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)
