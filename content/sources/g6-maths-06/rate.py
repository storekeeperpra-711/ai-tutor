from common import (T, opt, say, wrong, number_question, write,
                    BOOK, REVIEW, UNITARY, RATIO_RATE)

SKILL = RATIO_RATE


def rate(amount, units):
    """How much for one unit: rate(1000, 4) is 250 (per one)."""
    r, rest = divmod(amount, units)
    assert rest == 0, (amount, units)
    return r


# s2: 5 pens cost Rs 75, one pen (times instead of divide: 375)
S2 = rate(75, 5)
assert S2 == 15
# s4: 4 kg rice for Rs 1,000, rate per kg (times: 4,000)
S4 = rate(1000, 4)
assert S4 == 250
# s5: 180 km in 3 hours (times: 540)
S5 = rate(180, 3)
assert S5 == 60
# s7: 240 words in 6 minutes
S7 = rate(240, 6)
assert S7 == 40
# s8: petrol Rs 260 per litre, 5 litres (divided: 52)
S8 = 260 * 5
assert S8 == 1300 and 260 // 5 == 52
# s9: 60 litres in 4 minutes is 15 litres per minute
assert rate(60, 4) == 15
# s10: 2 kg for Rs 300 vs 5 kg for Rs 700
assert rate(300, 2) == 150 and rate(700, 5) == 140
# s11: 12 eggs for Rs 324 (the 6 eggs pack: Rs 30 each)
S11 = rate(324, 12)
assert S11 == 27 and rate(180, 6) == 30
# question bank: 45 km in 3 hours; 3 kg apples for Rs 450
QB = rate(45, 3)
assert QB == 15 and 45 * 3 == 135
assert rate(450, 3) == 150
# review: 360 bottles in 6 hours; Rs 35 a pen, 8 pens
R1 = rate(360, 6)
assert R1 == 60
R2 = 35 * 8
assert R2 == 280

lesson = {
 "id": "g6-maths-06-rate",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Find a rate as an amount for one unit, and use rates to solve real-life problems.", "textbook": f"{BOOK}, 4.1 Rate"}],
 "skills": [SKILL],
 "title": T("Rate", "شرح"),
 "estimated_minutes": 13,
 "prerequisites": [{"skill": UNITARY}],
 "misconceptions": [
   {"id": "multiply_not_divide", "description": "Multiplies the two amounts instead of dividing to find the amount for one."},
   {"id": "upside_down_rate", "description": "Divides the wrong way round (minutes ÷ litres instead of litres ÷ minutes)."},
   {"id": "divide_not_multiply", "description": "Divides when using a rate to find the amount for many."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_meaning", "type": "recall", "step": {
     "id": "qb_meaning", "type": "choice",
     "prompt": T("'Rs 250 per kg' means …", "'250 روپے فی کلو' کا مطلب ہے …"),
     "options": [
       opt("each_kg", "Rs 250 for each 1 kg", "ہر 1 کلو کے 250 روپے", True,
           "Yes! 'Per' means 'for each one'.", "جی ہاں! 'فی' یعنی 'ہر ایک کے لیے'۔"),
       opt("all", "Rs 250 for all the rice in the shop", "دکان کے سارے چاول 250 روپے کے", False,
           "'Per kg' means for each kilogram, not for all of it.", "'فی کلو' یعنی ہر کلو کے لیے، سب کے لیے نہیں۔"),
       opt("kg_per_rupee", "250 kg for each rupee", "ہر روپے کے 250 کلو", False,
           "That is upside down. It is rupees for each kilogram.", "یہ اُلٹا ہے۔ یہ ہر کلو کے روپے ہیں۔", "upside_down_rate"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("A cyclist rides 45 km in 3 hours. What is her speed in km per hour?", "ایک سائیکل سوار 3 گھنٹوں میں 45 کلومیٹر چلاتی ہے۔ اس کی رفتار کتنے کلومیٹر فی گھنٹہ ہے؟"),
     QB,
     T("km for one hour: divide by the hours.", "ایک گھنٹے کے کلومیٹر: گھنٹوں سے تقسیم کریں۔"),
     T("Right! 15 km per hour.", "درست! 15 کلومیٹر فی گھنٹہ"),
     T("45 ÷ 3 = 15 km per hour.", "45 ÷ 3 = 15 کلومیٹر فی گھنٹہ"),
     common_wrong=[wrong(135, "Divide, don't multiply: 45 ÷ 3 = 15.", "ضرب نہیں، تقسیم کریں: 45 ÷ 3 = 15", "multiply_not_divide")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("3 kg of apples cost Rs 450. Sara says 1 kg costs Rs 1,350. What is wrong?", "3 کلو سیب 450 روپے کے ہیں۔ سارہ کہتی ہے 1 کلو 1,350 روپے کا ہے۔ کیا غلطی ہے؟"),
     "options": [
       opt("divide", "She multiplied. 1 kg is less: 450 ÷ 3 = Rs 150.", "اس نے ضرب دی۔ 1 کلو سستا ہوگا: 450 ÷ 3 = 150 روپے", True,
           "Yes! One kilogram costs less than three.", "جی ہاں! ایک کلو تین کلو سے سستا ہے۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "1 kg can't cost more than 3 kg. 450 ÷ 3 = 150.", "1 کلو، 3 کلو سے مہنگا نہیں ہو سکتا۔ 450 ÷ 3 = 150", "multiply_not_divide"),
       opt("add", "She should add: 450 + 3 = 453.", "اسے جمع کرنا چاہیے: 450 + 3 = 453", False,
           "For one kg, share the price by 3: 450 ÷ 3 = 150.", "ایک کلو کے لیے قیمت کو 3 پر بانٹیں: 450 ÷ 3 = 150"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_rate", "front": T("Rate?", "شرح؟"),
    "back": T("How much of one thing for each one of another: Rs 250 per kg, 60 km per hour.", "ایک چیز کی مقدار، دوسری کی ہر اکائی کے لیے: 250 روپے فی کلو، 60 کلومیٹر فی گھنٹہ۔")},
   {"id": "f_find", "front": T("How to find a rate?", "شرح کیسے نکالیں؟"),
    "back": T("Divide the amount by the number of units: 180 km ÷ 3 h = 60 km/h.", "مقدار کو اکائیوں کی تعداد سے تقسیم کریں: 180 کلومیٹر ÷ 3 گھنٹے = 60 کلومیٹر فی گھنٹہ")},
 ],
 "home_tasks": [{"id": "h_shop", "text": T(
   "Look at two packs of the same thing at home or in a shop (like 1 kg and 5 kg of sugar). Find the price per kg of each. Which is the better buy?",
   "گھر یا دکان میں ایک ہی چیز کے دو پیکٹ دیکھیں (جیسے 1 کلو اور 5 کلو چینی)۔ ہر ایک کی فی کلو قیمت نکالیں۔ کون سا سستا سودا ہے؟")}],
 "glossary": [T("Rate", "شرح"), T("Per", "فی"), T("Speed", "رفتار")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Rice is Rs 250 per kg. The bus goes 60 km per hour. What does 'per' really mean?",
                     "چاول 250 روپے فی کلو ہیں۔ بس 60 کلومیٹر فی گھنٹہ چلتی ہے۔ 'فی' کا اصل مطلب کیا ہے؟"),
    "text": T("Today we learn about rates: how much for each one. First, the unitary method.", "آج ہم شرح کے بارے میں سیکھیں گے: ہر ایک کے لیے کتنا۔ پہلے اکائی کا طریقہ۔")},
   number_question(
     "s2_foundation",
     T("5 pens cost Rs 75. How much does 1 pen cost?", "5 قلم 75 روپے کے ہیں۔ 1 قلم کتنے کا ہے؟"),
     S2,
     T("Share Rs 75 among 5 pens.", "75 روپے کو 5 قلموں میں بانٹیں۔"),
     T("Right! 75 ÷ 5 = Rs 15.", "درست! 75 ÷ 5 = 15 روپے"),
     T("75 ÷ 5 = 15, so one pen is Rs 15.", "75 ÷ 5 = 15، تو ایک قلم 15 روپے کا ہے۔"),
     common_wrong=[wrong(375, "One pen costs less than five. Divide: 75 ÷ 5 = 15.", "ایک قلم پانچ سے سستا ہے۔ تقسیم کریں: 75 ÷ 5 = 15", "multiply_not_divide")],
     qtype="recall", skill=UNITARY),
   {"id": "s3_rule", "type": "explain",
    "character": say("happy", "'Per' means 'for each one'. To find a rate, divide by the number of units!", "'فی' یعنی 'ہر ایک کے لیے'۔ شرح نکالنے کے لیے اکائیوں کی تعداد سے تقسیم کریں!"),
    "text": T("A rate compares two different kinds of quantity, like rupees and kilograms, or kilometres and hours. It tells how much for ONE unit, and we say 'per': Rs 250 per kg, 60 km per hour (60 km/h). To find a rate, divide: 4 kg cost Rs 1,000, so the rate is 1,000 ÷ 4 = Rs 250 per kg. A ratio like 3:5 compares quantities of the same kind.",
              "شرح دو مختلف قسم کی مقداروں کا موازنہ ہے، جیسے روپے اور کلوگرام، یا کلومیٹر اور گھنٹے۔ یہ ایک اکائی کے لیے مقدار بتاتی ہے، اور ہم 'فی' کہتے ہیں: 250 روپے فی کلو، 60 کلومیٹر فی گھنٹہ (60 km/h)۔ شرح نکالنے کے لیے تقسیم کریں: 4 کلو 1,000 روپے کے ہیں، تو شرح 1,000 ÷ 4 = 250 روپے فی کلو۔ 3:5 جیسی نسبت ایک ہی قسم کی مقداروں کا موازنہ کرتی ہے۔")},
   number_question(
     "s4_rice",
     T("4 kg of rice cost Rs 1,000. What is the rate in rupees per kg?", "4 کلو چاول 1,000 روپے کے ہیں۔ شرح کتنے روپے فی کلو ہے؟"),
     S4,
     T("Rupees for 1 kg: divide by 4.", "1 کلو کے روپے: 4 سے تقسیم کریں۔"),
     T("Right! Rs 250 per kg.", "درست! 250 روپے فی کلو"),
     T("1,000 ÷ 4 = 250, so Rs 250 per kg.", "1,000 ÷ 4 = 250، تو 250 روپے فی کلو"),
     common_wrong=[wrong(4000, "Divide, don't multiply: 1,000 ÷ 4 = 250.", "ضرب نہیں، تقسیم کریں: 1,000 ÷ 4 = 250", "multiply_not_divide")]),
   number_question(
     "s5_bus",
     T("A bus travels 180 km in 3 hours. What is its speed in km per hour?", "ایک بس 3 گھنٹوں میں 180 کلومیٹر چلتی ہے۔ اس کی رفتار کتنے کلومیٹر فی گھنٹہ ہے؟"),
     S5,
     T("km for 1 hour: divide by 3.", "1 گھنٹے کے کلومیٹر: 3 سے تقسیم کریں۔"),
     T("Right! 60 km/h.", "درست! 60 کلومیٹر فی گھنٹہ"),
     T("180 ÷ 3 = 60 km per hour.", "180 ÷ 3 = 60 کلومیٹر فی گھنٹہ"),
     common_wrong=[wrong(540, "In one hour the bus goes less than in three. 180 ÷ 3 = 60.", "ایک گھنٹے میں بس تین سے کم چلتی ہے۔ 180 ÷ 3 = 60", "multiply_not_divide")]),
   {"id": "s6_which", "type": "choice",
    "prompt": T("Which of these is a rate?", "ان میں سے شرح کون سی ہے؟"),
    "options": [
      opt("per_dozen", "Rs 120 per dozen eggs", "120 روپے فی درجن انڈے", True,
          "Yes! Rupees for each dozen: two different kinds of quantity.", "جی ہاں! ہر درجن کے روپے: دو مختلف قسم کی مقداریں۔"),
      opt("boys_girls", "Boys to girls is 3:5", "لڑکے اور لڑکیاں 3:5", False,
          "Boys and girls are the same kind (people): that is a ratio.", "لڑکے اور لڑکیاں ایک ہی قسم (لوگ) ہیں: یہ نسبت ہے۔"),
      opt("fifteen_kg", "15 kg", "15 کلو", False,
          "That is just one amount. A rate is 'something per something'.", "یہ صرف ایک مقدار ہے۔ شرح 'کچھ فی کچھ' ہوتی ہے۔"),
    ]},
   number_question(
     "s7_typing",
     T("Ayesha types 240 words in 6 minutes. How many words per minute is that?", "عائشہ 6 منٹ میں 240 الفاظ ٹائپ کرتی ہے۔ یہ کتنے الفاظ فی منٹ ہیں؟"),
     S7,
     T("Words for 1 minute: divide by 6.", "1 منٹ کے الفاظ: 6 سے تقسیم کریں۔"),
     T("Right! 40 words per minute.", "درست! 40 الفاظ فی منٹ"),
     T("240 ÷ 6 = 40 words per minute.", "240 ÷ 6 = 40 الفاظ فی منٹ"),
     common_wrong=[wrong(1440, "Divide, don't multiply: 240 ÷ 6 = 40.", "ضرب نہیں، تقسیم کریں: 240 ÷ 6 = 40", "multiply_not_divide")]),
   number_question(
     "s8_petrol",
     T("Petrol costs Rs 260 per litre. How much do 5 litres cost?", "پیٹرول 260 روپے فی لیٹر ہے۔ 5 لیٹر کتنے کے ہوں گے؟"),
     S8,
     T("Rs 260 for each litre, and there are 5 litres.", "ہر لیٹر کے 260 روپے، اور 5 لیٹر ہیں۔"),
     T("Right! 260 × 5 = Rs 1,300.", "درست! 260 × 5 = 1,300 روپے"),
     T("Each litre is Rs 260, so 5 litres are 260 × 5 = 1,300.", "ہر لیٹر 260 روپے کا، تو 5 لیٹر 260 × 5 = 1,300"),
     common_wrong=[wrong(52, "We know the price of 1 litre; 5 litres cost more. Multiply: 1,300.", "1 لیٹر کی قیمت معلوم ہے؛ 5 لیٹر مہنگے ہوں گے۔ ضرب دیں: 1,300", "divide_not_multiply")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("A tap fills 60 litres in 4 minutes. Usman says the rate is 4 ÷ 60 litres per minute. What is wrong?", "ایک نل 4 منٹ میں 60 لیٹر بھرتا ہے۔ عثمان کہتا ہے شرح 4 ÷ 60 لیٹر فی منٹ ہے۔ کیا غلطی ہے؟"),
    "options": [
      opt("flip", "Litres per minute is litres ÷ minutes: 60 ÷ 4 = 15.", "لیٹر فی منٹ یعنی لیٹر ÷ منٹ: 60 ÷ 4 = 15", True,
          "Yes! The 'per' amount goes on the bottom.", "جی ہاں! 'فی' والی مقدار نیچے آتی ہے۔"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "4 ÷ 60 is minutes per litre. Litres per minute: 60 ÷ 4 = 15.", "4 ÷ 60 منٹ فی لیٹر ہے۔ لیٹر فی منٹ: 60 ÷ 4 = 15", "upside_down_rate"),
      opt("times", "It should be 60 × 4 = 240.", "یہ 60 × 4 = 240 ہونا چاہیے۔", False,
          "In one minute the tap fills less than in four: 60 ÷ 4 = 15.", "ایک منٹ میں نل چار منٹ سے کم بھرتا ہے: 60 ÷ 4 = 15", "multiply_not_divide"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "The big bag costs more money. So the small bag is cheaper, right? Can you check?",
                     "بڑا تھیلا زیادہ پیسوں کا ہے۔ تو چھوٹا تھیلا سستا ہے نا؟ کیا آپ جانچ سکتے ہیں؟"),
    "task": T("A 2 kg bag of sugar costs Rs 300. A 5 kg bag costs Rs 700. Which is the better buy? Explain using the price per kg.", "چینی کا 2 کلو کا تھیلا 300 روپے کا ہے۔ 5 کلو کا تھیلا 700 روپے کا ہے۔ کون سا سستا سودا ہے؟ فی کلو قیمت سے وضاحت کریں۔"),
    "key_idea": "2 kg bag: 300 ÷ 2 = Rs 150 per kg. 5 kg bag: 700 ÷ 5 = Rs 140 per kg. The 5 kg bag is the better buy because each kilogram costs less, even though the bag costs more.",
    "levels": {
      "got_it": "Finds Rs 150 per kg and Rs 140 per kg and says the 5 kg bag is the better buy because each kg is cheaper.",
      "partly": "Finds one rate, or picks the 5 kg bag without comparing per kg.",
      "not_yet": "Picks the 2 kg bag because it costs less in total, or gives no reason."},
    "keywords": [
      ["150", "ڈیڑھ سو"],
      ["140", "ایک سو چالیس"],
      ["per kg", "each kg", "فی کلو", "ہر کلو"],
      ["5 kg", "big", "بڑا", "پانچ کلو"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Rs 140 per kg beats Rs 150.", "بہت خوب! 140 روپے فی کلو، 150 سے سستا ہے۔"),
      "partly": T("Good start! Work out the price of 1 kg in each bag.", "اچھی شروعات! ہر تھیلے میں 1 کلو کی قیمت نکالیں۔"),
      "not_yet": T("Divide each price by its kilograms. Which kg is cheaper?", "ہر قیمت کو اس کے کلو سے تقسیم کریں۔ کون سا کلو سستا ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_eggs",
     T("Pack A has 6 eggs for Rs 180. Pack B has 12 eggs for Rs 324. What is the price of one egg in pack B?", "پیکٹ A میں 6 انڈے 180 روپے کے ہیں۔ پیکٹ B میں 12 انڈے 324 روپے کے۔ پیکٹ B میں ایک انڈے کی قیمت کیا ہے؟"),
     S11,
     T("Divide pack B's price by its 12 eggs.", "پیکٹ B کی قیمت کو اس کے 12 انڈوں سے تقسیم کریں۔"),
     T("Right! Rs 27 an egg, cheaper than Rs 30 in pack A.", "درست! 27 روپے فی انڈا، پیکٹ A کے 30 روپے سے سستا۔"),
     T("324 ÷ 12 = 27, so Rs 27 per egg.", "324 ÷ 12 = 27، تو 27 روپے فی انڈا"),
     common_wrong=[wrong(30, "That is pack A (180 ÷ 6). Pack B: 324 ÷ 12 = 27.", "یہ پیکٹ A ہے (180 ÷ 6)۔ پیکٹ B: 324 ÷ 12 = 27")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Per kg, per hour, per minute: now you can find any rate and spot the better buy!", "فی کلو، فی گھنٹہ، فی منٹ: اب آپ کوئی بھی شرح نکال سکتے ہیں اور سستا سودا پہچان سکتے ہیں!"),
    "text": T("A rate is an amount for each one unit of something else. To find it, divide by the number of units. To use it, multiply by the number of units. To find the better buy, compare the price per unit.",
              "شرح کسی دوسری چیز کی ہر ایک اکائی کے لیے مقدار ہے۔ اسے نکالنے کے لیے اکائیوں کی تعداد سے تقسیم کریں۔ اسے استعمال کرنے کے لیے اکائیوں کی تعداد سے ضرب دیں۔ سستا سودا پہچاننے کے لیے فی اکائی قیمت کا موازنہ کریں۔"),
    "points": [T("Find a rate: divide.", "شرح نکالنا: تقسیم"),
               T("Use a rate: multiply.", "شرح استعمال کرنا: ضرب")]},
 ],
 "review_questions": [
   {"id": "r_bottles", "type": "apply", "skill": SKILL, "step": number_question(
     "r_bottles",
     T("A machine fills 360 bottles in 6 hours. How many bottles per hour?", "ایک مشین 6 گھنٹوں میں 360 بوتلیں بھرتی ہے۔ فی گھنٹہ کتنی بوتلیں؟"),
     R1,
     T("Divide by the hours.", "گھنٹوں سے تقسیم کریں۔"),
     T("Right! 60 bottles per hour.", "درست! 60 بوتلیں فی گھنٹہ"),
     T("360 ÷ 6 = 60 bottles per hour.", "360 ÷ 6 = 60 بوتلیں فی گھنٹہ"),
     common_wrong=[wrong(2160, "Divide, don't multiply: 360 ÷ 6 = 60.", "ضرب نہیں، تقسیم کریں: 360 ÷ 6 = 60", "multiply_not_divide")],
     qtype=None)},
   {"id": "r_pens", "type": "apply", "skill": SKILL, "step": number_question(
     "r_pens",
     T("Pens cost Rs 35 each. How much do 8 pens cost?", "قلم 35 روپے فی قلم ہیں۔ 8 قلم کتنے کے ہوں گے؟"),
     R2,
     T("Rs 35 for each of 8 pens.", "8 قلموں میں سے ہر ایک کے 35 روپے۔"),
     T("Right! 35 × 8 = Rs 280.", "درست! 35 × 8 = 280 روپے"),
     T("35 × 8 = 280.", "35 × 8 = 280"),
     common_wrong=[wrong(43, "Multiply, don't add: 35 × 8 = 280.", "جمع نہیں، ضرب دیں: 35 × 8 = 280")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh after matching the app with PCTB Mathematics 6 (Sub-domain 4, Rate). No textbook text or exercises were used.",
   "Rate is taught after the unitary method, which it uses: a rate is the amount for one unit.",
   "Urdu terms to check: شرح (rate), فی (per), رفتار (speed).",
   "The numbers were worked out in content/sources/g6-maths-06/rate.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
# ---------- pictures ----------
from figs import attach, bars, road

HOURS = ["1h", "2h", "3h"]

attach(lesson, {
  "s1_hook": bars(
    [(3, "Rs250", None, False)],
    "Three equal boxes in a row, each a bag of 1 kg of rice marked Rs 250: every kg costs Rs 250.",
    "ایک قطار میں تین برابر خانے، ہر خانہ 1 کلوگرام چاول کا تھیلا جس پر Rs 250 لکھا ہے: ہر کلوگرام Rs 250 کا ہے۔",
    box=64, under="1kg"),
  "s3_rule": bars(
    [(4, str(S4), None, False)],
    f"A strip of 4 equal boxes, one for each kg of rice, with 1kg under each box. A bracket over the strip is marked Rs 1000, and each box is marked {S4}.",
    f"4 برابر خانوں کی پٹی، چاول کے ہر کلوگرام کے لیے ایک، ہر خانے کے نیچے 1kg۔ پٹی کے اوپر قوس پر Rs 1000 لکھا ہے، اور ہر خانے پر {S4} لکھا ہے۔",
    box=56, over="Rs1000", under="1kg"),
  "s4_rice": bars(
    [(4, "?", None, False)],
    "A strip of 4 equal boxes, one for each kg of rice, with 1kg under each box. A bracket over the strip is marked Rs 1000; each box has a question mark.",
    "4 برابر خانوں کی پٹی، چاول کے ہر کلوگرام کے لیے ایک، ہر خانے کے نیچے 1kg۔ پٹی کے اوپر قوس پر Rs 1000 لکھا ہے؛ ہر خانے پر سوالیہ نشان ہے۔",
    box=56, over="Rs1000", under="1kg"),
  "s5_bus": road(
    180, 3,
    "A road 180 km long, marked with a bracket under it, cut into 3 equal pieces. The marks above say 1h, 2h and 3h; each piece has a question mark.",
    "180 کلومیٹر لمبی سڑک، نیچے قوس کے ساتھ، 3 برابر ٹکڑوں میں بٹی ہوئی۔ اوپر کے نشانوں پر 1h، 2h اور 3h لکھا ہے؛ ہر ٹکڑے پر سوالیہ نشان ہے۔",
    piece_text="?", times=HOURS, total_text="180km"),
  "s7_typing": bars(
    [(6, "?", None, False)],
    "A strip of 6 equal boxes, one for each minute, with a bracket over it marked 240 words. Each box has a question mark.",
    "6 برابر خانوں کی پٹی، ہر منٹ کے لیے ایک، اس کے اوپر 240 الفاظ لکھی قوس۔ ہر خانے پر سوالیہ نشان ہے۔",
    over="240"),
  "s8_petrol": bars(
    [(5, "260", None, False)],
    "A strip of 5 equal boxes, one for each litre of petrol, with 1L under each box and 260 rupees in each box. The bracket over the whole strip has a question mark.",
    "5 برابر خانوں کی پٹی، پیٹرول کے ہر لیٹر کے لیے ایک، ہر خانے کے نیچے 1L اور ہر خانے میں 260 روپے۔ پوری پٹی کے اوپر قوس پر سوالیہ نشان ہے۔",
    box=50, over="?", under="1L"),
  "s11_eggs": bars(
    [(6, None, "180", False), (12, ["?"] + [None] * 11, "324", True)],
    "Two packs of eggs drawn as strips of equal boxes, one box for each egg. Pack A has 6 boxes and costs Rs 180. Pack B has 12 boxes and costs Rs 324; its first box has a question mark.",
    "انڈوں کے دو پیکٹ، برابر خانوں کی پٹیوں کی شکل میں، ہر انڈے کے لیے ایک خانہ۔ پیکٹ A میں 6 خانے ہیں اور قیمت Rs 180 ہے۔ پیکٹ B میں 12 خانے ہیں اور قیمت Rs 324 ہے؛ اس کے پہلے خانے پر سوالیہ نشان ہے۔",
    box=20, left=["A", "B"]),
  "qb_apply": road(
    45, 3,
    "A road 45 km long, marked with a bracket under it, cut into 3 equal pieces. The marks above say 1h, 2h and 3h; each piece has a question mark.",
    "45 کلومیٹر لمبی سڑک، نیچے قوس کے ساتھ، 3 برابر ٹکڑوں میں بٹی ہوئی۔ اوپر کے نشانوں پر 1h، 2h اور 3h لکھا ہے؛ ہر ٹکڑے پر سوالیہ نشان ہے۔",
    piece_text="?", times=HOURS, total_text="45km"),
})
write(lesson)
