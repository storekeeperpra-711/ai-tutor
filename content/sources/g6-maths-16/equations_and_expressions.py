from common import (T, opt, say, wrong, number_question, write, value, solves,
                    REF, REVIEW, ALG_SUBSTITUTION, ALG_EQUATIONS, EQ_RECOGNISE)

SKILL = EQ_RECOGNISE


def balance(left, right, alt_en, alt_ur):
    """A level balance scale: `left` on one pan, `right` on the other."""
    items = [
        {"kind": "polygon", "points": [[85, 105], [115, 105], [100, 92]], "fill": True},
        {"kind": "line", "from": [100, 92], "to": [100, 30]},
        {"kind": "line", "from": [40, 30], "to": [160, 30]},
        {"kind": "point", "at": [100, 30]},
    ]
    for cx, text in ((40, left), (160, right)):
        items += [
            {"kind": "line", "from": [cx, 30], "to": [cx - 25, 60]},
            {"kind": "line", "from": [cx, 30], "to": [cx + 25, 60]},
            {"kind": "polygon", "points": [[cx - 30, 60], [cx + 30, 60], [cx + 20, 72], [cx - 20, 72]], "fill": True},
            {"kind": "label", "at": [cx, 86], "text": text},
        ]
    items.append({"kind": "label", "at": [100, 16], "text": "="})
    for it in items:
        if it["kind"] == "label":
            assert 1 <= len(it["text"]) <= 6
    return {"width": 200, "height": 110, "alt": T(alt_en, alt_ur), "items": items}


# s2: 2x + 5 when x = 4 (reading 2x as 24 gives 29)
S2 = value("2x + 5", x=4)
assert S2 == 13 and 24 + 5 == 29
# s3: the worked example 3x + 5 = 20 has solution x = 5
assert solves("3x + 5 = 20", x=5)
# s5: 8 + 5 = 12 is a false arithmetic equation
assert 8 + 5 != 12
# s6: evaluate 4x − 2 for x = 3 (reading 4x as 43 gives 41)
S6 = value("4x − 2", x=3)
assert S6 == 10 and 43 - 2 == 41
# s8: "5 more than a number is 12" -> n + 5 = 12, n = 7
assert solves("n + 5 = 12", n=7)
# s11: Ali's age a + 6 = 18 (adding gives 24)
S11 = [a for a in range(1, 30) if solves("a + 6 = 18", a=a)]
assert S11 == [12] and 18 + 6 == 24
S11 = S11[0]
# question bank and review
QB = value("5m + 1", m=3)
assert QB == 16 and 53 + 1 == 54
assert 4 * 4 == 16 and 2 * 4 != 16  # x² = 16 has x = 4 but x² is not 2x
R2 = value("6 + 2y", y=5)
assert R2 == 16 and 6 + 25 == 31

lesson = {
 "id": "g6-maths-16-equations-and-expressions",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Tell an algebraic equation from an algebraic expression in one variable, and recognise a linear equation in one variable (7.1, 7.1.1, 7.2.1).", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Equations and expressions", "مساوات اور الجبری جملے"),
 "estimated_minutes": 13,
 "prerequisites": [{"skill": ALG_SUBSTITUTION}, {"skill": ALG_EQUATIONS}],
 "misconceptions": [
   {"id": "letter_means_equation", "description": "Thinks anything with a letter is an equation, even with no = sign."},
   {"id": "power_is_linear", "description": "Counts x² = 9 or xy = 6 as a linear equation in one variable."},
   {"id": "joins_digits", "description": "Reads 4x with x = 3 as 43 instead of 4 × 3."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_meaning", "type": "recall", "step": {
     "id": "qb_meaning", "type": "choice",
     "prompt": T("What does an equation have that an expression does not?", "مساوات میں ایسا کیا ہوتا ہے جو الجبری جملے میں نہیں ہوتا؟"),
     "options": [
       opt("equals", "An = sign", "= کا نشان", True,
           "Yes! An equation says two things are equal.", "جی ہاں! مساوات بتاتی ہے کہ دو چیزیں برابر ہیں۔"),
       opt("letter", "A letter", "ایک حرف", False,
           "Expressions have letters too, like 3x + 5. The = sign makes an equation.", "الجبری جملوں میں بھی حرف ہوتے ہیں، جیسے 3x + 5۔ = کا نشان مساوات بناتا ہے۔", "letter_means_equation"),
       opt("plus", "A + sign", "+ کا نشان", False,
           "3x + 5 has a + sign but is an expression. Look for the = sign.", "3x + 5 میں + ہے مگر یہ الجبری جملہ ہے۔ = کا نشان دیکھیں۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("Find the value of the expression 5m + 1 when m = 3.", "جب m = 3 ہو تو الجبری جملے 5m + 1 کی قیمت معلوم کریں۔"),
     QB,
     T("5m means 5 × m.", "5m یعنی 5 × m"),
     T("Right! 5 × 3 + 1 = 16.", "درست! 5 × 3 + 1 = 16"),
     T("5 × 3 = 15, then 15 + 1 = 16.", "5 × 3 = 15، پھر 15 + 1 = 16"),
     common_wrong=[wrong(54, "5m is 5 × 3, not 53: 15 + 1 = 16.", "5m یعنی 5 × 3، 53 نہیں: 15 + 1 = 16", "joins_digits")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Bilal says x² = 16 is a linear equation in one variable. What is wrong?", "بلال کہتا ہے x² = 16 ایک متغیر والی خطی مساوات ہے۔ کیا غلطی ہے؟"),
     "options": [
       opt("power", "x has power 2. In a linear equation the letter has power 1 only.", "x کی طاقت 2 ہے۔ خطی مساوات میں حرف کی طاقت صرف 1 ہوتی ہے۔", True,
           "Yes! x² is x × x, so it is not linear.", "جی ہاں! x² یعنی x × x، اس لیے یہ خطی نہیں۔"),
       opt("no_equals", "It has no = sign.", "اس میں = کا نشان نہیں۔", False,
           "It does have =. The problem is the power 2 on x.", "اس میں = ہے۔ مسئلہ x پر طاقت 2 کا ہے۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "x² means x × x: power 2. Linear needs power 1.", "x² یعنی x × x: طاقت 2۔ خطی کے لیے طاقت 1 چاہیے۔", "power_is_linear"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_difference", "front": T("Expression or equation?", "الجبری جملہ یا مساوات؟"),
    "back": T("3x + 5 is an expression (no =). 3x + 5 = 20 is an equation.", "3x + 5 الجبری جملہ ہے (= نہیں)۔ 3x + 5 = 20 مساوات ہے۔")},
   {"id": "f_linear", "front": T("Linear equation in one variable?", "ایک متغیر والی خطی مساوات؟"),
    "back": T("One letter, power 1 only: x + 4 = 9.", "ایک حرف، صرف طاقت 1: x + 4 = 9")},
 ],
 "home_tasks": [{"id": "h_balance", "text": T(
   "Hang two plastic bags from the ends of a ruler or hanger. Put the same number of coins in each so it hangs level: that is an equation. Write one equation and one expression about your coins, e.g. c + 3 = 8 and c + 3.",
   "ایک فٹے یا ہینگر کے دونوں سروں پر دو تھیلیاں لٹکائیں۔ دونوں میں برابر سکے ڈالیں تاکہ وہ سیدھا لٹکے: یہ مساوات ہے۔ اپنے سکوں کے بارے میں ایک مساوات اور ایک الجبری جملہ لکھیں، جیسے c + 3 = 8 اور c + 3۔")}],
 "glossary": [T("Equation", "مساوات"), T("Expression", "الجبری جملہ"), T("Variable", "متغیر"),
              T("Linear equation", "خطی مساوات"), T("Open sentence", "کھلا جملہ"), T("Closed sentence", "بند جملہ")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Babar scored 3x + 5 runs. Is that a question with an answer, or just a way to write runs?",
                     "بابر نے 3x + 5 رنز بنائے۔ کیا یہ سوال ہے جس کا جواب ہو، یا رنز لکھنے کا ایک طریقہ؟"),
    "text": T("Today we learn the difference between an expression and an equation. First, a quick substitution check.",
              "آج ہم الجبری جملے اور مساوات کا فرق سیکھیں گے۔ پہلے قیمت رکھنے کا ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("Find the value of 2x + 5 when x = 4.", "جب x = 4 ہو تو 2x + 5 کی قیمت معلوم کریں۔"),
     S2,
     T("2x means 2 × x.", "2x یعنی 2 × x"),
     T("Right! 2 × 4 + 5 = 13.", "درست! 2 × 4 + 5 = 13"),
     T("2 × 4 = 8, then 8 + 5 = 13.", "2 × 4 = 8، پھر 8 + 5 = 13"),
     common_wrong=[wrong(29, "2x is 2 × 4, not 24: 8 + 5 = 13.", "2x یعنی 2 × 4، 24 نہیں: 8 + 5 = 13", "joins_digits")],
     qtype="recall", skill=ALG_SUBSTITUTION),
   {"id": "s3_rule", "type": "explain",
    "character": say("happy", "No = sign? Expression. An = sign? Equation, like a balance that is level!",
                     "= کا نشان نہیں؟ الجبری جملہ۔ = کا نشان ہے؟ مساوات، برابر ترازو کی طرح!"),
    "text": T("An expression has no = sign, like 3x + 5. We can find its value when we know x. An equation says two things are equal, like 3x + 5 = 20, a level balance. We can solve it: find the x that makes it true (here x = 5). 4 + 3 = 7 is an arithmetic equation: no letter, and it is either true or false (a closed sentence). 3x + 5 = 20 is an algebraic equation: it has a letter, so it is an open sentence until we know x. If the letter has power 1 only, like x + 4 = 9, it is a linear equation in one variable. x² = 9 (power 2) and xy = 6 (two letters) are not.",
              "الجبری جملے میں = کا نشان نہیں ہوتا، جیسے 3x + 5۔ x معلوم ہو تو ہم اس کی قیمت نکال سکتے ہیں۔ مساوات بتاتی ہے کہ دو چیزیں برابر ہیں، جیسے 3x + 5 = 20، ایک برابر ترازو۔ ہم اسے حل کر سکتے ہیں: وہ x ڈھونڈیں جو اسے درست کرے (یہاں x = 5)۔ 4 + 3 = 7 حسابی مساوات ہے: اس میں حرف نہیں، اور یہ یا درست ہے یا غلط (بند جملہ)۔ 3x + 5 = 20 الجبری مساوات ہے: اس میں حرف ہے، اس لیے جب تک x معلوم نہ ہو یہ کھلا جملہ ہے۔ اگر حرف کی طاقت صرف 1 ہو، جیسے x + 4 = 9، تو یہ ایک متغیر والی خطی مساوات ہے۔ x² = 9 (طاقت 2) اور xy = 6 (دو حرف) خطی مساوات نہیں۔"),
    "figure": balance("3x+5", "20",
                      "A level balance scale. The left pan holds 3x + 5 and the right pan holds 20, with an equals sign above the middle.",
                      "ایک برابر ترازو۔ بائیں پلڑے میں 3x + 5 اور دائیں پلڑے میں 20 ہے، اور درمیان کے اوپر برابر کا نشان ہے۔")},
   {"id": "s4_which_equation", "type": "choice",
    "prompt": T("Which one is an equation?", "ان میں سے مساوات کون سی ہے؟"),
    "options": [
      opt("eq", "3x + 5 = 20", "3x + 5 = 20", True,
          "Yes! It has an = sign: two sides that are equal.", "جی ہاں! اس میں = ہے: دو برابر اطراف۔"),
      opt("expr", "3x + 5", "3x + 5", False,
          "It has a letter, but no = sign. It is an expression.", "اس میں حرف ہے مگر = نہیں۔ یہ الجبری جملہ ہے۔", "letter_means_equation"),
      opt("term", "7y", "7y", False,
          "7y means 7 × y. No = sign, so it is an expression.", "7y یعنی 7 × y۔ = نہیں، اس لیے یہ الجبری جملہ ہے۔", "letter_means_equation"),
    ]},
   {"id": "s5_closed", "type": "choice",
    "prompt": T("8 + 5 = 12 is an arithmetic equation (no letter). Is it true or false?", "8 + 5 = 12 ایک حسابی مساوات ہے (حرف نہیں)۔ کیا یہ درست ہے یا غلط؟"),
    "options": [
      opt("false", "False", "غلط", True,
          "Yes! 8 + 5 = 13, not 12. With no letter, we can say true or false straight away.", "جی ہاں! 8 + 5 = 13، 12 نہیں۔ حرف نہ ہو تو فوراً درست یا غلط کہہ سکتے ہیں۔"),
      opt("true", "True", "درست", False,
          "8 + 5 = 13, so 8 + 5 = 12 is false.", "8 + 5 = 13، اس لیے 8 + 5 = 12 غلط ہے۔"),
      opt("cant_tell", "We can't tell", "نہیں بتا سکتے", False,
          "There is no letter, so we can tell: 8 + 5 = 13, so it is false. A closed sentence.", "حرف نہیں، اس لیے بتا سکتے ہیں: 8 + 5 = 13، تو یہ غلط ہے۔ بند جملہ۔"),
    ]},
   number_question(
     "s6_evaluate",
     T("A mango costs x rupees. 4 mangoes with a 2 rupee discount cost 4x − 2. Find the value of 4x − 2 when x = 3.",
       "ایک آم x روپے کا ہے۔ 2 روپے رعایت کے ساتھ 4 آم 4x − 2 کے ہیں۔ جب x = 3 ہو تو 4x − 2 کی قیمت معلوم کریں۔"),
     S6,
     T("4 × 3 first, then − 2.", "پہلے 4 × 3، پھر − 2"),
     T("Right! 12 − 2 = 10. An expression gives a value once we know x.", "درست! 12 − 2 = 10۔ x معلوم ہو تو الجبری جملے کی قیمت ملتی ہے۔"),
     T("4 × 3 = 12, then 12 − 2 = 10.", "4 × 3 = 12، پھر 12 − 2 = 10"),
     common_wrong=[wrong(41, "4x is 4 × 3, not 43: 12 − 2 = 10.", "4x یعنی 4 × 3، 43 نہیں: 12 − 2 = 10", "joins_digits")]),
   {"id": "s7_linear", "type": "choice",
    "prompt": T("Which is a linear equation in one variable?", "ان میں سے ایک متغیر والی خطی مساوات کون سی ہے؟"),
    "options": [
      opt("linear", "x + 4 = 9", "x + 4 = 9", True,
          "Yes! One letter, x, with power 1.", "جی ہاں! ایک حرف، x، طاقت 1 کے ساتھ۔"),
      opt("square", "x² = 9", "x² = 9", False,
          "x² is x × x: power 2. Linear needs power 1.", "x² یعنی x × x: طاقت 2۔ خطی کے لیے طاقت 1 چاہیے۔", "power_is_linear"),
      opt("two_vars", "xy = 6", "xy = 6", False,
          "xy has two letters, x and y. We want one variable only.", "xy میں دو حرف ہیں، x اور y۔ ہمیں صرف ایک متغیر چاہیے۔", "power_is_linear"),
    ]},
   {"id": "s8_sentence", "type": "choice",
    "prompt": T("Ahmed had n mangoes. He got 5 more and now has 12. Which matches '5 more than a number is 12'?",
                "احمد کے پاس n آم تھے۔ اسے 5 اور ملے اور اب اس کے پاس 12 ہیں۔ '5 زیادہ ایک عدد سے، 12 ہے' کس سے ملتا ہے؟"),
    "options": [
      opt("equation", "n + 5 = 12", "n + 5 = 12", True,
          "Yes! 'is 12' becomes '= 12', so it is an equation.", "جی ہاں! '12 ہے' بنتا ہے '= 12'، اس لیے یہ مساوات ہے۔"),
      opt("expression", "n + 5", "n + 5", False,
          "n + 5 is only '5 more than a number'. 'is 12' adds '= 12'.", "n + 5 صرف 'ایک عدد سے 5 زیادہ' ہے۔ '12 ہے' سے '= 12' لگتا ہے۔"),
      opt("times", "5n = 12", "5n = 12", False,
          "5n means 5 times n. '5 more' means + 5: n + 5 = 12.", "5n یعنی 5 گنا n۔ '5 زیادہ' یعنی + 5: n + 5 = 12"),
    ]},
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Hira says, '2y + 7 is an equation because it has a letter.' What went wrong?",
                "حرا کہتی ہے، '2y + 7 مساوات ہے کیونکہ اس میں حرف ہے۔' کیا غلطی ہوئی؟"),
    "options": [
      opt("no_equals", "It has no = sign, so it is an expression.", "اس میں = کا نشان نہیں، اس لیے یہ الجبری جملہ ہے۔", True,
          "Yes! A letter alone does not make an equation; the = sign does.", "جی ہاں! صرف حرف سے مساوات نہیں بنتی؛ = کا نشان بناتا ہے۔"),
      opt("two_letters", "An equation needs two letters.", "مساوات کے لیے دو حرف چاہییں۔", False,
          "x + 4 = 9 has one letter and is an equation. The = sign is what matters.", "x + 4 = 9 میں ایک حرف ہے اور یہ مساوات ہے۔ اصل بات = کا نشان ہے۔"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "2y + 7 has no = sign. It is an expression, not an equation.", "2y + 7 میں = نہیں۔ یہ الجبری جملہ ہے، مساوات نہیں۔", "letter_means_equation"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "x + 6 and x + 6 = 10 look nearly the same. What is the difference? Can you teach me?",
                     "x + 6 اور x + 6 = 10 تقریباً ایک جیسے لگتے ہیں۔ فرق کیا ہے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: what is the difference between x + 6 and x + 6 = 10?",
              "اپنے الفاظ میں بتائیں: x + 6 اور x + 6 = 10 میں کیا فرق ہے؟"),
    "key_idea": "x + 6 is an expression: it has no = sign, and we can find its value for any x. x + 6 = 10 is an equation: the = sign says both sides are equal, so we can solve it and find x = 4.",
    "levels": {
      "got_it": "Says x + 6 is an expression with no = sign, and x + 6 = 10 is an equation (has =) that can be solved (x = 4).",
      "partly": "Points to the = sign but does not say which is the expression and which the equation, or does not mention solving.",
      "not_yet": "Gives no difference, or says they are the same."},
    "keywords": [
      ["expression", "الجبری جملہ", "jumla"],
      ["equation", "مساوات", "masawat"],
      ["=", "equal", "equals", "برابر"],
      ["solve", "4", "حل"]],
    "fallback_feedback": {
      "got_it": T("Well explained! The = sign turns an expression into an equation we can solve.", "بہت خوب! = کا نشان الجبری جملے کو مساوات بنا دیتا ہے جسے ہم حل کر سکتے ہیں۔"),
      "partly": T("Good start! Now say which one is the equation, and what x makes it true.", "اچھی شروعات! اب بتائیں مساوات کون سی ہے، اور کون سا x اسے درست کرتا ہے۔"),
      "not_yet": T("Look for the = sign. Which one has it? That one is the equation.", "= کا نشان ڈھونڈیں۔ کس میں ہے؟ وہی مساوات ہے۔")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_solve",
     T("In 6 years Ali will be 18, so a + 6 = 18. What value of a makes this equation true?",
       "6 سال بعد علی 18 سال کا ہو گا، تو a + 6 = 18۔ a کی کون سی قیمت اس مساوات کو درست کرتی ہے؟"),
     S11,
     T("What number plus 6 makes 18?", "کون سا عدد جمع 6 برابر 18؟"),
     T("Right! 12 + 6 = 18, so Ali is 12 now.", "درست! 12 + 6 = 18، تو علی ابھی 12 سال کا ہے۔"),
     T("18 − 6 = 12. Check: 12 + 6 = 18.", "18 − 6 = 12۔ جانچ: 12 + 6 = 18"),
     common_wrong=[wrong(24, "24 + 6 = 30, not 18. Take 6 away: 18 − 6 = 12.", "24 + 6 = 30، 18 نہیں۔ 6 نفی کریں: 18 − 6 = 12")],
     character=None) | {"figure": balance("a+6", "18",
                         "A level balance scale. The left pan holds a + 6 and the right pan holds 18, with an equals sign above the middle.",
                         "ایک برابر ترازو۔ بائیں پلڑے میں a + 6 اور دائیں پلڑے میں 18 ہے، اور درمیان کے اوپر برابر کا نشان ہے۔")},
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "No = sign: expression, find its value. An = sign: equation, solve it. Well done!",
                     "= نہیں: الجبری جملہ، قیمت نکالیں۔ = ہے: مساوات، حل کریں۔ شاباش!"),
    "text": T("An expression, like 3x + 5, has no = sign; we can find its value when we know x. An equation, like 3x + 5 = 20, says two sides are equal; we can solve it. With no letter (4 + 3 = 7) an equation is simply true or false. A linear equation in one variable has one letter with power 1, like x + 4 = 9.",
              "الجبری جملہ، جیسے 3x + 5، میں = نہیں ہوتا؛ x معلوم ہو تو اس کی قیمت نکلتی ہے۔ مساوات، جیسے 3x + 5 = 20، بتاتی ہے کہ دونوں اطراف برابر ہیں؛ ہم اسے حل کر سکتے ہیں۔ حرف کے بغیر (4 + 3 = 7) مساوات بس درست یا غلط ہوتی ہے۔ ایک متغیر والی خطی مساوات میں ایک حرف طاقت 1 کے ساتھ ہوتا ہے، جیسے x + 4 = 9۔"),
    "points": [T("No = : expression. With = : equation.", "= نہیں: الجبری جملہ۔ = ہے: مساوات۔"),
               T("Linear: one letter, power 1.", "خطی: ایک حرف، طاقت 1۔")]},
 ],
 "review_questions": [
   {"id": "r_which", "type": "recall", "skill": SKILL, "step": {
     "id": "r_which", "type": "choice",
     "prompt": T("Which one is an expression?", "ان میں سے الجبری جملہ کون سا ہے؟"),
     "options": [
       opt("expr", "k + 9", "k + 9", True,
           "Yes! No = sign, so it is an expression.", "جی ہاں! = نہیں، اس لیے یہ الجبری جملہ ہے۔"),
       opt("eq", "k + 9 = 15", "k + 9 = 15", False,
           "This has an = sign, so it is an equation.", "اس میں = ہے، اس لیے یہ مساوات ہے۔"),
       opt("arith", "6 + 9 = 15", "6 + 9 = 15", False,
           "This has an = sign: an arithmetic equation.", "اس میں = ہے: حسابی مساوات۔"),
     ]}},
   {"id": "r_value", "type": "apply", "skill": SKILL, "step": number_question(
     "r_value",
     T("Find the value of 6 + 2y when y = 5.", "جب y = 5 ہو تو 6 + 2y کی قیمت معلوم کریں۔"),
     R2,
     T("2y means 2 × y.", "2y یعنی 2 × y"),
     T("Right! 6 + 10 = 16.", "درست! 6 + 10 = 16"),
     T("2 × 5 = 10, then 6 + 10 = 16.", "2 × 5 = 10، پھر 6 + 10 = 16"),
     common_wrong=[wrong(31, "2y is 2 × 5, not 25: 6 + 10 = 16.", "2y یعنی 2 × 5، 25 نہیں: 6 + 10 = 16", "joins_digits")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Linear Equations unit (7.1, 7.1.1, 7.2.1). No textbook text or exercises were used.",
   "The key test is the = sign: a letter alone does not make an equation. The balance scale picture shows an equation as two equal sides.",
   "Open and closed sentences are named once; the main aim is sorting expression / equation and linear / not linear.",
   "Urdu terms to check: مساوات (equation), الجبری جملہ (algebraic expression), حسابی مساوات (arithmetic equation), خطی مساوات (linear equation), متغیر (variable), کھلا / بند جملہ (open / closed sentence), طاقت (power).",
   "The numbers were worked out in content/sources/g6-maths-16/equations_and_expressions.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)
