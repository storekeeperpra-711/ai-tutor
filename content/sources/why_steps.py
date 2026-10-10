"""Opens a lesson with two short steps that answer "why do I need this?".

s0_why: the need that led people to the idea and what it solved (Mithu asks
the question). s0_use: where it helps in real life. Both are plain "explain"
steps, so the lesson schema is unchanged.

A unit keeps its texts in its own why.py, {lesson id: entry}, and its
common.write() calls add_why(). An entry has "say" (Mithu's one-line
question), "need" (what the problem was and what the idea solved) and "use"
(where it is used), each T(en, ur):

    "g6-maths-04-what-are-integers": {
        "say": T("Why did people need numbers below zero?", "..."),
        "need": T("...", "..."),
        "use": T("...", "..."),
    },

An entry may also have "define" (a short textbook definition, T(en, ur)); it
becomes a text-only s0_define step before s0_why, so the lesson reads:
definition, why it was needed, where it is used, then practice and quiz.

A lesson that has no entry is left as it is (practice sets and tests).
"""

WHY_STEP = "s0_why"
USE_STEP = "s0_use"
DEFINE_STEP = "s0_define"
MAX_SAY_WORDS = 20
MAX_TEXT_WORDS = 90


def add_why(lesson: dict, why: dict) -> dict:
    entry = why.get(lesson["id"])
    if entry is None:
        return lesson
    required = {"say", "need", "use"}
    assert required <= set(entry) <= required | {"define"}, (lesson["id"], sorted(entry))
    ids = {s["id"] for s in lesson["steps"]}
    assert not {WHY_STEP, USE_STEP, DEFINE_STEP} & ids, lesson["id"]
    for key, limit in (("say", MAX_SAY_WORDS), ("need", MAX_TEXT_WORDS), ("use", MAX_TEXT_WORDS), ("define", MAX_TEXT_WORDS)):
        if key not in entry:
            continue
        for lang in ("en", "ur"):
            text = entry[key][lang].strip()
            assert text, (lesson["id"], key, lang)
            assert len(text.split()) <= limit, (lesson["id"], key, lang, len(text.split()))
    steps = [
        {
            "id": WHY_STEP,
            "type": "explain",
            "character": {"emotion": "curious", "say": entry["say"]},
            "text": entry["need"],
        },
        {"id": USE_STEP, "type": "explain", "text": entry["use"]},
    ]
    if "define" in entry:
        steps.insert(0, {"id": DEFINE_STEP, "type": "explain", "text": entry["define"]})
        lesson["version"] += 1
    lesson["steps"] = steps + lesson["steps"]
    # A child part-way through the old lesson starts it again (resumeIndex),
    # rather than landing two steps early.
    lesson["version"] += 1
    lesson["estimated_minutes"] += 1
    return lesson
