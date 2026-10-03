import 'package:ai_tutor/checkers/linear_inequality_checker.dart';
import 'package:ai_tutor/checkers/rational.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  SolutionSet solve(String text) => parseLinearInequality(text).solutions;

  group('solutions', () {
    test('a positive x keeps the direction', () {
      expect(
        solve('2x - 3 < 7'),
        Ray(Rational(5), below: true, inclusive: false),
      );
      expect(
        solve('x + 1 >= 4'),
        Ray(Rational(3), below: false, inclusive: true),
      );
    });

    test('a negative x flips it', () {
      expect(
        solve('-3x <= 12'),
        Ray(Rational(-4), below: false, inclusive: true),
      );
      expect(
        solve('5 - x > 2'),
        Ray(Rational(3), below: true, inclusive: false),
      );
    });

    test('number on the left, brackets and fractions', () {
      expect(solve('4 > x'), Ray(Rational(4), below: true, inclusive: false));
      expect(
        solve('(x + 5)/3 <= 1 - x'),
        Ray(Rational(-1, 2), below: true, inclusive: true),
      );
    });

    test('Urdu digits and ≤ ≥ signs', () {
      expect(solve('x ≤ ۴'), Ray(Rational(4), below: true, inclusive: true));
      expect(solve('2x ≥ 6'), Ray(Rational(3), below: false, inclusive: true));
    });

    test('no x left: every number or none', () {
      expect(solve('x + 1 < x + 2'), const AllNumbers());
      expect(solve('x + 2 <= x + 1'), const NoNumbers());
    });

    test('unreadable', () {
      for (final bad in [
        '2x + 3',
        'x < 3 < 4',
        'x = 3',
        'x < 3 = 4',
        'x² < 4',
      ]) {
        expect(
          () => parseLinearInequality(bad),
          throwsFormatException,
          reason: bad,
        );
      }
    });
  });

  group('working', () {
    test('correct working ends in x op number', () {
      final r = checkInequalityWorking('2x < 10\nx < 5', '2x - 3 < 7');
      expect(r.isCorrect, isTrue);
      expect(r.solutions!.describe('x'), 'x < 5');
    });

    test('flipping when dividing by a negative', () {
      expect(
        checkInequalityWorking('-2x >= -6; x <= 3', '7 - 2x >= 1').isCorrect,
        isTrue,
      );
      final forgot = checkInequalityWorking('-2x >= -6\nx >= 3', '7 - 2x >= 1');
      expect(forgot.mistake, InequalityMistake.wrongDirection);
      expect(forgot.details['line'], 2);
    });

    test('a wrong step names its line', () {
      final r = checkInequalityWorking('2x < 4\nx < 2', '2x - 3 < 7');
      expect(r.mistake, InequalityMistake.brokenStep);
      expect(r.details['line'], 1);
    });

    test('unfinished and unreadable', () {
      expect(
        checkInequalityWorking('2x < 10', '2x - 3 < 7').mistake,
        InequalityMistake.notFinished,
      );
      expect(
        checkInequalityWorking('2x is less than 10', '2x - 3 < 7').mistake,
        InequalityMistake.unreadable,
      );
      expect(
        checkInequalityWorking('', '2x - 3 < 7').mistake,
        InequalityMistake.unreadable,
      );
    });

    test('a single final answer works too (number line results)', () {
      expect(checkInequalityWorking('x <= 4', 'x <= 4').isCorrect, isTrue);
      expect(
        checkInequalityWorking('x < 4', 'x <= 4').mistake,
        InequalityMistake.brokenStep,
      );
      expect(
        checkInequalityWorking('x >= 4', 'x <= 4').mistake,
        InequalityMistake.wrongDirection,
      );
      expect(checkInequalityWorking('4 >= x', 'x <= 4').isCorrect, isTrue);
    });
  });
}
