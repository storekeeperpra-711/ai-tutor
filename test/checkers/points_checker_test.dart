import 'package:ai_tutor/checkers/points_checker.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  const corners = '(0, 0), (4, 0), (4, 2), (0, 6)';

  test('the same points in any order are right', () {
    for (final answer in [
      corners,
      '(4,2) (0,6) (0,0) (4,0)',
      '(0, 6); (4, 2); (4, 0); (0, 0)',
      '(0,0), (4,0), (4,2) and (0,6)',
      '(۰، ۰)، (۴، ۰)، (۴، ۲)، (۰، ۶)',
      '(0, 0), (0, 0), (4, 0), (4, 2), (0, 6)',
    ]) {
      expect(checkPoints(answer, corners).isCorrect, isTrue, reason: answer);
    }
  });

  test('fractions and decimals', () {
    expect(checkPoints('(1.5, -2)', '(3/2, -2)').isCorrect, isTrue);
  });

  test('names a point that is not a corner', () {
    final result = checkPoints('(0, 0), (6, 0)', corners);
    expect(result.mistake, PointsMistake.wrongPoint);
    expect(result.details['point'], '(6, 0)');
  });

  test('says how many corners are missing', () {
    final result = checkPoints('(0, 0), (4, 0)', corners);
    expect(result.mistake, PointsMistake.missing);
    expect(result.details['count'], 2);
  });

  test('anything else is unreadable', () {
    for (final answer in ['', '4, 2', '(4, 2', '(a, 2)', '(1, 2) x']) {
      expect(
        checkPoints(answer, corners).mistake,
        PointsMistake.unreadable,
        reason: answer,
      );
    }
  });
}
