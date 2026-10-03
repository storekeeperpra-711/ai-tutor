import 'package:ai_tutor/character/sounds.dart';
import 'package:ai_tutor/features/effort/effort.dart';
import 'package:ai_tutor/models/lesson_step.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import '../fakes.dart';
import '../helpers.dart';
import '../lessons/play_helpers.dart';
import '../mastery/lessons.dart';

final counting = loadLessons().firstWhere(
  (l) => l.id == 'g0-maths-01-count-the-mangoes',
);

Future<FakeBackend> openHomeFor(
  WidgetTester tester, {
  required int grade,
  Map<String, Object> prefs = const {},
}) async {
  final backend = FakeBackend();
  await backend.db.addStudent(student('kid', name: 'Zara', grade: grade));
  await tester.pumpWidget(await buildTestApp(backend: backend, prefs: prefs));
  await tester.pumpAndSettle();
  await tapKey(tester, 'student-kid');
  return backend;
}

void main() {
  setUp(() {
    final view =
        TestWidgetsFlutterBinding.instance.platformDispatcher.views.first;
    view.physicalSize = const Size(1080, 2340);
    view.devicePixelRatio = 3;
  });

  tearDown(() {
    TestWidgetsFlutterBinding.instance.platformDispatcher.views.first
      ..resetPhysicalSize()
      ..resetDevicePixelRatio();
  });

  testWidgets('Nursery: village path, Mithu greets by name, big Play', (
    tester,
  ) async {
    final backend = await openHomeFor(tester, grade: -1);
    expect(find.byKey(const Key('early-home')), findsOneWidget);
    expect(find.byKey(const Key('play-next')), findsOneWidget);
    expect(
      find.byKey(Key('village-stop-${counting.id}')),
      findsOneWidget,
      reason: 'only the Nursery lesson is on the path',
    );
    expect(
      find.byKey(const Key('village-stop-g6-maths-02-dividing-fractions')),
      findsNothing,
    );
    // Mithu says hello by name, aloud, without being asked.
    expect(backend.narrator.said.single.text, contains('Zara'));
  });

  testWidgets('Grades 3-5: quest, subject tiles, badges and a tip', (
    tester,
  ) async {
    await openHomeFor(tester, grade: 4);
    expect(find.byKey(const Key('primary-home')), findsOneWidget);
    expect(find.byKey(const Key('mithu-tip')), findsOneWidget);
    expect(find.byKey(const Key('quest-card')), findsOneWidget);
    expect(find.byKey(const Key('subject-maths')), findsOneWidget);
    expect(find.text('0 of 4 skills secure'), findsNothing);
    await tester.ensureVisible(find.byKey(const Key('badge-shelf')));
    expect(find.text('0 of 6 badges'), findsOneWidget);
  });

  testWidgets('Grades 6-8: levels per subject and the badge collection', (
    tester,
  ) async {
    await openHomeFor(tester, grade: 7);
    expect(find.byKey(const Key('middle-home')), findsOneWidget);
    expect(find.text('Level 1'), findsWidgets);
    expect(find.byKey(const Key('badge-shelf')), findsOneWidget);
    expect(find.byKey(const Key('quest-card')), findsNothing);
  });

  testWidgets('Grades 9-12: exam countdown, mastery by subject, no Mithu', (
    tester,
  ) async {
    final exam = DateTime.now().add(const Duration(days: 30));
    await openHomeFor(
      tester,
      grade: 10,
      prefs: {'examDate.kid': exam.toIso8601String().substring(0, 10)},
    );
    expect(find.byKey(const Key('older-home')), findsOneWidget);
    expect(find.text('30 days to your board exam'), findsOneWidget);
    expect(find.byKey(const Key('subject-mastery-chemistry')), findsOneWidget);
    // Not childish: Mithu is off unless the student switches him on.
    expect(find.byKey(const Key('mithu-tip')), findsNothing);
    expect(find.byKey(const Key('badge-shelf')), findsNothing);
  });

  testWidgets('Grades 9-12 without a date are asked to set one', (
    tester,
  ) async {
    await openHomeFor(tester, grade: 9);
    expect(
      find.text('Set your board exam date to see a countdown'),
      findsOneWidget,
    );
  });

  testWidgets(
    'a child who cannot read finishes Count the mangoes with taps alone',
    (tester) async {
      final backend = await openHomeFor(tester, grade: -1);
      await tapKey(tester, 'play-next');

      for (final step in counting.steps) {
        // Nothing to type, and Mithu says every instruction by himself.
        expect(find.byType(TextField), findsNothing);
        expect(
          backend.narrator.said.map((v) => v.stepId),
          contains(step.id),
          reason: step.id,
        );
        // One mistake along the way, fixed by trying again.
        await answerStep(tester, step, tryWrongFirst: step.id == 's3_two');
        await tapKey(tester, 'step-continue');
      }

      // Mithu counted the mangoes aloud as they went into the basket.
      expect(
        backend.narrator.said.map((v) => v.text),
        containsAll(['one', 'two', 'three', 'four', 'five']),
      );
      expect(backend.sounds.played, contains(Sound.basket));

      // Three stars for effort, then back on the village path.
      expect(find.byKey(const Key('lesson-celebration')), findsOneWidget);
      expect(find.byKey(const Key('star-2-on')), findsOneWidget);
      await tapKey(tester, 'celebration-done');
      expect(find.byKey(const Key('early-home')), findsOneWidget);
      expect(
        find.descendant(
          of: find.byKey(Key('village-stop-${counting.id}')),
          matching: find.byIcon(Icons.check_rounded),
        ),
        findsOneWidget,
      );
      final steps = await backend.db.stepResultsOf('kid');
      expect(steps.where((r) => r.attempts > 1), isNotEmpty);
      expect(
        counting.steps.whereType<QuestionStep>().map((q) => q.id),
        everyElement(isIn(steps.map((r) => r.stepId))),
      );
    },
  );

  testWidgets('badges appear on the shelf as they are earned', (tester) async {
    final backend = await openHomeFor(tester, grade: 7);
    await tester.ensureVisible(find.byKey(const Key('badge-shelf')));
    expect(find.byKey(const Key('badge-firstLesson-not-yet')), findsOneWidget);

    await answer(backend.db, 'kid', 0, lessonId: counting.id, stepCount: 1);
    await tester.pumpAndSettle();
    expect(find.byKey(const Key('badge-firstLesson-earned')), findsOneWidget);
    expect(EffortBadge.values, hasLength(6));
  });
}
