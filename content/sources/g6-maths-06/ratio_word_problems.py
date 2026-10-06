from common import (T, opt, say, wrong, ratio, simplest, same_ratio, share, missing_term,
                    ratio_question, number_question, write,
                    REF, REVIEW, RATIO_MEANING, RATIO_EQUIVALENT, RATIO_SHARE, RATIO_PROPORTION,
                    UNITARY, RATIO_WORD_PROBLEMS)

SKILL = RATIO_WORD_PROBLEMS

# s4, s5: 4 people eat 12 rotis; 10 people?
ROTIS_EACH = 12 // 4
ROTIS_10 = ROTIS_EACH * 10
assert ROTIS_10 == 30 and 12 + (10 - 4) == 18

# s6: Zahid and Asif put Rs 3000 and Rs 2000 into a shop; profit Rs 1500 shared 3 : 2.
assert simplest(3000, 2000) == (3, 2)
ZAHID, ASIF = share(1500, (3, 2))
assert (ZAHID, ASIF) == (900, 600)

# s7: 240 students, 96 girls: girls to boys in simplest form.
BOYS_7 = 240 - 96
S7 = simplest(96, BOYS_7)
assert BOYS_7 == 144 and S7 == (2, 3)
assert simplest(96, 240) == (2, 5)

# s8: a 5 m pole casts a 3 m shadow; a tree casts a 12 m shadow at the same time.
TREE = missing_term(3, 5, 12)  # shadow : height :: shadow : height
assert TREE == 20 and 5 + (12 - 3) == 14

# s9: boys to girls 3 : 4 and there are 21 boys.
ONE_PART_9 = 21 // 3
GIRLS_9 = 4 * ONE_PART_9
assert ONE_PART_9 == 7 and GIRLS_9 == 28 and (21 // 7) * 4 == 12

# The unit test.
U2 = simplest(18, 24)
assert U2 == (3, 4)
U3 = share(56, (3, 5))
assert U3 == [21, 35]
U4 = 6 * 15 // 9
assert U4 == 10 and same_ratio(6, 9, U4, 15)
U5 = (540 // 3) * 5
assert U5 == 900

# Question bank and review.
assert share(800, (3, 5)) == [300, 500]
assert (12 // 3) * 8 == 32
MAP_KM = missing_term(2, 5, 14)
assert MAP_KM == 35 and 5 + (14 - 2) == 17
PAINT_BLUE = 2 * (15 // 5)
assert PAINT_BLUE == 6 and same_ratio(2, 5, PAINT_BLUE, 15) and 15 - 3 == 12

lesson = {
 "id": "g6-maths-06-ratio-word-problems",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Solve real-life problems with ratios: comparing, sharing, proportion and the unitary method, choosing the right method for each problem.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Ratio word problems", "نسبت کے عملی سوالات"),
 "estimated_minutes": 18,
 "prerequisites": [{"skill": RATIO_MEANING}, {"skill": RATIO_EQUIVALENT}, {"skill": RATIO_SHARE},
                   {"skill": RATIO_PROPORTION}, {"skill": UNITARY}],
 "misconceptions": [
   {"id": "share_vs_total", "description": "Treats one person's share as the total (divides it by all the parts), or the total as one share."},
   {"id": "additive_thinking", "description": "Adds the difference instead of scaling (4 people eat 12 rotis, so 10 people eat 18)."},
   {"id": "order_swapped", "description": "Writes or uses the ratio the wrong way round."},
   {"id": "part_for_whole", "description": "Compares a part with the whole when the question asks for part to part."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_which_method", "type": "recall", "step": {
     "id": "qb_which_method", "type": "choice",
     "prompt": T("\"Share Rs 800 between two sisters in the ratio 3 : 5.\" Which method do you use?", "\"800 روپے دو بہنوں میں 3 : 5 کی نسبت سے تقسیم کریں۔\" آپ کون سا طریقہ استعمال کریں گے؟"),
     "options": [
       opt("share", "Add the parts (8), find one part, multiply.", "حصے جمع کریں (8)، ایک حصہ معلوم کریں، ضرب دیں۔", True,
           "Yes! You know the total, so add the parts: 800 ÷ 8 = 100, shares Rs 300 and Rs 500.", "جی ہاں! کل معلوم ہے، اس لیے حصے جمع کریں: 800 ÷ 8 = 100، حصے 300 روپے اور 500 روپے۔"),
       opt("half", "Halve it.", "آدھا کریں۔", False,
           "Halving is only for 1 : 1. Here it is 3 : 5.", "آدھا صرف 1 : 1 کے لیے ہے۔ یہاں 3 : 5 ہے۔"),
       opt("unitary", "Find the price of one sister.", "ایک بہن کی قیمت معلوم کریں۔", False,
           "There's no price here. You know the total, so share it in the ratio.", "یہاں کوئی قیمت نہیں۔ کل معلوم ہے، اس لیے اسے نسبت میں بانٹیں۔"),
     ]}},
   {"id": "qb_kites", "type": "apply", "step": number_question(
     "qb_kites",
     T("3 kites need 12 m of string. How many metres of string do 8 kites need?", "3 پتنگوں کے لیے 12 میٹر ڈور چاہیے۔ 8 پتنگوں کے لیے کتنے میٹر ڈور چاہیے؟"),
     32,
     T("How much string does 1 kite need?", "1 پتنگ کو کتنی ڈور چاہیے؟"),
     T("Right! 1 kite needs 4 m, so 8 kites need 32 m.", "درست! 1 پتنگ کو 4 میٹر، اس لیے 8 پتنگوں کو 32 میٹر۔"),
     T("12 ÷ 3 = 4 m for one kite. 8 × 4 = 32 m.", "ایک پتنگ: 12 ÷ 3 = 4 میٹر۔ 8 × 4 = 32 میٹر۔"),
     common_wrong=[wrong(17, "5 more kites need much more than 5 m. Find 1 kite first.", "5 پتنگیں زیادہ کے لیے 5 میٹر سے کہیں زیادہ چاہیے۔ پہلے 1 پتنگ معلوم کریں۔", "additive_thinking")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Sana and Rabia share sweets in the ratio 2 : 5. Sana gets 10. Rabia says: \"10 ÷ 7 parts...\" and gets stuck. What should she do?", "ثنا اور رابعہ مٹھائی 2 : 5 کی نسبت سے بانٹتی ہیں۔ ثنا کو 10 ملتی ہیں۔ رابعہ کہتی ہے: \"10 ÷ 7 حصے...\" اور الجھ جاتی ہے۔ اسے کیا کرنا چاہیے؟"),
     "options": [
       opt("parts", "10 is Sana's 2 parts, not the total. One part is 5, so Rabia gets 25.", "10 ثنا کے 2 حصے ہیں، کل نہیں۔ ایک حصہ 5، اس لیے رابعہ کو 25۔", True,
           "Right! Divide a share by its own parts: 10 ÷ 2 = 5, then 5 × 5 = 25.", "درست! حصے کو اس کے اپنے حصوں سے تقسیم کریں: 10 ÷ 2 = 5، پھر 5 × 5 = 25"),
       opt("total", "Divide by 7 anyway and round.", "پھر بھی 7 سے تقسیم کر کے قریب ترین عدد لیں۔", False,
           "10 is not the total, so 7 is the wrong number of parts. Sana's 10 is 2 parts.", "10 کل نہیں، اس لیے 7 غلط تعداد ہے۔ ثنا کی 10، 2 حصے ہیں۔", "share_vs_total"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_choose", "front": T("Ratio problem: which method?", "نسبت کا سوال: کون سا طریقہ؟"),
    "back": T("Total known → add the parts and share. One pair known (4 pens Rs 120) → unitary method or proportion. Two amounts to compare → write a ratio and simplify.", "کل معلوم ← حصے جمع کر کے بانٹیں۔ ایک جوڑا معلوم (4 قلم 120 روپے) ← اکائی کا طریقہ یا تناسب۔ دو مقداروں کا موازنہ ← نسبت لکھ کر سادہ کریں۔")},
   {"id": "f_share_known", "front": T("You know ONE share, not the total. What next?", "آپ کو ایک حصہ معلوم ہے، کل نہیں۔ اب کیا؟"),
    "back": T("Divide that share by its own number of parts to find one part. 2 : 5, first share 10 → one part 5 → second share 25.", "اس حصے کو اس کے اپنے حصوں سے تقسیم کر کے ایک حصہ معلوم کریں۔ 2 : 5، پہلا حصہ 10 ← ایک حصہ 5 ← دوسرا حصہ 25")},
 ],
 "home_tasks": [{"id": "h_recipe", "text": T(
   "Ask someone at home for a recipe (like chai or rice) and how many people it is for. Work out how much of each thing is needed for your whole family.",
   "گھر میں کسی سے کوئی ترکیب پوچھیں (جیسے چائے یا چاول) اور یہ کتنے لوگوں کے لیے ہے۔ حساب لگائیں کہ پورے گھر والوں کے لیے ہر چیز کتنی چاہیے۔")}],
 "glossary": [T("Ratio", "نسبت"), T("Proportion", "تناسب"), T("Share", "حصہ"), T("Unitary method", "اکائی کا طریقہ"), T("Profit", "منافع")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Ratios are everywhere: in the kitchen, the shop and the bazaar! Ready to solve real problems?",
                     "نسبتیں ہر جگہ ہیں: باورچی خانے میں، دکان میں اور بازار میں! کیا آپ اصل سوال حل کرنے کے لیے تیار ہیں؟"),
    "text": T("In this lesson you read a story, choose the method, and solve it. At the end there is a short test on the whole Ratio and Proportion unit. First, a quick check.",
              "اس سبق میں آپ کہانی پڑھیں گے، طریقہ چنیں گے، اور حل کریں گے۔ آخر میں نسبت اور تناسب کے پورے باب پر ایک چھوٹا ٹیسٹ ہے۔ پہلے ایک چھوٹا سا سوال۔")},
   {"id": "s2_foundation", "type": "choice", "question_type": "recall", "skill": RATIO_SHARE,
    "prompt": T("To share an amount in the ratio 3 : 5, how many equal parts do you cut it into?", "کسی مقدار کو 3 : 5 کی نسبت میں بانٹنے کے لیے اسے کتنے برابر حصوں میں کاٹتے ہیں؟"),
    "options": [
      opt("eight", "8", "8", True, "Yes! 3 + 5 = 8 parts.", "جی ہاں! 3 + 5 = 8 حصے۔"),
      opt("fifteen", "15", "15", False, "Add the parts, don't multiply: 3 + 5 = 8.", "حصے جمع کریں، ضرب نہ دیں: 3 + 5 = 8"),
      opt("two", "2", "2", False, "There are 2 people, but 3 + 5 = 8 parts.", "لوگ 2 ہیں، لیکن 3 + 5 = 8 حصے ہیں۔"),
    ]},
   {"id": "s3_which_method", "type": "explain",
    "character": say("thinking", "Ask yourself: what do I know, and what do I want?", "خود سے پوچھیں: مجھے کیا معلوم ہے، اور کیا چاہیے؟"),
    "text": T("Know the TOTAL and a ratio? Add the parts and share. Know ONE PAIR (4 pens cost Rs 120) and want another? Use the unitary method or a proportion. Want to COMPARE two amounts? Write a ratio in the right order and simplify. Always check: does the answer make sense?",
              "کل اور نسبت معلوم ہے؟ حصے جمع کر کے بانٹیں۔ ایک جوڑا معلوم ہے (4 قلم 120 روپے) اور دوسرا چاہیے؟ اکائی کا طریقہ یا تناسب استعمال کریں۔ دو مقداروں کا موازنہ کرنا ہے؟ صحیح ترتیب میں نسبت لکھ کر سادہ کریں۔ ہمیشہ جانچیں: کیا جواب سمجھ میں آتا ہے؟")},
   {"id": "s4_choose", "type": "choice", "question_type": "apply",
    "prompt": T("\"At a dawat, 4 guests eat 12 rotis. How many rotis do 10 guests eat?\" Which method fits?", "\"ایک دعوت میں 4 مہمان 12 روٹیاں کھاتے ہیں۔ 10 مہمان کتنی روٹیاں کھائیں گے؟\" کون سا طریقہ ٹھیک ہے؟"),
    "options": [
      opt("unitary", "Unitary method: rotis for 1 guest, then 10 guests.", "اکائی کا طریقہ: 1 مہمان کی روٹیاں، پھر 10 مہمان۔", True,
          "Yes! We know one pair (4 guests, 12 rotis) and want another.", "جی ہاں! ہمیں ایک جوڑا معلوم ہے (4 مہمان، 12 روٹیاں) اور دوسرا چاہیے۔"),
      opt("share", "Sharing: add 4 + 12.", "تقسیم: 4 + 12 جمع کریں۔", False,
          "4 and 12 are guests and rotis, not parts of a total.", "4 اور 12 مہمان اور روٹیاں ہیں، کسی کل کے حصے نہیں۔"),
      opt("add", "Add 6 rotis for 6 more guests.", "6 مہمان زیادہ کے لیے 6 روٹیاں جمع کریں۔", False,
          "Each guest eats more than 1 roti! Find rotis for 1 guest.", "ہر مہمان 1 سے زیادہ روٹی کھاتا ہے! 1 مہمان کی روٹیاں معلوم کریں۔", "additive_thinking"),
    ]},
   number_question(
     "s5_rotis",
     T("Now solve it: 4 guests eat 12 rotis. How many rotis do 10 guests eat?", "اب حل کریں: 4 مہمان 12 روٹیاں کھاتے ہیں۔ 10 مہمان کتنی روٹیاں کھائیں گے؟"),
     ROTIS_10,
     T("1 guest eats 12 ÷ 4 rotis.", "1 مہمان 12 ÷ 4 روٹیاں کھاتا ہے۔"),
     T(f"Right! {ROTIS_EACH} rotis each, so 10 × {ROTIS_EACH} = {ROTIS_10}.", f"درست! ہر ایک {ROTIS_EACH} روٹیاں، اس لیے 10 × {ROTIS_EACH} = {ROTIS_10}"),
     T(f"12 ÷ 4 = {ROTIS_EACH} rotis for one guest. 10 × {ROTIS_EACH} = {ROTIS_10}.", f"ایک مہمان: 12 ÷ 4 = {ROTIS_EACH} روٹیاں۔ 10 × {ROTIS_EACH} = {ROTIS_10}"),
     common_wrong=[wrong(18, "6 more guests eat more than 6 rotis: each eats 3.", "6 مہمان زیادہ 6 سے زیادہ روٹیاں کھائیں گے: ہر ایک 3 کھاتا ہے۔", "additive_thinking"),
                   wrong(120, "12 rotis are for 4 guests, not 1. Divide by 4 first.", "12 روٹیاں 4 مہمانوں کی ہیں، 1 کی نہیں۔ پہلے 4 سے تقسیم کریں۔")]),
   number_question(
     "s6_profit",
     T("Zahid put Rs 3000 and Asif Rs 2000 into a small shop. They share the profit of Rs 1500 in the same ratio, 3 : 2. How much does Zahid get, in rupees?",
       "زاہد نے ایک چھوٹی دکان میں 3000 روپے اور آصف نے 2000 روپے لگائے۔ وہ 1500 روپے منافع اسی نسبت 3 : 2 میں بانٹتے ہیں۔ زاہد کو کتنے روپے ملیں گے؟"),
     ZAHID,
     T("You know the total profit: 3 + 2 = 5 parts.", "کل منافع معلوم ہے: 3 + 2 = 5 حصے۔"),
     T(f"Right! One part is 1500 ÷ 5 = 300, so Zahid gets 3 × 300 = Rs {ZAHID} and Asif Rs {ASIF}.", f"درست! ایک حصہ 1500 ÷ 5 = 300، اس لیے زاہد کو 3 × 300 = {ZAHID} روپے اور آصف کو {ASIF} روپے۔"),
     T(f"5 parts: 1500 ÷ 5 = 300. Zahid has 3 parts: 3 × 300 = Rs {ZAHID}.", f"5 حصے: 1500 ÷ 5 = 300۔ زاہد کے 3 حصے: 3 × 300 = {ZAHID} روپے۔"),
     common_wrong=[wrong(750, "That is half. Zahid put in more, so he gets 3 of the 5 parts.", "یہ آدھا ہے۔ زاہد نے زیادہ لگایا، اس لیے اسے 5 میں سے 3 حصے ملتے ہیں۔"),
                   wrong(ASIF, f"Rs {ASIF} is Asif's share (2 parts). Zahid has 3 parts.", f"{ASIF} روپے آصف کا حصہ ہے (2 حصے)۔ زاہد کے 3 حصے ہیں۔", "order_swapped")]),
   ratio_question(
     "s7_school",
     T("A school has 240 students; 96 are girls. Write the ratio of girls to boys in its simplest form.", "ایک سکول میں 240 طلبہ ہیں؛ 96 لڑکیاں ہیں۔ لڑکیوں اور لڑکوں کی نسبت سادہ ترین شکل میں لکھیں۔"),
     *S7,
     T(f"First find the boys: 240 − 96. Then simplify 96 : {BOYS_7}.", f"پہلے لڑکے معلوم کریں: 240 − 96۔ پھر 96 : {BOYS_7} کو سادہ کریں۔"),
     T(f"Right! {BOYS_7} boys, and 96 : {BOYS_7} = 2 : 3 (both ÷ 48).", f"درست! {BOYS_7} لڑکے، اور 96 : {BOYS_7} = 2 : 3 (دونوں ÷ 48)۔"),
     T(f"Boys: 240 − 96 = {BOYS_7}. 96 : {BOYS_7}: divide both by 48 to get 2 : 3.", f"لڑکے: 240 − 96 = {BOYS_7}۔ 96 : {BOYS_7}: دونوں کو 48 سے تقسیم کریں تو 2 : 3"),
     common_wrong=[wrong("2:5", "2 : 5 is girls to ALL students. The question asks girls to boys.", "2 : 5 لڑکیوں اور تمام طلبہ کی نسبت ہے۔ سوال لڑکیوں اور لڑکوں کی نسبت پوچھتا ہے۔", "part_for_whole"),
                   wrong("3:2", "That is boys to girls. Girls come first.", "یہ لڑکوں اور لڑکیوں کی نسبت ہے۔ لڑکیاں پہلے ہیں۔", "order_swapped")]),
   number_question(
     "s8_tree",
     T("At the same time of day, a 5 m pole has a 3 m shadow and a tree has a 12 m shadow. How tall is the tree, in m?", "دن کے ایک ہی وقت میں 5 میٹر کے کھمبے کا سایہ 3 میٹر اور ایک درخت کا سایہ 12 میٹر ہے۔ درخت کتنے میٹر اونچا ہے؟"),
     TREE,
     T("Shadow to height is the same: 3 : 5 :: 12 : ?", "سایہ اور اونچائی کی نسبت ایک جیسی ہے: 3 : 5 :: 12 : ?"),
     T(f"Right! 3 × 4 = 12, so the height is 5 × 4 = {TREE} m.", f"درست! 3 × 4 = 12، اس لیے اونچائی 5 × 4 = {TREE} میٹر۔"),
     T(f"3 : 5 :: 12 : ?. The shadow is 4 times longer, so the tree is 5 × 4 = {TREE} m.", f"3 : 5 :: 12 : ?۔ سایہ 4 گنا لمبا ہے، اس لیے درخت 5 × 4 = {TREE} میٹر۔"),
     common_wrong=[wrong(14, "The shadow is 4 times longer, not 9 m longer for the height. Multiply.", "سایہ 4 گنا لمبا ہے؛ اونچائی میں 9 میٹر جمع نہ کریں۔ ضرب دیں۔", "additive_thinking")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("In a class, boys to girls is 3 : 4, and there are 21 boys. Kashif says: \"7 parts, 21 ÷ 7 = 3, so 4 × 3 = 12 girls.\" What went wrong?",
                "ایک جماعت میں لڑکوں اور لڑکیوں کی نسبت 3 : 4 ہے، اور 21 لڑکے ہیں۔ کاشف کہتا ہے: \"7 حصے، 21 ÷ 7 = 3، اس لیے 4 × 3 = 12 لڑکیاں۔\" کیا غلطی ہوئی؟"),
    "options": [
      opt("share", f"21 is the boys (3 parts), not the whole class. One part is 21 ÷ 3 = {ONE_PART_9}, so {GIRLS_9} girls.", f"21 لڑکے ہیں (3 حصے)، پوری جماعت نہیں۔ ایک حصہ 21 ÷ 3 = {ONE_PART_9}، اس لیے {GIRLS_9} لڑکیاں۔", True,
          "Yes! Check: 12 girls would be fewer than 21 boys, but 3 : 4 means more girls.", "جی ہاں! جانچیں: 12 لڑکیاں 21 لڑکوں سے کم ہوں گی، لیکن 3 : 4 کا مطلب زیادہ لڑکیاں ہے۔"),
      opt("nothing", "Nothing. He added the parts and shared.", "کوئی غلطی نہیں۔ اس نے حصے جمع کر کے بانٹا۔", False,
          "Adding the parts is for a total. 21 is only the boys' share.", "حصے جمع کرنا کل کے لیے ہے۔ 21 صرف لڑکوں کا حصہ ہے۔", "share_vs_total"),
      opt("order", "He should use 4 : 3.", "اسے 4 : 3 استعمال کرنا چاہیے۔", False,
          "The order 3 : 4 is right (boys first). The mistake is treating 21 as the total.", "ترتیب 3 : 4 ٹھیک ہے (لڑکے پہلے)۔ غلطی 21 کو کل سمجھنا ہے۔", "order_swapped"),
    ]},
   {"id": "s10_explain_choice", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Can you teach me? When do I add the parts of a ratio, and when don't I?",
                     "کیا آپ مجھے سمجھا سکتے ہیں؟ نسبت کے حصے کب جمع کرتے ہیں، اور کب نہیں؟"),
    "task": T("In your own words: boys to girls is 3 : 4. Why do we divide by 7 when we know the whole class, but by 3 when we know only the boys?",
              "اپنے الفاظ میں بتائیں: لڑکوں اور لڑکیوں کی نسبت 3 : 4 ہے۔ پوری جماعت معلوم ہو تو 7 سے تقسیم کیوں کرتے ہیں، اور صرف لڑکے معلوم ہوں تو 3 سے کیوں؟"),
    "key_idea": "The whole class is all 3 + 4 = 7 parts, so dividing it by 7 gives one part. The boys are only their own 3 parts, so dividing the boys by 3 gives one part. Always divide an amount by the number of parts it is made of.",
    "levels": {
      "got_it": "Says the whole class is 7 parts (3 + 4) while the boys are only 3 parts, so you divide each amount by the number of parts it contains.",
      "partly": "Mentions 7 parts or 3 parts but does not link each amount with its own number of parts.",
      "not_yet": "Says to always divide by 7, gives no reason, or the reasoning is wrong."},
    "keywords": [
      ["part", "حص", "hiss"],
      ["whole", "total", "class", "all", "کل", "پوری", "جماعت", "kul", "poori", "jamat"],
      ["boys", "only", "3", "لڑک", "صرف", "lark", "sirf"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Divide each amount by the number of parts it is made of: the class is 7 parts, the boys are 3.",
                  "بہت خوب سمجھایا! ہر مقدار کو اس کے اپنے حصوں سے تقسیم کریں: جماعت 7 حصے ہے، لڑکے 3۔"),
      "partly": T("Good start! Now say how many parts the whole class is, and how many parts the boys are.", "اچھی شروعات! اب بتائیں کہ پوری جماعت کتنے حصے ہے، اور لڑکے کتنے حصے۔"),
      "not_yet": T("Think: in 3 : 4, how many parts are boys? How many parts are boys and girls together?",
                   "سوچیں: 3 : 4 میں لڑکے کتنے حصے ہیں؟ لڑکے اور لڑکیاں مل کر کتنے حصے ہیں؟")},
    "limit_per_day": 3, "max_attempts": 2},
   {"id": "s11_unit_test", "type": "explain",
    "character": say("encouraging", "Test time! Five questions from the whole Ratio unit. You can do it!", "ٹیسٹ کا وقت! نسبت کے پورے باب سے پانچ سوال۔ آپ کر سکتے ہیں!"),
    "text": T("This short test has one question on each part of the unit: writing a ratio, simplest form, sharing, proportion and the unitary method. Read each one carefully and check that your answer makes sense.",
              "اس چھوٹے ٹیسٹ میں باب کے ہر حصے سے ایک سوال ہے: نسبت لکھنا، سادہ ترین شکل، تقسیم، تناسب اور اکائی کا طریقہ۔ ہر سوال غور سے پڑھیں اور دیکھیں کہ جواب سمجھ میں آتا ہے۔")},
   {"id": "u1_write", "type": "choice", "question_type": "recall", "skill": RATIO_MEANING,
    "prompt": T("Test 1: A team has 7 boys and 9 girls. What is the ratio of girls to boys?", "ٹیسٹ 1: ایک ٹیم میں 7 لڑکے اور 9 لڑکیاں ہیں۔ لڑکیوں اور لڑکوں کی نسبت کیا ہے؟"),
    "options": [
      opt("right", "9 : 7", "9 : 7", True, "Yes! Girls first: 9 : 7.", "جی ہاں! لڑکیاں پہلے: 9 : 7"),
      opt("swapped", "7 : 9", "7 : 9", False, "That is boys to girls. Girls come first.", "یہ لڑکوں اور لڑکیوں کی نسبت ہے۔ لڑکیاں پہلے ہیں۔", "order_swapped"),
      opt("whole", "9 : 16", "9 : 16", False, "16 is the whole team. Compare girls with boys.", "16 پوری ٹیم ہے۔ لڑکیوں کا موازنہ لڑکوں سے کریں۔", "part_for_whole"),
    ]},
   ratio_question(
     "u2_simplest",
     T("Test 2: Write 18 : 24 in its simplest form.", "ٹیسٹ 2: 18 : 24 کو سادہ ترین شکل میں لکھیں۔"),
     *U2,
     T("6 divides both 18 and 24.", "6، 18 اور 24 دونوں کو تقسیم کرتا ہے۔"),
     T("Right! 18 : 24 = 3 : 4.", "درست! 18 : 24 = 3 : 4"),
     T("Divide both by 6: 18 ÷ 6 = 3 and 24 ÷ 6 = 4. So 3 : 4.", "دونوں کو 6 سے تقسیم کریں: 18 ÷ 6 = 3 اور 24 ÷ 6 = 4۔ اس لیے 3 : 4"),
     common_wrong=[wrong("9:12", "9 : 12 is equal, but 3 still divides both. Keep going.", "9 : 12 برابر ہے، لیکن 3 اب بھی دونوں کو تقسیم کرتا ہے۔ آگے بڑھیں۔"),
                   wrong("6:8", "6 : 8 is equal, but 2 still divides both. Keep going.", "6 : 8 برابر ہے، لیکن 2 اب بھی دونوں کو تقسیم کرتا ہے۔ آگے بڑھیں۔")],
     qtype="recall", skill=RATIO_EQUIVALENT),
   number_question(
     "u3_sweets",
     T("Test 3: Share 56 sweets between Ayan and Mahnoor in the ratio 3 : 5. How many does Mahnoor get?", "ٹیسٹ 3: 56 مٹھائیاں ایان اور ماہ نور میں 3 : 5 کی نسبت سے بانٹیں۔ ماہ نور کو کتنی ملیں گی؟"),
     U3[1],
     T("3 + 5 = 8 parts.", "3 + 5 = 8 حصے۔"),
     T(f"Right! One part is 56 ÷ 8 = 7, so Mahnoor gets 5 × 7 = {U3[1]}.", f"درست! ایک حصہ 56 ÷ 8 = 7، اس لیے ماہ نور کو 5 × 7 = {U3[1]}۔"),
     T(f"8 parts: 56 ÷ 8 = 7. Mahnoor has 5 parts: 5 × 7 = {U3[1]}.", f"8 حصے: 56 ÷ 8 = 7۔ ماہ نور کے 5 حصے: 5 × 7 = {U3[1]}"),
     common_wrong=[wrong(28, "That is half each. The ratio is 3 : 5.", "یہ ہر ایک کو آدھا ہے۔ نسبت 3 : 5 ہے۔"),
                   wrong(U3[0], f"{U3[0]} is Ayan's share (3 parts). Mahnoor has 5.", f"{U3[0]} ایان کا حصہ ہے (3 حصے)۔ ماہ نور کے 5 ہیں۔")],
     skill=RATIO_SHARE),
   number_question(
     "u4_proportion",
     T("Test 4: Find the missing term: 6 : 9 :: ? : 15", "ٹیسٹ 4: غائب رکن معلوم کریں: 6 : 9 :: ? : 15"),
     U4,
     T("Extremes = means: 6 × 15 = 9 × ?", "طرفین = وسطین: 6 × 15 = 9 × ?"),
     T(f"Right! 6 × 15 = 90, and 90 ÷ 9 = {U4}. Both ratios are 2 : 3.", f"درست! 6 × 15 = 90، اور 90 ÷ 9 = {U4}۔ دونوں نسبتیں 2 : 3 ہیں۔"),
     T(f"6 × 15 = 90 = 9 × ?, so ? = 90 ÷ 9 = {U4}.", f"6 × 15 = 90 = 9 × ?، اس لیے ? = 90 ÷ 9 = {U4}"),
     common_wrong=[wrong(12, "You added 6 because 9 + 6 = 15. Use extremes = means instead.", "آپ نے 6 جمع کیا کیونکہ 9 + 6 = 15۔ اس کے بجائے طرفین = وسطین استعمال کریں۔", "additive_thinking")],
     skill=RATIO_PROPORTION),
   number_question(
     "u5_apples",
     T("Test 5: 3 kg of apples cost Rs 540. How much do 5 kg cost, in rupees?", "ٹیسٹ 5: 3 کلوگرام سیب 540 روپے کے ہیں۔ 5 کلوگرام کتنے روپے کے ہوں گے؟"),
     U5,
     T("1 kg: 540 ÷ 3.", "1 کلوگرام: 540 ÷ 3"),
     T(f"Right! 1 kg is Rs 180, so 5 kg cost Rs {U5}.", f"درست! 1 کلوگرام 180 روپے، اس لیے 5 کلوگرام {U5} روپے۔"),
     T(f"540 ÷ 3 = 180 for 1 kg. 5 × 180 = Rs {U5}.", f"1 کلوگرام: 540 ÷ 3 = 180۔ 5 × 180 = {U5} روپے۔"),
     common_wrong=[wrong(542, "2 more kg don't cost Rs 2 more. Find 1 kg first.", "2 کلوگرام زیادہ کی قیمت 2 روپے زیادہ نہیں۔ پہلے 1 کلوگرام معلوم کریں۔", "additive_thinking"),
                   wrong(2700, "Rs 540 is for 3 kg. Divide by 3 first.", "540 روپے 3 کلوگرام کے ہیں۔ پہلے 3 سے تقسیم کریں۔")],
     skill=UNITARY),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "You finished the whole Ratio and Proportion unit. Shabash!", "آپ نے نسبت اور تناسب کا پورا باب مکمل کر لیا۔ شاباش!"),
    "text": T("For a ratio story, ask: what do I know, and what do I want? Total known: add the parts and share. One pair known: unitary method or proportion. Comparing: write the ratio in order and simplify. Check that the answer makes sense.",
              "نسبت کی کہانی میں پوچھیں: مجھے کیا معلوم ہے، اور کیا چاہیے؟ کل معلوم: حصے جمع کر کے بانٹیں۔ ایک جوڑا معلوم: اکائی کا طریقہ یا تناسب۔ موازنہ: ترتیب سے نسبت لکھ کر سادہ کریں۔ جانچیں کہ جواب سمجھ میں آتا ہے۔"),
    "points": [T("Divide an amount by the number of parts it is made of.", "مقدار کو اس کے اپنے حصوں کی تعداد سے تقسیم کریں۔"),
               T("Ratios grow by ×, never by +.", "نسبتیں × سے بڑھتی ہیں، کبھی + سے نہیں۔")]},
 ],
 "review_questions": [
   {"id": "r_paint", "type": "apply", "skill": SKILL, "step": number_question(
     "r_paint",
     T("Paint is mixed blue to white in the ratio 2 : 5. Faiza uses 15 tins of white. How many tins of blue does she need?",
       "رنگ نیلا اور سفید 2 : 5 کی نسبت میں ملایا جاتا ہے۔ فائزہ سفید رنگ کے 15 ڈبے استعمال کرتی ہے۔ اسے نیلے رنگ کے کتنے ڈبے چاہییں؟"),
     PAINT_BLUE,
     T("The 15 white tins are 5 parts. How many tins is one part?", "سفید کے 15 ڈبے 5 حصے ہیں۔ ایک حصہ کتنے ڈبے ہے؟"),
     T(f"Right! One part is 15 ÷ 5 = 3, so blue is 2 × 3 = {PAINT_BLUE} tins.", f"درست! ایک حصہ 15 ÷ 5 = 3، اس لیے نیلا 2 × 3 = {PAINT_BLUE} ڈبے۔"),
     T(f"White is 5 parts: 15 ÷ 5 = 3 tins each. Blue is 2 parts: 2 × 3 = {PAINT_BLUE}.", f"سفید 5 حصے: 15 ÷ 5 = 3 ڈبے فی حصہ۔ نیلا 2 حصے: 2 × 3 = {PAINT_BLUE}"),
     common_wrong=[wrong(12, "Taking 3 away keeps the gap, not the ratio. Find one part: 15 ÷ 5.", "3 کم کرنے سے فرق رہتا ہے، نسبت نہیں۔ ایک حصہ معلوم کریں: 15 ÷ 5", "additive_thinking"),
                   wrong(30, "15 is only the white paint (5 parts), so blue is less than white.", "15 صرف سفید رنگ ہے (5 حصے)، اس لیے نیلا سفید سے کم ہوگا۔", "share_vs_total")],
     qtype=None)},
   {"id": "r_proportion", "type": "apply", "skill": SKILL, "step": number_question(
     "r_proportion",
     T("A map shows 2 cm for every 5 km. Two villages are 14 cm apart on the map. How many km apart are they?", "ایک نقشے پر ہر 5 کلومیٹر کے لیے 2 سینٹی میٹر ہیں۔ نقشے پر دو گاؤں 14 سینٹی میٹر دور ہیں۔ وہ کتنے کلومیٹر دور ہیں؟"),
     MAP_KM,
     T("2 : 5 :: 14 : ?. What do you multiply 2 by to get 14?", "2 : 5 :: 14 : ?۔ 2 کو کس عدد سے ضرب دیں تو 14 بنتا ہے؟"),
     T(f"Right! 2 × 7 = 14, so 5 × 7 = {MAP_KM} km.", f"درست! 2 × 7 = 14، اس لیے 5 × 7 = {MAP_KM} کلومیٹر۔"),
     T(f"2 : 5 :: 14 : ?. 2 × 7 = 14, so 5 × 7 = {MAP_KM} km.", f"2 : 5 :: 14 : ?۔ 2 × 7 = 14، اس لیے 5 × 7 = {MAP_KM} کلومیٹر۔"),
     common_wrong=[wrong(17, "You added 12 because 2 + 12 = 14. Multiply instead: 2 × 7 = 14.", "آپ نے 12 جمع کیا کیونکہ 2 + 12 = 14۔ اس کے بجائے ضرب دیں: 2 × 7 = 14", "additive_thinking")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Ratio and Proportion unit. No textbook text or exercises were used. Prices and amounts are round numbers for the sums.",
   "Unit number to be confirmed against the PCTB Grade 6 book: the files are named g6-maths-06. Fix the names and curriculum_refs if the unit differs.",
   "Urdu terms to check against the Punjab textbook: نسبت کے عملی سوالات (ratio word problems), منافع (profit).",
   "The lesson teaches choosing the method (s3, s4) before solving: total known means share; one pair known means unitary method or proportion; comparing means write and simplify.",
   "s11 to u5 are a short unit test, one question per earlier lesson. Each u-step is tagged with that lesson's skill (meaning, equivalent, share, proportion, unitary_method), so it counts as practice for that skill rather than for word problems.",
   "The numbers were worked out in content/sources/g6-maths-06/ratio_word_problems.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
assert 12 + (10 - 4) == 18 and 540 + 2 == 542 and 9 + 6 == 15
write(lesson)
