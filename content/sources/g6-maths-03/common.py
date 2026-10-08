import json
from decimal import Decimal as D
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

REF = "Not a chapter of PCTB Mathematics 6 (SNC 2022) (revision unit): Decimals"
REVIEW = {"status": "draft", "reviewed_by": None, "date": None}

# Skills from earlier work that these lessons build on.
FRACTIONS_EQUIVALENT = "maths.fractions.equivalent"

# Skills of the Decimals unit.
DEC_PLACE_VALUE = "maths.decimals.place_value"
DEC_COMPARE = "maths.decimals.compare"
DEC_ADD_SUBTRACT = "maths.decimals.add_subtract"
DEC_MULTIPLY_DIVIDE = "maths.decimals.multiply_divide"
DEC_WORD_PROBLEMS = "maths.decimals.word_problems"


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


def decimal_line(id, prompt, answer, hint, good, bad, *, lo="0", hi="1", step="0.1", start=None, common_wrong=(), qtype="apply", skill=None):
    """A number-line step with decimal labels: the child moves the marker to [answer]."""
    lo, hi, step_, answer = D(lo), D(hi), D(step), D(answer)
    start = D(start) if start is not None else lo
    assert lo <= answer <= hi and lo <= start <= hi
    assert (answer - lo) % step_ == 0 and (hi - lo) / step_ <= 20
    s = {"id": id, "type": "sim"}
    if qtype:
        s["question_type"] = qtype
    if skill:
        s["skill"] = skill
    s.update({
        "renderer": "native", "sim_id": "number_line", "prompt": prompt,
        "params": {"min": num(lo), "max": num(hi), "step": num(step_), "start": num(start), "labels": "decimal"},
        "expected": {"result": "value", "checker": "numeric", "answer": dec(answer)},
        "hint": hint, "feedback_correct": good, "feedback_wrong": bad,
    })
    if common_wrong:
        s["common_wrong"] = [dict(w, answer=dec(w["answer"])) for w in common_wrong]
    return s
