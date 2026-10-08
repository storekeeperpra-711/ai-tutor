from common import (T, opt, say, wrong, number_question, table_text, write,
                    BOOK, REVIEW, DH_TABLES, DH_KINDS)

SKILL = DH_KINDS


def in_class(data, lo, hi):
    """How many values fall in the class lo–hi (both ends included)."""
    return sum(1 for x in data if lo <= x <= hi)


def nums(xs, sep=", "):
    return sep.join(str(x) for x in xs)


# s2: reading a table total (foundation)
FRUIT = [(("Mangoes", "آم"), 7), (("Bananas", "کیلے"), 5), (("Apples", "سیب"), 8)]
FRUIT_EN, FRUIT_UR = table_text(FRUIT)
S2 = sum(v for _, v in FRUIT)
assert S2 == 20

# s4, s5: test marks out of 30 of twelve children, grouped into 1–10, 11–20, 21–30
MARKS = (4, 17, 9, 22, 13, 28, 11, 6, 19, 25, 15, 8)
assert len(MARKS) == 12
S4 = in_class(MARKS, 11, 20)
assert S4 == 5
S5 = in_class(MARKS, 21, 30)
assert S5 == 3
assert in_class(MARKS, 1, 10) + S4 + S5 == len(MARKS)

# s8: total of a grouped frequency table
AGES = [(("Age 1–10", "عمر 1 تا 10"), 6), (("Age 11–20", "عمر 11 تا 20"), 9), (("Age 21–30", "عمر 21 تا 30"), 4)]
AGES_EN, AGES_UR = table_text(AGES, " people", " افراد")
S8 = sum(v for _, v in AGES)
assert S8 == 19

# s11: runs scored by ten batters, class 21–30
RUNS = (12, 25, 31, 8, 27, 22, 40, 19, 29, 35)
S11 = in_class(RUNS, 21, 30)
assert S11 == 4  # 25, 27, 22, 29
assert in_class(RUNS, 1, 10) == 1 and in_class(RUNS, 11, 20) == 2 and in_class(RUNS, 31, 40) == 3

# question bank: class 11–20
QB_DATA = (3, 14, 18, 7, 20, 11, 9)
QB = in_class(QB_DATA, 11, 20)
assert QB == 4  # 14, 18, 20, 11

# review: class 1–10
R2_DATA = (5, 12, 10, 1, 16, 7, 19)
R2 = in_class(R2_DATA, 1, 10)
assert R2 == 4  # 5, 10, 1, 7

lesson = {
 "id": "g6-maths-10-kinds-of-data",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Tell ungrouped data from grouped data, group values into classes and count the frequency of each class, and tell discrete (counted) data from continuous (measured) data.", "textbook": BOOK}],
 "skills": [SKILL],
 "title": T("Kinds of data", "مواد کی اقسام"),
 "estimated_minutes": 15,
 "prerequisites": [{"skill": DH_TABLES}],
 "misconceptions": [
   {"id": "whole_means_discrete", "description": "Thinks a measurement is discrete because it is written as a whole number (e.g. height in whole cm)."},
   {"id": "counts_class_edges", "description": "Leaves out values that sit exactly on the ends of a class, such as 20 in the class 11–20, or counts them in the wrong class."},
   {"id": "number_means_discrete", "description": "Thinks any data made of numbers is discrete, and only words are continuous (or the other way round)."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_continuous", "type": "recall", "step": {
     "id": "qb_continuous", "type": "choice",
     "prompt": T("What is continuous data?", "مسلسل مواد کیا ہوتا ہے؟"),
     "options": [
       opt("measured", "Data we get by measuring, like height or time", "وہ مواد جو ناپ کر ملے، جیسے قد یا وقت", True,
           "Yes! Measured data can take any value in between.", "جی ہاں! ناپا گیا مواد درمیان کی کوئی بھی قیمت لے سکتا ہے۔"),
       opt("counted", "Data we get by counting, like number of pens", "وہ مواد جو گن کر ملے، جیسے قلموں کی تعداد", False,
           "Counted data is discrete. Continuous data is measured.", "گنا گیا مواد منفصل ہے۔ مسلسل مواد ناپا جاتا ہے۔"),
       opt("words", "Data written in words, not numbers", "وہ مواد جو الفاظ میں لکھا ہو، اعداد میں نہیں", False,
           "Both kinds are numbers. Continuous data is measured.", "دونوں اقسام اعداد ہیں۔ مسلسل مواد ناپا جاتا ہے۔", "number_means_discrete"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T(f"Data: {nums(QB_DATA)}. How many values are in the class 11–20?", f"مواد: {nums(QB_DATA, '، ')}۔ گروہ 11 تا 20 میں کتنی قیمتیں ہیں؟"),
     QB,
     T("Look for values from 11 up to 20, including 11 and 20.", "11 سے 20 تک کی قیمتیں ڈھونڈیں، 11 اور 20 سمیت۔"),
     T("Right! 14, 18, 20 and 11.", "درست! 14، 18، 20 اور 11"),
     T("14, 18, 20 and 11 are in 11–20: that is 4.", "14، 18، 20 اور 11 گروہ 11 تا 20 میں ہیں: یہ 4 ہیں۔"),
     common_wrong=[wrong(3, "Don't forget 20. It is the end of the class, so it counts: 4.", "20 نہ بھولیں۔ یہ گروہ کا آخری عدد ہے، تو یہ گنا جائے گا: 4", "counts_class_edges")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Zainab says the time she takes to walk to school is discrete data, because her watch shows 12 minutes. What went wrong?",
                 "زینب کہتی ہے کہ اسکول پیدل جانے کا وقت منفصل مواد ہے، کیونکہ اس کی گھڑی 12 منٹ دکھاتی ہے۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("measured", "Time is measured, so it is continuous. It could be 12 and a half minutes.", "وقت ناپا جاتا ہے، اس لیے یہ مسلسل ہے۔ یہ ساڑھے 12 منٹ بھی ہو سکتا ہے۔", True,
           "Yes! A rounded reading is still a measurement.", "جی ہاں! گول کی ہوئی قیمت بھی پیمائش ہی ہے۔"),
       opt("nothing", "Nothing. 12 is a whole number.", "کوئی غلطی نہیں۔ 12 مکمل عدد ہے۔", False,
           "The watch rounds it. Time is measured, so it is continuous.", "گھڑی اسے گول کرتی ہے۔ وقت ناپا جاتا ہے، اس لیے مسلسل ہے۔", "whole_means_discrete"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_disc_cont", "front": T("Discrete or continuous?", "منفصل یا مسلسل؟"),
    "back": T("Counted (children, goals) = discrete. Measured (height, weight, time) = continuous.", "گنا گیا (بچے، گول) = منفصل۔ ناپا گیا (قد، وزن، وقت) = مسلسل۔")},
   {"id": "f_grouped", "front": T("Grouped data?", "گروہ بند مواد؟"),
    "back": T("Values put into classes like 1–10, 11–20, with how many fall in each (the frequency).", "قیمتیں گروہوں میں رکھی جائیں جیسے 1 تا 10، 11 تا 20، اور ہر ایک میں کتنی ہیں (تعدد)۔")},
 ],
 "home_tasks": [{"id": "h_family", "text": T(
   "Write down two things about your family you can count (like number of cousins) and two things you can measure (like each person's height). Which are discrete and which are continuous?",
   "اپنے گھر والوں کے بارے میں دو چیزیں لکھیں جو گنی جا سکیں (جیسے کزنز کی تعداد) اور دو جو ناپی جا سکیں (جیسے ہر ایک کا قد)۔ کون سی منفصل ہیں اور کون سی مسلسل؟")}],
 "glossary": [T("Ungrouped data", "غیر گروہ بند مواد"), T("Grouped data", "گروہ بند مواد"), T("Class (group)", "گروہ (جماعت)"),
              T("Frequency", "تعدد"), T("Discrete data", "منفصل مواد"), T("Continuous data", "مسلسل مواد")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Hamza counted his class: 32 children. Then he measured his height: 141 cm. Are these the same kind of number?",
                     "حمزہ نے اپنی جماعت گنی: 32 بچے۔ پھر اپنا قد ناپا: 141 سینٹی میٹر۔ کیا یہ ایک ہی قسم کے اعداد ہیں؟"),
    "text": T("Today we learn the kinds of data: ungrouped and grouped, discrete and continuous. First, a quick check.",
              "آج ہم مواد کی اقسام سیکھیں گے: غیر گروہ بند اور گروہ بند، منفصل اور مسلسل۔ پہلے ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T(f"Fruit sold at a stall: {FRUIT_EN}. How many fruits altogether?", f"ایک ٹھیلے پر بکنے والے پھل: {FRUIT_UR}۔ کل کتنے پھل؟"),
     S2,
     T("Add all three.", "تینوں جمع کریں۔"),
     T("Right! 20.", "درست! 20"),
     T("7 + 5 + 8 = 20.", "7 + 5 + 8 = 20"),
     common_wrong=[wrong(3, "3 is the number of kinds of fruit. Add them: 20.", "3 پھلوں کی اقسام کی تعداد ہے۔ جمع کریں: 20")],
     qtype="recall", skill=DH_TABLES),
   {"id": "s3_kinds", "type": "explain",
    "character": say("happy", "Counted things jump in steps of one. Measured things can be any size in between!",
                     "گنی جانے والی چیزیں ایک ایک کر کے بڑھتی ہیں۔ ناپی جانے والی چیزیں درمیان کی کوئی بھی قیمت لے سکتی ہیں!"),
    "text": T("Ungrouped data is a plain list of values, like 4, 17, 9, 22. When there are many values, we make grouped data: we choose classes such as 1–10, 11–20 and 21–30, and count how many values fall in each class. That count is the frequency. Both ends belong to the class: 20 goes in 11–20.\n"
              "Discrete data is counted: number of children, goals, books. It can only be whole steps (you can't have 2.5 children). Continuous data is measured: height, weight, time, temperature. It can take any value in between, like 141.5 cm, even if we round it.",
              "غیر گروہ بند مواد قیمتوں کی سادہ فہرست ہے، جیسے 4، 17، 9، 22۔ جب قیمتیں بہت ہوں تو ہم گروہ بند مواد بناتے ہیں: ہم گروہ چنتے ہیں جیسے 1 تا 10، 11 تا 20 اور 21 تا 30، اور گنتے ہیں کہ ہر گروہ میں کتنی قیمتیں ہیں۔ یہ گنتی تعدد کہلاتی ہے۔ دونوں سرے گروہ میں شامل ہیں: 20 گروہ 11 تا 20 میں جائے گا۔\n"
              "منفصل مواد گنا جاتا ہے: بچوں، گولوں یا کتابوں کی تعداد۔ یہ صرف پورے قدموں میں ہوتا ہے (ڈھائی بچے نہیں ہو سکتے)۔ مسلسل مواد ناپا جاتا ہے: قد، وزن، وقت، درجہ حرارت۔ یہ درمیان کی کوئی بھی قیمت لے سکتا ہے، جیسے 141.5 سینٹی میٹر، چاہے ہم اسے گول کر دیں۔")},
   number_question(
     "s4_class_count",
     T(f"Test marks out of 30 of twelve children: {nums(MARKS)}. How many marks are in the class 11–20?",
       f"بارہ بچوں کے 30 میں سے ٹیسٹ نمبر: {nums(MARKS, '، ')}۔ گروہ 11 تا 20 میں کتنے نمبر ہیں؟"),
     S4,
     T("Go through the list and tick each mark from 11 to 20.", "فہرست میں سے ہر وہ نمبر نشان لگائیں جو 11 سے 20 تک ہو۔"),
     T("Right! 17, 13, 11, 19 and 15.", "درست! 17، 13، 11، 19 اور 15"),
     T("17, 13, 11, 19 and 15 are in 11–20: that is 5.", "17، 13، 11، 19 اور 15 گروہ 11 تا 20 میں ہیں: یہ 5 ہیں۔"),
     common_wrong=[wrong(4, "Don't leave out 11. It is the start of the class: 5.", "11 نہ چھوڑیں۔ یہ گروہ کا پہلا عدد ہے: 5", "counts_class_edges"),
                   wrong(12, "12 is how many children there are. Count only marks from 11 to 20: 5.", "12 بچوں کی تعداد ہے۔ صرف 11 سے 20 تک کے نمبر گنیں: 5")]),
   number_question(
     "s5_class_count",
     T(f"Same marks: {nums(MARKS)}. What is the frequency of the class 21–30?",
       f"وہی نمبر: {nums(MARKS, '، ')}۔ گروہ 21 تا 30 کا تعدد کیا ہے؟"),
     S5,
     T("Frequency means how many. Count marks from 21 to 30.", "تعدد کا مطلب ہے کتنے۔ 21 سے 30 تک کے نمبر گنیں۔"),
     T("Right! 22, 28 and 25.", "درست! 22، 28 اور 25"),
     T("22, 28 and 25 are in 21–30: the frequency is 3.", "22، 28 اور 25 گروہ 21 تا 30 میں ہیں: تعدد 3 ہے۔"),
     common_wrong=[wrong(4, "4 is how many are in 1–10. For 21–30 there are 3.", "4 گروہ 1 تا 10 میں ہیں۔ 21 تا 30 میں 3 ہیں۔")]),
   {"id": "s6_which_continuous", "type": "choice", "question_type": "apply",
    "prompt": T("Which of these is continuous data?", "ان میں سے کون سا مسلسل مواد ہے؟"),
    "options": [
      opt("weight", "The weights of children in a class", "جماعت کے بچوں کے وزن", True,
          "Yes! Weight is measured, so it is continuous.", "جی ہاں! وزن ناپا جاتا ہے، اس لیے یہ مسلسل ہے۔"),
      opt("brothers", "The number of brothers each child has", "ہر بچے کے بھائیوں کی تعداد", False,
          "Brothers are counted, so that is discrete.", "بھائی گنے جاتے ہیں، اس لیے یہ منفصل ہے۔"),
      opt("goals", "Goals scored in hockey matches", "ہاکی میچوں میں کیے گئے گول", False,
          "Goals are counted, so that is discrete.", "گول گنے جاتے ہیں، اس لیے یہ منفصل ہے۔", "number_means_discrete"),
    ]},
   {"id": "s7_mangoes", "type": "choice", "question_type": "apply",
    "prompt": T("Bilal records the number of mangoes in each crate at his father's shop. What kind of data is this?",
                "بلال اپنے ابو کی دکان پر ہر پیٹی میں آموں کی تعداد لکھتا ہے۔ یہ کس قسم کا مواد ہے؟"),
    "options": [
      opt("discrete", "Discrete", "منفصل", True,
          "Yes! Mangoes are counted: 40, 41, 42, never 40.5.", "جی ہاں! آم گنے جاتے ہیں: 40، 41، 42، کبھی 40.5 نہیں۔"),
      opt("continuous", "Continuous", "مسلسل", False,
          "The number of mangoes is counted, not measured, so it is discrete.", "آموں کی تعداد گنی جاتی ہے، ناپی نہیں جاتی، اس لیے یہ منفصل ہے۔"),
    ]},
   number_question(
     "s8_total_freq",
     T(f"A grouped table of the ages of people at a wedding: {AGES_EN}. How many people are in the table altogether?",
       f"ایک شادی میں لوگوں کی عمروں کا گروہ بند جدول: {AGES_UR}۔ جدول میں کل کتنے افراد ہیں؟"),
     S8,
     T("Add the frequencies of all the classes.", "سب گروہوں کے تعدد جمع کریں۔"),
     T("Right! 19 people.", "درست! 19 افراد"),
     T("6 + 9 + 4 = 19.", "6 + 9 + 4 = 19"),
     common_wrong=[wrong(3, "3 is the number of classes. Add the frequencies: 19.", "3 گروہوں کی تعداد ہے۔ تعدد جمع کریں: 19"),
                   wrong(30, "30 is the end of the last class. Add the frequencies: 19.", "30 آخری گروہ کا آخری عدد ہے۔ تعدد جمع کریں: 19")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Fatima says: \"Height is discrete data, because we always write it in whole centimetres, like 138 cm.\" What went wrong?",
                "فاطمہ کہتی ہے: \"قد منفصل مواد ہے، کیونکہ ہم اسے ہمیشہ پورے سینٹی میٹر میں لکھتے ہیں، جیسے 138 سینٹی میٹر۔\" کیا غلطی ہوئی؟"),
    "options": [
      opt("measured", "Height is measured. It could be 138.4 cm; we just round it. So it is continuous.", "قد ناپا جاتا ہے۔ یہ 138.4 سینٹی میٹر بھی ہو سکتا ہے؛ ہم بس اسے گول کرتے ہیں۔ اس لیے یہ مسلسل ہے۔", True,
          "Yes! Rounding doesn't change the kind of data.", "جی ہاں! گول کرنے سے مواد کی قسم نہیں بدلتی۔"),
      opt("nothing", "Nothing. Whole numbers are always discrete.", "کوئی غلطی نہیں۔ مکمل اعداد ہمیشہ منفصل ہوتے ہیں۔", False,
          "We write whole cm only because we round. Height is measured, so it is continuous.", "ہم صرف گول کرنے کی وجہ سے پورے سینٹی میٹر لکھتے ہیں۔ قد ناپا جاتا ہے، اس لیے مسلسل ہے۔", "whole_means_discrete"),
      opt("grouped", "Height is grouped data, not discrete.", "قد گروہ بند مواد ہے، منفصل نہیں۔", False,
          "Any data can be grouped. The question is counted or measured: height is measured, so continuous.", "کوئی بھی مواد گروہ بند ہو سکتا ہے۔ سوال یہ ہے کہ گنا گیا یا ناپا گیا: قد ناپا جاتا ہے، اس لیے مسلسل۔"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "The number of children is discrete, but their heights are continuous. Why? Can you teach me?",
                     "بچوں کی تعداد منفصل ہے، لیکن ان کے قد مسلسل ہیں۔ کیوں؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why is the number of children discrete, but their heights continuous?",
              "اپنے الفاظ میں بتائیں: بچوں کی تعداد منفصل کیوں ہے، لیکن ان کے قد مسلسل کیوں ہیں؟"),
    "key_idea": "Children are counted, so the number can only go up in whole steps (no half child). Height is measured, so it can be any value between two whole centimetres, even if we round when we write it.",
    "levels": {
      "got_it": "Says children are counted in whole steps while height is measured and can take any value in between.",
      "partly": "Mentions counting or measuring, but not both, or doesn't say why that matters.",
      "not_yet": "Gives no reason, or says it depends on whether the number is whole."},
    "keywords": [
      ["count", "گن", "گنتی"],
      ["measure", "ناپ", "پیمائش"],
      ["between", "half", "any", "درمیان", "آدھا", "کوئی بھی"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Counted means discrete, measured means continuous.", "بہت خوب! گنا گیا یعنی منفصل، ناپا گیا یعنی مسلسل۔"),
      "partly": T("Good start! Now say which one is counted and which is measured.", "اچھی شروعات! اب بتائیں کون سا گنا جاتا ہے اور کون سا ناپا جاتا ہے۔"),
      "not_yet": T("Can a class have 32 and a half children? Can a child be 141 and a half cm tall?", "کیا جماعت میں ساڑھے 32 بچے ہو سکتے ہیں؟ کیا کسی بچے کا قد ساڑھے 141 سینٹی میٹر ہو سکتا ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_runs",
     T(f"Runs scored by ten batters in a school match: {nums(RUNS)}. How many scores are in the class 21–30?",
       f"اسکول کے ایک میچ میں دس بلے بازوں کے رنز: {nums(RUNS, '، ')}۔ گروہ 21 تا 30 میں کتنے اسکور ہیں؟"),
     S11,
     T("Tick each score from 21 to 30.", "21 سے 30 تک کا ہر اسکور نشان لگائیں۔"),
     T("Right! 25, 27, 22 and 29.", "درست! 25، 27، 22 اور 29"),
     T("25, 27, 22 and 29 are in 21–30: that is 4.", "25، 27، 22 اور 29 گروہ 21 تا 30 میں ہیں: یہ 4 ہیں۔"),
     common_wrong=[wrong(5, "31 is not in 21–30; it starts the next class. The answer is 4.", "31 گروہ 21 تا 30 میں نہیں؛ یہ اگلا گروہ شروع کرتا ہے۔ جواب 4 ہے۔", "counts_class_edges"),
                   wrong(10, "10 is how many batters there are. Count only 21 to 30: 4.", "10 بلے بازوں کی تعداد ہے۔ صرف 21 تا 30 گنیں: 4")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Now you can sort data like a scientist!", "اب آپ سائنس دان کی طرح مواد کو ترتیب دے سکتے ہیں!"),
    "text": T("Ungrouped data is a plain list. Grouped data puts values into classes like 1–10, 11–20, and the frequency is how many are in each class (both ends count). Discrete data is counted (children, goals); continuous data is measured (height, weight, time, temperature), even when we round it.",
              "غیر گروہ بند مواد ایک سادہ فہرست ہے۔ گروہ بند مواد قیمتوں کو گروہوں میں رکھتا ہے جیسے 1 تا 10، 11 تا 20، اور تعدد یہ ہے کہ ہر گروہ میں کتنی قیمتیں ہیں (دونوں سرے شامل)۔ منفصل مواد گنا جاتا ہے (بچے، گول)؛ مسلسل مواد ناپا جاتا ہے (قد، وزن، وقت، درجہ حرارت)، چاہے ہم اسے گول کر دیں۔"),
    "points": [T("Grouped data: classes and their frequencies.", "گروہ بند مواد: گروہ اور ان کے تعدد۔"),
               T("Counted = discrete. Measured = continuous.", "گنا گیا = منفصل۔ ناپا گیا = مسلسل۔")]},
 ],
 "review_questions": [
   {"id": "r_temp", "type": "apply", "skill": SKILL, "step": {
     "id": "r_temp", "type": "choice",
     "prompt": T("The temperature in Lahore at noon each day is recorded. What kind of data is this?", "لاہور میں ہر روز دوپہر کا درجہ حرارت لکھا جاتا ہے۔ یہ کس قسم کا مواد ہے؟"),
     "options": [
       opt("continuous", "Continuous", "مسلسل", True,
           "Yes! Temperature is measured.", "جی ہاں! درجہ حرارت ناپا جاتا ہے۔"),
       opt("discrete", "Discrete", "منفصل", False,
           "Temperature is measured, not counted, so it is continuous.", "درجہ حرارت ناپا جاتا ہے، گنا نہیں جاتا، اس لیے مسلسل ہے۔", "whole_means_discrete"),
     ]}},
   {"id": "r_class", "type": "apply", "skill": SKILL, "step": number_question(
     "r_class",
     T(f"Data: {nums(R2_DATA)}. What is the frequency of the class 1–10?", f"مواد: {nums(R2_DATA, '، ')}۔ گروہ 1 تا 10 کا تعدد کیا ہے؟"),
     R2,
     T("Count values from 1 to 10, including 10.", "1 سے 10 تک کی قیمتیں گنیں، 10 سمیت۔"),
     T("Right! 5, 10, 1 and 7.", "درست! 5، 10، 1 اور 7"),
     T("5, 10, 1 and 7 are in 1–10: the frequency is 4.", "5، 10، 1 اور 7 گروہ 1 تا 10 میں ہیں: تعدد 4 ہے۔"),
     common_wrong=[wrong(3, "Don't forget 10. It is the end of the class: 4.", "10 نہ بھولیں۔ یہ گروہ کا آخری عدد ہے: 4", "counts_class_edges")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Data Management sub-domain (kinds of data). No textbook text or exercises were used.",
   "Classes include both ends (1–10, 11–20, ...), so a value like 20 goes in 11–20. With no pictures yet, data are given as lists and tables written in a line.",
   "The key test for discrete vs continuous is counted vs measured; the find-error steps target the idea that a rounded whole number (138 cm, 12 minutes) makes data discrete.",
   "Urdu terms to check: مواد (data), گروہ بند مواد / غیر گروہ بند مواد (grouped / ungrouped data), گروہ (class), تعدد (frequency), منفصل مواد (discrete data), مسلسل مواد (continuous data).",
   "The numbers were worked out in content/sources/g6-maths-10/kinds_of_data.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)
