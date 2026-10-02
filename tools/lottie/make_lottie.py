#!/usr/bin/env python3
"""Make the app's small Lottie animations (assets/lottie/) from code.

Usage: python tools/lottie/make_lottie.py

Hand-written so they stay tiny (a few KB) and need no design tool.
Each function returns one animation as a dict in the Lottie format.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

OUT = Path(__file__).resolve().parents[2] / "assets" / "lottie"
FPS = 30
EASE_OUT = {"o": {"x": [0.2], "y": [0]}, "i": {"x": [0.3], "y": [1]}}


def static(value):
    return {"a": 0, "k": value}


def animated(*frames):
    """frames: (time, value) pairs. Every keyframe but the last gets easing."""
    keys = []
    for n, (t, v) in enumerate(frames):
        key = {"t": t, "s": v if isinstance(v, list) else [v]}
        if n < len(frames) - 1:
            key.update(EASE_OUT)
        keys.append(key)
    return {"a": 1, "k": keys}


def transform(position, scale=None, opacity=None, rotation=0):
    return {
        "a": static([0, 0, 0]),
        "p": position,
        "s": scale or static([100, 100, 100]),
        "r": static(rotation),
        "o": opacity or static(100),
    }


def fill(rgb):
    return {"ty": "fl", "c": static([*rgb, 1]), "o": static(100), "r": 1}


def group(*items):
    return {
        "ty": "gr",
        "it": [
            *items,
            {
                "ty": "tr",
                "p": static([0, 0]),
                "a": static([0, 0]),
                "s": static([100, 100]),
                "r": static(0),
                "o": static(100),
            },
        ],
    }


def layer(index, name, ks, shapes, end):
    return {
        "ddd": 0,
        "ind": index,
        "ty": 4,
        "nm": name,
        "sr": 1,
        "ks": ks,
        "ao": 0,
        "shapes": shapes,
        "ip": 0,
        "op": end,
        "st": 0,
        "bm": 0,
    }


def animation(name, size, end, layers):
    return {
        "v": "5.7.4",
        "fr": FPS,
        "ip": 0,
        "op": end,
        "w": size,
        "h": size,
        "nm": name,
        "ddd": 0,
        "assets": [],
        "layers": layers,
    }


def star(outer):
    return {
        "ty": "sr",
        "sy": 1,
        "d": 1,
        "pt": static(5),
        "p": static([0, 0]),
        "r": static(0),
        "ir": static(outer * 0.45),
        "is": static(0),
        "or": static(outer),
        "os": static(0),
    }


def celebrate():
    """Stars and dots burst out from the middle and fade (1.5 s)."""
    size, end, c = 400, 45, 200
    colors = [(1, 0.72, 0.15), (0.26, 0.63, 0.28), (0.12, 0.53, 0.9), (0.9, 0.3, 0.45)]
    layers = []
    for n in range(14):
        angle = 2 * math.pi * n / 14
        reach = 150 if n % 2 == 0 else 110
        target = [c + reach * math.cos(angle), c + reach * math.sin(angle), 0]
        shape = star(18) if n % 2 == 0 else {"ty": "el", "p": static([0, 0]), "s": static([16, 16])}
        layers.append(
            layer(
                n + 1,
                f"bit{n}",
                transform(
                    animated((0, [c, c, 0]), (30, target)),
                    scale=animated((0, [20, 20, 100]), (12, [110, 110, 100]), (end, [80, 80, 100])),
                    opacity=animated((0, 100), (24, 100), (end, 0)),
                    rotation=0,
                ),
                [group(shape, fill(colors[n % len(colors)]))],
                end,
            )
        )
    return animation("celebrate", size, end, layers)


def roti_quarters():
    """A roti is cut into quarters and the pieces move apart (3 s, for
    the dividing fractions lesson)."""
    size, end, c, r = 400, 90, 200, 130
    k = 0.5523 * r  # Bezier handle length for a quarter circle.
    quarter = {
        "ty": "sh",
        "ks": static(
            {
                "c": True,
                "v": [[0, 0], [r, 0], [0, r]],
                "i": [[0, 0], [0, 0], [k, 0]],
                "o": [[0, 0], [0, k], [0, 0]],
            }
        ),
    }
    edge = {"ty": "st", "c": static([0.55, 0.36, 0.2, 1]), "o": static(100), "w": static(4), "lc": 2, "lj": 2}
    layers = []
    for n in range(4):
        angle = math.pi / 4 + n * math.pi / 2  # Each piece moves out along its middle.
        apart = [c + 28 * math.cos(angle), c + 28 * math.sin(angle), 0]
        layers.append(
            layer(
                n + 1,
                f"quarter{n}",
                transform(
                    animated((0, [c, c, 0]), (20 + 12 * n, [c, c, 0]), (40 + 12 * n, apart), (end, apart)),
                    rotation=90 * n,
                ),
                [group(quarter, fill((0.96, 0.78, 0.45)), edge)],
                end,
            )
        )
    return animation("roti_quarters", size, end, layers)


ANIMATIONS = {"celebrate.json": celebrate, "roti_quarters.json": roti_quarters}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, make in ANIMATIONS.items():
        path = OUT / name
        path.write_text(json.dumps(make(), separators=(",", ":")) + "\n", encoding="utf-8")
        print(f"wrote {path.relative_to(OUT.parents[1])} ({path.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
