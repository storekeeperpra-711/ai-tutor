/// Checks fraction answers. Any equal value is correct (6/8 = 3/4 = 0.75),
/// unless the question asks for lowest terms.
library;

import 'normalize.dart';
import 'numeric_checker.dart';
import 'rational.dart';

enum FractionVerdict { correct, notSimplest, wrong, unreadable }

class FractionResult {
  const FractionResult(this.verdict, {this.value, this.simplest});

  final FractionVerdict verdict;

  /// What the student's answer equals.
  final Rational? value;

  /// The answer in lowest terms (for the "simplify" feedback).
  final Rational? simplest;

  bool get isCorrect => verdict == FractionVerdict.correct;
}

FractionResult checkFraction(
  String input,
  Rational expected, {
  bool requireSimplest = false,
}) {
  final value = parseRational(input);
  if (value == null) {
    return const FractionResult(FractionVerdict.unreadable);
  }
  if (value != expected) {
    return FractionResult(FractionVerdict.wrong, value: value);
  }
  if (requireSimplest && !_writtenInLowestTerms(input)) {
    return FractionResult(
      FractionVerdict.notSimplest,
      value: value,
      simplest: expected,
    );
  }
  return FractionResult(FractionVerdict.correct, value: value);
}

/// True unless the student wrote a fraction a/b that can still be divided
/// (like 6/8). Whole numbers, decimals and mixed numbers like 1 1/2 count
/// as simplest when their fraction part is.
bool _writtenInLowestTerms(String input) {
  final match = RegExp(r'(\d+)\s*/\s*(\d+)\s*$')
      .firstMatch(normalizeInput(input));
  if (match == null) return true;
  return gcdOf([int.parse(match[1]!), int.parse(match[2]!)]) == 1;
}
