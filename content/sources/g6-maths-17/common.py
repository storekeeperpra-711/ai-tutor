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
