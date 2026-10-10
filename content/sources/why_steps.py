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

A lesson that has no entry is left as it is (practice sets and tests).
"""

WHY_STEP = "s0_why"
USE_STEP = "s0_use"
MAX_SAY_WORDS = 20
MAX_TEXT_WORDS = 90


def add_why(lesson: dict, why: dict) -> dict:
    entry = why.get(lesson["id"])
    if entry is None:
        return lesson
    assert set(entry) == {"say", "need", "use"}, (lesson["id"], sorted(entry))
    ids = {s["id"] for s in lesson["steps"]}
    assert WHY_STEP not in ids and USE_STEP not in ids, lesson["id"]
    for key, limit in (("say", MAX_SAY_WORDS), ("need", MAX_TEXT_WORDS), ("use", MAX_TEXT_WORDS)):
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
    lesson["steps"] = steps + lesson["steps"]
    # A child part-way through the old lesson starts it again (resumeIndex),
    # rather than landing two steps early.
    lesson["version"] += 1
    lesson["estimated_minutes"] += 1
    return lesson
