from collections import Counter

from common import (T, opt, say, wrong, number_question, table_text, write,
                    REF, REVIEW, DH_TABLES, DH_MEAN, DH_MODE_RANGE)
from figs import Line, bar_graph, figure, label, line, attach, W

SKILL = DH_MODE_RANGE


def mode(*xs):
    counts = Counter(xs).most_common()
    assert len(counts) == 1 or counts[0][1] > counts[1][1], xs  # exactly one mode
    return counts[0][0]


def spread(*xs):
    return max(xs) - min(xs)


# s2
S2_DATA = (3, 5, 7)
assert sum(S2_DATA) // 3 == 5 and sum(S2_DATA) % 3 == 0
# s4
S4_DATA = (3, 5, 5, 7, 2, 5, 3)
S4 = mode(*S4_DATA)
assert S4 == 5 and S4_DATA.count(5) == 3
# s5
S5_DATA = (12, 4, 19, 8)
S5 = spread(*S5_DATA)
assert S5 == 15 and 12 - 4 == 8
# s6: shoe sizes as a table; the mode is the size with the most children
SHOES = [(("Size 3", "سائز 3"), 4), (("Size 4", "سائز 4"), 9), (("Size 5", "سائز 5"), 6)]
SHOES_EN, SHOES_UR = table_text(SHOES, " children", " بچے")
S6 = 4
assert max(SHOES, key=lambda r: r[1])[0][0] == f"Size {S6}"
# s7
S7_DATA = (18, 25, 21, 30, 16)
S7 = spread(*S7_DATA)
assert S7 == 14 and 30 - 18 == 12
# s9: 7, 2, 9, 4 -> 9 - 2, not 9 - 7
assert spread(7, 2, 9, 4) == 7 and 9 - 7 == 2
# s11: smallest 12, range 25 -> largest
S11 = 12 + 25
assert S11 == 37 and 25 - 12 == 13
# question bank and review
QB = spread(15, 3, 22, 9)
assert QB == 19 and 22 - 9 == 13
R1_DATA = (2, 4, 4, 6, 4, 2)
R1 = mode(*R1_DATA)
assert R1 == 4 and R1_DATA.count(4) == 3
R2 = spread(50, 35, 62, 41)
assert R2 == 27 and 62 - 50 == 12


def nums(xs):
    return ", ".join(str(x) for x in xs)


lesson = {
 "id": "g6-maths-10-mode-and-range",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Find the mode (most common value) and the range (largest minus smallest) of a set of data, and say what each tells us.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Mode and range", "عادہ (موڈ) اور وسعت (رینج)"),
 "estimated_minutes": 13,
 "prerequisites": [{"skill": DH_MEAN}, {"skill": DH_TABLES}],
 "misconceptions": [
   {"id": "mode_is_count", "description": "Gives how many times the mode appears instead of the mode itself."},
   {"id": "range_is_largest", "description": "Gives the largest value as the range."},
   {"id": "range_not_smallest", "description": "Takes away the first or another value instead of the smallest."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_mode", "type": "recall", "step": {
     "id": "qb_mode", "type": "choice",
     "prompt": T("What is the mode of a set of data?", "مواد کا عادہ (موڈ) کیا ہوتا ہے؟"),
     "options": [
       opt("most", "The value that appears most often", "وہ قیمت جو سب سے زیادہ بار آئے", True, "Yes! Mode = most often.", "جی ہاں! موڈ = سب سے زیادہ بار۔"),
       opt("biggest", "The biggest value", "سب سے بڑی قیمت", False, "The mode is the most common value, not the biggest.", "موڈ سب سے عام قیمت ہے، سب سے بڑی نہیں۔"),
       opt("spread", "Largest minus smallest", "سب سے بڑی منفی سب سے چھوٹی", False, "That is the range. The mode is the most common value.", "یہ رینج ہے۔ موڈ سب سے عام قیمت ہے۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("Find the range of 15, 3, 22 and 9.", "15، 3، 22 اور 9 کی رینج معلوم کریں۔"),
     QB,
     T("Largest − smallest.", "سب سے بڑا − سب سے چھوٹا"),
     T("Right! 22 − 3 = 19.", "درست! 22 − 3 = 19"),
     T("22 − 3 = 19.", "22 − 3 = 19"),
     common_wrong=[wrong(22, "22 is the largest. Range = 22 − 3 = 19.", "22 سب سے بڑا ہے۔ رینج = 22 − 3 = 19", "range_is_largest"),
                   wrong(13, "Take away the smallest, 3: 22 − 3 = 19.", "سب سے چھوٹا، 3، نفی کریں: 22 − 3 = 19", "range_not_smallest")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T(f"Data: {nums(R1_DATA)}. Imran says the mode is 3, because the most common number appears 3 times. What went wrong?",
                 f"مواد: {nums(R1_DATA)}۔ عمران کہتا ہے موڈ 3 ہے، کیونکہ سب سے عام عدد 3 بار آتا ہے۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("value", "The mode is the number itself, 4, not how many times it appears.", "موڈ خود عدد، 4، ہے، نہ کہ کتنی بار آیا۔", True,
           "Yes! 4 appears 3 times, so the mode is 4.", "جی ہاں! 4 تین بار آتا ہے، تو موڈ 4 ہے۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "3 isn't even in the data! The mode is 4.", "3 تو مواد میں ہے ہی نہیں! موڈ 4 ہے۔", "mode_is_count"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_mode", "front": T("Mode?", "موڈ؟"),
    "back": T("The value that appears most often. In 3, 5, 5, 7 the mode is 5.", "جو قیمت سب سے زیادہ بار آئے۔ 3، 5، 5، 7 میں موڈ 5 ہے۔")},
   {"id": "f_range", "front": T("Range?", "رینج؟"),
    "back": T("Largest − smallest. It shows how spread out the data is.", "سب سے بڑا − سب سے چھوٹا۔ یہ دکھاتی ہے مواد کتنا پھیلا ہوا ہے۔")},
 ],
 "home_tasks": [{"id": "h_shoes", "text": T(
   "Find out the shoe size of everyone at home. Which size is the mode? What is the range, from the smallest foot to the biggest?",
   "گھر میں سب کے جوتے کا سائز معلوم کریں۔ کون سا سائز موڈ ہے؟ سب سے چھوٹے سے سب سے بڑے پاؤں تک رینج کتنی ہے؟")}],
 "glossary": [T("Mode", "عادہ (موڈ)"), T("Range", "وسعت (رینج)"), T("Most often", "سب سے زیادہ بار"), T("Spread", "پھیلاؤ")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "A shopkeeper orders school shoes. Which size should he order most of? And how big is the difference between the smallest and biggest feet?",
                     "دکاندار سکول کے جوتے منگواتا ہے۔ کون سا سائز سب سے زیادہ منگوائے؟ اور سب سے چھوٹے اور بڑے پاؤں میں کتنا فرق ہے؟"),
    "text": T("Today we meet two more ways to describe data: the mode and the range. First, a quick check.", "آج ہم مواد بیان کرنے کے دو اور طریقے سیکھیں گے: موڈ اور رینج۔ پہلے ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T(f"Find the mean of {nums(S2_DATA)}.", f"{nums(S2_DATA)} کی اوسط معلوم کریں۔"),
     5,
     T("Total ÷ 3.", "کل ÷ 3"),
     T("Right! 5.", "درست! 5"),
     T("15 ÷ 3 = 5.", "15 ÷ 3 = 5"),
     common_wrong=[wrong(15, "15 is the total. Divide by 3: 5.", "15 کل ہے۔ 3 سے تقسیم کریں: 5")],
     qtype="recall", skill=DH_MEAN),
   {"id": "s3_mode_range", "type": "explain",
    "character": say("happy", "Mode: most often. Range: biggest minus smallest!", "موڈ: سب سے زیادہ بار۔ رینج: سب سے بڑا منفی سب سے چھوٹا!"),
    "text": T("The mode is the value that appears most often: count how many times each value appears and pick the winner. The range is the largest value minus the smallest: it shows how spread out the data is. Always find the true smallest, not just the first number. In the picture, the data 3, 5, 5, 7: the tallest stack is at 5, so the mode is 5, and the range is 7 − 3 = 4.",
              "موڈ وہ قیمت ہے جو سب سے زیادہ بار آئے: ہر قیمت کتنی بار آئی گنیں اور جیتنے والی چنیں۔ رینج سب سے بڑی قیمت منفی سب سے چھوٹی ہے: یہ دکھاتی ہے مواد کتنا پھیلا ہوا ہے۔ ہمیشہ اصل سب سے چھوٹا عدد ڈھونڈیں، صرف پہلا نہیں۔ تصویر میں مواد 3، 5، 5، 7 ہے: سب سے اونچا ڈھیر 5 پر ہے، تو موڈ 5 ہے، اور رینج 7 − 3 = 4 ہے۔")},
   number_question(
     "s4_mode",
     T(f"Find the mode of {nums(S4_DATA)}.", f"{nums(S4_DATA)} کا موڈ معلوم کریں۔"),
     S4,
     T("Which number appears most often?", "کون سا عدد سب سے زیادہ بار آتا ہے؟"),
     T("Right! 5 appears 3 times.", "درست! 5 تین بار آتا ہے۔"),
     T("5 appears 3 times, more than any other: the mode is 5.", "5 تین بار آتا ہے، سب سے زیادہ: موڈ 5 ہے۔"),
     common_wrong=[wrong(3, "3 is how many times 5 appears. The mode is the number itself: 5.", "3 یہ ہے کہ 5 کتنی بار آیا۔ موڈ خود عدد ہے: 5", "mode_is_count"),
                   wrong(7, "7 is the largest, but it appears only once. The mode is 5.", "7 سب سے بڑا ہے، لیکن صرف ایک بار آتا ہے۔ موڈ 5 ہے۔")]),
   number_question(
     "s5_range",
     T(f"Find the range of {nums(S5_DATA)}.", f"{nums(S5_DATA)} کی رینج معلوم کریں۔"),
     S5,
     T("Largest is 19, smallest is 4.", "سب سے بڑا 19، سب سے چھوٹا 4"),
     T("Right! 19 − 4 = 15.", "درست! 19 − 4 = 15"),
     T("19 − 4 = 15.", "19 − 4 = 15"),
     common_wrong=[wrong(19, "19 is the largest. Range = 19 − 4 = 15.", "19 سب سے بڑا ہے۔ رینج = 19 − 4 = 15", "range_is_largest"),
                   wrong(8, "Use the largest and smallest, not the first two: 19 − 4 = 15.", "سب سے بڑا اور سب سے چھوٹا لیں، پہلے دو نہیں: 19 − 4 = 15", "range_not_smallest")]),
   number_question(
     "s6_shoes",
     T(f"Shoe sizes in a class: {SHOES_EN}. Which shoe size is the mode?", f"ایک جماعت کے جوتوں کے سائز: {SHOES_UR}۔ کون سا سائز موڈ ہے؟"),
     S6,
     T("Which size has the most children?", "کس سائز کے سب سے زیادہ بچے ہیں؟"),
     T("Right! Size 4, with 9 children.", "درست! سائز 4، 9 بچوں کے ساتھ۔"),
     T("Size 4 has the most children (9), so the mode is size 4.", "سائز 4 کے سب سے زیادہ بچے (9) ہیں، تو موڈ سائز 4 ہے۔"),
     common_wrong=[wrong(9, "9 is how many children. The mode is the size: 4.", "9 بچوں کی تعداد ہے۔ موڈ سائز ہے: 4", "mode_is_count")]),
   number_question(
     "s7_temps",
     T(f"Temperatures this week (°C): {nums(S7_DATA)}. What is the range?", f"اس ہفتے کا درجہ حرارت (°C): {nums(S7_DATA)}۔ رینج کتنی ہے؟"),
     S7,
     T("Hottest minus coldest.", "سب سے گرم منفی سب سے ٹھنڈا"),
     T("Right! 30 − 16 = 14 degrees.", "درست! 30 − 16 = 14 درجے"),
     T("30 − 16 = 14.", "30 − 16 = 14"),
     common_wrong=[wrong(12, "The smallest is 16, not 18: 30 − 16 = 14.", "سب سے چھوٹا 16 ہے، 18 نہیں: 30 − 16 = 14", "range_not_smallest"),
                   wrong(30, "30 is the hottest. Range = 30 − 16 = 14.", "30 سب سے گرم ہے۔ رینج = 30 − 16 = 14", "range_is_largest")]),
   {"id": "s8_which", "type": "choice", "question_type": "apply",
    "prompt": T("A shopkeeper wants to know which uniform size to order the most of. Which should he find?", "دکاندار جاننا چاہتا ہے کون سا یونیفارم سائز سب سے زیادہ منگوائے۔ اسے کیا معلوم کرنا چاہیے؟"),
    "options": [
      opt("mode", "The mode", "موڈ", True, "Yes! The mode is the size most children wear.", "جی ہاں! موڈ وہ سائز ہے جو سب سے زیادہ بچے پہنتے ہیں۔"),
      opt("range", "The range", "رینج", False, "The range shows the spread, not the most common size.", "رینج پھیلاؤ دکھاتی ہے، سب سے عام سائز نہیں۔"),
      opt("mean", "The mean", "اوسط", False, "The mean might not be a real size. The mode is the most common size.", "اوسط شاید اصل سائز نہ ہو۔ موڈ سب سے عام سائز ہے۔"),
    ]},
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("To find the range of 7, 2, 9, 4, Sana works out 9 − 7 = 2. What went wrong?", "7، 2، 9، 4 کی رینج کے لیے ثنا 9 − 7 = 2 نکالتی ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("smallest", "She took away the first number, not the smallest. 9 − 2 = 7.", "اس نے پہلا عدد نفی کیا، سب سے چھوٹا نہیں۔ 9 − 2 = 7", True,
          "Yes! Find the true smallest, 2.", "جی ہاں! اصل سب سے چھوٹا، 2، ڈھونڈیں۔"),
      opt("add", "She should add: 9 + 2 = 11.", "اسے جمع کرنا چاہیے: 9 + 2 = 11", False,
          "Range is a take-away: largest − smallest = 7.", "رینج نفی ہے: سب سے بڑا − سب سے چھوٹا = 7"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "7 isn't the smallest; 2 is. Range = 9 − 2 = 7.", "7 سب سے چھوٹا نہیں؛ 2 ہے۔ رینج = 9 − 2 = 7", "range_not_smallest"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Two classes both have a mean mark of 7. Why might the range still be useful? Can you teach me?",
                     "دو جماعتوں کے نمبروں کی اوسط 7 ہے۔ پھر بھی رینج کیوں کام کی ہو سکتی ہے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: what does the range tell us that the mean doesn't?", "اپنے الفاظ میں بتائیں: رینج ہمیں کیا بتاتی ہے جو اوسط نہیں بتاتی؟"),
    "key_idea": "The range shows how spread out the data is. Two sets can have the same mean, but in one the values are close together (small range) and in the other they are far apart (big range).",
    "levels": {
      "got_it": "Says the range shows how spread out or different the values are, which the mean does not show.",
      "partly": "Says range is largest minus smallest without saying what it tells us.",
      "not_yet": "Gives no reason, or mixes it up with the mode."},
    "keywords": [
      ["spread", "different", "apart", "پھیل", "فرق"],
      ["largest", "smallest", "biggest", "بڑا", "چھوٹا"],
      ["close", "same", "together", "قریب", "ایک جیسے"]],
    "fallback_feedback": {
      "got_it": T("Well explained! The range shows how spread out the values are.", "بہت خوب! رینج دکھاتی ہے قیمتیں کتنی پھیلی ہوئی ہیں۔"),
      "partly": T("Good start! Now say what a big range or a small range tells you.", "اچھی شروعات! اب بتائیں بڑی یا چھوٹی رینج کیا بتاتی ہے۔"),
      "not_yet": T("Think of marks 6, 7, 8 and marks 1, 7, 13. Same mean, 7. What is different about them?", "نمبر 6، 7، 8 اور نمبر 1، 7، 13 سوچیں۔ اوسط ایک، 7۔ ان میں کیا فرق ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_largest",
     T("The smallest value in some data is 12 and the range is 25. What is the largest value?", "کچھ مواد میں سب سے چھوٹی قیمت 12 اور رینج 25 ہے۔ سب سے بڑی قیمت کیا ہے؟"),
     S11,
     T("Largest − 12 = 25.", "سب سے بڑا − 12 = 25"),
     T("Right! 37. Check: 37 − 12 = 25.", "درست! 37۔ جانچ: 37 − 12 = 25"),
     T("12 + 25 = 37.", "12 + 25 = 37"),
     common_wrong=[wrong(13, "Add the range to the smallest: 12 + 25 = 37.", "رینج کو سب سے چھوٹے میں جمع کریں: 12 + 25 = 37")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Mode and range done!", "موڈ اور رینج مکمل!"),
    "text": T("The mode is the value that appears most often (the value, not the count). The range is largest − smallest, and shows how spread out the data is. Find the true smallest and largest, not just the first and last numbers.",
              "موڈ وہ قیمت ہے جو سب سے زیادہ بار آئے (قیمت، گنتی نہیں)۔ رینج سب سے بڑا − سب سے چھوٹا ہے، اور دکھاتی ہے مواد کتنا پھیلا ہے۔ اصل سب سے چھوٹا اور بڑا ڈھونڈیں، صرف پہلا اور آخری عدد نہیں۔"),
    "points": [T("Mode = most often.", "موڈ = سب سے زیادہ بار۔"),
               T("Range = largest − smallest.", "رینج = سب سے بڑا − سب سے چھوٹا۔")]},
 ],
 "review_questions": [
   {"id": "r_mode", "type": "apply", "skill": SKILL, "step": number_question(
     "r_mode",
     T(f"Find the mode of {nums(R1_DATA)}.", f"{nums(R1_DATA)} کا موڈ معلوم کریں۔"),
     R1,
     T("Most often.", "سب سے زیادہ بار"),
     T("Right! 4.", "درست! 4"),
     T("4 appears 3 times: the mode is 4.", "4 تین بار آتا ہے: موڈ 4 ہے۔"),
     common_wrong=[wrong(3, "3 is the count. The mode is 4.", "3 گنتی ہے۔ موڈ 4 ہے۔", "mode_is_count")],
     qtype=None)},
   {"id": "r_range", "type": "apply", "skill": SKILL, "step": number_question(
     "r_range",
     T("Find the range of 50, 35, 62 and 41.", "50، 35، 62 اور 41 کی رینج معلوم کریں۔"),
     R2,
     T("Largest − smallest.", "سب سے بڑا − سب سے چھوٹا"),
     T("Right! 62 − 35 = 27.", "درست! 62 − 35 = 27"),
     T("62 − 35 = 27.", "62 − 35 = 27"),
     common_wrong=[wrong(12, "The smallest is 35, not 50: 62 − 35 = 27.", "سب سے چھوٹا 35 ہے، 50 نہیں: 62 − 35 = 27", "range_not_smallest")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Data Handling unit. No textbook text or exercises were used.",
   "Every data set has exactly one mode (checked in the script). Lists are deliberately not in order, so children must find the true smallest and largest for the range.",
   "Urdu terms to check: عادہ / موڈ (mode), وسعت / رینج (range). Many teachers use the English words; please confirm the PCTB terms.",
   "The numbers were worked out in content/sources/g6-maths-10/mode_range.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
# ---------- pictures ----------
EXAMPLE = (3, 5, 5, 7)
assert mode(*EXAMPLE) == 5 and spread(*EXAMPLE) == 4


def nums_ur(xs):
    return "، ".join(str(x) for x in xs)


def example_plot():
    """A dot plot of 3, 5, 5, 7 with the range measured above it."""
    nl = Line(2, 8, 92)
    nl.ticks(range(2, 9))
    nl.stacks(EXAMPLE)
    lo, hi = min(EXAMPLE), max(EXAMPLE)
    y = 34
    nl.items += [line((nl.x(lo), y), (nl.x(hi), y), dashed=True),
                 line((nl.x(lo), y - 5), (nl.x(lo), y + 5)), line((nl.x(hi), y - 5), (nl.x(hi), y + 5)),
                 label(((nl.x(lo) + nl.x(hi)) / 2, y - 14), f"{hi}-{lo}={hi - lo}")]
    return figure(W, 124,
        "A number line from 2 to 8 with a dot for each value of 3, 5, 5, 7: one dot above 3, a stack of two dots above 5 and one dot above 7. Above them a dashed line runs from 3 to 7, marked 7-3=4.",
        "2 سے 8 تک عددی لکیر، 3، 5، 5، 7 کی ہر قیمت کا ایک نقطہ: 3 کے اوپر ایک نقطہ، 5 کے اوپر دو نقطوں کا ڈھیر اور 7 کے اوپر ایک نقطہ۔ ان کے اوپر 3 سے 7 تک ڈیش والی لکیر ہے، جس پر 7-3=4 لکھا ہے۔",
        nl.items)


def spread_line(data, lo, hi, tick=1):
    """The values as dots on a number line, each with its number above."""
    nl = Line(lo, hi, 0)
    rows = nl.dots(data, texts=True)
    y = 30 + rows * 17
    nl = Line(lo, hi, y)
    nl.ticks(range(lo, hi + 1, tick), labelled=[v for v in (lo, hi) if v not in data])
    nl.dots(data)
    return figure(W, y + 32,
        f"A number line from {lo} to {hi}, with a tick at every whole number, and a dot at each value: {', '.join(map(str, data))}. Each dot has its number above it.",
        f"{lo} سے {hi} تک عددی لکیر، ہر مکمل عدد پر نشان، اور ہر قیمت پر ایک نقطہ: {nums_ur(data)}۔ ہر نقطے کے اوپر اس کا عدد لکھا ہے۔",
        nl.items)


def largest_from_range():
    nl = Line(0, 40, 64)
    nl.ticks([v for v in range(0, 41, 5) if abs(v - S11) > 2], labelled=(0,))
    a, b = 12, S11
    nl.items += [line((nl.x(a), nl.y - 6), (nl.x(a), nl.y + 6)), label((nl.x(a), nl.y + 18), a),
                 line((nl.x(b), nl.y - 6), (nl.x(b), nl.y + 6)), label((nl.x(b), nl.y + 18), "?")]
    nl.items.append({"kind": "circle", "center": [round(nl.x(a), 1), nl.y], "radius": 5, "fill": True})
    y = nl.y - 24
    nl.items += [line((nl.x(a), y), (nl.x(b), y), dashed=True),
                 line((nl.x(a), y - 5), (nl.x(a), y + 5)), line((nl.x(b), y - 5), (nl.x(b), y + 5)),
                 label(((nl.x(a) + nl.x(b)) / 2, y - 13), 25)]
    return figure(W, 96,
        "A number line from 0. A dot marks the smallest value, 12. A dashed line marked 25 (the range) runs from 12 to a point marked with a question mark, the largest value.",
        "0 سے شروع ہونے والی عددی لکیر۔ ایک نقطہ سب سے چھوٹی قیمت، 12، دکھاتا ہے۔ 25 (رینج) والی ڈیش لکیر 12 سے سوالیہ نشان والے نقطے تک جاتی ہے، جو سب سے بڑی قیمت ہے۔",
        nl.items)


def mode_plot(data, lo, hi):
    nl = Line(lo, hi, 18 + 13 * max(data.count(v) for v in data) + 8)
    nl.ticks(range(lo, hi + 1))
    nl.stacks(data)
    counts = ", ".join(f"{data.count(v)} above {v}" for v in sorted(set(data)))
    counts_ur = "، ".join(f"{v} کے اوپر {data.count(v)}" for v in sorted(set(data)))
    return figure(W, nl.y + 32,
        f"A dot plot on a number line from {lo} to {hi}, one dot for each value of {', '.join(map(str, data))}: {counts}.",
        f"{lo} سے {hi} تک عددی لکیر پر نقطوں کا خاکہ، {nums_ur(data)} کی ہر قیمت کا ایک نقطہ: {counts_ur}۔",
        nl.items)


SHOE_SIZES = [en.split()[1] for (en, _), _ in SHOES]
attach(lesson, {
    "s3_mode_range": example_plot(),
    "s5_range": spread_line(S5_DATA, 0, 20),
    "s6_shoes": bar_graph([v for _, v in SHOES], SHOE_SIZES,
        "A bar graph of shoe sizes, with a scale from 0 to 10 going up in 2s: size 3 has 4 children, size 4 has 9 and size 5 has 6. The sizes are written under the bars.",
        "جوتوں کے سائز کا بار گراف، پیمانہ 0 سے 10 تک، 2 کے وقفے سے: سائز 3 کے 4 بچے، سائز 4 کے 9 اور سائز 5 کے 6۔ سائز ستونوں کے نیچے لکھے ہیں۔",
        top=10, step=2),
    "s7_temps": spread_line(S7_DATA, 15, 30),
    "s9_find_error": spread_line((7, 2, 9, 4), 0, 10),
    "s11_largest": largest_from_range(),
    "qb_apply": spread_line((15, 3, 22, 9), 0, 25),
    "qb_find_error": mode_plot(R1_DATA, 1, 7),
    "r_range": spread_line((50, 35, 62, 41), 30, 65),
})
write(lesson)
