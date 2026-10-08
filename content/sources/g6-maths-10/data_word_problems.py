from collections import Counter

from common import (T, opt, say, wrong, number_question, tally, table_text, write,
                    REF, REVIEW, DH_TABLES, DH_BAR_GRAPHS, DH_MEAN, DH_MODE_RANGE, DH_WORD_PROBLEMS)
from figs import bar_graph, squares_bar, tally_figure, height_bars, attach

SKILL = DH_WORD_PROBLEMS


def mean(*xs):
    assert sum(xs) % len(xs) == 0, xs
    return sum(xs) // len(xs)


def mode(*xs):
    counts = Counter(xs).most_common()
    assert len(counts) == 1 or counts[0][1] > counts[1][1], xs
    return counts[0][0]


def nums(xs):
    return ", ".join(str(x) for x in xs)


# s2
S2 = mean(8, 12, 10)
assert S2 == 10 and 8 + 12 + 10 == 30
# s4, s5: samosas sold each day
SAMOSAS = [(("Monday", "پیر"), 40), (("Tuesday", "منگل"), 35), (("Wednesday", "بدھ"), 50), (("Thursday", "جمعرات"), 45), (("Friday", "جمعہ"), 30)]
SAMOSAS_EN, SAMOSAS_UR = table_text(SAMOSAS)
SOLD = [v for _, v in SAMOSAS]
S4 = mean(*SOLD)
assert S4 == 40 and sum(SOLD) == 200
S5 = max(SOLD) - min(SOLD)
assert S5 == 20
# s6: each square stands for 10 kg; the bar is 7 squares tall
S6 = 7 * 10
assert S6 == 70
# s7: mean of 5 matches is 30
S7 = 30 * 5
assert S7 == 150
# s8: savings, mean 50 over 4 weeks
S8 = 50 * 4 - (40 + 60 + 45)
assert S8 == 55 and mean(40, 60, 45, S8) == 50
# s9: 10, 0, 20 -> divide by 3, zero counts
assert mean(10, 0, 20) == 10 and 30 // 2 == 15
# u1 to u5
U1 = 19
assert tally(U1) == "IIII/ IIII/ IIII/ IIII"
U2 = 8 * 5
assert U2 == 40
U3_DATA = (9, 11, 13, 7)
U3 = mean(*U3_DATA)
assert U3 == 10 and sum(U3_DATA) == 40
U4_DATA = (2, 3, 3, 8, 3, 1)
U4 = mode(*U4_DATA)
assert U4 == 3 and U4_DATA.count(3) == 3
U5_DATA = (120, 135, 128, 142)
U5 = max(U5_DATA) - min(U5_DATA)
assert U5 == 22 and 142 - 128 == 14
# question bank and review
QB = mean(250, 300, 350)
assert QB == 300 and 250 + 300 + 350 == 900
R1 = 6 * 20
assert R1 == 120
R2_DATA = (14, 9, 21, 9, 17)
R2 = max(R2_DATA) - min(R2_DATA)
assert R2 == 12 and mode(*R2_DATA) == 9

lesson = {
 "id": "g6-maths-10-data-word-problems",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Solve real-life problems with tables, bar graphs, mean, mode and range, choosing the right measure.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Data word problems", "مواد کے عبارتی سوال"),
 "estimated_minutes": 16,
 "prerequisites": [{"skill": DH_MEAN}, {"skill": DH_MODE_RANGE}, {"skill": DH_BAR_GRAPHS}, {"skill": DH_TABLES}],
 "misconceptions": [
   {"id": "forgets_divide", "description": "Gives the total instead of the mean."},
   {"id": "skips_zero", "description": "Leaves out a zero value when counting how many numbers there are."},
   {"id": "ignores_scale", "description": "Reads the number of squares on a bar graph as the value."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_which", "type": "recall", "step": {
     "id": "qb_which", "type": "choice",
     "prompt": T("You want to know how spread out the heights in your class are. Which should you find?", "آپ جاننا چاہتے ہیں کہ جماعت کی لمبائیاں کتنی پھیلی ہوئی ہیں۔ کیا معلوم کریں؟"),
     "options": [
       opt("range", "The range", "رینج", True, "Yes! The range shows the spread: tallest − shortest.", "جی ہاں! رینج پھیلاؤ دکھاتی ہے: سب سے لمبا − سب سے چھوٹا۔"),
       opt("mode", "The mode", "موڈ", False, "The mode is the most common height, not the spread.", "موڈ سب سے عام لمبائی ہے، پھیلاؤ نہیں۔"),
       opt("total", "The total", "کل", False, "Adding the heights doesn't show the spread. Use the range.", "لمبائیاں جمع کرنے سے پھیلاؤ نہیں دکھتا۔ رینج لیں۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("A family's electricity bills for three months were Rs 250, Rs 300 and Rs 350. What was the mean bill, in rupees?", "ایک خاندان کے تین مہینوں کے بجلی کے بل 250، 300 اور 350 روپے تھے۔ اوسط بل کتنے روپے تھا؟"),
     QB,
     T("Total ÷ 3.", "کل ÷ 3"),
     T("Right! Rs 300.", "درست! 300 روپے"),
     T("900 ÷ 3 = 300.", "900 ÷ 3 = 300"),
     common_wrong=[wrong(900, "900 is the total. Divide by 3: 300.", "900 کل ہے۔ 3 سے تقسیم کریں: 300", "forgets_divide")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Each square on a bar graph stands for 20 people. A bar is 6 squares tall. Kashif says 26 people. What went wrong?", "بار گراف کا ہر خانہ 20 لوگوں کو ظاہر کرتا ہے۔ ایک ستون 6 خانے اونچا ہے۔ کاشف کہتا ہے 26 لوگ۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("multiply", "He added. Multiply: 6 × 20 = 120 people.", "اس نے جمع کیا۔ ضرب دیں: 6 × 20 = 120 لوگ", True,
           "Yes! Each of the 6 squares is 20 people.", "جی ہاں! 6 خانوں میں سے ہر ایک 20 لوگ ہے۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "6 squares of 20 each is 6 × 20 = 120.", "20 والے 6 خانے یعنی 6 × 20 = 120", "ignores_scale"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_choose", "front": T("Which measure?", "کون سا پیمانہ؟"),
    "back": T("Fair share: mean. Most common: mode. How spread out: range. Altogether: total.", "برابر حصہ: اوسط۔ سب سے عام: موڈ۔ کتنا پھیلا: رینج۔ سب مل کر: کل۔")},
   {"id": "f_zero", "front": T("Does a zero count in the mean?", "کیا صفر اوسط میں گنا جاتا ہے؟"),
    "back": T("Yes! Mean of 10, 0, 20 is 30 ÷ 3 = 10.", "جی ہاں! 10، 0، 20 کی اوسط 30 ÷ 3 = 10")},
 ],
 "home_tasks": [{"id": "h_week", "text": T(
   "For one week, write down how many glasses of water you drink each day. At the end, find the total, the mean, the mode and the range.",
   "ایک ہفتہ روزانہ لکھیں آپ کتنے گلاس پانی پیتے ہیں۔ آخر میں کل، اوسط، موڈ اور رینج نکالیں۔")}],
 "glossary": [T("Mean", "اوسط"), T("Mode", "موڈ"), T("Range", "رینج"), T("Total", "کل")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Shopkeepers, cricketers and farmers all use data! Let's solve their real problems.",
                     "دکاندار، کرکٹر اور کسان سب مواد استعمال کرتے ہیں! آئیں ان کے اصل سوال حل کریں۔"),
    "text": T("Today we use everything from the Data handling unit on real-life problems, then a short unit test. First, a quick check.",
              "آج ہم مواد کے پورے باب کو اصل زندگی کے سوالوں پر لگائیں گے، پھر ایک چھوٹا ٹیسٹ۔ پہلے ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("Find the mean of 8, 12 and 10.", "8، 12 اور 10 کی اوسط معلوم کریں۔"),
     S2,
     T("Total ÷ 3.", "کل ÷ 3"),
     T("Right! 10.", "درست! 10"),
     T("30 ÷ 3 = 10.", "30 ÷ 3 = 10"),
     common_wrong=[wrong(30, "30 is the total. Divide by 3: 10.", "30 کل ہے۔ 3 سے تقسیم کریں: 10", "forgets_divide")],
     qtype="recall", skill=DH_MEAN),
   {"id": "s3_plan", "type": "explain",
    "character": say("thinking", "First ask: does the question want a total, a difference, a fair share, the most common, or the spread?",
                     "پہلے پوچھیں: سوال کل چاہتا ہے، فرق، برابر حصہ، سب سے عام، یا پھیلاؤ؟"),
    "text": T("Altogether: add (total). How many more: take away. Fair share or average: mean = total ÷ how many. Most common: mode. How spread out: range = largest − smallest. On a bar graph, check the scale first.",
              "سب مل کر: جمع (کل)۔ کتنے زیادہ: نفی۔ برابر حصہ یا اوسط: اوسط = کل ÷ تعداد۔ سب سے عام: موڈ۔ کتنا پھیلا: رینج = سب سے بڑا − سب سے چھوٹا۔ بار گراف میں پہلے پیمانہ دیکھیں۔")},
   number_question(
     "s4_samosas",
     T(f"A shop sold these samosas: {SAMOSAS_EN}. What is the mean number sold per day?", f"ایک دکان نے یہ سموسے بیچے: {SAMOSAS_UR}۔ روزانہ اوسطاً کتنے بکے؟"),
     S4,
     T("Total of 5 days ÷ 5.", "5 دنوں کا کل ÷ 5"),
     T("Right! 40 a day.", "درست! روزانہ 40"),
     T("40 + 35 + 50 + 45 + 30 = 200, and 200 ÷ 5 = 40.", "40 + 35 + 50 + 45 + 30 = 200، اور 200 ÷ 5 = 40"),
     common_wrong=[wrong(200, "200 is the total. Divide by 5 days: 40.", "200 کل ہے۔ 5 دنوں سے تقسیم کریں: 40", "forgets_divide")]),
   number_question(
     "s5_range",
     T(f"Same shop: {SAMOSAS_EN}. What is the range of samosas sold?", f"وہی دکان: {SAMOSAS_UR}۔ بکنے والے سموسوں کی رینج کتنی ہے؟"),
     S5,
     T("Best day − worst day.", "سب سے اچھا دن − سب سے کمزور دن"),
     T("Right! 50 − 30 = 20.", "درست! 50 − 30 = 20"),
     T("50 − 30 = 20.", "50 − 30 = 20"),
     common_wrong=[wrong(50, "50 is the best day. Range = 50 − 30 = 20.", "50 سب سے اچھا دن ہے۔ رینج = 50 − 30 = 20"),
                   wrong(10, "The smallest is 30, not 40: 50 − 30 = 20.", "سب سے چھوٹا 30 ہے، 40 نہیں: 50 − 30 = 20")]),
   number_question(
     "s6_wheat",
     T("A farmer's bar graph shows wheat harvested. Each square stands for 10 kg. This year's bar is 7 squares tall. How many kg of wheat?", "ایک کسان کا بار گراف کٹی ہوئی گندم دکھاتا ہے۔ ہر خانہ 10 کلو ہے۔ اس سال کا ستون 7 خانے اونچا ہے۔ کتنے کلو گندم؟"),
     S6,
     T("7 squares, 10 kg each.", "7 خانے، ہر ایک 10 کلو"),
     T("Right! 70 kg.", "درست! 70 کلو"),
     T("7 × 10 = 70 kg.", "7 × 10 = 70"),
     common_wrong=[wrong(7, "Each square is 10 kg: 7 × 10 = 70.", "ہر خانہ 10 کلو ہے: 7 × 10 = 70", "ignores_scale")]),
   number_question(
     "s7_runs",
     T("A batsman's mean score over 5 matches is 30 runs. How many runs did he score altogether?", "ایک بلے باز کی 5 میچوں میں اوسط 30 رنز ہے۔ اس نے کل کتنے رنز بنائے؟"),
     S7,
     T("Total = mean × how many.", "کل = اوسط × تعداد"),
     T("Right! 150 runs.", "درست! 150 رنز"),
     T("30 × 5 = 150.", "30 × 5 = 150"),
     common_wrong=[wrong(6, "That divides. Total = 30 × 5 = 150.", "یہ تقسیم ہے۔ کل = 30 × 5 = 150"),
                   wrong(35, "Multiply, don't add: 30 × 5 = 150.", "جمع نہیں، ضرب: 30 × 5 = 150")]),
   number_question(
     "s8_savings",
     T("Sana saved a mean of Rs 50 a week for 4 weeks. In the first three weeks she saved Rs 40, Rs 60 and Rs 45. How much did she save in week 4?", "ثنا نے 4 ہفتوں میں اوسطاً 50 روپے ہفتہ بچائے۔ پہلے تین ہفتوں میں 40، 60 اور 45 روپے بچائے۔ چوتھے ہفتے کتنے بچائے؟"),
     S8,
     T("The total must be 50 × 4 = 200.", "کل 50 × 4 = 200 ہونا چاہیے۔"),
     T("Right! Rs 55.", "درست! 55 روپے"),
     T("200 − (40 + 60 + 45) = 200 − 145 = 55.", "200 − (40 + 60 + 45) = 200 − 145 = 55"),
     common_wrong=[wrong(50, "50 is the mean, but week 4 must make the total 200: Rs 55.", "50 اوسط ہے، لیکن چوتھا ہفتہ کل کو 200 بنائے: 55 روپے")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Over three days a shop sold 10, 0 and 20 cakes. Rehan says the mean is 30 ÷ 2 = 15, because the 0 doesn't count. What went wrong?",
                "تین دنوں میں ایک دکان نے 10، 0 اور 20 کیک بیچے۔ ریحان کہتا ہے اوسط 30 ÷ 2 = 15 ہے، کیونکہ 0 نہیں گنا جاتا۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("zero", "The 0 is a real day and counts. 30 ÷ 3 = 10.", "0 بھی ایک اصل دن ہے اور گنا جاتا ہے۔ 30 ÷ 3 = 10", True,
          "Yes! There were 3 days, so divide by 3.", "جی ہاں! 3 دن تھے، تو 3 سے تقسیم کریں۔"),
      opt("total", "The total should be 31.", "کل 31 ہونا چاہیے۔", False,
          "10 + 0 + 20 = 30 is right. Divide by 3 days: 10.", "10 + 0 + 20 = 30 درست ہے۔ 3 دنوں سے تقسیم کریں: 10"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "A day with 0 sales is still a day. 30 ÷ 3 = 10.", "صفر بکری والا دن بھی دن ہے۔ 30 ÷ 3 = 10", "skips_zero"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "A shoe shop wants to know which size to stock most. Should it use the mean or the mode? Why? Can you teach me?",
                     "جوتوں کی دکان جاننا چاہتی ہے کون سا سائز سب سے زیادہ رکھے۔ اوسط لے یا موڈ؟ کیوں؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why is the mode better than the mean for choosing which shoe size to stock most?",
              "اپنے الفاظ میں بتائیں: سب سے زیادہ کون سا سائز رکھنا ہے، اس کے لیے موڈ اوسط سے بہتر کیوں ہے؟"),
    "key_idea": "The mode is the size most people actually wear, so it sells the most. The mean might not be a real size (like 4.6), and fewer people may wear it.",
    "levels": {
      "got_it": "Says the mode is the size most people wear (most common), while the mean may not be a real or popular size.",
      "partly": "Says the mode is the most common without comparing with the mean, or the reverse.",
      "not_yet": "Chooses the mean, or gives no reason."},
    "keywords": [
      ["mode", "most", "common", "موڈ", "سب سے زیادہ", "عام"],
      ["mean", "average", "اوسط"],
      ["real", "size", "wear", "buy", "سائز", "پہن", "خرید"]],
    "fallback_feedback": {
      "got_it": T("Well explained! The mode is the size most people wear; the mean might not even be a real size.", "بہت خوب! موڈ وہ سائز ہے جو سب سے زیادہ لوگ پہنتے ہیں؛ اوسط شاید اصل سائز بھی نہ ہو۔"),
      "partly": T("Good start! Now say why the mean might not help the shop.", "اچھی شروعات! اب بتائیں اوسط دکان کے کام کیوں نہ آئے۔"),
      "not_yet": T("If the mean shoe size is 4.6, can the shop sell size 4.6? Which size do the most customers wear?", "اگر اوسط سائز 4.6 ہو تو کیا دکان 4.6 سائز بیچ سکتی ہے؟ سب سے زیادہ گاہک کون سا سائز پہنتے ہیں؟")},
    "limit_per_day": 3, "max_attempts": 2},
   {"id": "s11_unit_test", "type": "explain",
    "character": say("encouraging", "Test time! Five questions from the whole Data handling unit. You can do it!",
                     "ٹیسٹ کا وقت! مواد کے پورے باب سے پانچ سوال۔ آپ کر سکتے ہیں!"),
    "text": T("This short test has questions on tally marks, bar graphs, mean, mode and a real-life problem. Take your time.",
              "اس چھوٹے ٹیسٹ میں ٹیلی، بار گراف، اوسط، موڈ اور ایک اصل زندگی کا سوال ہے۔ آرام سے کریں۔")},
   number_question(
     "u1_tally",
     T(f"Test 1: How many do these tally marks show? {tally(U1)}", f"ٹیسٹ 1: یہ ٹیلی کے نشان کتنے دکھاتے ہیں؟ {tally(U1)}"),
     U1,
     T("Three gates of 5, then 4.", "5 کے تین دروازے، پھر 4"),
     T("Right! 19.", "درست! 19"),
     T("5 + 5 + 5 + 4 = 19.", "5 + 5 + 5 + 4 = 19"),
     common_wrong=[wrong(16, "Each gate is 5, not 4: 19.", "ہر دروازہ 5 ہے، 4 نہیں: 19")],
     qtype="recall", skill=DH_TABLES),
   number_question(
     "u2_bar",
     T("Test 2: On a bar graph each square stands for 5 books. A bar is 8 squares tall. How many books?", "ٹیسٹ 2: بار گراف کا ہر خانہ 5 کتابیں ہے۔ ایک ستون 8 خانے اونچا ہے۔ کتنی کتابیں؟"),
     U2,
     T("8 × 5.", "8 × 5"),
     T("Right! 40 books.", "درست! 40 کتابیں"),
     T("8 × 5 = 40.", "8 × 5 = 40"),
     common_wrong=[wrong(8, "Each square is 5 books: 40.", "ہر خانہ 5 کتابیں ہے: 40", "ignores_scale")],
     qtype="apply", skill=DH_BAR_GRAPHS),
   number_question(
     "u3_mean",
     T(f"Test 3: Find the mean of {nums(U3_DATA)}.", f"ٹیسٹ 3: {nums(U3_DATA)} کی اوسط معلوم کریں۔"),
     U3,
     T("Total ÷ 4.", "کل ÷ 4"),
     T("Right! 10.", "درست! 10"),
     T("40 ÷ 4 = 10.", "40 ÷ 4 = 10"),
     common_wrong=[wrong(40, "40 is the total. Divide by 4: 10.", "40 کل ہے۔ 4 سے تقسیم کریں: 10", "forgets_divide")],
     qtype="apply", skill=DH_MEAN),
   number_question(
     "u4_mode",
     T(f"Test 4: Find the mode of {nums(U4_DATA)}.", f"ٹیسٹ 4: {nums(U4_DATA)} کا موڈ معلوم کریں۔"),
     U4,
     T("Which number appears most often?", "کون سا عدد سب سے زیادہ بار آتا ہے؟"),
     T("Right! 3.", "درست! 3"),
     T("3 appears three times: the mode is 3.", "3 تین بار آتا ہے: موڈ 3 ہے۔"),
     common_wrong=[wrong(8, "8 is the largest, but appears once. The mode is 3.", "8 سب سے بڑا ہے، لیکن ایک بار آتا ہے۔ موڈ 3 ہے۔")],
     qtype="apply", skill=DH_MODE_RANGE),
   number_question(
     "u5_heights",
     T(f"Test 5: The heights of four children are {nums(U5_DATA)} cm. What is the range of their heights, in cm?", f"ٹیسٹ 5: چار بچوں کی لمبائیاں {nums(U5_DATA)} سینٹی میٹر ہیں۔ ان کی لمبائیوں کی رینج کتنے سینٹی میٹر ہے؟"),
     U5,
     T("Tallest − shortest.", "سب سے لمبا − سب سے چھوٹا"),
     T("Right! 142 − 120 = 22 cm.", "درست! 142 − 120 = 22 سینٹی میٹر"),
     T("142 − 120 = 22.", "142 − 120 = 22"),
     common_wrong=[wrong(14, "The shortest is 120, not 128: 142 − 120 = 22.", "سب سے چھوٹا 120 ہے، 128 نہیں: 142 − 120 = 22")],
     qtype="apply"),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Data handling unit complete! You can read and use data now.", "مواد کا باب مکمل! اب آپ مواد پڑھ اور استعمال کر سکتے ہیں۔"),
    "text": T("Choose the right tool: total for 'altogether', take away for 'how many more', mean for a fair share, mode for the most common, range for the spread. Check bar graph scales, and remember a zero still counts as a value.",
              "صحیح طریقہ چنیں: 'سب مل کر' کے لیے کل، 'کتنے زیادہ' کے لیے نفی، برابر حصے کے لیے اوسط، سب سے عام کے لیے موڈ، پھیلاؤ کے لیے رینج۔ بار گراف کا پیمانہ دیکھیں، اور یاد رکھیں صفر بھی ایک قیمت ہے۔"),
    "points": [T("Pick the right measure first.", "پہلے صحیح پیمانہ چنیں۔"),
               T("A zero still counts.", "صفر بھی گنا جاتا ہے۔")]},
 ],
 "review_questions": [
   {"id": "r_scale", "type": "apply", "skill": SKILL, "step": number_question(
     "r_scale",
     T("Each square on a bar graph stands for 20 people. A bar is 6 squares tall. How many people?", "بار گراف کا ہر خانہ 20 لوگ ہے۔ ایک ستون 6 خانے اونچا ہے۔ کتنے لوگ؟"),
     R1,
     T("6 × 20.", "6 × 20"),
     T("Right! 120 people.", "درست! 120 لوگ"),
     T("6 × 20 = 120.", "6 × 20 = 120"),
     common_wrong=[wrong(26, "Multiply, don't add: 6 × 20 = 120.", "جمع نہیں، ضرب: 6 × 20 = 120", "ignores_scale")],
     qtype=None)},
   {"id": "r_range", "type": "apply", "skill": SKILL, "step": number_question(
     "r_range",
     T(f"Goals scored by a team in five matches: {nums(R2_DATA)}. What is the range?", f"ایک ٹیم کے پانچ میچوں میں گول: {nums(R2_DATA)}۔ رینج کتنی ہے؟"),
     R2,
     T("Largest − smallest.", "سب سے بڑا − سب سے چھوٹا"),
     T("Right! 21 − 9 = 12.", "درست! 21 − 9 = 12"),
     T("21 − 9 = 12.", "21 − 9 = 12"),
     common_wrong=[wrong(9, "9 is the mode. The range is 21 − 9 = 12.", "9 موڈ ہے۔ رینج 21 − 9 = 12 ہے۔")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Data Handling unit. No textbook text or exercises were used.",
   "The main skill here is choosing the right measure (total, difference, mean, mode, range). s9 checks that a zero value still counts in the mean.",
   "The unit test (u1 to u5) has one question per earlier lesson plus a real-life problem. Each is tagged with that lesson's skill, so results feed back into the mastery of earlier lessons.",
   "The numbers were worked out in content/sources/g6-maths-10/data_word_problems.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
# ---------- pictures ----------
DAYS = [en[:2] for (en, _), _ in SAMOSAS]
assert DAYS == ["Mo", "Tu", "We", "Th", "Fr"]


def samosa_graph():
    return bar_graph(SOLD, DAYS,
        "A bar graph of samosas sold, with a scale from 0 to 50 in 10s: Mo (Monday) 40, Tu (Tuesday) 35, We (Wednesday) 50, Th (Thursday) 45, Fr (Friday) 30.",
        "بکنے والے سموسوں کا بار گراف، پیمانہ 0 سے 50 تک، 10 کے وقفے سے: Mo (پیر) 40، Tu (منگل) 35، We (بدھ) 50، Th (جمعرات) 45، Fr (جمعہ) 30۔",
        top=50, step=10)


def one_bar(n, each, cat, what_en, what_ur):
    return squares_bar(n, each, cat,
                       f"One bar of {what_en} made of {n} squares stacked up. A key beside it shows one square = {each}.",
                       f"{what_ur} کا ایک ستون جو {n} خانوں سے بنا ہے۔ ساتھ کی کلید دکھاتی ہے: ایک خانہ = {each}۔")


WEEKS = [40, 60, 45]
assert S8 + sum(WEEKS) == 50 * 4
attach(lesson, {
    "s4_samosas": samosa_graph(),
    "s5_range": samosa_graph(),
    "s6_wheat": one_bar(7, 10, "W", "wheat", "گندم"),
    "s7_runs": bar_graph([30] * 5, ["1", "2", "3", "4", "5"],
        "Five equal bars, one for each match 1 to 5, each at the mean, 30 runs, with 30 written above each bar.",
        "پانچ برابر ستون، ہر میچ 1 سے 5 کا ایک، ہر ایک اوسط یعنی 30 رنز پر، ہر ستون کے اوپر 30 لکھا ہے۔",
        top=30, step=10, numbers=False, bar_text=["30"] * 5, height=130),
    "s8_savings": bar_graph(WEEKS + [0], ["1", "2", "3", "4"],
        "Bars for weeks 1 to 4 of Sana's savings: 40, 60 and 45 rupees, with the value above each. Week 4 has no bar, only a question mark. A dashed line across the graph shows the mean, 50.",
        "ثنا کی بچت کے ہفتوں 1 سے 4 کے ستون: 40، 60 اور 45 روپے، ہر ایک کے اوپر اس کی قیمت۔ ہفتہ 4 کا کوئی ستون نہیں، صرف سوالیہ نشان۔ گراف کے آر پار ڈیش والی لکیر اوسط، 50، دکھاتی ہے۔",
        top=60, step=10, numbers=False, bar_text=["40", "60", "45", None], missing=3, mean_line=50, mean_text="50"),
    "s9_find_error": bar_graph([10, 0, 20], ["1", "2", "3"],
        "Bars for cakes sold on days 1, 2 and 3: 10, 0 and 20, with the value above each. Day 2 has no bar, only 0 written on the line, but it is still one of the 3 days.",
        "دن 1، 2 اور 3 کو بکنے والے کیکوں کے ستون: 10، 0 اور 20، ہر ایک کے اوپر اس کی قیمت۔ دن 2 کا کوئی ستون نہیں، صرف لکیر پر 0 لکھا ہے، لیکن یہ بھی 3 دنوں میں سے ایک دن ہے۔",
        top=20, step=5, numbers=False, bar_text=["10", "0", "20"], height=130),
    "u1_tally": tally_figure(U1, "Tally marks: 3 groups of five, each four upright lines with a fifth line across them, then 4 single lines.",
                             "ٹیلی کے نشان: پانچ کے 3 گروہ، ہر ایک میں چار کھڑی لکیریں اور ان کے اوپر پانچویں ترچھی لکیر، پھر 4 اکیلی لکیریں۔"),
    "u2_bar": one_bar(8, 5, "B", "books", "کتابوں"),
    "u5_heights": height_bars(list(U5_DATA),
        "Bars for the heights of four children, in the order given, with the height in cm above each: 120, 135, 128, 142.",
        "چار بچوں کے قد کے ستون، دی گئی ترتیب میں، ہر ایک کے اوپر قد سینٹی میٹر میں: 120، 135، 128، 142۔"),
    "qb_find_error": one_bar(6, 20, "P", "people", "لوگوں"),
    "r_scale": one_bar(6, 20, "P", "people", "لوگوں"),
})
write(lesson)
