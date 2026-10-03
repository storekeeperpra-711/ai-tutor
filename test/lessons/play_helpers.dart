import 'package:ai_tutor/checkers/linear_equation_checker.dart';
import 'package:ai_tutor/lessons/steps/sim_step_view.dart';
import 'package:ai_tutor/models/lesson_step.dart';
import 'package:ai_tutor/sims/sim_host.dart';
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

/// An explanation with one word from every keyword group.
String goodExplanation(AiExplainStep step) =>
    'I think ${step.keywords.map((g) => g.first).join(' and ')} is the idea';

/// Typed working or answer that the photo step's checker accepts.
String rightPhotoAnswer(PhotoCheckStep step) {
  if (step.checker != 'linear_equation') return step.expected;
  final solution =
      parseLinearEquation(step.expected, variable: step.variable).solution
          as OneSolution;
  return '${step.expected}\n${step.variable} = ${solution.value}';
}

String wrongPhotoAnswer(PhotoCheckStep step) => switch (step.checker) {
  'linear_equation' => '${step.expected}\n${step.variable} = 999',
  'chem_equation' => 'H2 + O2 -> H2O',
  'fraction' => '999/1000',
  _ => '999',
};

/// The right result for a sim step, as the simulation would report it.
Object rightSimAnswer(SimStep step) {
  final e = step.expected!;
  return e.checker == 'numeric' ? num.parse(e.answer) : e.answer;
}

/// A wrong result: a known common mistake if the step has one.
Object wrongSimAnswer(SimStep step) {
  final e = step.expected!;
  if (step.commonWrong.isNotEmpty) {
    final w = step.commonWrong.first.answer;
    return e.checker == 'numeric' ? num.parse(w) : w;
  }
  return switch (e.checker) {
    'numeric' => num.parse(e.answer) + 1,
    'chem_equation' => 'N2 + H2 -> NH3',
    'fraction' => '999/1000',
    _ => 'zzz',
  };
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
    case SimStep(:final expected?):
      // Widget tests have no WebView, so report results straight to the
      // step, as the simulation would.
      final sim = tester.state<SimStepViewState>(find.byType(SimStepView));
      if (tryWrongFirst) {
        sim.onSimEvent(
          SimEvent('result', {expected.result: wrongSimAnswer(step)}),
        );
        await tester.pumpAndSettle();
        expect(find.byKey(const Key('feedback-try')), findsOneWidget);
      }
      sim.onSimEvent(
        SimEvent('result', {expected.result: rightSimAnswer(step)}),
      );
      await tester.pumpAndSettle();
      expect(find.byKey(const Key('feedback-good')), findsOneWidget);
    case AiExplainStep():
      // One word from each idea group: a full answer for the keywords.
      final input = find.byKey(const Key('answer-input'));
      if (tryWrongFirst) {
        await tester.enterText(input, 'I do not know');
        await tapKey(tester, 'step-check');
        expect(find.byKey(const Key('feedback-try')), findsOneWidget);
        await tapKey(tester, 'ai-improve');
      }
      await tester.enterText(input, goodExplanation(step));
      await tapKey(tester, 'step-check');
      expect(find.byKey(const Key('feedback-good')), findsOneWidget);
    case PhotoCheckStep():
      // Widget tests have no camera: type the working instead.
      final input = find.byKey(const Key('answer-input'));
      if (tryWrongFirst) {
        await tapKey(tester, 'photo-type');
        await tester.enterText(input, wrongPhotoAnswer(step));
        await tapKey(tester, 'step-check');
        expect(find.byKey(const Key('feedback-try')), findsOneWidget);
        await tapKey(tester, 'photo-try-again');
      }
      await tapKey(tester, 'photo-type');
      await tester.enterText(input, rightPhotoAnswer(step));
      await tapKey(tester, 'step-check');
      expect(find.byKey(const Key('feedback-good')), findsOneWidget);
    case TapCountStep():
      // Tap mangoes into the basket and the tick: pictures only.
      final extra = tryWrongFirst && step.count < step.shown ? 1 : 0;
      for (var i = 0; i < step.count + extra; i++) {
        await tapKey(tester, 'mango-$i');
      }
      if (extra > 0) {
        await tapKey(tester, 'step-check');
        expect(find.byKey(const Key('step-continue')), findsNothing);
        await tapKey(tester, 'basket-mango-${step.count}');
      }
      await tapKey(tester, 'step-check');
      expect(find.byKey(const Key('step-continue')), findsOneWidget);
    case PickPictureStep():
      final wrong = step.options.where((o) => !step.isRight(o)).firstOrNull;
      if (wrong != null && tryWrongFirst) {
        await tapKey(tester, 'picture-${wrong.id}');
        expect(find.byKey(const Key('step-continue')), findsNothing);
      }
      await tapKey(
        tester,
        'picture-${step.options.firstWhere(step.isRight).id}',
      );
      expect(find.byKey(const Key('step-continue')), findsOneWidget);
    case SimStep() || VideoStep() || LottieStep():
      break;
    case ExplainStep() || SummaryStep() || UnsupportedStep():
      break;
  }
}
