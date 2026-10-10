"""Practice set for Exercise 12.1 of the book: sample spaces for coins, dice, cards
and balls, the probability of a single event, equally likely or not, and short
word problems. The questions are new; only the kinds of question follow the book."""
from fractions import Fraction as F

from common import (T, say, nq, pq, ch, practice_lesson, practice_intro, write, EX_SKILL, frac,
                    coins, balls, P, DICE, VOWELS, PR_SAMPLE_SPACE, PR_SINGLE_EVENT,
                    PR_LIKELIHOOD, PR_WORD_PROBLEMS)
from figs import coins_row, coin_table, dice_faces, bag, cards, key, with_fig

SKILL = EX_SKILL["12.1"]

# q1: one coin
assert coins(1) == ["H", "T"]
# q2: two coins
Q2 = len(coins(2))
assert Q2 == 4 and coins(2) == ["HH", "HT", "TH", "TT"]
# q4: three coins
Q4 = len(coins(3))
assert Q4 == 8 and len(coins(3)) != 6
# q5: two dice
TWO_DICE = [(a, b) for a in DICE for b in DICE]
Q5 = len(TWO_DICE)
assert Q5 == 36 and len(DICE) * 2 == 12
# q6: a dice shows more than 4
Q6 = P(lambda o: o > 4, DICE)
assert Q6 == F(1, 3) and P(lambda o: o >= 4, DICE) == F(1, 2) and F(2, 4) != Q6
# q7: a bag of 12 balls, 4 red, 3 blue, 5 green; P(green)
BAG = balls(red=4, blue=3, green=5)
Q7 = P(lambda o: o == "green", BAG)
assert len(BAG) == 12 and Q7 == F(5, 12) and F(5, 7) != Q7 and len([b for b in BAG if b != "green"]) == 7
# q8: PLANET cards, P(vowel)
WORD = "PLANET"
Q8 = P(lambda o: o in VOWELS, WORD)
assert Q8 == F(1, 3) and sum(1 for o in WORD if o in VOWELS) == 2 and F(2, 4) != Q8 and F(4, 6) != Q8
# q9: two coins, exactly one head
Q9 = P(lambda o: o.count("H") == 1, coins(2))
assert Q9 == F(1, 2) and F(1, 4) != Q9 and F(1, 3) != Q9
# q11: two dice, the sum is 7
Q11 = F(sum(1 for a, b in TWO_DICE if a + b == 7), len(TWO_DICE))
assert Q11 == F(1, 6) and sum(1 for a, b in TWO_DICE if a + b == 7) == 6 and F(1, 12) != Q11 and F(1, 36) != Q11
# q12: raffle, 40 tickets, Sana has 5
TICKETS, MINE = 40, 5
Q12 = F(MINE, TICKETS)
assert Q12 == F(1, 8) and F(MINE, TICKETS - MINE) == F(1, 7) and Q12 != F(1, 7)
# q13 (find the error): 3 red, 5 blue; P(red) = 3/8, not 3/5
Q13 = P(lambda o: o == "red", balls(red=3, blue=5))
assert Q13 == F(3, 8) and F(3, 5) != Q13
# q14: 24 marbles, P(green) = 1/6, so the number of green marbles
Q14_N, Q14_P = 24, F(1, 6)
Q14 = Q14_P * Q14_N
assert Q14 == 4 and Q14.denominator == 1
Q14 = int(Q14)
# bank and review
QB_DICE = P(lambda o: o in (1, 2, 3), DICE)
assert QB_DICE == F(1, 2)
QB2 = P(lambda o: o == "head", ["head", "tail"])
assert QB2 == F(1, 2)
QB3 = P(lambda o: o in VOWELS, "RIVER")          # I and E
assert QB3 == F(2, 5) and F(2, 3) != QB3
R1 = P(lambda o: o == 7, DICE)
assert R1 == 0
R2 = P(lambda o: o in DICE, DICE)
assert R2 == 1
R3 = P(lambda o: o == "blue", balls(red=5, blue=3, green=2))
assert R3 == F(3, 10)

F_TOSS = coins_row(["H", "T"],
    "Two coins side by side, one showing H (heads) and one showing T (tails). They stand for the two outcomes of one toss.",
    "دو سکے ساتھ ساتھ، ایک پر H (چت) اور ایک پر T (پٹ)۔ یہ ایک اچھال کے دو نتائج کو ظاہر کرتے ہیں۔")
F_TABLE = coin_table(
    "The table for tossing two coins. The first coin is down the side and the second coin is across the top. The four cells show HH, HT, TH and TT.",
    "دو سکے اچھالنے کا جدول۔ پہلا سکہ اطراف میں اور دوسرا سکہ اوپر ہے۔ چار خانوں میں HH، HT، TH اور TT لکھا ہے۔")
F_DICE = dice_faces(DICE)
F_BAG = bag(BAG, key("green", "red", "blue"))
F_CARDS = cards(WORD)
F_BAG_QB = bag(balls(red=3, blue=5), key("red", "blue"))

lesson = practice_lesson(
 "12.1", script="exercise_12_1.py",
 title=T("Exercise 12.1 practice: sample spaces and probability", "مشق 12.1 کی پریکٹس: نمونی فضا اور احتمال"),
 outcome="List and count the outcomes of coins, dice, cards and balls, find the probability of a single event as n(E) / n(S), tell equally likely from not equally likely outcomes, and solve short word problems.",
 prerequisites=[PR_SAMPLE_SPACE, PR_SINGLE_EVENT, PR_LIKELIHOOD, PR_WORD_PROBLEMS],
 misconceptions=[
   {"id": "space_miscount", "description": "Counts the outcomes of two or three coins or two dice wrongly, for example adding instead of multiplying, or counting HT and TH as one."},
   {"id": "upside_down", "description": "Writes n(S) / n(E) instead of n(E) / n(S)."},
   {"id": "part_to_part", "description": "Divides by the other outcomes (3 red to 5 blue) instead of by all the outcomes."},
   {"id": "event_miscount", "description": "Counts the favourable outcomes wrongly, for example including the boundary number in 'more than 4'."},
   {"id": "equally_likely_mix", "description": "Thinks the outcomes of a bag with different numbers of each colour are equally likely."},
   {"id": "one_way_only", "description": "Counts only one way of getting an outcome of two coins or two dice (HT but not TH, 1 and 6 but not 6 and 1)."},
 ],
 steps=[
   practice_intro("12.1",
     "Here you practise listing sample spaces for coins, dice, cards and balls, finding the probability of an event, and deciding whether outcomes are equally likely.",
     "اس میں آپ سکوں، پانسوں، کارڈوں اور گیندوں کی نمونی فضا لکھنا، واقعے کا احتمال نکالنا، اور یہ فیصلہ کرنا دہرائیں گے کہ نتائج یکساں امکان کے ہیں یا نہیں۔",
     "Exercise 12.1 is about probability. Ready?", "مشق 12.1 احتمال کے بارے میں ہے۔ تیار؟"),
   with_fig(ch("q1_space", ("A fair coin is tossed once. What is the sample space?", "ایک منصفانہ سکہ ایک بار اچھالا جاتا ہے۔ نمونی فضا کیا ہے؟"),
      ("S = {H, T}", "S = {H, T}", "Yes! A coin can land heads (H) or tails (T), and nothing else.", "جی ہاں! سکہ چت (H) یا پٹ (T) گر سکتا ہے، اور کچھ نہیں۔"),
      [("S = {H}", "S = {H}", "A coin can also land tails.", "سکہ پٹ بھی گر سکتا ہے۔", "space_miscount"),
       ("S = {HH, TT}", "S = {HH, TT}", "That is for two coins, and even then it leaves out HT and TH.", "یہ دو سکوں کے لیے ہے، اور تب بھی اس میں HT اور TH رہ گئے ہیں۔", "space_miscount")],
      0, qtype="recall"), F_TOSS),
   with_fig(nq("q2_two_coins", ("Two coins are tossed together. How many outcomes are in the sample space? The table shows the first coin down the side and the second across the top.", "دو سکے ایک ساتھ اچھالے جاتے ہیں۔ نمونی فضا میں کتنے نتائج ہیں؟ جدول میں پہلا سکہ اطراف میں اور دوسرا اوپر ہے۔"), Q2,
      ("Count the cells: HH, HT, TH, TT.", "خانے گنیں: HH، HT، TH، TT"),
      ("Right! 2 × 2 = 4 outcomes.", "درست! 2 × 2 = 4 نتائج"), ("HH, HT, TH, TT: four.", "HH، HT، TH، TT: چار"),
      [(2, "2 is the outcomes of one coin. Two coins: 2 × 2 = 4.", "2 ایک سکے کے نتائج ہیں۔ دو سکے: 2 × 2 = 4", "space_miscount"),
       (3, "3 counts HT and TH as one. They are different outcomes: 4.", "3 میں HT اور TH کو ایک گنا گیا۔ یہ الگ نتائج ہیں: 4", "one_way_only")], qtype="recall"), F_TABLE),
   {"id": "s_idea", "type": "explain",
    "character": say("thinking", "List every outcome once, count them, then count the ones you want.", "ہر نتیجہ ایک بار لکھیں، گنیں، پھر مطلوبہ نتائج گنیں۔"),
    "text": T("The sample space S lists every possible outcome of an experiment: a coin gives {H, T}, a dice gives {1, 2, 3, 4, 5, 6}. Two coins give 2 × 2 = 4 outcomes, three coins 2 × 2 × 2 = 8, and two dice 6 × 6 = 36. The probability of an event E is P(E) = n(E) ÷ n(S): the outcomes you want, over all the outcomes. Outcomes are equally likely when none is favoured, like a fair coin or a fair dice. P = 0 is impossible and P = 1 is certain.",
              "نمونی فضا S کسی تجربے کے تمام ممکنہ نتائج لکھتی ہے: سکے کی {H, T}، پانسے کی {1, 2, 3, 4, 5, 6}۔ دو سکوں کے 2 × 2 = 4 نتائج، تین سکوں کے 2 × 2 × 2 = 8، اور دو پانسوں کے 6 × 6 = 36 ہوتے ہیں۔ واقعے E کا احتمال P(E) = n(E) ÷ n(S) ہے: مطلوبہ نتائج تقسیم تمام نتائج۔ نتائج یکساں امکان کے ہوتے ہیں جب کسی کو ترجیح نہ ہو، جیسے منصفانہ سکہ یا منصفانہ پانسہ۔ P = 0 ناممکن اور P = 1 یقینی ہے۔")},
   nq("q3_three_coins", ("Three coins are tossed together. How many outcomes are in the sample space?", "تین سکے ایک ساتھ اچھالے جاتے ہیں۔ نمونی فضا میں کتنے نتائج ہیں؟"), Q4,
      ("Each coin has 2 outcomes: 2 × 2 × 2.", "ہر سکے کے 2 نتائج ہیں: 2 × 2 × 2"),
      ("Right! 2 × 2 × 2 = 8 outcomes.", "درست! 2 × 2 × 2 = 8 نتائج"), ("HHH, HHT, HTH, HTT, THH, THT, TTH, TTT: eight.", "HHH، HHT، HTH، HTT، THH، THT، TTH، TTT: آٹھ"),
      [(6, "6 is 2 + 2 + 2. The coins multiply: 2 × 2 × 2 = 8.", "6 یعنی 2 + 2 + 2۔ سکوں کے نتائج ضرب ہوتے ہیں: 2 × 2 × 2 = 8", "space_miscount"),
       (9, "9 is 3 × 3. Each coin has 2 outcomes: 2 × 2 × 2 = 8.", "9 یعنی 3 × 3۔ ہر سکے کے 2 نتائج ہیں: 2 × 2 × 2 = 8", "space_miscount")]),
   nq("q4_two_dice", ("Two fair dice are rolled together. How many outcomes are in the sample space?", "دو منصفانہ پانسے ایک ساتھ پھینکے جاتے ہیں۔ نمونی فضا میں کتنے نتائج ہیں؟"), Q5,
      ("Each dice has 6 outcomes: 6 × 6.", "ہر پانسے کے 6 نتائج ہیں: 6 × 6"),
      ("Right! 6 × 6 = 36 outcomes.", "درست! 6 × 6 = 36 نتائج"), ("For each of the 6 faces of the first dice there are 6 faces of the second: 36.", "پہلے پانسے کے ہر رخ کے لیے دوسرے کے 6 رخ ہیں: 36"),
      [(12, "12 is 6 + 6. The dice multiply: 6 × 6 = 36.", "12 یعنی 6 + 6۔ پانسوں کے نتائج ضرب ہوتے ہیں: 6 × 6 = 36", "space_miscount"),
       (6, "6 is the outcomes of one dice. Two dice: 36.", "6 ایک پانسے کے نتائج ہیں۔ دو پانسے: 36", "space_miscount")]),
   with_fig(pq("q5_dice", ("A fair dice is rolled once. What is the probability that the number is more than 4? Write it as a fraction.", "ایک منصفانہ پانسہ ایک بار پھینکا جاتا ہے۔ عدد 4 سے بڑا آنے کا احتمال کیا ہے؟ کسر کی شکل میں لکھیں۔"), Q6,
      ("The numbers more than 4 are 5 and 6. Out of 6.", "4 سے بڑے اعداد 5 اور 6 ہیں۔ کل 6 میں سے۔"),
      ("Right! n(E) = 2 (the numbers 5 and 6), n(S) = 6, so P = 2/6 = 1/3.", "درست! n(E) = 2 (اعداد 5 اور 6)، n(S) = 6، تو P = 2/6 = 1/3"), ("2 favourable outcomes out of 6: 2/6 = 1/3.", "6 میں سے 2 مطلوبہ نتائج: 2/6 = 1/3"),
      [("3/6", "3/6 counts the 4 as well. 'More than 4' starts at 5: 2/6 = 1/3.", "3/6 میں 4 بھی گنا گیا۔ '4 سے بڑا' 5 سے شروع ہوتا ہے: 2/6 = 1/3", "event_miscount"),
       ("6/2", "6/2 is upside down. P = n(E) ÷ n(S) = 2/6 = 1/3.", "6/2 الٹا ہے۔ P = n(E) ÷ n(S) = 2/6 = 1/3", "upside_down")], qtype="recall"), F_DICE),
   with_fig(pq("q6_bag", ("A bag has 4 red, 3 blue and 5 green balls (R, B, G on the picture). One ball is taken out at random. What is the probability that it is green?", "ایک تھیلے میں 4 سرخ، 3 نیلی اور 5 سبز گیندیں ہیں (تصویر میں R، B، G)۔ ایک گیند بغیر دیکھے نکالی جاتی ہے۔ اس کے سبز ہونے کا احتمال کیا ہے؟"), Q7,
      ("Green balls over all balls in the bag.", "سبز گیندیں تقسیم تھیلے کی تمام گیندیں۔"),
      ("Right! 4 + 3 + 5 = 12 balls, 5 are green: P = 5/12.", "درست! 4 + 3 + 5 = 12 گیندیں، 5 سبز ہیں: P = 5/12"), ("n(E) = 5 and n(S) = 12.", "n(E) = 5 اور n(S) = 12"),
      [("5/7", "5/7 divides by the 7 balls that are not green. Divide by all 12: 5/12.", "5/7 میں 7 غیر سبز گیندوں سے تقسیم کیا گیا۔ تمام 12 سے تقسیم کریں: 5/12", "part_to_part"),
       ("12/5", "12/5 is upside down. P = 5/12.", "12/5 الٹا ہے۔ P = 5/12", "upside_down")]), F_BAG),
   with_fig(pq("q7_cards", ("The letters of the word PLANET are written on six cards, one letter on each. One card is picked at random. What is the probability that it is a vowel?", "لفظ PLANET کے حروف چھ کارڈوں پر لکھے ہیں، ہر کارڈ پر ایک حرف۔ ایک کارڈ بغیر دیکھے اٹھایا جاتا ہے۔ اس کے حرفِ علت ہونے کا احتمال کیا ہے؟"), Q8,
      ("The vowels are A and E. Count all the cards.", "حروفِ علت A اور E ہیں۔ تمام کارڈ گنیں۔"),
      ("Right! 2 vowels out of 6 cards: 2/6 = 1/3.", "درست! 6 کارڈوں میں سے 2 حروفِ علت: 2/6 = 1/3"), ("n(E) = 2 and n(S) = 6.", "n(E) = 2 اور n(S) = 6"),
      [("2/4", "2/4 divides by the 4 consonants. Divide by all 6 cards: 2/6 = 1/3.", "2/4 میں 4 حروفِ صحیح سے تقسیم کیا گیا۔ تمام 6 کارڈوں سے تقسیم کریں: 2/6 = 1/3", "part_to_part"),
       ("4/6", "4/6 counts the consonants. The vowels are A and E: 2/6 = 1/3.", "4/6 میں حروفِ صحیح گنے گئے۔ حروفِ علت A اور E ہیں: 2/6 = 1/3", "event_miscount")]), F_CARDS),
   with_fig(pq("q8_one_head", ("Two fair coins are tossed. What is the probability of getting exactly one head?", "دو منصفانہ سکے اچھالے جاتے ہیں۔ ٹھیک ایک چت آنے کا احتمال کیا ہے؟"), Q9,
      ("List the outcomes with exactly one H. There are two ways.", "ٹھیک ایک H والے نتائج لکھیں۔ دو طریقے ہیں۔"),
      ("Right! HT and TH are two of the four outcomes: 2/4 = 1/2.", "درست! HT اور TH چار میں سے دو نتائج ہیں: 2/4 = 1/2"), ("n(E) = 2 and n(S) = 4.", "n(E) = 2 اور n(S) = 4"),
      [("1/4", "1/4 counts only HT. TH also has exactly one head: 2/4 = 1/2.", "1/4 میں صرف HT گنا گیا۔ TH میں بھی ٹھیک ایک چت ہے: 2/4 = 1/2", "one_way_only"),
       ("1/3", "1/3 treats HT and TH as one outcome out of three. There are 4 outcomes: 2/4 = 1/2.", "1/3 میں HT اور TH کو ایک نتیجہ مان کر تین میں سے لیا گیا۔ نتائج 4 ہیں: 2/4 = 1/2", "one_way_only")]), F_TABLE),
   ch("q9_equal", ("Which of these has equally likely outcomes?", "ان میں سے کس کے نتائج یکساں امکان کے ہیں؟"),
      ("rolling a fair dice and looking at the number", "منصفانہ پانسہ پھینک کر عدد دیکھنا", "Yes! Each face is as likely as any other.", "جی ہاں! ہر رخ دوسرے رخ جتنا ممکن ہے۔"),
      [("taking a ball from a bag with 1 red ball and 9 blue balls and looking at the colour", "1 سرخ اور 9 نیلی گیندوں والے تھیلے سے ایک گیند نکال کر رنگ دیکھنا", "Blue is far more likely than red, so the colours are not equally likely.", "نیلی سرخ سے کہیں زیادہ ممکن ہے، تو رنگ یکساں امکان کے نہیں۔", "equally_likely_mix"),
       ("a bag with 2 red and 6 blue balls: red or blue", "2 سرخ اور 6 نیلی گیندوں والا تھیلا: سرخ یا نیلی", "There are three times as many blue balls, so the colours are not equally likely.", "نیلی گیندیں تین گنا ہیں، تو رنگ یکساں امکان کے نہیں۔", "equally_likely_mix"),
       ("a spinner where one part takes up half the circle", "ایک چکر جس میں ایک حصہ آدھا دائرہ گھیرتا ہے", "The big part is more likely, so the parts are not equally likely.", "بڑا حصہ زیادہ ممکن ہے، تو حصے یکساں امکان کے نہیں۔", "equally_likely_mix")],
      1, qtype="apply"),
   pq("q10_sum7", ("Two fair dice are rolled. What is the probability that the sum of the two numbers is 7? Write it as a fraction.", "دو منصفانہ پانسے پھینکے جاتے ہیں۔ دونوں اعداد کا مجموعہ 7 آنے کا احتمال کیا ہے؟ کسر کی شکل میں لکھیں۔"), Q11,
      ("List the pairs that add to 7: (1,6), (2,5), ... Out of 36.", "7 بنانے والے جوڑے لکھیں: (1,6)، (2,5)، ... کل 36 میں سے۔"),
      ("Right! The pairs are (1,6), (2,5), (3,4), (4,3), (5,2), (6,1): 6 of 36, so 6/36 = 1/6.", "درست! جوڑے (1,6)، (2,5)، (3,4)، (4,3)، (5,2)، (6,1) ہیں: 36 میں سے 6، تو 6/36 = 1/6"), ("n(E) = 6 and n(S) = 36.", "n(E) = 6 اور n(S) = 36"),
      [("3/36", "3/36 counts only (1,6), (2,5), (3,4). (6,1), (5,2) and (4,3) are different outcomes too: 6/36 = 1/6.", "3/36 میں صرف (1,6)، (2,5)، (3,4) گنے گئے۔ (6,1)، (5,2) اور (4,3) بھی الگ نتائج ہیں: 6/36 = 1/6", "one_way_only"),
       ("1/12", "1/12 uses 12 outcomes (6 + 6). Two dice have 36 outcomes: 6/36 = 1/6.", "1/12 میں 12 نتائج (6 + 6) لیے گئے۔ دو پانسوں کے 36 نتائج ہیں: 6/36 = 1/6", "space_miscount")]),
   pq("q11_raffle", (f"In a raffle {TICKETS} tickets are sold, and Sana bought {MINE} of them. One ticket is drawn at random. What is the probability that Sana wins?", f"ایک لکی ڈرا میں {TICKETS} ٹکٹ بکتے ہیں، اور ثناء نے ان میں سے {MINE} خریدے۔ ایک ٹکٹ بغیر دیکھے نکالا جاتا ہے۔ ثناء کے جیتنے کا احتمال کیا ہے؟"), Q12,
      ("Her tickets over all the tickets.", "اس کے ٹکٹ تقسیم تمام ٹکٹ۔"),
      ("Right! 5 of the 40 tickets: 5/40 = 1/8.", "درست! 40 ٹکٹوں میں سے 5: 5/40 = 1/8"), ("5 ÷ 5 = 1 and 40 ÷ 5 = 8.", "5 ÷ 5 = 1 اور 40 ÷ 5 = 8"),
      [("5/35", "5/35 compares her tickets with the 35 other tickets. Divide by all 40: 5/40 = 1/8.", "5/35 میں اس کے ٹکٹوں کا باقی 35 سے موازنہ کیا گیا۔ تمام 40 سے تقسیم کریں: 5/40 = 1/8", "part_to_part"),
       ("40/5", "40/5 is upside down. P = 5/40 = 1/8.", "40/5 الٹا ہے۔ P = 5/40 = 1/8", "upside_down")]),
   nq("q12_how_many", (f"A bag has {Q14_N} marbles. The probability of taking out a green marble at random is 1/6. How many green marbles are in the bag?", f"ایک تھیلے میں {Q14_N} کنچے ہیں۔ بغیر دیکھے سبز کنچہ نکلنے کا احتمال 1/6 ہے۔ تھیلے میں کتنے سبز کنچے ہیں؟"), Q14,
      ("P = green ÷ 24, so green = 1/6 of 24.", "P = سبز ÷ 24، تو سبز = 24 کا 1/6"),
      ("Right! 1/6 of 24 is 24 ÷ 6 = 4 green marbles.", "درست! 24 کا 1/6 یعنی 24 ÷ 6 = 4 سبز کنچے"), ("24 ÷ 6 = 4, and 4/24 = 1/6.", "24 ÷ 6 = 4، اور 4/24 = 1/6"),
      [(6, "6 is the bottom of the fraction. Green is 1/6 of 24: 4.", "6 کسر کا نچلا عدد ہے۔ سبز 24 کا 1/6 ہے: 4", "upside_down"),
       (18, "18 is 24 − 6. Green is 1/6 of 24: 24 ÷ 6 = 4.", "18 یعنی 24 − 6۔ سبز 24 کا 1/6 ہے: 24 ÷ 6 = 4", "part_to_part")]),
   with_fig(ch("q13_find_error", ("A bag has 3 red and 5 blue balls. Faisal says: the probability of red is 3/5. What went wrong?", "ایک تھیلے میں 3 سرخ اور 5 نیلی گیندیں ہیں۔ فیصل کہتا ہے: سرخ کا احتمال 3/5 ہے۔ کیا غلطی ہوئی؟"),
      ("He divided by the 5 blue balls. He should divide by all 8 balls: P(red) = 3/8.", "اس نے 5 نیلی گیندوں سے تقسیم کیا۔ اسے تمام 8 گیندوں سے تقسیم کرنا چاہیے: P(سرخ) = 3/8", "Yes! The bottom number is all the outcomes: 3 + 5 = 8.", "جی ہاں! نچلا عدد تمام نتائج ہیں: 3 + 5 = 8"),
      [("Nothing. 3/5 is right.", "کوئی غلطی نہیں۔ 3/5 ٹھیک ہے۔", "3/5 compares red with blue. Probability compares red with all the balls.", "3/5 سرخ کا نیلی سے موازنہ ہے۔ احتمال سرخ کا تمام گیندوں سے موازنہ ہے۔", "part_to_part"),
       ("He should write 5/3.", "اسے 5/3 لکھنا چاہیے۔", "5/3 is more than 1, and no probability is more than 1.", "5/3، 1 سے بڑا ہے، اور کوئی احتمال 1 سے بڑا نہیں ہوتا۔", "upside_down")],
      1, qtype="find_error"), F_BAG_QB),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! You can find the chance of an event.", "شاباش! آپ کسی واقعے کا امکان نکال سکتے ہیں۔"),
    "text": T("List the sample space first: one coin 2 outcomes, two coins 4, three coins 8, one dice 6, two dice 36. P(E) = n(E) ÷ n(S), the outcomes you want over all the outcomes, never over the other outcomes. Count every way: HT and TH are different. A fair coin or dice has equally likely outcomes; a bag with unequal numbers of colours does not. P = 0 is impossible, P = 1 is certain.",
              "پہلے نمونی فضا لکھیں: ایک سکے کے 2 نتائج، دو سکوں کے 4، تین سکوں کے 8، ایک پانسے کے 6، دو پانسوں کے 36۔ P(E) = n(E) ÷ n(S)، یعنی مطلوبہ نتائج تقسیم تمام نتائج، کبھی باقی نتائج سے نہیں۔ ہر طریقہ گنیں: HT اور TH الگ ہیں۔ منصفانہ سکے یا پانسے کے نتائج یکساں امکان کے ہوتے ہیں؛ مختلف تعداد کے رنگوں والے تھیلے کے نہیں۔ P = 0 ناممکن، P = 1 یقینی ہے۔"),
    "points": [T("P(E) = n(E) ÷ n(S).", "P(E) = n(E) ÷ n(S)"),
               T("Divide by all the outcomes, not the others.", "تمام نتائج سے تقسیم کریں، باقی سے نہیں۔")]},
 ],
 bank=[
   {"id": "qb_recall", "type": "recall", "step": ch("qb_recall", ("What is the formula for the probability of an event E?", "واقعہ E کے احتمال کا کلیہ کیا ہے؟"),
      ("P(E) = n(E) ÷ n(S)", "P(E) = n(E) ÷ n(S)", "Yes! The outcomes you want over all the outcomes.", "جی ہاں! مطلوبہ نتائج تقسیم تمام نتائج۔"),
      [("P(E) = n(S) ÷ n(E)", "P(E) = n(S) ÷ n(E)", "That is upside down.", "یہ الٹا ہے۔", "upside_down"),
       ("P(E) = n(E) ÷ the number of other outcomes", "P(E) = n(E) ÷ باقی نتائج کی تعداد", "Divide by all the outcomes, not only the others.", "تمام نتائج سے تقسیم کریں، صرف باقی سے نہیں۔", "part_to_part")],
      0, qtype=None)},
   {"id": "qb_dice", "type": "apply", "step": with_fig(pq("qb_dice", ("A fair dice is rolled once. What is the probability that the number is 1, 2 or 3? Write it as a fraction.", "ایک منصفانہ پانسہ ایک بار پھینکا جاتا ہے۔ عدد 1، 2 یا 3 آنے کا احتمال کیا ہے؟ کسر کی شکل میں لکھیں۔"), QB_DICE,
      ("Three favourable numbers out of 6.", "6 میں سے تین مطلوبہ اعداد۔"),
      ("Right! 3/6 = 1/2.", "درست! 3/6 = 1/2"), ("n(E) = 3 and n(S) = 6.", "n(E) = 3 اور n(S) = 6"),
      [("3/3", "3/3 divides by the 3 numbers not wanted. Divide by all 6: 3/6 = 1/2.", "3/3 میں غیر مطلوبہ 3 اعداد سے تقسیم کیا گیا۔ تمام 6 سے تقسیم کریں: 3/6 = 1/2", "part_to_part"),
       ("6/3", "6/3 is upside down. P = 3/6 = 1/2.", "6/3 الٹا ہے۔ P = 3/6 = 1/2", "upside_down")], qtype=None), F_DICE)},
   {"id": "qb_cards", "type": "apply", "step": pq("qb_cards", ("The letters of the word RIVER are on five cards. One card is picked at random. What is the probability that it is a vowel?", "لفظ RIVER کے حروف پانچ کارڈوں پر ہیں۔ ایک کارڈ بغیر دیکھے اٹھایا جاتا ہے۔ اس کے حرفِ علت ہونے کا احتمال کیا ہے؟"), QB3,
      ("The vowels are I and E.", "حروفِ علت I اور E ہیں۔"),
      ("Right! 2 vowels out of 5 cards: 2/5.", "درست! 5 کارڈوں میں سے 2 حروفِ علت: 2/5"), ("n(E) = 2 and n(S) = 5.", "n(E) = 2 اور n(S) = 5"),
      [("2/3", "2/3 divides by the 3 consonants. Divide by all 5 cards: 2/5.", "2/3 میں 3 حروفِ صحیح سے تقسیم کیا گیا۔ تمام 5 کارڈوں سے تقسیم کریں: 2/5", "part_to_part")], qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": ch("qb_find_error", ("Rabia says: when two coins are tossed there are 3 outcomes, HH, HT and TT. What went wrong?", "ربیعہ کہتی ہے: دو سکے اچھالنے پر 3 نتائج ہوتے ہیں، HH، HT اور TT۔ کیا غلطی ہوئی؟"),
      ("She left out TH. HT and TH are different outcomes, so there are 4.", "اس نے TH چھوڑ دیا۔ HT اور TH الگ نتائج ہیں، تو 4 ہیں۔", "Yes! The first coin can be H or T, and so can the second: 2 × 2 = 4.", "جی ہاں! پہلا سکہ H یا T ہو سکتا ہے، اور دوسرا بھی: 2 × 2 = 4"),
      [("Nothing. 3 is right.", "کوئی غلطی نہیں۔ 3 ٹھیک ہے۔", "HT (head then tail) and TH (tail then head) are not the same.", "HT (پہلے چت پھر پٹ) اور TH (پہلے پٹ پھر چت) ایک جیسے نہیں۔", "one_way_only"),
       ("There are 2 outcomes, H and T.", "2 نتائج ہیں، H اور T۔", "That is for one coin. Two coins give 4.", "یہ ایک سکے کے لیے ہے۔ دو سکوں کے 4 ہیں۔", "space_miscount")],
      0, qtype=None)},
 ],
 review=[
   {"id": "r_impossible", "type": "apply", "step": pq("r_impossible", ("A fair dice is rolled once. What is the probability that the number is 7? Write it as a fraction or a number.", "ایک منصفانہ پانسہ ایک بار پھینکا جاتا ہے۔ عدد 7 آنے کا احتمال کیا ہے؟ کسر یا عدد کی شکل میں لکھیں۔"), R1,
      ("Is there any face with 7?", "کیا کسی رخ پر 7 ہے؟"),
      ("Right! No face shows 7, so n(E) = 0 and P = 0/6 = 0. It is impossible.", "درست! کسی رخ پر 7 نہیں، تو n(E) = 0 اور P = 0/6 = 0۔ یہ ناممکن ہے۔"), ("0 favourable outcomes: P = 0.", "0 مطلوبہ نتائج: P = 0"),
      [("1/6", "1/6 would be for one face, like 6. There is no face with 7: 0.", "1/6 ایک رخ کا ہوتا، جیسے 6 کا۔ 7 والا کوئی رخ نہیں: 0", "event_miscount")], qtype=None)},
   {"id": "r_blue", "type": "apply", "step": pq("r_blue", ("A bag has 5 red, 3 blue and 2 green balls. One ball is taken out at random. What is the probability that it is blue?", "ایک تھیلے میں 5 سرخ، 3 نیلی اور 2 سبز گیندیں ہیں۔ ایک گیند بغیر دیکھے نکالی جاتی ہے۔ اس کے نیلی ہونے کا احتمال کیا ہے؟"), R3,
      ("Blue balls over all balls.", "نیلی گیندیں تقسیم تمام گیندیں۔"),
      ("Right! 5 + 3 + 2 = 10 balls, 3 are blue: 3/10.", "درست! 5 + 3 + 2 = 10 گیندیں، 3 نیلی ہیں: 3/10"), ("n(E) = 3 and n(S) = 10.", "n(E) = 3 اور n(S) = 10"),
      [("3/7", "3/7 divides by the 7 balls that are not blue. Divide by all 10: 3/10.", "3/7 میں 7 غیر نیلی گیندوں سے تقسیم کیا گیا۔ تمام 10 سے تقسیم کریں: 3/10", "part_to_part")], qtype=None)},
 ],
 glossary=[T("Experiment", "تجربہ"), T("Outcome", "نتیجہ"), T("Sample space", "نمونی فضا"), T("Event", "واقعہ"),
           T("Probability", "احتمال"), T("Equally likely", "یکساں امکان"), T("Fair coin", "منصفانہ سکہ"), T("At random", "بغیر دیکھے / اتفاقاً")],
 flashcards=[
   {"id": "f_formula", "front": T("How do you find the probability of an event?", "کسی واقعے کا احتمال کیسے نکالتے ہیں؟"),
    "back": T("P(E) = n(E) ÷ n(S): the outcomes you want over all the outcomes.", "P(E) = n(E) ÷ n(S): مطلوبہ نتائج تقسیم تمام نتائج۔")},
   {"id": "f_spaces", "front": T("How many outcomes do two coins, three coins and two dice have?", "دو سکوں، تین سکوں اور دو پانسوں کے کتنے نتائج ہوتے ہیں؟"),
    "back": T("Two coins 4, three coins 8, two dice 36.", "دو سکوں کے 4، تین سکوں کے 8، دو پانسوں کے 36")},
 ],
 home_task={"id": "h_probability", "text": T(
   "Toss two coins 40 times and write down HH, HT, TH or TT each time. Count how many times you got exactly one head. Compare the fraction you got with 1/2, the probability you worked out. Are they close?",
   "دو سکے 40 بار اچھالیں اور ہر بار HH، HT، TH یا TT لکھیں۔ گنیں کہ کتنی بار ٹھیک ایک چت آئی۔ اپنی کسر کا موازنہ 1/2 سے کریں، جو احتمال آپ نے نکالا تھا۔ کیا یہ قریب ہیں؟")},
 notes=["Covers the sample space of one, two and three coins and of two dice (q1 to q4, qb_find_error), the probability of an event with a dice, a bag of balls and letter cards (q5 to q7, qb_dice, qb_cards, r_blue), two coins and two dice (q8, q10), equally likely outcomes (q9), a raffle word problem and working back from a probability (q11, q12), P = 0 (r_impossible) and the common mistake of dividing by the other outcomes (q13).",
        "Each wrong answer is a real mistake: adding instead of multiplying for two coins or two dice, writing the fraction upside down, dividing by the other outcomes, counting only one way (HT but not TH), and including the boundary number in 'more than 4'.",
        "Typed probabilities use the fraction checker without 'simplest form', as in the existing probability lessons, so 2/6, 1/3 and 0.5-style decimals of the same value are all right. Figure labels are single letters or numbers; the step text says what they stand for.",
        "Urdu terms to check: تجربہ, نتیجہ, نمونی فضا, واقعہ, احتمال, یکساں امکان, منصفانہ سکہ and لکی ڈرا, all as in the existing Probability lessons. حرفِ علت (vowel) and حرفِ صحیح (consonant), چت / پٹ (heads / tails) and کنچے (marbles) are everyday words used here, and a teacher should confirm them."],
 minutes=20,
)
write(lesson)
