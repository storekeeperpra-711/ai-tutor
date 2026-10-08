import math

from common import (T, opt, say, wrong, number_question, write, show,
                    REF, REVIEW, SET_KINDS, SET_SUBSETS, SET_VENN)

SKILL = SET_VENN

# ---------------------------------------------------------------------------
# Venn diagram pictures. U is a lightly filled rectangle; each set is a filled
# circle inside it. Every element is a small label, and the script checks that
# each label sits inside exactly the circles of the sets it belongs to.
# ---------------------------------------------------------------------------
W, H = 100, 64
EDGE = 3            # the rectangle U is drawn this far in from the picture edge
GAP = 3             # a label keeps at least this much room from a circle line
SPACE = 7           # labels keep at least this far apart from each other
MARGIN = 0.025 * max(W, H)


def r1(v):
    return round(v, 1)


def ring(center, radius, elems, start=-90):
    """Places elements evenly round a small ring inside a circle."""
    cx, cy = center
    if len(elems) == 1:
        return {elems[0]: (cx, cy)}
    step = 360 / len(elems)
    return {e: (r1(cx + radius * math.cos(math.radians(start + i * step))),
                r1(cy + radius * math.sin(math.radians(start + i * step))))
            for i, e in enumerate(elems)}


def venn(alt, universe, sets, where, u_at=(9, 10), check=True):
    """universe: every element of U. sets: (name, center, radius, members,
    name angle). where: element -> label position."""
    items = [{"kind": "polygon", "points": [[EDGE, EDGE], [W - EDGE, EDGE], [W - EDGE, H - EDGE], [EDGE, H - EDGE]], "fill": True}]
    labels = [("U", u_at)]
    for name, (cx, cy), r, members, angle in sets:
        assert EDGE + 2 <= cx - r and cx + r <= W - EDGE - 2 and EDGE + 2 <= cy - r and cy + r <= H - EDGE - 2, name
        if check:
            assert set(members) <= set(universe), name
        items.append({"kind": "circle", "center": [cx, cy], "radius": r, "fill": True})
        d = r + 5
        at = (r1(cx + d * math.cos(math.radians(angle))), r1(cy + d * math.sin(math.radians(angle))))
        labels.append((name, at))
    assert set(where) == set(universe)
    labels += [(str(e), where[e]) for e in universe]
    for text, (x, y) in labels:
        assert MARGIN <= x - EDGE and x <= W - EDGE - MARGIN and MARGIN <= y - EDGE and y <= H - EDGE - MARGIN, (text, x, y)
    for i, (a, pa) in enumerate(labels):
        for b, pb in labels[i + 1:]:
            assert math.dist(pa, pb) >= SPACE, (a, b)
    # A set's name sits just outside its own circle.
    for (name, (cx, cy), r, _, _), (_, at) in zip(sets, labels[1:]):
        assert math.dist(at, (cx, cy)) >= r + GAP, name
    if check:
        for e in universe:
            for name, c, r, members, _ in sets:
                d = math.dist(where[e], c)
                assert (d <= r - GAP) if e in members else (d >= r + GAP), (e, name)
    items += [{"kind": "label", "at": list(at), "text": text.strip()} for text, at in labels]
    return {"width": W, "height": H, "alt": alt, "items": items}


def outside_count(universe, *sets):
    return len(set(universe) - set().union(*sets))


# s2: {2, 4} and {1, 2, 3, 4}
assert {2, 4} <= {1, 2, 3, 4} and not {1, 2, 3, 4} <= {2, 4}

# s3: U = 1 to 10, A = even numbers
U3 = list(range(1, 11))
A3 = [n for n in U3 if n % 2 == 0]
assert A3 == [2, 4, 6, 8, 10] and outside_count(U3, A3) == 5
FIG3 = venn(
    T("A rectangle marked U holds the numbers 1 to 10. Inside it is a circle marked A holding 2, 4, 6, 8 and 10. The numbers 1, 3, 5, 7 and 9 are inside the rectangle but outside the circle.",
      "ایک مستطیل پر U لکھا ہے، اس میں 1 سے 10 تک اعداد ہیں۔ اس کے اندر ایک دائرہ A ہے جس میں 2، 4، 6، 8 اور 10 ہیں۔ اعداد 1، 3، 5، 7 اور 9 مستطیل کے اندر لیکن دائرے سے باہر ہیں۔"),
    U3, [("A", (58, 32), 22, A3, 225)],
    {**ring((58, 32), 12, A3), 1: (14, 22), 3: (26, 36), 5: (14, 50), 7: (89, 16), 9: (89, 48)})

# s4: U = 1 to 12, A = multiples of 3; 7 is in U but not in A
U4 = list(range(1, 13))
A4 = [n for n in U4 if n % 3 == 0]
assert 7 in U4 and 7 not in A4
FIG4 = venn(
    T("A rectangle U holds the numbers 1 to 12. A circle A inside it holds 3, 6, 9 and 12. The numbers 1, 2, 4, 5, 7, 8, 10 and 11 are in the rectangle outside the circle.",
      "مستطیل U میں 1 سے 12 تک اعداد ہیں۔ اس کے اندر دائرہ A میں 3، 6، 9 اور 12 ہیں۔ اعداد 1، 2، 4، 5، 7، 8، 10 اور 11 مستطیل میں دائرے سے باہر ہیں۔"),
    U4, [("A", (60, 32), 20, A4, 225)],
    {**ring((60, 32), 10, A4),
     1: (14, 20), 2: (28, 20), 4: (14, 34), 5: (28, 34), 7: (14, 48), 8: (28, 48), 10: (89, 18), 11: (89, 46)})

# s5: a cricket team, players 1 to 11; A = players who bowled today
U5 = list(range(1, 12))
A5 = [3, 5, 8, 10, 11]
S5 = len(A5)
assert S5 == 5 and len(U5) == 11 and outside_count(U5, A5) == 6
FIG5 = venn(
    T("A rectangle U holds the shirt numbers 1 to 11 of a cricket team. A circle A inside it holds 3, 5, 8, 10 and 11. The numbers 1, 2, 4, 6, 7 and 9 are in the rectangle outside the circle.",
      "مستطیل U میں کرکٹ ٹیم کی قمیضوں کے نمبر 1 سے 11 تک ہیں۔ اس کے اندر دائرہ A میں 3، 5، 8، 10 اور 11 ہیں۔ نمبر 1، 2، 4، 6، 7 اور 9 مستطیل میں دائرے سے باہر ہیں۔"),
    U5, [("A", (62, 32), 21, A5, 225)],
    {**ring((62, 32), 11.5, A5),
     1: (14, 20), 2: (28, 20), 4: (14, 34), 6: (28, 34), 7: (14, 48), 9: (28, 48)})

# s6: U = letters of PAKISTAN, V = its vowels
U6 = list(dict.fromkeys("PAKISTAN"))
V6 = [c for c in U6 if c in "AEIOU"]
assert U6 == list("PAKISTN") and V6 == ["A", "I"]
FIG6 = venn(
    T("A rectangle U holds the letters P, A, K, I, S, T and N. A circle V inside it holds A and I. The letters P, K, S, T and N are in the rectangle outside the circle.",
      "مستطیل U میں حروف P، A، K، I، S، T اور N ہیں۔ اس کے اندر دائرہ V میں A اور I ہیں۔ حروف P، K، S، T اور N مستطیل میں دائرے سے باہر ہیں۔"),
    U6, [("V", (60, 32), 16, V6, 225)],
    {**ring((60, 32), 7, V6, start=180),
     "P": (14, 22), "K": (28, 22), "S": (14, 44), "T": (28, 44), "N": (88, 48)})

# s7: U = 1 to 12, P = prime numbers; how many elements of U are outside P?
U7 = list(range(1, 13))
P7 = [n for n in U7 if n > 1 and all(n % d for d in range(2, n))]
S7 = outside_count(U7, P7)
assert P7 == [2, 3, 5, 7, 11] and S7 == 7
FIG7 = venn(
    T("A rectangle U holds the numbers 1 to 12. A circle P inside it holds 2, 3, 5, 7 and 11. The numbers 1, 4, 6, 8, 9, 10 and 12 are in the rectangle outside the circle.",
      "مستطیل U میں 1 سے 12 تک اعداد ہیں۔ اس کے اندر دائرہ P میں 2، 3، 5، 7 اور 11 ہیں۔ اعداد 1، 4، 6، 8، 9، 10 اور 12 مستطیل میں دائرے سے باہر ہیں۔"),
    U7, [("P", (62, 32), 21, P7, 225)],
    {**ring((62, 32), 11.5, P7),
     1: (14, 20), 4: (28, 20), 6: (14, 34), 8: (28, 34), 9: (14, 48), 10: (28, 48), 12: (89, 50)})

# s8: a subset drawn inside: B = multiples of 4 inside A = even numbers
U8 = list(range(1, 11))
A8 = [n for n in U8 if n % 2 == 0]
B8 = [n for n in U8 if n % 4 == 0]
assert B8 == [4, 8] and set(B8) < set(A8) and not set(A8) <= set(B8)
FIG8 = venn(
    T("A rectangle U holds the numbers 1 to 10. Inside it a big circle A holds 2, 6 and 10, and a small circle B drawn inside A holds 4 and 8. The numbers 1, 3, 5, 7 and 9 are outside both circles.",
      "مستطیل U میں 1 سے 10 تک اعداد ہیں۔ اس کے اندر بڑے دائرے A میں 2، 6 اور 10 ہیں، اور A کے اندر بنے چھوٹے دائرے B میں 4 اور 8 ہیں۔ اعداد 1، 3، 5، 7 اور 9 دونوں دائروں سے باہر ہیں۔"),
    U8, [("A", (56, 32), 25, A8, 225), ("B", (64, 32), 10, B8, 300)],
    {4: (60, 32), 8: (68, 32), 2: (42, 22), 6: (40, 36), 10: (48, 48),
     1: (13, 22), 3: (13, 40), 5: (22, 54), 7: (89, 14), 9: (89, 50)})

# s9: Hamza draws B = {4, 8} as a separate circle next to A = {2, 4, 6, 8, 10}
# (his picture is wrong on purpose, so the membership check is off).
FIG9 = venn(
    T("Hamza's drawing: a rectangle U with two separate circles side by side. Circle A holds 2, 4, 6, 8 and 10. Circle B, outside A, holds 4 and 8 again.",
      "حمزہ کی تصویر: مستطیل U میں دو الگ الگ دائرے ساتھ ساتھ ہیں۔ دائرہ A میں 2، 4، 6، 8 اور 10 ہیں۔ A سے باہر دائرہ B میں دوبارہ 4 اور 8 ہیں۔"),
    ["2", "4", "6", "8", "10", "4 ", "8 "],
    [("A", (32, 34), 19, [], 225), ("B", (76, 34), 12, [], 315)],
    {**ring((32, 34), 10.5, ["2", "4", "6", "8", "10"]), **ring((76, 34), 6, ["4 ", "8 "], start=180)},
    check=False)

# s11: a cricket team, B = batters, W = bowlers, no player in both
U11 = list(range(1, 12))
B11, W11 = [1, 2, 3, 4, 5], [8, 9, 10, 11]
assert not set(B11) & set(W11)
S11 = outside_count(U11, B11, W11)
assert S11 == 2 and len(B11) + len(W11) == 9
FIG11 = venn(
    T("A rectangle U holds the shirt numbers 1 to 11. Two separate circles that do not touch are inside it: circle B holds 1, 2, 3, 4 and 5, and circle W holds 8, 9, 10 and 11. The numbers 6 and 7 are outside both circles.",
      "مستطیل U میں قمیضوں کے نمبر 1 سے 11 تک ہیں۔ اس کے اندر دو الگ دائرے ہیں جو ایک دوسرے کو نہیں چھوتے: دائرہ B میں 1، 2، 3، 4 اور 5 ہیں، اور دائرہ W میں 8، 9، 10 اور 11 ہیں۔ نمبر 6 اور 7 دونوں دائروں سے باہر ہیں۔"),
    U11, [("B", (30, 30), 17, B11, 135), ("W", (72, 30), 15, W11, 315)],
    {**ring((30, 30), 9, B11), **ring((72, 30), 8, W11, start=-45), 6: (42, 55), 7: (58, 55)})

# question bank: U = 1 to 8, A = factors of 8; 3 is outside A
UQ = list(range(1, 9))
AQ = [n for n in UQ if 8 % n == 0]
assert AQ == [1, 2, 4, 8] and 3 not in AQ
FIGQ = venn(
    T("A rectangle U holds the numbers 1 to 8. A circle A inside it holds 1, 2, 4 and 8. The numbers 3, 5, 6 and 7 are in the rectangle outside the circle.",
      "مستطیل U میں 1 سے 8 تک اعداد ہیں۔ اس کے اندر دائرہ A میں 1، 2، 4 اور 8 ہیں۔ اعداد 3، 5، 6 اور 7 مستطیل میں دائرے سے باہر ہیں۔"),
    UQ, [("A", (60, 32), 18, AQ, 225)],
    {**ring((60, 32), 9, AQ), 3: (16, 22), 5: (30, 22), 6: (16, 44), 7: (30, 44)})
# months of the year with 31 days
MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
QB = sum(1 for d in MONTH_DAYS if d != 31)
assert QB == 5 and sum(1 for d in MONTH_DAYS if d == 31) == 7

# review
R1 = len([n for n in range(1, 11) if n % 2])
assert R1 == 5
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
TDAYS = [d for d in DAYS if d.startswith("T")]
R2 = len(DAYS) - len(TDAYS)
assert TDAYS == ["Tuesday", "Thursday"] and R2 == 5

lesson = {
 "id": "g6-maths-01-universal-set-and-venn-diagrams",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Recognise the universal set U (p. 75) and use Venn diagrams to represent sets (5.3, 5.3.1) and subsets (5.3.2): draw U as a rectangle and sets as circles inside it, and read elements, n(A) and the tabular form from a diagram.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("The universal set and Venn diagrams", "عالمی سیٹ اور وین ڈایاگرام"),
 "estimated_minutes": 15,
 "prerequisites": [{"skill": SET_SUBSETS}, {"skill": SET_KINDS}],
 "misconceptions": [
   {"id": "counts_universal", "description": "Counts every element in the rectangle U when asked for n(A) or for the elements of A."},
   {"id": "outside_is_in", "description": "Thinks an element drawn in the rectangle but outside a circle belongs to that set."},
   {"id": "subset_outside", "description": "Draws a subset as a separate circle instead of inside the bigger set's circle."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_rectangle", "type": "recall", "step": {
     "id": "qb_rectangle", "type": "choice",
     "prompt": T("In a Venn diagram, what does the rectangle show?", "وین ڈایاگرام میں مستطیل کیا دکھاتی ہے؟"),
     "options": [
       opt("universal", "The universal set U: all the elements we are talking about", "عالمی سیٹ U: وہ تمام رکن جن کی ہم بات کر رہے ہیں", True,
           "Yes! Every other set is drawn inside it.", "جی ہاں! باقی ہر سیٹ اس کے اندر بنتا ہے۔"),
       opt("subset", "The smallest set", "سب سے چھوٹا سیٹ", False,
           "The rectangle is the biggest: U holds everything under discussion.", "مستطیل سب سے بڑی ہے: U میں زیرِ بحث سب کچھ ہے۔"),
       opt("empty", "The empty set", "خالی سیٹ", False,
           "The rectangle is U, the set of all the elements we are talking about.", "مستطیل U ہے، ان تمام رکنوں کا سیٹ جن کی ہم بات کر رہے ہیں۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("U = the months of the year. A = the months with 31 days. A has 7 elements. How many months of U are outside the circle A?",
       "U = سال کے مہینے۔ A = وہ مہینے جن میں 31 دن ہوں۔ A کے 7 رکن ہیں۔ U کے کتنے مہینے دائرہ A سے باہر ہیں؟"),
     QB,
     T("n(U) = 12. Take away the 7 inside A.", "n(U) = 12۔ A کے اندر والے 7 نفی کریں۔"),
     T("Right! 12 − 7 = 5 months.", "درست! 12 − 7 = 5 مہینے"),
     T("12 − 7 = 5 months are outside A.", "12 − 7 = 5 مہینے A سے باہر ہیں۔"),
     common_wrong=[wrong(7, "7 are inside A. Outside A: 12 − 7 = 5.", "7 تو A کے اندر ہیں۔ A سے باہر: 12 − 7 = 5"),
                   wrong(12, "12 is n(U), all the months. Outside A: 12 − 7 = 5.", "12 تو n(U) ہے، سب مہینے۔ A سے باہر: 12 − 7 = 5", "counts_universal")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "figure": FIGQ,
     "prompt": T("Look at the Venn diagram. Ayesha says 3 ∈ A, because 3 is in the picture. What went wrong?",
                 "وین ڈایاگرام دیکھیں۔ عائشہ کہتی ہے 3 ∈ A، کیونکہ 3 تصویر میں ہے۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("outside", "3 is inside U but outside the circle A, so 3 ∉ A.", "3، U کے اندر لیکن دائرہ A سے باہر ہے، اس لیے 3 ∉ A۔", True,
           "Yes! Only the elements inside the circle belong to A.", "جی ہاں! صرف دائرے کے اندر والے رکن A کے ہیں۔"),
       opt("nothing", "Nothing, everything in the picture is in A.", "کوئی غلطی نہیں، تصویر کی ہر چیز A میں ہے۔", False,
           "The rectangle is U. A is only what is inside its circle: 1, 2, 4, 8.", "مستطیل U ہے۔ A صرف اس کے دائرے کے اندر ہے: 1، 2، 4، 8", "outside_is_in"),
       opt("not_u", "3 is not in U either.", "3، U میں بھی نہیں۔", False,
           "3 is inside the rectangle, so 3 ∈ U. It is outside the circle, so 3 ∉ A.", "3 مستطیل کے اندر ہے، تو 3 ∈ U۔ یہ دائرے سے باہر ہے، تو 3 ∉ A۔"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_universal", "front": T("Universal set U?", "عالمی سیٹ U؟"),
    "back": T("The set of all the elements under discussion. In a Venn diagram it is the rectangle.", "زیرِ بحث تمام رکنوں کا سیٹ۔ وین ڈایاگرام میں یہ مستطیل ہے۔")},
   {"id": "f_subset_circle", "front": T("How do we draw B ⊆ A in a Venn diagram?", "وین ڈایاگرام میں B ⊆ A کیسے بناتے ہیں؟"),
    "back": T("Circle B inside circle A, both inside the rectangle U.", "دائرہ B دائرہ A کے اندر، اور دونوں مستطیل U کے اندر۔")},
 ],
 "home_tasks": [{"id": "h_week", "text": T(
   "With a ruler, draw a rectangle on paper and write U = the days of the week in its corner. Inside it, draw a circle S for the days you go to school, and write those days inside the circle. Write the other days inside the rectangle but outside the circle. What is n(S)?",
   "فٹے سے کاغذ پر ایک مستطیل بنائیں اور کونے میں لکھیں U = ہفتے کے دن۔ اس کے اندر ایک دائرہ S بنائیں ان دنوں کے لیے جب آپ سکول جاتے ہیں، اور وہ دن دائرے میں لکھیں۔ باقی دن مستطیل کے اندر لیکن دائرے سے باہر لکھیں۔ n(S) کتنا ہے؟")}],
 "glossary": [T("Universal set", "عالمی سیٹ"), T("Venn diagram", "وین ڈایاگرام"), T("Tabular form", "جدولی شکل"),
              T("Descriptive form", "بیانیہ شکل"), T("Subset", "ذیلی سیٹ"), T("Element", "رکن")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "At the bazaar, one big basket holds all the fruit. The mangoes sit in a small bowl inside it. Can we draw sets like that?",
                     "بازار میں ایک بڑی ٹوکری میں سارے پھل ہیں۔ آم اس کے اندر ایک چھوٹے پیالے میں رکھے ہیں۔ کیا ہم سیٹ بھی ایسے بنا سکتے ہیں؟"),
    "text": T("Today we meet the universal set and learn to draw sets as pictures called Venn diagrams. First, a quick check.",
              "آج ہم عالمی سیٹ سے ملیں گے اور سیٹوں کو تصویر کی شکل میں بنانا سیکھیں گے جسے وین ڈایاگرام کہتے ہیں۔ پہلے ایک چھوٹا سا سوال۔")},
   {"id": "s2_foundation", "type": "choice", "question_type": "recall", "skill": SET_SUBSETS,
    "prompt": T("A = {2, 4} and B = {1, 2, 3, 4}. Which is true?", "A = {2, 4} اور B = {1, 2, 3, 4}۔ کون سا درست ہے؟"),
    "options": [
      opt("a_in_b", "A ⊆ B", "A ⊆ B", True, "Yes! 2 and 4 are both in B.", "جی ہاں! 2 اور 4 دونوں B میں ہیں۔"),
      opt("b_in_a", "B ⊆ A", "B ⊆ A", False, "1 and 3 are in B but not in A, so B is not a subset of A. A ⊆ B.", "1 اور 3، B میں ہیں لیکن A میں نہیں، اس لیے B، A کا ذیلی سیٹ نہیں۔ A ⊆ B"),
      opt("neither", "Neither", "کوئی بھی نہیں", False, "Every element of A is in B, so A ⊆ B.", "A کا ہر رکن B میں ہے، اس لیے A ⊆ B"),
    ]},
   {"id": "s3_venn", "type": "explain",
    "character": say("happy", "The rectangle holds everything we are talking about. Each circle is one set inside it!",
                     "مستطیل میں وہ سب ہے جس کی ہم بات کر رہے ہیں۔ ہر دائرہ اس کے اندر ایک سیٹ ہے!"),
    "figure": FIG3,
    "text": T(f"The universal set U is the set of all the elements under discussion. Here U = {show(U3)}. In a Venn diagram we draw U as a rectangle and each set as a circle (or oval) inside it, and write the elements in their places. A = {show(A3)} (tabular form), or A = the even numbers in U (descriptive form). The elements 2, 4, 6, 8, 10 go inside the circle, so 6 ∈ A. The other elements of U go inside the rectangle but outside the circle, so 5 ∈ U but 5 ∉ A. Counting the circle gives n(A) = {len(A3)}.",
              f"عالمی سیٹ U زیرِ بحث تمام رکنوں کا سیٹ ہے۔ یہاں U = {show(U3)}۔ وین ڈایاگرام میں U کو مستطیل اور ہر سیٹ کو اس کے اندر دائرے (یا بیضوی شکل) کی صورت میں بناتے ہیں، اور رکن ان کی جگہ پر لکھتے ہیں۔ A = {show(A3)} (جدولی شکل)، یا A = U کے جفت اعداد (بیانیہ شکل)۔ رکن 2، 4، 6، 8، 10 دائرے کے اندر آتے ہیں، اس لیے 6 ∈ A۔ U کے باقی رکن مستطیل کے اندر لیکن دائرے سے باہر آتے ہیں، اس لیے 5 ∈ U لیکن 5 ∉ A۔ دائرے کے رکن گننے سے n(A) = {len(A3)}۔")},
   {"id": "s4_where_7", "type": "choice",
    "figure": FIG4,
    "prompt": T("Look at the Venn diagram. Which is true about 7?", "وین ڈایاگرام دیکھیں۔ 7 کے بارے میں کون سا درست ہے؟"),
    "options": [
      opt("u_not_a", "7 ∈ U but 7 ∉ A", "7 ∈ U لیکن 7 ∉ A", True,
          "Yes! 7 is inside the rectangle but outside the circle.", "جی ہاں! 7 مستطیل کے اندر لیکن دائرے سے باہر ہے۔"),
      opt("in_a", "7 ∈ A", "7 ∈ A", False,
          "7 is outside the circle A, so 7 ∉ A. A = {3, 6, 9, 12}.", "7 دائرہ A سے باہر ہے، اس لیے 7 ∉ A۔ A = {3, 6, 9, 12}", "outside_is_in"),
      opt("not_u", "7 ∉ U", "7 ∉ U", False,
          "7 is inside the rectangle, so 7 ∈ U. Every element in the picture belongs to U.", "7 مستطیل کے اندر ہے، اس لیے 7 ∈ U۔ تصویر کا ہر رکن U کا ہے۔"),
    ]},
   number_question(
     "s5_count",
     T("A cricket team's shirt numbers make the set U. The circle A shows the players who bowled today. What is n(A)?",
       "کرکٹ ٹیم کی قمیضوں کے نمبر سیٹ U بناتے ہیں۔ دائرہ A ان کھلاڑیوں کو دکھاتا ہے جنہوں نے آج بولنگ کی۔ n(A) کتنا ہے؟"),
     S5,
     T("Count only the numbers inside the circle.", "صرف دائرے کے اندر والے نمبر گنیں۔"),
     T("Right! A = {3, 5, 8, 10, 11}, so n(A) = 5.", "درست! A = {3, 5, 8, 10, 11}، تو n(A) = 5"),
     T("Inside the circle are 3, 5, 8, 10 and 11: n(A) = 5.", "دائرے کے اندر 3، 5، 8، 10 اور 11 ہیں: n(A) = 5"),
     common_wrong=[wrong(11, "11 is n(U), the whole team. Count only inside the circle: 5.", "11 تو n(U) ہے، پوری ٹیم۔ صرف دائرے کے اندر گنیں: 5", "counts_universal"),
                   wrong(6, "6 players are outside the circle. Inside it are 5.", "6 کھلاڑی دائرے سے باہر ہیں۔ اندر 5 ہیں۔", "outside_is_in")]) | {"figure": FIG5},
   {"id": "s6_tabular", "type": "choice",
    "figure": FIG6,
    "prompt": T("U is the set of letters of the word PAKISTAN, and V is the set of its vowels. Which writes V in tabular form?",
                "U لفظ PAKISTAN کے حروف کا سیٹ ہے، اور V اس کے حروفِ علت کا سیٹ ہے۔ کون سا V کو جدولی شکل میں لکھتا ہے؟"),
    "options": [
      opt("vowels", "V = {A, I}", "V = {A, I}", True,
          "Yes! Only A and I are inside the circle.", "جی ہاں! صرف A اور I دائرے کے اندر ہیں۔"),
      opt("all", "V = {P, A, K, I, S, T, N}", "V = {P, A, K, I, S, T, N}", False,
          "That is U, every letter in the rectangle. V is only inside the circle: {A, I}.", "یہ U ہے، مستطیل کا ہر حرف۔ V صرف دائرے کے اندر ہے: {A, I}", "counts_universal"),
      opt("outside", "V = {P, K, S, T, N}", "V = {P, K, S, T, N}", False,
          "Those letters are outside the circle, so they are not in V. V = {A, I}.", "یہ حروف دائرے سے باہر ہیں، اس لیے V میں نہیں۔ V = {A, I}", "outside_is_in"),
    ]},
   number_question(
     "s7_outside",
     T("U = {1, 2, 3, …, 12} and P is the set of prime numbers in U. How many elements of U are outside the circle P?",
       "U = {1, 2, 3, …, 12} اور P، U کے مفرد اعداد کا سیٹ ہے۔ U کے کتنے رکن دائرہ P سے باہر ہیں؟"),
     S7,
     T("n(U) = 12 and n(P) = 5. Or count the numbers outside the circle.", "n(U) = 12 اور n(P) = 5۔ یا دائرے سے باہر والے اعداد گنیں۔"),
     T("Right! 1, 4, 6, 8, 9, 10, 12: that is 7.", "درست! 1، 4، 6، 8، 9، 10، 12: یعنی 7"),
     T("12 − 5 = 7. They are 1, 4, 6, 8, 9, 10 and 12.", "12 − 5 = 7۔ یہ 1، 4، 6، 8، 9، 10 اور 12 ہیں۔"),
     common_wrong=[wrong(5, "5 is n(P), the numbers inside the circle. Outside: 12 − 5 = 7.", "5 تو n(P) ہے، دائرے کے اندر والے۔ باہر: 12 − 5 = 7"),
                   wrong(12, "12 is all of U. Leave out the 5 primes: 7.", "12 تو پورا U ہے۔ 5 مفرد نکالیں: 7", "counts_universal")]) | {"figure": FIG7},
   {"id": "s8_subset_inside", "type": "choice",
    "figure": FIG8,
    "prompt": T("U = {1, 2, …, 10}, A = the even numbers in U and B = the multiples of 4 in U. Circle B is drawn inside circle A. Which is true?",
                "U = {1, 2, …, 10}، A = U کے جفت اعداد اور B = U میں 4 کے اضعاف۔ دائرہ B دائرہ A کے اندر بنا ہے۔ کون سا درست ہے؟"),
    "options": [
      opt("b_sub_a", "B ⊂ A", "B ⊂ A", True,
          "Yes! 4 and 8 are even too, so every element of B is in A.", "جی ہاں! 4 اور 8 جفت بھی ہیں، اس لیے B کا ہر رکن A میں ہے۔"),
      opt("a_sub_b", "A ⊂ B", "A ⊂ B", False,
          "2, 6 and 10 are in A but not in B. The smaller circle B is the subset: B ⊂ A.", "2، 6 اور 10، A میں ہیں لیکن B میں نہیں۔ چھوٹا دائرہ B ذیلی سیٹ ہے: B ⊂ A"),
      opt("apart", "A and B have no elements in common", "A اور B کا کوئی رکن مشترک نہیں", False,
          "4 and 8 are in both, because B is drawn inside A: B ⊂ A.", "4 اور 8 دونوں میں ہیں، کیونکہ B، A کے اندر بنا ہے: B ⊂ A", "subset_outside"),
    ]},
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "figure": FIG9,
    "prompt": T("U = {1, 2, …, 10}, A = {2, 4, 6, 8, 10} and B = {4, 8}. Hamza draws circle B next to circle A, not touching it, and writes 4 and 8 in both circles. What went wrong?",
                "U = {1, 2, …, 10}، A = {2, 4, 6, 8, 10} اور B = {4, 8}۔ حمزہ دائرہ B کو دائرہ A کے ساتھ الگ بناتا ہے، اور 4 اور 8 دونوں دائروں میں لکھتا ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("inside", "B ⊂ A, so circle B should be inside circle A, with 4 and 8 written once.", "B ⊂ A، اس لیے دائرہ B دائرہ A کے اندر ہونا چاہیے، اور 4 اور 8 ایک ہی بار لکھے جائیں۔", True,
          "Yes! A subset's circle goes inside the bigger set's circle.", "جی ہاں! ذیلی سیٹ کا دائرہ بڑے سیٹ کے دائرے کے اندر بنتا ہے۔"),
      opt("bigger", "Circle B should be bigger than circle A.", "دائرہ B دائرہ A سے بڑا ہونا چاہیے۔", False,
          "B has fewer elements. The mistake is where B is: it belongs inside A.", "B کے رکن کم ہیں۔ غلطی B کی جگہ میں ہے: یہ A کے اندر ہونا چاہیے۔"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "Each element is written once in a Venn diagram. Since B ⊂ A, draw B inside A.", "وین ڈایاگرام میں ہر رکن ایک بار لکھا جاتا ہے۔ چونکہ B ⊂ A، B کو A کے اندر بنائیں۔", "subset_outside"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why do we draw the circle of a subset inside the circle of the bigger set? Can you teach me?",
                     "ذیلی سیٹ کا دائرہ بڑے سیٹ کے دائرے کے اندر کیوں بناتے ہیں؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: if B ⊆ A, why is circle B drawn inside circle A?",
              "اپنے الفاظ میں بتائیں: اگر B ⊆ A ہو تو دائرہ B دائرہ A کے اندر کیوں بنتا ہے؟"),
    "key_idea": "Every element of B is also an element of A. Each element is written only once, so the elements of B must be inside A's circle as well, which puts the whole circle B inside circle A.",
    "levels": {
      "got_it": "Says every element of B is also in A, so B's elements (and so its circle) must lie inside A's circle.",
      "partly": "Says B is smaller or part of A, without saying every element of B is in A.",
      "not_yet": "Gives no reason, or says it is just how it is drawn."},
    "keywords": [
      ["every", "all", "each", "ہر", "تمام", "har"],
      ["element", "member", "رکن", "rukn"],
      ["inside", "also", "in a", "اندر", "بھی", "andar"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Every element of B is in A, so B sits inside A.", "بہت خوب! B کا ہر رکن A میں ہے، اس لیے B، A کے اندر ہے۔"),
      "partly": T("Good start! Now say what is true about every element of B.", "اچھی شروعات! اب بتائیں B کے ہر رکن کے بارے میں کیا سچ ہے۔"),
      "not_yet": T("Take A = {2, 4, 6, 8} and B = {4, 8}. Is 4 in A? Is 8 in A? So where must 4 and 8 be written?", "A = {2, 4, 6, 8} اور B = {4, 8} لیں۔ کیا 4، A میں ہے؟ کیا 8، A میں ہے؟ تو 4 اور 8 کہاں لکھے جائیں؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_two_sets",
     T("U is a cricket team, shirt numbers 1 to 11. B = the batters and W = the bowlers. No player is in both, so the two circles do not touch. How many players are outside both circles?",
       "U ایک کرکٹ ٹیم ہے، قمیضوں کے نمبر 1 سے 11۔ B = بلے باز اور W = گیند باز۔ کوئی کھلاڑی دونوں میں نہیں، اس لیے دونوں دائرے ایک دوسرے کو نہیں چھوتے۔ کتنے کھلاڑی دونوں دائروں سے باہر ہیں؟"),
     S11,
     T("n(U) = 11. Take away n(B) and n(W).", "n(U) = 11۔ n(B) اور n(W) نفی کریں۔"),
     T("Right! 6 and 7: 2 players.", "درست! 6 اور 7: دو کھلاڑی"),
     T("11 − 5 − 4 = 2. They are 6 and 7.", "11 − 5 − 4 = 2۔ یہ 6 اور 7 ہیں۔"),
     common_wrong=[wrong(9, "9 players are inside the circles. Outside both: 11 − 9 = 2.", "9 کھلاڑی دائروں کے اندر ہیں۔ دونوں سے باہر: 11 − 9 = 2"),
                   wrong(11, "11 is the whole team, n(U). Outside both circles: 2.", "11 تو پوری ٹیم، n(U) ہے۔ دونوں دائروں سے باہر: 2", "counts_universal")]) | {"figure": FIG11},
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Rectangle for U, circles for sets, and a subset inside its bigger set. Well done!",
                     "U کے لیے مستطیل، سیٹوں کے لیے دائرے، اور ذیلی سیٹ اپنے بڑے سیٹ کے اندر۔ شاباش!"),
    "figure": FIG8,
    "text": T("The universal set U holds all the elements under discussion; in a Venn diagram it is a rectangle. Each set is a circle inside it, with its elements written inside. Elements outside a circle are in U but not in that set (∉). If B ⊆ A, circle B goes inside circle A. Two sets with no common elements are drawn as separate circles. To read a set, list what is inside its circle (tabular form) and count it for n(A).",
              "عالمی سیٹ U میں زیرِ بحث تمام رکن ہوتے ہیں؛ وین ڈایاگرام میں یہ مستطیل ہے۔ ہر سیٹ اس کے اندر ایک دائرہ ہے، جس کے رکن اس میں لکھے ہوتے ہیں۔ دائرے سے باہر کے رکن U میں ہیں لیکن اس سیٹ میں نہیں (∉)۔ اگر B ⊆ A ہو تو دائرہ B دائرہ A کے اندر آتا ہے۔ جن دو سیٹوں کا کوئی رکن مشترک نہ ہو وہ الگ الگ دائروں میں بنتے ہیں۔ سیٹ پڑھنے کے لیے اس کے دائرے کے رکن لکھیں (جدولی شکل) اور n(A) کے لیے گنیں۔"),
    "points": [T("Rectangle = U; circle = a set.", "مستطیل = U؛ دائرہ = ایک سیٹ۔"),
               T("Subset: a circle inside a circle.", "ذیلی سیٹ: دائرے کے اندر دائرہ۔")]},
 ],
 "review_questions": [
   {"id": "r_odd", "type": "apply", "skill": SKILL, "step": number_question(
     "r_odd",
     T("U = {1, 2, …, 10}. In a Venn diagram, circle A holds the odd numbers of U. What is n(A)?",
       "U = {1, 2, …, 10}۔ وین ڈایاگرام میں دائرہ A میں U کے طاق اعداد ہیں۔ n(A) کتنا ہے؟"),
     R1,
     T("A = {1, 3, 5, …}. Count them.", "A = {1, 3, 5, …}۔ انہیں گنیں۔"),
     T("Right! A = {1, 3, 5, 7, 9}, so n(A) = 5.", "درست! A = {1, 3, 5, 7, 9}، تو n(A) = 5"),
     T("A = {1, 3, 5, 7, 9}: n(A) = 5.", "A = {1, 3, 5, 7, 9}: n(A) = 5"),
     common_wrong=[wrong(10, "10 is n(U). Count only the odd numbers: 5.", "10 تو n(U) ہے۔ صرف طاق اعداد گنیں: 5", "counts_universal")],
     qtype=None)},
   {"id": "r_days", "type": "apply", "skill": SKILL, "step": number_question(
     "r_days",
     T("U = the days of the week. Circle T holds the days whose English name starts with T: Tuesday and Thursday. How many days are outside circle T?",
       "U = ہفتے کے دن۔ دائرہ T میں وہ دن ہیں جن کا انگریزی نام T سے شروع ہو: Tuesday اور Thursday۔ کتنے دن دائرہ T سے باہر ہیں؟"),
     R2,
     T("n(U) = 7 and n(T) = 2.", "n(U) = 7 اور n(T) = 2"),
     T("Right! 7 − 2 = 5 days.", "درست! 7 − 2 = 5 دن"),
     T("7 − 2 = 5 days are outside T.", "7 − 2 = 5 دن T سے باہر ہیں۔"),
     common_wrong=[wrong(2, "2 days are inside T. Outside: 7 − 2 = 5.", "2 دن T کے اندر ہیں۔ باہر: 7 − 2 = 5"),
                   wrong(7, "7 is all the days, n(U). Outside T: 5.", "7 تو سب دن، n(U) ہے۔ T سے باہر: 5", "counts_universal")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Sets unit. No textbook text or exercises were used.",
   "Follows the book's order: the universal set U (p. 75), then 5.3 Venn diagrams: 5.3.1 representing a set and 5.3.2 representing a subset. Union and intersection are deliberately not taught here.",
   "Every picture is drawn by the app from the figure data; the script checks that each number or letter sits inside exactly the circles of the sets it belongs to (Hamza's wrong drawing in s9 is the only exception, on purpose).",
   "The vowel set in s6 is called V, not A, so its name does not clash with the letter A inside it.",
   "Urdu terms to check: عالمی سیٹ (universal set; some books use کائناتی سیٹ), وین ڈایاگرام (Venn diagram), جدولی شکل (tabular form), بیانیہ شکل (descriptive form), حروفِ علت (vowels), اضعاف (multiples).",
   "The numbers and pictures were worked out in content/sources/g6-maths-01/universal_set_venn.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)
