from common import (T, opt, say, wrong, signed, number_question, number_line, write,
                    REF, REVIEW, INT_MEANING, INT_ADD)
from figs import jumps_figure, chains_figure, thermometer_move, attach

SKILL = INT_ADD
S = signed

# s1, s4: −3 °C in the morning, 5 degrees warmer by noon.
assert -3 + 5 == 2
# s5: 4 + (−6)
assert 4 + -6 == -2
# s7: same signs
assert -5 + -3 == -8
# s8: different signs, the negative is further from 0
assert -9 + 4 == -5
# s9: Sara adds the digits and keeps the minus
assert -7 + 3 == -4 and -(7 + 3) == -10
# s10: zero pair
assert -4 + 4 == 0
# s11: Rs 6 in pocket, owes Rs 8
assert 6 + -8 == -2
# question bank and review
assert -6 + -2 == -8 and -2 + 7 == 5 and 3 + -10 == -7 and -8 + 8 == 0


def plus(a, b):
    """'−5 + (−3)': a negative number after + goes in brackets."""
    return f"{S(a)} + ({S(b)})" if b < 0 else f"{S(a)} + {b}"


# ---------- pictures ----------

FIG_S1 = thermometer_move(
    -5, 5, -3, 5,
    "A thermometer showing −3 °C, 3 marks below 0. Beside it an arrow goes up 5 marks, marked +5, to a question mark.",
    "ایک تھرمامیٹر جو −3 ڈگری دکھاتا ہے، 0 سے 3 نشان نیچے۔ ساتھ میں ایک تیر 5 نشان اوپر جاتا ہے، اس پر +5 لکھا ہے، اور ایک سوالیہ نشان تک پہنچتا ہے۔")

FIG_S3 = jumps_figure(
    -5, 5, [-3, 5],
    "A number line from −5 to 5. A jump marked +5 starts at −3 and goes 5 steps to the right, landing on 2.",
    "−5 سے 5 تک عددی خط۔ +5 والی ایک چھلانگ −3 سے شروع ہو کر 5 قدم دائیں جاتی ہے اور 2 پر اترتی ہے۔")

FIG_S6 = chains_figure(
    -10, 0, [[-5, -3], [-9, 4]],
    "Two number lines from −10 to 0. On the top one, a jump marked −3 goes left from −5 to −8. On the bottom one, a jump marked +4 goes right from −9 to −5.",
    "−10 سے 0 تک دو عددی خط۔ اوپر والے پر −3 والی چھلانگ −5 سے بائیں −8 تک جاتی ہے۔ نیچے والے پر +4 والی چھلانگ −9 سے دائیں −5 تک جاتی ہے۔")

FIG_S9 = jumps_figure(
    -10, 1, [-7, 3], end_text="?",
    alt_en="A number line from −10 to 1. A jump marked +3 starts at −7 and goes 3 steps to the RIGHT, to a question mark.",
    alt_ur="−10 سے 1 تک عددی خط۔ +3 والی ایک چھلانگ −7 سے شروع ہو کر 3 قدم دائیں جاتی ہے، ایک سوالیہ نشان تک۔")

FIG_S10 = jumps_figure(
    -5, 5, [-4, 4],
    "A number line from −5 to 5. A jump marked +4 starts at −4 and goes 4 steps to the right, landing exactly on 0.",
    "−5 سے 5 تک عددی خط۔ +4 والی ایک چھلانگ −4 سے شروع ہو کر 4 قدم دائیں جاتی ہے اور ٹھیک 0 پر اترتی ہے۔")

FIG_S11 = jumps_figure(
    -4, 8, [6, -8], end_text="?",
    alt_en="A number line from −4 to 8. A jump marked −8 starts at 6 and goes 8 steps to the left, past 0, to a question mark.",
    alt_ur="−4 سے 8 تک عددی خط۔ −8 والی ایک چھلانگ 6 سے شروع ہو کر 8 قدم بائیں جاتی ہے، 0 سے آگے، ایک سوالیہ نشان تک۔")

FIG_S12 = chains_figure(
    -5, 5, [[-3, 5], [4, -6]],
    "Two number lines from −5 to 5. Top: a jump marked +5 goes right from −3 to 2. Bottom: a jump marked −6 goes left from 4 to −2.",
    "−5 سے 5 تک دو عددی خط۔ اوپر: +5 والی چھلانگ −3 سے دائیں 2 تک جاتی ہے۔ نیچے: −6 والی چھلانگ 4 سے بائیں −2 تک جاتی ہے۔",
    every=5)

FIG_QB_ERROR = jumps_figure(
    -8, 4, [3, -10], end_text="?",
    alt_en="A number line from −8 to 4. A jump marked −10 starts at 3 and goes 10 steps to the LEFT, to a question mark.",
    alt_ur="−8 سے 4 تک عددی خط۔ −10 والی ایک چھلانگ 3 سے شروع ہو کر 10 قدم بائیں جاتی ہے، ایک سوالیہ نشان تک۔")

lesson = {
 "id": "g6-maths-04-adding-integers",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Add integers using a number line and the sign rules.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Adding integers", "صحیح اعداد کی جمع"),
 "estimated_minutes": 12,
 "prerequisites": [{"skill": INT_MEANING}],
 "misconceptions": [
   {"id": "add_digits_keep_minus", "description": "Adds the digits and keeps a minus sign when the signs are different: −7 + 3 = −10."},
   {"id": "negative_moves_right", "description": "Moves right on the number line when adding a negative number."},
   {"id": "wrong_sign", "description": "Gets the size right but the sign wrong: 4 + (−6) = 2."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_direction", "type": "recall", "step": {
     "id": "qb_direction", "type": "choice",
     "prompt": T("To add a negative number on the number line, which way do you move?", "عددی خط پر منفی عدد جمع کرنے کے لیے کس طرف جاتے ہیں؟"),
     "options": [
       opt("left", "Left", "بائیں", True, "Yes! Adding a negative number makes the answer smaller.", "جی ہاں! منفی عدد جمع کرنے سے جواب چھوٹا ہو جاتا ہے۔"),
       opt("right", "Right", "دائیں", False, "Right is for adding a positive number. A negative number takes you left.", "دائیں طرف مثبت عدد جمع کرنے کے لیے ہے۔ منفی عدد آپ کو بائیں لے جاتا ہے۔", "negative_moves_right"),
     ]}},
   {"id": "qb_same_sign", "type": "apply", "step": number_question(
     "qb_same_sign",
     T(f"Work out {plus(-6, -2)}", f"حل کریں: {plus(-6, -2)}"),
     -8,
     T("Both are negative: add 6 and 2, and keep the minus sign.", "دونوں منفی ہیں: 6 اور 2 جمع کریں، اور منفی کی علامت رکھیں۔"),
     T("Right! −6 + (−2) = −8.", "درست! −6 + (−2) = −8"),
     T("Start at −6 and move 2 more to the left: −8.", "−6 سے شروع کریں اور 2 مزید بائیں جائیں: −8"),
     common_wrong=[wrong(8, "Both numbers are negative, so the answer is negative too: −8.", "دونوں اعداد منفی ہیں، اس لیے جواب بھی منفی ہے: −8", "wrong_sign"),
                   wrong(-4, "That is −6 + 2. Here you add −2, so move left: −8.", "یہ −6 + 2 ہے۔ یہاں −2 جمع کرنا ہے، اس لیے بائیں جائیں: −8", "negative_moves_right")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Zainab wrote 3 + (−10) = 13. What went wrong?", "زینب نے لکھا 3 + (−10) = 13۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("left", "Adding −10 moves 10 LEFT from 3, so the answer is −7.", "−10 جمع کرنے کا مطلب 3 سے 10 بائیں جانا ہے، اس لیے جواب −7 ہے۔", True,
           "Yes! The signs are different: 10 − 3 = 7, and −10 is further from 0, so −7.", "جی ہاں! علامتیں مختلف ہیں: 10 − 3 = 7، اور −10 صفر سے زیادہ دور ہے، اس لیے −7"),
       opt("nothing", "Nothing. 3 + 10 = 13.", "کوئی غلطی نہیں۔ 3 + 10 = 13", False,
           "She added 10, but the number is −10. It moves you left.", "اس نے 10 جمع کیا، مگر عدد −10 ہے۔ یہ بائیں لے جاتا ہے۔", "negative_moves_right"),
       opt("minus13", "The answer should be −13.", "جواب −13 ہونا چاہیے۔", False,
           "That adds the digits and keeps the minus. The signs are different, so subtract: 10 − 3 = 7, giving −7.", "اس میں ہندسے جمع کر کے منفی رکھ دیا گیا۔ علامتیں مختلف ہیں، اس لیے تفریق کریں: 10 − 3 = 7، یعنی −7", "add_digits_keep_minus"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_same", "front": T("−5 + (−3) = ?", "−5 + (−3) = ؟"),
    "back": T("−8. Same signs: add the numbers and keep the sign.", "−8۔ ایک جیسی علامتیں: اعداد جمع کریں اور علامت رکھیں۔")},
   {"id": "f_different", "front": T("−9 + 4 = ?", "−9 + 4 = ؟"),
    "back": T("−5. Different signs: 9 − 4 = 5, and take the sign of the number further from 0 (−9).", "−5۔ مختلف علامتیں: 9 − 4 = 5، اور اس عدد کی علامت لیں جو 0 سے زیادہ دور ہو (−9)۔")},
   {"id": "f_zero", "front": T("−4 + 4 = ?", "−4 + 4 = ؟"),
    "back": T("0. A number plus its opposite is always 0.", "0۔ کسی عدد اور اس کے مخالف کا مجموعہ ہمیشہ 0 ہوتا ہے۔")},
 ],
 "home_tasks": [{"id": "h_steps", "text": T(
   "Draw a number line from −10 to 10 on the floor with chalk, or on paper. Stand on 2. Take 6 steps back (that is adding −6). Where are you? Make up 3 more for someone at home.",
   "چاک سے فرش پر، یا کاغذ پر، −10 سے 10 تک عددی خط بنائیں۔ 2 پر کھڑے ہوں۔ 6 قدم پیچھے جائیں (یہ −6 جمع کرنا ہے)۔ آپ کہاں ہیں؟ گھر میں کسی کے لیے ایسے 3 مزید سوال بنائیں۔")}],
 "glossary": [T("Sum", "مجموعہ"), T("Integer", "صحیح عدد"), T("Opposite", "مخالف عدد"), T("Zero pair", "صفر جوڑا")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious",
      "In Murree it is −3 °C at sunrise. By noon it is 5 degrees warmer. What is the temperature now?",
      "مری میں صبح −3 ڈگری ہے۔ دوپہر تک 5 ڈگری زیادہ گرم ہو جاتا ہے۔ اب درجہ حرارت کیا ہے؟"),
    "text": T("Today we add integers, positive and negative. First, a quick check.", "آج ہم صحیح اعداد جمع کریں گے، مثبت اور منفی۔ پہلے ایک چھوٹا سا سوال۔")},
   {"id": "s2_foundation", "type": "choice", "question_type": "recall", "skill": INT_MEANING,
    "prompt": T("Which is greater, −1 or −6?", "کون سا بڑا ہے، −1 یا −6؟"),
    "options": [
      opt("m1", S(-1), S(-1), True, "Yes! −1 is to the right of −6.", "جی ہاں! −1، −6 کے دائیں طرف ہے۔"),
      opt("m6", S(-6), S(-6), False, "−6 is further left, so it is smaller.", "−6 زیادہ بائیں ہے، اس لیے چھوٹا ہے۔"),
    ]},
   {"id": "s3_see_it", "type": "explain",
    "character": say("happy", "Adding is moving along the number line!", "جمع کرنا عددی خط پر چلنا ہے!"),
    "text": T("Start at the first number. Adding a positive number moves you RIGHT. Adding a negative number moves you LEFT. For Murree: start at −3 and move 5 to the right.",
              "پہلے عدد سے شروع کریں۔ مثبت عدد جمع کرنے سے آپ دائیں جاتے ہیں۔ منفی عدد جمع کرنے سے آپ بائیں جاتے ہیں۔ مری کے لیے: −3 سے شروع کریں اور 5 دائیں جائیں۔")},
   number_line(
     "s4_warmer",
     T(f"The marker is on −3. Move it to show {plus(-3, 5)}. Press Check.", f"نشان −3 پر ہے۔ اسے ہلا کر {plus(-3, 5)} دکھائیں۔ \"جانچیں\" دبائیں۔"),
     2,
     T("Adding 5 means 5 steps to the right.", "5 جمع کرنے کا مطلب 5 قدم دائیں۔"),
     T("Yes! −3 + 5 = 2. It is 2 °C at noon.", "جی ہاں! −3 + 5 = 2۔ دوپہر کو 2 ڈگری ہے۔"),
     T("From −3, count 5 to the right: −2, −1, 0, 1, 2.", "−3 سے 5 دائیں گنیں: −2، −1، 0، 1، 2"),
     start=-3,
     common_wrong=[wrong("-8", "That is 5 to the left. Adding a positive number moves right.", "یہ 5 بائیں ہے۔ مثبت عدد جمع کرنے سے دائیں جاتے ہیں۔", "negative_moves_right")]),
   number_line(
     "s5_add_negative",
     T(f"The marker is on 4. Move it to show {plus(4, -6)}. Press Check.", f"نشان 4 پر ہے۔ اسے ہلا کر {plus(4, -6)} دکھائیں۔ \"جانچیں\" دبائیں۔"),
     -2,
     T("Adding −6 means 6 steps to the LEFT.", "−6 جمع کرنے کا مطلب 6 قدم بائیں۔"),
     T("Yes! 4 + (−6) = −2.", "جی ہاں! 4 + (−6) = −2"),
     T("From 4, count 6 to the left: 3, 2, 1, 0, −1, −2.", "4 سے 6 بائیں گنیں: 3، 2، 1، 0، −1، −2"),
     start=4,
     common_wrong=[wrong("10", "That is 6 to the right. Adding a negative number moves left.", "یہ 6 دائیں ہے۔ منفی عدد جمع کرنے سے بائیں جاتے ہیں۔", "negative_moves_right"),
                   wrong("2", "Close, but the sign is wrong. You went past 0, so the answer is −2.", "قریب، مگر علامت غلط ہے۔ آپ 0 سے آگے گئے، اس لیے جواب −2 ہے۔", "wrong_sign")]),
   {"id": "s6_rules", "type": "explain",
    "character": say("thinking", "Two rules, so you don't need the number line every time.", "دو اصول، تاکہ ہر بار عددی خط کی ضرورت نہ پڑے۔"),
    "text": T("Same signs: add the numbers and keep the sign. −5 + (−3) = −8. Different signs: subtract the smaller from the bigger (ignoring signs), and take the sign of the number further from 0. −9 + 4: 9 − 4 = 5, and −9 is further from 0, so the answer is −5.",
              "ایک جیسی علامتیں: اعداد جمع کریں اور علامت رکھیں۔ −5 + (−3) = −8۔ مختلف علامتیں: علامتوں کو چھوڑ کر بڑے میں سے چھوٹا تفریق کریں، اور اس عدد کی علامت لیں جو 0 سے زیادہ دور ہو۔ −9 + 4: 9 − 4 = 5، اور −9 صفر سے زیادہ دور ہے، اس لیے جواب −5 ہے۔")},
   number_question(
     "s7_same_signs",
     T(f"Work out {plus(-5, -3)}", f"حل کریں: {plus(-5, -3)}"),
     -8,
     T("Same signs: add 5 and 3, keep the minus.", "ایک جیسی علامتیں: 5 اور 3 جمع کریں، منفی رکھیں۔"),
     T("Right! −5 + (−3) = −8.", "درست! −5 + (−3) = −8"),
     T("Both negative: 5 + 3 = 8, keep the minus: −8.", "دونوں منفی: 5 + 3 = 8، منفی رکھیں: −8"),
     common_wrong=[wrong(8, "Both numbers are negative, so the answer is negative: −8.", "دونوں اعداد منفی ہیں، اس لیے جواب منفی ہے: −8", "wrong_sign"),
                   wrong(-2, "That is −5 + 3. You are adding −3, so go further left: −8.", "یہ −5 + 3 ہے۔ آپ −3 جمع کر رہے ہیں، اس لیے مزید بائیں جائیں: −8", "negative_moves_right")]),
   number_question(
     "s8_different_signs",
     T(f"Work out {plus(-9, 4)}", f"حل کریں: {plus(-9, 4)}"),
     -5,
     T("Different signs: 9 − 4, and −9 is further from 0.", "مختلف علامتیں: 9 − 4، اور −9 صفر سے زیادہ دور ہے۔"),
     T("Right! −9 + 4 = −5.", "درست! −9 + 4 = −5"),
     T("9 − 4 = 5. −9 is further from 0, so the answer is negative: −5.", "9 − 4 = 5۔ −9 صفر سے زیادہ دور ہے، اس لیے جواب منفی ہے: −5"),
     common_wrong=[wrong(5, "The size is right, but −9 is further from 0, so the answer is negative: −5.", "مقدار درست ہے، مگر −9 صفر سے زیادہ دور ہے، اس لیے جواب منفی ہے: −5", "wrong_sign"),
                   wrong(-13, "The signs are different, so subtract, don't add: 9 − 4 = 5.", "علامتیں مختلف ہیں، اس لیے جمع نہیں تفریق کریں: 9 − 4 = 5", "add_digits_keep_minus")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Sara wrote −7 + 3 = −10. What went wrong?", "سارہ نے لکھا −7 + 3 = −10۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("subtract", "The signs are different, so she should subtract: 7 − 3 = 4, giving −4.", "علامتیں مختلف ہیں، اس لیے تفریق کرنی تھی: 7 − 3 = 4، یعنی −4", True,
          "Yes! From −7, moving 3 to the right gives −4.", "جی ہاں! −7 سے 3 دائیں جانے پر −4 آتا ہے۔"),
      opt("sign", "The answer should be 10.", "جواب 10 ہونا چاہیے۔", False,
          "Adding 3 moves right only 3 steps from −7. You don't reach 10.", "3 جمع کرنے سے −7 سے صرف 3 قدم دائیں جاتے ہیں۔ آپ 10 تک نہیں پہنچتے۔", "wrong_sign"),
      opt("nothing", "Nothing. 7 + 3 = 10.", "کوئی غلطی نہیں۔ 7 + 3 = 10", False,
          "Adding +3 to −7 moves right, towards 0, so the answer is closer to 0: −4.", "−7 میں 3 جمع کرنے سے دائیں، 0 کی طرف جاتے ہیں، اس لیے جواب 0 کے زیادہ قریب ہے: −4", "add_digits_keep_minus"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "I worked out −4 + 4 and got 0. Can you tell me why?", "میں نے −4 + 4 حل کیا اور 0 آیا۔ کیا آپ بتا سکتے ہیں کیوں؟"),
    "task": T("In your own words: why is −4 + 4 equal to 0? You can use the number line or money.",
              "اپنے الفاظ میں بتائیں: −4 + 4 کا جواب 0 کیوں ہے؟ آپ عددی خط یا پیسوں کی مثال دے سکتے ہیں۔"),
    "key_idea": "Start at −4 and move 4 to the right and you land on 0; −4 and 4 are opposites, so they cancel. Owing Rs 4 and then getting Rs 4 leaves nothing.",
    "levels": {
      "got_it": "Explains that moving 4 right from −4 reaches 0, or that −4 and 4 are opposites and cancel, or uses owing and paying back the same amount.",
      "partly": "Says they cancel or are opposites but gives no reason, or describes the number line without reaching 0.",
      "not_yet": "Gives a different answer, no reason, or wrong reasoning."},
    "keywords": [
      ["opposite", "cancel", "مخالف", "ختم", "khatam", "mukhalif", "barabar", "برابر"],
      ["right", "steps", "number line", "دائیں", "قدم", "عددی خط", "daen", "qadam"],
      ["owe", "pay", "ادھار", "واپس", "udhar", "wapas"]],
    "fallback_feedback": {
      "got_it": T("Well explained! −4 and 4 are opposites: from −4, 4 steps right lands on 0.",
                  "بہت خوب سمجھایا! −4 اور 4 مخالف ہیں: −4 سے 4 قدم دائیں 0 پر پہنچتے ہیں۔"),
      "partly": T("Good start! Now say where you land if you start at −4 and move 4 to the right.", "اچھی شروعات! اب بتائیں کہ −4 سے شروع کر کے 4 دائیں جائیں تو کہاں پہنچتے ہیں۔"),
      "not_yet": T("Think: you owe your friend Rs 4, then you pay Rs 4 back. How much do you owe now?",
                   "سوچیں: آپ پر دوست کے 4 روپے ادھار ہیں، پھر آپ 4 روپے واپس کر دیتے ہیں۔ اب کتنا ادھار ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_money",
     T("Hamza has Rs 6 (that is +6). He buys a pen for Rs 8 on credit from the shop (that is −8). Work out 6 + (−8) to find where he stands.",
       "حمزہ کے پاس 6 روپے ہیں (یعنی +6)۔ وہ دکان سے 8 روپے کا قلم ادھار لیتا ہے (یعنی −8)۔ اس کا حساب جاننے کے لیے 6 + (−8) حل کریں۔"),
     -2,
     T("He pays Rs 6 and still owes the rest. Owing is negative.", "وہ 6 روپے دیتا ہے اور باقی ادھار رہتا ہے۔ ادھار منفی ہے۔"),
     T("Right! 6 + (−8) = −2: he still owes Rs 2.", "درست! 6 + (−8) = −2: اس پر ابھی 2 روپے ادھار ہیں۔"),
     T("8 − 6 = 2, and −8 is further from 0, so −2. He owes Rs 2.", "8 − 6 = 2، اور −8 صفر سے زیادہ دور ہے، اس لیے −2۔ اس پر 2 روپے ادھار ہیں۔"),
     common_wrong=[wrong(2, "He can't pay all of it, so he still owes: the answer is negative, −2.", "وہ پورا نہیں دے سکتا، اس لیے ادھار باقی ہے: جواب منفی ہے، −2", "wrong_sign"),
                   wrong(14, "The pen is −8, so it moves left: 6 − 8.", "قلم −8 ہے، اس لیے بائیں جاتا ہے: 6 − 8", "negative_moves_right")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "You can add any integers now!", "اب آپ کوئی بھی صحیح اعداد جمع کر سکتے ہیں!"),
    "text": T("Adding a positive number: move right. Adding a negative number: move left. Same signs: add and keep the sign. Different signs: subtract, and take the sign of the number further from 0. A number plus its opposite is 0.",
              "مثبت عدد جمع کرنا: دائیں جائیں۔ منفی عدد جمع کرنا: بائیں جائیں۔ ایک جیسی علامتیں: جمع کریں اور علامت رکھیں۔ مختلف علامتیں: تفریق کریں، اور اس عدد کی علامت لیں جو 0 سے زیادہ دور ہو۔ کسی عدد اور اس کے مخالف کا مجموعہ 0 ہے۔"),
    "points": [T("−5 + (−3) = −8", "−5 + (−3) = −8"), T("−9 + 4 = −5", "−9 + 4 = −5"), T("−4 + 4 = 0", "−4 + 4 = 0")]},
 ],
 "review_questions": [
   {"id": "r_mixed", "type": "apply", "skill": SKILL, "step": number_question(
     "r_mixed",
     T(f"Work out {plus(-2, 7)}", f"حل کریں: {plus(-2, 7)}"),
     5,
     T("Different signs: 7 − 2, and 7 is further from 0.", "مختلف علامتیں: 7 − 2، اور 7 صفر سے زیادہ دور ہے۔"),
     T("Right! −2 + 7 = 5.", "درست! −2 + 7 = 5"),
     T("From −2, move 7 to the right: 5.", "−2 سے 7 دائیں جائیں: 5"),
     common_wrong=[wrong(-5, "7 is further from 0 and positive, so the answer is positive: 5.", "7 صفر سے زیادہ دور اور مثبت ہے، اس لیے جواب مثبت ہے: 5", "wrong_sign"),
                   wrong(-9, "The signs are different, so subtract: 7 − 2 = 5.", "علامتیں مختلف ہیں، اس لیے تفریق کریں: 7 − 2 = 5", "add_digits_keep_minus")],
     qtype=None)},
   {"id": "r_zero", "type": "recall", "skill": SKILL, "step": number_question(
     "r_zero",
     T(f"Work out {plus(-8, 8)}", f"حل کریں: {plus(-8, 8)}"),
     0,
     T("−8 and 8 are opposites.", "−8 اور 8 مخالف ہیں۔"),
     T("Right! A number plus its opposite is 0.", "درست! کسی عدد اور اس کے مخالف کا مجموعہ 0 ہے۔"),
     T("From −8, move 8 to the right: you land on 0.", "−8 سے 8 دائیں جائیں: آپ 0 پر پہنچتے ہیں۔"),
     common_wrong=[wrong(-16, "The signs are different, so they cancel: 0.", "علامتیں مختلف ہیں، اس لیے ختم ہو جاتے ہیں: 0", "add_digits_keep_minus"),
                   wrong(16, "−8 and 8 are opposites, so they cancel: 0.", "−8 اور 8 مخالف ہیں، اس لیے ختم ہو جاتے ہیں: 0")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Integers unit. No textbook text or exercises were used.",
   "A negative number after + is written in brackets: −5 + (−3). Check this matches the Punjab textbook's style.",
   "Urdu terms to check: مجموعہ (sum), صفر جوڑا (zero pair).",
   "The number-line steps start the marker on the first number, so the child only shows the move.",
   "The numbers were worked out in content/sources/g6-maths-04/adding_integers.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
attach(lesson, {
    "s1_hook": FIG_S1, "s3_see_it": FIG_S3, "s6_rules": FIG_S6, "s9_find_error": FIG_S9,
    "s10_explain_why": FIG_S10, "s11_money": FIG_S11, "s12_summary": FIG_S12,
    "qb_find_error": FIG_QB_ERROR,
})
write(lesson)
