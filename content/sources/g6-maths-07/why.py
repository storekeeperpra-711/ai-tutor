"""The two "why" steps that open each Introduction to Algebra lesson (see
why_steps.py): why people needed the idea, and where it is used today."""


def T(en, ur):
    return {"en": en, "ur": ur}


WHY = {
    "g6-maths-07-letters-for-numbers": {
        "define": T(
            "Definition: a variable is a letter that stands for a number that can change or is not known yet. A constant is a number that never changes. In n + 5, n is the variable and 5 is the constant.",
            "تعریف: متغیر وہ حرف ہے جو کسی ایسے عدد کی جگہ لکھا جاتا ہے جو بدل سکتا ہو یا ابھی معلوم نہ ہو۔ مستقل وہ عدد ہے جو کبھی نہیں بدلتا۔ n + 5 میں n متغیر ہے اور 5 مستقل۔",
        ),
        "say": T(
            "Why do mathematicians write letters instead of numbers?",
            "ریاضی دان اعداد کی جگہ حروف کیوں لکھتے ہیں؟",
        ),
        "need": T(
            "Often we do not know a number yet: how many marbles Ali has, or what a bus ticket will cost next year. Writing a full sentence every time is slow. So people started using a letter for the unknown number. One short expression like n + 5 then works for every possible n. It is a short way of writing a rule that is true for many numbers at once.",
            "اکثر ہمیں کوئی عدد ابھی معلوم نہیں ہوتا: علی کے پاس کتنے کنچے ہیں، یا اگلے سال بس کا ٹکٹ کتنے کا ہوگا۔ ہر بار پورا جملہ لکھنا سست کام ہے۔ اس لیے لوگوں نے نامعلوم عدد کے لیے حرف استعمال کرنا شروع کیا۔ پھر n + 5 جیسی ایک مختصر عبارت n کی ہر قیمت کے لیے کام کرتی ہے۔ یہ ایسے اصول کو مختصر لکھنے کا طریقہ ہے جو بہت سے اعداد کے لیے ایک ساتھ درست ہو۔",
        ),
        "use": T(
            "Where you will use it:\n• Shops: price × number of things, like p × n.\n• Phone: a mobile package that costs Rs 20 plus Rs 2 for each day.\n• Games: a cricket score that goes up by r runs every over.\n• Later: formulas in science, such as distance, area and speed.",
            "آپ اسے کہاں استعمال کریں گے:\n• دکان: قیمت × چیزوں کی تعداد، جیسے p × n۔\n• موبائل: ایسا پیکیج جس کی قیمت 20 روپے اور ہر دن کے 2 روپے ہو۔\n• کھیل: کرکٹ کا اسکور جو ہر اوور میں r رنز بڑھے۔\n• آگے چل کر: سائنس کے فارمولے، جیسے فاصلہ، رقبہ اور رفتار۔",
        ),
    },
    "g6-maths-07-terms-and-coefficients": {
        "define": T(
            "Definition: an expression is made of terms joined by + or −. In 5x + 3y − 7 the terms are 5x, 3y and −7. The number multiplying a letter is its coefficient (5 in 5x), and a term with no letter is a constant (−7).",
            "تعریف: عبارت ارکان سے بنتی ہے جو + یا − سے جڑے ہوتے ہیں۔ 5x + 3y − 7 میں ارکان 5x، 3y اور −7 ہیں۔ حرف کو ضرب دینے والا عدد اس کا عددی سر ہے (5x میں 5)، اور بغیر حرف والا رکن مستقل ہے (−7)۔",
        ),
        "say": T(
            "Why do the parts of 5x + 3y − 7 have special names?",
            "5x + 3y − 7 کے حصوں کے خاص نام کیوں ہیں؟",
        ),
        "need": T(
            "When people share a rule, they must point at its parts clearly. Saying \"the number in front\" or \"the part with no letter\" again and again is confusing. So each part got a name: terms, variables, coefficients and constants. With these names a teacher in Lahore and a student in Multan can talk about the same expression and understand each other at once.",
            "جب لوگ کوئی اصول ایک دوسرے کو بتاتے ہیں تو اس کے حصوں کی طرف صاف اشارہ کرنا ضروری ہوتا ہے۔ بار بار \"آگے والا عدد\" یا \"بغیر حرف والا حصہ\" کہنا الجھن پیدا کرتا ہے۔ اس لیے ہر حصے کو نام دیا گیا: ارکان، متغیر، عددی سر اور مستقل۔ ان ناموں سے لاہور کا استاد اور ملتان کا طالب علم ایک ہی عبارت کی بات کریں تو دونوں فوراً سمجھ جاتے ہیں۔",
        ),
        "use": T(
            "Where you will use it:\n• Bills: Rs 10 for each unit plus a fixed Rs 50 charge. The 10 is a coefficient and the 50 is a constant.\n• Taxi fares: a fixed start fee plus a price for each kilometre.\n• Reading formulas in science books.\n• Later: solving equations and drawing graphs.",
            "آپ اسے کہاں استعمال کریں گے:\n• بل: ہر یونٹ کے 10 روپے اور ایک مقررہ 50 روپے کا چارج۔ 10 عددی سر ہے اور 50 مستقل۔\n• ٹیکسی کا کرایہ: مقررہ ابتدائی کرایہ اور ہر کلومیٹر کی قیمت۔\n• سائنس کی کتابوں کے فارمولے پڑھنا۔\n• آگے چل کر: مساواتیں حل کرنا اور گراف بنانا۔",
        ),
    },
    "g6-maths-07-like-terms": {
        "define": T(
            "Definition: like terms have exactly the same letter part. 3a and 2a are like terms, so 3a + 2a = 5a. 3a and 2b are unlike terms, and they cannot be joined.",
            "تعریف: یکساں ارکان کا حرف والا حصہ بالکل ایک جیسا ہوتا ہے۔ 3a اور 2a یکساں ارکان ہیں، اس لیے 3a + 2a = 5a۔ 3a اور 2b غیر یکساں ارکان ہیں اور انہیں ملایا نہیں جا سکتا۔",
        ),
        "say": T(
            "Can I add 3 apples and 2 mangoes to get 5 of something?",
            "کیا میں 3 سیب اور 2 آم جمع کر کے 5 کچھ بنا سکتا ہوں؟",
        ),
        "need": T(
            "Long expressions are hard to read and easy to get wrong. People wanted to make them shorter without changing their value. The idea: join only things of the same kind. 3 apples + 2 apples = 5 apples, but 3 apples + 2 mangoes stay separate. In algebra the same is true: 3a + 2a = 5a, while 3a + 2b cannot be joined.",
            "لمبی عبارتیں پڑھنا مشکل اور ان میں غلطی کرنا آسان ہوتا ہے۔ لوگ چاہتے تھے کہ انہیں چھوٹا کیا جائے اور قیمت نہ بدلے۔ خیال یہ ہے: صرف ایک جیسی چیزیں ملائیں۔ 3 سیب + 2 سیب = 5 سیب، مگر 3 سیب + 2 آم الگ رہتے ہیں۔ الجبرا میں بھی یہی ہے: 3a + 2a = 5a، جبکہ 3a + 2b کو ملایا نہیں جا سکتا۔",
        ),
        "use": T(
            "Where you will use it:\n• Shop totals: add all the kilos of rice, then all the kilos of flour, separately.\n• Cricket: total fours and total sixes are counted apart.\n• Farm records: add the wheat sacks and the rice sacks in their own groups.\n• Later: making long algebra answers short and neat.",
            "آپ اسے کہاں استعمال کریں گے:\n• دکان کا حساب: چاول کے سارے کلو الگ جمع کریں، آٹے کے سارے کلو الگ۔\n• کرکٹ: کل چوکے اور کل چھکے الگ گنے جاتے ہیں۔\n• کھیت کا ریکارڈ: گندم کی بوریاں اور چاول کی بوریاں اپنے اپنے گروہ میں جمع کریں۔\n• آگے چل کر: الجبرا کے لمبے جواب کو مختصر اور صاف بنانا۔",
        ),
    },
    "g6-maths-07-adding-subtracting-expressions": {
        "define": T(
            "Definition: to add expressions, join their like terms: (3r + 2f) + (4r + f) = 7r + 3f. To subtract a bracket, change the sign of every term inside it: 5a − (2a − 3) = 5a − 2a + 3 = 3a + 3.",
            "تعریف: عبارتیں جمع کرنے کے لیے ان کے یکساں ارکان ملائیں: (3r + 2f) + (4r + f) = 7r + 3f۔ بریکٹ تفریق کرنے کے لیے اس کے اندر ہر رکن کی علامت بدل دیں: 5a − (2a − 3) = 5a − 2a + 3 = 3a + 3۔",
        ),
        "say": T(
            "Two shopkeepers combine their stock. How do we add whole lists?",
            "دو دکان دار اپنا مال ملاتے ہیں۔ پوری فہرستیں کیسے جمع کریں؟",
        ),
        "need": T(
            "Real problems rarely have a single term. A shop has (3 kg rice + 2 kg flour) and a second shop has (4 kg rice + 1 kg flour). To combine them, we add whole expressions. If one shop takes back some stock, we subtract a whole bracket, and every sign inside changes. These rules let us combine or compare whole lists of quantities without mistakes.",
            "اصل مسئلوں میں شاید ہی کبھی ایک ہی رکن ہوتا ہے۔ ایک دکان میں (3 کلو چاول + 2 کلو آٹا) ہے اور دوسری میں (4 کلو چاول + 1 کلو آٹا)۔ انہیں ملانے کے لیے ہم پوری عبارتیں جمع کرتے ہیں۔ اگر ایک دکان کچھ مال واپس لے تو ہم پورا بریکٹ تفریق کرتے ہیں، اور اندر کی ہر علامت بدل جاتی ہے۔ ان اصولوں سے ہم مقداروں کی پوری فہرستیں غلطی کے بغیر ملا یا موازنہ کر سکتے ہیں۔",
        ),
        "use": T(
            "Where you will use it:\n• Shops: combine the stock of two shops, or take away what was sold.\n• Farming: total crops from two fields.\n• Budgets: income and spending written as expressions.\n• Later: solving harder equations and working with formulas.",
            "آپ اسے کہاں استعمال کریں گے:\n• دکانیں: دو دکانوں کا مال ملانا، یا جو بک گیا اسے نکالنا۔\n• کھیتی: دو کھیتوں کی کل فصل۔\n• بجٹ: آمدنی اور خرچ کو عبارتوں کی شکل میں لکھنا۔\n• آگے چل کر: مشکل مساواتیں حل کرنا اور فارمولوں پر کام کرنا۔",
        ),
    },
    "g6-maths-07-substitution": {
        "define": T(
            "Definition: to substitute means to put a number in place of a letter and then work out the answer. If d = 7, then 20 + 2d = 20 + 2 × 7 = 34. The answer is the value of the expression.",
            "تعریف: قیمت رکھنے کا مطلب ہے حرف کی جگہ کوئی عدد لکھ کر جواب نکالنا۔ اگر d = 7 ہو تو 20 + 2d = 20 + 2 × 7 = 34۔ یہ جواب عبارت کی قیمت ہے۔",
        ),
        "say": T(
            "A rule is written with a letter. How do I get a real answer?",
            "اصول حرف کے ساتھ لکھا ہے۔ مجھے اصل جواب کیسے ملے گا؟",
        ),
        "need": T(
            "A rule with a letter is written once for all cases. But in real life we need one answer for one case. A phone package costs 20 + 2d rupees for d days. How much for 7 days? We put 7 in place of d: 20 + 2 × 7 = 34. This is substitution. One rule written once gives the answer for any number we choose.",
            "حرف والا اصول سب صورتوں کے لیے ایک بار لکھا جاتا ہے۔ مگر اصل زندگی میں ہمیں ایک صورت کا ایک جواب چاہیے۔ موبائل پیکیج d دنوں کے لیے 20 + 2d روپے کا ہے۔ 7 دن کا کتنا ہوگا؟ ہم d کی جگہ 7 رکھتے ہیں: 20 + 2 × 7 = 34۔ اسے قیمت رکھنا کہتے ہیں۔ ایک بار لکھا ہوا اصول ہمارے چنے ہوئے ہر عدد کا جواب دے دیتا ہے۔",
        ),
        "use": T(
            "Where you will use it:\n• Phone packages and electricity bills: put in the days or units.\n• Taxi fare: put in the kilometres.\n• Formulas: area of a rectangle l × w, or perimeter of a square 4s.\n• Spreadsheets and computer programs work the same way.",
            "آپ اسے کہاں استعمال کریں گے:\n• موبائل پیکیج اور بجلی کا بل: دن یا یونٹ رکھ دیں۔\n• ٹیکسی کا کرایہ: کلومیٹر رکھ دیں۔\n• فارمولے: مستطیل کا رقبہ l × w، یا مربع کا احاطہ 4s۔\n• اسپریڈ شیٹ اور کمپیوٹر پروگرام بھی اسی طرح کام کرتے ہیں۔",
        ),
    },
    "g6-maths-07-simple-equations": {
        "define": T(
            "Definition: an equation says that two things are equal, and it has an unknown letter. To solve it, find the number that makes it true by doing the same to both sides. In 5k = 35, divide both sides by 5, so k = 7.",
            "تعریف: مساوات بتاتی ہے کہ دو چیزیں برابر ہیں، اور اس میں ایک نامعلوم حرف ہوتا ہے۔ اسے حل کرنے کے لیے دونوں طرف ایک ہی کام کر کے وہ عدد ڈھونڈیں جس سے یہ درست ہو جائے۔ 5k = 35 میں دونوں طرف 5 سے تقسیم کریں تو k = 7۔",
        ),
        "say": T(
            "I paid Rs 500 and got Rs 120 back. How do I find the price?",
            "میں نے 500 روپے دیے اور 120 روپے واپس ملے۔ قیمت کیسے معلوم کروں؟",
        ),
        "need": T(
            "Traders and farmers always had questions with a missing number: what is the price, how many sacks are left? People needed a reliable way to find it, instead of guessing. The answer is to treat an equation like a balance: whatever we do to one side, we do to the other. About 1,200 years ago, al-Khwarizmi wrote a book in Baghdad on solving such problems. The word algebra comes from his word al-jabr.",
            "تاجروں اور کسانوں کے سامنے ہمیشہ ایسے سوال ہوتے تھے جن میں کوئی عدد غائب ہو: قیمت کیا ہے، کتنی بوریاں بچی ہیں؟ لوگوں کو اندازے کی جگہ اسے نکالنے کا پکا طریقہ چاہیے تھا۔ جواب یہ ہے کہ مساوات کو ترازو سمجھیں: جو ایک طرف کریں وہی دوسری طرف کریں۔ تقریباً 1200 سال پہلے بغداد میں الخوارزمی نے ایسے مسئلے حل کرنے پر کتاب لکھی۔ لفظ الجبرا ان کے لفظ \"الجبر\" سے بنا ہے۔",
        ),
        "use": T(
            "Where you will use it:\n• Shopping: finding the price when you know the money paid and the change.\n• Mobile load: how many days a balance will last.\n• Farming: how many sacks are left after a sale.\n• Later: science formulas and every part of higher maths.",
            "آپ اسے کہاں استعمال کریں گے:\n• خریداری: ادا کی ہوئی رقم اور بقایا معلوم ہو تو قیمت نکالنا۔\n• موبائل لوڈ: بیلنس کتنے دن چلے گا۔\n• کھیتی: فروخت کے بعد کتنی بوریاں بچیں۔\n• آگے چل کر: سائنس کے فارمولے اور اونچی ریاضی کا ہر حصہ۔",
        ),
    },
    "g6-maths-07-number-patterns": {
        "define": T(
            "Definition: a sequence is a list of numbers that follows a rule, and each number in it is a term. In 4, 7, 10, 13, … the rule is \"add 3\". The rule 3n + 1 gives every term: n = 1 gives 4, n = 2 gives 7.",
            "تعریف: سلسلہ اعداد کی وہ فہرست ہے جو کسی اصول پر چلتی ہے، اور اس کا ہر عدد ایک رکن ہے۔ 4، 7، 10، 13، … میں اصول \"3 جمع کریں\" ہے۔ اصول 3n + 1 ہر رکن دیتا ہے: n = 1 پر 4 اور n = 2 پر 7 ملتا ہے۔",
        ),
        "say": T(
            "Can I know the 100th number of a pattern without writing 100?",
            "کیا میں نمونے کا 100واں عدد 100 اعداد لکھے بغیر جان سکتا ہوں؟",
        ),
        "need": T(
            "Many things in life follow a pattern: bus stops that are 3 km apart, savings that grow by Rs 50 a week, rows of seats in a hall. Writing out every number to reach the 100th is slow. People found that a rule with a letter, like 3n + 1, gives any term at once. Finding the rule means we can predict what comes next, far ahead.",
            "زندگی میں بہت سی چیزیں ایک نمونے پر چلتی ہیں: ہر 3 کلومیٹر بعد بس اسٹاپ، ہر ہفتے 50 روپے بڑھتی بچت، ہال میں کرسیوں کی قطاریں۔ 100ویں عدد تک پہنچنے کے لیے ہر عدد لکھنا سست کام ہے۔ لوگوں نے دیکھا کہ 3n + 1 جیسا حرف والا اصول کوئی بھی رکن فوراً دے دیتا ہے۔ اصول مل جائے تو ہم بہت آگے کی بات پہلے سے بتا سکتے ہیں۔",
        ),
        "use": T(
            "Where you will use it:\n• Savings: Rs 50 added every week, so how much after 20 weeks?\n• Buildings: seats in the rows of a hall, where each row has 2 more.\n• Calendars and timetables that repeat.\n• Later: computer programs and the study of growth.",
            "آپ اسے کہاں استعمال کریں گے:\n• بچت: ہر ہفتے 50 روپے بڑھیں تو 20 ہفتے بعد کتنے ہوں گے؟\n• عمارتیں: ہال کی قطاروں میں کرسیاں، جہاں ہر قطار میں 2 زیادہ ہوں۔\n• کیلنڈر اور ٹائم ٹیبل جو بار بار دہراتے ہیں۔\n• آگے چل کر: کمپیوٹر پروگرام اور بڑھوتری کا مطالعہ۔",
        ),
    },
    "g6-maths-07-algebra-word-problems": {
        "say": T(
            "Problems come as stories. How do I turn a story into algebra?",
            "مسئلے کہانی کی شکل میں آتے ہیں۔ کہانی کو الجبرا میں کیسے بدلوں؟",
        ),
        "need": T(
            "Nobody gives us a ready equation. People hand us a story: \"I bought 3 pens and paid Rs 60\". The skill that matters is turning the words into an equation, solving it, and checking the answer in the story. Algebra became useful because it lets us solve a whole kind of problems with one method, so we do not need a new trick for each story.",
            "ہمیں کوئی تیار مساوات نہیں دیتا۔ لوگ ہمیں کہانی سناتے ہیں: \"میں نے 3 قلم خریدے اور 60 روپے دیے\"۔ اصل ہنر یہ ہے کہ الفاظ کو مساوات میں بدلیں، اسے حل کریں، اور جواب کو کہانی میں جانچیں۔ الجبرا اس لیے کام کا بنا کہ ایک ہی طریقے سے پوری قسم کے سوال حل ہو جاتے ہیں، ہر کہانی کے لیے نئی ترکیب نہیں چاہیے۔",
        ),
        "use": T(
            "Where you will use it:\n• Shopping: the price of one item from the total bill.\n• Sharing: how much each friend pays when a cost is shared.\n• Travel: how long a journey takes at a known speed.\n• Work: planning a budget or a farm's seed and water needs.",
            "آپ اسے کہاں استعمال کریں گے:\n• خریداری: کل بل سے ایک چیز کی قیمت نکالنا۔\n• بانٹنا: خرچ بانٹنے پر ہر دوست کتنا دے۔\n• سفر: معلوم رفتار پر سفر میں کتنا وقت لگے۔\n• کام: بجٹ بنانا، یا کھیت کے بیج اور پانی کی ضرورت کا اندازہ لگانا۔",
        ),
    },
}
