import 'package:ai_tutor/l10n/app_localizations.dart';
import 'package:ai_tutor/lessons/lesson_figure.dart';
import 'package:ai_tutor/lessons/step_registry.dart';
import 'package:ai_tutor/models/lesson_step.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';

const _altEn = 'A triangle and its mirror image across a dashed line.';
const _altUr = 'ایک مثلث اور ڈیش والی لکیر کے پار اس کا عکس۔';

const _figure = {
  'width': 100,
  'height': 60,
  'alt': {'en': _altEn, 'ur': _altUr},
  'items': [
    {
      'kind': 'polygon',
      'points': [
        [10, 10],
        [40, 10],
        [40, 40],
      ],
      'fill': true,
    },
    {
      'kind': 'line',
      'from': [50, 0],
      'to': [50, 60],
      'style': 'dashed',
    },
    {
      'kind': 'circle',
      'center': [70, 30],
      'radius': 10,
    },
    {
      'kind': 'arc',
      'center': [40, 10],
      'radius': 6,
      'start': 90,
      'sweep': 45,
    },
    {
      'kind': 'point',
      'at': [40, 40],
    },
    {
      'kind': 'label',
      'at': [8, 6],
      'text': 'A',
    },
  ],
};

const _text = {'en': 'Look at the picture.', 'ur': 'تصویر دیکھیں۔'};
const _feedback = {'en': 'Well done.', 'ur': 'شاباش۔'};

/// One step of each kind that shows its prompt with a figure.
Map<String, Map<String, dynamic>> _steps() => {
  'explain': {'id': 's1', 'type': 'explain', 'text': _text},
  'choice': {
    'id': 's1',
    'type': 'choice',
    'prompt': _text,
    'options': [
      {'id': 'a', 'text': _text, 'correct': true, 'feedback': _feedback},
      {'id': 'b', 'text': _text, 'correct': false, 'feedback': _feedback},
    ],
  },
  'number': {
    'id': 's1',
    'type': 'number',
    'prompt': _text,
    'answer': 2,
    'checker': 'numeric',
    'hint': _feedback,
    'feedback_correct': _feedback,
    'feedback_wrong': _feedback,
  },
  'text_check': {
    'id': 's1',
    'type': 'text_check',
    'prompt': _text,
    'checker': 'text',
    'expected': 'AB',
    'hint': _feedback,
    'feedback_correct': _feedback,
    'feedback_wrong': _feedback,
  },
  'summary': {'id': 's1', 'type': 'summary', 'text': _text},
};

Future<void> _pump(
  WidgetTester tester,
  Map<String, dynamic> json, {
  String language = 'en',
}) async {
  final step = LessonStep.fromJson(json);
  await tester.pumpWidget(
    ProviderScope(
      child: MaterialApp(
        locale: Locale(language),
        localizationsDelegates: AppLocalizations.localizationsDelegates,
        supportedLocales: AppLocalizations.supportedLocales,
        home: Scaffold(body: buildStep(step, (_) {}, lessonId: 'g6-test')),
      ),
    ),
  );
  await tester.pumpAndSettle();
}

void main() {
  test('a figure is read from the lesson JSON', () {
    final step = LessonStep.fromJson({
      ..._steps()['explain']!,
      'figure': _figure,
    });
    final figure = step.figure!;
    expect(figure.width, 100);
    expect(figure.alt.ur, _altUr);
    expect(figure.items.map((i) => i.kind), [
      'polygon',
      'line',
      'circle',
      'arc',
      'point',
      'label',
    ]);
    expect(figure.items[0].offsets, const [
      Offset(10, 10),
      Offset(40, 10),
      Offset(40, 40),
    ]);
    expect(figure.items[1].dashed, isTrue);
    expect(figure.items[3].sweep, 45);
    expect(figure.items[5].text, 'A');
    expect(LessonStep.fromJson(_steps()['explain']!).figure, isNull);
  });

  for (final MapEntry(key: type, value: json) in _steps().entries) {
    testWidgets('$type step draws its figure under the prompt', (tester) async {
      final handle = tester.ensureSemantics();
      await _pump(tester, {...json, 'figure': _figure});

      expect(find.byType(LessonFigure), findsOneWidget);
      expect(
        find.descendant(
          of: find.byType(LessonFigure),
          matching: find.byWidgetPredicate(
            (w) => w is CustomPaint && w.painter is FigurePainter,
          ),
        ),
        findsOneWidget,
      );
      expect(find.bySemanticsLabel(_altEn), findsOneWidget);
      // The figure comes after the prompt.
      expect(
        tester.getTopLeft(find.byType(LessonFigure)).dy,
        greaterThan(tester.getTopLeft(find.text(_text['en']!).first).dy),
      );
      handle.dispose();
    });

    testWidgets('$type step without a figure is unchanged', (tester) async {
      await _pump(tester, json);
      expect(find.byType(LessonFigure), findsNothing);
      expect(find.text(_text['en']!), findsWidgets);
    });
  }

  testWidgets('the alt text is in the app language', (tester) async {
    final handle = tester.ensureSemantics();
    await _pump(tester, {
      ..._steps()['explain']!,
      'figure': _figure,
    }, language: 'ur');
    expect(find.bySemanticsLabel(_altUr), findsOneWidget);
    expect(find.bySemanticsLabel(_altEn), findsNothing);
    handle.dispose();
  });

  testWidgets('a figure fits the screen width and keeps its shape', (
    tester,
  ) async {
    await _pump(tester, {..._steps()['explain']!, 'figure': _figure});
    final paint = find.descendant(
      of: find.byType(LessonFigure),
      matching: find.byType(CustomPaint),
    );
    final size = tester.getSize(paint);
    expect(size.width / size.height, closeTo(100 / 60, 0.01));
    expect(size.width, lessThanOrEqualTo(800));
  });
}
