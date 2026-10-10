"""Chapter 12 test (Probability), set out like the book's review exercise and a
board paper: multiple choice, short questions, then longer problems. The
questions are new; only the kinds of question follow the book."""
from fractions import Fraction as F

from common import (T, say, nq, pq, ch, write, book_ref, REVIEW, CHAPTER_12_TEST, coins, balls, P, DICE, VOWELS,
                    PR_SAMPLE_SPACE, PR_SINGLE_EVENT, PR_LIKELIHOOD, PR_WORD_PROBLEMS)
from figs import bag, cards, key, with_fig

SKILL = CHAPTER_12_TEST
TWO_DICE = [(a, b) for a in DICE for b in DICE]


def mcq(id, en, ur, right, wrongs, pos):
    return ch(id, ("MCQ: " + en, "کثیر انتخابی: " + ur), right, wrongs, pos, qtype="exam_style")


def short(id, en, ur, answer, hint, good, bad, wrongs=()):
    return pq(id, ("Short question: " + en, "مختصر سوال: " + ur), answer, hint, good, bad, wrongs, qtype="exam_style")


def long_p(id, en, ur, answer, hint, good, bad, wrongs=()):
    return pq(id, ("Long question: " + en, "تفصیلی سوال: " + ur), answer, hint, good, bad, wrongs, qtype="exam_style")


def long_n(id, en, ur, answer, hint, good, bad, wrongs=()):
    return nq(id, ("Long question: " + en, "تفصیلی سوال: " + ur), answer, hint, good, bad, wrongs, qtype="exam_style")


# MCQs
M1 = len(coins(1)) * len(DICE)
assert M1 == 12 and 2 + 6 == 8
M3_BAG = balls(red=5, blue=3)
M3 = P(lambda o: o == "blue", M3_BAG)
assert M3 == F(3, 8) and F(3, 5) != M3 and F(5, 8) != M3
M3_FIG = bag(M3_BAG, key("blue", "red"))
assert P(lambda o: o in DICE, DICE) == 1 and P(lambda o: o == 9, DICE) == 0 and F(5, 4) > 1
assert coins(2) == ["HH", "HT", "TH", "TT"]
M5_BAG = balls(white=1, black=7)
assert M5_BAG.count("white") != M5_BAG.count("black")

# short questions
S1 = P(lambda o: o in (2, 3, 5), DICE)
assert S1 == F(1, 2) and F(3, 3) != S1
S2 = P(lambda o: o == "TTT", coins(3))
assert S2 == F(1, 8) and len(coins(3)) == 8 and F(1, 3) != S2
WORD = "KARACHI"
S3 = P(lambda o: o in VOWELS, WORD)
assert S3 == F(3, 7) and sum(1 for o in WORD if o in VOWELS) == 3 and F(3, 4) != S3 and F(1, 7) != S3
S3_FIG = cards(WORD)
S4 = F(sum(1 for a, b in TWO_DICE if a == b), len(TWO_DICE))
assert S4 == F(1, 6) and F(1, 36) != S4

# long questions
L1_BAG = balls(red=6, blue=9, green=5)
L1 = P(lambda o: o != "blue", L1_BAG)
assert len(L1_BAG) == 20 and L1 == F(11, 20) and P(lambda o: o == "blue", L1_BAG) == F(9, 20) and F(11, 9) != L1
L2_N, L2_RED, L2_BLUE = 30, F(2, 5), F(1, 3)
L2_R, L2_B = L2_RED * L2_N, L2_BLUE * L2_N
assert L2_R == 12 and L2_B == 10 and L2_R.denominator == 1 and L2_B.denominator == 1
L2 = int(L2_N - L2_R - L2_B)
assert L2 == 8 and L2 != int(L2_R) and L2 != int(L2_B)
COIN_DICE = [(c, d) for c in ("H", "T") for d in DICE]
L3 = F(sum(1 for c, d in COIN_DICE if c == "H" and d % 2 == 0), len(COIN_DICE))
assert len(COIN_DICE) == 12 and L3 == F(1, 4) and F(1, 2) != L3 and F(1, 12) != L3
L4_N = sum(1 for a, b in TWO_DICE if a + b >= 9)
L4 = F(L4_N, len(TWO_DICE))
assert L4_N == 10 and L4 == F(5, 18) and sum(1 for a, b in TWO_DICE if a + b > 9) == 6 and F(6, 36) != L4 and F(10, 12) != L4

# question bank and review
QB1 = P(lambda o: o == 3, DICE)
assert QB1 == F(1, 6)
QB2 = len(coins(2))
assert QB2 == 4
QB3 = P(lambda o: o == "red", balls(red=2, blue=8))
assert QB3 == F(1, 5)
R1 = P(lambda o: o % 2 == 1, DICE)
assert R1 == F(1, 2)
R2 = P(lambda o: o == "H", ["H", "T"])
assert R2 == F(1, 2)

lesson = {
 "id": "g6-maths-17-chapter-12-test",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Answer exam-style questions on the whole of chapter 12: experiments and sample spaces, equally likely events, and the probability of a single event with coins, dice, cards and balls.",
                      "textbook": book_ref("Review Exercise 12")}],
 "skills": [SKILL],
 "title": T("Chapter 12 test: Probability", "باب 12 کا ٹیسٹ: احتمال"),
 "estimated_minutes": 25,
 "prerequisites": [{"skill": s} for s in (PR_SAMPLE_SPACE, PR_SINGLE_EVENT, PR_LIKELIHOOD, PR_WORD_PROBLEMS)],
 "misconceptions": [
   {"id": "space_miscount", "description": "Counts the outcomes of a coin and a dice, two coins or two dice wrongly, for example by adding instead of multiplying."},
   {"id": "upside_down", "description": "Writes n(S) / n(E) instead of n(E) / n(S), or gives a probability more than 1."},
   {"id": "part_to_part", "description": "Divides by the other outcomes (3 blue to 5 red) instead of by all the outcomes."},
   {"id": "event_miscount", "description": "Counts the favourable outcomes wrongly, for example including or leaving out the boundary value."},
   {"id": "equally_likely_mix", "description": "Thinks the outcomes of a bag with different numbers of each colour are equally likely."},
   {"id": "one_way_only", "description": "Counts only one way of getting an outcome of two coins or two dice."},
   {"id": "answer_is_other_quantity", "description": "Stops at a middle step, such as the number of one colour of ball, and gives it as the answer."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["exam_style"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_exam_dice", "type": "exam_style", "step": pq(
     "qb_exam_dice", ("A fair dice is rolled once. What is the probability that the number is 3? Write it as a fraction.", "ایک منصفانہ پانسہ ایک بار پھینکا جاتا ہے۔ عدد 3 آنے کا احتمال کیا ہے؟ کسر کی شکل میں لکھیں۔"), QB1,
     ("One face out of 6.", "6 میں سے ایک رخ۔"),
     ("Correct: 1/6.", "درست: 1/6"), ("n(E) = 1 and n(S) = 6.", "n(E) = 1 اور n(S) = 6"),
     [("6/1", "6/1 is upside down. P = 1/6.", "6/1 الٹا ہے۔ P = 1/6", "upside_down")], qtype=None)},
   {"id": "qb_exam_coins", "type": "exam_style", "step": nq(
     "qb_exam_coins", ("Two coins are tossed together. How many outcomes are in the sample space?", "دو سکے ایک ساتھ اچھالے جاتے ہیں۔ نمونی فضا میں کتنے نتائج ہیں؟"), QB2,
     ("HH, HT, TH, TT.", "HH، HT، TH، TT"),
     ("Correct: 2 × 2 = 4.", "درست: 2 × 2 = 4"), ("Four outcomes.", "چار نتائج"),
     [(3, "3 leaves out one of HT and TH. They are different: 4.", "3 میں HT یا TH میں سے ایک چھوٹ گیا۔ یہ الگ ہیں: 4", "one_way_only")], qtype=None)},
   {"id": "qb_exam_bag", "type": "exam_style", "step": pq(
     "qb_exam_bag", ("A bag has 2 red and 8 blue balls. One ball is taken out at random. What is the probability that it is red?", "ایک تھیلے میں 2 سرخ اور 8 نیلی گیندیں ہیں۔ ایک گیند بغیر دیکھے نکالی جاتی ہے۔ اس کے سرخ ہونے کا احتمال کیا ہے؟"), QB3,
     ("Red over all the balls.", "سرخ تقسیم تمام گیندیں۔"),
     ("Correct: 2/10 = 1/5.", "درست: 2/10 = 1/5"), ("n(E) = 2 and n(S) = 10.", "n(E) = 2 اور n(S) = 10"),
     [("2/8", "2/8 divides by the 8 blue balls. Divide by all 10: 1/5.", "2/8 میں 8 نیلی گیندوں سے تقسیم کیا گیا۔ تمام 10 سے تقسیم کریں: 1/5", "part_to_part")], qtype=None)},
 ]},
 "flashcards": [
   {"id": "f_formula", "front": T("Probability of an event?", "واقعے کا احتمال؟"),
    "back": T("P(E) = n(E) ÷ n(S): the outcomes you want over all the outcomes. It is always from 0 to 1.", "P(E) = n(E) ÷ n(S): مطلوبہ نتائج تقسیم تمام نتائج۔ یہ ہمیشہ 0 سے 1 کے درمیان ہوتا ہے۔")},
   {"id": "f_spaces", "front": T("Outcomes of two coins, a coin and a dice, two dice?", "دو سکوں، سکے اور پانسے، دو پانسوں کے نتائج؟"),
    "back": T("4, 12 and 36: multiply the outcomes of each.", "4، 12 اور 36: ہر ایک کے نتائج کو ضرب دیں۔")},
 ],
 "home_tasks": [{"id": "h_paper", "text": T(
   "Do Review Exercise 12 in your maths book in your notebook, setting out the working the way this test's answers do: list the sample space, count n(E) and n(S), then write P(E) = n(E) ÷ n(S) in its simplest form. Ask your teacher to check it.",
   "اپنی ریاضی کی کتاب کی اعادی مشق 12 اپنی کاپی میں حل کریں، اور کام اس ٹیسٹ کے جوابات کی طرح لکھیں: نمونی فضا لکھیں، n(E) اور n(S) گنیں، پھر P(E) = n(E) ÷ n(S) کو سادہ ترین شکل میں لکھیں۔ اپنے استاد سے جانچ کروائیں۔")}],
 "glossary": [T("Multiple choice", "کثیر انتخابی"), T("Short question", "مختصر سوال"), T("Long question", "تفصیلی سوال"),
              T("Model answer", "نمونہ جواب"), T("Review exercise", "اعادی مشق")],
 "steps": [
   {"id": "s1_paper", "type": "explain",
    "character": say("encouraging", "This is a test of the whole chapter, like the book's review exercise. Read each question carefully!",
                     "یہ پورے باب کا ٹیسٹ ہے، کتاب کی اعادی مشق کی طرح۔ ہر سوال غور سے پڑھیں!"),
    "text": T("This test goes with Review Exercise 12 of your maths book (PCTB Mathematics 6). It has three parts, like an exam paper: multiple choice questions (choose one answer), short questions (a few lines of working), and longer problems (full working in your notebook, then the final answer). The questions are new, not the book's. Type probabilities as fractions, like 1/6.",
              "یہ ٹیسٹ آپ کی ریاضی کی کتاب (پنجاب ٹیکسٹ بک بورڈ، ریاضی 6) کی اعادی مشق 12 کے ساتھ ہے۔ اس کے تین حصے ہیں، امتحانی پرچے کی طرح: کثیر انتخابی سوال (ایک جواب چنیں)، مختصر سوال (چند سطروں کا کام)، اور تفصیلی سوالات (کاپی میں پورا کام، پھر آخری جواب)۔ سوال نئے ہیں، کتاب والے نہیں۔ احتمال کو کسر کی شکل میں لکھیں، جیسے 1/6۔")},
   mcq("m1_coin_dice", "A coin is tossed and a dice is rolled together. How many outcomes are in the sample space?", "ایک سکہ اچھالا جاتا ہے اور ایک پانسہ ساتھ پھینکا جاتا ہے۔ نمونی فضا میں کتنے نتائج ہیں؟",
       ("12", "12", "Correct: 2 × 6 = 12.", "درست: 2 × 6 = 12"),
       [("8", "8", "8 is 2 + 6. The outcomes multiply: 12.", "8 یعنی 2 + 6۔ نتائج ضرب ہوتے ہیں: 12", "space_miscount"),
        ("6", "6", "6 is the outcomes of the dice alone. With the coin: 12.", "6 صرف پانسے کے نتائج ہیں۔ سکے کے ساتھ: 12", "space_miscount"),
        ("36", "36", "36 is for two dice. A coin has 2 outcomes: 2 × 6 = 12.", "36 دو پانسوں کا ہے۔ سکے کے 2 نتائج ہیں: 2 × 6 = 12", "space_miscount")], 1),
   mcq("m2_impossible", "The probability of an event that can never happen is:", "ایسے واقعے کا احتمال جو کبھی نہیں ہو سکتا:",
       ("0", "0", "Correct: an impossible event has n(E) = 0, so P = 0.", "درست: ناممکن واقعے میں n(E) = 0 ہوتا ہے، تو P = 0"),
       [("1", "1", "P = 1 is a certain event, one that always happens.", "P = 1 یقینی واقعہ ہے، جو ہمیشہ ہوتا ہے۔", "upside_down"),
        ("1/2", "1/2", "1/2 is an even chance.", "1/2 برابر امکان ہے۔", "upside_down"),
        ("-1", "−1", "A probability is never below 0.", "احتمال کبھی 0 سے کم نہیں ہوتا۔", "upside_down")], 0),
   with_fig(mcq("m3_blue", "A bag has 5 red and 3 blue balls (R and B on the picture). One ball is taken out at random. The probability that it is blue is:", "ایک تھیلے میں 5 سرخ اور 3 نیلی گیندیں ہیں (تصویر میں R اور B)۔ ایک گیند بغیر دیکھے نکالی جاتی ہے۔ اس کے نیلی ہونے کا احتمال ہے:",
       ("3/8", "3/8", "Correct: 3 blue out of 8 balls.", "درست: 8 گیندوں میں سے 3 نیلی۔"),
       [("3/5", "3/5", "5 is the number of red balls. Divide by all 8.", "5 سرخ گیندوں کی تعداد ہے۔ تمام 8 سے تقسیم کریں۔", "part_to_part"),
        ("5/8", "5/8", "5/8 is the probability of red.", "5/8 سرخ کا احتمال ہے۔", "event_miscount"),
        ("8/3", "8/3", "That is upside down, and bigger than 1.", "یہ الٹا ہے، اور 1 سے بڑا ہے۔", "upside_down")], 2), M3_FIG),
   mcq("m4_not_prob", "Which of these cannot be the probability of an event?", "ان میں سے کون سا کسی واقعے کا احتمال نہیں ہو سکتا؟",
       ("5/4", "5/4", "Correct: it is more than 1, and a probability is never more than 1.", "درست: یہ 1 سے بڑا ہے، اور احتمال کبھی 1 سے بڑا نہیں ہوتا۔"),
       [("3/4", "3/4", "3/4 is between 0 and 1, so it can be a probability.", "3/4، 0 اور 1 کے بیچ میں ہے، تو یہ احتمال ہو سکتا ہے۔", "upside_down"),
        ("0", "0", "0 is the probability of an impossible event.", "0 ناممکن واقعے کا احتمال ہے۔", "upside_down"),
        ("1", "1", "1 is the probability of a certain event.", "1 یقینی واقعے کا احتمال ہے۔", "upside_down")], 3),
   mcq("m5_not_equal", "In which case are the outcomes NOT equally likely?", "کس صورت میں نتائج یکساں امکان کے نہیں ہیں؟",
       ("taking a ball from a bag with 1 white and 7 black balls and noting the colour", "1 سفید اور 7 کالی گیندوں والے تھیلے سے گیند نکال کر رنگ دیکھنا", "Correct: black is seven times as likely as white.", "درست: کالی سفید سے سات گنا زیادہ ممکن ہے۔"),
       [("tossing a fair coin", "منصفانہ سکہ اچھالنا", "Heads and tails are equally likely.", "چت اور پٹ یکساں امکان کے ہیں۔", "equally_likely_mix"),
        ("rolling a fair dice", "منصفانہ پانسہ پھینکنا", "All six faces are equally likely.", "چھ کے چھ رخ یکساں امکان کے ہیں۔", "equally_likely_mix"),
        ("picking one of five different cards without looking", "پانچ مختلف کارڈوں میں سے ایک بغیر دیکھے اٹھانا", "Each card is as likely as any other.", "ہر کارڈ دوسرے جتنا ممکن ہے۔", "equally_likely_mix")], 0),
   mcq("m6_space", "The sample space of tossing two coins is:", "دو سکے اچھالنے کی نمونی فضا ہے:",
       ("{HH, HT, TH, TT}", "{HH, HT, TH, TT}", "Correct: four outcomes.", "درست: چار نتائج۔"),
       [("{HH, HT, TT}", "{HH, HT, TT}", "TH is missing. HT and TH are different outcomes.", "TH رہ گیا۔ HT اور TH الگ نتائج ہیں۔", "one_way_only"),
        ("{H, T}", "{H, T}", "That is for one coin.", "یہ ایک سکے کی ہے۔", "space_miscount"),
        ("{HH, TT}", "{HH, TT}", "HT and TH are missing.", "HT اور TH رہ گئے ہیں۔", "one_way_only")], 1),
   {"id": "s_short", "type": "explain",
    "text": T("Short questions. Work each one out in your notebook, then type the answer as a fraction.",
              "مختصر سوال۔ ہر ایک اپنی کاپی میں حل کریں، پھر جواب کسر کی شکل میں لکھیں۔")},
   short("q1_prime", "A fair dice is rolled once. Find the probability of a prime number.", "ایک منصفانہ پانسہ ایک بار پھینکا جاتا ہے۔ مفرد عدد آنے کا احتمال نکالیں۔",
      S1, ("The prime numbers on a dice are 2, 3 and 5.", "پانسے پر مفرد اعداد 2، 3 اور 5 ہیں۔"),
      ("Correct: 3/6 = 1/2.", "درست: 3/6 = 1/2"),
      ("Model answer: S = {1, 2, 3, 4, 5, 6}, n(S) = 6. E = {2, 3, 5}, n(E) = 3. P(E) = 3/6 = 1/2.", "نمونہ جواب: S = {1, 2, 3, 4, 5, 6}، n(S) = 6۔ E = {2, 3, 5}، n(E) = 3۔ P(E) = 3/6 = 1/2"),
      [("3/3", "3/3 divides by the 3 numbers that are not prime. Divide by all 6: 1/2.", "3/3 میں 3 غیر مفرد اعداد سے تقسیم کیا گیا۔ تمام 6 سے تقسیم کریں: 1/2", "part_to_part"),
       ("4/6", "4/6 counts 1 as prime too. 1 is not prime: 3/6 = 1/2.", "4/6 میں 1 کو بھی مفرد گنا گیا۔ 1 مفرد نہیں: 3/6 = 1/2", "event_miscount")]),
   short("q2_tails", "Three fair coins are tossed. Find the probability that all three show tails.", "تین منصفانہ سکے اچھالے جاتے ہیں۔ تینوں پر پٹ آنے کا احتمال نکالیں۔",
      S2, ("How many outcomes are there for three coins? Only one of them is TTT.", "تین سکوں کے کتنے نتائج ہیں؟ ان میں سے صرف ایک TTT ہے۔"),
      ("Correct: 1 out of 8, so 1/8.", "درست: 8 میں سے 1، تو 1/8"),
      ("Model answer: n(S) = 2 × 2 × 2 = 8. Only TTT has three tails, so n(E) = 1. P(E) = 1/8.", "نمونہ جواب: n(S) = 2 × 2 × 2 = 8۔ صرف TTT میں تین پٹ ہیں، تو n(E) = 1۔ P(E) = 1/8"),
      [("1/3", "1/3 uses 3 outcomes (one for each coin). Three coins have 8 outcomes: 1/8.", "1/3 میں 3 نتائج (ہر سکے کا ایک) لیے گئے۔ تین سکوں کے 8 نتائج ہیں: 1/8", "space_miscount"),
       ("8/1", "8/1 is upside down. P = 1/8.", "8/1 الٹا ہے۔ P = 1/8", "upside_down")]),
   with_fig(short("q3_cards", "The letters of the word KARACHI are written on seven cards, one letter on each. One card is picked at random. Find the probability that it shows a vowel.", "لفظ KARACHI کے حروف سات کارڈوں پر لکھے ہیں، ہر کارڈ پر ایک حرف۔ ایک کارڈ بغیر دیکھے اٹھایا جاتا ہے۔ اس پر حرفِ علت آنے کا احتمال نکالیں۔",
      S3, ("Count the vowels, including the letter that comes twice.", "حروفِ علت گنیں، اس حرف سمیت جو دو بار آیا ہے۔"),
      ("Correct: A, A and I make 3 vowels out of 7 cards: 3/7.", "درست: A، A اور I مل کر 7 کارڈوں میں سے 3 حروفِ علت ہیں: 3/7"),
      ("Model answer: n(S) = 7. The vowels are A, A, I, so n(E) = 3. P(E) = 3/7.", "نمونہ جواب: n(S) = 7۔ حروفِ علت A، A، I ہیں، تو n(E) = 3۔ P(E) = 3/7"),
      [("3/4", "3/4 divides by the 4 consonants. Divide by all 7 cards: 3/7.", "3/4 میں 4 حروفِ صحیح سے تقسیم کیا گیا۔ تمام 7 کارڈوں سے تقسیم کریں: 3/7", "part_to_part"),
       ("2/7", "2/7 counts the A once. Both cards with A are vowels: 3/7.", "2/7 میں A ایک بار گنا گیا۔ A والے دونوں کارڈ حروفِ علت ہیں: 3/7", "event_miscount")]), S3_FIG),
   short("q4_doubles", "Two fair dice are rolled. Find the probability that both show the same number.", "دو منصفانہ پانسے پھینکے جاتے ہیں۔ دونوں پر ایک ہی عدد آنے کا احتمال نکالیں۔",
      S4, ("The pairs are (1,1), (2,2), ... Out of 36.", "جوڑے (1,1)، (2,2)، ... ہیں۔ کل 36 میں سے۔"),
      ("Correct: 6 pairs out of 36, so 6/36 = 1/6.", "درست: 36 میں سے 6 جوڑے، تو 6/36 = 1/6"),
      ("Model answer: n(S) = 6 × 6 = 36. The pairs with the same number are (1,1), (2,2), (3,3), (4,4), (5,5), (6,6), so n(E) = 6. P(E) = 6/36 = 1/6.", "نمونہ جواب: n(S) = 6 × 6 = 36۔ ایک جیسے اعداد والے جوڑے (1,1)، (2,2)، (3,3)، (4,4)، (5,5)، (6,6) ہیں، تو n(E) = 6۔ P(E) = 6/36 = 1/6"),
      [("1/36", "1/36 counts only one pair. There are six: 6/36 = 1/6.", "1/36 میں صرف ایک جوڑا گنا گیا۔ چھ ہیں: 6/36 = 1/6", "one_way_only"),
       ("6/12", "6/12 uses 12 outcomes (6 + 6). Two dice have 36: 6/36 = 1/6.", "6/12 میں 12 نتائج (6 + 6) لیے گئے۔ دو پانسوں کے 36 ہیں: 6/36 = 1/6", "space_miscount")]),
   {"id": "s_long", "type": "explain",
    "text": T("Longer problems. Write the sample space, n(E), n(S) and full working in your notebook, then type the final answer.",
              "تفصیلی سوالات۔ اپنی کاپی میں نمونی فضا، n(E)، n(S) اور پورا کام لکھیں، پھر آخری جواب لکھیں۔")},
   long_p("l1_not_blue", "A bag has 6 red, 9 blue and 5 green balls. One ball is taken out at random. Find the probability that it is not blue.", "ایک تھیلے میں 6 سرخ، 9 نیلی اور 5 سبز گیندیں ہیں۔ ایک گیند بغیر دیکھے نکالی جاتی ہے۔ اس کے نیلی نہ ہونے کا احتمال نکالیں۔",
      L1, ("Not blue means red or green. Count them, and all the balls.", "نیلی نہ ہونے کا مطلب سرخ یا سبز ہے۔ انہیں اور تمام گیندوں کو گنیں۔"),
      ("Correct: 6 + 5 = 11 balls are not blue, out of 20: 11/20.", "درست: 6 + 5 = 11 گیندیں نیلی نہیں ہیں، 20 میں سے: 11/20"),
      ("Model answer: n(S) = 6 + 9 + 5 = 20. Not blue: 6 + 5 = 11, so n(E) = 11. P(E) = 11/20.", "نمونہ جواب: n(S) = 6 + 9 + 5 = 20۔ نیلی نہیں: 6 + 5 = 11، تو n(E) = 11۔ P(E) = 11/20"),
      [("9/20", "9/20 is the probability of blue. The question asks for not blue: 11/20.", "9/20 نیلی کا احتمال ہے۔ سوال نیلی نہ ہونا پوچھتا ہے: 11/20", "event_miscount"),
       ("11/9", "11/9 divides by the 9 blue balls and is more than 1. Divide by all 20: 11/20.", "11/9 میں 9 نیلی گیندوں سے تقسیم کیا گیا اور یہ 1 سے بڑا ہے۔ تمام 20 سے تقسیم کریں: 11/20", "part_to_part")]),
   long_n("l2_green", "A bag has 30 marbles. The probability of a red marble is 2/5 and the probability of a blue marble is 1/3. All the other marbles are green. How many green marbles are there?", "ایک تھیلے میں 30 کنچے ہیں۔ سرخ کنچے کا احتمال 2/5 اور نیلے کنچے کا احتمال 1/3 ہے۔ باقی سب کنچے سبز ہیں۔ سبز کنچے کتنے ہیں؟",
      L2, ("Find the number of red (2/5 of 30) and blue (1/3 of 30), then take them from 30.", "سرخ کی تعداد (30 کا 2/5) اور نیلے کی (30 کا 1/3) نکالیں، پھر انہیں 30 میں سے گھٹائیں۔"),
      ("Correct: red 12, blue 10, and 30 − 12 − 10 = 8 green.", "درست: سرخ 12، نیلے 10، اور 30 − 12 − 10 = 8 سبز"),
      ("Model answer: red = 2/5 of 30 = 12. Blue = 1/3 of 30 = 10. Green = 30 − 12 − 10 = 8.", "نمونہ جواب: سرخ = 30 کا 2/5 = 12۔ نیلے = 30 کا 1/3 = 10۔ سبز = 30 − 12 − 10 = 8"),
      [(12, "12 is the number of red marbles. The question asks for green: 8.", "12 سرخ کنچوں کی تعداد ہے۔ سوال سبز پوچھتا ہے: 8", "answer_is_other_quantity"),
       (22, "22 is red and blue together. Take them from 30: 8.", "22 سرخ اور نیلے ملا کر ہیں۔ انہیں 30 میں سے گھٹائیں: 8", "answer_is_other_quantity")]),
   long_p("l3_coin_dice", "A fair coin is tossed and a fair dice is rolled together. Find the probability of getting a head and an even number.", "ایک منصفانہ سکہ اچھالا جاتا ہے اور ایک منصفانہ پانسہ ساتھ پھینکا جاتا ہے۔ چت اور جفت عدد آنے کا احتمال نکالیں۔",
      L3, ("List the outcomes as pairs: H1, H2, ..., T6. How many have H and an even number?", "نتائج کو جوڑوں کی شکل میں لکھیں: H1، H2، ...، T6۔ ان میں سے کتنوں میں H اور جفت عدد ہے؟"),
      ("Correct: H2, H4, H6 are 3 of the 12 outcomes: 3/12 = 1/4.", "درست: H2، H4، H6، 12 نتائج میں سے 3: 3/12 = 1/4"),
      ("Model answer: n(S) = 2 × 6 = 12. The outcomes with a head and an even number are H2, H4, H6, so n(E) = 3. P(E) = 3/12 = 1/4.", "نمونہ جواب: n(S) = 2 × 6 = 12۔ چت اور جفت عدد والے نتائج H2، H4، H6 ہیں، تو n(E) = 3۔ P(E) = 3/12 = 1/4"),
      [("1/2", "1/2 only looks at the even number, or only at the head. Both must happen: 3/12 = 1/4.", "1/2 میں صرف جفت عدد یا صرف چت دیکھا گیا۔ دونوں ہونے چاہییں: 3/12 = 1/4", "event_miscount"),
       ("1/12", "1/12 counts one outcome. Three outcomes fit: 3/12 = 1/4.", "1/12 میں ایک نتیجہ گنا گیا۔ تین نتائج ٹھیک ہیں: 3/12 = 1/4", "one_way_only")]),
   long_p("l4_nine_or_more", "Two fair dice are rolled. Find the probability that the sum of the two numbers is 9 or more.", "دو منصفانہ پانسے پھینکے جاتے ہیں۔ دونوں اعداد کا مجموعہ 9 یا اس سے زیادہ آنے کا احتمال نکالیں۔",
      L4, ("List the pairs for the sums 9, 10, 11 and 12, both ways round. Out of 36.", "مجموعے 9، 10، 11 اور 12 کے جوڑے دونوں ترتیبوں میں لکھیں۔ کل 36 میں سے۔"),
      ("Correct: sum 9 has 4 pairs, sum 10 has 3, sum 11 has 2 and sum 12 has 1: 10 pairs, and 10/36 = 5/18.", "درست: مجموعہ 9 کے 4 جوڑے، 10 کے 3، 11 کے 2 اور 12 کا 1: 10 جوڑے، اور 10/36 = 5/18"),
      ("Model answer: n(S) = 36. Sum 9: (3,6), (4,5), (5,4), (6,3). Sum 10: (4,6), (5,5), (6,4). Sum 11: (5,6), (6,5). Sum 12: (6,6). So n(E) = 4 + 3 + 2 + 1 = 10. P(E) = 10/36 = 5/18.", "نمونہ جواب: n(S) = 36۔ مجموعہ 9: (3,6)، (4,5)، (5,4)، (6,3)۔ مجموعہ 10: (4,6)، (5,5)، (6,4)۔ مجموعہ 11: (5,6)، (6,5)۔ مجموعہ 12: (6,6)۔ تو n(E) = 4 + 3 + 2 + 1 = 10۔ P(E) = 10/36 = 5/18"),
      [("6/36", "6/36 is for 'more than 9'. '9 or more' includes the sum 9 too: 10/36 = 5/18.", "6/36 '9 سے زیادہ' کا ہے۔ '9 یا زیادہ' میں مجموعہ 9 بھی شامل ہے: 10/36 = 5/18", "event_miscount"),
       ("10/12", "10/12 uses 12 outcomes. Two dice have 36: 10/36 = 5/18.", "10/12 میں 12 نتائج لیے گئے۔ دو پانسوں کے 36 ہیں: 10/36 = 5/18", "space_miscount")]),
   {"id": "s_end_summary", "type": "summary",
    "character": say("celebrating", "You finished the chapter 12 test. Well done!", "آپ نے باب 12 کا ٹیسٹ مکمل کر لیا۔ شاباش!"),
    "text": T("In the exam: write the sample space and count n(S): a coin has 2 outcomes, two coins 4, three coins 8, a dice 6, two dice 36, and a coin with a dice 12 (multiply). Count n(E) carefully, every way: HT and TH, (1,6) and (6,1). P(E) = n(E) ÷ n(S), in its simplest form, always from 0 to 1: 0 is impossible, 1 is certain. Divide by all the outcomes, not only the others. Equally likely outcomes need nothing favoured. Answer what is asked, not a middle step.",
              "امتحان میں: نمونی فضا لکھیں اور n(S) گنیں: سکے کے 2 نتائج، دو سکوں کے 4، تین سکوں کے 8، پانسے کے 6، دو پانسوں کے 36، اور سکے اور پانسے کے 12 (ضرب دیں)۔ n(E) احتیاط سے گنیں، ہر طریقہ: HT اور TH، (1,6) اور (6,1)۔ P(E) = n(E) ÷ n(S)، سادہ ترین شکل میں، ہمیشہ 0 سے 1 کے بیچ: 0 ناممکن، 1 یقینی۔ تمام نتائج سے تقسیم کریں، صرف باقی سے نہیں۔ یکساں امکان کے نتائج میں کسی کو ترجیح نہیں ہوتی۔ وہ جواب دیں جو پوچھا گیا ہو، بیچ کا قدم نہیں۔"),
    "points": [T("List S, count n(E), then n(E) ÷ n(S).", "S لکھیں، n(E) گنیں، پھر n(E) ÷ n(S)۔"),
               T("A probability is never more than 1.", "احتمال کبھی 1 سے زیادہ نہیں ہوتا۔")]},
 ],
 "review_questions": [
   {"id": "r_exam_odd", "type": "exam_style", "skill": SKILL, "step": pq(
     "r_exam_odd", ("A fair dice is rolled once. What is the probability that the number is odd?", "ایک منصفانہ پانسہ ایک بار پھینکا جاتا ہے۔ عدد طاق آنے کا احتمال کیا ہے؟"), R1,
     ("The odd numbers are 1, 3, 5.", "طاق اعداد 1، 3، 5 ہیں۔"),
     ("Correct: 3/6 = 1/2.", "درست: 3/6 = 1/2"), ("n(E) = 3 and n(S) = 6.", "n(E) = 3 اور n(S) = 6"),
     [("3/3", "3/3 divides by the even numbers only. Divide by all 6: 1/2.", "3/3 میں صرف جفت اعداد سے تقسیم کیا گیا۔ تمام 6 سے تقسیم کریں: 1/2", "part_to_part")], qtype=None)},
   {"id": "r_exam_head", "type": "exam_style", "skill": SKILL, "step": pq(
     "r_exam_head", ("A fair coin is tossed once. What is the probability of a head?", "ایک منصفانہ سکہ ایک بار اچھالا جاتا ہے۔ چت آنے کا احتمال کیا ہے؟"), R2,
     ("S = {H, T}.", "S = {H, T}"),
     ("Correct: 1 out of 2, so 1/2.", "درست: 2 میں سے 1، تو 1/2"), ("n(E) = 1 and n(S) = 2.", "n(E) = 1 اور n(S) = 2"),
     [("2/1", "2/1 is upside down. P = 1/2.", "2/1 الٹا ہے۔ P = 1/2", "upside_down")], qtype=None)},
 ],
 "teacher_notes": [
   "A chapter test to use with Review Exercise 12 of the PCTB Mathematics 6 book, in the style of a paper: multiple choice, short questions, then longer problems. Only the kinds of question come from the book; every question, number and story here is new, because the book may not be copied.",
   "It has its own skill (maths.probability.chapter_12_test), with the skills of the Probability unit as prerequisites, and is mastered with exam_style questions, like the earlier chapter tests. Typed probabilities are checked by value, so 3/6 and 1/2 are both right.",
   "Urdu terms to check: کثیر انتخابی (multiple choice), مختصر سوال / تفصیلی سوال (short / long question), نمونہ جواب (model answer), اعادی مشق (review exercise), all as in the earlier chapter tests; the probability words come from the existing Probability lessons. حرفِ علت (vowel), حرفِ صحیح (consonant), چت / پٹ (heads / tails), مفرد عدد (prime number), طاق / جفت (odd / even) and کنچے (marbles) are everyday words used here, and a teacher should confirm them.",
   "The numbers were worked out in content/sources/g6-maths-17/chapter_12_test.py. Edit the script, not this file.",
 ],
 "review": REVIEW,
}

write(lesson)
