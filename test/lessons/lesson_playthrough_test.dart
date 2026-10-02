import 'dart:convert';
import 'dart:io';

import 'package:ai_tutor/checkers/linear_equation_checker.dart';
import 'package:ai_tutor/models/lesson.dart';
import 'package:ai_tutor/models/lesson_step.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import '../helpers.dart';

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

/// Opens [lesson] from the previewer and plays every step: tries a wrong
/// answer first (to check feedback appears), then the right one.
Future<void> playLesson(
  WidgetTester tester,
  Lesson lesson, {
  required bool urdu,
}) async {
  await tapKey(tester, 'open-previewer');
  await tapKey(tester, 'lesson-${lesson.id}');

  for (final step in lesson.steps) {
    switch (step) {
      case ChoiceStep():
        final wrong = step.options.where((o) => !o.correct).firstOrNull;
        if (wrong != null) {
          await tapKey(tester, 'option-${wrong.id}');
          expect(find.byKey(const Key('feedback-try')), findsOneWidget);
        }
        final right = step.options.firstWhere((o) => o.correct);
        await tapKey(tester, 'option-${right.id}');
        expect(find.byKey(const Key('feedback-good')), findsOneWidget);
      case NumberStep():
        final input = find.byKey(const Key('answer-input'));
        if (step.commonWrong.isNotEmpty) {
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
        await tester.enterText(input, wrong);
        await tapKey(tester, 'step-check');
        expect(find.byKey(const Key('feedback-try')), findsOneWidget);

        await tester.enterText(input, rightAnswer(step));
        await tapKey(tester, 'step-check');
        expect(find.byKey(const Key('feedback-good')), findsOneWidget);
      case ExplainStep() || SummaryStep() || UnsupportedStep():
        break;
    }
    await tapKey(tester, 'step-continue');
  }
}

void main() {
  final lessons = Directory('content/lessons')
      .listSync()
      .whereType<File>()
      .where((f) => f.path.endsWith('.json'))
      .map(
        (f) => Lesson.fromJson(
          jsonDecode(f.readAsStringSync()) as Map<String, dynamic>,
        ),
      )
      .toList();

  setUp(() {
    final view =
        TestWidgetsFlutterBinding.instance.platformDispatcher.views.first;
    // A typical small phone screen.
    view.physicalSize = const Size(1080, 2340);
    view.devicePixelRatio = 3;
  });

  tearDown(() {
    TestWidgetsFlutterBinding.instance.platformDispatcher.views.first
      ..resetPhysicalSize()
      ..resetDevicePixelRatio();
  });

  for (final lesson in lessons) {
    for (final language in ['en', 'ur']) {
      testWidgets('${lesson.id} plays end to end in $language', (tester) async {
        await tester.pumpWidget(
          await buildTestApp(prefs: {'locale': language}),
        );
        await tester.pumpAndSettle();

        await playLesson(tester, lesson, urdu: language == 'ur');

        // Finishing the lesson returns to the previewer.
        expect(find.byKey(Key('lesson-${lesson.id}')), findsOneWidget);
        expect(tester.takeException(), isNull);
      });
    }
  }

  testWidgets('number step shows the working after the last attempt', (
    tester,
  ) async {
    final lesson = lessons.firstWhere(
      (l) => l.id == 'g6-maths-02-dividing-fractions',
    );
    await tester.pumpWidget(await buildTestApp());
    await tester.pumpAndSettle();
    await tapKey(tester, 'open-previewer');
    await tapKey(tester, 'lesson-${lesson.id}');

    // Move to the first number step, answering correctly.
    for (final step in lesson.steps.takeWhile((s) => s is! NumberStep)) {
      if (step is ChoiceStep) {
        await tapKey(
          tester,
          'option-${step.options.firstWhere((o) => o.correct).id}',
        );
      }
      await tapKey(tester, 'step-continue');
    }

    final step = lesson.steps.whereType<NumberStep>().first;
    final input = find.byKey(const Key('answer-input'));

    await tester.enterText(input, 'abc');
    await tapKey(tester, 'step-check');
    expect(find.text('Please type a number, like 8 or ۸.'), findsOneWidget);

    for (var i = 0; i < step.maxAttempts; i++) {
      await tester.enterText(input, '999');
      await tapKey(tester, 'step-check');
    }
    expect(find.text(step.feedbackWrong.en), findsOneWidget);
    expect(find.byKey(const Key('step-continue')), findsOneWidget);
  });
}
