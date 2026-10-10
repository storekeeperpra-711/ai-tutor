"""Tests for validate_lessons.py. Run: python -m unittest discover tools"""

import copy
import json
import tempfile
import unittest
from pathlib import Path

import validate_lessons as v

EQUATIONS = v.LESSONS_DIR / "g9-maths-05-solving-linear-equations.json"
SAMPLE = v.LESSONS_DIR / "g6-maths-02-dividing-fractions.json"


class ValidateLessonsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.validator = v.load_validator()
        cls.lesson = json.loads(SAMPLE.read_text(encoding="utf-8"))

    def check(self, lesson, name=None):
        name = name or f"{lesson['id']}.json"
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / name
            path.write_text(json.dumps(lesson, ensure_ascii=False), encoding="utf-8")
            return v.validate_file(path, self.validator)

    def mutated(self):
        return copy.deepcopy(self.lesson)

    def assertProblem(self, problems, text):
        self.assertTrue(any(text in p for p in problems), f"'{text}' not in {problems}")

    def test_sample_lesson_is_valid(self):
        self.assertEqual(v.validate_file(SAMPLE, self.validator), [])

    def first_spoken(self, lesson):
        return next(s for s in lesson["steps"] if "character" in s)

    def test_why_steps_open_the_lesson(self):
        lesson = self.mutated()
        text = {"en": "Why?", "ur": "کیوں؟"}
        why = {"id": "s0_why", "type": "explain", "text": text, "character": {"emotion": "curious", "say": text}}
        use = {"id": "s0_use", "type": "explain", "text": text}
        lesson["version"] = 2
        lesson["steps"] = [why, use] + lesson["steps"]
        self.assertEqual(self.check(lesson), [])
        late = self.mutated()
        late["version"] = 2
        late["steps"] = [late["steps"][0], why, use] + late["steps"][1:]
        self.assertProblem(self.check(late), "must be the first two steps")
        speaking = copy.deepcopy(lesson)
        speaking["steps"][1]["character"] = {"emotion": "happy", "say": text}
        self.assertProblem(self.check(speaking), "s0_use is text only")
        old = copy.deepcopy(lesson)
        old["version"] = 1
        self.assertProblem(self.check(old), "version 2 or more")

    def test_mithu_line_must_fit_in_30_seconds(self):
        lesson = self.mutated()
        self.first_spoken(lesson)["character"]["say"]["en"] = "word " * 80
        self.assertProblem(self.check(lesson), "more than 30 seconds to say")

    def test_named_recording_must_exist(self):
        lesson = self.mutated()
        self.first_spoken(lesson)["character"]["audio"] = {"ur": "nope.m4a"}
        self.assertProblem(self.check(lesson), "assets/audio/nope.m4a doesn't exist")

    def test_recordings_need_a_short_mouth_file(self):
        lesson = self.mutated()
        step = self.first_spoken(lesson)
        audio = v.voice_file(lesson["id"], step["id"], "ur")
        old = v.AUDIO
        with tempfile.TemporaryDirectory() as d:
            v.AUDIO = Path(d)
            try:
                (v.AUDIO / audio).write_bytes(b"x")
                self.assertProblem(self.check(lesson), "is missing (the recorder makes it")
                (v.AUDIO / v.mouth_file(audio)).write_text("5" * 700)
                self.assertProblem(self.check(lesson), "recording is longer than 30 seconds")
                (v.AUDIO / v.mouth_file(audio)).write_text("5" * 100)
                self.assertEqual(self.check(lesson), [])
                (v.AUDIO / "typo__s1_ur.m4a").write_bytes(b"x")
                self.assertEqual(
                    v.check_unused_audio([lesson]),
                    ["assets/audio/typo__s1_ur.m4a isn't used by any Mithu line"],
                )
            finally:
                v.AUDIO = old

    def test_counting_lesson_rules(self):
        lesson = json.loads((v.LESSONS_DIR / "g0-maths-01-count-the-mangoes.json").read_text(encoding="utf-8"))
        self.assertEqual(self.check(lesson), [])
        pick = next(s for s in lesson["steps"] if s["type"] == "pick_picture")
        pick["options"][0]["picture"]["value"] = pick["show"]["value"]
        self.assertProblem(self.check(lesson), "exactly one picture must show")
        pick["options"][0]["picture"] = {"kind": "fingers", "value": 7}
        self.assertProblem(self.check(lesson), "0 to 5 fingers")
        tap = next(s for s in lesson["steps"] if s["type"] == "tap_count")
        tap["count"] = 3
        tap["available"] = 2
        self.assertProblem(self.check(lesson), "'available' must be at least 'count'")

    def test_missing_urdu_text(self):
        lesson = self.mutated()
        del lesson["title"]["ur"]
        self.assertProblem(self.check(lesson), "'ur' is a required property")

    def test_empty_text(self):
        lesson = self.mutated()
        lesson["steps"][0]["text"]["en"] = ""
        self.assertTrue(self.check(lesson))

    def test_ai_must_output_draft_or_known_status(self):
        lesson = self.mutated()
        lesson["review"]["status"] = "published"
        self.assertProblem(self.check(lesson), "review/status")

    def test_unknown_field_rejected(self):
        lesson = self.mutated()
        lesson["difficulty"] = "hard"
        self.assertProblem(self.check(lesson), "Additional properties")

    def test_id_must_match_file_name(self):
        self.assertProblem(self.check(self.lesson, name="g6-maths-02-other.json"), "must equal the file name")

    def test_grade_must_match_id(self):
        lesson = self.mutated()
        lesson["grade"] = 7
        self.assertProblem(self.check(lesson), "doesn't match the id")

    def test_duplicate_step_id(self):
        lesson = self.mutated()
        lesson["steps"][1]["id"] = lesson["steps"][0]["id"]
        self.assertProblem(self.check(lesson), "used twice")

    def test_unknown_misconception(self):
        lesson = self.mutated()
        lesson["steps"][2]["options"][0]["misconception_id"] = "made_up"
        self.assertProblem(self.check(lesson), "'made_up' is not in misconceptions")

    def test_choice_needs_a_correct_option(self):
        lesson = self.mutated()
        for option in lesson["steps"][1]["options"]:
            option["correct"] = False
        self.assertProblem(self.check(lesson), "no correct option")

    def test_correct_answer_not_in_common_wrong(self):
        lesson = self.mutated()
        step = next(s for s in lesson["steps"] if s["type"] == "number")
        step["common_wrong"].append({"answer": step["answer"], "feedback": {"en": "x", "ur": "x"}})
        self.assertProblem(self.check(lesson), "also listed in common_wrong")

    def test_mastery_skill_must_be_listed(self):
        lesson = self.mutated()
        lesson["mastery_criteria"]["maths.other.skill"] = {"question_types": ["recall"], "days": 1}
        self.assertProblem(self.check(lesson), "'maths.other.skill' is not in skills")

    def test_number_step_needs_hint(self):
        lesson = self.mutated()
        step = next(s for s in lesson["steps"] if s["type"] == "number")
        del step["hint"]
        self.assertProblem(self.check(lesson), "'hint' is a required property")


    def test_text_check_common_wrong_must_be_wrong(self):
        lesson = json.loads((v.LESSONS_DIR / "g10-chemistry-15-balancing-equations.json").read_text(encoding="utf-8"))
        step = next(s for s in lesson["steps"] if s["type"] == "text_check")
        step["common_wrong"] = [{"answer": step["expected"].replace(" ", ""), "feedback": {"en": "x", "ur": "x"}}]
        self.assertProblem(self.check(lesson), "a correct answer is also listed in common_wrong")

    def test_text_check_needs_known_checker(self):
        lesson = json.loads((v.LESSONS_DIR / "g10-chemistry-15-balancing-equations.json").read_text(encoding="utf-8"))
        step = next(s for s in lesson["steps"] if s["type"] == "text_check")
        step["checker"] = "magic"
        self.assertTrue(self.check(lesson))


    def test_mastery_needs_a_question_of_each_type(self):
        lesson = self.mutated()
        lesson["mastery_criteria"]["maths.fractions.divide_by_fraction"]["question_types"].append("exam_style")
        self.assertProblem(self.check(lesson), "no 'exam_style' question")

    def test_step_skill_must_be_known(self):
        lesson = self.mutated()
        lesson["steps"][1]["skill"] = "maths.unknown.skill"
        self.assertProblem(self.check(lesson), "is not a skill or prerequisite")

    def test_alternative_must_point_at_a_step(self):
        lesson = self.mutated()
        lesson["alternatives"][0]["for_step"] = "no_such_step"
        self.assertProblem(self.check(lesson), "for_step 'no_such_step'")

    def test_prerequisite_loop(self):
        a = {"skills": ["maths.a.one"], "prerequisites": [{"skill": "maths.b.two"}]}
        b = {"skills": ["maths.b.two"], "prerequisites": [{"skill": "maths.a.one"}]}
        problems = v.check_prerequisite_loops([a, b])
        self.assertProblem(problems, "prerequisite loop")
        self.assertEqual(v.check_prerequisite_loops([a]), [])


def mirror_figure():
    """A triangle and its mirror image across a dashed line."""
    return {
        "width": 100,
        "height": 60,
        "alt": {"en": "A triangle and its mirror image.", "ur": "ایک مثلث اور اس کا عکس۔"},
        "items": [
            {"kind": "polygon", "points": [[10, 10], [40, 10], [40, 40]], "fill": True},
            {"kind": "polygon", "points": [[90, 10], [60, 10], [60, 40]]},
            {"kind": "line", "from": [50, 0], "to": [50, 60], "style": "dashed"},
            {"kind": "circle", "center": [20, 45], "radius": 8},
            {"kind": "arc", "center": [40, 10], "radius": 6, "start": 90, "sweep": 45},
            {"kind": "point", "at": [40, 40]},
            {"kind": "label", "at": [8, 6], "text": "A"},
            {"kind": "label", "at": [30, 50], "text": "60°"},
        ],
    }


class FigureTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.validator = v.load_validator()
        cls.lesson = json.loads(SAMPLE.read_text(encoding="utf-8"))

    check = ValidateLessonsTest.check
    mutated = ValidateLessonsTest.mutated
    assertProblem = ValidateLessonsTest.assertProblem

    def with_figure(self, figure, step_type="explain"):
        lesson = self.mutated()
        step = next(s for s in lesson["steps"] if s["type"] == step_type)
        step["figure"] = figure
        return lesson

    def test_figure_on_steps_is_valid(self):
        for step_type in ("explain", "choice", "number", "summary"):
            self.assertEqual(self.check(self.with_figure(mirror_figure(), step_type)), [], step_type)

    def test_figure_needs_alt_in_both_languages(self):
        figure = mirror_figure()
        del figure["alt"]["ur"]
        self.assertProblem(self.check(self.with_figure(figure)), "'ur' is a required property")
        del figure["alt"]
        self.assertProblem(self.check(self.with_figure(figure)), "'alt' is a required property")
        figure = mirror_figure()
        figure["alt"]["ur"] = "  "
        self.assertProblem(v.check_figure(figure), "alt.ur is missing")

    def test_unknown_kind_and_fields(self):
        figure = mirror_figure()
        figure["items"].append({"kind": "image", "src": "a.png"})
        self.assertProblem(self.check(self.with_figure(figure)), "'image' is not one of")
        figure = mirror_figure()
        figure["items"][2]["style"] = "dotted"
        self.assertProblem(self.check(self.with_figure(figure)), "'dotted' is not one of")
        figure = mirror_figure()
        figure["items"][3]["colour"] = "red"
        self.assertProblem(self.check(self.with_figure(figure)), "Additional properties")

    def test_everything_inside_the_box(self):
        figure = mirror_figure()
        figure["items"][0]["points"][1] = [140, 10]
        figure["items"][3]["center"] = [5, 45]
        figure["items"][6]["at"] = [8, -2]
        problems = self.check(self.with_figure(figure))
        self.assertProblem(problems, "item 1 (polygon): [140, 10] goes outside the 100 x 60 box")
        self.assertProblem(problems, "item 4 (circle): [5, 45] with radius 8 goes outside")
        self.assertProblem(problems, "item 7 (label): [8, -2] goes outside")
        self.assertEqual(len(problems), 3, problems)

    def test_labels_are_short_and_not_words(self):
        for bad in ["Mirror", "A very long label", "دیکھو"]:
            figure = mirror_figure()
            figure["items"][6]["text"] = bad
            self.assertProblem(v.check_figure(figure), "label")
        for good in ["A", "B'", "60°", "5 cm", "90°", "12"]:
            figure = mirror_figure()
            figure["items"][6]["text"] = good
            self.assertEqual(v.check_figure(figure), [], good)

    def test_labels_stay_away_from_the_edge(self):
        for at in ([1, 30], [99, 30], [50, 1], [50, 59]):
            figure = mirror_figure()
            figure["items"][6]["at"] = at
            self.assertProblem(v.check_figure(figure), "too close to the edge")


class AiStepsTest(unittest.TestCase):
    """ai_explain and photo_check steps (Phase 6)."""

    @classmethod
    def setUpClass(cls):
        cls.validator = v.load_validator()
        cls.lesson = json.loads(EQUATIONS.read_text(encoding="utf-8"))

    def step(self, kind):
        lesson = copy.deepcopy(self.lesson)
        return lesson, next(s for s in lesson["steps"] if s["type"] == kind)

    def problems(self, lesson):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / f"{lesson['id']}.json"
            path.write_text(json.dumps(lesson, ensure_ascii=False), encoding="utf-8")
            return v.validate_file(path, self.validator)

    def assertProblem(self, problems, text):
        self.assertTrue(any(text in p for p in problems), f"'{text}' not in {problems}")

    def test_lesson_is_valid(self):
        self.assertEqual(self.problems(copy.deepcopy(self.lesson)), [])

    def test_ai_explain_needs_keywords_and_all_fallback_levels(self):
        lesson, step = self.step("ai_explain")
        del step["fallback_feedback"]["partly"]
        self.assertProblem(self.problems(lesson), "'partly' is a required property")
        lesson, step = self.step("ai_explain")
        step["keywords"] = []
        self.assertProblem(self.problems(lesson), "should be non-empty")

    def test_keywords_without_extra_spaces(self):
        lesson, step = self.step("ai_explain")
        step["keywords"][0].append(" balance")
        self.assertProblem(self.problems(lesson), "extra spaces")

    def test_photo_check_expected_fits_the_checker(self):
        lesson, step = self.step("photo_check")
        step["expected"] = "4x - 7"
        self.assertProblem(self.problems(lesson), "one equation with one '='")
        step.update(checker="numeric", expected="six")
        self.assertProblem(self.problems(lesson), "is not a number")
        step.update(checker="chem_equation", expected="H2 + O2")
        self.assertProblem(self.problems(lesson), "with '->'")

    def test_photo_check_needs_correct_working(self):
        lesson, step = self.step("photo_check")
        del step["correct_working"]
        self.assertProblem(self.problems(lesson), "'correct_working' is a required property")

    def test_ai_step_ids_unique_in_whole_lesson(self):
        lesson, step = self.step("photo_check")
        bank = next(iter(lesson["question_bank"].values()))
        bank[0]["step"]["id"] = step["id"]
        bank[0]["id"] = step["id"]
        self.assertProblem(self.problems(lesson), "must be unique in the whole lesson")


class RichStepsTest(unittest.TestCase):
    """sim, video and lottie steps (Phase 5)."""

    @classmethod
    def setUpClass(cls):
        cls.validator = v.load_validator()
        cls.lesson = json.loads(SAMPLE.read_text(encoding="utf-8"))

    def step(self, kind):
        lesson = copy.deepcopy(self.lesson)
        return lesson, next(s for s in lesson["steps"] if s["type"] == kind)

    def problems(self, lesson):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / f"{lesson['id']}.json"
            path.write_text(json.dumps(lesson, ensure_ascii=False), encoding="utf-8")
            return v.validate_file(path, self.validator)

    def assertProblem(self, problems, text):
        self.assertTrue(any(text in p for p in problems), f"'{text}' not in {problems}")

    def test_missing_simulation_file(self):
        lesson, sim = self.step("sim")
        sim["src"] = "nothing_here.html"
        self.assertProblem(self.problems(lesson), "assets/sims/nothing_here.html doesn't exist")

    def test_webview_sim_needs_src_and_native_needs_sim_id(self):
        lesson, sim = self.step("sim")
        del sim["src"]
        self.assertProblem(self.problems(lesson), "'src' is a required property")
        sim.update(renderer="native", sim_id="magic_box")
        self.assertProblem(self.problems(lesson), "sim_id")

    def test_question_needs_feedback_and_a_number(self):
        lesson, sim = self.step("sim")
        del sim["hint"]
        self.assertProblem(self.problems(lesson), "'hint' is a required property")
        lesson, sim = self.step("sim")
        sim["expected"]["answer"] = "six"
        self.assertProblem(self.problems(lesson), "is not a number")

    def test_explore_sim_cant_be_evidence(self):
        lesson, sim = self.step("sim")
        for key in ("expected", "hint", "feedback_correct", "feedback_wrong", "common_wrong"):
            sim.pop(key, None)
        self.assertEqual(self.problems(lesson), [])
        sim["question_type"] = "apply"
        self.assertProblem(self.problems(lesson), "question_type needs 'expected'")

    def test_native_params(self):
        lesson, sim = self.step("sim")
        for key in ("src", "params"):
            sim.pop(key)
        sim.update(renderer="native", sim_id="balance_scale")
        self.assertProblem(self.problems(lesson), "balance_scale needs params.equation")

    def region_step(self, **expected):
        lesson, sim = self.step("sim")
        for key in ("src", "common_wrong"):
            sim.pop(key, None)
        sim.update(renderer="native", sim_id="feasible_region", params={
            "constraints": ["x + y <= 6", "x <= 4", "x >= 0", "y >= 0"], "x_max": 7, "y_max": 7})
        sim["expected"] = {"result": "corners", "checker": "points", "answer": "(0, 0), (4, 0), (4, 2), (0, 6)", **expected}
        return lesson, sim

    def test_region_corners_are_worked_out(self):
        lesson, _ = self.region_step()
        self.assertEqual(self.problems(lesson), [])
        lesson, _ = self.region_step(answer="(0, 0), (4, 0), (0, 6)")
        self.assertProblem(self.problems(lesson), "but the constraints give (0, 0), (0, 6), (4, 0), (4, 2)")
        lesson, sim = self.region_step()
        sim["params"]["x_max"] = 3
        self.assertProblem(self.problems(lesson), "corner (4, 0) is outside the grid")
        lesson, sim = self.region_step()
        sim["params"]["constraints"].append("x + y >= 7")
        self.assertProblem(self.problems(lesson), "no corner in common")
        lesson, sim = self.region_step()
        sim["params"]["constraints"] = ["x + 2y <= 5", "x >= 0", "y >= 0"]
        self.assertProblem(self.problems(lesson), "not a whole-number point")

    def test_inequality_plane_answer_fits_the_grid(self):
        lesson, sim = self.region_step()
        sim.update(sim_id="inequality_plane", params={"size": 5})
        sim["expected"] = {"result": "inequality", "checker": "linear_inequality_2d", "answer": "y <= 2x + 1"}
        self.assertEqual(self.problems(lesson), [])
        sim["expected"]["answer"] = "y <= 2x + 1/3"
        self.assertProblem(self.problems(lesson), "doesn't pass through two grid points")
        sim["expected"]["answer"] = "y = 2x"
        self.assertProblem(self.problems(lesson), "must be one inequality in x and y")

    def test_video_files(self):
        lesson, video = self.step("video")
        video["src"]["ur"] = "missing_ur.mp4"
        video["captions"]["en"] = "https://example.com/a.vtt"
        problems = self.problems(lesson)
        self.assertProblem(problems, "src.ur: assets/videos/missing_ur.mp4 doesn't exist")
        self.assertEqual(len(problems), 1, problems)

    def test_lottie_file(self):
        lesson = copy.deepcopy(self.lesson)
        lesson["alternatives"][0]["steps"][0]["src"] = "nope.json"
        self.assertProblem(self.problems(lesson), "assets/lottie/nope.json doesn't exist")

    def test_simulations_must_work_offline(self):
        for page in v.ASSETS.joinpath("sims").glob("*.html"):
            self.assertIsNone(v.EXTERNAL.search(page.read_text(encoding="utf-8")), page.name)
        for bad in ['<script src="https://cdn.example.com/x.js">', "fetch('/api')", "url(//x.png)"]:
            self.assertIsNotNone(v.EXTERNAL.search(bad), bad)


if __name__ == "__main__":
    unittest.main()


class InequalityTest(unittest.TestCase):
    def test_one_inequality(self):
        for good in ["2x - 3 < 7", "x <= 4", "5 >= (x + 1)/2", "x ≥ -2"]:
            self.assertTrue(v.is_inequality(good), good)
        for bad in ["2x - 3 = 7", "x < 3 < 4", "x <= ", "x < 3 = 4", "x"]:
            self.assertFalse(v.is_inequality(bad), bad)
