"""The two "why" steps that open each Data Handling lesson (see
why_steps.py): why people needed the idea, and where it is used today."""


def T(en, ur):
    return {"en": en, "ur": ur}


WHY = {
    "g6-maths-10-kinds-of-data": {
        "define": T(
            "Definition: data is information we collect, such as counts or measurements. Data we count in whole numbers is discrete, like the children in a class. Data we measure, which can take any value in between, is continuous, like height or time.",
            "تعریف: مواد وہ معلومات ہیں جو ہم جمع کرتے ہیں، جیسے گنتی یا ناپ۔ جو مواد ہم پورے اعداد میں گنتے ہیں وہ منفصل ہے، جیسے جماعت کے بچے۔ جو مواد ہم ناپتے ہیں اور جو درمیان کی کوئی بھی قیمت ہو سکتا ہے وہ مسلسل ہے، جیسے قد یا وقت۔",
        ),
        "say": T(
            "Why do we sort data into kinds before we use it?",
            "ہم مواد کو استعمال سے پہلے قسموں میں کیوں بانٹتے ہیں؟",
        ),
        "need": T(
            "Counting children in a school and measuring their heights are different jobs. We can count children only in whole numbers, but a height can have any value in between. And a list of 500 marks is too long to read, so we put them in classes. Knowing the kind of data tells us how to collect it, how to group it and which graph will show it best.",
            "اسکول کے بچے گننا اور ان کا قد ناپنا دو الگ کام ہیں۔ بچے ہم صرف پورے اعداد میں گن سکتے ہیں، مگر قد درمیان کی کوئی بھی قیمت ہو سکتا ہے۔ اور 500 نمبروں کی فہرست پڑھنے کے لیے بہت لمبی ہے، اس لیے ہم انہیں جماعتوں میں بانٹ لیتے ہیں۔ مواد کی قسم جان لیں تو پتا چلتا ہے کہ اسے کیسے جمع کریں، کیسے گروہ بنائیں اور کون سا گراف اسے بہتر دکھائے گا۔",
        ),
        "use": T(
            "Where you will use it:\n• School: marks of a whole class put into groups like 1–10, 11–20.\n• Health: weights and heights of children at a clinic.\n• Weather: daily rainfall in millimetres.\n• Shops: how many of each item sold in a week.",
            "آپ اسے کہاں استعمال کریں گے:\n• اسکول: پوری جماعت کے نمبروں کو 1–10، 11–20 جیسے گروہوں میں بانٹنا۔\n• صحت: کلینک میں بچوں کا وزن اور قد۔\n• موسم: روزانہ بارش ملی میٹر میں۔\n• دکان: ہفتے میں ہر چیز کتنی بکی۔",
        ),
    },
    "g6-maths-10-tables-and-tallies": {
        "define": T(
            "Definition: a tally mark is a small line drawn for each item counted. Every fifth mark crosses the four before it, so IIII/ means 5. A table lists each group with its total.",
            "تعریف: ٹیلی کا نشان ہر گنی ہوئی چیز کے لیے لگائی جانے والی چھوٹی لکیر ہے۔ ہر پانچواں نشان پہلے چار کو کاٹتا ہے، اس لیے IIII/ کا مطلب 5 ہے۔ جدول ہر گروہ کو اس کی کل تعداد کے ساتھ لکھتا ہے۔",
        ),
        "say": T(
            "Votes are being counted at a class election. How do we not lose count?",
            "جماعت کے انتخاب میں ووٹ گنے جا رہے ہیں۔ گنتی کیسے نہ بھولیں؟",
        ),
        "need": T(
            "Imagine counting votes as they are called out. If you only keep numbers in your head, one distraction and you lose the count. So people made a mark for each vote on the spot, and every fifth mark crossed the first four. Counting in fives is quick and easy to check. The totals then go into a table, so anyone can read them.",
            "سوچیں کہ ووٹ بلند آواز میں پڑھے جا رہے ہیں اور آپ گنتی صرف دماغ میں رکھ رہے ہیں۔ ذرا سا دھیان بٹا تو گنتی گئی۔ اس لیے لوگوں نے ہر ووٹ پر موقع پر ہی ایک نشان لگایا، اور ہر پانچواں نشان پہلے چار کو کاٹتا ہے۔ پانچ پانچ کر کے گننا تیز ہے اور جانچنا آسان۔ پھر کل تعداد جدول میں لکھی جاتی ہے تاکہ ہر کوئی اسے پڑھ سکے۔",
        ),
        "use": T(
            "Where you will use it:\n• Elections: monitor and class captain votes.\n• Traffic: counting buses and rickshaws that pass your street.\n• Shops: counting how many of each item are sold in a day.\n• Sports: counting wickets, goals or catches.",
            "آپ اسے کہاں استعمال کریں گے:\n• انتخابات: مانیٹر اور کلاس کپتان کے ووٹ۔\n• ٹریفک: آپ کی گلی سے گزرنے والی بسیں اور رکشے گننا۔\n• دکان: دن میں ہر چیز کتنی بکی۔\n• کھیل: وکٹیں، گول یا کیچ گننا۔",
        ),
    },
    "g6-maths-10-bar-graphs": {
        "define": T(
            "Definition: a bar graph shows data with bars. Each bar stands for one group, and the height of the bar is its number, read from the scale at the side. All the bars have the same width.",
            "تعریف: بار گراف مواد کو ستونوں سے دکھاتا ہے۔ ہر ستون ایک گروہ کو ظاہر کرتا ہے اور ستون کی اونچائی اس کا عدد ہے، جو ساتھ والے پیمانے سے پڑھا جاتا ہے۔ سب ستونوں کی چوڑائی برابر ہوتی ہے۔",
        ),
        "say": T(
            "A page of numbers is boring. Can a picture show who has the most?",
            "اعداد کا صفحہ بورنگ ہے۔ کیا تصویر دکھا سکتی ہے کہ کس کے پاس سب سے زیادہ ہے؟",
        ),
        "need": T(
            "A long list of numbers is hard to compare. Our eyes can compare heights instantly. So people drew data as bars: one bar for each group, and the taller the bar, the bigger the number. At a glance you can see which is most, which is least and how big the gaps are, without reading a single figure.",
            "اعداد کی لمبی فہرست کا موازنہ مشکل ہے۔ ہماری آنکھ اونچائیوں کا موازنہ فوراً کر لیتی ہے۔ اس لیے لوگوں نے مواد کو ستونوں کی شکل میں بنایا: ہر گروہ کا ایک ستون، اور ستون جتنا اونچا اتنا بڑا عدد۔ ایک نظر میں نظر آ جاتا ہے کہ کون سب سے زیادہ ہے، کون سب سے کم، اور فرق کتنا بڑا ہے، ایک بھی عدد پڑھے بغیر۔",
        ),
        "use": T(
            "Where you will use it:\n• Newspapers and TV: results of polls, prices and the weather.\n• School: marks of different subjects side by side.\n• Farming: crop yield of different seasons.\n• Business: sales for each month of the year.",
            "آپ اسے کہاں استعمال کریں گے:\n• اخبار اور ٹی وی: رائے شماری، قیمتوں اور موسم کے نتائج۔\n• اسکول: مختلف مضامین کے نمبر ساتھ ساتھ۔\n• کھیتی: مختلف موسموں کی پیداوار۔\n• کاروبار: سال کے ہر مہینے کی فروخت۔",
        ),
    },
    "g6-maths-10-pie-charts-and-multiple-bar-graphs": {
        "define": T(
            "Definition: a pie chart is a circle cut into slices to show how a whole is shared. The angle of a slice is its part of 360°: a quarter of the whole is 90°. A double bar graph has two bars side by side for each group.",
            "تعریف: پائی چارٹ ٹکڑوں میں کٹا ہوا دائرہ ہے جو دکھاتا ہے کہ پورا کیسے بانٹا گیا۔ ٹکڑے کا زاویہ 360° کا اتنا ہی حصہ ہوتا ہے: پورے کا چوتھائی حصہ 90° ہے۔ دوہرے بار گراف میں ہر گروہ کے دو ستون ساتھ ساتھ ہوتے ہیں۔",
        ),
        "say": T(
            "How can one circle show how a whole is shared out?",
            "ایک دائرہ یہ کیسے دکھا سکتا ہے کہ پورا کیسے بانٹا گیا؟",
        ),
        "need": T(
            "Sometimes the question is not how many, but what share of the whole: how a family spends its income, or what fraction of a class likes each sport. A circle cut into slices, like a roti or a pizza, shows shares naturally: a bigger share, a bigger slice. And a double bar graph puts two groups side by side, such as boys and girls, so they are easy to compare.",
            "کبھی سوال یہ نہیں ہوتا کہ کتنے، بلکہ یہ کہ پورے کا کتنا حصہ ہے: ایک گھر اپنی آمدنی کیسے خرچ کرتا ہے، یا جماعت کا کتنا حصہ کون سا کھیل پسند کرتا ہے۔ روٹی یا پیزا کی طرح ٹکڑوں میں کٹا دائرہ حصے خود بخود دکھا دیتا ہے: بڑا حصہ، بڑا ٹکڑا۔ اور دوہرا بار گراف دو گروہوں کو، جیسے لڑکے اور لڑکیاں، ساتھ ساتھ رکھتا ہے تاکہ موازنہ آسان ہو۔",
        ),
        "use": T(
            "Where you will use it:\n• Family budget: how much goes to food, rent, school and bills.\n• Class survey: what share of children like cricket, football or hockey.\n• News: how votes were shared between parties.\n• Business: where a company's money comes from.",
            "آپ اسے کہاں استعمال کریں گے:\n• گھر کا بجٹ: کھانے، کرائے، اسکول اور بلوں پر کتنا خرچ ہوتا ہے۔\n• جماعت کا سروے: کتنے بچے کرکٹ، فٹ بال یا ہاکی پسند کرتے ہیں۔\n• خبریں: پارٹیوں میں ووٹ کیسے بٹے۔\n• کاروبار: کمپنی کی آمدنی کہاں سے آتی ہے۔",
        ),
    },
    "g6-maths-10-average-mean": {
        "define": T(
            "Definition: the mean, or average, is the total of the values divided by how many values there are. Mean = total ÷ number of values. For 2, 4 and 9: (2 + 4 + 9) ÷ 3 = 5.",
            "تعریف: اوسط تمام قیمتوں کے کل کو قیمتوں کی تعداد سے تقسیم کرنے سے ملتی ہے۔ اوسط = کل ÷ قیمتوں کی تعداد۔ مثلاً 2، 4 اور 9 کے لیے: (2 + 4 + 9) ÷ 3 = 5۔",
        ),
        "say": T(
            "Five friends have different sweets. How do we share them fairly?",
            "پانچ دوستوں کے پاس مختلف تعداد میں مٹھائیاں ہیں۔ انہیں برابر کیسے بانٹیں؟",
        ),
        "need": T(
            "One number is often easier to talk about than a long list. If a cricket team scores 30, 50, 20 and 40 in four matches, what is its usual score? We share the total equally: (30 + 50 + 20 + 40) ÷ 4 = 35. This fair-share number is the mean, or average. It sums up a whole list in one number, and lets us compare two different lists.",
            "ایک عدد کی بات کرنا اکثر لمبی فہرست سے آسان ہوتا ہے۔ اگر کرکٹ ٹیم چار میچوں میں 30، 50، 20 اور 40 بنائے تو اس کا عام اسکور کیا ہے؟ ہم کل کو برابر بانٹتے ہیں: (30 + 50 + 20 + 40) ÷ 4 = 35۔ برابر حصے کا یہ عدد اوسط ہے۔ یہ پوری فہرست کو ایک عدد میں بیان کرتا ہے اور دو مختلف فہرستوں کا موازنہ کرنے دیتا ہے۔",
        ),
        "use": T(
            "Where you will use it:\n• Cricket: batting average, or the average runs per over.\n• School: your average mark over all exams.\n• Weather: average temperature or rain of a month.\n• Home: average electricity or mobile spending each month.",
            "آپ اسے کہاں استعمال کریں گے:\n• کرکٹ: بیٹنگ اوسط، یا فی اوور اوسط رنز۔\n• اسکول: تمام امتحانوں میں آپ کے نمبروں کی اوسط۔\n• موسم: مہینے کا اوسط درجہ حرارت یا بارش۔\n• گھر: ہر مہینے بجلی یا موبائل کا اوسط خرچ۔",
        ),
    },
    "g6-maths-10-median": {
        "define": T(
            "Definition: the median is the middle value when the values are put in order. For 3, 5, 9 it is 5. If two values are in the middle, the median is halfway between them: for 2, 4, 6, 10 it is (4 + 6) ÷ 2 = 5.",
            "تعریف: وسطانیہ ترتیب میں لکھی قیمتوں کی بیچ والی قیمت ہے۔ 3، 5، 9 کا وسطانیہ 5 ہے۔ اگر بیچ میں دو قیمتیں ہوں تو وسطانیہ ان کے عین درمیان ہوتا ہے: 2، 4، 6، 10 کا وسطانیہ (4 + 6) ÷ 2 = 5 ہے۔",
        ),
        "say": T(
            "One very rich man lives in a poor village. What is the village's usual income?",
            "ایک غریب گاؤں میں ایک بہت امیر آدمی رہتا ہے۔ گاؤں کی عام آمدنی کیا ہے؟",
        ),
        "need": T(
            "The mean can be pulled up by one huge number. If four families earn Rs 20,000 and one earns Rs 500,000, the mean is Rs 116,000, which does not look like a normal family at all. People needed a fairer \"typical\" value. The median is the middle one when all the values are in order: half are below it and half are above it. Here it is Rs 20,000.",
            "ایک بہت بڑا عدد اوسط کو اوپر کھینچ سکتا ہے۔ اگر چار گھرانے 20,000 روپے کماتے ہوں اور ایک 500,000 روپے، تو اوسط 116,000 روپے بنتی ہے، جو کسی عام گھرانے جیسی بالکل نہیں لگتی۔ لوگوں کو \"عام\" قیمت کا ایک زیادہ منصفانہ پیمانہ چاہیے تھا۔ وسطانیہ ترتیب میں لکھی قیمتوں کی بیچ والی قیمت ہے: آدھی اس سے نیچے اور آدھی اوپر۔ یہاں یہ 20,000 روپے ہے۔",
        ),
        "use": T(
            "Where you will use it:\n• News: the typical income or house price in a city.\n• School: the middle mark of the class, which is not changed by one very high or low mark.\n• Sport: the typical score of a player.\n• Age: the middle age of people in a village.",
            "آپ اسے کہاں استعمال کریں گے:\n• خبریں: کسی شہر میں عام آمدنی یا مکان کی قیمت۔\n• اسکول: جماعت کا بیچ والا نمبر، جو ایک بہت اونچے یا بہت کم نمبر سے نہیں بدلتا۔\n• کھیل: کھلاڑی کا عام اسکور۔\n• عمر: گاؤں کے لوگوں کی بیچ والی عمر۔",
        ),
    },
    "g6-maths-10-mode-and-range": {
        "define": T(
            "Definition: the mode is the value that appears most often. The range is the largest value minus the smallest. For 2, 3, 3, 7 the mode is 3 and the range is 7 − 2 = 5.",
            "تعریف: موڈ وہ قیمت ہے جو سب سے زیادہ بار آئے۔ رینج سب سے بڑی قیمت منفی سب سے چھوٹی قیمت ہے۔ 2، 3، 3، 7 میں موڈ 3 ہے اور رینج 7 − 2 = 5 ہے۔",
        ),
        "say": T(
            "A shoe seller must order stock. Which size should he buy most of?",
            "جوتے بیچنے والے کو مال منگوانا ہے۔ وہ کون سا سائز سب سے زیادہ منگوائے؟",
        ),
        "need": T(
            "A shoe seller does not need the average shoe size: no one wears size 7.3. He needs the size that people buy most. That is the mode, the value that appears most often. He also wants to know how spread out the data is, for example the biggest and smallest sizes sold. The range, the largest minus the smallest, tells him that in one number.",
            "جوتے بیچنے والے کو اوسط سائز نہیں چاہیے: کوئی 7.3 سائز نہیں پہنتا۔ اسے وہ سائز چاہیے جو لوگ سب سے زیادہ خریدتے ہیں۔ یہی موڈ ہے، وہ قیمت جو سب سے زیادہ بار آئے۔ وہ یہ بھی جاننا چاہتا ہے کہ مواد کتنا پھیلا ہے، مثلاً بکنے والے سب سے بڑے اور سب سے چھوٹے سائز۔ رینج، یعنی سب سے بڑا منفی سب سے چھوٹا، یہ ایک عدد میں بتا دیتی ہے۔",
        ),
        "use": T(
            "Where you will use it:\n• Shops: which size, colour or flavour sells most.\n• Cricket: the most common score, and the gap between best and worst innings.\n• Weather: how far the temperature moved in a week.\n• Buses: the most common waiting time.",
            "آپ اسے کہاں استعمال کریں گے:\n• دکانیں: کون سا سائز، رنگ یا ذائقہ سب سے زیادہ بکتا ہے۔\n• کرکٹ: سب سے عام اسکور، اور بہترین اور بدترین اننگز کا فرق۔\n• موسم: ایک ہفتے میں درجہ حرارت کتنا بدلا۔\n• بسیں: سب سے عام انتظار کا وقت۔",
        ),
    },
    "g6-maths-10-data-word-problems": {
        "say": T(
            "Which tool do I pick when a real question about data comes up?",
            "مواد کا کوئی اصل سوال آئے تو میں کون سا اوزار چنوں؟",
        ),
        "need": T(
            "In real life nobody tells us \"find the mean\". We are asked: What is the usual score? Which size sells most? How different were the best and worst days? The skill that matters is reading the question, choosing the right tool (total, mean, median, mode, range or a graph), and explaining the answer in words. That is how data helps us decide.",
            "اصل زندگی میں کوئی ہمیں نہیں کہتا کہ \"اوسط نکالو\"۔ ہم سے پوچھا جاتا ہے: عام اسکور کیا ہے؟ کون سا سائز زیادہ بکتا ہے؟ بہترین اور بدترین دن میں کتنا فرق تھا؟ اصل ہنر یہ ہے کہ سوال پڑھیں، صحیح اوزار چنیں (کل، اوسط، وسطانیہ، موڈ، رینج یا گراف)، اور جواب الفاظ میں سمجھائیں۔ اسی طرح مواد ہمیں فیصلہ کرنے میں مدد دیتا ہے۔",
        ),
        "use": T(
            "Where you will use it:\n• Shopkeeping: deciding what stock to buy next week.\n• Farming: comparing crops of different years.\n• Sport: choosing players by their scores.\n• News: understanding surveys and reports without being fooled.",
            "آپ اسے کہاں استعمال کریں گے:\n• دکان داری: اگلے ہفتے کون سا مال خریدنا ہے یہ طے کرنا۔\n• کھیتی: مختلف سالوں کی فصلوں کا موازنہ۔\n• کھیل: کھلاڑیوں کو ان کے اسکور سے چننا۔\n• خبریں: سروے اور رپورٹیں سمجھنا اور دھوکا نہ کھانا۔",
        ),
    },
}
