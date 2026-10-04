import 'dart:convert';

import 'package:ai_tutor/app/crash_reports.dart';
import 'package:ai_tutor/features/phone_check/phone_check_screen.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:shared_preferences/shared_preferences.dart';

import '../fakes.dart';
import '../helpers.dart';
import '../lessons/play_helpers.dart';

void main() {
  test('sizes read as megabytes', () {
    expect(megabytes(0), '0.0 MB');
    expect(megabytes(1536 * 1024), '1.5 MB');
  });

  test('crashes are counted per day and kept for 7 days', () async {
    SharedPreferences.setMockInitialValues({});
    final counter = CrashCounter(await SharedPreferences.getInstance());
    expect(counter.lastWeek(DateTime(2026, 10, 4)), 0);
    await counter.add(DateTime(2026, 9, 27));
    await counter.add(DateTime(2026, 9, 28));
    await counter.add(DateTime(2026, 10, 4, 9));
    await counter.add(DateTime(2026, 10, 4, 18));
    // 28 September to 4 October is the last 7 days.
    expect(counter.lastWeek(DateTime(2026, 10, 4)), 3);
    expect(counter.lastWeek(DateTime(2026, 10, 11)), 0);
  });

  testWidgets('a long press on Settings opens the Phone check, which can '
      'remove saved videos', (tester) async {
    final backend = FakeBackend();
    backend.mediaIndex
      ..add('https://v/1.mp4', 30 * 1024 * 1024, DateTime(2026, 10, 1))
      ..add('https://v/2.mp4', 12 * 1024 * 1024, DateTime(2026, 10, 2));
    final today = DateTime.now();
    final day =
        '${today.year.toString().padLeft(4, '0')}-'
        '${today.month.toString().padLeft(2, '0')}-'
        '${today.day.toString().padLeft(2, '0')}';
    await tester.pumpWidget(
      await buildTestApp(
        backend: backend,
        prefs: {
          'crashes.days': jsonEncode({day: 2}),
        },
      ),
    );
    await tester.pumpAndSettle();

    await tester.tap(find.byIcon(Icons.settings));
    await tester.pumpAndSettle();
    await tester.longPress(find.byKey(const Key('settings-title')));
    await tester.pumpAndSettle();

    expect(find.text('Phone check'), findsOneWidget);
    final media = find.byKey(const Key('phone-check-media'));
    expect(
      find.descendant(of: media, matching: find.text('42.0 MB / 300.0 MB')),
      findsOneWidget,
    );
    expect(find.byKey(const Key('phone-check-memory')), findsOneWidget);
    expect(
      find.descendant(
        of: find.byKey(const Key('phone-check-lessons')),
        matching: find.text('0'),
      ),
      findsOneWidget,
    );

    await tester.scrollUntilVisible(
      find.byKey(const Key('phone-check-crashes')),
      200,
    );
    expect(
      find.descendant(
        of: find.byKey(const Key('phone-check-crashes')),
        matching: find.text('2'),
      ),
      findsOneWidget,
    );

    await tapKey(tester, 'phone-check-clear-media');
    expect(
      find.descendant(of: media, matching: find.text('0.0 MB / 300.0 MB')),
      findsOneWidget,
    );
  });
}
