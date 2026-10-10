"""The two "why" steps that open each Simplification lesson (see why_steps.py):
why people needed the idea, and where it is used today."""


def T(en, ur):
    return {"en": en, "ur": ur}


WHY = {
    "g6-maths-13-order-of-operations": {
        "say": T(
            "Bilal says 3 + 4 × 5 is 35. Sana says 23. Who is right?",
            "بلال کہتا ہے 3 + 4 × 5 کا جواب 35 ہے۔ ثنا کہتی ہے 23۔ کون درست ہے؟",
        ),
        "need": T(
            "If one sum can give two answers, nobody can trust a bill or a recipe. So everyone agreed on one order: multiplication and division first, then addition and subtraction, going from left to right. This is a rule that people made, not something found in nature. Because of it, a shopkeeper in Multan and a student in Karachi always get the same answer. Sana is right: 3 + 20 = 23.",
            "اگر ایک ہی سوال کے دو جواب نکلیں تو بل یا نسخے پر کوئی بھروسا نہیں کر سکتا۔ اس لیے سب نے ایک ترتیب مان لی: پہلے ضرب اور تقسیم، پھر جمع اور تفریق، بائیں سے دائیں۔ یہ قاعدہ لوگوں نے بنایا ہے، قدرت میں نہیں ملتا۔ اسی کی وجہ سے ملتان کے دکان دار اور کراچی کے طالب علم کو ہمیشہ ایک ہی جواب ملتا ہے۔ ثنا درست ہے: 3 + 20 = 23۔",
        ),
        "use": T(
            "Where you will use it:\n• Shop bills: 3 packs at Rs 20 plus a Rs 15 bag is 3 × 20 + 15.\n• Calculators and phones follow this same order.\n• Computer programs and spreadsheets use it for every formula.\n• Later: algebra and science formulas.",
            "آپ اسے کہاں استعمال کریں گے:\n• دکان کے بل: 20 روپے کے 3 پیک اور 15 روپے کا تھیلا یعنی 3 × 20 + 15۔\n• کیلکولیٹر اور موبائل یہی ترتیب مانتے ہیں۔\n• کمپیوٹر پروگرام اور اسپریڈ شیٹ ہر فارمولے میں اسے استعمال کرتے ہیں۔\n• آگے چل کر: الجبرا اور سائنس کے فارمولے۔",
        ),
    },
    "g6-maths-13-brackets": {
        "say": T(
            "I buy 2 notebooks and 3 pens, each Rs 10. How do I write it?",
            "میں 2 کاپیاں اور 3 قلم خریدتا ہوں، ہر ایک 10 روپے کا۔ اسے کیسے لکھوں؟",
        ),
        "need": T(
            "The usual order does × before +. But sometimes we need to add first, then multiply: (2 + 3) × 10 = Rs 50. People needed a way to say \"do this part first\". Brackets do that. They are like a fence around a part of the sum. With brackets, the same numbers can be made to give the answer we really mean. BODMAS is a handy way to remember the order.",
            "عام ترتیب میں × پہلے ہوتا ہے اور + بعد میں۔ مگر کبھی پہلے جمع کرنا ہوتا ہے، پھر ضرب: (2 + 3) × 10 = 50 روپے۔ لوگوں کو \"یہ حصہ پہلے کرو\" کہنے کا طریقہ چاہیے تھا۔ قوسین یہی کرتی ہیں۔ یہ سوال کے ایک حصے کے گرد باڑ جیسی ہیں۔ قوسین سے وہی اعداد وہ جواب دیتے ہیں جو ہم واقعی چاہتے ہیں۔ BODMAS ترتیب یاد رکھنے کا آسان طریقہ ہے۔",
        ),
        "use": T(
            "Where you will use it:\n• Shopping: total of many items, then times the price.\n• Spreadsheets and calculators: every formula uses brackets.\n• Sharing: (500 + 300) ÷ 4 for four friends.\n• Later: algebra, where brackets are everywhere.",
            "آپ اسے کہاں استعمال کریں گے:\n• خریداری: بہت سی چیزوں کا کل، پھر قیمت سے ضرب۔\n• اسپریڈ شیٹ اور کیلکولیٹر: ہر فارمولے میں قوسین ہوتی ہیں۔\n• بانٹنا: چار دوستوں کے لیے (500 + 300) ÷ 4۔\n• آگے چل کر: الجبرا، جہاں قوسین ہر جگہ ہوتی ہیں۔",
        ),
    },
    "g6-maths-13-fractions-decimals": {
        "say": T(
            "Is 3/4 of Rs 32 the same as 0.75 × 32? Do the same rules work?",
            "کیا 32 روپے کا 3/4 اور 0.75 × 32 ایک ہی ہیں؟ کیا وہی اصول چلتے ہیں؟",
        ),
        "need": T(
            "Real life mixes whole numbers, fractions and decimals in one sum: half a kilo at Rs 120.50 a kilo, or 3/4 of a field. If each kind of number had its own rules, nobody could keep track. The good news is that the order of operations stays the same. The word \"of\" means multiply, so 3/4 of 32 is 3/4 × 32 = 24. One set of rules does everything.",
            "اصل زندگی میں ایک ہی سوال میں پورے اعداد، کسریں اور اعشاریہ ملے ہوتے ہیں: آدھا کلو، 120.50 روپے کلو کے حساب سے، یا کھیت کا 3/4۔ اگر ہر قسم کے عدد کے الگ اصول ہوتے تو کوئی حساب نہ رکھ پاتا۔ اچھی بات یہ ہے کہ عملیات کی ترتیب وہی رہتی ہے۔ لفظ \"کا\" کا مطلب ضرب ہے، تو 32 کا 3/4 یعنی 3/4 × 32 = 24۔ ایک ہی اصول ہر کام کر دیتے ہیں۔",
        ),
        "use": T(
            "Where you will use it:\n• Markets: price per kilo times 1.5 kg of fruit.\n• Farming: 3/4 of a field planted, 1/2 of that with wheat.\n• Cooking: 1/2 cup of oil in a recipe made 3 times.\n• Money: bills with paisas, like Rs 45.50.",
            "آپ اسے کہاں استعمال کریں گے:\n• بازار: فی کلو قیمت ضرب ڈیڑھ کلو پھل۔\n• کھیتی: کھیت کے 3/4 میں فصل لگی، اس کے 1/2 میں گندم۔\n• کھانا پکانا: 1/2 کپ تیل والا نسخہ 3 بار بنانا۔\n• پیسے: پیسوں والے بل، جیسے 45.50 روپے۔",
        ),
    },
    "g6-maths-13-estimation": {
        "say": T(
            "Do I always need the exact answer, or is \"about\" enough?",
            "کیا مجھے ہمیشہ بالکل ٹھیک جواب چاہیے، یا \"تقریباً\" کافی ہے؟",
        ),
        "need": T(
            "In the market you do not stop to work out every price exactly. You think \"about Rs 500, so my Rs 1,000 is enough\". People round numbers to friendly ones, such as the nearest 10 or 100, so they can think quickly. A good estimate also catches big mistakes: if the sum should be near 500 and you get 5,000, something went wrong.",
            "بازار میں آپ ہر قیمت کا ٹھیک حساب لگانے کے لیے نہیں رکتے۔ آپ سوچتے ہیں \"تقریباً 500 روپے، تو میرے 1000 کافی ہیں\"۔ لوگ اعداد کو آسان اعداد کے قریب لے آتے ہیں، جیسے قریب ترین 10 یا 100، تاکہ جلدی سوچ سکیں۔ اچھا اندازہ بڑی غلطیاں بھی پکڑ لیتا ہے: اگر جواب 500 کے قریب ہونا چاہیے اور آپ کا جواب 5000 ہے تو کہیں گڑبڑ ہے۔",
        ),
        "use": T(
            "Where you will use it:\n• Shopping: do I have enough money for these things?\n• Travel: about how long will 190 km take?\n• Checking: is my calculator answer the right size?\n• Farming: about how many bags of grain from this field?",
            "آپ اسے کہاں استعمال کریں گے:\n• خریداری: کیا میرے پاس ان چیزوں کے لیے کافی پیسے ہیں؟\n• سفر: 190 کلومیٹر میں تقریباً کتنا وقت لگے گا؟\n• جانچ: کیا میرے کیلکولیٹر کا جواب صحیح سائز کا ہے؟\n• کھیتی: اس کھیت سے تقریباً کتنی بوریاں اناج ہوگا؟",
        ),
    },
    "g6-maths-13-simplification-word-problems": {
        "say": T(
            "A story has many numbers. How do I turn it into one sum?",
            "کہانی میں بہت سے اعداد ہیں۔ میں اسے ایک سوال میں کیسے بدلوں؟",
        ),
        "need": T(
            "Problems in life come as stories, with several amounts and several steps, not as a ready sum. People needed a way to write the whole story as one number sentence, with brackets where something must be done first, so that nothing is forgotten. Then BODMAS gives the answer, and an estimate checks it is sensible. This is how you solve a shopkeeper's bill or a trip's costs.",
            "زندگی کے مسئلے کہانی کی شکل میں آتے ہیں، کئی مقداروں اور کئی قدموں کے ساتھ، تیار سوال کی شکل میں نہیں۔ لوگوں کو پوری کہانی کو ایک عددی جملے میں لکھنے کا طریقہ چاہیے تھا، جہاں کچھ پہلے کرنا ہو وہاں قوسین لگا کر، تاکہ کچھ بھولے نہیں۔ پھر BODMAS جواب دیتا ہے اور اندازہ جانچتا ہے کہ جواب مناسب ہے۔ یوں دکان دار کا بل یا سفر کا خرچ حل ہوتا ہے۔",
        ),
        "use": T(
            "Where you will use it:\n• Shop bills with many items and a discount.\n• Trip costs: bus fare for the family plus food.\n• Cricket: runs and overs in a match.\n• Planning: how much to save each week for something you want.",
            "آپ اسے کہاں استعمال کریں گے:\n• بہت سی چیزوں اور رعایت والے دکان کے بل۔\n• سفر کا خرچ: خاندان کا بس کرایہ اور کھانا۔\n• کرکٹ: میچ میں رنز اور اوورز۔\n• منصوبہ بندی: کسی پسندیدہ چیز کے لیے ہر ہفتے کتنی بچت کرنی ہے۔",
        ),
    },
}
