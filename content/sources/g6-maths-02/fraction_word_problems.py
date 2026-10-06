from common import (F, T, opt, say, wrong, frac, mixed, unsimplified, fraction_question, write,
                    REF, REVIEW, EQUIVALENT, ADD_UNLIKE, MIXED, MULTIPLY, DIVIDE, WORD_PROBLEMS)

SKILL = WORD_PROBLEMS


def number_question(id, prompt, answer, hint, good, bad, *, common_wrong=(), qtype="apply", skill=None):
    """A step whose answer is a whole number (or an exact decimal)."""
    step = {"id": id, "type": "number"}
    if qtype:
        step["question_type"] = qtype
    if skill:
        step["skill"] = skill
    step.update({"prompt": prompt, "answer": answer, "checker": "numeric",
                 "hint": hint, "feedback_correct": good, "feedback_wrong": bad})
    if common_wrong:
        step["common_wrong"] = list(common_wrong)
    return step


def num(x: F):
    """A whole number as int, an exact decimal as float (for number steps)."""
    x = F(x)
    if x.denominator == 1:
        return x.numerator
    assert F(float(x)) == x, x  # only exact decimals
    return float(x)


def parts_added(whole: int, a: F, b: F) -> str:
    """The mistake: 1 1/2 + 3/4 -> 1 4/6 (adds the tops and the bottoms of the parts)."""
    return f"{whole} {a.numerator + b.numerator}/{a.denominator + b.denominator}"


# s2: the foundation: 3/4 × 8 (and the wrong operations)
assert F(3, 4) * 8 == 6 and unsimplified(3 * 8, 4 * 8) == "24/32" and F(24, 32) == F(3, 4)
assert 8 / F(3, 4) == F(32, 3) and mixed(F(32, 3)) == "10 2/3"

# s4, s5: the tailor's 6 metres, 1 1/2 metres for each kameez
CLOTH, KAMEEZ = 6, 1 + F(1, 2)
SUITS = CLOTH / KAMEEZ
assert SUITS == 4 and CLOTH * F(2, 3) == SUITS
assert CLOTH * KAMEEZ == 9

# s6: atta bought on two days
MONDAY, FRIDAY = 1 + F(1, 2), F(3, 4)
ATTA = MONDAY + FRIDAY
assert ATTA == F(9, 4) and mixed(ATTA) == "2 1/4"
assert parts_added(1, F(1, 2), F(3, 4)) == "1 4/6"
assert MONDAY - FRIDAY == F(3, 4)

# s7: petrol in the motorbike
TANK, USED = 4 + F(1, 4), 1 + F(1, 2)
PETROL = TANK - USED
assert PETROL == F(11, 4) and mixed(PETROL) == "2 3/4"
assert mixed(TANK + USED) == "5 3/4"
assert 4 - 1 + (F(1, 2) - F(1, 4)) == 3 + F(1, 4)  # the parts subtracted the wrong way round

# s8: the cricket match: 3/5 of 20 overs bowled before the rain
OVERS = 20
BOWLED = F(3, 5) * OVERS
LEFT = OVERS - BOWLED
assert BOWLED == 12 and LEFT == 8

# s9, s10: the atta bag
BAG, PER_DAY = 5, F(1, 2)
DAYS = BAG / PER_DAY
assert DAYS == 10 and BAG * PER_DAY == F(5, 2) and mixed(BAG * PER_DAY) == "2 1/2"

# u1-u5: the unit test
assert F(12, 18) == F(2, 3) and F(6, 9) == F(2, 3) and F(3, 2) != F(2, 3)
WALK = F(2, 3) + F(1, 4)
assert WALK == F(11, 12) and unsimplified(2 + 1, 3 + 4) == "3/7"
SUGAR = 13 * F(1, 4)
assert SUGAR == F(13, 4) and mixed(SUGAR) == "3 1/4" and divmod(13, 4) == (3, 1)
BOX, BARFI = 24, F(5, 8)
assert BARFI * BOX == 15 and BOX / BARFI == F(192, 5) and mixed(BOX / BARFI) == "38 2/5"
ROTIS, EACH = 6, F(3, 4)
CHILDREN = ROTIS / EACH
assert CHILDREN == 8 and ROTIS * EACH == F(9, 2) and num(ROTIS * EACH) == 4.5

# Question bank and review
assert F(2, 3) * 15 == 10
RICE, PACK = 9, F(3, 4)
assert RICE / PACK == 12 and num(RICE * PACK) == 6.75
assert F(3, 4) - F(1, 2) == F(1, 4) and F(3, 4) + F(1, 2) == F(5, 4) and mixed(F(5, 4)) == "1 1/4"
MILK = 4 * (1 + F(1, 2))
assert MILK == 6 and num(4 + F(1, 2)) == 4.5
LAWN = 5 - (2 + F(3, 4))
assert LAWN == F(9, 4) and mixed(LAWN) == "2 1/4" and mixed(5 + 2 + F(3, 4)) == "7 3/4"

lesson = {
 "id": "g6-maths-02-fraction-word-problems",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Solve real-life word problems involving addition, subtraction, multiplication and division of fractions and mixed numbers, choosing the operation from the story.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Fraction word problems", "کسور کے عبارتی سوالات"),
 "estimated_minutes": 20,
 "prerequisites": [{"skill": EQUIVALENT}, {"skill": ADD_UNLIKE}, {"skill": MIXED}, {"skill": MULTIPLY}, {"skill": DIVIDE}],
 "misconceptions": [
   {"id": "add_tops_and_bottoms", "description": "Adds the numerators and adds the denominators (1/2 + 3/4 = 4/6)."},
   {"id": "wrong_add_subtract", "description": "Adds when the story asks how much is left, or subtracts when it asks for the total."},
   {"id": "divide_instead_of_multiply", "description": "Divides when the story asks for a fraction of an amount (5/8 of 24 worked out as 24 ÷ 5/8)."},
   {"id": "multiply_instead_of_divide", "description": "Multiplies when the story asks how many equal parts fit (6 ÷ 1 1/2 worked out as 6 × 1 1/2)."},
   {"id": "one_step_only", "description": "Stops after the first step of a two-step problem (finds the overs bowled, not the overs left)."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_of_means", "type": "recall", "step": {
     "id": "qb_of_means", "type": "choice",
     "prompt": T("Zara ate 2/3 of 15 laddoos. Which operation finds how many she ate?", "زارا نے 15 لڈوؤں کا 2/3 کھایا۔ اس نے کتنے کھائے، یہ کس عمل سے معلوم ہو گا؟"),
     "options": [
       opt("multiply", "Multiply: 2/3 × 15", "ضرب: 2/3 × 15", True,
           "Yes! 'A fraction of' means multiply: 2/3 × 15 = 10 laddoos.", "جی ہاں! 'کا کسری حصہ' مطلب ضرب: 2/3 × 15 = 10 لڈو۔"),
       opt("divide", "Divide: 15 ÷ 2/3", "تقسیم: 15 ÷ 2/3", False,
           "15 ÷ 2/3 = 22 1/2, more than all 15 laddoos! She ate a part of them, so multiply.", "15 ÷ 2/3 = 22 1/2، یہ تو سارے 15 لڈوؤں سے بھی زیادہ ہے! اس نے ان کا ایک حصہ کھایا، اس لیے ضرب دیں۔", "divide_instead_of_multiply"),
       opt("subtract", "Subtract: 15 − 2/3", "تفریق: 15 − 2/3", False,
           "That takes away 2/3 of one laddoo. The story asks for 2/3 of all 15, so multiply.", "اس سے ایک لڈو کا 2/3 کم ہوتا ہے۔ سوال تو سارے 15 کے 2/3 کا ہے، اس لیے ضرب دیں۔"),
     ]}},
   {"id": "qb_rice_bags", "type": "apply", "step": number_question(
     "qb_rice_bags",
     T(f"A shopkeeper packs {RICE} kg of rice into bags of {frac(PACK)} kg each. How many bags does he fill?",
       f"ایک دکاندار {RICE} کلوگرام چاول {frac(PACK)} کلوگرام کے تھیلوں میں بھرتا ہے۔ وہ کتنے تھیلے بھرے گا؟"),
     num(RICE / PACK),
     T(f"How many {frac(PACK)} kg bags fit into {RICE} kg? Divide: {RICE} ÷ {frac(PACK)} = {RICE} × 4/3.", f"{RICE} کلوگرام میں {frac(PACK)} کلوگرام کے کتنے تھیلے آئیں گے؟ تقسیم کریں: {RICE} ÷ {frac(PACK)} = {RICE} × 4/3"),
     T(f"Right! {RICE} ÷ 3/4 = {RICE} × 4/3 = 12 bags.", f"درست! {RICE} ÷ 3/4 = {RICE} × 4/3 = 12 تھیلے۔"),
     T(f"We ask how many 3/4 kg bags fit, so divide: {RICE} ÷ 3/4 = {RICE} × 4/3 = 36/3 = 12 bags.", f"سوال یہ ہے کہ 3/4 کلوگرام کے کتنے تھیلے آئیں گے، اس لیے تقسیم کریں: {RICE} ÷ 3/4 = {RICE} × 4/3 = 36/3 = 12 تھیلے۔"),
     common_wrong=[wrong(num(RICE * PACK), "You multiplied. Each bag holds less than 1 kg, so there must be more than 9 bags. Divide.",
                         "آپ نے ضرب دی۔ ہر تھیلے میں 1 کلوگرام سے کم آتا ہے، اس لیے تھیلے 9 سے زیادہ ہوں گے۔ تقسیم کریں۔", "multiply_instead_of_divide")],
     qtype=None)},
   {"id": "qb_find_error_ribbon", "type": "find_error", "step": {
     "id": "qb_find_error_ribbon", "type": "choice",
     "prompt": T("Ayesha had 3/4 m of ribbon and used 1/2 m. Hamza says she has 3/4 + 1/2 = 1 1/4 m left. What went wrong?",
                 "عائشہ کے پاس 3/4 میٹر فیتہ تھا اور اس نے 1/2 میٹر استعمال کیا۔ حمزہ کہتا ہے کہ اس کے پاس 3/4 + 1/2 = 1 1/4 میٹر بچا۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("subtract", "'Left' means take away: 3/4 − 1/2 = 1/4 m.", "'بچا' کا مطلب ہے کم کریں: 3/4 − 1/2 = 1/4 میٹر", True,
           "Right! She used some ribbon, so she has less than 3/4 m, not more.", "درست! اس نے کچھ فیتہ استعمال کیا، اس لیے اس کے پاس 3/4 میٹر سے کم بچا، زیادہ نہیں۔"),
       opt("nothing", "Nothing, 1 1/4 m is right.", "کوئی غلطی نہیں، 1 1/4 میٹر درست ہے۔", False,
           "Can she have more ribbon after using some? 1 1/4 m is more than she started with.", "کیا کچھ استعمال کرنے کے بعد فیتہ زیادہ ہو سکتا ہے؟ 1 1/4 میٹر تو شروع سے بھی زیادہ ہے۔", "wrong_add_subtract"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_choose_operation", "front": T("How do you choose the operation in a fraction story?", "کسور کے عبارتی سوال میں عمل کیسے چنتے ہیں؟"),
    "back": T("Put together: add. How much is left or how much more: subtract. A fraction of an amount, or the same amount many times: multiply. How many parts fit: divide.",
              "اکٹھا کرنا ہو: جمع۔ کتنا بچا یا کتنا زیادہ: تفریق۔ کسی مقدار کا کسری حصہ، یا ایک ہی مقدار کئی بار: ضرب۔ کتنے حصے پورے آتے ہیں: تقسیم۔")},
   {"id": "f_does_it_make_sense", "front": T("How can you check a word problem answer?", "عبارتی سوال کا جواب کیسے جانچتے ہیں؟"),
    "back": T("Ask: should the answer be more or less than the starting amount? 5/8 of 24 barfi must be less than 24.", "پوچھیں: کیا جواب شروع والی مقدار سے زیادہ ہونا چاہیے یا کم؟ 24 برفیوں کا 5/8 تو 24 سے کم ہی ہو گا۔")},
 ],
 "home_tasks": [{"id": "h_kitchen_stories", "text": T(
   "Ask someone at home about things measured in fractions: atta in kg, milk in litres or cloth in metres. Make up one story for each operation (add, subtract, multiply, divide). Solve them and check that each answer makes sense.",
   "گھر میں کسی سے ایسی چیزوں کے بارے میں پوچھیں جو کسور میں ناپی جاتی ہیں: آٹا کلوگرام میں، دودھ لیٹر میں یا کپڑا میٹر میں۔ ہر عمل (جمع، تفریق، ضرب، تقسیم) کے لیے ایک کہانی بنائیں۔ انہیں حل کریں اور دیکھیں کہ ہر جواب سمجھ میں آتا ہے۔")}],
 "glossary": [T("Word problem", "عبارتی سوال"), T("Operation", "عمل"), T("Addition", "جمع"), T("Subtraction", "تفریق"),
              T("Multiplication", "ضرب"), T("Division", "تقسیم"), T("Reciprocal", "معکوس"), T("Mixed number", "مخلوط عدد"),
              T("Kilogram", "کلوگرام"), T("Metre", "میٹر"), T("Litre", "لیٹر")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Atta, cloth, petrol, rotis: fractions are everywhere at home! But how do I know whether to add, subtract, multiply or divide?",
                     "آٹا، کپڑا، پیٹرول، روٹیاں: گھر میں ہر طرف کسور ہیں! لیکن مجھے کیسے پتا چلے کہ جمع کروں، تفریق، ضرب یا تقسیم؟"),
    "text": T("In this lesson you read a story, choose the operation, and solve it. At the end there is a short test on the whole Fractions unit. First, a quick check.",
              "اس سبق میں آپ کہانی پڑھیں گے، عمل چنیں گے اور سوال حل کریں گے۔ آخر میں کسور کے پورے باب کا ایک چھوٹا سا ٹیسٹ ہے۔ پہلے ایک چھوٹا سا سوال۔")},
   {"id": "s2_foundation", "type": "choice", "question_type": "recall", "skill": MULTIPLY,
    "prompt": T("What is 3/4 of 8?", "8 کا 3/4 کتنا ہے؟"),
    "options": [
      opt("six", "6", "6", True,
          "Yes! 3/4 × 8 = 24/4 = 6. Or: 8 ÷ 4 = 2, and 3 × 2 = 6.", "جی ہاں! 3/4 × 8 = 24/4 = 6۔ یا: 8 ÷ 4 = 2، اور 3 × 2 = 6"),
      opt("ten_two_thirds", "10 2/3", "10 2/3", False,
          "That is 8 ÷ 3/4, more than 8! 3/4 of 8 is a part of 8, so it is less than 8.", "یہ تو 8 ÷ 3/4 ہے، جو 8 سے زیادہ ہے! 8 کا 3/4 اس کا ایک حصہ ہے، اس لیے 8 سے کم ہو گا۔", "divide_instead_of_multiply"),
      opt("same", "24/32", "24/32", False,
          "24/32 is still 3/4: the top and the bottom were both multiplied by 8. Multiply only the top: 24/4 = 6.", "24/32 تو اب بھی 3/4 ہی ہے: اوپر اور نیچے دونوں کو 8 سے ضرب دی گئی۔ صرف اوپر والے کو ضرب دیں: 24/4 = 6"),
    ]},
   {"id": "s3_four_questions", "type": "explain",
    "character": say("talking", "Picture the story first, then choose!", "پہلے کہانی کو ذہن میں دیکھیں، پھر عمل چنیں!"),
    "text": T("Ask what the story wants. Putting amounts together? Add. How much is left, or how much more? Subtract. A fraction of an amount, or the same amount many times? Multiply ('of' means ×). How many equal parts fit into an amount? Divide. Then check: should the answer be more or less than what you started with?",
              "دیکھیں کہانی کیا پوچھ رہی ہے۔ مقداریں اکٹھی کرنی ہیں؟ جمع کریں۔ کتنا بچا، یا کتنا زیادہ؟ تفریق کریں۔ کسی مقدار کا کسری حصہ، یا ایک ہی مقدار کئی بار؟ ضرب دیں ('کا' مطلب ×)۔ ایک مقدار میں کتنے برابر حصے آتے ہیں؟ تقسیم کریں۔ پھر جانچیں: جواب شروع والی مقدار سے زیادہ ہونا چاہیے یا کم؟")},
   {"id": "s4_tailor_choose", "type": "choice", "question_type": "apply",
    "prompt": T(f"A tailor has {CLOTH} metres of cloth. Each kameez needs {mixed(KAMEEZ)} metres. Which sum tells how many kameez he can make?",
                f"ایک درزی کے پاس {CLOTH} میٹر کپڑا ہے۔ ہر قمیض کے لیے {mixed(KAMEEZ)} میٹر چاہیے۔ کون سا سوال بتائے گا کہ وہ کتنی قمیضیں بنا سکتا ہے؟"),
    "options": [
      opt("divide", f"{CLOTH} ÷ {mixed(KAMEEZ)}", f"{CLOTH} ÷ {mixed(KAMEEZ)}", True,
          f"Yes! We ask how many pieces of {mixed(KAMEEZ)} m fit into {CLOTH} m, so we divide.", f"جی ہاں! سوال یہ ہے کہ {CLOTH} میٹر میں {mixed(KAMEEZ)} میٹر کے کتنے ٹکڑے آتے ہیں، اس لیے تقسیم کریں گے۔"),
      opt("multiply", f"{CLOTH} × {mixed(KAMEEZ)}", f"{CLOTH} × {mixed(KAMEEZ)}", False,
          f"{CLOTH} × {mixed(KAMEEZ)} = {CLOTH * KAMEEZ} metres: more cloth than he has! We want how many pieces fit.", f"{CLOTH} × {mixed(KAMEEZ)} = {CLOTH * KAMEEZ} میٹر: یہ تو اس کے کپڑے سے بھی زیادہ ہے! ہمیں یہ جاننا ہے کہ کتنے ٹکڑے آتے ہیں۔", "multiply_instead_of_divide"),
      opt("subtract", f"{CLOTH} − {mixed(KAMEEZ)}", f"{CLOTH} − {mixed(KAMEEZ)}", False,
          "That is the cloth left after one kameez. We want to know how many kameez in all.", "یہ ایک قمیض کے بعد بچا کپڑا ہے۔ ہمیں یہ جاننا ہے کہ کل کتنی قمیضیں بنیں گی۔", "wrong_add_subtract"),
    ]},
   number_question(
     "s5_tailor_solve",
     T(f"Now work it out: {CLOTH} ÷ {mixed(KAMEEZ)}. How many kameez can the tailor make?", f"اب حل کریں: {CLOTH} ÷ {mixed(KAMEEZ)}۔ درزی کتنی قمیضیں بنا سکتا ہے؟"),
     num(SUITS),
     T(f"{mixed(KAMEEZ)} = {frac(KAMEEZ)}. Dividing by {frac(KAMEEZ)} is the same as multiplying by its reciprocal, 2/3.", f"{mixed(KAMEEZ)} = {frac(KAMEEZ)}۔ {frac(KAMEEZ)} سے تقسیم کرنا اس کے معکوس 2/3 سے ضرب دینے جیسا ہے۔"),
     T(f"Right! {CLOTH} ÷ {frac(KAMEEZ)} = {CLOTH} × 2/3 = {SUITS} kameez.", f"درست! {CLOTH} ÷ {frac(KAMEEZ)} = {CLOTH} × 2/3 = {SUITS} قمیضیں۔"),
     T(f"{mixed(KAMEEZ)} = {frac(KAMEEZ)}, so {CLOTH} ÷ {frac(KAMEEZ)} = {CLOTH} × 2/3 = 12/3 = {SUITS}. Check: {SUITS} × {mixed(KAMEEZ)} = {CLOTH} metres.",
       f"{mixed(KAMEEZ)} = {frac(KAMEEZ)}، اس لیے {CLOTH} ÷ {frac(KAMEEZ)} = {CLOTH} × 2/3 = 12/3 = {SUITS}۔ جانچ: {SUITS} × {mixed(KAMEEZ)} = {CLOTH} میٹر۔"),
     common_wrong=[wrong(num(CLOTH * KAMEEZ), f"You multiplied. Each kameez needs more than 1 metre, so he can make fewer than {CLOTH}. Divide.",
                         f"آپ نے ضرب دی۔ ہر قمیض کو 1 میٹر سے زیادہ کپڑا چاہیے، اس لیے {CLOTH} سے کم قمیضیں بنیں گی۔ تقسیم کریں۔", "multiply_instead_of_divide")]),
   fraction_question(
     "s6_atta",
     T(f"Ammi bought {mixed(MONDAY)} kg of atta on Monday and {frac(FRIDAY)} kg on Friday. How much atta did she buy in all? Write a mixed number.",
       f"امی نے پیر کو {mixed(MONDAY)} کلوگرام آٹا خریدا اور جمعہ کو {frac(FRIDAY)} کلوگرام۔ انہوں نے کل کتنا آٹا خریدا؟ مخلوط عدد لکھیں۔"),
     mixed(ATTA),
     T("'In all' means put together: add. 1 1/2 = 1 2/4, so add the quarters.", "'کل' کا مطلب ہے اکٹھا کریں: جمع۔ 1 1/2 = 1 2/4، اب چوتھائیاں جمع کریں۔"),
     T(f"Right! 1 2/4 + 3/4 = 1 5/4 = {mixed(ATTA)} kg.", f"درست! 1 2/4 + 3/4 = 1 5/4 = {mixed(ATTA)} کلوگرام۔"),
     T(f"Add: 1 1/2 = 1 2/4. 1 2/4 + 3/4 = 1 5/4, and 5/4 = 1 1/4, so {mixed(ATTA)} kg.", f"جمع کریں: 1 1/2 = 1 2/4۔ 1 2/4 + 3/4 = 1 5/4، اور 5/4 = 1 1/4، اس لیے {mixed(ATTA)} کلوگرام۔"),
     common_wrong=[
       wrong(parts_added(1, F(1, 2), F(3, 4)), "You added the tops and the bottoms of 1/2 and 3/4. Make them quarters first: 1/2 = 2/4.",
             "آپ نے 1/2 اور 3/4 کے اوپر اور نیچے والے جمع کر دیے۔ پہلے چوتھائیاں بنائیں: 1/2 = 2/4", "add_tops_and_bottoms"),
       wrong(mixed(MONDAY - FRIDAY), "You subtracted. She bought atta on both days, so the total is more than 1 1/2 kg. Add.",
             "آپ نے تفریق کی۔ انہوں نے دونوں دن آٹا خریدا، اس لیے کل 1 1/2 کلوگرام سے زیادہ ہو گا۔ جمع کریں۔", "wrong_add_subtract"),
       wrong(frac(ATTA), "The right amount, but please write it as a mixed number: 9 ÷ 4 = ? remainder ?",
             "مقدار درست ہے، لیکن اسے مخلوط عدد کی شکل میں لکھیں: 9 ÷ 4 = ? باقی ?"),
     ]),
   fraction_question(
     "s7_petrol",
     T(f"Abbu's motorbike had {mixed(TANK)} litres of petrol. He used {mixed(USED)} litres going to the bazaar. How much petrol is left? Write a mixed number.",
       f"ابو کی موٹر سائیکل میں {mixed(TANK)} لیٹر پیٹرول تھا۔ بازار جانے میں {mixed(USED)} لیٹر خرچ ہوا۔ کتنا پیٹرول بچا؟ مخلوط عدد لکھیں۔"),
     mixed(PETROL),
     T(f"'Left' means take away. Change both to quarters: {mixed(TANK)} = {frac(TANK)} and {mixed(USED)} = {frac(USED)}.", f"'بچا' کا مطلب ہے کم کریں۔ دونوں کو چوتھائیوں میں بدلیں: {mixed(TANK)} = {frac(TANK)} اور {mixed(USED)} = {frac(USED)}"),
     T(f"Right! 17/4 − 6/4 = 11/4 = {mixed(PETROL)} litres.", f"درست! 17/4 − 6/4 = 11/4 = {mixed(PETROL)} لیٹر۔"),
     T(f"{mixed(TANK)} = 17/4 and {mixed(USED)} = 6/4. 17/4 − 6/4 = 11/4, and 11 ÷ 4 = 2 remainder 3: {mixed(PETROL)} litres.",
       f"{mixed(TANK)} = 17/4 اور {mixed(USED)} = 6/4۔ 17/4 − 6/4 = 11/4، اور 11 ÷ 4 = 2 باقی 3: یعنی {mixed(PETROL)} لیٹر۔"),
     common_wrong=[
       wrong(mixed(TANK + USED), "You added. He used some petrol, so less is left, not more. Subtract.",
             "آپ نے جمع کیا۔ پیٹرول خرچ ہوا، اس لیے کم بچا، زیادہ نہیں۔ تفریق کریں۔", "wrong_add_subtract"),
       wrong("3 1/4", "You took 1/4 from 1/2 the wrong way round. 1/4 − 1/2 can't be done, so change everything to quarters: 17/4 − 6/4.",
             "آپ نے 1/2 میں سے 1/4 الٹا گھٹا دیا۔ 1/4 − 1/2 نہیں ہو سکتا، اس لیے سب کو چوتھائیوں میں بدلیں: 17/4 − 6/4"),
       wrong(frac(PETROL), "The right amount, but please write it as a mixed number: 11 ÷ 4 = ? remainder ?",
             "مقدار درست ہے، لیکن اسے مخلوط عدد کی شکل میں لکھیں: 11 ÷ 4 = ? باقی ?"),
     ]),
   number_question(
     "s8_cricket",
     T(f"A T20 innings has {OVERS} overs. Rain stopped the match after 3/5 of the overs were bowled. How many overs were left?",
       f"ٹی ٹوئنٹی کی ایک اننگز میں {OVERS} اوور ہوتے ہیں۔ 3/5 اوور ہونے کے بعد بارش نے میچ روک دیا۔ کتنے اوور باقی تھے؟"),
     num(LEFT),
     T(f"Two steps: first 3/5 of {OVERS} (multiply), then take that away from {OVERS}.", f"دو مرحلے: پہلے {OVERS} کا 3/5 نکالیں (ضرب)، پھر اسے {OVERS} میں سے کم کریں۔"),
     T(f"Right! 3/5 × {OVERS} = {BOWLED} overs bowled, and {OVERS} − {BOWLED} = {LEFT} overs left.", f"درست! 3/5 × {OVERS} = {BOWLED} اوور ہوئے، اور {OVERS} − {BOWLED} = {LEFT} اوور باقی تھے۔"),
     T(f"{OVERS} ÷ 5 = 4, so 3/5 of {OVERS} = 3 × 4 = {BOWLED} overs bowled. Left: {OVERS} − {BOWLED} = {LEFT} overs.", f"{OVERS} ÷ 5 = 4، اس لیے {OVERS} کا 3/5 = 3 × 4 = {BOWLED} اوور ہوئے۔ باقی: {OVERS} − {BOWLED} = {LEFT} اوور۔"),
     common_wrong=[wrong(num(BOWLED), f"{BOWLED} overs were bowled. The question asks how many were left: {OVERS} − {BOWLED}.",
                         f"{BOWLED} اوور تو ہو چکے تھے۔ سوال یہ ہے کہ کتنے باقی تھے: {OVERS} − {BOWLED}", "one_step_only")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T(f"Ammi has a {BAG} kg bag of atta and uses {frac(PER_DAY)} kg every day. How many days will it last? Bilal wrote {BAG} × {frac(PER_DAY)} = {mixed(BAG * PER_DAY)} days. What went wrong?",
                f"امی کے پاس آٹے کا {BAG} کلوگرام کا تھیلا ہے اور وہ ہر روز {frac(PER_DAY)} کلوگرام استعمال کرتی ہیں۔ تھیلا کتنے دن چلے گا؟ بلال نے لکھا {BAG} × {frac(PER_DAY)} = {mixed(BAG * PER_DAY)} دن۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("divide", f"He should divide: how many {frac(PER_DAY)} kg fit into {BAG} kg? {BAG} ÷ {frac(PER_DAY)} = {DAYS} days.", f"اسے تقسیم کرنی چاہیے تھی: {BAG} کلوگرام میں {frac(PER_DAY)} کلوگرام کتنی بار آتا ہے؟ {BAG} ÷ {frac(PER_DAY)} = {DAYS} دن۔", True,
          f"Yes! Each day uses only half a kg, so {BAG} kg must last more than {BAG} days: {BAG} × 2 = {DAYS}.", f"جی ہاں! ہر روز صرف آدھا کلوگرام لگتا ہے، اس لیے {BAG} کلوگرام {BAG} دن سے زیادہ چلے گا: {BAG} × 2 = {DAYS}"),
      opt("nothing", "Nothing, the answer is right.", "کوئی غلطی نہیں، جواب درست ہے۔", False,
          f"Does it make sense? If she used a whole kg a day, the bag would last {BAG} days. She uses less, so it lasts longer.", f"کیا یہ سمجھ میں آتا ہے؟ اگر وہ روز پورا کلوگرام استعمال کرتیں تو تھیلا {BAG} دن چلتا۔ وہ اس سے کم استعمال کرتی ہیں، اس لیے زیادہ دن چلے گا۔", "multiply_instead_of_divide"),
      opt("subtract", f"He should subtract: {BAG} − {frac(PER_DAY)} = {mixed(BAG - PER_DAY)} days.", f"اسے تفریق کرنی چاہیے تھی: {BAG} − {frac(PER_DAY)} = {mixed(BAG - PER_DAY)} دن۔", False,
          "That is the atta left after one day, not the number of days.", "یہ تو ایک دن کے بعد بچا آٹا ہے، دنوں کی تعداد نہیں۔", "wrong_add_subtract"),
    ]},
   {"id": "s10_explain_choice", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Can you teach me? How did you know to divide in the atta story, and not multiply?",
                     "کیا آپ مجھے سمجھا سکتے ہیں؟ آٹے والی کہانی میں آپ کو کیسے پتا چلا کہ تقسیم کرنی ہے، ضرب نہیں؟"),
    "task": T(f"In your own words: how did you choose the operation for the atta story ({BAG} kg, {frac(PER_DAY)} kg a day)? How can you check that your answer makes sense?",
              f"اپنے الفاظ میں بتائیں: آٹے والی کہانی ({BAG} کلوگرام، روز {frac(PER_DAY)} کلوگرام) میں آپ نے عمل کیسے چنا؟ آپ کیسے جانچ سکتے ہیں کہ جواب سمجھ میں آتا ہے؟"),
    "key_idea": f"The story asks how many {frac(PER_DAY)} kg portions fit into {BAG} kg, so we divide: {BAG} ÷ {frac(PER_DAY)} = {DAYS} days. Check: each day uses less than 1 kg, so the bag lasts more than {BAG} days ({DAYS} × {frac(PER_DAY)} = {BAG}).",
    "levels": {
      "got_it": f"Says the question is how many half-kgs fit into {BAG} kg (or how many days), so divide, gets {DAYS}, and/or checks that the answer should be more than {BAG} because less than 1 kg is used each day.",
      "partly": f"Says divide or gives {DAYS}, but does not say why (how many fit) or how to check the answer.",
      "not_yet": "Chooses multiply or subtract, gives no reason, or the reasoning is wrong."},
    "keywords": [
      ["how many", "fit", "کتنے", "کتنی", "kitne", "kitni"],
      ["divide", "÷", "تقسیم", "taqseem", "taqsim"],
      [str(DAYS), "ten", "دس", "more than", "زیادہ", "zyada", "ziada"]],
    "fallback_feedback": {
      "got_it": T(f"Well explained! We ask how many {frac(PER_DAY)} kg fit into {BAG} kg, so we divide: {DAYS} days. Less than 1 kg a day means more than {BAG} days.",
                  f"بہت خوب سمجھایا! سوال یہ ہے کہ {BAG} کلوگرام میں {frac(PER_DAY)} کلوگرام کتنی بار آتا ہے، اس لیے تقسیم: {DAYS} دن۔ روز 1 کلوگرام سے کم، اس لیے {BAG} دن سے زیادہ۔"),
      "partly": T(f"Good start! Now say why you divide, and check: should the bag last more or fewer than {BAG} days?",
                  f"اچھی شروعات! اب بتائیں کہ تقسیم کیوں کی، اور جانچیں: تھیلا {BAG} دن سے زیادہ چلے گا یا کم؟"),
      "not_yet": T(f"Think: each day Ammi takes half a kg from the bag. How many halves are there in {BAG} kg?",
                   f"سوچیں: امی ہر روز تھیلے سے آدھا کلوگرام نکالتی ہیں۔ {BAG} کلوگرام میں کتنے آدھے ہیں؟")},
    "limit_per_day": 3, "max_attempts": 2},
   {"id": "s11_unit_test", "type": "explain",
    "character": say("encouraging", "Test time! Five questions from the whole Fractions unit. You can do it!", "ٹیسٹ کا وقت! کسور کے پورے باب سے پانچ سوال۔ آپ کر سکتے ہیں!"),
    "text": T("This short test has one question on each part of the unit: equivalent fractions, adding, mixed numbers, multiplying and dividing. Read each one carefully and check that your answer makes sense.",
              "اس چھوٹے ٹیسٹ میں باب کے ہر حصے سے ایک سوال ہے: مساوی کسور، جمع، مخلوط اعداد، ضرب اور تقسیم۔ ہر سوال غور سے پڑھیں اور دیکھیں کہ جواب سمجھ میں آتا ہے۔")},
   {"id": "u1_simplest", "type": "choice", "question_type": "recall", "skill": EQUIVALENT,
    "prompt": T("Test 1: What is 12/18 in its simplest form?", "ٹیسٹ 1: 12/18 کی سادہ ترین شکل کیا ہے؟"),
    "options": [
      opt("two_thirds", "2/3", "2/3", True,
          "Yes! 6 divides 12 and 18: 12/18 = 2/3.", "جی ہاں! 6، 12 اور 18 دونوں کو تقسیم کرتا ہے: 12/18 = 2/3"),
      opt("six_ninths", "6/9", "6/9", False,
          "6/9 is equal to 12/18, but 3 still divides 6 and 9. Keep going: 2/3.", "6/9، 12/18 کے برابر ہے، لیکن 3 اب بھی 6 اور 9 کو تقسیم کرتا ہے۔ آگے بڑھیں: 2/3"),
      opt("three_halves", "3/2", "3/2", False,
          "That is upside down: 3/2 is more than 1, but 12/18 is less than 1.", "یہ الٹا ہے: 3/2 تو 1 سے زیادہ ہے، جبکہ 12/18، 1 سے کم ہے۔"),
    ]},
   fraction_question(
     "u2_walk",
     T("Test 2: Sana walked 2/3 km to school and then 1/4 km to the shop. How far did she walk in all?",
       "ٹیسٹ 2: ثنا 2/3 کلومیٹر چل کر سکول گئی اور پھر 1/4 کلومیٹر چل کر دکان۔ وہ کل کتنا چلی؟"),
     frac(WALK),
     T("Add. 3 and 4 both go into 12: change both to twelfths.", "جمع کریں۔ 3 اور 4 دونوں 12 میں پورے آتے ہیں: دونوں کو بارہویں حصوں میں بدلیں۔"),
     T("Right! 8/12 + 3/12 = 11/12 km.", "درست! 8/12 + 3/12 = 11/12 کلومیٹر۔"),
     T("2/3 = 8/12 and 1/4 = 3/12. 8/12 + 3/12 = 11/12 km.", "2/3 = 8/12 اور 1/4 = 3/12۔ 8/12 + 3/12 = 11/12 کلومیٹر۔"),
     common_wrong=[wrong(unsimplified(2 + 1, 3 + 4), "You added the tops and the bottoms. 3/7 is less than 2/3! Change to twelfths first.",
                         "آپ نے اوپر اور نیچے والے جمع کر دیے۔ 3/7 تو 2/3 سے بھی کم ہے! پہلے بارہویں حصوں میں بدلیں۔", "add_tops_and_bottoms")],
     skill=ADD_UNLIKE),
   fraction_question(
     "u3_sugar",
     T("Test 3: Dadi bought 13 packets of sugar of 1/4 kg each: 13/4 kg. Write 13/4 as a mixed number.",
       "ٹیسٹ 3: دادی نے 1/4 کلوگرام والے چینی کے 13 پیکٹ خریدے: 13/4 کلوگرام۔ 13/4 کو مخلوط عدد کی شکل میں لکھیں۔"),
     mixed(SUGAR),
     T("4 quarters make 1 kg. 13 ÷ 4 = ? remainder ?", "4 چوتھائیاں 1 کلوگرام بناتی ہیں۔ 13 ÷ 4 = ? باقی ?"),
     T(f"Right! 13 ÷ 4 = 3 remainder 1, so {mixed(SUGAR)} kg.", f"درست! 13 ÷ 4 = 3 باقی 1، اس لیے {mixed(SUGAR)} کلوگرام۔"),
     T(f"13 ÷ 4 = 3 remainder 1: 3 whole kg and 1 quarter, {mixed(SUGAR)} kg.", f"13 ÷ 4 = 3 باقی 1: 3 پورے کلوگرام اور 1 چوتھائی، یعنی {mixed(SUGAR)} کلوگرام۔"),
     common_wrong=[
       wrong("1 3/4", "You swapped them. 13 ÷ 4 = 3 remainder 1: 3 is the whole kg and 1 goes on top.", "آپ نے جگہ بدل دی۔ 13 ÷ 4 = 3 باقی 1: 3 پورے کلوگرام ہیں اور 1 اوپر جاتا ہے۔"),
       wrong(frac(SUGAR), "That is the fraction we started with. Write it as whole kg and a fraction.", "یہ تو وہی کسر ہے جس سے شروع کیا۔ اسے پورے کلوگرام اور کسر کی شکل میں لکھیں۔"),
     ],
     qtype="recall", skill=MIXED),
   {"id": "u4_mithai", "type": "choice", "question_type": "find_error", "skill": MULTIPLY,
    "prompt": T(f"Test 4: A box of mithai has {BOX} pieces, and {frac(BARFI)} of them are barfi. Sana wrote {BOX} ÷ {frac(BARFI)} = {mixed(BOX / BARFI)} barfi. What went wrong?",
                f"ٹیسٹ 4: مٹھائی کے ڈبے میں {BOX} ٹکڑے ہیں، اور ان کا {frac(BARFI)} برفی ہے۔ ثنا نے لکھا {BOX} ÷ {frac(BARFI)} = {mixed(BOX / BARFI)} برفیاں۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("multiply", f"'{frac(BARFI)} of {BOX}' means multiply: {frac(BARFI)} × {BOX} = {BARFI * BOX} barfi.", f"'{BOX} کا {frac(BARFI)}' مطلب ضرب: {frac(BARFI)} × {BOX} = {BARFI * BOX} برفیاں۔", True,
          f"Yes! {BOX} ÷ 8 = 3, and 5 × 3 = {BARFI * BOX}. Her answer was more than the whole box!", f"جی ہاں! {BOX} ÷ 8 = 3، اور 5 × 3 = {BARFI * BOX}۔ اس کا جواب تو پورے ڈبے سے بھی زیادہ تھا!"),
      opt("nothing", "Nothing, the answer is right.", "کوئی غلطی نہیں، جواب درست ہے۔", False,
          f"Can there be more barfi than the {BOX} pieces in the box? The barfi is only a part of the box.", f"کیا ڈبے کے {BOX} ٹکڑوں سے زیادہ برفیاں ہو سکتی ہیں؟ برفی تو ڈبے کا صرف ایک حصہ ہے۔", "divide_instead_of_multiply"),
      opt("eighths", f"She should work out {BOX} ÷ 8 = 3 barfi.", f"اسے {BOX} ÷ 8 = 3 برفیاں نکالنی چاہییں تھیں۔", False,
          f"3 is only 1/8 of the box. {frac(BARFI)} is 5 of those eighths: 5 × 3 = {BARFI * BOX}.", f"3 تو ڈبے کا صرف 1/8 ہے۔ {frac(BARFI)} ایسے 5 آٹھویں حصے ہیں: 5 × 3 = {BARFI * BOX}"),
    ]},
   number_question(
     "u5_rotis",
     T(f"Test 5: Ammi has {ROTIS} rotis. Each child eats {frac(EACH)} of a roti. How many children can eat?",
       f"ٹیسٹ 5: امی کے پاس {ROTIS} روٹیاں ہیں۔ ہر بچہ {frac(EACH)} روٹی کھاتا ہے۔ کتنے بچے کھا سکتے ہیں؟"),
     num(CHILDREN),
     T(f"How many {frac(EACH)}s fit into {ROTIS}? Divide: multiply by the reciprocal, 4/3.", f"{ROTIS} میں {frac(EACH)} کتنی بار آتا ہے؟ تقسیم کریں: معکوس 4/3 سے ضرب دیں۔"),
     T(f"Right! {ROTIS} ÷ {frac(EACH)} = {ROTIS} × 4/3 = {CHILDREN} children.", f"درست! {ROTIS} ÷ {frac(EACH)} = {ROTIS} × 4/3 = {CHILDREN} بچے۔"),
     T(f"{ROTIS} ÷ {frac(EACH)} = {ROTIS} × 4/3 = 24/3 = {CHILDREN}. Each child eats less than a whole roti, so more than {ROTIS} children can eat.",
       f"{ROTIS} ÷ {frac(EACH)} = {ROTIS} × 4/3 = 24/3 = {CHILDREN}۔ ہر بچہ پوری روٹی سے کم کھاتا ہے، اس لیے {ROTIS} سے زیادہ بچے کھا سکتے ہیں۔"),
     common_wrong=[wrong(num(ROTIS * EACH), f"You multiplied. Each child eats less than one roti, so more than {ROTIS} children can eat. Divide.",
                         f"آپ نے ضرب دی۔ ہر بچہ ایک روٹی سے کم کھاتا ہے، اس لیے {ROTIS} سے زیادہ بچے کھا سکتے ہیں۔ تقسیم کریں۔", "multiply_instead_of_divide")],
     skill=DIVIDE),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "You finished the whole Fractions unit! Well done!", "آپ نے کسور کا پورا باب مکمل کر لیا! شاباش!"),
    "text": T("Read the story and picture it. Put together: add. Left or how much more: subtract. A fraction of an amount, or the same amount many times: multiply. How many parts fit: divide. Some stories need two steps. Always check that the answer makes sense.",
              "کہانی پڑھیں اور ذہن میں دیکھیں۔ اکٹھا کرنا: جمع۔ بچا یا کتنا زیادہ: تفریق۔ کسی مقدار کا کسری حصہ، یا ایک ہی مقدار کئی بار: ضرب۔ کتنے حصے آتے ہیں: تقسیم۔ کچھ سوالوں کے دو مرحلے ہوتے ہیں۔ ہمیشہ جانچیں کہ جواب سمجھ میں آتا ہے۔"),
    "points": [T(f"{frac(BARFI)} of {BOX} = {frac(BARFI)} × {BOX} = {BARFI * BOX}", f"{BOX} کا {frac(BARFI)} = {frac(BARFI)} × {BOX} = {BARFI * BOX}"),
               T(f"How many {frac(PER_DAY)} kg in {BAG} kg? {BAG} ÷ {frac(PER_DAY)} = {DAYS}", f"{BAG} کلوگرام میں {frac(PER_DAY)} کلوگرام کتنی بار؟ {BAG} ÷ {frac(PER_DAY)} = {DAYS}"),
               T("Check: a part of an amount is smaller than the amount.", "جانچ: کسی مقدار کا حصہ اس مقدار سے چھوٹا ہوتا ہے۔")]},
 ],
 "review_questions": [
   {"id": "r_milk", "type": "apply", "skill": SKILL, "step": number_question(
     "r_milk",
     T("Zara's family drinks 1 1/2 litres of milk every day. How much milk do they drink in 4 days? (litres)", "زارا کے گھر والے روز 1 1/2 لیٹر دودھ پیتے ہیں۔ 4 دن میں وہ کتنا دودھ پیتے ہیں؟ (لیٹر)"),
     num(MILK),
     T("The same amount 4 times: multiply. 4 × 1 1/2 = 4 × 3/2.", "ایک ہی مقدار 4 بار: ضرب۔ 4 × 1 1/2 = 4 × 3/2"),
     T(f"Right! 4 × 3/2 = 12/2 = {MILK} litres.", f"درست! 4 × 3/2 = 12/2 = {MILK} لیٹر۔"),
     T(f"4 × 1 = 4 and 4 × 1/2 = 2, so 4 + 2 = {MILK} litres.", f"4 × 1 = 4 اور 4 × 1/2 = 2، اس لیے 4 + 2 = {MILK} لیٹر۔"),
     common_wrong=[wrong(num(4 + F(1, 2)), "You multiplied the 1 but not the 1/2. 4 halves are 2 more litres.", "آپ نے 1 کو ضرب دی لیکن 1/2 کو نہیں۔ 4 آدھے 2 لیٹر اور بنتے ہیں۔")],
     qtype=None)},
   {"id": "r_lawn", "type": "apply", "skill": SKILL, "step": fraction_question(
     "r_lawn",
     T("A tailor had 5 metres of lawn. He cut 2 3/4 metres for a dupatta. How much lawn is left? Write a mixed number.", "ایک درزی کے پاس 5 میٹر لان تھی۔ اس نے دوپٹے کے لیے 2 3/4 میٹر کاٹی۔ کتنی لان بچی؟ مخلوط عدد لکھیں۔"),
     mixed(LAWN),
     T("'Left' means subtract. 5 = 4 4/4.", "'بچی' کا مطلب ہے تفریق۔ 5 = 4 4/4"),
     T(f"Right! 4 4/4 − 2 3/4 = {mixed(LAWN)} metres.", f"درست! 4 4/4 − 2 3/4 = {mixed(LAWN)} میٹر۔"),
     T(f"Write 5 as 4 4/4. Then 4 4/4 − 2 3/4 = {mixed(LAWN)} metres.", f"5 کو 4 4/4 لکھیں۔ پھر 4 4/4 − 2 3/4 = {mixed(LAWN)} میٹر۔"),
     common_wrong=[
       wrong(mixed(5 + 2 + F(3, 4)), "You added. He cut some cloth off, so less is left. Subtract.", "آپ نے جمع کیا۔ اس نے کپڑا کاٹا، اس لیے کم بچا۔ تفریق کریں۔", "wrong_add_subtract"),
       wrong("3 3/4", "5 − 2 = 3, but the 3/4 must be taken away too, not kept. Write 5 as 4 4/4.", "5 − 2 = 3، لیکن 3/4 بھی کم کرنا ہے، رکھنا نہیں۔ 5 کو 4 4/4 لکھیں۔"),
       wrong(frac(LAWN), "The right amount, but please write it as a mixed number.", "مقدار درست ہے، لیکن اسے مخلوط عدد کی شکل میں لکھیں۔"),
     ],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Fractions unit. No textbook text or exercises were used.",
   "Unit number to be confirmed against the PCTB Grade 6 book: the file is named g6-maths-02 to sit with the other fractions lessons. Fix the name and curriculum_refs if the unit differs.",
   "Urdu terms to check against the Punjab textbook: عبارتی سوال (word problem), عمل (operation), معکوس (reciprocal), کلوگرام / میٹر / لیٹر, اوور and ٹی ٹوئنٹی (cricket), and 'کا' used for 'of'.",
   "This is the last lesson of the unit. Steps s1 to s10 teach choosing the operation: foundation check (s2), the four questions (s3), choose then solve (s4, s5), add (s6), subtract (s7), a two-step problem (s8), find the error (s9), explain (s10).",
   "s11 to u5 are a short unit test, one question per earlier lesson. Each u-step is tagged with that lesson's skill (equivalent, add_unlike, mixed_numbers, multiply, divide_by_fraction), so it counts as practice for that skill rather than for word problems.",
   "Division stories only divide a whole number by a fraction or mixed number (as the dividing-fractions lesson teaches); no fraction ÷ fraction.",
   "In s8, '3/5 of the overs' is 12 overs of a 20-over innings; real scorecards write part-overs as 12.3 and so on, which this lesson avoids.",
   "The fraction checker accepts any equal value: where a step asks for a mixed number (s6, s7, u3, r_lawn), the improper fraction is listed in common_wrong with feedback asking for a mixed number (it costs an attempt).",
   "The answers and the common wrong answers were worked out with Python's fractions module in content/sources/g6-maths-02/fraction_word_problems.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)
