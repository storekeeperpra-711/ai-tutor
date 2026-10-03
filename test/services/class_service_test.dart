import 'package:ai_tutor/app/preferences.dart';
import 'package:ai_tutor/classes/class_service.dart';
import 'package:ai_tutor/classes/class_store.dart';
import 'package:ai_tutor/lessons/step_result.dart';
import 'package:ai_tutor/mastery/curriculum.dart';
import 'package:ai_tutor/services/auth_service.dart';
import 'package:ai_tutor/services/local_db.dart';
import 'package:ai_tutor/services/mastery_service.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:shared_preferences/shared_preferences.dart';

import '../fakes.dart';
import '../features/mastery_flow_test.dart' show practising;
import '../mastery/lessons.dart';

const lessonId = 'g6-maths-02-dividing-fractions';

void main() {
  late FakeBackend backend;
  late ProviderContainer container;
  late ClassService classes;
  final t0 = DateTime(2026, 10, 3, 9);

  setUp(() async {
    SharedPreferences.setMockInitialValues({});
    backend = FakeBackend();
    container = ProviderContainer(
      overrides: [
        sharedPreferencesProvider.overrideWithValue(
          await SharedPreferences.getInstance(),
        ),
        localDbProvider.overrideWithValue(backend.db),
        authServiceProvider.overrideWithValue(backend.auth),
        classStoreProvider.overrideWithValue(backend.classes),
        curriculumProvider.overrideWith(
          (ref) async => Curriculum(loadLessons()),
        ),
      ],
    );
    classes = container.read(classServiceProvider);
    await backend.auth.ensureSignedIn();
    await backend.db.addStudent(student('ayesha', grade: 6));
    backend.classes.addClass();
  });

  tearDown(() async {
    container.dispose();
    await backend.db.close();
  });

  String uid() => backend.auth.currentUser!.uid;
  Map<String, ClassMember> members() =>
      backend.classes.membersOf['class1'] ?? {};

  Future<void> joinAyesha() async {
    final found = await classes.find('abc 234');
    await classes.join((await backend.db.student('ayesha'))!, found, now: t0);
  }

  Future<void> answerWithMistake(DateTime at) => backend.db.recordStep(
    studentId: 'ayesha',
    lessonId: lessonId,
    lessonVersion: 1,
    stepIndex: 2,
    stepCount: 10,
    result: const StepResult(
      stepId: 's2',
      correct: false,
      attempts: 2,
      misconceptionIds: ['division_makes_smaller'],
    ),
    now: at,
  );

  test('the summary holds first name, grade, levels, mistakes and lessons', () {
    const fractions = 'maths.fractions.divide_by_fraction';
    final summary = classSummary(
      uid: 'phone-1',
      student: student('ayesha', grade: 6),
      joinedAt: t0,
      states: {fractions: practising(fractions, needsHelp: true)},
      progress: {
        lessonId: LessonProgress(
          studentId: 'ayesha',
          lessonId: lessonId,
          lessonVersion: 1,
          nextStep: 4,
          completed: false,
          updatedAt: t0,
        ),
      },
      steps: [
        for (final step in ['s1', 's2'])
          StepResultRow(
            studentId: 'ayesha',
            lessonId: lessonId,
            stepId: step,
            correct: false,
            attempts: 2,
            misconceptions: '["division_makes_smaller"]',
            answeredAt: t0,
            synced: false,
          ),
      ],
      curriculum: Curriculum(loadLessons()),
    );
    expect(summary.firstName, 'Ayesha');
    expect(summary.grade, 6);
    expect(summary.docId, 'phone-1_ayesha');
    expect(summary.skills.single.level, 'practising');
    expect(summary.skills.single.needsHelp, isTrue);
    expect(summary.misconceptions.single, (
      lessonId: lessonId,
      id: 'division_makes_smaller',
      count: 2,
    ));
    expect(summary.lessons.single.nextStep, 4);
    // Nothing else about the family: no PIN, no picture.
    expect(memberSummaryJson(summary).keys, {
      'uid',
      'student_id',
      'first_name',
      'grade',
      'joined_at',
      'skills',
      'misconceptions',
      'lessons',
    });
  });

  test(
    'a code is found in any case and with spaces; a wrong one is not',
    () async {
      expect((await classes.find('abc 234')).name, '9 A');
      expect((await classes.find('Abc-234')).id, 'class1');
      await expectLater(
        classes.find('ABC235'),
        throwsA(
          isA<ClassException>().having(
            (e) => e.problem,
            'problem',
            ClassProblem.notFound,
          ),
        ),
      );
      backend.setOnline(false);
      await expectLater(
        classes.find('ABC234'),
        throwsA(
          isA<ClassException>().having(
            (e) => e.problem,
            'problem',
            ClassProblem.noConnection,
          ),
        ),
      );
    },
  );

  test('joining shares the summary at once and records the family', () async {
    await joinAyesha();
    expect(members().keys, ['${uid()}_ayesha']);
    expect(backend.classes.families['class1'], {uid()});
    final rows = await backend.db.membershipsOf('ayesha');
    expect(rows.single.className, '9 A');
    expect(rows.single.sharedUid, uid());
  });

  test('a changed summary is shared at most every 15 minutes', () async {
    await joinAyesha();
    expect(backend.classes.memberWrites, 1);
    // Nothing changed: nothing written.
    await classes.sync(uid(), now: t0.add(const Duration(hours: 2)));
    expect(backend.classes.memberWrites, 1);

    final t1 = t0.add(const Duration(hours: 3));
    await answerWithMistake(t1);
    await classes.sync(uid(), now: t1);
    expect(backend.classes.memberWrites, 2);
    expect(members().values.single.misconceptions.single.count, 1);

    // Another answer soon after waits.
    await backend.db.recordStep(
      studentId: 'ayesha',
      lessonId: lessonId,
      lessonVersion: 1,
      stepIndex: 3,
      stepCount: 10,
      result: const StepResult(stepId: 's3', correct: true, attempts: 1),
      now: t1,
    );
    await classes.sync(uid(), now: t1.add(const Duration(minutes: 5)));
    expect(backend.classes.memberWrites, 2);
    await classes.sync(uid(), now: t1.add(const Duration(minutes: 16)));
    expect(backend.classes.memberWrites, 3);
    expect(members().values.single.lessons.single.nextStep, 4);
  });

  test(
    'after signing in to another account, the child joins again from it',
    () async {
      await joinAyesha();
      final oldUid = uid();
      backend.auth.accounts['mum@x.pk'] = ('secret1', 'adult-9');
      await backend.auth.signIn('mum@x.pk', 'secret1');
      await classes.sync('adult-9', now: t0.add(const Duration(minutes: 1)));
      expect(backend.classes.families['class1'], {oldUid, 'adult-9'});
      expect(members().keys, contains('adult-9_ayesha'));
    },
  );

  test('when the teacher deletes the class, the phone forgets it', () async {
    await joinAyesha();
    backend.classes
      ..classes.remove('class1')
      ..families.remove('class1');
    final t1 = t0.add(const Duration(hours: 1));
    await answerWithMistake(t1);
    await classes.sync(uid(), now: t1);
    expect(await backend.db.membershipsOf('ayesha'), isEmpty);
  });

  test(
    'assigned lessons are fetched on joining, then at most hourly',
    () async {
      await backend.classes.assignAs('class1', lessonId);
      await joinAyesha();
      await pumpEventQueue();
      final stream = backend.db.watchAssignmentsFor('ayesha');
      expect((await stream.first).map((a) => a.lessonId), [lessonId]);

      await backend.classes.assignAs('class1', 'g9-maths-05-feasible-region');
      await classes.sync(uid(), now: t0.add(const Duration(minutes: 10)));
      expect(await stream.first, hasLength(1));
      await classes.sync(uid(), now: t0.add(const Duration(minutes: 61)));
      expect(await stream.first, hasLength(2));
    },
  );

  test('leaving deletes the summary and the class lessons', () async {
    await backend.classes.assignAs('class1', lessonId);
    await joinAyesha();
    await pumpEventQueue();
    await classes.leave('ayesha', 'class1');
    await pumpEventQueue();
    expect(members(), isEmpty);
    expect(backend.classes.families['class1'], isEmpty);
    expect(await backend.db.membershipsOf('ayesha'), isEmpty);
    expect(await backend.db.watchAssignmentsFor('ayesha').first, isEmpty);
  });

  test("removing a child's profile takes them out of their classes", () async {
    await joinAyesha();
    await classes.leaveAll('ayesha');
    await backend.db.deleteStudent('ayesha');
    await pumpEventQueue();
    expect(members(), isEmpty);
  });
}
