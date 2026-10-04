import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import '../fakes.dart';
import '../helpers.dart';
import '../lessons/play_helpers.dart';

Color? highlight(WidgetTester tester, int i) {
  final box = tester.widget<AnimatedContainer>(
    find.byKey(Key('report-sentence-$i')),
  );
  return (box.decoration as BoxDecoration?)?.color;
}

Future<FakeBackend> openReport(
  WidgetTester tester, {
  Map<String, Object> prefs = const {},
  Set<String> voices = const {'en', 'ur'},
}) async {
  final backend = FakeBackend();
  backend.reportVoice.languages
    ..clear()
    ..addAll(voices);
  await backend.db.addStudent(student('ayesha', grade: 6));
  await answer(
    backend.db,
    'ayesha',
    0,
    lessonId: 'g6-maths-02-dividing-fractions',
  );
  await tester.pumpWidget(await buildTestApp(backend: backend, prefs: prefs));
  await tester.pumpAndSettle();
  await tapKey(tester, 'open-account');
  await tapKey(tester, 'report-ayesha');
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

  testWidgets('the report has a picture for each part and reads aloud', (
    tester,
  ) async {
    final backend = await openReport(tester);
    expect(find.text("Ayesha's week"), findsOneWidget);
    for (final part in ['learned', 'practice', 'home', 'effort']) {
      await tester.scrollUntilVisible(
        find.byKey(Key('report-part-$part')),
        300,
      );
    }
    expect(find.textContaining('Fold two paper circles'), findsOneWidget);
    await tester.scrollUntilVisible(
      find.byKey(const Key('report-listen')),
      -300,
    );

    backend.reportVoice.holdEach = true;
    await tester.tap(find.byKey(const Key('report-listen')));
    await tester.pump();
    // The first sentence is read and highlighted, the next one isn't yet.
    expect(backend.reportVoice.said.single.$2, 'en');
    expect(highlight(tester, 0), isNot(Colors.transparent));
    expect(highlight(tester, 1), Colors.transparent);

    backend.reportVoice.finishSentence();
    await tester.pump();
    await tester.pump();
    expect(backend.reportVoice.said, hasLength(2));
    expect(highlight(tester, 1), isNot(Colors.transparent));

    await tester.tap(find.byKey(const Key('report-stop')));
    await tester.pumpAndSettle();
    expect(find.byKey(const Key('report-listen')), findsOneWidget);
    expect(backend.reportVoice.said, hasLength(2));

    // All the way through.
    backend.reportVoice.holdEach = false;
    backend.reportVoice.said.clear();
    await tester.tap(find.byKey(const Key('report-listen')));
    await tester.pumpAndSettle();
    expect(
      backend.reportVoice.said.last.$1,
      'Ayesha practised on 1 of the last 7 days and answered 1 questions.',
    );
  });

  testWidgets('in Urdu it speaks Urdu', (tester) async {
    final backend = await openReport(tester, prefs: {'locale': 'ur'});
    await tester.tap(find.byKey(const Key('report-listen')));
    await tester.pumpAndSettle();
    expect(backend.reportVoice.said.first.$2, 'ur');
    expect(find.byKey(const Key('report-voice-help')), findsNothing);
  });

  testWidgets('without an Urdu voice, it explains how to add one', (
    tester,
  ) async {
    final backend = await openReport(
      tester,
      prefs: {'locale': 'ur'},
      voices: {'en'},
    );
    expect(find.byKey(const Key('report-voice-help')), findsOneWidget);
    await tester.tap(find.byKey(const Key('report-listen')));
    await tester.pumpAndSettle();
    expect(backend.reportVoice.said.first.$2, 'en');
    expect(backend.reportVoice.said.first.$1, startsWith('Ayesha'));
  });

  testWidgets('without any voice, the pictures carry the report', (
    tester,
  ) async {
    await openReport(tester, voices: {});
    expect(find.byKey(const Key('report-voice-help')), findsOneWidget);
    final button = tester.widget<ButtonStyleButton>(
      find.byKey(const Key('report-listen')),
    );
    expect(button.onPressed, isNull);
  });
}
