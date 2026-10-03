/// Checks a linear inequality in two unknowns, like `y <= 2x + 1` or
/// `x + y < 4`: the answer must describe the same region of the
/// xy-plane (the same boundary line, the same side, and the line included
/// or not), however it is written.
library;

import 'normalize.dart';
import 'rational.dart';

/// `a·x + b·y + c` with exact fractions.
class Linear2 {
  const Linear2(this.a, this.b, this.c);

  final Rational a;
  final Rational b;
  final Rational c;

  bool get isConstant => a.isZero && b.isZero;

  Linear2 operator +(Linear2 o) => Linear2(a + o.a, b + o.b, c + o.c);
  Linear2 operator -(Linear2 o) => Linear2(a - o.a, b - o.b, c - o.c);
  Linear2 operator -() => Linear2(-a, -b, -c);
  Linear2 scale(Rational k) => Linear2(a * k, b * k, c * k);

  Linear2 operator *(Linear2 o) {
    if (isConstant) return o.scale(c);
    if (o.isConstant) return scale(o.c);
    throw const FormatException('x times y');
  }

  Linear2 operator /(Linear2 o) {
    if (!o.isConstant || o.c.isZero) throw const FormatException('bad divisor');
    return scale(Rational.one / o.c);
  }

  Rational valueAt(Rational x, Rational y) => a * x + b * y + c;
}

/// Reads one side, like `2(x + y) - 3` or `x/2`, as `a·x + b·y + c`.
/// Throws [FormatException] if it can't.
Linear2 parseLinear2(String text) => _Parser(text).parseAll();

/// The points on one side of a straight line: `a·x + b·y + c < 0`
/// (or `≤ 0`), stored so that the same region always gives the same
/// numbers.
class HalfPlane {
  factory HalfPlane(Linear2 lhs, {required bool inclusive}) {
    // Make the first of a, b equal to 1 or −1 (dividing by a positive
    // number keeps the side).
    final lead = lhs.a.isZero ? lhs.b : lhs.a;
    if (lead.isZero) throw const FormatException('no x or y');
    final k = Rational.one / (lead.compareTo(Rational.zero) < 0 ? -lead : lead);
    return HalfPlane._(lhs.scale(k), inclusive);
  }

  const HalfPlane._(this.lhs, this.inclusive);

  /// The region is `lhs < 0`, or `lhs ≤ 0` when [inclusive].
  final Linear2 lhs;

  /// The boundary line is part of the region (≤ or ≥: a solid line).
  final bool inclusive;

  bool contains(Rational x, Rational y) {
    final sign = lhs.valueAt(x, y).compareTo(Rational.zero);
    return sign < 0 || (inclusive && sign == 0);
  }

  bool sameLine(HalfPlane o) => _same(lhs, o.lhs) || _same(lhs, -o.lhs);

  static bool _same(Linear2 p, Linear2 q) =>
      p.a == q.a && p.b == q.b && p.c == q.c;

  @override
  bool operator ==(Object other) =>
      other is HalfPlane &&
      _same(lhs, other.lhs) &&
      inclusive == other.inclusive;

  @override
  int get hashCode => Object.hash(lhs.a, lhs.b, lhs.c, inclusive);
}

final _operator = RegExp(r'<=|>=|<|>');

/// Reads one inequality in x and y, like `y >= (1/2)x - 3` or
/// `2x + 3y <= 12`. Throws [FormatException] if it can't, or if it has no
/// x or y.
HalfPlane parseHalfPlane(String input) {
  final text = normalizeInput(input);
  final ops = _operator.allMatches(text).toList();
  if (ops.length != 1 || text.contains('=') && !ops.single[0]!.endsWith('=')) {
    throw const FormatException('needs one of < <= > >=');
  }
  final op = ops.single;
  final left = parseLinear2(text.substring(0, op.start));
  final right = parseLinear2(text.substring(op.end));
  // left (op) right  →  (left − right) < 0, flipping for > and ≥.
  final diff = op[0]!.startsWith('<') ? left - right : right - left;
  return HalfPlane(diff, inclusive: op[0]!.endsWith('='));
}

enum HalfPlaneMistake {
  /// Not one inequality in x and y.
  unreadable,

  /// The boundary line is a different line.
  wrongLine,

  /// The right line, but the other side of it.
  wrongSide,

  /// The right side, but the line should (or shouldn't) be included:
  /// ≤ for <, a solid line for a dashed one.
  wrongBoundary,
}

/// Null when [input] describes the same region as [expected].
HalfPlaneMistake? checkHalfPlane(String input, String expected) {
  final want = parseHalfPlane(expected);
  final HalfPlane got;
  try {
    got = parseHalfPlane(input);
  } on FormatException {
    return HalfPlaneMistake.unreadable;
  }
  if (got == want) return null;
  if (!got.sameLine(want)) return HalfPlaneMistake.wrongLine;
  return HalfPlane._same(got.lhs, want.lhs)
      ? HalfPlaneMistake.wrongBoundary
      : HalfPlaneMistake.wrongSide;
}

/// Recursive-descent parser for `+ - * / ( )`, numbers, x and y, and
/// implied multiplication (`2x`, `3(x + y)`).
class _Parser {
  _Parser(String text) : _text = text.replaceAll(' ', '');

  final String _text;
  var _pos = 0;

  static const _x = Linear2(Rational.one, Rational.zero, Rational.zero);
  static const _y = Linear2(Rational.zero, Rational.one, Rational.zero);

  Linear2 parseAll() {
    if (_text.isEmpty) throw const FormatException('empty side');
    final result = _sum();
    if (_pos != _text.length) throw const FormatException('extra text');
    return result;
  }

  String? get _peek => _pos < _text.length ? _text[_pos] : null;

  Linear2 _sum() {
    var result = _product();
    while (_peek == '+' || _peek == '-') {
      final op = _text[_pos++];
      final next = _product();
      result = op == '+' ? result + next : result - next;
    }
    return result;
  }

  Linear2 _product() {
    var result = _unary();
    while (true) {
      final c = _peek;
      if (c == '*' || c == '/') {
        _pos++;
        final next = _unary();
        result = c == '*' ? result * next : result / next;
      } else if (c == '(' || c == 'x' || c == 'y') {
        result = result * _unary();
      } else {
        return result;
      }
    }
  }

  Linear2 _unary() {
    if (_peek == '-') {
      _pos++;
      return -_unary();
    }
    if (_peek == '+') {
      _pos++;
      return _unary();
    }
    return _atom();
  }

  Linear2 _atom() {
    final c = _peek;
    if (c == null) throw const FormatException('unexpected end');
    if (c == '(') {
      _pos++;
      final inner = _sum();
      if (_peek != ')') throw const FormatException('missing )');
      _pos++;
      return inner;
    }
    if (c == 'x' || c == 'y') {
      _pos++;
      return c == 'x' ? _x : _y;
    }
    final match = RegExp(r'\d+(\.\d+)?|\.\d+').matchAsPrefix(_text, _pos);
    if (match == null) throw FormatException('unexpected $c');
    _pos = match.end;
    final value = Rational.tryParseDecimal(match[0]!);
    if (value == null) throw const FormatException('number too long');
    return Linear2(Rational.zero, Rational.zero, value);
  }
}
