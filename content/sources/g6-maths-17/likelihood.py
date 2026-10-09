from fractions import Fraction as F

from common import (T, opt, say, wrong, probability_question, write, balls, P,
                    word, scale_question, DICE, COIN, BOOK, REVIEW, PR_SINGLE_EVENT, PR_LIKELIHOOD)

SKILL = PR_LIKELIHOOD


SPINNER = ["red", "red", "red", "yellow"]  # 4 equal parts
FEW_RED = balls(blue=9, red=1)

# s2: P(head)
S2 = P(lambda o: o == "H", COIN)
assert S2 == F(1, 2)
# s4: a number less than 7 on a dice
assert word(P(lambda o: o < 7, DICE)) == "certain"
# s5: red from 9 blue and 1 red
assert word(P(lambda o: o == "red", FEW_RED)) == "unlikely"
# s6: heads
assert word(S2) == "even_chance"
# s7: P(red) on the spinner (red to yellow: 3/1)
S7 = P(lambda o: o == "red", SPINNER)
assert S7 == F(3, 4) and word(S7) == "likely"
# s8: only the fair coin has equally likely outcomes
assert P(lambda o: o == "H", COIN) == P(lambda o: o == "T", COIN)
assert P(lambda o: o == "red", SPINNER) != P(lambda o: o == "yellow", SPINNER)
assert P(lambda o: o == "red", FEW_RED) != P(lambda o: o == "blue", FEW_RED)
# s9: two colours, but red 1/10 and blue 9/10
assert P(lambda o: o == "blue", FEW_RED) == F(9, 10)
# s11: 2 red and 8 blue, P(blue) (blue to red: 8/2)
S11 = P(lambda o: o == "blue", balls(red=2, blue=8))
assert S11 == F(4, 5) and word(S11) == "likely"
# question bank: P(yellow) on the spinner (yellow to red: 1/3)
QB = P(lambda o: o == "yellow", SPINNER)
assert QB == F(1, 4) and word(QB) == "unlikely"
# review: 9/10 is likely; P(odd) on a dice
assert word(F(9, 10)) == "likely"
R2 = P(lambda o: o % 2 == 1, DICE)
assert R2 == F(1, 2)

lesson = {
 "id": "g6-maths-17-likelihood",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Differentiate outcomes that are equally likely and not equally likely to occur; place events on the probability scale from 0 to 1.", "textbook": f"{BOOK}, 12.3 Probability of Single Event"}],
 "skills": [SKILL],
 "title": T("Likely, unlikely and equally likely", "زیادہ امکان، کم امکان اور یکساں امکان"),
 "estimated_minutes": 13,
 "prerequisites": [{"skill": PR_SINGLE_EVENT}],
 "misconceptions": [
   {"id": "two_kinds_equal", "description": "Thinks two kinds of outcome (red or blue) always means a 50-50 chance."},
   {"id": "more_than_one", "description": "Gives a probability bigger than 1."},
   {"id": "possible_is_likely", "description": "Thinks anything that can happen is likely."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_zero", "type": "recall", "step": scale_question(
     "qb_zero",
     T("An event has probability 0. It is …", "ایک واقعے کا احتمال 0 ہے۔ یہ ہے …"),
     "impossible",
     ("Yes! 0 means it can never happen.", "جی ہاں! 0 کا مطلب ہے یہ کبھی نہیں ہو سکتا۔"),
     "0 is the very bottom of the scale: impossible.", "0 پیمانے کا سب سے نیچے ہے: ناممکن۔", qtype=None)},
   {"id": "qb_apply", "type": "apply", "step": probability_question(
     "qb_apply",
     T("A spinner has 4 equal parts: 3 red and 1 yellow. What is P(yellow)?", "ایک اسپنر کے 4 برابر حصے ہیں: 3 سرخ اور 1 پیلا۔ P(پیلا) کیا ہے؟"),
     QB,
     T("1 yellow part out of 4 parts.", "4 حصوں میں سے 1 پیلا۔"),
     T("Right! 1/4, so yellow is unlikely.", "درست! 1/4، تو پیلا کم امکان ہے۔"),
     T("1 part out of 4: P(yellow) = 1/4.", "4 میں سے 1 حصہ: P(پیلا) = 1/4"),
     common_wrong=[wrong("1/3", "3 is the red parts. Divide by all 4 parts: 1/4.", "3 سرخ حصے ہیں۔ تمام 4 حصوں سے تقسیم کریں: 1/4"),
                   wrong("1/2", "Two colours, but not equal parts: 1 of 4 is yellow.", "دو رنگ ہیں، مگر حصے برابر نہیں: 4 میں سے 1 پیلا۔", "two_kinds_equal")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Sana says the probability that it rains tomorrow is 2, so it is very likely. What is wrong?", "ثنا کہتی ہے کہ کل بارش کا احتمال 2 ہے، تو بہت زیادہ امکان ہے۔ کیا غلطی ہے؟"),
     "options": [
       opt("max_one", "A probability can't be more than 1.", "احتمال 1 سے زیادہ نہیں ہو سکتا۔", True,
           "Yes! 1 already means certain.", "جی ہاں! 1 کا مطلب ہی یقینی ہے۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "The scale stops at 1 (certain). 2 is not a probability.", "پیمانہ 1 (یقینی) پر ختم ہوتا ہے۔ 2 احتمال نہیں۔", "more_than_one"),
       opt("unlikely", "2 means unlikely.", "2 کا مطلب کم امکان ہے۔", False,
           "No probability is 2. They go from 0 to 1.", "کوئی احتمال 2 نہیں ہوتا۔ یہ 0 سے 1 تک ہوتے ہیں۔", "more_than_one"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_scale", "front": T("The probability scale?", "احتمال کا پیمانہ؟"),
    "back": T("0 impossible, under 1/2 unlikely, 1/2 even chance, over 1/2 likely, 1 certain.", "0 ناممکن، 1/2 سے کم کم امکان، 1/2 برابر امکان، 1/2 سے زیادہ زیادہ امکان، 1 یقینی۔")},
   {"id": "f_equally", "front": T("Equally likely?", "یکساں امکان؟"),
    "back": T("Outcomes with the same probability, like H and T on a fair coin.", "ایک جتنے احتمال والے نتائج، جیسے منصفانہ سکے پر H اور T۔")},
 ],
 "home_tasks": [{"id": "h_scale", "text": T(
   "Draw a line and mark 0, 1/2 and 1. Put three things from your day on it: 'the sun sets today', 'I find a lion at home', 'it rains tomorrow'.",
   "ایک لکیر کھینچیں اور 0، 1/2 اور 1 لکھیں۔ اپنے دن کی تین باتیں اس پر رکھیں: 'آج سورج غروب ہوگا'، 'گھر میں شیر ملے گا'، 'کل بارش ہوگی'۔")}],
 "glossary": [T("Impossible", "ناممکن"), T("Unlikely", "کم امکان"), T("Even chance", "برابر امکان"), T("Likely", "زیادہ امکان"), T("Certain", "یقینی"), T("Equally likely", "یکساں امکان")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Will the sun rise tomorrow? Will it snow in Multan in June? Some things are surer than others!",
                     "کیا کل سورج نکلے گا؟ کیا جون میں ملتان میں برف پڑے گی؟ کچھ باتیں دوسری باتوں سے زیادہ یقینی ہیں!"),
    "text": T("Today we put chances in order, from impossible to certain, and learn when outcomes are equally likely. First, one probability to warm up.", "آج ہم امکانات کو ترتیب دیں گے، ناممکن سے یقینی تک، اور سیکھیں گے کہ نتائج کب یکساں ممکن ہوتے ہیں۔ پہلے ایک احتمال۔")},
   probability_question(
     "s2_foundation",
     T("A fair coin is tossed. What is P(head)?", "ایک منصفانہ سکہ اچھالا جاتا ہے۔ P(ہیڈ) کیا ہے؟"),
     S2,
     T("H is one outcome out of H and T.", "H اور T میں سے H ایک نتیجہ ہے۔"),
     T("Right! 1/2.", "درست! 1/2"),
     T("One outcome (H) out of two (H, T): 1/2.", "دو (H، T) میں سے ایک نتیجہ (H): 1/2"),
     common_wrong=[wrong("2", "Wanted outcomes on top: 1 out of 2 is 1/2.", "مطلوبہ نتائج اوپر: 2 میں سے 1 یعنی 1/2")],
     qtype="recall", skill=PR_SINGLE_EVENT),
   {"id": "s3_scale", "type": "explain",
    "character": say("happy", "Zero means never, one means always. Everything else sits in between!", "صفر یعنی کبھی نہیں، ایک یعنی ہمیشہ۔ باقی سب درمیان میں!"),
    "text": T("Every probability is on a scale from 0 to 1. 0 is impossible. Less than 1/2 is unlikely. Exactly 1/2 is an even chance. More than 1/2 is likely. 1 is certain. Outcomes are equally likely when they have the same probability, like H and T on a fair coin, or the six faces of a fair dice.",
              "ہر احتمال 0 سے 1 کے پیمانے پر ہوتا ہے۔ 0 ناممکن ہے۔ 1/2 سے کم، کم امکان ہے۔ ٹھیک 1/2 برابر امکان ہے۔ 1/2 سے زیادہ، زیادہ امکان ہے۔ 1 یقینی ہے۔ نتائج یکساں ممکن تب ہوتے ہیں جب ان کا احتمال ایک جتنا ہو، جیسے منصفانہ سکے پر H اور T، یا منصفانہ ڈائس کے چھ رُخ۔")},
   scale_question(
     "s4_certain",
     T("You roll a dice. How likely is a number less than 7?", "آپ ڈائس پھینکتے ہیں۔ 7 سے چھوٹا عدد آنے کا کتنا امکان ہے؟"),
     "certain",
     ("Yes! Every face is less than 7: P = 6/6 = 1.", "جی ہاں! ہر رُخ 7 سے چھوٹا ہے: P = 6/6 = 1"),
     "Every face (1 to 6) is less than 7, so P = 6/6 = 1: certain.", "ہر رُخ (1 سے 6) 7 سے چھوٹا ہے، تو P = 6/6 = 1: یقینی۔"),
   scale_question(
     "s5_unlikely",
     T("A bag has 9 blue balls and 1 red ball. How likely is it to pick red?", "ایک تھیلے میں 9 نیلی اور 1 سرخ گیند ہے۔ سرخ نکلنے کا کتنا امکان ہے؟"),
     "unlikely",
     ("Yes! P(red) = 1/10, less than 1/2.", "جی ہاں! P(سرخ) = 1/10، جو 1/2 سے کم ہے۔"),
     "Red can happen, but P(red) = 1/10, less than 1/2: unlikely.", "سرخ نکل سکتی ہے، مگر P(سرخ) = 1/10، جو 1/2 سے کم ہے: کم امکان۔",
     mis="possible_is_likely"),
   scale_question(
     "s6_even",
     T("You toss a fair coin. How likely is heads?", "آپ منصفانہ سکہ اچھالتے ہیں۔ ہیڈ آنے کا کتنا امکان ہے؟"),
     "even_chance",
     ("Yes! P(head) = 1/2: an even chance.", "جی ہاں! P(ہیڈ) = 1/2: برابر امکان۔"),
     "P(head) = 1/2, exactly the middle: an even chance.", "P(ہیڈ) = 1/2، بالکل درمیان: برابر امکان۔"),
   probability_question(
     "s7_spinner",
     T("A spinner has 4 equal parts: 3 red and 1 yellow. What is P(red)?", "ایک اسپنر کے 4 برابر حصے ہیں: 3 سرخ اور 1 پیلا۔ P(سرخ) کیا ہے؟"),
     S7,
     T("3 red parts out of 4 parts.", "4 حصوں میں سے 3 سرخ۔"),
     T("Right! 3/4: more than 1/2, so red is likely.", "درست! 3/4: 1/2 سے زیادہ، تو سرخ زیادہ امکان ہے۔"),
     T("3 parts out of 4: P(red) = 3/4.", "4 میں سے 3 حصے: P(سرخ) = 3/4"),
     common_wrong=[wrong("3/1", "1 is the yellow part. Divide by all 4 parts: 3/4.", "1 پیلا حصہ ہے۔ تمام 4 حصوں سے تقسیم کریں: 3/4", "more_than_one"),
                   wrong("1/2", "Two colours, but not equal parts: 3 of 4 are red.", "دو رنگ ہیں، مگر حصے برابر نہیں: 4 میں سے 3 سرخ۔", "two_kinds_equal")]),
   {"id": "s8_equally", "type": "choice",
    "prompt": T("Which of these has equally likely outcomes?", "ان میں سے کس کے نتائج یکساں ممکن ہیں؟"),
    "options": [
      opt("coin", "Tossing a fair coin: H or T", "منصفانہ سکہ اچھالنا: H یا T", True,
          "Yes! P(H) = P(T) = 1/2.", "جی ہاں! P(H) = P(T) = 1/2"),
      opt("spinner", "The spinner: red or yellow", "اسپنر: سرخ یا پیلا", False,
          "Red has 3 parts and yellow 1: 3/4 and 1/4 are not equal.", "سرخ کے 3 حصے اور پیلے کا 1: 3/4 اور 1/4 برابر نہیں۔", "two_kinds_equal"),
      opt("bag", "9 blue and 1 red ball: blue or red", "9 نیلی اور 1 سرخ گیند: نیلی یا سرخ", False,
          "Blue is 9/10 and red is 1/10: not equal.", "نیلی 9/10 اور سرخ 1/10: برابر نہیں۔", "two_kinds_equal"),
    ]},
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Hamza says: 'A bag has 9 blue balls and 1 red ball. There are two colours, so red and blue are equally likely.' What is wrong?", "حمزہ کہتا ہے: 'تھیلے میں 9 نیلی اور 1 سرخ گیند ہے۔ رنگ دو ہیں، تو سرخ اور نیلی یکساں ممکن ہیں۔' کیا غلطی ہے؟"),
    "options": [
      opt("count_balls", "Count the balls, not the colours: P(blue) = 9/10, P(red) = 1/10.", "رنگ نہیں، گیندیں گنیں: P(نیلی) = 9/10، P(سرخ) = 1/10", True,
          "Yes! Blue is much more likely.", "جی ہاں! نیلی کا امکان کہیں زیادہ ہے۔"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "Two colours doesn't mean 50-50. 9 of the 10 balls are blue.", "دو رنگ کا مطلب آدھا آدھا نہیں۔ 10 میں سے 9 گیندیں نیلی ہیں۔", "two_kinds_equal"),
      opt("red_likely", "Red is more likely because it is special.", "سرخ کا امکان زیادہ ہے کیونکہ وہ خاص ہے۔", False,
          "Only 1 ball is red: P(red) = 1/10, unlikely.", "صرف 1 گیند سرخ ہے: P(سرخ) = 1/10، کم امکان۔"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "A 6 can come up, so isn't it likely? Help me understand!",
                     "6 آ تو سکتا ہے، تو کیا یہ زیادہ امکان نہیں؟ مجھے سمجھائیں!"),
    "task": T("Explain why rolling a 6 on a fair dice is unlikely, but rolling a number less than 7 is certain.", "بتائیں کہ منصفانہ ڈائس پر 6 آنا کم امکان کیوں ہے، مگر 7 سے چھوٹا عدد آنا یقینی کیوں ہے۔"),
    "key_idea": "Only one face of six shows 6, so P(6) = 1/6, which is less than 1/2: unlikely. Every face is less than 7, so P = 6/6 = 1: certain.",
    "levels": {
      "got_it": "Says P(6) = 1/6 (one face of six), less than 1/2 so unlikely, and that all six faces are less than 7 so P = 1, certain.",
      "partly": "Explains one of the two, or names the words without the probabilities.",
      "not_yet": "Gives no reason."},
    "keywords": [
      ["1/6", "one out of six", "چھ میں سے ایک"],
      ["1/2", "half", "آدھا"],
      ["every", "all", "سب", "ہر"],
      ["1", "6/6", "one"]],
    "fallback_feedback": {
      "got_it": T("Well explained! 1/6 is low; 6/6 is certain.", "بہت خوب! 1/6 کم ہے؛ 6/6 یقینی ہے۔"),
      "partly": T("Good start! Now give the probability of each one.", "اچھی شروعات! اب ہر ایک کا احتمال بتائیں۔"),
      "not_yet": T("How many faces show 6? How many faces are less than 7?", "کتنے رُخ پر 6 ہے؟ کتنے رُخ 7 سے چھوٹے ہیں؟")},
    "limit_per_day": 3, "max_attempts": 2},
   probability_question(
     "s11_blue",
     T("A bag has 2 red and 8 blue balls. What is P(blue)?", "ایک تھیلے میں 2 سرخ اور 8 نیلی گیندیں ہیں۔ P(نیلی) کیا ہے؟"),
     S11,
     T("8 blue out of all the balls.", "تمام گیندوں میں سے 8 نیلی۔"),
     T("Right! 8/10 = 4/5: likely.", "درست! 8/10 = 4/5: زیادہ امکان۔"),
     T("8 blue out of 10 balls: 8/10 = 4/5.", "10 گیندوں میں سے 8 نیلی: 8/10 = 4/5"),
     common_wrong=[wrong("8/2", "A probability is never more than 1. Divide by all 10 balls: 8/10.", "احتمال کبھی 1 سے زیادہ نہیں ہوتا۔ تمام 10 گیندوں سے تقسیم کریں: 8/10", "more_than_one")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "From impossible to certain, you can place any event on the scale now!", "ناممکن سے یقینی تک، اب آپ کسی بھی واقعے کو پیمانے پر رکھ سکتے ہیں!"),
    "text": T("Probabilities go from 0 (impossible) to 1 (certain). Under 1/2 is unlikely, 1/2 is an even chance, over 1/2 is likely. Outcomes are equally likely only when their probabilities are the same; two colours in a bag don't make a 50-50 chance.",
              "احتمال 0 (ناممکن) سے 1 (یقینی) تک ہوتے ہیں۔ 1/2 سے کم، کم امکان؛ 1/2 برابر امکان؛ 1/2 سے زیادہ، زیادہ امکان۔ نتائج تب ہی یکساں ممکن ہیں جب ان کے احتمال ایک جتنے ہوں؛ تھیلے میں دو رنگ ہونے سے آدھا آدھا امکان نہیں بنتا۔"),
    "points": [T("0 impossible, 1/2 even chance, 1 certain.", "0 ناممکن، 1/2 برابر امکان، 1 یقینی۔"),
               T("Equally likely = same probability.", "یکساں امکان = ایک جتنا احتمال")]},
 ],
 "review_questions": [
   {"id": "r_word", "type": "apply", "skill": SKILL, "step": scale_question(
     "r_word",
     T("An event has probability 9/10. It is …", "ایک واقعے کا احتمال 9/10 ہے۔ یہ ہے …"),
     "likely",
     ("Yes! 9/10 is more than 1/2 but less than 1.", "جی ہاں! 9/10، 1/2 سے زیادہ مگر 1 سے کم ہے۔"),
     "9/10 is more than 1/2 and less than 1: likely.", "9/10، 1/2 سے زیادہ اور 1 سے کم ہے: زیادہ امکان۔", qtype=None)},
   {"id": "r_odd", "type": "apply", "skill": SKILL, "step": probability_question(
     "r_odd",
     T("You roll a dice. What is the probability of an odd number?", "آپ ڈائس پھینکتے ہیں۔ طاق عدد آنے کا احتمال کیا ہے؟"),
     R2,
     T("The odd faces are 1, 3 and 5.", "طاق رُخ 1، 3 اور 5 ہیں۔"),
     T("Right! 3/6 = 1/2: an even chance.", "درست! 3/6 = 1/2: برابر امکان۔"),
     T("E = {1, 3, 5}, so P = 3/6 = 1/2.", "E = {1, 3, 5}، تو P = 3/6 = 1/2"),
     common_wrong=[wrong("3", "3 is how many odd numbers. Divide by 6: 3/6.", "3 طاق اعداد کی تعداد ہے۔ 6 سے تقسیم کریں: 3/6")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Probability unit (PCTB Mathematics 6, Sub-domain 12). No textbook text or exercises were used.",
   "The five scale words (impossible, unlikely, even chance, likely, certain) follow the book's probability scale.",
   "Urdu terms to check: ناممکن، کم امکان، برابر امکان، زیادہ امکان، یقینی، یکساں امکان (equally likely)، طاق عدد (odd number).",
   "The numbers were worked out in content/sources/g6-maths-17/likelihood.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}

# ---------- pictures ----------
from figs import attach, step_says, coins_row, dice_faces, bag, key, spinner, likelihood_line

TWO_EIGHT = balls(red=2, blue=8)
step_says(lesson, "s5_unlikely", "9 blue balls and 1 red ball")
step_says(lesson, "s9_find_error", "9 blue balls and 1 red ball")
step_says(lesson, "s11_blue", "2 red and 8 blue balls")
step_says(lesson, "s7_spinner", "4 equal parts: 3 red and 1 yellow")
step_says(lesson, "qb_apply", "4 equal parts: 3 red and 1 yellow")
SPIN_TEXT = ["R" if c == "red" else "Y" for c in SPINNER]
SPIN_SHADE = [i for i, c in enumerate(SPINNER) if c == "red"]
n_red, n_yellow = SPINNER.count("red"), SPINNER.count("yellow")
SPIN_EN = f"{n_red} marked R (red) and shaded, {n_yellow} marked Y (yellow)"
SPIN_UR = f"{n_red} پر R (سرخ) لکھا ہے اور وہ رنگین ہیں، {n_yellow} پر Y (پیلا)"
LINE_EN = ("A line from 0 to 1. The 0 end is impossible and the 1 end is certain. "
           "A taller tick in the middle is an even chance (one half); the left half is unlikely and the right half likely.")
LINE_UR = ("0 سے 1 تک ایک لکیر۔ 0 والا سرا ناممکن اور 1 والا سرا یقینی ہے۔ "
           "درمیان میں لمبا نشان برابر امکان (آدھا) ہے؛ بایاں آدھا حصہ کم امکان اور دایاں آدھا زیادہ امکان۔")
SUMMARY_MARKS = [(F(0), "A"), (F(1, 2), "B"), (F(1), "C")]
assert [word(v) for v, _ in SUMMARY_MARKS] == ["impossible", "even_chance", "certain"]

attach(lesson, {
    "s2_foundation": coins_row(COIN, "The two faces of a fair coin: H (heads) and T (tails).",
                               "ایک منصفانہ سکے کے دو رخ: H (ہیڈ) اور T (ٹیل)۔"),
    "s3_scale": likelihood_line(LINE_EN, LINE_UR),
    "s4_certain": dice_faces(DICE),
    "s5_unlikely": bag(FEW_RED, key("red", "blue")),
    "s6_even": coins_row(COIN, "The two faces of a fair coin: H (heads) and T (tails).",
                         "ایک منصفانہ سکے کے دو رخ: H (ہیڈ) اور T (ٹیل)۔"),
    "s7_spinner": spinner(SPIN_TEXT, shade=SPIN_SHADE, what_en=SPIN_EN, what_ur=SPIN_UR),
    "s9_find_error": bag(FEW_RED, key("red", "blue")),
    "s11_blue": bag(TWO_EIGHT, key("blue", "red")),
    "s12_summary": likelihood_line(
        LINE_EN + " Three dots on the line: A at 0 (impossible), B in the middle (even chance) and C at 1 (certain).",
        LINE_UR + " لکیر پر تین نقطے: A، 0 پر (ناممکن)، B درمیان میں (برابر امکان) اور C، 1 پر (یقینی)۔",
        marks=SUMMARY_MARKS),
    "qb_apply": spinner(SPIN_TEXT, shade=SPIN_SHADE, what_en=SPIN_EN, what_ur=SPIN_UR),
    "r_odd": dice_faces(DICE),
})
write(lesson)
