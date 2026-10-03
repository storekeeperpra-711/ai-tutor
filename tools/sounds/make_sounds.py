#!/usr/bin/env python3
"""Makes the app's sound effects (assets/sounds/*.wav) from simple tones.

Generated rather than downloaded, so there are no licence questions and
the files stay tiny. Run from the repository root:

    python tools/sounds/make_sounds.py
"""

from __future__ import annotations

import math
import struct
import wave
from pathlib import Path

RATE = 22050
OUT = Path(__file__).resolve().parents[2] / "assets" / "sounds"

C5, E5, G5, A5, C6, E6, G6, C7 = 523.25, 659.25, 783.99, 880.0, 1046.5, 1318.5, 1568.0, 2093.0


def tone(freq: float, seconds: float, volume: float = 0.5, decay: float = 6.0, glide_to: float | None = None) -> list[float]:
    """A soft bell-like tone: sine plus a quiet octave, fading out."""
    n = int(RATE * seconds)
    out, phase = [], 0.0
    for i in range(n):
        t = i / RATE
        f = freq if glide_to is None else freq + (glide_to - freq) * (i / n)
        phase += 2 * math.pi * f / RATE
        attack = min(1.0, t / 0.005)  # 5 ms fade-in: no click
        env = attack * math.exp(-decay * t)
        out.append(volume * env * (math.sin(phase) + 0.25 * math.sin(2 * phase)))
    return out


def mix(*parts: tuple[float, list[float]]) -> list[float]:
    """Places each (start seconds, samples) on one track."""
    length = max(int(start * RATE) + len(s) for start, s in parts)
    track = [0.0] * length
    for start, samples in parts:
        offset = int(start * RATE)
        for i, v in enumerate(samples):
            track[offset + i] += v
    return track


def save(name: str, samples: list[float]) -> None:
    peak = max(1e-9, max(abs(s) for s in samples))
    scale = min(1.0, 0.8 / peak)
    # A short fade at the end so nothing clicks when it stops.
    fade = int(RATE * 0.01)
    for i in range(fade):
        samples[-1 - i] *= i / fade
    with wave.open(str(OUT / f"{name}.wav"), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(RATE)
        w.writeframes(b"".join(struct.pack("<h", int(s * scale * 32767)) for s in samples))


SOUNDS = {
    # A light tick for taps.
    "tap": lambda: tone(1400, 0.05, 0.35, decay=60),
    # Something dropping softly into a basket.
    "basket": lambda: tone(620, 0.16, 0.6, decay=18, glide_to=260),
    # Right: a rising three-note chime.
    "right": lambda: mix((0, tone(C6, 0.3)), (0.08, tone(E6, 0.3)), (0.16, tone(G6, 0.45))),
    # Try again: two gentle notes, friendly rather than a buzzer.
    "try_again": lambda: mix((0, tone(G5, 0.25, 0.4, decay=8)), (0.14, tone(E5, 0.35, 0.4, decay=8))),
    # Celebrate: a happy arpeggio with a sparkle on top.
    "celebrate": lambda: mix(
        (0, tone(C5, 0.4)),
        (0.1, tone(E5, 0.4)),
        (0.2, tone(G5, 0.4)),
        (0.3, tone(C6, 0.7, decay=4)),
        (0.42, tone(E6, 0.5, 0.25, decay=7)),
        (0.5, tone(G6, 0.5, 0.2, decay=7)),
        (0.58, tone(C7, 0.5, 0.15, decay=7)),
    ),
}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, make in SOUNDS.items():
        save(name, make())
        print(f"assets/sounds/{name}.wav")


if __name__ == "__main__":
    main()
