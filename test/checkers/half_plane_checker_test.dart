import 'package:ai_tutor/checkers/half_plane_checker.dart';
import 'package:ai_tutor/checkers/rational.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  group('the same region, written another way, is right', () {
    for (final (expected, answer) in [
      ('y <= 2x + 1', 'y <= 2x + 1'),
      ('y <= 2x + 1', '2x + 1 >= y'),
      ('y <= 2x + 1', '2x - y >= -1'),
      ('y <= 2x + 1', '-4x + 2y <= 2'),
      ('x + y < 4', 'y < 4 - x'),
      ('x + y < 4', '2(x + y) < 8'),
      ('y > (1/2)x - 3', '2y > x - 6'),
      ('y > (1/2)x - 3', 'y > x/2 - 3'),
      ('x >= 2', '2 <= x'),
      ('3x + 2y <= 12', '3x + 2y ≤ 12'),
      ('y >= -x', 'x + y ≥ 0'),
    ]) {
      test('$answer for $expected', () {
        expect(checkHalfPlane(answer, expected), isNull);
      });
    }
  });

  test('the other side of the right line', () {
    expect(
      checkHalfPlane('y >= 2x + 1', 'y <= 2x + 1'),
      HalfPlaneMistake.wrongSide,
    );
    expect(
      checkHalfPlane('y > 2x + 1', 'y <= 2x + 1'),
      HalfPlaneMistake.wrongSide,
    );
    expect(
      checkHalfPlane('x + y > 4', 'x + y < 4'),
      HalfPlaneMistake.wrongSide,
    );
  });

  test('the right side, but the line wrongly included or left out', () {
    expect(
      checkHalfPlane('y < 2x + 1', 'y <= 2x + 1'),
      HalfPlaneMistake.wrongBoundary,
    );
    expect(
      checkHalfPlane('4 - x >= y', 'x + y < 4'),
      HalfPlaneMistake.wrongBoundary,
    );
  });

  test('a different line', () {
    expect(
      checkHalfPlane('y <= 2x + 2', 'y <= 2x + 1'),
      HalfPlaneMistake.wrongLine,
    );
    expect(
      checkHalfPlane('y <= x + 1', 'y <= 2x + 1'),
      HalfPlaneMistake.wrongLine,
    );
    expect(checkHalfPlane('x <= 1', 'y <= 1'), HalfPlaneMistake.wrongLine);
  });

  test('answers that are not one inequality in x and y', () {
    for (final answer in [
      '',
      'y = 2x + 1',
      '3 < 4',
      'xy < 4',
      'y < 2x <= 3',
      'hello',
      'y < x²',
    ]) {
      expect(
        checkHalfPlane(answer, 'y <= 2x + 1'),
        HalfPlaneMistake.unreadable,
        reason: answer,
      );
    }
  });

  test('contains points on the right side, and the line when included', () {
    final h = parseHalfPlane('x + y <= 4');
    expect(h.contains(Rational(1), Rational(1)), isTrue);
    expect(h.contains(Rational(2), Rational(2)), isTrue);
    expect(h.contains(Rational(3), Rational(2)), isFalse);
    expect(
      parseHalfPlane('x + y < 4').contains(Rational(2), Rational(2)),
      isFalse,
    );
  });

  test('Urdu digits and the minus sign are read', () {
    expect(checkHalfPlane('y ≥ ۲x − ۱', 'y >= 2x - 1'), isNull);
  });
}
