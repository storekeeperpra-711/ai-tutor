import 'package:ai_tutor/features/phone_check/phone_check_screen.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import '../fakes.dart';
import '../helpers.dart';
import '../lessons/play_helpers.dart';

void main() {
  test('sizes read as megabytes', () {
    expect(megabytes(0), '0.0 MB');
    expect(megabytes(1536 * 1024), '1.5 MB');
  });

  testWidgets('a long press on Settings opens the Phone check, which can '
      'remove saved videos', (tester) async {
    final backend = FakeBackend();
    backend.mediaIndex
      ..add('https://v/1.mp4', 30 * 1024 * 1024, DateTime(2026, 10, 1))
      ..add('https://v/2.mp4', 12 * 1024 * 1024, DateTime(2026, 10, 2));
    await tester.pumpWidget(await buildTestApp(backend: backend));
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

    await tapKey(tester, 'phone-check-clear-media');
    expect(
      find.descendant(of: media, matching: find.text('0.0 MB / 300.0 MB')),
      findsOneWidget,
    );
  });
}
