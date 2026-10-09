from fractions import Fraction as F

from common import (T, opt, say, wrong, number_question, probability_question,
                    write, coins, balls, P, DICE, VOWELS, BOOK, REVIEW,
                    word, scale_question, PR_SAMPLE_SPACE, PR_SINGLE_EVENT,
                    PR_LIKELIHOOD, PR_WORD_PROBLEMS)

SKILL = PR_WORD_PROBLEMS
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]


def tickets(total, mine):
    """A lucky draw: one outcome per ticket, `mine` of them ours."""
    return ["mine"] * mine + ["other"] * (total - mine)


# s2: P(3) on a dice
S2 = P(lambda o: o == 3, DICE)
assert S2 == F(1, 6)
# s4: 40 tickets, Ali has 3 (to the others: 3/37)
S4 = P(lambda o: o == "mine", tickets(40, 3))
assert S4 == F(3, 40)
# s5: 6 mango, 4 strawberry, 10 orange toffees (one of three flavours: 1/3; to the rest: 6/14)
JAR = balls(mango=6, strawberry=4, orange=10)
S5 = P(lambda o: o == "mango", JAR)
assert S5 == F(3, 10) and len(JAR) - 6 == 14
# s6: a day of the week at random (Friday or not: 1/2)
assert P(lambda d: d == "Friday", DAYS) == F(1, 7)
# s7: 30 students, 18 girls: P(boy) (boys to girls: 12/18; girls: 18/30)
CLASS = balls(girl=18, boy=12)
S7 = P(lambda o: o == "boy", CLASS)
assert S7 == F(2, 5)
# s8: Ludo, a 5 or a 6
S8 = P(lambda o: o in (5, 6), DICE)
assert S8 == F(1, 3)
# s9: 1 ticket of 100 is 1/100, not 1/2
assert P(lambda o: o == "mine", tickets(100, 1)) == F(1, 100)
# s10: bag A (1 red, 3 blue) beats bag B (2 red, 8 blue) for red
A = P(lambda o: o == "red", balls(red=1, blue=3))
B = P(lambda o: o == "red", balls(red=2, blue=8))
assert A == F(1, 4) and B == F(1, 5) and A > B
# unit test
U1 = len(coins(3))
assert U1 == 8
U2 = P(lambda o: o > 2, DICE)
assert U2 == F(2, 3) and P(lambda o: o <= 2, DICE) == F(1, 3)
assert word(P(lambda o: o == "green", balls(green=7))) == "certain"
U4 = len([m for m in MONTHS if m.startswith("J")])
assert U4 == 3
U5 = P(lambda o: o == "mine", tickets(10, 3))  # 3 prize parts of 10
assert U5 == F(3, 10) and word(U5) == "unlikely"
# question bank: A to Z cards, P(vowel) (to the consonants: 5/21)
QB = P(lambda c: c in VOWELS, [chr(c) for c in range(ord("A"), ord("Z") + 1)])
assert QB == F(5, 26)
# question bank find_error: 5 mango, 5 orange, 10 lemon: P(mango) = 5/20
assert P(lambda o: o == "mango", balls(mango=5, orange=5, lemon=10)) == F(1, 4)
# review: 50 tickets, 5 bought; 24 students, 9 wear glasses
R1 = P(lambda o: o == "mine", tickets(50, 5))
assert R1 == F(1, 10)
R2 = P(lambda o: o == "no", balls(yes=9, no=15))
assert R2 == F(5, 8)

lesson = {
 "id": "g6-maths-17-probability-word-problems",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Solve real-world word problems on the probability of a single event and on equally likely outcomes.", "textbook": f"{BOOK}, 12.3 Probability of Single Event"}],
 "skills": [SKILL],
 "title": T("Probability word problems", "احتمال کے عملی سوالات"),
 "estimated_minutes": 18,
 "prerequisites": [{"skill": PR_LIKELIHOOD}, {"skill": PR_SINGLE_EVENT}, {"skill": PR_SAMPLE_SPACE}],
 "misconceptions": [
   {"id": "part_to_part", "description": "Divides by the other outcomes instead of by all outcomes."},
   {"id": "kinds_not_things", "description": "Uses the number of kinds (flavours, colours) as n(S) instead of the number of things."},
   {"id": "two_kinds_equal", "description": "Thinks 'win or lose' (two results) means a 1/2 chance."},
   {"id": "wrong_event", "description": "Counts the opposite event (girls instead of boys)."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_total", "type": "recall", "step": {
     "id": "qb_total", "type": "choice",
     "prompt": T("In a lucky draw, what is n(S)?", "لکی ڈرا میں n(S) کیا ہے؟"),
     "options": [
       opt("all", "The number of all the tickets", "تمام ٹکٹوں کی تعداد", True,
           "Yes! Any ticket could be drawn.", "جی ہاں! کوئی بھی ٹکٹ نکل سکتا ہے۔"),
       opt("mine", "The number of tickets I bought", "میرے خریدے ٹکٹوں کی تعداد", False,
           "That is n(E). n(S) is every ticket in the draw.", "یہ n(E) ہے۔ n(S) ڈرا کا ہر ٹکٹ ہے۔"),
       opt("two", "2: win or lose", "2: جیت یا ہار", False,
           "Win and lose are not equally likely. Count every ticket.", "جیت اور ہار یکساں ممکن نہیں۔ ہر ٹکٹ گنیں۔", "two_kinds_equal"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": probability_question(
     "qb_apply",
     T("The 26 letters A to Z are on 26 cards. Sana picks one. What is P(vowel)?", "A سے Z تک 26 حروف 26 کارڈز پر ہیں۔ ثنا ایک نکالتی ہے۔ P(حرفِ علت) کیا ہے؟"),
     QB,
     T("The vowels are A, E, I, O, U.", "حروفِ علت A، E، I، O، U ہیں۔"),
     T("Right! 5/26.", "درست! 5/26"),
     T("5 vowel cards out of 26 cards: 5/26.", "26 کارڈز میں سے 5 حرفِ علت: 5/26"),
     common_wrong=[wrong("5/21", "21 is the other letters. Divide by all 26: 5/26.", "21 باقی حروف ہیں۔ تمام 26 سے تقسیم کریں: 5/26", "part_to_part")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("A box has 5 mango, 5 orange and 10 lemon sweets. Bilal says P(mango) = 5/10. What is wrong?", "ایک ڈبے میں 5 آم، 5 مالٹے اور 10 لیموں والی میٹھی گولیاں ہیں۔ بلال کہتا ہے P(آم) = 5/10۔ کیا غلطی ہے؟"),
     "options": [
       opt("all_sweets", "There are 20 sweets in all: P(mango) = 5/20.", "کل 20 گولیاں ہیں: P(آم) = 5/20", True,
           "Yes! 5 + 5 + 10 = 20, so 5/20 = 1/4.", "جی ہاں! 5 + 5 + 10 = 20، تو 5/20 = 1/4"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "10 is only the lemon sweets. All of them: 20. P = 5/20.", "10 صرف لیموں والی ہیں۔ سب: 20۔ P = 5/20", "part_to_part"),
       opt("one_third", "It should be 1/3, for three flavours.", "تین ذائقوں کی وجہ سے 1/3 ہونا چاہیے۔", False,
           "Count sweets, not flavours: 5/20.", "ذائقے نہیں، گولیاں گنیں: 5/20", "kinds_not_things"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_steps", "front": T("Steps for a probability word problem?", "احتمال کے عملی سوال کے قدم؟"),
    "back": T("Count all outcomes, count the ones you want, divide, then say how likely.", "تمام نتائج گنیں، مطلوبہ گنیں، تقسیم کریں، پھر بتائیں کتنا امکان ہے۔")},
   {"id": "f_win_lose", "front": T("Is 'win or lose' 1/2?", "کیا 'جیت یا ہار' 1/2 ہے؟"),
    "back": T("Not always. 1 ticket of 100 wins with P = 1/100.", "ہمیشہ نہیں۔ 100 میں سے 1 ٹکٹ کے جیتنے کا P = 1/100")},
 ],
 "home_tasks": [{"id": "h_draw", "text": T(
   "Write the names of the days of the week on 7 slips of paper. Ask someone at home: what is P(a day starting with T)? Check by listing the days.",
   "ہفتے کے دنوں کے نام 7 پرچیوں پر لکھیں۔ گھر میں کسی سے پوچھیں: T سے شروع ہونے والے دن کا P کیا ہے؟ دن لکھ کر جانچیں۔")}],
 "glossary": [T("Lucky draw", "لکی ڈرا (قرعہ اندازی)"), T("At random", "بغیر دیکھے / اتفاقاً"), T("Probability", "احتمال")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "The school mela has a lucky draw! If I buy more tickets, how much better is my chance?",
                     "اسکول کے میلے میں لکی ڈرا ہے! اگر میں زیادہ ٹکٹ خریدوں تو میرا امکان کتنا بہتر ہوگا؟"),
    "text": T("Today we use probability in real life: lucky draws, toffee jars, Ludo and our class. Then a short test on the whole unit. First, one warm-up.", "آج ہم احتمال اصل زندگی میں استعمال کریں گے: لکی ڈرا، ٹافیوں کا مرتبان، لُڈو اور ہماری کلاس۔ پھر پورے باب کا چھوٹا ٹیسٹ۔ پہلے ایک سوال۔")},
   probability_question(
     "s2_foundation",
     T("You roll a dice. What is P(3)?", "آپ ڈائس پھینکتے ہیں۔ P(3) کیا ہے؟"),
     S2,
     T("One face out of six.", "چھ میں سے ایک رُخ۔"),
     T("Right! 1/6.", "درست! 1/6"),
     T("One face shows 3, out of 6 faces: 1/6.", "6 رُخ میں سے ایک پر 3 ہے: 1/6"),
     common_wrong=[wrong("1/3", "3 is the number we want, not the bottom. One face of six: 1/6.", "3 مطلوبہ عدد ہے، نیچے والا نہیں۔ چھ میں سے ایک رُخ: 1/6")],
     qtype="recall", skill=PR_SINGLE_EVENT),
   {"id": "s3_rule", "type": "explain",
    "character": say("happy", "Count all, count what you want, divide. Then say how likely it is!", "سب گنیں، مطلوبہ گنیں، تقسیم کریں۔ پھر بتائیں کتنا امکان ہے!"),
    "text": T("For a word problem: 1. Find n(S): every outcome that could happen (every ticket, every toffee, every student). 2. Find n(E): the outcomes you want. 3. P(E) = n(E) ÷ n(S). 4. Say how likely it is: under 1/2 is unlikely, over 1/2 is likely.",
              "عملی سوال کے لیے: 1۔ n(S) معلوم کریں: ہر وہ نتیجہ جو ہو سکتا ہے (ہر ٹکٹ، ہر ٹافی، ہر طالب علم)۔ 2۔ n(E) معلوم کریں: مطلوبہ نتائج۔ 3۔ P(E) = n(E) ÷ n(S)۔ 4۔ بتائیں کتنا امکان ہے: 1/2 سے کم، کم امکان؛ 1/2 سے زیادہ، زیادہ امکان۔")},
   probability_question(
     "s4_draw",
     T("40 tickets are sold for the lucky draw. Ali buys 3 of them. One ticket wins. What is the probability that Ali wins?", "لکی ڈرا کے 40 ٹکٹ بکے۔ علی نے ان میں سے 3 خریدے۔ ایک ٹکٹ جیتے گا۔ علی کے جیتنے کا احتمال کیا ہے؟"),
     S4,
     T("Ali's tickets out of all the tickets.", "تمام ٹکٹوں میں سے علی کے ٹکٹ۔"),
     T("Right! 3/40: unlikely, but better than 1/40.", "درست! 3/40: کم امکان، مگر 1/40 سے بہتر۔"),
     T("n(E) = 3 and n(S) = 40, so P = 3/40.", "n(E) = 3 اور n(S) = 40، تو P = 3/40"),
     common_wrong=[wrong("3/37", "37 is the other tickets. Divide by all 40: 3/40.", "37 باقی ٹکٹ ہیں۔ تمام 40 سے تقسیم کریں: 3/40", "part_to_part"),
                   wrong("1/40", "Ali has 3 tickets, so 3 outcomes win for him: 3/40.", "علی کے 3 ٹکٹ ہیں، تو 3 نتائج اس کی جیت ہیں: 3/40")]),
   probability_question(
     "s5_toffees",
     T("A jar has 6 mango, 4 strawberry and 10 orange toffees. Ayesha takes one without looking. What is P(mango)?", "ایک مرتبان میں 6 آم، 4 اسٹرابیری اور 10 مالٹے والی ٹافیاں ہیں۔ عائشہ بغیر دیکھے ایک لیتی ہے۔ P(آم) کیا ہے؟"),
     S5,
     T("How many toffees in all?", "کل کتنی ٹافیاں؟"),
     T("Right! 6/20 = 3/10.", "درست! 6/20 = 3/10"),
     T("6 + 4 + 10 = 20 toffees, 6 are mango: 6/20 = 3/10.", "6 + 4 + 10 = 20 ٹافیاں، 6 آم والی: 6/20 = 3/10"),
     common_wrong=[wrong("1/3", "Count toffees, not flavours: 6 out of 20.", "ذائقے نہیں، ٹافیاں گنیں: 20 میں سے 6", "kinds_not_things"),
                   wrong("6/14", "14 is the other toffees. Divide by all 20: 6/20.", "14 باقی ٹافیاں ہیں۔ تمام 20 سے تقسیم کریں: 6/20", "part_to_part")]),
   {"id": "s6_day", "type": "choice",
    "prompt": T("A day of the week is picked at random. What is P(Friday)?", "ہفتے کا ایک دن اتفاقاً چنا جاتا ہے۔ P(جمعہ) کیا ہے؟"),
    "options": [
      opt("one_seventh", "1/7", "1/7", True, "Yes! One day out of seven.", "جی ہاں! سات میں سے ایک دن۔"),
      opt("one_half", "1/2: it is Friday or it isn't", "1/2: جمعہ ہے یا نہیں", False,
          "'Friday or not' are not equally likely. 1 day out of 7: 1/7.", "'جمعہ یا نہیں' یکساں ممکن نہیں۔ 7 میں سے 1 دن: 1/7", "two_kinds_equal"),
      opt("seven", "7", "7", False, "A probability is never more than 1. 1 out of 7: 1/7.", "احتمال کبھی 1 سے زیادہ نہیں ہوتا۔ 7 میں سے 1: 1/7"),
    ]},
   probability_question(
     "s7_class",
     T("A class has 30 students: 18 girls and 12 boys. The teacher picks one student at random to ring the bell. What is P(a boy)?", "ایک کلاس میں 30 طلبہ ہیں: 18 لڑکیاں اور 12 لڑکے۔ استاد گھنٹی بجانے کے لیے اتفاقاً ایک طالب علم چنتے ہیں۔ P(لڑکا) کیا ہے؟"),
     S7,
     T("12 boys out of 30 students.", "30 طلبہ میں سے 12 لڑکے۔"),
     T("Right! 12/30 = 2/5.", "درست! 12/30 = 2/5"),
     T("n(E) = 12 boys, n(S) = 30 students: 12/30 = 2/5.", "n(E) = 12 لڑکے، n(S) = 30 طلبہ: 12/30 = 2/5"),
     common_wrong=[wrong("12/18", "18 is the girls. Divide by all 30 students: 12/30.", "18 لڑکیاں ہیں۔ تمام 30 طلبہ سے تقسیم کریں: 12/30", "part_to_part"),
                   wrong("18/30", "That is P(a girl). We want boys: 12/30.", "یہ P(لڑکی) ہے۔ ہمیں لڑکے چاہئیں: 12/30", "wrong_event")]),
   probability_question(
     "s8_ludo",
     T("In Ludo, Hamza wins if he rolls a 5 or a 6. What is the probability he wins on this roll?", "لُڈو میں حمزہ جیت جائے گا اگر 5 یا 6 آئے۔ اس باری جیتنے کا احتمال کیا ہے؟"),
     S8,
     T("E = {5, 6}.", "E = {5, 6}"),
     T("Right! 2/6 = 1/3.", "درست! 2/6 = 1/3"),
     T("Two faces win (5 and 6), out of 6: 2/6 = 1/3.", "6 میں سے دو رُخ (5 اور 6) جتاتے ہیں: 2/6 = 1/3"),
     common_wrong=[wrong("1/6", "Both 5 and 6 win, so n(E) = 2: 2/6.", "5 اور 6 دونوں جتاتے ہیں، تو n(E) = 2: 2/6")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Fatima buys 1 ticket in a lucky draw of 100 tickets. She says: 'I will either win or lose, so my chance is 1/2.' What is wrong?", "فاطمہ 100 ٹکٹوں والے لکی ڈرا میں 1 ٹکٹ خریدتی ہے۔ وہ کہتی ہے: 'میں یا جیتوں گی یا ہاروں گی، تو میرا امکان 1/2 ہے۔' کیا غلطی ہے؟"),
    "options": [
      opt("hundred", "Win and lose are not equally likely: P(win) = 1/100.", "جیت اور ہار یکساں ممکن نہیں: P(جیت) = 1/100", True,
          "Yes! Each ticket is an outcome: 1 of 100 is hers.", "جی ہاں! ہر ٹکٹ ایک نتیجہ ہے: 100 میں سے 1 اس کا۔"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "99 tickets make her lose and only 1 makes her win: 1/100.", "99 ٹکٹ ہرواتے ہیں اور صرف 1 جتاتا ہے: 1/100", "two_kinds_equal"),
      opt("certain", "She will surely win.", "وہ ضرور جیتے گی۔", False,
          "Only 1 of 100 tickets is hers: P = 1/100, very unlikely.", "100 میں سے صرف 1 ٹکٹ اس کا ہے: P = 1/100، بہت کم امکان۔"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Bag B has more red balls. So it's better, right? Can you check for me?",
                     "تھیلے B میں سرخ گیندیں زیادہ ہیں۔ تو وہ بہتر ہے نا؟ کیا آپ میرے لیے جانچ سکتے ہیں؟"),
    "task": T("Bag A has 1 red and 3 blue balls. Bag B has 2 red and 8 blue balls. Which bag gives a better chance of picking red? Explain.", "تھیلے A میں 1 سرخ اور 3 نیلی گیندیں ہیں۔ تھیلے B میں 2 سرخ اور 8 نیلی۔ کس تھیلے سے سرخ نکلنے کا امکان بہتر ہے؟ وضاحت کریں۔"),
    "key_idea": "Bag A: P(red) = 1/4. Bag B: P(red) = 2/10 = 1/5. 1/4 is bigger than 1/5, so bag A is better, even though bag B has more red balls: compare probabilities, not just counts.",
    "levels": {
      "got_it": "Finds 1/4 for bag A and 2/10 (1/5) for bag B and says bag A is better because 1/4 is bigger.",
      "partly": "Picks bag A without both probabilities, or finds the probabilities but compares them wrongly.",
      "not_yet": "Picks bag B because it has more red balls, or gives no reason."},
    "keywords": [
      ["1/4", "one quarter", "چوتھائی"],
      ["2/10", "1/5"],
      ["A"],
      ["bigger", "more", "greater", "زیادہ", "بڑا"]],
    "fallback_feedback": {
      "got_it": T("Well explained! 1/4 beats 1/5, so bag A.", "بہت خوب! 1/4، 1/5 سے بڑا ہے، تو تھیلا A۔"),
      "partly": T("Good start! Work out P(red) for each bag and compare.", "اچھی شروعات! ہر تھیلے کا P(سرخ) نکالیں اور موازنہ کریں۔"),
      "not_yet": T("More red balls isn't enough. What is P(red) in each bag?", "زیادہ سرخ گیندیں کافی نہیں۔ ہر تھیلے میں P(سرخ) کیا ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   {"id": "s11_unit_test", "type": "explain",
    "character": say("encouraging", "Test time! Five questions from the whole Probability unit. You can do it!",
                     "ٹیسٹ کا وقت! احتمال کے پورے باب سے پانچ سوال۔ آپ کر سکتے ہیں!"),
    "text": T("This short test has questions on sample spaces, the probability of an event, the probability scale and a real-life problem. Take your time.",
              "اس چھوٹے ٹیسٹ میں نمونی فضا، کسی واقعے کے احتمال، احتمال کے پیمانے اور ایک اصل زندگی کے سوال ہیں۔ آرام سے کریں۔")},
   number_question(
     "u1_coins",
     T("Test 1: Three coins are tossed together. How many outcomes are in the sample space?", "ٹیسٹ 1: تین سکے اکٹھے اچھالے جاتے ہیں۔ نمونی فضا میں کتنے نتائج ہیں؟"),
     U1,
     T("Two coins give 4. Each of those can end in H or T.", "دو سکوں سے 4۔ ہر ایک کے آخر میں H یا T آ سکتا ہے۔"),
     T("Right! 2 × 2 × 2 = 8.", "درست! 2 × 2 × 2 = 8"),
     T("HHH, HHT, HTH, HTT, THH, THT, TTH, TTT: 8.", "HHH، HHT، HTH، HTT، THH، THT، TTH، TTT: 8"),
     common_wrong=[wrong(6, "Each coin doubles the outcomes: 2 × 2 × 2 = 8, not 2 + 2 + 2.", "ہر سکہ نتائج دگنے کرتا ہے: 2 × 2 × 2 = 8، 2 + 2 + 2 نہیں۔"),
                   wrong(4, "That is two coins. Three coins give 8.", "یہ دو سکے ہیں۔ تین سکوں سے 8۔")],
     skill=PR_SAMPLE_SPACE),
   probability_question(
     "u2_dice",
     T("Test 2: You roll a dice. What is the probability of a number greater than 2?", "ٹیسٹ 2: آپ ڈائس پھینکتے ہیں۔ 2 سے بڑا عدد آنے کا احتمال کیا ہے؟"),
     U2,
     T("E = {3, 4, 5, 6}.", "E = {3, 4, 5, 6}"),
     T("Right! 4/6 = 2/3.", "درست! 4/6 = 2/3"),
     T("Four faces are greater than 2: 4/6 = 2/3.", "چار رُخ 2 سے بڑے ہیں: 4/6 = 2/3"),
     common_wrong=[wrong("2/6", "That is 2 or less. Greater than 2 is 3, 4, 5, 6: 4/6.", "یہ 2 یا کم ہے۔ 2 سے بڑے 3، 4، 5، 6: 4/6"),
                   wrong("4", "4 is how many faces. Divide by 6: 4/6.", "4 رُخوں کی تعداد ہے۔ 6 سے تقسیم کریں: 4/6")],
     skill=PR_SINGLE_EVENT),
   dict(scale_question(
     "u3_scale",
     T("Test 3: A bag has 7 green balls and nothing else. How likely is picking a green ball?", "ٹیسٹ 3: ایک تھیلے میں صرف 7 سبز گیندیں ہیں۔ سبز گیند نکلنے کا کتنا امکان ہے؟"),
     "certain",
     ("Yes! Every ball is green: P = 7/7 = 1.", "جی ہاں! ہر گیند سبز ہے: P = 7/7 = 1"),
     "Every ball is green, so P = 7/7 = 1: certain.", "ہر گیند سبز ہے، تو P = 7/7 = 1: یقینی۔"), skill=PR_LIKELIHOOD),
   number_question(
     "u4_months",
     T("Test 4: A month of the year is picked at random. How many outcomes are in the event 'the month starts with J'?", "ٹیسٹ 4: سال کا ایک مہینہ اتفاقاً چنا جاتا ہے۔ واقعہ 'مہینہ J سے شروع ہو' میں کتنے نتائج ہیں؟"),
     U4,
     T("Say the months in English: January, February, …", "مہینے انگریزی میں کہیں: January، February، …"),
     T("Right! January, June and July.", "درست! January، June اور July"),
     T("January, June and July start with J: 3 outcomes.", "January، June اور July، J سے شروع ہوتے ہیں: 3 نتائج"),
     common_wrong=[wrong(2, "Don't forget January! January, June, July: 3.", "January نہ بھولیں! January، June، July: 3"),
                   wrong(12, "12 is every month. Only 3 start with J.", "12 تو سب مہینے ہیں۔ صرف 3، J سے شروع ہوتے ہیں۔")],
     skill=PR_SAMPLE_SPACE),
   probability_question(
     "u5_spinner",
     T("Test 5: A spinner at the mela has 10 equal parts. 3 parts win a prize. What is the probability of winning a prize?", "ٹیسٹ 5: میلے کے ایک اسپنر کے 10 برابر حصے ہیں۔ 3 حصوں پر انعام ہے۔ انعام جیتنے کا احتمال کیا ہے؟"),
     U5,
     T("Winning parts out of all the parts.", "تمام حصوں میں سے جیتنے والے حصے۔"),
     T("Right! 3/10: unlikely.", "درست! 3/10: کم امکان۔"),
     T("3 winning parts out of 10: 3/10.", "10 میں سے 3 جیتنے والے حصے: 3/10"),
     common_wrong=[wrong("3/7", "7 is the parts with no prize. Divide by all 10: 3/10.", "7 بغیر انعام والے حصے ہیں۔ تمام 10 سے تقسیم کریں: 3/10", "part_to_part")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Probability unit complete! Now you can work out your chances anywhere.", "احتمال کا باب مکمل! اب آپ کہیں بھی اپنے امکانات نکال سکتے ہیں۔"),
    "text": T("Count every outcome for n(S), count the ones you want for n(E), and divide. Then say how likely it is. 'Win or lose' is not always 1/2: count the tickets. To compare two chances, compare the probabilities, not just the counts.",
              "n(S) کے لیے ہر نتیجہ گنیں، n(E) کے لیے مطلوبہ نتائج گنیں، اور تقسیم کریں۔ پھر بتائیں کتنا امکان ہے۔ 'جیت یا ہار' ہمیشہ 1/2 نہیں: ٹکٹ گنیں۔ دو امکانات کا موازنہ کرنے کے لیے احتمالات کا موازنہ کریں، صرف تعداد کا نہیں۔"),
    "points": [T("All outcomes on the bottom.", "تمام نتائج نیچے۔"),
               T("Compare probabilities, not counts.", "تعداد نہیں، احتمال کا موازنہ کریں۔")]},
 ],
 "review_questions": [
   {"id": "r_tickets", "type": "apply", "skill": SKILL, "step": probability_question(
     "r_tickets",
     T("50 tickets are sold in a lucky draw. Usman buys 5. What is the probability that Usman wins?", "لکی ڈرا میں 50 ٹکٹ بکے۔ عثمان نے 5 خریدے۔ عثمان کے جیتنے کا احتمال کیا ہے؟"),
     R1,
     T("Usman's tickets out of all the tickets.", "تمام ٹکٹوں میں سے عثمان کے ٹکٹ۔"),
     T("Right! 5/50 = 1/10.", "درست! 5/50 = 1/10"),
     T("5 out of 50: 5/50 = 1/10.", "50 میں سے 5: 5/50 = 1/10"),
     common_wrong=[wrong("5/45", "45 is the other tickets. Divide by all 50: 5/50.", "45 باقی ٹکٹ ہیں۔ تمام 50 سے تقسیم کریں: 5/50", "part_to_part")],
     qtype=None)},
   {"id": "r_glasses", "type": "apply", "skill": SKILL, "step": probability_question(
     "r_glasses",
     T("A class has 24 students. 9 of them wear glasses. One student is picked at random. What is P(no glasses)?", "ایک کلاس میں 24 طلبہ ہیں۔ ان میں سے 9 عینک لگاتے ہیں۔ ایک طالب علم اتفاقاً چنا جاتا ہے۔ P(عینک نہیں) کیا ہے؟"),
     R2,
     T("How many do NOT wear glasses?", "کتنے عینک نہیں لگاتے؟"),
     T("Right! 15/24 = 5/8.", "درست! 15/24 = 5/8"),
     T("24 − 9 = 15 without glasses: 15/24 = 5/8.", "24 − 9 = 15 بغیر عینک: 15/24 = 5/8"),
     common_wrong=[wrong("9/24", "That is P(glasses). Without glasses: 15/24.", "یہ P(عینک) ہے۔ بغیر عینک: 15/24", "wrong_event")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Probability unit (PCTB Mathematics 6, Sub-domain 12). No textbook text or exercises were used.",
   "The unit test (u1 to u5) covers sample space, probability of an event, the probability scale and a real-life problem.",
   "Months are named in English (January …) because the question is about their first letter.",
   "Urdu terms to check: لکی ڈرا / قرعہ اندازی (lucky draw), اتفاقاً (at random).",
   "The numbers were worked out in content/sources/g6-maths-17/probability_word_problems.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}

# ---------- pictures ----------
from figs import attach, step_says, dice_faces, bag, two_bags, key, cards, spinner, grid

for sid, text in (("s4_draw", "40 tickets"), ("s4_draw", "Ali buys 3"), ("s5_toffees", "6 mango, 4 strawberry and 10 orange"),
                  ("s7_class", "30 students: 18 girls and 12 boys"), ("s8_ludo", "5 or a 6"),
                  ("s10_explain_why", "Bag A has 1 red and 3 blue balls. Bag B has 2 red and 8 blue balls."),
                  ("u3_scale", "7 green balls"), ("u5_spinner", "10 equal parts. 3 parts win"),
                  ("qb_find_error", "5 mango, 5 orange and 10 lemon"), ("r_tickets", "50 tickets"),
                  ("r_tickets", "Usman buys 5"), ("r_glasses", "24 students. 9 of them wear glasses")):
    step_says(lesson, sid, text)
LUDO = [o for o in DICE if o in (5, 6)]
SPIN = tickets(10, 3)              # the mela spinner: 3 prize parts of 10
GLASSES = balls(yes=9, no=15)

attach(lesson, {
    "s2_foundation": dice_faces(DICE),
    "s4_draw": grid(tickets(40, 3), "mine", pre=("The lucky draw:", "قرعہ اندازی:"),
                    what_en=": they are Ali's tickets", what_ur=": یہ علی کے ٹکٹ ہیں"),
    "s5_toffees": bag(JAR, key("mango", "strawberry", "orange"), pre=("Ayesha's toffee jar.", "عائشہ کا ٹافیوں والا مرتبان۔")),
    "s6_day": cards([d[:2] for d in DAYS], pre=("The days of the week:", "ہفتے کے دن:")),
    "s7_class": grid(CLASS, "boy", shape="person", pre=("The class, one circle for each student.", "جماعت، ہر طالب علم کے لیے ایک دائرہ۔"),
                     what_en=": they are the boys, and the empty circles are the girls",
                     what_ur=": یہ لڑکے ہیں، اور خالی دائرے لڑکیاں ہیں"),
    "s8_ludo": dice_faces(DICE, ring=LUDO, pre=("Hamza's Ludo dice.", "حمزہ کا لُڈو کا پانسہ۔")),
    "s10_explain_why": two_bags(balls(red=1, blue=3), balls(red=2, blue=8), key("red", "blue")),
    "u3_scale": bag(balls(green=7), key("green")),
    "u5_spinner": spinner([None] * len(SPIN), shade=[i for i, o in enumerate(SPIN) if o == "mine"],
                          what_en=f"{SPIN.count('mine')} of them shaded (they win a prize) and {SPIN.count('other')} empty",
                          what_ur=f"جن میں سے {SPIN.count('mine')} رنگین ہیں (ان پر انعام ملتا ہے) اور {SPIN.count('other')} خالی"),
    "qb_find_error": bag(balls(mango=5, orange=5, lemon=10), key("mango", "orange", "lemon"), pre=("Bilal's box of sweets.", "بلال کا مٹھائیوں کا ڈبہ۔")),
    "r_tickets": grid(tickets(50, 5), "mine", pre=("The lucky draw:", "قرعہ اندازی:"),
                      what_en=": they are Usman's tickets", what_ur=": یہ عثمان کے ٹکٹ ہیں"),
    "r_glasses": grid(GLASSES, "yes", cols=8, shape="person", pre=("The class, one circle for each student.", "جماعت، ہر طالب علم کے لیے ایک دائرہ۔"),
                      what_en=": they are the students who wear glasses", what_ur=": یہ وہ طالب علم ہیں جو عینک لگاتے ہیں"),
})
write(lesson)
