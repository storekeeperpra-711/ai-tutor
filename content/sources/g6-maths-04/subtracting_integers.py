from common import (T, opt, say, wrong, signed, number_question, number_line, write,
                    REF, REVIEW, INT_ADD, INT_SUBTRACT)

SKILL = INT_SUBTRACT
S = signed

# s1, s4: 4 °C in the evening, 7 degrees colder at night.
assert 4 - 7 == -3
# s2: foundation
assert -6 + 2 == -4
# s5: the pattern 5 − 2, 5 − 1, 5 − 0, 5 − (−1), 5 − (−2)
PATTERN = [5 - b for b in (2, 1, 0, -1, -2)]
assert PATTERN == [3, 4, 5, 6, 7]
# s6, s7
assert 2 - -6 == 2 + 6 == 8
# s8
assert -3 - 5 == -3 + -5 == -8
# s9: Usman adds the digits and keeps the minus
assert -4 - -9 == 5 and -(4 + 9) == -13
# s10, s11: Lahore 12 °C, Murree −3 °C
assert 12 - -3 == 15
# question bank and review
assert -2 - 6 == -8 and -1 - -7 == 6 and 3 - 9 == -6 and -10 - -4 == -6


def minus(a, b):
    """'5 − (−3)': a negative number after − goes in brackets."""
    return f"{S(a)} − ({S(b)})" if b < 0 else f"{S(a)} − {b}"


lesson = {
 "id": "g6-maths-04-subtracting-integers",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Subtract integers by adding the opposite, and find the difference between two integers.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Subtracting integers", "صحیح اعداد کی تفریق"),
 "estimated_minutes": 13,
 "prerequisites": [{"skill": INT_ADD}],
 "misconceptions": [
   {"id": "minus_negative_is_minus", "description": "Thinks subtracting a negative makes the answer smaller: 5 − (−3) = 2."},
   {"id": "add_digits_keep_minus", "description": "Adds the digits and keeps a minus sign: −4 − (−9) = −13."},
   {"id": "order_swapped", "description": "Swaps the order: works out 7 − 4 instead of 4 − 7 and gets 3."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_rule", "type": "recall", "step": {
     "id": "qb_rule", "type": "choice",
     "prompt": T(f"Which is the same as {minus(-1, -7)}?", f"ان میں سے کون سا {minus(-1, -7)} کے برابر ہے؟"),
     "options": [
       opt("add", "−1 + 7", "−1 + 7", True, "Yes! Subtracting −7 is the same as adding 7. So the answer is 6.", "جی ہاں! −7 تفریق کرنا 7 جمع کرنے کے برابر ہے۔ اس لیے جواب 6 ہے۔"),
       opt("sub", "−1 − 7", "−1 − 7", False, "Subtracting a negative is adding the opposite: −1 + 7.", "منفی عدد تفریق کرنا اس کا مخالف جمع کرنا ہے: −1 + 7", "minus_negative_is_minus"),
       opt("addneg", "−1 + (−7)", "−1 + (−7)", False, "That is −1 − 7. The opposite of −7 is 7, so −1 + 7.", "یہ −1 − 7 ہے۔ −7 کا مخالف 7 ہے، اس لیے −1 + 7", "minus_negative_is_minus"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T(f"Work out {minus(-2, 6)}", f"حل کریں: {minus(-2, 6)}"),
     -8,
     T("Subtracting 6 moves 6 to the left from −2.", "6 تفریق کرنے سے −2 سے 6 بائیں جاتے ہیں۔"),
     T("Right! −2 − 6 = −8.", "درست! −2 − 6 = −8"),
     T("−2 − 6 = −2 + (−6). Same signs: 2 + 6 = 8, keep the minus: −8.", "−2 − 6 = −2 + (−6)۔ ایک جیسی علامتیں: 2 + 6 = 8، منفی رکھیں: −8"),
     common_wrong=[wrong(-4, "Both −2 and −6 go left of 0, so add 2 and 6: −2 − 6 = −8.", "−2 اور −6 دونوں 0 سے بائیں جاتے ہیں، اس لیے 2 اور 6 جمع کریں: −2 − 6 = −8"),
                   wrong(4, "That is −2 + 6. Subtracting 6 moves left, not right.", "یہ −2 + 6 ہے۔ 6 تفریق کرنے سے دائیں نہیں، بائیں جاتے ہیں۔")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T(f"Hira wrote {minus(3, 9)} = 6. What went wrong?", f"حرا نے لکھا {minus(3, 9)} = 6۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("order", "She worked out 9 − 3. From 3, moving 9 to the left gives −6.", "اس نے 9 − 3 حل کیا۔ 3 سے 9 بائیں جانے پر −6 آتا ہے۔", True,
           "Yes! You can't swap the numbers in a subtraction: 3 − 9 = −6.", "جی ہاں! تفریق میں اعداد کی جگہ نہیں بدل سکتے: 3 − 9 = −6"),
       opt("nothing", "Nothing. 9 − 3 = 6.", "کوئی غلطی نہیں۔ 9 − 3 = 6", False,
           "The question is 3 − 9, not 9 − 3. Taking 9 from 3 goes below 0.", "سوال 3 − 9 ہے، 9 − 3 نہیں۔ 3 میں سے 9 لینے سے 0 سے نیچے جاتے ہیں۔", "order_swapped"),
       opt("twelve", "The answer should be 12.", "جواب 12 ہونا چاہیے۔", False,
           "12 is 3 + 9. Subtracting 9 moves left from 3: −6.", "12، 3 + 9 ہے۔ 9 تفریق کرنے سے 3 سے بائیں جاتے ہیں: −6"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_rule", "front": T("How do you subtract an integer?", "صحیح عدد کیسے تفریق کرتے ہیں؟"),
    "back": T("Add its opposite. 5 − (−3) = 5 + 3 = 8, and −3 − 5 = −3 + (−5) = −8.", "اس کا مخالف جمع کریں۔ 5 − (−3) = 5 + 3 = 8، اور −3 − 5 = −3 + (−5) = −8")},
   {"id": "f_difference", "front": T("Lahore is 12 °C and Murree is −3 °C. How much warmer is Lahore?", "لاہور 12 ڈگری اور مری −3 ڈگری ہے۔ لاہور کتنا زیادہ گرم ہے؟"),
    "back": T("12 − (−3) = 12 + 3 = 15 degrees.", "12 − (−3) = 12 + 3 = 15 ڈگری")},
 ],
 "home_tasks": [{"id": "h_pattern", "text": T(
   "Copy and continue this pattern: 4 − 2 = 2, 4 − 1 = 3, 4 − 0 = 4, 4 − (−1) = ?, 4 − (−2) = ? What do you notice? Show it to someone at home.",
   "یہ نمونہ نقل کریں اور آگے بڑھائیں: 4 − 2 = 2، 4 − 1 = 3، 4 − 0 = 4، 4 − (−1) = ؟، 4 − (−2) = ؟ آپ نے کیا دیکھا؟ گھر میں کسی کو دکھائیں۔")}],
 "glossary": [T("Difference", "فرق"), T("Subtract", "تفریق کرنا"), T("Opposite", "مخالف عدد")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious",
      "In Murree it is 4 °C in the evening. At night it gets 7 degrees colder. How cold is the night?",
      "مری میں شام کو 4 ڈگری ہے۔ رات کو 7 ڈگری مزید ٹھنڈ ہو جاتی ہے۔ رات کتنی ٹھنڈی ہے؟"),
    "text": T("Today we subtract integers. First, a quick check of adding.", "آج ہم صحیح اعداد تفریق کریں گے۔ پہلے جمع کا ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("Work out −6 + 2", "حل کریں: −6 + 2"),
     -4,
     T("From −6, move 2 to the right.", "−6 سے 2 دائیں جائیں۔"),
     T("Right! −6 + 2 = −4.", "درست! −6 + 2 = −4"),
     T("Different signs: 6 − 2 = 4, and −6 is further from 0, so −4.", "مختلف علامتیں: 6 − 2 = 4، اور −6 صفر سے زیادہ دور ہے، اس لیے −4"),
     common_wrong=[wrong(4, "−6 is further from 0, so the answer is negative: −4.", "−6 صفر سے زیادہ دور ہے، اس لیے جواب منفی ہے: −4"),
                   wrong(-8, "Adding 2 moves right, towards 0: −4.", "2 جمع کرنے سے دائیں، 0 کی طرف جاتے ہیں: −4")],
     qtype="recall", skill=INT_ADD),
   {"id": "s3_see_it", "type": "explain",
    "character": say("happy", "Subtracting a positive number moves you left.", "مثبت عدد تفریق کرنے سے آپ بائیں جاتے ہیں۔"),
    "text": T("Getting 7 degrees colder is 4 − 7. Start at 4 and move 7 to the LEFT. You pass 0 and keep going.",
              "7 ڈگری مزید ٹھنڈ ہونا 4 − 7 ہے۔ 4 سے شروع کریں اور 7 بائیں جائیں۔ آپ 0 سے گزر کر آگے جاتے ہیں۔")},
   number_line(
     "s4_colder",
     T(f"The marker is on 4. Move it to show {minus(4, 7)}. Press Check.", f"نشان 4 پر ہے۔ اسے ہلا کر {minus(4, 7)} دکھائیں۔ \"جانچیں\" دبائیں۔"),
     -3,
     T("Subtracting 7 means 7 steps to the left.", "7 تفریق کرنے کا مطلب 7 قدم بائیں۔"),
     T("Yes! 4 − 7 = −3. The night is −3 °C.", "جی ہاں! 4 − 7 = −3۔ رات −3 ڈگری ہے۔"),
     T("From 4, count 7 to the left: 3, 2, 1, 0, −1, −2, −3.", "4 سے 7 بائیں گنیں: 3، 2، 1، 0، −1، −2، −3"),
     start=4,
     common_wrong=[wrong("3", "That is 7 − 4. The question is 4 − 7: you go past 0, to −3.", "یہ 7 − 4 ہے۔ سوال 4 − 7 ہے: آپ 0 سے آگے −3 تک جاتے ہیں۔", "order_swapped")]),
   {"id": "s5_pattern", "type": "explain",
    "character": say("thinking", "Look at the pattern. What happens when we take away a negative?", "نمونہ دیکھیں۔ منفی عدد تفریق کرنے سے کیا ہوتا ہے؟"),
    "text": T("5 − 2 = 3, 5 − 1 = 4, 5 − 0 = 5, 5 − (−1) = 6, 5 − (−2) = 7. Each time we take away one less, the answer goes up by 1. So subtracting a negative number is the same as adding its opposite: 5 − (−3) = 5 + 3 = 8. The rule always works: to subtract, add the opposite.",
              "5 − 2 = 3، 5 − 1 = 4، 5 − 0 = 5، 5 − (−1) = 6، 5 − (−2) = 7۔ ہر بار ایک کم تفریق کرنے پر جواب 1 بڑھ جاتا ہے۔ اس لیے منفی عدد تفریق کرنا اس کا مخالف جمع کرنے کے برابر ہے: 5 − (−3) = 5 + 3 = 8۔ یہ اصول ہمیشہ کام کرتا ہے: تفریق کے لیے مخالف جمع کریں۔")},
   {"id": "s6_rewrite", "type": "choice", "question_type": "recall",
    "prompt": T(f"Which is the same as {minus(2, -6)}?", f"ان میں سے کون سا {minus(2, -6)} کے برابر ہے؟"),
    "options": [
      opt("add", "2 + 6", "2 + 6", True, "Yes! Subtracting −6 is adding 6.", "جی ہاں! −6 تفریق کرنا 6 جمع کرنا ہے۔"),
      opt("sub", "2 − 6", "2 − 6", False, "That takes away 6. We are taking away −6, so add the opposite: 2 + 6.", "اس میں 6 تفریق ہو رہا ہے۔ ہم −6 تفریق کر رہے ہیں، اس لیے مخالف جمع کریں: 2 + 6", "minus_negative_is_minus"),
    ]},
   number_question(
     "s7_minus_negative",
     T(f"Work out {minus(2, -6)}", f"حل کریں: {minus(2, -6)}"),
     8,
     T("Change it to 2 + 6.", "اسے 2 + 6 میں بدلیں۔"),
     T("Right! 2 − (−6) = 2 + 6 = 8.", "درست! 2 − (−6) = 2 + 6 = 8"),
     T("Subtracting −6 is adding 6: 2 + 6 = 8.", "−6 تفریق کرنا 6 جمع کرنا ہے: 2 + 6 = 8"),
     common_wrong=[wrong(-4, "That is 2 − 6. Subtracting a negative is adding: 2 + 6 = 8.", "یہ 2 − 6 ہے۔ منفی تفریق کرنا جمع کرنا ہے: 2 + 6 = 8", "minus_negative_is_minus"),
                   wrong(-8, "Subtracting a negative makes the answer bigger: 2 + 6 = 8.", "منفی تفریق کرنے سے جواب بڑا ہوتا ہے: 2 + 6 = 8", "minus_negative_is_minus")]),
   number_question(
     "s8_negative_minus",
     T(f"Work out {minus(-3, 5)}", f"حل کریں: {minus(-3, 5)}"),
     -8,
     T("Add the opposite: −3 + (−5).", "مخالف جمع کریں: −3 + (−5)"),
     T("Right! −3 − 5 = −8.", "درست! −3 − 5 = −8"),
     T("−3 − 5 = −3 + (−5). Same signs: 3 + 5 = 8, keep the minus: −8.", "−3 − 5 = −3 + (−5)۔ ایک جیسی علامتیں: 3 + 5 = 8، منفی رکھیں: −8"),
     common_wrong=[wrong(2, "That is −3 + 5. Subtracting 5 moves left from −3: −8.", "یہ −3 + 5 ہے۔ 5 تفریق کرنے سے −3 سے بائیں جاتے ہیں: −8"),
                   wrong(-2, "Subtracting 5 moves further left from −3, past −5: −8.", "5 تفریق کرنے سے −3 سے مزید بائیں جاتے ہیں: −8"),
                   wrong(8, "Moving left from −3 stays negative: −8.", "−3 سے بائیں جانے پر جواب منفی رہتا ہے: −8")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T(f"Usman wrote {minus(-4, -9)} = −13. What went wrong?", f"عثمان نے لکھا {minus(-4, -9)} = −13۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("opposite", "Subtracting −9 means adding 9: −4 + 9 = 5.", "−9 تفریق کرنے کا مطلب 9 جمع کرنا ہے: −4 + 9 = 5", True,
          "Yes! −4 + 9: different signs, 9 − 4 = 5, and 9 is further from 0.", "جی ہاں! −4 + 9: مختلف علامتیں، 9 − 4 = 5، اور 9 صفر سے زیادہ دور ہے۔"),
      opt("minus5", "The answer should be −5.", "جواب −5 ہونا چاہیے۔", False,
          "The size is right, but −4 + 9 is positive, because 9 is further from 0: 5.", "مقدار درست ہے، مگر −4 + 9 مثبت ہے، کیونکہ 9 صفر سے زیادہ دور ہے: 5"),
      opt("nothing", "Nothing. 4 + 9 = 13 and both are negative.", "کوئی غلطی نہیں۔ 4 + 9 = 13 اور دونوں منفی ہیں۔", False,
          "There is a subtraction here. Taking away −9 means adding 9, so the answer goes up.", "یہاں تفریق ہے۔ −9 تفریق کرنے کا مطلب 9 جمع کرنا ہے، اس لیے جواب بڑھتا ہے۔", "add_digits_keep_minus"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Lahore is 12 °C and Murree is −3 °C. My friend says Lahore is only 9 degrees warmer. Is that right?",
                     "لاہور 12 ڈگری اور مری −3 ڈگری ہے۔ میرا دوست کہتا ہے لاہور صرف 9 ڈگری زیادہ گرم ہے۔ کیا یہ درست ہے؟"),
    "task": T("In your own words: how much warmer is Lahore (12 °C) than Murree (−3 °C), and why? Think of a thermometer.",
              "اپنے الفاظ میں بتائیں: لاہور (12 ڈگری)، مری (−3 ڈگری) سے کتنا زیادہ گرم ہے، اور کیوں؟ تھرمامیٹر کا سوچیں۔"),
    "key_idea": "The difference is 12 − (−3) = 12 + 3 = 15 degrees: 3 degrees from −3 up to 0, then 12 more up to 12. The friend got 9 by doing 12 − 3.",
    "levels": {
      "got_it": "Says 15 degrees, explaining 3 up to zero plus 12 more, or 12 − (−3) = 12 + 3.",
      "partly": "Says 15 with no reason, or says the friend is wrong without the right difference.",
      "not_yet": "Agrees with 9, gives another answer, or no reason."},
    "keywords": [
      ["15", "fifteen", "پندرہ", "pandrah", "۱۵"],
      ["zero", "0", "صفر", "sifar"],
      ["add", "plus", "+", "جمع", "jama"]],
    "fallback_feedback": {
      "got_it": T("Well explained! From −3 up to 0 is 3 degrees, then 12 more: 15 degrees. That is 12 − (−3) = 12 + 3.",
                  "بہت خوب سمجھایا! −3 سے 0 تک 3 ڈگری، پھر 12 مزید: 15 ڈگری۔ یعنی 12 − (−3) = 12 + 3"),
      "partly": T("Good start! Now count: how many degrees from −3 up to 0, and then from 0 up to 12?", "اچھی شروعات! اب گنیں: −3 سے 0 تک کتنی ڈگری، اور پھر 0 سے 12 تک؟"),
      "not_yet": T("Picture a thermometer. Count up from −3 to 0, then from 0 to 12. How many degrees in all?",
                   "ایک تھرمامیٹر کا سوچیں۔ −3 سے 0 تک اوپر گنیں، پھر 0 سے 12 تک۔ کل کتنی ڈگری؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_difference",
     T(f"So how many degrees warmer is Lahore? Work out {minus(12, -3)}", f"تو لاہور کتنی ڈگری زیادہ گرم ہے؟ حل کریں: {minus(12, -3)}"),
     15,
     T("Subtracting −3 is adding 3.", "−3 تفریق کرنا 3 جمع کرنا ہے۔"),
     T("Right! 12 − (−3) = 15. Lahore is 15 degrees warmer.", "درست! 12 − (−3) = 15۔ لاہور 15 ڈگری زیادہ گرم ہے۔"),
     T("12 − (−3) = 12 + 3 = 15.", "12 − (−3) = 12 + 3 = 15"),
     common_wrong=[wrong(9, "That is 12 − 3. Murree is BELOW zero, so add the 3 degrees: 15.", "یہ 12 − 3 ہے۔ مری صفر سے نیچے ہے، اس لیے 3 ڈگری جمع کریں: 15", "minus_negative_is_minus")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Subtracting is just adding the opposite!", "تفریق بس مخالف جمع کرنا ہے!"),
    "text": T("To subtract an integer, add its opposite. 4 − 7 = 4 + (−7) = −3. 5 − (−3) = 5 + 3 = 8. The difference between 12 °C and −3 °C is 12 − (−3) = 15 degrees.",
              "صحیح عدد تفریق کرنے کے لیے اس کا مخالف جمع کریں۔ 4 − 7 = 4 + (−7) = −3۔ 5 − (−3) = 5 + 3 = 8۔ 12 ڈگری اور −3 ڈگری کا فرق 12 − (−3) = 15 ڈگری ہے۔"),
    "points": [T("Subtracting a negative makes the answer bigger.", "منفی تفریق کرنے سے جواب بڑا ہوتا ہے۔"),
               T("You can't swap the numbers: 3 − 9 = −6, but 9 − 3 = 6.", "اعداد کی جگہ نہیں بدل سکتے: 3 − 9 = −6، مگر 9 − 3 = 6")]},
 ],
 "review_questions": [
   {"id": "r_minus_negative", "type": "apply", "skill": SKILL, "step": number_question(
     "r_minus_negative",
     T(f"Work out {minus(-10, -4)}", f"حل کریں: {minus(-10, -4)}"),
     -6,
     T("Change it to −10 + 4.", "اسے −10 + 4 میں بدلیں۔"),
     T("Right! −10 − (−4) = −10 + 4 = −6.", "درست! −10 − (−4) = −10 + 4 = −6"),
     T("Subtracting −4 is adding 4: −10 + 4 = −6.", "−4 تفریق کرنا 4 جمع کرنا ہے: −10 + 4 = −6"),
     common_wrong=[wrong(-14, "Subtracting −4 is adding 4, so move right: −6.", "−4 تفریق کرنا 4 جمع کرنا ہے، اس لیے دائیں جائیں: −6", "minus_negative_is_minus"),
                   wrong(6, "−10 is further from 0, so the answer is negative: −6.", "−10 صفر سے زیادہ دور ہے، اس لیے جواب منفی ہے: −6")],
     qtype=None)},
   {"id": "r_swap", "type": "recall", "skill": SKILL, "step": number_question(
     "r_swap",
     T(f"Work out {minus(3, 9)}", f"حل کریں: {minus(3, 9)}"),
     -6,
     T("From 3, move 9 to the left.", "3 سے 9 بائیں جائیں۔"),
     T("Right! 3 − 9 = −6.", "درست! 3 − 9 = −6"),
     T("3 − 9 = 3 + (−9). 9 − 3 = 6, and −9 is further from 0: −6.", "3 − 9 = 3 + (−9)۔ 9 − 3 = 6، اور −9 صفر سے زیادہ دور ہے: −6"),
     common_wrong=[wrong(6, "That is 9 − 3. Taking 9 from 3 goes below 0: −6.", "یہ 9 − 3 ہے۔ 3 میں سے 9 لینے سے 0 سے نیچے جاتے ہیں: −6", "order_swapped")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Integers unit. No textbook text or exercises were used.",
   "The rule 'subtract = add the opposite' is shown with a pattern (5 − 2, 5 − 1, 5 − 0, 5 − (−1) …) rather than just stated.",
   "Urdu terms to check: فرق (difference), تفریق (subtraction), مخالف عدد (opposite / additive inverse).",
   "The numbers were worked out in content/sources/g6-maths-04/subtracting_integers.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)
