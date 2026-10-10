"""Practice set for Exercise 2.1 of the book: natural and whole numbers,
reading and plotting integers on a number line, writing situations as
integers, opposites, and picking integers from a list. The questions are
new; only the kinds of question follow the book."""
from common import (T, opt, say, wrong, signed, number_question, number_line, choice_question,
                    practice_lesson, practice_intro, write, EX_SKILL, INT_MEANING)
from figs import NumberLine, number_line_figure, attach

SKILL = EX_SKILL["2.1"]

NATURAL = list(range(1, 6))
WHOLE = list(range(0, 6))
# q1: a whole number that is not a natural number
Q1_OPTS = (0, 1, -1, 10)
assert [n for n in Q1_OPTS if n >= 0 and n not in NATURAL + [1, 10]] == [0]
assert set(WHOLE) - set(NATURAL) == {0}
# q2: the opposite of 9
Q2 = -9
assert Q2 == -(9) and 9 + Q2 == 0
# q3: 12 m below sea level
Q3 = -12
assert Q3 < 0 and -Q3 == 12
# q4: a loss of Rs 250
Q4 = -250
assert Q4 < 0 and abs(Q4) == 250
# q5: which is not an integer
Q5_OPTS = (-7, 0, 2.5, 15)
assert [n for n in Q5_OPTS if n != int(n)] == [2.5]
# q6: plot -8
Q6 = -8
assert -10 <= Q6 <= 10 and Q6 < 0
# q7 and q8: points on a number line
PTS = {"P": -5, "Q": 2, "R": 5, "S": -2}
Q7 = PTS["P"]
assert Q7 == -5
Q8 = [k for k, v in PTS.items() if v == -PTS["R"]]
assert Q8 == ["P"] and -PTS["Q"] == PTS["S"]
# q9: steps between -4 and 5
Q9 = 5 - (-4)
assert Q9 == 9 and 4 + 5 == 9 and 5 - 4 == 1
# q10: the opposite of -6
Q10 = -(-6)
assert Q10 == 6 and -6 + Q10 == 0
# q12: integers from -3 to 3, both ends counted
Q12_LIST = list(range(-3, 4))
Q12 = len(Q12_LIST)
assert Q12 == 7 and 3 + 3 == 6 and 3 * 2 + 1 == Q12
# bank and review
QB_REC = -14
assert QB_REC == -(14)
QB_APP = abs(2 - (-6))
assert QB_APP == 8 and 6 - 2 == 4
R_REC = -(-13)
assert R_REC == 13
R_APP = -9
assert R_APP < 0


def points_figure(alt_en, alt_ur):
    nl = NumberLine(-8, 8, 40, hide=tuple(PTS.values()), keys=(-8, 8))
    for k, v in PTS.items():
        nl.mark(v, k)
    return number_line_figure(alt_en, alt_ur, [nl], 70)


ALT_EN = "A number line from −8 to 8 with four dots: P at −5, S at −2, Q at 2 and R at 5. The dots are marked with their letters, not their numbers."
ALT_UR = "−8 سے 8 تک عددی خط جس پر چار نقطے ہیں: P پر −5، S پر −2، Q پر 2 اور R پر 5۔ نقطوں پر عدد نہیں، حرف لکھے ہیں۔"

lesson = practice_lesson(
 "2.1", script="exercise_2_1.py",
 title=T("Exercise 2.1 practice: integers on the number line", "مشق 2.1 کی پریکٹس: عددی خط پر صحیح اعداد"),
 outcome="Recognize and identify integers (positive integers, negative integers and the neutral integer), and show them on a number line.",
 prerequisites=[INT_MEANING],
 misconceptions=[
   {"id": "sign_ignored", "description": "Ignores the minus sign: 12 m below sea level is written 12, and −6 is placed on the right of 0."},
   {"id": "opposite_same", "description": "Thinks the opposite of a number is the number itself, or that a negative number has no opposite."},
   {"id": "zero_sign", "description": "Thinks 0 is positive or negative, or not an integer."},
   {"id": "zero_natural", "description": "Thinks 0 is a natural number."},
   {"id": "gap_miscount", "description": "Subtracts the numbers without their signs, or leaves out 0 when counting."},
 ],
 steps=[
   practice_intro("2.1",
     "Here you work with natural and whole numbers, read and plot integers on a number line, write situations as integers, and find opposites.",
     "اس میں آپ قدرتی اور مکمل اعداد کے ساتھ کام کریں گے، عددی خط پر صحیح اعداد پڑھیں گے اور لگائیں گے، صورتحال کو صحیح عدد میں لکھیں گے، اور مخالف اعداد معلوم کریں گے۔",
     "Exercise 2.1 is about integers on the number line. Let's go!",
     "مشق 2.1 عددی خط پر صحیح اعداد کے بارے میں ہے۔ چلیں!"),
   choice_question(
     "q1_whole",
     T("Which of these is a whole number but not a natural number?", "ان میں سے کون سا مکمل عدد ہے مگر قدرتی عدد نہیں؟"),
     [opt("zero", "0", "0", True, "Yes! Natural numbers start at 1. Whole numbers are 0, 1, 2, 3 ...", "جی ہاں! قدرتی اعداد 1 سے شروع ہوتے ہیں۔ مکمل اعداد 0، 1، 2، 3 ... ہیں۔"),
      opt("one", "1", "1", False, "1 is both a natural number and a whole number.", "1 قدرتی عدد بھی ہے اور مکمل عدد بھی۔"),
      opt("minus_one", "−1", "−1", False, "−1 is negative, so it is neither natural nor whole. It is an integer.", "−1 منفی ہے، اس لیے نہ قدرتی ہے نہ مکمل۔ یہ صحیح عدد ہے۔"),
      opt("ten", "10", "10", False, "10 is both a natural number and a whole number.", "10 قدرتی عدد بھی ہے اور مکمل عدد بھی۔")],
     qtype="recall"),
   {"id": "s_opposite", "type": "explain",
    "character": say("thinking", "Every number has an opposite on the other side of 0.", "ہر عدد کا 0 کی دوسری طرف ایک مخالف عدد ہوتا ہے۔"),
    "text": T("The opposite of 4 is −4, and the opposite of −4 is 4. Opposites are the same distance from 0 but on different sides. A number and its opposite add up to 0. The integers are ... −3, −2, −1, 0, 1, 2, 3 ...; 0 is neither positive nor negative.",
              "4 کا مخالف عدد −4 ہے، اور −4 کا مخالف عدد 4 ہے۔ مخالف اعداد 0 سے برابر فاصلے پر ہوتے ہیں مگر مختلف طرف۔ عدد اور اس کا مخالف جمع ہو کر 0 بنتے ہیں۔ صحیح اعداد ... −3، −2، −1، 0، 1، 2، 3 ... ہیں؛ 0 نہ مثبت ہے نہ منفی۔")},
   number_question(
     "q2_opposite",
     T("Write the opposite of 9.", "9 کا مخالف عدد لکھیں۔"),
     Q2,
     T("Same distance from 0, but on the other side.", "0 سے اتنا ہی فاصلہ، مگر دوسری طرف۔"),
     T("Right! The opposite of 9 is −9.", "درست! 9 کا مخالف عدد −9 ہے۔"),
     T("9 is 9 steps right of 0, so its opposite is 9 steps left: −9.", "9، 0 سے 9 قدم دائیں ہے، اس لیے اس کا مخالف 9 قدم بائیں ہے: −9"),
     common_wrong=[wrong(9, "That is the same number. The opposite is on the other side of 0: −9.", "یہ وہی عدد ہے۔ مخالف عدد 0 کی دوسری طرف ہوتا ہے: −9", "opposite_same")],
     qtype="recall"),
   choice_question(
     "q3_sea",
     T("A diver is 12 m below sea level. Which integer shows her position, if sea level is 0?", "ایک غوطہ خور سطح سمندر سے 12 میٹر نیچے ہے۔ سطح سمندر 0 ہو تو اس کی جگہ کون سا صحیح عدد ظاہر کرتا ہے؟"),
     [opt("m12", "−12", "−12", True, "Yes! Below sea level is negative.", "جی ہاں! سطح سمندر سے نیچے منفی ہوتا ہے۔"),
      opt("p12", "12", "12", False, "12 would be 12 m above sea level.", "12 کا مطلب سطح سمندر سے 12 میٹر اوپر ہوتا۔", "sign_ignored"),
      opt("zero", "0", "0", False, "0 is sea level itself, and she is 12 m below it.", "0 تو سطح سمندر ہی ہے، اور وہ اس سے 12 میٹر نیچے ہے۔", "zero_sign")],
     qtype="recall"),
   number_question(
     "q4_loss",
     T("A shopkeeper has a loss of Rs 250. Write the loss as an integer, where profit is positive.", "ایک دکاندار کو 250 روپے کا نقصان ہوا۔ نقصان کو صحیح عدد میں لکھیں، جہاں منافع مثبت ہے۔"),
     Q4,
     T("A profit is positive, so a loss is the opposite.", "منافع مثبت ہے، اس لیے نقصان اس کا الٹ ہے۔"),
     T("Right! A loss of Rs 250 is −250.", "درست! 250 روپے کا نقصان −250 ہے۔"),
     T("Profit is positive, so a loss is negative: −250.", "منافع مثبت ہے، اس لیے نقصان منفی ہے: −250"),
     common_wrong=[wrong(250, "That would be a profit of Rs 250. A loss is negative: −250.", "یہ 250 روپے کا منافع ہوتا۔ نقصان منفی ہے: −250", "sign_ignored")]),
   choice_question(
     "q5_not_integer",
     T("Which of these numbers is not an integer?", "ان میں سے کون سا عدد صحیح عدد نہیں؟"),
     [opt("m7", "−7", "−7", False, "−7 is a negative integer.", "−7 منفی صحیح عدد ہے۔"),
      opt("zero", "0", "0", False, "0 is an integer, the neutral one.", "0 صحیح عدد ہے، غیر جانبدار صحیح عدد۔", "zero_sign"),
      opt("half", "2½", "2½", True, "Yes! 2½ is between 2 and 3, so it is not a whole step on the number line.", "جی ہاں! 2½، 2 اور 3 کے بیچ میں ہے، اس لیے عددی خط پر پورا قدم نہیں۔"),
      opt("p15", "+15", "+15", False, "+15 is the same as 15, a positive integer.", "+15 وہی 15 ہے، مثبت صحیح عدد۔")]),
   number_line(
     "q6_plot",
     T("Put the marker on −8. Press Check.", "نشان کو −8 پر رکھیں۔ \"جانچیں\" دبائیں۔"),
     Q6,
     T("Start at 0 and count 8 steps to the left.", "0 سے شروع کریں اور 8 قدم بائیں گنیں۔"),
     T("Right! −8 is 8 steps to the left of 0.", "درست! −8، 0 سے 8 قدم بائیں ہے۔"),
     T("−8 is 8 steps to the LEFT of 0.", "−8، 0 سے 8 قدم بائیں طرف ہے۔"),
     common_wrong=[wrong("8", "That is 8, to the right of 0. A minus sign means go LEFT.", "یہ 8 ہے، 0 کے دائیں طرف۔ منفی کا مطلب بائیں جائیں۔", "sign_ignored")]),
   number_question(
     "q7_read",
     T("Which integer does point P show on the number line?", "عددی خط پر نقطہ P کون سا صحیح عدد ظاہر کرتا ہے؟"),
     Q7,
     T("P is left of 0. Count the steps from 0 to P.", "P، 0 کے بائیں ہے۔ 0 سے P تک قدم گنیں۔"),
     T("Right! P is 5 steps left of 0: −5.", "درست! P، 0 سے 5 قدم بائیں ہے: −5"),
     T("P is 5 steps to the left of 0, so it shows −5.", "P، 0 سے 5 قدم بائیں ہے، اس لیے یہ −5 ہے۔"),
     common_wrong=[wrong(5, "5 is where R is, on the right. P is on the left: −5.", "5 پر R ہے، دائیں طرف۔ P بائیں طرف ہے: −5", "sign_ignored")]),
   choice_question(
     "q8_opposite_point",
     T("Which point is the opposite of R?", "کون سا نقطہ R کا مخالف ہے؟"),
     [opt("pt_p", "P", "P", True, "Yes! R is 5 and P is −5, the same distance from 0 on opposite sides.", "جی ہاں! R، 5 ہے اور P، −5، 0 سے برابر فاصلے پر مخالف طرف۔"),
      opt("pt_q", "Q", "Q", False, "Q is 2. The opposite of R (5) must be 5 steps from 0.", "Q، 2 ہے۔ R (5) کا مخالف 0 سے 5 قدم پر ہونا چاہیے۔", "opposite_same"),
      opt("pt_s", "S", "S", False, "S is −2. It is the opposite of Q, not of R.", "S، −2 ہے۔ یہ Q کا مخالف ہے، R کا نہیں۔", "opposite_same")]),
   number_question(
     "q9_gap",
     T("How many steps are there on the number line from −4 to 5?", "عددی خط پر −4 سے 5 تک کتنے قدم ہیں؟"),
     Q9,
     T("Count the steps from −4 to 0, then from 0 to 5.", "−4 سے 0 تک قدم گنیں، پھر 0 سے 5 تک۔"),
     T("Right! 4 + 5 = 9 steps.", "درست! 4 + 5 = 9 قدم"),
     T("−4 to 0 is 4 steps and 0 to 5 is 5 steps. 4 + 5 = 9.", "−4 سے 0 تک 4 قدم اور 0 سے 5 تک 5 قدم۔ 4 + 5 = 9"),
     common_wrong=[wrong(1, "That is 5 − 4. The two numbers are on opposite sides of 0, so add the steps: 9.", "یہ 5 − 4 ہے۔ دونوں اعداد 0 کے مخالف طرف ہیں، اس لیے قدم جمع کریں: 9", "gap_miscount")]),
   number_line(
     "q10_plot_opposite",
     T("Put the marker on the opposite of −6. Press Check.", "نشان کو −6 کے مخالف عدد پر رکھیں۔ \"جانچیں\" دبائیں۔"),
     Q10,
     T("−6 is 6 steps left of 0. Its opposite is 6 steps on the other side.", "−6، 0 سے 6 قدم بائیں ہے۔ اس کا مخالف دوسری طرف 6 قدم پر ہے۔"),
     T("Right! The opposite of −6 is 6.", "درست! −6 کا مخالف عدد 6 ہے۔"),
     T("−6 is 6 steps left of 0, so its opposite is 6 steps right: 6.", "−6، 0 سے 6 قدم بائیں ہے، اس لیے اس کا مخالف 6 قدم دائیں ہے: 6"),
     common_wrong=[wrong("-6", "That is −6 itself. The opposite is on the other side of 0.", "یہ تو −6 ہی ہے۔ مخالف عدد 0 کی دوسری طرف ہوتا ہے۔", "opposite_same")]),
   choice_question(
     "q11_zero",
     T("Which statement about 0 is true?", "0 کے بارے میں کون سا بیان درست ہے؟"),
     [opt("neither", "0 is an integer that is neither positive nor negative.", "0 ایسا صحیح عدد ہے جو نہ مثبت ہے نہ منفی۔", True, "Yes! That is why 0 is called the neutral integer.", "جی ہاں! اسی لیے 0 کو غیر جانبدار صحیح عدد کہتے ہیں۔"),
      opt("positive", "0 is a positive integer.", "0 مثبت صحیح عدد ہے۔", False, "Positive integers are 1, 2, 3 ... and start after 0.", "مثبت صحیح اعداد 1، 2، 3 ... ہیں اور 0 کے بعد شروع ہوتے ہیں۔", "zero_sign"),
      opt("negative", "0 is a negative integer.", "0 منفی صحیح عدد ہے۔", False, "Negative integers are −1, −2, −3 ... and are less than 0.", "منفی صحیح اعداد −1، −2، −3 ... ہیں اور 0 سے چھوٹے ہیں۔", "zero_sign"),
      opt("not_int", "0 is not an integer.", "0 صحیح عدد نہیں۔", False, "0 is an integer. It sits in the middle of the number line.", "0 صحیح عدد ہے۔ یہ عددی خط کے بیچ میں ہے۔", "zero_sign")]),
   number_question(
     "q12_count",
     T("How many integers are there from −3 to 3, counting both ends?", "−3 سے 3 تک، دونوں سرے ملا کر، کتنے صحیح اعداد ہیں؟"),
     Q12,
     T("Write them all: −3, −2, ... Don't forget 0.", "سب لکھیں: −3، −2، ... 0 کو نہ بھولیں۔"),
     T("Right! −3, −2, −1, 0, 1, 2, 3: seven integers.", "درست! −3، −2، −1، 0، 1، 2، 3: سات صحیح اعداد۔"),
     T("Three negative, 0, and three positive: 3 + 1 + 3 = 7.", "تین منفی، 0، اور تین مثبت: 3 + 1 + 3 = 7"),
     common_wrong=[wrong(6, "You left out 0. There are 3 + 1 + 3 = 7.", "آپ نے 0 چھوڑ دیا۔ کل 3 + 1 + 3 = 7 ہیں۔", "gap_miscount")]),
   choice_question(
     "q13_find_error",
     T("Hamza says the opposite of −6 is −6, because it already has a minus sign. What went wrong?", "حمزہ کہتا ہے −6 کا مخالف −6 ہے، کیونکہ اس پر پہلے ہی منفی کا نشان ہے۔ کیا غلطی ہوئی؟"),
     [opt("other_side", "The opposite is on the other side of 0, so it is 6.", "مخالف عدد 0 کی دوسری طرف ہوتا ہے، اس لیے یہ 6 ہے۔", True, "Yes! Opposites are the same distance from 0 on different sides.", "جی ہاں! مخالف اعداد 0 سے برابر فاصلے پر مختلف طرف ہوتے ہیں۔"),
      opt("zero", "The opposite of −6 is 0.", "−6 کا مخالف 0 ہے۔", False, "0 is the middle, not the opposite. −6 + 6 = 0 shows the opposite is 6.", "0 درمیان ہے، مخالف نہیں۔ −6 + 6 = 0 بتاتا ہے کہ مخالف 6 ہے۔"),
      opt("nothing", "Nothing. −6 has no other opposite.", "کوئی غلطی نہیں۔ −6 کا اور کوئی مخالف نہیں۔", False, "Every integer has an opposite. For −6 it is 6.", "ہر صحیح عدد کا ایک مخالف ہوتا ہے۔ −6 کا مخالف 6 ہے۔", "opposite_same")],
     qtype="find_error"),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! You read, plotted and wrote integers.", "شاباش! آپ نے صحیح اعداد پڑھے، لگائے اور لکھے۔"),
    "text": T("Natural numbers are 1, 2, 3 ...; whole numbers are 0, 1, 2, 3 ...; integers are ... −2, −1, 0, 1, 2 ... Below 0 is negative, above 0 is positive, and 0 is neither. Opposites are the same distance from 0 on different sides: the opposite of −6 is 6.",
              "قدرتی اعداد 1، 2، 3 ... ہیں؛ مکمل اعداد 0، 1، 2، 3 ... ہیں؛ صحیح اعداد ... −2، −1، 0، 1، 2 ... ہیں۔ 0 سے نیچے منفی، 0 سے اوپر مثبت، اور 0 نہ مثبت نہ منفی۔ مخالف اعداد 0 سے برابر فاصلے پر مختلف طرف ہوتے ہیں: −6 کا مخالف 6 ہے۔"),
    "points": [T("A loss, a debt or a temperature below zero is negative.", "نقصان، قرض یا صفر سے کم درجہ حرارت منفی ہے۔"),
               T("Between −4 and 5 there are 4 + 5 = 9 steps.", "−4 اور 5 کے بیچ 4 + 5 = 9 قدم ہیں۔")]},
 ],
 bank=[
   {"id": "qb_opposite", "type": "recall", "step": number_question(
     "qb_opposite",
     T("Write the opposite of 14.", "14 کا مخالف عدد لکھیں۔"),
     QB_REC,
     T("Same distance from 0, on the other side.", "0 سے اتنا ہی فاصلہ، دوسری طرف۔"),
     T("Right! −14.", "درست! −14"),
     T("The opposite of 14 is −14.", "14 کا مخالف عدد −14 ہے۔"),
     common_wrong=[wrong(14, "That is the same number. The opposite is −14.", "یہ وہی عدد ہے۔ مخالف −14 ہے۔", "opposite_same")],
     qtype=None)},
   {"id": "qb_gap", "type": "apply", "step": number_question(
     "qb_gap",
     T("How many steps are there on the number line from −6 to 2?", "عددی خط پر −6 سے 2 تک کتنے قدم ہیں؟"),
     QB_APP,
     T("Steps from −6 to 0, then from 0 to 2.", "−6 سے 0 تک قدم، پھر 0 سے 2 تک۔"),
     T("Right! 6 + 2 = 8.", "درست! 6 + 2 = 8"),
     T("−6 to 0 is 6 steps and 0 to 2 is 2 steps, so 8.", "−6 سے 0 تک 6 قدم اور 0 سے 2 تک 2 قدم، اس لیے 8"),
     common_wrong=[wrong(4, "That is 6 − 2. They are on opposite sides of 0, so add: 8.", "یہ 6 − 2 ہے۔ وہ 0 کے مخالف طرف ہیں، اس لیے جمع کریں: 8", "gap_miscount")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": choice_question(
     "qb_find_error",
     T("Imran says 0 is a natural number, because it is the first number we count from. What went wrong?", "عمران کہتا ہے 0 قدرتی عدد ہے، کیونکہ ہم اسی سے گنتی شروع کرتے ہیں۔ کیا غلطی ہوئی؟"),
     [opt("starts_one", "Natural numbers start at 1. 0 is a whole number.", "قدرتی اعداد 1 سے شروع ہوتے ہیں۔ 0 مکمل عدد ہے۔", True, "Yes! Natural numbers are 1, 2, 3 ...; add 0 to get the whole numbers.", "جی ہاں! قدرتی اعداد 1، 2، 3 ... ہیں؛ ان میں 0 ملانے سے مکمل اعداد بنتے ہیں۔"),
      opt("neg", "0 is a negative number.", "0 منفی عدد ہے۔", False, "0 is neither negative nor positive.", "0 نہ منفی ہے نہ مثبت۔", "zero_sign"),
      opt("nothing", "Nothing. 0 is a natural number.", "کوئی غلطی نہیں۔ 0 قدرتی عدد ہے۔", False, "Natural numbers start at 1.", "قدرتی اعداد 1 سے شروع ہوتے ہیں۔", "zero_natural")],
     qtype=None)},
 ],
 review=[
   {"id": "r_opposite", "type": "recall", "step": number_question(
     "r_opposite",
     T("Write the opposite of −13.", "−13 کا مخالف عدد لکھیں۔"),
     R_REC,
     T("−13 is left of 0. Its opposite is on the right.", "−13، 0 کے بائیں ہے۔ اس کا مخالف دائیں ہے۔"),
     T("Right! 13.", "درست! 13"),
     T("The opposite of −13 is 13.", "−13 کا مخالف عدد 13 ہے۔"),
     common_wrong=[wrong(-13, "That is the same number. The opposite is 13.", "یہ وہی عدد ہے۔ مخالف 13 ہے۔", "opposite_same")],
     qtype=None)},
   {"id": "r_temperature", "type": "apply", "step": number_question(
     "r_temperature",
     T("The temperature is 9 degrees below freezing (0). Write it as an integer.", "درجہ حرارت نقطہ انجماد (0) سے 9 درجے نیچے ہے۔ اسے صحیح عدد میں لکھیں۔"),
     R_APP,
     T("Below zero is negative.", "صفر سے نیچے منفی ہے۔"),
     T("Right! −9.", "درست! −9"),
     T("Below 0 is negative, so −9.", "0 سے نیچے منفی ہے، اس لیے −9"),
     common_wrong=[wrong(9, "9 would be 9 degrees above freezing. Below is −9.", "9 کا مطلب انجماد سے 9 درجے اوپر ہوتا۔ نیچے ہو تو −9", "sign_ignored")],
     qtype=None)},
 ],
 glossary=[T("Integer", "صحیح عدد"), T("Natural number", "قدرتی عدد"), T("Whole number", "مکمل عدد"), T("Opposite", "مخالف عدد"), T("Number line", "عددی خط")],
 flashcards=[
   {"id": "f_opposite", "front": T("What is the opposite of −20?", "−20 کا مخالف عدد کیا ہے؟"),
    "back": T("20. Opposites are the same distance from 0 on different sides.", "20۔ مخالف اعداد 0 سے برابر فاصلے پر مختلف طرف ہوتے ہیں۔")},
   {"id": "f_zero", "front": T("Is 0 positive, negative or neither?", "کیا 0 مثبت ہے، منفی ہے یا کچھ نہیں؟"),
    "back": T("Neither. 0 is the neutral integer, in the middle of the number line.", "نہ مثبت نہ منفی۔ 0 غیر جانبدار صحیح عدد ہے، عددی خط کے بیچ میں۔")},
 ],
 home_task={"id": "h_thermometer", "text": T(
   "Look at the weather forecast for a cold city, or draw a thermometer. Write three temperatures as integers, some above and some below zero, and mark them on a number line in your notebook.",
   "کسی ٹھنڈے شہر کی موسمی پیشگوئی دیکھیں یا تھرمامیٹر بنائیں۔ تین درجہ حرارت صحیح اعداد میں لکھیں، کچھ صفر سے اوپر اور کچھ نیچے، اور انہیں اپنی کاپی میں عددی خط پر لگائیں۔")},
 notes=["Covers natural and whole numbers (q1, qb_find_error), writing situations as integers (q3, q4), reading and plotting on a number line (q6 to q8, q10), opposites (q2, q8, q10, q13), picking integers from a list (q5, q11) and short number-line problems (q9, q12).",
        "The figure for q7 and q8 is drawn with the dots named by letters, so the child reads the number from the line.",
        "Urdu terms to check: قدرتی عدد (natural number), مکمل عدد (whole number), مخالف عدد (opposite), غیر جانبدار صحیح عدد (neutral integer), عددی خط (number line)."],
 minutes=16,
)

# Move the right option to a different place in some questions.
for step in lesson["steps"]:
    pos = {"q1_whole": 2, "q3_sea": 1, "q8_opposite_point": 2, "q11_zero": 3, "q13_find_error": 1}.get(step["id"])
    if pos is not None:
        right = next(o for o in step["options"] if o["correct"])
        step["options"].remove(right)
        step["options"].insert(pos, right)

attach(lesson, {
    "q7_read": points_figure(ALT_EN, ALT_UR),
    "q8_opposite_point": points_figure(ALT_EN, ALT_UR),
})
write(lesson)
