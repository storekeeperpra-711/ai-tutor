/// Keeps short maths like `3 × 2 = 6` or `1/2` left-to-right inside Urdu
/// (right-to-left) text. Without this, Urdu text can show `6 = 2 × 3`.
///
/// It wraps each maths run in Unicode "left-to-right isolate" marks
/// (U+2066 ... U+2069), which are invisible.
library;

final _mathRun = RegExp(
  r'[0-9۰-۹A-Za-z(][0-9۰-۹A-Za-z×÷=+\-−/.() ]*[0-9۰-۹A-Za-z)]',
);
final _operator = RegExp(r'[×÷=+\-−/]');

String isolateMath(String text) => text.replaceAllMapped(_mathRun, (m) {
  final run = m[0]!;
  return _operator.hasMatch(run) ? '\u2066$run\u2069' : run;
});
