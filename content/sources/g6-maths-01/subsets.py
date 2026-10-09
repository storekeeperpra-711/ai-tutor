from itertools import combinations

from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, SET_KINDS, SET_SUBSETS)

SKILL = SET_SUBSETS


def subsets(s):
    s = list(s)
    return [set(c) for r in range(len(s) + 1) for c in combinations(s, r)]


# s2: a set equivalent to {1, 2, 3} has 3 elements
S2 = len({1, 2, 3})
assert S2 == 3
# s4: subsets of {1, 2, 3, 4, 5}
B4 = {1, 2, 3, 4, 5}
assert {2, 4} <= B4 and not {4, 6} <= B4 and not {0, 1} <= B4
# s5: subsets of {a, b}
S5 = len(subsets("ab"))
assert S5 == 4
# s6: subsets of {p, q, r}
S6 = len(subsets("pqr"))
assert S6 == 8
# s7: proper subsets of {p, q, r}
S7 = len([s for s in subsets("pqr") if s != set("pqr")])
assert S7 == 7
# s8: the empty set is a subset of every set
assert set() <= {5, 6}
# s9: subsets of {1, 2}: { }, {1}, {2}, {1, 2}
assert len(subsets({1, 2})) == 4
# s11: subsets of a 4-element set
S11 = len(subsets(["red", "green", "blue", "yellow"]))
assert S11 == 16
# question bank and review
QB = len([s for s in subsets({1, 2, 3}) if len(s) == 2])
assert QB == 3
assert not {3} <= {1, 2}
R1 = len(subsets("mn"))
assert R1 == 4
R2 = len([s for s in subsets("ab") if s != set("ab")])
assert R2 == 3

lesson = {
 "id": "g6-maths-01-subsets",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Recognise subsets and proper subsets, and list or count all the subsets of a small set.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Subsets", "ذیلی سیٹ"),
 "estimated_minutes": 15,
 "prerequisites": [{"skill": SET_KINDS}],
 "misconceptions": [
   {"id": "forgets_empty_self", "description": "Leaves out the empty set or the set itself when listing subsets."},
   {"id": "extra_element", "description": "Thinks a set is a subset even when one of its elements is not in the bigger set."},
   {"id": "proper_includes_self", "description": "Counts the set itself as a proper subset."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_meaning", "type": "recall", "step": {
     "id": "qb_meaning", "type": "choice",
     "prompt": T("What does A ⊆ B mean?", "A ⊆ B کا کیا مطلب ہے؟"),
     "options": [
       opt("every", "Every element of A is also in B", "A کا ہر رکن B میں بھی ہے", True,
           "Yes! A is a subset of B.", "جی ہاں! A، B کا ذیلی سیٹ ہے۔"),
       opt("some", "Some elements of A are in B", "A کے کچھ رکن B میں ہیں", False,
           "Every element of A must be in B, not just some.", "A کا ہر رکن B میں ہونا چاہیے، صرف کچھ نہیں۔", "extra_element"),
       opt("bigger", "A has more elements than B", "A کے رکن B سے زیادہ ہیں", False,
           "A subset can't have more elements. Every element of A is in B.", "ذیلی سیٹ کے رکن زیادہ نہیں ہو سکتے۔ A کا ہر رکن B میں ہے۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("How many subsets of {1, 2, 3} have exactly 2 elements?", "{1, 2, 3} کے کتنے ذیلی سیٹ میں بالکل 2 رکن ہیں؟"),
     QB,
     T("List the pairs: {1, 2}, …", "جوڑے لکھیں: {1, 2}، …"),
     T("Right! {1, 2}, {1, 3} and {2, 3}.", "درست! {1, 2}، {1, 3} اور {2, 3}"),
     T("{1, 2}, {1, 3}, {2, 3}: 3 subsets.", "{1, 2}، {1, 3}، {2, 3}: تین ذیلی سیٹ"),
     common_wrong=[wrong(8, "8 is all the subsets. Only 3 have exactly 2 elements.", "8 تو تمام ذیلی سیٹ ہیں۔ صرف 3 میں بالکل 2 رکن ہیں۔")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Sara says {3} ⊆ {1, 2}. What is wrong?", "سارہ کہتی ہے {3} ⊆ {1, 2}۔ کیا غلطی ہے؟"),
     "options": [
       opt("not_in", "3 is not an element of {1, 2}, so {3} is not a subset.", "3، {1, 2} کا رکن نہیں، اس لیے {3} ذیلی سیٹ نہیں۔", True,
           "Yes! Every element must be in the bigger set.", "جی ہاں! ہر رکن بڑے سیٹ میں ہونا چاہیے۔"),
       opt("nothing", "Nothing, {3} is smaller.", "کوئی غلطی نہیں، {3} چھوٹا ہے۔", False,
           "Being smaller isn't enough. 3 is not in {1, 2}.", "چھوٹا ہونا کافی نہیں۔ 3، {1, 2} میں نہیں ہے۔", "extra_element"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_subset", "front": T("A ⊆ B?", "A ⊆ B؟"),
    "back": T("Every element of A is in B. { } and B itself are always subsets of B.", "A کا ہر رکن B میں ہے۔ { } اور خود B ہمیشہ B کے ذیلی سیٹ ہیں۔")},
   {"id": "f_count", "front": T("How many subsets?", "کتنے ذیلی سیٹ؟"),
    "back": T("1 element: 2. 2 elements: 4. 3 elements: 8. Each new element doubles it.", "1 رکن: 2۔ 2 رکن: 4۔ 3 رکن: 8۔ ہر نیا رکن دگنا کر دیتا ہے۔")},
 ],
 "home_tasks": [{"id": "h_fruit", "text": T(
   "Put three different fruits (or three spoons, cups or pebbles) on a table. How many different ways can you choose some of them, including choosing none and choosing all three? Check that you get 8.",
   "میز پر تین مختلف پھل (یا تین چمچ، کپ یا کنکر) رکھیں۔ ان میں سے کچھ چننے کے کتنے طریقے ہیں، کچھ نہ چننا اور تینوں چننا بھی شامل؟ دیکھیں کیا 8 آتے ہیں۔")}],
 "glossary": [T("Subset", "ذیلی سیٹ"), T("Proper subset", "حقیقی ذیلی سیٹ"), T("Empty set", "خالی سیٹ"), T("Element", "رکن")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "From a box of 3 sweets, how many different handfuls could you take, if taking none counts too?",
                     "3 ٹافیوں کے ڈبے سے کتنی مختلف مٹھیاں لے سکتے ہیں، اگر کچھ نہ لینا بھی گنا جائے؟"),
    "text": T("Today we learn about subsets. First, a quick check.", "آج ہم ذیلی سیٹ کے بارے میں سیکھیں گے۔ پہلے ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("A = {1, 2, 3}. How many elements does a set equivalent to A have?", "A = {1, 2, 3}۔ A کے ہم قوت سیٹ کے کتنے رکن ہوں گے؟"),
     S2,
     T("Equivalent means the same number of elements.", "ہم قوت یعنی رکنوں کی برابر تعداد۔"),
     T("Right! 3.", "درست! 3"),
     T("A has 3 elements, so any equivalent set has 3.", "A کے 3 رکن ہیں، تو ہر ہم قوت سیٹ کے بھی 3 ہوں گے۔"),
     common_wrong=[wrong(6, "Equivalent means the same number of elements as A: 3.", "ہم قوت یعنی A جتنے رکن: 3")],
     qtype="recall", skill=SET_KINDS),
   {"id": "s3_subsets", "type": "explain",
    "character": say("happy", "A subset is a set made only from things in the bigger set!", "ذیلی سیٹ وہ سیٹ ہے جو صرف بڑے سیٹ کی چیزوں سے بنے!"),
    "text": T("A is a subset of B (A ⊆ B) if every element of A is also in B. The empty set { } is a subset of every set, and every set is a subset of itself. A proper subset (⊂) is any subset except the set itself. The subsets of {a, b} are { }, {a}, {b} and {a, b}: 4 of them. Each new element doubles the number: 2, 4, 8, 16, …",
              "A، B کا ذیلی سیٹ ہے (A ⊆ B) اگر A کا ہر رکن B میں بھی ہو۔ خالی سیٹ { } ہر سیٹ کا ذیلی سیٹ ہے، اور ہر سیٹ خود اپنا ذیلی سیٹ ہے۔ حقیقی ذیلی سیٹ (⊂) خود سیٹ کے علاوہ ہر ذیلی سیٹ ہے۔ {a, b} کے ذیلی سیٹ { }، {a}، {b} اور {a, b} ہیں: کل 4۔ ہر نیا رکن تعداد دگنی کر دیتا ہے: 2، 4، 8، 16، …")},
   {"id": "s4_which", "type": "choice",
    "prompt": T("B = {1, 2, 3, 4, 5}. Which is a subset of B?", "B = {1, 2, 3, 4, 5}۔ کون سا B کا ذیلی سیٹ ہے؟"),
    "options": [
      opt("two_four", "{2, 4}", "{2, 4}", True, "Yes! 2 and 4 are both in B.", "جی ہاں! 2 اور 4 دونوں B میں ہیں۔"),
      opt("four_six", "{4, 6}", "{4, 6}", False, "6 is not in B, so {4, 6} is not a subset.", "6، B میں نہیں، اس لیے {4, 6} ذیلی سیٹ نہیں۔", "extra_element"),
      opt("zero_one", "{0, 1}", "{0, 1}", False, "0 is not in B, so {0, 1} is not a subset.", "0، B میں نہیں، اس لیے {0, 1} ذیلی سیٹ نہیں۔", "extra_element"),
    ]},
   number_question(
     "s5_two",
     T("How many subsets does {a, b} have?", "{a, b} کے کتنے ذیلی سیٹ ہیں؟"),
     S5,
     T("Don't forget { } and {a, b} itself.", "{ } اور خود {a, b} کو نہ بھولیں۔"),
     T("Right! { }, {a}, {b}, {a, b}.", "درست! { }، {a}، {b}، {a, b}"),
     T("{ }, {a}, {b}, {a, b}: 4 subsets.", "{ }، {a}، {b}، {a, b}: چار ذیلی سیٹ"),
     common_wrong=[wrong(2, "{a} and {b} are two, but { } and {a, b} count too: 4.", "{a} اور {b} دو ہیں، لیکن { } اور {a, b} بھی گنے جاتے ہیں: 4", "forgets_empty_self"),
                   wrong(3, "Count the empty set too: { }, {a}, {b}, {a, b} is 4.", "خالی سیٹ بھی گنیں: { }، {a}، {b}، {a, b} یعنی 4", "forgets_empty_self")]),
   number_question(
     "s6_three",
     T("How many subsets does {p, q, r} have?", "{p, q, r} کے کتنے ذیلی سیٹ ہیں؟"),
     S6,
     T("{a, b} had 4. One more element doubles it.", "{a, b} کے 4 تھے۔ ایک اور رکن اسے دگنا کر دیتا ہے۔"),
     T("Right! 8 subsets.", "درست! 8 ذیلی سیٹ"),
     T("{ }, {p}, {q}, {r}, {p, q}, {p, r}, {q, r}, {p, q, r}: 8.", "{ }، {p}، {q}، {r}، {p, q}، {p, r}، {q, r}، {p, q, r}: آٹھ"),
     common_wrong=[wrong(6, "Add { } and {p, q, r} itself: 8.", "{ } اور خود {p, q, r} شامل کریں: 8", "forgets_empty_self"),
                   wrong(7, "Count the empty set too: 8.", "خالی سیٹ بھی گنیں: 8", "forgets_empty_self")]),
   number_question(
     "s7_proper",
     T("How many proper subsets does {p, q, r} have?", "{p, q, r} کے کتنے حقیقی ذیلی سیٹ ہیں؟"),
     S7,
     T("All the subsets except {p, q, r} itself.", "خود {p, q, r} کے علاوہ تمام ذیلی سیٹ۔"),
     T("Right! 8 − 1 = 7.", "درست! 8 − 1 = 7"),
     T("8 subsets, minus the set itself: 7.", "8 ذیلی سیٹ، خود سیٹ نکال کر: 7"),
     common_wrong=[wrong(8, "A proper subset can't be the set itself: 8 − 1 = 7.", "حقیقی ذیلی سیٹ خود سیٹ نہیں ہو سکتا: 8 − 1 = 7", "proper_includes_self"),
                   wrong(6, "The empty set is a proper subset too: 7.", "خالی سیٹ بھی حقیقی ذیلی سیٹ ہے: 7", "forgets_empty_self")]),
   {"id": "s8_empty", "type": "choice",
    "prompt": T("Is { } a subset of {5, 6}?", "کیا { }، {5, 6} کا ذیلی سیٹ ہے؟"),
    "options": [
      opt("yes", "Yes, the empty set is a subset of every set", "جی ہاں، خالی سیٹ ہر سیٹ کا ذیلی سیٹ ہے", True,
          "Yes! It has no element that is missing from {5, 6}.", "جی ہاں! اس کا کوئی ایسا رکن نہیں جو {5, 6} میں نہ ہو۔"),
      opt("no", "No, it has nothing in it", "نہیں، اس میں کچھ نہیں", False,
          "It has no element outside {5, 6}, so it is a subset.", "اس کا کوئی رکن {5, 6} سے باہر نہیں، اس لیے یہ ذیلی سیٹ ہے۔", "forgets_empty_self"),
    ]},
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Sana lists the subsets of {1, 2} as {1} and {2}, and says there are 2. What went wrong?", "ثنا {1, 2} کے ذیلی سیٹ {1} اور {2} لکھتی ہے، اور کہتی ہے یہ 2 ہیں۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("missing", "She left out { } and {1, 2}. There are 4.", "اس نے { } اور {1, 2} چھوڑ دیے۔ یہ 4 ہیں۔", True,
          "Yes! The empty set and the set itself always count.", "جی ہاں! خالی سیٹ اور خود سیٹ ہمیشہ گنے جاتے ہیں۔"),
      opt("three", "She left out {1, 2}. There are 3.", "اس نے {1, 2} چھوڑ دیا۔ یہ 3 ہیں۔", False,
          "{ } is a subset too: there are 4.", "{ } بھی ذیلی سیٹ ہے: یہ 4 ہیں۔", "forgets_empty_self"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "{ } and {1, 2} are subsets too: 4 altogether.", "{ } اور {1, 2} بھی ذیلی سیٹ ہیں: کل 4", "forgets_empty_self"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "{a, b} has 4 subsets, but {a, b, c} has 8. Why does one more element double the number? Can you teach me?",
                     "{a, b} کے 4 ذیلی سیٹ ہیں، لیکن {a, b, c} کے 8۔ ایک رکن بڑھنے سے تعداد دگنی کیوں ہو جاتی ہے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why does adding one element double the number of subsets?", "اپنے الفاظ میں بتائیں: ایک رکن بڑھانے سے ذیلی سیٹوں کی تعداد دگنی کیوں ہو جاتی ہے؟"),
    "key_idea": "Every old subset can be taken twice: once without the new element and once with it added. So each old subset gives two new ones, and the number doubles.",
    "levels": {
      "got_it": "Says each old subset appears once without the new element and once with it, so the count doubles.",
      "partly": "Says the new element can be in or out, without linking it to doubling.",
      "not_yet": "Gives no reason."},
    "keywords": [
      ["with", "without", "in or out", "ساتھ", "بغیر"],
      ["each", "every", "old", "ہر", "پرانا"],
      ["double", "twice", "two", "دگنا", "دو"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Each old subset comes once without c and once with c.", "بہت خوب! ہر پرانا ذیلی سیٹ ایک بار c کے بغیر اور ایک بار c کے ساتھ آتا ہے۔"),
      "partly": T("Good start! Now say what that means for each of the old subsets.", "اچھی شروعات! اب بتائیں ہر پرانے ذیلی سیٹ پر اس کا کیا اثر ہے۔"),
      "not_yet": T("Take the 4 subsets of {a, b}. Now make each one again with c added. How many do you have now?", "{a, b} کے 4 ذیلی سیٹ لیں۔ اب ہر ایک میں c ڈال کر دوبارہ بنائیں۔ اب کتنے ہیں؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_colours",
     T("How many subsets does {red, green, blue, yellow} have?", "{سرخ، سبز، نیلا، پیلا} کے کتنے ذیلی سیٹ ہیں؟"),
     S11,
     T("3 elements give 8. One more element doubles it.", "3 رکن سے 8 بنتے ہیں۔ ایک اور رکن اسے دگنا کر دیتا ہے۔"),
     T("Right! 16 subsets.", "درست! 16 ذیلی سیٹ"),
     T("2 × 2 × 2 × 2 = 16.", "2 × 2 × 2 × 2 = 16"),
     common_wrong=[wrong(8, "8 is for 3 elements. With 4, double it: 16.", "8 تو 3 رکن کے لیے ہے۔ 4 کے لیے دگنا کریں: 16"),
                   wrong(15, "Count the empty set too: 16.", "خالی سیٹ بھی گنیں: 16", "forgets_empty_self")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "You can find every subset now!", "اب آپ ہر ذیلی سیٹ ڈھونڈ سکتے ہیں!"),
    "text": T("A ⊆ B when every element of A is in B. The empty set and B itself are always subsets of B. Proper subsets are all of them except B itself. A set with 1, 2, 3 or 4 elements has 2, 4, 8 or 16 subsets: each new element doubles the number.",
              "A ⊆ B جب A کا ہر رکن B میں ہو۔ خالی سیٹ اور خود B ہمیشہ B کے ذیلی سیٹ ہیں۔ حقیقی ذیلی سیٹ خود B کے علاوہ سب ہیں۔ 1، 2، 3 یا 4 رکن والے سیٹ کے 2، 4، 8 یا 16 ذیلی سیٹ ہوتے ہیں: ہر نیا رکن تعداد دگنی کر دیتا ہے۔"),
    "points": [T("{ } and the set itself always count.", "{ } اور خود سیٹ ہمیشہ گنے جاتے ہیں۔"),
               T("Proper subsets: leave out the set itself.", "حقیقی ذیلی سیٹ: خود سیٹ کو چھوڑ دیں۔")]},
 ],
 "review_questions": [
   {"id": "r_mn", "type": "apply", "skill": SKILL, "step": number_question(
     "r_mn",
     T("How many subsets does {m, n} have?", "{m, n} کے کتنے ذیلی سیٹ ہیں؟"),
     R1,
     T("{ }, {m}, …", "{ }، {m}، …"),
     T("Right! 4.", "درست! 4"),
     T("{ }, {m}, {n}, {m, n}: 4.", "{ }، {m}، {n}، {m, n}: چار"),
     common_wrong=[wrong(2, "Include { } and {m, n}: 4.", "{ } اور {m, n} شامل کریں: 4", "forgets_empty_self")],
     qtype=None)},
   {"id": "r_proper", "type": "apply", "skill": SKILL, "step": number_question(
     "r_proper",
     T("How many proper subsets does {a, b} have?", "{a, b} کے کتنے حقیقی ذیلی سیٹ ہیں؟"),
     R2,
     T("All 4 subsets except {a, b} itself.", "4 ذیلی سیٹ میں سے خود {a, b} کے علاوہ۔"),
     T("Right! 3.", "درست! 3"),
     T("{ }, {a}, {b}: 3.", "{ }، {a}، {b}: تین"),
     common_wrong=[wrong(4, "A proper subset can't be {a, b} itself: 3.", "حقیقی ذیلی سیٹ خود {a, b} نہیں ہو سکتا: 3", "proper_includes_self")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Sets unit. No textbook text or exercises were used.",
   "The doubling rule (2, 4, 8, 16) is shown by pattern and by \"with or without the new element\"; the formula 2ⁿ is not needed yet.",
   "Urdu terms to check: ذیلی سیٹ (subset), حقیقی ذیلی سیٹ (proper subset).",
   "The numbers were worked out in content/sources/g6-maths-01/subsets.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
# ---------- pictures ----------
from figs import (attach, oval_figure, two_ovals, set_boxes, doubling_chain, sweets_box,
                  en_list, ur_list)

SWEETS = 3                                   # the hook: a box of 3 sweets
assert len(subsets(range(SWEETS))) == S6


def brace(s):
    """A small set as written in a box: {a, b}, or { } when empty."""
    return "{" + ", ".join(str(x) for x in sorted(s)) + "}" if s else "{ }"


AB = subsets("ab")
AB_TEXT = [brace(s) for s in AB]
assert len(AB_TEXT) == S5 and AB_TEXT == ["{ }", "{a}", "{b}", "{a, b}"]
SANA = [{1}, {2}]
assert all(s <= {1, 2} for s in SANA) and len(SANA) < len(subsets({1, 2}))
COLOURS = ["R", "G", "B", "Y"]               # red, green, blue, yellow
assert len(subsets(COLOURS)) == S11
SIZES = [1, 2, 3, 4]
assert [len(subsets(range(k))) for k in SIZES] == [2 ** k for k in SIZES] == [2, 4, 8, 16]
QB_SET = [1, 2, 3]
assert QB == len([s for s in subsets(QB_SET) if len(s) == 2])


def one(elems, name=None, en_name="", ur_name="", **kw):
    named_en = f"named {name} " if name else ""
    named_ur = f"{name} نام کی " if name else ""
    return oval_figure(list(elems),
        f"An oval {named_en}holding {en_list(list(elems))}{en_name}.",
        f"{named_ur}بیضوی شکل جس میں {ur_list(list(elems))} ہیں{ur_name}۔", name=name, **kw)


attach(lesson, {
    "s1_hook": sweets_box(SWEETS,
        f"A box holding {SWEETS} sweets, numbered 1 to {SWEETS}.",
        f"ایک ڈبہ جس میں {SWEETS} ٹافیاں ہیں، ان پر 1 سے {SWEETS} تک نمبر ہیں۔"),
    "s3_subsets": set_boxes(AB_TEXT,
        f"{len(AB_TEXT)} boxes, one for each subset of {{a, b}}: the empty set {{ }}, {{a}}, {{b}} and {{a, b}}.",
        f"{len(AB_TEXT)} خانے، {{a, b}} کے ہر ذیلی سیٹ کا ایک: خالی سیٹ {{ }}، {{a}}، {{b}} اور {{a, b}}۔"),
    "s4_which": one(sorted(B4), "B", cols=5),
    "s5_two": one("ab"),
    "s6_three": one("pqr"),
    "s9_find_error": set_boxes([brace(s) for s in SANA],
        "Sana's list: two boxes, one holding {1} and one holding {2}.",
        "ثنا کی فہرست: دو خانے، ایک میں {1} اور ایک میں {2}۔"),
    "s11_colours": one(COLOURS, en_name=": R for red, G for green, B for blue and Y for yellow",
                       ur_name=": R سرخ، G سبز، B نیلا اور Y پیلا"),
    "s12_summary": doubling_chain(SIZES,
        "Four boxes in a row joined by arrows marked ×2. Above each box are dots for the elements of a set: 1, 2, 3 and 4 dots. Inside the boxes are the numbers of subsets: 2, 4, 8 and 16.",
        "ایک قطار میں چار خانے، جنہیں ×2 والے تیر جوڑتے ہیں۔ ہر خانے کے اوپر سیٹ کے رکنوں کے نقطے ہیں: 1، 2، 3 اور 4 نقطے۔ خانوں کے اندر ذیلی سیٹوں کی تعداد ہے: 2، 4، 8 اور 16۔"),
    "qb_apply": one(QB_SET),
    "qb_find_error": two_ovals([3], [1, 2],
        "Two ovals: the left one holds 3, and the right one holds 1 and 2.",
        "دو بیضوی شکلیں: بائیں میں 3 ہے، اور دائیں میں 1 اور 2 ہیں۔", names=(None, None)),
    "r_mn": one("mn"),
    "r_proper": one("ab"),
})
write(lesson)
