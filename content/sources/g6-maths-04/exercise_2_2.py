"""Practice set for Exercise 2.2 of the book: order integers, write
absolute values, and order integers by their absolute values. The
questions are new; only the kinds of question follow the book."""
from common import (T, opt, say, wrong, signed, number_question, choice_question,
                    practice_lesson, practice_intro, write, EX_SKILL, INT_MEANING, INT_ABSOLUTE)

SKILL = EX_SKILL["2.2"]


def lst(xs):
    return ", ".join(signed(x) for x in xs)


def order_options(correct, wrongs, why_en, why_ur, pos=0):
    """Options for an ordering question: the first is right, each of the
    others is a different (wrong) order of the same numbers."""
    orders = [correct] + [w[0] for w in wrongs]
    assert len({tuple(o) for o in orders}) == len(orders)
    assert all(sorted(o) == sorted(correct) for o in orders)
    opts = [opt("o0", lst(correct), lst(correct), True, why_en, why_ur)]
    for k, (o, fen, fur, mis) in enumerate(wrongs, 1):
        opts.append(opt(f"o{k}", lst(o), lst(o), False, fen, fur, mis))
    opts.insert(pos, opts.pop(0))
    return opts


# q1: |-10|
Q1 = abs(-10)
assert Q1 == 10 and -10 != Q1
# q2: smallest of 3, -5, 0, -8
Q2_SET = (3, -5, 0, -8)
Q2 = min(Q2_SET)
assert Q2 == -8 and max(Q2_SET, key=abs) == -8 and min(Q2_SET, key=abs) == 0
# q3: ascending 4, -2, 0, -7
Q3_SET = [4, -2, 0, -7]
Q3_ASC = sorted(Q3_SET)
Q3_DESC = sorted(Q3_SET, reverse=True)
Q3_BY_ABS = sorted(Q3_SET, key=abs)
assert Q3_ASC == [-7, -2, 0, 4] and Q3_DESC == [4, 0, -2, -7] and Q3_BY_ABS == [0, -2, 4, -7]
assert Q3_ASC not in (Q3_DESC, Q3_BY_ABS, Q3_SET)
# q4: |-18|
Q4 = abs(-18)
assert Q4 == 18
# q5: the greatest of -15, -3, -9, -21
Q5_SET = (-15, -3, -9, -21)
Q5 = max(Q5_SET)
assert Q5 == -3 and min(Q5_SET) == -21
# q6: descending 6, -9, -1, 2
Q6_SET = [6, -9, -1, 2]
Q6_DESC = sorted(Q6_SET, reverse=True)
Q6_ASC = sorted(Q6_SET)
Q6_ABS_DESC = sorted(Q6_SET, key=abs, reverse=True)
assert Q6_DESC == [6, 2, -1, -9] and Q6_ASC == [-9, -1, 2, 6] and Q6_ABS_DESC == [-9, 6, 2, -1]
# q7: |-4| + |9|
Q7 = abs(-4) + abs(9)
assert Q7 == 13 and -4 + 9 == 5
# q8: ascending by absolute value: -9, 3, -5, 7
Q8_SET = [-9, 3, -5, 7]
Q8 = sorted(Q8_SET, key=abs)
Q8_PLAIN = sorted(Q8_SET)
Q8_DESC = sorted(Q8_SET, key=abs, reverse=True)
assert Q8 == [3, -5, 7, -9] and Q8_PLAIN == [-9, -5, 3, 7] and Q8_DESC == [-9, 7, -5, 3]
# q9: how many integers have absolute value 8
Q9_ALL = [n for n in range(-20, 21) if abs(n) == 8]
Q9 = len(Q9_ALL)
assert Q9_ALL == [-8, 8] and Q9 == 2
# q10: descending by absolute value: -12, 5, -20, 9
Q10_SET = [-12, 5, -20, 9]
Q10 = sorted(Q10_SET, key=abs, reverse=True)
Q10_PLAIN = sorted(Q10_SET, reverse=True)
Q10_ASC = sorted(Q10_SET, key=abs)
assert Q10 == [-20, -12, 9, 5] and Q10_PLAIN == [9, 5, -12, -20] and Q10_ASC == [5, 9, -12, -20]
# q11: temperatures warmer than -4
Q11_SET = (-3, 5, -9, 0)
Q11 = len([t for t in Q11_SET if t > -4])
assert Q11 == 3 and len([t for t in Q11_SET if t > 0]) == 1
# q12: greatest absolute value among -14, 9, -21, 18
Q12_SET = (-14, 9, -21, 18)
Q12 = max(Q12_SET, key=abs)
assert Q12 == -21 and max(Q12_SET) == 18 and abs(Q12) == 21
# q13 (find error): -8, -3, -1 ascending
Q13_SET = [-8, -3, -1]
assert sorted(Q13_SET) == [-8, -3, -1] and sorted(Q13_SET, reverse=True) == [-1, -3, -8]
# bank and review
QB_REC = abs(-25)
assert QB_REC == 25
QB_APP = sorted([-6, 4, -1, 0, 3])
assert QB_APP == [-6, -1, 0, 3, 4]
QB_APP_COUNT = QB_APP.index(0)
assert QB_APP_COUNT == 2 and QB_APP[0] == -6
R_REC = abs(-31)
assert R_REC == 31
R_SET = [-2, 8, -11, 6]
R_ASC = sorted(R_SET)
R_ABS = sorted(R_SET, key=abs)
assert R_ASC == [-11, -2, 6, 8] and R_ABS == [-2, 6, 8, -11]

lesson = practice_lesson(
 "2.2", script="exercise_2_2.py",
 title=T("Exercise 2.2 practice: ordering and absolute value", "مشق 2.2 کی پریکٹس: ترتیب اور مطلق قیمت"),
 outcome="Calculate the absolute (numerical) value of an integer, and arrange integers and their absolute values in ascending and descending order using a number line.",
 prerequisites=[INT_MEANING, INT_ABSOLUTE],
 misconceptions=[
   {"id": "bigger_digits", "description": "Thinks a negative number with bigger digits is greater: −9 > −2."},
   {"id": "sign_kept", "description": "Gives the absolute value with its minus sign: |−10| = −10."},
   {"id": "abs_added_signed", "description": "Adds the numbers with their signs when asked for the sum of absolute values."},
   {"id": "abs_order_mixed", "description": "Orders by value when the question asks for absolute values, or the other way round."},
   {"id": "one_value", "description": "Thinks only one integer has a given absolute value."},
 ],
 steps=[
   practice_intro("2.2",
     "Here you put integers in order, find absolute values, and put integers in order of their absolute values.",
     "اس میں آپ صحیح اعداد کو ترتیب میں رکھیں گے، مطلق قیمتیں معلوم کریں گے، اور صحیح اعداد کو ان کی مطلق قیمت کی ترتیب میں رکھیں گے۔",
     "Exercise 2.2 is about order and absolute value. Ready?",
     "مشق 2.2 ترتیب اور مطلق قیمت کے بارے میں ہے۔ تیار؟"),
   number_question(
     "q1_abs",
     T("Find |−10|.", "|−10| معلوم کریں۔"),
     Q1,
     T("Absolute value is the distance from 0. How far is −10 from 0?", "مطلق قیمت 0 سے فاصلہ ہے۔ −10، 0 سے کتنی دور ہے؟"),
     T("Right! |−10| = 10.", "درست! |−10| = 10"),
     T("−10 is 10 steps from 0, and a distance is never negative: |−10| = 10.", "−10، 0 سے 10 قدم دور ہے، اور فاصلہ کبھی منفی نہیں ہوتا: |−10| = 10"),
     common_wrong=[wrong(-10, "A distance is never negative. |−10| = 10.", "فاصلہ کبھی منفی نہیں ہوتا۔ |−10| = 10", "sign_kept")],
     qtype="recall"),
   choice_question(
     "q2_smallest",
     T("Which is the smallest of 3, −5, 0 and −8?", "3، −5، 0 اور −8 میں سے سب سے چھوٹا کون سا ہے؟"),
     [opt("m8", "−8", "−8", True, "Yes! −8 is farthest to the left, so it is the smallest.", "جی ہاں! −8 سب سے بائیں ہے، اس لیے سب سے چھوٹا ہے۔"),
      opt("m5", "−5", "−5", False, "−5 is to the right of −8, so it is bigger than −8.", "−5، −8 کے دائیں ہے، اس لیے −8 سے بڑا ہے۔"),
      opt("zero", "0", "0", False, "0 is bigger than every negative number.", "0 ہر منفی عدد سے بڑا ہے۔"),
      opt("three", "3", "3", False, "3 is the biggest of the four.", "3 ان چاروں میں سب سے بڑا ہے۔")],
     qtype="recall"),
   {"id": "s_order", "type": "explain",
    "character": say("thinking", "On the number line, bigger numbers are further right.", "عددی خط پر بڑے اعداد زیادہ دائیں ہوتے ہیں۔"),
    "text": T("Ascending order goes from the smallest to the biggest, left to right on the number line: −7, −2, 0, 4. Descending order goes from the biggest to the smallest. A negative number with bigger digits is smaller: −9 is less than −2. The absolute value |n| is the distance of n from 0, so |−9| = 9 and |4| = 4. To order by absolute value, first write each absolute value, then order those.",
              "صعودی ترتیب سب سے چھوٹے سے سب سے بڑے کی طرف ہوتی ہے، عددی خط پر بائیں سے دائیں: −7، −2، 0، 4۔ نزولی ترتیب سب سے بڑے سے سب سے چھوٹے کی طرف ہوتی ہے۔ بڑے ہندسوں والا منفی عدد چھوٹا ہوتا ہے: −9، −2 سے چھوٹا ہے۔ مطلق قیمت |n|، n کا 0 سے فاصلہ ہے، اس لیے |−9| = 9 اور |4| = 4۔ مطلق قیمت کی ترتیب کے لیے پہلے ہر مطلق قیمت لکھیں، پھر انہیں ترتیب دیں۔")},
   choice_question(
     "q3_ascending",
     T("Arrange 4, −2, 0, −7 in ascending order.", "4، −2، 0، −7 کو صعودی ترتیب میں لکھیں۔"),
     order_options(Q3_ASC, [
         (Q3_DESC, "That is descending order (biggest first). Ascending starts with the smallest.", "یہ نزولی ترتیب ہے (بڑے سے شروع)۔ صعودی ترتیب سب سے چھوٹے سے شروع ہوتی ہے۔", "abs_order_mixed"),
         (Q3_BY_ABS, "That orders them by distance from 0. Order them by value: the smallest is −7.", "یہ 0 سے فاصلے کی ترتیب ہے۔ قیمت کی ترتیب بنائیں: سب سے چھوٹا −7 ہے۔", "abs_order_mixed"),
         (Q3_SET, "That is the order they were given in. Put the smallest first: −7.", "یہ تو دی گئی ترتیب ہے۔ سب سے چھوٹا پہلے رکھیں: −7", None)],
       "Yes! −7 < −2 < 0 < 4, left to right on the number line.", "جی ہاں! −7 < −2 < 0 < 4، عددی خط پر بائیں سے دائیں۔", pos=2),
     qtype="apply"),
   number_question(
     "q4_abs",
     T("Write the absolute value of −18.", "−18 کی مطلق قیمت لکھیں۔"),
     Q4,
     T("How many steps is −18 from 0?", "−18، 0 سے کتنے قدم دور ہے؟"),
     T("Right! |−18| = 18.", "درست! |−18| = 18"),
     T("−18 is 18 steps from 0, so |−18| = 18.", "−18، 0 سے 18 قدم دور ہے، اس لیے |−18| = 18"),
     common_wrong=[wrong(-18, "The absolute value is a distance, so it is not negative: 18.", "مطلق قیمت فاصلہ ہے، اس لیے منفی نہیں: 18", "sign_kept")]),
   number_question(
     "q5_greatest",
     T("Which is the greatest of −15, −3, −9 and −21?", "−15، −3، −9 اور −21 میں سے سب سے بڑا کون سا ہے؟"),
     Q5,
     T("The one closest to 0 is the greatest of the negatives.", "منفی اعداد میں جو 0 کے سب سے قریب ہو وہ سب سے بڑا ہے۔"),
     T("Right! −3 is nearest to 0, so it is the greatest.", "درست! −3، 0 کے سب سے قریب ہے، اس لیے سب سے بڑا ہے۔"),
     T("On the number line −3 is furthest to the right, so −3 is the greatest.", "عددی خط پر −3 سب سے دائیں ہے، اس لیے −3 سب سے بڑا ہے۔"),
     common_wrong=[wrong(-21, "−21 has the biggest digits but is the smallest, furthest left. The greatest is −3.", "−21 کے ہندسے بڑے ہیں مگر یہ سب سے چھوٹا ہے، سب سے بائیں۔ سب سے بڑا −3 ہے۔", "bigger_digits")]),
   choice_question(
     "q6_descending",
     T("Arrange 6, −9, −1, 2 in descending order.", "6، −9، −1، 2 کو نزولی ترتیب میں لکھیں۔"),
     order_options(Q6_DESC, [
         (Q6_ASC, "That is ascending order (smallest first). Descending starts with the biggest.", "یہ صعودی ترتیب ہے (چھوٹے سے شروع)۔ نزولی ترتیب سب سے بڑے سے شروع ہوتی ہے۔", "abs_order_mixed"),
         (Q6_ABS_DESC, "That orders them by distance from 0. By value, 6 is the biggest and −9 the smallest.", "یہ 0 سے فاصلے کی ترتیب ہے۔ قیمت میں 6 سب سے بڑا اور −9 سب سے چھوٹا ہے۔", "abs_order_mixed"),
         ([6, 2, -9, -1], "−9 is smaller than −1, so −1 comes before −9: 6, 2, −1, −9.", "−9، −1 سے چھوٹا ہے، اس لیے −1 پہلے آئے گا: 6، 2، −1، −9", "bigger_digits")],
       "Yes! 6 > 2 > −1 > −9.", "جی ہاں! 6 > 2 > −1 > −9", pos=1),
     qtype="apply"),
   number_question(
     "q7_sum_abs",
     T("Find |−4| + |9|.", "|−4| + |9| معلوم کریں۔"),
     Q7,
     T("Find each absolute value first: |−4| = 4.", "پہلے ہر مطلق قیمت معلوم کریں: |−4| = 4"),
     T("Right! 4 + 9 = 13.", "درست! 4 + 9 = 13"),
     T("|−4| = 4 and |9| = 9, so 4 + 9 = 13.", "|−4| = 4 اور |9| = 9، اس لیے 4 + 9 = 13"),
     common_wrong=[wrong(5, "That is −4 + 9. Take the absolute values first: 4 + 9 = 13.", "یہ −4 + 9 ہے۔ پہلے مطلق قیمتیں لیں: 4 + 9 = 13", "abs_added_signed")]),
   choice_question(
     "q8_abs_ascending",
     T("Arrange −9, 3, −5, 7 in ascending order of their absolute values.", "−9، 3، −5، 7 کو ان کی مطلق قیمتوں کی صعودی ترتیب میں لکھیں۔"),
     order_options(Q8, [
         (Q8_PLAIN, "That orders them by value. The absolute values are 9, 3, 5, 7, so start with 3.", "یہ قیمت کی ترتیب ہے۔ مطلق قیمتیں 9، 3، 5، 7 ہیں، اس لیے 3 سے شروع کریں۔", "abs_order_mixed"),
         (Q8_DESC, "That is descending (9, 7, 5, 3). Ascending starts with the smallest absolute value, 3.", "یہ نزولی (9، 7، 5، 3) ہے۔ صعودی ترتیب سب سے چھوٹی مطلق قیمت 3 سے شروع ہوتی ہے۔", "abs_order_mixed"),
         ([3, 7, -5, -9], "|−5| = 5 is smaller than |7| = 7, so −5 comes before 7.", "|−5| = 5، |7| = 7 سے چھوٹی ہے، اس لیے −5، 7 سے پہلے آئے گا۔", "abs_order_mixed")],
       "Yes! The absolute values are 3, 5, 7, 9.", "جی ہاں! مطلق قیمتیں 3، 5، 7، 9 ہیں۔", pos=3),
     qtype="apply"),
   number_question(
     "q9_two_values",
     T("How many integers have an absolute value of 8?", "کتنے صحیح اعداد کی مطلق قیمت 8 ہے؟"),
     Q9,
     T("Which numbers are 8 steps from 0? Look on both sides.", "کون سے اعداد 0 سے 8 قدم دور ہیں؟ دونوں طرف دیکھیں۔"),
     T("Right! 8 and −8.", "درست! 8 اور −8"),
     T("8 is 8 steps right of 0 and −8 is 8 steps left, so two integers.", "8، 0 سے 8 قدم دائیں اور −8، 8 قدم بائیں ہے، اس لیے دو صحیح اعداد۔"),
     common_wrong=[wrong(1, "−8 is also 8 steps from 0. There are two: 8 and −8.", "−8 بھی 0 سے 8 قدم دور ہے۔ دو ہیں: 8 اور −8", "one_value")]),
   choice_question(
     "q10_abs_descending",
     T("Arrange −12, 5, −20, 9 in descending order of their absolute values.", "−12، 5، −20، 9 کو ان کی مطلق قیمتوں کی نزولی ترتیب میں لکھیں۔"),
     order_options(Q10, [
         (Q10_PLAIN, "That orders them by value. The absolute values are 12, 5, 20, 9, so start with 20.", "یہ قیمت کی ترتیب ہے۔ مطلق قیمتیں 12، 5، 20، 9 ہیں، اس لیے 20 سے شروع کریں۔", "abs_order_mixed"),
         (Q10_ASC, "That is ascending (5, 9, 12, 20). Descending starts with the biggest absolute value, 20.", "یہ صعودی (5، 9، 12، 20) ہے۔ نزولی ترتیب سب سے بڑی مطلق قیمت 20 سے شروع ہوتی ہے۔", "abs_order_mixed"),
         ([-20, 9, -12, 5], "|−12| = 12 is bigger than |9| = 9, so −12 comes before 9.", "|−12| = 12، |9| = 9 سے بڑی ہے، اس لیے −12، 9 سے پہلے آئے گا۔", "abs_order_mixed")],
       "Yes! The absolute values are 20, 12, 9, 5.", "جی ہاں! مطلق قیمتیں 20، 12، 9، 5 ہیں۔", pos=2),
     qtype="apply"),
   number_question(
     "q11_warmer",
     T("Four towns have temperatures −3, 5, −9 and 0 degrees. How many are warmer than −4 degrees?", "چار شہروں کا درجہ حرارت −3، 5، −9 اور 0 ڈگری ہے۔ کتنے شہر −4 ڈگری سے گرم ہیں؟"),
     Q11,
     T("Warmer means greater. Which of the four are to the right of −4?", "گرم کا مطلب بڑا۔ ان چاروں میں سے کون −4 کے دائیں ہیں؟"),
     T("Right! −3, 0 and 5 are greater than −4: three towns.", "درست! −3، 0 اور 5، −4 سے بڑے ہیں: تین شہر۔"),
     T("−3 > −4, 0 > −4 and 5 > −4, but −9 < −4. So 3 towns.", "−3 > −4، 0 > −4 اور 5 > −4، مگر −9 < −4۔ اس لیے 3 شہر۔"),
     common_wrong=[wrong(1, "Negative numbers can be warmer than −4 too. −3 and 0 are greater than −4. Answer 3.", "منفی اعداد بھی −4 سے بڑے ہو سکتے ہیں۔ −3 اور 0، −4 سے بڑے ہیں۔ جواب 3", "bigger_digits")]),
   number_question(
     "q12_greatest_abs",
     T("Which of −14, 9, −21 and 18 has the greatest absolute value?", "−14، 9، −21 اور 18 میں سے کس کی مطلق قیمت سب سے زیادہ ہے؟"),
     Q12,
     T("Write the four absolute values: 14, 9, ... Then find the biggest.", "چاروں مطلق قیمتیں لکھیں: 14، 9، ... پھر سب سے بڑی ڈھونڈیں۔"),
     T("Right! |−21| = 21 is the greatest.", "درست! |−21| = 21 سب سے بڑی ہے۔"),
     T("The absolute values are 14, 9, 21 and 18. The greatest is 21, which belongs to −21.", "مطلق قیمتیں 14، 9، 21 اور 18 ہیں۔ سب سے بڑی 21 ہے، جو −21 کی ہے۔"),
     common_wrong=[wrong(18, "18 is the greatest number, but |−21| = 21 is bigger than 18. The answer is −21.", "18 سب سے بڑا عدد ہے، مگر |−21| = 21، 18 سے بڑی ہے۔ جواب −21", "abs_order_mixed")]),
   choice_question(
     "q13_find_error",
     T("Sara arranges −8, −3, −1 in ascending order and writes −1, −3, −8, because 8 is the biggest digit. What went wrong?", "سارہ −8، −3، −1 کو صعودی ترتیب میں −1، −3، −8 لکھتی ہے، کیونکہ 8 سب سے بڑا ہندسہ ہے۔ کیا غلطی ہوئی؟"),
     [opt("left", "On the number line −8 is furthest left, so it is the smallest and comes first: −8, −3, −1.", "عددی خط پر −8 سب سے بائیں ہے، اس لیے سب سے چھوٹا ہے اور پہلے آتا ہے: −8، −3، −1", True,
          "Yes! For negative numbers, bigger digits mean smaller.", "جی ہاں! منفی اعداد میں بڑے ہندسوں کا مطلب چھوٹا عدد ہے۔"),
      opt("abs", "She should have used absolute values: 1, 3, 8.", "اسے مطلق قیمتیں لینی چاہییں تھیں: 1، 3، 8", False,
          "The question asks for the order of the numbers themselves, not their absolute values.", "سوال خود اعداد کی ترتیب پوچھتا ہے، ان کی مطلق قیمتوں کی نہیں۔", "abs_order_mixed"),
      opt("nothing", "Nothing. −1, −3, −8 is ascending.", "کوئی غلطی نہیں۔ −1، −3، −8 صعودی ہے۔", False,
          "−1, −3, −8 goes from biggest to smallest, which is descending.", "−1، −3، −8 بڑے سے چھوٹے کی طرف ہے، یعنی نزولی۔", "bigger_digits")],
     qtype="find_error"),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! You ordered integers and used absolute values.", "شاباش! آپ نے صحیح اعداد کو ترتیب دی اور مطلق قیمتیں استعمال کیں۔"),
    "text": T("On the number line the numbers grow to the right. Ascending goes smallest to biggest, descending goes biggest to smallest, and a negative number with bigger digits is smaller. The absolute value |n| is the distance from 0: |−10| = 10. To order by absolute value, write the absolute values first.",
              "عددی خط پر اعداد دائیں طرف بڑھتے ہیں۔ صعودی ترتیب چھوٹے سے بڑے، نزولی ترتیب بڑے سے چھوٹے کی طرف ہے، اور بڑے ہندسوں والا منفی عدد چھوٹا ہوتا ہے۔ مطلق قیمت |n|، 0 سے فاصلہ ہے: |−10| = 10۔ مطلق قیمت کی ترتیب کے لیے پہلے مطلق قیمتیں لکھیں۔"),
    "points": [T("−9 is less than −2, even though 9 is more than 2.", "−9، −2 سے چھوٹا ہے، چاہے 9، 2 سے بڑا ہے۔"),
               T("Both 8 and −8 have absolute value 8.", "8 اور −8 دونوں کی مطلق قیمت 8 ہے۔")]},
 ],
 bank=[
   {"id": "qb_abs", "type": "recall", "step": number_question(
     "qb_abs",
     T("Find |−25|.", "|−25| معلوم کریں۔"),
     QB_REC,
     T("The distance of −25 from 0.", "−25 کا 0 سے فاصلہ۔"),
     T("Right! 25.", "درست! 25"),
     T("|−25| = 25.", "|−25| = 25"),
     common_wrong=[wrong(-25, "A distance is never negative: 25.", "فاصلہ کبھی منفی نہیں ہوتا: 25", "sign_kept")],
     qtype=None)},
   {"id": "qb_order", "type": "apply", "step": number_question(
     "qb_order",
     T("Write −6, 4, −1, 0, 3 in ascending order. Which number is the second one?", "−6، 4، −1، 0، 3 کو صعودی ترتیب میں لکھیں۔ دوسرا عدد کون سا ہے؟"),
     QB_APP[1],
     T("The smallest is first, then the next smallest.", "سب سے چھوٹا پہلے، پھر اس سے اگلا۔"),
     T("Right! −6, −1, 0, 3, 4: the second is −1.", "درست! −6، −1، 0، 3، 4: دوسرا −1 ہے۔"),
     T("Ascending: −6, −1, 0, 3, 4. The second is −1.", "صعودی: −6، −1، 0، 3، 4۔ دوسرا −1 ہے۔"),
     common_wrong=[wrong(4, "That is the biggest. Ascending starts with the smallest, −6, and the second is −1.", "یہ سب سے بڑا ہے۔ صعودی ترتیب سب سے چھوٹے −6 سے شروع ہوتی ہے اور دوسرا −1 ہے۔", "abs_order_mixed"),
                   wrong(-6, "−6 is the first one. The second is −1.", "−6 پہلا ہے۔ دوسرا −1 ہے۔", "bigger_digits")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": choice_question(
     "qb_find_error",
     T("Bilal says |−7| = −7 because the number is negative. What went wrong?", "بلال کہتا ہے |−7| = −7 کیونکہ عدد منفی ہے۔ کیا غلطی ہوئی؟"),
     [opt("distance", "Absolute value is a distance from 0, which is never negative: |−7| = 7.", "مطلق قیمت 0 سے فاصلہ ہے، جو کبھی منفی نہیں ہوتا: |−7| = 7", True,
          "Yes! −7 is 7 steps from 0.", "جی ہاں! −7، 0 سے 7 قدم دور ہے۔"),
      opt("zero", "|−7| = 0.", "|−7| = 0", False, "Only |0| is 0. −7 is 7 steps from 0.", "صرف |0| صفر ہے۔ −7، 0 سے 7 قدم دور ہے۔"),
      opt("nothing", "Nothing. |−7| = −7.", "کوئی غلطی نہیں۔ |−7| = −7", False, "The bars remove the sign: |−7| = 7.", "یہ لکیریں علامت ہٹا دیتی ہیں: |−7| = 7", "sign_kept")],
     qtype=None)},
 ],
 review=[
   {"id": "r_abs", "type": "recall", "step": number_question(
     "r_abs",
     T("Find |−31|.", "|−31| معلوم کریں۔"),
     R_REC,
     T("Distance from 0.", "0 سے فاصلہ۔"),
     T("Right! 31.", "درست! 31"),
     T("|−31| = 31.", "|−31| = 31"),
     common_wrong=[wrong(-31, "A distance is not negative: 31.", "فاصلہ منفی نہیں ہوتا: 31", "sign_kept")],
     qtype=None)},
   {"id": "r_order", "type": "apply", "step": choice_question(
     "r_order",
     T("Arrange −2, 8, −11, 6 in ascending order of their absolute values.", "−2، 8، −11، 6 کو ان کی مطلق قیمتوں کی صعودی ترتیب میں لکھیں۔"),
     order_options(R_ABS, [
         (R_ASC, "That orders them by value. The absolute values are 2, 8, 11, 6, so start with 2.", "یہ قیمت کی ترتیب ہے۔ مطلق قیمتیں 2، 8، 11، 6 ہیں، اس لیے 2 سے شروع کریں۔", "abs_order_mixed"),
         ([8, 6, -2, -11], "That is not in order of any kind. The absolute values should go 2, 6, 8, 11.", "یہ کسی بھی ترتیب میں نہیں۔ مطلق قیمتیں 2، 6، 8، 11 ہونی چاہییں۔", None),
         (sorted(R_SET, key=abs, reverse=True), "That is descending. Ascending starts with the smallest absolute value, 2.", "یہ نزولی ہے۔ صعودی ترتیب سب سے چھوٹی مطلق قیمت 2 سے شروع ہوتی ہے۔", "abs_order_mixed")],
       "Yes! The absolute values go 2, 6, 8, 11.", "جی ہاں! مطلق قیمتیں 2، 6، 8، 11 ہیں۔", pos=1),
     qtype=None)},
 ],
 glossary=[T("Ascending order", "صعودی ترتیب"), T("Descending order", "نزولی ترتیب"), T("Absolute value", "مطلق قیمت"), T("Integer", "صحیح عدد"), T("Number line", "عددی خط")],
 flashcards=[
   {"id": "f_order", "front": T("Which is greater, −3 or −9?", "−3 اور −9 میں سے کون بڑا ہے؟"),
    "back": T("−3. It is further right on the number line, nearer to 0.", "−3۔ یہ عددی خط پر زیادہ دائیں اور 0 کے قریب ہے۔")},
   {"id": "f_abs", "front": T("What is |−15|?", "|−15| کیا ہے؟"),
    "back": T("15. Absolute value is the distance from 0, so it is never negative.", "15۔ مطلق قیمت 0 سے فاصلہ ہے، اس لیے کبھی منفی نہیں۔")},
 ],
 home_task={"id": "h_cards", "text": T(
   "Write the integers from −9 to 9 on separate pieces of paper. Shuffle them, pick five, and put them in ascending order, then in order of their absolute values. Check with the number line.",
   "کاغذ کے الگ ٹکڑوں پر −9 سے 9 تک صحیح اعداد لکھیں۔ انہیں ملائیں، پانچ اٹھائیں، اور صعودی ترتیب میں رکھیں، پھر مطلق قیمت کی ترتیب میں۔ عددی خط سے جانچیں۔")},
 notes=["Covers ordering integers (q2, q3, q5, q6, q11, q13), absolute values (q1, q4, q7, q9, q12) and ordering by absolute value (q8, q10).",
        "Each ordering question has wrong options that are real mistakes: the opposite direction, ordering by absolute value instead of value, or treating bigger digits as bigger for negative numbers.",
        "Urdu terms to check: صعودی ترتیب / نزولی ترتیب (ascending / descending order), مطلق قیمت (absolute value)."],
 minutes=18,
)

write(lesson)
