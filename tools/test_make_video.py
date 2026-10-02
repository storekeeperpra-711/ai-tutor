"""Tests for tools/video/make_video.py (no ffmpeg needed)."""

import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "video"))

import make_video  # noqa: E402

SCRIPTS = Path(__file__).resolve().parent / "video" / "scripts"


class MakeVideoTest(unittest.TestCase):
    def test_timestamps(self):
        self.assertEqual(make_video.timestamp(0), "00:00:00.000")
        self.assertEqual(make_video.timestamp(65.5), "00:01:05.500")

    def test_captions_have_one_cue_per_scene(self):
        script = {"scenes": [
            {"seconds": 2, "draw": "title", "caption": {"en": "One", "ur": "ایک"}},
            {"seconds": 3, "draw": "title", "caption": {"en": "Two", "ur": "دو"}},
        ]}
        vtt = make_video.captions(script, "en")
        self.assertTrue(vtt.startswith("WEBVTT"))
        self.assertIn("00:00:02.000 --> 00:00:05.000\nTwo", vtt)
        self.assertIn("دو", make_video.captions(script, "ur"))

    def test_script_checks(self):
        script = {"scenes": [{"seconds": 130, "draw": "nothing", "caption": {"en": "x"}}]}
        problems = make_video.check_script(script)
        self.assertEqual(len(problems), 3, problems)

    def test_every_script_is_valid_and_draws_in_both_languages(self):
        for path in SCRIPTS.glob("*.json"):
            script = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(make_video.check_script(script), [], path.name)
            short = dict(script, fps=1)  # One frame a second is enough here.
            for lang in make_video.LANGUAGES:
                count = sum(1 for _ in make_video.frames(short, lang))
                self.assertEqual(count, sum(s["seconds"] for s in script["scenes"]))


if __name__ == "__main__":
    unittest.main()
