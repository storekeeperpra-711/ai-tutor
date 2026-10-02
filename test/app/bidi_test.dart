import 'package:ai_tutor/app/bidi.dart';
import 'package:flutter_test/flutter_test.dart';

const lri = '\u2066';
const pdi = '\u2069';

void main() {
  test('wraps maths in left-to-right isolate marks', () {
    expect(isolateMath('یعنی 3 × 2 = 6 آدھے'), 'یعنی ${lri}3 × 2 = 6$pdi آدھے');
  });

  test('wraps fractions', () {
    expect(isolateMath('چوتھائی (1/4) روٹی'), 'چوتھائی $lri(1/4)$pdi روٹی');
  });

  test('leaves plain numbers and English words alone', () {
    expect(isolateMath('3 روٹیاں'), '3 روٹیاں');
    expect(isolateMath('معکوس (Reciprocal)'), 'معکوس (Reciprocal)');
  });

  test('does not include the Urdu full stop', () {
    expect(isolateMath('3 ÷ 1/2 = 6۔'), '${lri}3 ÷ 1/2 = 6$pdi۔');
  });
}
