import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import '../lessons/play_helpers.dart';
import 'tier_homes_test.dart' show openHomeFor;

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

  testWidgets('the bottom menu opens lessons, badges and settings', (
    tester,
  ) async {
    await openHomeFor(tester, grade: 6);
    expect(find.byKey(const Key('bottom-bar')), findsOneWidget);
    expect(find.byKey(const Key('middle-home')), findsOneWidget);

    await tapKey(tester, 'nav-lessons');
    expect(find.byKey(const Key('lessons-tab')), findsOneWidget);
    expect(find.byKey(const Key('middle-home')), findsNothing);
    expect(find.byKey(const Key('course-card')), findsOneWidget);
    expect(find.byKey(const Key('unit-g6-maths-05')), findsOneWidget);

    await tapKey(tester, 'nav-badges');
    expect(find.byKey(const Key('badges-tab')), findsOneWidget);
    expect(find.byKey(const Key('badge-firstLesson-not-yet')), findsOneWidget);
    expect(find.textContaining('You earn badges for effort'), findsOneWidget);

    await tapKey(tester, 'nav-home');
    expect(find.byKey(const Key('middle-home')), findsOneWidget);

    await tapKey(tester, 'nav-settings');
    expect(find.byKey(const Key('language-ur')), findsOneWidget);
  });

  testWidgets('switching learner starts again on Home', (tester) async {
    await openHomeFor(tester, grade: 9);
    await tapKey(tester, 'nav-badges');
    await tapKey(tester, 'switch-learner');
    await tapKey(tester, 'student-kid');
    expect(find.byKey(const Key('older-home')), findsOneWidget);
  });

  testWidgets('the little ones have no bottom menu', (tester) async {
    await openHomeFor(tester, grade: 1);
    expect(find.byKey(const Key('early-home')), findsOneWidget);
    expect(find.byKey(const Key('bottom-bar')), findsNothing);
    expect(find.byIcon(Icons.settings), findsOneWidget);
  });
}
