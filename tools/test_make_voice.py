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
                unittest.mock.patch.object(make_voice, "PAUSE", 0), \
                unittest.mock.patch.object(  # no ffmpeg needed
                    make_voice, "save", lambda wav, path: path.write_bytes(wav)):
            out = Path(tmp)
            ok = make_voice.make_sample(out, "key", ["Sulafat", "Achird", "Leda"])
            self.assertTrue(ok)
            # Urdu line 1 first, in each voice in turn.
            self.assertEqual(calls, ["Sulafat", "Achird", "Leda"])
            self.assertTrue((out / "Sulafat_1_ur.m4a").exists())
            self.assertTrue((out / "Achird_1_ur.m4a").exists())
            self.assertIn("daily limit", (out / "README.txt").read_text())


class FakeKV:
    def __init__(self, values=None):
        self.values = dict(values or {})
        self.writes = []

    def get(self, key):
        return self.values.get(key)

    def put_many(self, values):
        self.writes.append(sorted(values))
        self.values.update(values)


def fake_encode(wav):
    return b"m4a", b"0123"


class MakeAllTest(unittest.TestCase):
    def setUp(self):
        self.calls = []
        for target, value in [("PAUSE", 0), ("encode", fake_encode),
                              ("synthesize", self.fake_synthesize)]:
            patcher = unittest.mock.patch.object(make_voice, target, value)
            patcher.start()
            self.addCleanup(patcher.stop)
        self.limit_after = None

    def fake_synthesize(self, text, voice, style, key):
        if self.limit_after is not None and len(self.calls) >= self.limit_after:
            raise make_voice.DailyLimit("used up")
        self.calls.append((text, voice))
        return b"wav"

    def test_every_line_has_its_own_file_grade_9_first(self):
        lines = make_voice.all_lines()
        names = [l["name"] for l in lines]
        self.assertEqual(len(names), len(set(names)))
        self.assertTrue(names[0].startswith("g9-"))
        self.assertEqual(names[0][-6:], "ur.m4a")
        self.assertEqual(names[1][-6:], "en.m4a")
        self.assertGreater(len(lines), 80)

    def test_hash_changes_with_the_text_or_voice(self):
        a = make_voice.line_hash("Hello", "en")
        self.assertEqual(a, make_voice.line_hash("Hello", "en"))
        self.assertNotEqual(a, make_voice.line_hash("Hello!", "en"))
        with unittest.mock.patch.object(make_voice, "VOICE", "Achird"):
            self.assertNotEqual(a, make_voice.line_hash("Hello", "en"))

    def test_stores_each_recording_with_the_index(self):
        kv = FakeKV()
        ok, made, left = make_voice.make_all(kv, "key", limit=2)
        self.assertEqual((ok, made), (True, 2))
        self.assertEqual(left, len(make_voice.all_lines()) - 2)
        first = make_voice.all_lines()[0]["name"]
        self.assertEqual(kv.values[first], b"m4a")
        self.assertEqual(kv.values[first[:-4] + ".mouth"], b"0123")
        index = json.loads(kv.values["index"])
        self.assertEqual(index["voice"], "Sulafat")
        self.assertEqual(len(index["files"]), 2)
        self.assertTrue(all(self.calls[0][1] == "Sulafat" for _ in self.calls))

    def test_carries_on_the_next_day_and_skips_what_is_made(self):
        kv = FakeKV()
        self.limit_after = 3
        ok, made, _ = make_voice.make_all(kv, "key")
        self.assertEqual((ok, made), (True, 3))
        self.calls.clear()
        self.limit_after = None
        ok, made, left = make_voice.make_all(kv, "key", limit=1)
        self.assertEqual((made, len(json.loads(kv.values["index"])["files"])), (1, 4))
        self.assertEqual(self.calls[0][0], make_voice.all_lines()[3]["text"])

    def test_makes_a_changed_line_again_and_forgets_removed_ones(self):
        lines = make_voice.all_lines()
        files = {l["name"]: l["hash"] for l in lines}
        files[lines[5]["name"]] = "old"
        files["gone__s1_en.m4a"] = "abc"
        kv = FakeKV({"index": json.dumps({"files": files}).encode()})
        ok, made, left = make_voice.make_all(kv, "key")
        self.assertEqual((ok, made, left), (True, 1, 0))
        self.assertEqual(self.calls, [(lines[5]["text"], "Sulafat")])
        index = json.loads(kv.values["index"])["files"]
        self.assertNotIn("gone__s1_en.m4a", index)
        self.assertEqual(index[lines[5]["name"]], lines[5]["hash"])

    def test_nothing_to_do_calls_nobody(self):
        lines = make_voice.all_lines()
        index = {"voice": "Sulafat", "files": {l["name"]: l["hash"] for l in lines}}
        kv = FakeKV({"index": json.dumps(index).encode()})
        self.assertEqual(make_voice.make_all(kv, "key"), (True, 0, 0))
        self.assertEqual((self.calls, kv.writes), ([], []))


class KVTest(unittest.TestCase):
    def test_bulk_write_is_base64(self):
        import kv as kv_module
        sent = {}

        class Fake(kv_module.KV):
            def _call(self, method, url, body=None, raw=False):
                sent.update(method=method, url=url, body=body)
                return {"success": True}

        store = Fake("t", "acct", "ns1")
        store.put_many({"a.m4a": b"\x00\x01"})
        self.assertEqual(sent["method"], "PUT")
        self.assertTrue(sent["url"].endswith("/accounts/acct/storage/kv/namespaces/ns1/bulk"))
        self.assertEqual(sent["body"], [{"key": "a.m4a", "value": "AAE=", "base64": True}])


if __name__ == "__main__":
    unittest.main()
