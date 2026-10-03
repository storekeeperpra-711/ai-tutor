import 'package:ai_tutor/checkers/rational.dart';
import 'package:ai_tutor/l10n/app_localizations.dart';
import 'package:ai_tutor/models/lesson_step.dart';
import 'package:ai_tutor/models/localized_text.dart';
import 'package:ai_tutor/sims/native/balance_scale.dart';
import 'package:ai_tutor/sims/native/graph_plotter.dart';
import 'package:ai_tutor/sims/native/native_sims.dart';
import 'package:ai_tutor/sims/sim_host.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

/// Shows one native interactive on its own and collects what it reports.
Future<List<SimEvent>> showSim(
  WidgetTester tester,
  String simId,
  Map<String, dynamic> params, {
  String language = 'en',
}) async {
  final events = <SimEvent>[];
  final step = SimStep(
    id: 's',
    type: 'sim',
    renderer: 'native',
    simId: simId,
    params: params,
    prompt: const LocalizedText(en: 'p', ur: 'p'),
  );
  await tester.pumpWidget(
    MaterialApp(
      locale: Locale(language),
      localizationsDelegates: AppLocalizations.localizationsDelegates,
      supportedLocales: AppLocalizations.supportedLocales,
      home: Scaffold(
        body: SizedBox(
          height: 480,
          child: nativeSims[simId]!(
            SimArgs(step: step, language: language, onEvent: events.add),
          ),
        ),
      ),
    ),
  );
  await tester.pumpAndSettle();
  return events;
}

Future<void> tap(WidgetTester tester, String key, [int times = 1]) async {
  for (var i = 0; i < times; i++) {
    await tester.ensureVisible(find.byKey(Key(key)));
    await tester.tap(find.byKey(Key(key)));
    await tester.pumpAndSettle();
  }
}

Map<String, dynamic> lastResult(List<SimEvent> events) =>
    events.lastWhere((e) => e.event == 'result').data;

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

  testWidgets('fraction bars: cut into thirds and count the pieces', (
    tester,
  ) async {
    final events = await showSim(tester, 'fraction_bars', {'wholes': 2});
    await tap(tester, 'cut-plus', 2);
    expect(find.byKey(const Key('piece-1-2')), findsOneWidget);
    for (var bar = 0; bar < 2; bar++) {
      for (var piece = 0; piece < 3; piece++) {
        await tap(tester, 'piece-$bar-$piece');
      }
    }
    await tap(tester, 'piece-0-0'); // Tapping again takes it back.
    await tap(tester, 'piece-0-0');
    await tap(tester, 'sim-check');
    expect(lastResult(events), {'pieces': 6, 'cut': 3, 'total': 6});

    // Changing the cut starts the counting again.
    await tap(tester, 'cut-plus');
    await tap(tester, 'sim-check');
    expect(lastResult(events)['pieces'], 0);
  });

  testWidgets('balance scale: one side only tips it; both sides solve it', (
    tester,
  ) async {
    final events = await showSim(tester, 'balance_scale', {
      'equation': '3x + 6 = 15',
    });
    String state() =>
        tester.widget<Text>(find.byKey(const Key('scale-state'))).data!;
    expect(state(), 'Balanced');

    await tap(tester, 'left-one');
    expect(state(), 'Not balanced!');
    expect(find.byKey(const Key('scale-share')), findsNothing);
    await tap(tester, 'sim-undo');
    expect(state(), 'Balanced');

    for (var i = 0; i < 6; i++) {
      await tap(tester, 'left-one');
      await tap(tester, 'right-one');
    }
    await tap(tester, 'sim-check');
    expect(lastResult(events).containsKey('x'), isFalse);

    await tap(tester, 'scale-share');
    await tap(tester, 'sim-check');
    expect(lastResult(events), {'x': 3, 'balanced': true, 'moves': 13});
  });

  testWidgets('balance scale in Urdu fits a small screen', (tester) async {
    await showSim(tester, 'balance_scale', {
      'equation': '2x + 3 = 11',
    }, language: 'ur');
    expect(tester.takeException(), isNull);
  });

  test('balance scale reads whole-number equations only', () {
    final p = Pans.parse('2x + 3 = x + 7')!;
    expect((p.leftX, p.leftOnes, p.rightX, p.rightOnes), (2, 3, 1, 7));
    expect(Pans.parse('2x - 3 = 7'), isNull);
    expect(Pans.parse('x/2 = 3'), isNull);
    expect(Pans.parse('nonsense'), isNull);
    expect(const Pans(3, 0, 0, 9).shareBy, 3);
    expect(const Pans(3, 1, 0, 9).shareBy, isNull);
    expect(const Pans(0, 4, 1, 0).isolatedX, 4);
  });

  test('line equations read naturally', () {
    expect(lineEquation(Rational(2), Rational(1)), 'y = 2x + 1');
    expect(lineEquation(Rational(1, 2), Rational(-3)), 'y = (1/2)x - 3');
    expect(lineEquation(Rational(-1), Rational.zero), 'y = -x');
    expect(lineEquation(Rational.zero, Rational(4)), 'y = 4');
    expect(lineEquation(Rational(-2, 3), Rational(1, 2)), 'y = (-2/3)x + 1/2');
  });

  testWidgets('atom balancer: change coefficients until balanced', (
    tester,
  ) async {
    final events = await showSim(tester, 'atom_balancer', {
      'equation': 'N2 + H2 -> NH3',
    });
    expect(find.byKey(const Key('atoms-balanced')), findsNothing);
    await tap(tester, 'coef-2-plus');
    await tap(tester, 'coef-1-plus', 2);
    expect(find.byKey(const Key('atoms-balanced')), findsOneWidget);
    await tap(tester, 'sim-check');
    expect(lastResult(events), {
      'equation': 'N2 + 3H2 -> 2NH3',
      'balanced': true,
    });
  });

  testWidgets('number line: move the marker in steps', (tester) async {
    final events = await showSim(tester, 'number_line', {
      'min': 0,
      'max': 2,
      'step': 0.25,
    });
    await tap(tester, 'line-right', 7);
    expect(find.text('Your number: 7/4'), findsOneWidget);
    await tap(tester, 'line-left');
    await tap(tester, 'sim-check');
    expect(lastResult(events), {'value': '3/2'});
  });

  testWidgets('inequality line: pick a number, a dot and a direction', (
    tester,
  ) async {
    final events = await showSim(tester, 'inequality_line', {
      'min': -6,
      'max': 6,
    });
    expect(find.text('x ≥ 0'), findsOneWidget);
    await tap(tester, 'line-left', 2);
    await tester.tap(find.byIcon(Icons.circle_outlined));
    await tester.pumpAndSettle();
    await tester.tap(find.byIcon(Icons.arrow_back));
    await tester.pumpAndSettle();
    expect(find.text('x < -2'), findsOneWidget);
    await tap(tester, 'sim-check');
    expect(lastResult(events), {'inequality': 'x < -2'});
  });

  testWidgets('graph plotter: move a point and read y = mx + c', (
    tester,
  ) async {
    final events = await showSim(tester, 'graph_plotter', {
      'points': [
        [0, 1],
        [2, 2],
      ],
    });
    expect(find.text('y = (1/2)x + 1'), findsOneWidget);
    await tap(tester, 'point-1');
    await tap(tester, 'move-up', 2);
    await tap(tester, 'sim-check');
    expect(lastResult(events), {
      'm': '3/2',
      'c': '1',
      'equation': 'y = (3/2)x + 1',
    });
    await tap(tester, 'move-left', 2);
    await tap(tester, 'sim-check');
    expect(lastResult(events)['vertical'], isTrue);
  });

  testWidgets('a bad equation reports an error instead of crashing', (
    tester,
  ) async {
    final events = await showSim(tester, 'atom_balancer', {'equation': '??'});
    expect(events.single.event, 'error');
  });
}
