import 'package:ai_tutor/lessons/step_result.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import '../lessons/play_helpers.dart';
import '../mastery/lessons.dart';
import 'tier_homes_test.dart' show openHomeFor;

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

  testWidgets(
    'Lessons shows how much is done and each lesson by book chapter',
    (tester) async {
      final lessons = loadLessons();
      final grade6 = lessons.where((l) => l.grade == 6).length;
      final factors = lessons.firstWhere(
        (l) => l.id == 'g6-maths-05-factors-and-multiples',
      );
      final primes = lessons.firstWhere(
        (l) => l.id == 'g6-maths-05-prime-numbers',
      );
      final backend = await openHomeFor(tester, grade: 6);
      Future<void> record(String id, int step, int count) => tester.runAsync(
        () => backend.db.recordStep(
          studentId: 'kid',
          lessonId: id,
          lessonVersion: 1,
          stepIndex: step,
          stepCount: count,
          result: StepResult(stepId: 's$step', correct: true, attempts: 1),
        ),
      );
      await record(factors.id, factors.steps.length - 1, factors.steps.length);
      await record(primes.id, 1, primes.steps.length);

      await tapKey(tester, 'nav-lessons');
      expect(find.byKey(const Key('course-card')), findsOneWidget);
      expect(find.text('1 of $grade6 lessons done'), findsOneWidget);
      expect(find.text('${100 ~/ grade6}% done'), findsOneWidget);
      expect(find.textContaining('Done means you finished'), findsOneWidget);

      // Units are grouped like the book's contents.
      expect(find.text('1. Numbers and Operations'), findsOneWidget);
      expect(find.text('Factors and Multiples'), findsOneWidget);

      // The first unfinished unit (Factors, first in the book) is open.
      expect(find.text('1 / 14'), findsOneWidget);
      expect(
        tester
            .widget<Text>(find.byKey(Key('course-lesson-status-${factors.id}')))
            .data,
        'Done',
      );
      expect(
        tester
            .widget<Text>(find.byKey(Key('course-lesson-status-${primes.id}')))
            .data,
        'Step 3 of ${primes.steps.length}',
      );

      // Other classes' lessons come after, under their own heading.
      await tester.scrollUntilVisible(
        find.text('Other lessons'),
        300,
        maxScrolls: 100,
      );
      expect(find.text('Other lessons'), findsOneWidget);

      // Tapping a lesson opens it.
      await tester.scrollUntilVisible(
        find.byKey(Key('course-lesson-${primes.id}')),
        -300,
        maxScrolls: 100,
      );
      await tapKey(tester, 'course-lesson-${primes.id}');
      expect(find.byKey(const Key('course-card')), findsNothing);
    },
  );
}
