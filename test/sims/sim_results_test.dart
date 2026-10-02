import 'package:ai_tutor/l10n/app_localizations.dart';
import 'package:ai_tutor/lessons/answer_checking.dart';
import 'package:ai_tutor/models/lesson_step.dart';
import 'package:ai_tutor/sims/web_sim_view.dart';
import 'package:flutter/widgets.dart';
import 'package:flutter_test/flutter_test.dart';

SimStep simStep(String result, String checker, String answer) {
  Map<String, String> t(String s) => {'en': s, 'ur': s};
  return SimStep.fromJson({
    'id': 's',
    'type': 'sim',
    'renderer': 'native',
    'sim_id': 'fraction_bars',
    'prompt': t('?'),
    'expected': {'result': result, 'checker': checker, 'answer': answer},
    'hint': t('hint'),
    'feedback_correct': t('yes'),
    'feedback_wrong': t('working'),
    'common_wrong': [
      {
        'answer': '1.5',
        'misconception_id': 'division_makes_smaller',
        'feedback': t('smaller?'),
      },
    ],
  });
}

void main() {
  final en = lookupAppLocalizations(const Locale('en'));

  group('simulation results go through the same checkers', () {
    test('numeric, with a known mistake', () {
      final step = simStep('children', 'numeric', '6');
      expect(checkSimResult(step, {'children': 6}, en, 'en').correct, isTrue);
      expect(checkSimResult(step, {'children': 6.0}, en, 'en').correct, isTrue);
      final wrong = checkSimResult(step, {'children': 1.5}, en, 'en');
      expect(wrong.correct, isFalse);
      expect(wrong.message, 'smaller?');
      expect(wrong.misconceptionId, 'division_makes_smaller');
    });

    test('fractions reported as text', () {
      final step = simStep('value', 'fraction', '7/4');
      expect(checkSimResult(step, {'value': '7/4'}, en, 'en').correct, isTrue);
      expect(checkSimResult(step, {'value': 1.75}, en, 'en').correct, isTrue);
      expect(checkSimResult(step, {'value': '3/2'}, en, 'en').correct, isFalse);
    });

    test('chemical equations name what is unbalanced', () {
      final step = simStep('equation', 'chem_equation', 'N2 + 3H2 -> 2NH3');
      expect(
        checkSimResult(
          step,
          {'equation': 'N2 + 3H2 -> 2NH3'},
          en,
          'en',
        ).correct,
        isTrue,
      );
      final wrong = checkSimResult(
        step,
        {'equation': 'N2 + H2 -> 2NH3'},
        en,
        'en',
      );
      expect(wrong.correct, isFalse);
      expect(wrong.message, contains('H'));
    });

    test('a missing value is not counted as an attempt', () {
      final step = simStep('x', 'numeric', '3');
      final result = checkSimResult(step, {'balanced': true}, en, 'en');
      expect(result.countsAsAttempt, isFalse);
      expect(result.message, en.simNoResult);
    });
  });

  group('WebView protocol', () {
    test('only the simulation file itself may load', () {
      const asset = 'assets/sims/roti_strips.html';
      expect(
        isSimUrl(
          'file:///android_asset/flutter_assets/assets/sims/roti_strips.html',
          asset,
        ),
        isTrue,
      );
      expect(isSimUrl('https://example.com/', asset), isFalse);
      expect(
        isSimUrl(
          'file:///android_asset/flutter_assets/assets/sims/other.html',
          asset,
        ),
        isFalse,
      );
      expect(
        isSimUrl(
          'file:///android_asset/flutter_assets/assets/sims/roti_strips.html?x=1',
          asset,
        ),
        isFalse,
      );
    });

    test('TutorBridge messages are read safely', () {
      final e = parseSimMessage('{"event":"result","data":{"children":8}}')!;
      expect(e.event, 'result');
      expect(e.data, {'children': 8});
      expect(parseSimMessage('{"event":"ready"}')!.data, isEmpty);
      expect(parseSimMessage('not json'), isNull);
      expect(parseSimMessage('[1,2]'), isNull);
      expect(parseSimMessage('{"event":3}'), isNull);
      expect(parseSimMessage('{"event":"result","data":[1]}'), isNull);
    });
  });
}
