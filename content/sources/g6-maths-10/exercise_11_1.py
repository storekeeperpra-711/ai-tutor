"""Practice set for Exercise 11.1 of the book: what data is, grouped and ungrouped
data (frequency tables), and discrete and continuous data. The questions are new;
only the kinds of question follow the book."""
from common import (T, say, nq, ch, practice_lesson, practice_intro, write, EX_SKILL,
                    DH_TABLES, DH_KINDS)
from figs import table_figure, with_fig

SKILL = EX_SKILL["11.1"]

# raw marks of 12 children, and the classes 0-9, 10-19, 20-29
MARKS = [14, 9, 17, 22, 9, 14, 25, 17, 9, 28, 14, 22]
CLASSES = [(0, 9), (10, 19), (20, 29)]
FREQ = [sum(1 for m in MARKS if lo <= m <= hi) for lo, hi in CLASSES]
assert FREQ == [3, 5, 4] and sum(FREQ) == len(MARKS) == 12
ROWS = [(f"{lo}-{hi}", f) for (lo, hi), f in zip(CLASSES, FREQ)]
RAW = ", ".join(map(str, MARKS))

Q4 = FREQ[1]                       # children with 10 to 19 marks
assert Q4 == 5 and FREQ[0] == 3 and FREQ[2] == 4
Q5 = sum(FREQ)
assert Q5 == 12 and len(CLASSES) == 3
Q6 = 19 - 10 + 1                   # whole numbers in the class 10-19
assert Q6 == 10 and len(range(10, 20)) == 10 and 19 - 10 == 9
Q10 = sum(1 for m in MARKS if 20 <= m <= 29)
assert Q10 == 4 and Q10 == FREQ[2] and sum(1 for m in MARKS if 10 <= m <= 19) == 5
Q10_LOW = sum(1 for m in MARKS if m < 20)     # fewer than 20 marks
assert Q10_LOW == 8 and Q10_LOW + Q10 == 12
# bank: a table of 20-24, 25-29 classes: 8 and 7 children, total 15
QB_ROWS = [("20-24", 8), ("25-29", 7)]
QB = sum(f for _, f in QB_ROWS)
assert QB == 15
QB_WIDTH = 24 - 20 + 1
assert QB_WIDTH == 5
R1 = len(range(30, 40))
assert R1 == 10
R2 = 5 + 9 + 6
assert R2 == 20

F_TABLE = table_figure(ROWS,
    "A frequency table of the marks of 12 children in three classes. Class 0-9 has 3 children, class 10-19 has 5 children and class 20-29 has 4 children.",
    "12 بچوں کے نمبروں کا تعدد جدول، تین گروہوں میں۔ گروہ 0-9 میں 3 بچے، گروہ 10-19 میں 5 بچے اور گروہ 20-29 میں 4 بچے ہیں۔",
    tallies=False, name_w=64)
F_QB = table_figure(QB_ROWS,
    "A frequency table of the ages of 15 cousins in two classes. Class 20-24 has 8 cousins and class 25-29 has 7 cousins.",
    "15 کزنوں کی عمروں کا تعدد جدول، دو گروہوں میں۔ گروہ 20-24 میں 8 اور گروہ 25-29 میں 7 کزن ہیں۔",
    tallies=False, name_w=64)

lesson = practice_lesson(
 "11.1", script="exercise_11_1.py",
 title=T("Exercise 11.1 practice: kinds of data", "مشق 11.1 کی پریکٹس: مواد کی اقسام"),
 outcome="Say what data is, tell grouped from ungrouped data, read a frequency table, and tell discrete from continuous data.",
 prerequisites=[DH_TABLES, DH_KINDS],
 misconceptions=[
   {"id": "table_is_graph", "description": "Thinks data is the graph or the table itself, not the facts and numbers collected."},
   {"id": "grouped_ungrouped_mix", "description": "Calls a list of single values grouped, or a table of classes ungrouped."},
   {"id": "class_width_off", "description": "Finds the number of values in a class by subtracting (19 - 10 = 9) and forgets to count both ends."},
   {"id": "counted_wrong_class", "description": "Counts the values in the wrong class, or forgets a class, when reading or sorting data."},
   {"id": "number_means_discrete", "description": "Thinks anything written as a number is discrete, even when it is measured (height, time, weight)."},
   {"id": "measured_is_counted", "description": "Calls a counted quantity (goals, pages) continuous because it is a number."},
 ],
 steps=[
   practice_intro("11.1",
     "Here you practise what data is, grouped and ungrouped data, reading a frequency table, and discrete and continuous data.",
     "اس میں آپ مواد کیا ہے، گروہ بند اور غیر گروہ بند مواد، تعدد جدول پڑھنا، اور منفصل اور مسلسل مواد دہرائیں گے۔",
     "Exercise 11.1 is about kinds of data. Ready?", "مشق 11.1 مواد کی اقسام کے بارے میں ہے۔ تیار؟"),
   ch("q1_data", ("What is data?", "مواد (ڈیٹا) کیا ہوتا ہے؟"),
      ("facts and numbers collected to find something out", "کوئی بات معلوم کرنے کے لیے جمع کیے گئے حقائق اور اعداد", "Yes! A survey or a count gives us data.", "جی ہاں! سروے یا گنتی سے ہمیں مواد ملتا ہے۔"),
      [("only a picture such as a pie chart", "صرف تصویر جیسے دائری نقشہ", "A pie chart shows data. The data is the facts and numbers behind it.", "دائری نقشہ مواد کو دکھاتا ہے۔ مواد اس کے پیچھے کے حقائق اور اعداد ہیں۔", "table_is_graph"),
       ("only a long number", "صرف ایک لمبا عدد", "Data is a collection of many facts or numbers, not one number.", "مواد بہت سے حقائق یا اعداد کا مجموعہ ہے، ایک عدد نہیں۔", "table_is_graph")],
      0, qtype="recall"),
   ch("q2_how", ("Hira counts how many cars pass the school gate in one hour. She collects data by:", "ہیرا ایک گھنٹے میں سکول کے گیٹ سے گزرنے والی گاڑیاں گنتی ہے۔ وہ مواد جمع کرتی ہے:"),
      ("observation (watching and counting)", "مشاہدے سے (دیکھ کر گننا)", "Yes! She watches and counts; she asks nobody.", "جی ہاں! وہ دیکھ کر گنتی ہے؛ کسی سے پوچھتی نہیں۔"),
      [("a questionnaire (written questions)", "سوالنامے سے (لکھے ہوئے سوال)", "A questionnaire asks people written questions. Hira asks nobody.", "سوالنامہ لوگوں سے لکھے ہوئے سوال پوچھتا ہے۔ ہیرا کسی سے نہیں پوچھتی۔", "table_is_graph"),
       ("an interview (talking to a person)", "انٹرویو سے (کسی شخص سے بات)", "An interview needs a person to talk to. She only watches.", "انٹرویو میں کسی شخص سے بات کرنی پڑتی ہے۔ وہ صرف دیکھتی ہے۔", "table_is_graph")],
      1, qtype="recall"),
   {"id": "s_idea", "type": "explain",
    "character": say("thinking", "Single values, or classes? Counted, or measured? Ask these two things.", "الگ الگ قیمتیں یا گروہ؟ گنا ہوا یا ناپا ہوا؟ یہ دو باتیں پوچھیں۔"),
    "text": T("Ungrouped data lists every value one by one. Grouped data puts the values into classes such as 0-9, 10-19, 20-29, and a frequency table says how many values fall in each class. A class like 10-19 holds ten whole numbers, because both ends count. Discrete data is counted and takes separate values (goals, pages, children). Continuous data is measured and can be any value in a range (height, time, weight).",
              "غیر گروہ بند مواد میں ہر قیمت الگ الگ لکھی جاتی ہے۔ گروہ بند مواد میں قیمتیں 0-9، 10-19، 20-29 جیسے گروہوں میں رکھی جاتی ہیں، اور تعدد جدول بتاتا ہے کہ ہر گروہ میں کتنی قیمتیں ہیں۔ 10-19 جیسے گروہ میں دس مکمل اعداد ہوتے ہیں، کیونکہ دونوں سرے گنے جاتے ہیں۔ منفصل مواد گنا جاتا ہے اور الگ الگ قیمتیں لیتا ہے (گول، صفحے، بچے)۔ مسلسل مواد ناپا جاتا ہے اور کسی حد کے اندر کوئی بھی قیمت ہو سکتی ہے (قد، وقت، وزن)۔")},
   ch("q3_kind", (f"A teacher writes the marks of 12 children one by one: {RAW}. This is:", f"ایک استاد 12 بچوں کے نمبر ایک ایک کر کے لکھتا ہے: {RAW}۔ یہ ہے:"),
      ("ungrouped data", "غیر گروہ بند مواد", "Yes! Every mark is listed on its own.", "جی ہاں! ہر نمبر الگ لکھا ہے۔"),
      [("grouped data", "گروہ بند مواد", "Grouped data would put the marks in classes such as 0-9. Here each one is listed.", "گروہ بند مواد میں نمبر 0-9 جیسے گروہوں میں ہوتے۔ یہاں ہر ایک الگ لکھا ہے۔", "grouped_ungrouped_mix"),
       ("a frequency table", "تعدد جدول", "A frequency table counts how many fall in each class. This is just the list.", "تعدد جدول بتاتا ہے کہ ہر گروہ میں کتنے ہیں۔ یہ تو صرف فہرست ہے۔", "grouped_ungrouped_mix")],
      0, qtype="recall"),
   with_fig(nq("q4_read", ("The marks are put into classes, as in the picture. How many children got 10 to 19 marks?", "نمبر تصویر کی طرح گروہوں میں رکھے گئے ہیں۔ کتنے بچوں کے 10 سے 19 نمبر آئے؟"), Q4,
      ("Find the row 10-19 and read its frequency.", "10-19 والی قطار ڈھونڈیں اور اس کا تعدد پڑھیں۔"),
      ("Right! The class 10-19 has 5 children.", "درست! گروہ 10-19 میں 5 بچے ہیں۔"), ("Read the number beside 10-19: 5.", "10-19 کے ساتھ والا عدد پڑھیں: 5"),
      [(3, "3 is the class 0-9. Look at the row 10-19: 5.", "3 گروہ 0-9 کا ہے۔ 10-19 والی قطار دیکھیں: 5", "counted_wrong_class"),
       (4, "4 is the class 20-29. Look at the row 10-19: 5.", "4 گروہ 20-29 کا ہے۔ 10-19 والی قطار دیکھیں: 5", "counted_wrong_class")], qtype="recall"), F_TABLE),
   with_fig(nq("q5_total", ("How many children are there in the table altogether?", "جدول میں کل کتنے بچے ہیں؟"), Q5,
      ("Add the three frequencies.", "تینوں تعدد جمع کریں۔"),
      ("Right! 3 + 5 + 4 = 12 children.", "درست! 3 + 5 + 4 = 12 بچے"), ("3 + 5 + 4 = 12.", "3 + 5 + 4 = 12"),
      [(3, "3 is only the number of classes. Add the frequencies: 12.", "3 صرف گروہوں کی تعداد ہے۔ تعدد جمع کریں: 12", "counted_wrong_class"),
       (5, "5 is one class. Add all three: 12.", "5 ایک گروہ ہے۔ تینوں جمع کریں: 12", "counted_wrong_class")]), F_TABLE),
   nq("q6_width", ("How many whole numbers are in the class 10-19? Count both ends.", "گروہ 10-19 میں کتنے مکمل اعداد ہیں؟ دونوں سرے گنیں۔"), Q6,
      ("List them: 10, 11, 12, and so on up to 19.", "لکھیں: 10، 11، 12، اور اسی طرح 19 تک۔"),
      ("Right! 10, 11, ..., 19 is ten numbers.", "درست! 10، 11، ...، 19 یعنی دس اعداد"), ("19 − 10 = 9, and then add 1 for the first number: 10.", "19 − 10 = 9، اور پہلا عدد گننے کے لیے 1 جمع کریں: 10"),
      [(9, "19 − 10 = 9 forgets the number 10 itself. Add 1: 10.", "19 − 10 = 9 میں خود عدد 10 رہ جاتا ہے۔ 1 جمع کریں: 10", "class_width_off"),
       (19, "19 is the last number, not how many there are: 10.", "19 آخری عدد ہے، گنتی نہیں: 10", "class_width_off")]),
   ch("q7_discrete", ("The number of pages in a storybook is:", "کہانی کی کتاب کے صفحوں کی تعداد ہے:"),
      ("discrete data", "منفصل مواد", "Yes! Pages are counted: 1, 2, 3, never 2.5.", "جی ہاں! صفحے گنے جاتے ہیں: 1، 2، 3، کبھی 2.5 نہیں۔"),
      [("continuous data", "مسلسل مواد", "Continuous data is measured. Pages are counted one by one.", "مسلسل مواد ناپا جاتا ہے۔ صفحے ایک ایک کر کے گنے جاتے ہیں۔", "measured_is_counted"),
       ("neither, because it is a number", "کوئی نہیں، کیونکہ یہ عدد ہے", "Every quantity of numbers is one or the other. Pages are counted, so discrete.", "اعداد کی ہر مقدار ان میں سے ایک ہوتی ہے۔ صفحے گنے جاتے ہیں، تو منفصل۔", "measured_is_counted")],
      1, qtype="apply"),
   ch("q8_continuous", ("The time Bilal takes to walk to school is:", "بلال کو سکول پیدل جانے میں جو وقت لگتا ہے وہ ہے:"),
      ("continuous data", "مسلسل مواد", "Yes! Time is measured and can be 12.5 minutes or 12.51 minutes.", "جی ہاں! وقت ناپا جاتا ہے اور 12.5 منٹ یا 12.51 منٹ ہو سکتا ہے۔"),
      [("discrete data", "منفصل مواد", "Discrete data is counted. Time is measured, so it can fall between whole numbers.", "منفصل مواد گنا جاتا ہے۔ وقت ناپا جاتا ہے، تو مکمل اعداد کے بیچ بھی ہو سکتا ہے۔", "number_means_discrete"),
       ("grouped data", "گروہ بند مواد", "Grouped is about how data is written down, not about counted or measured.", "گروہ بند اس کے بارے میں ہے کہ مواد کیسے لکھا جائے، گنا ہوا یا ناپا ہوا نہیں۔", "grouped_ungrouped_mix")],
      2, qtype="apply"),
   ch("q9_which", ("Which one of these is continuous data?", "ان میں سے کون سا مسلسل مواد ہے؟"),
      ("the weight of a bag of rice", "چاول کی بوری کا وزن", "Yes! Weight is measured on a scale.", "جی ہاں! وزن ترازو سے ناپا جاتا ہے۔"),
      [("the number of goals in a match", "میچ میں گولوں کی تعداد", "Goals are counted: 0, 1, 2.", "گول گنے جاتے ہیں: 0، 1، 2", "measured_is_counted"),
       ("the number of chairs in a room", "کمرے میں کرسیوں کی تعداد", "Chairs are counted.", "کرسیاں گنی جاتی ہیں۔", "measured_is_counted"),
       ("the number of girls in a class", "جماعت میں لڑکیوں کی تعداد", "Girls are counted.", "لڑکیاں گنی جاتی ہیں۔", "measured_is_counted")],
      3, qtype="apply"),
   nq("q10_sort", (f"Sort the marks {RAW} into the class 20-29. How many marks are in this class?", f"نمبر {RAW} کو گروہ 20-29 میں چھانٹیں۔ اس گروہ میں کتنے نمبر ہیں؟"), Q10,
      ("Go through the list and tick each mark from 20 to 29.", "فہرست دیکھیں اور 20 سے 29 تک کے ہر نمبر پر نشان لگائیں۔"),
      ("Right! The marks 22, 25, 28 and 22 make 4.", "درست! نمبر 22، 25، 28 اور 22 مل کر 4 بنتے ہیں۔"), ("Tick 22, 25, 28 and 22: four marks.", "22، 25، 28 اور 22 پر نشان لگائیں: چار نمبر"),
      [(3, "3 is the number of different marks. 22 appears twice: 4.", "3 مختلف نمبروں کی تعداد ہے۔ 22 دو بار آیا ہے: 4", "counted_wrong_class"),
       (5, "5 is the class 10-19. Count the class 20-29: 4.", "5 گروہ 10-19 کا ہے۔ گروہ 20-29 گنیں: 4", "counted_wrong_class")]),
   ch("q11_find_error", ("Zara says: height is discrete data because heights are written as numbers. What went wrong?", "زارا کہتی ہے: قد منفصل مواد ہے کیونکہ قد اعداد میں لکھے جاتے ہیں۔ کیا غلطی ہوئی؟"),
      ("Height is measured and can be any value, so it is continuous. Discrete data is counted.", "قد ناپا جاتا ہے اور کوئی بھی قیمت ہو سکتا ہے، تو یہ مسلسل ہے۔ منفصل مواد گنا جاتا ہے۔", "Yes! Being written as a number does not make data discrete.", "جی ہاں! عدد میں لکھا ہونے سے مواد منفصل نہیں ہو جاتا۔"),
      [("Nothing. All numbers are discrete.", "کوئی غلطی نہیں۔ ہر عدد منفصل ہوتا ہے۔", "A measured height such as 142.5 cm is not counted in whole steps.", "ناپا ہوا قد جیسے 142.5 سینٹی میٹر پورے قدموں میں نہیں گنا جاتا۔", "number_means_discrete"),
       ("Height is grouped data.", "قد گروہ بند مواد ہے۔", "Grouped or ungrouped is about how the data is written, not what it is.", "گروہ بند یا غیر گروہ بند اس کے بارے میں ہے کہ مواد کیسے لکھا گیا، وہ کیا ہے اس کے بارے میں نہیں۔", "grouped_ungrouped_mix")],
      1, qtype="find_error"),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! Now you can name any data you meet.", "شاباش! اب آپ کسی بھی مواد کا نام بتا سکتے ہیں۔"),
    "text": T("Data is facts and numbers collected by observation, a survey, an interview or a questionnaire. Ungrouped data lists each value; grouped data puts values in classes and a frequency table counts each class. A class like 10-19 has 10 whole numbers. Counted data is discrete; measured data is continuous.",
              "مواد وہ حقائق اور اعداد ہیں جو مشاہدے، سروے، انٹرویو یا سوالنامے سے جمع کیے جاتے ہیں۔ غیر گروہ بند مواد ہر قیمت الگ لکھتا ہے؛ گروہ بند مواد قیمتوں کو گروہوں میں رکھتا ہے اور تعدد جدول ہر گروہ گنتا ہے۔ 10-19 جیسے گروہ میں 10 مکمل اعداد ہیں۔ گنا ہوا مواد منفصل ہے؛ ناپا ہوا مواد مسلسل ہے۔"),
    "points": [T("Counted is discrete; measured is continuous.", "گنا ہوا منفصل؛ ناپا ہوا مسلسل۔"),
               T("A class holds both of its ends: 10-19 is ten numbers.", "گروہ میں اس کے دونوں سرے آتے ہیں: 10-19 یعنی دس اعداد۔")]},
 ],
 bank=[
   {"id": "qb_grouped", "type": "recall", "step": ch("qb_grouped", ("Data that is put into classes such as 0-9 and 10-19 is called:", "جو مواد 0-9 اور 10-19 جیسے گروہوں میں رکھا جائے وہ کہلاتا ہے:"),
      ("grouped data", "گروہ بند مواد", "Yes! Classes mean grouped.", "جی ہاں! گروہ یعنی گروہ بند۔"),
      [("ungrouped data", "غیر گروہ بند مواد", "Ungrouped data lists each value on its own.", "غیر گروہ بند مواد ہر قیمت الگ لکھتا ہے۔", "grouped_ungrouped_mix"),
       ("continuous data", "مسلسل مواد", "Continuous is about measuring, not about classes.", "مسلسل ناپنے کے بارے میں ہے، گروہوں کے بارے میں نہیں۔", "grouped_ungrouped_mix")],
      1, qtype=None)},
   {"id": "qb_total", "type": "apply", "step": with_fig(nq("qb_total", ("How many cousins are there in the table altogether?", "جدول میں کل کتنے کزن ہیں؟"), QB,
      ("Add the two frequencies.", "دونوں تعدد جمع کریں۔"),
      ("Right! 8 + 7 = 15.", "درست! 8 + 7 = 15"), ("8 + 7 = 15.", "8 + 7 = 15"),
      [(8, "8 is only the class 20-24. Add 7 as well: 15.", "8 صرف گروہ 20-24 ہے۔ 7 بھی جمع کریں: 15", "counted_wrong_class"),
       (2, "2 is the number of classes. Add the frequencies: 15.", "2 گروہوں کی تعداد ہے۔ تعدد جمع کریں: 15", "counted_wrong_class")], qtype=None), F_QB)},
   {"id": "qb_width", "type": "apply", "step": nq("qb_width", ("How many whole numbers are in the class 20-24?", "گروہ 20-24 میں کتنے مکمل اعداد ہیں؟"), QB_WIDTH,
      ("List them: 20, 21, 22, 23, 24.", "لکھیں: 20، 21، 22، 23، 24"),
      ("Right! There are 5 numbers.", "درست! 5 اعداد ہیں۔"), ("20, 21, 22, 23, 24 is five numbers.", "20، 21، 22، 23، 24 یعنی پانچ اعداد"),
      [(4, "24 − 20 = 4 forgets 20 itself. Add 1: 5.", "24 − 20 = 4 میں خود 20 رہ جاتا ہے۔ 1 جمع کریں: 5", "class_width_off")], qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": ch("qb_find_error", ("Sami says: the number of students in a class is continuous data because it can be large. What went wrong?", "سامی کہتا ہے: جماعت میں طلبہ کی تعداد مسلسل مواد ہے کیونکہ یہ بڑی ہو سکتی ہے۔ کیا غلطی ہوئی؟"),
      ("Students are counted one by one, so it is discrete. Size does not decide.", "طلبہ ایک ایک کر کے گنے جاتے ہیں، تو یہ منفصل ہے۔ بڑا ہونے سے فیصلہ نہیں ہوتا۔", "Yes! Counted means discrete, however big.", "جی ہاں! گنا ہوا یعنی منفصل، چاہے کتنا بھی بڑا ہو۔"),
      [("Nothing. Big numbers are continuous.", "کوئی غلطی نہیں۔ بڑے اعداد مسلسل ہوتے ہیں۔", "Size of the number does not matter; counting does.", "عدد کے بڑے ہونے سے فرق نہیں پڑتا؛ گننے سے پڑتا ہے۔", "measured_is_counted"),
       ("It is grouped data.", "یہ گروہ بند مواد ہے۔", "Grouped is about classes, not about counting.", "گروہ بند کا تعلق گروہوں سے ہے، گننے سے نہیں۔", "grouped_ungrouped_mix")],
      0, qtype=None)},
 ],
 review=[
   {"id": "r_width", "type": "apply", "step": nq("r_width", ("How many whole numbers are in the class 30-39?", "گروہ 30-39 میں کتنے مکمل اعداد ہیں؟"), R1,
      ("List them from 30 to 39.", "30 سے 39 تک لکھیں۔"),
      ("Right! There are 10 numbers.", "درست! 10 اعداد ہیں۔"), ("30, 31, ..., 39 is ten numbers.", "30، 31، ...، 39 یعنی دس اعداد"),
      [(9, "39 − 30 = 9 forgets 30 itself. Add 1: 10.", "39 − 30 = 9 میں خود 30 رہ جاتا ہے۔ 1 جمع کریں: 10", "class_width_off")], qtype=None)},
   {"id": "r_total", "type": "apply", "step": nq("r_total", ("A frequency table has the frequencies 5, 9 and 6. How many values are there altogether?", "ایک تعدد جدول میں تعدد 5، 9 اور 6 ہیں۔ کل کتنی قیمتیں ہیں؟"), R2,
      ("Add the three frequencies.", "تینوں تعدد جمع کریں۔"),
      ("Right! 5 + 9 + 6 = 20.", "درست! 5 + 9 + 6 = 20"), ("5 + 9 = 14, and 14 + 6 = 20.", "5 + 9 = 14، اور 14 + 6 = 20"),
      [(9, "9 is the biggest frequency. Add all three: 20.", "9 سب سے بڑا تعدد ہے۔ تینوں جمع کریں: 20", "counted_wrong_class")], qtype=None)},
 ],
 glossary=[T("Data", "مواد (ڈیٹا)"), T("Grouped data", "گروہ بند مواد"), T("Ungrouped data", "غیر گروہ بند مواد"), T("Frequency", "تعدد"),
           T("Class (group)", "گروہ (جماعت)"), T("Discrete data", "منفصل مواد"), T("Continuous data", "مسلسل مواد"), T("Table", "جدول")],
 flashcards=[
   {"id": "f_kinds", "front": T("How do you tell discrete from continuous data?", "منفصل اور مسلسل مواد میں فرق کیسے کرتے ہیں؟"),
    "back": T("Discrete data is counted (goals, pages). Continuous data is measured (height, time, weight).", "منفصل مواد گنا جاتا ہے (گول، صفحے)۔ مسلسل مواد ناپا جاتا ہے (قد، وقت، وزن)۔")},
   {"id": "f_class", "front": T("How many whole numbers are in the class 10-19?", "گروہ 10-19 میں کتنے مکمل اعداد ہیں؟"),
    "back": T("Ten: both 10 and 19 count.", "دس: 10 اور 19 دونوں گنے جاتے ہیں۔")},
 ],
 home_task={"id": "h_data", "text": T(
   "Ask 15 people at home or in your street how many brothers and sisters they have, and write the answers one by one (ungrouped data). Then put them in a frequency table. Say whether your data is discrete or continuous, and why.",
   "گھر یا گلی کے 15 لوگوں سے پوچھیں کہ ان کے کتنے بہن بھائی ہیں، اور جوابات ایک ایک کر کے لکھیں (غیر گروہ بند مواد)۔ پھر انہیں تعدد جدول میں رکھیں۔ بتائیں کہ آپ کا مواد منفصل ہے یا مسلسل، اور کیوں۔")},
 notes=["Covers what data is and how it is collected (q1, q2), ungrouped and grouped data (q3, qb_grouped), reading and adding a frequency table (q4, q5, qb_total), the number of whole numbers in a class (q6, qb_width), discrete and continuous data (q7 to q9, q11) and sorting raw marks into a class (q10).",
        "Each wrong answer is a real mistake: counting the wrong class, subtracting to find the class width, and calling measured data discrete or counted data continuous.",
        "Urdu terms to check: مواد (ڈیٹا), گروہ بند مواد, غیر گروہ بند مواد, تعدد, گروہ (جماعت), منفصل مواد, مسلسل مواد and جدول, all as in the existing Data Handling lessons. New Urdu terms, which a teacher should confirm: مشاہدہ (observation), سروے (survey), انٹرویو (interview) and سوالنامہ (questionnaire)."],
 minutes=16,
)
for s in lesson["steps"]:
    pass
write(lesson)
