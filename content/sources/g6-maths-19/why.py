"""The two "why" steps that open each Constructions lesson (see
why_steps.py): why people needed the idea, and where it is used today."""


def T(en, ur):
    return {"en": en, "ur": ur}


WHY = {
    "g6-maths-19-bisectors-and-perpendiculars": {
        "define": T(
            "Definition: a bisector cuts something into two equal parts. The perpendicular bisector of a line AB passes through its midpoint M and meets AB at 90°. Every point on it is the same distance from A and from B.",
            "تعریف: ناصف کسی چیز کو دو برابر حصوں میں بانٹتا ہے۔ لکیر AB کا عمودی ناصف اس کے درمیانی نقطہ M سے گزرتا ہے اور AB سے 90° پر ملتا ہے۔ اس کا ہر نقطہ A اور B سے برابر فاصلے پر ہوتا ہے۔",
        ),
        "say": T(
            "How does a builder find the exact middle of a wall or a straight corner?",
            "معمار دیوار کا ٹھیک بیچ یا سیدھا کونا کیسے ڈھونڈتا ہے؟",
        ),
        "need": T(
            "Builders, tailors and farmers have always needed an exact middle point and a square corner. Guessing by eye gives crooked walls and uneven fields. A ruler and a pair of compasses solve this: two arcs from each end of a line cross at two points, and the line through them cuts it exactly in half and meets it at 90°. No guessing is needed, and anyone gets the same result.",
            "معماروں، درزیوں اور کسانوں کو ہمیشہ ٹھیک بیچ کا نقطہ اور سیدھا کونا چاہیے رہا ہے۔ آنکھ سے اندازہ لگانے پر دیواریں ٹیڑھی اور کھیت اونچے نیچے بنتے ہیں۔ پیمانہ اور پرکار یہ مسئلہ حل کرتے ہیں: لکیر کے ہر سرے سے دو قوس ایک دوسرے کو دو نقطوں پر کاٹتے ہیں، اور ان سے گزرتی لکیر اسے ٹھیک آدھا کرتی ہے اور 90° پر ملتی ہے۔ اندازہ نہیں لگانا پڑتا اور ہر کسی کو ایک ہی نتیجہ ملتا ہے۔",
        ),
        "use": T(
            "Where you will use it:\n• Building: marking the centre of a wall, a door or a room.\n• Tailoring: folding cloth exactly in half, and a square corner.\n• Farming: marking out a square or rectangular field.\n• Design: making patterns and drawing maps.",
            "آپ اسے کہاں استعمال کریں گے:\n• تعمیر: دیوار، دروازے یا کمرے کا بیچ نشان زد کرنا۔\n• درزی کا کام: کپڑے کو ٹھیک آدھا موڑنا، اور سیدھا کونا۔\n• کھیتی: مربع یا مستطیل کھیت کا نشان لگانا۔\n• ڈیزائن: نقش و نگار بنانا، اور نقشے کھینچنا۔",
        ),
    },
    "g6-maths-19-constructing-angles": {
        "define": T(
            "Definition: constructing means drawing exactly with only a ruler and a pair of compasses. An angle bisector is the ray that splits an angle into two equal angles. We can construct 60° and 90°, and bisecting them gives 30° and 45°.",
            "تعریف: تعمیر کا مطلب صرف پیمانے اور پرکار سے ٹھیک ٹھیک بنانا ہے۔ زاویے کا ناصف وہ شعاع ہے جو زاویے کو دو برابر زاویوں میں بانٹے۔ ہم 60° اور 90° بنا سکتے ہیں، اور انہیں آدھا کرنے سے 30° اور 45° ملتے ہیں۔",
        ),
        "say": T(
            "A carpenter has no protractor. How can he still make a perfect 60° or 90° corner?",
            "بڑھئی کے پاس پروٹریکٹر نہیں ہے۔ وہ پھر بھی ٹھیک 60° یا 90° کا کونا کیسے بنائے؟",
        ),
        "need": T(
            "Craftsmen need exact angles for roof beams, window frames and tiles. A measuring tool can be wrong or missing, but a compass and a ruler always work. With arcs of the same width we can make a 60° angle, and by halving it, 30°. We can also split any angle exactly in half with a bisector. This is a way to build angles with no numbers to read.",
            "کاریگروں کو چھت کی کڑیوں، کھڑکی کے چوکھٹوں اور ٹائلوں کے لیے ٹھیک زاویے چاہیے ہوتے ہیں۔ ناپنے کا آلہ غلط یا غائب ہو سکتا ہے، مگر پرکار اور پیمانہ ہمیشہ کام کرتے ہیں۔ ایک ہی کھلاؤ کی قوسوں سے ہم 60° کا زاویہ بنا سکتے ہیں، اور اسے آدھا کر کے 30°۔ ناصف سے کسی بھی زاویے کو ٹھیک آدھا بھی کر سکتے ہیں۔ یہ زاویے بنانے کا ایسا طریقہ ہے جس میں کوئی عدد پڑھنا نہیں پڑتا۔",
        ),
        "use": T(
            "Where you will use it:\n• Carpentry: roof frames, doors and window corners.\n• Tiling and floors: patterns with neat angles.\n• Art and design: stars, kites and geometric patterns.\n• Technical drawing: plans for engineers and architects.",
            "آپ اسے کہاں استعمال کریں گے:\n• بڑھئی کا کام: چھت کے ڈھانچے، دروازوں اور کھڑکیوں کے کونے۔\n• ٹائل اور فرش: صاف زاویوں والے نقش۔\n• آرٹ اور ڈیزائن: ستارے، پتنگیں اور جیومیٹری کے نقش۔\n• تکنیکی ڈرائنگ: انجینئروں اور نقشہ نویسوں کے نقشے۔",
        ),
    },
    "g6-maths-19-unknown-angles-and-construction-problems": {
        "define": T(
            "Definition: angles on a straight line add up to 180°, angles around a point add up to 360°, and the angles of a triangle add up to 180°. For example, if one angle on a straight line is 65°, the other is 180° − 65° = 115°.",
            "تعریف: سیدھی لکیر پر زاویوں کا مجموعہ 180° ہوتا ہے، ایک نقطے کے گرد 360°، اور مثلث کے زاویوں کا مجموعہ 180°۔ مثلاً سیدھی لکیر پر ایک زاویہ 65° ہو تو دوسرا 180° − 65° = 115° ہے۔",
        ),
        "say": T(
            "How can I find an angle I cannot measure?",
            "جو زاویہ میں ناپ نہیں سکتا اسے کیسے معلوم کروں؟",
        ),
        "need": T(
            "Sometimes an angle is hard to reach or measure, like the corner of a roof high up, or a bend in a road on a map. But angles follow fixed rules: angles on a straight line add up to 180°, around a point to 360°, and in a triangle to 180°. With these facts we can work out the missing angle by sums alone. Real construction problems also need us to draw and then check our work.",
            "کبھی کسی زاویے تک پہنچنا یا اسے ناپنا مشکل ہوتا ہے، جیسے اونچی چھت کا کونا، یا نقشے پر سڑک کا موڑ۔ مگر زاویے پکے اصولوں پر چلتے ہیں: سیدھی لکیر پر زاویوں کا مجموعہ 180°، ایک نقطے کے گرد 360°، اور مثلث میں 180°۔ ان حقیقتوں سے ہم گم زاویہ صرف حساب سے نکال لیتے ہیں۔ تعمیر کے اصل سوالوں میں ہمیں بنانا بھی پڑتا ہے اور اپنا کام جانچنا بھی۔",
        ),
        "use": T(
            "Where you will use it:\n• Building: checking that a roof slope or a ramp is right.\n• Maps: finding directions and angles between roads.\n• Cricket and football: the angle of a shot or a pass.\n• Later: geometry, surveying and engineering.",
            "آپ اسے کہاں استعمال کریں گے:\n• تعمیر: جانچنا کہ چھت کی ڈھلان یا ریمپ ٹھیک ہے۔\n• نقشے: سمتیں اور سڑکوں کے درمیان زاویے معلوم کرنا۔\n• کرکٹ اور فٹ بال: شاٹ یا پاس کا زاویہ۔\n• آگے چل کر: جیومیٹری، پیمائش زمین اور انجینئرنگ۔",
        ),
    },
}
