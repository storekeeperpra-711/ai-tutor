import 'dart:convert';
import 'dart:io';

import 'package:ai_tutor/models/lesson.dart';
import 'package:ai_tutor/services/profiles.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import '../fakes.dart';
import '../helpers.dart';
import '../lessons/play_helpers.dart';

final lesson = Lesson.fromJson(
  jsonDecode(
    File('content/lessons/g6-maths-02-dividing-fractions.json')
        .readAsStringSync(),
  ) as Map<String, dynamic>,
);

/// Answers the next [count] steps of the open lesson, starting at [from].
Future<void> playSteps(WidgetTester tester, int from, int count) async {
  for (final step in lesson.steps.skip(from).take(count)) {
    await answerStep(tester, step, tryWrongFirst: false);
    await tapKey(tester, 'step-continue');
  }
}

Future<void> addLearner(
  WidgetTester tester, {
  required String name,
  required String grade,
  String pin = '',
}) async {
  await tapKey(tester, 'add-learner');
  await tester.enterText(find.byKey(const Key('first-name')), name);
  await tester.ensureVisible(find.text(grade).last);
  await tester.tap(find.text(grade).last);
  await tester.pumpAndSettle();
  await tapKey(tester, 'avatar-cricket');
  if (pin.isNotEmpty) {
    await tester.enterText(find.byKey(const Key('pin')), pin);
  }
  await tapKey(tester, 'consent');
  await tapKey(tester, 'save-learner');
}

Future<void> goBack(WidgetTester tester) async {
  await tester.tap(find.byType(BackButton));
  await tester.pumpAndSettle();
}

String statusOf(WidgetTester tester) => tester
    .widget<Text>(find.byKey(Key('home-lesson-status-${lesson.id}')))
    .data!;

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

  testWidgets('two children on one phone keep separate progress', (
    tester,
  ) async {
    final backend = FakeBackend();
    await tester.pumpWidget(await buildTestApp(backend: backend));
    await tester.pumpAndSettle();

    // Ayesha (with a PIN) plays three steps.
    await addLearner(tester, name: 'Ayesha', grade: 'Grade 6', pin: '1234');
    expect(find.text('Hello, Ayesha!'), findsOneWidget);
    await tapKey(tester, 'home-lesson-${lesson.id}');
    await playSteps(tester, 0, 3);
    await goBack(tester);
    expect(statusOf(tester), 'Continue at step 4 of ${lesson.steps.length}');

    // Bilal (no PIN) has his own, empty progress.
    await tapKey(tester, 'switch-learner');
    await addLearner(tester, name: 'Bilal', grade: 'Grade 9');
    expect(find.text('Hello, Bilal!'), findsOneWidget);
    expect(statusOf(tester), 'Start');
    await tapKey(tester, 'home-lesson-${lesson.id}');
    await playSteps(tester, 0, 1);
    await goBack(tester);
    expect(statusOf(tester), 'Continue at step 2 of ${lesson.steps.length}');

    // Back to Ayesha: her profile needs her PIN.
    await tapKey(tester, 'switch-learner');
    final ayesha = (await backend.db.select(backend.db.students).get()).first;
    await tapKey(tester, 'student-${ayesha.id}');
    for (final d in '9999'.split('')) {
      await tapKey(tester, 'pin-$d');
    }
    expect(find.byKey(const Key('pin-wrong')), findsOneWidget);
    for (final d in '1234'.split('')) {
      await tapKey(tester, 'pin-$d');
    }
    expect(find.text('Hello, Ayesha!'), findsOneWidget);
    expect(statusOf(tester), 'Continue at step 4 of ${lesson.steps.length}');

    // The lesson reopens exactly where she stopped.
    await tapKey(tester, 'home-lesson-${lesson.id}');
    expect(find.text('Step 4 of ${lesson.steps.length}'), findsOneWidget);

    // Both children's work reached the account, separately.
    final uid = backend.auth.currentUser!.uid;
    final bilal = (await backend.db.select(backend.db.students).get()).last;
    expect(
      backend.remote.progressDoc(uid, ayesha.id, lesson.id)!['next_step'],
      3,
    );
    expect(
      backend.remote.progressDoc(uid, bilal.id, lesson.id)!['next_step'],
      1,
    );
    // Only a salted hash of the PIN leaves the phone.
    final doc = backend.remote.docs['accounts/$uid/students/${ayesha.id}']!;
    expect(doc['pin_hash'], isNot(contains('1234')));
    expect(checkPin('1234', doc['pin_hash']! as String), isTrue);
  });

  testWidgets('a lesson carries on offline and syncs when back online', (
    tester,
  ) async {
    final backend = FakeBackend();
    await backend.db.addStudent(student('ayesha'));
    await tester.pumpWidget(await buildTestApp(backend: backend));
    await tester.pumpAndSettle();

    await tapKey(tester, 'student-ayesha');
    await tapKey(tester, 'home-lesson-${lesson.id}');
    await playSteps(tester, 0, 2);
    final uid = backend.auth.currentUser!.uid;
    expect(
      backend.remote.progressDoc(uid, 'ayesha', lesson.id)!['next_step'],
      2,
    );
    expect(find.byKey(const Key('sync-status')), findsNothing);

    // The connection drops mid-lesson. The lesson doesn't stop.
    backend.setOnline(false);
    await tester.pumpAndSettle();
    expect(
      find.text('Offline: your work is saved on this phone'),
      findsOneWidget,
    );
    await playSteps(tester, 2, 2);
    expect(find.text('Step 5 of ${lesson.steps.length}'), findsOneWidget);
    expect(await backend.db.pendingCount(), 2);
    expect(
      backend.remote.progressDoc(uid, 'ayesha', lesson.id)!['next_step'],
      2,
    );

    // Back online: the waiting answers sync by themselves.
    backend.setOnline(true);
    await tester.pumpAndSettle();
    expect(
      backend.remote.progressDoc(uid, 'ayesha', lesson.id)!['next_step'],
      4,
    );
    expect(await backend.db.pendingCount(), 0);
    expect(find.byKey(const Key('sync-status')), findsNothing);
  });
}
