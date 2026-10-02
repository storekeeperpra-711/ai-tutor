import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:shared_preferences/shared_preferences.dart';

import 'helpers.dart';

TextDirection directionOf(WidgetTester tester) =>
    Directionality.of(tester.element(find.byType(Scaffold).first));

void main() {
  testWidgets('starts in English, left-to-right', (tester) async {
    await tester.pumpWidget(await buildTestApp());
    await tester.pumpAndSettle();

    expect(find.text('AI Tutor'), findsOneWidget);
    expect(directionOf(tester), TextDirection.ltr);
  });

  testWidgets('switching to Urdu flips the app to right-to-left', (
    tester,
  ) async {
    await tester.pumpWidget(await buildTestApp());
    await tester.pumpAndSettle();

    await tester.tap(find.byIcon(Icons.settings));
    await tester.pumpAndSettle();
    await tester.tap(find.byKey(const Key('language-ur')));
    await tester.pumpAndSettle();

    expect(find.text('ترتیبات'), findsOneWidget);
    expect(directionOf(tester), TextDirection.rtl);

    // The choice is remembered for the next launch.
    final prefs = await SharedPreferences.getInstance();
    expect(prefs.getString('locale'), 'ur');

    await tester.tap(find.byType(BackButton));
    await tester.pumpAndSettle();
    expect(find.text('اے آئی ٹیوٹر'), findsOneWidget);
    expect(directionOf(tester), TextDirection.rtl);
  });

  testWidgets('remembers Urdu from the last launch', (tester) async {
    await tester.pumpWidget(await buildTestApp(prefs: {'locale': 'ur'}));
    await tester.pumpAndSettle();

    expect(find.text('اے آئی ٹیوٹر'), findsOneWidget);
    expect(directionOf(tester), TextDirection.rtl);
  });

  testWidgets('Urdu test screen opens', (tester) async {
    await tester.pumpWidget(await buildTestApp());
    await tester.pumpAndSettle();

    await tester.tap(find.text('Urdu text test'));
    await tester.pumpAndSettle();

    expect(find.textContaining('کششِ ثقل'), findsWidgets);
    expect(directionOf(tester), TextDirection.rtl);
  });

  testWidgets('choosing an age tier changes the theme', (tester) async {
    await tester.pumpWidget(await buildTestApp());
    await tester.pumpAndSettle();
    final before = Theme.of(tester.element(find.byType(Scaffold))).colorScheme;

    await tester.tap(find.byIcon(Icons.settings));
    await tester.pumpAndSettle();
    await tester.tap(find.byKey(const Key('tier-early')));
    await tester.pumpAndSettle();

    final after = Theme.of(tester.element(find.byType(Scaffold).last))
        .colorScheme;
    expect(after.primary, isNot(before.primary));
  });
}
