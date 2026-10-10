import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "content" / "sources"))

from why import WHY  # noqa: E402
from why_steps import add_why  # noqa: E402

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
    add_why(lesson, WHY)
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

# ---------------------------------------------------------------------------
# Practice sets that go with the book's exercises of chapter 10 (Geometrical Constructions),
# and the chapter test. Each
# practice lesson has its own skill, with the chapter's skills it practises
# as prerequisites.
UNIT_ID = "g6-maths-09"
EX_SKILL = {"10.3": "maths.geometry.ex_10_3"}


def book_ref(part):
    """'Exercise 10.1' -> the textbook string for curriculum_refs."""
    return f"PCTB Mathematics 6 (SNC 2022), Sub-domain 10: Geometrical Constructions, {part}"


def nq(id, prompt, answer, hint, good, bad, wrongs=(), qtype="apply"):
    """number_question with (en, ur) tuples; wrongs are (answer, en, ur, misconception)."""
    for w in wrongs:
        assert w[0] != answer, id
    return number_question(id, T(*prompt), answer, T(*hint), T(*good), T(*bad),
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
