import 'dart:convert';
import 'dart:io';

import 'package:ai_tutor/models/lesson.dart';
import 'package:ai_tutor/models/lesson_step.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import '../helpers.dart';
import 'play_helpers.dart';

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
    await answerStep(tester, step, urdu: urdu);
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
      await answerStep(tester, step, tryWrongFirst: false);
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
