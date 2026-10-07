from fractions import Fraction as F

from common import (T, opt, say, wrong, number_question, probability_question,
                    write, frac, coins, balls, P, DICE, VOWELS, BOOK, REVIEW,
                    PR_SAMPLE_SPACE, PR_SINGLE_EVENT)

SKILL = PR_SINGLE_EVENT
BAG = balls(red=3, blue=2, green=5)

# s2: two coins, n(S)
S2 = len(coins(2))
assert S2 == 4
# s4: P(6) on a dice (upside down: 6/1)
S4 = P(lambda o: o == 6, DICE)
assert S4 == F(1, 6)
# s5: P(even) on a dice = 3/6 (forgetting to divide by n(S) gives 3)
S5 = P(lambda o: o % 2 == 0, DICE)
assert S5 == F(3, 6) == F(1, 2)
# s6: P(red) from the bag (red to the rest: 3/7; one of three colours: 1/3)
S6 = P(lambda o: o == "red", BAG)
assert S6 == F(3, 10) and len([b for b in BAG if b != "red"]) == 7
# s7: P(green) from the bag
S7 = P(lambda o: o == "green", BAG)
assert S7 == F(1, 2)
# s8: MULTAN cards, P(vowel) (vowels to consonants: 2/4)
S8 = P(lambda o: o in VOWELS, "MULTAN")
assert S8 == F(2, 6) == F(1, 3)
# s9: P(7) on a dice is 0 (no outcome), not 1/7
assert P(lambda o: o == 7, DICE) == 0
# s11: spinner 1 to 8, P(greater than 5) (to the rest: 3/5; 5 or less: 5/8)
S11 = P(lambda o: o > 5, range(1, 9))
assert S11 == F(3, 8)
# question bank: P(less than 3) on a dice (with 3: 3/6)
QB = P(lambda o: o < 3, DICE)
assert QB == F(1, 3) and P(lambda o: o <= 3, DICE) == F(1, 2)
# question bank find_error: 4 red and 6 blue, P(red) = 4/10, not 4/6
assert P(lambda o: o == "red", balls(red=4, blue=6)) == F(2, 5)
# review: P(prime) on a dice (counting 1 as prime: 4/6); P(blue) with 4 red, 6 blue
R1 = P(lambda o: o in (2, 3, 5), DICE)
assert R1 == F(1, 2)
R2 = P(lambda o: o == "blue", balls(red=4, blue=6))
assert R2 == F(3, 5)


def W(answer: str, en, ur, mis=None):
    """A wrong answer written the way a child types it (2/4 stays 2/4)."""
    return wrong(answer, en, ur, mis)


lesson = {
 "id": "g6-maths-17-probability-of-an-event",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Find the probability of a single event.", "textbook": f"{BOOK}, 12.3 Probability of Single Event"}],
 "skills": [SKILL],
 "title": T("Probability of an event", "کسی واقعے کا احتمال"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": PR_SAMPLE_SPACE}],
 "misconceptions": [
   {"id": "upside_down", "description": "Writes n(S)/n(E) instead of n(E)/n(S)."},
   {"id": "part_to_part", "description": "Divides by the other outcomes (3 red to 7 others) instead of by all outcomes."},
   {"id": "colours_not_objects", "description": "Uses the number of colours as n(S) instead of the number of balls."},
   {"id": "no_divide", "description": "Gives n(E), the count, instead of the probability n(E)/n(S)."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_rule", "type": "recall", "step": {
     "id": "qb_rule", "type": "choice",
     "prompt": T("The probability of an event E is …", "واقعہ E کا احتمال ہے …"),
     "options": [
       opt("e_over_s", "P(E) = n(E) ÷ n(S)", "P(E) = n(E) ÷ n(S)", True,
           "Yes! The outcomes we want, out of all the outcomes.", "جی ہاں! مطلوبہ نتائج، تمام نتائج میں سے۔"),
       opt("s_over_e", "P(E) = n(S) ÷ n(E)", "P(E) = n(S) ÷ n(E)", False,
           "That is upside down. Wanted outcomes on top: n(E) ÷ n(S).", "یہ اُلٹا ہے۔ مطلوبہ نتائج اوپر: n(E) ÷ n(S)", "upside_down"),
       opt("minus", "P(E) = n(S) − n(E)", "P(E) = n(S) − n(E)", False,
           "We divide, not subtract: n(E) ÷ n(S).", "ہم تقسیم کرتے ہیں، تفریق نہیں: n(E) ÷ n(S)"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": probability_question(
     "qb_apply",
     T("You roll a dice. What is the probability of a number less than 3?", "آپ ڈائس پھینکتے ہیں۔ 3 سے چھوٹا عدد آنے کا احتمال کیا ہے؟"),
     QB,
     T("Less than 3 means 1 or 2. Out of how many?", "3 سے چھوٹا یعنی 1 یا 2۔ کتنے میں سے؟"),
     T(f"Right! 2/6 = {frac(QB)}.", f"درست! 2/6 = {frac(QB)}"),
     T("E = {1, 2}, so P = 2/6 = 1/3.", "E = {1, 2}، تو P = 2/6 = 1/3"),
     common_wrong=[W("3/6", "3 is not less than 3. E = {1, 2}: P = 2/6.", "3، 3 سے چھوٹا نہیں۔ E = {1, 2}: P = 2/6")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("A bag has 4 red and 6 blue balls. Usman says P(red) = 4/6. What is wrong?", "ایک تھیلے میں 4 سرخ اور 6 نیلی گیندیں ہیں۔ عثمان کہتا ہے P(سرخ) = 4/6۔ کیا غلطی ہے؟"),
     "options": [
       opt("total", "He must divide by all 10 balls: P(red) = 4/10.", "اسے تمام 10 گیندوں سے تقسیم کرنا ہے: P(سرخ) = 4/10", True,
           "Yes! n(S) is every ball: 4 + 6 = 10.", "جی ہاں! n(S) ہر گیند ہے: 4 + 6 = 10"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "6 is only the blue balls. Divide by all 10: 4/10.", "6 صرف نیلی گیندیں ہیں۔ تمام 10 سے تقسیم کریں: 4/10", "part_to_part"),
       opt("flip", "It should be 6/4.", "یہ 6/4 ہونا چاہیے۔", False,
           "A probability is never more than 1. P(red) = 4/10.", "احتمال کبھی 1 سے زیادہ نہیں ہوتا۔ P(سرخ) = 4/10", "upside_down"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_rule", "front": T("P(E) = ?", "P(E) = ؟"),
    "back": T("n(E) ÷ n(S): the outcomes we want out of all the outcomes.", "n(E) ÷ n(S): مطلوبہ نتائج، تمام نتائج میں سے۔")},
   {"id": "f_head", "front": T("P(head) with a fair coin?", "منصفانہ سکے پر P(ہیڈ)؟"),
    "back": T("1/2: one outcome (H) out of two (H, T).", "1/2: دو (H، T) میں سے ایک نتیجہ (H)۔")},
 ],
 "home_tasks": [{"id": "h_bag", "text": T(
   "Put 3 spoons and 1 fork in a cup. Without looking, how likely are you to pull out the fork? Write P(fork) as a fraction, then try it 8 times.",
   "ایک کپ میں 3 چمچ اور 1 کانٹا رکھیں۔ بغیر دیکھے کانٹا نکلنے کا احتمال کیا ہے؟ P(کانٹا) کسر میں لکھیں، پھر 8 بار آزمائیں۔")}],
 "glossary": [T("Probability", "احتمال"), T("Fair coin", "منصفانہ سکہ"), T("Event", "واقعہ"), T("Sample space", "نمونی فضا")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Is the cricket toss fair? What is the chance the captain calls it right? Let's find a number for it!",
                     "کیا کرکٹ کا ٹاس منصفانہ ہے؟ کپتان کے صحیح کہنے کا کتنا امکان ہے؟ آئیں اس کا عدد نکالیں!"),
    "text": T("Today we find the probability of an event: a number that says how likely it is. First, remember the sample space.", "آج ہم کسی واقعے کا احتمال نکالیں گے: ایک عدد جو بتاتا ہے کہ وہ کتنا ممکن ہے۔ پہلے نمونی فضا یاد کریں۔")},
   number_question(
     "s2_foundation",
     T("Two coins are tossed. How many outcomes are in the sample space?", "دو سکے اچھالے جاتے ہیں۔ نمونی فضا میں کتنے نتائج ہیں؟"),
     S2,
     T("HH, HT, …", "HH، HT، …"),
     T("Right! S = {HH, HT, TH, TT}.", "درست! S = {HH, HT, TH, TT}"),
     T("S = {HH, HT, TH, TT}: 4 outcomes.", "S = {HH, HT, TH, TT}: 4 نتائج"),
     common_wrong=[wrong(3, "HT and TH are different outcomes: 4 in all.", "HT اور TH الگ نتائج ہیں: کل 4۔")],
     qtype="recall", skill=PR_SAMPLE_SPACE),
   {"id": "s3_rule", "type": "explain",
    "character": say("happy", "Count what you want, count everything, and divide. That's probability!", "جو چاہیے وہ گنیں، سب کچھ گنیں، اور تقسیم کریں۔ یہی احتمال ہے!"),
    "text": T("When all outcomes are equally likely, the probability of an event E is P(E) = n(E) ÷ n(S): the number of outcomes we want, out of all the outcomes. A fair coin: P(head) = 1/2, because H is one outcome out of two. A probability is never less than 0 or more than 1.",
              "جب تمام نتائج یکساں ممکن ہوں تو واقعہ E کا احتمال P(E) = n(E) ÷ n(S) ہے: مطلوبہ نتائج کی تعداد، تمام نتائج میں سے۔ منصفانہ سکہ: P(ہیڈ) = 1/2، کیونکہ H دو میں سے ایک نتیجہ ہے۔ احتمال کبھی 0 سے کم یا 1 سے زیادہ نہیں ہوتا۔")},
   probability_question(
     "s4_six",
     T("You roll a dice. What is the probability of getting a 6? Type it as a fraction.", "آپ ڈائس پھینکتے ہیں۔ 6 آنے کا احتمال کیا ہے؟ کسر میں لکھیں۔"),
     S4,
     T("How many faces show 6? How many faces are there?", "کتنے رُخ پر 6 ہے؟ کل کتنے رُخ ہیں؟"),
     T("Right! One 6 out of six faces: 1/6.", "درست! چھ رُخ میں سے ایک 6: 1/6"),
     T("n(E) = 1 (just the 6), n(S) = 6. P = 1/6.", "n(E) = 1 (صرف 6)، n(S) = 6۔ P = 1/6"),
     common_wrong=[W("6", "6 is the number on the face. One face out of six: 1/6.", "6 تو رُخ کا عدد ہے۔ چھ میں سے ایک رُخ: 1/6", "upside_down")]),
   probability_question(
     "s5_even",
     T("What is the probability of rolling an even number?", "جفت عدد آنے کا احتمال کیا ہے؟"),
     S5,
     T("E = {2, 4, 6}. Out of how many?", "E = {2, 4, 6}۔ کتنے میں سے؟"),
     T("Right! 3/6, which is the same as 1/2.", "درست! 3/6، جو 1/2 کے برابر ہے۔"),
     T("n(E) = 3 and n(S) = 6, so P = 3/6 = 1/2.", "n(E) = 3 اور n(S) = 6، تو P = 3/6 = 1/2"),
     common_wrong=[W("3", "3 is how many even numbers. Divide by all 6: 3/6 = 1/2.", "3 جفت اعداد کی تعداد ہے۔ تمام 6 سے تقسیم کریں: 3/6 = 1/2", "no_divide")]),
   {"id": "s6_red", "type": "choice",
    "prompt": T("A bag has 3 red, 2 blue and 5 green balls. What is P(red)?", "ایک تھیلے میں 3 سرخ، 2 نیلی اور 5 سبز گیندیں ہیں۔ P(سرخ) کیا ہے؟"),
    "options": [
      opt("three_tenths", "3/10", "3/10", True, "Yes! 3 red balls out of 10 balls.", "جی ہاں! 10 گیندوں میں سے 3 سرخ۔"),
      opt("three_sevenths", "3/7", "3/7", False, "7 is the balls that are not red. Divide by all 10: 3/10.", "7 وہ گیندیں ہیں جو سرخ نہیں۔ تمام 10 سے تقسیم کریں: 3/10", "part_to_part"),
      opt("one_third", "1/3", "1/3", False, "There are 3 colours, but 10 balls, and more green than red. P(red) = 3/10.", "رنگ 3 ہیں، مگر گیندیں 10، اور سبز سرخ سے زیادہ۔ P(سرخ) = 3/10", "colours_not_objects"),
    ]},
   probability_question(
     "s7_green",
     T("Same bag. What is P(green)?", "وہی تھیلا۔ P(سبز) کیا ہے؟"),
     S7,
     T("How many green balls? How many balls in all?", "کتنی سبز گیندیں؟ کل کتنی گیندیں؟"),
     T("Right! 5/10 = 1/2.", "درست! 5/10 = 1/2"),
     T("5 green out of 10 balls: 5/10 = 1/2.", "10 گیندوں میں سے 5 سبز: 5/10 = 1/2"),
     common_wrong=[W("1/3", "Each ball is an outcome, not each colour: 5/10.", "ہر گیند ایک نتیجہ ہے، ہر رنگ نہیں: 5/10", "colours_not_objects"),
                   W("5/5", "5/5 would mean every ball is green. 5 out of 10: 1/2.", "5/5 کا مطلب ہوگا ہر گیند سبز ہے۔ 10 میں سے 5: 1/2")]),
   probability_question(
     "s8_multan",
     T("The letters of MULTAN are on 6 cards. Bilal picks one. What is P(vowel)?", "لفظ MULTAN کے حروف 6 کارڈز پر ہیں۔ بلال ایک نکالتا ہے۔ P(حرفِ علت) کیا ہے؟"),
     S8,
     T("The vowels in MULTAN are U and A.", "MULTAN میں حروفِ علت U اور A ہیں۔"),
     T("Right! 2/6 = 1/3.", "درست! 2/6 = 1/3"),
     T("2 vowel cards out of 6 cards: 2/6 = 1/3.", "6 کارڈز میں سے 2 حرفِ علت: 2/6 = 1/3"),
     common_wrong=[W("2/4", "4 is the other letters. Divide by all 6 cards: 2/6.", "4 باقی حروف ہیں۔ تمام 6 کارڈز سے تقسیم کریں: 2/6", "part_to_part"),
                   W("2", "2 is how many vowels. Divide by 6: 2/6 = 1/3.", "2 حروفِ علت کی تعداد ہے۔ 6 سے تقسیم کریں: 2/6 = 1/3", "no_divide")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Rida says the probability of rolling a 7 on a dice is 1/7. What is wrong?", "ردا کہتی ہے کہ ڈائس پر 7 آنے کا احتمال 1/7 ہے۔ کیا غلطی ہے؟"),
    "options": [
      opt("zero", "No face shows 7, so n(E) = 0 and P = 0/6 = 0.", "کسی رُخ پر 7 نہیں، تو n(E) = 0 اور P = 0/6 = 0", True,
          "Yes! An event that can't happen has probability 0.", "جی ہاں! جو واقعہ ہو ہی نہ سکے اس کا احتمال 0 ہے۔"),
      opt("one_sixth", "It should be 1/6.", "یہ 1/6 ہونا چاہیے۔", False,
          "1/6 is for a number that is on the dice. 7 is not on it: P = 0.", "1/6 اس عدد کے لیے ہے جو ڈائس پر ہو۔ 7 اس پر نہیں: P = 0"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "The dice has 6 faces, not 7, and none shows 7. P = 0.", "ڈائس کے 6 رُخ ہیں، 7 نہیں، اور کسی پر 7 نہیں۔ P = 0"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why is the chance of heads exactly one half? Can you teach me?",
                     "ہیڈ آنے کا امکان ٹھیک آدھا کیوں ہے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("Explain why P(head) = 1/2 when you toss a fair coin. Use n(E) and n(S).", "بتائیں کہ منصفانہ سکہ اچھالنے پر P(ہیڈ) = 1/2 کیوں ہے۔ n(E) اور n(S) استعمال کریں۔"),
    "key_idea": "The sample space is {H, T}, so n(S) = 2. The event 'head' is {H}, so n(E) = 1. Both outcomes are equally likely, so P(head) = n(E) ÷ n(S) = 1/2.",
    "levels": {
      "got_it": "Says there are 2 equally likely outcomes (H and T), 1 of them is a head, so P = 1 ÷ 2 = 1/2.",
      "partly": "Says 'one out of two' without naming the outcomes, or names them without dividing.",
      "not_yet": "Gives no reason."},
    "keywords": [
      ["2", "two", "دو"],
      ["1", "one", "ایک"],
      ["tail", "ٹیل", "T"],
      ["divide", "out of", "میں سے", "تقسیم"]],
    "fallback_feedback": {
      "got_it": T("Well explained! One head out of two outcomes.", "بہت خوب! دو نتائج میں سے ایک ہیڈ۔"),
      "partly": T("Good start! Name both outcomes, then say how many are heads.", "اچھی شروعات! دونوں نتائج بتائیں، پھر کتنے ہیڈ ہیں۔"),
      "not_yet": T("A coin can land H or T. How many of those are heads?", "سکہ H یا T آ سکتا ہے۔ ان میں سے کتنے ہیڈ ہیں؟")},
    "limit_per_day": 3, "max_attempts": 2},
   probability_question(
     "s11_spinner",
     T("A spinner has 8 equal parts numbered 1 to 8. What is the probability of a number greater than 5?", "ایک اسپنر کے 8 برابر حصے ہیں جن پر 1 سے 8 لکھا ہے۔ 5 سے بڑا عدد آنے کا احتمال کیا ہے؟"),
     S11,
     T("E = {6, 7, 8}.", "E = {6, 7, 8}"),
     T("Right! 3/8.", "درست! 3/8"),
     T("n(E) = 3 (6, 7, 8) and n(S) = 8, so P = 3/8.", "n(E) = 3 (6، 7، 8) اور n(S) = 8، تو P = 3/8"),
     common_wrong=[W("3/5", "5 is the other numbers. Divide by all 8: 3/8.", "5 باقی اعداد ہیں۔ تمام 8 سے تقسیم کریں: 3/8", "part_to_part"),
                   W("5/8", "That is 5 or less. Greater than 5 is 6, 7, 8: 3/8.", "یہ 5 یا کم ہے۔ 5 سے بڑے 6، 7، 8 ہیں: 3/8")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Wanted outcomes over all outcomes. Now you can give any chance a number!", "مطلوبہ نتائج تقسیم تمام نتائج۔ اب آپ کسی بھی امکان کو عدد دے سکتے ہیں!"),
    "text": T("P(E) = n(E) ÷ n(S). Count the outcomes you want, divide by all the outcomes, and simplify if you like. An event that can't happen has probability 0. A probability is never more than 1.",
              "P(E) = n(E) ÷ n(S)۔ مطلوبہ نتائج گنیں، تمام نتائج سے تقسیم کریں، اور چاہیں تو مختصر کریں۔ جو واقعہ ہو ہی نہ سکے اس کا احتمال 0 ہے۔ احتمال کبھی 1 سے زیادہ نہیں ہوتا۔"),
    "points": [T("P(E) = n(E) ÷ n(S)", "P(E) = n(E) ÷ n(S)"),
               T("Divide by ALL the outcomes.", "تمام نتائج سے تقسیم کریں۔")]},
 ],
 "review_questions": [
   {"id": "r_prime", "type": "apply", "skill": SKILL, "step": probability_question(
     "r_prime",
     T("You roll a dice. What is the probability of a prime number?", "آپ ڈائس پھینکتے ہیں۔ مفرد عدد آنے کا احتمال کیا ہے؟"),
     R1,
     T("The primes up to 6 are 2, 3 and 5. 1 is not prime.", "6 تک مفرد اعداد 2، 3 اور 5 ہیں۔ 1 مفرد نہیں۔"),
     T("Right! 3/6 = 1/2.", "درست! 3/6 = 1/2"),
     T("E = {2, 3, 5}, so P = 3/6 = 1/2.", "E = {2, 3, 5}، تو P = 3/6 = 1/2"),
     common_wrong=[W("4/6", "1 is not a prime number. E = {2, 3, 5}: 3/6.", "1 مفرد عدد نہیں۔ E = {2, 3, 5}: 3/6")],
     qtype=None)},
   {"id": "r_blue", "type": "apply", "skill": SKILL, "step": probability_question(
     "r_blue",
     T("A bag has 4 red and 6 blue balls. What is P(blue)?", "ایک تھیلے میں 4 سرخ اور 6 نیلی گیندیں ہیں۔ P(نیلی) کیا ہے؟"),
     R2,
     T("6 blue out of how many balls?", "کتنی گیندوں میں سے 6 نیلی؟"),
     T("Right! 6/10 = 3/5.", "درست! 6/10 = 3/5"),
     T("6 blue out of 10 balls: 6/10 = 3/5.", "10 گیندوں میں سے 6 نیلی: 6/10 = 3/5"),
     common_wrong=[W("6/4", "Divide by all 10 balls, not by the red ones: 6/10.", "سرخ سے نہیں، تمام 10 گیندوں سے تقسیم کریں: 6/10", "part_to_part")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Probability unit (PCTB Mathematics 6, Sub-domain 12, 12.3). No textbook text or exercises were used.",
   "Answers are checked by value, so 3/6, 1/2 and 0.5 are all accepted; the feedback shows the simplest form.",
   "The book writes P(E) = n(E)/n(S); the lesson uses the same notation.",
   "Urdu terms to check: احتمال (probability), منصفانہ سکہ (fair coin), مفرد عدد (prime number), جفت عدد (even number).",
   "The numbers were worked out in content/sources/g6-maths-17/probability_of_an_event.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)
