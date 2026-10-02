import 'package:ai_tutor/checkers/linear_equation_checker.dart';
import 'package:ai_tutor/checkers/rational.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  const equation = '2x + 3 = 11';

  group('parseLinearEquation', () {
    test('solves different forms', () {
      expect(
        parseLinearEquation('2x + 3 = 11').solution,
        OneSolution(Rational(4)),
      );
      expect(
        parseLinearEquation('3(x - 1) = x/2 + 4').solution,
        OneSolution(Rational(14, 5)),
      );
      expect(
        parseLinearEquation('۲x − ۴ = 0').solution,
        OneSolution(Rational(2)),
      );
      expect(
        parseLinearEquation('-x = 2.5').solution,
        OneSolution(Rational(-5, 2)),
      );
      expect(parseLinearEquation('x + 1 = x + 1').solution, const AnyValue());
      expect(parseLinearEquation('x + 1 = x').solution, const NoValue());
    });

    test('rejects non-linear or broken input', () {
      for (final bad in [
        'x*x = 4',
        '2x + = 3',
        'x = ',
        '2x + 3',
        '1/x = 2',
        'y = 2',
      ]) {
        expect(
          () => parseLinearEquation(bad),
          throwsFormatException,
          reason: bad,
        );
      }
    });
  });

  group('checkLinearWorking', () {
    test('accepts correct working, line by line', () {
      final result = checkLinearWorking('2x + 3 = 11\n2x = 8\nx = 4', equation);
      expect(result.isCorrect, isTrue);
      expect(result.value, Rational(4));
    });

    test('accepts just the answer, and number = x', () {
      expect(checkLinearWorking('x = 4', equation).isCorrect, isTrue);
      expect(checkLinearWorking('2x = 8; 4 = x', equation).isCorrect, isTrue);
    });

    test('names the first broken line', () {
      // Moved +3 without changing its sign.
      final result = checkLinearWorking('2x = 11 + 3\nx = 7', equation);
      expect(result.mistake, LinearMistake.brokenStep);
      expect(result.details['line'], 1);

      final later = checkLinearWorking('2x = 8\nx = 8 - 2\nx = 6', equation);
      expect(later.details['line'], 2);
    });

    test('wrong final answer is a broken step', () {
      expect(
        checkLinearWorking('x = 5', equation).mistake,
        LinearMistake.brokenStep,
      );
    });

    test('correct but unfinished working', () {
      expect(
        checkLinearWorking('2x = 8', equation).mistake,
        LinearMistake.notFinished,
      );
    });

    test('unreadable lines are named', () {
      final result = checkLinearWorking('2x = 8\nx equals 4', equation);
      expect(result.mistake, LinearMistake.unreadable);
      expect(result.details['line'], 2);
      expect(
        checkLinearWorking('  ', equation).mistake,
        LinearMistake.unreadable,
      );
    });
  });
}
