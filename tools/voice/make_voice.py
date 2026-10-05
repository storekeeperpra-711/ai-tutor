"""Makes Mithu's voice with Google's Gemini text-to-speech.

Each Mithu line in a lesson ("character": {"say": {...}}) becomes one
recording per language, named the way the app looks for it
(lib/character/voice_lines.dart): `<lesson>__<step>_<lang>.m4a`, with a
`.mouth` file next to it that moves Mithu's beak.

    # A few lines in several voices, to choose a voice by ear:
    python tools/voice/make_voice.py sample --out voice-samples

Needs GEMINI_API_KEY (a GitHub secret; never paste it anywhere else) and
ffmpeg. The audio is made once, in GitHub Actions, never on a child's phone.
"""

from __future__ import annotations

import argparse
import array
import base64
import io
import json
import math
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
import wave
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LESSONS = ROOT / "content" / "lessons"

MODEL = "gemini-3.8-flash-tts"
ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/interactions"

# How Mithu should sound, per language. Gemini finds the language by itself.
STYLE = {
    "en": "a warm, kind teacher from Pakistan talking to one child; slow, clear and encouraging",
    "ur": "a warm, kind Pakistani teacher speaking Urdu to one child; slow, clear and encouraging",
}

# Voices to try in the sample (Gemini's own descriptions in brackets).
SAMPLE_VOICES = {
    "Sulafat": "warm",
    "Vindemiatrix": "gentle",
    "Achird": "friendly",
    "Sadaltager": "knowledgeable",
}

# Seconds between requests, to stay inside the free limits.
PAUSE = 7

# Lines for the sample: (lesson file, step id).
SAMPLE_LINES = [
    ("g9-maths-05-solving-linear-equations", "s1_scale"),
    ("g0-maths-01-count-the-mangoes", None),  # the first line
]

MOUTH_PER_SECOND = 20  # as in MouthTrack.perSecond


def voice_file_name(lesson_id: str, step_id: str, language: str) -> str:
    return f"{lesson_id}__{step_id}_{language}.m4a"


def mithu_lines(lesson: dict) -> list[dict]:
    """Every Mithu line in a lesson with the id of the step it is in."""
    found: list[dict] = []

    def walk(node, step_id):
        if isinstance(node, dict):
            if isinstance(node.get("id"), str) and "type" in node:
                step_id = node["id"]
            character = node.get("character")
            if isinstance(character, dict) and "say" in character and step_id:
                found.append({"step": step_id, "say": character["say"]})
            for key, value in node.items():
                if key != "character":
                    walk(value, step_id)
        elif isinstance(node, list):
            for value in node:
                walk(value, step_id)

    walk(lesson.get("steps", []), None)
    walk(lesson.get("question_bank", []), None)
    return found


def load_lesson(lesson_id: str) -> dict:
    return json.loads((LESSONS / f"{lesson_id}.json").read_text(encoding="utf-8"))


def request_body(text: str, voice: str, style: str) -> dict:
    return {
        "model": MODEL,
        "input": [{
            "type": "user_input",
            "content": [{
                "type": "text",
                "text": text,
                "annotations": [{"type": "speech_metadata", "style": style}],
            }],
        }],
        "response_format": {"type": "audio"},
        "generation_config": {"speech_config": [{"voice": voice}]},
    }


def find_audio(response) -> bytes | None:
    """The first base64 audio in Gemini's answer, wherever it is."""
    if isinstance(response, dict):
        data = response.get("data")
        mime = str(response.get("mime_type") or response.get("mimeType") or "")
        if isinstance(data, str) and (mime.startswith("audio") or not mime):
            try:
                audio = base64.b64decode(data, validate=True)
            except ValueError:
                audio = b""
            if len(audio) > 1000:
                return audio
        for value in response.values():
            if (audio := find_audio(value)) is not None:
                return audio
    elif isinstance(response, list):
        for value in response:
            if (audio := find_audio(value)) is not None:
                return audio
    return None


def as_wav(audio: bytes) -> bytes:
    """Gemini sends WAV; raw 24 kHz 16-bit mono PCM is wrapped as WAV."""
    if audio[:4] == b"RIFF":
        return audio
    out = io.BytesIO()
    with wave.open(out, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(24000)
        w.writeframes(audio)
    return out.getvalue()


class DailyLimit(RuntimeError):
    """The free tier's requests for today are used up (10 a day for this
    model in October 2026); waiting minutes won't help."""


def is_daily_limit(detail: str) -> bool:
    return "per day" in detail or "requests per day" in detail.lower()


def synthesize(text: str, voice: str, style: str, key: str) -> bytes:
    """Speaks [text]; waits and tries again when the free limit is hit."""
    body = json.dumps(request_body(text, voice, style)).encode()
    for attempt in range(6):
        req = urllib.request.Request(
            ENDPOINT,
            data=body,
            headers={"x-goog-api-key": key, "Content-Type": "application/json"},
        )
        try:
            with urllib.request.urlopen(req, timeout=120) as res:
                audio = find_audio(json.load(res))
            if audio is None:
                raise RuntimeError("Gemini answered without audio")
            return as_wav(audio)
        except urllib.error.HTTPError as e:
            detail = e.read().decode(errors="replace")[:500]
            if e.code == 429 and is_daily_limit(detail):
                raise DailyLimit(f"Gemini's free daily limit is used up: {detail}") from None
            if e.code in (429, 500, 503) and attempt < 5:
                wait = 20 * (attempt + 1)
                print(f"  Gemini said {e.code}; trying again in {wait} s")
                time.sleep(wait)
                continue
            raise RuntimeError(f"Gemini said {e.code}: {detail}") from None
    raise RuntimeError("Gemini kept saying it is busy")


def mouth_track(wav_bytes: bytes) -> str:
    """How loud the voice is, 20 times a second, as digits 0-9 (the same
    scale as MouthTrack.levelFromDb: -50 dBFS is closed, -10 is open)."""
    with wave.open(io.BytesIO(wav_bytes)) as w:
        if w.getsampwidth() != 2:
            raise ValueError("expected 16-bit audio")
        rate, channels = w.getframerate(), w.getnchannels()
        samples = array.array("h", w.readframes(w.getnframes()))
    if sys.byteorder == "big":
        samples.byteswap()
    window = rate * channels // MOUTH_PER_SECOND
    digits = []
    for start in range(0, len(samples), window):
        chunk = samples[start:start + window]
        rms = math.sqrt(sum(s * s for s in chunk) / len(chunk)) if chunk else 0
        db = 20 * math.log10(rms / 32768) if rms > 0 else -100
        level = min(max((db + 50) / 40, 0), 1)
        digits.append(str(round(level * 9)))
    return "".join(digits)


def to_m4a(wav_bytes: bytes, out: Path) -> None:
    """Small AAC for phones: mono, 32 kbit/s (about 4 KB a second)."""
    subprocess.run(
        ["ffmpeg", "-loglevel", "error", "-y", "-f", "wav", "-i", "pipe:0",
         "-ac", "1", "-c:a", "aac", "-b:a", "32k", str(out)],
        input=wav_bytes, check=True,
    )


def save(wav_bytes: bytes, out: Path) -> None:
    to_m4a(wav_bytes, out)
    out.with_suffix(".mouth").write_text(mouth_track(wav_bytes))


def sample_lines() -> list[tuple[str, str, dict]]:
    """(lesson id, step id, text) for the sample."""
    picked = []
    for lesson_id, step_id in SAMPLE_LINES:
        lines = mithu_lines(load_lesson(lesson_id))
        line = next(l for l in lines if step_id in (None, l["step"]))
        picked.append((lesson_id, line["step"], line["say"]))
    return picked


def make_sample(out: Path, key: str, voices: list[str]) -> bool:
    """Urdu first and one line at a time across the voices, so a day cut
    short by the free limit still has the same line in several voices to
    compare. Returns False only on a real error."""
    out.mkdir(parents=True, exist_ok=True)
    index = ["Mithu voice samples", ""]

    def write_index():
        (out / "README.txt").write_text("\n".join(index) + "\n", encoding="utf-8")

    for n, (_, _, say) in enumerate(sample_lines(), 1):
        for language in ("ur", "en"):
            text = say.get(language)
            if not text:
                continue
            for voice in voices:
                name = f"{voice}_{n}_{language}.m4a"
                print(f"{voice} line {n} {language}")
                try:
                    wav = synthesize(text, voice, STYLE[language], key)
                except DailyLimit as e:
                    print(f"::warning::{e} Run it again tomorrow for the rest.")
                    index.append("(Stopped here: the free daily limit. Run again tomorrow.)")
                    write_index()
                    return True
                except RuntimeError as e:
                    print(f"Stopped: {e}")
                    index.append(f"(Stopped here: {e})")
                    write_index()
                    return False
                save(wav, out / name)
                index.append(f"{name} ({voice}, {SAMPLE_VOICES.get(voice, '')}): {text}")
                write_index()
                time.sleep(PAUSE)
    return True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("mode", choices=["sample"])
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--voices", default=",".join(SAMPLE_VOICES),
                        help="comma-separated Gemini voice names")
    args = parser.parse_args(argv)
    voices = [v.strip() for v in args.voices.split(",") if v.strip()]
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        print("GEMINI_API_KEY is missing. Add it as a GitHub secret "
              "(docs/setup/gemini-voice.md).")
        return 1
    return 0 if make_sample(args.out, key, voices) else 1


if __name__ == "__main__":
    sys.exit(main())
