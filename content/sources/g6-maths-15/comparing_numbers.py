from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, WN_PLACE_VALUE, WN_SYSTEMS, WN_COMPARE, LAKH, pk)

SKILL = WN_COMPARE

# s2: value of 3 in 3,20,000
S2 = 3 * LAKH
assert S2 == 300000 and pk(320000) == "3,20,000"
# s4: 98,765 or 1,02,345 (more digits wins, though 9 > 1)
S4 = max(98765, 102345)
assert S4 == 102345 and len(str(102345)) > len(str(98765))
# s5: 7,45,210 or 7,54,120 (same digits; the ten thousands decide)
S5 = max(745210, 754120)
assert S5 == 754120
# s6: smallest of 3,09,000; 3,90,000; 39,000
assert min(309000, 390000, 39000) == 39000
# s7: smallest 6-digit number
S7 = 10 ** 5
assert S7 == 100000 and len(str(S7)) == 6 and len(str(S7 - 1)) == 5
# s8: biggest of 52,000; 5,20,000; 5,02,000
S8 = max(52000, 520000, 502000)
assert S8 == 520000
# s9: 89,999 < 1,00,000
assert 89999 < LAKH
# s11: Town A 3,45,600; Town B 3,54,060
S11 = max(345600, 354060)
assert S11 == 354060
# question bank and review
QB = 10 ** 7 - 1
assert QB == 9999999 and len(str(QB)) == 7
R1 = 10 ** 6
assert R1 == 1000000 and len(str(R1)) == 7
R2 = max(607000, 670000)
assert R2 == 670000

lesson = {
 "id": "g6-maths-15-comparing-numbers",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Compare and order large numbers by counting digits and comparing place by place from the left.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Comparing large numbers", "بڑے اعداد کا موازنہ"),
 "estimated_minutes": 13,
 "prerequisites": [{"skill": WN_SYSTEMS}, {"skill": WN_PLACE_VALUE}],
 "misconceptions": [
   {"id": "first_digit", "description": "Compares the first digits without first counting how many digits each number has."},
   {"id": "wrong_place", "description": "Compares digits in different places, or stops at the first digit when they are equal."},
   {"id": "digit_count", "description": "Mixes up the largest and smallest numbers with a given number of digits."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_rule", "type": "recall", "step": {
     "id": "qb_rule", "type": "choice",
     "prompt": T("Two whole numbers have different numbers of digits. Which is bigger?", "دو مکمل اعداد میں ہندسوں کی تعداد مختلف ہے۔ کون سا بڑا ہے؟"),
     "options": [
       opt("more", "The one with more digits", "جس میں زیادہ ہندسے ہوں", True,
           "Yes! Count the digits first.", "جی ہاں! پہلے ہندسے گنیں۔"),
       opt("first", "The one with the bigger first digit", "جس کا پہلا ہندسہ بڑا ہو", False,
           "Only if they have the same number of digits. More digits wins first.", "صرف تب جب ہندسوں کی تعداد برابر ہو۔ پہلے زیادہ ہندسے جیتتے ہیں۔", "first_digit"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("What is the largest 7-digit number?", "سب سے بڑا 7 ہندسی عدد کون سا ہے؟"),
     QB,
     T("Use the biggest digit in every place.", "ہر مقام پر سب سے بڑا ہندسہ لگائیں۔"),
     T(f"Right! {pk(QB)}.", f"درست! {pk(QB)}"),
     T(f"Seven 9s: {pk(QB)}.", f"سات 9: {pk(QB)}"),
     common_wrong=[wrong(999999, "That has only 6 digits. Seven 9s: 99,99,999.", "اس میں صرف 6 ہندسے ہیں۔ سات 9: 99,99,999", "digit_count"),
                   wrong(1000000, "That is the smallest 7-digit number. The largest is 99,99,999.", "یہ سب سے چھوٹا 7 ہندسی عدد ہے۔ سب سے بڑا 99,99,999 ہے۔", "digit_count")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Zainab says 4,38,000 is bigger than 4,83,000 because 3 comes before 8. What is wrong?", "زینب کہتی ہے 4,38,000 بڑا ہے 4,83,000 سے کیونکہ 3 پہلے آتا ہے۔ کیا غلطی ہے؟"),
     "options": [
       opt("compare", "The lakhs are equal (4), so compare the next place: 8 > 3, so 4,83,000 is bigger.", "لاکھ برابر ہیں (4)، تو اگلا مقام دیکھیں: 8 > 3، تو 4,83,000 بڑا ہے۔", True,
           "Yes! Go left to right until the digits differ.", "جی ہاں! بائیں سے دائیں چلیں جب تک ہندسے مختلف نہ ہوں۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "Compare the ten thousands: 8 is more than 3, so 4,83,000 is bigger.", "دس ہزار کا موازنہ کریں: 8 بڑا ہے 3 سے، تو 4,83,000 بڑا ہے۔", "wrong_place"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_digits", "front": T("Comparing: step 1?", "موازنہ: پہلا قدم؟"),
    "back": T("Count the digits. More digits = bigger.", "ہندسے گنیں۔ زیادہ ہندسے = بڑا")},
   {"id": "f_left", "front": T("Same number of digits?", "ہندسے برابر ہوں؟"),
    "back": T("Compare from the left until two digits differ.", "بائیں سے موازنہ کریں جب تک دو ہندسے مختلف نہ ہوں۔")},
 ],
 "home_tasks": [{"id": "h_prices", "text": T(
   "Find the prices of two things in an advert (a motorbike and a car, or two phones). Which costs more? Explain how you knew.",
   "کسی اشتہار میں دو چیزوں کی قیمتیں دیکھیں (موٹر سائیکل اور گاڑی، یا دو فون)۔ کون سی مہنگی ہے؟ بتائیں آپ کو کیسے پتا چلا۔")}],
 "glossary": [T("Greater than (>)", "بڑا (>)"), T("Less than (<)", "چھوٹا (<)"), T("Order", "ترتیب")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Two villages, two big numbers. Which village has more people? Let's find out!",
                     "دو گاؤں، دو بڑے اعداد۔ کس گاؤں میں زیادہ لوگ ہیں؟ آئیں معلوم کریں!"),
    "text": T("Today we compare and order large numbers. First, a quick place value check.", "آج ہم بڑے اعداد کا موازنہ کریں گے اور انہیں ترتیب دیں گے۔ پہلے مقامی قیمت کا ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("What is the value of the digit 3 in 3,20,000?", "3,20,000 میں 3 کی مقامی قیمت کیا ہے؟"),
     S2,
     T("The 3 is in the lakhs place.", "3 لاکھ کے مقام پر ہے۔"),
     T(f"Right! 3 lakh = {pk(S2)}.", f"درست! 3 لاکھ = {pk(S2)}"),
     T(f"3 is in the lakhs place: {pk(S2)}.", f"3 لاکھ کے مقام پر ہے: {pk(S2)}"),
     common_wrong=[wrong(3, "That is the digit. Its value is 3 lakh.", "یہ ہندسہ ہے۔ اس کی قیمت 3 لاکھ ہے۔")],
     qtype="recall", skill=WN_PLACE_VALUE),
   {"id": "s3_rule", "type": "explain",
    "character": say("happy", "Count the digits first. Then go left to right!", "پہلے ہندسے گنیں۔ پھر بائیں سے دائیں چلیں!"),
    "text": T("Step 1: count the digits. The number with more digits is bigger: 1,02,345 (6 digits) > 98,765 (5 digits). Step 2: if they have the same number of digits, compare from the left. When two digits differ, the bigger digit wins: 7,54,120 > 7,45,210 because 5 > 4 in the ten thousands place.",
              "قدم 1: ہندسے گنیں۔ جس عدد میں زیادہ ہندسے ہوں وہ بڑا ہے: 1,02,345 (6 ہندسے) > 98,765 (5 ہندسے)۔ قدم 2: اگر ہندسے برابر ہوں تو بائیں سے موازنہ کریں۔ جہاں دو ہندسے مختلف ہوں، بڑا ہندسہ جیتتا ہے: 7,54,120 > 7,45,210 کیونکہ دس ہزار کے مقام پر 5 > 4")},
   number_question(
     "s4_digits",
     T("Which is bigger: 98,765 or 1,02,345? Type the bigger number.", "کون سا بڑا ہے: 98,765 یا 1,02,345؟ بڑا عدد لکھیں۔"),
     S4,
     T("Count the digits.", "ہندسے گنیں۔"),
     T(f"Right! {pk(S4)} has 6 digits.", f"درست! {pk(S4)} میں 6 ہندسے ہیں۔"),
     T("1,02,345 has 6 digits and 98,765 has 5, so 1,02,345 is bigger.", "1,02,345 میں 6 ہندسے ہیں اور 98,765 میں 5، تو 1,02,345 بڑا ہے۔"),
     common_wrong=[wrong(98765, "9 > 1, but 98,765 has only 5 digits. 1,02,345 has 6: it is bigger.", "9 > 1، مگر 98,765 میں صرف 5 ہندسے ہیں۔ 1,02,345 میں 6 ہیں: یہ بڑا ہے۔", "first_digit")]),
   number_question(
     "s5_left",
     T("Which is bigger: 7,45,210 or 7,54,120? Type the bigger number.", "کون سا بڑا ہے: 7,45,210 یا 7,54,120؟ بڑا عدد لکھیں۔"),
     S5,
     T("Both have 7 lakh. Look at the next digit.", "دونوں میں 7 لاکھ ہیں۔ اگلا ہندسہ دیکھیں۔"),
     T(f"Right! {pk(S5)}.", f"درست! {pk(S5)}"),
     T("The lakhs are both 7. Ten thousands: 5 > 4, so 7,54,120 is bigger.", "لاکھ دونوں میں 7 ہیں۔ دس ہزار: 5 > 4، تو 7,54,120 بڑا ہے۔"),
     common_wrong=[wrong(745210, "Compare the ten thousands: 5 > 4, so 7,54,120 is bigger.", "دس ہزار کا موازنہ کریں: 5 > 4، تو 7,54,120 بڑا ہے۔", "wrong_place")]),
   {"id": "s6_smallest", "type": "choice",
    "prompt": T("Which is the smallest?", "سب سے چھوٹا کون سا ہے؟"),
    "options": [
      opt("n39000", "39,000", "39,000", True, "Yes! It has only 5 digits.", "جی ہاں! اس میں صرف 5 ہندسے ہیں۔"),
      opt("n309000", "3,09,000", "3,09,000", False, "It has 6 digits. 39,000 has only 5, so 39,000 is smaller.", "اس میں 6 ہندسے ہیں۔ 39,000 میں صرف 5، تو 39,000 چھوٹا ہے۔", "first_digit"),
      opt("n390000", "3,90,000", "3,90,000", False, "That is the biggest. 39,000 has the fewest digits.", "یہ سب سے بڑا ہے۔ 39,000 میں سب سے کم ہندسے ہیں۔"),
    ]},
   number_question(
     "s7_smallest_six",
     T("What is the smallest 6-digit number?", "سب سے چھوٹا 6 ہندسی عدد کون سا ہے؟"),
     S7,
     T("Start with 1, then all zeros.", "1 سے شروع کریں، پھر سب صفر۔"),
     T("Right! 1,00,000 (1 lakh).", "درست! 1,00,000 (1 لاکھ)"),
     T("A 6-digit number can't start with 0, so the smallest is 1,00,000.", "6 ہندسی عدد 0 سے شروع نہیں ہو سکتا، تو سب سے چھوٹا 1,00,000 ہے۔"),
     common_wrong=[wrong(99999, "That is the largest 5-digit number. Add 1: 1,00,000.", "یہ سب سے بڑا 5 ہندسی عدد ہے۔ 1 جمع کریں: 1,00,000", "digit_count"),
                   wrong(111111, "1,00,000 is smaller and still has 6 digits.", "1,00,000 اس سے چھوٹا ہے اور اس میں بھی 6 ہندسے ہیں۔", "digit_count")]),
   number_question(
     "s8_biggest",
     T("Which is the biggest: 52,000; 5,20,000; 5,02,000? Type it.", "سب سے بڑا کون سا ہے: 52,000؛ 5,20,000؛ 5,02,000؟ اسے لکھیں۔"),
     S8,
     T("Two have 6 digits. Compare those from the left.", "دو میں 6 ہندسے ہیں۔ انہیں بائیں سے دیکھیں۔"),
     T(f"Right! {pk(S8)}.", f"درست! {pk(S8)}"),
     T("52,000 has 5 digits. Of the other two, 2 > 0 in the ten thousands, so 5,20,000.", "52,000 میں 5 ہندسے ہیں۔ باقی دو میں دس ہزار پر 2 > 0، تو 5,20,000"),
     common_wrong=[wrong(502000, "Compare the ten thousands: 2 > 0, so 5,20,000 is bigger.", "دس ہزار دیکھیں: 2 > 0، تو 5,20,000 بڑا ہے۔", "wrong_place"),
                   wrong(52000, "52,000 has only 5 digits, so it is the smallest.", "52,000 میں صرف 5 ہندسے ہیں، تو یہ سب سے چھوٹا ہے۔", "first_digit")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Bilal says 89,999 is bigger than 1,00,000 because 8 is bigger than 1. What went wrong?", "بلال کہتا ہے 89,999 بڑا ہے 1,00,000 سے کیونکہ 8 بڑا ہے 1 سے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("digits", "He didn't count the digits. 1,00,000 has 6 digits, so it is bigger.", "اس نے ہندسے نہیں گنے۔ 1,00,000 میں 6 ہندسے ہیں، تو یہ بڑا ہے۔", True,
          "Yes! Count the digits before looking at the first digit.", "جی ہاں! پہلا ہندسہ دیکھنے سے پہلے ہندسے گنیں۔"),
      opt("last", "He should compare the last digits.", "اسے آخری ہندسوں کا موازنہ کرنا چاہیے۔", False,
          "Always start from the left, after counting the digits.", "ہمیشہ بائیں سے شروع کریں، ہندسے گننے کے بعد۔", "wrong_place"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "89,999 is less than 90 thousand. 1,00,000 is 100 thousand.", "89,999 نوے ہزار سے کم ہے۔ 1,00,000 سو ہزار ہے۔", "first_digit"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why is a number with more digits always bigger? Can you teach me?",
                     "زیادہ ہندسوں والا عدد ہمیشہ بڑا کیوں ہوتا ہے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why is any 6-digit number bigger than any 5-digit number?", "اپنے الفاظ میں بتائیں: کوئی بھی 6 ہندسی عدد کسی بھی 5 ہندسی عدد سے بڑا کیوں ہوتا ہے؟"),
    "key_idea": "The biggest 5-digit number is 99,999. The smallest 6-digit number is 1,00,000, which is one more. So every 6-digit number is at least 1 lakh, and every 5-digit number is less than 1 lakh.",
    "levels": {
      "got_it": "Says the largest 5-digit number (99,999) is less than the smallest 6-digit number (1,00,000), or that 6 digits means at least a lakh.",
      "partly": "Says a 6-digit number reaches the lakhs place, without comparing the two.",
      "not_yet": "Gives no reason."},
    "keywords": [
      ["99999", "99,999"],
      ["100000", "1,00,000", "lakh", "لاکھ"],
      ["place", "مقام"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Even the smallest 6-digit number beats the largest 5-digit one.", "بہت خوب! سب سے چھوٹا 6 ہندسی عدد بھی سب سے بڑے 5 ہندسی عدد سے بڑا ہے۔"),
      "partly": T("Good start! Now compare 99,999 with 1,00,000.", "اچھی شروعات! اب 99,999 کا 1,00,000 سے موازنہ کریں۔"),
      "not_yet": T("What is the largest 5-digit number? What is the smallest 6-digit number?", "سب سے بڑا 5 ہندسی عدد کون سا ہے؟ سب سے چھوٹا 6 ہندسی عدد کون سا ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_towns",
     T("Town A has 3,45,600 people. Town B has 3,54,060 people. Type the bigger population.", "قصبہ الف میں 3,45,600 لوگ ہیں۔ قصبہ ب میں 3,54,060 لوگ ہیں۔ زیادہ آبادی لکھیں۔"),
     S11,
     T("Same lakhs (3). Compare the ten thousands.", "لاکھ برابر (3)۔ دس ہزار کا موازنہ کریں۔"),
     T(f"Right! Town B, {pk(S11)}.", f"درست! قصبہ ب، {pk(S11)}"),
     T("Lakhs: 3 and 3. Ten thousands: 5 > 4, so 3,54,060.", "لاکھ: 3 اور 3۔ دس ہزار: 5 > 4، تو 3,54,060"),
     common_wrong=[wrong(345600, "Look at the ten thousands: 5 > 4, so Town B, 3,54,060.", "دس ہزار دیکھیں: 5 > 4، تو قصبہ ب، 3,54,060", "wrong_place")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Count the digits, then go left to right. You are a number judge now!", "ہندسے گنیں، پھر بائیں سے دائیں۔ اب آپ اعداد کے جج ہیں!"),
    "text": T("To compare whole numbers: first count the digits (more digits = bigger). If they have the same number of digits, compare from the left until two digits differ.",
              "مکمل اعداد کا موازنہ: پہلے ہندسے گنیں (زیادہ ہندسے = بڑا)۔ اگر ہندسے برابر ہوں تو بائیں سے موازنہ کریں جب تک دو ہندسے مختلف نہ ہوں۔"),
    "points": [T("More digits = bigger.", "زیادہ ہندسے = بڑا"),
               T("Same digits: compare from the left.", "ہندسے برابر: بائیں سے موازنہ۔")]},
 ],
 "review_questions": [
   {"id": "r_smallest", "type": "apply", "skill": SKILL, "step": number_question(
     "r_smallest",
     T("What is the smallest 7-digit number?", "سب سے چھوٹا 7 ہندسی عدد کون سا ہے؟"),
     R1,
     T("1 followed by six zeros.", "1 کے بعد چھ صفر۔"),
     T(f"Right! {pk(R1)} (10 lakh).", f"درست! {pk(R1)} (10 لاکھ)"),
     T(f"Start with 1, then zeros: {pk(R1)}.", f"1 سے شروع کریں، پھر صفر: {pk(R1)}"),
     common_wrong=[wrong(999999, "That is the largest 6-digit number. Add 1: 10,00,000.", "یہ سب سے بڑا 6 ہندسی عدد ہے۔ 1 جمع کریں: 10,00,000", "digit_count"),
                   wrong(1111111, "10,00,000 is smaller and still has 7 digits.", "10,00,000 اس سے چھوٹا ہے اور اس میں بھی 7 ہندسے ہیں۔", "digit_count")],
     qtype=None)},
   {"id": "r_bigger", "type": "apply", "skill": SKILL, "step": number_question(
     "r_bigger",
     T("Which is bigger: 6,07,000 or 6,70,000? Type the bigger number.", "کون سا بڑا ہے: 6,07,000 یا 6,70,000؟ بڑا عدد لکھیں۔"),
     R2,
     T("Same lakhs. Compare the ten thousands.", "لاکھ برابر۔ دس ہزار دیکھیں۔"),
     T(f"Right! {pk(R2)}.", f"درست! {pk(R2)}"),
     T("Ten thousands: 7 > 0, so 6,70,000.", "دس ہزار: 7 > 0، تو 6,70,000"),
     common_wrong=[wrong(607000, "Ten thousands: 7 > 0, so 6,70,000 is bigger.", "دس ہزار: 7 > 0، تو 6,70,000 بڑا ہے۔", "wrong_place")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Whole Numbers unit. No textbook text or exercises were used.",
   "Steps that ask for the bigger number take a typed answer, so the lesson works without drag-and-drop ordering.",
   "Urdu terms to check: موازنہ (compare), ترتیب (order), ہندسی (digit) as in 6 ہندسی عدد.",
   "The numbers were worked out in content/sources/g6-maths-15/comparing_numbers.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)
