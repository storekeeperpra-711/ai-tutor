import 'package:ai_tutor/app/bidi.dart';
import 'package:flutter_test/flutter_test.dart';

const lri = '\u2066';
const pdi = '\u2069';
const nb = '\u00a0';
const wj = '\u2060';
const minus = '\u2212';

void main() {
  test('wraps maths in left-to-right isolate marks', () {
    expect(
      isolateMath('یعنی 3 × 2 = 6 آدھے'),
      'یعنی ${lri}3$nb×${nb}2$nb=${nb}6$pdi آدھے',
    );
  });

  test('wraps fractions', () {
    expect(
      isolateMath('چوتھائی (1/4) روٹی'),
      'چوتھائی $lri(1/${wj}4)$pdi روٹی',
    );
  });

  test('leaves plain numbers and English words alone', () {
    expect(isolateMath('3 روٹیاں'), '3 روٹیاں');
    expect(isolateMath('معکوس (Reciprocal)'), 'معکوس (Reciprocal)');
    expect(
      isolateMath('Add 3 to the x-axis', rtl: false),
      'Add 3 to the x-axis',
    );
  });

  test('does not include the Urdu full stop', () {
    expect(
      isolateMath('3 ÷ 1/2 = 6۔'),
      '${lri}3$nb÷${nb}1/${wj}2$nb=${nb}6$pdi۔',
    );
  });

  test('a negative number keeps its minus on the left', () {
    expect(isolateMath('جواب -8 ہے'), 'جواب $lri${minus}8$pdi ہے');
    expect(isolateMath('جواب \u22128 ہے'), 'جواب $lri${minus}8$pdi ہے');
    expect(
      isolateMath('5 - (-8) = 13'),
      '${lri}5$nb$minus$nb(${minus}8)$nb=${nb}13$pdi',
    );
  });

  test('an equation never breaks, in English too', () {
    expect(
      isolateMath('Solve 2x + 3 = 7 now', rtl: false),
      'Solve 2x$nb+${nb}3$nb=${nb}7 now',
    );
  });
}
