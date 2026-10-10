"""Practice set for Exercise 5.2 of the book: empty, finite, infinite and
singleton sets, cardinal numbers, the signs for subset, superset, proper
subset, not a subset and equivalent, equal and equivalent sets, and listing
all the subsets of a set. The questions are new; only the kinds of question
follow the book."""
from itertools import combinations
from common import (T, say, nq, ch, practice_lesson, practice_intro, write, show,
                    EX_SKILL, SET_MEANING, SET_KINDS, SET_SUBSETS)
import figs

SKILL = EX_SKILL["5.2"]


def primes_between(a, b):
    return {k for k in range(a + 1, b) if k > 1 and all(k % d for d in range(2, k))}


def subsets(items):
    items = list(items)
    return [set(c) for r in range(len(items) + 1) for c in combinations(items, r)]


# q1: the empty set
DAYS = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31,
        "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}
assert [m for m, d in DAYS.items() if d == 32] == []
assert [m for m, d in DAYS.items() if d in (28, 29)] == ["February"]
assert primes_between(20, 30) == {23, 29}
# q2: the singleton set
assert primes_between(8, 12) == {11}
assert primes_between(10, 20) == {11, 13, 17, 19}
assert [n for n in range(11, 12) if n % 2 == 0] == []
assert [n for n in range(1, 20) if n % 7 == 0] == [7, 14]
# q3: the infinite set (the multiples of 9 never end; the others can be counted)
assert 366 == 365 + 1 and len("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 26 and len(range(0, 1000000)) == 1000000
# q4: multiples of 6 below 50
M4 = [n for n in range(1, 50) if n % 6 == 0]
Q4 = len(M4)
assert M4 == [6, 12, 18, 24, 30, 36, 42, 48] and Q4 == 8 and M4[-1] == 48 and 50 // 6 == 8
# q5: letters of MATHEMATICS
Q5 = len(set("MATHEMATICS"))
assert Q5 == 8 and len("MATHEMATICS") == 11
# q6: A = {1, 3, 5}, B = {1, 2, 3, 4, 5}
A6, B6 = {1, 3, 5}, {1, 2, 3, 4, 5}
assert A6 < B6 and not B6 < A6 and A6 <= B6 and len(A6) != len(B6)
# q7: {2, 4, 6, 8} ⊇ {4, 8}
C7, D7 = {2, 4, 6, 8}, {4, 8}
assert C7 >= D7 and not C7 <= D7 and C7 != D7 and len(C7) != len(D7)
# q8: equal and equivalent
P8, Q8 = {"a", "b", "c"}, {1, 2, 3}
assert len(P8) == len(Q8) and P8 != Q8
assert {1, 2, 3} == {3, 2, 1}
# q9: subsets of {a, b, c}
S9 = subsets("abc")
assert len(S9) == 8 == 2 ** 3 and len([s for s in S9 if s != set("abc")]) == 7
# q10: all subsets of {5, 7}
S10 = subsets([5, 7])
assert [show(s) for s in S10] == ["{ }", "{5}", "{7}", "{5, 7}"] and len(S10) == 4
# q11: proper subsets of a 4-element set
S11 = subsets("wxyz")
Q11 = len([s for s in S11 if s != set("wxyz")])
assert len(S11) == 16 and Q11 == 15
# q12: the improper subset of {1, 2, 3}
S12 = [s for s in subsets([1, 2, 3]) if s == {1, 2, 3}]
assert S12 == [{1, 2, 3}] and set() < {1, 2, 3}
# bank and review
QB_APP = len(subsets("mnpq"))
assert QB_APP == 16
assert {"a"} != {"b"} and len({"a"}) == len({"b"})
R1 = len([n for n in range(1, 15) if n % 2])
assert R1 == 7
R2 = len([s for s in subsets([1, 2]) if s != {1, 2}])
assert R2 == 3

lesson = practice_lesson(
 "5.2", script="exercise_5_2.py",
 title=T("Exercise 5.2 practice: kinds of sets and subsets", "مشق 5.2 کی پریکٹس: سیٹ کی اقسام اور ذیلی سیٹ"),
 outcome="Tell empty, singleton, finite and infinite sets apart, give the cardinal number of a set, use the signs for subset, superset, proper subset, not a subset and equivalent, tell equal sets from equivalent sets, and list all the subsets of a set as proper or improper.",
 prerequisites=[SET_MEANING, SET_KINDS, SET_SUBSETS],
 misconceptions=[
   {"id": "zero_is_empty", "description": "Thinks {0} is the empty set."},
   {"id": "empty_or_one", "description": "Mixes up the empty set (no elements) with a singleton set (one element)."},
   {"id": "big_is_infinite", "description": "Thinks a very large set that can still be counted is infinite."},
   {"id": "count_off", "description": "Counts the elements wrongly: includes 0, counts repeated letters twice, or gives the largest element instead of how many."},
   {"id": "symbol_direction", "description": "Uses a subset or proper subset sign the wrong way round."},
   {"id": "equal_means_equivalent", "description": "Thinks sets with the same number of elements are equal, or that equal sets must be written in the same order."},
   {"id": "forgets_empty_self", "description": "Leaves out the empty set or the set itself when listing or counting all the subsets."},
   {"id": "proper_count", "description": "Counts all the subsets as the proper subsets, or the empty set as the improper one."},
 ],
 steps=[
   practice_intro("5.2",
     "Here you tell empty, singleton, finite and infinite sets apart, count elements, use the subset signs, compare sets, and list all the subsets of a set.",
     "اس میں آپ خالی، اکائی، محدود اور لامحدود سیٹوں میں فرق کریں گے، ارکان گنیں گے، ذیلی سیٹ کی علامتیں استعمال کریں گے، سیٹوں کا موازنہ کریں گے اور کسی سیٹ کے تمام ذیلی سیٹ لکھیں گے۔",
     "Exercise 5.2 is about kinds of sets and subsets. Ready?", "مشق 5.2 سیٹ کی اقسام اور ذیلی سیٹ کے بارے میں ہے۔ تیار؟"),
   ch("q1_empty", ("Which of these is the empty set?", "ان میں سے کون سا خالی سیٹ ہے؟"),
      ("The months of the year that have 32 days", "سال کے وہ مہینے جن کے 32 دن ہوں", "Yes! No month has 32 days, so there are no elements.", "جی ہاں! کسی مہینے کے 32 دن نہیں ہوتے، اس لیے کوئی رکن نہیں۔"),
      [("The set {0}", "سیٹ {0}", "{0} has one element, the number 0. The empty set has none.", "{0} کا ایک رکن ہے، عدد 0۔ خالی سیٹ کا کوئی رکن نہیں۔", "zero_is_empty"),
       ("The months of the year that have 28 or 29 days", "سال کے وہ مہینے جن کے 28 یا 29 دن ہوں", "February has 28 or 29 days. That is one element, so the set is {February}.", "فروری کے 28 یا 29 دن ہوتے ہیں۔ یہ ایک رکن ہے، اس لیے سیٹ {فروری} ہے۔", "empty_or_one"),
       ("The prime numbers between 20 and 30", "20 اور 30 کے درمیان مفرد اعداد", "23 and 29 are prime, so the set has two elements.", "23 اور 29 مفرد ہیں، اس لیے سیٹ کے دو رکن ہیں۔")],
      2, qtype="recall"),
   ch("q2_singleton", ("Which of these is a singleton set (exactly one element)?", "ان میں سے کون سا اکائی سیٹ ہے (بالکل ایک رکن)؟"),
      ("The prime numbers between 8 and 12", "8 اور 12 کے درمیان مفرد اعداد", "Yes! Only 11 is prime between 8 and 12: {11}.", "جی ہاں! 8 اور 12 کے درمیان صرف 11 مفرد ہے: {11}"),
      [("The prime numbers between 10 and 20", "10 اور 20 کے درمیان مفرد اعداد", "11, 13, 17 and 19 are all prime: four elements.", "11، 13، 17 اور 19 سب مفرد ہیں: چار رکن۔"),
       ("The even numbers between 10 and 12", "10 اور 12 کے درمیان جفت اعداد", "11 is the only number between 10 and 12, and it is odd. The set is empty.", "10 اور 12 کے درمیان صرف 11 ہے اور وہ طاق ہے۔ سیٹ خالی ہے۔", "empty_or_one"),
       ("The multiples of 7 less than 20", "20 سے چھوٹے 7 کے اضعاف", "7 and 14 are both multiples: two elements.", "7 اور 14 دونوں اضعاف ہیں: دو رکن۔")],
      0, qtype="recall"),
   ch("q3_infinite", ("Which of these sets is infinite?", "ان میں سے کون سا سیٹ لامحدود ہے؟"),
      ("The multiples of 9", "9 کے اضعاف", "Yes! 9, 18, 27, ... never ends.", "جی ہاں! 9، 18، 27، ... کبھی ختم نہیں ہوتے۔"),
      [("The days of a leap year", "لیپ سال کے دن", "There are 366 of them. That is many, but they can be counted: finite.", "ان کی تعداد 366 ہے۔ یہ بہت ہیں مگر گنے جا سکتے ہیں: محدود۔", "big_is_infinite"),
       ("The whole numbers less than 1,000,000", "1,000,000 سے چھوٹے مکمل اعداد", "It is a huge set, but it ends at 999,999, so it is finite.", "یہ بہت بڑا سیٹ ہے مگر 999,999 پر ختم ہوتا ہے، اس لیے محدود ہے۔", "big_is_infinite"),
       ("The letters of the English alphabet", "انگریزی حروفِ تہجی", "There are 26 letters: finite.", "26 حروف ہیں: محدود۔")],
      1, qtype="recall"),
   nq("q4_cardinal", ("Let A be the set of multiples of 6 less than 50. What is n(A), the number of elements?", "فرض کریں A، 50 سے چھوٹے 6 کے اضعاف کا سیٹ ہے۔ n(A)، یعنی ارکان کی تعداد، کیا ہے؟"), Q4,
      ("List them: 6, 12, 18 ... and stop before 50. Then count.", "فہرست بنائیں: 6، 12، 18 ... اور 50 سے پہلے رک جائیں۔ پھر گنیں۔"),
      ("Right! {6, 12, 18, 24, 30, 36, 42, 48}: n(A) = 8.", "درست! {6, 12, 18, 24, 30, 36, 42, 48}: n(A) = 8"),
      ("The multiples are 6, 12, 18, 24, 30, 36, 42, 48. Count them: 8.", "اضعاف 6، 12، 18، 24، 30، 36، 42، 48 ہیں۔ انھیں گنیں: 8"),
      [(48, "48 is the biggest element. n(A) is how many elements there are: 8.", "48 سب سے بڑا رکن ہے۔ n(A) ارکان کی تعداد ہے: 8", "count_off"),
       (9, "That counts one too many. List them and count: 8.", "یہ ایک زیادہ گنتا ہے۔ فہرست بنا کر گنیں: 8", "count_off")]),
   nq("q5_letters", ("What is n(M), if M is the set of the letters of the word \"MATHEMATICS\"?", "اگر M لفظ \"MATHEMATICS\" کے حروف کا سیٹ ہے تو n(M) کیا ہے؟"), Q5,
      ("M, A and T each appear twice. A set writes each letter once.", "M، A اور T دو دو بار آتے ہیں۔ سیٹ ہر حرف ایک بار لکھتا ہے۔"),
      ("Right! {M, A, T, H, E, I, C, S}: 8.", "درست! {M, A, T, H, E, I, C, S}: 8"),
      ("The word has 11 letters, but M, A, T repeat. The different letters are M, A, T, H, E, I, C, S: 8.", "لفظ میں 11 حروف ہیں مگر M، A، T دہراتے ہیں۔ مختلف حروف M، A، T، H، E، I، C، S ہیں: 8"),
      [(11, "That counts every letter, repeats too. A set counts each letter once: 8.", "یہ ہر حرف گنتا ہے، دہرائے ہوئے بھی۔ سیٹ ہر حرف ایک بار گنتا ہے: 8", "count_off")]),
   {"id": "s_rules", "type": "explain",
    "character": say("thinking", "Compare sets by their elements. Subsets are sets inside a set.", "سیٹوں کا موازنہ ان کے ارکان سے کریں۔ ذیلی سیٹ کسی سیٹ کے اندر کے سیٹ ہیں۔"),
    "text": T("The empty set { } has no elements, and a singleton set has exactly one. A finite set can be counted to the end; an infinite set never ends. n(A) is the number of elements of A. A ⊆ B means every element of A is in B, and B ⊇ A is the same thing read the other way. If A is a subset of B but not equal to B, A is a proper subset, written A ⊂ B. A ⊄ B means A is not a subset of B. Equal sets have exactly the same elements, in any order. Equivalent sets (A ↔ B) have the same number of elements. A set with n elements has 2 to the power n subsets: the empty set and the set itself are always among them. The set itself is the improper subset; all the others are proper.",
              "خالی سیٹ { } کا کوئی رکن نہیں ہوتا اور اکائی سیٹ کا بالکل ایک رکن ہوتا ہے۔ محدود سیٹ آخر تک گنا جا سکتا ہے؛ لامحدود سیٹ کبھی ختم نہیں ہوتا۔ n(A) سیٹ A کے ارکان کی تعداد ہے۔ A ⊆ B کا مطلب ہے A کا ہر رکن B میں ہے، اور B ⊇ A وہی بات دوسری طرف سے پڑھی گئی ہے۔ اگر A، B کا ذیلی سیٹ ہو مگر B کے برابر نہ ہو تو A حقیقی ذیلی سیٹ ہے، جو A ⊂ B لکھا جاتا ہے۔ A ⊄ B کا مطلب ہے A، B کا ذیلی سیٹ نہیں۔ برابر سیٹوں کے ارکان بالکل ایک جیسے ہوتے ہیں، کسی بھی ترتیب میں۔ ہم قوت سیٹوں (A ↔ B) کے ارکان کی تعداد برابر ہوتی ہے۔ n ارکان والے سیٹ کے 2 کی طاقت n ذیلی سیٹ ہوتے ہیں: خالی سیٹ اور خود سیٹ ہمیشہ ان میں شامل ہوتے ہیں۔ خود سیٹ غیر حقیقی ذیلی سیٹ ہے؛ باقی سب حقیقی ہیں۔")},
   ch("q6_proper", ("A = {1, 3, 5} and B = {1, 2, 3, 4, 5}. Which statement is true?", "A = {1, 3, 5} اور B = {1, 2, 3, 4, 5}۔ کون سا بیان درست ہے؟"),
      ("A ⊂ B", "A ⊂ B", "Yes! Every element of A is in B, and B has more, so A is a proper subset of B.", "جی ہاں! A کا ہر رکن B میں ہے اور B میں مزید ہیں، اس لیے A، B کا حقیقی ذیلی سیٹ ہے۔"),
      [("B ⊂ A", "B ⊂ A", "B has elements (2 and 4) that A does not have, so B is not inside A.", "B کے رکن (2 اور 4) A میں نہیں، اس لیے B، A کے اندر نہیں۔", "symbol_direction"),
       ("A ⊄ B", "A ⊄ B", "1, 3 and 5 are all in B, so A is a subset of B.", "1، 3 اور 5 سب B میں ہیں، اس لیے A، B کا ذیلی سیٹ ہے۔", "symbol_direction"),
       ("A ↔ B", "A ↔ B", "A has 3 elements and B has 5, so they are not equivalent.", "A کے 3 اور B کے 5 رکن ہیں، اس لیے یہ ہم قوت نہیں۔", "equal_means_equivalent")],
      0),
   ch("q7_superset", ("Which sign makes this true? {2, 4, 6, 8} __ {4, 8}", "کون سی علامت اسے درست بناتی ہے؟ {2, 4, 6, 8} __ {4, 8}"),
      ("⊇", "⊇", "Yes! {2, 4, 6, 8} contains every element of {4, 8}, so it is a superset.", "جی ہاں! {2, 4, 6, 8} میں {4, 8} کا ہر رکن ہے، اس لیے یہ فوقی سیٹ ہے۔"),
      [("⊆", "⊆", "That says the left set is inside {4, 8}. 2 and 6 are not in {4, 8}.", "یہ کہتا ہے بائیں سیٹ {4, 8} کے اندر ہے۔ 2 اور 6، {4, 8} میں نہیں۔", "symbol_direction"),
       ("=", "=", "The sets have different elements, so they are not equal.", "سیٹوں کے ارکان مختلف ہیں، اس لیے یہ برابر نہیں۔", "equal_means_equivalent"),
       ("↔", "↔", "The sets have 4 and 2 elements, so they are not equivalent.", "سیٹوں کے 4 اور 2 رکن ہیں، اس لیے یہ ہم قوت نہیں۔", "equal_means_equivalent")],
      3),
   ch("q8_equal_equivalent", ("P = {a, b, c} and Q = {1, 2, 3}. Which statement is true?", "P = {a, b, c} اور Q = {1, 2, 3}۔ کون سا بیان درست ہے؟"),
      ("They are equivalent but not equal.", "یہ ہم قوت ہیں مگر برابر نہیں۔", "Yes! Both have 3 elements, but the elements are different.", "جی ہاں! دونوں کے 3 رکن ہیں مگر ارکان مختلف ہیں۔"),
      [("They are equal, because both have 3 elements.", "یہ برابر ہیں، کیونکہ دونوں کے 3 رکن ہیں۔", "Equal sets need the same elements, not just the same number of them.", "برابر سیٹوں کے ارکان ایک جیسے ہونا ضروری ہے، صرف تعداد نہیں۔", "equal_means_equivalent"),
       ("They are neither equal nor equivalent.", "یہ نہ برابر ہیں نہ ہم قوت۔", "They have the same number of elements, so they are equivalent.", "ان کے ارکان کی تعداد برابر ہے، اس لیے یہ ہم قوت ہیں۔"),
       ("They are equal and equivalent.", "یہ برابر اور ہم قوت ہیں۔", "Their elements differ (letters and numbers), so they are not equal.", "ان کے ارکان مختلف ہیں (حروف اور اعداد)، اس لیے یہ برابر نہیں۔", "equal_means_equivalent")],
      0),
   ch("q9_find_error", ("Hira says {1, 2, 3} and {3, 2, 1} are different sets because the order is different. What went wrong?", "ہیرا کہتی ہے {1, 2, 3} اور {3, 2, 1} مختلف سیٹ ہیں کیونکہ ترتیب مختلف ہے۔ کیا غلطی ہوئی؟"),
      ("Order does not matter in a set. Both have the same elements, so they are equal.", "سیٹ میں ترتیب سے فرق نہیں پڑتا۔ دونوں کے ارکان ایک جیسے ہیں، اس لیے یہ برابر ہیں۔", "Yes! Same elements means the same set.", "جی ہاں! ایک جیسے ارکان کا مطلب ایک ہی سیٹ۔"),
      [("Nothing. Different order makes a different set.", "کوئی غلطی نہیں۔ مختلف ترتیب سے مختلف سیٹ بنتا ہے۔", "A set is only about which elements are in it, not the order.", "سیٹ صرف اس بات سے ہے کہ اس میں کون سے ارکان ہیں، ترتیب سے نہیں۔", "equal_means_equivalent"),
       ("They are equivalent but not equal.", "یہ ہم قوت ہیں مگر برابر نہیں۔", "They are equivalent, but they are also equal, because the elements are the same.", "یہ ہم قوت ہیں، مگر برابر بھی ہیں کیونکہ ارکان ایک جیسے ہیں۔", "equal_means_equivalent")],
      0, qtype="find_error"),
   nq("q10_subsets_count", ("How many subsets does the set {a, b, c} have, counting the empty set and the set itself?", "سیٹ {a, b, c} کے کتنے ذیلی سیٹ ہیں، خالی سیٹ اور خود سیٹ کو ملا کر؟"), len(S9),
      ("List them by size: none, one element, two elements, all three.", "سائز کے لحاظ سے لکھیں: کوئی نہیں، ایک رکن، دو رکن، تینوں۔"),
      ("Right! { }, {a}, {b}, {c}, {a, b}, {a, c}, {b, c}, {a, b, c}: 8.", "درست! { }، {a}، {b}، {c}، {a, b}، {a, c}، {b, c}، {a, b, c}: 8"),
      ("A set with 3 elements has 2 × 2 × 2 = 8 subsets.", "3 ارکان والے سیٹ کے 2 × 2 × 2 = 8 ذیلی سیٹ ہوتے ہیں۔"),
      [(6, "Count the empty set and the set itself too: 8.", "خالی سیٹ اور خود سیٹ کو بھی گنیں: 8", "forgets_empty_self"),
       (7, "That is the number of proper subsets. All the subsets include the set itself: 8.", "یہ حقیقی ذیلی سیٹ کی تعداد ہے۔ تمام ذیلی سیٹ میں خود سیٹ بھی شامل ہے: 8", "proper_count")]),
   ch("q11_list_subsets", ("Which list shows all the subsets of {5, 7}?", "کون سی فہرست {5, 7} کے تمام ذیلی سیٹ دکھاتی ہے؟"),
      ("{ }, {5}, {7}, {5, 7}", "{ }، {5}، {7}، {5, 7}", "Yes! Four subsets: none, each one alone, and both.", "جی ہاں! چار ذیلی سیٹ: کوئی نہیں، ہر ایک اکیلا، اور دونوں۔"),
      [("{5}, {7}, {5, 7}", "{5}، {7}، {5, 7}", "The empty set { } is a subset of every set. Add it: 4 subsets.", "خالی سیٹ { } ہر سیٹ کا ذیلی سیٹ ہے۔ اسے شامل کریں: 4 ذیلی سیٹ۔", "forgets_empty_self"),
       ("{ }, {5}, {7}", "{ }، {5}، {7}", "The set itself, {5, 7}, is also a subset. Add it.", "خود سیٹ {5, 7} بھی ذیلی سیٹ ہے۔ اسے شامل کریں۔", "forgets_empty_self"),
       ("{ }, {5}, {7}, {5, 7}, {7, 5}", "{ }، {5}، {7}، {5, 7}، {7, 5}", "{5, 7} and {7, 5} are the same set. List it once.", "{5, 7} اور {7, 5} ایک ہی سیٹ ہیں۔ اسے ایک بار لکھیں۔", "equal_means_equivalent")],
      1),
   nq("q12_proper_count", ("How many proper subsets does {w, x, y, z} have?", "{w, x, y, z} کے کتنے حقیقی ذیلی سیٹ ہیں؟"), Q11,
      ("All subsets: 2 × 2 × 2 × 2. A proper subset is any subset except the set itself.", "تمام ذیلی سیٹ: 2 × 2 × 2 × 2۔ حقیقی ذیلی سیٹ خود سیٹ کے علاوہ ہر ذیلی سیٹ ہے۔"),
      ("Right! 16 subsets, minus the set itself: 15.", "درست! 16 ذیلی سیٹ، منفی خود سیٹ: 15"),
      ("4 elements give 2 × 2 × 2 × 2 = 16 subsets. Take away the improper one, the set itself: 15.", "4 ارکان کے 2 × 2 × 2 × 2 = 16 ذیلی سیٹ ہوتے ہیں۔ غیر حقیقی یعنی خود سیٹ نکال دیں: 15"),
      [(16, "That is all the subsets. The set itself is not a proper subset: 15.", "یہ تمام ذیلی سیٹ ہیں۔ خود سیٹ حقیقی ذیلی سیٹ نہیں: 15", "proper_count"),
       (14, "That also takes away the empty set. The empty set is a proper subset, so only remove the set itself: 15.", "اس میں خالی سیٹ بھی نکل گیا۔ خالی سیٹ حقیقی ذیلی سیٹ ہے، اس لیے صرف خود سیٹ نکالیں: 15", "proper_count")]),
   ch("q13_improper", ("Which subset of {1, 2, 3} is its improper subset?", "{1, 2, 3} کا غیر حقیقی ذیلی سیٹ کون سا ہے؟"),
      ("{1, 2, 3}", "{1, 2, 3}", "Yes! The set itself is the only improper subset.", "جی ہاں! خود سیٹ ہی واحد غیر حقیقی ذیلی سیٹ ہے۔"),
      [("{ }", "{ }", "The empty set is a proper subset. Only the set itself is improper.", "خالی سیٹ حقیقی ذیلی سیٹ ہے۔ صرف خود سیٹ غیر حقیقی ہے۔", "proper_count"),
       ("{1, 2}", "{1, 2}", "{1, 2} leaves out 3, so it is a proper subset.", "{1, 2} میں 3 نہیں، اس لیے یہ حقیقی ذیلی سیٹ ہے۔"),
       ("{3}", "{3}", "{3} is smaller than the set, so it is a proper subset.", "{3} سیٹ سے چھوٹا ہے، اس لیے یہ حقیقی ذیلی سیٹ ہے۔")],
      2),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! You know your kinds of sets and subsets.", "شاباش! آپ سیٹ کی اقسام اور ذیلی سیٹ جانتے ہیں۔"),
    "text": T("The empty set has no elements ({0} has one). A singleton has one element. A finite set ends; an infinite set does not, and a big set that ends is still finite. A set with n elements has 2ⁿ subsets, including { } and the set itself; the set itself is the improper subset and all the others are proper. Equal sets have the same elements; equivalent sets only have the same number of them.",
              "خالی سیٹ کا کوئی رکن نہیں ({0} کا ایک رکن ہے)۔ اکائی سیٹ کا ایک رکن ہوتا ہے۔ محدود سیٹ ختم ہو جاتا ہے؛ لامحدود نہیں ہوتا، اور بڑا سیٹ جو ختم ہو جائے پھر بھی محدود ہے۔ n ارکان والے سیٹ کے 2ⁿ ذیلی سیٹ ہوتے ہیں، جن میں { } اور خود سیٹ بھی ہیں؛ خود سیٹ غیر حقیقی ذیلی سیٹ ہے اور باقی سب حقیقی۔ برابر سیٹوں کے ارکان ایک جیسے ہوتے ہیں؛ ہم قوت سیٹوں کے ارکان کی صرف تعداد برابر ہوتی ہے۔"),
    "points": [T("To list subsets, go by size: none, one, two, ... all.", "ذیلی سیٹ لکھنے کے لیے سائز کے لحاظ سے چلیں: کوئی نہیں، ایک، دو، ... سب۔"),
               T("Proper subsets = all subsets − 1.", "حقیقی ذیلی سیٹ = تمام ذیلی سیٹ − 1")]},
 ],
 bank=[
   {"id": "qb_infinite", "type": "recall", "step": ch("qb_infinite", ("Which of these sets is infinite?", "ان میں سے کون سا سیٹ لامحدود ہے؟"),
      ("The odd numbers", "طاق اعداد", "Yes! 1, 3, 5, 7, ... never ends.", "جی ہاں! 1، 3، 5، 7، ... کبھی ختم نہیں ہوتے۔"),
      [("The odd numbers less than 100", "100 سے چھوٹے طاق اعداد", "It ends at 99, so it is finite.", "یہ 99 پر ختم ہو جاتا ہے، اس لیے محدود ہے۔", "big_is_infinite"),
       ("The students of a big school", "بڑے اسکول کے طلبہ", "Even a big school can be counted: finite.", "بڑا اسکول بھی گنا جا سکتا ہے: محدود۔", "big_is_infinite")],
      0, qtype=None)},
   {"id": "qb_subsets", "type": "apply", "step": nq("qb_subsets", ("How many subsets does {m, n, p, q} have?", "{m, n, p, q} کے کتنے ذیلی سیٹ ہیں؟"), QB_APP,
      ("Each element is in a subset or out of it: 2 × 2 × 2 × 2.", "ہر رکن یا ذیلی سیٹ میں ہوتا ہے یا نہیں: 2 × 2 × 2 × 2"),
      ("Right! 2 × 2 × 2 × 2 = 16.", "درست! 2 × 2 × 2 × 2 = 16"), ("4 elements give 2⁴ = 16 subsets.", "4 ارکان کے 2⁴ = 16 ذیلی سیٹ ہوتے ہیں۔"),
      [(15, "That leaves out the set itself. All the subsets: 16.", "اس میں خود سیٹ رہ گیا۔ تمام ذیلی سیٹ: 16", "proper_count"),
       (8, "That is for 3 elements. With 4 elements double it: 16.", "یہ 3 ارکان کے لیے ہے۔ 4 ارکان کے لیے دگنا کریں: 16", "forgets_empty_self")], qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": ch("qb_find_error",
      ("Rafi says {a} and {b} are equal sets because each has one element. What went wrong?", "رافع کہتا ہے {a} اور {b} برابر سیٹ ہیں کیونکہ ہر ایک کا ایک رکن ہے۔ کیا غلطی ہوئی؟"),
      ("They are equivalent (same number of elements), but not equal, because a and b are different elements.", "یہ ہم قوت ہیں (ارکان کی تعداد برابر)، مگر برابر نہیں کیونکہ a اور b مختلف ارکان ہیں۔", "Yes! Equal needs the same elements.", "جی ہاں! برابر ہونے کے لیے ایک جیسے ارکان چاہییں۔"),
      [("Nothing. Sets with one element each are equal.", "کوئی غلطی نہیں۔ ایک ایک رکن والے سیٹ برابر ہوتے ہیں۔", "The same number of elements only makes them equivalent.", "ارکان کی تعداد برابر ہونے سے یہ صرف ہم قوت ہوتے ہیں۔", "equal_means_equivalent"),
       ("They are not even equivalent.", "یہ تو ہم قوت بھی نہیں۔", "Both have one element, so they are equivalent.", "دونوں کا ایک ایک رکن ہے، اس لیے یہ ہم قوت ہیں۔")],
      0, qtype=None)},
 ],
 review=[
   {"id": "r_cardinal", "type": "recall", "step": nq("r_cardinal", ("How many elements does the set of the odd numbers less than 15 have?", "15 سے چھوٹے طاق اعداد کے سیٹ کے کتنے ارکان ہیں؟"), R1,
      ("List 1, 3, 5 ... and stop before 15.", "1، 3، 5 ... لکھیں اور 15 سے پہلے رک جائیں۔"),
      ("Right! 1, 3, 5, 7, 9, 11, 13: 7.", "درست! 1، 3، 5، 7، 9، 11، 13: 7"), ("1, 3, 5, 7, 9, 11, 13 are 7 numbers.", "1، 3، 5، 7، 9، 11، 13 یعنی 7 اعداد۔"),
      [(8, "15 is not less than 15. Count to 13: 7.", "15، 15 سے چھوٹا نہیں۔ 13 تک گنیں: 7", "count_off")], qtype=None)},
   {"id": "r_proper", "type": "apply", "step": nq("r_proper", ("How many proper subsets does {1, 2} have?", "{1, 2} کے کتنے حقیقی ذیلی سیٹ ہیں؟"), R2,
      ("The subsets are { }, {1}, {2}, {1, 2}. Which is improper?", "ذیلی سیٹ { }، {1}، {2}، {1, 2} ہیں۔ غیر حقیقی کون سا ہے؟"),
      ("Right! { }, {1} and {2}: 3.", "درست! { }، {1} اور {2}: 3"), ("4 subsets, minus the set itself: 3.", "4 ذیلی سیٹ، منفی خود سیٹ: 3"),
      [(4, "That is all the subsets. Take away the set itself: 3.", "یہ تمام ذیلی سیٹ ہیں۔ خود سیٹ نکال دیں: 3", "proper_count")], qtype=None)},
 ],
 glossary=[T("Empty set", "خالی سیٹ"), T("Singleton set", "اکائی سیٹ"), T("Finite set", "محدود سیٹ"), T("Infinite set", "لامحدود سیٹ"),
           T("Subset", "ذیلی سیٹ"), T("Proper subset", "حقیقی ذیلی سیٹ"), T("Improper subset", "غیر حقیقی ذیلی سیٹ"), T("Equivalent sets", "ہم قوت سیٹ")],
 flashcards=[
   {"id": "f_equal_equiv", "front": T("Equal or equivalent sets?", "برابر یا ہم قوت سیٹ؟"),
    "back": T("Equal: the same elements. Equivalent: the same number of elements.", "برابر: ایک جیسے ارکان۔ ہم قوت: ارکان کی تعداد برابر۔")},
   {"id": "f_subsets", "front": T("How many subsets does a set with n elements have?", "n ارکان والے سیٹ کے کتنے ذیلی سیٹ ہوتے ہیں؟"),
    "back": T("2ⁿ, counting { } and the set itself. The set itself is the only improper one.", "2ⁿ، جن میں { } اور خود سیٹ شامل ہیں۔ خود سیٹ ہی واحد غیر حقیقی ہے۔")},
 ],
 home_task={"id": "h_subsets_home", "text": T(
   "Take three different fruits (or coins) from your kitchen. Lay out every way of choosing some of them, including choosing none and choosing all. How many ways did you find? Check: it should be 8.",
   "اپنے باورچی خانے سے تین مختلف پھل (یا سکے) لیں۔ ان میں سے کچھ چننے کے سب طریقے رکھ کر دکھائیں، جن میں کوئی نہ چننا اور سب چننا بھی شامل ہے۔ آپ کو کتنے طریقے ملے؟ جانچ: یہ 8 ہونے چاہییں۔")},
 notes=["Covers the empty set and the singleton set (q1, q2), finite and infinite sets (q3), cardinal numbers (q4, q5), the signs ⊂, ⊇ and ↔ (q6, q7), equal and equivalent sets (q8, q9), listing and counting subsets (q10, q11, q12) and the improper subset (q13).",
        "Each wrong answer is a real mistake: {0} taken as empty, an empty set mixed up with a singleton, a big set taken as infinite, 0 or repeated letters counted, a sign used the wrong way, equal mixed up with equivalent, and the empty set or the set itself left out.",
        "Urdu terms to check: اکائی سیٹ (singleton set), فوقی سیٹ (superset), غیر حقیقی ذیلی سیٹ (improper subset), ہم قوت (equivalent), ارکان کی تعداد (cardinal number)."],
 minutes=20,
)

figs.attach(lesson, {
    "q6_proper": figs.two_ovals(sorted(A6), sorted(B6), "Two ovals: A holds 1, 3 and 5; B holds 1, 2, 3, 4 and 5.", "دو بیضوی شکلیں: A میں 1، 3 اور 5 ہیں؛ B میں 1، 2، 3، 4 اور 5 ہیں۔", cols=2),
    "q11_list_subsets": figs.oval_figure([5, 7], "An oval named S holding 5 and 7.", "بیضوی شکل S جس میں 5 اور 7 ہیں۔", name="S"),
})
write(lesson)
