"""The two "why" steps that open each Percentages lesson (see why_steps.py):
why people needed the idea, and where it is used today."""


def T(en, ur):
    return {"en": en, "ur": ur}


WHY = {
    "g6-maths-11-what-is-a-percent": {
        "define": T(
            "Definition: a percent is a fraction whose bottom number is 100. The sign % means \"out of 100\". So 25% = 25/100 = 1/4.",
            "تعریف: فیصد ایسی کسر ہے جس کا نیچے والا عدد 100 ہو۔ نشان % کا مطلب ہے \"100 میں سے\"۔ یوں 25% = 25/100 = 1/4۔",
        ),
        "say": T(
            "A shop says \"sale, 20% off\". What does 20% even mean?",
            "دکان کہتی ہے \"سیل، 20% رعایت\"۔ 20% کا مطلب کیا ہے؟",
        ),
        "need": T(
            "Fractions with different bottoms are hard to compare: is 3/5 more than 7/12? People who traded and collected taxes found it easier to always compare out of the same whole, 100. A percent is just a fraction whose bottom is 100. Now 60% and 58% can be compared at a glance. \"Per cent\" simply means \"for every hundred\".",
            "مختلف نیچے والے عدد کی کسروں کا موازنہ مشکل ہے: کیا 3/5، 7/12 سے زیادہ ہے؟ تجارت کرنے والوں اور ٹیکس لینے والوں کو آسان لگا کہ ہمیشہ ایک ہی کل، یعنی 100 میں سے موازنہ کریں۔ فیصد ایسی کسر ہے جس کا نیچے والا عدد 100 ہو۔ اب 60% اور 58% کو ایک نظر میں پرکھا جا سکتا ہے۔ \"فیصد\" کا مطلب ہی ہے \"ہر سو میں سے\"۔",
        ),
        "use": T(
            "Where you will use it:\n• Shops: 20% off, or 10% extra on a pack.\n• Phones: battery at 75%.\n• School: marks, like 80% in a test.\n• Weather: 60% chance of rain.\n• Farming: 30% of the field is wheat.",
            "آپ اسے کہاں استعمال کریں گے:\n• دکانیں: 20% رعایت، یا پیک پر 10% اضافی۔\n• موبائل: بیٹری 75% پر۔\n• اسکول: نمبر، جیسے ٹیسٹ میں 80%۔\n• موسم: بارش کا 60% امکان۔\n• کھیتی: کھیت کا 30% حصہ گندم ہے۔",
        ),
    },
    "g6-maths-11-percents-fractions-decimals": {
        "define": T(
            "Definition: a fraction, a decimal and a percent can be three names for the same amount. To get the percent, make the bottom 100, or multiply the decimal by 100: 1/2 = 50/100 = 0.5 = 50%.",
            "تعریف: کسر، اعشاریہ اور فیصد ایک ہی مقدار کے تین نام ہو سکتے ہیں۔ فیصد بنانے کے لیے نیچے والا عدد 100 کریں، یا اعشاریہ کو 100 سے ضرب دیں: 1/2 = 50/100 = 0.5 = 50%۔",
        ),
        "say": T(
            "A shop says half off, another says 0.5 off, another 50% off. Same?",
            "ایک دکان کہتی ہے آدھی قیمت، دوسری 0.5 رعایت، تیسری 50% رعایت۔ کیا سب ایک ہیں؟",
        ),
        "need": T(
            "The same amount can be written in three ways: a fraction (1/2), a decimal (0.5) or a percent (50%). Each is handy in a different place. Fractions suit sharing, decimals suit money and measuring, percents suit comparing. People needed a way to move between them, so that 1/2, 0.5 and 50% are seen to be exactly the same amount.",
            "ایک ہی مقدار تین طرح لکھی جا سکتی ہے: کسر (1/2)، اعشاریہ (0.5) یا فیصد (50%)۔ ہر ایک الگ جگہ کام آتی ہے۔ کسر بانٹنے کے لیے، اعشاریہ پیسوں اور ناپ کے لیے، اور فیصد موازنے کے لیے۔ لوگوں کو ان کے درمیان بدلنے کا طریقہ چاہیے تھا تاکہ پتا چلے کہ 1/2، 0.5 اور 50% بالکل ایک ہی مقدار ہیں۔",
        ),
        "use": T(
            "Where you will use it:\n• Shopping: is 1/4 off better than 20% off?\n• Cricket: a batter's score shown as a decimal or a percent.\n• Marks: 17 out of 20 turned into a percent.\n• Cooking and farming: 0.5 kg is half a kilo, 1/2 a bag of seed.",
            "آپ اسے کہاں استعمال کریں گے:\n• خریداری: کیا 1/4 رعایت 20% رعایت سے بہتر ہے؟\n• کرکٹ: بلے باز کی کارکردگی اعشاریہ یا فیصد میں۔\n• نمبر: 20 میں سے 17 کو فیصد میں بدلنا۔\n• کھانا پکانا اور کھیتی: 0.5 کلو آدھا کلو ہے، اور 1/2 تھیلا بیج۔",
        ),
    },
    "g6-maths-11-percent-of-an-amount": {
        "define": T(
            "Definition: to find a percent of an amount, multiply the amount by the percent and divide by 100. So 25% of 80 = 80 × 25 ÷ 100 = 20.",
            "تعریف: کسی مقدار کا فیصد نکالنے کے لیے مقدار کو فیصد سے ضرب دیں اور 100 سے تقسیم کریں۔ یوں 80 کا 25% = 80 × 25 ÷ 100 = 20۔",
        ),
        "say": T(
            "A shirt costs Rs 800 and is 25% off. How much do I save?",
            "قمیص 800 روپے کی ہے اور 25% رعایت ہے۔ مجھے کتنی بچت ہوگی؟",
        ),
        "need": T(
            "Knowing that 25% means 25 out of every 100 is not enough. People need the actual amount: how many rupees off, how much tax to pay, how much interest to earn. The trick is to cut the amount into 100 equal parts and take that many parts. Easy percents like 50%, 25% and 10% are halves, quarters and tenths. So 25% of Rs 800 is Rs 200.",
            "یہ جاننا کافی نہیں کہ 25% کا مطلب ہر 100 میں سے 25 ہے۔ لوگوں کو اصل رقم چاہیے: کتنے روپے کی رعایت، کتنا ٹیکس دینا ہے، کتنا منافع ملے گا۔ ترکیب یہ ہے کہ مقدار کے 100 برابر ٹکڑے کریں اور اتنے ٹکڑے لیں۔ آسان فیصد جیسے 50%، 25% اور 10% آدھا، چوتھائی اور دسواں حصہ ہیں۔ تو 800 روپے کا 25% ہے 200 روپے۔",
        ),
        "use": T(
            "Where you will use it:\n• Sales: how many rupees a discount takes off.\n• Bills: tax added to a bill.\n• Savings: profit on money kept in a bank.\n• Farming: 40% of 50 acres is sown with cotton.\n• Mobile load: tax taken from a recharge.",
            "آپ اسے کہاں استعمال کریں گے:\n• سیل: رعایت سے کتنے روپے کم ہوتے ہیں۔\n• بل: بل پر لگنے والا ٹیکس۔\n• بچت: بینک میں رکھی رقم پر منافع۔\n• کھیتی: 50 ایکڑ کا 40% کپاس کے لیے بویا گیا۔\n• موبائل لوڈ: ریچارج سے کٹنے والا ٹیکس۔",
        ),
    },
    "g6-maths-11-finding-the-percentage": {
        "define": T(
            "Definition: to write a part as a percent of the whole, divide the part by the whole and multiply by 100. Percent = part ÷ whole × 100. So 9 out of 20 is 9 ÷ 20 × 100 = 45%.",
            "تعریف: حصے کو کل کے فیصد کے طور پر لکھنے کے لیے حصے کو کل سے تقسیم کریں اور 100 سے ضرب دیں۔ فیصد = حصہ ÷ کل × 100۔ یوں 20 میں سے 9 یعنی 9 ÷ 20 × 100 = 45%۔",
        ),
        "say": T(
            "Ali got 18 out of 20. Is that good? What percent is it?",
            "علی کے 20 میں سے 18 نمبر آئے۔ کیا یہ اچھے ہیں؟ یہ کتنے فیصد ہے؟",
        ),
        "need": T(
            "Two tests can have different totals: 18 out of 20 and 40 out of 50. Which is better? We cannot tell until we put both out of the same whole. Turning the score into a percent does exactly that: 18 out of 20 is 90%, 40 out of 50 is 80%. Part divided by whole, times 100, gives a fair comparison.",
            "دو ٹیسٹوں کے کل نمبر الگ ہو سکتے ہیں: 20 میں سے 18 اور 50 میں سے 40۔ کون سا بہتر ہے؟ جب تک دونوں کو ایک ہی کل میں نہ لائیں، پتا نہیں چلتا۔ نمبر کو فیصد میں بدلنے سے یہی ہوتا ہے: 20 میں سے 18 یعنی 90%، 50 میں سے 40 یعنی 80%۔ حصہ تقسیم کل، ضرب 100، منصفانہ موازنہ دیتا ہے۔",
        ),
        "use": T(
            "Where you will use it:\n• School: marks in different tests, compared fairly.\n• Cricket: 45 runs from 60 balls, as a percent of balls scored on.\n• Farming: what percent of seeds came up.\n• Shops: what percent of the stock is sold.",
            "آپ اسے کہاں استعمال کریں گے:\n• اسکول: مختلف ٹیسٹوں کے نمبروں کا منصفانہ موازنہ۔\n• کرکٹ: 60 گیندوں پر 45 رنز۔\n• کھیتی: کتنے فیصد بیج اگے۔\n• دکان: مال کا کتنے فیصد بک چکا ہے۔",
        ),
    },
    "g6-maths-11-percentage-change": {
        "define": T(
            "Definition: percentage change is the change divided by the original amount, times 100. If the new amount is bigger it is an increase, if smaller a decrease. From 50 to 60: (60 − 50) ÷ 50 × 100 = 20% increase.",
            "تعریف: فیصد تبدیلی وہ تبدیلی ہے جسے اصل مقدار سے تقسیم کر کے 100 سے ضرب دیں۔ نئی مقدار بڑی ہو تو اضافہ ہے، چھوٹی ہو تو کمی۔ 50 سے 60: (60 − 50) ÷ 50 × 100 = 20% اضافہ۔",
        ),
        "say": T(
            "A bus fare goes from Rs 40 to Rs 50. Is that a big rise?",
            "بس کا کرایہ 40 روپے سے 50 روپے ہو گیا۔ کیا یہ بڑا اضافہ ہے؟",
        ),
        "need": T(
            "A rise of Rs 10 sounds the same everywhere, but it hurts more on a Rs 40 fare than on a Rs 4,000 one. To judge how big a change is, we must compare it with where we started. Percentage change does this: change divided by the original amount, times 100. Rs 40 to Rs 50 is a rise of 25%. Prices, crops and populations are compared this way.",
            "10 روپے کا اضافہ ہر جگہ ایک جیسا سنائی دیتا ہے، مگر 40 روپے کے کرائے پر یہ 4000 روپے والے سے زیادہ چبھتا ہے۔ تبدیلی کتنی بڑی ہے، یہ جاننے کے لیے اسے شروع کی مقدار سے ملانا پڑتا ہے۔ فیصد تبدیلی یہی کرتی ہے: تبدیلی تقسیم اصل مقدار، ضرب 100۔ 40 سے 50 روپے یعنی 25% اضافہ۔ قیمتوں، فصلوں اور آبادی کا موازنہ اسی طرح ہوتا ہے۔",
        ),
        "use": T(
            "Where you will use it:\n• Prices: flour or petrol rising by some percent.\n• Sales: a price cut of 15% before Eid.\n• Farming: this year's wheat harvest against last year's.\n• Weather: rain this month compared with last month.",
            "آپ اسے کہاں استعمال کریں گے:\n• قیمتیں: آٹا یا پیٹرول کتنے فیصد مہنگا ہوا۔\n• سیل: عید سے پہلے قیمت میں 15% کمی۔\n• کھیتی: اس سال کی گندم کی فصل پچھلے سال کے مقابلے میں۔\n• موسم: اس مہینے کی بارش پچھلے مہینے کے مقابلے میں۔",
        ),
    },
    "g6-maths-11-percent-word-problems": {
        "say": T(
            "Real shops never ask \"find 25% of 800\". How do I use percents?",
            "اصل دکان دار کبھی نہیں کہتا \"800 کا 25% نکالو\"۔ میں فیصد کہاں لگاؤں؟",
        ),
        "need": T(
            "Percents were made to settle real money matters: discounts, taxes, profit and loss, interest. These come as stories with several steps. The skill is to pick out the whole, find the percent of it, then decide whether to take it off or add it on. Then say the answer in words, like \"you pay Rs 600\". That is how you spot a good deal.",
            "فیصد اصل پیسوں کے معاملات طے کرنے کے لیے بنے: رعایت، ٹیکس، نفع نقصان، منافع۔ یہ مسئلے کئی قدموں والی کہانیوں کی شکل میں آتے ہیں۔ ہنر یہ ہے کہ کل مقدار پہچانیں، اس کا فیصد نکالیں، پھر طے کریں کہ اسے گھٹانا ہے یا بڑھانا۔ پھر جواب الفاظ میں بتائیں، جیسے \"آپ 600 روپے دیں گے\"۔ اسی سے اچھا سودا پہچانا جاتا ہے۔",
        ),
        "use": T(
            "Where you will use it:\n• Buying: the price after a discount, or after tax.\n• Running a shop: profit and loss on what you sell.\n• Saving: how much a bank adds to your money.\n• Family: how much of the monthly income goes to rent and food.",
            "آپ اسے کہاں استعمال کریں گے:\n• خریداری: رعایت یا ٹیکس کے بعد قیمت۔\n• دکان چلانا: بیچے ہوئے مال پر نفع نقصان۔\n• بچت: بینک آپ کی رقم میں کتنا اضافہ کرتا ہے۔\n• گھر: ماہانہ آمدنی کا کتنا حصہ کرائے اور کھانے پر جاتا ہے۔",
        ),
    },
}
