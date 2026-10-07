from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, TIMES_TABLES, WN_PLACE_VALUE, LAKH, CRORE, pk)

SKILL = WN_PLACE_VALUE

# s2: 10 x 10 x 10
S2 = 10 * 10 * 10
assert S2 == 1000
# s4: value of 6 in 6,40,000 (6 lakh; 6 ten thousands would be 60,000)
S4_NUM = 640000
S4 = 6 * LAKH
assert pk(S4_NUM) == "6,40,000" and S4 == 600000
# s5: thousands in a lakh
S5 = LAKH // 1000
assert S5 == 100
# s6: 1 crore written with commas
assert pk(CRORE) == "1,00,00,000" and pk(10 * LAKH) == "10,00,000"
# s7: three lakh twenty-five thousand
S7 = 3 * LAKH + 25 * 1000
assert S7 == 325000 and pk(S7) == "3,25,000"
# s8: lakhs in a crore
S8 = CRORE // LAKH
assert S8 == 100
# s9: 45,00,000 is forty-five lakh
assert pk(45 * LAKH) == "45,00,000"
# s11: Rs 5,00,000 in Rs 1000 notes
S11 = 5 * LAKH // 1000
assert S11 == 500
# question bank and review
QB_NUM = 82000000
QB = 8 * CRORE
assert pk(QB_NUM) == "8,20,00,000" and QB == 80000000
assert pk(250000) == "2,50,000"
R1_NUM = 450000
R1 = 4 * LAKH
assert pk(R1_NUM) == "4,50,000" and R1 == 400000
R2 = LAKH // 10000
assert R2 == 10

lesson = {
 "id": "g6-maths-15-lakhs-and-crores",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Read, write and find the place value of digits in numbers up to crores, using Pakistani commas.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Lakhs and crores", "لاکھ اور کروڑ"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": TIMES_TABLES}],
 "misconceptions": [
   {"id": "digit_not_value", "description": "Gives the digit itself, or the wrong place, instead of its value."},
   {"id": "lakh_ten_thousand", "description": "Thinks 1 lakh is 10,000 or 10 thousands."},
   {"id": "crore_ten_lakh", "description": "Thinks 1 crore is 10 lakh."},
   {"id": "lost_zero", "description": "Drops a zero when writing a number from words."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_zeros", "type": "recall", "step": {
     "id": "qb_zeros", "type": "choice",
     "prompt": T("How many zeros are in 1 lakh?", "1 لاکھ میں کتنے صفر ہیں؟"),
     "options": [
       opt("five", "5 (1,00,000)", "5 (1,00,000)", True,
           "Yes! 1 lakh = 1,00,000.", "جی ہاں! 1 لاکھ = 1,00,000"),
       opt("four", "4 (10,000)", "4 (10,000)", False,
           "10,000 is ten thousand. 1 lakh is 1,00,000: 5 zeros.", "10,000 دس ہزار ہے۔ 1 لاکھ 1,00,000 ہے: 5 صفر۔", "lakh_ten_thousand"),
       opt("seven", "7 (1,00,00,000)", "7 (1,00,00,000)", False,
           "That is 1 crore. 1 lakh has 5 zeros.", "یہ 1 کروڑ ہے۔ 1 لاکھ میں 5 صفر ہیں۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T(f"What is the value of the digit 8 in {pk(QB_NUM)}?", f"{pk(QB_NUM)} میں 8 کی مقامی قیمت کیا ہے؟"),
     QB,
     T("The 8 is in the crores place.", "8 کروڑ کے مقام پر ہے۔"),
     T(f"Right! 8 crore = {pk(QB)}.", f"درست! 8 کروڑ = {pk(QB)}"),
     T(f"8 is in the crores place, so its value is 8 crore = {pk(QB)}.", f"8 کروڑ کے مقام پر ہے، تو اس کی قیمت 8 کروڑ = {pk(QB)} ہے۔"),
     common_wrong=[wrong(8, "That is the digit. Its value is 8 crore.", "یہ ہندسہ ہے۔ اس کی قیمت 8 کروڑ ہے۔", "digit_not_value"),
                   wrong(8000000, "That is 80 lakh. The 8 is in the crores place: 8 crore.", "یہ 80 لاکھ ہے۔ 8 کروڑ کے مقام پر ہے: 8 کروڑ", "digit_not_value")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Hamza reads 2,50,000 as 'twenty-five thousand'. What is wrong?", "حمزہ 2,50,000 کو 'پچیس ہزار' پڑھتا ہے۔ کیا غلطی ہے؟"),
     "options": [
       opt("lakh", "It is two lakh fifty thousand.", "یہ دو لاکھ پچاس ہزار ہے۔", True,
           "Yes! The 2 is in the lakhs place.", "جی ہاں! 2 لاکھ کے مقام پر ہے۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "Twenty-five thousand is 25,000. This number has 6 digits: two lakh fifty thousand.", "پچیس ہزار 25,000 ہے۔ اس عدد میں 6 ہندسے ہیں: دو لاکھ پچاس ہزار۔"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_lakh", "front": T("1 lakh?", "1 لاکھ؟"),
    "back": T("1,00,000 = 100 thousand.", "1,00,000 = 100 ہزار")},
   {"id": "f_crore", "front": T("1 crore?", "1 کروڑ؟"),
    "back": T("1,00,00,000 = 100 lakh.", "1,00,00,000 = 100 لاکھ")},
 ],
 "home_tasks": [{"id": "h_news", "text": T(
   "Find a big number in a newspaper or on the TV news (a price, a budget or a population). Write it with commas and read it aloud in lakhs or crores.",
   "اخبار یا ٹی وی خبروں میں کوئی بڑا عدد ڈھونڈیں (قیمت، بجٹ یا آبادی)۔ اسے کاما لگا کر لکھیں اور لاکھ یا کروڑ میں بلند آواز سے پڑھیں۔")}],
 "glossary": [T("Lakh", "لاکھ"), T("Crore", "کروڑ"), T("Place value", "مقامی قیمت")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "A new car costs Rs 45,00,000. How do we even read that number?",
                     "ایک نئی گاڑی 45,00,000 روپے کی ہے۔ ہم یہ عدد پڑھیں کیسے؟"),
    "text": T("Today we read and write big numbers in lakhs and crores. First, a quick multiplication check.", "آج ہم بڑے اعداد لاکھ اور کروڑ میں پڑھیں اور لکھیں گے۔ پہلے ضرب کا ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("What is 10 × 10 × 10?", "10 × 10 × 10 کتنا ہے؟"),
     S2,
     T("10 × 10 = 100, then × 10.", "10 × 10 = 100، پھر × 10"),
     T("Right! 1000.", "درست! 1000"),
     T("10 × 10 = 100, and 100 × 10 = 1000.", "10 × 10 = 100، اور 100 × 10 = 1000"),
     common_wrong=[wrong(30, "Multiply, don't add: 10 × 10 × 10 = 1000.", "جمع نہیں، ضرب: 10 × 10 × 10 = 1000"),
                   wrong(100, "That is 10 × 10. Multiply by 10 again: 1000.", "یہ 10 × 10 ہے۔ پھر 10 سے ضرب دیں: 1000")],
     qtype="recall", skill=TIMES_TABLES),
   {"id": "s3_rule", "type": "explain",
    "character": say("happy", "Each place is 10 times the place on its right!", "ہر مقام اپنے دائیں والے مقام سے 10 گنا ہے!"),
    "text": T("Places from the right: ones, tens, hundreds, thousands, ten thousands, lakhs, ten lakhs, crores, ten crores. 100 thousand = 1 lakh (1,00,000). 100 lakh = 1 crore (1,00,00,000). In the Pakistani system, put a comma after the first 3 digits from the right, then after every 2 digits: 2,45,67,890 is two crore forty-five lakh sixty-seven thousand eight hundred ninety.",
              "دائیں سے مقامات: اکائی، دہائی، سینکڑہ، ہزار، دس ہزار، لاکھ، دس لاکھ، کروڑ، دس کروڑ۔ 100 ہزار = 1 لاکھ (1,00,000)۔ 100 لاکھ = 1 کروڑ (1,00,00,000)۔ پاکستانی نظام میں دائیں سے پہلے 3 ہندسوں کے بعد کاما لگائیں، پھر ہر 2 ہندسوں کے بعد: 2,45,67,890 یعنی دو کروڑ پینتالیس لاکھ سڑسٹھ ہزار آٹھ سو نوے۔")},
   number_question(
     "s4_value",
     T(f"What is the value of the digit 6 in {pk(S4_NUM)}?", f"{pk(S4_NUM)} میں 6 کی مقامی قیمت کیا ہے؟"),
     S4,
     T("The 6 is in the lakhs place.", "6 لاکھ کے مقام پر ہے۔"),
     T(f"Right! 6 lakh = {pk(S4)}.", f"درست! 6 لاکھ = {pk(S4)}"),
     T(f"6 is in the lakhs place, so its value is 6 lakh = {pk(S4)}.", f"6 لاکھ کے مقام پر ہے، تو اس کی قیمت 6 لاکھ = {pk(S4)} ہے۔"),
     common_wrong=[wrong(6, "That is the digit. Its value is 6 lakh.", "یہ ہندسہ ہے۔ اس کی قیمت 6 لاکھ ہے۔", "digit_not_value"),
                   wrong(60000, "That is the ten thousands place. The 6 is in the lakhs place: 6,00,000.", "یہ دس ہزار کا مقام ہے۔ 6 لاکھ کے مقام پر ہے: 6,00,000", "digit_not_value")]),
   number_question(
     "s5_thousands",
     T("How many thousands make 1 lakh?", "کتنے ہزار مل کر 1 لاکھ بنتے ہیں؟"),
     S5,
     T("1,00,000 ÷ 1000.", "1,00,000 ÷ 1000"),
     T("Right! 100 thousands make 1 lakh.", "درست! 100 ہزار سے 1 لاکھ بنتا ہے۔"),
     T("1,00,000 ÷ 1000 = 100.", "1,00,000 ÷ 1000 = 100"),
     common_wrong=[wrong(10, "10 thousand is 10,000. 1 lakh is 100 thousand.", "10 ہزار 10,000 ہے۔ 1 لاکھ 100 ہزار ہے۔", "lakh_ten_thousand"),
                   wrong(1000, "1000 thousands would be 10 lakh. 1 lakh = 100 thousand.", "1000 ہزار 10 لاکھ ہوں گے۔ 1 لاکھ = 100 ہزار")]),
   {"id": "s6_crore", "type": "choice",
    "prompt": T("Which is 1 crore?", "1 کروڑ کون سا ہے؟"),
    "options": [
      opt("crore", "1,00,00,000", "1,00,00,000", True, "Yes! 1 followed by 7 zeros.", "جی ہاں! 1 کے بعد 7 صفر۔"),
      opt("ten_lakh", "10,00,000", "10,00,000", False, "That is 10 lakh. 1 crore = 100 lakh.", "یہ 10 لاکھ ہے۔ 1 کروڑ = 100 لاکھ", "crore_ten_lakh"),
      opt("lakh", "1,00,000", "1,00,000", False, "That is 1 lakh. 1 crore is 1,00,00,000.", "یہ 1 لاکھ ہے۔ 1 کروڑ 1,00,00,000 ہے۔"),
    ]},
   number_question(
     "s7_write",
     T("Write 'three lakh twenty-five thousand' as a number.", "'تین لاکھ پچیس ہزار' کو عدد میں لکھیں۔"),
     S7,
     T("3 lakh is 3,00,000. Add 25,000.", "3 لاکھ 3,00,000 ہے۔ 25,000 جمع کریں۔"),
     T(f"Right! {pk(S7)}.", f"درست! {pk(S7)}"),
     T(f"3,00,000 + 25,000 = {pk(S7)}.", f"3,00,000 + 25,000 = {pk(S7)}"),
     common_wrong=[wrong(32500, "That is only 5 digits, which is thousands. 3 lakh needs 6 digits: 3,25,000.", "یہ صرف 5 ہندسے ہیں، یعنی ہزار۔ 3 لاکھ کے لیے 6 ہندسے: 3,25,000", "lost_zero"),
                   wrong(30025000, "Don't write 3 lakh and 25 thousand side by side. Add them: 3,25,000.", "3 لاکھ اور 25 ہزار ساتھ ساتھ نہ لکھیں۔ جمع کریں: 3,25,000")]),
   number_question(
     "s8_lakhs",
     T("How many lakhs make 1 crore?", "کتنے لاکھ مل کر 1 کروڑ بنتے ہیں؟"),
     S8,
     T("1,00,00,000 ÷ 1,00,000.", "1,00,00,000 ÷ 1,00,000"),
     T("Right! 100 lakh = 1 crore.", "درست! 100 لاکھ = 1 کروڑ"),
     T("1 crore has 2 more zeros than 1 lakh, so it is 100 lakh.", "1 کروڑ میں 1 لاکھ سے 2 صفر زیادہ ہیں، تو یہ 100 لاکھ ہے۔"),
     common_wrong=[wrong(10, "10 lakh is 10,00,000. 1 crore is 100 lakh.", "10 لاکھ 10,00,000 ہے۔ 1 کروڑ 100 لاکھ ہے۔", "crore_ten_lakh")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Ahmed reads 45,00,000 as 'forty-five thousand'. What went wrong?", "احمد 45,00,000 کو 'پینتالیس ہزار' پڑھتا ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("lakh", "It is forty-five lakh. The 45 is in the lakhs places.", "یہ پینتالیس لاکھ ہے۔ 45 لاکھ کے مقامات پر ہے۔", True,
          "Yes! Forty-five thousand is 45,000.", "جی ہاں! پینتالیس ہزار 45,000 ہے۔"),
      opt("crore", "It is forty-five crore.", "یہ پینتالیس کروڑ ہے۔", False,
          "45 crore would be 45,00,00,000. This is 45 lakh.", "45 کروڑ 45,00,00,000 ہوگا۔ یہ 45 لاکھ ہے۔"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "45,000 is forty-five thousand. 45,00,000 has two more zeros: 45 lakh.", "45,000 پینتالیس ہزار ہے۔ 45,00,000 میں دو صفر زیادہ ہیں: 45 لاکھ"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why are 100 thousands the same as 1 lakh? Can you teach me?",
                     "100 ہزار اور 1 لاکھ برابر کیوں ہیں؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why do 100 thousands make 1 lakh?", "اپنے الفاظ میں بتائیں: 100 ہزار سے 1 لاکھ کیوں بنتا ہے؟"),
    "key_idea": "Each place is 10 times the one on its right. 10 thousands make ten thousand (10,000), and 10 ten-thousands make 1 lakh, so 10 × 10 = 100 thousands make 1 lakh (1000 × 100 = 1,00,000).",
    "levels": {
      "got_it": "Says 1000 × 100 = 1,00,000, or that each place is 10 times the last, so two places up is 100 times.",
      "partly": "Says 100 × 1000 without explaining the places.",
      "not_yet": "Gives no reason."},
    "keywords": [
      ["10", "ten", "دس"],
      ["100", "hundred", "سو"],
      ["place", "مقام"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Two places up means 10 × 10 = 100 times.", "بہت خوب! دو مقام اوپر یعنی 10 × 10 = 100 گنا۔"),
      "partly": T("Good start! Now say how the places grow by 10 each time.", "اچھی شروعات! اب بتائیں کہ مقامات ہر بار 10 گنا کیسے بڑھتے ہیں۔"),
      "not_yet": T("How many thousands make ten thousand? How many ten thousands make a lakh?", "کتنے ہزار سے دس ہزار بنتا ہے؟ کتنے دس ہزار سے ایک لاکھ؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_notes",
     T("A school fund has Rs 5,00,000. How many Rs 1000 notes is that?", "سکول کے فنڈ میں 5,00,000 روپے ہیں۔ یہ 1000 روپے کے کتنے نوٹ ہیں؟"),
     S11,
     T("1 lakh = 100 thousand. How many thousands in 5 lakh?", "1 لاکھ = 100 ہزار۔ 5 لاکھ میں کتنے ہزار؟"),
     T("Right! 500 notes.", "درست! 500 نوٹ"),
     T("5 lakh = 5 × 100 thousand = 500 thousand, so 500 notes.", "5 لاکھ = 5 × 100 ہزار = 500 ہزار، تو 500 نوٹ"),
     common_wrong=[wrong(50, "1 lakh is 100 thousand, not 10: 500 notes.", "1 لاکھ 100 ہزار ہے، 10 نہیں: 500 نوٹ", "lakh_ten_thousand"),
                   wrong(5000, "5000 notes of Rs 1000 would be 50 lakh. 5 lakh is 500 notes.", "1000 روپے کے 5000 نوٹ 50 لاکھ ہوں گے۔ 5 لاکھ 500 نوٹ ہیں۔")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Lakhs and crores are easy now. Big numbers, no fear!", "لاکھ اور کروڑ اب آسان ہیں۔ بڑے اعداد، کوئی ڈر نہیں!"),
    "text": T("100 thousand = 1 lakh (1,00,000). 100 lakh = 1 crore (1,00,00,000). Pakistani commas: 3 digits from the right, then every 2. The value of a digit depends on its place.",
              "100 ہزار = 1 لاکھ (1,00,000)۔ 100 لاکھ = 1 کروڑ (1,00,00,000)۔ پاکستانی کامے: دائیں سے 3 ہندسے، پھر ہر 2۔ ہندسے کی قیمت اس کے مقام پر منحصر ہے۔"),
    "points": [T("1 lakh = 1,00,000.", "1 لاکھ = 1,00,000"),
               T("1 crore = 100 lakh.", "1 کروڑ = 100 لاکھ")]},
 ],
 "review_questions": [
   {"id": "r_value", "type": "apply", "skill": SKILL, "step": number_question(
     "r_value",
     T(f"What is the value of the digit 4 in {pk(R1_NUM)}?", f"{pk(R1_NUM)} میں 4 کی مقامی قیمت کیا ہے؟"),
     R1,
     T("The 4 is in the lakhs place.", "4 لاکھ کے مقام پر ہے۔"),
     T(f"Right! 4 lakh = {pk(R1)}.", f"درست! 4 لاکھ = {pk(R1)}"),
     T(f"4 is in the lakhs place: {pk(R1)}.", f"4 لاکھ کے مقام پر ہے: {pk(R1)}"),
     common_wrong=[wrong(4, "That is the digit. Its value is 4 lakh.", "یہ ہندسہ ہے۔ اس کی قیمت 4 لاکھ ہے۔", "digit_not_value"),
                   wrong(40000, "That is the ten thousands place. The 4 is in the lakhs place.", "یہ دس ہزار کا مقام ہے۔ 4 لاکھ کے مقام پر ہے۔", "digit_not_value")],
     qtype=None)},
   {"id": "r_ten_thousands", "type": "apply", "skill": SKILL, "step": number_question(
     "r_ten_thousands",
     T("How many ten thousands (10,000) make 1 lakh?", "کتنے دس ہزار (10,000) مل کر 1 لاکھ بنتے ہیں؟"),
     R2,
     T("1,00,000 ÷ 10,000.", "1,00,000 ÷ 10,000"),
     T("Right! 10.", "درست! 10"),
     T("1,00,000 ÷ 10,000 = 10.", "1,00,000 ÷ 10,000 = 10"),
     common_wrong=[wrong(100, "100 thousands make a lakh, but only 10 ten thousands.", "100 ہزار سے لاکھ بنتا ہے، مگر دس ہزار صرف 10۔")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Whole Numbers unit. No textbook text or exercises were used.",
   "Children may type answers with or without commas (6,00,000 or 600000); both are accepted.",
   "Urdu terms to check: مقامی قیمت (place value), لاکھ, کروڑ, کاما.",
   "The numbers were worked out in content/sources/g6-maths-15/lakhs_and_crores.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)
