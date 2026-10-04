import 'package:ai_tutor/ai/ai_service.dart';
import 'package:ai_tutor/services/local_db.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import '../fakes.dart';
import '../helpers.dart';
import '../lessons/play_helpers.dart';
import 'profiles_and_progress_test.dart' show addLearner, goBack;

Future<Student> start(WidgetTester tester, FakeBackend backend) async {
  await tester.pumpWidget(await buildTestApp(backend: backend));
  await tester.pumpAndSettle();
  await addLearner(tester, name: 'Ayesha', grade: 'Grade 9');
  return (await backend.db.select(backend.db.students).get()).single;
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

  testWidgets('Mithu\'s replies to queued answers appear on the home screen', (
    tester,
  ) async {
    final backend = FakeBackend();
    final ayesha = await start(tester, backend);
    expect(find.byKey(const Key('mithu-notes-card')), findsNothing);

    for (final id in ['q1', 'q2']) {
      await backend.db.queueAnswer(
        QueuedAnswer(
          id: id,
          studentId: ayesha.id,
          lessonId: 'g9-maths-05-solving-linear-equations',
          stepId: 's5_explain_balance',
          task: 'Why do we do the same to both sides?',
          lang: 'en',
          answer: 'answer $id',
          createdAt: DateTime(2026, 10, 3),
          uploaded: true,
          status: 'waiting',
          seen: false,
        ),
      );
    }
    await backend.db.saveReply(
      'q1',
      status: 'answered',
      level: 'partly',
      reply: 'Good start!',
    );
    await tester.pumpAndSettle();

    expect(find.text('Mithu has new notes for you (1)'), findsOneWidget);
    await tapKey(tester, 'mithu-notes-card');
    expect(find.text('Good start!'), findsOneWidget);
    expect(find.text('“answer q2”'), findsOneWidget);
    expect(find.textContaining('Checked by AI'), findsOneWidget);

    await goBack(tester);
    await tester.pumpAndSettle();
    expect(find.byKey(const Key('mithu-notes-card')), findsNothing);
  });

  testWidgets("Mithu's weekly note ends the report when online", (
    tester,
  ) async {
    final backend = FakeBackend();
    final ayesha = await start(tester, backend);
    final uid = backend.auth.currentUser!.uid;
    backend
        .remote
        .docs['accounts/$uid/students/${ayesha.id}/reports/2026-10-04'] = {
      'week': '2026-10-04',
      'note': {'en': 'Ayesha practised well.', 'ur': 'عائشہ نے اچھی مشق کی۔'},
      'stats': {'active_days': 4},
    };

    await tapKey(tester, 'open-account');
    await tapKey(tester, 'report-${ayesha.id}');
    await tester.scrollUntilVisible(
      find.byKey(const Key('report-mithu-note')),
      300,
    );
    expect(find.text('Ayesha practised well.'), findsOneWidget);
    await goBack(tester);

    // Offline, the report still works, without the note.
    backend.setOnline(false);
    await tapKey(tester, 'report-${ayesha.id}');
    await tester.scrollUntilVisible(
      find.byKey(const Key('report-part-effort')),
      300,
    );
    expect(find.byKey(const Key('report-mithu-note')), findsNothing);
  });

  testWidgets('the cost dashboard shows AI use per student per day', (
    tester,
  ) async {
    final backend = FakeBackend();
    await start(tester, backend);
    await tester.tap(find.byTooltip('Settings'));
    await tester.pumpAndSettle();
    await tapKey(tester, 'open-ai-costs');
    expect(find.text(r'Last 7 days: $0.0045'), findsOneWidget);
    expect(find.textContaining('2026-10-03'), findsOneWidget);
    expect(find.textContaining('2 text · 1 photos'), findsOneWidget);

    await goBack(tester);
    backend.setOnline(false);
    await tapKey(tester, 'open-ai-costs');
    expect(find.byKey(const Key('costs-error')), findsOneWidget);
  });

  testWidgets('an admin also sees the daily learning totals', (tester) async {
    final backend = FakeBackend();
    backend.ai.costReport = const CostReport(
      all: true,
      totalUsd: 0,
      rows: [],
      learning: [
        LearningDay(
          day: '2026-10-03',
          students: 5,
          lessons: 7,
          lessonsFinished: 3,
          questions: 40,
          firstTry: 25,
          aiCalls: 12,
        ),
      ],
    );
    await start(tester, backend);
    await tester.tap(find.byTooltip('Settings'));
    await tester.pumpAndSettle();
    await tapKey(tester, 'open-ai-costs');
    expect(find.text('Learning in the whole project'), findsOneWidget);
    expect(
      find.text(
        '5 children · 7 lessons (3 finished) · 40 questions '
        '(25 right first time) · 12 AI checks',
      ),
      findsOneWidget,
    );
  });
}
