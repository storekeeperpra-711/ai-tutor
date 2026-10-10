"""The two "why" steps that open each Integers lesson (see why_steps.py):
why people needed the idea, and where it is used today."""


def T(en, ur):
    return {"en": en, "ur": ur}


WHY = {
    "g6-maths-04-what-are-integers": {
        "say": T(
            "Why did people ever need numbers below zero?",
            "لوگوں کو صفر سے کم اعداد کی ضرورت کیوں پڑی؟",
        ),
        "need": T(
            "Counting numbers start at 1, and 0 means \"nothing\". But a shopkeeper sometimes owes money, and some places are colder than zero or lower than the sea. Plain numbers could not show this. So people made negative numbers: +500 for Rs 500 you have, −500 for Rs 500 you owe. About 1,400 years ago, Brahmagupta, a mathematician in India, wrote clear rules for using them.",
            "گنتی کے اعداد 1 سے شروع ہوتے ہیں اور 0 کا مطلب \"کچھ نہیں\" ہے۔ مگر دکان دار پر کبھی ادھار بھی ہوتا ہے، اور کچھ جگہیں صفر سے زیادہ ٹھنڈی یا سطح سمندر سے نیچی ہوتی ہیں۔ عام اعداد یہ سب نہیں دکھا سکتے تھے۔ اس لیے لوگوں نے منفی اعداد بنائے: +500 یعنی 500 روپے آپ کے پاس ہیں، −500 یعنی 500 روپے آپ کو دینے ہیں۔ تقریباً 1400 سال پہلے ہندوستان کے ریاضی دان برہم گپت نے انہیں استعمال کرنے کے صاف اصول لکھے۔",
        ),
        "use": T(
            "Where you will use integers:\n• Weather: Murree at −3 °C, Lahore at 12 °C.\n• Money: your savings, or a loan you must pay back.\n• Heights: a mountain 4,000 m above the sea, a mine 200 m below it.\n• Games: a team 2 goals ahead is +2; behind by 3 is −3.",
            "صحیح اعداد آپ کہاں استعمال کریں گے:\n• موسم: مری میں −3 ڈگری، لاہور میں 12 ڈگری۔\n• پیسے: آپ کی بچت، یا وہ قرض جو واپس کرنا ہے۔\n• اونچائی: سطح سمندر سے 4000 میٹر اونچا پہاڑ، 200 میٹر نیچی کان۔\n• کھیل: جو ٹیم 2 گول آگے ہو وہ +2، 3 گول پیچھے ہو تو −3۔",
        ),
    },
    "g6-maths-04-absolute-value": {
        "define": T(
            "Definition: the absolute value of a number is its distance from 0 on the number line, without its direction. We write it with two bars: |−5| = 5 and |5| = 5. It is never negative.",
            "تعریف: کسی عدد کی مطلق قدر عددی خط پر 0 سے اس کا فاصلہ ہے، سمت کے بغیر۔ ہم اسے دو لکیروں کے بیچ لکھتے ہیں: |−5| = 5 اور |5| = 5۔ یہ کبھی منفی نہیں ہوتی۔",
        ),
        "say": T(
            "Two buses go 5 km, one east and one west. Did one go less?",
            "دو بسیں 5 کلومیٹر چلیں، ایک مشرق، ایک مغرب۔ کیا کوئی کم چلی؟",
        ),
        "need": T(
            "Sometimes we care only about how far, not which way. A bus that goes 5 km east and a bus that goes 5 km west have travelled the same distance, but one is +5 and the other is −5. People needed a way to talk about the size of a number without its sign. That size is called the absolute value: |−5| = 5 and |5| = 5.",
            "کبھی ہمیں صرف یہ جاننا ہوتا ہے کہ کتنا دور، یہ نہیں کہ کس طرف۔ 5 کلومیٹر مشرق جانے والی بس اور 5 کلومیٹر مغرب جانے والی بس نے برابر فاصلہ طے کیا، مگر ایک +5 ہے اور دوسری −5۔ لوگوں کو عدد کی مقدار بغیر اس کی علامت کے بیان کرنے کا طریقہ چاہیے تھا۔ اس مقدار کو مطلق قدر کہتے ہیں: |−5| = 5 اور |5| = 5۔",
        ),
        "use": T(
            "Where you will use it:\n• Distance: your school is 300 m from home, whichever side you walk.\n• Measuring: a rope cut 2 cm too long or 2 cm too short has an error of 2 cm.\n• Temperature: how far a day is from freezing, hot or cold.\n• Money: the size of a profit or a loss.",
            "آپ اسے کہاں استعمال کریں گے:\n• فاصلہ: آپ کا اسکول گھر سے 300 میٹر دور ہے، چاہے کسی بھی طرف چلیں۔\n• ناپ: رسی 2 سینٹی میٹر زیادہ کٹے یا 2 سینٹی میٹر کم، غلطی 2 سینٹی میٹر ہی ہے۔\n• درجہ حرارت: دن جمنے کے نقطے سے کتنا دور ہے، گرم ہو یا ٹھنڈا۔\n• پیسے: نفع یا نقصان کی مقدار۔",
        ),
    },
    "g6-maths-04-adding-integers": {
        "say": T(
            "A shopkeeper has Rs 300 and owes Rs 500. Is he rich or poor?",
            "دکان دار کے پاس 300 روپے ہیں اور 500 روپے دینے ہیں۔ وہ امیر ہے یا غریب؟",
        ),
        "need": T(
            "To answer, he must add +300 and −500 together. People needed clear rules for adding numbers that go up and numbers that go down, so that everyone gets the same answer. These rules work every time, without counting every step: +300 + (−500) = −200. He still owes Rs 200.",
            "جواب کے لیے اسے +300 اور −500 کو جمع کرنا ہوگا۔ لوگوں کو اوپر جانے والے اور نیچے جانے والے اعداد کو جمع کرنے کے صاف اصول چاہیے تھے تاکہ سب کو ایک ہی جواب ملے۔ یہ اصول ہر بار کام کرتے ہیں، ہر قدم گنے بغیر: +300 + (−500) = −200۔ اسے اب بھی 200 روپے دینے ہیں۔",
        ),
        "use": T(
            "Where you will use it:\n• Bank or mobile wallet: your balance after you put money in and take money out.\n• Temperature: it was −2 °C at night and rose by 9 degrees.\n• Lifts: you are in the basement at −1 and go up 4 floors.\n• Games: points won and points lost in a match.",
            "آپ اسے کہاں استعمال کریں گے:\n• بینک یا موبائل والٹ: رقم ڈالنے اور نکالنے کے بعد آپ کا بیلنس۔\n• درجہ حرارت: رات کو −2 ڈگری تھا اور 9 ڈگری بڑھ گیا۔\n• لفٹ: آپ تہہ خانے میں −1 پر ہیں اور 4 منزلیں اوپر جاتے ہیں۔\n• کھیل: میچ میں جیتے اور ہارے ہوئے پوائنٹس۔",
        ),
    },
    "g6-maths-04-subtracting-integers": {
        "say": T(
            "How much warmer is Lahore at 12 °C than Murree at −3 °C?",
            "لاہور 12 ڈگری پر مری سے، جو −3 ڈگری پر ہے، کتنا گرم ہے؟",
        ),
        "need": T(
            "To find a difference we subtract: 12 − (−3). But taking away a negative number looked strange, and many people got stuck. The big idea that fixed it: subtracting a number is the same as adding its opposite. So 12 − (−3) = 12 + 3 = 15. Every hard subtraction turns into an addition we already know.",
            "فرق نکالنے کے لیے ہم منفی کرتے ہیں: 12 − (−3)۔ مگر منفی عدد کو نکالنا عجیب لگتا تھا اور بہت سے لوگ اٹک جاتے تھے۔ جس بڑے خیال نے یہ مسئلہ حل کیا وہ یہ ہے: کسی عدد کو منفی کرنا اس کے الٹ کو جمع کرنے کے برابر ہے۔ تو 12 − (−3) = 12 + 3 = 15۔ ہر مشکل منفی ایک ایسا جمع بن جاتا ہے جو ہمیں پہلے سے آتا ہے۔",
        ),
        "use": T(
            "Where you will use it:\n• Weather: how much hotter or colder one city is than another.\n• Heights: the gap between a mountain top and the floor of a mine.\n• Money: how much your savings changed from last month.\n• Sports: how far one team is ahead of another on the table.",
            "آپ اسے کہاں استعمال کریں گے:\n• موسم: ایک شہر دوسرے سے کتنا گرم یا ٹھنڈا ہے۔\n• اونچائی: پہاڑ کی چوٹی اور کان کی تہہ کے درمیان فاصلہ۔\n• پیسے: پچھلے مہینے کے مقابلے میں آپ کی بچت کتنی بدلی۔\n• کھیل: ٹیبل پر ایک ٹیم دوسری سے کتنی آگے ہے۔",
        ),
    },
    "g6-maths-04-multiplying-and-dividing-integers": {
        "say": T(
            "A shop loses Rs 50 every day for 7 days. How much in all?",
            "ایک دکان 7 دن تک روزانہ 50 روپے کا نقصان اٹھاتی ہے۔ کل کتنا؟",
        ),
        "need": T(
            "That is 7 groups of −50. People wanted multiplication and division to work for negative numbers too, with the same rules every time. The sign rules do this: same signs give a positive answer, different signs give a negative answer. So 7 × (−50) = −350, a loss of Rs 350. A shopkeeper and a scientist always get the same answer.",
            "یہ −50 کے 7 گروہ ہیں۔ لوگ چاہتے تھے کہ ضرب اور تقسیم منفی اعداد کے لیے بھی کام کریں، ہر بار ایک ہی اصول سے۔ علامت کے اصول یہی کرتے ہیں: ایک جیسی علامتوں کا جواب مثبت، مختلف علامتوں کا جواب منفی۔ تو 7 × (−50) = −350، یعنی 350 روپے کا نقصان۔ دکان دار اور سائنس دان کو ہمیشہ ایک ہی جواب ملتا ہے۔",
        ),
        "use": T(
            "Where you will use it:\n• Money: a loss every day, or a monthly instalment you pay.\n• Temperature: it falls 3 degrees every hour for 4 hours.\n• Diving: a diver goes down 2 m every minute.\n• Sharing a debt: Rs 600 owed, shared equally by 3 friends.",
            "آپ اسے کہاں استعمال کریں گے:\n• پیسے: روزانہ نقصان، یا ہر مہینے ادا کی جانے والی قسط۔\n• درجہ حرارت: ہر گھنٹے 3 ڈگری گرتا ہے، 4 گھنٹے تک۔\n• غوطہ خوری: غوطہ خور ہر منٹ 2 میٹر نیچے جاتا ہے۔\n• قرض بانٹنا: 600 روپے کا قرض، 3 دوست برابر بانٹتے ہیں۔",
        ),
    },
    "g6-maths-04-laws-of-integers": {
        "say": T(
            "Can you add 25 + 37 + 75 in any order you like?",
            "کیا آپ 25 + 37 + 75 کو اپنی مرضی کی ترتیب سے جمع کر سکتے ہیں؟",
        ),
        "need": T(
            "When we add or multiply many numbers, we want to swap them or regroup them to make the work easy. But is that always allowed? Mathematicians gave the safe moves names: commutative (swap the order), associative (regroup), and distributive (spread a multiplication over a sum). They are true for integers too, so we can calculate quickly and still be sure of the answer.",
            "جب ہم بہت سے اعداد کو جمع یا ضرب کرتے ہیں تو چاہتے ہیں کہ انہیں بدل کر یا نئے گروہ بنا کر کام آسان کریں۔ مگر کیا یہ ہمیشہ جائز ہے؟ ریاضی دانوں نے ان محفوظ چالوں کے نام رکھے: تبادلی (ترتیب بدلنا)، تلازمی (نئے گروہ بنانا) اور توزیعی (ضرب کو جمع پر پھیلانا)۔ یہ صحیح اعداد کے لیے بھی درست ہیں، اس لیے ہم تیزی سے حساب کر سکتے ہیں اور جواب کے بارے میں پکے رہتے ہیں۔",
        ),
        "use": T(
            "Where you will use it:\n• Shopping: add a bill in any order, like 25 + 75 first to make 100.\n• Mental maths: 7 × 102 = 7 × 100 + 7 × 2 = 714.\n• Checking: add numbers upwards and downwards to see if you get the same answer.\n• Later: algebra and computer programs use these same rules.",
            "آپ اسے کہاں استعمال کریں گے:\n• خریداری: بل کو کسی بھی ترتیب سے جمع کریں، جیسے پہلے 25 + 75 کر کے 100 بنا لیں۔\n• ذہنی حساب: 7 × 102 = 7 × 100 + 7 × 2 = 714۔\n• جانچ: اعداد کو اوپر سے نیچے اور نیچے سے اوپر جمع کر کے دیکھیں کہ جواب ایک ہی آتا ہے۔\n• آگے چل کر: الجبرا اور کمپیوٹر پروگرام یہی اصول استعمال کرتے ہیں۔",
        ),
    },
    "g6-maths-04-integer-word-problems": {
        "say": T(
            "Real problems come as stories, not as sums. How do we start?",
            "اصل مسئلے کہانی کی شکل میں آتے ہیں، جمع تفریق کی شکل میں نہیں۔ ہم کہاں سے شروع کریں؟",
        ),
        "need": T(
            "Floors above and below the ground, hot and cold weather, money in and money out: integers were made to describe stories like these. The skill that matters is turning a story into a sum with + and − signs, solving it, and then saying the answer in words. That is how maths leaves the classroom and helps in real life.",
            "زمین سے اوپر اور نیچے کی منزلیں، گرم اور ٹھنڈا موسم، آنے والے اور جانے والے پیسے: صحیح اعداد ایسی ہی کہانیاں بیان کرنے کے لیے بنے تھے۔ اصل ہنر یہ ہے کہ کہانی کو + اور − والی جمع تفریق میں بدلیں، اسے حل کریں، اور پھر جواب الفاظ میں بتائیں۔ یوں ریاضی کلاس سے نکل کر حقیقی زندگی میں کام آتی ہے۔",
        ),
        "use": T(
            "Where you will use it:\n• Bank statements and mobile wallet records.\n• Weather reports and travel to cold places.\n• Lift buttons in tall buildings, with floors below ground.\n• Shop accounts: what came in, what went out, what is left.",
            "آپ اسے کہاں استعمال کریں گے:\n• بینک اسٹیٹمنٹ اور موبائل والٹ کا ریکارڈ۔\n• موسم کی رپورٹ اور ٹھنڈی جگہوں کا سفر۔\n• اونچی عمارتوں کی لفٹ کے بٹن، جن میں زمین سے نیچے کی منزلیں بھی ہوتی ہیں۔\n• دکان کا حساب: کیا آیا، کیا گیا، کیا بچا۔",
        ),
    },
}
