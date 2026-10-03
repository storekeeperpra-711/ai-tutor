import 'package:ai_tutor/character/mithu.dart';
import 'package:ai_tutor/character/mithu_bubble.dart';
import 'package:ai_tutor/character/mithu_controller.dart';
import 'package:ai_tutor/models/lesson_step.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

CharacterLine _line(String emotion) => CharacterLine.fromJson({
  'emotion': emotion,
  'say': {'en': 'Hello', 'ur': 'سلام'},
});

MithuMood _shown(WidgetTester tester) =>
    tester.widget<MithuView>(find.byKey(const Key('mithu'))).mood;

Widget _app(Widget child, {bool still = false}) => MaterialApp(
  home: MediaQuery(
    data: MediaQueryData(disableAnimations: still),
    child: Scaffold(body: child),
  ),
);

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
}
