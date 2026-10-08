from math import gcd

from figs import attach, percent_bar
from common import (D, T, opt, say, wrong, number_question, write,
                    REF, REVIEW, PC_CONVERT, PC_OF_AMOUNT, PC_FIND, as_percent)

SKILL = PC_FIND

# s2: 0.9 -> 90%
S2 = D("0.9") * 100
assert S2 == 90
# s4: 18 marks out of 20
S4 = as_percent(18, 20)
assert S4 == 90
# s5: 12 out of 50
S5 = as_percent(12, 50)
assert S5 == 24
# s6: 7 of 25 children absent
S6 = as_percent(7, 25)
assert S6 == 28
# s7: Rs 30 saved out of Rs 200
S7 = as_percent(30, 200)
assert S7 == 15
# s8: 45 out of 60
S8 = as_percent(45, 60)
assert S8 == 75
# s9: 15 out of 30 is 50%, not 15%
assert as_percent(15, 30) == 50
# s11: 6 bad mangoes out of 40
S11 = as_percent(6, 40)
assert S11 == 15
# question bank and review
QB = as_percent(9, 10)
assert QB == 90
R1 = as_percent(3, 4)
assert R1 == 75
R2 = as_percent(16, 80)
assert R2 == 20

lesson = {
 "id": "g6-maths-11-finding-the-percentage",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Write one amount as a percentage of another, such as test marks out of 20 as a percent.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Finding the percentage", "فیصد معلوم کرنا"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": PC_OF_AMOUNT}, {"skill": PC_CONVERT}],
 "misconceptions": [
   {"id": "part_as_percent", "description": "Gives the part itself as the percent (15 out of 30 = 15%)."},
   {"id": "upside_down", "description": "Divides the whole by the part instead of the part by the whole."},
   {"id": "forgets_100", "description": "Stops at the fraction or decimal and forgets to multiply by 100 (0.9 instead of 90%)."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_rule", "type": "recall", "step": {
     "id": "qb_rule", "type": "choice",
     "prompt": T("How do you find what percent 6 is of 24?", "6، 24 کا کتنے فیصد ہے، یہ کیسے معلوم کرتے ہیں؟"),
     "options": [
       opt("part_whole", "Work out 6/24, then multiply by 100", "6/24 نکالیں، پھر 100 سے ضرب دیں", True,
           "Yes! 6/24 = 1/4 = 25%.", "جی ہاں! 6/24 = 1/4 = 25%"),
       opt("whole_part", "Work out 24/6, then multiply by 100", "24/6 نکالیں، پھر 100 سے ضرب دیں", False,
           "That's upside down. Part over whole: 6/24.", "یہ الٹا ہے۔ حصہ اوپر، کل نیچے: 6/24", "upside_down"),
       opt("just_six", "It is 6%", "یہ 6% ہے", False,
           "6% means 6 out of 100. Here it's 6 out of 24: 25%.", "6% یعنی 100 میں سے 6۔ یہاں 24 میں سے 6 ہے: 25%", "part_as_percent"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("Bilal gets 9 out of 10 in a quiz. What percent is that? Type just the number.", "بلال کوئز میں 10 میں سے 9 لیتا ہے۔ یہ کتنے فیصد ہے؟ صرف عدد لکھیں۔"),
     QB,
     T("9/10 = ?/100", "9/10 = ?/100"),
     T("Right! 90%.", "درست! 90%"),
     T("9/10 = 90/100 = 90%.", "9/10 = 90/100 = 90%"),
     common_wrong=[wrong(9, "9 out of 10 is not 9%. 9/10 = 90/100 = 90%.", "10 میں سے 9، 9% نہیں ہے۔ 9/10 = 90/100 = 90%", "part_as_percent"),
                   wrong(D("0.9"), "0.9 is the decimal. Multiply by 100: 90%.", "0.9 اعشاریہ ہے۔ 100 سے ضرب دیں: 90%", "forgets_100")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Out of 50 seeds, 40 grow. Mehwish works out 50 ÷ 40 × 100 = 125%. What went wrong?", "50 بیجوں میں سے 40 اگتے ہیں۔ مہوش 50 ÷ 40 × 100 = 125% نکالتی ہے۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("flip", "It should be part ÷ whole: 40 ÷ 50 × 100 = 80%.", "حصہ ÷ کل ہونا چاہیے: 40 ÷ 50 × 100 = 80%", True,
           "Yes! Only some seeds grew, so it must be less than 100%.", "جی ہاں! کچھ ہی بیج اگے، تو یہ 100% سے کم ہونا چاہیے۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "More than 100% would mean more seeds grew than were planted! 40 ÷ 50 × 100 = 80%.", "100% سے زیادہ کا مطلب ہوتا کہ بوئے گئے سے زیادہ بیج اگے! 40 ÷ 50 × 100 = 80%", "upside_down"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_rule", "front": T("What percent is the part of the whole?", "حصہ کل کا کتنے فیصد ہے؟"),
    "back": T("Part ÷ whole × 100. 18 out of 20: 18 ÷ 20 × 100 = 90%.", "حصہ ÷ کل × 100۔ 20 میں سے 18: 18 ÷ 20 × 100 = 90%")},
   {"id": "f_check", "front": T("Quick check?", "فوری جانچ؟"),
    "back": T("A part of the whole is never more than 100%.", "کل کا حصہ کبھی 100% سے زیادہ نہیں ہوتا۔")},
 ],
 "home_tasks": [{"id": "h_marks", "text": T(
   "Look at a recent test or homework mark, like 14 out of 20. Work out the percentage. Then ask someone at home what mark out of 20 would make 100%.",
   "کسی حالیہ ٹیسٹ یا کام کے نمبر دیکھیں، جیسے 20 میں سے 14۔ اس کا فیصد نکالیں۔ پھر گھر میں کسی سے پوچھیں 20 میں سے کتنے نمبر 100% بناتے ہیں۔")}],
 "glossary": [T("Percentage", "فیصد"), T("Part", "حصہ"), T("Whole", "کل"), T("Marks", "نمبر")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Ayesha got 18 out of 20 in maths. Her report card asks for a percentage. What should she write?",
                     "عائشہ نے ریاضی میں 20 میں سے 18 لیے۔ رپورٹ کارڈ میں فیصد لکھنا ہے۔ وہ کیا لکھے؟"),
    "text": T("Today we find what percent one amount is of another. First, a quick check.", "آج ہم معلوم کریں گے کہ ایک مقدار دوسری کا کتنے فیصد ہے۔ پہلے ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("Write 0.9 as a percent. Type just the number.", "0.9 کو فیصد میں لکھیں۔ صرف عدد لکھیں۔"),
     S2,
     T("Multiply by 100.", "100 سے ضرب دیں۔"),
     T("Right! 0.9 = 90%.", "درست! 0.9 = 90%"),
     T("0.9 × 100 = 90.", "0.9 × 100 = 90"),
     common_wrong=[wrong(9, "Multiply by 100, not 10: 90%.", "10 نہیں، 100 سے ضرب دیں: 90%")],
     qtype="recall", skill=PC_CONVERT),
   {"id": "s3_find", "type": "explain",
    "character": say("happy", "Write it as a fraction, then turn the fraction into a percent!", "اسے کسر لکھیں، پھر کسر کو فیصد بنائیں!"),
    "text": T("To find what percent a part is of a whole: write part/whole, then multiply by 100. 18 out of 20 is 18/20. Make the bottom 100: 18/20 = 90/100 = 90%. Or work out 18 ÷ 20 = 0.9, and 0.9 × 100 = 90%. The part goes on top. A part of something is never more than 100%.",
              "یہ معلوم کرنے کے لیے کہ حصہ کل کا کتنے فیصد ہے: حصہ/کل لکھیں، پھر 100 سے ضرب دیں۔ 20 میں سے 18 یعنی 18/20۔ نیچے والا 100 بنائیں: 18/20 = 90/100 = 90%۔ یا 18 ÷ 20 = 0.9، اور 0.9 × 100 = 90%۔ حصہ اوپر آتا ہے۔ کسی چیز کا حصہ کبھی 100% سے زیادہ نہیں ہوتا۔")},
   number_question(
     "s4_marks",
     T("Ayesha got 18 out of 20. What percent is that? Type just the number.", "عائشہ نے 20 میں سے 18 لیے۔ یہ کتنے فیصد ہے؟ صرف عدد لکھیں۔"),
     S4,
     T("18/20 = ?/100. Multiply top and bottom by 5.", "18/20 = ?/100۔ اوپر اور نیچے کو 5 سے ضرب دیں۔"),
     T("Right! 90%.", "درست! 90%"),
     T("18/20 = 90/100 = 90%.", "18/20 = 90/100 = 90%"),
     common_wrong=[wrong(18, "18 out of 20 is not 18%. 18/20 = 90/100 = 90%.", "20 میں سے 18، 18% نہیں ہے۔ 18/20 = 90/100 = 90%", "part_as_percent"),
                   wrong(D("0.9"), "0.9 is the decimal. Multiply by 100: 90%.", "0.9 اعشاریہ ہے۔ 100 سے ضرب دیں: 90%", "forgets_100")]),
   number_question(
     "s5_fifty",
     T("12 out of 50 children in a school play hockey. What percent is that? Type just the number.", "ایک اسکول کے 50 میں سے 12 بچے ہاکی کھیلتے ہیں۔ یہ کتنے فیصد ہے؟ صرف عدد لکھیں۔"),
     S5,
     T("12/50 = ?/100. Multiply top and bottom by 2.", "12/50 = ?/100۔ اوپر اور نیچے کو 2 سے ضرب دیں۔"),
     T("Right! 24%.", "درست! 24%"),
     T("12/50 = 24/100 = 24%.", "12/50 = 24/100 = 24%"),
     common_wrong=[wrong(12, "Make the bottom 100: 12/50 = 24/100 = 24%.", "نیچے والا 100 بنائیں: 12/50 = 24/100 = 24%", "part_as_percent")]),
   number_question(
     "s6_absent",
     T("7 of the 25 children in a class are absent. What percent are absent? Type just the number.", "ایک کلاس کے 25 میں سے 7 بچے غیر حاضر ہیں۔ کتنے فیصد غیر حاضر ہیں؟ صرف عدد لکھیں۔"),
     S6,
     T("7/25 = ?/100. Multiply top and bottom by 4.", "7/25 = ?/100۔ اوپر اور نیچے کو 4 سے ضرب دیں۔"),
     T("Right! 28%.", "درست! 28%"),
     T("7/25 = 28/100 = 28%.", "7/25 = 28/100 = 28%"),
     common_wrong=[wrong(7, "Make the bottom 100: 7/25 = 28/100 = 28%.", "نیچے والا 100 بنائیں: 7/25 = 28/100 = 28%", "part_as_percent"),
                   wrong(72, "72% are present. Absent: 7/25 = 28%.", "72% حاضر ہیں۔ غیر حاضر: 7/25 = 28%")]),
   number_question(
     "s7_saved",
     T("Usman had Rs 200 and saved Rs 30. What percent of his money did he save? Type just the number.", "عثمان کے پاس 200 روپے تھے اور اس نے 30 روپے بچائے۔ اس نے اپنے پیسوں کا کتنے فیصد بچایا؟ صرف عدد لکھیں۔"),
     S7,
     T("30/200 = ?/100. Divide top and bottom by 2.", "30/200 = ?/100۔ اوپر اور نیچے کو 2 سے تقسیم کریں۔"),
     T("Right! 15%.", "درست! 15%"),
     T("30/200 = 15/100 = 15%.", "30/200 = 15/100 = 15%"),
     common_wrong=[wrong(30, "Rs 30 out of Rs 200 is not 30%. 30/200 = 15/100 = 15%.", "200 میں سے 30 روپے، 30% نہیں ہیں۔ 30/200 = 15/100 = 15%", "part_as_percent")]),
   number_question(
     "s8_sixty",
     T("A bus has 60 seats. 45 are taken. What percent of the seats are taken? Type just the number.", "ایک بس میں 60 نشستیں ہیں۔ 45 بھری ہیں۔ کتنے فیصد نشستیں بھری ہیں؟ صرف عدد لکھیں۔"),
     S8,
     T("Simplify 45/60 first: divide top and bottom by 15.", "پہلے 45/60 کو سادہ کریں: اوپر اور نیچے کو 15 سے تقسیم کریں۔"),
     T("Right! 45/60 = 3/4 = 75%.", "درست! 45/60 = 3/4 = 75%"),
     T("45/60 = 3/4 = 75/100 = 75%.", "45/60 = 3/4 = 75/100 = 75%"),
     common_wrong=[wrong(45, "Make it out of 100: 45/60 = 3/4 = 75%.", "اسے 100 میں سے بنائیں: 45/60 = 3/4 = 75%", "part_as_percent"),
                   wrong(25, "25% of seats are empty. Taken: 3/4 = 75%.", "25% نشستیں خالی ہیں۔ بھری: 3/4 = 75%")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Rashid scores 15 out of 30 and says he got 15%. What went wrong?", "راشد 30 میں سے 15 لیتا ہے اور کہتا ہے اس کے 15% ہیں۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("half", "15 out of 30 is half, which is 50%.", "30 میں سے 15 آدھا ہے، جو 50% ہے۔", True,
          "Yes! 15/30 = 1/2 = 50%.", "جی ہاں! 15/30 = 1/2 = 50%"),
      opt("thirty", "It should be 30%.", "یہ 30% ہونا چاہیے۔", False,
          "15/30 = 1/2, and a half is 50%.", "15/30 = 1/2، اور آدھا 50% ہے۔"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "15% is 15 out of 100. He got 15 out of 30: 50%.", "15% یعنی 100 میں سے 15۔ اس کے 30 میں سے 15 ہیں: 50%", "part_as_percent"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why do we multiply part ÷ whole by 100 to get a percent? Can you teach me?",
                     "فیصد نکالنے کے لیے حصہ ÷ کل کو 100 سے ضرب کیوں دیتے ہیں؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why is 18 out of 20 the same as 90%?", "اپنے الفاظ میں بتائیں: 20 میں سے 18، 90% کے برابر کیوں ہے؟"),
    "key_idea": "A percent is out of 100. 18 out of 20 is the fraction 18/20. Changing it to an equal fraction with 100 at the bottom (90/100), or multiplying by 100, tells us how many there would be out of 100.",
    "levels": {
      "got_it": "Says percent means out of 100, and 18/20 becomes 90/100 (or 0.9 × 100) to show how many out of 100.",
      "partly": "Says multiply by 100 or make it out of 100, without explaining the link.",
      "not_yet": "Gives no reason, or just repeats the rule."},
    "keywords": [
      ["100", "hundred", "سو"],
      ["fraction", "18/20", "90/100", "کسر"],
      ["equal", "same", "برابر", "ایک جیسا"]],
    "fallback_feedback": {
      "got_it": T("Well explained! 18 out of 20 is the same as 90 out of 100.", "بہت خوب! 20 میں سے 18، 100 میں سے 90 کے برابر ہے۔"),
      "partly": T("Good start! Now say how 18/20 turns into a number out of 100.", "اچھی شروعات! اب بتائیں 18/20 کیسے 100 میں سے عدد بنتا ہے۔"),
      "not_yet": T("Percent means out of 100. If 20 marks became 100 marks, how many would 18 marks become?", "فیصد یعنی 100 میں سے۔ اگر 20 نمبر 100 نمبر بن جائیں تو 18 نمبر کتنے بنیں گے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_mangoes",
     T("A crate has 40 mangoes. 6 are bad. What percent of the mangoes are bad? Type just the number.", "ایک پیٹی میں 40 آم ہیں۔ 6 خراب ہیں۔ کتنے فیصد آم خراب ہیں؟ صرف عدد لکھیں۔"),
     S11,
     T("6 ÷ 40, then × 100.", "6 ÷ 40، پھر × 100"),
     T("Right! 15% are bad.", "درست! 15% خراب ہیں۔"),
     T("6 ÷ 40 = 0.15, and 0.15 × 100 = 15.", "6 ÷ 40 = 0.15، اور 0.15 × 100 = 15"),
     common_wrong=[wrong(6, "6 out of 40 is not 6%. 6 ÷ 40 × 100 = 15%.", "40 میں سے 6، 6% نہیں ہے۔ 6 ÷ 40 × 100 = 15%", "part_as_percent"),
                   wrong(85, "85% are good. Bad: 6 ÷ 40 × 100 = 15%.", "85% اچھے ہیں۔ خراب: 6 ÷ 40 × 100 = 15%")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Now you can work out your own test percentages!", "اب آپ اپنے ٹیسٹ کا فیصد خود نکال سکتے ہیں!"),
    "text": T("To find what percent a part is of a whole: part ÷ whole × 100. Or write part/whole and make the bottom 100. The part goes on top, and a part of something is never more than 100%.",
              "یہ معلوم کرنے کے لیے کہ حصہ کل کا کتنے فیصد ہے: حصہ ÷ کل × 100۔ یا حصہ/کل لکھ کر نیچے والا 100 بنائیں۔ حصہ اوپر آتا ہے، اور کسی چیز کا حصہ کبھی 100% سے زیادہ نہیں ہوتا۔"),
    "points": [T("Percent = part ÷ whole × 100.", "فیصد = حصہ ÷ کل × 100۔"),
               T("Part on top, whole underneath.", "حصہ اوپر، کل نیچے۔")]},
 ],
 "review_questions": [
   {"id": "r_quarter", "type": "apply", "skill": SKILL, "step": number_question(
     "r_quarter",
     T("What percent is 3 out of 4? Type just the number.", "4 میں سے 3 کتنے فیصد ہے؟ صرف عدد لکھیں۔"),
     R1,
     T("3/4 = ?/100", "3/4 = ?/100"),
     T("Right! 75%.", "درست! 75%"),
     T("3/4 = 75/100 = 75%.", "3/4 = 75/100 = 75%"),
     common_wrong=[wrong(3, "3 out of 4 is not 3%. 3/4 = 75%.", "4 میں سے 3، 3% نہیں ہے۔ 3/4 = 75%", "part_as_percent")],
     qtype=None)},
   {"id": "r_eighty", "type": "apply", "skill": SKILL, "step": number_question(
     "r_eighty",
     T("What percent is 16 out of 80? Type just the number.", "80 میں سے 16 کتنے فیصد ہے؟ صرف عدد لکھیں۔"),
     R2,
     T("Simplify 16/80 first.", "پہلے 16/80 کو سادہ کریں۔"),
     T("Right! 16/80 = 1/5 = 20%.", "درست! 16/80 = 1/5 = 20%"),
     T("16/80 = 1/5 = 20/100 = 20%.", "16/80 = 1/5 = 20/100 = 20%"),
     common_wrong=[wrong(500, "That's upside down: 80 ÷ 16. Part ÷ whole: 16/80 = 20%.", "یہ الٹا ہے: 80 ÷ 16۔ حصہ ÷ کل: 16/80 = 20%", "upside_down")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Percentages unit. No textbook text or exercises were used.",
   "Two methods are shown: make the bottom 100, or part ÷ whole × 100. Every answer is a whole-number percent.",
   "Urdu terms to check: فیصد (percentage), حصہ (part), کل (whole).",
   "The numbers were worked out in content/sources/g6-maths-11/finding_the_percentage.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}


def bar_of(part, whole, pct=None, *, rs=False):
    """A percentage bar for part out of whole: amounts above, percents below,
    the part's percent shown as pct or as a question mark."""
    pieces = whole // gcd(part, whole)
    cut = (f" cut into {pieces} equal pieces", f" جو {pieces} برابر ٹکڑوں میں بٹی ہے") if pieces <= 25 else ("", "")
    rs_en, rs_ur = ("Rs ", " روپے") if rs else ("", "")
    shown_en = pct if pct else "a question mark"
    shown_ur = pct if pct else "سوالیہ نشان"
    en = (f"A bar for the whole, {rs_en}{whole},{cut[0]}, shaded from the start up to {rs_en}{part}. "
          f"Above the bar: 0, {part} at the end of the shading, and {whole} at the end. "
          f"Below the bar: 0%, {shown_en} under {part}, and 100% under {whole}.")
    ur = (f"پورے {whole}{rs_ur} کے لیے ایک پٹی{cut[1]}، شروع سے {part}{rs_ur} تک رنگی ہوئی۔ "
          f"پٹی کے اوپر: 0، رنگ کے آخر میں {part}، اور آخر میں {whole}۔ "
          f"پٹی کے نیچے: 0%، {part} کے نیچے {shown_ur}، اور {whole} کے نیچے 100%۔")
    return percent_bar(part, whole, en, ur, bottom=pct or "?")


# Pictures: percentage bars, the amounts above and 0% to 100% below.
attach(lesson, {
 "s3_find": bar_of(18, 20, f"{S4}%"),
 "s4_marks": bar_of(18, 20),
 "s5_fifty": bar_of(12, 50),
 "s6_absent": bar_of(7, 25),
 "s7_saved": bar_of(30, 200, rs=True),
 "s8_sixty": bar_of(45, 60),
 "s11_mangoes": bar_of(6, 40),
 "qb_find_error": bar_of(40, 50),
 "r_eighty": bar_of(16, 80),
})
write(lesson)
