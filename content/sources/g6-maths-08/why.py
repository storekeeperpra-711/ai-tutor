"""The two "why" steps that open each Area and Perimeter lesson (see why_steps.py):
why people needed the idea, and where it is used today."""


def T(en, ur):
    return {"en": en, "ur": ur}


WHY = {
    "g6-maths-08-perimeter": {
        "define": T(
            "Definition: the perimeter of a shape is the total distance around its edge: add the lengths of all its sides. For a rectangle, perimeter = 2 × (length + width), so a 6 m by 4 m rectangle has perimeter 2 × (6 + 4) = 20 m.",
            "تعریف: کسی شکل کا احاطہ اس کے کنارے کے گرد کل فاصلہ ہے: اس کے سب اضلاع کی لمبائیاں جمع کریں۔ مستطیل کا احاطہ = 2 × (لمبائی + چوڑائی)، اس لیے 6 میٹر × 4 میٹر کی مستطیل کا احاطہ 2 × (6 + 4) = 20 میٹر ہے۔",
        ),
        "say": T(
            "How much wire do we need to fence a field?",
            "کھیت کے گرد باڑ لگانے کے لیے کتنا تار چاہیے؟",
        ),
        "need": T(
            "A farmer who wants to fence his field must buy the right length of wire. Too little and the fence is not finished; too much and money is wasted. People needed a way to measure the distance all the way around a shape. We call it the perimeter: add up the lengths of all the sides. For a rectangle, 2 × (length + width).",
            "جو کسان اپنے کھیت کے گرد باڑ لگانا چاہتا ہے اسے تار کی ٹھیک لمبائی خریدنی ہوتی ہے۔ کم ہو تو باڑ پوری نہیں ہوتی، زیادہ ہو تو پیسے ضائع ہوتے ہیں۔ لوگوں کو شکل کے گرد پورے فاصلے کو ناپنے کا طریقہ چاہیے تھا۔ اسے احاطہ کہتے ہیں: تمام اضلاع کی لمبائیاں جمع کریں۔ مستطیل کے لیے 2 × (لمبائی + چوڑائی)۔",
        ),
        "use": T(
            "Where you will use it:\n• Fencing a field, a garden or a cricket ground.\n• Buying lace or a border for a dupatta or a tablecloth.\n• Putting a frame around a picture or a blackboard.\n• Running once round the school ground: how far is it?",
            "آپ اسے کہاں استعمال کریں گے:\n• کھیت، باغیچے یا کرکٹ گراؤنڈ کے گرد باڑ لگانے میں۔\n• دوپٹے یا میز پوش کے لیے لیس یا کنارہ خریدنے میں۔\n• تصویر یا بلیک بورڈ کے گرد فریم لگانے میں۔\n• اسکول کے گراؤنڈ کا ایک چکر دوڑنے پر: کتنا فاصلہ بنا؟",
        ),
    },
    "g6-maths-08-area-of-rectangles": {
        "define": T(
            "Definition: area is the amount of flat surface a shape covers, counted in unit squares. For a rectangle, area = length × width. A 6 m by 4 m rectangle has area 6 × 4 = 24 square metres (m²).",
            "تعریف: رقبہ وہ سطح ہے جسے کوئی شکل گھیرتی ہے، اسے اکائی مربعوں میں گنتے ہیں۔ مستطیل کا رقبہ = لمبائی × چوڑائی۔ 6 میٹر × 4 میٹر کی مستطیل کا رقبہ 6 × 4 = 24 مربع میٹر (m²) ہے۔",
        ),
        "say": T(
            "Two plots have the same fence. Do they have the same space?",
            "دو پلاٹوں کی باڑ برابر ہے۔ کیا ان میں جگہ بھی برابر ہے؟",
        ),
        "need": T(
            "Land is bought, sold and farmed by how much surface it covers, not only how long its edge is. A long thin plot and a square plot can have the same fence but very different space inside. People needed a number for the surface itself. We count unit squares: for a rectangle, area = length × width, in square metres.",
            "زمین اس لحاظ سے خریدی، بیچی اور کاشت کی جاتی ہے کہ وہ کتنی سطح گھیرتی ہے، صرف کنارے کی لمبائی سے نہیں۔ لمبا پتلا پلاٹ اور مربع پلاٹ ایک جیسی باڑ رکھ سکتے ہیں مگر اندر کی جگہ بہت مختلف ہوتی ہے۔ لوگوں کو خود سطح کے لیے ایک عدد چاہیے تھا۔ ہم اکائی مربعے گنتے ہیں: مستطیل کے لیے رقبہ = لمبائی × چوڑائی، مربع میٹر میں۔",
        ),
        "use": T(
            "Where you will use it:\n• How many floor tiles cover a room.\n• How much paint a wall needs.\n• The size of a plot or a field before buying or sowing.\n• Cloth needed to cover a table or a charpai.",
            "آپ اسے کہاں استعمال کریں گے:\n• کمرے کے فرش پر کتنی ٹائلیں لگیں گی۔\n• دیوار کے رنگ کے لیے کتنا پینٹ چاہیے۔\n• خریدنے یا بیج بونے سے پہلے پلاٹ یا کھیت کا سائز۔\n• میز یا چارپائی ڈھانپنے کے لیے کتنا کپڑا چاہیے۔",
        ),
    },
    "g6-maths-08-area-of-triangles": {
        "define": T(
            "Definition: area of a triangle = ½ × base × height, where the height is the straight-down distance from the top point to the base. A triangle with base 8 cm and height 5 cm has area ½ × 8 × 5 = 20 cm².",
            "تعریف: مثلث کا رقبہ = ½ × قاعدہ × اونچائی، جہاں اونچائی اوپر کے نقطے سے قاعدے تک سیدھا عمودی فاصلہ ہے۔ قاعدہ 8 سینٹی میٹر اور اونچائی 5 سینٹی میٹر والے مثلث کا رقبہ ½ × 8 × 5 = 20 مربع سینٹی میٹر ہے۔",
        ),
        "say": T(
            "A field is shaped like a triangle. How do we measure it?",
            "ایک کھیت مثلث کی شکل کا ہے۔ ہم اسے کیسے ناپیں؟",
        ),
        "need": T(
            "Not every plot is a rectangle. Many are cut at a slant by a road or a canal. People noticed that a triangle fits inside a rectangle with the same base and height, and fills exactly half of it. So we already know the answer: area of a triangle = ½ × base × height. A new shape was solved using a shape we knew.",
            "ہر پلاٹ مستطیل نہیں ہوتا۔ بہت سے سڑک یا نہر کی وجہ سے ترچھے کٹے ہوتے ہیں۔ لوگوں نے دیکھا کہ مثلث اسی قاعدے اور اونچائی والی مستطیل کے اندر آ جاتی ہے اور اس کا ٹھیک آدھا حصہ بھرتی ہے۔ یوں جواب ہمیں پہلے سے معلوم ہے: مثلث کا رقبہ = ½ × قاعدہ × اونچائی۔ نئی شکل کو ایک جانی پہچانی شکل کی مدد سے حل کر لیا گیا۔",
        ),
        "use": T(
            "Where you will use it:\n• A corner plot or field cut by a road or a canal.\n• Triangular roof ends and the sails of a boat.\n• A flag, a kite or a triangular signboard.\n• Cutting a triangle of cloth or card for a project.",
            "آپ اسے کہاں استعمال کریں گے:\n• سڑک یا نہر سے کٹا ہوا کونے کا پلاٹ یا کھیت۔\n• چھت کے مثلث سرے اور کشتی کے بادبان۔\n• جھنڈا، پتنگ یا مثلث کا سائن بورڈ۔\n• کسی پراجیکٹ کے لیے کپڑے یا گتے کی مثلث کاٹنا۔",
        ),
    },
    "g6-maths-08-parallelogram-and-trapezium": {
        "define": T(
            "Definition: a parallelogram has two pairs of parallel sides; its area = base × height. A trapezium has one pair of parallel sides; its area = ½ × (sum of the parallel sides) × height. With parallel sides 5 cm and 9 cm and height 4 cm: ½ × (5 + 9) × 4 = 28 cm².",
            "تعریف: متوازی الاضلاع کے متوازی اضلاع کے دو جوڑے ہوتے ہیں؛ رقبہ = قاعدہ × اونچائی۔ ذوزنقہ میں ایک جوڑا متوازی ہوتا ہے؛ رقبہ = ½ × (متوازی اضلاع کا مجموعہ) × اونچائی۔ 5 اور 9 سینٹی میٹر کے متوازی اضلاع اور 4 سینٹی میٹر اونچائی پر ½ × (5 + 9) × 4 = 28 مربع سینٹی میٹر۔",
        ),
        "say": T(
            "A plot has slanted sides. Can we still find its area?",
            "ایک پلاٹ کے اضلاع ترچھے ہیں۔ کیا ہم پھر بھی اس کا رقبہ نکال سکتے ہیں؟",
        ),
        "need": T(
            "Real plots, roofs and windows often have slanted sides, so they are not rectangles. The good news is that we can cut and move pieces. A parallelogram can be cut and moved into a rectangle: area = base × height. A trapezium is two triangles joined: area = ½ × (sum of the parallel sides) × height. Old tools solve the new shapes.",
            "اصل پلاٹوں، چھتوں اور کھڑکیوں کے اضلاع اکثر ترچھے ہوتے ہیں، اس لیے وہ مستطیل نہیں ہوتے۔ اچھی بات یہ ہے کہ ہم ٹکڑے کاٹ کر ہٹا سکتے ہیں۔ متوازی الاضلاع کو کاٹ کر مستطیل بنایا جا سکتا ہے: رقبہ = قاعدہ × اونچائی۔ ذوزنقہ دو مثلثوں سے مل کر بنتا ہے: رقبہ = ½ × (متوازی اضلاع کا مجموعہ) × اونچائی۔ پرانے طریقے نئی شکلیں حل کر دیتے ہیں۔",
        ),
        "use": T(
            "Where you will use it:\n• Land plots with slanted sides.\n• Sloping roofs and the side of a ramp.\n• Windows, tiles and bricks laid in slanted patterns.\n• A canal or a bucket whose sides lean outwards.",
            "آپ اسے کہاں استعمال کریں گے:\n• ترچھے اضلاع والے زمین کے پلاٹ۔\n• ڈھلوان چھتیں اور ریمپ کا پہلو۔\n• کھڑکیاں، ٹائلیں اور ترچھے ڈیزائن میں لگی اینٹیں۔\n• نہر یا بالٹی جس کے پہلو باہر کو جھکے ہوں۔",
        ),
    },
    "g6-maths-08-compound-shapes": {
        "define": T(
            "Definition: a compound shape is made by joining simple shapes, such as rectangles. To find its area, split it into simple pieces and add, or take the empty part away from a big rectangle. Pieces of 12 m² and 8 m² make 12 + 8 = 20 m².",
            "تعریف: مرکب شکل سادہ شکلوں، جیسے مستطیلوں، کو جوڑ کر بنتی ہے۔ اس کا رقبہ نکالنے کے لیے اسے سادہ ٹکڑوں میں بانٹ کر جمع کریں، یا بڑی مستطیل میں سے خالی حصہ تفریق کریں۔ 12 مربع میٹر اور 8 مربع میٹر کے ٹکڑے مل کر 12 + 8 = 20 مربع میٹر بناتے ہیں۔",
        ),
        "say": T(
            "A floor is shaped like the letter L. How do we find its area?",
            "ایک فرش حرف L کی شکل کا ہے۔ اس کا رقبہ کیسے نکالیں؟",
        ),
        "need": T(
            "Rooms, houses and gardens are often joined from several rectangles, like an L-shaped hall. There is no single formula for them, and we do not need one. We use two ideas: split the shape into rectangles and add their areas, or put a big rectangle around it and take away the empty part. Both ways give the same answer.",
            "کمرے، گھر اور باغیچے اکثر کئی مستطیلوں کو جوڑ کر بنتے ہیں، جیسے L شکل کا ہال۔ ان کے لیے کوئی ایک فارمولا نہیں اور اس کی ضرورت بھی نہیں۔ ہم دو خیال استعمال کرتے ہیں: شکل کو مستطیلوں میں بانٹ کر رقبے جمع کریں، یا اس کے گرد بڑی مستطیل بنا کر خالی حصہ گھٹا دیں۔ دونوں طریقوں سے ایک ہی جواب آتا ہے۔",
        ),
        "use": T(
            "Where you will use it:\n• Tiles for an L-shaped room or a house with a courtyard.\n• Paint for a wall with a door and a window cut out.\n• The area of a garden with a flower bed in the middle.\n• A plan of a school building drawn on paper.",
            "آپ اسے کہاں استعمال کریں گے:\n• L شکل کے کمرے یا صحن والے گھر کے لیے ٹائلیں۔\n• دروازے اور کھڑکی کٹی ہوئی دیوار کے رنگ کے لیے پینٹ۔\n• ایسے باغیچے کا رقبہ جس کے بیچ میں پھولوں کی کیاری ہو۔\n• کاغذ پر بنا ہوا اسکول کی عمارت کا نقشہ۔",
        ),
    },
    "g6-maths-08-area-of-a-path": {
        "define": T(
            "Definition: a path is a strip of equal width around a shape. Its area = area of the outer rectangle − area of the inner rectangle. A 10 m by 8 m garden with a 1 m wide path makes an outer rectangle 12 m by 10 m: 12 × 10 − 10 × 8 = 40 m².",
            "تعریف: راستہ شکل کے گرد برابر چوڑائی کی پٹی ہے۔ راستے کا رقبہ = باہر کی مستطیل کا رقبہ − اندر کی مستطیل کا رقبہ۔ 10 × 8 میٹر کے باغ کے گرد 1 میٹر چوڑا راستہ ہو تو باہر کی مستطیل 12 × 10 میٹر بنتی ہے: 12 × 10 − 10 × 8 = 40 مربع میٹر۔",
        ),
        "say": T(
            "A path runs around a park. How much ground does it cover?",
            "پارک کے گرد ایک راستہ بنا ہے۔ وہ کتنی زمین گھیرتا ہے؟",
        ),
        "need": T(
            "Paths run around fields, ponds and gardens, and someone must pay for the bricks, cement or grass to cover them. A path is a ring-shaped space between an inner and an outer rectangle. People found the easy way: area of the outer rectangle minus area of the inner rectangle. The difference is just the path.",
            "راستے کھیتوں، تالابوں اور باغیچوں کے گرد بنتے ہیں، اور کسی کو ان پر لگنے والی اینٹوں، سیمنٹ یا گھاس کا خرچ دینا ہوتا ہے۔ راستہ اندر اور باہر کی دو مستطیلوں کے درمیان چھلّے جیسی جگہ ہے۔ لوگوں نے آسان طریقہ نکالا: باہر کی مستطیل کا رقبہ منفی اندر کی مستطیل کا رقبہ۔ فرق ہی راستہ ہے۔",
        ),
        "use": T(
            "Where you will use it:\n• Bricks or tiles for a path around a lawn.\n• A border around a swimming pool or a pond.\n• A frame around a photo or a notice board.\n• The wall around a house plot: how much surface does it cover?",
            "آپ اسے کہاں استعمال کریں گے:\n• لان کے گرد راستے کے لیے اینٹیں یا ٹائلیں۔\n• سوئمنگ پول یا تالاب کے گرد کنارہ۔\n• تصویر یا نوٹس بورڈ کے گرد فریم۔\n• گھر کے پلاٹ کے گرد دیوار: وہ کتنی سطح گھیرتی ہے؟",
        ),
    },
    "g6-maths-08-area-word-problems": {
        "say": T(
            "A shopkeeper asks: perimeter or area, which one do I pay for?",
            "دکان دار پوچھتا ہے: احاطہ یا رقبہ، مجھے کس کے پیسے دینے ہیں؟",
        ),
        "need": T(
            "In real life nobody says \"find the area\". They say: how much tile do I need, or how much fence? The skill that matters is to read the story and decide: is it the edge (perimeter, paid per metre) or the surface (area, paid per square metre)? Then use the right formula and add the cost. This saves money and avoids mistakes.",
            "حقیقی زندگی میں کوئی نہیں کہتا \"رقبہ نکالیں\"۔ وہ کہتے ہیں: کتنی ٹائل چاہیے، یا کتنی باڑ؟ اصل ہنر یہ ہے کہ کہانی پڑھ کر فیصلہ کریں: کنارہ ہے (احاطہ، فی میٹر قیمت) یا سطح ہے (رقبہ، فی مربع میٹر قیمت)؟ پھر صحیح فارمولا لگائیں اور خرچ جمع کریں۔ اس سے پیسے بچتے ہیں اور غلطیاں نہیں ہوتیں۔",
        ),
        "use": T(
            "Where you will use it:\n• Estimating the cost of tiles, paint or carpet.\n• Fencing a farm or a plot and paying per metre.\n• Planning a garden or a cricket pitch.\n• Understanding a builder's or a contractor's estimate.",
            "آپ اسے کہاں استعمال کریں گے:\n• ٹائلوں، پینٹ یا قالین کا خرچ اندازہ کرنے میں۔\n• فارم یا پلاٹ کی باڑ لگانا اور فی میٹر ادائیگی کرنا۔\n• باغیچے یا کرکٹ پچ کی منصوبہ بندی۔\n• معمار یا ٹھیکے دار کا تخمینہ سمجھنے میں۔",
        ),
    },
}
