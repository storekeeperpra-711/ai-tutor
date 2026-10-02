import 'package:ai_tutor/checkers/fraction_checker.dart';
import 'package:ai_tutor/checkers/numeric_checker.dart';
import 'package:ai_tutor/checkers/rational.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  final threeQuarters = Rational(3, 4);

  group('parseRational', () {
    test('reads fractions, mixed numbers and decimals exactly', () {
      expect(parseRational('3/4'), threeQuarters);
      expect(parseRational('1 1/2'), Rational(3, 2));
      expect(parseRational('-2 3/4'), Rational(-11, 4));
      expect(parseRational('0.75'), threeQuarters);
      expect(parseRational('1/3'), Rational(1, 3));
    });

    test('reads Urdu digits and number words', () {
      expect(parseRational('۳/۴'), threeQuarters);
      expect(parseRational('۱ ۱/۲'), Rational(3, 2));
      expect(parseRational('aath'), Rational(8));
      expect(parseRational('Teen'), Rational(3));
      expect(parseRational('آٹھ'), Rational(8));
      expect(parseRational('twelve'), Rational(12));
    });

    test('rejects nonsense', () {
      expect(parseRational('3/'), isNull);
      expect(parseRational('1/0'), isNull);
      expect(parseRational('three quarters'), isNull);
      expect(parseRational('1 2 3'), isNull);
    });
  });

  group('checkFraction', () {
    test('any equal value is correct by default', () {
      for (final answer in ['3/4', '6/8', '0.75', '۶/۸']) {
        expect(checkFraction(answer, threeQuarters).isCorrect, isTrue);
      }
    });

    test('improper and mixed forms are both accepted', () {
      expect(checkFraction('3/2', Rational(3, 2)).isCorrect, isTrue);
      expect(checkFraction('1 1/2', Rational(3, 2)).isCorrect, isTrue);
    });

    test('flags answers not in lowest terms when asked', () {
      final result = checkFraction('6/8', threeQuarters, requireSimplest: true);
      expect(result.verdict, FractionVerdict.notSimplest);
      expect(result.simplest, threeQuarters);
      expect(
        checkFraction('1 2/4', Rational(3, 2), requireSimplest: true).verdict,
        FractionVerdict.notSimplest,
      );
      expect(
        checkFraction('3/4', threeQuarters, requireSimplest: true).isCorrect,
        isTrue,
      );
      expect(
        checkFraction('0.75', threeQuarters, requireSimplest: true).isCorrect,
        isTrue,
      );
    });

    test('wrong and unreadable answers', () {
      expect(
        checkFraction('4/3', threeQuarters).verdict,
        FractionVerdict.wrong,
      );
      expect(checkFraction('4/3', threeQuarters).value, Rational(4, 3));
      expect(
        checkFraction('abc', threeQuarters).verdict,
        FractionVerdict.unreadable,
      );
    });
  });

  test('Rational keeps exact values', () {
    expect(Rational(1, 3) + Rational(1, 3), Rational(2, 3));
    expect(Rational(2, -4), Rational(-1, 2));
    expect(Rational(6, 8).toString(), '3/4');
    expect(Rational.tryParseDecimal('-.5'), Rational(-1, 2));
  });
}
