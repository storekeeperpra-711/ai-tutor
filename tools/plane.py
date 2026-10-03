"""Inequalities in x and y, with exact fractions: the same reading as
lib/checkers/half_plane_checker.dart, plus the corners of the region
several inequalities make (for linear programming lessons).

    >>> corners(["x + y <= 6", "x <= 4", "x >= 0", "y >= 0"])
    [(0, 0), (0, 6), (4, 0), (4, 2)]
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations

Point = tuple[Fraction, Fraction]


@dataclass(frozen=True)
class Linear2:
    """a·x + b·y + c"""

    a: Fraction
    b: Fraction
    c: Fraction

    def __add__(self, o: Linear2) -> Linear2:
        return Linear2(self.a + o.a, self.b + o.b, self.c + o.c)

    def __neg__(self) -> Linear2:
        return Linear2(-self.a, -self.b, -self.c)

    def __sub__(self, o: Linear2) -> Linear2:
        return self + -o

    def scale(self, k: Fraction) -> Linear2:
        return Linear2(self.a * k, self.b * k, self.c * k)

    @property
    def constant(self) -> bool:
        return self.a == 0 and self.b == 0

    def at(self, x: Fraction, y: Fraction) -> Fraction:
        return self.a * x + self.b * y + self.c


class _Parser:
    def __init__(self, text: str):
        self.text = text.replace(" ", "")
        self.pos = 0

    def parse(self) -> Linear2:
        if not self.text:
            raise ValueError("empty side")
        result = self.sum()
        if self.pos != len(self.text):
            raise ValueError("extra text")
        return result

    def peek(self) -> str | None:
        return self.text[self.pos] if self.pos < len(self.text) else None

    def sum(self) -> Linear2:
        result = self.product()
        while self.peek() in ("+", "-"):
            op = self.text[self.pos]
            self.pos += 1
            nxt = self.product()
            result = result + nxt if op == "+" else result - nxt
        return result

    def product(self) -> Linear2:
        result = self.unary()
        while True:
            c = self.peek()
            if c in ("*", "/"):
                self.pos += 1
                nxt = self.unary()
                result = _times(result, nxt) if c == "*" else _divide(result, nxt)
            elif c in ("(", "x", "y"):
                result = _times(result, self.unary())
            else:
                return result

    def unary(self) -> Linear2:
        if self.peek() == "-":
            self.pos += 1
            return -self.unary()
        if self.peek() == "+":
            self.pos += 1
            return self.unary()
        return self.atom()

    def atom(self) -> Linear2:
        c = self.peek()
        if c is None:
            raise ValueError("unexpected end")
        if c == "(":
            self.pos += 1
            inner = self.sum()
            if self.peek() != ")":
                raise ValueError("missing )")
            self.pos += 1
            return inner
        if c in ("x", "y"):
            self.pos += 1
            return Linear2(Fraction(c == "x"), Fraction(c == "y"), Fraction(0))
        match = re.compile(r"\d+(\.\d+)?|\.\d+").match(self.text, self.pos)
        if not match:
            raise ValueError(f"unexpected {c}")
        self.pos = match.end()
        return Linear2(Fraction(0), Fraction(0), Fraction(match.group()))


def _times(p: Linear2, q: Linear2) -> Linear2:
    if p.constant:
        return q.scale(p.c)
    if q.constant:
        return p.scale(q.c)
    raise ValueError("x times y")


def _divide(p: Linear2, q: Linear2) -> Linear2:
    if not q.constant or q.c == 0:
        raise ValueError("bad divisor")
    return p.scale(1 / q.c)


def parse_linear(text: str) -> Linear2:
    return _Parser(_normalize(text)).parse()


def _normalize(text: str) -> str:
    return text.replace("≤", "<=").replace("≥", ">=").replace("−", "-").replace("×", "*").replace("÷", "/")


@dataclass(frozen=True)
class HalfPlane:
    """lhs < 0, or lhs <= 0 when inclusive; lhs scaled so the first of a, b is ±1."""

    lhs: Linear2
    inclusive: bool

    def contains(self, p: Point) -> bool:
        value = self.lhs.at(*p)
        return value < 0 or (self.inclusive and value == 0)

    def on_line(self, p: Point) -> bool:
        return self.lhs.at(*p) == 0


def parse_half_plane(text: str) -> HalfPlane:
    """Reads `y <= 2x + 1`, `x + y > 4`, ... Raises ValueError if it can't."""
    text = _normalize(text)
    ops = re.findall(r"<=|>=|<|>", text)
    if len(ops) != 1 or ("=" in text and not ops[0].endswith("=")):
        raise ValueError("needs one of < <= > >=")
    left_text, right_text = re.split(r"<=|>=|<|>", text)
    left, right = parse_linear(left_text), parse_linear(right_text)
    diff = left - right if ops[0].startswith("<") else right - left
    lead = diff.a if diff.a != 0 else diff.b
    if lead == 0:
        raise ValueError("no x or y")
    return HalfPlane(diff.scale(1 / abs(lead)), ops[0].endswith("="))


def is_half_plane(text: str) -> bool:
    try:
        parse_half_plane(text)
        return True
    except (ValueError, ZeroDivisionError):
        return False


def _number(n: Fraction) -> str:
    return str(n.numerator) if n.denominator == 1 else f"{n.numerator}/{n.denominator}"


def describe(p: Point) -> str:
    return f"({_number(p[0])}, {_number(p[1])})"


def parse_points(text: str) -> list[Point]:
    """Reads `(0, 0), (4, 0)`. Raises ValueError if it can't."""
    pattern = re.compile(r"\(([^(),]+),([^(),]+)\)")
    points = [(Fraction(m.group(1).strip()), Fraction(m.group(2).strip())) for m in pattern.finditer(text)]
    rest = re.sub(r"\band\b|[,;\s]", "", pattern.sub(" ", text))
    if not points or rest:
        raise ValueError("not points")
    return points


def corners(constraints: list[str]) -> list[Point]:
    """The corners of the region where every constraint holds, sorted.
    Raises ValueError if the region is empty or not closed in."""
    planes = [parse_half_plane(c) for c in constraints]
    found = set()
    for p, q in combinations(planes, 2):
        (a1, b1, c1), (a2, b2, c2) = (p.lhs.a, p.lhs.b, p.lhs.c), (q.lhs.a, q.lhs.b, q.lhs.c)
        det = a1 * b2 - a2 * b1
        if det == 0:
            continue
        point = ((b1 * c2 - b2 * c1) / det, (a2 * c1 - a1 * c2) / det)
        # A corner of the closed region: the boundary lines are included
        # there even for < and > (the region comes as close as you like).
        if all(h.lhs.at(*point) <= 0 for h in planes):
            found.add(point)
    if not found:
        raise ValueError("the inequalities have no corner in common")
    if not _bounded(planes):
        raise ValueError("the region is not closed in on every side")
    return sorted(found)


def _bounded(planes: list[HalfPlane]) -> bool:
    # Closed in if no direction (dx, dy) can be walked forever: for every
    # direction some constraint grows along it. Directions to try: along
    # each boundary line, both ways.
    for h in planes:
        for sign in (1, -1):
            dx, dy = -h.lhs.b * sign, h.lhs.a * sign
            if all(g.lhs.a * dx + g.lhs.b * dy <= 0 for g in planes):
                return False
    return True


def value(objective: str, p: Point) -> Fraction:
    return parse_linear(objective).at(*p)
