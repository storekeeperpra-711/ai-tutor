"""The two "why" steps that open each Factors and Multiples teaching lesson
(see why_steps.py): the need behind the idea, and where it is used today."""


def T(en, ur):
    return {"en": en, "ur": ur}


WHY = {
    "g6-maths-05-factors-and-multiples": {
        "say": T(
            "How can 12 laddoos be shared into equal rows with none left?",
            "12 لڈو برابر قطاروں میں کیسے بانٹیں کہ کوئی نہ بچے؟",
        ),
        "need": T(
            "People often share things equally: sweets among children, eggs in trays, chairs in rows. Some amounts split evenly and some do not. 12 laddoos make 2 rows of 6 or 3 rows of 4, but 13 will not split that way. People needed a clear way to know which numbers fit into which. Factors are the numbers that divide exactly. Multiples are what you get by repeating a number, like a times table.",
            "لوگ اکثر چیزیں برابر بانٹتے ہیں: بچوں میں مٹھائی، ٹرے میں انڈے، قطاروں میں کرسیاں۔ کچھ تعداد برابر بٹ جاتی ہے اور کچھ نہیں۔ 12 لڈو 2 قطاروں میں 6 یا 3 قطاروں میں 4 بن جاتے ہیں، مگر 13 اس طرح نہیں بٹتے۔ لوگوں کو جاننا تھا کہ کون سا عدد کس میں پورا آتا ہے۔ اجزائے ضربی وہ اعداد ہیں جو پورا تقسیم کرتے ہیں۔ اضعاف وہ ہیں جو کسی عدد کو بار بار دہرانے سے ملتے ہیں، جیسے پہاڑا۔",
        ),
        "use": T(
            "Where you will use it:\n• Shops: packing 24 eggs in equal trays or 36 pencils in equal boxes.\n• School: seating children in equal rows.\n• Buses: a bus every 15 minutes comes at 15, 30, 45 ... minutes.\n• Times tables: they are just multiples.",
            "آپ اسے کہاں استعمال کریں گے:\n• دکان: 24 انڈے برابر ٹرے میں یا 36 پنسلیں برابر ڈبوں میں رکھنا۔\n• اسکول: بچوں کو برابر قطاروں میں بٹھانا۔\n• بسیں: ہر 15 منٹ بعد آنے والی بس 15، 30، 45 ... منٹ پر آتی ہے۔\n• پہاڑے: یہ دراصل اضعاف ہی ہیں۔",
        ),
    },
    "g6-maths-05-prime-numbers": {
        "say": T(
            "Why can 13 laddoos never make equal rows, except one long row?",
            "13 لڈو ایک لمبی قطار کے سوا برابر قطاروں میں کیوں نہیں بٹتے؟",
        ),
        "need": T(
            "Try to put 13 laddoos in equal rows. Only one row of 13 or 13 rows of 1 will work. Numbers like 2, 3, 5, 7, 11 and 13 cannot be split any further. They are called prime numbers. Every other number, like 12, can be built by multiplying primes: 12 = 2 × 2 × 3. So primes are like the basic building blocks of all numbers, and prime factors show what a number is made of.",
            "13 لڈو برابر قطاروں میں رکھ کر دیکھیں۔ صرف 13 کی ایک قطار یا 1 کی 13 قطاریں بنتی ہیں۔ 2، 3، 5، 7، 11 اور 13 جیسے اعداد کو مزید نہیں توڑا جا سکتا۔ انہیں مفرد اعداد کہتے ہیں۔ باقی ہر عدد، جیسے 12، مفرد اعداد کو ضرب دے کر بنایا جا سکتا ہے: 12 = 2 × 2 × 3۔ یوں مفرد اعداد تمام اعداد کی بنیادی اینٹوں کی طرح ہیں، اور مفرد اجزائے ضربی بتاتے ہیں کہ عدد کس سے بنا ہے۔",
        ),
        "use": T(
            "Where you will use it:\n• Sharing: knowing that 13 sweets cannot be shared equally among 2, 3 or 4 children.\n• Finding factors: breaking a big number into primes makes its factors easy to see.\n• HCF and LCM: prime factors give a quick way to find both.\n• Secret codes: phones and online shopping use very large primes to keep information safe.",
            "آپ اسے کہاں استعمال کریں گے:\n• بانٹنا: یہ جاننا کہ 13 مٹھائیاں 2، 3 یا 4 بچوں میں برابر نہیں بٹ سکتیں۔\n• اجزائے ضربی: بڑے عدد کو مفرد اعداد میں توڑنے سے اس کے اجزائے ضربی آسانی سے نظر آتے ہیں۔\n• عاد اعظم اور ذو اضعاف اقل: مفرد اجزائے ضربی سے دونوں جلدی نکلتے ہیں۔\n• خفیہ کوڈ: فون اور آن لائن خریداری معلومات کو محفوظ رکھنے کے لیے بہت بڑے مفرد اعداد استعمال کرتے ہیں۔",
        ),
    },
    "g6-maths-05-highest-common-factor": {
        "say": T(
            "How can 12 roses and 18 marigolds make the most equal bunches?",
            "12 گلاب اور 18 گیندے سے زیادہ سے زیادہ برابر گچھے کیسے بنیں؟",
        ),
        "need": T(
            "A flower seller has 12 roses and 18 marigolds. She wants the most bunches that are all the same, with nothing left over. The number of bunches must divide both 12 and 18. Listing the common factors shows the choices: 1, 2, 3 and 6. The biggest is 6, so she makes 6 bunches. This biggest shared factor is the highest common factor (HCF). It solves any problem of the largest equal groups.",
            "ایک پھول والی کے پاس 12 گلاب اور 18 گیندے ہیں۔ وہ زیادہ سے زیادہ ایسے گچھے بنانا چاہتی ہے جو سب ایک جیسے ہوں اور کچھ نہ بچے۔ گچھوں کی تعداد 12 اور 18 دونوں کو تقسیم کرنی چاہیے۔ مشترک اجزائے ضربی لکھیں تو چناؤ نظر آتے ہیں: 1، 2، 3 اور 6۔ سب سے بڑا 6 ہے، تو وہ 6 گچھے بنائے گی۔ یہ سب سے بڑا مشترک جزو عاد اعظم ہے۔ یہ سب سے بڑے برابر گروہوں کا ہر سوال حل کرتا ہے۔",
        ),
        "use": T(
            "Where you will use it:\n• Tiles: the biggest square tile that covers a floor exactly.\n• School: the longest equal rows for boys and girls at assembly.\n• Shops: packing two kinds of goods into the most equal packets.\n• Fractions: cutting 12/18 down to 2/3.",
            "آپ اسے کہاں استعمال کریں گے:\n• ٹائل: وہ سب سے بڑی مربع ٹائل جو فرش کو پورا ڈھانپ دے۔\n• اسکول: اسمبلی میں لڑکوں اور لڑکیوں کی سب سے لمبی برابر قطاریں۔\n• دکان: دو قسم کا سامان زیادہ سے زیادہ برابر پیکٹوں میں رکھنا۔\n• کسر: 12/18 کو کم کر کے 2/3 بنانا۔",
        ),
    },
    "g6-maths-05-lowest-common-multiple": {
        "say": T(
            "Two buses leave together. When will they leave together again?",
            "دو بسیں ساتھ روانہ ہوئیں۔ وہ دوبارہ ساتھ کب روانہ ہوں گی؟",
        ),
        "need": T(
            "One bus leaves a stop every 4 minutes and another every 6 minutes. They leave together now. When will they leave together again? The first bus leaves at 4, 8, 12 ... and the second at 6, 12, 18 ... The first time in both lists is 12. This smallest shared multiple is the lowest common multiple (LCM). People needed it to find when things that repeat at different speeds meet again.",
            "ایک بس اڈے سے ہر 4 منٹ بعد اور دوسری ہر 6 منٹ بعد روانہ ہوتی ہے۔ دونوں ابھی ساتھ گئیں۔ دوبارہ ساتھ کب جائیں گی؟ پہلی بس 4، 8، 12 ... پر اور دوسری 6، 12، 18 ... پر جاتی ہے۔ دونوں فہرستوں میں پہلا مشترک وقت 12 ہے۔ یہ سب سے چھوٹا مشترک ضعف ذو اضعاف اقل ہے۔ لوگوں کو اس کی ضرورت تھی کہ مختلف رفتار سے دہرائی جانے والی چیزیں دوبارہ کب ملتی ہیں۔",
        ),
        "use": T(
            "Where you will use it:\n• Buses and trains: when two routes leave together again.\n• School: two bells that ring at different gaps.\n• Chores: a tap that is checked every 3 days and a tank every 4 days are both checked on day 12.\n• Fractions: finding a common denominator to add 1/4 and 1/6.",
            "آپ اسے کہاں استعمال کریں گے:\n• بسیں اور ریل گاڑیاں: دو راستوں کی گاڑیاں دوبارہ ساتھ کب چلیں گی۔\n• اسکول: مختلف وقفوں سے بجنے والی دو گھنٹیاں۔\n• کام: نلکا ہر 3 دن اور ٹنکی ہر 4 دن بعد دیکھی جائے تو دونوں 12ویں دن ساتھ دیکھی جاتی ہیں۔\n• کسر: 1/4 اور 1/6 جمع کرنے کے لیے مشترک مخرج نکالنا۔",
        ),
    },
    "g6-maths-05-hcf-times-lcm": {
        "say": T(
            "Is there a shortcut that links the HCF, the LCM and the two numbers?",
            "کیا عاد اعظم، ذو اضعاف اقل اور دونوں اعداد کا کوئی آسان تعلق ہے؟",
        ),
        "need": T(
            "Finding the HCF and the LCM both take time, especially for big numbers. People noticed a pattern. For 12 and 18, the HCF is 6 and the LCM is 36, and 6 × 36 = 216, which is the same as 12 × 18. This holds for any two numbers. So if you know the two numbers and one of the HCF or LCM, you can find the other with one multiplication and one division, without a long search.",
            "دونوں نکالنے میں وقت لگتا ہے، خاص طور پر بڑے اعداد میں۔ لوگوں نے ایک ترتیب دیکھی۔ 12 اور 18 کا عاد اعظم 6 اور ذو اضعاف اقل 36 ہے، اور 6 × 36 = 216 ہے، جو 12 × 18 کے برابر ہے۔ یہ کسی بھی دو اعداد کے لیے سچ ہے۔ تو اگر آپ کو دونوں اعداد اور عاد اعظم یا ذو اضعاف اقل میں سے ایک معلوم ہو، تو دوسرا ایک ضرب اور ایک تقسیم سے مل جاتا ہے، لمبی تلاش کے بغیر۔",
        ),
        "use": T(
            "Where you will use it:\n• Checking: after finding the HCF and LCM, multiply them to check your answer.\n• Saving time: find the LCM of 15 and 20 from their HCF 5, as 300 ÷ 5 = 60.\n• Exams: many problems give one of the two and ask for the other.",
            "آپ اسے کہاں استعمال کریں گے:\n• جانچ: عاد اعظم اور ذو اضعاف اقل نکال کر انہیں ضرب دیں اور اپنا جواب جانچیں۔\n• وقت کی بچت: 15 اور 20 کے عاد اعظم 5 سے ذو اضعاف اقل نکالیں، 300 ÷ 5 = 60۔\n• امتحان: بہت سے سوالوں میں دونوں میں سے ایک دیا ہوتا ہے اور دوسرا پوچھا جاتا ہے۔",
        ),
    },
    "g6-maths-05-squares-and-index-notation": {
        "say": T(
            "How do we write 2 × 2 × 2 × 2 × 2 × 2 without writing it all out?",
            "2 × 2 × 2 × 2 × 2 × 2 کو پورا لکھے بغیر کیسے لکھیں؟",
        ),
        "need": T(
            "Some numbers of dots make a perfect square, like 49 dots in 7 rows of 7. People measuring square fields and floors met such numbers again and again. Also, writing the same number many times is slow and easy to get wrong. So they made a short way: 7 × 7 = 7² and 2 × 2 × 2 × 2 × 2 × 2 = 2⁶. The small raised number says how many times to multiply. It is called the index.",
            "کچھ تعداد کے نقطے پورا مربع بناتے ہیں، جیسے 7 قطاروں میں 7 نقطے، یعنی 49۔ مربع کھیت اور فرش ناپنے والوں کو ایسے اعداد بار بار ملتے تھے۔ اور ایک ہی عدد بہت بار لکھنا سست ہے اور غلطی کا امکان بھی رہتا ہے۔ تو مختصر طریقہ بنا: 7 × 7 = 7² اور 2 × 2 × 2 × 2 × 2 × 2 = 2⁶۔ اوپر چھوٹا عدد بتاتا ہے کہ کتنی بار ضرب دینی ہے۔ اسے قوت کہتے ہیں۔",
        ),
        "use": T(
            "Where you will use it:\n• Area: a square field with 20 m sides has area 20² = 400 m².\n• Tiles: a square of 8 by 8 tiles has 8² = 64 tiles.\n• Big numbers: 10³ = 1,000 and 10⁶ = 1,000,000 are quick to write.\n• Prime factors: 72 = 2³ × 3² is much shorter than 2 × 2 × 2 × 3 × 3.",
            "آپ اسے کہاں استعمال کریں گے:\n• رقبہ: 20 میٹر کے ضلع والے مربع کھیت کا رقبہ 20² = 400 مربع میٹر ہے۔\n• ٹائل: 8 ضرب 8 ٹائلوں کے مربع میں 8² = 64 ٹائلیں ہوتی ہیں۔\n• بڑے اعداد: 10³ = 1000 اور 10⁶ = 1000000 جلدی لکھے جاتے ہیں۔\n• مفرد اجزائے ضربی: 72 = 2³ × 3² کو 2 × 2 × 2 × 3 × 3 سے بہت چھوٹا لکھا جاتا ہے۔",
        ),
    },
    "g6-maths-05-factor-word-problems": {
        "say": T(
            "Real problems do not say HCF or LCM. How do we know which to use?",
            "اصل سوال میں عاد اعظم یا ذو اضعاف اقل نہیں لکھا ہوتا۔ ہم کیسے جانیں کون سا استعمال کریں؟",
        ),
        "need": T(
            "In real life nobody tells you to find an HCF or an LCM. A shopkeeper just asks how many equal packets he can make, or when two things happen together again. The skill is to read the story and pick the right tool. Splitting into the largest equal groups needs the HCF. Things that repeat and meet again need the LCM. Choosing correctly saves wasted work and wrong answers.",
            "اصل زندگی میں کوئی نہیں کہتا کہ عاد اعظم یا ذو اضعاف اقل نکالو۔ دکان دار بس پوچھتا ہے کہ کتنے برابر پیکٹ بن سکتے ہیں، یا دو چیزیں دوبارہ ساتھ کب ہوں گی۔ ہنر یہ ہے کہ کہانی پڑھ کر صحیح طریقہ چنا جائے۔ سب سے بڑے برابر گروہوں کے لیے عاد اعظم چاہیے۔ دہرائی جانے والی چیزیں جو دوبارہ ملتی ہیں ان کے لیے ذو اضعاف اقل۔ صحیح چناؤ وقت اور غلط جوابوں سے بچاتا ہے۔",
        ),
        "use": T(
            "Where you will use it:\n• Shops: packing goods into the most equal packets.\n• Tiling: choosing the largest square tile for a room.\n• Timetables: when two buses or two bells match again.\n• Farming: planting rows of two crops in equal plots.",
            "آپ اسے کہاں استعمال کریں گے:\n• دکان: سامان کو زیادہ سے زیادہ برابر پیکٹوں میں رکھنا۔\n• ٹائل: کمرے کے لیے سب سے بڑی مربع ٹائل چننا۔\n• اوقات: دو بسیں یا دو گھنٹیاں دوبارہ کب ایک ساتھ ہوں گی۔\n• کھیتی: دو فصلوں کی قطاریں برابر قطعوں میں لگانا۔",
        ),
    },
}
