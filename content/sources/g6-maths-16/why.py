"""The two "why" steps that open each Linear Equations lesson (see
why_steps.py): why people needed the idea, and where it is used today."""


def T(en, ur):
    return {"en": en, "ur": ur}


WHY = {
    "g6-maths-16-equations-and-expressions": {
        "say": T(
            "What is the difference between 3x + 5 and 3x + 5 = 20?",
            "3x + 5 اور 3x + 5 = 20 میں کیا فرق ہے؟",
        ),
        "need": T(
            "People often know the total but not one of the parts: \"I paid Rs 20 in all. What did one cost?\" They used a letter for the thing they did not know. An expression like 3x + 5 is a rule that gives a number for each x. An equation says two things are equal, like a balance, and lets us ask: which x makes it true?",
            "لوگوں کو اکثر کل معلوم ہوتا ہے مگر ایک حصہ نہیں: \"میں نے کل 20 روپے دیے۔ ایک چیز کی قیمت کیا تھی؟\" انہوں نے نامعلوم چیز کے لیے ایک حرف رکھ لیا۔ 3x + 5 جیسا الجبری جملہ ایک اصول ہے جو ہر x کے لیے ایک عدد دیتا ہے۔ مساوات کہتی ہے کہ دو چیزیں برابر ہیں، ترازو کی طرح، اور ہمیں پوچھنے دیتی ہے: کون سا x اسے سچ بناتا ہے؟",
        ),
        "use": T(
            "Where you will use it:\n• Shopping: total bill = number of items × price + delivery.\n• Rickshaw fare: Rs 50 plus Rs 20 for every km.\n• Mobile packages: a fixed charge plus a charge per minute.\n• Later: science formulas and computer programs.",
            "آپ اسے کہاں استعمال کریں گے:\n• خریداری: کل بل = چیزوں کی تعداد × قیمت + ڈیلیوری۔\n• رکشے کا کرایہ: 50 روپے اور ہر کلومیٹر کے 20 روپے۔\n• موبائل پیکج: ایک طے شدہ چارج اور ہر منٹ کا چارج۔\n• آگے چل کر: سائنس کے فارمولے اور کمپیوٹر پروگرام۔",
        ),
    },
    "g6-maths-16-forming-equations": {
        "say": T(
            "\"5 less than a number is 12.\" How do I write that in maths?",
            "\"ایک عدد سے 5 کم 12 ہے۔\" اسے ریاضی میں کیسے لکھوں؟",
        ),
        "need": T(
            "Problems are told in words, but equations are solved in symbols. Long ago, people wrote whole sentences for every problem, which was slow. A short way of writing is quicker and clearer. A letter stands for the unknown number, and key words turn into signs: \"more than\" is +, \"less than\" is −, \"is\" is =. Now \"5 less than a number is 12\" is x − 5 = 12.",
            "مسئلے الفاظ میں بتائے جاتے ہیں، مگر مساوات علامتوں میں حل ہوتی ہے۔ ہر مسئلے کے لیے پورے جملے لکھنا سست تھا۔ لکھنے کا مختصر طریقہ تیز اور صاف ہے۔ نامعلوم عدد کے لیے ایک حرف، اور خاص الفاظ علامتوں میں: \"سے زیادہ\" یعنی +، \"سے کم\" یعنی −، \"ہے\" یعنی =۔ اب \"ایک عدد سے 5 کم 12 ہے\" بن جاتا ہے x − 5 = 12۔",
        ),
        "use": T(
            "Where you will use it:\n• Shopping: \"I had some money, spent Rs 50, and have Rs 120 left\".\n• Cricket: \"runs needed after the first innings\".\n• Farming: \"how many bags in each row\".\n• Phones: writing a rule in a spreadsheet or program.",
            "آپ اسے کہاں استعمال کریں گے:\n• خریداری: \"میرے پاس کچھ پیسے تھے، 50 روپے خرچ کیے، اب 120 روپے بچے ہیں\"۔\n• کرکٹ: \"پہلی اننگز کے بعد کتنے رنز چاہئیں\"۔\n• کھیتی: \"ہر قطار میں کتنی بوریاں ہیں\"۔\n• موبائل: اسپریڈ شیٹ یا پروگرام میں اصول لکھنا۔",
        ),
    },
    "g6-maths-16-two-step-equations": {
        "say": T(
            "A rickshaw costs Rs 50 plus Rs 20 per km. Fare Rs 210. How far?",
            "رکشہ 50 روپے اور ہر کلومیٹر کے 20 روپے لیتا ہے۔ کرایہ 210 روپے۔ کتنی دور؟",
        ),
        "need": T(
            "Many real problems have two things happening: a fixed charge, then a charge for each unit. To find the unknown, people found a clever idea: undo what was done, in reverse order, and do the same thing to both sides to keep the balance. For 20k + 50 = 210, take away 50, then divide by 20, and k = 8 km. This works for any numbers.",
            "بہت سے مسئلوں میں دو باتیں ہوتی ہیں: ایک طے شدہ چارج، پھر ہر اکائی کا چارج۔ نامعلوم عدد نکالنے کے لیے لوگوں کو ایک ہوشیار خیال ملا: جو کیا گیا اسے الٹی ترتیب سے ختم کرو، اور ترازو برابر رکھنے کے لیے دونوں طرف ایک ہی عمل کرو۔ 20k + 50 = 210 میں 50 نکالیں، پھر 20 سے تقسیم کریں، تو k = 8 کلومیٹر۔ یہ طریقہ کسی بھی اعداد کے لیے چلتا ہے۔",
        ),
        "use": T(
            "Where you will use it:\n• Travel: taxi, rickshaw or app fares with a starting charge.\n• Mobile load: a fixed fee plus a rate per minute.\n• Markets: a bill that includes a delivery charge.\n• Saving: how many weeks until you reach your target.",
            "آپ اسے کہاں استعمال کریں گے:\n• سفر: ٹیکسی، رکشہ یا ایپ کا کرایہ جس میں شروع کا چارج ہو۔\n• موبائل لوڈ: طے شدہ فیس اور فی منٹ ریٹ۔\n• بازار: ڈیلیوری چارج والا بل۔\n• بچت: ہدف تک پہنچنے میں کتنے ہفتے لگیں گے۔",
        ),
    },
    "g6-maths-16-equations-with-brackets": {
        "say": T(
            "3 friends each pay the same for a bill plus Rs 2 tip. Total Rs 21?",
            "3 دوست بل کے ساتھ ہر ایک 2 روپے ٹپ دیتے ہیں۔ کل 21 روپے؟",
        ),
        "need": T(
            "When the same thing happens to a whole group, we put the group in brackets: 3(x + 2) = 21 means 3 people each pay x + 2. People needed to solve this without guessing. There are two ways: divide both sides by 3 first, or open the bracket and multiply every term inside. Both give x = 5, so you can check one way against the other.",
            "جب ایک ہی بات پورے گروہ کے ساتھ ہو تو ہم گروہ کو قوسین میں رکھتے ہیں: 3(x + 2) = 21 کا مطلب ہے 3 لوگ ہر ایک x + 2 دیتا ہے۔ لوگوں کو اسے اندازے کے بغیر حل کرنا تھا۔ دو طریقے ہیں: پہلے دونوں طرف کو 3 سے تقسیم کریں، یا قوسین کھول کر اندر کے ہر حصے کو ضرب دیں۔ دونوں سے x = 5 آتا ہے، تو آپ ایک طریقے کو دوسرے سے جانچ سکتے ہیں۔",
        ),
        "use": T(
            "Where you will use it:\n• Groups: the same fee plus a small extra for each person.\n• Shops: 4 packs, each with the same price plus tax.\n• Farming: the same amount of seed and fertiliser for each field.\n• Planning: costs of a school trip for the whole class.",
            "آپ اسے کہاں استعمال کریں گے:\n• گروہ: ہر فرد کی ایک جیسی فیس اور تھوڑا سا اضافہ۔\n• دکانیں: 4 پیک، ہر ایک کی وہی قیمت اور ٹیکس۔\n• کھیتی: ہر کھیت کے لیے برابر بیج اور کھاد۔\n• منصوبہ بندی: پوری جماعت کے اسکول ٹرپ کا خرچ۔",
        ),
    },
    "g6-maths-16-checking-solutions": {
        "say": T(
            "I solved it and got x = 4. How can I be sure I am right?",
            "میں نے حل کیا اور x = 4 آیا۔ مجھے کیسے یقین ہو کہ میں درست ہوں؟",
        ),
        "need": T(
            "Everyone makes mistakes when solving. A shopkeeper counts the change again before handing it over. In the same way, we put the answer back in place of the letter and see if both sides are equal. If they are, the answer is certainly right. If not, we have found a mistake before it costs us. This check always works.",
            "حل کرتے ہوئے سب سے غلطی ہوتی ہے۔ دکان دار باقی پیسے دینے سے پہلے انہیں دوبارہ گنتا ہے۔ اسی طرح ہم جواب کو حرف کی جگہ رکھ کر دیکھتے ہیں کہ دونوں طرف برابر ہیں یا نہیں۔ اگر ہیں تو جواب یقیناً درست ہے۔ اگر نہیں، تو نقصان سے پہلے ہی غلطی پکڑ لی۔ یہ جانچ ہمیشہ کام کرتی ہے۔",
        ),
        "use": T(
            "Where you will use it:\n• Exams: confirm your answer before you move on.\n• Shops: re-check the bill and the change.\n• Trying values: does x = 6 fit this rule?\n• Computer programs: testing a formula with a known value.",
            "آپ اسے کہاں استعمال کریں گے:\n• امتحان: آگے بڑھنے سے پہلے اپنا جواب پکا کریں۔\n• دکان: بل اور باقی پیسے دوبارہ جانچیں۔\n• قیمتیں آزمانا: کیا x = 6 اس اصول پر پورا اترتا ہے؟\n• کمپیوٹر پروگرام: معلوم قیمت سے فارمولا جانچنا۔",
        ),
    },
    "g6-maths-16-equation-word-problems": {
        "say": T(
            "Nobody asks me to \"solve 20k + 50 = 210\". How does it help?",
            "کوئی مجھ سے نہیں کہتا \"20k + 50 = 210 حل کرو\"۔ یہ کیسے کام آتا ہے؟",
        ),
        "need": T(
            "Equations were not made to be sums on a page. They were made to answer questions from life: how many km, how many weeks, how many items. The skill is to pick a letter for what you do not know, write an equation from the story, solve it, then check the answer in the story and say it in words. That is how algebra helps with real decisions.",
            "مساوات صفحے پر سوال حل کرنے کے لیے نہیں بنیں۔ یہ زندگی کے سوالوں کا جواب دینے کے لیے بنیں: کتنے کلومیٹر، کتنے ہفتے، کتنی چیزیں۔ ہنر یہ ہے کہ جو معلوم نہیں اس کے لیے حرف چنیں، کہانی سے مساوات لکھیں، حل کریں، پھر جواب کو کہانی میں جانچیں اور الفاظ میں بتائیں۔ یوں الجبرا اصل فیصلوں میں مدد دیتا ہے۔",
        ),
        "use": T(
            "Where you will use it:\n• Travel: how far can I go with Rs 300?\n• Shopping: how many items can I buy within my budget?\n• Saving: how many weeks to buy a cricket bat.\n• Later: engineers, shopkeepers and computer programmers use this daily.",
            "آپ اسے کہاں استعمال کریں گے:\n• سفر: 300 روپے میں میں کتنی دور جا سکتا ہوں؟\n• خریداری: اپنے بجٹ میں کتنی چیزیں خرید سکتا ہوں؟\n• بچت: کرکٹ کا بلا خریدنے میں کتنے ہفتے لگیں گے۔\n• آگے چل کر: انجینئر، دکان دار اور کمپیوٹر پروگرامر روزانہ یہ استعمال کرتے ہیں۔",
        ),
    },
}
