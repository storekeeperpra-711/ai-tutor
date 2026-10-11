"""The two "why" steps that open each Probability lesson (see why_steps.py):
why people needed the idea, and where it is used today."""


def T(en, ur):
    return {"en": en, "ur": ur}


WHY = {
    "g6-maths-17-likelihood": {
        "define": T(
            "Definition: likelihood tells how possible it is that something happens. It runs from impossible (it cannot happen), through unlikely, equally likely and likely, to certain (it must happen). A coin landing head or tail is equally likely; the sun rising tomorrow is certain.",
            "تعریف: امکان بتاتا ہے کہ کوئی بات ہونا کتنا ممکن ہے۔ یہ ناممکن (ہو ہی نہیں سکتی) سے شروع ہو کر کم امکان، برابر امکان اور زیادہ امکان سے ہوتا ہوا یقینی (ضرور ہوگی) تک جاتا ہے۔ سکے کا ہیڈ یا ٹیل آنا برابر امکان ہے؛ کل سورج کا نکلنا یقینی ہے۔",
        ),
        "say": T(
            "Will it rain today? Nobody can be sure, so what do we say?",
            "کیا آج بارش ہوگی؟ کوئی یقین سے نہیں کہہ سکتا، تو ہم کیا کہیں؟",
        ),
        "need": T(
            "Many things in life are not certain: rain, a cricket match, the next bus. We cannot say \"yes\" or \"no\" for sure, but we can say how much to expect it. People needed words to compare chances, like certain, likely, unlikely and impossible. These words are the first step to measuring chance with numbers.",
            "زندگی میں بہت سی باتیں یقینی نہیں ہوتیں: بارش، کرکٹ کا میچ، اگلی بس۔ ہم یقین سے \"ہاں\" یا \"نہیں\" نہیں کہہ سکتے، مگر یہ ضرور بتا سکتے ہیں کہ اس کی کتنی امید ہے۔ لوگوں کو امکانات کا موازنہ کرنے کے لیے الفاظ چاہیے تھے، جیسے یقینی، زیادہ امکان، کم امکان اور ناممکن۔ یہ الفاظ امکان کو اعداد سے ناپنے کی پہلی سیڑھی ہیں۔",
        ),
        "use": T(
            "Where you will use it:\n• Weather: \"a high chance of rain\" in a forecast.\n• Cricket: a team that is likely to win a match.\n• Daily life: taking an umbrella or leaving early for school.\n• Games: knowing a coin toss is equally likely to be head or tail.",
            "آپ اسے کہاں استعمال کریں گے:\n• موسم: پیش گوئی میں \"بارش کا زیادہ امکان\"۔\n• کرکٹ: وہ ٹیم جس کے میچ جیتنے کا امکان زیادہ ہے۔\n• روزمرہ: چھتری لے جانا یا اسکول کے لیے جلدی نکلنا۔\n• کھیل: یہ جاننا کہ سکہ اچھالنے پر ہیڈ اور ٹیل کا امکان یکساں ہے۔",
        ),
    },
    "g6-maths-17-sample-space": {
        "define": T(
            "Definition: an experiment is an action whose result we cannot be sure of. Each result is an outcome. The sample space is the set of all outcomes, and an event is some of them. Rolling a die: sample space {1, 2, 3, 4, 5, 6}; the event \"even number\" is {2, 4, 6}.",
            "تعریف: تجربہ ایسا عمل ہے جس کے نتیجے کا ہمیں یقین نہیں ہوتا۔ ہر ممکنہ نتیجہ ایک نتیجہ کہلاتا ہے۔ نمونی فضا تمام نتائج کا سیٹ ہے، اور واقعہ ان میں سے کچھ نتائج ہیں۔ ڈائس پھینکنا: نمونی فضا {1, 2, 3, 4, 5, 6}؛ واقعہ \"جفت عدد\" ہے {2, 4, 6}۔",
        ),
        "say": T(
            "Before the toss, what can happen? Can you list everything?",
            "سکہ اچھالنے سے پہلے کیا کیا ہو سکتا ہے؟ کیا آپ سب لکھ سکتے ہیں؟",
        ),
        "need": T(
            "To talk about chance, we must first know everything that could happen. Toss a coin: head or tail. Roll a die: 1, 2, 3, 4, 5 or 6. If a result is missed, the chance is counted wrongly. So people made clear words: an experiment, its outcomes, the sample space (the set of all outcomes), and an event (some of the outcomes we care about).",
            "امکان کی بات کرنے کے لیے پہلے یہ جاننا ضروری ہے کہ کیا کیا ہو سکتا ہے۔ سکہ اچھالیں: ہیڈ یا ٹیل۔ ڈائس پھینکیں: 1، 2، 3، 4، 5 یا 6۔ اگر کوئی نتیجہ رہ جائے تو امکان غلط گنا جاتا ہے۔ اس لیے لوگوں نے صاف الفاظ بنائے: تجربہ، اس کے نتائج، نمونی فضا (تمام نتائج کا سیٹ) اور واقعہ (وہ کچھ نتائج جن میں ہمیں دلچسپی ہے)۔",
        ),
        "use": T(
            "Where you will use it:\n• Games: all the ways a die or two coins can land.\n• Cricket: the toss, and the ways a ball can end.\n• Planning: listing all the choices before you decide.\n• Computers: testing a program on every possible input.",
            "آپ اسے کہاں استعمال کریں گے:\n• کھیل: ڈائس یا دو سکے جتنی طرح گر سکتے ہیں ان سب کی فہرست۔\n• کرکٹ: ٹاس، اور گیند کے ختم ہونے کے طریقے۔\n• منصوبہ بندی: فیصلے سے پہلے سب انتخاب لکھنا۔\n• کمپیوٹر: پروگرام کو ہر ممکن ان پٹ پر آزمانا۔",
        ),
    },
    "g6-maths-17-probability-of-an-event": {
        "define": T(
            "Definition: when all outcomes are equally likely, the probability of an event E is P(E) = n(E) ÷ n(S), the number of outcomes in E over the number of all outcomes. It is always from 0 (impossible) to 1 (certain). For a die, P(even) = 3 ÷ 6 = 1/2.",
            "تعریف: جب تمام نتائج کا امکان برابر ہو تو واقعہ E کا احتمال P(E) = n(E) ÷ n(S) ہے، یعنی E کے نتائج کی تعداد تقسیم تمام نتائج کی تعداد۔ یہ ہمیشہ 0 (ناممکن) سے 1 (یقینی) کے بیچ ہوتا ہے۔ ڈائس پر P(جفت) = 3 ÷ 6 = 1/2۔",
        ),
        "say": T(
            "Can we put a number on how likely something is?",
            "کیا ہم کسی بات کے امکان کو عدد سے بتا سکتے ہیں؟",
        ),
        "need": T(
            "Words like \"likely\" are not enough when two people disagree about a fair game. More than 350 years ago, French mathematicians Pascal and Fermat wrote to each other about how to share the prize of a game of chance that was stopped half way. This work helped start probability. The idea: count the outcomes you want, divide by all outcomes. P(E) = n(E) ÷ n(S), always between 0 and 1.",
            "جب دو لوگ کسی کھیل کے منصفانہ ہونے پر اختلاف کریں تو \"زیادہ امکان\" جیسے الفاظ کافی نہیں ہوتے۔ 350 سال سے زیادہ پہلے فرانس کے ریاضی دانوں پاسکل اور فرما نے ایک دوسرے کو خط لکھے کہ آدھے میں رکے ہوئے اتفاقی کھیل کے انعام کیسے بانٹی جائے۔ اس کام نے احتمال کی ابتدا میں مدد دی۔ خیال یہ ہے: مطلوبہ نتائج گنیں، سب نتائج پر تقسیم کریں۔ P(E) = n(E) ÷ n(S)، جو ہمیشہ 0 اور 1 کے بیچ ہوتا ہے۔",
        ),
        "use": T(
            "Where you will use it:\n• Weather: \"70% chance of rain\" is a probability.\n• Cricket: the chance of winning the toss is 1/2.\n• Games: the chance of rolling a 6 is 1/6.\n• Insurance and science: judging risk and testing medicines.",
            "آپ اسے کہاں استعمال کریں گے:\n• موسم: \"بارش کا 70 فیصد امکان\" ایک احتمال ہے۔\n• کرکٹ: ٹاس جیتنے کا احتمال 1/2 ہے۔\n• کھیل: ڈائس پر 6 آنے کا احتمال 1/6 ہے۔\n• بیمہ اور سائنس: خطرے کا اندازہ اور دواؤں کی جانچ۔",
        ),
    },
    "g6-maths-17-probability-word-problems": {
        "say": T(
            "A bag has 3 red and 5 blue balls. What is the chance of red?",
            "تھیلے میں 3 سرخ اور 5 نیلی گیندیں ہیں۔ سرخ نکلنے کا احتمال کیا ہے؟",
        ),
        "need": T(
            "Real chance questions come as stories: a bag of balls, a spinner, a class, a deck of cards. The skill that matters is to list or count the outcomes, find the ones we want, and write the probability as a fraction. Here 3 of 8 balls are red, so the chance is 3/8. Then say in words what the answer means.",
            "امکان کے حقیقی سوال کہانی کی شکل میں آتے ہیں: گیندوں کا تھیلا، گھومنے والی سوئی، جماعت، تاش کے پتے۔ اصل ہنر یہ ہے کہ نتائج کی فہرست بنائیں یا گنیں، مطلوبہ نتائج ڈھونڈیں، اور احتمال کو کسر کی صورت میں لکھیں۔ یہاں 8 میں سے 3 گیندیں سرخ ہیں، تو احتمال 3/8 ہے۔ پھر الفاظ میں بتائیں کہ جواب کا مطلب کیا ہے۔",
        ),
        "use": T(
            "Where you will use it:\n• Games and fairs: judging whether a lucky draw is fair.\n• School: the chance that a child picked at random is a girl.\n• Weather and sports: reading forecasts and match chances.\n• Everyday choices: weighing a small risk against a reward.",
            "آپ اسے کہاں استعمال کریں گے:\n• کھیل اور میلے: یہ جانچنا کہ قرعہ اندازی منصفانہ ہے یا نہیں۔\n• اسکول: بے ترتیب چنے گئے بچے کے لڑکی ہونے کا احتمال۔\n• موسم اور کھیل: پیش گوئیاں اور میچ جیتنے کا امکان سمجھنا۔\n• روزمرہ فیصلے: چھوٹے خطرے کو فائدے کے مقابل تولنا۔",
        ),
    },
}
