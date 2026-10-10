/// Keeps maths like `3 × 2 = 6`, `x + 3 = 7` or `-8` in one piece.
///
/// In Urdu (right-to-left) text, the maths is wrapped in invisible
/// "left-to-right isolate" marks (U+2066 ... U+2069). Without this Urdu text
/// can show `6 = 2 × 3`, or `-8` as `8-`.
///
/// In both languages the spaces inside the maths become no-break spaces and
/// the minus becomes a real minus sign (U+2212), so an equation never splits
/// across two lines: it fits on one line or moves down whole.
library;

const _digit = r'[0-9۰-۹]';
const _number = '$_digit+(?:[.,]$_digit+)*';
// A number (with an optional letter or two, like 2x), or one letter.
const _operand =
    '\\(*[-−]?(?:$_number[A-Za-z]{0,2}|[A-Za-z][²³]?(?![A-Za-z]))\\)*';
const _operator = r'[×÷=+\-−/<>≤≥]';

// An equation: operands joined by operators. Or a lone negative number.
final _math = RegExp(
  '(?:$_operand(?:[  ]*$_operator[  ]*$_operand)+)'
  '|(?<![0-9۰-۹A-Za-z)])[-−]$_number',
);

String _glue(String run) =>
    run.replaceAll(' ', ' ').replaceAll('-', '−').replaceAll('/', '/⁠');

/// Returns [text] with maths kept together. [rtl] also adds the
/// left-to-right isolate marks needed inside Urdu text.
String isolateMath(String text, {bool rtl = true}) =>
    text.replaceAllMapped(_math, (m) {
      final run = _glue(m[0]!);
      return rtl ? '\u2066$run\u2069' : run;
    });
