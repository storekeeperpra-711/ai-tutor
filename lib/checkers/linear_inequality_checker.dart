/// Checks working for a linear inequality in one unknown, line by line,
/// like the linear equation checker: every line must have the same
/// solutions as the line before, and the last line must be `x < number`
/// (or `≤ > ≥`, or `number > x`).
library;

import 'linear_equation_checker.dart';
import 'normalize.dart';
import 'rational.dart';

/// The numbers that make an inequality true.
sealed class SolutionSet {
  const SolutionSet();
}

/// Every number (e.g. `0x < 3`).
class AllNumbers extends SolutionSet {
  const AllNumbers();
  @override
  bool operator ==(Object other) => other is AllNumbers;
  @override
  int get hashCode => 1;
}

/// No number (e.g. `0x > 3`).
class NoNumbers extends SolutionSet {
  const NoNumbers();
  @override
  bool operator ==(Object other) => other is NoNumbers;
  @override
  int get hashCode => 2;
}

/// `x < bound`, `x ≤ bound`, `x > bound` or `x ≥ bound`.
class Ray extends SolutionSet {
  const Ray(this.bound, {required this.below, required this.inclusive});

  final Rational bound;

  /// The solutions are less than [bound].
  final bool below;

  /// [bound] itself is a solution (≤ or ≥: a filled dot on the line).
  final bool inclusive;

  /// The way students write it: `x <= 4`.
  String describe(String variable) =>
      '$variable ${below ? '<' : '>'}${inclusive ? '=' : ''} $bound';

  @override
  bool operator ==(Object other) =>
      other is Ray &&
      other.bound == bound &&
      other.below == below &&
      other.inclusive == inclusive;
  @override
  int get hashCode => Object.hash(bound, below, inclusive);
}

class ParsedInequality {
  const ParsedInequality(this.left, this.op, this.right);

  final Linear left;

  /// One of `<`, `<=`, `>`, `>=`.
  final String op;
  final Linear right;

  SolutionSet get solutions {
    // left − right (op) 0, i.e. a·x + b (op) 0.
    final diff = left - right;
    final below = op.startsWith('<');
    final inclusive = op.endsWith('=');
    if (diff.a.isZero) {
      final sign = diff.b.compareTo(Rational.zero);
      final holds =
          (below && (sign < 0 || (inclusive && sign == 0))) ||
          (!below && (sign > 0 || (inclusive && sign == 0)));
      return holds ? const AllNumbers() : const NoNumbers();
    }
    // a·x (op) −b. Dividing by a negative a flips the sign.
    final negative = diff.a.compareTo(Rational.zero) < 0;
    return Ray(
      -diff.b / diff.a,
      below: below != negative,
      inclusive: inclusive,
    );
  }

  /// The solutions if this line reads `x op number` (or `number op x`).
  Ray? get finalRay {
    bool isX(Linear l) => l.a == Rational.one && l.b.isZero;
    if ((isX(left) && right.a.isZero) || (isX(right) && left.a.isZero)) {
      return solutions as Ray;
    }
    return null;
  }
}

final _operator = RegExp(r'<=|>=|<|>');

/// Reads one inequality like `2x - 3 < 7` or `5 >= (x + 1)/2`.
/// Throws [FormatException] if it can't.
ParsedInequality parseLinearInequality(String input, {String variable = 'x'}) {
  final text = normalizeInput(input);
  final ops = _operator.allMatches(text).toList();
  if (ops.length != 1 || text.contains('=') && !ops.single[0]!.endsWith('=')) {
    throw const FormatException('needs one of < <= > >=');
  }
  final op = ops.single;
  return ParsedInequality(
    parseLinearExpression(text.substring(0, op.start), variable: variable),
    op[0]!,
    parseLinearExpression(text.substring(op.end), variable: variable),
  );
}

enum InequalityMistake {
  /// A line can't be read as an inequality (`line` is 1-based).
  unreadable,

  /// This line has different solutions from the line before.
  brokenStep,

  /// Like [brokenStep], but only the direction changed: usually from
  /// multiplying or dividing by a negative number without flipping the
  /// sign (or flipping it when that wasn't needed).
  wrongDirection,

  /// Working is correct so far but doesn't end in `x < number`.
  notFinished,
}

class InequalityResult {
  const InequalityResult.correct(this.solutions)
    : mistake = null,
      details = const {};
  const InequalityResult(this.mistake, [this.details = const {}])
    : solutions = null;

  final InequalityMistake? mistake;

  /// The student's final answer when correct.
  final Ray? solutions;

  /// - unreadable, brokenStep, wrongDirection: `line` (1-based)
  final Map<String, Object> details;

  bool get isCorrect => mistake == null;
}

/// Checks the student's working [input] (one inequality per line, or lines
/// separated by `;`) for solving [inequality].
InequalityResult checkInequalityWorking(
  String input,
  String inequality, {
  String variable = 'x',
}) {
  final original = parseLinearInequality(inequality, variable: variable);
  final lines = input
      .split(RegExp(r'[\n;]'))
      .map((l) => l.trim())
      .where((l) => l.isNotEmpty)
      .toList();
  if (lines.isEmpty) {
    return const InequalityResult(InequalityMistake.unreadable, {'line': 1});
  }

  var previous = original.solutions;
  ParsedInequality? last;
  for (var i = 0; i < lines.length; i++) {
    final ParsedInequality parsed;
    try {
      parsed = parseLinearInequality(lines[i], variable: variable);
    } on FormatException {
      return InequalityResult(InequalityMistake.unreadable, {'line': i + 1});
    }
    final now = parsed.solutions;
    if (now != previous) {
      final flipped =
          now is Ray &&
          previous is Ray &&
          now.bound == previous.bound &&
          now.below != previous.below;
      return InequalityResult(
        flipped
            ? InequalityMistake.wrongDirection
            : InequalityMistake.brokenStep,
        {'line': i + 1},
      );
    }
    previous = now;
    last = parsed;
  }

  final ray = last!.finalRay;
  if (ray == null) return const InequalityResult(InequalityMistake.notFinished);
  return InequalityResult.correct(ray);
}
