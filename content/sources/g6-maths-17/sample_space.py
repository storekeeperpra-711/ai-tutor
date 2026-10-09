from common import (T, opt, say, wrong, number_question, write, coins, balls,
                    DICE, VOWELS, BOOK, REVIEW, SET_MEANING, PR_SAMPLE_SPACE)

SKILL = PR_SAMPLE_SPACE

# s2: members of {2, 4, 6, 8} (the biggest member is 8)
S2 = len({2, 4, 6, 8})
assert S2 == 4
# s4: rolling a dice
S4 = len(DICE)
assert S4 == 6
# s6: tossing two coins: HH, HT, TH, TT (HT and TH as one gives 3)
S6 = len(coins(2))
assert S6 == 4 and len({frozenset(o) for o in coins(2)}) == 3
# s7: a bag of 3 red, 2 blue and 5 green balls: one outcome per ball
S7 = len(balls(red=3, blue=2, green=5))
assert S7 == 10
# s8: event "an even number" on a dice
S8 = len([o for o in DICE if o % 2 == 0])
assert S8 == 3
# s9: two coins, Sana missed TH
assert set(coins(2)) - {"HH", "HT", "TT"} == {"TH"}
# s11: vowel cards in LAHORE
S11 = len([c for c in "LAHORE" if c in VOWELS])
assert S11 == 3 and len("LAHORE") == 6
# question bank: spinner 1 to 8, "greater than 5" (5 itself is not)
QB = len([o for o in range(1, 9) if o > 5])
assert QB == 3 and len([o for o in range(1, 9) if o >= 5]) == 4
# review: two coins, exactly one head; PAKISTAN cards showing a vowel
R1 = len([o for o in coins(2) if o.count("H") == 1])
assert R1 == 2
R2 = len([c for c in "PAKISTAN" if c in VOWELS])
assert R2 == 3 and len(set("PAKISTAN") & VOWELS) == 2

lesson = {
 "id": "g6-maths-17-sample-space",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Explain experiments, outcomes, sample space and events.", "textbook": f"{BOOK}, 12.1 Experiment and 12.2 Sample Space and an Event"}],
 "skills": [SKILL],
 "title": T("Outcomes and sample space", "نتائج اور نمونی فضا"),
 "estimated_minutes": 13,
 "prerequisites": [{"skill": SET_MEANING}],
 "misconceptions": [
   {"id": "order_ignored", "description": "Counts HT and TH (or similar outcomes in a different order) as one outcome."},
   {"id": "colours_not_objects", "description": "Counts kinds (colours, letters) instead of the things themselves (balls, cards)."},
   {"id": "missing_outcomes", "description": "Lists only some outcomes, such as the smallest and the biggest."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_meaning", "type": "recall", "step": {
     "id": "qb_meaning", "type": "choice",
     "prompt": T("The set of all possible outcomes of an experiment is called the …", "کسی تجربے کے تمام ممکنہ نتائج کا سیٹ کہلاتا ہے …"),
     "options": [
       opt("sample_space", "sample space", "نمونی فضا", True,
           "Yes! We write it as S, like S = {H, T}.", "جی ہاں! ہم اسے S لکھتے ہیں، جیسے S = {H, T}۔"),
       opt("event", "event", "واقعہ", False,
           "An event is only some of the outcomes. All of them together is the sample space.", "واقعہ صرف کچھ نتائج ہوتا ہے۔ سب نتائج مل کر نمونی فضا ہیں۔"),
       opt("outcome", "outcome", "نتیجہ", False,
           "An outcome is just one result. All the outcomes together make the sample space.", "نتیجہ صرف ایک نتیجہ ہے۔ سب نتائج مل کر نمونی فضا بناتے ہیں۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("A spinner has the numbers 1 to 8. How many outcomes are in the event 'a number greater than 5'?", "ایک اسپنر پر 1 سے 8 تک اعداد ہیں۔ واقعہ '5 سے بڑا عدد' میں کتنے نتائج ہیں؟"),
     QB,
     T("Greater than 5 does not include 5.", "5 سے بڑا میں 5 شامل نہیں۔"),
     T("Right! E = {6, 7, 8}.", "درست! E = {6, 7, 8}"),
     T("The numbers greater than 5 are 6, 7 and 8: three outcomes.", "5 سے بڑے اعداد 6، 7 اور 8 ہیں: تین نتائج۔"),
     common_wrong=[wrong(4, "5 is not greater than 5. E = {6, 7, 8}: 3 outcomes.", "5، 5 سے بڑا نہیں۔ E = {6, 7, 8}: 3 نتائج")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Bilal says the sample space of rolling a dice is S = {1, 6}, the smallest and biggest numbers. What is wrong?", "بلال کہتا ہے کہ ڈائس پھینکنے کی نمونی فضا S = {1, 6} ہے، سب سے چھوٹا اور سب سے بڑا عدد۔ کیا غلطی ہے؟"),
     "options": [
       opt("all", "S must list every outcome: {1, 2, 3, 4, 5, 6}.", "S میں ہر نتیجہ لکھنا ہے: {1, 2, 3, 4, 5, 6}", True,
           "Yes! Any of the six faces can come up.", "جی ہاں! چھ میں سے کوئی بھی رُخ آ سکتا ہے۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "A dice can also show 2, 3, 4 or 5. S = {1, 2, 3, 4, 5, 6}.", "ڈائس پر 2، 3، 4 یا 5 بھی آ سکتا ہے۔ S = {1, 2, 3, 4, 5, 6}", "missing_outcomes"),
       opt("six_only", "S should be {6}.", "S کو {6} ہونا چاہیے۔", False,
           "6 is just one outcome. S has all six: {1, 2, 3, 4, 5, 6}.", "6 صرف ایک نتیجہ ہے۔ S میں چھ ہیں: {1, 2, 3, 4, 5, 6}", "missing_outcomes"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_outcome", "front": T("Outcome?", "نتیجہ؟"),
    "back": T("One possible result of an experiment, like H when you toss a coin.", "کسی تجربے کا ایک ممکنہ نتیجہ، جیسے سکہ اچھالنے پر H۔")},
   {"id": "f_sample_space", "front": T("Sample space S?", "نمونی فضا S؟"),
    "back": T("The set of all outcomes. A dice: S = {1, 2, 3, 4, 5, 6}.", "تمام نتائج کا سیٹ۔ ڈائس: S = {1, 2, 3, 4, 5, 6}")},
   {"id": "f_event", "front": T("Event?", "واقعہ؟"),
    "back": T("Some of the outcomes, like 'an even number' = {2, 4, 6}.", "کچھ نتائج، جیسے 'جفت عدد' = {2, 4, 6}")},
 ],
 "home_tasks": [{"id": "h_coins", "text": T(
   "Take two coins at home. Toss them together 12 times and write down what you get each time (HH, HT, TH or TT). Did you see all four outcomes?",
   "گھر میں دو سکے لیں۔ انہیں 12 بار اکٹھے اچھالیں اور ہر بار لکھیں کہ کیا آیا (HH، HT، TH یا TT)۔ کیا چاروں نتائج آئے؟")}],
 "glossary": [T("Experiment", "تجربہ"), T("Outcome", "نتیجہ"), T("Sample space", "نمونی فضا"), T("Event", "واقعہ")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Before a cricket match, the captains toss a coin. What can happen? Let's list every possibility!",
                     "کرکٹ میچ سے پہلے کپتان سکہ اچھالتے ہیں۔ کیا ہو سکتا ہے؟ آئیں ہر امکان لکھیں!"),
    "text": T("Today we learn the words of probability: experiment, outcome, sample space and event. First, a quick question about sets.", "آج ہم احتمال کے الفاظ سیکھیں گے: تجربہ، نتیجہ، نمونی فضا اور واقعہ۔ پہلے سیٹ کا ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("How many members does the set {2, 4, 6, 8} have?", "سیٹ {2, 4, 6, 8} کے کتنے ارکان ہیں؟"),
     S2,
     T("Count the numbers inside the brackets.", "بریکٹ کے اندر اعداد گنیں۔"),
     T("Right! It has 4 members.", "درست! اس کے 4 ارکان ہیں۔"),
     T("Count them: 2, 4, 6, 8. That is 4 members.", "گنیں: 2، 4، 6، 8۔ یہ 4 ارکان ہیں۔"),
     common_wrong=[wrong(8, "8 is the biggest member. Count the members: 2, 4, 6, 8 is 4.", "8 سب سے بڑا رکن ہے۔ ارکان گنیں: 2، 4، 6، 8 یعنی 4۔")],
     qtype="recall", skill=SET_MEANING),
   {"id": "s3_words", "type": "explain",
    "character": say("happy", "Toss a coin: H or T. Those two outcomes make the sample space, S = {H, T}.", "سکہ اچھالیں: H یا T۔ یہ دو نتائج نمونی فضا بناتے ہیں، S = {H, T}۔"),
    "text": T("An experiment is something we do whose result we can't be sure of, like tossing a coin. Each possible result is an outcome: heads (H) or tails (T). The set of all outcomes is the sample space S. For a coin, S = {H, T}, so n(S) = 2. For a dice, S = {1, 2, 3, 4, 5, 6}. An event is some of the outcomes, like 'an even number' = {2, 4, 6}.",
              "تجربہ ایسا کام ہے جس کے نتیجے کا ہمیں یقین نہ ہو، جیسے سکہ اچھالنا۔ ہر ممکنہ نتیجہ ایک نتیجہ (outcome) ہے: ہیڈ (H) یا ٹیل (T)۔ تمام نتائج کا سیٹ نمونی فضا S ہے۔ سکے کے لیے S = {H, T}، تو n(S) = 2۔ ڈائس کے لیے S = {1, 2, 3, 4, 5, 6}۔ واقعہ کچھ نتائج ہوتا ہے، جیسے 'جفت عدد' = {2, 4, 6}۔")},
   number_question(
     "s4_dice",
     T("You roll a dice once. How many outcomes are in the sample space?", "آپ ڈائس ایک بار پھینکتے ہیں۔ نمونی فضا میں کتنے نتائج ہیں؟"),
     S4,
     T("A dice has a number on each face.", "ڈائس کے ہر رُخ پر ایک عدد ہے۔"),
     T("Right! S = {1, 2, 3, 4, 5, 6}, so n(S) = 6.", "درست! S = {1, 2, 3, 4, 5, 6}، تو n(S) = 6"),
     T("Any face can come up: 1, 2, 3, 4, 5 or 6. That is 6 outcomes.", "کوئی بھی رُخ آ سکتا ہے: 1، 2، 3، 4، 5 یا 6۔ یہ 6 نتائج ہیں۔"),
     common_wrong=[wrong(1, "One roll gives one number, but it could be any of 6. n(S) = 6.", "ایک بار پھینکنے سے ایک عدد آتا ہے، مگر وہ 6 میں سے کوئی بھی ہو سکتا ہے۔ n(S) = 6", "missing_outcomes")]),
   {"id": "s5_coin_space", "type": "choice",
    "prompt": T("Which is the sample space of tossing one coin?", "ایک سکہ اچھالنے کی نمونی فضا کون سی ہے؟"),
    "options": [
      opt("h_t", "{H, T}", "{H, T}", True, "Yes! Heads or tails: two outcomes.", "جی ہاں! ہیڈ یا ٹیل: دو نتائج۔"),
      opt("h", "{H}", "{H}", False, "Tails can come up too. S = {H, T}.", "ٹیل بھی آ سکتا ہے۔ S = {H, T}", "missing_outcomes"),
      opt("h_t_h_t", "{H, T, H, T}", "{H, T, H, T}", False, "Each outcome is listed once. S = {H, T}.", "ہر نتیجہ ایک بار لکھا جاتا ہے۔ S = {H, T}"),
    ]},
   number_question(
     "s6_two_coins",
     T("Now toss two coins together: a 5-rupee coin and a 10-rupee coin. How many outcomes are there?", "اب دو سکے اکٹھے اچھالیں: 5 روپے کا اور 10 روپے کا۔ کتنے نتائج ہیں؟"),
     S6,
     T("List them: HH, HT, TH, …", "لکھیں: HH، HT، TH، …"),
     T("Right! S = {HH, HT, TH, TT}.", "درست! S = {HH, HT, TH, TT}"),
     T("S = {HH, HT, TH, TT}. HT (5 heads, 10 tails) is different from TH.", "S = {HH, HT, TH, TT}۔ HT (5 کا ہیڈ، 10 کا ٹیل) اور TH الگ ہیں۔"),
     common_wrong=[wrong(3, "HT and TH are different: the 5-rupee coin shows H in one and T in the other. There are 4.", "HT اور TH الگ ہیں: ایک میں 5 روپے والا H ہے اور دوسرے میں T۔ کل 4 ہیں۔", "order_ignored"),
                   wrong(2, "That is one coin. Two coins give HH, HT, TH and TT: 4 outcomes.", "یہ ایک سکہ ہے۔ دو سکوں سے HH، HT، TH اور TT: 4 نتائج۔", "missing_outcomes")]),
   number_question(
     "s7_balls",
     T("A bag has 3 red, 2 blue and 5 green balls. Hamza picks one ball without looking. How many different balls could he pick?", "ایک تھیلے میں 3 سرخ، 2 نیلی اور 5 سبز گیندیں ہیں۔ حمزہ بغیر دیکھے ایک گیند نکالتا ہے۔ وہ کتنی مختلف گیندوں میں سے کوئی نکال سکتا ہے؟"),
     S7,
     T("Each ball is one outcome. Count all the balls.", "ہر گیند ایک نتیجہ ہے۔ سب گیندیں گنیں۔"),
     T("Right! 3 + 2 + 5 = 10 outcomes.", "درست! 3 + 2 + 5 = 10 نتائج"),
     T("Any of the balls can come out: 3 + 2 + 5 = 10.", "کوئی بھی گیند نکل سکتی ہے: 3 + 2 + 5 = 10"),
     common_wrong=[wrong(3, "There are 3 colours, but 10 balls. Each ball is an outcome: 10.", "رنگ 3 ہیں، مگر گیندیں 10۔ ہر گیند ایک نتیجہ ہے: 10", "colours_not_objects")]),
   number_question(
     "s8_event",
     T("Roll a dice. How many outcomes are in the event E = 'an even number'?", "ڈائس پھینکیں۔ واقعہ E = 'جفت عدد' میں کتنے نتائج ہیں؟"),
     S8,
     T("Even numbers can be shared into twos: which faces?", "جفت اعداد دو دو میں بٹ جاتے ہیں: کون سے رُخ؟"),
     T("Right! E = {2, 4, 6}.", "درست! E = {2, 4, 6}"),
     T("The even faces are 2, 4 and 6, so E has 3 outcomes.", "جفت رُخ 2، 4 اور 6 ہیں، تو E میں 3 نتائج ہیں۔"),
     common_wrong=[wrong(6, "6 is all the outcomes. Only 2, 4 and 6 are even: 3.", "6 تو سب نتائج ہیں۔ صرف 2، 4 اور 6 جفت ہیں: 3"),
                   wrong(2, "Don't forget 2! E = {2, 4, 6}: 3 outcomes.", "2 نہ بھولیں! E = {2, 4, 6}: 3 نتائج", "missing_outcomes")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Sana writes the sample space of tossing two coins as S = {HH, HT, TT}. What is wrong?", "ثنا دو سکے اچھالنے کی نمونی فضا S = {HH, HT, TT} لکھتی ہے۔ کیا غلطی ہے؟"),
    "options": [
      opt("missing_th", "TH is missing: first coin tails, second heads is another outcome.", "TH رہ گیا: پہلا سکہ ٹیل، دوسرا ہیڈ ایک اور نتیجہ ہے۔", True,
          "Yes! S = {HH, HT, TH, TT}, so n(S) = 4.", "جی ہاں! S = {HH, HT, TH, TT}، تو n(S) = 4"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "HT and TH are different outcomes. S = {HH, HT, TH, TT}.", "HT اور TH الگ نتائج ہیں۔ S = {HH, HT, TH, TT}", "order_ignored"),
      opt("no_hh", "HH should not be there.", "HH نہیں ہونا چاہیے۔", False,
          "Both coins can land heads, so HH stays. TH is the one missing.", "دونوں سکے ہیڈ آ سکتے ہیں، تو HH رہے گا۔ TH رہ گیا ہے۔"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "I always mix up the sample space and an event. Can you teach me the difference?",
                     "میں ہمیشہ نمونی فضا اور واقعہ میں الجھ جاتا ہوں۔ کیا آپ مجھے فرق سکھا سکتے ہیں؟"),
    "task": T("You roll a dice. Write the sample space, and the event 'a number greater than 4'. How are they different?", "آپ ڈائس پھینکتے ہیں۔ نمونی فضا لکھیں، اور واقعہ '4 سے بڑا عدد'۔ ان میں کیا فرق ہے؟"),
    "key_idea": "The sample space is every outcome: S = {1, 2, 3, 4, 5, 6}. The event 'greater than 4' is only some of them: E = {5, 6}. An event is part of the sample space.",
    "levels": {
      "got_it": "Writes S = {1, 2, 3, 4, 5, 6} and E = {5, 6}, and says the event is part of (some of) the sample space.",
      "partly": "Writes one set correctly, or both without saying how they differ.",
      "not_yet": "Gives no sets or no reason."},
    "keywords": [
      ["5", "five", "پانچ"],
      ["6", "six", "چھ"],
      ["all", "every", "تمام", "سب"],
      ["part", "some", "کچھ", "حصہ"]],
    "fallback_feedback": {
      "got_it": T("Well explained! E = {5, 6} is part of S.", "بہت خوب! E = {5, 6}، S کا حصہ ہے۔"),
      "partly": T("Good start! S has every face; which faces are greater than 4?", "اچھی شروعات! S میں ہر رُخ ہے؛ 4 سے بڑے رُخ کون سے ہیں؟"),
      "not_yet": T("List all six faces first. Then pick the ones greater than 4.", "پہلے چھ رُخ لکھیں۔ پھر 4 سے بڑے چن لیں۔")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_letters",
     T("The letters of LAHORE are written on 6 cards. Ayesha picks one card. How many outcomes are in the event 'a vowel'?", "لفظ LAHORE کے حروف 6 کارڈز پر لکھے ہیں۔ عائشہ ایک کارڈ نکالتی ہے۔ واقعہ 'حرفِ علت (vowel)' میں کتنے نتائج ہیں؟"),
     S11,
     T("The vowels are A, E, I, O and U. Which are in LAHORE?", "حروفِ علت A، E، I، O اور U ہیں۔ LAHORE میں کون سے ہیں؟"),
     T("Right! E = {A, O, E}.", "درست! E = {A, O, E}"),
     T("L-A-H-O-R-E: the vowels are A, O and E, so 3 outcomes.", "L-A-H-O-R-E: حروفِ علت A، O اور E ہیں، تو 3 نتائج۔"),
     common_wrong=[wrong(2, "Check the last letter: E is a vowel too. A, O, E: 3.", "آخری حرف دیکھیں: E بھی حرفِ علت ہے۔ A، O، E: 3", "missing_outcomes"),
                   wrong(6, "6 is all the cards. Only A, O and E are vowels: 3.", "6 تو سب کارڈ ہیں۔ صرف A، O اور E حروفِ علت ہیں: 3")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Experiment, outcome, sample space, event. You know all four words now!", "تجربہ، نتیجہ، نمونی فضا، واقعہ۔ اب آپ چاروں الفاظ جانتے ہیں!"),
    "text": T("An experiment has outcomes. The set of all outcomes is the sample space S, and n(S) is how many there are. An event is some of the outcomes. With two coins, HT and TH are different outcomes. In a bag, each ball is an outcome, not each colour.",
              "تجربے کے نتائج ہوتے ہیں۔ تمام نتائج کا سیٹ نمونی فضا S ہے، اور n(S) ان کی تعداد ہے۔ واقعہ کچھ نتائج ہوتا ہے۔ دو سکوں میں HT اور TH الگ نتائج ہیں۔ تھیلے میں ہر گیند ایک نتیجہ ہے، ہر رنگ نہیں۔"),
    "points": [T("Coin: S = {H, T}. Dice: S = {1, …, 6}.", "سکہ: S = {H, T}۔ ڈائس: S = {1، …، 6}"),
               T("An event is part of S.", "واقعہ S کا حصہ ہے۔")]},
 ],
 "review_questions": [
   {"id": "r_one_head", "type": "apply", "skill": SKILL, "step": number_question(
     "r_one_head",
     T("Two coins are tossed. How many outcomes have exactly one head?", "دو سکے اچھالے جاتے ہیں۔ کتنے نتائج میں ٹھیک ایک ہیڈ ہے؟"),
     R1,
     T("S = {HH, HT, TH, TT}. Count the ones with one H.", "S = {HH, HT, TH, TT}۔ ایک H والے گنیں۔"),
     T("Right! HT and TH.", "درست! HT اور TH"),
     T("HT and TH each have one head: 2 outcomes.", "HT اور TH میں ایک ایک ہیڈ ہے: 2 نتائج۔"),
     common_wrong=[wrong(1, "HT and TH are different outcomes, and both have one head: 2.", "HT اور TH الگ نتائج ہیں، اور دونوں میں ایک ہیڈ ہے: 2", "order_ignored")],
     qtype=None)},
   {"id": "r_vowels", "type": "apply", "skill": SKILL, "step": number_question(
     "r_vowels",
     T("The letters of PAKISTAN are written on 8 cards. How many cards show a vowel?", "لفظ PAKISTAN کے حروف 8 کارڈز پر لکھے ہیں۔ کتنے کارڈز پر حرفِ علت ہے؟"),
     R2,
     T("Go letter by letter: P-A-K-I-S-T-A-N.", "حرف بہ حرف دیکھیں: P-A-K-I-S-T-A-N"),
     T("Right! A, I and A: 3 cards.", "درست! A، I اور A: 3 کارڈ"),
     T("There are two A cards and one I card: 3.", "A کے دو کارڈ اور I کا ایک کارڈ: 3"),
     common_wrong=[wrong(2, "A is on two cards. Count each card: A, I, A = 3.", "A دو کارڈز پر ہے۔ ہر کارڈ گنیں: A، I، A = 3", "colours_not_objects")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Probability unit (PCTB Mathematics 6, Sub-domain 12). No textbook text or exercises were used; the book was used only for its outline and words.",
   "The book writes S = {H, T}, n(S) and 'dice' for one or many; the lesson does the same.",
   "Urdu terms to check: تجربہ (experiment), نتیجہ (outcome), نمونی فضا (sample space), واقعہ (event), احتمال (probability), حرفِ علت (vowel). Heads and tails are written ہیڈ / ٹیل.",
   "The numbers were worked out in content/sources/g6-maths-17/sample_space.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}

# ---------- pictures ----------
from figs import (attach, step_says, figure, label, circle, coins_row, coin_table, dice_faces, dice_cube,
                  bag, key, cards, spinner, W)

SET = [2, 4, 6, 8]
assert len(SET) == S2
step_says(lesson, "s2_foundation", "{" + ", ".join(map(str, SET)) + "}")
BAG = balls(red=3, blue=2, green=5)
assert len(BAG) == S7
step_says(lesson, "s7_balls", "3 red, 2 blue and 5 green")
step_says(lesson, "s11_letters", "LAHORE")
step_says(lesson, "r_vowels", "PAKISTAN")
step_says(lesson, "qb_apply", "1 to 8")
step_says(lesson, "s6_two_coins", "5-rupee coin and a 10-rupee coin")
TWO = coins(2)
assert len(TWO) == 4


def set_figure(members):
    """A set drawn as a big circle with its members inside."""
    c, r = (W / 2, 62), 50
    items = [circle(c, r)]
    for i, m in enumerate(members):
        x = c[0] + (i % 2 - 0.5) * 40
        y = c[1] + (i // 2 - 0.5) * 36
        items.append(label((x, y), m))
    return figure(W, 124, f"A big circle (the set) with the members {', '.join(map(str, members))} inside it.",
                  f"ایک بڑا دائرہ (سیٹ) جس کے اندر ارکان {'، '.join(map(str, members))} ہیں۔", items)


attach(lesson, {
    "s1_hook": coins_row(["H"], "A coin spinning in the air, with a curved line above it. It shows H (heads).",
                         "ہوا میں گھومتا ایک سکہ، اوپر ایک خم دار لکیر۔ اس پر H (ہیڈ) نظر آ رہا ہے۔", toss=True),
    "s2_foundation": set_figure(SET),
    "s3_words": dice_faces(DICE, pre=("The sample space of a dice, S = {1, 2, 3, 4, 5, 6}:", "پانسے کی نمونی فضا، S = {1, 2, 3, 4, 5, 6}:")),
    "s4_dice": dice_cube(),
    "s6_two_coins": coins_row(["5", "10"], "Two coins side by side: a 5-rupee coin marked 5 and a 10-rupee coin marked 10.",
                              "دو سکے ساتھ ساتھ: 5 لکھا 5 روپے کا سکہ اور 10 لکھا 10 روپے کا سکہ۔"),
    "s7_balls": bag(BAG, key("red", "blue", "green")),
    "s8_event": dice_faces(DICE),
    "s11_letters": cards("LAHORE"),
    "s12_summary": coin_table(
        "A table for tossing two coins. Down the side: the first coin, H or T. Across the top: the second coin, H or T. The four cells hold HH, HT, TH and TT.",
        "دو سکے اچھالنے کا جدول۔ بائیں طرف نیچے کو: پہلا سکہ، H یا T۔ اوپر: دوسرا سکہ، H یا T۔ چار خانوں میں HH، HT، TH اور TT ہیں۔"),
    "qb_apply": spinner([str(n) for n in range(1, 9)]),
    "r_one_head": coin_table(
        "A table for tossing two coins. Down the side: the first coin, H or T. Across the top: the second coin, H or T. The four cells hold HH, HT, TH and TT.",
        "دو سکے اچھالنے کا جدول۔ بائیں طرف نیچے کو: پہلا سکہ، H یا T۔ اوپر: دوسرا سکہ، H یا T۔ چار خانوں میں HH، HT، TH اور TT ہیں۔"),
    "r_vowels": cards("PAKISTAN"),
})
write(lesson)
