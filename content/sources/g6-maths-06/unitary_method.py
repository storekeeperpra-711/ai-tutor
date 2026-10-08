from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, TIMES_TABLES, RATIO_PROPORTION, UNITARY)

SKILL = UNITARY


def unitary(total: int, count: int, wanted: int) -> tuple[int, int]:
    """(cost of one, cost of [wanted]) when [count] cost [total]."""
    one, rest = divmod(total, count)
    assert rest == 0, (total, count)
    return one, one * wanted


# 4 pens cost Rs 120; Ali needs 7 (s1 to s4).
PEN, SEVEN_PENS = unitary(120, 4, 7)
assert (PEN, SEVEN_PENS) == (30, 210)
assert 120 + (7 - 4) == 123 and 120 * 7 == 840

# s5: 5 kg of sugar cost Rs 750: 1 kg?
SUGAR, _ = unitary(750, 5, 1)
assert SUGAR == 150

# s6: 6 eggs cost Rs 180: 10 eggs?
EGG, TEN_EGGS = unitary(180, 6, 10)
assert (EGG, TEN_EGGS) == (30, 300)

# s7: a bus goes 150 km in 3 hours: how far in 5 hours?
KM_PER_HOUR, FIVE_HOURS = unitary(150, 3, 5)
assert (KM_PER_HOUR, FIVE_HOURS) == (50, 250)

# s8: Rehan's 3 notebooks for Rs 90; 5 cost?
NOTEBOOK, FIVE_NOTEBOOKS = unitary(90, 3, 5)
assert (NOTEBOOK, FIVE_NOTEBOOKS) == (30, 150)

# s9: 8 kg of atta cost Rs 960: how many kg for Rs 600?
ATTA_KG, _ = unitary(960, 8, 1)
assert ATTA_KG == 120 and 600 % ATTA_KG == 0
ATTA_FOR_600 = 600 // ATTA_KG
assert ATTA_FOR_600 == 5

# s11: 12 bananas cost Rs 144: 5 bananas?
BANANA, FIVE_BANANAS = unitary(144, 12, 5)
assert (BANANA, FIVE_BANANAS) == (12, 60)

# Question bank and review.
assert unitary(250, 5, 8) == (50, 400)
assert unitary(84, 7, 3) == (12, 36)
assert unitary(200, 4, 9) == (50, 450)

lesson = {
 "id": "g6-maths-06-unitary-method",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Solve direct proportion problems with the unitary method: first find the value of one, then of the number wanted.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("The unitary method", "اکائی کا طریقہ"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": RATIO_PROPORTION}, {"skill": TIMES_TABLES}],
 "misconceptions": [
   {"id": "additive_thinking", "description": "Adds the difference in the number of things to the price (4 pens Rs 120, so 7 pens Rs 123)."},
   {"id": "skips_unit", "description": "Multiplies the whole price by the new number without first finding the price of one (Rs 120 × 7)."},
   {"id": "divides_wrong_way", "description": "Divides the number of things by the price, or the wrong two numbers, when finding the value of one."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_first_step", "type": "recall", "step": {
     "id": "qb_first_step", "type": "choice",
     "prompt": T("5 kg of rice cost Rs 250. You want the price of 8 kg. What do you find first?", "5 کلوگرام چاول 250 روپے کے ہیں۔ آپ 8 کلوگرام کی قیمت جاننا چاہتے ہیں۔ پہلے کیا معلوم کریں گے؟"),
     "options": [
       opt("a", "The price of 1 kg: 250 ÷ 5 = Rs 50.", "1 کلوگرام کی قیمت: 250 ÷ 5 = 50 روپے۔", True,
           "Yes! Then 8 kg cost 8 × 50 = Rs 400.", "جی ہاں! پھر 8 کلوگرام کی قیمت 8 × 50 = 400 روپے۔"),
       opt("b", "250 × 8", "250 × 8", False,
           "Rs 250 is for 5 kg, not 1 kg. Find the price of 1 kg first.", "250 روپے 5 کلوگرام کے ہیں، 1 کلوگرام کے نہیں۔ پہلے 1 کلوگرام کی قیمت معلوم کریں۔", "skips_unit"),
       opt("c", "250 + 3", "250 + 3", False,
           "3 more kg don't cost Rs 3! Find the price of 1 kg first.", "3 کلوگرام زیادہ کی قیمت 3 روپے نہیں ہوتی! پہلے 1 کلوگرام کی قیمت معلوم کریں۔", "additive_thinking"),
     ]}},
   {"id": "qb_mangoes", "type": "apply", "step": number_question(
     "qb_mangoes",
     T("7 mangoes cost Rs 84. How much do 3 mangoes cost, in rupees?", "7 آم 84 روپے کے ہیں۔ 3 آم کتنے روپے کے ہوں گے؟"),
     36,
     T("First find the price of 1 mango: 84 ÷ 7.", "پہلے 1 آم کی قیمت معلوم کریں: 84 ÷ 7"),
     T("Right! 1 mango costs Rs 12, so 3 cost 3 × 12 = Rs 36.", "درست! 1 آم 12 روپے کا، اس لیے 3 آم 3 × 12 = 36 روپے کے۔"),
     T("84 ÷ 7 = 12 for one mango. 3 × 12 = Rs 36.", "ایک آم: 84 ÷ 7 = 12۔ 3 × 12 = 36 روپے۔"),
     common_wrong=[wrong(12, "Rs 12 is one mango. You need 3.", "12 روپے ایک آم کی قیمت ہے۔ آپ کو 3 چاہییں۔"),
                   wrong(80, "Taking away 4 rupees doesn't match 4 fewer mangoes. Find the price of one first.", "4 آم کم ہونے سے 4 روپے کم نہیں ہوتے۔ پہلے ایک کی قیمت معلوم کریں۔", "additive_thinking")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("4 bottles of juice cost Rs 200. Hira says 9 bottles cost 200 × 9 = Rs 1800. Is she right?", "جوس کی 4 بوتلیں 200 روپے کی ہیں۔ حرا کہتی ہے 9 بوتلیں 200 × 9 = 1800 روپے کی ہیں۔ کیا وہ درست ہے؟"),
     "options": [
       opt("no", "No. Rs 200 is for 4 bottles. 1 bottle is Rs 50, so 9 cost Rs 450.", "نہیں۔ 200 روپے 4 بوتلوں کے ہیں۔ 1 بوتل 50 روپے کی، اس لیے 9 بوتلیں 450 روپے کی۔", True,
           "Right! Find one first: 200 ÷ 4 = 50, then 9 × 50 = 450.", "درست! پہلے ایک معلوم کریں: 200 ÷ 4 = 50، پھر 9 × 50 = 450"),
       opt("yes", "Yes. Multiply the price by the number of bottles.", "ہاں۔ قیمت کو بوتلوں کی تعداد سے ضرب دیں۔", False,
           "That works only with the price of ONE bottle. Rs 200 is for 4.", "یہ صرف ایک بوتل کی قیمت سے ہوتا ہے۔ 200 روپے 4 بوتلوں کے ہیں۔", "skips_unit"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_unitary", "front": T("What is the unitary method?", "اکائی کا طریقہ کیا ہے؟"),
    "back": T("First find the value of ONE, then multiply. 4 pens cost Rs 120 → 1 pen Rs 30 → 7 pens 7 × 30 = Rs 210.", "پہلے ایک کی قیمت معلوم کریں، پھر ضرب دیں۔ 4 قلم 120 روپے ← 1 قلم 30 روپے ← 7 قلم 7 × 30 = 210 روپے")},
   {"id": "f_check", "front": T("How can you check the answer makes sense?", "کیسے جانچیں کہ جواب درست لگتا ہے؟"),
    "back": T("More things should cost more, fewer should cost less. 7 pens must cost more than 4 pens.", "زیادہ چیزیں زیادہ کی، کم چیزیں کم کی ہوں گی۔ 7 قلم، 4 قلموں سے مہنگے ہونے چاہییں۔")},
 ],
 "home_tasks": [{"id": "h_shop", "text": T(
   "Ask at home or at a shop how much a dozen (12) eggs cost. Work out the price of 1 egg, then of 5 eggs. Check with an adult.",
   "گھر میں یا دکان پر پوچھیں کہ ایک درجن (12) انڈے کتنے کے ہیں۔ 1 انڈے کی قیمت نکالیں، پھر 5 انڈوں کی۔ کسی بڑے سے جانچ کروائیں۔")}],
 "glossary": [T("Unitary method", "اکائی کا طریقہ"), T("Unit (one)", "اکائی (ایک)"), T("Direct proportion", "راست تناسب"), T("Price", "قیمت")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious",
      "At the bookshop, 4 pens cost Rs 120. Ali needs 7 pens for his class. How much money should he take?",
      "کتابوں کی دکان پر 4 قلم 120 روپے کے ہیں۔ علی کو اپنی جماعت کے لیے 7 قلم چاہییں۔ وہ کتنے پیسے لے کر جائے؟"),
    "text": T("Today we learn a simple trick for questions like this. First, a quick check.",
              "آج ہم ایسے سوالوں کے لیے ایک آسان طریقہ سیکھیں گے۔ پہلے ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("What is 120 ÷ 4?", "120 ÷ 4 کتنا ہے؟"),
     PEN,
     T("4 × 3 = 12, so think of 4 × 30.", "4 × 3 = 12، اس لیے 4 × 30 کے بارے میں سوچیں۔"),
     T("Yes! 120 ÷ 4 = 30.", "جی ہاں! 120 ÷ 4 = 30"),
     T("4 × 30 = 120, so 120 ÷ 4 = 30.", "4 × 30 = 120، اس لیے 120 ÷ 4 = 30"),
     common_wrong=[wrong(3, "4 × 3 = 12, not 120. Try 4 × 30.", "4 × 3 = 12 ہے، 120 نہیں۔ 4 × 30 آزمائیں۔")],
     qtype="recall", skill=TIMES_TABLES),
   {"id": "s3_predict", "type": "choice",
    "prompt": T("Guess first: 4 pens cost Rs 120. How much do 7 pens cost?", "پہلے اندازہ لگائیں: 4 قلم 120 روپے کے ہیں۔ 7 قلم کتنے کے ہوں گے؟"),
    "options": [
      opt("added", f"Rs {120 + 3}: 3 more pens, 3 more rupees", f"{120 + 3} روپے: 3 قلم زیادہ، 3 روپے زیادہ", False,
          "A pen costs much more than Rs 1! Let's find the price of one pen.", "ایک قلم 1 روپے سے کہیں زیادہ کا ہے! آئیں ایک قلم کی قیمت معلوم کریں۔", "additive_thinking"),
      opt("times", f"Rs {120 * 7}: 120 × 7", f"{120 * 7} روپے: 120 × 7", False,
          "Rs 120 is the price of 4 pens, not 1. Let's find the price of one pen.", "120 روپے 4 قلموں کی قیمت ہے، 1 کی نہیں۔ آئیں ایک قلم کی قیمت معلوم کریں۔", "skips_unit"),
      opt("right", f"Rs {SEVEN_PENS}", f"{SEVEN_PENS} روپے", True,
          "Good thinking! Let's see how to work it out.", "بہت خوب سوچا! آئیں دیکھیں اسے کیسے نکالتے ہیں۔"),
    ]},
   {"id": "s4_method", "type": "explain",
    "character": say("happy", "Find ONE first, then any number is easy!", "پہلے ایک معلوم کریں، پھر کوئی بھی تعداد آسان ہے!"),
    "text": T(f"Step 1, find one: 4 pens cost Rs 120, so 1 pen costs 120 ÷ 4 = Rs {PEN}. Step 2, find the number you want: 7 pens cost 7 × {PEN} = Rs {SEVEN_PENS}. This is the unitary method (\"unit\" means one). It works when twice as many things cost twice as much: this is called direct proportion.",
              f"پہلا قدم، ایک معلوم کریں: 4 قلم 120 روپے کے ہیں، اس لیے 1 قلم 120 ÷ 4 = {PEN} روپے کا۔ دوسرا قدم، مطلوبہ تعداد: 7 قلم 7 × {PEN} = {SEVEN_PENS} روپے کے۔ یہ اکائی کا طریقہ ہے (اکائی یعنی ایک)۔ یہ تب کام کرتا ہے جب دگنی چیزوں کی قیمت بھی دگنی ہو: اسے راست تناسب کہتے ہیں۔")},
   number_question(
     "s5_one_kg",
     T("5 kg of sugar cost Rs 750. How much does 1 kg cost, in rupees?", "5 کلوگرام چینی 750 روپے کی ہے۔ 1 کلوگرام کتنے روپے کی ہے؟"),
     SUGAR,
     T("Share Rs 750 equally among 5 kg.", "750 روپے کو 5 کلوگرام میں برابر بانٹیں۔"),
     T(f"Right! 750 ÷ 5 = Rs {SUGAR} for 1 kg.", f"درست! 1 کلوگرام: 750 ÷ 5 = {SUGAR} روپے۔"),
     T(f"Divide the price by the number of kg: 750 ÷ 5 = Rs {SUGAR}.", f"قیمت کو کلوگرام کی تعداد سے تقسیم کریں: 750 ÷ 5 = {SUGAR} روپے۔"),
     qtype="recall",
     common_wrong=[wrong(750 * 5, "1 kg must cost less than 5 kg. Divide, don't multiply.", "1 کلوگرام، 5 کلوگرام سے سستا ہوگا۔ تقسیم کریں، ضرب نہیں۔", "divides_wrong_way")]),
   number_question(
     "s6_eggs",
     T("6 eggs cost Rs 180. How much do 10 eggs cost, in rupees?", "6 انڈے 180 روپے کے ہیں۔ 10 انڈے کتنے روپے کے ہوں گے؟"),
     TEN_EGGS,
     T("Find the price of 1 egg first: 180 ÷ 6.", "پہلے 1 انڈے کی قیمت معلوم کریں: 180 ÷ 6"),
     T(f"Right! 1 egg costs Rs {EGG}, so 10 eggs cost 10 × {EGG} = Rs {TEN_EGGS}.", f"درست! 1 انڈا {EGG} روپے کا، اس لیے 10 انڈے 10 × {EGG} = {TEN_EGGS} روپے کے۔"),
     T(f"1 egg: 180 ÷ 6 = Rs {EGG}. 10 eggs: 10 × {EGG} = Rs {TEN_EGGS}.", f"1 انڈا: 180 ÷ 6 = {EGG} روپے۔ 10 انڈے: 10 × {EGG} = {TEN_EGGS} روپے۔"),
     common_wrong=[wrong(184, "4 more eggs don't cost Rs 4. Find the price of one egg first.", "4 انڈے زیادہ کی قیمت 4 روپے نہیں۔ پہلے ایک انڈے کی قیمت معلوم کریں۔", "additive_thinking"),
                   wrong(1800, "Rs 180 is for 6 eggs, not 1. Divide by 6 first.", "180 روپے 6 انڈوں کے ہیں، 1 کے نہیں۔ پہلے 6 سے تقسیم کریں۔", "skips_unit"),
                   wrong(EGG, f"Rs {EGG} is one egg. You need 10.", f"{EGG} روپے ایک انڈے کی قیمت ہے۔ آپ کو 10 چاہییں۔")]),
   number_question(
     "s7_bus",
     T("A bus goes 150 km in 3 hours at the same speed. How far does it go in 5 hours, in km?", "ایک بس ایک ہی رفتار سے 3 گھنٹوں میں 150 کلومیٹر چلتی ہے۔ 5 گھنٹوں میں کتنے کلومیٹر چلے گی؟"),
     FIVE_HOURS,
     T("How far does it go in 1 hour?", "1 گھنٹے میں کتنا چلتی ہے؟"),
     T(f"Right! {KM_PER_HOUR} km in 1 hour, so 5 × {KM_PER_HOUR} = {FIVE_HOURS} km.", f"درست! 1 گھنٹے میں {KM_PER_HOUR} کلومیٹر، اس لیے 5 × {KM_PER_HOUR} = {FIVE_HOURS} کلومیٹر۔"),
     T(f"1 hour: 150 ÷ 3 = {KM_PER_HOUR} km. 5 hours: 5 × {KM_PER_HOUR} = {FIVE_HOURS} km.", f"1 گھنٹہ: 150 ÷ 3 = {KM_PER_HOUR} کلومیٹر۔ 5 گھنٹے: 5 × {KM_PER_HOUR} = {FIVE_HOURS} کلومیٹر۔"),
     common_wrong=[wrong(152, "2 more hours means much more than 2 km. Find 1 hour first.", "2 گھنٹے زیادہ کا مطلب 2 کلومیٹر سے بہت زیادہ ہے۔ پہلے 1 گھنٹہ معلوم کریں۔", "additive_thinking"),
                   wrong(750, "150 km is for 3 hours, not 1. Divide by 3 first.", "150 کلومیٹر 3 گھنٹوں کے ہیں، 1 کا نہیں۔ پہلے 3 سے تقسیم کریں۔", "skips_unit")]),
   {"id": "s8_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("3 notebooks cost Rs 90. Rehan says 5 notebooks cost 90 + 2 = Rs 92. What went wrong?",
                "3 کاپیاں 90 روپے کی ہیں۔ ریحان کہتا ہے 5 کاپیاں 90 + 2 = 92 روپے کی ہیں۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("unit", f"He added 2 rupees for 2 notebooks. 1 notebook is Rs {NOTEBOOK}, so 5 cost Rs {FIVE_NOTEBOOKS}.", f"اس نے 2 کاپیوں کے 2 روپے جمع کیے۔ 1 کاپی {NOTEBOOK} روپے کی، اس لیے 5 کاپیاں {FIVE_NOTEBOOKS} روپے کی۔", True,
          f"Yes! 90 ÷ 3 = {NOTEBOOK}, then 5 × {NOTEBOOK} = {FIVE_NOTEBOOKS}.", f"جی ہاں! 90 ÷ 3 = {NOTEBOOK}، پھر 5 × {NOTEBOOK} = {FIVE_NOTEBOOKS}"),
      opt("nothing", "Nothing. 5 notebooks cost a bit more than 3.", "کوئی غلطی نہیں۔ 5 کاپیاں 3 سے تھوڑی مہنگی ہیں۔", False,
          "Each notebook costs Rs 30, so 2 more cost Rs 60 more, not Rs 2.", "ہر کاپی 30 روپے کی ہے، اس لیے 2 زیادہ کی قیمت 60 روپے زیادہ، 2 روپے نہیں۔", "additive_thinking"),
      opt("times", "He should do 90 × 5 = Rs 450.", "اسے 90 × 5 = 450 روپے کرنا چاہیے۔", False,
          "Rs 90 is for 3 notebooks. Find one first: 90 ÷ 3.", "90 روپے 3 کاپیوں کے ہیں۔ پہلے ایک معلوم کریں: 90 ÷ 3", "skips_unit"),
    ]},
   number_question(
     "s9_atta",
     T("8 kg of atta cost Rs 960. How many kg can you buy with Rs 600?", "8 کلوگرام آٹا 960 روپے کا ہے۔ 600 روپے میں کتنے کلوگرام آٹا آئے گا؟"),
     ATTA_FOR_600,
     T("First find the price of 1 kg. Then: how many of those fit in Rs 600?", "پہلے 1 کلوگرام کی قیمت معلوم کریں۔ پھر: 600 روپے میں ایسے کتنے آتے ہیں؟"),
     T(f"Right! 1 kg costs 960 ÷ 8 = Rs {ATTA_KG}, so Rs 600 buys 600 ÷ {ATTA_KG} = {ATTA_FOR_600} kg.", f"درست! 1 کلوگرام 960 ÷ 8 = {ATTA_KG} روپے کا، اس لیے 600 روپے میں 600 ÷ {ATTA_KG} = {ATTA_FOR_600} کلوگرام۔"),
     T(f"1 kg: 960 ÷ 8 = Rs {ATTA_KG}. Rs 600 ÷ {ATTA_KG} = {ATTA_FOR_600} kg.", f"1 کلوگرام: 960 ÷ 8 = {ATTA_KG} روپے۔ 600 ÷ {ATTA_KG} = {ATTA_FOR_600} کلوگرام۔"),
     common_wrong=[wrong(ATTA_KG, f"Rs {ATTA_KG} is the price of 1 kg. How many kg does Rs 600 buy?", f"{ATTA_KG} روپے 1 کلوگرام کی قیمت ہے۔ 600 روپے میں کتنے کلوگرام آئیں گے؟")]),
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Can you teach me? Why do we find the price of ONE pen first?",
                     "کیا آپ مجھے سمجھا سکتے ہیں؟ ہم پہلے ایک قلم کی قیمت کیوں معلوم کرتے ہیں؟"),
    "task": T("In your own words: 4 pens cost Rs 120. Why do we find the price of 1 pen before working out 7 pens?",
              "اپنے الفاظ میں بتائیں: 4 قلم 120 روپے کے ہیں۔ 7 قلموں کی قیمت نکالنے سے پہلے ہم 1 قلم کی قیمت کیوں معلوم کرتے ہیں؟"),
    "key_idea": "Rs 120 is the price of 4 pens, not of 7. Once we know one pen costs Rs 30, we can find the price of any number of pens by multiplying: 7 × 30 = Rs 210.",
    "levels": {
      "got_it": "Says that Rs 120 is for 4 pens, and knowing the price of one (Rs 30) lets you multiply by any number, such as 7.",
      "partly": "Says to divide by 4 or mentions Rs 30, but does not explain why one pen helps to find 7 pens.",
      "not_yet": "Says to add or multiply 120 directly, gives no reason, or the reasoning is wrong."},
    "keywords": [
      ["one", "1", "single", "ایک", "ek"],
      ["30", "تیس", "tees"],
      ["multiply", "any", "times", "×", "ضرب", "کوئی بھی", "zarb", "koi bhi"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Once you know 1 pen is Rs 30, any number of pens is easy: 7 × 30 = Rs 210.",
                  "بہت خوب سمجھایا! جب پتا ہو کہ 1 قلم 30 روپے کا ہے تو کتنے بھی قلم آسان ہیں: 7 × 30 = 210 روپے۔"),
      "partly": T("Good start! Now say how the price of one pen helps you find the price of 7.", "اچھی شروعات! اب بتائیں کہ ایک قلم کی قیمت 7 قلموں کی قیمت نکالنے میں کیسے مدد کرتی ہے۔"),
      "not_yet": T("Think: Rs 120 buys 4 pens. Is that the price of 7 pens, or of 1 pen? What do we need?",
                   "سوچیں: 120 روپے میں 4 قلم آتے ہیں۔ کیا یہ 7 قلموں کی قیمت ہے یا 1 قلم کی؟ ہمیں کیا چاہیے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_bananas",
     T("A dozen (12) bananas cost Rs 144. How much do 5 bananas cost, in rupees?", "ایک درجن (12) کیلے 144 روپے کے ہیں۔ 5 کیلے کتنے روپے کے ہوں گے؟"),
     FIVE_BANANAS,
     T("1 banana: 144 ÷ 12.", "1 کیلا: 144 ÷ 12"),
     T(f"Right! 1 banana is Rs {BANANA}, so 5 cost 5 × {BANANA} = Rs {FIVE_BANANAS}.", f"درست! 1 کیلا {BANANA} روپے کا، اس لیے 5 کیلے 5 × {BANANA} = {FIVE_BANANAS} روپے کے۔"),
     T(f"144 ÷ 12 = Rs {BANANA} for one. 5 × {BANANA} = Rs {FIVE_BANANAS}.", f"ایک کیلا: 144 ÷ 12 = {BANANA} روپے۔ 5 × {BANANA} = {FIVE_BANANAS} روپے۔"),
     common_wrong=[wrong(BANANA, f"Rs {BANANA} is one banana. You need 5.", f"{BANANA} روپے ایک کیلے کی قیمت ہے۔ آپ کو 5 چاہییں۔"),
                   wrong(137, "7 fewer bananas save much more than Rs 7. Find one banana first.", "7 کیلے کم ہونے سے 7 روپے سے کہیں زیادہ بچتے ہیں۔ پہلے ایک کیلا معلوم کریں۔", "additive_thinking")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Now you can work out prices for any number of things!", "اب آپ کسی بھی تعداد کی چیزوں کی قیمت نکال سکتے ہیں!"),
    "text": T("Unitary method: first find the value of ONE (divide), then multiply by the number you want. Check that the answer makes sense: more things cost more, fewer cost less.",
              "اکائی کا طریقہ: پہلے ایک کی قیمت معلوم کریں (تقسیم)، پھر مطلوبہ تعداد سے ضرب دیں۔ جانچیں کہ جواب درست لگتا ہے: زیادہ چیزیں زیادہ کی، کم چیزیں کم کی۔"),
    "points": [T("4 pens Rs 120 → 1 pen Rs 30 → 7 pens Rs 210", "4 قلم 120 روپے ← 1 قلم 30 روپے ← 7 قلم 210 روپے"),
               T("Don't add the difference: 3 more pens don't cost Rs 3 more.", "فرق جمع نہ کریں: 3 قلم زیادہ کی قیمت 3 روپے زیادہ نہیں۔")]},
 ],
 "review_questions": [
   {"id": "r_rice", "type": "apply", "skill": SKILL, "step": number_question(
     "r_rice",
     T("5 kg of rice cost Rs 250. How much do 8 kg cost, in rupees?", "5 کلوگرام چاول 250 روپے کے ہیں۔ 8 کلوگرام کتنے روپے کے ہوں گے؟"),
     400,
     T("1 kg: 250 ÷ 5.", "1 کلوگرام: 250 ÷ 5"),
     T("Right! 1 kg is Rs 50, so 8 kg cost Rs 400.", "درست! 1 کلوگرام 50 روپے، اس لیے 8 کلوگرام 400 روپے۔"),
     T("250 ÷ 5 = 50 for 1 kg. 8 × 50 = Rs 400.", "1 کلوگرام: 250 ÷ 5 = 50۔ 8 × 50 = 400 روپے۔"),
     common_wrong=[wrong(253, "3 more kg don't cost Rs 3 more. Find 1 kg first.", "3 کلوگرام زیادہ کی قیمت 3 روپے زیادہ نہیں۔ پہلے 1 کلوگرام معلوم کریں۔", "additive_thinking"),
                   wrong(2000, "Rs 250 is for 5 kg. Divide by 5 first.", "250 روپے 5 کلوگرام کے ہیں۔ پہلے 5 سے تقسیم کریں۔", "skips_unit")],
     qtype=None)},
   {"id": "r_juice", "type": "apply", "skill": SKILL, "step": number_question(
     "r_juice",
     T("4 bottles of juice cost Rs 200. How much do 9 bottles cost, in rupees?", "جوس کی 4 بوتلیں 200 روپے کی ہیں۔ 9 بوتلیں کتنے روپے کی ہوں گی؟"),
     450,
     T("1 bottle: 200 ÷ 4.", "1 بوتل: 200 ÷ 4"),
     T("Right! 1 bottle is Rs 50, so 9 cost Rs 450.", "درست! 1 بوتل 50 روپے، اس لیے 9 بوتلیں 450 روپے۔"),
     T("200 ÷ 4 = 50 for one. 9 × 50 = Rs 450.", "ایک بوتل: 200 ÷ 4 = 50۔ 9 × 50 = 450 روپے۔"),
     common_wrong=[wrong(1800, "Rs 200 is for 4 bottles. Divide by 4 first.", "200 روپے 4 بوتلوں کے ہیں۔ پہلے 4 سے تقسیم کریں۔", "skips_unit")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Ratio and Proportion unit. No textbook text or exercises were used. Prices are round numbers for the sums, not real market prices.",
   "Unit number to be confirmed against the PCTB Grade 6 book: the files are named g6-maths-06. Fix the names and curriculum_refs if the unit differs.",
   "Urdu terms to check against the Punjab textbook: اکائی کا طریقہ (unitary method), راست تناسب (direct proportion).",
   "Only direct proportion is taught here; inverse proportion (more workers, fewer days) is left for a later lesson.",
   "s9 works the method backwards (how much can I buy?), which many children find harder.",
   "The numbers were worked out in content/sources/g6-maths-06/unitary_method.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
assert 120 + 3 == 123 and 150 + 2 == 152 and 144 - 7 == 137 and 250 + 3 == 253
# ---------- pictures ----------
from figs import attach, double_line


def unit_line(one, n, marks, tags, alt_en, alt_ur, **kw):
    """A double number line: each step is 1 thing on top and `one` (its
    value) below; marks {count: (top, bottom)}."""
    return double_line(1, one, n, marks, alt_en, alt_ur, tags=tags, **kw)


attach(lesson, {
  "s1_hook": unit_line(
    PEN, 7, {4: ("4", "120"), 7: ("7", "?")}, ("", "Rs"),
    "A double number line in steps of one pen. On top, 4 pens and 7 pens; below, Rs 120 under the 4 and a question mark under the 7.",
    "ایک ایک قلم کے قدموں والی دوہری عددی لکیر۔ اوپر 4 قلم اور 7 قلم؛ نیچے 4 کے نیچے Rs 120 اور 7 کے نیچے سوالیہ نشان۔"),
  "s4_method": unit_line(
    PEN, 7, {1: ("1", str(PEN)), 4: ("4", "120"), 7: ("7", str(SEVEN_PENS))}, ("", "Rs"),
    f"A double number line in steps of one pen. On top 1, 4 and 7 pens; below them Rs {PEN}, Rs 120 and Rs {SEVEN_PENS}.",
    f"ایک ایک قلم کے قدموں والی دوہری عددی لکیر۔ اوپر 1، 4 اور 7 قلم؛ ان کے نیچے Rs {PEN}، Rs 120 اور Rs {SEVEN_PENS}۔"),
  "s5_one_kg": unit_line(
    SUGAR, 5, {1: ("1", "?"), 5: ("5", "750")}, ("kg", "Rs"),
    "A double number line in steps of 1 kg. On top, 1 kg and 5 kg; below, a question mark under the 1 and Rs 750 under the 5.",
    "1 کلوگرام کے قدموں والی دوہری عددی لکیر۔ اوپر 1 کلوگرام اور 5 کلوگرام؛ نیچے 1 کے نیچے سوالیہ نشان اور 5 کے نیچے Rs 750۔"),
  "s6_eggs": unit_line(
    EGG, 10, {6: ("6", "180"), 10: ("10", "?")}, ("", "Rs"),
    "A double number line in steps of one egg. On top, 6 eggs and 10 eggs; below, Rs 180 under the 6 and a question mark under the 10.",
    "ایک ایک انڈے کے قدموں والی دوہری عددی لکیر۔ اوپر 6 انڈے اور 10 انڈے؛ نیچے 6 کے نیچے Rs 180 اور 10 کے نیچے سوالیہ نشان۔"),
  "s7_bus": unit_line(
    KM_PER_HOUR, 5, {3: ("3", "150"), 5: ("5", "?")}, ("h", "km"),
    "A double number line in steps of one hour. On top, 3 hours and 5 hours; below, 150 km under the 3 and a question mark under the 5.",
    "ایک ایک گھنٹے کے قدموں والی دوہری عددی لکیر۔ اوپر 3 گھنٹے اور 5 گھنٹے؛ نیچے 3 کے نیچے 150 کلومیٹر اور 5 کے نیچے سوالیہ نشان۔"),
  "s9_atta": unit_line(
    ATTA_KG, 8, {8: ("8", "960"), ATTA_FOR_600: ("?", "600")}, ("kg", "Rs"),
    "A double number line for atta: kg on top, rupees below. 8 kg is over Rs 960. Further left, Rs 600 has a question mark over it.",
    "آٹے کی دوہری عددی لکیر: اوپر کلوگرام، نیچے روپے۔ 8 کلوگرام Rs 960 کے اوپر ہے۔ اس سے بائیں طرف Rs 600 کے اوپر سوالیہ نشان ہے۔",
    ticks=False),
  "s11_bananas": unit_line(
    BANANA, 12, {5: ("5", "?"), 12: ("12", "144")}, ("", "Rs"),
    "A double number line in steps of one banana. On top, 5 and 12 bananas; below, a question mark under the 5 and Rs 144 under the 12.",
    "ایک ایک کیلے کے قدموں والی دوہری عددی لکیر۔ اوپر 5 اور 12 کیلے؛ نیچے 5 کے نیچے سوالیہ نشان اور 12 کے نیچے Rs 144۔"),
  "qb_mangoes": unit_line(
    84 // 7, 7, {3: ("3", "?"), 7: ("7", "84")}, ("", "Rs"),
    "A double number line in steps of one mango. On top, 3 and 7 mangoes; below, a question mark under the 3 and Rs 84 under the 7.",
    "ایک ایک آم کے قدموں والی دوہری عددی لکیر۔ اوپر 3 اور 7 آم؛ نیچے 3 کے نیچے سوالیہ نشان اور 7 کے نیچے Rs 84۔"),
  "r_rice": unit_line(
    250 // 5, 8, {5: ("5", "250"), 8: ("8", "?")}, ("kg", "Rs"),
    "A double number line in steps of 1 kg of rice. On top, 5 kg and 8 kg; below, Rs 250 under the 5 and a question mark under the 8.",
    "چاول کے 1 کلوگرام کے قدموں والی دوہری عددی لکیر۔ اوپر 5 کلوگرام اور 8 کلوگرام؛ نیچے 5 کے نیچے Rs 250 اور 8 کے نیچے سوالیہ نشان۔"),
})
write(lesson)
