import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

REF = "PCTB Mathematics 6 (SNC 2022), Sub-domain 5: Sets"
REVIEW = {"status": "draft", "reviewed_by": None, "date": None}

# Skills from earlier work that these lessons build on.
FACTORS = "maths.factors.factors_multiples"
PRIMES = "maths.factors.primes"

# Skills of the Sets unit.
SET_MEANING = "maths.sets.meaning"
SET_KINDS = "maths.sets.kinds"
SET_SUBSETS = "maths.sets.subsets"
SET_UNION_INTERSECTION = "maths.sets.union_intersection"
SET_WORD_PROBLEMS = "maths.sets.word_problems"


def show(s):
    """A set as children write it: {2, 4, 6}, or { } when empty.
    Numbers are listed smallest first; words keep the given order."""
    items = sorted(s) if all(isinstance(x, int) for x in s) else list(s)
    return "{" + ", ".join(str(x) for x in items) + "}" if items else "{ }"


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



def number_question(id, prompt, answer: int, hint, good, bad, *, common_wrong=(), qtype="apply", skill=None, character=None):
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


