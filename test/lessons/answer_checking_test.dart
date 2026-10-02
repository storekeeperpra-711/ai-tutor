import 'package:ai_tutor/l10n/app_localizations.dart';
import 'package:ai_tutor/lessons/answer_checking.dart';
import 'package:ai_tutor/models/lesson_step.dart';
import 'package:flutter/widgets.dart';
import 'package:flutter_test/flutter_test.dart';

TextCheckStep textStep(
  String checker,
  String expected, {
  List<Map<String, Object>> commonWrong = const [],
  bool requireSimplest = false,
  List<String> accept = const [],
}) {
  Map<String, String> t(String s) => {'en': s, 'ur': s};
  return TextCheckStep.fromJson({
    'id': 'q',
    'type': 'text_check',
    'prompt': t('?'),
    'checker': checker,
    'expected': expected,
    'require_simplest': requireSimplest,
    'accept': accept,
    'hint': t('hint'),
    'feedback_correct': t('yes'),
    'feedback_wrong': t('working'),
    'common_wrong': commonWrong,
  });
}

void main() {
  final en = lookupAppLocalizations(const Locale('en'));
  final ur = lookupAppLocalizations(const Locale('ur'));

  test('chemistry feedback names the element and counts', () {
    final step = textStep('chem_equation', '2H2 + O2 -> 2H2O');
    final result = checkTextStep(step, 'H2 + O2 -> H2O', en, 'en');
    expect(result.correct, isFalse);
    expect(result.countsAsAttempt, isTrue);
    expect(
      result.message,
      contains('O atoms: 2 on the left and 1 on the right'),
    );

    final urdu = checkTextStep(step, 'H2 + O2 -> H2O', ur, 'ur');
    expect(urdu.message, contains('بائیں طرف 2'));
  });

  test('an unknown element symbol does not use up an attempt', () {
    final step = textStep('chem_equation', '2Na + Cl2 -> 2NaCl');
    final result = checkTextStep(step, '2Na + Cl2 -> 2Nacl', en, 'en');
    expect(result.countsAsAttempt, isFalse);
    expect(result.message, contains('"Nacl" is not an element symbol'));
  });

  test('algebra feedback names the broken line', () {
    final step = textStep('linear_equation', '2x + 3 = 11');
    final result = checkTextStep(step, '2x = 14\nx = 7', en, 'en');
    expect(result.message, contains('Line 1'));
    expect(checkTextStep(step, '2x = 8\nx = 4', en, 'en').correct, isTrue);
    expect(checkTextStep(step, '2x = 8', en, 'en').countsAsAttempt, isFalse);
  });

  test('fraction not in lowest terms is "almost"', () {
    final step = textStep('fraction', '3/4', requireSimplest: true);
    final result = checkTextStep(step, '6/8', en, 'en');
    expect(result.correct, isFalse);
    expect(result.countsAsAttempt, isFalse);
    expect(result.message, en.fractionNotSimplest);
    expect(checkTextStep(step, '۳/۴', en, 'en').correct, isTrue);
  });

  test('a common wrong answer gets its own feedback first', () {
    final step = textStep(
      'linear_equation',
      '3x + 5 = 20',
      commonWrong: [
        {
          'answer': 'x = 25/3',
          'feedback': {'en': 'You added 5.', 'ur': 'آپ نے 5 جمع کیا۔'},
          'misconception_id': 'move_without_sign_change',
        },
      ],
    );
    final result = checkTextStep(step, 'x=25/3', en, 'en');
    expect(result.message, 'You added 5.');
    expect(result.misconceptionId, 'move_without_sign_change');
    expect(
      checkTextStep(step, 'x = 25/3', ur, 'ur').message,
      'آپ نے 5 جمع کیا۔',
    );
  });

  test('text checker ignores case and spaces and accepts alternatives', () {
    final step = textStep(
      'text',
      'Photosynthesis',
      accept: ['photo synthesis'],
    );
    expect(checkTextStep(step, ' photosynthesis ', en, 'en').correct, isTrue);
    expect(checkTextStep(step, 'PhotoSynthesis', en, 'en').correct, isTrue);
    expect(checkTextStep(step, 'respiration', en, 'en').correct, isFalse);
    expect(checkTextStep(step, '  ', en, 'en').countsAsAttempt, isFalse);
  });

  test('number step with the fraction checker', () {
    final step = NumberStep.fromJson({
      'id': 'n',
      'type': 'number',
      'prompt': {'en': '?', 'ur': '?'},
      'answer': 0.75,
      'checker': 'fraction',
      'require_simplest': true,
      'hint': {'en': 'h', 'ur': 'h'},
      'feedback_correct': {'en': 'y', 'ur': 'y'},
      'feedback_wrong': {'en': 'w', 'ur': 'w'},
    });
    expect(checkNumberStep(step, '3/4', en, 'en').correct, isTrue);
    expect(checkNumberStep(step, '6/8', en, 'en').countsAsAttempt, isFalse);
    expect(
      checkNumberStep(step, 'abc', en, 'en').message,
      en.fractionUnreadable,
    );
  });
}
