#!/usr/bin/env python3
"""Check lesson files against the lesson schema and the rules a schema can't express.

Usage:
    python tools/validate_lessons.py                 # every file in content/lessons/
    python tools/validate_lessons.py path/to/a.json  # only the given files

Exits with status 1 if any lesson has a problem, printing one line per problem.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "content" / "schema" / "lesson.schema.json"
LESSONS_DIR = ROOT / "content" / "lessons"
ASSETS = ROOT / "assets"

# Simulations must work offline: no links to anything outside the file.
EXTERNAL = re.compile(r"""(?:src|href)\s*=\s*["']?(?:https?:)?//|url\(\s*["']?(?:https?:)?//|\bfetch\s*\(|XMLHttpRequest|WebSocket|@import""", re.I)

# Params each native interactive can't do without.
NATIVE_PARAMS = {"balance_scale": ["equation"], "atom_balancer": ["equation"]}

FILE_NAME = re.compile(r"^g([0-9]|1[0-2])-[a-z][a-z_]*-[0-9]{2}-[a-z0-9]+(-[a-z0-9]+)*\.json$")


def load_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=Draft202012Validator.FORMAT_CHECKER)


def all_steps(lesson: dict):
    """Yield (where, step) for every step in the lesson, including nested ones."""
    for step in lesson.get("steps", []):
        yield "steps", step
    for alt in lesson.get("alternatives", []):
        for step in alt.get("steps", []):
            yield f"alternatives/{alt.get('id')}", step
    for skill, questions in lesson.get("question_bank", {}).items():
        for q in questions:
            yield f"question_bank/{skill}", q.get("step", {})
    for q in lesson.get("review_questions", []):
        yield "review_questions", q.get("step", {})


def check_rules(lesson: dict, path: Path) -> list[str]:
    """Rules that JSON Schema can't express. Assumes the schema already passed."""
    problems = []

    if not FILE_NAME.match(path.name):
        problems.append(f"file name '{path.name}' must look like g6-maths-02-dividing-fractions.json")
    if lesson["id"] != path.stem:
        problems.append(f"id '{lesson['id']}' must equal the file name '{path.stem}'")
    grade_in_id = int(lesson["id"].split("-")[0][1:])
    if grade_in_id != lesson["grade"]:
        problems.append(f"grade {lesson['grade']} doesn't match the id (g{grade_in_id})")
    subject_in_id = lesson["id"].split("-")[1]
    if subject_in_id != lesson["subject"]:
        problems.append(f"subject '{lesson['subject']}' doesn't match the id ('{subject_in_id}')")

    seen = set()
    for step in lesson["steps"]:
        if step["id"] in seen:
            problems.append(f"step id '{step['id']}' is used twice")
        seen.add(step["id"])

    misconceptions = {m["id"] for m in lesson["misconceptions"]}
    for where, step in all_steps(lesson):
        refs = [o.get("misconception_id") for o in step.get("options", [])]
        refs += [w.get("misconception_id") for w in step.get("common_wrong", [])]
        for ref in refs:
            if ref is not None and ref not in misconceptions:
                problems.append(f"{where}/{step['id']}: misconception '{ref}' is not in misconceptions")

        if step.get("type") == "choice" and not any(o["correct"] for o in step["options"]):
            problems.append(f"{where}/{step['id']}: choice step has no correct option")

        if step.get("type") == "number":
            answers = [w["answer"] for w in step.get("common_wrong", [])]
            if step["answer"] in answers:
                problems.append(f"{where}/{step['id']}: the correct answer is also listed in common_wrong")

        if step.get("type") == "text_check":
            def squash(text: str) -> str:
                return "".join(text.split()).lower()
            right = {squash(step["expected"]), *(squash(a) for a in step.get("accept", []))}
            if step["checker"] != "linear_equation" and any(
                squash(w["answer"]) in right for w in step.get("common_wrong", [])
            ):
                problems.append(f"{where}/{step['id']}: a correct answer is also listed in common_wrong")
            if "accept" in step and step["checker"] != "text":
                problems.append(f"{where}/{step['id']}: 'accept' only works with the text checker")

    for where, step in all_steps(lesson):
        problems += [f"{where}/{step.get('id')}: {p}" for p in check_media(step)]
        problems += [f"{where}/{step.get('id')}: {p}" for p in check_ai_step(step)]

    problems += check_voice(lesson)

    # The AI server finds AI steps by id anywhere in the lesson.
    ai_ids = [s["id"] for _, s in all_steps(lesson) if s.get("type") in AI_STEPS]
    all_ids = [s.get("id") for _, s in all_steps(lesson)]
    for step_id in sorted(set(ai_ids)):
        if all_ids.count(step_id) > 1:
            problems.append(f"AI step id '{step_id}' must be unique in the whole lesson")

    skills = set(lesson["skills"])
    for field in ("mastery_criteria", "question_bank"):
        for skill in lesson[field]:
            if skill not in skills:
                problems.append(f"{field}: skill '{skill}' is not in skills")
    for q in lesson.get("review_questions", []):
        if "skill" in q and q["skill"] not in skills:
            problems.append(f"review_questions/{q['id']}: skill '{q['skill']}' is not in skills")

    # Steps may test the lesson's skills or a prerequisite (foundation check).
    known = skills | {p["skill"] for p in lesson["prerequisites"]}
    for where, step in all_steps(lesson):
        if "skill" in step and step["skill"] not in known:
            problems.append(f"{where}/{step['id']}: skill '{step['skill']}' is not a skill or prerequisite of this lesson")

    step_ids = {step["id"] for step in lesson["steps"]}
    for alt in lesson.get("alternatives", []):
        if "for_step" in alt and alt["for_step"] not in step_ids:
            problems.append(f"alternatives/{alt['id']}: for_step '{alt['for_step']}' is not a step")

    # Mastery must be reachable: every required question type needs a question.
    available = evidence_types(lesson)
    for skill, criteria in lesson["mastery_criteria"].items():
        for qtype in criteria["question_types"]:
            if qtype not in available.get(skill, set()):
                problems.append(
                    f"mastery_criteria/{skill}: no '{qtype}' question (tag a step with question_type or add one to question_bank)"
                )

    return problems


def check_media(step: dict) -> list[str]:
    """Files used by sim, video and lottie steps exist and are allowed."""
    problems = []
    kind = step.get("type")
    if kind == "sim":
        if step["renderer"] == "webview":
            path = ASSETS / "sims" / step["src"]
            if not path.exists():
                problems.append(f"simulation file assets/sims/{step['src']} doesn't exist")
            elif EXTERNAL.search(path.read_text(encoding="utf-8")):
                problems.append(f"assets/sims/{step['src']} loads something from outside the file (it must work offline)")
        else:
            for key in NATIVE_PARAMS.get(step["sim_id"], []):
                if key not in step.get("params", {}):
                    problems.append(f"{step['sim_id']} needs params.{key}")
        expected = step.get("expected")
        if expected and expected["checker"] == "numeric":
            try:
                float(expected["answer"])
            except ValueError:
                problems.append(f"expected answer '{expected['answer']}' is not a number")
        if "question_type" in step and not expected:
            problems.append("question_type needs 'expected' (a sim without a question can't show mastery)")
    elif kind == "video":
        for field in ("src", "captions"):
            for lang, path in step.get(field, {}).items():
                if path.startswith("https://"):
                    continue
                file = ASSETS / "videos" / path
                if not file.exists():
                    problems.append(f"{field}.{lang}: assets/videos/{path} doesn't exist")
                elif field == "captions" and not file.read_text(encoding="utf-8").startswith("WEBVTT"):
                    problems.append(f"captions.{lang}: assets/videos/{path} is not a WebVTT file")
    elif kind == "lottie":
        if not (ASSETS / "lottie" / step["src"]).exists():
            problems.append(f"assets/lottie/{step['src']} doesn't exist")
    return problems


AI_STEPS = ("ai_explain", "photo_check")

AUDIO = ASSETS / "audio"
LANGUAGES = ("en", "ur")
# Mithu speaks at about 2.5 words a second; a line must fit in 30 seconds.
MAX_LINE_SECONDS = 30
WORDS_PER_SECOND = 2.5
MOUTH_PER_SECOND = 20


def voice_file(lesson_id: str, step_id: str, lang: str) -> str:
    """The recording's name in assets/audio (see lib/character/voice_lines.dart)."""
    return f"{lesson_id}__{step_id}_{lang}.m4a"


def mouth_file(audio: str) -> str:
    return audio.rsplit(".", 1)[0] + ".mouth"


def voice_files(lesson: dict) -> set[str]:
    """Every recording file name this lesson's Mithu lines can use."""
    names = set()
    for _, step in all_steps(lesson):
        line = step.get("character")
        if line:
            for lang in LANGUAGES:
                names.add(line.get("audio", {}).get(lang) or voice_file(lesson["id"], step["id"], lang))
    return names


def check_voice(lesson: dict) -> list[str]:
    """Mithu's lines: short enough to say, and recordings that exist and fit."""
    problems = []
    seen: dict[str, str] = {}
    for where, step in all_steps(lesson):
        line = step.get("character")
        if not line:
            continue
        name = f"{where}/{step['id']}"
        if step["id"] in seen and seen[step["id"]] != where:
            problems.append(f"{name}: steps where Mithu speaks need an id unique in the whole lesson (recordings are named after it)")
        seen.setdefault(step["id"], where)
        for lang in LANGUAGES:
            words = len(line["say"][lang].split())
            if words / WORDS_PER_SECOND > MAX_LINE_SECONDS:
                problems.append(f"{name}: Mithu's {lang} line has {words} words, more than {MAX_LINE_SECONDS} seconds to say")
            explicit = line.get("audio", {}).get(lang)
            audio = explicit or voice_file(lesson["id"], step["id"], lang)
            if not (AUDIO / audio).exists():
                if explicit:
                    problems.append(f"{name}: audio.{lang}: assets/audio/{audio} doesn't exist")
                continue
            mouth = AUDIO / mouth_file(audio)
            if not mouth.exists():
                problems.append(f"{name}: assets/audio/{mouth.name} is missing (the recorder makes it with the recording)")
            elif len(mouth.read_text(encoding="utf-8").strip()) > MAX_LINE_SECONDS * MOUTH_PER_SECOND:
                problems.append(f"{name}: the {lang} recording is longer than {MAX_LINE_SECONDS} seconds")
    return problems


def check_unused_audio(lessons: list[dict]) -> list[str]:
    """Recordings no lesson line uses (a typo in a name, or a deleted step)."""
    used = set()
    for lesson in lessons:
        for audio in voice_files(lesson):
            used |= {audio, mouth_file(audio)}
    return [
        f"assets/audio/{f.name} isn't used by any Mithu line"
        for f in sorted(AUDIO.glob("*"))
        if f.is_file() and not f.name.startswith(".") and f.name not in used
    ]


def check_ai_step(step: dict) -> list[str]:
    """Rules for ai_explain and photo_check steps."""
    problems = []
    if step.get("type") == "ai_explain":
        for i, group in enumerate(step["keywords"]):
            if any(word != word.strip() or not word.strip() for word in group):
                problems.append(f"keywords group {i + 1} has an empty word or extra spaces")
    elif step.get("type") == "photo_check":
        expected, checker = step["expected"], step["checker"]
        if checker == "numeric":
            try:
                float(expected)
            except ValueError:
                problems.append(f"expected '{expected}' is not a number")
        elif checker == "linear_equation" and expected.count("=") != 1:
            problems.append(f"expected '{expected}' must be one equation with one '='")
        elif checker == "chem_equation" and "->" not in expected:
            problems.append(f"expected '{expected}' must be an equation with '->'")
    return problems


def evidence_types(lesson: dict) -> dict[str, set[str]]:
    """Question types the lesson can ask, per skill (steps, alternatives, bank, reviews)."""
    default = lesson["skills"][0]
    found: dict[str, set[str]] = {}
    for step in lesson["steps"] + [s for alt in lesson.get("alternatives", []) for s in alt["steps"]]:
        if "question_type" in step:
            found.setdefault(step.get("skill", default), set()).add(step["question_type"])
    for skill, questions in lesson["question_bank"].items():
        for q in questions:
            found.setdefault(q.get("skill", skill), set()).add(q["type"])
    for q in lesson.get("review_questions", []):
        found.setdefault(q.get("skill", default), set()).add(q["type"])
    return found


def check_prerequisite_loops(lessons: list[dict]) -> list[str]:
    """Skills must not depend on themselves through prerequisites."""
    needs: dict[str, set[str]] = {}
    for lesson in lessons:
        for skill in lesson["skills"]:
            needs.setdefault(skill, set()).update(p["skill"] for p in lesson["prerequisites"])

    problems = []
    state: dict[str, str] = {}

    def visit(skill: str, path: list[str]) -> None:
        if state.get(skill) == "done":
            return
        if state.get(skill) == "visiting":
            loop = path[path.index(skill):] + [skill]
            problems.append("prerequisite loop: " + " -> ".join(loop))
            return
        state[skill] = "visiting"
        for need in sorted(needs.get(skill, ())):
            visit(need, path + [skill])
        state[skill] = "done"

    for skill in sorted(needs):
        visit(skill, [])
    return problems


def validate_file(path: Path, validator: Draft202012Validator) -> list[str]:
    try:
        lesson = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"not valid JSON: {e}"]

    errors = sorted(validator.iter_errors(lesson), key=lambda e: list(e.absolute_path))
    if errors:
        return [f"{'/'.join(map(str, e.absolute_path)) or '(top level)'}: {e.message}" for e in errors]
    return check_rules(lesson, path)


def main(argv: list[str]) -> int:
    validator = load_validator()
    paths = [Path(p) for p in argv] or sorted(LESSONS_DIR.glob("*.json"))
    if not paths:
        print("No lesson files found.")
        return 0

    failed = 0
    valid = []
    for path in paths:
        problems = validate_file(path, validator)
        if not problems:
            valid.append(json.loads(path.read_text(encoding="utf-8")))
        if problems:
            failed += 1
            print(f"FAIL {path.name}")
            for p in problems:
                print(f"  - {p}")
        else:
            print(f"ok   {path.name}")

    loops = check_prerequisite_loops(valid)
    if not argv:
        loops += check_unused_audio(valid)
    for problem in loops:
        print(f"FAIL {problem}")

    print(f"\n{len(paths) - failed} of {len(paths)} lessons valid.")
    return 1 if failed or loops else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
