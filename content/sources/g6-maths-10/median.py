from common import (T, opt, say, wrong, number_question, write,
                    BOOK, REVIEW, DH_MEAN, DH_MEDIAN)

SKILL = DH_MEDIAN


def median(*xs):
    s = sorted(xs)
    n = len(s)
    if n % 2:
        return s[n // 2]
    a, b = s[n // 2 - 1], s[n // 2]
    assert (a + b) % 2 == 0, xs  # keep every median a whole number
    return (a + b) // 2


def unsorted_middle(*xs):
    """What a child gets by taking the middle of the list as written."""
    n = len(xs)
    if n % 2:
        return xs[n // 2]
    a, b = xs[n // 2 - 1], xs[n // 2]
    assert (a + b) % 2 == 0, xs
    return (a + b) // 2


def nums(xs):
    return ", ".join(str(x) for x in xs)


def nums_ur(xs):
    return "، ".join(str(x) for x in xs)


# s1 / s3: worked example
EX = (7, 2, 9)
assert sorted(EX) == [2, 7, 9] and median(*EX) == 7
EX_EVEN = (3, 5, 9, 11)
assert median(*EX_EVEN) == 7 and 5 + 9 == 14
# s2: a mean (prerequisite)
S2 = sum((3, 5, 10)) // 3
assert S2 == 6 and sum((3, 5, 10)) == 18 and sum((3, 5, 10)) % 3 == 0
# s4: odd count, not in order
S4_DATA = (8, 3, 6)
S4 = median(*S4_DATA)
S4_WRONG = unsorted_middle(*S4_DATA)
assert S4 == 6 and S4_WRONG == 3
# s5: five test marks
S5_DATA = (6, 9, 4, 8, 5)
S5 = median(*S5_DATA)
S5_WRONG = unsorted_middle(*S5_DATA)
assert S5 == 6 and S5_WRONG == 4 and sorted(S5_DATA) == [4, 5, 6, 8, 9]
# s6: even count
S6_DATA = (12, 4, 10, 6)
S6 = median(*S6_DATA)
S6_WRONG = unsorted_middle(*S6_DATA)
assert S6 == 8 and S6_WRONG == 7 and sorted(S6_DATA) == [4, 6, 10, 12]
# s7: ages of seven cousins
S7_DATA = (11, 13, 12, 11, 14, 12, 13)
S7 = median(*S7_DATA)
S7_WRONG = unsorted_middle(*S7_DATA)
assert S7 == 12 and S7_WRONG == 11 and sorted(S7_DATA) == [11, 11, 12, 12, 13, 13, 14]
# s8: one very large value pulls the mean up, not the median
S8_DATA = (10, 20, 15, 25, 130)
S8 = median(*S8_DATA)
S8_MEAN = sum(S8_DATA) // len(S8_DATA)
S8_WRONG = unsorted_middle(*S8_DATA)
assert S8 == 20 and S8_MEAN == 40 and sum(S8_DATA) == 200 and S8_WRONG == 15
# s9: sorted even list, picks one middle value instead of halfway
S9_DATA = (3, 5, 9, 11)
assert median(*S9_DATA) == 7 and sorted(S9_DATA) == list(S9_DATA)
# s11: six values
S11_DATA = (8, 14, 6, 20, 10, 16)
S11 = median(*S11_DATA)
S11_WRONG = unsorted_middle(*S11_DATA)
assert S11 == 12 and S11_WRONG == 13 and sorted(S11_DATA) == [6, 8, 10, 14, 16, 20]
# question bank and review
QB_DATA = (15, 3, 11, 7, 9)
QB = median(*QB_DATA)
QB_WRONG = unsorted_middle(*QB_DATA)
assert QB == 9 and QB_WRONG == 11
QBE_DATA = (8, 2, 6)
assert median(*QBE_DATA) == 6 and unsorted_middle(*QBE_DATA) == 2
R1_DATA = (21, 17, 25, 19)
R1 = median(*R1_DATA)
assert R1 == 20 and sorted(R1_DATA) == [17, 19, 21, 25] and unsorted_middle(*R1_DATA) == 21
R2_DATA = (40, 50, 10, 30, 20)
R2 = median(*R2_DATA)
R2_WRONG = unsorted_middle(*R2_DATA)
assert R2 == 30 and R2_WRONG == 10

lesson = {
 "id": "g6-maths-10-median",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Find the median of a set of numbers by putting them in order and taking the middle value, or halfway between the two middle values when there is an even count.", "textbook": BOOK}],
 "skills": [SKILL],
 "title": T("Median", "وسطانیہ"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": DH_MEAN}],
 "misconceptions": [
   {"id": "forgets_to_sort", "description": "Does not put the numbers in order before looking for the middle."},
   {"id": "unsorted_middle", "description": "Takes the middle number of the list as it is written, which is not the median unless the list is in order."},
   {"id": "picks_one_middle", "description": "For an even count, gives one of the two middle values instead of the number halfway between them."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_first", "type": "recall", "step": {
     "id": "qb_first", "type": "choice",
     "prompt": T("What is the first thing to do when finding the median?", "وسطانیہ نکالتے وقت سب سے پہلے کیا کرتے ہیں؟"),
     "options": [
       opt("sort", "Put the numbers in order", "اعداد کو ترتیب میں لکھیں", True,
           "Yes! Order first, then find the middle.", "جی ہاں! پہلے ترتیب، پھر درمیان۔"),
       opt("add", "Add all the numbers", "سب اعداد جمع کریں", False,
           "Adding is for the mean. For the median, put them in order first.", "جمع کرنا اوسط کے لیے ہے۔ وسطانیہ کے لیے پہلے ترتیب دیں۔"),
       opt("middle", "Pick the middle number as written", "لکھے ہوئے اعداد میں سے درمیانی چنیں", False,
           "Only after putting them in order! Sort first.", "صرف ترتیب دینے کے بعد! پہلے ترتیب دیں۔", "forgets_to_sort"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T(f"Find the median of {nums(QB_DATA)}.", f"{nums_ur(QB_DATA)} کا وسطانیہ معلوم کریں۔"),
     QB,
     T("Put them in order first.", "پہلے ترتیب دیں۔"),
     T("Right! 9.", "درست! 9"),
     T("In order: 3, 7, 9, 11, 15. The middle one is 9.", "ترتیب میں: 3، 7، 9، 11، 15۔ درمیانی عدد 9 ہے۔"),
     common_wrong=[wrong(QB_WRONG, "11 is the middle of the list as written. In order: 3, 7, 9, 11, 15, so the median is 9.",
                         "11 لکھی ہوئی فہرست کا درمیانی عدد ہے۔ ترتیب میں: 3، 7، 9، 11، 15، تو وسطانیہ 9 ہے۔", "unsorted_middle")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T(f"Ali says the median of {nums(QBE_DATA)} is 2, because 2 is in the middle. What went wrong?",
                 f"علی کہتا ہے {nums_ur(QBE_DATA)} کا وسطانیہ 2 ہے، کیونکہ 2 درمیان میں ہے۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("sort", "He didn't sort first. In order: 2, 6, 8, so the median is 6.", "اس نے پہلے ترتیب نہیں دی۔ ترتیب میں: 2، 6، 8، تو وسطانیہ 6 ہے۔", True,
           "Yes! 2 is the smallest, so it can't be the middle.", "جی ہاں! 2 سب سے چھوٹا ہے، یہ درمیانی نہیں ہو سکتا۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "2 is the smallest number! Sort first: 2, 6, 8. The median is 6.", "2 تو سب سے چھوٹا عدد ہے! پہلے ترتیب: 2، 6، 8۔ وسطانیہ 6 ہے۔", "unsorted_middle"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_median", "front": T("Median?", "وسطانیہ؟"),
    "back": T("Put the numbers in order. The middle one is the median. 8, 3, 6 → 3, 6, 8 → 6.", "اعداد کو ترتیب دیں۔ درمیانی عدد وسطانیہ ہے۔ 8، 3، 6 ← 3، 6، 8 ← 6")},
   {"id": "f_even", "front": T("Median of an even count?", "جفت تعداد کا وسطانیہ؟"),
    "back": T("Halfway between the two middle numbers: add them and halve. 3, 5, 9, 11 → (5 + 9) ÷ 2 = 7.", "دونوں درمیانی اعداد کے بیچ کا عدد: جمع کر کے آدھا کریں۔ 3، 5، 9، 11 ← (5 + 9) ÷ 2 = 7")},
 ],
 "home_tasks": [{"id": "h_line_up", "text": T(
   "Ask five people at home their ages. Write the ages on slips of paper and line them up from youngest to oldest. Which age is in the middle? That is the median age!",
   "گھر کے پانچ افراد سے ان کی عمریں پوچھیں۔ عمریں کاغذ کی پرچیوں پر لکھ کر سب سے چھوٹی سے سب سے بڑی تک قطار بنائیں۔ درمیان میں کون سی عمر ہے؟ یہی وسطانیہ عمر ہے!")}],
 "glossary": [T("Median", "وسطانیہ"), T("In order", "ترتیب میں"), T("Middle value", "درمیانی قیمت"),
              T("Halfway", "آدھے راستے پر / بیچ میں"), T("Average (mean)", "اوسط")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Three children stand in a line by height. Who is in the middle? Easy, if they stand in order!",
                     "تین بچے قد کے حساب سے قطار میں کھڑے ہیں۔ درمیان میں کون ہے؟ آسان ہے، اگر وہ ترتیب سے کھڑے ہوں!"),
    "text": T("Today we find the median: the middle value. First, a quick check on the mean.", "آج ہم وسطانیہ نکالیں گے: درمیانی قیمت۔ پہلے اوسط پر ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("Find the mean of 3, 5 and 10.", "3، 5 اور 10 کی اوسط معلوم کریں۔"),
     S2,
     T("Total, then divide by 3.", "کل، پھر 3 سے تقسیم"),
     T("Right! 6.", "درست! 6"),
     T("3 + 5 + 10 = 18, and 18 ÷ 3 = 6.", "3 + 5 + 10 = 18، اور 18 ÷ 3 = 6"),
     common_wrong=[wrong(18, "18 is the total. Divide by 3: 6.", "18 کل ہے۔ 3 سے تقسیم کریں: 6")],
     qtype="recall", skill=DH_MEAN),
   {"id": "s3_median", "type": "explain",
    "character": say("happy", "Order first, then find the middle. That's the whole secret!", "پہلے ترتیب، پھر درمیان۔ بس یہی راز ہے!"),
    "text": T("To find the median: 1) put the numbers in order, smallest to largest; 2) the middle number is the median. For 7, 2, 9: in order 2, 7, 9, so the median is 7. If there is an even count, there are two middle numbers. The median is halfway between them: add them and halve. For 3, 5, 9, 11: (5 + 9) ÷ 2 = 7.",
              "وسطانیہ نکالنے کے لیے: 1) اعداد کو چھوٹے سے بڑے کی ترتیب میں لکھیں؛ 2) درمیانی عدد وسطانیہ ہے۔ 7، 2، 9 کے لیے: ترتیب میں 2، 7، 9، تو وسطانیہ 7 ہے۔ اگر اعداد کی تعداد جفت ہو تو دو درمیانی اعداد ہوتے ہیں۔ وسطانیہ ان کے بالکل بیچ میں ہوتا ہے: انہیں جمع کر کے آدھا کریں۔ 3، 5، 9، 11 کے لیے: (5 + 9) ÷ 2 = 7۔")},
   number_question(
     "s4_three",
     T(f"Find the median of {nums(S4_DATA)}.", f"{nums_ur(S4_DATA)} کا وسطانیہ معلوم کریں۔"),
     S4,
     T("Put them in order first.", "پہلے ترتیب دیں۔"),
     T("Right! In order: 3, 6, 8. The middle is 6.", "درست! ترتیب میں: 3، 6، 8۔ درمیانی 6 ہے۔"),
     T("In order: 3, 6, 8. The middle one is 6.", "ترتیب میں: 3، 6، 8۔ درمیانی عدد 6 ہے۔"),
     common_wrong=[wrong(S4_WRONG, "3 is in the middle of the list as written, but it is the smallest. In order: 3, 6, 8, so 6.",
                         "3 لکھی ہوئی فہرست کے درمیان ہے، لیکن یہ سب سے چھوٹا ہے۔ ترتیب میں: 3، 6، 8، تو 6۔", "unsorted_middle")]),
   number_question(
     "s5_marks",
     T(f"Hamza's quiz marks out of 10 are {nums(S5_DATA)}. What is his median mark?",
       f"حمزہ کے 10 میں سے کوئز نمبر {nums_ur(S5_DATA)} ہیں۔ اس کے نمبروں کا وسطانیہ کیا ہے؟"),
     S5,
     T("Order all five, then take the third.", "پانچوں کو ترتیب دیں، پھر تیسرا لیں۔"),
     T("Right! 6.", "درست! 6"),
     T("In order: 4, 5, 6, 8, 9. The middle one is 6.", "ترتیب میں: 4، 5، 6، 8، 9۔ درمیانی عدد 6 ہے۔"),
     common_wrong=[wrong(S5_WRONG, "4 is the middle of the list as written. Sort first: 4, 5, 6, 8, 9. The median is 6.",
                         "4 لکھی ہوئی فہرست کا درمیانی عدد ہے۔ پہلے ترتیب: 4، 5، 6، 8، 9۔ وسطانیہ 6 ہے۔", "unsorted_middle")]),
   number_question(
     "s6_even",
     T(f"Find the median of {nums(S6_DATA)}.", f"{nums_ur(S6_DATA)} کا وسطانیہ معلوم کریں۔"),
     S6,
     T("In order: 4, 6, 10, 12. Two numbers are in the middle. Add them and halve.", "ترتیب میں: 4، 6، 10، 12۔ درمیان میں دو اعداد ہیں۔ انہیں جمع کر کے آدھا کریں۔"),
     T("Right! (6 + 10) ÷ 2 = 8.", "درست! (6 + 10) ÷ 2 = 8"),
     T("In order: 4, 6, 10, 12. Halfway between 6 and 10 is (6 + 10) ÷ 2 = 8.", "ترتیب میں: 4، 6، 10، 12۔ 6 اور 10 کے بیچ میں (6 + 10) ÷ 2 = 8 ہے۔"),
     common_wrong=[wrong(6, "6 is one of the two middle numbers. The median is halfway between 6 and 10: 8.",
                         "6 دو درمیانی اعداد میں سے ایک ہے۔ وسطانیہ 6 اور 10 کے بیچ میں ہے: 8", "picks_one_middle"),
                   wrong(10, "10 is one of the two middle numbers. The median is halfway between 6 and 10: 8.",
                         "10 دو درمیانی اعداد میں سے ایک ہے۔ وسطانیہ 6 اور 10 کے بیچ میں ہے: 8", "picks_one_middle"),
                   wrong(S6_WRONG, "You used 4 and 10, the middle of the list as written. Sort first: 4, 6, 10, 12. The median is 8.",
                         "آپ نے 4 اور 10 لیے، جو لکھی ہوئی فہرست کے درمیان ہیں۔ پہلے ترتیب: 4، 6، 10، 12۔ وسطانیہ 8 ہے۔", "forgets_to_sort")]),
   number_question(
     "s7_ages",
     T(f"The ages of seven cousins are {nums(S7_DATA)}. What is the median age?",
       f"سات کزنز کی عمریں {nums_ur(S7_DATA)} ہیں۔ وسطانیہ عمر کیا ہے؟"),
     S7,
     T("Write all seven in order, keeping repeats. The 4th one is the middle.", "ساتوں کو ترتیب میں لکھیں، دہرائے ہوئے بھی۔ چوتھا درمیانی ہے۔"),
     T("Right! 12.", "درست! 12"),
     T("In order: 11, 11, 12, 12, 13, 13, 14. The 4th one is 12.", "ترتیب میں: 11، 11، 12، 12، 13، 13، 14۔ چوتھا عدد 12 ہے۔"),
     common_wrong=[wrong(S7_WRONG, "11 is the 4th number as written. Sort first: 11, 11, 12, 12, 13, 13, 14. The median is 12.",
                         "11 لکھی ہوئی فہرست میں چوتھا ہے۔ پہلے ترتیب: 11، 11، 12، 12، 13، 13، 14۔ وسطانیہ 12 ہے۔", "unsorted_middle")]),
   number_question(
     "s8_big_value",
     T(f"Five friends have saved {nums(S8_DATA)} rupees. Their mean is {S8_MEAN} rupees, because one friend saved a lot. What is the median?",
       f"پانچ دوستوں نے {nums_ur(S8_DATA)} روپے بچائے ہیں۔ ان کی اوسط {S8_MEAN} روپے ہے، کیونکہ ایک دوست نے بہت زیادہ بچائے۔ وسطانیہ کیا ہے؟"),
     S8,
     T("Order them: 10, 15, 20, 25, 130.", "ترتیب دیں: 10، 15، 20، 25، 130"),
     T("Right! 20 rupees. The big 130 pulls the mean up to 40, but the median stays at 20, closer to what most friends saved.",
       "درست! 20 روپے۔ بڑا 130 اوسط کو 40 تک کھینچ لیتا ہے، لیکن وسطانیہ 20 رہتا ہے، جو زیادہ تر دوستوں کی بچت کے قریب ہے۔"),
     T("In order: 10, 15, 20, 25, 130. The middle one is 20.", "ترتیب میں: 10، 15، 20، 25، 130۔ درمیانی عدد 20 ہے۔"),
     common_wrong=[wrong(S8_MEAN, "40 is the mean. The median is the middle value in order: 20.",
                         "40 اوسط ہے۔ وسطانیہ ترتیب میں درمیانی قیمت ہے: 20"),
                   wrong(S8_WRONG, "15 is the middle of the list as written. In order: 10, 15, 20, 25, 130, so 20.",
                         "15 لکھی ہوئی فہرست کا درمیانی عدد ہے۔ ترتیب میں: 10، 15، 20، 25، 130، تو 20۔", "unsorted_middle")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T(f"Hina finds the median of {nums(S9_DATA)}. She says it is 5. What went wrong?",
                f"حنا {nums_ur(S9_DATA)} کا وسطانیہ نکالتی ہے۔ وہ کہتی ہے یہ 5 ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("halfway", "There are two middle numbers, 5 and 9. The median is halfway: (5 + 9) ÷ 2 = 7.", "دو درمیانی اعداد ہیں، 5 اور 9۔ وسطانیہ بیچ میں ہے: (5 + 9) ÷ 2 = 7", True,
          "Yes! With an even count, take halfway between the two middle numbers.", "جی ہاں! جفت تعداد میں دونوں درمیانی اعداد کا بیچ لیں۔"),
      opt("sort", "She forgot to put them in order.", "وہ ترتیب دینا بھول گئی۔", False,
          "They are already in order. The mistake is taking only 5: the median is (5 + 9) ÷ 2 = 7.", "یہ پہلے ہی ترتیب میں ہیں۔ غلطی صرف 5 لینا ہے: وسطانیہ (5 + 9) ÷ 2 = 7 ہے۔"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "5 is only one of the two middle numbers. Halfway between 5 and 9 is 7.", "5 دو درمیانی اعداد میں سے صرف ایک ہے۔ 5 اور 9 کے بیچ میں 7 ہے۔", "picks_one_middle"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why must we put the numbers in order before finding the median? Can you teach me?",
                     "وسطانیہ نکالنے سے پہلے اعداد کو ترتیب کیوں دینا ضروری ہے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why do we sort the numbers before we pick the middle one?", "اپنے الفاظ میں بتائیں: درمیانی عدد چننے سے پہلے ہم اعداد کو ترتیب کیوں دیتے ہیں؟"),
    "key_idea": "The median is the value with as many numbers below it as above it. Only when the numbers are in order does the middle position hold that value; in a jumbled list the middle position can hold the smallest or largest number.",
    "levels": {
      "got_it": "Says the median has half the values below and half above, and only sorting puts that value in the middle position.",
      "partly": "Says sorting is needed, or that the median is the middle, without linking them.",
      "not_yet": "Gives no reason, or just repeats the rule."},
    "keywords": [
      ["order", "sort", "smallest", "ترتیب", "چھوٹ"],
      ["middle", "half", "درمیان", "آدھ", "بیچ"],
      ["below", "above", "bigger", "smaller", "اوپر", "نیچے", "بڑ"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Only in order is the middle place the true middle value.", "بہت خوب! صرف ترتیب میں ہی درمیانی جگہ پر اصل درمیانی قیمت ہوتی ہے۔"),
      "partly": T("Good start! Now say what goes wrong in the middle place if the list is jumbled.", "اچھی شروعات! اب بتائیں اگر فہرست بے ترتیب ہو تو درمیانی جگہ پر کیا غلط ہوتا ہے۔"),
      "not_yet": T("Think of 8, 3, 6. The 3 is in the middle place, but is it the middle value?", "8، 3، 6 کو سوچیں۔ 3 درمیانی جگہ پر ہے، لیکن کیا یہ درمیانی قیمت ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_six",
     T(f"Runs scored by six batters: {nums(S11_DATA)}. What is the median?",
       f"چھ بلے بازوں کے رنز: {nums_ur(S11_DATA)}۔ وسطانیہ کیا ہے؟"),
     S11,
     T("Sort all six, then find halfway between the 3rd and 4th.", "چھ کو ترتیب دیں، پھر تیسرے اور چوتھے کا بیچ نکالیں۔"),
     T("Right! (10 + 14) ÷ 2 = 12.", "درست! (10 + 14) ÷ 2 = 12"),
     T("In order: 6, 8, 10, 14, 16, 20. Halfway between 10 and 14 is 12.", "ترتیب میں: 6، 8، 10، 14، 16، 20۔ 10 اور 14 کے بیچ میں 12 ہے۔"),
     common_wrong=[wrong(10, "10 is one of the two middle numbers. Halfway between 10 and 14 is 12.",
                         "10 دو درمیانی اعداد میں سے ایک ہے۔ 10 اور 14 کے بیچ میں 12 ہے۔", "picks_one_middle"),
                   wrong(14, "14 is one of the two middle numbers. Halfway between 10 and 14 is 12.",
                         "14 دو درمیانی اعداد میں سے ایک ہے۔ 10 اور 14 کے بیچ میں 12 ہے۔", "picks_one_middle"),
                   wrong(S11_WRONG, "You used 6 and 20, the middle of the list as written. Sort first: the median is 12.",
                         "آپ نے 6 اور 20 لیے، جو لکھی ہوئی فہرست کے درمیان ہیں۔ پہلے ترتیب دیں: وسطانیہ 12 ہے۔", "forgets_to_sort")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "You can find the median now!", "اب آپ وسطانیہ نکال سکتے ہیں!"),
    "text": T("Median = the middle value once the numbers are in order. With an even count, it is halfway between the two middle numbers: add them and halve. One very large value can pull the mean up a lot, but the median hardly moves.",
              "وسطانیہ = اعداد کو ترتیب دینے کے بعد درمیانی قیمت۔ جفت تعداد ہو تو یہ دونوں درمیانی اعداد کے بیچ میں ہے: جمع کر کے آدھا کریں۔ ایک بہت بڑا عدد اوسط کو بہت اوپر لے جا سکتا ہے، لیکن وسطانیہ مشکل سے ہلتا ہے۔"),
    "points": [T("Sort first, then take the middle.", "پہلے ترتیب، پھر درمیانی۔"),
               T("Even count: add the two middle numbers and halve.", "جفت تعداد: دونوں درمیانی اعداد جمع کر کے آدھا کریں۔")]},
 ],
 "review_questions": [
   {"id": "r_median4", "type": "apply", "skill": SKILL, "step": number_question(
     "r_median4",
     T(f"Find the median of {nums(R1_DATA)}.", f"{nums_ur(R1_DATA)} کا وسطانیہ معلوم کریں۔"),
     R1,
     T("Sort, then halfway between the two middle numbers.", "ترتیب دیں، پھر دونوں درمیانی اعداد کا بیچ۔"),
     T("Right! 20.", "درست! 20"),
     T("In order: 17, 19, 21, 25. (19 + 21) ÷ 2 = 20.", "ترتیب میں: 17، 19، 21، 25۔ (19 + 21) ÷ 2 = 20"),
     common_wrong=[wrong(19, "19 is one of the two middle numbers. Halfway between 19 and 21 is 20.",
                         "19 دو درمیانی اعداد میں سے ایک ہے۔ 19 اور 21 کے بیچ میں 20 ہے۔", "picks_one_middle"),
                   wrong(21, "21 is one of the two middle numbers. Halfway between 19 and 21 is 20.",
                         "21 دو درمیانی اعداد میں سے ایک ہے۔ 19 اور 21 کے بیچ میں 20 ہے۔", "picks_one_middle")],
     qtype=None)},
   {"id": "r_median5", "type": "apply", "skill": SKILL, "step": number_question(
     "r_median5",
     T(f"Find the median of {nums(R2_DATA)}.", f"{nums_ur(R2_DATA)} کا وسطانیہ معلوم کریں۔"),
     R2,
     T("Put them in order first.", "پہلے ترتیب دیں۔"),
     T("Right! 30.", "درست! 30"),
     T("In order: 10, 20, 30, 40, 50. The middle one is 30.", "ترتیب میں: 10، 20، 30، 40، 50۔ درمیانی عدد 30 ہے۔"),
     common_wrong=[wrong(R2_WRONG, "10 is the middle of the list as written. Sort first: the median is 30.",
                         "10 لکھی ہوئی فہرست کا درمیانی عدد ہے۔ پہلے ترتیب دیں: وسطانیہ 30 ہے۔", "unsorted_middle")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Data Management sub-domain. No textbook text or exercises were used.",
   "Most lists are deliberately not in order, so the middle of the list as written is a different (wrong) number; this catches children who skip sorting. Every median is a whole number: even-count lists were chosen so the two middle values add to an even number.",
   "Step s8 compares mean and median once: one very large saving pulls the mean up to 40 while the median stays at 20.",
   "Urdu terms to check: وسطانیہ (median), اوسط (mean), ترتیب (order), جفت (even). Please confirm these match the PCTB book.",
   "The numbers were worked out in content/sources/g6-maths-10/median.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)
