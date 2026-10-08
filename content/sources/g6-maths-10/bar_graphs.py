from common import (T, opt, say, wrong, number_question, tally, table_text, write,
                    REF, REVIEW, DH_TABLES, DH_BAR_GRAPHS)
from figs import bar_graph, squares_bar, tally_figure, attach

SKILL = DH_BAR_GRAPHS

# s2
S2 = 11
assert tally(S2) == "IIII/ IIII/ I"
# s4: books read, bar heights
BOOKS = [(("Ali", "علی"), 7), (("Sara", "سارہ"), 12), (("Omar", "عمر"), 9), (("Hina", "حنا"), 4)]
BOOKS_EN, BOOKS_UR = table_text(BOOKS)
S4 = 12 - 4
assert S4 == 8 and 12 + 4 == 16 and max(v for _, v in BOOKS) == 12
# s5: each square stands for 2 children; the bar is 6 squares tall
S5 = 6 * 2
assert S5 == 12
# s6: each square stands for 5; the bar is 7 squares tall
S6 = 7 * 5
assert S6 == 35 and 7 + 5 == 12
# s7, s8: rupees saved each day
SAVED = [(("Monday", "پیر"), 15), (("Tuesday", "منگل"), 20), (("Wednesday", "بدھ"), 10), (("Thursday", "جمعرات"), 25)]
SAVED_EN, SAVED_UR = table_text(SAVED, " rupees", " روپے")
S7 = sum(v for _, v in SAVED)
assert S7 == 70 and min(SAVED, key=lambda r: r[1])[0][0] == "Wednesday"
# s9: each square stands for 10; the bar is 4 squares tall
assert 4 * 10 == 40
# s11: a bar ends halfway between the 20 and 30 lines
S11 = (20 + 30) // 2
assert S11 == 25
# question bank and review
QB = 5 * 4
assert QB == 20 and 5 + 4 == 9
R1 = 9 * 2
assert R1 == 18
R2 = 25 - 10
assert R2 == 15

lesson = {
 "id": "g6-maths-10-bar-graphs",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Read values, differences and totals from a bar graph, using its scale.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Bar graphs", "بار گراف (ستونی گراف)"),
 "estimated_minutes": 13,
 "prerequisites": [{"skill": DH_TABLES}],
 "misconceptions": [
   {"id": "ignores_scale", "description": "Reads the number of squares as the value, ignoring that each square stands for more than one."},
   {"id": "adds_for_difference", "description": "Adds two bars when the question asks how many more."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_height", "type": "recall", "step": {
     "id": "qb_height", "type": "choice",
     "prompt": T("On a bar graph, what does the height of a bar show?", "بار گراف میں ستون کی اونچائی کیا دکھاتی ہے؟"),
     "options": [
       opt("count", "How many there are of that thing", "اس چیز کی تعداد", True, "Yes! A taller bar means more.", "جی ہاں! اونچا ستون یعنی زیادہ۔"),
       opt("order", "The order things came in", "چیزوں کی ترتیب", False, "The height shows how many, read against the scale.", "اونچائی تعداد دکھاتی ہے، پیمانے کے مطابق۔"),
       opt("width", "How wide the thing is", "چیز کی چوڑائی", False, "All bars are the same width. The height shows how many.", "سب ستون ایک جتنے چوڑے ہیں۔ اونچائی تعداد دکھاتی ہے۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("On a bar graph, each square stands for 4 children. A bar is 5 squares tall. How many children does it show?", "ایک بار گراف میں ہر خانہ 4 بچوں کو ظاہر کرتا ہے۔ ایک ستون 5 خانے اونچا ہے۔ یہ کتنے بچے دکھاتا ہے؟"),
     QB,
     T("5 squares, 4 each.", "5 خانے، ہر ایک 4"),
     T("Right! 20 children.", "درست! 20 بچے"),
     T("5 × 4 = 20.", "5 × 4 = 20"),
     common_wrong=[wrong(5, "Each square is 4 children: 5 × 4 = 20.", "ہر خانہ 4 بچے ہے: 5 × 4 = 20", "ignores_scale"),
                   wrong(9, "Multiply, don't add: 5 × 4 = 20.", "جمع نہیں، ضرب: 5 × 4 = 20")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("On a bar graph each square stands for 10 people. A bar is 4 squares tall. Asma says it shows 4 people. What went wrong?", "ایک بار گراف میں ہر خانہ 10 لوگوں کو ظاہر کرتا ہے۔ ایک ستون 4 خانے اونچا ہے۔ عاصمہ کہتی ہے یہ 4 لوگ دکھاتا ہے۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("scale", "She forgot the scale: 4 × 10 = 40 people.", "وہ پیمانہ بھول گئی: 4 × 10 = 40 لوگ", True,
           "Yes! Always check what one square stands for.", "جی ہاں! ہمیشہ دیکھیں ایک خانہ کتنے کو ظاہر کرتا ہے۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "Each square is 10 people, so 4 squares are 40.", "ہر خانہ 10 لوگ ہے، تو 4 خانے 40 ہیں۔", "ignores_scale"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_bar", "front": T("How do you read a bar graph?", "بار گراف کیسے پڑھتے ہیں؟"),
    "back": T("Look along from the top of the bar to the scale. Check what one square stands for first.", "ستون کے اوپر سے پیمانے تک دیکھیں۔ پہلے دیکھیں ایک خانہ کتنے کو ظاہر کرتا ہے۔")},
   {"id": "f_scale", "front": T("Each square = 5. Bar is 7 squares. Value?", "ہر خانہ = 5۔ ستون 7 خانے۔ قیمت؟"),
    "back": T("7 × 5 = 35.", "7 × 5 = 35")},
 ],
 "home_tasks": [{"id": "h_draw", "text": T(
   "Use your colour survey from the last lesson. Draw a bar graph on squared paper: one bar for each colour, one square for each vote. Which bar is tallest?",
   "پچھلے سبق کا رنگوں والا سروے لیں۔ خانوں والے کاغذ پر بار گراف بنائیں: ہر رنگ کا ایک ستون، ہر ووٹ کا ایک خانہ۔ کون سا ستون سب سے اونچا ہے؟")}],
 "glossary": [T("Bar graph", "بار گراف (ستونی گراف)"), T("Bar", "ستون"), T("Scale", "پیمانہ"), T("Axis", "محور")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "A picture can show data faster than a list. Tall bars, short bars: you see the winner at once!",
                     "تصویر فہرست سے جلدی مواد دکھاتی ہے۔ اونچے ستون، چھوٹے ستون: جیتنے والا فوراً نظر آتا ہے!"),
    "text": T("Today we read bar graphs, like the one in the picture. First, a quick check.", "آج ہم بار گراف پڑھیں گے، جیسے تصویر والا۔ پہلے ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T(f"How many do these tally marks show? {tally(S2)}", f"یہ ٹیلی کے نشان کتنے دکھاتے ہیں؟ {tally(S2)}"),
     S2,
     T("Each gate is 5.", "ہر دروازہ 5 ہے۔"),
     T("Right! 11.", "درست! 11"),
     T("5 + 5 + 1 = 11.", "5 + 5 + 1 = 11"),
     common_wrong=[wrong(9, "Each gate is 5, not 4: 5 + 5 + 1 = 11.", "ہر دروازہ 5 ہے، 4 نہیں: 5 + 5 + 1 = 11")],
     qtype="recall", skill=DH_TABLES),
   {"id": "s3_bars", "type": "explain",
    "character": say("happy", "Always check the scale first: what does one square stand for?", "ہمیشہ پہلے پیمانہ دیکھیں: ایک خانہ کتنے کو ظاہر کرتا ہے؟"),
    "text": T("A bar graph has one bar for each group. The taller the bar, the more there are. The scale up the side tells you the numbers. Sometimes one square stands for more than one, like 2 or 5 or 10: then multiply the number of squares by that amount.",
              "بار گراف میں ہر گروہ کا ایک ستون ہوتا ہے۔ ستون جتنا اونچا، تعداد اتنی زیادہ۔ کنارے کا پیمانہ عدد بتاتا ہے۔ کبھی ایک خانہ ایک سے زیادہ، جیسے 2 یا 5 یا 10، کو ظاہر کرتا ہے: تب خانوں کو اس سے ضرب دیں۔")},
   number_question(
     "s4_more",
     T(f"A bar graph shows books read this month: {BOOKS_EN}. How many more books did Sara read than Hina?", f"ایک بار گراف اس مہینے پڑھی گئی کتابیں دکھاتا ہے: {BOOKS_UR}۔ سارہ نے حنا سے کتنی زیادہ کتابیں پڑھیں؟"),
     S4,
     T("Take the shorter bar from the taller one.", "اونچے ستون میں سے چھوٹا نفی کریں۔"),
     T("Right! 12 − 4 = 8 more.", "درست! 12 − 4 = 8 زیادہ"),
     T("12 − 4 = 8.", "12 − 4 = 8"),
     common_wrong=[wrong(16, "That adds them. 'How many more' is 12 − 4 = 8.", "یہ جمع ہے۔ 'کتنے زیادہ' یعنی 12 − 4 = 8", "adds_for_difference")]),
   number_question(
     "s5_scale2",
     T("On a bar graph of favourite fruits, each square stands for 2 children. The mango bar is 6 squares tall. How many children chose mango?", "پسندیدہ پھلوں کے بار گراف میں ہر خانہ 2 بچوں کو ظاہر کرتا ہے۔ آم کا ستون 6 خانے اونچا ہے۔ کتنے بچوں نے آم چنا؟"),
     S5,
     T("6 squares, 2 children each.", "6 خانے، ہر ایک 2 بچے"),
     T("Right! 12 children.", "درست! 12 بچے"),
     T("6 × 2 = 12.", "6 × 2 = 12"),
     common_wrong=[wrong(6, "Each square is 2 children: 6 × 2 = 12.", "ہر خانہ 2 بچے ہے: 6 × 2 = 12", "ignores_scale")]),
   number_question(
     "s6_scale5",
     T("Each square stands for 5 cars. A bar is 7 squares tall. How many cars does it show?", "ہر خانہ 5 گاڑیوں کو ظاہر کرتا ہے۔ ایک ستون 7 خانے اونچا ہے۔ یہ کتنی گاڑیاں دکھاتا ہے؟"),
     S6,
     T("7 × 5.", "7 × 5"),
     T("Right! 35 cars.", "درست! 35 گاڑیاں"),
     T("7 × 5 = 35.", "7 × 5 = 35"),
     common_wrong=[wrong(7, "Each square is 5 cars: 7 × 5 = 35.", "ہر خانہ 5 گاڑیاں ہے: 7 × 5 = 35", "ignores_scale"),
                   wrong(12, "Multiply, don't add: 7 × 5 = 35.", "جمع نہیں، ضرب: 7 × 5 = 35")]),
   number_question(
     "s7_total",
     T(f"A bar graph shows money Bilal saved: {SAVED_EN}. How much did he save altogether, in rupees?", f"ایک بار گراف بلال کی بچت دکھاتا ہے: {SAVED_UR}۔ اس نے کل کتنے روپے بچائے؟"),
     S7,
     T("Add all four bars.", "چاروں ستون جمع کریں۔"),
     T("Right! Rs 70.", "درست! 70 روپے"),
     T("15 + 20 + 10 + 25 = 70.", "15 + 20 + 10 + 25 = 70"),
     common_wrong=[wrong(25, "25 is the tallest bar. Add them all: 70.", "25 سب سے اونچا ستون ہے۔ سب جمع کریں: 70")]),
   {"id": "s8_least", "type": "choice", "question_type": "apply",
    "prompt": T(f"Same graph: {SAVED_EN}. On which day did he save the least?", f"وہی گراف: {SAVED_UR}۔ کس دن اس نے سب سے کم بچایا؟"),
    "options": [
      opt("wed", "Wednesday", "بدھ", True, "Yes! Wednesday has the shortest bar, Rs 10.", "جی ہاں! بدھ کا ستون سب سے چھوٹا ہے، 10 روپے۔"),
      opt("thu", "Thursday", "جمعرات", False, "Thursday is the tallest bar, the most. Look for the shortest.", "جمعرات سب سے اونچا ستون، یعنی سب سے زیادہ۔ سب سے چھوٹا دیکھیں۔"),
      opt("mon", "Monday", "پیر", False, "Monday is Rs 15. Wednesday is less: Rs 10.", "پیر 15 روپے ہے۔ بدھ کم ہے: 10 روپے۔"),
    ]},
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Each square stands for 10 people. A bar is 4 squares tall. Asma says it shows 4 people. What went wrong?", "ہر خانہ 10 لوگوں کو ظاہر کرتا ہے۔ ایک ستون 4 خانے اونچا ہے۔ عاصمہ کہتی ہے یہ 4 لوگ دکھاتا ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("scale", "She forgot the scale: 4 × 10 = 40 people.", "وہ پیمانہ بھول گئی: 4 × 10 = 40 لوگ", True,
          "Yes! Check what one square stands for.", "جی ہاں! دیکھیں ایک خانہ کتنے کو ظاہر کرتا ہے۔"),
      opt("fourteen", "It should be 4 + 10 = 14 people.", "یہ 4 + 10 = 14 لوگ ہونے چاہییں۔", False,
          "Each square is 10, so multiply: 40.", "ہر خانہ 10 ہے، تو ضرب دیں: 40"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "Each square is 10 people, so 4 squares show 40.", "ہر خانہ 10 لوگ ہے، تو 4 خانے 40 دکھاتے ہیں۔", "ignores_scale"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why should you look at the scale before reading a bar graph? Can you teach me?",
                     "بار گراف پڑھنے سے پہلے پیمانہ کیوں دیکھنا چاہیے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why must you check the scale of a bar graph first?", "اپنے الفاظ میں بتائیں: بار گراف کا پیمانہ پہلے کیوں دیکھنا ضروری ہے؟"),
    "key_idea": "One square might stand for 1, 2, 5, 10 or more. If you just count squares without the scale, you get the wrong number; you must multiply by what each square stands for.",
    "levels": {
      "got_it": "Says one square may stand for more than one, so you multiply by the scale to get the real number.",
      "partly": "Says the scale changes the numbers, without explaining how.",
      "not_yet": "Gives no reason."},
    "keywords": [
      ["square", "each", "خانہ", "ہر"],
      ["more than one", "2", "5", "10", "زیادہ"],
      ["multiply", "times", "ضرب", "zarb"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Each square may stand for many, so multiply by the scale.", "بہت خوب! ہر خانہ کئی کو ظاہر کر سکتا ہے، تو پیمانے سے ضرب دیں۔"),
      "partly": T("Good start! Now say what you do with the scale: add or multiply?", "اچھی شروعات! اب بتائیں پیمانے کے ساتھ کیا کرتے ہیں: جمع یا ضرب؟"),
      "not_yet": T("If one square stands for 10 people, how many do 3 squares show? What if you didn't know about the 10?", "اگر ایک خانہ 10 لوگ ہو تو 3 خانے کتنے دکھاتے ہیں؟ اگر آپ کو 10 کا پتا نہ ہو تو؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_halfway",
     T("A bar ends exactly halfway between the 20 line and the 30 line. What number does it show?", "ایک ستون 20 والی لکیر اور 30 والی لکیر کے بالکل درمیان ختم ہوتا ہے۔ یہ کون سا عدد دکھاتا ہے؟"),
     S11,
     T("Halfway between 20 and 30.", "20 اور 30 کا درمیان"),
     T("Right! 25.", "درست! 25"),
     T("Halfway between 20 and 30 is 25.", "20 اور 30 کا درمیان 25 ہے۔"),
     common_wrong=[wrong(20, "It goes past 20, halfway to 30: 25.", "یہ 20 سے آگے، 30 کے آدھے راستے تک جاتا ہے: 25")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Bar graphs mastered!", "بار گراف آ گئے!"),
    "text": T("Each bar shows how many are in one group. Check the scale first: if one square stands for 2, 5 or 10, multiply the number of squares by it. Take away for 'how many more'; add all the bars for the total.",
              "ہر ستون ایک گروہ کی تعداد دکھاتا ہے۔ پہلے پیمانہ دیکھیں: اگر ایک خانہ 2، 5 یا 10 ہو تو خانوں کو اس سے ضرب دیں۔ 'کتنے زیادہ' کے لیے نفی؛ کل کے لیے سب ستون جمع کریں۔"),
    "points": [T("Check the scale first.", "پہلے پیمانہ دیکھیں۔"),
               T("Taller bar = more.", "اونچا ستون = زیادہ۔")]},
 ],
 "review_questions": [
   {"id": "r_scale", "type": "apply", "skill": SKILL, "step": number_question(
     "r_scale",
     T("Each square stands for 2 goats. A bar is 9 squares tall. How many goats?", "ہر خانہ 2 بکریوں کو ظاہر کرتا ہے۔ ایک ستون 9 خانے اونچا ہے۔ کتنی بکریاں؟"),
     R1,
     T("9 × 2.", "9 × 2"),
     T("Right! 18 goats.", "درست! 18 بکریاں"),
     T("9 × 2 = 18.", "9 × 2 = 18"),
     common_wrong=[wrong(9, "Each square is 2 goats: 18.", "ہر خانہ 2 بکریاں ہے: 18", "ignores_scale")],
     qtype=None)},
   {"id": "r_more", "type": "apply", "skill": SKILL, "step": number_question(
     "r_more",
     T(f"Money saved: {SAVED_EN}. How much more was saved on Thursday than on Wednesday, in rupees?", f"بچت: {SAVED_UR}۔ جمعرات کو بدھ سے کتنے روپے زیادہ بچائے؟"),
     R2,
     T("25 − 10.", "25 − 10"),
     T("Right! Rs 15 more.", "درست! 15 روپے زیادہ"),
     T("25 − 10 = 15.", "25 − 10 = 15"),
     common_wrong=[wrong(35, "That adds them. 'How much more' is 25 − 10 = 15.", "یہ جمع ہے۔ 'کتنا زیادہ' یعنی 25 − 10 = 15", "adds_for_difference")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Data Handling unit. No textbook text or exercises were used.",
   "Each bar graph is drawn as a picture (bars against a scale, or bars made of squares with a key such as one square = 5) and also written in words in the step. Drawing one on squared paper (the home task) makes it concrete.",
   "The scale questions (one square stands for 2, 5 or 10) catch the most common mistake: counting squares as the value.",
   "Urdu terms to check: بار گراف / ستونی گراف (bar graph), ستون (bar), پیمانہ (scale), محور (axis).",
   "The numbers were worked out in content/sources/g6-maths-10/bar_graphs.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
# ---------- pictures ----------
BOOK_CATS = [en[0] for (en, _), _ in BOOKS]                 # A, S, O, H
BOOK_VALS = [v for _, v in BOOKS]
DAY_CATS = ["Mo", "Tu", "We", "Th"]
assert [en[:2] for (en, _), _ in SAVED] == DAY_CATS
SAVED_VALS = [v for _, v in SAVED]


def books_graph():
    return bar_graph(BOOK_VALS, BOOK_CATS,
                     "A bar graph of books read this month, with a scale from 0 to 12 going up in 2s: A (Ali) 7, S (Sara) 12, O (Omar) 9, H (Hina) 4. Sara's bar is the tallest and Hina's the shortest.",
                     "اس مہینے پڑھی گئی کتابوں کا بار گراف، پیمانہ 0 سے 12 تک، 2 کے وقفے سے: A (علی) 7، S (سارہ) 12، O (عمر) 9، H (حنا) 4۔ سارہ کا ستون سب سے اونچا اور حنا کا سب سے چھوٹا ہے۔",
                     top=12, step=2)


def saved_graph():
    return bar_graph(SAVED_VALS, DAY_CATS,
                     "A bar graph of rupees Bilal saved, with a scale from 0 to 25 going up in 5s: Mo (Monday) 15, Tu (Tuesday) 20, We (Wednesday) 10, Th (Thursday) 25.",
                     "بلال کی بچت (روپے) کا بار گراف، پیمانہ 0 سے 25 تک، 5 کے وقفے سے: Mo (پیر) 15، Tu (منگل) 20، We (بدھ) 10، Th (جمعرات) 25۔",
                     top=25, step=5)


def one_bar(n, each, cat, what_en, what_ur):
    return squares_bar(n, each, cat,
                       f"One bar of {what_en} made of {n} squares stacked up. A key beside it shows one square = {each}.",
                       f"{what_ur} کا ایک ستون جو {n} خانوں سے بنا ہے۔ ساتھ کی کلید دکھاتی ہے: ایک خانہ = {each}۔")


attach(lesson, {
    "s1_hook": books_graph(),
    "s2_foundation": tally_figure(S2, "Tally marks: two groups of five, each four upright lines with a fifth line across them, then 1 single line.",
                                  "ٹیلی کے نشان: پانچ کے 2 گروہ، ہر ایک میں چار کھڑی لکیریں اور ان کے اوپر پانچویں ترچھی لکیر، پھر 1 اکیلی لکیر۔"),
    "s3_bars": bar_graph(SAVED_VALS, DAY_CATS,
                         "A bar graph where each bar is made of squares and a key shows one square = 5. The scale goes 0, 5, 10, 15, 20, 25. Mo is 3 squares (15), Tu 4 squares (20), We 2 squares (10), Th 5 squares (25).",
                         "ایک بار گراف جس کا ہر ستون خانوں سے بنا ہے اور کلید دکھاتی ہے: ایک خانہ = 5۔ پیمانہ 0، 5، 10، 15، 20، 25۔ Mo تین خانے (15)، Tu چار خانے (20)، We دو خانے (10)، Th پانچ خانے (25)۔",
                         top=25, step=5, square=5, legend=5),
    "s4_more": books_graph(),
    "s5_scale2": one_bar(6, 2, "M", "mango votes", "آم کے ووٹوں"),
    "s6_scale5": one_bar(7, 5, "C", "cars", "گاڑیوں"),
    "s7_total": saved_graph(),
    "s8_least": saved_graph(),
    "s9_find_error": one_bar(4, 10, "P", "people", "لوگوں"),
    "s11_halfway": bar_graph([S11], None,
                             "A bar graph with a scale from 0 to 40 in 10s and dashed lines across at 20 and 30. One bar ends exactly halfway between the 20 line and the 30 line.",
                             "ایک بار گراف جس کا پیمانہ 0 سے 40 تک، 10 کے وقفے سے، اور 20 اور 30 پر ڈیش والی لکیریں ہیں۔ ایک ستون 20 والی اور 30 والی لکیر کے بالکل درمیان ختم ہوتا ہے۔",
                             top=40, step=10, grid=(20, 30), height=180),
    "qb_height": books_graph(),
    "qb_apply": one_bar(5, 4, "C", "children", "بچوں"),
    "qb_find_error": one_bar(4, 10, "P", "people", "لوگوں"),
    "r_scale": one_bar(9, 2, "G", "goats", "بکریوں"),
    "r_more": saved_graph(),
})
write(lesson)
