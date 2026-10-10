"""Practice set for Exercise 11.2 of the book: reading vertical, horizontal and
multiple (double) bar graphs. The app cannot check a drawing, so the questions
are about reading the graphs and working with what they say. The questions are
new; only the kinds of question follow the book."""
from common import (T, say, nq, ch, practice_lesson, practice_intro, write, EX_SKILL,
                    DH_BAR_GRAPHS, DH_PIE_CHARTS, DH_KINDS)
from figs import bar_graph, hbar_graph, double_bar_graph, with_fig

SKILL = EX_SKILL["11.2"]

# vertical bar graph: library books borrowed on five days (scale goes up in tens)
DAYS = ["Mo", "Tu", "We", "Th", "Fr"]
BORROW = [20, 25, 10, 30, 15]
assert len(DAYS) == len(BORROW) and max(BORROW) == 30
Q3 = BORROW[1]
assert Q3 == 25 and 20 < Q3 < 30
Q4_DAY = DAYS[BORROW.index(max(BORROW))]
assert Q4_DAY == "Th" and BORROW.index(max(BORROW)) == 3
Q5 = max(BORROW) - min(BORROW)
assert Q5 == 20 and max(BORROW) + min(BORROW) == 40
Q6 = sum(BORROW)
assert Q6 == 100 and max(BORROW) == 30

# horizontal bar graph: members of four clubs
CLUBS = ["A", "B", "C", "D"]
MEMBERS = [12, 20, 8, 16]
Q7 = MEMBERS[1]
assert Q7 == 20
Q8 = MEMBERS[1] - MEMBERS[2]
assert Q8 == 12 and MEMBERS[1] + MEMBERS[2] == 28

# double bar graph: boys and girls in three classes (scale goes up in fives)
CLASS = ["A", "B", "C"]
PAIRS = [(15, 20), (10, 5), (20, 15)]
Q9 = PAIRS[2][1]
assert Q9 == 15
Q10 = PAIRS[0][0] + PAIRS[0][1]
assert Q10 == 35 and PAIRS[0][0] == 15
Q11 = PAIRS[0][1] - PAIRS[0][0]
assert Q11 == 5 and PAIRS[1][0] - PAIRS[1][1] == 5
Q12_ALL_BOYS = sum(b for b, _ in PAIRS)
assert Q12_ALL_BOYS == 45 and sum(g for _, g in PAIRS) == 40

# bank and review
QB_BARS = [10, 35, 20]       # value read halfway between marks, scale in tens
QB = QB_BARS[1]
assert QB == 35 and 30 < QB < 40
QB_LOW = QB_BARS[0]
assert QB_LOW == 10
R1_BARS = [8, 12, 4, 16]     # horizontal, scale in fours
R1 = R1_BARS[3] - R1_BARS[2]
assert R1 == 12 and sum(R1_BARS) == 40
R2_PAIRS = [(30, 25), (10, 20)]
R2 = R2_PAIRS[1][1] - R2_PAIRS[1][0]
assert R2 == 10 and sum(R2_PAIRS[1]) == 30

F_V = bar_graph(BORROW, DAYS,
    "A bar graph of library books borrowed on five days. The side scale goes up in tens from 0 to 30. Monday 20, Tuesday 25 (halfway between 20 and 30), Wednesday 10, Thursday 30, Friday 15.",
    "پانچ دنوں میں لائبریری سے لی گئی کتابوں کا بار گراف۔ اطراف کا پیمانہ 0 سے 30 تک دس دس کے قدموں میں ہے۔ پیر 20، منگل 25 (20 اور 30 کے ٹھیک بیچ میں)، بدھ 10، جمعرات 30، جمعہ 15۔",
    top=30, step=10)
F_H = hbar_graph(MEMBERS, CLUBS,
    "A horizontal bar graph of members in four clubs. The scale along the bottom goes up in fours from 0 to 20. Club A 12, club B 20, club C 8, club D 16.",
    "چار کلبوں کے ارکان کا افقی بار گراف۔ نیچے کا پیمانہ 0 سے 20 تک چار چار کے قدموں میں ہے۔ کلب A میں 12، کلب B میں 20، کلب C میں 8، کلب D میں 16۔",
    top=20, step=4)
F_D = double_bar_graph(PAIRS, CLASS,
    "A double bar graph of boys (filled bar) and girls (empty bar) in three classes. The scale goes up in fives. Class A: 15 boys and 20 girls. Class B: 10 boys and 5 girls. Class C: 20 boys and 15 girls.",
    "تین جماعتوں میں لڑکوں (بھرا ستون) اور لڑکیوں (خالی ستون) کا دوہرا بار گراف۔ پیمانہ پانچ پانچ کے قدموں میں ہے۔ جماعت A: 15 لڑکے اور 20 لڑکیاں۔ جماعت B: 10 لڑکے اور 5 لڑکیاں۔ جماعت C: 20 لڑکے اور 15 لڑکیاں۔",
    top=20, step=5)
F_QB = bar_graph(QB_BARS, ["A", "B", "C"],
    "A bar graph with three bars A, B and C. The side scale goes up in tens from 0 to 40. Bar A reaches 10, bar B reaches 35 (halfway between 30 and 40) and bar C reaches 20.",
    "تین ستونوں A، B اور C کا بار گراف۔ اطراف کا پیمانہ 0 سے 40 تک دس دس کے قدموں میں ہے۔ ستون A 10 تک، ستون B 35 تک (30 اور 40 کے ٹھیک بیچ میں) اور ستون C 20 تک پہنچتا ہے۔",
    top=40, step=10)
F_R1 = hbar_graph(R1_BARS, ["A", "B", "C", "D"],
    "A horizontal bar graph with four bars. The scale along the bottom goes up in fours from 0 to 16. Bar A 8, bar B 12, bar C 4, bar D 16.",
    "چار ستونوں کا افقی بار گراف۔ نیچے کا پیمانہ 0 سے 16 تک چار چار کے قدموں میں ہے۔ ستون A 8، ستون B 12، ستون C 4، ستون D 16۔",
    top=16, step=4)
F_R2 = double_bar_graph(R2_PAIRS, ["A", "B"],
    "A double bar graph of boys (filled bar) and girls (empty bar) in two teams. The scale goes up in tens. Team A: 30 boys and 25 girls. Team B: 10 boys and 20 girls.",
    "دو ٹیموں میں لڑکوں (بھرا ستون) اور لڑکیوں (خالی ستون) کا دوہرا بار گراف۔ پیمانہ دس دس کے قدموں میں ہے۔ ٹیم A: 30 لڑکے اور 25 لڑکیاں۔ ٹیم B: 10 لڑکے اور 20 لڑکیاں۔",
    top=30, step=10)

lesson = practice_lesson(
 "11.2", script="exercise_11_2.py",
 title=T("Exercise 11.2 practice: reading bar graphs", "مشق 11.2 کی پریکٹس: بار گراف پڑھنا"),
 outcome="Read vertical, horizontal and multiple (double) bar graphs, using the scale, and answer questions about the values, the biggest and smallest bars, totals and differences.",
 prerequisites=[DH_BAR_GRAPHS, DH_PIE_CHARTS],
 misconceptions=[
   {"id": "scale_misread", "description": "Reads a bar that ends between two marks as the lower mark, or reads the scale step as 1."},
   {"id": "bar_height_vs_name", "description": "Gives the number of the bar's position or the name of the bar instead of its height."},
   {"id": "diff_as_total", "description": "Adds two bars when asked how many more, or subtracts when asked for the total."},
   {"id": "one_bar_only", "description": "Reads only one bar of a double bar graph and ignores the other, or mixes the two bars up."},
   {"id": "bars_not_added", "description": "Gives the biggest bar as the total, or leaves out a bar when adding."},
   {"id": "key_ignored", "description": "Forgets the key, so does not know which bar of a pair stands for which group."},
 ],
 steps=[
   practice_intro("11.2",
     "Here you practise reading vertical, horizontal and double bar graphs: the scale, the biggest bar, totals and differences. You only read; the drawing is for your notebook.",
     "اس میں آپ عمودی، افقی اور دوہرے بار گراف پڑھنا دہرائیں گے: پیمانہ، سب سے بڑا ستون، کل اور فرق۔ آپ صرف پڑھیں گے؛ بنانا کاپی میں کریں۔",
     "Exercise 11.2 is about bar graphs. Ready?", "مشق 11.2 بار گراف کے بارے میں ہے۔ تیار؟"),
   ch("q1_scale", ("The numbers up the side of a bar graph, in equal steps like 10, 20, 30, are called the:", "بار گراف کے اطراف میں برابر قدموں والے اعداد، جیسے 10، 20، 30، کہلاتے ہیں:"),
      ("scale", "پیمانہ", "Yes! The scale tells how much each step is worth.", "جی ہاں! پیمانہ بتاتا ہے کہ ہر قدم کتنے کا ہے۔"),
      [("key", "کلید", "A key says what each bar or colour means. The scale is the numbers on the axis.", "کلید بتاتی ہے کہ ہر ستون یا رنگ کا مطلب کیا ہے۔ پیمانہ محور کے اعداد ہیں۔", "key_ignored"),
       ("frequency", "تعدد", "Frequency is the count a bar shows, not the numbers along the side.", "تعدد وہ گنتی ہے جو ستون دکھاتا ہے، اطراف کے اعداد نہیں۔", "bar_height_vs_name")],
      0, qtype="recall"),
   {"id": "s_idea", "type": "explain",
    "character": say("thinking", "First the scale, then the bar. Find where the top of the bar meets the side.", "پہلے پیمانہ، پھر ستون۔ دیکھیں ستون کا اوپری سرا اطراف سے کہاں ملتا ہے۔"),
    "text": T("The height of a bar (or the length of a horizontal bar) shows how many. Read across to the scale. If the top is halfway between two marks, the value is halfway between them: halfway between 20 and 30 is 25. A double bar graph has two bars for each group; the key says which bar is which. For totals, add the bars you need; for how many more, subtract.",
              "ستون کی اونچائی (یا افقی ستون کی لمبائی) بتاتی ہے کہ کتنے ہیں۔ پیمانے تک سیدھ میں پڑھیں۔ اگر اوپری سرا دو نشانوں کے ٹھیک بیچ میں ہو تو قیمت بھی ان کے ٹھیک بیچ میں ہے: 20 اور 30 کے بیچ 25 ہے۔ دوہرے بار گراف میں ہر گروہ کے دو ستون ہوتے ہیں؛ کلید بتاتی ہے کہ کون سا ستون کس کا ہے۔ کل کے لیے ضروری ستون جمع کریں؛ کتنے زیادہ کے لیے گھٹائیں۔")},
   with_fig(nq("q2_halfway", ("The graph shows library books borrowed on five days. How many books were borrowed on Tuesday (Tu)? The bar ends halfway between two marks.", "گراف پانچ دنوں میں لی گئی کتابیں دکھاتا ہے۔ منگل (Tu) کو کتنی کتابیں لی گئیں؟ ستون دو نشانوں کے ٹھیک بیچ میں ختم ہوتا ہے۔"), Q3,
      ("The marks are 20 and 30. Halfway between them?", "نشان 20 اور 30 ہیں۔ ان کے ٹھیک بیچ میں کیا ہے؟"),
      ("Right! Halfway between 20 and 30 is 25.", "درست! 20 اور 30 کے ٹھیک بیچ میں 25 ہے۔"), ("(20 + 30) ÷ 2 = 25.", "(20 + 30) ÷ 2 = 25"),
      [(20, "20 is the mark below. The bar goes past 20, halfway to 30: 25.", "20 نیچے والا نشان ہے۔ ستون 20 سے آگے 30 کی طرف آدھا جاتا ہے: 25", "scale_misread"),
       (30, "30 is the mark above. The bar stops halfway: 25.", "30 اوپر والا نشان ہے۔ ستون بیچ میں رکتا ہے: 25", "scale_misread")], qtype="recall"), F_V),
   with_fig(ch("q3_most", ("On which day were the most books borrowed?", "کس دن سب سے زیادہ کتابیں لی گئیں؟"),
      ("Thursday (Th)", "جمعرات (Th)", "Yes! Its bar is the tallest, reaching 30.", "جی ہاں! اس کا ستون سب سے اونچا ہے، 30 تک۔"),
      [("Tuesday (Tu)", "منگل (Tu)", "Tuesday is 25. Thursday's bar is taller, 30.", "منگل 25 ہے۔ جمعرات کا ستون اونچا ہے، 30", "scale_misread"),
       ("Friday (Fr)", "جمعہ (Fr)", "Friday is the last bar, but not the tallest. It is 15.", "جمعہ آخری ستون ہے، لیکن سب سے اونچا نہیں۔ یہ 15 ہے۔", "bar_height_vs_name"),
       ("Monday (Mo)", "پیر (Mo)", "Monday is 20, less than Thursday's 30.", "پیر 20 ہے، جمعرات کے 30 سے کم۔", "scale_misread")],
      0, qtype="apply"), F_V),
   with_fig(nq("q4_diff", ("How many more books were borrowed on the busiest day than on the quietest day?", "سب سے مصروف دن سب سے پُرسکون دن سے کتنی کتابیں زیادہ لی گئیں؟"), Q5,
      ("Biggest bar minus smallest bar.", "سب سے بڑا ستون منفی سب سے چھوٹا ستون۔"),
      ("Right! 30 − 10 = 20 books.", "درست! 30 − 10 = 20 کتابیں"), ("The tallest is 30 and the shortest is 10: 30 − 10 = 20.", "سب سے اونچا 30 اور سب سے چھوٹا 10 ہے: 30 − 10 = 20"),
      [(40, "40 is 30 + 10, the two bars added. 'How many more' means subtract: 20.", "40 یعنی 30 + 10، دونوں ستون جمع۔ 'کتنے زیادہ' کا مطلب گھٹانا ہے: 20", "diff_as_total"),
       (10, "10 is the shortest bar. Subtract it from 30: 20.", "10 سب سے چھوٹا ستون ہے۔ اسے 30 میں سے گھٹائیں: 20", "bar_height_vs_name")]), F_V),
   with_fig(nq("q5_total", ("How many books were borrowed on the five days altogether?", "پانچوں دنوں میں کل کتنی کتابیں لی گئیں؟"), Q6,
      ("Add all five bars: 20, 25, 10, 30, 15.", "پانچوں ستون جمع کریں: 20، 25، 10، 30، 15"),
      ("Right! 20 + 25 + 10 + 30 + 15 = 100.", "درست! 20 + 25 + 10 + 30 + 15 = 100"), ("20 + 25 = 45, + 10 = 55, + 30 = 85, + 15 = 100.", "20 + 25 = 45، + 10 = 55، + 30 = 85، + 15 = 100"),
      [(30, "30 is only the tallest bar. Add all five: 100.", "30 صرف سب سے اونچا ستون ہے۔ پانچوں جمع کریں: 100", "bars_not_added"),
       (75, "75 leaves out one bar. Add all five: 100.", "75 میں ایک ستون رہ گیا۔ پانچوں جمع کریں: 100", "bars_not_added")]), F_V),
   with_fig(nq("q6_hbar", ("The horizontal bar graph shows the members of four clubs A, B, C and D. How many members does club B have?", "افقی بار گراف چار کلبوں A، B، C اور D کے ارکان دکھاتا ہے۔ کلب B کے کتنے ارکان ہیں؟"), Q7,
      ("Read along the bar of B to the scale at the bottom.", "B کے ستون کے ساتھ نیچے کے پیمانے تک پڑھیں۔"),
      ("Right! The bar of B reaches 20.", "درست! B کا ستون 20 تک پہنچتا ہے۔"), ("Follow the end of the bar down to the scale: 20.", "ستون کے سرے کو نیچے پیمانے تک دیکھیں: 20"),
      [(2, "2 is the position of B in the list. Read its length: 20.", "2 فہرست میں B کی جگہ ہے۔ اس کی لمبائی پڑھیں: 20", "bar_height_vs_name"),
       (16, "16 is club D. Club B is the longest bar: 20.", "16 کلب D ہے۔ کلب B سب سے لمبا ستون ہے: 20", "bar_height_vs_name")], qtype="apply"), F_H),
   with_fig(nq("q7_hdiff", ("How many more members does club B have than club C?", "کلب B کے ارکان کلب C سے کتنے زیادہ ہیں؟"), Q8,
      ("Read both bars, then subtract.", "دونوں ستون پڑھیں، پھر گھٹائیں۔"),
      ("Right! 20 − 8 = 12 more.", "درست! 20 − 8 = 12 زیادہ"), ("B has 20 and C has 8: 20 − 8 = 12.", "B کے 20 اور C کے 8 ہیں: 20 − 8 = 12"),
      [(28, "28 is 20 + 8. 'How many more' means subtract: 12.", "28 یعنی 20 + 8۔ 'کتنے زیادہ' کا مطلب گھٹانا ہے: 12", "diff_as_total"),
       (20, "20 is club B alone. Subtract club C's 8: 12.", "20 صرف کلب B ہے۔ کلب C کے 8 گھٹائیں: 12", "diff_as_total")]), F_H),
   with_fig(nq("q8_double", ("The double bar graph shows boys (filled bar) and girls (empty bar) in classes A, B and C. How many girls are in class C?", "دوہرا بار گراف جماعتوں A، B اور C میں لڑکے (بھرا ستون) اور لڑکیاں (خالی ستون) دکھاتا ہے۔ جماعت C میں کتنی لڑکیاں ہیں؟"), Q9,
      ("Find class C, then take the empty bar.", "جماعت C ڈھونڈیں، پھر خالی ستون لیں۔"),
      ("Right! The empty bar of class C reaches 15.", "درست! جماعت C کا خالی ستون 15 تک پہنچتا ہے۔"), ("The filled bar is the boys (20). The empty bar is the girls: 15.", "بھرا ستون لڑکوں کا ہے (20)۔ خالی ستون لڑکیوں کا ہے: 15"),
      [(20, "20 is the filled bar, the boys of class C. The girls' bar is 15.", "20 بھرا ستون ہے، یعنی جماعت C کے لڑکے۔ لڑکیوں کا ستون 15 ہے۔", "one_bar_only"),
       (35, "35 is boys and girls together. The question asks for girls: 15.", "35 لڑکے اور لڑکیاں ملا کر ہیں۔ سوال لڑکیاں پوچھتا ہے: 15", "one_bar_only")], qtype="apply"), F_D),
   with_fig(nq("q9_class_total", ("How many children are there in class A altogether?", "جماعت A میں کل کتنے بچے ہیں؟"), Q10,
      ("Add the boys' bar and the girls' bar of class A.", "جماعت A کا لڑکوں کا اور لڑکیوں کا ستون جمع کریں۔"),
      ("Right! 15 + 20 = 35 children.", "درست! 15 + 20 = 35 بچے"), ("Boys 15 and girls 20: 15 + 20 = 35.", "لڑکے 15 اور لڑکیاں 20: 15 + 20 = 35"),
      [(15, "15 is only the boys. Add the girls too: 35.", "15 صرف لڑکے ہیں۔ لڑکیاں بھی جمع کریں: 35", "one_bar_only"),
       (20, "20 is only the girls. Add the boys too: 35.", "20 صرف لڑکیاں ہیں۔ لڑکے بھی جمع کریں: 35", "one_bar_only")]), F_D),
   with_fig(nq("q10_more_girls", ("How many more girls than boys are in class A?", "جماعت A میں لڑکوں سے لڑکیاں کتنی زیادہ ہیں؟"), Q11,
      ("Girls' bar minus boys' bar in class A.", "جماعت A میں لڑکیوں کا ستون منفی لڑکوں کا ستون۔"),
      ("Right! 20 − 15 = 5 more girls.", "درست! 20 − 15 = 5 لڑکیاں زیادہ"), ("The girls are 20 and the boys are 15: 20 − 15 = 5.", "لڑکیاں 20 اور لڑکے 15 ہیں: 20 − 15 = 5"),
      [(35, "35 is both bars added. 'How many more' means subtract: 5.", "35 دونوں ستون جمع ہیں۔ 'کتنے زیادہ' کا مطلب گھٹانا ہے: 5", "diff_as_total"),
       (20, "20 is the girls alone. Subtract the 15 boys: 5.", "20 صرف لڑکیاں ہیں۔ 15 لڑکے گھٹائیں: 5", "diff_as_total")]), F_D),
   with_fig(ch("q11_find_error", ("Daud looks at class A in the double bar graph and says: there are 15 children in class A, because the first bar reaches 15. What went wrong?", "داؤد دوہرے بار گراف میں جماعت A دیکھ کر کہتا ہے: جماعت A میں 15 بچے ہیں، کیونکہ پہلا ستون 15 تک پہنچتا ہے۔ کیا غلطی ہوئی؟"),
      ("The first bar is only the boys. The girls' bar must be added too: 15 + 20 = 35.", "پہلا ستون صرف لڑکوں کا ہے۔ لڑکیوں کا ستون بھی جمع کرنا ہوگا: 15 + 20 = 35", "Yes! Each class has two bars, and both are needed for the number of children.", "جی ہاں! ہر جماعت کے دو ستون ہیں، اور بچوں کی تعداد کے لیے دونوں چاہییں۔"),
      [("Nothing. A class is shown by its first bar.", "کوئی غلطی نہیں۔ جماعت کو اس کا پہلا ستون دکھاتا ہے۔", "Each class has two bars, one for each group.", "ہر جماعت کے دو ستون ہیں، ہر گروہ کا ایک۔", "one_bar_only"),
       ("He should have used the taller bar, 20.", "اسے اونچا ستون، 20، لینا چاہیے تھا۔", "The taller bar is only the girls. The total needs both.", "اونچا ستون صرف لڑکیوں کا ہے۔ کل کے لیے دونوں چاہییں۔", "one_bar_only")],
      1, qtype="find_error"), F_D),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! You can read any bar graph.", "شاباش! آپ کوئی بھی بار گراف پڑھ سکتے ہیں۔"),
    "text": T("Read the scale first, then the bar. A bar ending halfway between two marks is halfway between their values. For a double bar graph, use the key and read the right bar; add both bars for a class total. 'How many more' means subtract, 'altogether' means add.",
              "پہلے پیمانہ پڑھیں، پھر ستون۔ جو ستون دو نشانوں کے ٹھیک بیچ میں ختم ہو وہ ان کی قیمتوں کے ٹھیک بیچ میں ہے۔ دوہرے بار گراف میں کلید دیکھیں اور صحیح ستون پڑھیں؛ جماعت کے کل کے لیے دونوں ستون جمع کریں۔ 'کتنے زیادہ' کا مطلب گھٹانا، 'کل' کا مطلب جمع کرنا ہے۔"),
    "points": [T("Scale first, then the bar.", "پہلے پیمانہ، پھر ستون۔"),
               T("More than: subtract. Altogether: add.", "کتنے زیادہ: گھٹائیں۔ کل: جمع کریں۔")]},
 ],
 bank=[
   {"id": "qb_key", "type": "recall", "step": ch("qb_key", ("In a double bar graph, what tells you which bar of each pair is which group?", "دوہرے بار گراف میں کون سی چیز بتاتی ہے کہ جوڑے کا کون سا ستون کس گروہ کا ہے؟"),
      ("the key", "کلید", "Yes! The key shows which bar is boys and which is girls.", "جی ہاں! کلید دکھاتی ہے کہ کون سا ستون لڑکوں کا اور کون سا لڑکیوں کا ہے۔"),
      [("the tallest bar", "سب سے اونچا ستون", "The height shows how many, not which group.", "اونچائی بتاتی ہے کہ کتنے ہیں، کون سا گروہ نہیں۔", "key_ignored"),
       ("the scale", "پیمانہ", "The scale gives the numbers, not the groups.", "پیمانہ اعداد دیتا ہے، گروہ نہیں۔", "key_ignored")],
      2, qtype=None)},
   {"id": "qb_read", "type": "apply", "step": with_fig(nq("qb_read", ("The graph's scale goes up in tens. Bar B ends halfway between 30 and 40. What does bar B show?", "گراف کا پیمانہ دس دس کے قدموں میں ہے۔ ستون B، 30 اور 40 کے ٹھیک بیچ میں ختم ہوتا ہے۔ ستون B کتنا دکھاتا ہے؟"), QB,
      ("Halfway between 30 and 40.", "30 اور 40 کے ٹھیک بیچ میں۔"),
      ("Right! (30 + 40) ÷ 2 = 35.", "درست! (30 + 40) ÷ 2 = 35"), ("30 + 5 = 35.", "30 + 5 = 35"),
      [(30, "30 is the mark below. The bar goes halfway to 40: 35.", "30 نیچے والا نشان ہے۔ ستون 40 کی طرف آدھا جاتا ہے: 35", "scale_misread"),
       (40, "40 is the mark above. The bar stops halfway: 35.", "40 اوپر والا نشان ہے۔ ستون بیچ میں رکتا ہے: 35", "scale_misread")], qtype=None), F_QB)},
   {"id": "qb_diff", "type": "apply", "step": with_fig(nq("qb_diff", ("How many more does bar B show than bar A?", "ستون B، ستون A سے کتنا زیادہ دکھاتا ہے؟"), QB - QB_LOW,
      ("Bar B is 35 and bar A is 10.", "ستون B کا 35 اور ستون A کا 10 ہے۔"),
      ("Right! 35 − 10 = 25.", "درست! 35 − 10 = 25"), ("Subtract: 35 − 10 = 25.", "گھٹائیں: 35 − 10 = 25"),
      [(45, "45 is 35 + 10. 'How many more' means subtract: 25.", "45 یعنی 35 + 10۔ 'کتنے زیادہ' کا مطلب گھٹانا ہے: 25", "diff_as_total")], qtype=None), F_QB)},
   {"id": "qb_find_error", "type": "find_error", "step": with_fig(ch("qb_find_error", ("Rida reads bar B and says it shows 30, because the bar goes past the 30 mark. What went wrong?", "ریدا ستون B پڑھ کر کہتی ہے کہ یہ 30 دکھاتا ہے، کیونکہ ستون 30 کے نشان سے آگے جاتا ہے۔ کیا غلطی ہوئی؟"),
      ("The bar is halfway between 30 and 40, so it shows 35, not 30.", "ستون 30 اور 40 کے ٹھیک بیچ میں ہے، تو یہ 35 دکھاتا ہے، 30 نہیں۔", "Yes! Read the top of the bar, not the mark below it.", "جی ہاں! ستون کا اوپری سرا پڑھیں، نیچے والا نشان نہیں۔"),
      [("Nothing. A bar always shows the mark below it.", "کوئی غلطی نہیں۔ ستون ہمیشہ نیچے والا نشان دکھاتا ہے۔", "A bar can end between marks. Then read halfway.", "ستون نشانوں کے بیچ میں بھی ختم ہو سکتا ہے۔ تب بیچ کی قیمت پڑھیں۔", "scale_misread"),
       ("It shows 40, the mark above.", "یہ 40 دکھاتا ہے، اوپر والا نشان۔", "The bar does not reach 40. It stops halfway.", "ستون 40 تک نہیں پہنچتا۔ یہ بیچ میں رک جاتا ہے۔", "scale_misread")],
      0, qtype=None), F_QB)},
 ],
 review=[
   {"id": "r_hbar", "type": "apply", "step": with_fig(nq("r_hbar", ("The horizontal graph shows four bars A, B, C and D. How many more does bar D show than bar C?", "افقی گراف میں چار ستون A، B، C اور D ہیں۔ ستون D، ستون C سے کتنا زیادہ دکھاتا ہے؟"), R1,
      ("Read D and C, then subtract.", "D اور C پڑھیں، پھر گھٹائیں۔"),
      ("Right! 16 − 4 = 12.", "درست! 16 − 4 = 12"), ("D is 16 and C is 4: 16 − 4 = 12.", "D کا 16 اور C کا 4 ہے: 16 − 4 = 12"),
      [(20, "20 is 16 + 4. 'How many more' means subtract: 12.", "20 یعنی 16 + 4۔ 'کتنے زیادہ' کا مطلب گھٹانا ہے: 12", "diff_as_total")], qtype=None), F_R1)},
   {"id": "r_double", "type": "apply", "step": with_fig(nq("r_double", ("In team B of the double bar graph, how many more girls (empty bar) than boys (filled bar) are there?", "دوہرے بار گراف کی ٹیم B میں لڑکیاں (خالی ستون) لڑکوں (بھرا ستون) سے کتنی زیادہ ہیں؟"), R2,
      ("Team B: girls' bar minus boys' bar.", "ٹیم B: لڑکیوں کا ستون منفی لڑکوں کا ستون۔"),
      ("Right! 20 − 10 = 10 more girls.", "درست! 20 − 10 = 10 لڑکیاں زیادہ"), ("The girls are 20 and the boys are 10: 20 − 10 = 10.", "لڑکیاں 20 اور لڑکے 10 ہیں: 20 − 10 = 10"),
      [(30, "30 is boys and girls added. 'How many more' means subtract: 10.", "30 لڑکے اور لڑکیاں جمع ہیں۔ 'کتنے زیادہ' کا مطلب گھٹانا ہے: 10", "diff_as_total")], qtype=None), F_R2)},
 ],
 glossary=[T("Bar graph", "بار گراف (ستونی گراف)"), T("Bar", "ستون"), T("Scale", "پیمانہ"), T("Axis", "محور"),
           T("Multiple (double) bar graph", "دوہرا بار گراف"), T("Total", "کل")],
 flashcards=[
   {"id": "f_halfway", "front": T("A bar ends halfway between 20 and 30. What does it show?", "ستون 20 اور 30 کے ٹھیک بیچ میں ختم ہوتا ہے۔ یہ کیا دکھاتا ہے؟"),
    "back": T("25: halfway between the two marks.", "25: دونوں نشانوں کے ٹھیک بیچ میں۔")},
   {"id": "f_double", "front": T("How do you read a double bar graph?", "دوہرا بار گراف کیسے پڑھتے ہیں؟"),
    "back": T("Use the key to see which bar is which, read the bar you need, and add both bars for a total.", "کلید سے دیکھیں کون سا ستون کس کا ہے، مطلوبہ ستون پڑھیں، اور کل کے لیے دونوں جمع کریں۔")},
 ],
 home_task={"id": "h_bars", "text": T(
   "Count the vowels (a, e, i, o, u) in a paragraph of your textbook and draw a horizontal bar graph in your notebook with a scale and a title. Then draw a double bar graph of the number of boys and girls in each of three classes of your school, with a key.",
   "اپنی کتاب کے ایک پیراگراف میں حروفِ علت (a, e, i, o, u) گنیں اور کاپی میں پیمانے اور عنوان کے ساتھ افقی بار گراف بنائیں۔ پھر اپنے سکول کی تین جماعتوں میں لڑکوں اور لڑکیوں کی تعداد کا دوہرا بار گراف کلید کے ساتھ بنائیں۔")},
 notes=["Covers the meaning of the scale (q1), reading a bar that ends between two marks (q2, qb_read, qb_find_error), the tallest bar, a difference and a total from a vertical graph (q3 to q5), a horizontal graph (q6, q7) and a double bar graph with a key (q8 to q11).",
        "Each wrong answer is a real mistake: reading the mark below, adding for 'how many more', reading only one bar of a pair, and answering with the position of a bar.",
        "The app cannot check a drawing, so these questions are about reading the graphs; drawing them is the home task. Figure labels are single letters or numbers; the step text says what the letters stand for.",
        "Urdu terms to check: بار گراف (ستونی گراف), ستون, پیمانہ, محور and دوہرا بار گراف, all as in the existing Data Handling lessons. New Urdu terms, which a teacher should confirm: کلید (key of a graph) and افقی بار گراف / عمودی بار گراف (horizontal / vertical bar graph)."],
 minutes=18,
)
write(lesson)
