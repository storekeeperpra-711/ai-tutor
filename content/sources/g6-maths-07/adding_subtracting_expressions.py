from common import (T, opt, say, wrong, text_question, write, expr, expr_forms,
                    collect, negate, BOOK, REVIEW, ALG_LIKE_TERMS, ALG_ADD_SUBTRACT)

SKILL = ALG_ADD_SUBTRACT


def add(a, b):
    return collect(*a, *b)


def sub(a, b):
    return collect(*a, *negate(*b))


def wrong_sub(a, b):
    """The common slip: only the first term of the bracket is subtracted."""
    (c, v), *rest = b
    return collect(*a, (-c, v), *rest)


def expression_question(id, prompt, terms, hint, good, bad, *, common_wrong=(), qtype="apply", skill=None):
    """A typed expression; any order of the terms is accepted."""
    expected = expr(*terms)
    forms = [f for f in expr_forms(*terms) if f != expected.replace(" ", "")]
    for w in common_wrong:
        assert w["answer"].replace(" ", "") not in expr_forms(*terms), (id, w["answer"])
    return text_question(id, prompt, expected, hint, good, bad, accept=forms,
                         common_wrong=common_wrong, qtype=qtype, skill=skill)


def show(terms):
    """For feedback: the expression with a real minus sign."""
    return expr(*terms, minus="−").replace("-", "−")


S2 = collect((3, "a"), (2, "a"))
assert S2 == ((5, "a"),)
S4 = add([(2, "x"), (5, "")], [(3, "x"), (1, "")])
assert S4 == ((5, "x"), (6, ""))
S5 = add([(4, "a"), (3, "b")], [(1, "a"), (-1, "b")])
assert S5 == ((5, "a"), (2, "b")) and collect((4, "a"), (3, "b"), (-1, "b")) == ((4, "a"), (2, "b"))
S6 = sub([(6, "m"), (5, "")], [(2, "m"), (3, "")])
assert S6 == ((4, "m"), (2, "")) and wrong_sub([(6, "m"), (5, "")], [(2, "m"), (3, "")]) == ((4, "m"), (8, ""))
S7 = sub([(7, "y"), (9, "")], [(3, "y"), (4, "")])
assert S7 == ((4, "y"), (5, "")) and wrong_sub([(7, "y"), (9, "")], [(3, "y"), (4, "")]) == ((4, "y"), (13, ""))
S8 = sub([(5, "p"), (-2, "")], [(1, "p"), (-6, "")])
assert S8 == ((4, "p"), (4, "")) and wrong_sub([(5, "p"), (-2, "")], [(1, "p"), (-6, "")]) == ((4, "p"), (-8, ""))
assert sub([(8, "n"), (3, "")], [(5, "n"), (2, "")]) == ((3, "n"), (1, ""))
assert wrong_sub([(8, "n"), (3, "")], [(5, "n"), (2, "")]) == ((3, "n"), (5, ""))
S11 = collect((1, "x"), (2, ""), (2, "x"), (1, ""), (3, "x"))
assert S11 == ((6, "x"), (3, ""))
QB = sub([(9, "k"), (7, "")], [(4, "k"), (2, "")])
assert QB == ((5, "k"), (5, ""))
assert add([(2, "a"), (1, "b")], [(3, "a"), (4, "b")]) == ((5, "a"), (5, "b"))
R1 = add([(3, "x"), (2, "y")], [(1, "x"), (5, "y")])
assert R1 == ((4, "x"), (7, "y"))
R2 = sub([(10, "m"), (6, "")], [(3, "m"), (4, "")])
assert R2 == ((7, "m"), (2, ""))

lesson = {
 "id": "g6-maths-07-adding-subtracting-expressions",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Add and subtract algebraic expressions, removing brackets and collecting like terms.", "textbook": f"{BOOK}, Addition and subtraction of algebraic expressions"}],
 "skills": [SKILL],
 "title": T("Adding and subtracting expressions", "عبارتوں کی جمع اور تفریق"),
 "estimated_minutes": 15,
 "prerequisites": [{"skill": ALG_LIKE_TERMS}],
 "misconceptions": [
   {"id": "first_term_only", "description": "When subtracting a bracket, changes the sign of only the first term inside it."},
   {"id": "unlike_joined", "description": "Adds unlike terms together (5x + 6 becomes 11x)."},
   {"id": "lone_letter_zero", "description": "Forgets that a lone letter (a) means 1a when collecting."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_rule", "type": "recall", "step": {
     "id": "qb_rule", "type": "choice",
     "prompt": T("To take away (3a + 4), you …", "(3a + 4) تفریق کرنے کے لیے آپ …"),
     "options": [
       opt("both", "take away 3a AND take away 4", "3a بھی تفریق کریں اور 4 بھی", True,
           "Yes! −(3a + 4) = −3a − 4.", "جی ہاں! −(3a + 4) = −3a − 4"),
       opt("first", "take away 3a and add 4", "3a تفریق کریں اور 4 جمع کریں", False,
           "The whole bracket is taken away, so 4 is taken away too: −3a − 4.", "پوری بریکٹ تفریق ہوتی ہے، تو 4 بھی تفریق: −3a − 4", "first_term_only"),
       opt("ignore", "just drop the bracket", "بس بریکٹ ہٹا دیں", False,
           "The minus in front changes every sign inside: −3a − 4.", "سامنے کا منفی اندر کی ہر علامت بدلتا ہے: −3a − 4", "first_term_only"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": expression_question(
     "qb_apply",
     T("Simplify (9k + 7) − (4k + 2).", "(9k + 7) − (4k + 2) کو مختصر کریں۔"),
     QB,
     T("Take away 4k AND take away 2.", "4k بھی تفریق کریں اور 2 بھی۔"),
     T(f"Right! {show(QB)}.", f"درست! {show(QB)}"),
     T("9k − 4k = 5k and 7 − 2 = 5: 5k + 5.", "9k − 4k = 5k اور 7 − 2 = 5: 5k + 5"),
     common_wrong=[wrong("5k + 9", "Take away the 2 as well: 7 − 2 = 5. 5k + 5.", "2 بھی تفریق کریں: 7 − 2 = 5۔ 5k + 5", "first_term_only")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Hamza writes (2a + b) + (3a + 4b) = 5a + 4b. What is wrong?", "حمزہ لکھتا ہے (2a + b) + (3a + 4b) = 5a + 4b۔ کیا غلطی ہے؟"),
     "options": [
       opt("one_b", "b means 1b, so b + 4b = 5b: the answer is 5a + 5b.", "b یعنی 1b، تو b + 4b = 5b: جواب 5a + 5b", True,
           "Yes! Don't lose the lone b.", "جی ہاں! اکیلا b نہ کھوئیں۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "He left out the first b. b + 4b = 5b: 5a + 5b.", "اس نے پہلا b چھوڑ دیا۔ b + 4b = 5b: 5a + 5b", "lone_letter_zero"),
       opt("all", "It should be 10ab.", "یہ 10ab ہونا چاہیے۔", False,
           "a and b are unlike terms; they stay apart: 5a + 5b.", "a اور b غیر یکساں ارکان ہیں؛ الگ رہتے ہیں: 5a + 5b", "unlike_joined"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_add", "front": T("(3a + 2b) + (4a + b)?", "(3a + 2b) + (4a + b)؟"),
    "back": T("Collect like terms: 7a + 3b.", "یکساں ارکان جمع کریں: 7a + 3b")},
   {"id": "f_sub", "front": T("−(2x + 1)?", "−(2x + 1)؟"),
    "back": T("Change EVERY sign in the bracket: −2x − 1.", "بریکٹ کی ہر علامت بدلیں: −2x − 1")},
 ],
 "home_tasks": [{"id": "h_fruit", "text": T(
   "Put 5 apples and 4 oranges in a basket (5a + 4o). Take out 2 apples and 1 orange. Write what you took out as a bracket and what is left as an expression.",
   "ایک ٹوکری میں 5 سیب اور 4 مالٹے رکھیں (5a + 4o)۔ 2 سیب اور 1 مالٹا نکالیں۔ جو نکالا اسے بریکٹ میں اور جو بچا اسے عبارت میں لکھیں۔")}],
 "glossary": [T("Expression", "عبارت"), T("Like terms", "یکساں ارکان"), T("Bracket", "بریکٹ (قوسین)"), T("Simplify", "مختصر کرنا")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "A basket has 6 mangoes and 5 bananas. Take out 2 mangoes and 3 bananas. Can algebra keep track?",
                     "ٹوکری میں 6 آم اور 5 کیلے ہیں۔ 2 آم اور 3 کیلے نکالیں۔ کیا الجبرا حساب رکھ سکتا ہے؟"),
    "text": T("Today we add and subtract whole expressions, with brackets. First, collect like terms.", "آج ہم بریکٹ والی پوری عبارتیں جمع اور تفریق کریں گے۔ پہلے یکساں ارکان جمع کریں۔")},
   expression_question(
     "s2_foundation",
     T("Simplify 3a + 2a.", "3a + 2a کو مختصر کریں۔"),
     S2,
     T("3 a's and 2 more a's.", "3 a اور 2 مزید a"),
     T("Right! 5a.", "درست! 5a"),
     T("3a + 2a = 5a, like 3 apples + 2 apples.", "3a + 2a = 5a، جیسے 3 سیب + 2 سیب"),
     common_wrong=[wrong("6a", "Add the coefficients, don't multiply: 3 + 2 = 5. 5a.", "عددی سر جمع کریں، ضرب نہیں: 3 + 2 = 5۔ 5a")],
     qtype="recall", skill=ALG_LIKE_TERMS),
   {"id": "s3_rule", "type": "explain",
    "character": say("happy", "Adding? Just collect like terms. Subtracting? Change every sign in the bracket first!", "جمع؟ بس یکساں ارکان جمع کریں۔ تفریق؟ پہلے بریکٹ کی ہر علامت بدلیں!"),
    "text": T("To add expressions, remove the brackets and collect like terms: (3a + 2b) + (4a + b) = 3a + 2b + 4a + b = 7a + 3b. To subtract, the minus sign takes away EVERYTHING in the bracket, so every sign inside changes: (5x + 4) − (2x + 1) = 5x + 4 − 2x − 1 = 3x + 3. Unlike terms, like 3x and 3, stay apart.",
              "عبارتیں جمع کرنے کے لیے بریکٹ ہٹائیں اور یکساں ارکان جمع کریں: (3a + 2b) + (4a + b) = 3a + 2b + 4a + b = 7a + 3b۔ تفریق میں منفی کی علامت بریکٹ کی ہر چیز تفریق کرتی ہے، تو اندر کی ہر علامت بدل جاتی ہے: (5x + 4) − (2x + 1) = 5x + 4 − 2x − 1 = 3x + 3۔ غیر یکساں ارکان، جیسے 3x اور 3، الگ رہتے ہیں۔")},
   expression_question(
     "s4_add",
     T("Simplify (2x + 5) + (3x + 1).", "(2x + 5) + (3x + 1) کو مختصر کریں۔"),
     S4,
     T("x terms together, numbers together.", "x والے ارکان اکٹھے، اعداد اکٹھے۔"),
     T(f"Right! {show(S4)}.", f"درست! {show(S4)}"),
     T("2x + 3x = 5x and 5 + 1 = 6: 5x + 6.", "2x + 3x = 5x اور 5 + 1 = 6: 5x + 6"),
     common_wrong=[wrong("11x", "5x and 6 are unlike terms; they stay apart: 5x + 6.", "5x اور 6 غیر یکساں ہیں؛ الگ رہتے ہیں: 5x + 6", "unlike_joined")]),
   expression_question(
     "s5_add_two",
     T("Simplify (4a + 3b) + (a − b).", "(4a + 3b) + (a − b) کو مختصر کریں۔"),
     S5,
     T("a means 1a, and −b means −1b.", "a یعنی 1a، اور −b یعنی −1b"),
     T(f"Right! {show(S5)}.", f"درست! {show(S5)}"),
     T("4a + a = 5a and 3b − b = 2b: 5a + 2b.", "4a + a = 5a اور 3b − b = 2b: 5a + 2b"),
     common_wrong=[wrong("4a + 2b", "Don't lose the lone a: 4a + a = 5a. 5a + 2b.", "اکیلا a نہ کھوئیں: 4a + a = 5a۔ 5a + 2b", "lone_letter_zero")]),
   {"id": "s6_subtract", "type": "choice",
    "prompt": T("What is (6m + 5) − (2m + 3)?", "(6m + 5) − (2m + 3) کیا ہے؟"),
    "options": [
      opt("right", show(S6), show(S6), True, "Yes! 6m − 2m = 4m and 5 − 3 = 2.", "جی ہاں! 6m − 2m = 4m اور 5 − 3 = 2"),
      opt("first_only", "4m + 8", "4m + 8", False, "The 3 must be taken away too: 5 − 3 = 2. 4m + 2.", "3 بھی تفریق کرنا ہے: 5 − 3 = 2۔ 4m + 2", "first_term_only"),
      opt("added", "8m + 2", "8m + 2", False, "Take away 2m, don't add it: 6m − 2m = 4m.", "2m تفریق کریں، جمع نہیں: 6m − 2m = 4m"),
    ]},
   expression_question(
     "s7_subtract",
     T("Simplify (7y + 9) − (3y + 4).", "(7y + 9) − (3y + 4) کو مختصر کریں۔"),
     S7,
     T("−(3y + 4) = −3y − 4.", "−(3y + 4) = −3y − 4"),
     T(f"Right! {show(S7)}.", f"درست! {show(S7)}"),
     T("7y − 3y = 4y and 9 − 4 = 5: 4y + 5.", "7y − 3y = 4y اور 9 − 4 = 5: 4y + 5"),
     common_wrong=[wrong("4y + 13", "The 4 is taken away too: 9 − 4 = 5. 4y + 5.", "4 بھی تفریق ہوتا ہے: 9 − 4 = 5۔ 4y + 5", "first_term_only")]),
   expression_question(
     "s8_negative",
     T("Simplify (5p − 2) − (p − 6).", "(5p − 2) − (p − 6) کو مختصر کریں۔"),
     S8,
     T("−(p − 6) = −p + 6: taking away −6 adds 6.", "−(p − 6) = −p + 6: −6 تفریق کرنے سے 6 جمع ہوتا ہے۔"),
     T(f"Right! {show(S8)}.", f"درست! {show(S8)}"),
     T("5p − p = 4p and −2 + 6 = 4: 4p + 4.", "5p − p = 4p اور −2 + 6 = 4: 4p + 4"),
     common_wrong=[wrong("4p - 8", "−(−6) is +6, so −2 + 6 = 4: 4p + 4.", "−(−6) یعنی +6، تو −2 + 6 = 4: 4p + 4", "first_term_only")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Sana writes (8n + 3) − (5n + 2) = 3n + 5. What is wrong?", "ثنا لکھتی ہے (8n + 3) − (5n + 2) = 3n + 5۔ کیا غلطی ہے؟"),
    "options": [
      opt("both_signs", "She added the 2. Take it away: 3 − 2 = 1, so 3n + 1.", "اس نے 2 جمع کر دیا۔ اسے تفریق کریں: 3 − 2 = 1، تو 3n + 1", True,
          "Yes! The minus takes away the whole bracket.", "جی ہاں! منفی پوری بریکٹ تفریق کرتا ہے۔"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "−(5n + 2) = −5n − 2. 3 − 2 = 1: 3n + 1.", "−(5n + 2) = −5n − 2۔ 3 − 2 = 1: 3n + 1", "first_term_only"),
      opt("n_wrong", "The n part is wrong: it should be 13n.", "n والا حصہ غلط ہے: 13n ہونا چاہیے۔", False,
          "8n − 5n = 3n is right. The mistake is +2; it should be −2: 3n + 1.", "8n − 5n = 3n ٹھیک ہے۔ غلطی +2 میں ہے؛ −2 ہونا چاہیے: 3n + 1"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why does −(2x + 1) turn the + 1 into − 1? It wasn't next to the minus! Help me.",
                     "−(2x + 1) میں + 1، − 1 کیوں بن جاتا ہے؟ یہ تو منفی کے ساتھ نہیں تھا! میری مدد کریں۔"),
    "task": T("Explain why (5x + 4) − (2x + 1) is 3x + 3 and not 3x + 5.", "بتائیں کہ (5x + 4) − (2x + 1) کا جواب 3x + 3 کیوں ہے، 3x + 5 کیوں نہیں۔"),
    "key_idea": "The minus sign takes away the whole bracket, both 2x and 1. So −(2x + 1) = −2x − 1. Then 5x − 2x = 3x and 4 − 1 = 3, giving 3x + 3. 3x + 5 comes from taking away only 2x and adding the 1.",
    "levels": {
      "got_it": "Says the whole bracket is taken away (−2x − 1), so 4 − 1 = 3, giving 3x + 3.",
      "partly": "Gets 3x + 3 but doesn't say why the 1 is subtracted.",
      "not_yet": "Gives no reason."},
    "keywords": [
      ["whole", "both", "everything", "پوری", "دونوں"],
      ["-1", "− 1", "minus 1", "take away 1", "1 تفریق"],
      ["3x + 3", "3x+3"],
      ["bracket", "بریکٹ"]],
    "fallback_feedback": {
      "got_it": T("Well explained! The whole bracket goes, so − 1.", "بہت خوب! پوری بریکٹ تفریق، تو − 1"),
      "partly": T("Good start! Why is the 1 taken away and not added?", "اچھی شروعات! 1 تفریق کیوں ہوتا ہے، جمع کیوں نہیں؟"),
      "not_yet": T("If you give away (2 mangoes + 1 banana), do you give the banana too?", "اگر آپ (2 آم + 1 کیلا) دیں، تو کیا کیلا بھی دیں گے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   expression_question(
     "s11_perimeter",
     T("A triangle has sides x + 2, 2x + 1 and 3x. Write its perimeter as simply as you can.", "ایک مثلث کے اضلاع x + 2، 2x + 1 اور 3x ہیں۔ اس کا احاطہ جتنا مختصر ہو سکے لکھیں۔"),
     S11,
     T("Add all three sides: x terms, then numbers.", "تینوں اضلاع جمع کریں: پہلے x والے، پھر اعداد۔"),
     T(f"Right! {show(S11)}.", f"درست! {show(S11)}"),
     T("x + 2x + 3x = 6x and 2 + 1 = 3: 6x + 3.", "x + 2x + 3x = 6x اور 2 + 1 = 3: 6x + 3"),
     common_wrong=[wrong("5x + 3", "x means 1x: 1 + 2 + 3 = 6. 6x + 3.", "x یعنی 1x: 1 + 2 + 3 = 6۔ 6x + 3", "lone_letter_zero"),
                   wrong("9x", "6x and 3 are unlike terms: 6x + 3.", "6x اور 3 غیر یکساں ہیں: 6x + 3", "unlike_joined")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Brackets don't scare you now. Collect, and watch the minus signs!", "اب بریکٹ سے ڈر نہیں لگتا۔ جمع کریں، اور منفی علامات کا دھیان رکھیں!"),
    "text": T("To add expressions, remove the brackets and collect like terms. To subtract, change the sign of every term in the bracket being taken away, then collect. Unlike terms stay apart, and a lone letter means 1 of it.",
              "عبارتیں جمع کرنے کے لیے بریکٹ ہٹائیں اور یکساں ارکان جمع کریں۔ تفریق کے لیے تفریق ہونے والی بریکٹ کے ہر رکن کی علامت بدلیں، پھر جمع کریں۔ غیر یکساں ارکان الگ رہتے ہیں، اور اکیلا حرف یعنی اس کا 1۔"),
    "points": [T("−(a + b) = −a − b", "−(a + b) = −a − b"),
               T("Collect like terms only.", "صرف یکساں ارکان جمع کریں۔")]},
 ],
 "review_questions": [
   {"id": "r_add", "type": "apply", "skill": SKILL, "step": expression_question(
     "r_add",
     T("Simplify (3x + 2y) + (x + 5y).", "(3x + 2y) + (x + 5y) کو مختصر کریں۔"),
     R1,
     T("x means 1x.", "x یعنی 1x"),
     T(f"Right! {show(R1)}.", f"درست! {show(R1)}"),
     T("3x + x = 4x and 2y + 5y = 7y: 4x + 7y.", "3x + x = 4x اور 2y + 5y = 7y: 4x + 7y"),
     common_wrong=[wrong("3x + 7y", "Don't lose the lone x: 3x + x = 4x.", "اکیلا x نہ کھوئیں: 3x + x = 4x", "lone_letter_zero")],
     qtype=None)},
   {"id": "r_subtract", "type": "apply", "skill": SKILL, "step": expression_question(
     "r_subtract",
     T("Simplify (10m + 6) − (3m + 4).", "(10m + 6) − (3m + 4) کو مختصر کریں۔"),
     R2,
     T("Take away 3m and take away 4.", "3m تفریق کریں اور 4 بھی۔"),
     T(f"Right! {show(R2)}.", f"درست! {show(R2)}"),
     T("10m − 3m = 7m and 6 − 4 = 2: 7m + 2.", "10m − 3m = 7m اور 6 − 4 = 2: 7m + 2"),
     common_wrong=[wrong("7m + 10", "The 4 is taken away too: 6 − 4 = 2. 7m + 2.", "4 بھی تفریق ہوتا ہے: 6 − 4 = 2۔ 7m + 2", "first_term_only")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh after matching the app with PCTB Mathematics 6 (Sub-domain 6, addition and subtraction of expressions). No textbook text or exercises were used.",
   "Typed answers accept the terms in any order (5x + 6 or 6 + 5x); spaces don't matter.",
   "Urdu terms to check: عبارت (expression), یکساں ارکان (like terms), بریکٹ / قوسین (bracket), مختصر کرنا (simplify).",
   "The numbers were worked out in content/sources/g6-maths-07/adding_subtracting_expressions.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)
