/// Checks a list of points, like the corners of a region:
/// `(0, 0), (4, 0), (0, 3)`. The order doesn't matter.
library;

import 'normalize.dart';
import 'numeric_checker.dart';
import 'rational.dart';

typedef Point = (Rational, Rational);

final _point = RegExp(r'\(([^(),]+),([^(),]+)\)');

/// Reads points written as `(x, y)`, separated by commas, semicolons,
/// spaces or "and". Throws [FormatException] if anything else is there.
List<Point> parsePoints(String input) {
  final text = normalizeInput(input);
  final points = <Point>[];
  for (final m in _point.allMatches(text)) {
    final x = parseRational(m[1]!.trim());
    final y = parseRational(m[2]!.trim());
    if (x == null || y == null) throw const FormatException('bad number');
    points.add((x, y));
  }
  final rest = text
      .replaceAll(_point, ' ')
      .replaceAll(RegExp(r'\band\b|اور|aur|[,;\s]', caseSensitive: false), '');
  if (points.isEmpty || rest.isNotEmpty) {
    throw const FormatException('not points');
  }
  return points;
}

/// `(4, 0)`, `(3/2, -1)`.
String describePoint(Point p) => '(${p.$1}, ${p.$2})';

enum PointsMistake {
  /// Not written as points.
  unreadable,

  /// `point` is not one of the expected points.
  wrongPoint,

  /// All the points are right, but `count` are missing.
  missing,
}

class PointsResult {
  const PointsResult.correct() : mistake = null, details = const {};
  const PointsResult(this.mistake, [this.details = const {}]);

  final PointsMistake? mistake;

  /// - wrongPoint: `point` (as written by [describePoint])
  /// - missing: `count`
  final Map<String, Object> details;

  bool get isCorrect => mistake == null;
}

/// Checks the student's points [input] against [expected] (in the same
/// form).
PointsResult checkPoints(String input, String expected) {
  final want = parsePoints(expected).toSet();
  final Set<Point> got;
  try {
    got = parsePoints(input).toSet();
  } on FormatException {
    return const PointsResult(PointsMistake.unreadable);
  }
  for (final p in got) {
    if (!want.contains(p)) {
      return PointsResult(PointsMistake.wrongPoint, {
        'point': describePoint(p),
      });
    }
  }
  final missing = want.length - got.length;
  if (missing > 0) {
    return PointsResult(PointsMistake.missing, {'count': missing});
  }
  return const PointsResult.correct();
}
