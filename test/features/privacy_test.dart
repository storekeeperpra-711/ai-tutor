import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import '../fakes.dart';
import '../helpers.dart';
import '../lessons/play_helpers.dart';

Color? highlight(WidgetTester tester, int i) {
  final box = tester.widget<AnimatedContainer>(
    find.byKey(Key('privacy-part-$i')),
  );
  return (box.decoration as BoxDecoration?)?.color;
}

Future<void> openFromSettings(WidgetTester tester, String key) async {
  await tester.tap(find.byIcon(Icons.settings));
  await tester.pumpAndSettle();
  await tester.scrollUntilVisible(
    find.byKey(Key(key)),
    300,
    scrollable: find.byType(Scrollable).last,
  );
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

  testWidgets('a parent reads the privacy note in Settings and listens', (
    tester,
  ) async {
    final backend = FakeBackend();
    await tester.pumpWidget(await buildTestApp(backend: backend));
    await tester.pumpAndSettle();
    await openFromSettings(tester, 'open-privacy');
    await tapKey(tester, 'open-privacy');

    expect(find.text('Privacy note'), findsOneWidget);
    await tester.scrollUntilVisible(
      find.textContaining("Your child's name is never sent"),
      300,
    );
    await tester.scrollUntilVisible(
      find.textContaining('kept for 90 days'),
      300,
    );
    await tester.scrollUntilVisible(
      find.byKey(const Key('privacy-listen')),
      -300,
    );

    backend.reportVoice.holdEach = true;
    await tapKey(tester, 'privacy-listen');
    expect(backend.reportVoice.said.single.$1, startsWith('This note says'));
    expect(highlight(tester, 0), isNot(Colors.transparent));
    backend.reportVoice.finishSentence();
    await tester.pump();
    await tester.pump();
    expect(backend.reportVoice.said[1].$1, startsWith('What we keep. '));
    expect(highlight(tester, 1), isNot(Colors.transparent));

    await tapKey(tester, 'privacy-stop');
    expect(find.byKey(const Key('privacy-listen')), findsOneWidget);
    expect(backend.reportVoice.said, hasLength(2));
  });

  testWidgets('in Urdu without an Urdu voice, Listen reads the English', (
    tester,
  ) async {
    final backend = FakeBackend();
    backend.reportVoice.languages.remove('ur');
    await tester.pumpWidget(
      await buildTestApp(backend: backend, prefs: {'locale': 'ur'}),
    );
    await tester.pumpAndSettle();
    await openFromSettings(tester, 'open-privacy');
    await tapKey(tester, 'open-privacy');
    expect(find.text('رازداری کا نوٹ'), findsWidgets);
    await tapKey(tester, 'privacy-listen');
    expect(backend.reportVoice.said, hasLength(8));
    expect(backend.reportVoice.said.every((s) => s.$2 == 'en'), isTrue);
  });

  testWidgets('without any voice there is no Listen button', (tester) async {
    final backend = FakeBackend();
    backend.reportVoice.languages.clear();
    await tester.pumpWidget(await buildTestApp(backend: backend));
    await tester.pumpAndSettle();
    await tapKey(tester, 'home-privacy');
    expect(find.text('Privacy note'), findsOneWidget);
    expect(find.byKey(const Key('privacy-listen')), findsNothing);
  });

  testWidgets('adding a child links the note and asks consent for AI help', (
    tester,
  ) async {
    await tester.pumpWidget(await buildTestApp());
    await tester.pumpAndSettle();
    await tapKey(tester, 'add-learner');
    await tester.scrollUntilVisible(
      find.byKey(const Key('consent')),
      300,
      scrollable: find.byType(Scrollable).last,
    );
    expect(find.textContaining('I have read the privacy note'), findsOneWidget);
    expect(find.textContaining("Mithu's AI help"), findsOneWidget);
    await tapKey(tester, 'open-privacy');
    expect(find.text('Privacy note'), findsOneWidget);
  });

  testWidgets('a parent can turn AI help off in Settings', (tester) async {
    await tester.pumpWidget(await buildTestApp());
    await tester.pumpAndSettle();
    await openFromSettings(tester, 'ai-help');
    final before = tester.widget<SwitchListTile>(
      find.byKey(const Key('ai-help')),
    );
    expect(before.value, isTrue);
    await tapKey(tester, 'ai-help');
    expect(
      tester.widget<SwitchListTile>(find.byKey(const Key('ai-help'))).value,
      isFalse,
    );
  });
}
