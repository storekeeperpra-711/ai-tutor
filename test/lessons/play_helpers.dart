import 'package:ai_tutor/checkers/linear_equation_checker.dart';
import 'package:ai_tutor/models/lesson_step.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

/// Writes [n] with Urdu digits (۰–۹), the way a student might type it.
String toUrduDigits(num n) => n
    .toString()
    .split('')
    .map((c) => '0123456789'.contains(c) ? '۰۱۲۳۴۵۶۷۸۹'[int.parse(c)] : c)
    .join();

String formatNumber(double n) =>
    n == n.roundToDouble() ? n.toInt().toString() : n.toString();

/// A correct answer for a text_check step.
String rightAnswer(TextCheckStep step) {
  if (step.checker != 'linear_equation') return step.expected;
  final solution =
      parseLinearEquation(step.expected, variable: step.variable).solution
          as OneSolution;
  return '${step.variable} = ${solution.value}';
}

Future<void> tapKey(WidgetTester tester, String key) async {
  final finder = find.byKey(Key(key));
  // Lesson files load from the asset bundle with real (not fake) async,
  // so give the loading a moment of real time if needed.
  for (var i = 0; i < 100 && finder.evaluate().isEmpty; i++) {
    await tester.runAsync(
      () => Future<void>.delayed(const Duration(milliseconds: 10)),
    );
    await tester.pump();
  }
  await tester.ensureVisible(finder);
  await tester.pumpAndSettle();
  await tester.tap(finder);
  await tester.pumpAndSettle();
}

/// Answers [step]: with [tryWrongFirst], a wrong answer first (to check
/// feedback appears), then the right one. Doesn't press Continue.
Future<void> answerStep(
  WidgetTester tester,
  LessonStep step, {
  bool urdu = false,
  bool tryWrongFirst = true,
}) async {
  switch (step) {
    case ChoiceStep():
      final wrong = step.options.where((o) => !o.correct).firstOrNull;
      if (wrong != null && tryWrongFirst) {
        await tapKey(tester, 'option-${wrong.id}');
        expect(find.byKey(const Key('feedback-try')), findsOneWidget);
      }
      final right = step.options.firstWhere((o) => o.correct);
      await tapKey(tester, 'option-${right.id}');
      expect(find.byKey(const Key('feedback-good')), findsOneWidget);
    case NumberStep():
      final input = find.byKey(const Key('answer-input'));
      if (step.commonWrong.isNotEmpty && tryWrongFirst) {
        await tester.enterText(
          input,
          formatNumber(step.commonWrong.first.answer),
        );
        await tapKey(tester, 'step-check');
        expect(find.byKey(const Key('feedback-try')), findsOneWidget);
      }
      final answer = formatNumber(step.answer);
      await tester.enterText(
        input,
        urdu ? toUrduDigits(num.parse(answer)) : answer,
      );
      await tapKey(tester, 'step-check');
      expect(find.byKey(const Key('feedback-good')), findsOneWidget);
    case TextCheckStep():
      final input = find.byKey(const Key('answer-input'));
      final wrong = step.commonWrong.isNotEmpty
          ? step.commonWrong.first.answer
          : switch (step.checker) {
              'chem_equation' => 'Xx2 -> Xx',
              'linear_equation' => '${step.variable} = 999',
              'fraction' => '999/1000',
              _ => 'zzz',
            };
      if (tryWrongFirst) {
        await tester.enterText(input, wrong);
        await tapKey(tester, 'step-check');
        expect(find.byKey(const Key('feedback-try')), findsOneWidget);
      }

      await tester.enterText(input, rightAnswer(step));
      await tapKey(tester, 'step-check');
      expect(find.byKey(const Key('feedback-good')), findsOneWidget);
    case ExplainStep() || SummaryStep() || UnsupportedStep():
      break;
  }
}
