import 'package:ai_tutor/services/local_db.dart';
import 'package:flutter_test/flutter_test.dart';

import '../fakes.dart';

void main() {
  late LocalDb db;

  setUp(() async {
    db = FakeBackend().db;
    await db.addStudent(student('ayesha'));
    await db.addStudent(student('bilal', name: 'Bilal'));
  });

  tearDown(() => db.close());

  test('each step moves the resume point on', () async {
    await answer(db, 'ayesha', 0);
    await answer(db, 'ayesha', 1);
    final p = await db.progress('ayesha', 'lesson-a');
    expect(p!.nextStep, 2);
    expect(p.completed, isFalse);
  });

  test('the last step finishes the lesson', () async {
    for (var i = 0; i < 5; i++) {
      await answer(db, 'ayesha', i);
    }
    final p = await db.progress('ayesha', 'lesson-a');
    expect(p!.completed, isTrue);
  });

  test('two children keep separate progress', () async {
    await answer(db, 'ayesha', 0);
    await answer(db, 'ayesha', 1);
    await answer(db, 'ayesha', 2);
    await answer(db, 'bilal', 0);
    expect((await db.progress('ayesha', 'lesson-a'))!.nextStep, 3);
    expect((await db.progress('bilal', 'lesson-a'))!.nextStep, 1);
  });

  test('unsynced answers are counted and grouped per lesson', () async {
    await answer(db, 'ayesha', 0);
    await answer(db, 'ayesha', 1);
    await answer(db, 'bilal', 0, lessonId: 'lesson-b');
    expect(await db.pendingCount(), 3);
    expect(await db.watchPendingCount().first, 3);

    final uploads = await db.pendingUploads();
    expect(uploads, hasLength(2));
    await db.markStepsSynced(uploads.expand((u) => u.steps).toList());
    expect(await db.pendingCount(), 0);
  });

  test('an answer changed during upload stays in the queue', () async {
    await answer(db, 'ayesha', 0, now: DateTime(2026, 10, 2, 9));
    final uploading = (await db.pendingUploads()).single.steps;
    // The child plays the step again while the upload is on its way.
    await answer(db, 'ayesha', 0, now: DateTime(2026, 10, 2, 10));
    await db.markStepsSynced(uploading);
    expect(await db.pendingCount(), 1);
  });

  test('removing a child removes their progress', () async {
    await answer(db, 'ayesha', 0);
    await db.deleteStudent('ayesha');
    expect(await db.student('ayesha'), isNull);
    expect(await db.progress('ayesha', 'lesson-a'), isNull);
    expect(await db.pendingCount(), 0);
  });

  test('remote progress is merged; newer local progress wins', () async {
    await answer(db, 'ayesha', 0, now: DateTime(2026, 10, 2, 12));
    await db.mergeRemote(
      RemoteData(
        students: [student('zara', name: 'Zara')],
        progress: [
          LessonProgress(
            studentId: 'ayesha',
            lessonId: 'lesson-a',
            lessonVersion: 1,
            nextStep: 4,
            completed: false,
            updatedAt: DateTime(2026, 10, 1),
          ),
          LessonProgress(
            studentId: 'zara',
            lessonId: 'lesson-a',
            lessonVersion: 1,
            nextStep: 2,
            completed: false,
            updatedAt: DateTime(2026, 10, 1),
          ),
        ],
      ),
    );
    expect((await db.progress('ayesha', 'lesson-a'))!.nextStep, 1);
    expect((await db.progress('zara', 'lesson-a'))!.nextStep, 2);
    expect((await db.student('zara'))!.synced, isTrue);
  });
}
