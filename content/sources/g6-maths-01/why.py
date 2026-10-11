"""The two "why" steps that open each Sets lesson (see why_steps.py):
why people needed the idea, and where it is used today."""


def T(en, ur):
    return {"en": en, "ur": ur}


WHY = {
    "g6-maths-01-what-is-a-set": {
        "define": T(
            "Definition: a set is a well-defined collection of things, called its elements. In braces: A = {2, 4, 6}. We write 4 ∈ A for \"4 is an element of A\", and 5 ∉ A for \"5 is not in A\".",
            "تعریف: سیٹ چیزوں کا ایسا واضح گروہ ہے جس میں ہر چیز کے بارے میں طے ہو کہ وہ اس میں ہے یا نہیں۔ ان چیزوں کو رکن کہتے ہیں۔ قوسین { } میں: A = {2, 4, 6}۔ 4 ∈ A یعنی \"4، A کا رکن ہے\"، اور 5 ∉ A یعنی \"5، A میں نہیں\"۔",
        ),
        "say": T(
            "How do you describe a group so clearly that nobody argues about it?",
            "کسی گروہ کو اتنا صاف کیسے بتائیں کہ کوئی بحث نہ کرے؟",
        ),
        "need": T(
            "\"Tall boys\" or \"good players\" is not clear: who decides? People needed a way to say exactly what is in a group, so that everyone agrees. A set is a well-defined collection: for any thing, you can say yes or no, it is in. About 150 years ago, a German mathematician, Georg Cantor, studied collections like this, and sets became one of the basic ideas of all maths.",
            "\"لمبے لڑکے\" یا \"اچھے کھلاڑی\" صاف بات نہیں ہے: فیصلہ کون کرے؟ لوگوں کو ایسا طریقہ چاہیے تھا کہ گروہ میں بالکل کیا ہے یہ طے ہو جائے اور سب متفق ہوں۔ سیٹ ایسا واضح گروہ ہے کہ ہر چیز کے بارے میں ہاں یا نہ میں کہہ سکیں کہ وہ اس میں ہے یا نہیں۔ تقریباً 150 سال پہلے جرمنی کے ریاضی دان جارج کینٹر نے ایسے گروہوں کا مطالعہ کیا، اور سیٹ پوری ریاضی کے بنیادی خیالوں میں شامل ہو گئے۔",
        ),
        "use": T(
            "Where you will use it:\n• School: the list of students in your class, or the subjects you study.\n• Shop: items in stock, kept apart from items sold out.\n• Phone: your contacts list; each name is in it once.\n• Computers: databases and websites sort things into sets.",
            "آپ اسے کہاں استعمال کریں گے:\n• اسکول: آپ کی جماعت کے طلبہ کی فہرست، یا وہ مضامین جو آپ پڑھتے ہیں۔\n• دکان: موجود سامان، اور وہ سامان جو ختم ہو گیا۔\n• فون: آپ کے رابطوں کی فہرست؛ ہر نام ایک بار ہوتا ہے۔\n• کمپیوٹر: ڈیٹا بیس اور ویب سائٹیں چیزوں کو سیٹوں میں ترتیب دیتی ہیں۔",
        ),
    },
    "g6-maths-01-kinds-of-sets": {
        "define": T(
            "Definition: an empty set has no elements, written { }. A finite set can be counted to the end, like {1, 2, 3}. An infinite set never ends, like {1, 2, 3, …}. Equal sets have exactly the same elements. Equivalent sets only have the same number of elements.",
            "تعریف: خالی سیٹ میں کوئی رکن نہیں ہوتا، اسے { } لکھتے ہیں۔ محدود سیٹ گنتے گنتے ختم ہو جاتا ہے، جیسے {1, 2, 3}۔ لامحدود سیٹ کبھی ختم نہیں ہوتا، جیسے {1, 2, 3, …}۔ برابر سیٹوں کے ارکان بالکل ایک جیسے ہوتے ہیں۔ ہم قوت سیٹوں میں صرف ارکان کی تعداد برابر ہوتی ہے۔",
        ),
        "say": T(
            "Can a group have nothing in it? Can a group never end?",
            "کیا کسی گروہ میں کچھ بھی نہ ہو سکتا ہے؟ کیا کوئی گروہ کبھی ختم نہ ہو؟",
        ),
        "need": T(
            "Real groups come in different kinds. A shop shelf may be empty today. The days of the week end at seven, but counting numbers never end. People needed names for these cases so that they could talk about them clearly: empty set, finite set, infinite set. They also needed to say when two sets are equal, or just have the same number of members.",
            "حقیقی گروہ کئی طرح کے ہوتے ہیں۔ دکان کی الماری آج خالی ہو سکتی ہے۔ ہفتے کے دن سات پر ختم ہو جاتے ہیں، مگر گنتی کے اعداد کبھی ختم نہیں ہوتے۔ لوگوں کو ان صورتوں کے نام چاہیے تھے تاکہ ان کے بارے میں صاف بات ہو سکے: خالی سیٹ، محدود سیٹ، لامحدود سیٹ۔ انہیں یہ بتانے کا طریقہ بھی چاہیے تھا کہ دو سیٹ کب برابر ہیں، اور کب صرف ان کے رکنوں کی تعداد برابر ہے۔",
        ),
        "use": T(
            "Where you will use it:\n• Shop: an empty shelf is the empty set; stock you can count is a finite set.\n• Class: the days of the week, or the months of the year.\n• Number games: even numbers go on forever, an infinite set.\n• Computers: a search that finds nothing gives an empty list.",
            "آپ اسے کہاں استعمال کریں گے:\n• دکان: خالی الماری خالی سیٹ ہے؛ گنا جا سکنے والا سامان محدود سیٹ ہے۔\n• جماعت: ہفتے کے دن، یا سال کے مہینے۔\n• اعداد کے کھیل: جفت اعداد ہمیشہ چلتے رہتے ہیں، یہ لامحدود سیٹ ہے۔\n• کمپیوٹر: جس تلاش میں کچھ نہ ملے وہ خالی فہرست دیتی ہے۔",
        ),
    },
    "g6-maths-01-subsets": {
        "define": T(
            "Definition: A is a subset of B, written A ⊆ B, if every element of A is also an element of B. For example, {1, 2} ⊆ {1, 2, 3}. The empty set is a subset of every set, and every set is a subset of itself.",
            "تعریف: اگر A کا ہر رکن B کا بھی رکن ہو تو A، B کا ذیلی سیٹ ہے، جسے A ⊆ B لکھتے ہیں۔ مثلاً {1, 2} ⊆ {1, 2, 3}۔ خالی سیٹ ہر سیٹ کا ذیلی سیٹ ہوتا ہے، اور ہر سیٹ اپنا ذیلی سیٹ بھی ہوتا ہے۔",
        ),
        "say": T(
            "Girls in your class are also students of the school. Is that a rule?",
            "آپ کی جماعت کی لڑکیاں اسکول کی طالبات بھی ہیں۔ کیا یہ کوئی اصول ہے؟",
        ),
        "need": T(
            "Some groups sit inside bigger groups: the cricket team is inside the class, and the class is inside the school. People needed an exact way to say \"every member of this group is also in that one\". That is a subset, written A ⊆ B. It also helps us count all the ways to pick some things from a group, for example which toppings to choose.",
            "کچھ گروہ بڑے گروہوں کے اندر ہوتے ہیں: کرکٹ ٹیم جماعت کے اندر ہے، اور جماعت اسکول کے اندر۔ لوگوں کو یہ کہنے کا درست طریقہ چاہیے تھا کہ \"اس گروہ کا ہر رکن اس دوسرے گروہ میں بھی ہے\"۔ یہی ذیلی سیٹ ہے، جسے A ⊆ B لکھتے ہیں۔ اس سے ہم یہ بھی گن سکتے ہیں کہ کسی گروہ میں سے کچھ چیزیں چننے کے کتنے طریقے ہیں، مثلاً کون سی چیزیں ڈالیں۔",
        ),
        "use": T(
            "Where you will use it:\n• School: a class is a subset of the school, a team is a subset of the class.\n• Shop: the fruits are a subset of everything the shop sells.\n• Choosing: with 3 flavours, you can pick in 8 ways, including none.\n• Computers: filters pick a subset, like only the unread messages.",
            "آپ اسے کہاں استعمال کریں گے:\n• اسکول: جماعت اسکول کا ذیلی سیٹ ہے، ٹیم جماعت کا ذیلی سیٹ۔\n• دکان: پھل دکان کے سارے سامان کا ذیلی سیٹ ہیں۔\n• انتخاب: 3 ذائقوں میں سے آپ 8 طریقوں سے چن سکتے ہیں، کچھ نہ چننا بھی شامل ہے۔\n• کمپیوٹر: فلٹر ایک ذیلی سیٹ چنتا ہے، جیسے صرف نہ پڑھے ہوئے پیغامات۔",
        ),
    },
    "g6-maths-01-union-and-intersection": {
        "define": T(
            "Definition: the union A ∪ B has all elements in A or B or both. The intersection A ∩ B has only elements in both. If A = {1, 2, 3} and B = {3, 4}, then A ∪ B = {1, 2, 3, 4} and A ∩ B = {3}.",
            "تعریف: اجتماع A ∪ B میں A یا B یا دونوں کے سب ارکان ہوتے ہیں۔ تقاطع A ∩ B میں صرف وہ ارکان ہوتے ہیں جو دونوں میں ہوں۔ اگر A = {1, 2, 3} اور B = {3, 4} ہو تو A ∪ B = {1, 2, 3, 4} اور A ∩ B = {3}۔",
        ),
        "say": T(
            "Ali likes cricket, Sara likes cricket and hockey. Who likes either game?",
            "علی کو کرکٹ پسند ہے، سارہ کو کرکٹ اور ہاکی۔ کسی ایک کھیل کو کون پسند کرتا ہے؟",
        ),
        "need": T(
            "Two groups often overlap. A teacher wants to invite everyone who plays cricket or hockey, but a child who plays both should be counted only once. She also needs those who play both. People needed clear names for these two jobs: the union A ∪ B puts the groups together, and the intersection A ∩ B keeps only what they share.",
            "دو گروہ اکثر ایک دوسرے سے ملتے ہیں۔ استاد کرکٹ یا ہاکی کھیلنے والے سب کو بلانا چاہتی ہے، مگر جو بچہ دونوں کھیلتا ہے اسے ایک ہی بار گننا ہے۔ اسے دونوں کھیلنے والے بھی الگ چاہییں۔ لوگوں کو ان دو کاموں کے صاف نام چاہیے تھے: اجتماع A ∪ B دونوں گروہوں کو ملاتا ہے، اور تقاطع A ∩ B صرف وہ رکھتا ہے جو دونوں میں مشترک ہو۔",
        ),
        "use": T(
            "Where you will use it:\n• School: students in the cricket team or the hockey team, counted once.\n• Shop: customers who buy tea and also buy sugar.\n• Phone: contacts who are friends and also family.\n• Search: a website search for \"red\" and \"shirt\" shows only what matches both.",
            "آپ اسے کہاں استعمال کریں گے:\n• اسکول: کرکٹ یا ہاکی ٹیم کے طلبہ، ہر ایک ایک بار گنا ہوا۔\n• دکان: وہ گاہک جو چائے بھی خریدتے ہیں اور چینی بھی۔\n• فون: وہ رابطے جو دوست بھی ہیں اور رشتہ دار بھی۔\n• تلاش: ویب سائٹ پر \"سرخ\" اور \"قمیص\" تلاش کریں تو صرف وہ آتا ہے جو دونوں سے ملتا ہو۔",
        ),
    },
    "g6-maths-01-universal-set-and-venn-diagrams": {
        "define": T(
            "Definition: the universal set U is the set of all the things we are talking about. A Venn diagram draws U as a box and each set as a circle inside it. Where two circles overlap, we see the elements that are in both sets.",
            "تعریف: عالمی سیٹ U ان تمام چیزوں کا سیٹ ہے جن کی ہم بات کر رہے ہوں۔ وین ڈایاگرام میں U کو ڈبے کی شکل میں اور ہر سیٹ کو اس کے اندر دائرے کی شکل میں بناتے ہیں۔ جہاں دو دائرے ملتے ہیں وہاں وہ ارکان نظر آتے ہیں جو دونوں سیٹوں میں ہوں۔",
        ),
        "say": T(
            "Can we draw a group so you can see who is in it?",
            "کیا ہم کسی گروہ کی تصویر بنا سکتے ہیں کہ دیکھ کر پتا چل جائے اس میں کون ہے؟",
        ),
        "need": T(
            "When groups overlap, a list of names is hard to follow. People needed a picture that shows everything at one glance. An English mathematician, John Venn, made such circle pictures popular more than 140 years ago. All the things we talk about go in one big box, the universal set U. Each group is a circle inside it, and the overlap shows what they share.",
            "جب گروہ آپس میں ملتے ہوں تو ناموں کی فہرست سے بات سمجھنا مشکل ہو جاتا ہے۔ لوگوں کو ایسی تصویر چاہیے تھی جو سب کچھ ایک نظر میں دکھا دے۔ انگلستان کے ریاضی دان جان وین نے 140 سال سے زیادہ پہلے ایسی دائروں والی تصویروں کو عام کیا۔ جن چیزوں کی ہم بات کر رہے ہیں وہ سب ایک بڑے ڈبے یعنی عالمی سیٹ U میں ہوتی ہیں۔ ہر گروہ اس کے اندر ایک دائرہ ہے، اور ملاپ کی جگہ مشترک چیزیں دکھاتی ہے۔",
        ),
        "use": T(
            "Where you will use it:\n• Surveys: how many children like mangoes, bananas, or both.\n• Class: who joined the quiz club, the art club, or both.\n• Explaining: a quick drawing makes a mixed-up problem clear.\n• Computers: charts that show what two lists have in common.",
            "آپ اسے کہاں استعمال کریں گے:\n• سروے: کتنے بچوں کو آم پسند ہیں، کتنوں کو کیلے، اور کتنوں کو دونوں۔\n• جماعت: کون کوئز کلب میں گیا، کون آرٹ کلب میں، اور کون دونوں میں۔\n• سمجھانا: ایک جلدی کی ڈرائنگ الجھا ہوا سوال صاف کر دیتی ہے۔\n• کمپیوٹر: ایسے چارٹ جو دکھاتے ہیں کہ دو فہرستوں میں کیا مشترک ہے۔",
        ),
    },
    "g6-maths-01-set-word-problems": {
        "say": T(
            "40 children, 25 like cricket, 20 like hockey. How many like both?",
            "40 بچے ہیں، 25 کو کرکٹ پسند ہے، 20 کو ہاکی۔ کتنوں کو دونوں پسند ہیں؟",
        ),
        "need": T(
            "Real questions rarely say \"find the union\". They tell a story with numbers, and we must find what is missing. Here 25 + 20 = 45 is more than 40, so some children were counted twice: 5 like both. The skill is to turn the story into sets and a Venn diagram, so that nobody is counted twice and nobody is missed.",
            "حقیقی سوال شاید ہی کہتے ہیں کہ \"اجتماع نکالو\"۔ وہ اعداد کے ساتھ ایک کہانی بتاتے ہیں اور ہمیں جو کم ہے وہ نکالنا ہوتا ہے۔ یہاں 25 + 20 = 45 ہے جو 40 سے زیادہ ہے، اس لیے کچھ بچے دو بار گنے گئے: 5 کو دونوں پسند ہیں۔ ہنر یہ ہے کہ کہانی کو سیٹوں اور وین ڈایاگرام میں بدلیں، تاکہ کوئی دو بار نہ گنا جائے اور کوئی رہ نہ جائے۔",
        ),
        "use": T(
            "Where you will use it:\n• Surveys: counting people who chose one answer, the other, or both.\n• School: planning clubs when some children join two.\n• Shops: customers who buy one item, another, or both.\n• Elections and polls: voters who fit more than one group.",
            "آپ اسے کہاں استعمال کریں گے:\n• سروے: ایک جواب، دوسرا جواب یا دونوں چننے والوں کی گنتی۔\n• اسکول: کلبوں کی منصوبہ بندی جب کچھ بچے دو کلبوں میں ہوں۔\n• دکانیں: وہ گاہک جو ایک چیز خریدیں، دوسری یا دونوں۔\n• انتخابات اور رائے شماری: وہ ووٹر جو ایک سے زیادہ گروہوں میں آتے ہیں۔",
        ),
    },
}
