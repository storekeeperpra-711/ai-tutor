import 'package:ai_tutor/app/motion_widgets.dart';
import 'package:ai_tutor/app/theme/age_tier.dart';
import 'package:ai_tutor/app/theme/app_theme.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

Widget _app(Widget child, {bool still = false}) => MaterialApp(
  theme: buildTheme(AgeTier.older, const Locale('en')),
  home: MediaQuery(
    data: MediaQueryData(disableAnimations: still),
    child: Scaffold(body: child),
  ),
);

double _opacity(WidgetTester tester, Finder child) => tester
    .widget<FadeTransition>(
      find.ancestor(of: child, matching: find.byType(FadeTransition)).first,
    )
    .opacity
    .value;

void main() {
  testWidgets('cards float in one after another', (tester) async {
    await tester.pumpWidget(
      _app(
        Column(
          children: [
            for (var i = 0; i < 3; i++)
              EnterAnimation(index: i, child: Text('card $i')),
          ],
        ),
      ),
    );
    expect(_opacity(tester, find.text('card 0')), 0);
    await tester.pump(const Duration(milliseconds: 200));
    final first = _opacity(tester, find.text('card 0'));
    final third = _opacity(tester, find.text('card 2'));
    expect(first, greaterThan(third));
    await tester.pumpAndSettle();
    expect(_opacity(tester, find.text('card 2')), 1);
  });

  testWidgets('with less movement, cards are there at once', (tester) async {
    await tester.pumpWidget(
      _app(const EnterAnimation(index: 5, child: Text('card')), still: true),
    );
    expect(_opacity(tester, find.text('card')), 1);
  });

  testWidgets('a pressed card sinks and the tap still arrives', (tester) async {
    var taps = 0;
    await tester.pumpWidget(
      _app(
        Center(
          child: Pressable(
            child: FilledButton(
              onPressed: () => taps++,
              child: const Text('Go'),
            ),
          ),
        ),
      ),
    );
    double scale() =>
        tester.widget<AnimatedScale>(find.byType(AnimatedScale)).scale;
    final gesture = await tester.startGesture(
      tester.getCenter(find.text('Go')),
    );
    await tester.pump();
    expect(scale(), lessThan(1));
    await gesture.up();
    await tester.pumpAndSettle();
    expect(scale(), 1);
    expect(taps, 1);
  });

  testWidgets('numbers count up to their value', (tester) async {
    await tester.pumpWidget(
      _app(CountUp(value: 180, format: (n) => '$n points')),
    );
    await tester.pump(const Duration(milliseconds: 100));
    expect(find.text('180 points'), findsNothing);
    await tester.pumpAndSettle();
    expect(find.text('180 points'), findsOneWidget);
  });

  testWidgets('new screens rise with a curved edge', (tester) async {
    await tester.pumpWidget(_app(const Text('first')));
    final navigator = tester.state<NavigatorState>(find.byType(Navigator));
    navigator.push(
      MaterialPageRoute<void>(
        builder: (_) => const Scaffold(body: Text('second')),
      ),
    );
    await tester.pump();
    await tester.pump(const Duration(milliseconds: 150));
    expect(find.byType(ClipPath), findsWidgets);
    await tester.pumpAndSettle();
    expect(find.text('second'), findsOneWidget);
    expect(
      find.ancestor(of: find.text('second'), matching: find.byType(ClipPath)),
      findsNothing,
    );
  });

  test(
    'the curved edge covers nothing at the start and everything at the end',
    () {
      const size = Size(390, 844);
      expect(
        const WaveClipper(0).getClip(size).contains(const Offset(195, 800)),
        isFalse,
      );
      final full = const WaveClipper(1).getClip(size);
      expect(full.contains(const Offset(1, 1)), isTrue);
      expect(full.contains(const Offset(389, 843)), isTrue);
      // Halfway, the middle of the edge is higher than its ends.
      final half = const WaveClipper(0.5).getClip(size);
      expect(half.contains(const Offset(195, 440)), isTrue);
      expect(half.contains(const Offset(5, 440)), isFalse);
    },
  );

  testWidgets('drifting dots move once round, then rest; still with less '
      'movement', (tester) async {
    await tester.pumpWidget(_app(const SizedBox.expand(child: FloatingDots())));
    await tester.pump(const Duration(seconds: 1));
    expect(tester.hasRunningAnimations, isTrue);
    await tester.pump(const Duration(seconds: 14));
    expect(tester.hasRunningAnimations, isFalse);

    await tester.pumpWidget(
      _app(const SizedBox.expand(child: FloatingDots()), still: true),
    );
    // (The new theme fades in first.)
    await tester.pump(const Duration(seconds: 1));
    expect(tester.hasRunningAnimations, isFalse);
  });
}
