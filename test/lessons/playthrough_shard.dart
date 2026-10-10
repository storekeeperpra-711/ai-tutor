import 'dart:convert';
import 'dart:io';

import 'package:ai_tutor/app/bidi.dart';
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
  await openPreviewLesson(tester, lesson.id);

  for (final step in lesson.steps) {
    await answerStep(tester, step, urdu: urdu);
    await tapKey(tester, 'step-continue');
  }
}

/// Plays the lessons of one shard. The lessons are split over several test
/// files so each runs in its own process: one file playing every lesson ran
/// out of memory on the CI machine as lessons were added.
void runPlaythroughShard(int shard, int shards) {
  final lessons =
      Directory('content/lessons')
          .listSync()
          .whereType<File>()
          .where((f) => f.path.endsWith('.json'))
          .map(
            (f) => Lesson.fromJson(
              jsonDecode(f.readAsStringSync()) as Map<String, dynamic>,
            ),
          )
          .toList()
        ..sort((a, b) => a.id.compareTo(b.id));

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

  for (var i = shard; i < lessons.length; i += shards) {
    final lesson = lessons[i];
    for (final language in ['en', 'ur']) {
      testWidgets('${lesson.id} plays end to end in $language', (tester) async {
        await tester.pumpWidget(
          await buildTestApp(prefs: {'locale': language}),
        );
        await tester.pumpAndSettle();

        await playLesson(tester, lesson, urdu: language == 'ur');

        // Mithu celebrates with three effort stars (wrong answers were
        // tried again), then Home returns to the previewer.
        expect(find.byKey(const Key('lesson-celebration')), findsOneWidget);
        expect(find.byKey(const Key('star-2-on')), findsOneWidget);
        await tapKey(tester, 'celebration-done');
        expect(find.byKey(Key('lesson-${lesson.id}')), findsOneWidget);
        expect(tester.takeException(), isNull);
      });
    }
  }

  if (shard != 0) return;

  testWidgets('number step shows the working after the last attempt', (
    tester,
  ) async {
    final lesson = lessons.firstWhere(
      (l) => l.id == 'g6-maths-02-dividing-fractions',
    );
    await tester.pumpWidget(await buildTestApp());
    await tester.pumpAndSettle();
    await openPreviewLesson(tester, lesson.id);

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
    expect(
      find.text(isolateMath(step.feedbackWrong.en, rtl: false)),
      findsOneWidget,
    );
    expect(find.byKey(const Key('step-continue')), findsOneWidget);
  });
}
