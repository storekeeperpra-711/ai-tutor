from figs import attach, scale_bar, strip
from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, FRACTIONS_MULTIPLY, PC_CONVERT, PC_OF_AMOUNT, percent_of)

SKILL = PC_OF_AMOUNT

# s2: 1/4 of 20
S2 = 20 // 4
assert S2 == 5
# s4: 10% of 300
S4 = percent_of(10, 300)
assert S4 == 30
# s5: 50% of 84
S5 = percent_of(50, 84)
assert S5 == 42
# s6: 25% of 200
S6 = percent_of(25, 200)
assert S6 == 50
# s7: 20% of Rs 500 = 2 x 10%
S7 = percent_of(20, 500)
assert S7 == 100 and S7 == 2 * percent_of(10, 500)
# s8: 15% of 60 = 10% + 5%
S8 = percent_of(15, 60)
assert S8 == 9 and S8 == percent_of(10, 60) + percent_of(5, 60)
# s9: 20% of 40 is 8, not 20
assert percent_of(20, 40) == 8
# s11: 75% of 40 children passed
S11 = percent_of(75, 40)
assert S11 == 30
# question bank and review
QB = percent_of(5, 80)
assert QB == 4
R1 = percent_of(10, 70)
assert R1 == 7
R2 = percent_of(25, 48)
assert R2 == 12

lesson = {
 "id": "g6-maths-11-percent-of-an-amount",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Find a percentage of an amount, using 10%, 50% and 25% as building blocks.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Percent of an amount", "کسی مقدار کا فیصد"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": PC_CONVERT}, {"skill": FRACTIONS_MULTIPLY}],
 "misconceptions": [
   {"id": "percent_as_answer", "description": "Gives the percent itself as the answer (20% of 40 = 20)."},
   {"id": "ten_percent_wrong", "description": "Finds 10% by taking away 10 instead of dividing by 10."},
   {"id": "rest_instead", "description": "Gives the amount left over instead of the percent asked for."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_ten", "type": "recall", "step": {
     "id": "qb_ten", "type": "choice",
     "prompt": T("What is the quickest way to find 10% of an amount?", "کسی مقدار کا 10% نکالنے کا سب سے آسان طریقہ کیا ہے؟"),
     "options": [
       opt("div10", "Divide it by 10", "اسے 10 سے تقسیم کریں", True,
           "Yes! 10% is one tenth.", "جی ہاں! 10% یعنی دسواں حصہ۔"),
       opt("minus10", "Take away 10", "10 نفی کریں", False,
           "10% is a tenth of the amount, so divide by 10.", "10% مقدار کا دسواں حصہ ہے، تو 10 سے تقسیم کریں۔", "ten_percent_wrong"),
       opt("times10", "Multiply it by 10", "اسے 10 سے ضرب دیں", False,
           "10% is smaller than the amount. Divide by 10.", "10% مقدار سے چھوٹا ہے۔ 10 سے تقسیم کریں۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("Find 5% of 80.", "80 کا 5% معلوم کریں۔"),
     QB,
     T("10% of 80 is 8. 5% is half of that.", "80 کا 10% یعنی 8۔ 5% اس کا آدھا ہے۔"),
     T("Right! 4.", "درست! 4"),
     T("10% = 8, so 5% = 4.", "10% = 8، تو 5% = 4"),
     common_wrong=[wrong(5, "5 is the percent. 5% of 80 is 4.", "5 فیصد ہے۔ 80 کا 5% یعنی 4", "percent_as_answer"),
                   wrong(8, "8 is 10%. 5% is half of it: 4.", "8 یعنی 10%۔ 5% اس کا آدھا ہے: 4")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Zara says 10% of 90 is 80, because 90 − 10 = 80. What went wrong?", "زارا کہتی ہے 90 کا 10% یعنی 80، کیونکہ 90 − 10 = 80۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("divide", "10% means divide by 10: 10% of 90 is 9.", "10% یعنی 10 سے تقسیم: 90 کا 10% یعنی 9", True,
           "Yes! 10% is a tenth, a small part of 90.", "جی ہاں! 10% دسواں حصہ ہے، 90 کا چھوٹا سا حصہ۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "80 is most of 90! 10% is one tenth: 9.", "80 تو 90 کا زیادہ تر حصہ ہے! 10% دسواں حصہ ہے: 9", "ten_percent_wrong"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_blocks", "front": T("Easy percents?", "آسان فیصد؟"),
    "back": T("50% = half. 25% = quarter. 10% = ÷ 10.", "50% = آدھا۔ 25% = چوتھائی۔ 10% = ÷ 10")},
   {"id": "f_build", "front": T("20% or 15%?", "20% یا 15%؟"),
    "back": T("20% = 10% × 2. 15% = 10% + 5%.", "20% = 10% × 2۔ 15% = 10% + 5%")},
 ],
 "home_tasks": [{"id": "h_sale", "text": T(
   "Ask someone at home the price of something you buy often, like a bag of flour or a bottle of oil. Work out 10% and 50% of that price. What would 20% off save?",
   "گھر میں کسی سے کوئی ایسی چیز کی قیمت پوچھیں جو اکثر خریدی جاتی ہے، جیسے آٹے کا تھیلا یا تیل کی بوتل۔ اس قیمت کا 10% اور 50% نکالیں۔ 20% رعایت سے کتنی بچت ہو گی؟")}],
 "glossary": [T("Percent of", "کا فیصد"), T("Discount", "رعایت"), T("Amount", "مقدار"), T("Tenth", "دسواں حصہ")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "The shop says 20% off a Rs 500 school bag. How much money do we save?",
                     "دکان پر لکھا ہے 500 روپے کے اسکول بیگ پر 20% رعایت۔ ہم کتنے پیسے بچائیں گے؟"),
    "text": T("Today we find a percent of an amount. First, a quick check on fractions.", "آج ہم کسی مقدار کا فیصد نکالیں گے۔ پہلے کسروں کا ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("What is 1/4 of 20?", "20 کا 1/4 کیا ہے؟"),
     S2,
     T("Divide 20 into 4 equal parts.", "20 کو 4 برابر حصوں میں بانٹیں۔"),
     T("Right! 5.", "درست! 5"),
     T("20 ÷ 4 = 5.", "20 ÷ 4 = 5"),
     common_wrong=[wrong(80, "That multiplies. A quarter of 20 is 20 ÷ 4 = 5.", "یہ ضرب ہے۔ 20 کا چوتھائی 20 ÷ 4 = 5")],
     qtype="recall", skill=FRACTIONS_MULTIPLY),
   {"id": "s3_blocks", "type": "explain",
    "character": say("happy", "Start with the easy ones, then build the rest from them!", "پہلے آسان والے نکالیں، پھر باقی انہی سے بنائیں!"),
    "text": T("Some percents are easy: 50% is half (÷ 2), 25% is a quarter (÷ 4), 10% is a tenth (÷ 10). Build others from these: 20% = 10% × 2, 5% = half of 10%, 15% = 10% + 5%. For any percent: divide the amount by 100, then multiply by the percent. For 20% of 500: 10% is 50, so 20% is 100.",
              "کچھ فیصد آسان ہیں: 50% آدھا (÷ 2)، 25% چوتھائی (÷ 4)، 10% دسواں حصہ (÷ 10)۔ باقی انہی سے بنائیں: 20% = 10% × 2، 5% = 10% کا آدھا، 15% = 10% + 5%۔ کسی بھی فیصد کے لیے: مقدار کو 100 سے تقسیم کریں، پھر فیصد سے ضرب دیں۔ 500 کا 20%: 10% یعنی 50، تو 20% یعنی 100۔")},
   number_question(
     "s4_ten",
     T("Find 10% of 300.", "300 کا 10% معلوم کریں۔"),
     S4,
     T("Divide by 10.", "10 سے تقسیم کریں۔"),
     T("Right! 30.", "درست! 30"),
     T("300 ÷ 10 = 30.", "300 ÷ 10 = 30"),
     common_wrong=[wrong(290, "10% is not 10 less. It is a tenth: 300 ÷ 10 = 30.", "10% یعنی 10 کم نہیں۔ یہ دسواں حصہ ہے: 300 ÷ 10 = 30", "ten_percent_wrong"),
                   wrong(10, "10 is the percent. 10% of 300 is 30.", "10 فیصد ہے۔ 300 کا 10% یعنی 30", "percent_as_answer")]),
   number_question(
     "s5_half",
     T("Find 50% of 84.", "84 کا 50% معلوم کریں۔"),
     S5,
     T("50% is half.", "50% یعنی آدھا۔"),
     T("Right! 42.", "درست! 42"),
     T("Half of 84 is 42.", "84 کا آدھا 42 ہے۔"),
     common_wrong=[wrong(34, "50% is not 50 less. It is half: 42.", "50% یعنی 50 کم نہیں۔ یہ آدھا ہے: 42"),
                   wrong(50, "50 is the percent. Half of 84 is 42.", "50 فیصد ہے۔ 84 کا آدھا 42 ہے۔", "percent_as_answer")]),
   number_question(
     "s6_quarter",
     T("Find 25% of 200.", "200 کا 25% معلوم کریں۔"),
     S6,
     T("25% is a quarter: divide by 4.", "25% یعنی چوتھائی: 4 سے تقسیم کریں۔"),
     T("Right! 50.", "درست! 50"),
     T("200 ÷ 4 = 50.", "200 ÷ 4 = 50"),
     common_wrong=[wrong(25, "25 is the percent. A quarter of 200 is 50.", "25 فیصد ہے۔ 200 کا چوتھائی 50 ہے۔", "percent_as_answer"),
                   wrong(150, "150 is what is left (75%). 25% is 50.", "150 باقی ہے (75%)۔ 25% یعنی 50", "rest_instead")]),
   number_question(
     "s7_bag",
     T("A school bag costs Rs 500. The shop gives 20% off. How many rupees do you save?", "اسکول بیگ 500 روپے کا ہے۔ دکان 20% رعایت دیتی ہے۔ آپ کتنے روپے بچاتے ہیں؟"),
     S7,
     T("10% of 500 is 50. 20% is twice that.", "500 کا 10% یعنی 50۔ 20% اس کا دگنا ہے۔"),
     T("Right! You save Rs 100.", "درست! آپ 100 روپے بچاتے ہیں۔"),
     T("10% = 50, so 20% = 100.", "10% = 50، تو 20% = 100"),
     common_wrong=[wrong(400, "Rs 400 is the new price. The saving is 20%: Rs 100.", "400 روپے نئی قیمت ہے۔ بچت 20% ہے: 100 روپے", "rest_instead"),
                   wrong(50, "Rs 50 is 10%. 20% is twice that: Rs 100.", "50 روپے یعنی 10%۔ 20% اس کا دگنا ہے: 100 روپے")]),
   number_question(
     "s8_fifteen",
     T("Find 15% of 60.", "60 کا 15% معلوم کریں۔"),
     S8,
     T("10% of 60 is 6, and 5% is half of that.", "60 کا 10% یعنی 6، اور 5% اس کا آدھا۔"),
     T("Right! 6 + 3 = 9.", "درست! 6 + 3 = 9"),
     T("10% = 6, 5% = 3, so 15% = 9.", "10% = 6، 5% = 3، تو 15% = 9"),
     common_wrong=[wrong(15, "15 is the percent. 15% of 60 is 6 + 3 = 9.", "15 فیصد ہے۔ 60 کا 15% یعنی 6 + 3 = 9", "percent_as_answer"),
                   wrong(6, "6 is only 10%. Add 5% (3): 9.", "6 صرف 10% ہے۔ 5% (3) جمع کریں: 9")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Hamza says 20% of 40 is 20. What went wrong?", "حمزہ کہتا ہے 40 کا 20% یعنی 20۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("eight", "He just used the 20. 10% of 40 is 4, so 20% is 8.", "اس نے بس 20 لکھ دیا۔ 40 کا 10% یعنی 4، تو 20% یعنی 8", True,
          "Yes! 20 would be half of 40, which is 50%.", "جی ہاں! 20 تو 40 کا آدھا ہے، یعنی 50%۔"),
      opt("twenty_two", "It should be 40 − 20 = 20 anyway.", "ویسے بھی 40 − 20 = 20 ہے۔", False,
          "Taking away 20 isn't finding 20%. 20% of 40 is 8.", "20 نفی کرنا 20% نکالنا نہیں ہے۔ 40 کا 20% یعنی 8"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "20 is half of 40, which is 50%. 20% of 40 is 8.", "20 تو 40 کا آدھا ہے، یعنی 50%۔ 40 کا 20% یعنی 8", "percent_as_answer"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why does dividing by 10 give 10% of an amount? Can you teach me?",
                     "10 سے تقسیم کرنے سے مقدار کا 10% کیوں ملتا ہے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why is 10% of an amount the same as the amount divided by 10?", "اپنے الفاظ میں بتائیں: کسی مقدار کا 10% اسے 10 سے تقسیم کرنے کے برابر کیوں ہے؟"),
    "key_idea": "10% means 10 out of 100, which is 1/10. Finding one tenth of something means cutting it into 10 equal parts and taking one, which is dividing by 10.",
    "levels": {
      "got_it": "Says 10% is 10 out of 100 = one tenth, and a tenth means dividing into 10 equal parts.",
      "partly": "Says 10% is a tenth, without linking it to dividing.",
      "not_yet": "Gives no reason, or just repeats the rule."},
    "keywords": [
      ["tenth", "1/10", "دسواں"],
      ["10 out of 100", "out of 100", "100 میں سے"],
      ["equal parts", "parts", "برابر", "حصے"]],
    "fallback_feedback": {
      "got_it": T("Well explained! 10% is one tenth, so we divide by 10.", "بہت خوب! 10% دسواں حصہ ہے، اس لیے 10 سے تقسیم کرتے ہیں۔"),
      "partly": T("Good start! Now say how a tenth is linked to dividing by 10.", "اچھی شروعات! اب بتائیں دسواں حصہ 10 سے تقسیم سے کیسے جڑا ہے۔"),
      "not_yet": T("Write 10% as a fraction: 10/100. What does that simplify to?", "10% کو کسر میں لکھیں: 10/100۔ یہ سادہ ہو کر کیا بنتا ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_class",
     T("A class has 40 children. 75% of them passed the test. How many children passed?", "ایک کلاس میں 40 بچے ہیں۔ ان میں سے 75% ٹیسٹ میں پاس ہوئے۔ کتنے بچے پاس ہوئے؟"),
     S11,
     T("75% is three quarters. A quarter of 40 is 10.", "75% یعنی تین چوتھائی۔ 40 کا چوتھائی 10 ہے۔"),
     T("Right! 30 children passed.", "درست! 30 بچے پاس ہوئے۔"),
     T("A quarter is 10, so three quarters is 30.", "چوتھائی 10، تو تین چوتھائی 30"),
     common_wrong=[wrong(10, "10 is 25%, the children who did not pass. 75% is 30.", "10 یعنی 25%، جو پاس نہیں ہوئے۔ 75% یعنی 30", "rest_instead"),
                   wrong(75, "There are only 40 children! 75% of 40 is 30.", "بچے تو صرف 40 ہیں! 40 کا 75% یعنی 30", "percent_as_answer")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "You can work out sale prices now!", "اب آپ سیل کی قیمتیں نکال سکتے ہیں!"),
    "text": T("To find a percent of an amount, use the easy ones: 50% = half, 25% = quarter, 10% = divide by 10. Build the rest: 20% = 2 × 10%, 5% = half of 10%, 75% = 3 × 25%. Or divide by 100 and multiply by the percent.",
              "کسی مقدار کا فیصد نکالنے کے لیے آسان والے استعمال کریں: 50% = آدھا، 25% = چوتھائی، 10% = 10 سے تقسیم۔ باقی بنائیں: 20% = 2 × 10%، 5% = 10% کا آدھا، 75% = 3 × 25%۔ یا 100 سے تقسیم کر کے فیصد سے ضرب دیں۔"),
    "points": [T("10% = amount ÷ 10.", "10% = مقدار ÷ 10۔"),
               T("Build other percents from 10%, 25% and 50%.", "باقی فیصد 10%، 25% اور 50% سے بنائیں۔")]},
 ],
 "review_questions": [
   {"id": "r_ten", "type": "apply", "skill": SKILL, "step": number_question(
     "r_ten",
     T("Find 10% of 70.", "70 کا 10% معلوم کریں۔"),
     R1,
     T("Divide by 10.", "10 سے تقسیم کریں۔"),
     T("Right! 7.", "درست! 7"),
     T("70 ÷ 10 = 7.", "70 ÷ 10 = 7"),
     common_wrong=[wrong(60, "10% is a tenth, not 10 less: 7.", "10% دسواں حصہ ہے، 10 کم نہیں: 7", "ten_percent_wrong")],
     qtype=None)},
   {"id": "r_quarter", "type": "apply", "skill": SKILL, "step": number_question(
     "r_quarter",
     T("Find 25% of 48.", "48 کا 25% معلوم کریں۔"),
     R2,
     T("A quarter: divide by 4.", "چوتھائی: 4 سے تقسیم کریں۔"),
     T("Right! 12.", "درست! 12"),
     T("48 ÷ 4 = 12.", "48 ÷ 4 = 12"),
     common_wrong=[wrong(25, "25 is the percent. A quarter of 48 is 12.", "25 فیصد ہے۔ 48 کا چوتھائی 12 ہے۔", "percent_as_answer")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Percentages unit. No textbook text or exercises were used.",
   "Children build percents from 10%, 25% and 50% (mental strategy) before the general rule of dividing by 100.",
   "Urdu terms to check: رعایت (discount), دسواں حصہ (tenth).",
   "The numbers were worked out in content/sources/g6-maths-11/percent_of_amount.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}


def part_of(p, amount, parts, *, rs=False):
    """A percentage bar: a bar for `amount` cut into `parts` equal parts with
    p% shaded. Above it the amounts 0, "?" and the whole amount; below it
    0%, p% and 100%. Its alt text in both languages."""
    shaded = p * parts // 100
    assert shaded * 100 == p * parts
    whole = f"Rs{amount}" if rs else str(amount)
    rupees = ("Rs " if rs else "", " روپے" if rs else "")
    en = (f"A bar for the whole amount, {rupees[0]}{amount}, cut into {parts} equal parts, with {shaded} of them shaded. "
          f"Above the bar: 0 at the start, a question mark at the end of the shading, and {rupees[0]}{amount} at the end. "
          f"Below the bar: 0%, {p}% under the question mark, and 100% under {amount}.")
    ur = (f"پوری رقم {amount}{rupees[1]} کے لیے ایک پٹی جو {parts} برابر حصوں میں بٹی ہے، ان میں سے {shaded} رنگے ہیں۔ "
          f"پٹی کے اوپر: شروع میں 0، رنگ کے آخر میں سوالیہ نشان، اور آخر میں {amount}{rupees[1]}۔ "
          f"پٹی کے نیچے: 0%، سوالیہ نشان کے نیچے {p}%، اور {amount} کے نیچے 100%۔")
    f = p / 100
    return scale_bar(f, [(0, "0"), (f, "?"), (1, whole)], [(0, "0%"), (f, f"{p}%"), (1, "100%")], en, ur, pieces=parts)


# Pictures: strip (bar) models, the whole amount above, the percents under.
assert S7 == 2 * 500 / 10
attach(lesson, {
 "s2_foundation": scale_bar(0.25, [(0, "0"), (0.25, "?"), (1, "20")], [(0, "0"), (0.25, "1/4"), (1, "1")],
   "A bar for 20 cut into 4 equal parts, the first part shaded. Above the bar: 0, a question mark at the end of the shading, and 20 at the end. Below the bar: 0, 1/4 under the question mark, and 1 at the end.",
   "20 کے لیے ایک پٹی جو 4 برابر حصوں میں بٹی ہے، پہلا حصہ رنگا ہے۔ پٹی کے اوپر: 0، رنگ کے آخر میں سوالیہ نشان، اور آخر میں 20۔ پٹی کے نیچے: 0، سوالیہ نشان کے نیچے 1/4، اور آخر میں 1۔",
   pieces=4),
 "s3_blocks": strip("500", 10, 2,
   "A strip for 500 cut into 10 equal parts, with 50 written in each part. The first 2 parts are shaded. Under the strip: 0% at the start, 10% after one part, 20% after two parts, and 100% at the end.",
   "500 کے لیے ایک پٹی جو 10 برابر حصوں میں بٹی ہے، ہر حصے میں 50 لکھا ہے۔ پہلے 2 حصے رنگے ہیں۔ پٹی کے نیچے: شروع میں 0%، ایک حصے کے بعد 10%، دو حصوں کے بعد 20%، اور آخر میں 100%۔",
   ask=None, inside=str(500 // 10), under=[(0, "0%"), (0.1, "10%"), (0.2, "20%"), (1, "100%")]),
 "s4_ten": part_of(10, 300, 10),
 "s5_half": part_of(50, 84, 2),
 "s6_quarter": part_of(25, 200, 4),
 "s7_bag": part_of(20, 500, 10, rs=True),
 "s8_fifteen": part_of(15, 60, 20),
 "s9_find_error": part_of(20, 40, 10),
 "s11_class": part_of(75, 40, 4),
 "qb_apply": part_of(5, 80, 20),
 "r_quarter": part_of(25, 48, 4),
})
write(lesson)
