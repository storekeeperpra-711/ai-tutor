import 'dart:convert';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import '../fakes.dart';
import '../helpers.dart';
import 'classes_test.dart' show waitFor;
import '../lessons/play_helpers.dart';

const lessonId = 'g6-maths-02-dividing-fractions';
const videoEn = 'https://media.example/roti_en.mp4';
const captionsEn = 'https://media.example/roti_en.vtt';
const videoUr = 'https://media.example/roti_ur.mp4';
const captionsUr = 'https://media.example/roti_ur.vtt';

/// The fractions lesson, published with its videos as links.
void addLinkedVideoLesson(FakeBackend b) {
  final text = File('content/lessons/$lessonId.json').readAsStringSync();
  final linked = text
      .replaceAll('"fractions_roti_en.mp4"', '"$videoEn"')
      .replaceAll('"fractions_roti_en.vtt"', '"$captionsEn"')
      .replaceAll('"fractions_roti_ur.mp4"', '"$videoUr"')
      .replaceAll('"fractions_roti_ur.vtt"', '"$captionsUr"');
  // Published lessons reach the phone when the app starts.
  b.remote.publishLesson(jsonDecode(linked) as Map<String, Object?>);
}

Future<void> openSettings(WidgetTester tester) async {
  await tester.tap(find.byIcon(Icons.settings));
  await tester.pumpAndSettle();
}

void main() {
  testWidgets('Data saver is on by default and shows the mobile data used', (
    tester,
  ) async {
    await tester.pumpWidget(
      await buildTestApp(
        prefs: {
          'data.days': jsonEncode({
            // Today's date as the app sees it.
            _today(): [0, 3 * 1024 * 1024],
          }),
        },
      ),
    );
    await tester.pumpAndSettle();
    await openSettings(tester);
    await tester.scrollUntilVisible(
      find.byKey(const Key('data-used-mobile')),
      300,
      scrollable: find.byType(Scrollable).last,
    );
    final saver = tester.widget<SwitchListTile>(
      find.byKey(const Key('data-saver')),
    );
    expect(saver.value, isTrue);
    expect(
      find.text('Mobile data used in the last 7 days: 3.0 MB'),
      findsOneWidget,
    );
    await tapKey(tester, 'data-saver');
    expect(
      tester.widget<SwitchListTile>(find.byKey(const Key('data-saver'))).value,
      isFalse,
    );
  });

  testWidgets('with no video links, Downloads says there is nothing to do', (
    tester,
  ) async {
    await tester.pumpWidget(await buildTestApp());
    await tester.pumpAndSettle();
    await openSettings(tester);
    await tester.scrollUntilVisible(
      find.byKey(const Key('open-downloads')),
      300,
      scrollable: find.byType(Scrollable).last,
    );
    await tapKey(tester, 'open-downloads');
    await waitFor(tester, find.byKey(const Key('downloads-none')));
    expect(find.byKey(const Key('downloads-none')), findsOneWidget);
  });

  testWidgets('a parent downloads a lesson\'s videos and removes them', (
    tester,
  ) async {
    final backend = FakeBackend();
    addLinkedVideoLesson(backend);
    await tester.pumpWidget(await buildTestApp(backend: backend));
    await tester.pumpAndSettle();
    await openSettings(tester);
    await tester.scrollUntilVisible(
      find.byKey(const Key('open-downloads')),
      300,
      scrollable: find.byType(Scrollable).last,
    );
    await tapKey(tester, 'open-downloads');

    await waitFor(tester, find.byKey(const Key('download-save-$lessonId')));
    await tester.tap(find.byKey(const Key('download-save-$lessonId')));
    await waitFor(tester, find.byKey(const Key('download-remove-$lessonId')));
    expect(backend.mediaManager.downloaded.toSet(), {videoEn, captionsEn});
    expect(find.text('Saved on this phone (10.0 MB)'), findsOneWidget);

    await tester.tap(find.byKey(const Key('download-remove-$lessonId')));
    await waitFor(tester, find.byKey(const Key('download-save-$lessonId')));
    expect(backend.mediaIndex.objects, isEmpty);

    // Offline, the parent is told.
    backend.mediaManager.failDownloads = true;
    await tester.tap(find.byKey(const Key('download-save-$lessonId')));
    // (Plain pumps: the fake download fails at once, with no real waiting.)
    for (var i = 0; i < 10; i++) {
      await tester.pump(const Duration(milliseconds: 100));
    }
    expect(find.byKey(const Key('download-failed-$lessonId')), findsOneWidget);
    expect(
      find.text("Couldn't download. Check the internet and try again."),
      findsOneWidget,
    );
  });
}

String _today() {
  final t = DateTime.now();
  return '${t.year.toString().padLeft(4, '0')}-'
      '${t.month.toString().padLeft(2, '0')}-'
      '${t.day.toString().padLeft(2, '0')}';
}
