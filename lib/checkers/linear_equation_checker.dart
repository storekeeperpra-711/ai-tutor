/// Checks working for a linear equation in one unknown, line by line,
/// like the balance-scale lesson: every line must keep the scale balanced
/// (have the same solution as the line before), and the last line must be
/// `x = number`, checked by putting it back into the original equation.
library;

import 'normalize.dart';
import 'rational.dart';

/// `a·x + b` with exact fractions.
class Linear {
  const Linear(this.a, this.b);

  final Rational a;
  final Rational b;

  Linear operator +(Linear o) => Linear(a + o.a, b + o.b);
  Linear operator -(Linear o) => Linear(a - o.a, b - o.b);
  Linear operator -() => Linear(-a, -b);

  Linear operator *(Linear o) {
    if (!a.isZero && !o.a.isZero) throw const FormatException('x times x');
    return Linear(a * o.b + o.a * b, b * o.b);
  }

  Linear operator /(Linear o) {
    if (!o.a.isZero || o.b.isZero) throw const FormatException('bad divisor');
    return Linear(a / o.b, b / o.b);
  }

  Rational valueAt(Rational x) => a * x + b;
}

/// What a line (an equation) says about the unknown.
sealed class Solution {
  const Solution();
}

class OneSolution extends Solution {
  const OneSolution(this.value);
  final Rational value;
  @override
  bool operator ==(Object other) =>
      other is OneSolution && other.value == value;
  @override
  int get hashCode => value.hashCode;
}

class AnyValue extends Solution {
  const AnyValue();
  @override
  bool operator ==(Object other) => other is AnyValue;
  @override
  int get hashCode => 1;
}

class NoValue extends Solution {
  const NoValue();
  @override
  bool operator ==(Object other) => other is NoValue;
  @override
  int get hashCode => 2;
}

class ParsedEquation {
  const ParsedEquation(this.left, this.right);

  final Linear left;
  final Linear right;

  Solution get solution {
    final diff = left - right; // a·x + b = 0
    if (!diff.a.isZero) return OneSolution(-diff.b / diff.a);
    return diff.b.isZero ? const AnyValue() : const NoValue();
  }

  /// The value if this line reads `x = number` (or `number = x`).
  Rational? get finalValue {
    bool isX(Linear l) => l.a == Rational.one && l.b.isZero;
    if (isX(left) && right.a.isZero) return right.b;
    if (isX(right) && left.a.isZero) return left.b;
    return null;
  }
}

/// Reads one equation like `2x + 3 = 11` or `3(x - 1) = x/2 + 4`.
/// Throws [FormatException] if it can't.
ParsedEquation parseLinearEquation(String input, {String variable = 'x'}) {
  final sides = normalizeInput(input).split('=');
  if (sides.length != 2) throw const FormatException('needs one =');
  return ParsedEquation(
    _ExpressionParser(sides[0], variable).parseAll(),
    _ExpressionParser(sides[1], variable).parseAll(),
  );
}

enum LinearMistake {
  /// A line can't be read as an equation (`line` is 1-based).
  unreadable,

  /// This line doesn't have the same solution as the line before.
  brokenStep,

  /// Working is correct so far but doesn't end in `x = number`.
  notFinished,
}

class LinearResult {
  const LinearResult.correct(this.value) : mistake = null, details = const {};
  const LinearResult(this.mistake, [this.details = const {}]) : value = null;

  final LinearMistake? mistake;

  /// The student's final answer when correct.
  final Rational? value;

  /// - unreadable, brokenStep: `line` (1-based line of the student's work)
  final Map<String, Object> details;

  bool get isCorrect => mistake == null;
}

/// Checks the student's working [input] (one equation per line, or lines
/// separated by `;`) for solving [equation].
LinearResult checkLinearWorking(
  String input,
  String equation, {
  String variable = 'x',
}) {
  final original = parseLinearEquation(equation, variable: variable);
  final lines = input
      .split(RegExp(r'[\n;]'))
      .map((l) => l.trim())
      .where((l) => l.isNotEmpty)
      .toList();
  if (lines.isEmpty) {
    return const LinearResult(LinearMistake.unreadable, {'line': 1});
  }

  var previous = original.solution;
  ParsedEquation? last;
  for (var i = 0; i < lines.length; i++) {
    final ParsedEquation parsed;
    try {
      parsed = parseLinearEquation(lines[i], variable: variable);
    } on FormatException {
      return LinearResult(LinearMistake.unreadable, {'line': i + 1});
    }
    if (parsed.solution != previous) {
      return LinearResult(LinearMistake.brokenStep, {'line': i + 1});
    }
    previous = parsed.solution;
    last = parsed;
  }

  final value = last!.finalValue;
  // Substitution check: the answer must make the original equation true.
  if (value == null ||
      original.left.valueAt(value) != original.right.valueAt(value)) {
    return const LinearResult(LinearMistake.notFinished);
  }
  return LinearResult.correct(value);
}

/// Recursive-descent parser for `+ - * / ( )`, numbers, the unknown,
/// and implied multiplication (`2x`, `3(x+1)`, `(x+1)2` is not allowed).
class _ExpressionParser {
  _ExpressionParser(String text, this.variable)
    : _text = text.replaceAll(' ', '');

  final String _text;
  final String variable;
  var _pos = 0;

  Linear parseAll() {
    if (_text.isEmpty) throw const FormatException('empty side');
    final result = _sum();
    if (_pos != _text.length) throw const FormatException('extra text');
    return result;
  }

  String? get _peek => _pos < _text.length ? _text[_pos] : null;

  Linear _sum() {
    var result = _product();
    while (_peek == '+' || _peek == '-') {
      final op = _text[_pos++];
      final next = _product();
      result = op == '+' ? result + next : result - next;
    }
    return result;
  }

  Linear _product() {
    var result = _unary();
    while (true) {
      final c = _peek;
      if (c == '*' || c == '/') {
        _pos++;
        final next = _unary();
        result = c == '*' ? result * next : result / next;
      } else if (c != null && (c == '(' || c == variable)) {
        result = result * _unary(); // implied multiplication: 2x, 3(x+1)
      } else {
        return result;
      }
    }
  }

  Linear _unary() {
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

  Linear _atom() {
    final c = _peek;
    if (c == null) throw const FormatException('unexpected end');
    if (c == '(') {
      _pos++;
      final inner = _sum();
      if (_peek != ')') throw const FormatException('missing )');
      _pos++;
      return inner;
    }
    if (c == variable) {
      _pos++;
      return const Linear(Rational.one, Rational.zero);
    }
    final match = RegExp(r'\d+(\.\d+)?|\.\d+').matchAsPrefix(_text, _pos);
    if (match == null) throw FormatException('unexpected $c');
    _pos = match.end;
    return Linear(Rational.zero, Rational.tryParseDecimal(match[0]!)!);
  }
}
