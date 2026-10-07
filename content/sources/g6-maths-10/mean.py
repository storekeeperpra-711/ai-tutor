from common import (T, opt, say, wrong, number_question, table_text, write,
                    REF, REVIEW, DH_TABLES, DH_MEAN)

SKILL = DH_MEAN


def mean(*xs):
    total = sum(xs)
    assert total % len(xs) == 0, xs
    return total // len(xs)


# s2: a table total
PETS = [(("Cats", "بلیاں"), 6), (("Dogs", "کتے"), 4), (("Birds", "پرندے"), 9)]
PETS_EN, PETS_UR = table_text(PETS)
S2 = sum(v for _, v in PETS)
assert S2 == 19
# s4
S4 = mean(4, 6, 8)
assert S4 == 6 and 4 + 6 + 8 == 18
# s5: test marks
S5 = mean(7, 9, 5, 10, 9)
assert S5 == 8 and 7 + 9 + 5 + 10 + 9 == 40
# s6: runs in four matches
S6 = mean(12, 30, 25, 33)
assert S6 == 25 and 12 + 30 + 25 + 33 == 100
# s7: mean 10 of three numbers -> total
S7 = 10 * 3
assert S7 == 30
# s8: mean 15 of four numbers, three known
S8 = 15 * 4 - (10 + 20 + 12)
assert S8 == 18 and mean(10, 20, 12, S8) == 15 and 10 + 20 + 12 == 42
# s9: 2, 4, 9 -> divide by 3, not 2
assert mean(2, 4, 9) == 5 and 15 / 2 == 7.5
# s11: temperatures
S11 = mean(30, 32, 31, 29, 33)
assert S11 == 31 and 30 + 32 + 31 + 29 + 33 == 155
# question bank and review
QB = mean(5, 7, 12)
assert QB == 8 and 5 + 7 + 12 == 24
R1 = mean(10, 20, 30, 40)
assert R1 == 25 and 10 + 20 + 30 + 40 == 100
R2 = mean(6, 6, 9)
assert R2 == 7 and 6 + 6 + 9 == 21

lesson = {
 "id": "g6-maths-10-average-mean",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Find the average (mean) of a set of numbers as the total divided by how many numbers there are, and use it to find a missing value.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Average (mean)", "اوسط"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": DH_TABLES}],
 "misconceptions": [
   {"id": "forgets_divide", "description": "Gives the total instead of dividing by how many numbers there are."},
   {"id": "wrong_count", "description": "Divides by the wrong number, such as one less than the count."},
   {"id": "mean_is_middle", "description": "Takes the middle number of the list as the mean."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_how", "type": "recall", "step": {
     "id": "qb_how", "type": "choice",
     "prompt": T("How do you find the average (mean) of some numbers?", "کچھ اعداد کی اوسط کیسے نکالتے ہیں؟"),
     "options": [
       opt("total_div", "Add them, then divide by how many numbers there are", "انہیں جمع کریں، پھر اعداد کی تعداد سے تقسیم کریں", True,
           "Yes! Total ÷ how many.", "جی ہاں! کل ÷ تعداد۔"),
       opt("add", "Just add them", "بس جمع کریں", False, "That gives the total. Then divide by how many.", "یہ کل ہے۔ پھر تعداد سے تقسیم کریں۔", "forgets_divide"),
       opt("middle", "Pick the middle number", "درمیانی عدد چنیں", False, "The mean shares the total equally: total ÷ how many.", "اوسط کل کو برابر بانٹتی ہے: کل ÷ تعداد۔", "mean_is_middle"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("Find the mean of 5, 7 and 12.", "5، 7 اور 12 کی اوسط معلوم کریں۔"),
     QB,
     T("Total, then divide by 3.", "کل، پھر 3 سے تقسیم"),
     T("Right! 8.", "درست! 8"),
     T("5 + 7 + 12 = 24, and 24 ÷ 3 = 8.", "5 + 7 + 12 = 24، اور 24 ÷ 3 = 8"),
     common_wrong=[wrong(24, "24 is the total. Divide by 3: 8.", "24 کل ہے۔ 3 سے تقسیم کریں: 8", "forgets_divide"),
                   wrong(12, "That divides by 2. There are 3 numbers: 24 ÷ 3 = 8.", "یہ 2 سے تقسیم ہے۔ اعداد 3 ہیں: 24 ÷ 3 = 8", "wrong_count")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Nadia's scores are 6, 8 and 10. She says her average is 24. What went wrong?", "نادیہ کے نمبر 6، 8 اور 10 ہیں۔ وہ کہتی ہے اس کی اوسط 24 ہے۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("divide", "24 is the total. Divide by 3: the mean is 8.", "24 کل ہے۔ 3 سے تقسیم کریں: اوسط 8 ہے۔", True,
           "Yes! The mean can't be bigger than every score.", "جی ہاں! اوسط ہر نمبر سے بڑی نہیں ہو سکتی۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "24 is bigger than all her scores! Divide the total by 3: 8.", "24 تو اس کے سب نمبروں سے بڑا ہے! کل کو 3 سے تقسیم کریں: 8", "forgets_divide"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_mean", "front": T("Average (mean)?", "اوسط؟"),
    "back": T("Total ÷ how many. Mean of 4, 6, 8: 18 ÷ 3 = 6.", "کل ÷ تعداد۔ 4، 6، 8 کی اوسط: 18 ÷ 3 = 6")},
   {"id": "f_total", "front": T("Know the mean, need the total?", "اوسط معلوم، کل چاہیے؟"),
    "back": T("Total = mean × how many.", "کل = اوسط × تعداد")},
 ],
 "home_tasks": [{"id": "h_share", "text": T(
   "Take three piles of beans or pebbles of different sizes. Count each pile. Now share all of them out equally into three piles. How many in each? That is the mean!",
   "دانوں یا کنکروں کی تین مختلف ڈھیریاں لیں۔ ہر ڈھیری گنیں۔ اب سب کو تین برابر ڈھیریوں میں بانٹیں۔ ہر ایک میں کتنے؟ یہی اوسط ہے!")}],
 "glossary": [T("Average (mean)", "اوسط"), T("Total", "کل"), T("Share equally", "برابر بانٹنا"), T("Data", "مواد (ڈیٹا)")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Three friends have 4, 6 and 8 sweets. If they share them out fairly, how many does each get?",
                     "تین دوستوں کے پاس 4، 6 اور 8 ٹافیاں ہیں۔ اگر وہ برابر بانٹیں تو ہر ایک کو کتنی ملیں گی؟"),
    "text": T("Today we find the average, also called the mean. First, a quick check.", "آج ہم اوسط نکالیں گے۔ پہلے ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T(f"Pets in a street: {PETS_EN}. How many pets altogether?", f"ایک گلی کے پالتو جانور: {PETS_UR}۔ کل کتنے جانور؟"),
     S2,
     T("Add all three.", "تینوں جمع کریں۔"),
     T("Right! 19.", "درست! 19"),
     T("6 + 4 + 9 = 19.", "6 + 4 + 9 = 19"),
     common_wrong=[wrong(3, "3 is the number of kinds. Add them: 19.", "3 اقسام کی تعداد ہے۔ جمع کریں: 19")],
     qtype="recall", skill=DH_TABLES),
   {"id": "s3_mean", "type": "explain",
    "character": say("happy", "The mean is what everyone gets if we share fairly!", "اوسط وہ ہے جو برابر بانٹنے پر ہر ایک کو ملے!"),
    "text": T("To find the mean (average): 1) add all the numbers to get the total; 2) divide by how many numbers there are. For 4, 6 and 8: total 18, three numbers, 18 ÷ 3 = 6. The mean is always between the smallest and the largest number.",
              "اوسط نکالنے کے لیے: 1) سب اعداد جمع کر کے کل نکالیں؛ 2) اعداد کی تعداد سے تقسیم کریں۔ 4، 6 اور 8 کے لیے: کل 18، تین اعداد، 18 ÷ 3 = 6۔ اوسط ہمیشہ سب سے چھوٹے اور سب سے بڑے عدد کے درمیان ہوتی ہے۔")},
   number_question(
     "s4_sweets",
     T("Find the mean of 4, 6 and 8.", "4، 6 اور 8 کی اوسط معلوم کریں۔"),
     S4,
     T("Total 18, three numbers.", "کل 18، تین اعداد"),
     T("Right! 6 each.", "درست! ہر ایک کو 6"),
     T("18 ÷ 3 = 6.", "18 ÷ 3 = 6"),
     common_wrong=[wrong(18, "18 is the total. Share it among 3: 6.", "18 کل ہے۔ اسے 3 میں بانٹیں: 6", "forgets_divide"),
                   wrong(9, "That divides by 2. There are 3 numbers: 18 ÷ 3 = 6.", "یہ 2 سے تقسیم ہے۔ اعداد 3 ہیں: 18 ÷ 3 = 6", "wrong_count")]),
   number_question(
     "s5_marks",
     T("Ayesha's test marks out of 10 are 7, 9, 5, 10 and 9. What is her mean mark?", "عائشہ کے 10 میں سے ٹیسٹ نمبر 7، 9، 5، 10 اور 9 ہیں۔ اس کے نمبروں کی اوسط کیا ہے؟"),
     S5,
     T("Add all five, then divide by 5.", "پانچوں جمع کریں، پھر 5 سے تقسیم"),
     T("Right! 8.", "درست! 8"),
     T("7 + 9 + 5 + 10 + 9 = 40, and 40 ÷ 5 = 8.", "7 + 9 + 5 + 10 + 9 = 40، اور 40 ÷ 5 = 8"),
     common_wrong=[wrong(40, "40 is the total. Divide by 5: 8.", "40 کل ہے۔ 5 سے تقسیم کریں: 8", "forgets_divide"),
                   wrong(10, "That divides by 4. There are 5 marks: 40 ÷ 5 = 8.", "یہ 4 سے تقسیم ہے۔ نمبر 5 ہیں: 40 ÷ 5 = 8", "wrong_count")]),
   number_question(
     "s6_runs",
     T("Babar scores 12, 30, 25 and 33 runs in four cricket matches. What is his mean score?", "بابر چار کرکٹ میچوں میں 12، 30، 25 اور 33 رنز بناتا ہے۔ اس کی اوسط کیا ہے؟"),
     S6,
     T("Total ÷ 4.", "کل ÷ 4"),
     T("Right! 25 runs.", "درست! 25 رنز"),
     T("12 + 30 + 25 + 33 = 100, and 100 ÷ 4 = 25.", "12 + 30 + 25 + 33 = 100، اور 100 ÷ 4 = 25"),
     common_wrong=[wrong(100, "100 is the total. Divide by 4: 25.", "100 کل ہے۔ 4 سے تقسیم کریں: 25", "forgets_divide")]),
   number_question(
     "s7_total",
     T("The mean of three numbers is 10. What is their total?", "تین اعداد کی اوسط 10 ہے۔ ان کا کل کیا ہے؟"),
     S7,
     T("Total = mean × how many.", "کل = اوسط × تعداد"),
     T("Right! 30.", "درست! 30"),
     T("10 × 3 = 30.", "10 × 3 = 30"),
     common_wrong=[wrong(10, "10 is the mean. The total is 10 × 3 = 30.", "10 اوسط ہے۔ کل 10 × 3 = 30 ہے۔"),
                   wrong(13, "Multiply, don't add: 10 × 3 = 30.", "جمع نہیں، ضرب: 10 × 3 = 30")]),
   number_question(
     "s8_missing",
     T("The mean of four numbers is 15. Three of them are 10, 20 and 12. What is the fourth number?", "چار اعداد کی اوسط 15 ہے۔ ان میں سے تین 10، 20 اور 12 ہیں۔ چوتھا عدد کیا ہے؟"),
     S8,
     T("The total must be 15 × 4 = 60. Take away the three you know.", "کل 15 × 4 = 60 ہونا چاہیے۔ معلوم تینوں نفی کریں۔"),
     T("Right! 18. Check: 10 + 20 + 12 + 18 = 60, and 60 ÷ 4 = 15.", "درست! 18۔ جانچ: 10 + 20 + 12 + 18 = 60، اور 60 ÷ 4 = 15"),
     T("60 − 42 = 18.", "60 − 42 = 18"),
     common_wrong=[wrong(15, "The mean is 15, but the fourth number must make the total 60: 18.", "اوسط 15 ہے، لیکن چوتھا عدد کل کو 60 بنائے: 18")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("To find the mean of 2, 4 and 9, Usman works out 15 ÷ 2 = 7.5. What went wrong?", "2، 4 اور 9 کی اوسط کے لیے عثمان 15 ÷ 2 = 7.5 نکالتا ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("count", "There are 3 numbers, so divide by 3: 15 ÷ 3 = 5.", "اعداد 3 ہیں، تو 3 سے تقسیم کریں: 15 ÷ 3 = 5", True,
          "Yes! Divide by how many numbers there are.", "جی ہاں! اعداد کی تعداد سے تقسیم کریں۔"),
      opt("total", "The total is wrong.", "کل غلط ہے۔", False,
          "2 + 4 + 9 = 15 is right. He divided by the wrong number: 3, not 2.", "2 + 4 + 9 = 15 درست ہے۔ اس نے غلط عدد سے تقسیم کیا: 3، نہ کہ 2۔"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "There are 3 numbers, so divide by 3: 5.", "اعداد 3 ہیں، تو 3 سے تقسیم کریں: 5", "wrong_count"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why do we divide the total by how many numbers there are? Can you teach me?",
                     "ہم کل کو اعداد کی تعداد سے کیوں تقسیم کرتے ہیں؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why is the mean the total divided by how many numbers there are?", "اپنے الفاظ میں بتائیں: اوسط کل کو تعداد سے تقسیم کیوں ہوتی ہے؟"),
    "key_idea": "The mean is what each would get if the total were shared out equally. Sharing equally among a number of people (or values) means dividing the total by that number.",
    "levels": {
      "got_it": "Says the mean is the total shared equally, and sharing equally means dividing by how many.",
      "partly": "Mentions sharing or dividing, without linking them.",
      "not_yet": "Gives no reason, or just repeats the rule."},
    "keywords": [
      ["share", "equal", "fair", "بانٹ", "برابر"],
      ["total", "all", "کل", "سب"],
      ["divide", "each", "تقسیم", "ہر ایک"]],
    "fallback_feedback": {
      "got_it": T("Well explained! The mean is the total shared out equally.", "بہت خوب! اوسط کل کو برابر بانٹنا ہے۔"),
      "partly": T("Good start! Now say how sharing equally and dividing are linked.", "اچھی شروعات! اب بتائیں برابر بانٹنا اور تقسیم کیسے جڑے ہیں۔"),
      "not_yet": T("Think of the three friends sharing 18 sweets fairly. What did you do to find each share?", "تین دوستوں کو سوچیں جو 18 ٹافیاں برابر بانٹتے ہیں۔ ہر ایک کا حصہ نکالنے کے لیے آپ نے کیا کیا؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_temps",
     T("The temperature at noon for five days was 30°, 32°, 31°, 29° and 33°. What was the mean temperature, in degrees?", "پانچ دن دوپہر کا درجہ حرارت 30°، 32°، 31°، 29° اور 33° تھا۔ اوسط درجہ حرارت کتنے درجے تھا؟"),
     S11,
     T("Total ÷ 5.", "کل ÷ 5"),
     T("Right! 31°.", "درست! 31°"),
     T("30 + 32 + 31 + 29 + 33 = 155, and 155 ÷ 5 = 31.", "30 + 32 + 31 + 29 + 33 = 155، اور 155 ÷ 5 = 31"),
     common_wrong=[wrong(155, "155 is the total. Divide by 5: 31.", "155 کل ہے۔ 5 سے تقسیم کریں: 31", "forgets_divide")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "You can find averages now!", "اب آپ اوسط نکال سکتے ہیں!"),
    "text": T("Mean (average) = total ÷ how many numbers. It is what each would get if everything were shared equally, so it always lies between the smallest and largest values. Turned around: total = mean × how many.",
              "اوسط = کل ÷ اعداد کی تعداد۔ یہ وہ ہے جو سب کچھ برابر بانٹنے پر ہر ایک کو ملے، اس لیے یہ ہمیشہ سب سے چھوٹی اور سب سے بڑی قیمت کے درمیان ہوتی ہے۔ الٹا: کل = اوسط × تعداد۔"),
    "points": [T("Mean = total ÷ how many.", "اوسط = کل ÷ تعداد۔"),
               T("Total = mean × how many.", "کل = اوسط × تعداد۔")]},
 ],
 "review_questions": [
   {"id": "r_mean4", "type": "apply", "skill": SKILL, "step": number_question(
     "r_mean4",
     T("Find the mean of 10, 20, 30 and 40.", "10، 20، 30 اور 40 کی اوسط معلوم کریں۔"),
     R1,
     T("Total ÷ 4.", "کل ÷ 4"),
     T("Right! 25.", "درست! 25"),
     T("100 ÷ 4 = 25.", "100 ÷ 4 = 25"),
     common_wrong=[wrong(100, "Divide the total by 4: 25.", "کل کو 4 سے تقسیم کریں: 25", "forgets_divide")],
     qtype=None)},
   {"id": "r_mean3", "type": "apply", "skill": SKILL, "step": number_question(
     "r_mean3",
     T("Find the mean of 6, 6 and 9.", "6، 6 اور 9 کی اوسط معلوم کریں۔"),
     R2,
     T("Total ÷ 3.", "کل ÷ 3"),
     T("Right! 7.", "درست! 7"),
     T("21 ÷ 3 = 7.", "21 ÷ 3 = 7"),
     common_wrong=[wrong(6, "6 is the middle number. The mean is 21 ÷ 3 = 7.", "6 درمیانی عدد ہے۔ اوسط 21 ÷ 3 = 7 ہے۔", "mean_is_middle")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Data Handling unit. No textbook text or exercises were used.",
   "The mean is introduced as fair sharing (sweets, beans). Every mean in the lesson is a whole number, so children can focus on the idea, not long division.",
   "Urdu terms to check: اوسط (average/mean), کل (total).",
   "The numbers were worked out in content/sources/g6-maths-10/mean.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)
