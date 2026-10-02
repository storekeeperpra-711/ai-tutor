#!/usr/bin/env python3
"""Make a short explainer video in English and Urdu, with captions.

Usage:
    python tools/video/make_video.py tools/video/scripts/fractions_roti.json
    python tools/video/make_video.py SCRIPT --out assets/videos --lang ur

A script is a JSON list of scenes. Each scene says how long it lasts,
what to draw (one of the drawers below, with its params) and the caption
in both languages. For every language this writes:
    <name>_<lang>.mp4   720p H.264, no sound, small (about 1 MB a minute)
    <name>_<lang>.vtt   WebVTT captions, one cue per scene

Needs Pillow (with raqm, for Urdu) and ffmpeg on the PATH. Colours follow
the spec: orange = force, teal = velocity, purple = acceleration.
"""

from __future__ import annotations

import argparse
import json
import math
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from PIL import Image, ImageDraw, ImageFont, features

ROOT = Path(__file__).resolve().parents[2]
URDU_FONT = ROOT / "assets" / "fonts" / "NotoNastaliqUrdu-Variable.ttf"
LATIN_FONTS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/Library/Fonts/Arial.ttf",
    "C:/Windows/Fonts/arial.ttf",
]
LANGUAGES = ("en", "ur")
MAX_SECONDS = 120

INK = (62, 39, 35)
PAPER = (255, 250, 242)
ROTI = (245, 200, 115)
ROTI_EDGE = (141, 90, 51)
ORANGE = (251, 140, 0)  # force
TEAL = (0, 137, 123)  # velocity
PURPLE = (106, 27, 154)  # acceleration


@dataclass
class Frame:
    """What a drawer gets for one frame."""

    draw: ImageDraw.ImageDraw
    size: tuple[int, int]
    t: float  # 0..1 through the scene
    lang: str
    fonts: "Fonts"


class Fonts:
    def __init__(self) -> None:
        latin = next((p for p in LATIN_FONTS if Path(p).exists()), None)
        self._latin = latin
        self._cache: dict[tuple[str, int], ImageFont.FreeTypeFont] = {}

    def get(self, lang: str, size: int):
        key = (lang, size)
        if key not in self._cache:
            if lang == "ur":
                engine = ImageFont.Layout.RAQM if features.check("raqm") else ImageFont.Layout.BASIC
                self._cache[key] = ImageFont.truetype(str(URDU_FONT), int(size * 0.85), layout_engine=engine)
            elif self._latin:
                self._cache[key] = ImageFont.truetype(self._latin, size)
            else:
                self._cache[key] = ImageFont.load_default(size)
        return self._cache[key]


def text(f: Frame, value: str, center: tuple[float, float], size: int, lang: str | None = None,
         fill=INK) -> None:
    """Draws text centred on a point. Maths stays left to right."""
    lang = lang or f.lang
    font = f.fonts.get(lang, size)
    kwargs = {"direction": "rtl", "language": "ur"} if lang == "ur" and features.check("raqm") else {}
    f.draw.text(center, value, font=font, fill=fill, anchor="mm", **kwargs)


def ease(t: float) -> float:
    t = min(1.0, max(0.0, t))
    return t * t * (3 - 2 * t)


# ---- Drawers: (frame, params) -> None ------------------------------------


def draw_title(f: Frame, p: dict) -> None:
    w, h = f.size
    text(f, p["title"][f.lang], (w / 2, h * 0.4), 72)
    if "subtitle" in p:
        alpha = ease(f.t * 3 - 0.5)
        if alpha > 0:
            text(f, p["subtitle"], (w / 2, h * 0.62), 64, lang="en", fill=ORANGE)


def _roti_centres(f: Frame, count: int) -> list[tuple[float, float]]:
    w, h = f.size
    gap = w / (count + 1)
    return [(gap * (i + 1), h * 0.45) for i in range(count)]


def draw_rotis(f: Frame, p: dict) -> None:
    """Rotis, optionally cut into `cut` pieces (cut lines grow in), with
    pieces numbered one by one when `count` is true. The `label` shows
    from `label_at` (0..1 through the scene), so it can wait for the
    counting to finish."""
    count, cut = p.get("rotis", 2), p.get("cut", 1)
    grow = ease(f.t * 2) if p.get("animate_cut") else 1.0
    r = min(f.size[0] / (count + 1) * 0.42, f.size[1] * 0.3)
    numbered = int(ease(f.t * 1.2) * count * cut + 1e-6) if p.get("count") else 0
    n = 0
    for cx, cy in _roti_centres(f, count):
        f.draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=ROTI, outline=ROTI_EDGE, width=6)
        if cut > 1:
            for k in range(cut):
                a = -math.pi / 2 + 2 * math.pi * k / cut
                f.draw.line([cx, cy, cx + r * grow * math.cos(a), cy + r * grow * math.sin(a)],
                            fill=ROTI_EDGE, width=6)
        for k in range(cut if numbered else 0):
            n += 1
            if n > numbered:
                break
            a = -math.pi / 2 + 2 * math.pi * (k + 0.5) / cut
            px, py = cx + r * 0.6 * math.cos(a), cy + r * 0.6 * math.sin(a)
            f.draw.ellipse([px - 26, py - 26, px + 26, py + 26], fill=ORANGE)
            text(f, str(n), (px, py), 32, lang="en", fill=(255, 255, 255))
    if "label" in p and f.t >= p.get("label_at", 0):
        text(f, p["label"][f.lang], (f.size[0] / 2, f.size[1] * 0.85), 48)


def draw_equations(f: Frame, p: dict) -> None:
    """Lines of maths that appear one after another."""
    w, h = f.size
    lines = p["lines"]
    shown = 1 + int(ease(f.t * 1.3) * (len(lines) - 1) + 1e-6)
    top = h / 2 - (len(lines) - 1) * 60
    for i, line in enumerate(lines[:shown]):
        colour = ORANGE if i == len(lines) - 1 else INK
        text(f, line, (w / 2, top + i * 120), 80, lang="en", fill=colour)
    if "label" in p:
        text(f, p["label"][f.lang], (w / 2, h * 0.88), 44)


DRAWERS: dict[str, Callable[[Frame, dict], None]] = {
    "title": draw_title,
    "rotis": draw_rotis,
    "equations": draw_equations,
}


# ---- Script, captions and encoding ----------------------------------------


def load_script(path: Path) -> dict:
    script = json.loads(path.read_text(encoding="utf-8"))
    problems = check_script(script)
    if problems:
        raise SystemExit("Script problems:\n" + "\n".join(f"  - {p}" for p in problems))
    return script


def check_script(script: dict) -> list[str]:
    problems = []
    total = sum(s["seconds"] for s in script["scenes"])
    if total > MAX_SECONDS:
        problems.append(f"{total} s is longer than {MAX_SECONDS} s")
    for i, scene in enumerate(script["scenes"]):
        if scene["draw"] not in DRAWERS:
            problems.append(f"scene {i + 1}: unknown drawer '{scene['draw']}'")
        for lang in LANGUAGES:
            if not scene.get("caption", {}).get(lang):
                problems.append(f"scene {i + 1}: no {lang} caption")
    return problems


def timestamp(seconds: float) -> str:
    ms = round(seconds * 1000)
    return f"{ms // 3600000:02}:{ms // 60000 % 60:02}:{ms // 1000 % 60:02}.{ms % 1000:03}"


def captions(script: dict, lang: str) -> str:
    """WebVTT with one cue per scene."""
    out, start = ["WEBVTT", ""], 0.0
    for n, scene in enumerate(script["scenes"], 1):
        end = start + scene["seconds"]
        out += [str(n), f"{timestamp(start)} --> {timestamp(end)}", scene["caption"][lang], ""]
        start = end
    return "\n".join(out)


def frames(script: dict, lang: str):
    """Yields every frame as an RGB image."""
    fps = script.get("fps", 12)
    size = tuple(script.get("size", [1280, 720]))
    fonts = Fonts()
    for scene in script["scenes"]:
        count = max(1, round(scene["seconds"] * fps))
        for i in range(count):
            image = Image.new("RGB", size, PAPER)
            frame = Frame(ImageDraw.Draw(image), size, i / max(1, count - 1), lang, fonts)
            DRAWERS[scene["draw"]](frame, scene.get("params", {}))
            yield image


def encode(script: dict, lang: str, out: Path) -> None:
    fps = script.get("fps", 12)
    w, h = script.get("size", [1280, 720])
    command = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w}x{h}", "-r", str(fps), "-i", "-",
        "-c:v", "libx264", "-preset", "slow", "-tune", "animation", "-crf", "30",
        "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-an", str(out),
    ]
    with subprocess.Popen(command, stdin=subprocess.PIPE) as ffmpeg:
        assert ffmpeg.stdin is not None
        for image in frames(script, lang):
            ffmpeg.stdin.write(image.tobytes())
        ffmpeg.stdin.close()
        if ffmpeg.wait() != 0:
            raise SystemExit("ffmpeg failed")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("script", type=Path)
    parser.add_argument("--out", type=Path, default=ROOT / "assets" / "videos")
    parser.add_argument("--lang", choices=LANGUAGES, action="append")
    args = parser.parse_args(argv)
    if not shutil.which("ffmpeg"):
        print("ffmpeg is not installed (https://ffmpeg.org/download.html).")
        return 1
    if not features.check("raqm"):
        print("Warning: Pillow has no raqm, so Urdu letters won't join. Try: pip install --upgrade pillow")

    script = load_script(args.script)
    args.out.mkdir(parents=True, exist_ok=True)
    for lang in args.lang or LANGUAGES:
        video = args.out / f"{script['name']}_{lang}.mp4"
        encode(script, lang, video)
        (args.out / f"{script['name']}_{lang}.vtt").write_text(captions(script, lang) + "\n", encoding="utf-8")
        seconds = sum(s["seconds"] for s in script["scenes"])
        print(f"wrote {video.name}: {seconds} s, {video.stat().st_size / 1024:.0f} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
