import 'package:ai_tutor/checkers/numeric_checker.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  group('parseNumber', () {
    test('reads plain, decimal and negative numbers', () {
      expect(parseNumber('8'), 8);
      expect(parseNumber(' 2.5 '), 2.5);
      expect(parseNumber('-3'), -3);
    });

    test('reads Urdu and Arabic digits', () {
      expect(parseNumber('۸'), 8);
      expect(parseNumber('۱۲'), 12);
      expect(parseNumber('٢٫٥'), 2.5);
      expect(parseNumber('−۴'), -4);
    });

    test('reads simple fractions', () {
      expect(parseNumber('3/4'), 0.75);
      expect(parseNumber('۱/۲'), 0.5);
      expect(parseNumber('1 / 2'), 0.5);
    });

    test('rejects things that are not numbers', () {
      expect(parseNumber(''), isNull);
      expect(parseNumber('eight'), isNull);
      expect(parseNumber('آٹھ'), isNull);
      expect(parseNumber('3/0'), isNull);
      expect(parseNumber('/4'), isNull);
    });
  });

  group('numbersMatch', () {
    test('exact by default', () {
      expect(numbersMatch(8, 8), isTrue);
      expect(numbersMatch(8.1, 8), isFalse);
    });

    test('uses tolerance', () {
      expect(numbersMatch(3.14, 3.1416, tolerance: 0.01), isTrue);
      expect(numbersMatch(3.2, 3.1416, tolerance: 0.01), isFalse);
    });

    test('ignores floating point noise', () {
      expect(numbersMatch(0.1 + 0.2, 0.3), isTrue);
    });
  });
}
