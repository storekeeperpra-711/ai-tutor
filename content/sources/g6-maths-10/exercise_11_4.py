"""Practice set for Exercise 11.4 of the book: the mean (including a missing value
when the mean is given), the median for an odd and an even number of values, and
the mode. The questions are new; only the kinds of question follow the book."""
from statistics import mean, median, mode

from common import (T, say, nq, ch, practice_lesson, practice_intro, write, EX_SKILL,
                    DH_MEAN, DH_MEDIAN, DH_MODE_RANGE, DH_WORD_PROBLEMS)
from figs import bar_graph, with_fig


def whole(x):
    assert x == int(x), x
    return int(x)


SKILL = EX_SKILL["11.4"]

# q2: mean of five values
A = [12, 7, 9, 15, 7]
Q2 = whole(mean(A))
assert Q2 == 10 and sum(A) == 50 and median(A) == 9 and mode(A) == 7
# q3: missing value from the mean
Q3_MEAN, Q3_N, Q3_KNOWN = 8, 5, [4, 10, 6, 9]
Q3 = Q3_MEAN * Q3_N - sum(Q3_KNOWN)
assert Q3 == 11 and mean(Q3_KNOWN + [Q3]) == Q3_MEAN and Q3_MEAN != Q3
# q4: median of seven values given out of order
B = [14, 6, 11, 9, 20, 8, 17]
Q4 = whole(median(B))
assert Q4 == 11 and sorted(B) == [6, 8, 9, 11, 14, 17, 20] and B[3] == 9
# q5: median of six values (mean of the two middle values)
C = [3, 9, 5, 12, 7, 10]
SC = sorted(C)
Q5 = whole(median(C))
assert SC == [3, 5, 7, 9, 10, 12] and Q5 == 8 and (SC[2] + SC[3]) / 2 == 8
# q6: mode
D = [4, 6, 4, 9, 6, 4, 8]
Q6 = mode(D)
assert Q6 == 4 and D.count(4) == 3 and D.count(6) == 2
# q8: a new value is added to five values
E_MEAN, E_N, E_NEW = 10, 5, 16
E_TOTAL = E_MEAN * E_N
Q8 = whole((E_TOTAL + E_NEW) / (E_N + 1))
assert Q8 == 11 and E_TOTAL == 50 and (E_MEAN + E_NEW) / 2 == 13
# q9: runs in four matches shown by bars
RUNS = [6, 10, 8, 12]
Q9 = whole(mean(RUNS))
assert Q9 == 9 and sum(RUNS) == 36
# q10: median of unsorted values
G = [9, 3, 7, 5, 1]
Q10 = whole(median(G))
assert Q10 == 5 and G[2] == 7 and sorted(G) == [1, 3, 5, 7, 9]
# q11: total from the mean
H_MEAN, H_N = 12, 4
Q11 = H_MEAN * H_N
assert Q11 == 48
# bank and review
QB_DATA = [9, 5, 11, 7]
QB = whole(mean(QB_DATA))
assert QB == 8 and sum(QB_DATA) == 32 and max(QB_DATA) == 11
QB_MODE = [3, 5, 3, 7, 5, 3]
assert mode(QB_MODE) == 3
R1_DATA = [13, 7, 21, 4, 10]
R1 = whole(median(R1_DATA))
assert R1 == 10 and sorted(R1_DATA) == [4, 7, 10, 13, 21] and R1_DATA[2] == 21
R2_DATA = [2, 5, 2, 9, 5, 2, 7]
R2 = mode(R2_DATA)
assert R2 == 2 and R2_DATA.count(5) == 2

F_RUNS = bar_graph(RUNS, ["1", "2", "3", "4"],
    "A bar graph of the runs scored in four matches. The side scale goes up in two from 0 to 12. Match 1: 6 runs, match 2: 10 runs, match 3: 8 runs, match 4: 12 runs.",
    "چار میچوں میں بنائے گئے رنز کا بار گراف۔ اطراف کا پیمانہ 0 سے 12 تک دو دو کے قدموں میں ہے۔ میچ 1: 6 رنز، میچ 2: 10 رنز، میچ 3: 8 رنز، میچ 4: 12 رنز۔",
    top=12, step=2)

lesson = practice_lesson(
 "11.4", script="exercise_11_4.py",
 title=T("Exercise 11.4 practice: mean, median and mode", "مشق 11.4 کی پریکٹس: اوسط، وسطانیہ اور عادہ"),
 outcome="Find the mean of data (and a missing value when the mean is given), the median for an odd and an even number of values, and the mode.",
 prerequisites=[DH_MEAN, DH_MEDIAN, DH_MODE_RANGE, DH_WORD_PROBLEMS],
 misconceptions=[
   {"id": "total_not_mean", "description": "Gives the total of the values as the mean, or divides by the wrong number of values."},
   {"id": "median_unsorted", "description": "Takes the middle value of the list as written, without putting the values in order first."},
   {"id": "median_even_one", "description": "With an even number of values, picks one of the two middle values instead of finding the number halfway between them."},
   {"id": "mode_vs_mean", "description": "Mixes up mode, median and mean, or gives the biggest value as the mode."},
   {"id": "missing_not_total", "description": "Gives the mean as the missing value, or forgets to multiply the mean by the number of values before taking the known ones away."},
   {"id": "mean_of_means", "description": "Finds the new mean by averaging the old mean and the new value, instead of using the total and the new number of values."},
 ],
 steps=[
   practice_intro("11.4",
     "Here you practise the mean, the median and the mode, a missing value when the mean is given, and when to use each.",
     "اس میں آپ اوسط، وسطانیہ اور عادہ، اوسط دیا ہو تو غائب قیمت، اور ہر ایک کب استعمال کرنا ہے، دہرائیں گے۔",
     "Exercise 11.4 is about mean, median and mode. Ready?", "مشق 11.4 اوسط، وسطانیہ اور عادہ کے بارے میں ہے۔ تیار؟"),
   ch("q1_mean", ("The mean of a list of numbers is found by:", "اعداد کی فہرست کا اوسط اس طرح نکلتا ہے:"),
      ("adding all the values and dividing by how many values there are", "سب قیمتیں جمع کر کے قیمتوں کی تعداد سے تقسیم کرنا", "Yes! Mean = total ÷ number of values.", "جی ہاں! اوسط = کل ÷ قیمتوں کی تعداد"),
      [("finding the middle value", "درمیانی قیمت ڈھونڈنا", "The middle value in order is the median.", "ترتیب میں درمیانی قیمت وسطانیہ ہے۔", "mode_vs_mean"),
       ("finding the value that appears most often", "وہ قیمت ڈھونڈنا جو سب سے زیادہ بار آئے", "That is the mode.", "یہ عادہ ہے۔", "mode_vs_mean")],
      0, qtype="recall"),
   {"id": "s_idea", "type": "explain",
    "character": say("thinking", "Mean shares out fairly, median is the middle, mode is the most common.", "اوسط برابر بانٹتا ہے، وسطانیہ بیچ میں ہے، عادہ سب سے عام ہے۔"),
    "text": T("Mean = total ÷ number of values. If the mean is given, total = mean × number of values, so a missing value = total − the known values. Median: put the values in order first. With an odd number of values it is the middle one. With an even number it is halfway between the two middle ones: add them and halve. Mode: the value that appears most often.",
              "اوسط = کل ÷ قیمتوں کی تعداد۔ اگر اوسط دیا ہو تو کل = اوسط × قیمتوں کی تعداد، اور غائب قیمت = کل − معلوم قیمتیں۔ وسطانیہ: پہلے قیمتیں ترتیب میں لکھیں۔ طاق تعداد ہو تو درمیانی قیمت ہے۔ جفت تعداد ہو تو دو درمیانی قیمتوں کے ٹھیک بیچ میں ہے: انہیں جمع کر کے آدھا کریں۔ عادہ: وہ قیمت جو سب سے زیادہ بار آئے۔")},
   nq("q2_mean", (f"Find the mean of {', '.join(map(str, A))}.", f"{'، '.join(map(str, A))} کا اوسط نکالیں۔"), Q2,
      ("Add the five values, then divide by 5.", "پانچوں قیمتیں جمع کریں، پھر 5 سے تقسیم کریں۔"),
      ("Right! The total is 50, and 50 ÷ 5 = 10.", "درست! کل 50 ہے، اور 50 ÷ 5 = 10"), ("12 + 7 + 9 + 15 + 7 = 50, and 50 ÷ 5 = 10.", "12 + 7 + 9 + 15 + 7 = 50، اور 50 ÷ 5 = 10"),
      [(50, "50 is the total. Divide by 5, the number of values: 10.", "50 کل ہے۔ قیمتوں کی تعداد 5 سے تقسیم کریں: 10", "total_not_mean"),
       (12, "12 is the first value. Add all five and divide by 5: 10.", "12 پہلی قیمت ہے۔ پانچوں جمع کر کے 5 سے تقسیم کریں: 10", "total_not_mean")], qtype="recall"),
   nq("q3_missing", (f"The mean of five numbers is {Q3_MEAN}. Four of them are {', '.join(map(str, Q3_KNOWN))}. What is the fifth number?", f"پانچ اعداد کا اوسط {Q3_MEAN} ہے۔ ان میں سے چار {'، '.join(map(str, Q3_KNOWN))} ہیں۔ پانچواں عدد کیا ہے؟"), Q3,
      ("Total = mean × 5. Then take away the four known numbers.", "کل = اوسط × 5۔ پھر چار معلوم اعداد گھٹائیں۔"),
      ("Right! Total 8 × 5 = 40, known 4 + 10 + 6 + 9 = 29, and 40 − 29 = 11.", "درست! کل 8 × 5 = 40، معلوم 4 + 10 + 6 + 9 = 29، اور 40 − 29 = 11"), ("40 − 29 = 11.", "40 − 29 = 11"),
      [(8, "8 is the mean. First find the total, 8 × 5 = 40, then take away 29: 11.", "8 اوسط ہے۔ پہلے کل 8 × 5 = 40 نکالیں، پھر 29 گھٹائیں: 11", "missing_not_total"),
       (40, "40 is the total of all five. Take away the four known numbers: 11.", "40 پانچوں کا کل ہے۔ چار معلوم اعداد گھٹائیں: 11", "missing_not_total")]),
   nq("q4_median_odd", (f"Find the median of {', '.join(map(str, B))}.", f"{'، '.join(map(str, B))} کا وسطانیہ نکالیں۔"), Q4,
      ("Put the numbers in order first, then take the middle one.", "پہلے اعداد کو ترتیب میں لکھیں، پھر درمیانی لیں۔"),
      ("Right! In order: 6, 8, 9, 11, 14, 17, 20. The middle one is 11.", "درست! ترتیب میں: 6، 8، 9، 11، 14، 17، 20۔ درمیانی 11 ہے۔"), ("Seven numbers: the 4th one in order is 11.", "سات اعداد: ترتیب میں چوتھا 11 ہے۔"),
      [(9, "9 is the middle of the list as written. Put them in order first: 11.", "9 لکھی ہوئی فہرست کا بیچ ہے۔ پہلے ترتیب میں لکھیں: 11", "median_unsorted"),
       (20, "20 is the biggest number, not the middle one. In order the middle is 11.", "20 سب سے بڑا عدد ہے، درمیانی نہیں۔ ترتیب میں درمیانی 11 ہے۔", "mode_vs_mean")]),
   nq("q5_median_even", (f"Find the median of {', '.join(map(str, C))}.", f"{'، '.join(map(str, C))} کا وسطانیہ نکالیں۔"), Q5,
      ("In order, there are two middle numbers. Go halfway between them.", "ترتیب میں دو درمیانی اعداد ہیں۔ ان کے ٹھیک بیچ میں جائیں۔"),
      ("Right! In order: 3, 5, 7, 9, 10, 12. The middle two are 7 and 9, and (7 + 9) ÷ 2 = 8.", "درست! ترتیب میں: 3، 5، 7، 9، 10، 12۔ درمیانی دو 7 اور 9 ہیں، اور (7 + 9) ÷ 2 = 8"), ("(7 + 9) ÷ 2 = 8.", "(7 + 9) ÷ 2 = 8"),
      [(7, "7 is only one of the two middle numbers. Halfway between 7 and 9 is 8.", "7 دو درمیانی اعداد میں سے صرف ایک ہے۔ 7 اور 9 کے ٹھیک بیچ میں 8 ہے۔", "median_even_one"),
       (9, "9 is only one of the two middle numbers. Halfway between 7 and 9 is 8.", "9 دو درمیانی اعداد میں سے صرف ایک ہے۔ 7 اور 9 کے ٹھیک بیچ میں 8 ہے۔", "median_even_one")]),
   nq("q6_mode", (f"Find the mode of {', '.join(map(str, D))}.", f"{'، '.join(map(str, D))} کا عادہ نکالیں۔"), Q6,
      ("Which number appears most often?", "کون سا عدد سب سے زیادہ بار آتا ہے؟"),
      ("Right! 4 appears three times, more than any other.", "درست! 4 تین بار آتا ہے، کسی بھی دوسرے سے زیادہ۔"), ("Count each: 4 appears 3 times, 6 appears 2 times.", "ہر ایک گنیں: 4 تین بار، 6 دو بار"),
      [(9, "9 is the biggest number, not the most common. The mode is 4.", "9 سب سے بڑا عدد ہے، سب سے عام نہیں۔ عادہ 4 ہے۔", "mode_vs_mean"),
       (3, "3 is how many times 4 appears. The mode is the number itself: 4.", "3 یہ ہے کہ 4 کتنی بار آیا۔ عادہ خود عدد ہے: 4", "mode_vs_mean")]),
   ch("q7_which", ("A shopkeeper wants to know which shoe size to order the most of. Which average helps most?", "ایک دکاندار جاننا چاہتا ہے کہ کون سا ناپ سب سے زیادہ منگوائے۔ کون سا اوسط سب سے زیادہ مدد کرتا ہے؟"),
      ("the mode (the most common size)", "عادہ (سب سے عام ناپ)", "Yes! The most common size sells the most.", "جی ہاں! سب سے عام ناپ سب سے زیادہ بکتا ہے۔"),
      [("the mean", "اوسط", "A mean such as 7.4 may not be a real shoe size.", "7.4 جیسا اوسط شاید اصل جوتے کا ناپ نہ ہو۔", "mode_vs_mean"),
       ("the total", "کل", "The total of the sizes tells nothing about which to order.", "ناپوں کا کل نہیں بتاتا کون سا منگوانا ہے۔", "total_not_mean")],
      1, qtype="apply"),
   nq("q8_new", (f"The mean of five numbers is {E_MEAN}. A sixth number, {E_NEW}, is added. What is the mean of the six numbers?", f"پانچ اعداد کا اوسط {E_MEAN} ہے۔ چھٹا عدد {E_NEW} شامل کیا جاتا ہے۔ چھ اعداد کا اوسط کیا ہے؟"), Q8,
      ("Old total = 10 × 5. Add the new number, then divide by 6.", "پرانا کل = 10 × 5۔ نیا عدد جمع کریں، پھر 6 سے تقسیم کریں۔"),
      ("Right! (50 + 16) ÷ 6 = 66 ÷ 6 = 11.", "درست! (50 + 16) ÷ 6 = 66 ÷ 6 = 11"), ("50 + 16 = 66, and 66 ÷ 6 = 11.", "50 + 16 = 66، اور 66 ÷ 6 = 11"),
      [(13, "13 averages 10 and 16, but the 10 stands for five numbers. Use the totals: 11.", "13، 10 اور 16 کا اوسط ہے، مگر 10 پانچ اعداد کا ہے۔ کل استعمال کریں: 11", "mean_of_means"),
       (66, "66 is the new total. Divide by 6: 11.", "66 نیا کل ہے۔ 6 سے تقسیم کریں: 11", "total_not_mean")]),
   with_fig(nq("q9_graph", ("The bar graph shows the runs scored in four matches. What is the mean number of runs per match?", "بار گراف چار میچوں میں بنائے گئے رنز دکھاتا ہے۔ فی میچ اوسط رنز کتنے ہیں؟"), Q9,
      ("Read the four bars, add them, divide by 4.", "چاروں ستون پڑھیں، جمع کریں، 4 سے تقسیم کریں۔"),
      ("Right! 6 + 10 + 8 + 12 = 36, and 36 ÷ 4 = 9.", "درست! 6 + 10 + 8 + 12 = 36، اور 36 ÷ 4 = 9"), ("36 ÷ 4 = 9.", "36 ÷ 4 = 9"),
      [(36, "36 is the total runs. Divide by 4 matches: 9.", "36 کل رنز ہیں۔ 4 میچوں سے تقسیم کریں: 9", "total_not_mean"),
       (12, "12 is the highest bar. The mean uses all four bars: 9.", "12 سب سے اونچا ستون ہے۔ اوسط میں چاروں ستون آتے ہیں: 9", "total_not_mean")]), F_RUNS),
   ch("q10_find_error", (f"Naila finds the median of {', '.join(map(str, G))}. She says it is 7, the middle number of the list. What went wrong?", f"نائلہ {'، '.join(map(str, G))} کا وسطانیہ نکالتی ہے۔ وہ کہتی ہے یہ 7 ہے، یعنی فہرست کا درمیانی عدد۔ کیا غلطی ہوئی؟"),
      ("She forgot to put the numbers in order first. In order, 1, 3, 5, 7, 9, the median is 5.", "وہ پہلے اعداد کو ترتیب میں لکھنا بھول گئی۔ ترتیب میں 1، 3، 5، 7، 9 کا وسطانیہ 5 ہے۔", "Yes! The median is the middle of the ordered list.", "جی ہاں! وسطانیہ ترتیب وار فہرست کا درمیانی عدد ہے۔"),
      [("Nothing. 7 is right.", "کوئی غلطی نہیں۔ 7 ٹھیک ہے۔", "7 is the middle of the list as written, but not in order.", "7 لکھی ہوئی فہرست کا بیچ ہے، مگر ترتیب میں نہیں۔", "median_unsorted"),
       ("She should have added them and divided by 5.", "اسے سب جمع کر کے 5 سے تقسیم کرنا چاہیے تھا۔", "That is the mean. The median needs the numbers in order.", "یہ اوسط ہے۔ وسطانیہ کے لیے اعداد کو ترتیب میں لکھنا پڑتا ہے۔", "mode_vs_mean")],
      0, qtype="find_error"),
   nq("q11_total", (f"The mean of {H_N} numbers is {H_MEAN}. What is their total?", f"{H_N} اعداد کا اوسط {H_MEAN} ہے۔ ان کا کل کیا ہے؟"), Q11,
      ("Total = mean × number of values.", "کل = اوسط × قیمتوں کی تعداد"),
      ("Right! 12 × 4 = 48.", "درست! 12 × 4 = 48"), ("Mean times the number of values: 12 × 4 = 48.", "اوسط ضرب قیمتوں کی تعداد: 12 × 4 = 48"),
      [(12, "12 is the mean. The total is 12 × 4 = 48.", "12 اوسط ہے۔ کل 12 × 4 = 48 ہے۔", "missing_not_total"),
       (3, "3 is 12 ÷ 4, the wrong way round. Multiply: 48.", "3 یعنی 12 ÷ 4، الٹا۔ ضرب دیں: 48", "missing_not_total")]),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! Mean, median and mode are all yours.", "شاباش! اوسط، وسطانیہ اور عادہ سب آپ کے ہیں۔"),
    "text": T("Mean = total ÷ number of values, and total = mean × number of values. Median: order the values; the middle one for an odd count, halfway between the two middle ones for an even count. Mode: the most common value. A new value changes the total and the count, so use the totals.",
              "اوسط = کل ÷ قیمتوں کی تعداد، اور کل = اوسط × قیمتوں کی تعداد۔ وسطانیہ: قیمتیں ترتیب میں لکھیں؛ طاق تعداد میں درمیانی، جفت تعداد میں دو درمیانی قیمتوں کے ٹھیک بیچ میں۔ عادہ: سب سے عام قیمت۔ نئی قیمت کل اور تعداد دونوں بدلتی ہے، اس لیے کل استعمال کریں۔"),
    "points": [T("Median: put them in order first.", "وسطانیہ: پہلے ترتیب میں لکھیں۔"),
               T("Total = mean × how many.", "کل = اوسط × کتنے۔")]},
 ],
 bank=[
   {"id": "qb_mode", "type": "recall", "step": ch("qb_mode", ("The value that appears most often in a list is called the:", "فہرست میں جو قیمت سب سے زیادہ بار آئے وہ کہلاتی ہے:"),
      ("mode", "عادہ", "Yes! The mode is the most common value.", "جی ہاں! عادہ سب سے عام قیمت ہے۔"),
      [("median", "وسطانیہ", "The median is the middle value in order.", "وسطانیہ ترتیب میں درمیانی قیمت ہے۔", "mode_vs_mean"),
       ("mean", "اوسط", "The mean is the total divided by how many.", "اوسط کل ÷ تعداد ہے۔", "mode_vs_mean")],
      0, qtype=None)},
   {"id": "qb_mean", "type": "apply", "step": nq("qb_mean", (f"Find the mean of {', '.join(map(str, QB_DATA))}.", f"{'، '.join(map(str, QB_DATA))} کا اوسط نکالیں۔"), QB,
      ("Add the four values, then divide by 4.", "چاروں قیمتیں جمع کریں، پھر 4 سے تقسیم کریں۔"),
      ("Right! 9 + 5 + 11 + 7 = 32, and 32 ÷ 4 = 8.", "درست! 9 + 5 + 11 + 7 = 32، اور 32 ÷ 4 = 8"), ("32 ÷ 4 = 8.", "32 ÷ 4 = 8"),
      [(32, "32 is the total. Divide by 4, the number of values: 8.", "32 کل ہے۔ قیمتوں کی تعداد 4 سے تقسیم کریں: 8", "total_not_mean"),
       (11, "11 is the biggest value. The mean uses all four: 8.", "11 سب سے بڑی قیمت ہے۔ اوسط میں چاروں آتی ہیں: 8", "total_not_mean")], qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": ch("qb_find_error", ("Yusuf finds the mean of 6, 8, 10, 12, 14 by adding them (50) and dividing by 4. What went wrong?", "یوسف 6، 8، 10، 12، 14 کا اوسط انہیں جمع کر کے (50) اور 4 سے تقسیم کر کے نکالتا ہے۔ کیا غلطی ہوئی؟"),
      ("There are 5 values, so divide by 5: 50 ÷ 5 = 10.", "5 قیمتیں ہیں، تو 5 سے تقسیم کریں: 50 ÷ 5 = 10", "Yes! Divide by how many values there are.", "جی ہاں! قیمتوں کی تعداد سے تقسیم کریں۔"),
      [("Nothing. 12.5 is right.", "کوئی غلطی نہیں۔ 12.5 ٹھیک ہے۔", "There are five values, not four.", "قیمتیں پانچ ہیں، چار نہیں۔", "total_not_mean"),
       ("He should not add them, but pick the middle one.", "اسے جمع نہیں کرنا چاہیے، بلکہ درمیانی چننی چاہیے۔", "That is the median. The mean uses the total.", "یہ وسطانیہ ہے۔ اوسط میں کل استعمال ہوتا ہے۔", "mode_vs_mean")],
      1, qtype=None)},
 ],
 review=[
   {"id": "r_median", "type": "apply", "step": nq("r_median", (f"Find the median of {', '.join(map(str, R1_DATA))}.", f"{'، '.join(map(str, R1_DATA))} کا وسطانیہ نکالیں۔"), R1,
      ("Put them in order first.", "پہلے ترتیب میں لکھیں۔"),
      ("Right! In order: 4, 7, 10, 13, 21. The middle one is 10.", "درست! ترتیب میں: 4، 7، 10، 13، 21۔ درمیانی 10 ہے۔"), ("The 3rd of five in order is 10.", "پانچ میں سے ترتیب میں تیسرا 10 ہے۔"),
      [(21, "21 is the middle of the list as written. In order the middle is 10.", "21 لکھی ہوئی فہرست کا بیچ ہے۔ ترتیب میں درمیانی 10 ہے۔", "median_unsorted")], qtype=None)},
   {"id": "r_mode", "type": "apply", "step": nq("r_mode", (f"Find the mode of {', '.join(map(str, R2_DATA))}.", f"{'، '.join(map(str, R2_DATA))} کا عادہ نکالیں۔"), R2,
      ("Which number appears most often?", "کون سا عدد سب سے زیادہ بار آتا ہے؟"),
      ("Right! 2 appears three times.", "درست! 2 تین بار آتا ہے۔"), ("Count: 2 appears 3 times, 5 appears 2 times.", "گنیں: 2 تین بار، 5 دو بار"),
      [(9, "9 is the biggest number, not the most common. The mode is 2.", "9 سب سے بڑا عدد ہے، سب سے عام نہیں۔ عادہ 2 ہے۔", "mode_vs_mean")], qtype=None)},
 ],
 glossary=[T("Average (mean)", "اوسط"), T("Median", "وسطانیہ"), T("Mode", "عادہ (موڈ)"), T("Total", "کل"), T("In order", "ترتیب میں"), T("Middle value", "درمیانی قیمت")],
 flashcards=[
   {"id": "f_median", "front": T("How do you find the median when there are two middle values?", "جب دو درمیانی قیمتیں ہوں تو وسطانیہ کیسے نکالتے ہیں؟"),
    "back": T("Put the values in order, add the two middle ones and halve.", "قیمتیں ترتیب میں لکھیں، دو درمیانی جمع کریں اور آدھا کریں۔")},
   {"id": "f_missing", "front": T("The mean of 5 numbers is 8 and four are known. How do you find the fifth?", "5 اعداد کا اوسط 8 ہے اور چار معلوم ہیں۔ پانچواں کیسے نکالیں؟"),
    "back": T("Total = 8 × 5 = 40. Take away the four known numbers.", "کل = 8 × 5 = 40۔ چار معلوم اعداد گھٹائیں۔")},
 ],
 home_task={"id": "h_average", "text": T(
   "Write down the number of letters in the first 11 words of a page of your book. Put them in order and find the median, find the mode, and find the mean (total ÷ 11). Say which one you think describes a typical word best.",
   "اپنی کتاب کے ایک صفحے کے پہلے 11 الفاظ میں حروف کی تعداد لکھیں۔ انہیں ترتیب میں لکھیں اور وسطانیہ، عادہ اور اوسط (کل ÷ 11) نکالیں۔ بتائیں کہ آپ کے خیال میں کون سا ایک عام لفظ کو سب سے اچھا بیان کرتا ہے۔")},
 notes=["Covers the mean (q2, q9, qb_mean, qb_find_error), a missing value or a total from the mean (q3, q11), the median for an odd and an even number of values (q4, q5, q10, r_median), the mode (q6, qb_mode, r_mode), choosing an average (q7) and a changed mean (q8).",
        "Each wrong answer is a real mistake: giving the total as the mean, taking the middle of an unordered list, picking one of the two middle values, mixing up mean, median and mode, and averaging the old mean with the new value.",
        "Urdu terms to check: اوسط, وسطانیہ, عادہ (موڈ), کل, ترتیب میں and درمیانی قیمت, all as in the existing Data Handling lessons. No new Urdu terms were added."],
 minutes=18,
)
write(lesson)
