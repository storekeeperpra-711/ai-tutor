/// Keeps maths like `3 × 2 = 6`, `x + 3 = 7`, `-8` or `4 ∈ A` in one piece.
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
// A set written with braces, like {2, 4, 6}.
const _set = r'\{[^{}]*\}';
// A set function like n(A) or P(A ∪ B).
const _function = r"[A-Za-z]\([A-Za-z0-9∪∩' ]+\)";
// A number (with an optional letter or two, like 2x), one letter, a set,
// a set function, or the empty set.
const _operand =
    '\\(*[-−]?(?:$_set|$_function|∅|$_number[A-Za-z]{0,2}|[A-Za-z][²³\']?(?![A-Za-z]))\\)*';
// Set signs (∈ ∉ ⊂ ⊆ ∪ ∩ ...) are mirrored by the right-to-left rules unless
// they sit inside the isolate, so they count as operators too.
const _operator = r'[×÷=≠≈↔+\-−/<>≤≥∈∉∋∌⊂⊃⊆⊇⊄∪∩∖]';

// An equation: operands joined by operators. Or a lone negative number, or
// a set on its own.
final _math = RegExp(
  '(?:$_operand(?:[\u00a0 ]*$_operator[\u00a0 ]*$_operand)+)'
  '|(?<![0-9۰-۹A-Za-z)])[-−]$_number'
  '|$_set',
);

// Spaces inside {braces} stay normal so a long set can still wrap there.
String _glue(String run) => run.splitMapJoin(
  RegExp(_set),
  onMatch: (m) => m[0]!.replaceAll('-', '\u2212'),
  onNonMatch: (s) => s
      .replaceAll(' ', '\u00a0')
      .replaceAll('-', '\u2212')
      .replaceAll('/', '/\u2060'),
);

/// Returns [text] with maths kept together. [rtl] also adds the
/// left-to-right isolate marks needed inside Urdu text.
String isolateMath(String text, {bool rtl = true}) =>
    text.replaceAllMapped(_math, (m) {
      final run = _glue(m[0]!);
      return rtl ? '\u2066$run\u2069' : run;
    });
