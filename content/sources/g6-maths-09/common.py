import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

REF = "PCTB Mathematics 6 (SNC 2022), Sub-domains 9 and 10: Symmetry, Geometrical Constructions (angle facts)"
REVIEW = {"status": "draft", "reviewed_by": None, "date": None}

# Skills from earlier work that these lessons build on.
PA_TRIANGLE = "maths.measurement.area_triangle"

# Skills of the Angles unit.
AN_TYPES = "maths.geometry.angle_types"
AN_LINE = "maths.geometry.angles_on_line"
AN_PAIRS = "maths.geometry.complementary_supplementary"
AN_TRIANGLE = "maths.geometry.triangle_angles"
AN_WORD_PROBLEMS = "maths.geometry.word_problems"


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


# The five kinds of angle, smallest first, with the test that decides each.
KINDS = [
    ("acute", "Acute", "حادہ زاویہ", lambda d: 0 < d < 90),
    ("right", "Right", "قائمہ زاویہ", lambda d: d == 90),
    ("obtuse", "Obtuse", "منفرجہ زاویہ", lambda d: 90 < d < 180),
    ("straight", "Straight", "مستقیم زاویہ", lambda d: d == 180),
    ("reflex", "Reflex", "منعکس زاویہ", lambda d: 180 < d < 360),
]

RULE = {
    "acute": T("Acute angles are less than 90°.", "حادہ زاویہ 90° سے کم ہوتا ہے۔"),
    "right": T("A right angle is exactly 90°.", "قائمہ زاویہ بالکل 90° ہوتا ہے۔"),
    "obtuse": T("Obtuse angles are between 90° and 180°.", "منفرجہ زاویہ 90° اور 180° کے درمیان ہوتا ہے۔"),
    "straight": T("A straight angle is exactly 180°.", "مستقیم زاویہ بالکل 180° ہوتا ہے۔"),
    "reflex": T("Reflex angles are between 180° and 360°.", "منعکس زاویہ 180° اور 360° کے درمیان ہوتا ہے۔"),
}


def kind_of(degrees):
    found = [k for k, _, _, test in KINDS if test(degrees)]
    assert len(found) == 1, degrees
    return found[0]


def kind_question(id, degrees, prompt, *, qtype="apply", skill=None, mis=None):
    """A choice step: which kind of angle is this many degrees?
    The right option and every feedback line come from kind_of, so none
    is typed by hand."""
    right = kind_of(degrees)
    right_ur = next(ur for k, _, ur, _ in KINDS if k == right)
    step = {"id": id, "type": "choice"}
    if qtype:
        step["question_type"] = qtype
    if skill:
        step["skill"] = skill
    step["prompt"] = prompt
    step["options"] = [
        opt(k, en, ur, k == right,
            f"Yes! {degrees}° is {en.lower()}. " + RULE[k]["en"] if k == right
            else f"Not quite. {RULE[right]['en']} So {degrees}° is {right}.",
            f"جی ہاں! {degrees}° {ur} ہے۔ " + RULE[k]["ur"] if k == right
            else f"ابھی نہیں۔ {RULE[right]['ur']} اس لیے {degrees}° {right_ur} ہے۔",
            None if k == right else (mis or {}).get(k))
        for k, en, ur, _ in KINDS
    ]
    return step
