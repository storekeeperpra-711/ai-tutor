from common import (T, opt, say, wrong, number_question, write, show,
                    REF, REVIEW, SET_MEANING, SET_KINDS)

SKILL = SET_KINDS


def primes_below(n):
    return {p for p in range(2, n) if all(p % d for d in range(2, p))}


# s2: elements of {2, 4, 6, 8}
S2 = len({2, 4, 6, 8})
assert S2 == 4
# s4: months with 32 days -> empty
S4 = 0
# s6: {1, 2, 3} and {3, 1, 2} are equal
assert {1, 2, 3} == {3, 1, 2}
# s7: {a, b, c} and {1, 2, 3}: equivalent, not equal
assert len({"a", "b", "c"}) == len({1, 2, 3}) and {"a", "b", "c"} != {1, 2, 3}
# s8: primes less than 20
P20 = primes_below(20)
S8 = len(P20)
assert P20 == {2, 3, 5, 7, 11, 13, 17, 19} and S8 == 8
# s9: {0} has one element
assert len({0}) == 1
# s11: even primes
S11 = len({p for p in primes_below(100) if p % 2 == 0})
assert S11 == 1
# question bank and review
QB = len({n for n in range(1, 30) if n % 5 == 0})
assert QB == 5
R1 = len({n for n in range(0, 1)})
assert R1 == 1
R2 = len({n for n in range(11, 20) if n % 2 == 0})
assert R2 == 4

lesson = {
 "id": "g6-maths-01-kinds-of-sets",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Recognise empty, finite and infinite sets, and tell equal sets from equivalent sets.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Kinds of sets", "سیٹوں کی اقسام"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": SET_MEANING}],
 "misconceptions": [
   {"id": "zero_is_empty", "description": "Thinks {0} is the empty set, though it has one element."},
   {"id": "equal_equivalent", "description": "Mixes up equal sets (same elements) and equivalent sets (same number of elements)."},
   {"id": "big_is_infinite", "description": "Thinks a large set that can be counted is infinite."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_empty", "type": "recall", "step": {
     "id": "qb_empty", "type": "choice",
     "prompt": T("What is the empty set?", "خالی سیٹ کیا ہے؟"),
     "options": [
       opt("none", "A set with no elements, written { } or ∅", "ایسا سیٹ جس کا کوئی رکن نہ ہو، { } یا ∅ لکھا جاتا ہے", True,
           "Yes! It has 0 elements.", "جی ہاں! اس کے 0 رکن ہیں۔"),
       opt("zero", "The set {0}", "سیٹ {0}", False,
           "{0} has one element, the number 0. The empty set has none.", "{0} کا ایک رکن ہے، عدد 0۔ خالی سیٹ کا کوئی رکن نہیں۔", "zero_is_empty"),
       opt("small", "A set with only one element", "صرف ایک رکن والا سیٹ", False,
           "One element is not empty. The empty set has no elements.", "ایک رکن خالی نہیں۔ خالی سیٹ کا کوئی رکن نہیں۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("How many elements are in the set of multiples of 5 less than 30?", "30 سے چھوٹے 5 کے اضعاف کے سیٹ میں کتنے رکن ہیں؟"),
     QB,
     T("{5, 10, …}", "{5, 10, …}"),
     T("Right! {5, 10, 15, 20, 25} has 5.", "درست! {5, 10, 15, 20, 25} کے 5 رکن ہیں۔"),
     T("5, 10, 15, 20, 25: 5 elements. 30 is not less than 30.", "5، 10، 15، 20، 25: پانچ رکن۔ 30، 30 سے چھوٹا نہیں۔"),
     common_wrong=[wrong(6, "30 is not less than 30: {5, 10, 15, 20, 25} has 5.", "30، 30 سے چھوٹا نہیں: {5, 10, 15, 20, 25} کے 5 رکن ہیں۔")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Ali says {1, 2, 3} and {4, 5, 6} are equal sets. What is wrong?", "علی کہتا ہے {1, 2, 3} اور {4, 5, 6} برابر سیٹ ہیں۔ کیا غلطی ہے؟"),
     "options": [
       opt("equiv", "They have different elements, so they are only equivalent (both have 3).", "ان کے رکن مختلف ہیں، اس لیے یہ صرف ہم قوت ہیں (دونوں کے 3)۔", True,
           "Yes! Equal needs the same elements.", "جی ہاں! برابر ہونے کے لیے رکن ایک جیسے ہوں۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "Same number of elements makes them equivalent. Equal sets have the same elements.", "رکنوں کی برابر تعداد انہیں ہم قوت بناتی ہے۔ برابر سیٹوں کے رکن ایک جیسے ہوتے ہیں۔", "equal_equivalent"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_empty", "front": T("Empty set?", "خالی سیٹ؟"),
    "back": T("No elements: { } or ∅. Careful: {0} is not empty.", "کوئی رکن نہیں: { } یا ∅۔ دھیان: {0} خالی نہیں۔")},
   {"id": "f_equal", "front": T("Equal or equivalent?", "برابر یا ہم قوت؟"),
    "back": T("Equal: same elements. Equivalent: same number of elements.", "برابر: ایک جیسے رکن۔ ہم قوت: رکنوں کی برابر تعداد۔")},
 ],
 "home_tasks": [{"id": "h_kinds", "text": T(
   "Think of one empty set (like the set of cats in your house that can fly), one finite set and one infinite set. Tell someone at home which is which and why.",
   "ایک خالی سیٹ (جیسے آپ کے گھر کی اڑنے والی بلیوں کا سیٹ)، ایک محدود سیٹ اور ایک لامحدود سیٹ سوچیں۔ گھر میں کسی کو بتائیں کون سا کون سا ہے اور کیوں۔")}],
 "glossary": [T("Empty set", "خالی سیٹ"), T("Finite", "محدود"), T("Infinite", "لامحدود"), T("Equivalent", "ہم قوت")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Can a set have nothing in it? Can a set go on forever? Let's find out!",
                     "کیا سیٹ میں کچھ بھی نہ ہو؟ کیا سیٹ ہمیشہ چلتا رہے؟ آئیں معلوم کریں!"),
    "text": T("Today we learn the kinds of sets. First, a quick check.", "آج ہم سیٹوں کی اقسام سیکھیں گے۔ پہلے ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("How many elements are in {2, 4, 6, 8}?", "{2, 4, 6, 8} میں کتنے رکن ہیں؟"),
     S2,
     T("Count what is inside the braces.", "بریکٹ کے اندر گنیں۔"),
     T("Right! 4.", "درست! 4"),
     T("2, 4, 6, 8: 4 elements.", "2، 4، 6، 8: چار رکن"),
     common_wrong=[wrong(8, "8 is the largest element. Count them: 4.", "8 سب سے بڑا رکن ہے۔ انہیں گنیں: 4")],
     qtype="recall", skill=SET_MEANING),
   {"id": "s3_kinds", "type": "explain",
    "character": say("happy", "Empty, finite, infinite, equal, equivalent. Let's meet them one by one!", "خالی، محدود، لامحدود، برابر، ہم قوت۔ آئیں ایک ایک سے ملیں!"),
    "text": T("The empty set has no elements; we write { } or ∅. A finite set can be counted to the end, like the days of the week. An infinite set goes on forever, like {1, 2, 3, …}. Equal sets have exactly the same elements: {1, 2, 3} = {3, 1, 2}. Equivalent sets have the same number of elements: {a, b, c} and {1, 2, 3}.",
              "خالی سیٹ کا کوئی رکن نہیں؛ اسے { } یا ∅ لکھتے ہیں۔ محدود سیٹ آخر تک گنا جا سکتا ہے، جیسے ہفتے کے دن۔ لامحدود سیٹ ہمیشہ چلتا رہتا ہے، جیسے {1, 2, 3, …}۔ برابر سیٹوں کے رکن بالکل ایک جیسے ہوتے ہیں: {1, 2, 3} = {3, 1, 2}۔ ہم قوت سیٹوں کے رکنوں کی تعداد برابر ہوتی ہے: {a, b, c} اور {1, 2, 3}۔")},
   number_question(
     "s4_empty",
     T("How many elements are in the set of months that have 32 days?", "32 دن والے مہینوں کے سیٹ میں کتنے رکن ہیں؟"),
     S4,
     T("Does any month have 32 days?", "کیا کسی مہینے کے 32 دن ہوتے ہیں؟"),
     T("Right! None. It is the empty set.", "درست! کوئی نہیں۔ یہ خالی سیٹ ہے۔"),
     T("No month has 32 days, so the set is empty: 0 elements.", "کسی مہینے کے 32 دن نہیں، تو سیٹ خالی ہے: 0 رکن"),
     common_wrong=[wrong(12, "There are 12 months, but none has 32 days: 0.", "مہینے 12 ہیں، لیکن کسی کے 32 دن نہیں: 0"),
                   wrong(1, "Not even one month has 32 days: 0.", "ایک مہینے کے بھی 32 دن نہیں: 0")]),
   {"id": "s5_infinite", "type": "choice",
    "prompt": T("Which set is infinite?", "کون سا سیٹ لامحدود ہے؟"),
    "options": [
      opt("naturals", "{1, 2, 3, 4, …}, the counting numbers", "{1, 2, 3, 4, …}، گنتی کے اعداد", True,
          "Yes! The counting numbers never end.", "جی ہاں! گنتی کے اعداد کبھی ختم نہیں ہوتے۔"),
      opt("people", "The people living in Lahore", "لاہور میں رہنے والے لوگ", False,
          "That's a big set, but it can be counted, so it is finite.", "یہ بڑا سیٹ ہے، لیکن گنا جا سکتا ہے، اس لیے محدود ہے۔", "big_is_infinite"),
      opt("days", "The days of the week", "ہفتے کے دن", False,
          "There are only 7 days: finite.", "دن صرف 7 ہیں: محدود۔"),
    ]},
   {"id": "s6_equal", "type": "choice",
    "prompt": T("A = {1, 2, 3} and B = {3, 1, 2}. What are A and B?", "A = {1, 2, 3} اور B = {3, 1, 2}۔ A اور B کیا ہیں؟"),
    "options": [
      opt("equal", "Equal sets", "برابر سیٹ", True,
          "Yes! Same elements; the order doesn't matter.", "جی ہاں! ایک جیسے رکن؛ ترتیب اہم نہیں۔"),
      opt("different", "Different sets, because the order is different", "مختلف سیٹ، کیونکہ ترتیب مختلف ہے", False,
          "Order doesn't matter in a set. They have the same elements, so they are equal.", "سیٹ میں ترتیب اہم نہیں۔ ان کے رکن ایک جیسے ہیں، اس لیے برابر ہیں۔"),
    ]},
   {"id": "s7_equivalent", "type": "choice",
    "prompt": T("A = {a, b, c} and B = {1, 2, 3}. What are A and B?", "A = {a, b, c} اور B = {1, 2, 3}۔ A اور B کیا ہیں؟"),
    "options": [
      opt("equiv", "Equivalent, but not equal", "ہم قوت، لیکن برابر نہیں", True,
          "Yes! Both have 3 elements, but the elements are different.", "جی ہاں! دونوں کے 3 رکن ہیں، لیکن رکن مختلف ہیں۔"),
      opt("equal", "Equal", "برابر", False,
          "Equal sets need the same elements. These only have the same number.", "برابر سیٹوں کے رکن ایک جیسے ہوں۔ ان کی صرف تعداد برابر ہے۔", "equal_equivalent"),
      opt("neither", "Neither", "کوئی بھی نہیں", False,
          "Both have 3 elements, so they are equivalent.", "دونوں کے 3 رکن ہیں، اس لیے ہم قوت ہیں۔"),
    ]},
   number_question(
     "s8_primes",
     T("How many elements are in the set of prime numbers less than 20?", "20 سے چھوٹے مفرد اعداد کے سیٹ میں کتنے رکن ہیں؟"),
     S8,
     T("2, 3, 5, 7, … keep going up to 19.", "2، 3، 5، 7، … 19 تک جاری رکھیں۔"),
     T(f"Right! {show(P20)} has 8 elements. It is finite.", f"درست! {show(P20)} کے 8 رکن ہیں۔ یہ محدود ہے۔"),
     T(f"{show(P20)}: 8 elements.", f"{show(P20)}: آٹھ رکن"),
     common_wrong=[wrong(9, "1 is not a prime number: 8 elements.", "1 مفرد عدد نہیں ہے: 8 رکن"),
                   wrong(7, "Count again, including 2: 2, 3, 5, 7, 11, 13, 17, 19 is 8.", "2 سمیت دوبارہ گنیں: 2، 3، 5، 7، 11، 13، 17، 19 یعنی 8")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Hina says {0} is the empty set. What went wrong?", "حنا کہتی ہے {0} خالی سیٹ ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("one", "{0} has one element, the number 0, so it is not empty.", "{0} کا ایک رکن ہے، عدد 0، اس لیے یہ خالی نہیں۔", True,
          "Yes! The empty set is { }, with nothing inside.", "جی ہاں! خالی سیٹ { } ہے، جس کے اندر کچھ نہیں۔"),
      opt("nothing", "Nothing, 0 means nothing.", "کوئی غلطی نہیں، 0 کا مطلب کچھ نہیں۔", False,
          "0 is a number, and here it is inside the set. So {0} has one element.", "0 ایک عدد ہے، اور یہاں سیٹ کے اندر ہے۔ تو {0} کا ایک رکن ہے۔", "zero_is_empty"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Equal sets are always equivalent, but equivalent sets are not always equal. Why? Can you teach me?",
                     "برابر سیٹ ہمیشہ ہم قوت ہوتے ہیں، لیکن ہم قوت سیٹ ہمیشہ برابر نہیں۔ کیوں؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why are equal sets always equivalent, but equivalent sets not always equal?", "اپنے الفاظ میں بتائیں: برابر سیٹ ہمیشہ ہم قوت کیوں ہوتے ہیں، لیکن ہم قوت سیٹ ہمیشہ برابر کیوں نہیں؟"),
    "key_idea": "Equal sets have exactly the same elements, so they must have the same number of elements (equivalent). But two sets can have the same number of elements with different elements, like {a, b, c} and {1, 2, 3}, so equivalent sets need not be equal.",
    "levels": {
      "got_it": "Says equal means same elements (so same number), while equivalent only means same number, and gives or describes an example of different elements.",
      "partly": "Explains one direction only.",
      "not_yet": "Gives no reason."},
    "keywords": [
      ["same elements", "same members", "ایک جیسے رکن"],
      ["same number", "how many", "تعداد", "برابر تعداد"],
      ["different", "example", "مختلف", "مثال"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Same elements means same number, but not the other way round.", "بہت خوب! ایک جیسے رکن کا مطلب برابر تعداد ہے، لیکن الٹا نہیں۔"),
      "partly": T("Good start! Now explain the other direction, with an example.", "اچھی شروعات! اب دوسری طرف بھی مثال سے سمجھائیں۔"),
      "not_yet": T("Look at {a, b, c} and {1, 2, 3}. Do they have the same number of elements? The same elements?", "{a, b, c} اور {1, 2, 3} دیکھیں۔ کیا ان کے رکنوں کی تعداد برابر ہے؟ کیا رکن ایک جیسے ہیں؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_even_primes",
     T("How many elements are in the set of even prime numbers?", "جفت مفرد اعداد کے سیٹ میں کتنے رکن ہیں؟"),
     S11,
     T("Every even number above 2 can be divided by 2.", "2 سے بڑا ہر جفت عدد 2 سے تقسیم ہوتا ہے۔"),
     T("Right! Only {2}: 1 element.", "درست! صرف {2}: ایک رکن"),
     T("2 is the only even prime, so the set is {2}: 1 element.", "2 واحد جفت مفرد عدد ہے، تو سیٹ {2} ہے: ایک رکن"),
     common_wrong=[wrong(0, "2 is even and prime! The set is {2}: 1 element.", "2 جفت بھی ہے اور مفرد بھی! سیٹ {2} ہے: ایک رکن")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "You know five kinds of sets now!", "اب آپ سیٹوں کی پانچ قسمیں جانتے ہیں!"),
    "text": T("Empty set: no elements, { } or ∅ (but {0} has one element). Finite: can be counted to the end. Infinite: goes on forever. Equal sets: the same elements, in any order. Equivalent sets: the same number of elements.",
              "خالی سیٹ: کوئی رکن نہیں، { } یا ∅ (لیکن {0} کا ایک رکن ہے)۔ محدود: آخر تک گنا جا سکتا ہے۔ لامحدود: ہمیشہ چلتا رہتا ہے۔ برابر سیٹ: ایک جیسے رکن، کسی بھی ترتیب میں۔ ہم قوت سیٹ: رکنوں کی برابر تعداد۔"),
    "points": [T("Equal: same elements.", "برابر: ایک جیسے رکن۔"),
               T("Equivalent: same number of elements.", "ہم قوت: رکنوں کی برابر تعداد۔")]},
 ],
 "review_questions": [
   {"id": "r_zero", "type": "apply", "skill": SKILL, "step": number_question(
     "r_zero",
     T("How many elements are in the set of whole numbers less than 1?", "1 سے چھوٹے مکمل اعداد کے سیٹ میں کتنے رکن ہیں؟"),
     R1,
     T("Whole numbers start at 0.", "مکمل اعداد 0 سے شروع ہوتے ہیں۔"),
     T("Right! {0}: 1 element.", "درست! {0}: ایک رکن"),
     T("The set is {0}, which has 1 element.", "سیٹ {0} ہے، جس کا ایک رکن ہے۔"),
     common_wrong=[wrong(0, "0 is a whole number less than 1. The set is {0}: 1 element.", "0، 1 سے چھوٹا مکمل عدد ہے۔ سیٹ {0} ہے: ایک رکن", "zero_is_empty")],
     qtype=None)},
   {"id": "r_evens", "type": "apply", "skill": SKILL, "step": number_question(
     "r_evens",
     T("How many elements are in the set of even numbers between 10 and 20?", "10 اور 20 کے درمیان جفت اعداد کے سیٹ میں کتنے رکن ہیں؟"),
     R2,
     T("Between: don't count 10 or 20.", "درمیان: 10 یا 20 نہ گنیں۔"),
     T("Right! {12, 14, 16, 18}: 4.", "درست! {12, 14, 16, 18}: چار"),
     T("12, 14, 16, 18: 4 elements.", "12، 14، 16، 18: چار رکن"),
     common_wrong=[wrong(6, "\"Between\" leaves out 10 and 20: {12, 14, 16, 18}, 4 elements.", "\"درمیان\" میں 10 اور 20 شامل نہیں: {12, 14, 16, 18}، چار رکن")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Sets unit. No textbook text or exercises were used.",
   "\"Between\" is used to mean the end numbers are left out; the hints say so where it matters.",
   "Urdu terms to check: خالی سیٹ (empty set), محدود (finite), لامحدود (infinite), ہم قوت (equivalent), مفرد (prime).",
   "The numbers were worked out in content/sources/g6-maths-01/kinds_of_sets.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
# ---------- pictures ----------
from figs import (attach, figure, set_oval, two_ovals, oval_figure, number_line, number_grid,
                  label, line, arrow_right, en_list, ur_list, W)

EQ_A, EQ_B = [1, 2, 3], [3, 1, 2]            # s3, s6: equal sets
assert set(EQ_A) == set(EQ_B)
EV_A, EV_B = ["a", "b", "c"], [1, 2, 3]      # s3, s7: equivalent sets
assert len(EV_A) == len(EV_B) and set(EV_A) != set(EV_B)
QB_A, QB_B = [1, 2, 3], [4, 5, 6]            # qb_find_error
assert len(QB_A) == len(QB_B) and set(QB_A) != set(QB_B)
ZERO = [0]
assert len(set(ZERO)) == 1


def hook():
    """An empty oval on the left; a number line 1, 2, 3, 4, 5 with an
    arrow (it goes on forever) on the right."""
    items, rx, ry = set_oval(56, 46, [], rx=36, ry=28)
    items.append(label((56, 92), "{ }"))
    x0, gap = 130, 30
    for i in range(5):
        items += [line((x0 + i * gap, 41), (x0 + i * gap, 51)), label((x0 + i * gap, 66), i + 1)]
    items.append(line((x0 - 8, 46), (x0 + 4 * gap + 10, 46)))
    items += arrow_right(x0 + 4 * gap + 10, W - 14, 46)
    return figure(W, 106,
        "Left: an empty oval with { } written under it, a set with nothing in it. Right: a number line with 1, 2, 3, 4 and 5 that goes on with an arrow, because the counting numbers never end.",
        "بائیں: ایک خالی بیضوی شکل جس کے نیچے { } لکھا ہے، ایسا سیٹ جس میں کچھ نہیں۔ دائیں: ایک عددی لکیر جس پر 1، 2، 3، 4 اور 5 ہیں اور تیر کے ساتھ آگے چلتی جاتی ہے، کیونکہ گنتی کے اعداد کبھی ختم نہیں ہوتے۔",
        items)


def summary():
    """An empty oval, then two equal sets with '=' between them."""
    items, _, _ = set_oval(38, 52, [], rx=24, ry=24)
    items.append(label((38, 94), "{ }"))
    for cx, elems, name in ((128, EQ_A, "A"), (248, EQ_B, "B")):
        part, _, _ = set_oval(cx, 52, elems, name=name, rx=40, ry=26, cols=3, dx=22)
        items += part
    items.append(label((188, 52), "="))
    return figure(W, 108,
        f"Left: an empty oval with {{ }} under it, the empty set. Right: oval A holding {en_list(EQ_A)} and oval B holding {en_list(EQ_B)}, with an equals sign between them: the same elements in a different order, so A and B are equal.",
        f"بائیں: ایک خالی بیضوی شکل جس کے نیچے {{ }} ہے، یعنی خالی سیٹ۔ دائیں: بیضوی شکل A میں {ur_list(EQ_A)} اور بیضوی شکل B میں {ur_list(EQ_B)}، درمیان میں برابر کا نشان: رکن وہی ہیں، ترتیب مختلف، اس لیے A اور B برابر ہیں۔",
        items)


def pair(a, b, en_extra="", ur_extra="", **kw):
    return two_ovals(a, b,
        f"Two ovals: A holds {en_list(a)} and B holds {en_list(b)}.{en_extra}",
        f"دو بیضوی شکلیں: A میں {ur_list(a)} اور B میں {ur_list(b)} ہیں۔{ur_extra}", **kw)


attach(lesson, {
    "s1_hook": hook(),
    "s3_kinds": pair(EV_A, EV_B,
        " A line joins a to 1, b to 2 and c to 3, so every element has exactly one partner: the sets are equivalent.",
        " ایک لکیر a کو 1 سے، b کو 2 سے اور c کو 3 سے ملاتی ہے، یوں ہر رکن کا ٹھیک ایک ساتھی ہے: سیٹ ہم قوت ہیں۔",
        match=True),
    "s6_equal": pair(EQ_A, EQ_B, cols=3),
    "s7_equivalent": pair(EV_A, EV_B, cols=3),
    "s8_primes": number_grid(1, 19,
        "The numbers 1 to 19 in boxes, 1 to 10 in the top row and 11 to 19 in the bottom row.",
        "خانوں میں 1 سے 19 تک اعداد، اوپر والی قطار میں 1 سے 10 اور نیچے والی میں 11 سے 19۔"),
    "s9_find_error": oval_figure(ZERO,
        "An oval with the number 0 written inside it: the set {0}.",
        "ایک بیضوی شکل جس کے اندر عدد 0 لکھا ہے: سیٹ {0}۔"),
    "s12_summary": summary(),
    "qb_find_error": pair(QB_A, QB_B, cols=3),
    "r_zero": number_line(0, 6,
        "A number line of whole numbers starting at 0: 0, 1, 2, 3, 4, 5, 6, going on with an arrow.",
        "مکمل اعداد کی عددی لکیر جو 0 سے شروع ہوتی ہے: 0، 1، 2، 3، 4، 5، 6، اور تیر کے ساتھ آگے چلتی ہے۔", arrow=True),
    "r_evens": number_line(10, 20,
        "A number line with the whole numbers from 10 to 20 written under it.",
        "ایک عددی لکیر جس کے نیچے 10 سے 20 تک کے مکمل اعداد لکھے ہیں۔"),
})
write(lesson)
