"""Chapter 11 test (Data Management), set out like the book's review exercise and
a board paper: multiple choice, short questions, then longer problems. The
questions are new; only the kinds of question follow the book."""
from fractions import Fraction as F
from statistics import mean, median, mode

from common import (T, say, nq, ch, write, book_ref, REVIEW, CHAPTER_11_TEST,
                    DH_TABLES, DH_KINDS, DH_BAR_GRAPHS, DH_PIE_CHARTS, DH_MEAN, DH_MEDIAN,
                    DH_MODE_RANGE, DH_WORD_PROBLEMS)
from figs import bar_graph, double_bar_graph, pie_chart, with_fig

SKILL = CHAPTER_11_TEST
FULL = 360


def whole(x):
    assert x == int(x), x
    return int(x)


def angle(value, total):
    a = F(value, total) * FULL
    assert a.denominator == 1
    return int(a)


def mcq(id, en, ur, right, wrongs, pos):
    return ch(id, ("MCQ: " + en, "کثیر انتخابی: " + ur), right, wrongs, pos, qtype="exam_style")


def short(id, en, ur, answer, hint, good, bad, wrongs=()):
    return nq(id, ("Short question: " + en, "مختصر سوال: " + ur), answer, hint, good, bad, wrongs, qtype="exam_style")


def long_q(id, en, ur, answer, hint, good, bad, wrongs=()):
    return nq(id, ("Long question: " + en, "تفصیلی سوال: " + ur), answer, hint, good, bad, wrongs, qtype="exam_style")


# MCQ 3: juice sold on four days, scale in tens
JUICE = [25, 40, 15, 35]
M3 = JUICE[0] + JUICE[1]
assert M3 == 65 and JUICE[1] == 40 and JUICE[0] + JUICE[3] == 60 and sum(JUICE) - JUICE[2] == 100
M3_FIG = bar_graph(JUICE, ["Mo", "Tu", "We", "Th"],
    "A bar graph of cups of juice sold on four days. The side scale goes up in tens from 0 to 40. Monday 25, Tuesday 40, Wednesday 15, Thursday 35.",
    "چار دنوں میں بکنے والے جوس کے کپوں کا بار گراف۔ اطراف کا پیمانہ 0 سے 40 تک دس دس کے قدموں میں ہے۔ پیر 25، منگل 40، بدھ 15، جمعرات 35۔",
    top=40, step=10)
# MCQ 4: a quarter of a pie chart
M4 = angle(25, 100)
assert M4 == 90 and 25 != M4 and angle(1, 2) == 180
# MCQ 5: median of five values, unsorted
M5_DATA = [3, 8, 5, 10, 4]
M5 = whole(median(M5_DATA))
assert M5 == 5 and M5_DATA[2] == 5 and mean(M5_DATA) == 6 and sorted(M5_DATA) == [3, 4, 5, 8, 10]
# the middle of the list as written is 5 too, so use another set to separate the mistakes
M5_DATA = [7, 2, 9, 4, 6]
M5 = whole(median(M5_DATA))
assert M5 == 6 and M5_DATA[2] == 9 and mean(M5_DATA) == 5.6 and sorted(M5_DATA) == [2, 4, 6, 7, 9]
# MCQ 6: mode
M6_DATA = [5, 7, 5, 9, 7, 5]
M6 = mode(M6_DATA)
assert M6 == 5 and M6_DATA.count(7) == 2 and M6_DATA.count(5) == 3

# short questions
S1_DATA = [14, 18, 10, 16, 12]
S1 = whole(mean(S1_DATA))
assert S1 == 14 and sum(S1_DATA) == 70
S2_DATA = [8, 14, 6, 18, 10, 20]
S2 = whole(median(S2_DATA))
assert sorted(S2_DATA) == [6, 8, 10, 14, 18, 20] and S2 == 12 and S2_DATA[2:4] == [6, 18]
S3_V, S3_T = 24, 144
S3 = angle(S3_V, S3_T)
assert S3 == 60 and F(S3_V, S3_T) * 100 != S3
BASKETS = [35, 20, 45, 30]
S4 = BASKETS[2] - BASKETS[1]
assert S4 == 25 and sum(BASKETS) == 130
S4_FIG = bar_graph(BASKETS, ["A", "B", "C", "D"],
    "A bar graph of baskets of fruit sold by four shops A, B, C and D. The side scale goes up in tens from 0 to 50. Shop A 35, shop B 20, shop C 45, shop D 30.",
    "چار دکانوں A، B، C اور D کی بیچی گئی پھلوں کی ٹوکریوں کا بار گراف۔ اطراف کا پیمانہ 0 سے 50 تک دس دس کے قدموں میں ہے۔ دکان A کی 35، دکان B کی 20، دکان C کی 45، دکان D کی 30۔",
    top=50, step=10)

# long questions
L1_MEAN, L1_N, L1_KNOWN = 9, 6, [4, 12, 7, 10, 8]
L1_SIXTH = L1_MEAN * L1_N - sum(L1_KNOWN)
L1_ALL = sorted(L1_KNOWN + [L1_SIXTH])
L1 = whole(median(L1_ALL))
assert L1_SIXTH == 13 and L1_ALL == [4, 7, 8, 10, 12, 13] and L1 == 9 and mean(L1_ALL) == L1_MEAN
L2_T, L2_X, L2_Y = 240, 35, 25
L2_Z = 100 - L2_X - L2_Y
L2 = whole(F(L2_Z, 100) * L2_T)
assert L2_Z == 40 and L2 == 96 and F(L2_X + L2_Y, 100) * L2_T == 144
L2_ANG = [angle(L2_X, 100), angle(L2_Y, 100), angle(L2_Z, 100)]
assert L2_ANG == [126, 90, 144] and sum(L2_ANG) == FULL
L2_FIG = pie_chart([(L2_ANG[0], "X", f"{L2_X}%"), (L2_ANG[1], "Y", f"{L2_Y}%"), (L2_ANG[2], "Z", "?")],
    "A pie chart of 240 pupils with three sectors X, Y and Z. X is 35 percent and Y is 25 percent. The sector Z is marked with a question mark.",
    "240 طلبہ کا دائری نقشہ جس کے تین ٹکڑے X، Y اور Z ہیں۔ X کا 35 فیصد اور Y کا 25 فیصد ہے۔ ٹکڑے Z پر سوالیہ نشان ہے۔")
L3_PAIRS = [(20, 15), (10, 25), (15, 15)]
L3_BOYS, L3_GIRLS = sum(b for b, _ in L3_PAIRS), sum(g for _, g in L3_PAIRS)
L3 = L3_GIRLS - L3_BOYS
assert (L3_BOYS, L3_GIRLS, L3) == (45, 55, 10) and L3_BOYS + L3_GIRLS == 100
L3_FIG = double_bar_graph(L3_PAIRS, ["A", "B", "C"],
    "A double bar graph of boys (filled bar) and girls (empty bar) in three classes A, B and C. The scale goes up in fives. Class A: 20 boys and 15 girls. Class B: 10 boys and 25 girls. Class C: 15 boys and 15 girls.",
    "تین جماعتوں A، B اور C میں لڑکوں (بھرا ستون) اور لڑکیوں (خالی ستون) کا دوہرا بار گراف۔ پیمانہ پانچ پانچ کے قدموں میں ہے۔ جماعت A: 20 لڑکے اور 15 لڑکیاں۔ جماعت B: 10 لڑکے اور 25 لڑکیاں۔ جماعت C: 15 لڑکے اور 15 لڑکیاں۔",
    top=25, step=5)
L4_N1, L4_M1, L4_N2, L4_M2 = 4, 7, 6, 12
L4_TOTAL = L4_N1 * L4_M1 + L4_N2 * L4_M2
L4 = whole(F(L4_TOTAL, L4_N1 + L4_N2))
assert L4_TOTAL == 100 and L4 == 10 and (L4_M1 + L4_M2) / 2 != L4

# question bank and review
QB_DATA = [6, 9, 12]
QB1 = whole(mean(QB_DATA))
assert QB1 == 9
QB2 = angle(1, 3)
assert QB2 == 120
QB3_DATA = [15, 3, 9, 21, 12]
QB3 = whole(median(QB3_DATA))
assert QB3 == 12 and QB3_DATA[2] == 9
R1_DATA = [4, 8, 8, 5, 8, 4]
R1 = mode(R1_DATA)
assert R1 == 8
R2 = angle(3, 12)
assert R2 == 90

lesson = {
 "id": "g6-maths-10-chapter-11-test",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Answer exam-style questions on the whole of chapter 11: grouped and ungrouped data, discrete and continuous data, reading bar graphs and pie charts, sector angles, and the mean, median and mode.",
                      "textbook": book_ref("Review Exercise 11")}],
 "skills": [SKILL],
 "title": T("Chapter 11 test: Data Management", "باب 11 کا ٹیسٹ: مواد کا انتظام"),
 "estimated_minutes": 25,
 "prerequisites": [{"skill": s} for s in (DH_TABLES, DH_KINDS, DH_BAR_GRAPHS, DH_PIE_CHARTS, DH_MEAN, DH_MEDIAN, DH_MODE_RANGE, DH_WORD_PROBLEMS)],
 "misconceptions": [
   {"id": "grouped_ungrouped_mix", "description": "Calls a list of single values grouped, or a table of classes ungrouped."},
   {"id": "measured_is_counted", "description": "Mixes up counted (discrete) and measured (continuous) data."},
   {"id": "scale_misread", "description": "Reads a bar that ends between two marks as the lower mark, or leaves out a bar when adding."},
   {"id": "diff_as_total", "description": "Adds two bars when asked how many more, or subtracts when asked for the total."},
   {"id": "pie_total_wrong", "description": "Uses 100 or 180 instead of 360 degrees for the whole pie, or gives the percentage as the angle."},
   {"id": "median_unsorted", "description": "Takes the middle value of the list as written, without putting the values in order first."},
   {"id": "total_not_mean", "description": "Gives the total as the mean, or gives the biggest value as the mode or the mean."},
   {"id": "answer_is_other_quantity", "description": "Stops at a middle step, such as the missing value, and gives it as the answer."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["exam_style"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_exam_mean", "type": "exam_style", "step": nq(
     "qb_exam_mean", ("Find the mean of 6, 9 and 12.", "6، 9 اور 12 کا اوسط نکالیں۔"), QB1,
     ("Add them, then divide by 3.", "جمع کریں، پھر 3 سے تقسیم کریں۔"),
     ("Correct: 27 ÷ 3 = 9.", "درست: 27 ÷ 3 = 9"), ("6 + 9 + 12 = 27, and 27 ÷ 3 = 9.", "6 + 9 + 12 = 27، اور 27 ÷ 3 = 9"),
     [(27, "27 is the total. Divide by 3: 9.", "27 کل ہے۔ 3 سے تقسیم کریں: 9", "total_not_mean")], qtype=None)},
   {"id": "qb_exam_angle", "type": "exam_style", "step": nq(
     "qb_exam_angle", ("One third of the people in a pie chart like mangoes. What is the angle of the mango sector, in degrees?", "دائری نقشے میں ایک تہائی لوگوں کو آم پسند ہیں۔ آم کے ٹکڑے کا زاویہ درجوں میں کتنا ہے؟"), QB2,
     ("One third of 360.", "360 کا ایک تہائی۔"),
     ("Correct: 360 ÷ 3 = 120°.", "درست: 360 ÷ 3 = 120°"), ("360 ÷ 3 = 120.", "360 ÷ 3 = 120"),
     [(33, "33 is about the percentage. The angle is 360 ÷ 3 = 120.", "33 تقریباً فیصد ہے۔ زاویہ 360 ÷ 3 = 120 ہے۔", "pie_total_wrong")], qtype=None)},
   {"id": "qb_exam_median", "type": "exam_style", "step": nq(
     "qb_exam_median", ("Find the median of 15, 3, 9, 21, 12.", "15، 3، 9، 21، 12 کا وسطانیہ نکالیں۔"), QB3,
     ("Put them in order first.", "پہلے ترتیب میں لکھیں۔"),
     ("Correct: 3, 9, 12, 15, 21. The middle one is 12.", "درست: 3، 9، 12، 15، 21۔ درمیانی 12 ہے۔"), ("The 3rd of five in order is 12.", "پانچ میں سے ترتیب میں تیسرا 12 ہے۔"),
     [(9, "9 is the middle of the list as written. In order it is 12.", "9 لکھی ہوئی فہرست کا بیچ ہے۔ ترتیب میں 12 ہے۔", "median_unsorted")], qtype=None)},
 ]},
 "flashcards": [
   {"id": "f_angle", "front": T("Sector angle of a pie chart?", "دائری نقشے کے ٹکڑے کا زاویہ؟"),
    "back": T("Value ÷ total × 360°.", "قیمت ÷ کل × 360°")},
   {"id": "f_avgs", "front": T("Mean, median, mode?", "اوسط، وسطانیہ، عادہ؟"),
    "back": T("Mean: total ÷ how many. Median: the middle value in order. Mode: the most common value.", "اوسط: کل ÷ تعداد۔ وسطانیہ: ترتیب میں درمیانی قیمت۔ عادہ: سب سے عام قیمت۔")},
 ],
 "home_tasks": [{"id": "h_paper", "text": T(
   "Do Review Exercise 11 in your maths book in your notebook, setting out the working the way this test's answers do: write the rule you use, put in the numbers, work out the answer. Draw the graphs and pie charts with a ruler and protractor. Ask your teacher to check it.",
   "اپنی ریاضی کی کتاب کی اعادی مشق 11 اپنی کاپی میں حل کریں، اور کام اس ٹیسٹ کے جوابات کی طرح لکھیں: جو اصول استعمال کریں وہ لکھیں، اعداد رکھیں، جواب نکالیں۔ گراف اور دائری نقشے پیمانے اور زاویہ پیما سے بنائیں۔ اپنے استاد سے جانچ کروائیں۔")}],
 "glossary": [T("Multiple choice", "کثیر انتخابی"), T("Short question", "مختصر سوال"), T("Long question", "تفصیلی سوال"),
              T("Model answer", "نمونہ جواب"), T("Review exercise", "اعادی مشق")],
 "steps": [
   {"id": "s1_paper", "type": "explain",
    "character": say("encouraging", "This is a test of the whole chapter, like the book's review exercise. Read each question carefully!",
                     "یہ پورے باب کا ٹیسٹ ہے، کتاب کی اعادی مشق کی طرح۔ ہر سوال غور سے پڑھیں!"),
    "text": T("This test goes with Review Exercise 11 of your maths book (PCTB Mathematics 6). It has three parts, like an exam paper: multiple choice questions (choose one answer), short questions (a few lines of working), and longer problems (full working in your notebook, then the final answer). The questions are new, not the book's. Use your notebook for the working.",
              "یہ ٹیسٹ آپ کی ریاضی کی کتاب (پنجاب ٹیکسٹ بک بورڈ، ریاضی 6) کی اعادی مشق 11 کے ساتھ ہے۔ اس کے تین حصے ہیں، امتحانی پرچے کی طرح: کثیر انتخابی سوال (ایک جواب چنیں)، مختصر سوال (چند سطروں کا کام)، اور تفصیلی سوالات (کاپی میں پورا کام، پھر آخری جواب)۔ سوال نئے ہیں، کتاب والے نہیں۔ کام کے لیے اپنی کاپی استعمال کریں۔")},
   mcq("m1_grouped", "A table shows the ages of children in classes 5-9, 10-14 and 15-19, with how many children are in each class. This is:", "ایک جدول بچوں کی عمریں گروہوں 5-9، 10-14 اور 15-19 میں دکھاتا ہے، اور ہر گروہ میں بچوں کی تعداد بتاتا ہے۔ یہ ہے:",
       ("grouped data", "گروہ بند مواد", "Correct: the values are put in classes.", "درست: قیمتیں گروہوں میں رکھی گئی ہیں۔"),
       [("ungrouped data", "غیر گروہ بند مواد", "Ungrouped data lists every value on its own.", "غیر گروہ بند مواد ہر قیمت الگ لکھتا ہے۔", "grouped_ungrouped_mix"),
        ("continuous data", "مسلسل مواد", "Continuous is about measuring. This table is about classes.", "مسلسل ناپنے کے بارے میں ہے۔ یہ جدول گروہوں کے بارے میں ہے۔", "grouped_ungrouped_mix"),
        ("a pie chart", "دائری نقشہ", "A pie chart is a picture. This is a table.", "دائری نقشہ تصویر ہے۔ یہ جدول ہے۔", "grouped_ungrouped_mix")], 0),
   mcq("m2_discrete", "Which one of these is discrete data?", "ان میں سے کون سا منفصل مواد ہے؟",
       ("the number of eggs in a basket", "ٹوکری میں انڈوں کی تعداد", "Correct: eggs are counted.", "درست: انڈے گنے جاتے ہیں۔"),
       [("the length of a rope", "رسی کی لمبائی", "Length is measured, so continuous.", "لمبائی ناپی جاتی ہے، تو مسلسل۔", "measured_is_counted"),
        ("the weight of a mango", "آم کا وزن", "Weight is measured, so continuous.", "وزن ناپا جاتا ہے، تو مسلسل۔", "measured_is_counted"),
        ("the time taken to run a race", "دوڑ میں لگنے والا وقت", "Time is measured, so continuous.", "وقت ناپا جاتا ہے، تو مسلسل۔", "measured_is_counted")], 2),
   with_fig(mcq("m3_juice", "The bar graph shows cups of juice sold. How many cups were sold on Monday (Mo) and Tuesday (Tu) together?", "بار گراف بکنے والے جوس کے کپ دکھاتا ہے۔ پیر (Mo) اور منگل (Tu) کو ملا کر کتنے کپ بکے؟",
       ("65", "65", "Correct: 25 + 40 = 65. Monday's bar is halfway between 20 and 30.", "درست: 25 + 40 = 65۔ پیر کا ستون 20 اور 30 کے ٹھیک بیچ میں ہے۔"),
       [("60", "60", "That reads Monday as 20. The bar is halfway between 20 and 30: 25.", "اس میں پیر کو 20 پڑھا گیا۔ ستون 20 اور 30 کے بیچ میں ہے: 25", "scale_misread"),
        ("40", "40", "That is Tuesday alone. Add Monday's 25.", "یہ صرف منگل ہے۔ پیر کے 25 بھی جمع کریں۔", "scale_misread"),
        ("15", "15", "That is 40 − 25, the difference. 'Together' means add.", "یہ 40 − 25 ہے، فرق۔ 'ملا کر' کا مطلب جمع ہے۔", "diff_as_total")], 1), M3_FIG),
   mcq("m4_quarter", "A sector is 25% of a pie chart. Its angle is:", "دائری نقشے کا ایک ٹکڑا 25٪ ہے۔ اس کا زاویہ ہے:",
       ("90°", "90°", "Correct: 25 ÷ 100 × 360 = 90.", "درست: 25 ÷ 100 × 360 = 90"),
       [("25°", "25°", "25 is the percentage. A quarter of 360° is 90°.", "25 فیصد ہے۔ 360° کا چوتھائی 90° ہے۔", "pie_total_wrong"),
        ("180°", "180°", "180° is half the circle.", "180° آدھا دائرہ ہے۔", "pie_total_wrong"),
        ("100°", "100°", "A pie chart is 360°, not 100°.", "دائری نقشہ 360° کا ہے، 100° کا نہیں۔", "pie_total_wrong")], 3),
   mcq("m5_median", f"The median of {', '.join(map(str, M5_DATA))} is:", f"{'، '.join(map(str, M5_DATA))} کا وسطانیہ ہے:",
       ("6", "6", "Correct: in order 2, 4, 6, 7, 9, the middle is 6.", "درست: ترتیب میں 2، 4، 6، 7، 9 کا بیچ 6 ہے۔"),
       [("9", "9", "9 is the middle of the list as written. Put them in order first.", "9 لکھی ہوئی فہرست کا بیچ ہے۔ پہلے ترتیب میں لکھیں۔", "median_unsorted"),
        ("5.6", "5.6", "That is the mean (28 ÷ 5). The median is the middle value: 6.", "یہ اوسط ہے (28 ÷ 5)۔ وسطانیہ درمیانی قیمت ہے: 6", "total_not_mean"),
        ("7", "7", "7 is the second from the end in order. The middle is 6.", "7 ترتیب میں آخر سے دوسرا ہے۔ درمیانی 6 ہے۔", "median_unsorted")], 0),
   mcq("m6_mode", f"The mode of {', '.join(map(str, M6_DATA))} is:", f"{'، '.join(map(str, M6_DATA))} کا عادہ ہے:",
       ("5", "5", "Correct: 5 appears three times.", "درست: 5 تین بار آتا ہے۔"),
       [("7", "7", "7 appears two times; 5 appears three times.", "7 دو بار آتا ہے؛ 5 تین بار۔", "total_not_mean"),
        ("9", "9", "9 is the biggest number, not the most common.", "9 سب سے بڑا عدد ہے، سب سے عام نہیں۔", "total_not_mean"),
        ("3", "3", "3 is how many times 5 appears. The mode is 5.", "3 یہ ہے کہ 5 کتنی بار آیا۔ عادہ 5 ہے۔", "total_not_mean")], 1),
   {"id": "s_short", "type": "explain",
    "text": T("Short questions. Work each one out in your notebook, then type the answer.",
              "مختصر سوال۔ ہر ایک اپنی کاپی میں حل کریں، پھر جواب لکھیں۔")},
   short("q1_mean", f"Find the mean of the marks {', '.join(map(str, S1_DATA))}.", f"نمبروں {'، '.join(map(str, S1_DATA))} کا اوسط نکالیں۔",
      S1, ("Total ÷ number of values.", "کل ÷ قیمتوں کی تعداد"),
      ("Correct: 70 ÷ 5 = 14.", "درست: 70 ÷ 5 = 14"),
      ("Model answer: total = 14 + 18 + 10 + 16 + 12 = 70. Mean = 70 ÷ 5 = 14.", "نمونہ جواب: کل = 14 + 18 + 10 + 16 + 12 = 70۔ اوسط = 70 ÷ 5 = 14"),
      [(70, "70 is the total. Divide by 5: 14.", "70 کل ہے۔ 5 سے تقسیم کریں: 14", "total_not_mean"),
       (18, "18 is the biggest mark. The mean uses all five: 14.", "18 سب سے بڑا نمبر ہے۔ اوسط میں پانچوں آتے ہیں: 14", "total_not_mean")]),
   short("q2_median", f"Find the median of {', '.join(map(str, S2_DATA))}.", f"{'، '.join(map(str, S2_DATA))} کا وسطانیہ نکالیں۔",
      S2, ("Put them in order. With six numbers, go halfway between the middle two.", "ترتیب میں لکھیں۔ چھ اعداد ہوں تو درمیانی دو کے ٹھیک بیچ میں جائیں۔"),
      ("Correct: 6, 8, 10, 14, 18, 20. (10 + 14) ÷ 2 = 12.", "درست: 6، 8، 10، 14، 18، 20۔ (10 + 14) ÷ 2 = 12"),
      ("Model answer: in order 6, 8, 10, 14, 18, 20. The middle two are 10 and 14. Median = (10 + 14) ÷ 2 = 12.", "نمونہ جواب: ترتیب میں 6، 8، 10، 14، 18، 20۔ درمیانی دو 10 اور 14 ہیں۔ وسطانیہ = (10 + 14) ÷ 2 = 12"),
      [(6, "6 and 18 are the middle two of the list as written. Put them in order first: 12.", "6 اور 18 لکھی ہوئی فہرست کے درمیانی دو ہیں۔ پہلے ترتیب میں لکھیں: 12", "median_unsorted"),
       (10, "10 is only one of the two middle numbers. Halfway between 10 and 14 is 12.", "10 دو درمیانی اعداد میں سے صرف ایک ہے۔ 10 اور 14 کے ٹھیک بیچ میں 12 ہے۔", "median_unsorted")]),
   short("q3_angle", f"In a pie chart of {S3_T} pupils, {S3_V} like drawing best. Find the angle of the drawing sector, in degrees.", f"{S3_T} طلبہ کے دائری نقشے میں {S3_V} کو ڈرائنگ سب سے زیادہ پسند ہے۔ ڈرائنگ کے ٹکڑے کا زاویہ درجوں میں نکالیں۔",
      S3, ("Angle = value ÷ total × 360.", "زاویہ = قیمت ÷ کل × 360"),
      ("Correct: 24 ÷ 144 × 360 = 60°.", "درست: 24 ÷ 144 × 360 = 60°"),
      ("Model answer: 24 ÷ 144 = 1/6, and 1/6 of 360 is 60°.", "نمونہ جواب: 24 ÷ 144 = 1/6، اور 360 کا 1/6 یعنی 60°"),
      [(24, "24 is the number of pupils. The angle is 24 ÷ 144 × 360 = 60.", "24 طلبہ کی تعداد ہے۔ زاویہ 24 ÷ 144 × 360 = 60 ہے۔", "pie_total_wrong"),
       (17, "17 is about 24 ÷ 144 × 100, a percentage. Multiply by 360: 60.", "17 تقریباً 24 ÷ 144 × 100 ہے، یعنی فیصد۔ 360 سے ضرب دیں: 60", "pie_total_wrong")]),
   with_fig(short("q4_baskets", "The bar graph shows baskets of fruit sold by four shops. How many more baskets did shop C sell than shop B?", "بار گراف چار دکانوں کی بیچی گئی پھلوں کی ٹوکریاں دکھاتا ہے۔ دکان C نے دکان B سے کتنی ٹوکریاں زیادہ بیچیں؟",
      S4, ("Read both bars, then subtract.", "دونوں ستون پڑھیں، پھر گھٹائیں۔"),
      ("Correct: 45 − 20 = 25.", "درست: 45 − 20 = 25"),
      ("Model answer: shop C sold 45 and shop B sold 20, so 45 − 20 = 25 more baskets.", "نمونہ جواب: دکان C نے 45 اور دکان B نے 20 بیچیں، تو 45 − 20 = 25 ٹوکریاں زیادہ"),
      [(65, "65 is 45 + 20. 'How many more' means subtract: 25.", "65 یعنی 45 + 20۔ 'کتنی زیادہ' کا مطلب گھٹانا ہے: 25", "diff_as_total"),
       (45, "45 is shop C alone. Take away shop B's 20: 25.", "45 صرف دکان C ہے۔ دکان B کے 20 گھٹائیں: 25", "diff_as_total")]), S4_FIG),
   {"id": "s_long", "type": "explain",
    "text": T("Longer problems. Write the rule and full working in your notebook, then type the final answer.",
              "تفصیلی سوالات۔ اپنی کاپی میں اصول اور پورا کام لکھیں، پھر آخری جواب لکھیں۔")},
   long_q("l1_mean_median", f"The mean of six numbers is {L1_MEAN}. Five of them are {', '.join(map(str, L1_KNOWN))}. Find the sixth number, and then the median of all six numbers.", f"چھ اعداد کا اوسط {L1_MEAN} ہے۔ ان میں سے پانچ {'، '.join(map(str, L1_KNOWN))} ہیں۔ چھٹا عدد نکالیں، پھر چھ کے چھ اعداد کا وسطانیہ نکالیں۔",
      L1, ("Total = 9 × 6. Take away the five known numbers. Then order all six and go halfway between the middle two.", "کل = 9 × 6۔ پانچ معلوم اعداد گھٹائیں۔ پھر چھ کو ترتیب میں لکھیں اور درمیانی دو کے ٹھیک بیچ میں جائیں۔"),
      ("Correct: sixth number = 54 − 41 = 13. In order 4, 7, 8, 10, 12, 13: (8 + 10) ÷ 2 = 9.", "درست: چھٹا عدد = 54 − 41 = 13۔ ترتیب میں 4، 7، 8، 10، 12، 13: (8 + 10) ÷ 2 = 9"),
      ("Model answer: total = 9 × 6 = 54. Known: 4 + 12 + 7 + 10 + 8 = 41. Sixth = 54 − 41 = 13. In order: 4, 7, 8, 10, 12, 13. The middle two are 8 and 10, so median = (8 + 10) ÷ 2 = 9.", "نمونہ جواب: کل = 9 × 6 = 54۔ معلوم: 4 + 12 + 7 + 10 + 8 = 41۔ چھٹا = 54 − 41 = 13۔ ترتیب میں: 4، 7، 8، 10، 12، 13۔ درمیانی دو 8 اور 10 ہیں، تو وسطانیہ = (8 + 10) ÷ 2 = 9"),
      [(13, "13 is the sixth number, the middle step. The question asks for the median: 9.", "13 چھٹا عدد ہے، بیچ کا قدم۔ سوال وسطانیہ پوچھتا ہے: 9", "answer_is_other_quantity"),
       (8, "8 is only one of the two middle numbers. Halfway between 8 and 10 is 9.", "8 دو درمیانی اعداد میں سے صرف ایک ہے۔ 8 اور 10 کے ٹھیک بیچ میں 9 ہے۔", "median_unsorted")]),
   with_fig(long_q("l2_pie", "The pie chart shows what 240 pupils chose for sports day. Sector X is 35% and sector Y is 25%. How many pupils are in sector Z?", "دائری نقشہ دکھاتا ہے کہ 240 طلبہ نے کھیلوں کے دن کے لیے کیا چنا۔ ٹکڑا X، 35٪ اور ٹکڑا Y، 25٪ ہے۔ ٹکڑے Z میں کتنے طلبہ ہیں؟",
      L2, ("Find the percentage of Z first: 100 − 35 − 25. Then take that percentage of 240.", "پہلے Z کا فیصد نکالیں: 100 − 35 − 25۔ پھر 240 کا وہ فیصد لیں۔"),
      ("Correct: Z = 40%, and 40 ÷ 100 × 240 = 96 pupils.", "درست: Z = 40٪، اور 40 ÷ 100 × 240 = 96 طلبہ"),
      ("Model answer: the sectors make 100%, so Z = 100 − 35 − 25 = 40%. Number of pupils = 40 ÷ 100 × 240 = 96.", "نمونہ جواب: ٹکڑے مل کر 100٪ بنتے ہیں، تو Z = 100 − 35 − 25 = 40٪۔ طلبہ کی تعداد = 40 ÷ 100 × 240 = 96"),
      [(40, "40 is the percentage of Z. The question asks for pupils: 96.", "40، Z کا فیصد ہے۔ سوال طلبہ پوچھتا ہے: 96", "answer_is_other_quantity"),
       (144, "144 pupils are in X and Y together (60%). Z is 40% of 240: 96.", "144 طلبہ X اور Y میں ملا کر ہیں (60٪)۔ Z، 240 کا 40٪ ہے: 96", "answer_is_other_quantity")]), L2_FIG),
   with_fig(long_q("l3_double", "The double bar graph shows boys (filled bar) and girls (empty bar) in classes A, B and C. How many more girls than boys are there in the three classes together?", "دوہرا بار گراف جماعتوں A، B اور C میں لڑکے (بھرا ستون) اور لڑکیاں (خالی ستون) دکھاتا ہے۔ تینوں جماعتوں میں مل کر لڑکوں سے لڑکیاں کتنی زیادہ ہیں؟",
      L3, ("Add all the boys' bars, add all the girls' bars, then subtract.", "لڑکوں کے سب ستون جمع کریں، لڑکیوں کے سب ستون جمع کریں، پھر گھٹائیں۔"),
      ("Correct: boys 20 + 10 + 15 = 45, girls 15 + 25 + 15 = 55, and 55 − 45 = 10.", "درست: لڑکے 20 + 10 + 15 = 45، لڑکیاں 15 + 25 + 15 = 55، اور 55 − 45 = 10"),
      ("Model answer: boys = 20 + 10 + 15 = 45. Girls = 15 + 25 + 15 = 55. There are 55 − 45 = 10 more girls.", "نمونہ جواب: لڑکے = 20 + 10 + 15 = 45۔ لڑکیاں = 15 + 25 + 15 = 55۔ لڑکیاں 55 − 45 = 10 زیادہ ہیں۔"),
      [(100, "100 is all the children added. 'How many more' means subtract: 10.", "100 سب بچے جمع ہیں۔ 'کتنی زیادہ' کا مطلب گھٹانا ہے: 10", "diff_as_total"),
       (55, "55 is the number of girls. Take away the 45 boys: 10.", "55 لڑکیوں کی تعداد ہے۔ 45 لڑکے گھٹائیں: 10", "answer_is_other_quantity")]), L3_FIG),
   long_q("l4_combined", "The mean of 4 numbers is 7. The mean of 6 other numbers is 12. Find the mean of all 10 numbers.", "4 اعداد کا اوسط 7 ہے۔ 6 دوسرے اعداد کا اوسط 12 ہے۔ سب 10 اعداد کا اوسط نکالیں۔",
      L4, ("Find each total (mean × how many), add the totals, and divide by 10.", "ہر کل نکالیں (اوسط × تعداد)، کل جمع کریں، اور 10 سے تقسیم کریں۔"),
      ("Correct: totals 28 and 72 make 100, and 100 ÷ 10 = 10.", "درست: کل 28 اور 72 مل کر 100 بنتے ہیں، اور 100 ÷ 10 = 10"),
      ("Model answer: first total = 7 × 4 = 28. Second total = 12 × 6 = 72. All together: 28 + 72 = 100 over 10 numbers. Mean = 100 ÷ 10 = 10.", "نمونہ جواب: پہلا کل = 7 × 4 = 28۔ دوسرا کل = 12 × 6 = 72۔ سب مل کر: 10 اعداد پر 28 + 72 = 100۔ اوسط = 100 ÷ 10 = 10"),
      [(100, "100 is the total of all ten. Divide by 10: 10.", "100 سب دس کا کل ہے۔ 10 سے تقسیم کریں: 10", "total_not_mean")]),
   {"id": "s_end_summary", "type": "summary",
    "character": say("celebrating", "You finished the chapter 11 test. Well done!", "آپ نے باب 11 کا ٹیسٹ مکمل کر لیا۔ شاباش!"),
    "text": T("In the exam: ungrouped data lists every value, grouped data puts them in classes; counted data is discrete and measured data is continuous. Read the scale first on a bar graph; for 'how many more' subtract, for 'altogether' add. A pie chart is 100% and 360°: angle = value ÷ total × 360°. Mean = total ÷ how many; the median is the middle value in order (halfway between the middle two for an even count); the mode is the most common value. For a missing value, total = mean × how many. Answer what is asked, not a middle step.",
              "امتحان میں: غیر گروہ بند مواد ہر قیمت لکھتا ہے، گروہ بند مواد انہیں گروہوں میں رکھتا ہے؛ گنا ہوا مواد منفصل اور ناپا ہوا مسلسل ہے۔ بار گراف میں پہلے پیمانہ پڑھیں؛ 'کتنے زیادہ' میں گھٹائیں، 'کل' میں جمع کریں۔ دائری نقشہ 100٪ اور 360° ہے: زاویہ = قیمت ÷ کل × 360°۔ اوسط = کل ÷ تعداد؛ وسطانیہ ترتیب میں درمیانی قیمت ہے (جفت تعداد میں درمیانی دو کے بیچ میں)؛ عادہ سب سے عام قیمت ہے۔ غائب قیمت کے لیے کل = اوسط × تعداد۔ وہ جواب دیں جو پوچھا گیا ہو، بیچ کا قدم نہیں۔"),
    "points": [T("Rule, numbers, answer.", "اصول، اعداد، جواب۔"),
               T("Answer what is asked, not a middle step.", "وہ جواب دیں جو پوچھا گیا ہو، بیچ کا قدم نہیں۔")]},
 ],
 "review_questions": [
   {"id": "r_exam_mode", "type": "exam_style", "skill": SKILL, "step": nq(
     "r_exam_mode", (f"Find the mode of {', '.join(map(str, R1_DATA))}.", f"{'، '.join(map(str, R1_DATA))} کا عادہ نکالیں۔"), R1,
     ("Which number appears most often?", "کون سا عدد سب سے زیادہ بار آتا ہے؟"),
     ("Correct: 8 appears three times.", "درست: 8 تین بار آتا ہے۔"), ("Count: 8 appears 3 times, 4 appears 2 times.", "گنیں: 8 تین بار، 4 دو بار"),
     [(3, "3 is how many times 8 appears. The mode is 8.", "3 یہ ہے کہ 8 کتنی بار آیا۔ عادہ 8 ہے۔", "total_not_mean")], qtype=None)},
   {"id": "r_exam_angle", "type": "exam_style", "skill": SKILL, "step": nq(
     "r_exam_angle", ("3 of 12 children walk to school. What is the angle of the walking sector in a pie chart, in degrees?", "12 میں سے 3 بچے پیدل سکول آتے ہیں۔ دائری نقشے میں پیدل والے ٹکڑے کا زاویہ درجوں میں کتنا ہے؟"), R2,
     ("3 ÷ 12 × 360.", "3 ÷ 12 × 360"),
     ("Correct: 3 ÷ 12 = 1/4, and 1/4 of 360 is 90°.", "درست: 3 ÷ 12 = 1/4، اور 360 کا 1/4 یعنی 90°"), ("360 ÷ 4 = 90.", "360 ÷ 4 = 90"),
     [(3, "3 is the number of children. The angle is 3 ÷ 12 × 360 = 90.", "3 بچوں کی تعداد ہے۔ زاویہ 3 ÷ 12 × 360 = 90 ہے۔", "pie_total_wrong")], qtype=None)},
 ],
 "teacher_notes": [
   "A chapter test to use with Review Exercise 11 of the PCTB Mathematics 6 book, in the style of a paper: multiple choice, short questions, then longer problems. Only the kinds of question come from the book; every question, number and story here is new, because the book may not be copied.",
   "It has its own skill (maths.data.chapter_11_test), with the skills of the Data Handling unit as prerequisites, and is mastered with exam_style questions, like the earlier chapter tests. The app cannot check a drawing, so the questions are about reading graphs and tables and calculating; drawing the graphs and pie charts is a home task.",
   "Urdu terms to check: کثیر انتخابی (multiple choice), مختصر سوال / تفصیلی سوال (short / long question), نمونہ جواب (model answer), اعادی مشق (review exercise), all as in the earlier chapter tests; the data words come from the existing Data Handling lessons. No new Urdu terms were added.",
   "The numbers were worked out in content/sources/g6-maths-10/chapter_11_test.py. Edit the script, not this file.",
 ],
 "review": REVIEW,
}

write(lesson)
