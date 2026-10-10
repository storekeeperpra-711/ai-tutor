"""Practice set for Exercise 5.1 of the book: decide whether a collection is a
well-defined set, use the signs for "belongs to" and "does not belong to", and
write a set in tabular form and in descriptive form. The questions are new;
only the kinds of question follow the book."""
import calendar
from common import (T, say, nq, sq, ch, practice_lesson, practice_intro, write, show,
                    EX_SKILL, SET_MEANING)
import figs

SKILL = EX_SKILL["5.1"]


def primes_below(n):
    return {k for k in range(2, n) if all(k % d for d in range(2, k))}


# q2: months with exactly 31 days
Q2 = sum(1 for m in range(1, 13) if calendar.monthrange(2023, m)[1] == 31)
assert Q2 == 7 and sum(1 for m in range(1, 13) if calendar.monthrange(2023, m)[1] == 30) == 4
# q3: A = {3, 6, 9, 12, 15}
A3 = {3, 6, 9, 12, 15}
assert 12 in A3 and 5 not in A3 and 9 in A3 and 15 in A3
# q4: letters of LAHORE
L4 = set("LAHORE")
assert show(sorted(L4)) and "R" in L4 and "P" not in L4 and "E" in L4 and "N" not in L4
# q5: first five multiples of 4
Q5 = [4 * k for k in range(1, 6)]
assert Q5 == [4, 8, 12, 16, 20] and show([1, 2, 3, 4, 5]) != show(Q5)
# q6: distinct letters of BALLOON
Q6 = len(set("BALLOON"))
assert Q6 == 5 and len("BALLOON") == 7
# q7: natural numbers between 5 and 10
Q7 = [n for n in range(1, 100) if 5 < n < 10]
assert Q7 == [6, 7, 8, 9]
Q7_WRONG = [list(range(5, 11)), list(range(5, 10)), list(range(6, 11))]
assert all(w != Q7 for w in Q7_WRONG)
# q8: {2, 3, 5, 7} described
P8 = {2, 3, 5, 7}
assert primes_below(10) == P8 and primes_below(12) != P8 and primes_below(7) != P8
assert {n for n in range(1, 8) if n % 2} != P8 and {n for n in range(1, 8) if n % 2} == {1, 3, 5, 7}
# q9: odd numbers greater than 2 and less than 10
Q9 = [n for n in range(1, 100) if n % 2 and 2 < n < 10]
assert Q9 == [3, 5, 7, 9] and [n for n in range(1, 10) if n % 2] == [1, 3, 5, 7, 9]
# q10: letters of SEEDS
S10 = ["S", "E", "D"]
assert sorted(set("SEEDS")) == sorted(S10) and len("SEEDS") == 5
# q11: 9 is not in {1, 3, 5, 7}
assert 9 not in {1, 3, 5, 7}
# bank and review
assert len(set("COOLER")) == 5
R1 = len(set("PEPPER"))
assert R1 == 3
R2 = len([d for d in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday") if d[0] == "S"])
assert R2 == 2

lesson = practice_lesson(
 "5.1", script="exercise_5_1.py",
 title=T("Exercise 5.1 practice: writing sets", "مشق 5.1 کی پریکٹس: سیٹ لکھنا"),
 outcome="Decide whether a collection is a well-defined set, use the signs for belongs to and does not belong to, and write a set in tabular form and in descriptive form.",
 prerequisites=[SET_MEANING],
 misconceptions=[
   {"id": "opinion_is_set", "description": "Thinks a collection decided by opinion (tasty, best, tall) is a set."},
   {"id": "sign_swapped", "description": "Mixes up the signs for belongs to and does not belong to."},
   {"id": "repeated_element", "description": "Writes or counts a repeated letter or number more than once."},
   {"id": "ends_included", "description": "Includes the end numbers when the question says between."},
   {"id": "wrong_list", "description": "Lists the numbers that go with the rule (like the multipliers) instead of the numbers that fit the rule."},
   {"id": "too_wide_rule", "description": "Picks a description that fits more numbers than the set holds, or fewer."},
 ],
 steps=[
   practice_intro("5.1",
     "Here you decide whether a collection is a set, use the signs for belongs to and does not belong to, and write sets in tabular and descriptive form.",
     "اس میں آپ فیصلہ کریں گے کہ کوئی مجموعہ سیٹ ہے یا نہیں، تعلق رکھتا ہے اور تعلق نہیں رکھتا کی علامتیں استعمال کریں گے، اور سیٹ کو جدولی اور بیانیہ شکل میں لکھیں گے۔",
     "Exercise 5.1 is about writing sets. Ready?", "مشق 5.1 سیٹ لکھنے کے بارے میں ہے۔ تیار؟"),
   ch("q1_well_defined", ("Which of these collections is a set (well defined)?", "ان مجموعوں میں سے کون سا سیٹ ہے (واضح طور پر بیان کردہ)؟"),
      ("The letters of the word \"LAHORE\"", "لفظ \"LAHORE\" کے حروف", "Yes! Anyone can say for sure which letters are in it.", "جی ہاں! ہر کوئی یقین سے بتا سکتا ہے کہ اس میں کون سے حروف ہیں۔"),
      [("The tastiest fruits", "سب سے مزے دار پھل", "\"Tastiest\" is an opinion. People will not agree on the members, so it is not a set.", "\"مزے دار\" ایک رائے ہے۔ ارکان پر لوگ متفق نہیں ہوں گے، اس لیے یہ سیٹ نہیں۔", "opinion_is_set"),
       ("The tall boys of a class", "جماعت کے لمبے لڑکے", "How tall is \"tall\"? There is no fixed rule, so it is not a set.", "\"لمبا\" کتنا لمبا؟ کوئی مقررہ اصول نہیں، اس لیے یہ سیٹ نہیں۔", "opinion_is_set"),
       ("The most beautiful places in Pakistan", "پاکستان کی سب سے خوبصورت جگہیں", "Beauty is a matter of opinion, so the members are not well defined.", "خوبصورتی رائے کی بات ہے، اس لیے ارکان واضح طور پر بیان کردہ نہیں۔", "opinion_is_set")],
      1, qtype="recall"),
   nq("q2_months", ("How many months of a year have exactly 31 days? This is the number of elements in the set of such months.", "سال کے کتنے مہینوں میں پورے 31 دن ہوتے ہیں؟ یہ ایسے مہینوں کے سیٹ کے ارکان کی تعداد ہے۔"), Q2,
      ("Think: Jan, Mar, May ... Say the months and count the ones with 31 days.", "سوچیں: جنوری، مارچ، مئی ... مہینے بولیں اور 31 دن والے گنیں۔"),
      ("Right! January, March, May, July, August, October and December: 7.", "درست! جنوری، مارچ، مئی، جولائی، اگست، اکتوبر اور دسمبر: 7"),
      ("The months are January, March, May, July, August, October, December. That is 7 elements.", "مہینے جنوری، مارچ، مئی، جولائی، اگست، اکتوبر، دسمبر ہیں۔ یعنی 7 رکن۔"),
      [(4, "4 months have 30 days. Count the ones with 31: 7.", "4 مہینوں میں 30 دن ہوتے ہیں۔ 31 دن والے گنیں: 7", "wrong_list")],
      qtype="recall"),
   {"id": "s_rules", "type": "explain",
    "character": say("thinking", "A set has clear members. Each member is written once, inside { }.", "سیٹ کے ارکان واضح ہوتے ہیں۔ ہر رکن ایک ہی بار { } کے اندر لکھا جاتا ہے۔"),
    "text": T("A set is a collection of well-defined, distinct things, so everyone can tell for sure what is in it. \"Tasty fruits\" is only an opinion, so it is not a set. We name a set with a capital letter and write its elements inside braces { }. In tabular form we list the elements: A = {3, 6, 9}. In descriptive form we describe them in words: A is the set of multiples of 3 less than 10. Each element is written once, and the order does not matter. The sign ∈ means belongs to, and ∉ means does not belong to: 6 ∈ A and 7 ∉ A.",
              "سیٹ واضح طور پر بیان کردہ اور مختلف چیزوں کا مجموعہ ہے، اس لیے ہر کوئی یقین سے بتا سکتا ہے کہ اس میں کیا ہے۔ \"مزے دار پھل\" صرف رائے ہے، اس لیے سیٹ نہیں۔ سیٹ کا نام بڑے حرف سے رکھتے ہیں اور ارکان کو قوسین { } کے اندر لکھتے ہیں۔ جدولی شکل میں ارکان کی فہرست لکھتے ہیں: A = {3, 6, 9}۔ بیانیہ شکل میں انھیں الفاظ میں بیان کرتے ہیں: A، 10 سے چھوٹے 3 کے اضعاف کا سیٹ ہے۔ ہر رکن ایک ہی بار لکھا جاتا ہے اور ترتیب سے فرق نہیں پڑتا۔ علامت ∈ کا مطلب تعلق رکھتا ہے اور ∉ کا مطلب تعلق نہیں رکھتا: 6 ∈ A اور 7 ∉ A۔")},
   ch("q3_belongs", ("A = {3, 6, 9, 12, 15}. Which statement is true?", "A = {3, 6, 9, 12, 15}۔ کون سا بیان درست ہے؟"),
      ("12 ∈ A", "12 ∈ A", "Yes! 12 is listed in A, so it belongs to A.", "جی ہاں! 12 سیٹ A میں لکھا ہے، اس لیے A سے تعلق رکھتا ہے۔"),
      [("5 ∈ A", "5 ∈ A", "5 is not listed in A, so 5 ∉ A.", "5 سیٹ A میں نہیں ہے، اس لیے 5 ∉ A۔", "sign_swapped"),
       ("9 ∉ A", "9 ∉ A", "9 is listed in A, so 9 ∈ A. The sign ∉ means does not belong.", "9 سیٹ A میں لکھا ہے، اس لیے 9 ∈ A۔ علامت ∉ کا مطلب تعلق نہیں رکھتا۔", "sign_swapped"),
       ("15 ∉ A", "15 ∉ A", "15 is the last element of A, so 15 ∈ A.", "15، A کا آخری رکن ہے، اس لیے 15 ∈ A۔", "sign_swapped")],
      0, qtype="recall"),
   ch("q4_belongs_letters", ("L is the set of the letters of the word \"LAHORE\". Which statement is true?", "L لفظ \"LAHORE\" کے حروف کا سیٹ ہے۔ کون سا بیان درست ہے؟"),
      ("R ∈ L", "R ∈ L", "Yes! R is a letter of LAHORE.", "جی ہاں! R لفظ LAHORE کا حرف ہے۔"),
      [("P ∈ L", "P ∈ L", "There is no P in LAHORE, so P ∉ L.", "LAHORE میں P نہیں ہے، اس لیے P ∉ L۔", "sign_swapped"),
       ("E ∉ L", "E ∉ L", "E is the last letter of LAHORE, so E ∈ L.", "E لفظ LAHORE کا آخری حرف ہے، اس لیے E ∈ L۔", "sign_swapped"),
       ("N ∈ L", "N ∈ L", "There is no N in LAHORE, so N ∉ L.", "LAHORE میں N نہیں ہے، اس لیے N ∉ L۔", "sign_swapped")],
      2),
   sq("q5_multiples", ("Write the set of the first five multiples of 4 in tabular form (like {1, 2, 3}).", "4 کے پہلے پانچ اضعاف کا سیٹ جدولی شکل میں لکھیں (جیسے {1, 2, 3})۔"), Q5,
      ("4 × 1, 4 × 2, 4 × 3 ... Write the answers, not the multipliers.", "4 × 1، 4 × 2، 4 × 3 ... جوابات لکھیں، ضرب دینے والے اعداد نہیں۔"),
      ("Right! {4, 8, 12, 16, 20}.", "درست! {4, 8, 12, 16, 20}"),
      ("The multiples of 4 are 4, 8, 12, 16, 20. Write them inside { }.", "4 کے اضعاف 4، 8، 12، 16، 20 ہیں۔ انھیں { } کے اندر لکھیں۔"),
      [("{1, 2, 3, 4, 5}", "Those are the numbers you multiply 4 by. The multiples are 4 × each of them: {4, 8, 12, 16, 20}.", "یہ وہ اعداد ہیں جن سے 4 کو ضرب دیتے ہیں۔ اضعاف ان میں سے ہر ایک کے ساتھ 4 کا حاصل ضرب ہیں: {4, 8, 12, 16, 20}", "wrong_list"),
       ("{4, 8, 12, 16}", "That has only four multiples. The first five end with 20.", "اس میں صرف چار اضعاف ہیں۔ پہلے پانچ 20 پر ختم ہوتے ہیں۔", "wrong_list")]),
   nq("q6_distinct", ("The set B holds the letters of the word \"BALLOON\". How many elements does B have?", "سیٹ B میں لفظ \"BALLOON\" کے حروف ہیں۔ B کے کتنے ارکان ہیں؟"), Q6,
      ("L and O each appear twice. A set lists each element once.", "L اور O دو دو بار آتے ہیں۔ سیٹ ہر رکن ایک ہی بار لکھتا ہے۔"),
      ("Right! B = {B, A, L, O, N}: 5 elements.", "درست! B = {B, A, L, O, N}: 5 رکن"),
      ("The word has 7 letters, but L and O repeat. The distinct letters are B, A, L, O, N: 5.", "لفظ میں 7 حروف ہیں مگر L اور O دہراتے ہیں۔ مختلف حروف B، A، L، O، N ہیں: 5"),
      [(7, "That counts every letter, including the repeats. A set lists each element once: 5.", "یہ ہر حرف گنتا ہے، دہرائے ہوئے بھی۔ سیٹ ہر رکن ایک ہی بار لکھتا ہے: 5", "repeated_element")]),
   ch("q7_between", ("Which is the tabular form of the set of natural numbers between 5 and 10?", "5 اور 10 کے درمیان قدرتی اعداد کے سیٹ کی جدولی شکل کون سی ہے؟"),
      (show(Q7), show(Q7), "Yes! \"Between\" leaves out 5 and 10 themselves.", "جی ہاں! \"درمیان\" میں خود 5 اور 10 شامل نہیں ہوتے۔"),
      [(show(Q7_WRONG[0]), show(Q7_WRONG[0]), "That includes both 5 and 10. Between means they are left out.", "اس میں 5 اور 10 دونوں شامل ہیں۔ درمیان کا مطلب ہے کہ انھیں چھوڑ دیں۔", "ends_included"),
       (show(Q7_WRONG[1]), show(Q7_WRONG[1]), "That includes 5. Between means 5 is left out.", "اس میں 5 شامل ہے۔ درمیان کا مطلب ہے کہ 5 کو چھوڑ دیں۔", "ends_included"),
       (show(Q7_WRONG[2]), show(Q7_WRONG[2]), "That includes 10. Between means 10 is left out.", "اس میں 10 شامل ہے۔ درمیان کا مطلب ہے کہ 10 کو چھوڑ دیں۔", "ends_included")],
      3),
   ch("q8_describe", ("Which description fits the set {2, 3, 5, 7}?", "کون سی بیانیہ شکل سیٹ {2, 3, 5, 7} پر پوری اترتی ہے؟"),
      ("The prime numbers less than 10", "10 سے چھوٹے مفرد اعداد", "Yes! The primes below 10 are exactly 2, 3, 5 and 7.", "جی ہاں! 10 سے چھوٹے مفرد اعداد بالکل 2، 3، 5 اور 7 ہیں۔"),
      [("The prime numbers less than 12", "12 سے چھوٹے مفرد اعداد", "That also holds 11, which is not in the set.", "اس میں 11 بھی آتا ہے جو سیٹ میں نہیں۔", "too_wide_rule"),
       ("The odd numbers less than 8", "8 سے چھوٹے طاق اعداد", "That holds 1, which is not in the set, and leaves out 2.", "اس میں 1 آتا ہے جو سیٹ میں نہیں، اور 2 رہ جاتا ہے۔", "too_wide_rule"),
       ("The prime numbers less than 7", "7 سے چھوٹے مفرد اعداد", "That leaves out 7. It gives {2, 3, 5}.", "اس میں 7 رہ جاتا ہے۔ یہ {2, 3, 5} دیتا ہے۔", "too_wide_rule")],
      1),
   sq("q9_odd_tabular", ("Write in tabular form the set of odd numbers greater than 2 and less than 10 (like {1, 2, 3}).", "2 سے بڑے اور 10 سے چھوٹے طاق اعداد کا سیٹ جدولی شکل میں لکھیں (جیسے {1, 2, 3})۔"), Q9,
      ("List the odd numbers after 2 and stop before 10.", "2 کے بعد کے طاق اعداد لکھیں اور 10 سے پہلے رک جائیں۔"),
      ("Right! {3, 5, 7, 9}.", "درست! {3, 5, 7, 9}"),
      ("The odd numbers after 2 and before 10 are 3, 5, 7, 9.", "2 کے بعد اور 10 سے پہلے طاق اعداد 3، 5، 7، 9 ہیں۔"),
      [("{1, 3, 5, 7, 9}", "1 is not greater than 2. Start at 3: {3, 5, 7, 9}.", "1، 2 سے بڑا نہیں۔ 3 سے شروع کریں: {3, 5, 7, 9}", "ends_included")]),
   ch("q10_find_error", ("Zara writes the set of the letters of the word \"SEEDS\" as {S, E, E, D, S}. What went wrong?", "زارہ لفظ \"SEEDS\" کے حروف کا سیٹ {S, E, E, D, S} لکھتی ہے۔ کیا غلطی ہوئی؟"),
      ("A set lists each element once, so it should be {S, E, D}.", "سیٹ ہر رکن ایک ہی بار لکھتا ہے، اس لیے یہ {S, E, D} ہونا چاہیے۔", "Yes! Repeated letters are written only once.", "جی ہاں! دہرائے ہوئے حروف صرف ایک بار لکھے جاتے ہیں۔"),
      [("Nothing. Every letter of the word should be written.", "کوئی غلطی نہیں۔ لفظ کا ہر حرف لکھنا چاہیے۔", "In a set, an element is not repeated. The set is {S, E, D}.", "سیٹ میں رکن دہرایا نہیں جاتا۔ سیٹ {S, E, D} ہے۔", "repeated_element"),
       ("She should use ( ) instead of { }.", "اسے { } کی جگہ ( ) استعمال کرنا چاہیے۔", "A set is written in braces { }. The mistake is the repeated letters.", "سیٹ قوسین { } میں لکھا جاتا ہے۔ غلطی دہرائے ہوئے حروف ہیں۔")],
      1, qtype="find_error"),
   ch("q11_find_error_sign", ("Imran says 9 ∈ {1, 3, 5, 7} because 9 is odd like the others. What went wrong?", "عمران کہتا ہے 9 ∈ {1, 3, 5, 7} کیونکہ 9 بھی دوسروں کی طرح طاق ہے۔ کیا غلطی ہوئی؟"),
      ("9 is not listed in the set, so it is not an element: 9 ∉ {1, 3, 5, 7}.", "9 سیٹ میں لکھا ہی نہیں، اس لیے یہ رکن نہیں: 9 ∉ {1, 3, 5, 7}۔", "Yes! Only what is listed belongs to the set.", "جی ہاں! سیٹ سے وہی تعلق رکھتا ہے جو اس میں لکھا ہو۔"),
      [("Nothing. 9 is odd, so it belongs.", "کوئی غلطی نہیں۔ 9 طاق ہے، اس لیے تعلق رکھتا ہے۔", "Being odd is not enough. The set lists 1, 3, 5, 7 only.", "طاق ہونا کافی نہیں۔ سیٹ میں صرف 1، 3، 5، 7 لکھے ہیں۔", "sign_swapped"),
       ("He should write 9 = {1, 3, 5, 7}.", "اسے 9 = {1, 3, 5, 7} لکھنا چاہیے۔", "An equals sign compares things of the same kind. A number and a set are different.", "برابر کی علامت ایک جیسی چیزوں کا موازنہ کرتی ہے۔ عدد اور سیٹ مختلف ہیں۔")],
      2, qtype="find_error"),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! You wrote and read sets.", "شاباش! آپ نے سیٹ لکھے اور پڑھے۔"),
    "text": T("A set must be well defined: opinions like tasty or beautiful do not make a set. Write its elements once each inside { }. Use ∈ for belongs to and ∉ for does not belong to. Tabular form lists the elements; descriptive form says the rule in words. Between leaves out the end numbers.",
              "سیٹ واضح طور پر بیان کردہ ہونا چاہیے: مزے دار یا خوبصورت جیسی رائے سے سیٹ نہیں بنتا۔ اس کے ارکان ایک ایک بار { } میں لکھیں۔ ∈ تعلق رکھتا ہے اور ∉ تعلق نہیں رکھتا کے لیے استعمال کریں۔ جدولی شکل ارکان کی فہرست ہے؛ بیانیہ شکل اصول کو الفاظ میں کہتی ہے۔ درمیان میں آخری اعداد شامل نہیں ہوتے۔"),
    "points": [T("Check a tabular form against the rule: nothing missing, nothing extra.", "جدولی شکل کو اصول سے ملا کر دیکھیں: کچھ کم نہ ہو، کچھ زیادہ نہ ہو۔"),
               T("Repeated letters are written once.", "دہرائے ہوئے حروف ایک ہی بار لکھے جاتے ہیں۔")]},
 ],
 bank=[
   {"id": "qb_well_defined", "type": "recall", "step": ch("qb_well_defined", ("Which of these is a set (well defined)?", "ان میں سے کون سا سیٹ ہے (واضح طور پر بیان کردہ)؟"),
      ("The days of the week", "ہفتے کے دن", "Yes! There are exactly seven, and everyone agrees.", "جی ہاں! ٹھیک سات ہیں اور سب متفق ہیں۔"),
      [("The nicest days of the week", "ہفتے کے سب سے اچھے دن", "\"Nicest\" is an opinion, so it is not a set.", "\"سب سے اچھے\" رائے ہے، اس لیے یہ سیٹ نہیں۔", "opinion_is_set"),
       ("The clever girls of a school", "اسکول کی ذہین لڑکیاں", "\"Clever\" has no fixed rule, so it is not a set.", "\"ذہین\" کا کوئی مقررہ اصول نہیں، اس لیے یہ سیٹ نہیں۔", "opinion_is_set")],
      0, qtype=None)},
   {"id": "qb_count", "type": "apply", "step": nq("qb_count", ("How many elements are in the set of the letters of the word \"COOLER\"?", "لفظ \"COOLER\" کے حروف کے سیٹ میں کتنے ارکان ہیں؟"), len(set("COOLER")),
      ("O appears twice. Count it once.", "O دو بار آتا ہے۔ اسے ایک ہی بار گنیں۔"),
      ("Right! {C, O, L, E, R}: 5.", "درست! {C, O, L, E, R}: 5"), ("The word has 6 letters but O repeats, so the set has 5 elements.", "لفظ میں 6 حروف ہیں مگر O دہراتا ہے، اس لیے سیٹ کے 5 ارکان ہیں۔"),
      [(6, "That counts O twice. Count it once: 5.", "یہ O کو دو بار گنتا ہے۔ ایک ہی بار گنیں: 5", "repeated_element")], qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": ch("qb_find_error",
      ("Sana reads 8 ∉ {2, 4, 6, 8} as \"8 is in the set\". What went wrong?", "ثناء 8 ∉ {2, 4, 6, 8} کو \"8 سیٹ میں ہے\" پڑھتی ہے۔ کیا غلطی ہوئی؟"),
      ("∉ means does not belong. And the statement is false, because 8 is in the set.", "∉ کا مطلب تعلق نہیں رکھتا۔ اور یہ بیان غلط ہے کیونکہ 8 سیٹ میں ہے۔", "Yes! The sign ∉ says \"does not belong to\".", "جی ہاں! علامت ∉ کہتی ہے \"تعلق نہیں رکھتا\"۔"),
      [("Nothing. ∉ means belongs to.", "کوئی غلطی نہیں۔ ∉ کا مطلب تعلق رکھتا ہے۔", "∈ is the sign for belongs to. ∉ has a line through it: does not belong.", "تعلق رکھتا ہے کی علامت ∈ ہے۔ ∉ پر لکیر ہے: تعلق نہیں رکھتا۔", "sign_swapped"),
       ("She should say 8 is not a number.", "اسے کہنا چاہیے 8 عدد نہیں۔", "8 is a number. The mistake is in reading the sign.", "8 عدد ہے۔ غلطی علامت پڑھنے میں ہے۔")],
      1, qtype=None)},
 ],
 review=[
   {"id": "r_count", "type": "recall", "step": nq("r_count", ("How many elements are in the set of the letters of the word \"PEPPER\"?", "لفظ \"PEPPER\" کے حروف کے سیٹ میں کتنے ارکان ہیں؟"), R1,
      ("Write each different letter once.", "ہر مختلف حرف ایک بار لکھیں۔"),
      ("Right! {P, E, R}: 3.", "درست! {P, E, R}: 3"), ("The letters are P, E, R, each written once: 3.", "حروف P، E، R ہیں، ہر ایک ایک بار: 3"),
      [(6, "That counts every letter. Write each different letter once: 3.", "یہ ہر حرف گنتا ہے۔ ہر مختلف حرف ایک بار لکھیں: 3", "repeated_element")], qtype=None)},
   {"id": "r_days", "type": "apply", "step": nq("r_days", ("How many days of the week have a name that starts with S?", "ہفتے کے کتنے دنوں کا نام S سے شروع ہوتا ہے؟ (انگریزی نام)"), R2,
      ("Say the seven days and listen for S.", "سات دن بولیں اور S سنیں۔"),
      ("Right! Saturday and Sunday: 2.", "درست! Saturday اور Sunday: 2"), ("Only Saturday and Sunday start with S: 2.", "صرف Saturday اور Sunday S سے شروع ہوتے ہیں: 2"),
      [(7, "That is all the days. Only those starting with S count: 2.", "یہ سارے دن ہیں۔ صرف S سے شروع ہونے والے گنیں: 2", "wrong_list")], qtype=None)},
 ],
 glossary=[T("Set", "سیٹ"), T("Element", "رکن"), T("Well defined", "واضح طور پر بیان کردہ"), T("Tabular form", "جدولی شکل"), T("Descriptive form", "بیانیہ شکل")],
 flashcards=[
   {"id": "f_signs", "front": T("What do ∈ and ∉ mean?", "∈ اور ∉ کا کیا مطلب ہے؟"),
    "back": T("∈ means belongs to (is an element of). ∉ means does not belong to.", "∈ کا مطلب تعلق رکھتا ہے (رکن ہے)۔ ∉ کا مطلب تعلق نہیں رکھتا۔")},
   {"id": "f_forms", "front": T("What are tabular and descriptive form?", "جدولی اور بیانیہ شکل کیا ہیں؟"),
    "back": T("Tabular form lists the elements in { }. Descriptive form says the rule in words.", "جدولی شکل ارکان کو { } میں لکھتی ہے۔ بیانیہ شکل اصول کو الفاظ میں کہتی ہے۔")},
 ],
 home_task={"id": "h_sets_at_home", "text": T(
   "Write three sets from your home in tabular form (for example, the members of your family whose names start with the same letter, or the spoons in a drawer). Then write each in descriptive form and tell a friend whether a given item belongs (∈) or not (∉).",
   "اپنے گھر کے تین سیٹ جدولی شکل میں لکھیں (مثلاً گھر کے وہ افراد جن کے نام ایک ہی حرف سے شروع ہوتے ہیں، یا دراز کے چمچ)۔ پھر ہر ایک کو بیانیہ شکل میں لکھیں اور کسی دوست کو بتائیں کہ دی گئی چیز سیٹ سے تعلق رکھتی ہے (∈) یا نہیں (∉)۔")},
 notes=["Covers well-defined collections (q1), counting and writing the elements of a set (q2, q6), the signs for belongs to and does not belong to (q3, q4, q11), tabular form (q5, q7, q9), descriptive form (q8) and a find-the-error question (q10, q11).",
        "Each wrong answer is a real mistake: an opinion taken as a set, the two signs swapped, a repeated letter counted twice, the end numbers included for between, and a rule that fits too many or too few numbers.",
        "Urdu terms to check: واضح طور پر بیان کردہ (well defined), رکن (element), جدولی شکل / بیانیہ شکل (tabular / descriptive form), تعلق رکھتا ہے (belongs to), اضعاف (multiples)."],
 minutes=15,
)

figs.attach(lesson, {
    "q3_belongs": figs.oval_figure(sorted(A3), "An oval named A holding 3, 6, 9, 12 and 15.", "بیضوی شکل A جس میں 3، 6، 9، 12 اور 15 ہیں۔", name="A"),
    "q6_distinct": figs.letter_tiles("BALLOON", "The word BALLOON written one letter to a tile: B, A, L, L, O, O, N.", "لفظ BALLOON ایک ٹائل پر ایک حرف: B، A، L، L، O، O، N۔"),
})
write(lesson)
