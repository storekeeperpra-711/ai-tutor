from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, WN_PLACE_VALUE, WN_SYSTEMS, WN_COMPARE, WN_PROPERTIES, WN_WORD_PROBLEMS,
                    LAKH, CRORE, MILLION, pk)

SKILL = WN_WORD_PROBLEMS

# s2: 6 x (10 + 3) (forgetting to multiply the 3: 63)
S2 = 6 * (10 + 3)
assert S2 == 78 and 6 * 10 + 3 == 63
# s4: 2,50,000 bricks a month for 4 months
S4 = 250000 * 4
assert S4 == 10 * LAKH and pk(S4) == "10,00,000"
# s5: 1,25,400 people, 38,600 children
S5 = 125400 - 38600
assert S5 == 86800 and 125400 + 38600 == 164000
# s6: 4 stands of 27,000 seats
assert 27000 * 4 == 108000
# s7: 3 crore shared by 100 schools
S7 = 3 * CRORE // 100
assert S7 == 3 * LAKH and 3 * CRORE // 10 == 30 * LAKH
# s8: 1,80,000 passengers a day for 7 days
S8 = 180000 * 7
assert S8 == 1260000 and pk(S8) == "12,60,000"
# s9: 5 buses of 60 children
assert 5 * 60 == 300 and 60 + 5 == 65
# unit test
U1 = 7 * LAKH
assert pk(730000) == "7,30,000" and U1 == 700000
U2 = 6 * MILLION // LAKH
assert U2 == 60
U3 = max(809500, 890050)
assert U3 == 890050
U4 = 25 * 47 * 4
assert U4 == 100 * 47 == 4700
U5 = 450000 + 375000
assert U5 == 825000 and pk(U5) == "8,25,000"
# question bank and review
QB = 3 * 45000 + 20000
assert QB == 155000 and 3 * (45000 + 20000) == 195000
R1 = 18000 * 3
assert R1 == 54000
R2 = 10 * LAKH - 275000
assert R2 == 725000

lesson = {
 "id": "g6-maths-15-whole-number-word-problems",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Solve real-life problems with large whole numbers, choosing the right operation.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Whole numbers word problems", "مکمل اعداد کے عملی سوال"),
 "estimated_minutes": 18,
 "prerequisites": [{"skill": WN_PROPERTIES}, {"skill": WN_COMPARE}, {"skill": WN_SYSTEMS}, {"skill": WN_PLACE_VALUE}],
 "misconceptions": [
   {"id": "wrong_operation", "description": "Adds when the story needs multiplying, or the other way round."},
   {"id": "adds_difference", "description": "Adds the two numbers when the story asks for what is left."},
   {"id": "lost_zero", "description": "Drops or adds a zero when working with lakhs and crores."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_left", "type": "recall", "step": {
     "id": "qb_left", "type": "choice",
     "prompt": T("A story asks 'how many are left?'. Which operation do you use?", "سوال پوچھتا ہے 'کتنے باقی ہیں؟'۔ آپ کون سا عمل کریں گے؟"),
     "options": [
       opt("subtract", "Subtract (−)", "تفریق (−)", True,
           "Yes! Take away what is used.", "جی ہاں! جو استعمال ہوا وہ نکالیں۔"),
       opt("add", "Add (+)", "جمع (+)", False,
           "Adding makes it bigger. 'Left' means take away: −.", "جمع سے بڑھتا ہے۔ 'باقی' یعنی نکالنا: −", "adds_difference"),
       opt("times", "Multiply (×)", "ضرب (×)", False,
           "× is for equal groups. 'Left' means −.", "× برابر گروپوں کے لیے ہے۔ 'باقی' یعنی −", "wrong_operation"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("A farmer sells 3 buffaloes at Rs 45,000 each and a cart for Rs 20,000. How much does he get? (3 × 45,000 + 20,000)", "ایک کسان 45,000 روپے فی بھینس کے حساب سے 3 بھینسیں اور 20,000 روپے کی ایک گاڑی بیچتا ہے۔ اسے کتنے پیسے ملتے ہیں؟ (3 × 45,000 + 20,000)"),
     QB,
     T("3 × 45,000 first.", "پہلے 3 × 45,000"),
     T(f"Right! Rs {pk(QB)}.", f"درست! {pk(QB)} روپے"),
     T(f"3 × 45,000 = 1,35,000, then + 20,000 = {pk(QB)}.", f"3 × 45,000 = 1,35,000، پھر + 20,000 = {pk(QB)}"),
     common_wrong=[wrong(195000, "There is only 1 cart, not 3: 1,35,000 + 20,000 = 1,55,000.", "گاڑی صرف 1 ہے، 3 نہیں: 1,35,000 + 20,000 = 1,55,000", "wrong_operation")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("A tank holds 5,000 litres. 1,200 litres are used. Kamran says 6,200 litres are left. What is wrong?", "ٹینکی میں 5,000 لیٹر آتا ہے۔ 1,200 لیٹر استعمال ہو گیا۔ کامران کہتا ہے 6,200 لیٹر باقی ہے۔ کیا غلطی ہے؟"),
     "options": [
       opt("subtract", "He added. Left means subtract: 5,000 − 1,200 = 3,800.", "اس نے جمع کیا۔ باقی یعنی تفریق: 5,000 − 1,200 = 3,800", True,
           "Yes! What is left can't be more than the tank holds.", "جی ہاں! باقی پانی ٹینکی کی گنجائش سے زیادہ نہیں ہو سکتا۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "6,200 is more than the full tank! 5,000 − 1,200 = 3,800.", "6,200 تو پوری ٹینکی سے بھی زیادہ ہے! 5,000 − 1,200 = 3,800", "adds_difference"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_words", "front": T("'Altogether', 'total'?", "'کل'، 'مجموعی'؟"),
    "back": T("Usually add, or × for equal groups.", "عموماً جمع، یا برابر گروپوں کے لیے ×")},
   {"id": "f_left", "front": T("'Left', 'more than', 'difference'?", "'باقی'، 'کتنا زیادہ'، 'فرق'؟"),
    "back": T("Subtract.", "تفریق")},
 ],
 "home_tasks": [{"id": "h_story", "text": T(
   "Make up your own story with a number in lakhs (a car price, a crop sale or a school fund). Ask someone at home to solve it.",
   "لاکھوں والے عدد کے ساتھ اپنی ایک کہانی بنائیں (گاڑی کی قیمت، فصل کی فروخت یا سکول کا فنڈ)۔ گھر میں کسی سے اسے حل کروائیں۔")}],
 "glossary": [T("Total", "کل"), T("Difference", "فرق"), T("Each", "ہر ایک")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Bricks, buses and budgets: big numbers are everywhere. Let's solve real problems!",
                     "اینٹیں، بسیں اور بجٹ: بڑے اعداد ہر جگہ ہیں۔ آئیں اصل سوال حل کریں!"),
    "text": T("Today we solve word problems with large numbers. First, a quick check on breaking up numbers.", "آج ہم بڑے اعداد کے عملی سوال حل کریں گے۔ پہلے اعداد توڑنے کا ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("Work out 6 × (10 + 3).", "6 × (10 + 3) نکالیں۔"),
     S2,
     T("6 × 10 + 6 × 3.", "6 × 10 + 6 × 3"),
     T("Right! 60 + 18 = 78.", "درست! 60 + 18 = 78"),
     T("6 × 10 = 60, 6 × 3 = 18, 60 + 18 = 78.", "6 × 10 = 60، 6 × 3 = 18، 60 + 18 = 78"),
     common_wrong=[wrong(63, "Multiply the 3 by 6 too: 60 + 18 = 78.", "3 کو بھی 6 سے ضرب دیں: 60 + 18 = 78")],
     qtype="recall", skill=WN_PROPERTIES),
   {"id": "s3_rule", "type": "explain",
    "character": say("happy", "Read, choose, work, check. Four steps to any word problem!", "پڑھیں، چنیں، حل کریں، جانچیں۔ ہر عملی سوال کے چار قدم!"),
    "text": T("1. Read the story and find the numbers. 2. Choose the operation: total → +; equal groups → ×; left or difference → −; sharing equally → ÷. 3. Work it out, keeping the zeros right. 4. Check: does the answer make sense?",
              "1۔ کہانی پڑھیں اور اعداد ڈھونڈیں۔ 2۔ عمل چنیں: کل → +؛ برابر گروپ → ×؛ باقی یا فرق → −؛ برابر بانٹنا → ÷۔ 3۔ حل کریں، صفر صحیح رکھیں۔ 4۔ جانچیں: کیا جواب سمجھ میں آتا ہے؟")},
   number_question(
     "s4_bricks",
     T("A kiln makes 2,50,000 bricks a month. How many bricks does it make in 4 months?", "ایک بھٹہ ہر مہینے 2,50,000 اینٹیں بناتا ہے۔ 4 مہینوں میں کتنی اینٹیں بنائے گا؟"),
     S4,
     T("Equal groups: 2,50,000 × 4.", "برابر گروپ: 2,50,000 × 4"),
     T(f"Right! {pk(S4)} bricks (10 lakh).", f"درست! {pk(S4)} اینٹیں (10 لاکھ)"),
     T(f"2,50,000 × 4 = {pk(S4)}.", f"2,50,000 × 4 = {pk(S4)}"),
     common_wrong=[wrong(100000, "2.5 lakh × 4 = 10 lakh: 10,00,000. Count the zeros.", "ڈھائی لاکھ × 4 = 10 لاکھ: 10,00,000۔ صفر گنیں۔", "lost_zero"),
                   wrong(250004, "4 months means × 4, not + 4: 10,00,000.", "4 مہینے یعنی × 4، + 4 نہیں: 10,00,000", "wrong_operation")]),
   number_question(
     "s5_adults",
     T("A town has 1,25,400 people. 38,600 of them are children. How many are adults?", "ایک قصبے میں 1,25,400 لوگ ہیں۔ ان میں 38,600 بچے ہیں۔ بالغ کتنے ہیں؟"),
     S5,
     T("The rest: 1,25,400 − 38,600.", "باقی: 1,25,400 − 38,600"),
     T(f"Right! {pk(S5)} adults.", f"درست! {pk(S5)} بالغ"),
     T(f"1,25,400 − 38,600 = {pk(S5)}.", f"1,25,400 − 38,600 = {pk(S5)}"),
     common_wrong=[wrong(164000, "Adding gives more than the whole town. Subtract: 86,800.", "جمع کرنے سے پورے قصبے سے زیادہ ہو جاتا ہے۔ تفریق کریں: 86,800", "adds_difference")]),
   {"id": "s6_operation", "type": "choice",
    "prompt": T("A cricket stadium has 4 stands with 27,000 seats in each. Which sum finds all the seats?", "کرکٹ سٹیڈیم میں 4 سٹینڈ ہیں، ہر ایک میں 27,000 نشستیں۔ تمام نشستیں کون سا حساب بتائے گا؟"),
    "options": [
      opt("times", "27,000 × 4", "27,000 × 4", True, "Yes! 4 equal groups: 1,08,000 seats.", "جی ہاں! 4 برابر گروپ: 1,08,000 نشستیں۔"),
      opt("plus", "27,000 + 4", "27,000 + 4", False, "Adding 4 adds 4 seats. There are 4 stands of 27,000: ×.", "4 جمع کرنے سے 4 نشستیں بڑھتی ہیں۔ 27,000 کے 4 سٹینڈ ہیں: ×", "wrong_operation"),
      opt("divide", "27,000 ÷ 4", "27,000 ÷ 4", False, "÷ shares out. Here each stand has 27,000, so ×.", "÷ بانٹتا ہے۔ یہاں ہر سٹینڈ میں 27,000 ہیں، تو ×", "wrong_operation"),
    ]},
   number_question(
     "s7_schools",
     T("The government gives Rs 3,00,00,000 (3 crore) to be shared equally by 100 schools. How much does each school get?", "حکومت 3,00,00,000 روپے (3 کروڑ) دیتی ہے جو 100 سکولوں میں برابر بانٹے جائیں۔ ہر سکول کو کتنے ملیں گے؟"),
     S7,
     T("Sharing equally: ÷ 100. Remove two zeros.", "برابر بانٹنا: ÷ 100۔ دو صفر ہٹائیں۔"),
     T(f"Right! Rs {pk(S7)} (3 lakh) each.", f"درست! ہر ایک کو {pk(S7)} روپے (3 لاکھ)"),
     T(f"3,00,00,000 ÷ 100 = {pk(S7)}.", f"3,00,00,000 ÷ 100 = {pk(S7)}"),
     common_wrong=[wrong(3000000, "That is ÷ 10. For ÷ 100 remove two zeros: 3,00,000.", "یہ ÷ 10 ہے۔ ÷ 100 کے لیے دو صفر ہٹائیں: 3,00,000", "lost_zero"),
                   wrong(30000, "That removes three zeros. ÷ 100 removes two: 3,00,000.", "اس میں تین صفر ہٹ گئے۔ ÷ 100 سے دو ہٹتے ہیں: 3,00,000", "lost_zero")]),
   number_question(
     "s8_metro",
     T("A metro bus carries 1,80,000 passengers a day. How many does it carry in a week (7 days)?", "میٹرو بس روزانہ 1,80,000 مسافر لے جاتی ہے۔ ایک ہفتے (7 دن) میں کتنے؟"),
     S8,
     T("1,80,000 × 7.", "1,80,000 × 7"),
     T(f"Right! {pk(S8)} passengers.", f"درست! {pk(S8)} مسافر"),
     T(f"18 × 7 = 126, then add the four zeros: {pk(S8)}.", f"18 × 7 = 126، پھر چار صفر لگائیں: {pk(S8)}"),
     common_wrong=[wrong(126000, "1,80,000 has four zeros after 18: 12,60,000.", "1,80,000 میں 18 کے بعد چار صفر ہیں: 12,60,000", "lost_zero"),
                   wrong(180007, "A week is 7 days of passengers: × 7, not + 7.", "ہفتہ یعنی 7 دن کے مسافر: × 7، + 7 نہیں", "wrong_operation")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("5 buses each carry 60 children. Hina says 60 + 5 = 65 children. What went wrong?", "5 بسوں میں سے ہر ایک میں 60 بچے ہیں۔ حنا کہتی ہے 60 + 5 = 65 بچے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("times", "Equal groups need ×: 60 × 5 = 300.", "برابر گروپوں کے لیے ×: 60 × 5 = 300", True,
          "Yes! 5 buses of 60 is 300 children.", "جی ہاں! 60 کی 5 بسیں یعنی 300 بچے۔"),
      opt("minus", "She should subtract: 60 − 5 = 55.", "اسے تفریق کرنی چاہیے: 60 − 5 = 55", False,
          "Nothing is taken away. 5 groups of 60: ×.", "کچھ نکالا نہیں جا رہا۔ 60 کے 5 گروپ: ×", "wrong_operation"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "One bus alone has 60. Five buses have 60 × 5 = 300.", "اکیلی ایک بس میں 60 ہیں۔ پانچ بسوں میں 60 × 5 = 300", "wrong_operation"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "How do you know whether to add or multiply in a story? Can you teach me?",
                     "آپ کو کیسے پتا چلتا ہے کہ کہانی میں جمع کرنا ہے یا ضرب؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: when do we multiply instead of add? Give an example.", "اپنے الفاظ میں بتائیں: ہم جمع کی بجائے ضرب کب کرتے ہیں؟ ایک مثال دیں۔"),
    "key_idea": "We multiply when there are equal groups (the same amount many times), like 5 buses with 60 children each. We add when we put different amounts together.",
    "levels": {
      "got_it": "Says multiply for equal groups or the same amount repeated, with an example.",
      "partly": "Gives an example without the idea of equal groups, or the idea without an example.",
      "not_yet": "Gives no reason."},
    "keywords": [
      ["equal", "same", "each", "برابر", "ہر"],
      ["group", "times", "گروپ", "بار"],
      ["multiply", "ضرب"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Equal groups mean multiply.", "بہت خوب! برابر گروپ یعنی ضرب۔"),
      "partly": T("Good start! Now say what makes the groups special.", "اچھی شروعات! اب بتائیں ان گروپوں میں کیا خاص ہے۔"),
      "not_yet": T("Think of 5 buses with 60 children in each. Is it 60 + 5 or 60 × 5? Why?", "60 بچوں والی 5 بسوں کا سوچیں۔ یہ 60 + 5 ہے یا 60 × 5؟ کیوں؟")},
    "limit_per_day": 3, "max_attempts": 2},
   {"id": "s11_unit_test", "type": "explain",
    "character": say("encouraging", "Test time! Five questions from the whole Whole numbers unit. You can do it!",
                     "ٹیسٹ کا وقت! مکمل اعداد کے پورے باب سے پانچ سوال۔ آپ کر سکتے ہیں!"),
    "text": T("This short test has questions on place value, millions, comparing, properties and a real-life problem. Take your time.",
              "اس چھوٹے ٹیسٹ میں مقامی قیمت، ملین، موازنہ، خصوصیات اور ایک اصل زندگی کا سوال ہے۔ آرام سے کریں۔")},
   number_question(
     "u1_place_value",
     T("Test 1: What is the value of the digit 7 in 7,30,000?", "ٹیسٹ 1: 7,30,000 میں 7 کی مقامی قیمت کیا ہے؟"),
     U1,
     T("The 7 is in the lakhs place.", "7 لاکھ کے مقام پر ہے۔"),
     T(f"Right! 7 lakh = {pk(U1)}.", f"درست! 7 لاکھ = {pk(U1)}"),
     T(f"7 is in the lakhs place: {pk(U1)}.", f"7 لاکھ کے مقام پر ہے: {pk(U1)}"),
     common_wrong=[wrong(7, "That is the digit. Its value is 7 lakh.", "یہ ہندسہ ہے۔ اس کی قیمت 7 لاکھ ہے۔"),
                   wrong(70000, "That is the ten thousands place. The 7 is in the lakhs place.", "یہ دس ہزار کا مقام ہے۔ 7 لاکھ کے مقام پر ہے۔")],
     qtype="recall", skill=WN_PLACE_VALUE),
   number_question(
     "u2_millions",
     T("Test 2: 6 million is how many lakh?", "ٹیسٹ 2: 6 ملین کتنے لاکھ ہیں؟"),
     U2,
     T("1 million = 10 lakh.", "1 ملین = 10 لاکھ"),
     T("Right! 60 lakh.", "درست! 60 لاکھ"),
     T("6 × 10 = 60.", "6 × 10 = 60"),
     common_wrong=[wrong(6, "1 million is 10 lakh: 60.", "1 ملین 10 لاکھ ہے: 60"),
                   wrong(600, "1 million is 10 lakh, not 100: 60.", "1 ملین 10 لاکھ ہے، 100 نہیں: 60")],
     qtype="apply", skill=WN_SYSTEMS),
   number_question(
     "u3_compare",
     T("Test 3: Which is bigger: 8,09,500 or 8,90,050? Type the bigger number.", "ٹیسٹ 3: کون سا بڑا ہے: 8,09,500 یا 8,90,050؟ بڑا عدد لکھیں۔"),
     U3,
     T("Same lakhs. Compare the ten thousands.", "لاکھ برابر۔ دس ہزار دیکھیں۔"),
     T(f"Right! {pk(U3)}.", f"درست! {pk(U3)}"),
     T("Ten thousands: 9 > 0, so 8,90,050.", "دس ہزار: 9 > 0، تو 8,90,050"),
     common_wrong=[wrong(809500, "Ten thousands: 9 > 0, so 8,90,050 is bigger.", "دس ہزار: 9 > 0، تو 8,90,050 بڑا ہے۔")],
     qtype="apply", skill=WN_COMPARE),
   number_question(
     "u4_properties",
     T("Test 4: Work out 25 × 47 × 4.", "ٹیسٹ 4: 25 × 47 × 4 نکالیں۔"),
     U4,
     T("25 × 4 = 100 first.", "پہلے 25 × 4 = 100"),
     T("Right! 100 × 47 = 4700.", "درست! 100 × 47 = 4700"),
     T("25 × 4 = 100, and 100 × 47 = 4700.", "25 × 4 = 100، اور 100 × 47 = 4700"),
     common_wrong=[wrong(76, "Multiply, don't add: 100 × 47 = 4700.", "جمع نہیں، ضرب: 100 × 47 = 4700")],
     qtype="apply", skill=WN_PROPERTIES),
   number_question(
     "u5_charity",
     T("Test 5: A charity collects Rs 4,50,000 in March and Rs 3,75,000 in April. How much is that altogether?", "ٹیسٹ 5: ایک فلاحی ادارہ مارچ میں 4,50,000 روپے اور اپریل میں 3,75,000 روپے جمع کرتا ہے۔ کل کتنے ہوئے؟"),
     U5,
     T("Altogether: add.", "کل: جمع کریں۔"),
     T(f"Right! Rs {pk(U5)}.", f"درست! {pk(U5)} روپے"),
     T(f"4,50,000 + 3,75,000 = {pk(U5)}.", f"4,50,000 + 3,75,000 = {pk(U5)}"),
     common_wrong=[wrong(75000, "That is the difference. Altogether means add: 8,25,000.", "یہ فرق ہے۔ کل یعنی جمع: 8,25,000", "adds_difference"),
                   wrong(725000, "Carry the 1: 50,000 + 75,000 = 1,25,000. Total 8,25,000.", "1 آگے لے جائیں: 50,000 + 75,000 = 1,25,000۔ کل 8,25,000")],
     qtype="apply"),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Whole numbers unit complete! Lakhs, crores and millions are your friends now.", "مکمل اعداد کا باب مکمل! لاکھ، کروڑ اور ملین اب آپ کے دوست ہیں۔"),
    "text": T("Read the story, choose the operation (total +, equal groups ×, left or difference −, sharing ÷), keep the zeros right, and check that the answer makes sense.",
              "کہانی پڑھیں، عمل چنیں (کل +، برابر گروپ ×، باقی یا فرق −، بانٹنا ÷)، صفر صحیح رکھیں، اور جانچیں کہ جواب سمجھ میں آتا ہے۔"),
    "points": [T("Equal groups: ×. Sharing: ÷.", "برابر گروپ: ×۔ بانٹنا: ÷"),
               T("Count the zeros, then check.", "صفر گنیں، پھر جانچیں۔")]},
 ],
 "review_questions": [
   {"id": "r_tickets", "type": "apply", "skill": SKILL, "step": number_question(
     "r_tickets",
     T("A cricket match sells 18,000 tickets each day for 3 days. How many tickets is that?", "ایک کرکٹ میچ کے لیے 3 دن تک روزانہ 18,000 ٹکٹ بکتے ہیں۔ کل کتنے ٹکٹ ہوئے؟"),
     R1,
     T("Equal groups: 18,000 × 3.", "برابر گروپ: 18,000 × 3"),
     T(f"Right! {pk(R1)} tickets.", f"درست! {pk(R1)} ٹکٹ"),
     T("18 × 3 = 54, so 54,000.", "18 × 3 = 54، تو 54,000"),
     common_wrong=[wrong(18003, "3 days means × 3, not + 3: 54,000.", "3 دن یعنی × 3، + 3 نہیں: 54,000", "wrong_operation")],
     qtype=None)},
   {"id": "r_left", "type": "apply", "skill": SKILL, "step": number_question(
     "r_left",
     T("A family saves Rs 10,00,000 and spends Rs 2,75,000 on a wedding. How much is left?", "ایک خاندان 10,00,000 روپے بچاتا ہے اور 2,75,000 روپے ایک شادی پر خرچ کرتا ہے۔ کتنے باقی ہیں؟"),
     R2,
     T("Left: 10,00,000 − 2,75,000.", "باقی: 10,00,000 − 2,75,000"),
     T(f"Right! Rs {pk(R2)}.", f"درست! {pk(R2)} روپے"),
     T(f"10,00,000 − 2,75,000 = {pk(R2)}.", f"10,00,000 − 2,75,000 = {pk(R2)}"),
     common_wrong=[wrong(1275000, "Spending makes it less. Subtract: 7,25,000.", "خرچ کرنے سے کم ہوتا ہے۔ تفریق کریں: 7,25,000", "adds_difference")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Whole Numbers unit. No textbook text or exercises were used.",
   "The numbers in the stories (bricks, metro passengers, a school fund) are made up but realistic for Punjab.",
   "The five-question unit test at the end covers every lesson of the unit.",
   "The numbers were worked out in content/sources/g6-maths-15/whole_number_word_problems.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)
