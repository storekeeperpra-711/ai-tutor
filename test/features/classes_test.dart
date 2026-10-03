import 'package:ai_tutor/classes/class_store.dart';
import 'package:ai_tutor/lessons/step_result.dart';
import 'package:ai_tutor/services/local_db.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import '../fakes.dart';
import '../helpers.dart';
import '../lessons/play_helpers.dart';

const lessonId = 'g6-maths-02-dividing-fractions';
const teacherEmail = 'teacher@school.pk';

/// Waits (in real time, for asset loading) until [finder] finds something.
Future<void> waitFor(WidgetTester tester, Finder finder) async {
  for (var i = 0; i < 200 && finder.evaluate().isEmpty; i++) {
    await tester.runAsync(
      () => Future<void>.delayed(const Duration(milliseconds: 10)),
    );
    await tester.pump();
  }
  await tester.pumpAndSettle();
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

  testWidgets('a parent joins a child to a class after agreeing, and leaves', (
    tester,
  ) async {
    final backend = FakeBackend();
    backend.classes.addClass();
    await backend.db.addStudent(student('ayesha', grade: 6));
    await tester.pumpWidget(await buildTestApp(backend: backend));
    await tester.pumpAndSettle();

    await tapKey(tester, 'open-account');
    await tapKey(tester, 'classes-ayesha');
    expect(find.text('Not in a class yet.'), findsOneWidget);

    await tester.enterText(find.byKey(const Key('class-code')), 'abc 999');
    await tapKey(tester, 'find-class');
    expect(find.textContaining('No class has this code'), findsOneWidget);

    await tester.enterText(find.byKey(const Key('class-code')), 'abc 234');
    await tapKey(tester, 'find-class');
    expect(find.text('Class: 9 A'), findsOneWidget);

    // Nothing is shared until a parent agrees.
    await tapKey(tester, 'join-class');
    expect(backend.classes.membersOf, isEmpty);
    await tapKey(tester, 'class-consent');
    await waitFor(tester, find.byKey(const Key('join-class')));
    await tapKey(tester, 'join-class');
    await waitFor(tester, find.byKey(const Key('class-class1')));

    final uid = backend.auth.currentUser!.uid;
    final member = backend.classes.membersOf['class1']!['${uid}_ayesha']!;
    expect(member.firstName, 'Ayesha');
    expect(member.grade, 6);
    expect(find.byKey(const Key('class-class1')), findsOneWidget);

    await tapKey(tester, 'leave-class1');
    await tapKey(tester, 'confirm-leave-class');
    expect(find.byKey(const Key('class-class1')), findsNothing);
    expect(backend.classes.membersOf['class1'], isEmpty);
  });

  testWidgets('joining without internet says so', (tester) async {
    final backend = FakeBackend();
    backend.classes.addClass();
    await backend.db.addStudent(student('ayesha', grade: 6));
    await tester.pumpWidget(await buildTestApp(backend: backend));
    await tester.pumpAndSettle();
    await tapKey(tester, 'open-account');
    await tapKey(tester, 'classes-ayesha');

    backend.setOnline(false);
    await tester.enterText(find.byKey(const Key('class-code')), 'ABC234');
    await tapKey(tester, 'find-class');
    expect(find.textContaining('This needs internet'), findsOneWidget);
  });

  testWidgets("the teacher's lesson tops the child's plan until finished", (
    tester,
  ) async {
    final backend = FakeBackend();
    backend.classes.addClass();
    await backend.classes.assignAs(
      'class1',
      lessonId,
      due: DateTime(2026, 10, 10),
    );
    await backend.db.addStudent(student('ayesha', grade: 6));
    await backend.db.joinClass(
      ClassMembership(
        studentId: 'ayesha',
        classId: 'class1',
        className: '9 A',
        joinedAt: DateTime(2026, 10, 1),
      ),
    );
    await tester.pumpWidget(await buildTestApp(backend: backend));
    await tester.pumpAndSettle();
    await tapKey(tester, 'student-ayesha');

    // The phone fetched the lesson while syncing.
    final assigned = find.byKey(const Key('plan-assigned-$lessonId'));
    await waitFor(tester, assigned);
    expect(
      find.descendant(
        of: assigned,
        matching: find.textContaining('From your teacher'),
      ),
      findsOneWidget,
    );
    expect(backend.classes.families['class1'], isNotEmpty);

    // Finishing the lesson takes it off.
    await tester.runAsync(
      () => backend.db.recordStep(
        studentId: 'ayesha',
        lessonId: lessonId,
        lessonVersion: 1,
        stepIndex: 9,
        stepCount: 10,
        result: const StepResult(stepId: 'last', correct: true, attempts: 1),
      ),
    );
    await tester.pumpAndSettle();
    expect(assigned, findsNothing);
  });

  testWidgets(
    'a teacher creates a class, sees students and mistakes, assigns and deletes',
    (tester) async {
      final backend = FakeBackend();
      backend.auth.accounts[teacherEmail] = ('secret1', 'teacher1');
      await backend.auth.signIn(teacherEmail, 'secret1');
      // A child who will be in the class the teacher creates.
      backend.classes.membersOf['class1'] = {
        'phone-9_s1': ClassMember(
          uid: 'phone-9',
          studentId: 's1',
          firstName: 'Bilal',
          grade: 6,
          joinedAt: DateTime(2026, 10, 1),
          skills: const [
            (
              skill: 'maths.fractions.divide_by_fraction',
              level: 'learning',
              needsHelp: true,
              lastDay: '2026-10-02',
              nextReview: null,
            ),
          ],
          misconceptions: const [
            (lessonId: lessonId, id: 'division_makes_smaller', count: 3),
          ],
          lessons: const [(lessonId: lessonId, completed: true, nextStep: 10)],
        ),
      };
      await tester.pumpWidget(
        await buildTestApp(backend: backend, prefs: {'accountRole': 'teacher'}),
      );
      await tester.pumpAndSettle();

      await tapKey(tester, 'open-account');
      await tapKey(tester, 'my-classes');
      await waitFor(tester, find.byKey(const Key('no-classes')));
      expect(find.byKey(const Key('no-classes')), findsOneWidget);

      await tapKey(tester, 'new-class');
      await tester.enterText(find.byKey(const Key('class-name')), '6 B Maths');
      await tapKey(tester, 'create-class');
      await waitFor(tester, find.byKey(const Key('class-code-text')));

      final created = backend.classes.classes['class1']!;
      expect(created.name, '6 B Maths');
      expect(created.teacherUid, 'teacher1');
      expect(find.text('Code: ${created.code}'), findsOneWidget);
      expect(find.byKey(const Key('member-phone-9_s1')), findsOneWidget);
      expect(find.textContaining('Needs help with'), findsOneWidget);
      await waitFor(
        tester,
        find.text('Believes dividing always gives a smaller answer.'),
      );
      expect(
        find.text('Believes dividing always gives a smaller answer.'),
        findsOneWidget,
      );
      expect(find.text('Made by: Bilal'), findsOneWidget);

      await tapKey(tester, 'assign-lesson');
      await tapKey(tester, 'assign-lesson-choice');
      await tester.tap(find.byKey(const Key('assign-$lessonId')).last);
      await tester.pumpAndSettle();
      await tapKey(tester, 'confirm-assign');
      expect(
        backend.classes.assignmentsOf['class1']!.single.lessonId,
        lessonId,
      );
      final tile = find.byKey(const Key('assignment-$lessonId'));
      expect(tile, findsOneWidget);
      expect(
        find.descendant(of: tile, matching: find.text('1 of 1 finished')),
        findsOneWidget,
      );

      await tapKey(tester, 'unassign-$lessonId');
      expect(backend.classes.assignmentsOf['class1'], isEmpty);

      await tapKey(tester, 'delete-class');
      await tapKey(tester, 'confirm-delete-class');
      await waitFor(tester, find.byKey(const Key('no-classes')));
      expect(backend.classes.classes, isEmpty);
    },
  );
}
