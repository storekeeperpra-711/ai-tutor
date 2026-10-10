import json
import sys
from fractions import Fraction as F
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "content" / "sources"))

from why import WHY  # noqa: E402
from why_steps import add_why  # noqa: E402

BOOK = "PCTB Mathematics 6 (SNC 2022), Sub-domain 12: Probability"
REVIEW = {"status": "draft", "reviewed_by": None, "date": None}

# Skills from earlier work that these lessons build on.
SET_MEANING = "maths.sets.meaning"
RATIO_MEANING = "maths.ratio.meaning"

# Skills of the Probability unit.
PR_SAMPLE_SPACE = "maths.probability.sample_space"
PR_SINGLE_EVENT = "maths.probability.single_event"
PR_LIKELIHOOD = "maths.probability.likelihood"
PR_WORD_PROBLEMS = "maths.probability.word_problems"

# Sample spaces, built in code so no outcome is missed or counted twice.
COIN = ["H", "T"]
DICE = [1, 2, 3, 4, 5, 6]


def coins(n):
    """Every outcome of tossing n coins: coins(2) is HH, HT, TH, TT."""
    return ["".join(p) for p in product(COIN, repeat=n)]


def balls(**colours):
    """One outcome per ball: balls(red=3, blue=2) has 5 outcomes."""
    return [c for c, n in colours.items() for _ in range(n)]


def P(event, space):
    """P(E) = n(E) / n(S), where event is a test on one outcome."""
    return F(sum(1 for o in space if event(o)), len(space))


def frac(x) -> str:
    """3/4, or 2 for a whole number."""
    x = F(x)
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


VOWELS = set("AEIOU")

assert coins(2) == ["HH", "HT", "TH", "TT"] and len(coins(3)) == 8
assert P(lambda o: o % 2 == 0, DICE) == F(1, 2)
assert P(lambda o: o == "red", balls(red=3, blue=2, green=5)) == F(3, 10)


def T(en, ur):
    return {"en": en, "ur": ur}


def opt(id, en, ur, correct, fen, fur, mis=None):
    o = {"id": id, "text": T(en, ur), "correct": correct, "feedback": T(fen, fur)}
    if mis:
        o["misconception_id"] = mis
    return o


def say(emotion, en, ur):
    return {"emotion": emotion, "say": T(en, ur)}


def wrong(answer, en, ur, mis=None):
    w = {"answer": answer, "feedback": T(en, ur)}
    if mis:
        w["misconception_id"] = mis
    return w


def number_question(id, prompt, answer, hint, good, bad, *, common_wrong=(), qtype="apply", skill=None, character=None):
    """A step whose answer is a whole number."""
    step = {"id": id, "type": "number"}
    if qtype:
        step["question_type"] = qtype
    if skill:
        step["skill"] = skill
    if character:
        step["character"] = character
    step.update({"prompt": prompt, "answer": answer, "checker": "numeric",
                 "hint": hint, "feedback_correct": good, "feedback_wrong": bad})
    if common_wrong:
        step["common_wrong"] = list(common_wrong)
    return step


def probability_question(id, prompt, answer: F, hint, good, bad, *, common_wrong=(), qtype="apply", skill=None, character=None):
    """A typed probability, checked by value: 3/6, 1/2 and 0.5 are all right."""
    step = {"id": id, "type": "text_check"}
    if qtype:
        step["question_type"] = qtype
    if skill:
        step["skill"] = skill
    if character:
        step["character"] = character
    step.update({
        "prompt": prompt, "checker": "fraction", "expected": frac(answer),
        "hint": hint, "feedback_correct": good, "feedback_wrong": bad,
    })
    if common_wrong:
        step["common_wrong"] = list(common_wrong)
    return step


def word(p):
    """Where a probability sits on the scale."""
    if p == 0:
        return "impossible"
    if p == 1:
        return "certain"
    if p == F(1, 2):
        return "even_chance"
    return "likely" if p > F(1, 2) else "unlikely"


SCALE = [
  ("impossible", "Impossible", "ناممکن"),
  ("unlikely", "Unlikely", "کم امکان"),
  ("even_chance", "Even chance", "برابر امکان"),
  ("likely", "Likely", "زیادہ امکان"),
  ("certain", "Certain", "یقینی"),
]


def scale_question(id, prompt, answer, good, why_en, why_ur, *, qtype="apply", mis=None):
    """A choice of the five words on the probability scale."""
    assert answer in [k for k, _, _ in SCALE]
    step = {"id": id, "type": "choice"}
    if qtype:
        step["question_type"] = qtype
    step["prompt"] = prompt
    step["options"] = [
        opt(k, en, ur, k == answer,
            *(good if k == answer else (why_en, why_ur)), None if k == answer else mis)
        for k, en, ur in SCALE
    ]
    return step


def check_lesson(lesson):
    """Checks before writing: no common wrong answer has the right value,
    each choice has one right option, and Mithu's lines are short."""
    def steps():
        yield from lesson["steps"]
        for qs in lesson["question_bank"].values():
            for q in qs:
                yield q["step"]
        for q in lesson.get("review_questions", []):
            yield q["step"]
    for step in steps():
        if step["type"] == "text_check":
            for w in step.get("common_wrong", []):
                assert F(w["answer"]) != F(step["expected"]), step["id"]
        if step["type"] == "number":
            assert step["answer"] not in [w["answer"] for w in step.get("common_wrong", [])], step["id"]
        if step["type"] == "choice":
            assert sum(o["correct"] for o in step["options"]) == 1, step["id"]
        line = step.get("character")
        if line:
            for lang in ("en", "ur"):
                assert len(line["say"][lang].split()) <= 30, (step["id"], lang)


def write(lesson):
    add_why(lesson, WHY)
    check_lesson(lesson)
    path = ROOT / "content" / "lessons" / f"{lesson['id']}.json"
    path.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wrote", path.name)


# ---------------------------------------------------------------------------
# Practice sets that go with the book's exercises of chapter 12 (Probability), and the
# chapter test. Each practice lesson has its own skill, with the chapter's
# skills it practises as prerequisites.
UNIT_ID = "g6-maths-17"
EX_SKILL = {"12.1": "maths.probability.ex_12_1"}
CHAPTER_12_TEST = "maths.probability.chapter_12_test"


def book_ref(part):
    """'Exercise 12.1' -> the textbook string for curriculum_refs."""
    return f"{BOOK}, {part}"


def nq(id, prompt, answer, hint, good, bad, wrongs=(), qtype="apply"):
    """number_question with (en, ur) tuples; wrongs are (answer, en, ur, misconception)."""
    for w in wrongs:
        assert w[0] != answer, id
    return number_question(id, T(*prompt), answer, T(*hint), T(*good), T(*bad),
                           common_wrong=[wrong(a, en, ur, mis) for a, en, ur, mis in wrongs], qtype=qtype)


def pq(id, prompt, answer, hint, good, bad, wrongs=(), qtype="apply"):
    """probability_question with (en, ur) tuples; wrongs are (answer string, en, ur, misconception)."""
    for w in wrongs:
        assert F(w[0]) != F(answer), id
    return probability_question(id, T(*prompt), answer, T(*hint), T(*good), T(*bad),
                                common_wrong=[wrong(a, en, ur, mis) for a, en, ur, mis in wrongs], qtype=qtype)


def ch(id, prompt, right, wrongs, pos, qtype="apply"):
    """A choice step with (en, ur) prompt. right is (en, ur, feedback_en,
    feedback_ur); each wrong is the same plus an optional misconception. The
    right option goes at index pos."""
    options = [opt("x", right[0], right[1], True, right[2], right[3])]
    for w in wrongs:
        options.append(opt("x", w[0], w[1], False, w[2], w[3], w[4] if len(w) > 4 else None))
    options.insert(pos, options.pop(0))
    for k, o in enumerate(options):
        o["id"] = "abcd"[k]
    step = {"id": id, "type": "choice"}
    if qtype:
        step["question_type"] = qtype
    step.update({"prompt": T(*prompt), "options": options})
    return step


def practice_lesson(ex, *, script, title, outcome, prerequisites, misconceptions, steps,
                    bank, review, glossary, flashcards, home_task, notes, minutes=18):
    """A practice set to use next to Exercise `ex` of the book: its own
    skill, mastered with recall, apply and find_error questions."""
    skill = EX_SKILL[ex]
    return {
        "id": UNIT_ID + "-exercise-" + ex.replace(".", "-"),
        "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
        "curriculum_refs": [{"outcome": outcome, "textbook": book_ref(f"Exercise {ex}")}],
        "skills": [skill],
        "title": title,
        "estimated_minutes": minutes,
        "prerequisites": [{"skill": s} for s in prerequisites],
        "misconceptions": misconceptions,
        "mastery_criteria": {skill: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
        "question_bank": {skill: bank},
        "flashcards": flashcards,
        "home_tasks": [home_task],
        "glossary": glossary,
        "steps": steps,
        "review_questions": [dict(q, skill=skill) for q in review],
        "teacher_notes": [
            f"A practice set to use next to Exercise {ex} of the PCTB Mathematics 6 book. Only the exercise number and the kinds of question come from the book; every question, number and story here is new, because the book may not be copied.",
            *notes,
            f"The numbers were worked out in content/sources/{UNIT_ID}/{script}; edit that script, not this file.",
        ],
        "review": REVIEW,
    }


def practice_intro(ex, kinds_en, kinds_ur, line_en, line_ur):
    """The first step: which exercise of the book this set goes with."""
    return {"id": "s1_intro", "type": "explain",
            "character": say("encouraging", line_en, line_ur),
            "text": T(f"This practice set goes with Exercise {ex} of your maths book (PCTB Mathematics 6). {kinds_en} The questions are new, not the book's, and go from easy to harder. You can keep your book open beside you.",
                      f"یہ پریکٹس آپ کی ریاضی کی کتاب (پنجاب ٹیکسٹ بک بورڈ، ریاضی 6) کی مشق {ex} کے ساتھ ہے۔ {kinds_ur} سوال نئے ہیں، کتاب والے نہیں، اور آسان سے مشکل کی طرف جاتے ہیں۔ آپ اپنی کتاب ساتھ کھول کر رکھ سکتے ہیں۔")}
