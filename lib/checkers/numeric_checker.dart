/// Checks number answers: `8`, `۸`, `2.5`, `-3`, `3/4`, `1 1/2`, `aath`.
library;

import 'normalize.dart';
import 'rational.dart';

/// Reads a number the way students type it. Returns null if the text is
/// not a number.
double? parseNumber(String input) => parseRational(input)?.toDouble();

/// Like [parseNumber] but exact: whole numbers, decimals, fractions
/// (`3/4`), mixed numbers (`1 1/2`, `-2 3/4`) and number words.
Rational? parseRational(String input) {
  final word = numberFromWord(input);
  if (word != null) return Rational(word);

  final text = normalizeInput(input).replaceAll(RegExp(r'\s+'), ' ').trim();
  if (text.isEmpty) return null;

  // Mixed number: whole, space, fraction.
  final mixed = RegExp(r'^([+-]?)(\d+) (\d+) ?/ ?(\d+)$').firstMatch(text);
  if (mixed != null) {
    final bottom = int.parse(mixed[4]!);
    if (bottom == 0) return null;
    final value =
        Rational(int.parse(mixed[2]!)) + Rational(int.parse(mixed[3]!), bottom);
    return mixed[1] == '-' ? -value : value;
  }

  // Spaces are fine around "/" but not inside a number ("1 2 3").
  final compact = text.replaceAll(RegExp(r' ?/ ?'), '/');
  if (compact.contains(' ')) return null;
  final slash = compact.indexOf('/');
  if (slash >= 0) {
    final top = Rational.tryParseDecimal(compact.substring(0, slash));
    final bottom = Rational.tryParseDecimal(compact.substring(slash + 1));
    if (top == null || bottom == null || bottom.isZero) return null;
    return top / bottom;
  }
  return Rational.tryParseDecimal(compact);
}

/// True if [value] equals [target] within [tolerance].
bool numbersMatch(double value, double target, {double tolerance = 0}) =>
    (value - target).abs() <= tolerance + 1e-9;
