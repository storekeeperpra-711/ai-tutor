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
  return (await tester.runAsync(
    () => backend.db.select(backend.db.students).get(),
  ))!.single;
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

    await tester.runAsync(() async {
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
    });
    await tester.pumpAndSettle();

    expect(find.text('Mithu has new notes for you (1)'), findsOneWidget);
    await tapKey(tester, 'mithu-notes-card');
    expect(find.text('Good start!'), findsOneWidget);
    expect(find.text('“answer q2”'), findsOneWidget);
    expect(find.textContaining('Checked by AI'), findsOneWidget);

    await goBack(tester);
    await tester.runAsync(() => Future<void>.delayed(Duration.zero));
    await tester.pumpAndSettle();
    expect(find.byKey(const Key('mithu-notes-card')), findsNothing);
  });

  testWidgets('a parent reads the weekly report, and offline is explained', (
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
      'stats': {
        'active_days': 4,
        'lessons_finished': 2,
        'questions_answered': 30,
      },
    };

    await tapKey(tester, 'open-account');
    await tapKey(tester, 'report-${ayesha.id}');
    expect(find.text('Ayesha practised well.'), findsOneWidget);
    expect(find.textContaining('4 days of practice'), findsOneWidget);
    await tester.tap(find.text('Close'));
    await tester.pumpAndSettle();

    backend.setOnline(false);
    await tapKey(tester, 'report-${ayesha.id}');
    expect(find.byKey(const Key('report-error')), findsOneWidget);
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
}
