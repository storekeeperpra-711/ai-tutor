import json
from decimal import Decimal as D
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

REF = "PCTB Grade 6 Mathematics (unit to be confirmed): Simplification"
REVIEW = {"status": "draft", "reviewed_by": None, "date": None}

# Skills from earlier work that these lessons build on.
INT_MULTIPLY_DIVIDE = "maths.integers.multiply_divide"
DEC_PLACE_VALUE = "maths.decimals.place_value"
DEC_MULTIPLY_DIVIDE = "maths.decimals.multiply_divide"
FRACTIONS_ADD_UNLIKE = "maths.fractions.add_unlike"
FRACTIONS_MULTIPLY = "maths.fractions.multiply"

# Skills of the Simplification unit.
SM_ORDER = "maths.simplify.order_of_operations"
SM_BRACKETS = "maths.simplify.brackets"
SM_FRACTIONS_DECIMALS = "maths.simplify.fractions_decimals"
SM_ESTIMATE = "maths.simplify.estimation"
SM_WORD_PROBLEMS = "maths.simplify.word_problems"

def percent_of(p, amount):
    """p% of amount, as an exact Decimal."""
    return D(p) * D(amount) / 100


def as_percent(part, whole):
    """part out of whole as a percent, as an exact Decimal."""
    return D(part) * 100 / D(whole)

def num(x):
    """A Decimal as a plain JSON number: D('0.70') -> 0.7, D('3') -> 3."""
    if isinstance(x, D):
        x = x.normalize()
        return int(x) if x == x.to_integral_value() else float(x)
    return x


def dec(x) -> str:
    """A Decimal as children write it: 0.7, 12.05, 3."""
    x = D(x).normalize()
    return f"{x:f}" if x != x.to_integral_value() else str(int(x))


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
    """A step whose answer is a number. A Decimal answer is written as a JSON number."""
    step = {"id": id, "type": "number"}
    if qtype:
        step["question_type"] = qtype
    if skill:
        step["skill"] = skill
    if character:
        step["character"] = character
    step.update({"prompt": prompt, "answer": num(answer), "checker": "numeric",
                 "hint": hint, "feedback_correct": good, "feedback_wrong": bad})
    if common_wrong:
        step["common_wrong"] = [dict(w, answer=num(w["answer"])) for w in common_wrong]
    return step



def check_lesson(lesson):
    """Checks before writing: no common wrong answer equals the right one,
    and Mithu's lines are short."""
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
                assert w["answer"].replace(" ", "") != step["expected"].replace(" ", ""), step["id"]
        if step["type"] == "sim":
            exp = step["expected"]["answer"]
            assert exp not in [w["answer"] for w in step.get("common_wrong", [])], step["id"]
        if step["type"] == "number":
            assert step["answer"] not in [w["answer"] for w in step.get("common_wrong", [])], step["id"]
        if step["type"] == "choice":
            assert sum(o["correct"] for o in step["options"]) == 1, step["id"]
        line = step.get("character")
        if line:
            for lang in ("en", "ur"):
                assert len(line["say"][lang].split()) <= 30, (step["id"], lang)


def write(lesson):
    check_lesson(lesson)
    path = ROOT / "content" / "lessons" / f"{lesson['id']}.json"
    path.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wrote", path.name)


