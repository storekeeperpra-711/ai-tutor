"""Tests for tools/voice/make_voice.py (no network or API key needed)."""

import base64
import io
import json
import math
import struct
import sys
import unittest
import unittest.mock
import wave
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "voice"))

import make_voice  # noqa: E402


def tone(seconds: float, amplitude: int, rate: int = 24000) -> bytes:
    out = io.BytesIO()
    with wave.open(out, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(rate)
        n = int(seconds * rate)
        w.writeframes(b"".join(
            struct.pack("<h", int(amplitude * math.sin(i / 10))) for i in range(n)))
    return out.getvalue()


class MakeVoiceTest(unittest.TestCase):
    def test_file_names_match_the_app(self):
        # lib/character/voice_lines.dart: voiceFileName
        self.assertEqual(
            make_voice.voice_file_name("g6-maths-02-dividing-fractions", "s1_hook", "ur"),
            "g6-maths-02-dividing-fractions__s1_hook_ur.m4a")

    def test_finds_mithu_lines_with_their_step(self):
        lines = make_voice.mithu_lines(make_voice.load_lesson(
            "g9-maths-05-solving-linear-equations"))
        steps = [l["step"] for l in lines]
        self.assertEqual(steps[0], "s1_scale")
        self.assertIn("s6_summary", steps)
        self.assertTrue(all("en" in l["say"] for l in lines))

    def test_every_lesson_line_has_a_step(self):
        for path in make_voice.LESSONS.glob("*.json"):
            lesson = json.loads(path.read_text(encoding="utf-8"))
            for line in make_voice.mithu_lines(lesson):
                self.assertRegex(line["step"], r"^[a-z0-9_]+$", path.name)

    def test_sample_uses_real_lines(self):
        lines = make_voice.sample_lines()
        self.assertEqual(len(lines), 2)
        self.assertTrue(all(say.get("ur") for _, _, say in lines))

    def test_request_sets_voice_and_style(self):
        body = make_voice.request_body("Hello", "Sulafat", "warm")
        self.assertEqual(body["model"], make_voice.MODEL)
        self.assertEqual(body["generation_config"]["speech_config"][0]["voice"], "Sulafat")
        content = body["input"][0]["content"][0]
        self.assertEqual(content["text"], "Hello")
        self.assertEqual(content["annotations"][0]["style"], "warm")

    def test_finds_audio_anywhere_in_the_answer(self):
        wav = tone(0.2, 8000)
        answer = {"id": "x", "steps": [{"content": [
            {"type": "text", "text": "ok"},
            {"type": "audio", "mime_type": "audio/wav",
             "data": base64.b64encode(wav).decode()},
        ]}]}
        self.assertEqual(make_voice.find_audio(answer), wav)
        self.assertIsNone(make_voice.find_audio({"steps": []}))

    def test_raw_pcm_is_wrapped_as_wav(self):
        pcm = b"\x00\x01" * 2400
        wav = make_voice.as_wav(pcm)
        with wave.open(io.BytesIO(wav)) as w:
            self.assertEqual(w.getframerate(), 24000)
            self.assertEqual(w.readframes(w.getnframes()), pcm)
        self.assertEqual(make_voice.as_wav(wav), wav)

    def test_mouth_track_follows_loudness(self):
        quiet = make_voice.mouth_track(tone(0.5, 10))
        loud = make_voice.mouth_track(tone(0.5, 20000))
        self.assertEqual(len(loud), 10)  # 20 a second
        self.assertTrue(set(quiet) <= {"0"})
        self.assertTrue(all(int(d) >= 7 for d in loud))


class DailyLimitTest(unittest.TestCase):
    def test_knows_the_daily_limit_from_a_busy_minute(self):
        self.assertTrue(make_voice.is_daily_limit(
            "Rate limit exceeded for model gemini-3.8-flash-tts "
            "(limit: 10 requests per day on Free Tier)."))
        self.assertFalse(make_voice.is_daily_limit(
            "Rate limit exceeded: 3 requests per minute."))

    def test_a_day_cut_short_keeps_what_was_made(self):
        calls = []

        def fake(text, voice, style, key):
            calls.append(voice)
            if len(calls) > 2:
                raise make_voice.DailyLimit("used up")
            return tone(0.3, 8000)

        import tempfile
        with tempfile.TemporaryDirectory() as tmp, \
                unittest.mock.patch.object(make_voice, "synthesize", fake), \
                unittest.mock.patch.object(make_voice, "PAUSE", 0):
            out = Path(tmp)
            ok = make_voice.make_sample(out, "key", ["Sulafat", "Achird", "Leda"])
            self.assertTrue(ok)
            # Urdu line 1 first, in each voice in turn.
            self.assertEqual(calls, ["Sulafat", "Achird", "Leda"])
            self.assertTrue((out / "Sulafat_1_ur.m4a").exists())
            self.assertTrue((out / "Achird_1_ur.m4a").exists())
            self.assertIn("daily limit", (out / "README.txt").read_text())


if __name__ == "__main__":
    unittest.main()
