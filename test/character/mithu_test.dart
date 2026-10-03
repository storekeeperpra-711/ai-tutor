import 'package:ai_tutor/character/mithu.dart';
import 'package:ai_tutor/character/mithu_bubble.dart';
import 'package:ai_tutor/character/mithu_controller.dart';
import 'package:ai_tutor/character/voice_lines.dart';
import 'package:ai_tutor/models/lesson_step.dart';
import 'package:ai_tutor/app/preferences.dart';
import 'package:ai_tutor/app/theme/age_tier.dart';
import 'package:ai_tutor/character/narrator.dart';
import 'package:ai_tutor/l10n/app_localizations.dart';
import 'package:ai_tutor/lessons/step_context.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:shared_preferences/shared_preferences.dart';

import '../fakes.dart';

import 'package:flutter_test/flutter_test.dart';

CharacterLine _line(String emotion) => CharacterLine.fromJson({
  'emotion': emotion,
  'say': {'en': 'Hello', 'ur': 'سلام'},
});

MithuMood _shown(WidgetTester tester) =>
    tester.widget<MithuView>(find.byKey(const Key('mithu'))).mood;

Widget _app(Widget child, {bool still = false, FakeNarrator? narrator}) =>
    ProviderScope(
      overrides: [
        sharedPreferencesProvider.overrideWithValue(_prefs),
        narratorProvider.overrideWithValue(narrator ?? FakeNarrator()),
      ],
      child: MaterialApp(
        localizationsDelegates: AppLocalizations.localizationsDelegates,
        supportedLocales: AppLocalizations.supportedLocales,
        home: MediaQuery(
          data: MediaQueryData(disableAnimations: still),
          child: Scaffold(body: child),
        ),
      ),
    );

late SharedPreferences _prefs;

class _Host extends StatefulWidget {
  const _Host();
  @override
  State<_Host> createState() => _HostState();
}

class _HostState extends State<_Host> {
  MithuReaction? reaction;
  void react(MithuReaction r) => setState(() => reaction = r);
  @override
  Widget build(BuildContext context) =>
      MithuBubble(line: _line('curious'), reaction: reaction);
}

void main() {
  setUp(() async {
    SharedPreferences.setMockInitialValues({});
    _prefs = await SharedPreferences.getInstance();
  });

  test('parses lesson emotions; unknown ones are idle', () {
    expect(MithuMood.parse('curious'), MithuMood.curious);
    expect(MithuMood.parse('celebrating'), MithuMood.celebrating);
    expect(MithuMood.parse('angry'), MithuMood.idle);
    expect(MithuMood.parse(null), MithuMood.idle);
  });

  testWidgets('controller: right is happy, wrong is curious then encouraging', (
    tester,
  ) async {
    {
      final c = MithuController(mood: MithuMood.thinking);
      c.react(correct: false);
      expect(c.mood, MithuMood.curious);
      await tester.pump(MithuController.curiousFor);
      expect(c.mood, MithuMood.encouraging);
      c.react(correct: true);
      expect(c.mood, MithuMood.happy);
      c.speaking = true;
      expect(c.mood, MithuMood.talking);
      c.speaking = false;
      c.reset();
      expect(c.mood, MithuMood.thinking);
      c.dispose();
    }
  });

  testWidgets('every mood draws, moving and still', (tester) async {
    for (final still in [false, true]) {
      for (final mood in MithuMood.values) {
        await tester.pumpWidget(_app(MithuView(mood: mood), still: still));
        await tester.pump(const Duration(milliseconds: 700));
        expect(tester.takeException(), isNull);
      }
    }
    // The movement stops by itself, so the screen can settle.
    await tester.pumpAndSettle();
  });

  testWidgets('the bubble shows the lesson mood and reacts to answers', (
    tester,
  ) async {
    await tester.pumpWidget(_app(const _Host()));
    expect(_shown(tester), MithuMood.curious);
    expect(find.text('Hello'), findsOneWidget);
    expect(find.bySemanticsLabel('Mithu (curious)'), findsOneWidget);

    final host = tester.state<_HostState>(find.byType(_Host));
    host.react((correct: false, attempt: 1));
    await tester.pump();
    expect(_shown(tester), MithuMood.curious);
    await tester.pump(MithuController.curiousFor);
    expect(_shown(tester), MithuMood.encouraging);

    host.react((correct: true, attempt: 2));
    await tester.pump();
    expect(_shown(tester), MithuMood.happy);
    await tester.pumpAndSettle();
  });

  testWidgets('Mithu speaks by itself only for Nursery to Grade 2', (
    tester,
  ) async {
    Future<FakeNarrator> show(AgeTier tier) async {
      SharedPreferences.setMockInitialValues({'ageTier': tier.name});
      _prefs = await SharedPreferences.getInstance();
      final narrator = FakeNarrator();
      await tester.pumpWidget(const SizedBox());
      await tester.pumpWidget(
        _app(
          StepContext(
            lessonId: 'g0-maths-01-count',
            stepId: 's1',
            child: MithuBubble(line: _line('happy')),
          ),
          narrator: narrator,
        ),
      );
      await tester.pumpAndSettle();
      return narrator;
    }

    final early = await show(AgeTier.early);
    expect(early.said.single.fileName, 'g0-maths-01-count__s1_en.m4a');
    final older = await show(AgeTier.primary);
    expect(older.said, isEmpty);
    await tester.tap(find.byKey(const Key('mithu-listen')));
    expect(older.said.single.text, 'Hello');
  });

  test('mouth tracks round-trip and follow the recording', () {
    final track = MouthTrack.parse('0369');
    expect(track.levels, [0, 3 / 9, 6 / 9, 1]);
    expect(track.encode(), '0369');
    expect(track.at(const Duration(milliseconds: 120)), 6 / 9);
    expect(track.at(const Duration(seconds: 5)), 0);
    expect(track.length, const Duration(milliseconds: 200));
    expect(MouthTrack.levelFromDb(-60), 0);
    expect(MouthTrack.levelFromDb(0), 1);
    expect(mouthFileName('a__s1_ur.m4a'), 'a__s1_ur.mouth');
  });
}
