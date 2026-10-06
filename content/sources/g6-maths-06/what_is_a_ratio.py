from common import (F, T, opt, say, wrong, ratio, ratio_question, write,
                    REF, REVIEW, UNIT_FRACTIONS, TIMES_TABLES, RATIO_MEANING)

SKILL = RATIO_MEANING

# Amna's basket: 3 mangoes and 5 apples (s1 to s4).
MANGOES, APPLES = 3, 5
assert F(MANGOES, MANGOES + APPLES) == F(3, 8)

# s5, s6: 12 girls and 15 boys in a class.
GIRLS, BOYS = 12, 15
CLASS = GIRLS + BOYS
assert CLASS == 27

# s7: 30 children, 13 girls: boys to girls is 17 : 13.
BOYS_7 = 30 - 13
assert BOYS_7 == 17

# s9: a 15 cm pencil and a 1 m (100 cm) ruler.
PENCIL_CM, RULER_CM = 15, 100

# s11: 2 cups of rice, 3 cups of water: water to rice is 3 : 2.
RICE, WATER = 2, 3

lesson = {
 "id": "g6-maths-06-what-is-a-ratio",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Understand a ratio as a comparison of two quantities of the same kind, and write it in the right order as a : b.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("What is a ratio?", "نسبت کیا ہے؟"),
 "estimated_minutes": 12,
 "prerequisites": [{"skill": UNIT_FRACTIONS}, {"skill": TIMES_TABLES}],
 "misconceptions": [
   {"id": "order_swapped", "description": "Writes the two numbers of a ratio the wrong way round (5 : 3 for mangoes to apples when there are 3 mangoes and 5 apples)."},
   {"id": "part_for_whole", "description": "Uses the total instead of a part (girls to boys written as girls to the whole class), or a part instead of the total."},
   {"id": "mixed_units", "description": "Compares quantities in different units (15 cm to 1 m written as 15 : 1)."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_what_is_ratio", "type": "recall", "step": {
     "id": "qb_what_is_ratio", "type": "choice",
     "prompt": T("What does the ratio 2 : 7 of boys to girls tell us?", "لڑکوں اور لڑکیوں کی نسبت 2 : 7 ہمیں کیا بتاتی ہے؟"),
     "options": [
       opt("a", "For every 2 boys there are 7 girls.", "ہر 2 لڑکوں کے مقابلے میں 7 لڑکیاں ہیں۔", True,
           "Yes! A ratio compares: 2 boys for every 7 girls.", "جی ہاں! نسبت موازنہ کرتی ہے: ہر 2 لڑکوں کے مقابلے میں 7 لڑکیاں۔"),
       opt("b", "There are 2 boys and 7 children in all.", "2 لڑکے ہیں اور کل 7 بچے ہیں۔", False,
           "The 7 is the girls, not all the children. The ratio compares boys with girls.", "7 لڑکیاں ہیں، کل بچے نہیں۔ نسبت لڑکوں کا موازنہ لڑکیوں سے کرتی ہے۔", "part_for_whole"),
       opt("c", "For every 2 girls there are 7 boys.", "ہر 2 لڑکیوں کے مقابلے میں 7 لڑکے ہیں۔", False,
           "The order matters: boys come first, so 2 is the boys and 7 is the girls.", "ترتیب اہم ہے: لڑکے پہلے ہیں، اس لیے 2 لڑکے ہیں اور 7 لڑکیاں۔", "order_swapped"),
     ]}},
   {"id": "qb_write_ratio", "type": "apply", "step": ratio_question(
     "qb_write_ratio",
     T("A shop has 9 red balloons and 4 blue balloons. Write the ratio of blue balloons to red balloons.",
       "ایک دکان میں 9 سرخ اور 4 نیلے غبارے ہیں۔ نیلے غباروں اور سرخ غباروں کی نسبت لکھیں۔"),
     4, 9,
     T("Blue is named first, so the blue number goes first.", "نیلا پہلے آیا ہے، اس لیے نیلے غباروں کا عدد پہلے لکھیں۔"),
     T("Right! Blue to red is 4 : 9.", "درست! نیلے اور سرخ کی نسبت 4 : 9 ہے۔"),
     T("Blue comes first in the question: 4 blue to 9 red, so 4 : 9.", "سوال میں نیلا پہلے ہے: 4 نیلے اور 9 سرخ، یعنی 4 : 9"),
     common_wrong=[wrong("9:4", "That is red to blue. The question asks blue to red, so blue goes first.", "یہ سرخ اور نیلے کی نسبت ہے۔ سوال نیلے اور سرخ کی نسبت پوچھتا ہے، اس لیے نیلا پہلے۔", "order_swapped")],
     qtype=None)},
   {"id": "qb_find_error_units", "type": "find_error", "step": {
     "id": "qb_find_error_units", "type": "choice",
     "prompt": T("Kamran says the ratio of 50 paisa to 1 rupee is 50 : 1. Is he right?", "کامران کہتا ہے کہ 50 پیسے اور 1 روپے کی نسبت 50 : 1 ہے۔ کیا وہ درست ہے؟"),
     "options": [
       opt("no", "No. 1 rupee is 100 paisa, so the ratio is 50 : 100.", "نہیں۔ 1 روپیہ 100 پیسے ہے، اس لیے نسبت 50 : 100 ہے۔", True,
           "Right! Change both to the same unit first: 50 paisa to 100 paisa.", "درست! پہلے دونوں کو ایک ہی اکائی میں بدلیں: 50 پیسے اور 100 پیسے۔"),
       opt("yes", "Yes. He wrote the two numbers in the right order.", "ہاں۔ اس نے دونوں عدد صحیح ترتیب میں لکھے۔", False,
           "The order is right, but paisa and rupees are different units. 1 rupee = 100 paisa.", "ترتیب ٹھیک ہے، لیکن پیسے اور روپے مختلف اکائیاں ہیں۔ 1 روپیہ = 100 پیسے۔", "mixed_units"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_ratio", "front": T("What is a ratio?", "نسبت کیا ہے؟"),
    "back": T("A way to compare two amounts of the same kind. 3 mangoes and 5 apples: mangoes to apples is 3 : 5, read \"3 to 5\".",
              "ایک ہی قسم کی دو مقداروں کا موازنہ کرنے کا طریقہ۔ 3 آم اور 5 سیب: آم اور سیب کی نسبت 3 : 5 ہے، پڑھیں \"3 اور 5\"۔")},
   {"id": "f_order", "front": T("Does the order of a ratio matter?", "کیا نسبت میں ترتیب اہم ہے؟"),
    "back": T("Yes. Write the numbers in the order the question names them. Mangoes to apples 3 : 5 is not the same as apples to mangoes 5 : 3.",
              "جی ہاں۔ عدد اسی ترتیب میں لکھیں جس میں سوال نام لیتا ہے۔ آم اور سیب 3 : 5، سیب اور آم 5 : 3 جیسا نہیں۔")},
 ],
 "home_tasks": [{"id": "h_count_home", "text": T(
   "Count the spoons and the plates in your kitchen. Write the ratio of spoons to plates, and then plates to spoons. Are they the same?",
   "اپنے باورچی خانے میں چمچ اور پلیٹیں گنیں۔ چمچوں اور پلیٹوں کی نسبت لکھیں، پھر پلیٹوں اور چمچوں کی۔ کیا یہ ایک جیسی ہیں؟")}],
 "glossary": [T("Ratio", "نسبت"), T("Compare", "موازنہ کرنا"), T("Order", "ترتیب"), T("Unit", "اکائی")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious",
      "Amna's basket has 3 mangoes and 5 apples. How can we compare them in one short way?",
      "آمنہ کی ٹوکری میں 3 آم اور 5 سیب ہیں۔ ہم انہیں ایک مختصر طریقے سے کیسے موازنہ کریں؟"),
    "text": T("Today we learn a new way to compare two amounts. First, a quick check.",
              "آج ہم دو مقداروں کا موازنہ کرنے کا ایک نیا طریقہ سیکھیں گے۔ پہلے ایک چھوٹا سا سوال۔")},
   {"id": "s2_foundation", "type": "choice", "question_type": "recall", "skill": UNIT_FRACTIONS,
    "prompt": T("Amna has 3 mangoes and 5 apples: 8 fruits in all. What fraction of the fruits are mangoes?",
                "آمنہ کے پاس 3 آم اور 5 سیب ہیں: کل 8 پھل۔ پھلوں کا کتنا حصہ آم ہیں؟"),
    "options": [
      opt("three_eighths", "3/8", "3/8", True,
          "Yes! 3 of the 8 fruits are mangoes: 3/8.", "جی ہاں! 8 پھلوں میں سے 3 آم ہیں: 3/8"),
      opt("three_fifths", "3/5", "3/5", False,
          "A fraction compares a part with the whole. The whole is all 8 fruits, so 3/8.", "کسر ایک حصے کا موازنہ پورے سے کرتی ہے۔ پورا 8 پھل ہیں، اس لیے 3/8", "part_for_whole"),
      opt("five_eighths", "5/8", "5/8", False,
          "5/8 of the fruits are apples. The mangoes are 3 of the 8.", "5/8 پھل سیب ہیں۔ آم 8 میں سے 3 ہیں۔"),
    ]},
   {"id": "s3_see_it", "type": "explain",
    "character": say("happy", "A ratio compares one part with another part!", "نسبت ایک حصے کا دوسرے حصے سے موازنہ کرتی ہے!"),
    "text": T(f"A fraction compares a part with the whole: 3/8 of the fruits are mangoes. A ratio compares two amounts with each other. Mangoes to apples is {ratio(MANGOES, APPLES)}, read \"3 to 5\": for every 3 mangoes there are 5 apples. The order matters: apples to mangoes is {ratio(APPLES, MANGOES)}.",
              f"کسر ایک حصے کا موازنہ پورے سے کرتی ہے: 3/8 پھل آم ہیں۔ نسبت دو مقداروں کا آپس میں موازنہ کرتی ہے۔ آم اور سیب کی نسبت {ratio(MANGOES, APPLES)} ہے، پڑھیں \"3 اور 5\": ہر 3 آموں کے مقابلے میں 5 سیب ہیں۔ ترتیب اہم ہے: سیب اور آم کی نسبت {ratio(APPLES, MANGOES)} ہے۔")},
   ratio_question(
     "s4_write_ratio",
     T("Write the ratio of apples to mangoes in Amna's basket (5 apples, 3 mangoes).", "آمنہ کی ٹوکری میں سیب اور آم کی نسبت لکھیں (5 سیب، 3 آم)۔"),
     APPLES, MANGOES,
     T("Apples are named first, so the number of apples goes first.", "سیب پہلے آئے ہیں، اس لیے سیبوں کا عدد پہلے لکھیں۔"),
     T("Right! Apples to mangoes is 5 : 3.", "درست! سیب اور آم کی نسبت 5 : 3 ہے۔"),
     T("Apples come first in the question: 5 apples to 3 mangoes, so 5 : 3.", "سوال میں سیب پہلے ہیں: 5 سیب اور 3 آم، یعنی 5 : 3"),
     common_wrong=[wrong(ratio(MANGOES, APPLES), "That is mangoes to apples. This time apples come first.", "یہ آم اور سیب کی نسبت ہے۔ اس بار سیب پہلے ہیں۔", "order_swapped")]),
   {"id": "s5_class", "type": "choice", "question_type": "apply",
    "prompt": T(f"A class has {GIRLS} girls and {BOYS} boys. What is the ratio of girls to boys?",
                f"ایک جماعت میں {GIRLS} لڑکیاں اور {BOYS} لڑکے ہیں۔ لڑکیوں اور لڑکوں کی نسبت کیا ہے؟"),
    "options": [
      opt("right", ratio(GIRLS, BOYS), ratio(GIRLS, BOYS), True,
          f"Yes! {GIRLS} girls for {BOYS} boys.", f"جی ہاں! {GIRLS} لڑکیاں اور {BOYS} لڑکے۔"),
      opt("swapped", ratio(BOYS, GIRLS), ratio(BOYS, GIRLS), False,
          "That is boys to girls. Girls are named first.", "یہ لڑکوں اور لڑکیوں کی نسبت ہے۔ لڑکیاں پہلے آئی ہیں۔", "order_swapped"),
      opt("whole", ratio(GIRLS, CLASS), ratio(GIRLS, CLASS), False,
          f"{CLASS} is the whole class. The question compares girls with boys only.", f"{CLASS} پوری جماعت ہے۔ سوال صرف لڑکیوں کا لڑکوں سے موازنہ کرتا ہے۔", "part_for_whole"),
    ]},
   {"id": "s6_part_whole", "type": "explain",
    "character": say("thinking", "Read the question carefully: which two amounts does it compare?", "سوال غور سے پڑھیں: یہ کن دو مقداروں کا موازنہ کرتا ہے؟"),
    "text": T(f"A ratio can also compare a part with the whole. Girls to the whole class is {ratio(GIRLS, CLASS)}, because {GIRLS} + {BOYS} = {CLASS}. Always check which two amounts the question names, and in which order.",
              f"نسبت ایک حصے کا پورے سے بھی موازنہ کر سکتی ہے۔ لڑکیوں اور پوری جماعت کی نسبت {ratio(GIRLS, CLASS)} ہے، کیونکہ {GIRLS} + {BOYS} = {CLASS}۔ ہمیشہ دیکھیں کہ سوال کن دو مقداروں کا نام لیتا ہے، اور کس ترتیب میں۔")},
   {"id": "s7_missing_part", "type": "number", "question_type": "apply",
    "prompt": T("A class of 30 children has 13 girls. The ratio of boys to girls is ? : 13. What is the missing number?",
                "30 بچوں کی ایک جماعت میں 13 لڑکیاں ہیں۔ لڑکوں اور لڑکیوں کی نسبت ? : 13 ہے۔ غائب عدد کیا ہے؟"),
    "answer": BOYS_7, "checker": "numeric",
    "hint": T("First find how many boys there are: 30 children take away 13 girls.", "پہلے معلوم کریں کہ لڑکے کتنے ہیں: 30 بچوں میں سے 13 لڑکیاں نکالیں۔"),
    "feedback_correct": T(f"Right! 30 − 13 = {BOYS_7} boys, so boys to girls is {ratio(BOYS_7, 13)}.", f"درست! 30 − 13 = {BOYS_7} لڑکے، اس لیے لڑکوں اور لڑکیوں کی نسبت {ratio(BOYS_7, 13)} ہے۔"),
    "feedback_wrong": T(f"There are 30 − 13 = {BOYS_7} boys. Boys to girls is {ratio(BOYS_7, 13)}.", f"لڑکے 30 − 13 = {BOYS_7} ہیں۔ لڑکوں اور لڑکیوں کی نسبت {ratio(BOYS_7, 13)} ہے۔"),
    "common_wrong": [
      wrong(30, "30 is all the children. The ratio needs the number of boys only.", "30 تمام بچے ہیں۔ نسبت کے لیے صرف لڑکوں کی تعداد چاہیے۔", "part_for_whole"),
      wrong(13, "13 is the girls, and they are already in the ratio. How many boys are there?", "13 لڑکیاں ہیں، اور وہ نسبت میں پہلے سے ہیں۔ لڑکے کتنے ہیں؟"),
    ]},
   {"id": "s8_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Usman has 4 pencils and 7 pens. He writes: pencils to pens = 7 : 4. What went wrong?",
                "عثمان کے پاس 4 پنسلیں اور 7 قلم ہیں۔ وہ لکھتا ہے: پنسلوں اور قلموں کی نسبت = 7 : 4۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("order", "He wrote them the wrong way round. Pencils come first: 4 : 7.", "اس نے الٹا لکھا۔ پنسلیں پہلے ہیں: 4 : 7", True,
          "Yes! 7 : 4 would mean 7 pencils for 4 pens.", "جی ہاں! 7 : 4 کا مطلب ہوگا 7 پنسلیں اور 4 قلم۔"),
      opt("nothing", "Nothing. 7 : 4 and 4 : 7 are the same.", "کوئی غلطی نہیں۔ 7 : 4 اور 4 : 7 ایک جیسے ہیں۔", False,
          "They are not the same: 4 : 7 means fewer pencils than pens, 7 : 4 means more.", "یہ ایک جیسے نہیں: 4 : 7 کا مطلب قلموں سے کم پنسلیں، 7 : 4 کا مطلب زیادہ۔", "order_swapped"),
      opt("total", "He should write 4 : 11, because there are 11 things.", "اسے 4 : 11 لکھنا چاہیے، کیونکہ کل 11 چیزیں ہیں۔", False,
          "4 : 11 is pencils to all the things. The question asks pencils to pens.", "4 : 11 پنسلوں اور تمام چیزوں کی نسبت ہے۔ سوال پنسلوں اور قلموں کی نسبت پوچھتا ہے۔", "part_for_whole"),
    ]},
   {"id": "s9_units", "type": "choice", "question_type": "apply",
    "prompt": T(f"A pencil is {PENCIL_CM} cm long and a ruler is 1 m long. What is the ratio of the pencil's length to the ruler's length?",
                f"ایک پنسل {PENCIL_CM} سینٹی میٹر لمبی ہے اور ایک فٹا 1 میٹر لمبا ہے۔ پنسل اور فٹے کی لمبائی کی نسبت کیا ہے؟"),
    "options": [
      opt("same_units", ratio(PENCIL_CM, RULER_CM), ratio(PENCIL_CM, RULER_CM), True,
          f"Yes! 1 m = {RULER_CM} cm, so it is {PENCIL_CM} cm to {RULER_CM} cm.", f"جی ہاں! 1 میٹر = {RULER_CM} سینٹی میٹر، اس لیے {PENCIL_CM} سینٹی میٹر اور {RULER_CM} سینٹی میٹر۔"),
      opt("mixed", ratio(PENCIL_CM, 1), ratio(PENCIL_CM, 1), False,
          f"That compares cm with m. Change 1 m to {RULER_CM} cm first.", f"یہ سینٹی میٹر کا میٹر سے موازنہ ہے۔ پہلے 1 میٹر کو {RULER_CM} سینٹی میٹر میں بدلیں۔", "mixed_units"),
      opt("swapped", ratio(RULER_CM, PENCIL_CM), ratio(RULER_CM, PENCIL_CM), False,
          "That is the ruler to the pencil. The pencil is named first.", "یہ فٹے اور پنسل کی نسبت ہے۔ پنسل پہلے آئی ہے۔", "order_swapped"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Can you teach me? 3 : 5 and 5 : 3 use the same numbers. Aren't they the same?",
                     "کیا آپ مجھے سمجھا سکتے ہیں؟ 3 : 5 اور 5 : 3 میں ایک جیسے عدد ہیں۔ کیا یہ ایک جیسے نہیں؟"),
    "task": T("In your own words: Amna has 3 mangoes and 5 apples. Why is mangoes to apples 3 : 5 and not 5 : 3?",
              "اپنے الفاظ میں بتائیں: آمنہ کے پاس 3 آم اور 5 سیب ہیں۔ آم اور سیب کی نسبت 3 : 5 کیوں ہے، 5 : 3 کیوں نہیں؟"),
    "key_idea": "The numbers of a ratio go in the same order as the things named. Mangoes are named first, so the number of mangoes (3) comes first. 5 : 3 would mean 5 mangoes for 3 apples, which is a different basket.",
    "levels": {
      "got_it": "Says the first number belongs to the first thing named (mangoes), so 3 goes first; or explains that 5 : 3 would mean more mangoes than apples.",
      "partly": "Says the order matters or that mangoes come first, but does not link the order of the numbers with the order of the things.",
      "not_yet": "Says they are the same, gives no reason, or the reasoning is wrong."},
    "keywords": [
      ["order", "first", "ترتیب", "پہلے", "tarteeb", "pehle", "pehlay"],
      ["mango", "آم", "aam"],
      ["different", "not the same", "more", "مختلف", "زیادہ", "mukhtalif", "zyada", "ziada"]],
    "fallback_feedback": {
      "got_it": T("Well explained! The first number belongs to the first thing named, so mangoes to apples is 3 : 5.",
                  "بہت خوب سمجھایا! پہلا عدد پہلی چیز کا ہوتا ہے، اس لیے آم اور سیب کی نسبت 3 : 5 ہے۔"),
      "partly": T("Good start! Now say which number belongs to the mangoes, and why it goes first.",
                  "اچھی شروعات! اب بتائیں کہ کون سا عدد آموں کا ہے، اور وہ پہلے کیوں آتا ہے۔"),
      "not_yet": T("Think: what would 5 : 3 mean? 5 mangoes for 3 apples. Is that Amna's basket?",
                   "سوچیں: 5 : 3 کا کیا مطلب ہوگا؟ 5 آم اور 3 سیب۔ کیا یہ آمنہ کی ٹوکری ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   ratio_question(
     "s11_recipe",
     T(f"Nani cooks rice with {RICE} cups of rice and {WATER} cups of water. Write the ratio of water to rice.",
       f"نانی {RICE} کپ چاول اور {WATER} کپ پانی سے چاول پکاتی ہیں۔ پانی اور چاول کی نسبت لکھیں۔"),
     WATER, RICE,
     T("Water is named first.", "پانی پہلے آیا ہے۔"),
     T(f"Right! Water to rice is {ratio(WATER, RICE)}.", f"درست! پانی اور چاول کی نسبت {ratio(WATER, RICE)} ہے۔"),
     T(f"Water comes first: {WATER} cups of water to {RICE} cups of rice, so {ratio(WATER, RICE)}.", f"پانی پہلے ہے: {WATER} کپ پانی اور {RICE} کپ چاول، یعنی {ratio(WATER, RICE)}"),
     common_wrong=[
       wrong(ratio(RICE, WATER), "That is rice to water. Water comes first here.", "یہ چاول اور پانی کی نسبت ہے۔ یہاں پانی پہلے ہے۔", "order_swapped"),
       wrong(ratio(WATER, RICE + WATER), "That is water to all the cups. Compare water with rice only.", "یہ پانی اور تمام کپوں کی نسبت ہے۔ پانی کا موازنہ صرف چاول سے کریں۔", "part_for_whole"),
     ]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Now you can compare two amounts with a ratio!", "اب آپ نسبت سے دو مقداروں کا موازنہ کر سکتے ہیں!"),
    "text": T("A ratio compares two amounts of the same kind, written a : b and read \"a to b\". Write the numbers in the order the question names them, and change both amounts to the same unit first.",
              "نسبت ایک ہی قسم کی دو مقداروں کا موازنہ کرتی ہے، a : b لکھی اور \"a اور b\" پڑھی جاتی ہے۔ عدد اسی ترتیب میں لکھیں جس میں سوال نام لیتا ہے، اور پہلے دونوں مقداروں کو ایک ہی اکائی میں بدلیں۔"),
    "points": [T("Mangoes to apples: 3 : 5. Apples to mangoes: 5 : 3.", "آم اور سیب: 3 : 5۔ سیب اور آم: 5 : 3۔"),
               T("15 cm to 1 m is 15 : 100, not 15 : 1.", "15 سینٹی میٹر اور 1 میٹر کی نسبت 15 : 100 ہے، 15 : 1 نہیں۔")]},
 ],
 "review_questions": [
   {"id": "r_write_ratio", "type": "apply", "skill": SKILL, "step": ratio_question(
     "r_write_ratio",
     T("A garden has 6 rose plants and 11 mint plants. Write the ratio of mint plants to rose plants.", "ایک باغ میں گلاب کے 6 اور پودینے کے 11 پودے ہیں۔ پودینے اور گلاب کے پودوں کی نسبت لکھیں۔"),
     11, 6,
     T("Mint is named first.", "پودینہ پہلے آیا ہے۔"),
     T("Right! Mint to roses is 11 : 6.", "درست! پودینے اور گلاب کی نسبت 11 : 6 ہے۔"),
     T("Mint comes first: 11 mint to 6 roses, so 11 : 6.", "پودینہ پہلے ہے: 11 پودینہ اور 6 گلاب، یعنی 11 : 6"),
     common_wrong=[wrong("6:11", "That is roses to mint. Mint comes first.", "یہ گلاب اور پودینے کی نسبت ہے۔ پودینہ پہلے ہے۔", "order_swapped")],
     qtype=None)},
   {"id": "r_units", "type": "apply", "skill": SKILL, "step": {
     "id": "r_units", "type": "number",
     "prompt": T("Write 40 minutes to 1 hour as a ratio in minutes: 40 : ?. What is the missing number?", "40 منٹ اور 1 گھنٹے کو منٹوں میں نسبت کے طور پر لکھیں: 40 : ?۔ غائب عدد کیا ہے؟"),
     "answer": 60, "checker": "numeric",
     "hint": T("How many minutes are in 1 hour?", "1 گھنٹے میں کتنے منٹ ہوتے ہیں؟"),
     "feedback_correct": T("Yes! 1 hour = 60 minutes, so 40 : 60.", "جی ہاں! 1 گھنٹہ = 60 منٹ، اس لیے 40 : 60"),
     "feedback_wrong": T("1 hour is 60 minutes, so the ratio is 40 : 60.", "1 گھنٹہ 60 منٹ ہے، اس لیے نسبت 40 : 60 ہے۔"),
     "common_wrong": [wrong(1, "That mixes minutes and hours. Change 1 hour to minutes first.", "اس میں منٹ اور گھنٹے ملے ہوئے ہیں۔ پہلے 1 گھنٹے کو منٹوں میں بدلیں۔", "mixed_units")]}},
 ],
 "teacher_notes": [
   "Written fresh for the Ratio and Proportion unit. No textbook text or exercises were used.",
   "Unit number to be confirmed against the PCTB Grade 6 book: the files are named g6-maths-06. Fix the names and curriculum_refs if the unit differs.",
   "Urdu terms to check against the Punjab textbook: نسبت (ratio), تناسب (proportion), اکائی (unit), ترتیب (order). A ratio a : b is read here as \"a اور b\"; some books read it \"a بہ b\".",
   "Typed ratios use the text checker: 5:3, 5 : 3 and \"5 to 3\" are all accepted; the swapped ratio gets its own feedback.",
   "Steps: foundation (s2) links ratio with fractions, then the idea (s3), writing ratios in order (s4, s5), part to whole (s6, s7), find the error (s8), units (s9), explain (s10), new context (s11).",
   "The numbers were worked out in content/sources/g6-maths-06/what_is_a_ratio.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)
