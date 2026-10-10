"""Figures for the chapter 10 practice sets. Every coordinate is worked out
here from the stated angles and lengths, so the picture matches the numbers.
Angles are in degrees, measured anticlockwise from the right-hand direction
(the usual way); screen y points down, so they are flipped when drawn."""
import math

from common import T


def r1(v):
    return round(v, 1)


def pt(p):
    return [r1(p[0]), r1(p[1])]


def label(at, text):
    return {"kind": "label", "at": pt(at), "text": text}


def dot(at):
    return {"kind": "point", "at": pt(at)}


def seg(a, b, dashed=False):
    item = {"kind": "line", "from": pt(a), "to": pt(b)}
    if dashed:
        item["style"] = "dashed"
    return item


def fig(w, h, en, ur, items):
    """A figure block; checks that everything is inside the box and labels keep 2.5% from the edge."""
    margin = 0.025 * max(w, h)
    for it in items:
        reach = it.get("radius", 0)
        pts = [*it.get("points", []), *(it[k] for k in ("from", "to", "center", "at") if k in it)]
        for x, y in pts:
            assert reach <= x <= w - reach and reach <= y <= h - reach, (en, it)
            if it["kind"] == "label":
                assert margin <= x <= w - margin and margin <= y <= h - margin, (en, it)
    return {"width": w, "height": h, "alt": T(en, ur), "items": items}


def with_fig(step, figure):
    step["figure"] = figure
    return step


def at_angle(c, length, deg):
    """The point `length` from c in direction `deg` (anticlockwise from the right)."""
    return (c[0] + length * math.cos(math.radians(deg)), c[1] - length * math.sin(math.radians(deg)))


def angle_arc(c, a1, a2, radius, dashed=False):
    """An arc round c from direction a1 to direction a2 (a1 < a2, anticlockwise)."""
    assert a1 < a2
    item = {"kind": "arc", "center": pt(c), "radius": radius, "start": r1((360 - a2) % 360), "sweep": r1(a2 - a1)}
    if dashed:
        item["style"] = "dashed"
    return item


def arc_toward(center, target, radius, spread=30):
    """A short dashed compass arc centred on `center`, drawn across `target`."""
    cx, cy = center
    ang = math.degrees(math.atan2(target[1] - cy, target[0] - cx))
    return {"kind": "arc", "center": pt(center), "radius": radius,
            "start": r1((ang - spread / 2) % 360), "sweep": spread, "style": "dashed"}


def crossings(a, b, radius):
    """Where two circles of the same radius round a and b meet (above, below the line a-b when it is horizontal)."""
    mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
    half = math.dist(a, b) / 2
    assert radius > half, "the compass must open more than half of AB"
    h = math.sqrt(radius ** 2 - half ** 2)
    ux, uy = (b[0] - a[0]) / (2 * half), (b[1] - a[1]) / (2 * half)
    return (mx + uy * h, my - ux * h), (mx - uy * h, my + ux * h)


def right_mark(x, y, size=4):
    """A small right-angle box above and to the right of (x, y)."""
    return [seg((x, y - size), (x + size, y - size)), seg((x + size, y - size), (x + size, y))]


# ---------- angle pictures ----------

def rays_fig(w, h, o, base, rays, en, ur, dashed=(), arcs=None):
    """A base arm to the right of o and rays at the given angles. `rays` is a
    list of (angle, text); text goes beyond the end of the ray. Rays in
    `dashed` are dashed."""
    items = [seg(o, (o[0] + base, o[1])), dot(o)]
    for ang, text in rays:
        assert 0 < ang < 180
        items.append(seg(o, at_angle(o, base * 0.8, ang), dashed=ang in dashed))
        if text:
            items.append(label(at_angle(o, base * 0.8 + 7, ang), text))
    for a1, a2, rad in arcs or []:
        items.append(angle_arc(o, a1, a2, rad))
    return fig(w, h, en, ur, items)


def line_fig(rays, texts, en, ur, w=130, h=64):
    """A straight horizontal line with a point O on it and rays from O at the
    given angles (0 < angle < 180). `texts` gives one label for each angle
    between neighbouring rays (including the line itself), left to right
    from the right-hand end: len(texts) == len(rays) + 1."""
    o = (w / 2, h - 10)
    assert len(texts) == len(rays) + 1 and rays == sorted(rays)
    items = [seg((8, o[1]), (w - 8, o[1])), dot(o)]
    for a in rays:
        items.append(seg(o, at_angle(o, 42, a)))
    edges = [0, *rays, 180]
    for k, text in enumerate(texts):
        a1, a2 = edges[k], edges[k + 1]
        if text:
            items.append(angle_arc(o, a1, a2, 10))
            items.append(label(at_angle(o, 21 if a2 - a1 > 25 else 25, (a1 + a2) / 2), text))
    return fig(w, h, en, ur, items)


def triangle_points(a_deg, b_deg, width=70):
    """A triangle with base from (0, 0) to (width, 0) and angles a_deg at the
    left, b_deg at the right, apex up. Returns (A, B, C) in maths coordinates."""
    c_deg = 180 - a_deg - b_deg
    assert c_deg > 0
    ac = width * math.sin(math.radians(b_deg)) / math.sin(math.radians(c_deg))
    return (0, 0), (width, 0), (ac * math.cos(math.radians(a_deg)), ac * math.sin(math.radians(a_deg)))


def tri_fig(a_deg, b_deg, texts, en, ur, w=120, h=76, names=("A", "B", "C")):
    """A triangle with angle texts (left, right, apex) written inside the
    corners, and the corner names outside. Scaled to fit the box."""
    A, B, C = triangle_points(a_deg, b_deg, 100)
    xs = [p[0] for p in (A, B, C)]
    span, height = max(xs) - min(xs), C[1]
    scale = min((w - 40) / span, (h - 26) / height)
    ox = (w - span * scale) / 2 - min(xs) * scale
    oy = h - 13
    X = [(ox + p[0] * scale, oy - p[1] * scale) for p in (A, B, C)]
    items = [seg(X[0], X[1]), seg(X[1], X[2]), seg(X[2], X[0])]
    cen = (sum(p[0] for p in X) / 3, sum(p[1] for p in X) / 3)
    for p, t, n in zip(X, texts, names):
        d = math.dist(p, cen)
        ux, uy = (cen[0] - p[0]) / d, (cen[1] - p[1]) / d
        if t:
            items.append(label((p[0] + 17 * ux, p[1] + 17 * uy), t))
        items.append(label((p[0] - 7 * ux, p[1] - 7 * uy), n))
    return fig(w, h, en, ur, items)
