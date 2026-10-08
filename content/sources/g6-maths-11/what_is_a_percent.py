from figs import attach, battery, hundred_grid, two_grids
from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, FRACTIONS_EQUIVALENT, PC_MEANING, as_percent)

SKILL = PC_MEANING

# s2: 1/4 = ?/100
S2 = 100 // 4
assert S2 == 25
# s4: 37 of 100 squares coloured
S4 = 37
assert as_percent(37, 100) == S4
# s5: 45% shaded -> not shaded
S5 = 100 - 45
assert S5 == 55
# s6: 9/100 as a percent
S6 = 9
assert as_percent(9, 100) == S6
# s8: 3/10 = 30/100
S8 = as_percent(3, 10)
assert S8 == 30
# s9: 7% is 7 out of 100, not 7 out of 10
assert as_percent(7, 10) == 70
# s11: 12 bad mangoes out of 100 -> good
S11 = 100 - 12
assert S11 == 88
# question bank and review
QB = as_percent(1, 5)
assert QB == 20
R1 = as_percent(1, 2)
assert R1 == 50
R2 = 100 - 64
assert R2 == 36

lesson = {
 "id": "g6-maths-11-what-is-a-percent",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Understand a percent as a number out of 100, and write simple fractions out of 100 or 10 as percents.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("What is a percent?", "فیصد کیا ہے؟"),
 "estimated_minutes": 12,
 "prerequisites": [{"skill": FRACTIONS_EQUIVALENT}],
 "misconceptions": [
   {"id": "out_of_ten", "description": "Reads a percent as a number out of 10 instead of out of 100."},
   {"id": "rest_not_whole", "description": "Forgets that the whole is 100%, so can't find the part that is left."},
   {"id": "denominator_as_percent", "description": "Uses the top number of a fraction as the percent without first making the bottom 100."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_mean", "type": "recall", "step": {
     "id": "qb_mean", "type": "choice",
     "prompt": T("What does 40% mean?", "40% کا کیا مطلب ہے؟"),
     "options": [
       opt("hundred", "40 out of every 100", "ہر 100 میں سے 40", True,
           "Yes! Per cent means out of 100.", "جی ہاں! فیصد کا مطلب ہے 100 میں سے۔"),
       opt("ten", "40 out of every 10", "ہر 10 میں سے 40", False,
           "Per cent means out of 100, not 10.", "فیصد کا مطلب 100 میں سے ہے، 10 میں سے نہیں۔", "out_of_ten"),
       opt("forty", "40 things", "40 چیزیں", False,
           "A percent is a part out of 100: 40 out of every 100.", "فیصد 100 میں سے حصہ ہے: ہر 100 میں سے 40۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("Write 1/5 as a percent. Type just the number.", "1/5 کو فیصد میں لکھیں۔ صرف عدد لکھیں۔"),
     QB,
     T("1/5 = ?/100. Multiply top and bottom by 20.", "1/5 = ?/100۔ اوپر اور نیچے کو 20 سے ضرب دیں۔"),
     T("Right! 1/5 = 20/100 = 20%.", "درست! 1/5 = 20/100 = 20%"),
     T("1/5 = 20/100, so it is 20%.", "1/5 = 20/100، یعنی 20%"),
     common_wrong=[wrong(1, "Make the bottom 100 first: 1/5 = 20/100 = 20%.", "پہلے نیچے والا 100 بنائیں: 1/5 = 20/100 = 20%", "denominator_as_percent"),
                   wrong(5, "Make the bottom 100 first: 1/5 = 20/100 = 20%.", "پہلے نیچے والا 100 بنائیں: 1/5 = 20/100 = 20%", "denominator_as_percent")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("A test has 10 questions. Hina gets 6 right and says she scored 6%. What went wrong?", "ٹیسٹ میں 10 سوال ہیں۔ حنا کے 6 درست ہیں اور وہ کہتی ہے اس کے 6% نمبر ہیں۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("hundred", "6 out of 10 is 60 out of 100, so she scored 60%.", "10 میں سے 6 یعنی 100 میں سے 60، تو اس کے 60% ہیں۔", True,
           "Yes! A percent is always out of 100.", "جی ہاں! فیصد ہمیشہ 100 میں سے ہوتا ہے۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "6% would be 6 out of 100. She got 6 out of 10, which is 60%.", "6% کا مطلب 100 میں سے 6 ہے۔ اس کے 10 میں سے 6 ہیں، یعنی 60%۔", "out_of_ten"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_percent", "front": T("Percent (%)?", "فیصد (%)؟"),
    "back": T("Out of 100. 25% = 25 out of 100 = 25/100.", "100 میں سے۔ 25% = 100 میں سے 25 = 25/100")},
   {"id": "f_whole", "front": T("The whole thing is…", "پوری چیز…"),
    "back": T("100%. If 30% is used, 70% is left.", "100% ہے۔ اگر 30% استعمال ہو تو 70% باقی ہے۔")},
 ],
 "home_tasks": [{"id": "h_spot", "text": T(
   "Look for the % sign at home or in the bazaar: a phone battery, a sale board, a packet of milk or biscuits. Write down three you find and say what each one means out of 100.",
   "گھر یا بازار میں % کا نشان ڈھونڈیں: فون کی بیٹری، سیل کا بورڈ، دودھ یا بسکٹ کا پیکٹ۔ تین لکھیں اور بتائیں ہر ایک کا مطلب 100 میں سے کیا ہے۔")}],
 "glossary": [T("Percent", "فیصد"), T("Out of 100", "100 میں سے"), T("Whole", "پورا"), T("Fraction", "کسر")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "My phone battery says 75%. Is that a lot or a little? What does the 75 count?",
                     "میرے فون کی بیٹری 75% دکھاتی ہے۔ یہ زیادہ ہے یا کم؟ 75 کس چیز کو گنتا ہے؟"),
    "text": T("Today we learn what a percent is. First, a quick check on fractions.", "آج ہم سیکھیں گے کہ فیصد کیا ہے۔ پہلے کسروں کا ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("1/4 = ?/100. What is the missing number?", "1/4 = ?/100۔ خالی جگہ پر کون سا عدد آئے گا؟"),
     S2,
     T("4 × 25 = 100, so multiply the top by 25 too.", "4 × 25 = 100، تو اوپر والے کو بھی 25 سے ضرب دیں۔"),
     T("Right! 1/4 = 25/100.", "درست! 1/4 = 25/100"),
     T("Multiply top and bottom by 25: 25/100.", "اوپر اور نیچے کو 25 سے ضرب دیں: 25/100"),
     common_wrong=[wrong(4, "Make the bottom 100 by multiplying by 25. Do the same to the top: 25.", "نیچے والے کو 25 سے ضرب دے کر 100 بنائیں۔ اوپر والے کے ساتھ بھی یہی کریں: 25")],
     qtype="recall", skill=FRACTIONS_EQUIVALENT),
   {"id": "s3_percent", "type": "explain",
    "character": say("happy", "Per cent means out of a hundred. Cent is an old word for hundred!", "فیصد کا مطلب ہے سو میں سے۔ فی صد یعنی ہر سو پر!"),
    "text": T("A percent is a number out of 100, and the sign % means \"out of 100\". 25% means 25 out of 100, which is 25/100, the same as 1/4. The whole thing is 100%. So a battery at 75% has 75 parts out of 100 left: three quarters full.",
              "فیصد 100 میں سے ایک عدد ہے، اور % کا نشان \"100 میں سے\" کا مطلب دیتا ہے۔ 25% کا مطلب ہے 100 میں سے 25، یعنی 25/100، جو 1/4 کے برابر ہے۔ پوری چیز 100% ہے۔ تو 75% والی بیٹری میں 100 میں سے 75 حصے باقی ہیں: تین چوتھائی بھری ہوئی۔")},
   number_question(
     "s4_squares",
     T("A grid has 100 squares. 37 are coloured green. What percent is green? Type just the number.", "ایک جال میں 100 خانے ہیں۔ 37 سبز ہیں۔ کتنے فیصد سبز ہیں؟ صرف عدد لکھیں۔"),
     S4,
     T("Out of 100 is the same as percent.", "100 میں سے یعنی فیصد۔"),
     T("Right! 37 out of 100 is 37%.", "درست! 100 میں سے 37 یعنی 37%"),
     T("37 out of 100 squares is 37%.", "100 میں سے 37 خانے یعنی 37%"),
     common_wrong=[wrong(63, "63 squares are not green. Green is 37 out of 100: 37%.", "63 خانے سبز نہیں ہیں۔ سبز 100 میں سے 37 ہیں: 37%")]),
   number_question(
     "s5_rest",
     T("45% of a wall is painted. What percent is not painted yet?", "ایک دیوار کا 45% رنگ ہو چکا ہے۔ کتنے فیصد ابھی باقی ہے؟"),
     S5,
     T("The whole wall is 100%.", "پوری دیوار 100% ہے۔"),
     T("Right! 100 − 45 = 55%.", "درست! 100 − 45 = 55%"),
     T("The whole is 100%, so 100 − 45 = 55.", "پورا 100% ہے، تو 100 − 45 = 55"),
     common_wrong=[wrong(45, "45% is the painted part. The rest is 100 − 45 = 55%.", "45% رنگ والا حصہ ہے۔ باقی 100 − 45 = 55% ہے۔", "rest_not_whole"),
                   wrong(5, "The whole is 100%, not 50%: 100 − 45 = 55.", "پورا 100% ہے، 50% نہیں: 100 − 45 = 55", "rest_not_whole")]),
   number_question(
     "s6_hundredths",
     T("Write 9/100 as a percent. Type just the number.", "9/100 کو فیصد میں لکھیں۔ صرف عدد لکھیں۔"),
     S6,
     T("The bottom is already 100.", "نیچے والا پہلے ہی 100 ہے۔"),
     T("Right! 9/100 = 9%.", "درست! 9/100 = 9%"),
     T("9 out of 100 is 9%.", "100 میں سے 9 یعنی 9%"),
     common_wrong=[wrong(90, "That would be 90 out of 100. 9/100 is 9%.", "یہ 100 میں سے 90 ہوتا۔ 9/100 یعنی 9%", "out_of_ten")]),
   {"id": "s7_half", "type": "choice",
    "prompt": T("Which is the same as 50%?", "کون سا 50% کے برابر ہے؟"),
    "options": [
      opt("half", "Half", "آدھا", True, "Yes! 50 out of 100 is one half.", "جی ہاں! 100 میں سے 50 یعنی آدھا۔"),
      opt("fifth", "One fifth", "پانچواں حصہ", False, "One fifth is 20 out of 100. 50 out of 100 is a half.", "پانچواں حصہ 100 میں سے 20 ہے۔ 100 میں سے 50 آدھا ہے۔"),
      opt("all", "All of it", "سارا", False, "All of it is 100%. 50% is half.", "سارا 100% ہے۔ 50% آدھا ہے۔", "rest_not_whole"),
    ]},
   number_question(
     "s8_tenths",
     T("3/10 of the children walk to school. What percent is that? Type just the number.", "3/10 بچے پیدل اسکول آتے ہیں۔ یہ کتنے فیصد ہے؟ صرف عدد لکھیں۔"),
     S8,
     T("3/10 = ?/100. Multiply top and bottom by 10.", "3/10 = ?/100۔ اوپر اور نیچے کو 10 سے ضرب دیں۔"),
     T("Right! 3/10 = 30/100 = 30%.", "درست! 3/10 = 30/100 = 30%"),
     T("3/10 = 30/100, so it is 30%.", "3/10 = 30/100، یعنی 30%"),
     common_wrong=[wrong(3, "Make the bottom 100 first: 3/10 = 30/100 = 30%.", "پہلے نیچے والا 100 بنائیں: 3/10 = 30/100 = 30%", "denominator_as_percent")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Ali says 7% means 7 out of 10. What went wrong?", "علی کہتا ہے 7% کا مطلب ہے 10 میں سے 7۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("hundred", "A percent is out of 100: 7% is 7 out of 100.", "فیصد 100 میں سے ہوتا ہے: 7% یعنی 100 میں سے 7۔", True,
          "Yes! 7 out of 10 would be 70%.", "جی ہاں! 10 میں سے 7 تو 70% ہوتا۔"),
      opt("seventy", "7% means 70 out of 100.", "7% کا مطلب 100 میں سے 70 ہے۔", False,
          "70 out of 100 is 70%. 7% is 7 out of 100.", "100 میں سے 70 یعنی 70%۔ 7% یعنی 100 میں سے 7۔"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "Per cent means out of 100, so 7% is 7 out of 100.", "فیصد کا مطلب 100 میں سے ہے، تو 7% یعنی 100 میں سے 7۔", "out_of_ten"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why is the whole thing 100%, and not 10% or 1000%? Can you teach me?",
                     "پوری چیز 100% کیوں ہے، 10% یا 1000% کیوں نہیں؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why is the whole of something 100%?", "اپنے الفاظ میں بتائیں: کسی چیز کا پورا حصہ 100% کیوں ہوتا ہے؟"),
    "key_idea": "A percent counts parts out of 100. If the whole is cut into 100 equal parts, all of them together are 100 out of 100, which is 100%.",
    "levels": {
      "got_it": "Says a percent counts parts out of 100, so all 100 parts make 100%.",
      "partly": "Says percent means out of 100, without linking it to the whole.",
      "not_yet": "Gives no reason, or just repeats that the whole is 100%."},
    "keywords": [
      ["100", "hundred", "سو"],
      ["parts", "pieces", "حصے", "ٹکڑے"],
      ["whole", "all", "پورا", "سارا", "سب"]],
    "fallback_feedback": {
      "got_it": T("Well explained! The whole is 100 parts out of 100.", "بہت خوب! پوری چیز 100 میں سے 100 حصے ہے۔"),
      "partly": T("Good start! Now say what happens when you take all 100 parts.", "اچھی شروعات! اب بتائیں جب سب 100 حصے لیں تو کیا ہوتا ہے۔"),
      "not_yet": T("Think of the grid of 100 squares. If all of them are green, what percent is green?", "100 خانوں والا جال سوچیں۔ اگر سب سبز ہوں تو کتنے فیصد سبز ہیں؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_mangoes",
     T("A box has 100 mangoes. 12 are bad. What percent of the mangoes are good?", "ایک پیٹی میں 100 آم ہیں۔ 12 خراب ہیں۔ کتنے فیصد آم اچھے ہیں؟"),
     S11,
     T("All the mangoes are 100%. Take away the bad ones.", "سارے آم 100% ہیں۔ خراب نکال دیں۔"),
     T("Right! 88% are good.", "درست! 88% اچھے ہیں۔"),
     T("100 − 12 = 88, so 88%.", "100 − 12 = 88، یعنی 88%"),
     common_wrong=[wrong(12, "12% are bad. The good ones are 100 − 12 = 88%.", "12% خراب ہیں۔ اچھے 100 − 12 = 88% ہیں۔", "rest_not_whole")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Now you know what the % sign means!", "اب آپ جانتے ہیں کہ % کا نشان کیا بتاتا ہے!"),
    "text": T("A percent is a number out of 100: 25% means 25 out of 100, or 25/100. The whole thing is 100%, so the part left over is 100 minus the part used. To turn a fraction into a percent, first make its bottom number 100.",
              "فیصد 100 میں سے ایک عدد ہے: 25% یعنی 100 میں سے 25، یا 25/100۔ پوری چیز 100% ہے، تو باقی حصہ 100 میں سے استعمال شدہ حصہ نکال کر ملتا ہے۔ کسر کو فیصد بنانے کے لیے پہلے اس کا نیچے والا عدد 100 بنائیں۔"),
    "points": [T("% means out of 100.", "% یعنی 100 میں سے۔"),
               T("The whole is 100%.", "پورا 100% ہے۔")]},
 ],
 "review_questions": [
   {"id": "r_half", "type": "apply", "skill": SKILL, "step": number_question(
     "r_half",
     T("Write 1/2 as a percent. Type just the number.", "1/2 کو فیصد میں لکھیں۔ صرف عدد لکھیں۔"),
     R1,
     T("1/2 = ?/100", "1/2 = ?/100"),
     T("Right! 50%.", "درست! 50%"),
     T("1/2 = 50/100 = 50%.", "1/2 = 50/100 = 50%"),
     common_wrong=[wrong(2, "Make the bottom 100: 1/2 = 50/100 = 50%.", "نیچے والا 100 بنائیں: 1/2 = 50/100 = 50%", "denominator_as_percent")],
     qtype=None)},
   {"id": "r_rest", "type": "apply", "skill": SKILL, "step": number_question(
     "r_rest",
     T("64% of the seats on a bus are taken. What percent are empty?", "بس کی 64% نشستیں بھری ہیں۔ کتنے فیصد خالی ہیں؟"),
     R2,
     T("The whole bus is 100%.", "پوری بس 100% ہے۔"),
     T("Right! 36%.", "درست! 36%"),
     T("100 − 64 = 36.", "100 − 64 = 36"),
     common_wrong=[wrong(64, "64% are taken. Empty: 100 − 64 = 36%.", "64% بھری ہیں۔ خالی: 100 − 64 = 36%", "rest_not_whole")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Percentages unit. No textbook text or exercises were used.",
   "Number answers are typed without the % sign; each prompt says \"type just the number\" where that might confuse.",
   "Urdu terms to check: فیصد (percent), کسر (fraction).",
   "The numbers were worked out in content/sources/g6-maths-11/what_is_a_percent.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
# Pictures: grids of 100 small squares, and a battery for the hook.
attach(lesson, {
 "s1_hook": battery(75,
   "A phone battery cut into four equal parts by dashed lines. Three of the four parts are shaded, and it says 75%.",
   "فون کی ایک بیٹری جسے ڈیش والی لکیروں سے چار برابر حصوں میں بانٹا گیا ہے۔ چار میں سے تین حصے رنگے ہوئے ہیں اور اس پر 75% لکھا ہے۔"),
 "s3_percent": two_grids(25, 100, "25%", "100%",
   "Two grids of 100 small squares. In the first, 25 squares (two and a half rows of 10) are shaded and it says 25%. In the second, all 100 squares are shaded and it says 100%.",
   "100 چھوٹے خانوں والے دو جال۔ پہلے میں 25 خانے (10 کی ڈھائی قطاریں) رنگے ہیں اور 25% لکھا ہے۔ دوسرے میں سارے 100 خانے رنگے ہیں اور 100% لکھا ہے۔"),
 "s4_squares": hundred_grid(S4,
   f"A grid of 100 small squares in 10 rows of 10. The first {S4 // 10} rows and {S4 % 10} more squares are shaded.",
   f"100 چھوٹے خانوں کا جال، 10 خانوں کی 10 قطاریں۔ پہلی {S4 // 10} قطاریں اور {S4 % 10} خانے مزید رنگے ہوئے ہیں۔"),
 "s5_rest": hundred_grid(100 - S5,
   f"A grid of 100 small squares for the wall. {100 - S5} squares are shaded and marked {100 - S5}%. The squares that are not shaded are marked with a question mark.",
   f"دیوار کے لیے 100 چھوٹے خانوں کا جال۔ {100 - S5} خانے رنگے ہیں اور ان پر {100 - S5}% لکھا ہے۔ جو خانے رنگے نہیں ان پر سوالیہ نشان ہے۔",
   shaded_text=f"{100 - S5}%", rest_text="?"),
 "s6_hundredths": hundred_grid(S6,
   f"A grid of 100 small squares with {S6} squares shaded in the top row.",
   f"100 چھوٹے خانوں کا جال جس کی اوپر والی قطار میں {S6} خانے رنگے ہیں۔"),
 "s8_tenths": hundred_grid(S8,
   "A grid of 100 small squares in 10 rows of 10. 3 of the 10 rows are shaded, and it says 3/10 next to them.",
   "100 چھوٹے خانوں کا جال، 10 خانوں کی 10 قطاریں۔ 10 میں سے 3 قطاریں رنگی ہیں اور ان کے ساتھ 3/10 لکھا ہے۔",
   shaded_text="3/10"),
 "s11_mangoes": hundred_grid(100 - S11,
   f"A grid of 100 small squares, one for each mango. {100 - S11} squares are shaded and marked {100 - S11}: the bad mangoes. The rest, the good mangoes, are marked with a question mark.",
   f"100 چھوٹے خانوں کا جال، ہر آم کے لیے ایک خانہ۔ {100 - S11} خانے رنگے ہیں اور ان پر {100 - S11} لکھا ہے: یہ خراب آم ہیں۔ باقی خانوں پر، یعنی اچھے آموں پر، سوالیہ نشان ہے۔",
   shaded_text=str(100 - S11), rest_text="?"),
 "r_rest": hundred_grid(100 - R2,
   f"A grid of 100 small squares for the seats on the bus. {100 - R2} squares are shaded and marked {100 - R2}%: the seats that are taken. The empty seats are marked with a question mark.",
   f"بس کی نشستوں کے لیے 100 چھوٹے خانوں کا جال۔ {100 - R2} خانے رنگے ہیں اور ان پر {100 - R2}% لکھا ہے: یہ بھری نشستیں ہیں۔ خالی نشستوں پر سوالیہ نشان ہے۔",
   shaded_text=f"{100 - R2}%", rest_text="?"),
})
write(lesson)
