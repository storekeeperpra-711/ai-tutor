import 'dart:io';

import 'package:ai_tutor/app/motion.dart';
import 'package:ai_tutor/features/common/celebration.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:lottie/lottie.dart';

import '../helpers.dart';
import '../lessons/play_helpers.dart';
import '../mastery/lessons.dart';

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

  test('every Lottie file loads', () async {
    for (final file in Directory(
      'assets/lottie',
    ).listSync().whereType<File>()) {
      if (!file.path.endsWith('.json')) continue;
      final composition = await LottieComposition.fromBytes(
        file.readAsBytesSync(),
      );
      expect(
        composition.duration,
        greaterThan(Duration.zero),
        reason: file.path,
      );
      expect(composition.layers, isNotEmpty, reason: file.path);
    }
  });

  testWidgets("a video that can't play shows its summary instead", (
    tester,
  ) async {
    await tester.pumpWidget(await buildTestApp());
    await tester.pumpAndSettle();
    await openPreviewLesson(tester, 'g6-maths-02-dividing-fractions');
    // Jump to the video by answering the steps before it.
    final lesson = loadLessonJson(lessonJson('g6-maths-02-dividing-fractions'));
    for (final step in lesson.steps.takeWhile((s) => s.type != 'video')) {
      await answerStep(tester, step, tryWrongFirst: false);
      await tapKey(tester, 'step-continue');
    }
    expect(find.byKey(const Key('video-fallback')), findsOneWidget);
    expect(find.textContaining('8 children can eat'), findsOneWidget);
    await tapKey(tester, 'step-continue');
    expect(find.byKey(const Key('video-fallback')), findsNothing);
  });

  testWidgets('Less movement turns animations off for the whole app', (
    tester,
  ) async {
    await tester.pumpWidget(await buildTestApp());
    await tester.pumpAndSettle();
    final context = tester.element(find.byType(Scaffold).first);
    expect(reduceMotion(context), isFalse);

    await tester.tap(find.byIcon(Icons.settings));
    await tester.pumpAndSettle();
    await tapKey(tester, 'less-motion');
    expect(reduceMotion(tester.element(find.byType(Scaffold).last)), isTrue);
  });

  testWidgets('a celebration shows and then removes itself', (tester) async {
    await tester.pumpWidget(
      const MaterialApp(home: Scaffold(body: SizedBox.expand())),
    );
    celebrate(tester.element(find.byType(Scaffold)), 'Well done!');
    await tester.pump();
    expect(find.text('Well done!'), findsOneWidget);
    await tester.pump(const Duration(seconds: 1));
    expect(find.text('Well done!'), findsOneWidget);
    await tester.pumpAndSettle();
    expect(find.text('Well done!'), findsNothing);
  });

  testWidgets('the developer screen opens every native interactive', (
    tester,
  ) async {
    await tester.pumpWidget(await buildTestApp());
    await tester.pumpAndSettle();
    await tapKey(tester, 'open-sim-gallery');
    // In the gallery's order, so the list only scrolls down.
    for (final id in [
      'roti_strips.html',
      'fraction_bars',
      'balance_scale',
      'atom_balancer',
      'number_line',
      'graph_plotter',
      'inequality_plane',
      'feasible_region',
    ]) {
      await tester.scrollUntilVisible(find.byKey(Key('gallery-$id')), 100);
      await tapKey(tester, 'gallery-$id');
      expect(find.byKey(const Key('sim-area')), findsOneWidget, reason: id);
      expect(tester.takeException(), isNull, reason: id);
      await tester.pageBack();
      await tester.pumpAndSettle();
    }
  });
}
