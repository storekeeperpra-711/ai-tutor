/// Minimal number checking for Phase 1. Phase 2 replaces this with the
/// full set of checkers (fractions, mixed numbers, units, ...).
library;

/// Reads a number the way students type it: `8`, `۸`, `2.5`, `-3`, `3/4`.
/// Returns null if the text is not a number.
double? parseNumber(String input) {
  final text = _normalizeDigits(input).replaceAll(' ', '');
  if (text.isEmpty) return null;

  final slash = text.indexOf('/');
  if (slash > 0) {
    final top = double.tryParse(text.substring(0, slash));
    final bottom = double.tryParse(text.substring(slash + 1));
    if (top == null || bottom == null || bottom == 0) return null;
    return top / bottom;
  }
  return double.tryParse(text);
}

/// True if [value] equals [target] within [tolerance].
bool numbersMatch(double value, double target, {double tolerance = 0}) =>
    (value - target).abs() <= tolerance + 1e-9;

/// Turns Urdu (۰–۹) and Arabic (٠–٩) digits into 0–9, and the Arabic
/// decimal separator and minus sign into `.` and `-`.
String _normalizeDigits(String input) {
  final out = StringBuffer();
  for (final rune in input.trim().runes) {
    if (rune >= 0x06F0 && rune <= 0x06F9) {
      out.writeCharCode(0x30 + rune - 0x06F0);
    } else if (rune >= 0x0660 && rune <= 0x0669) {
      out.writeCharCode(0x30 + rune - 0x0660);
    } else if (rune == 0x066B) {
      out.write('.');
    } else if (rune == 0x2212) {
      out.write('-');
    } else {
      out.writeCharCode(rune);
    }
  }
  return out.toString();
}
