// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'lesson_step.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

CharacterLine _$CharacterLineFromJson(Map<String, dynamic> json) =>
    $checkedCreate('CharacterLine', json, ($checkedConvert) {
      final val = CharacterLine(
        emotion: $checkedConvert('emotion', (v) => v as String),
        say: $checkedConvert(
          'say',
          (v) => LocalizedText.fromJson(v as Map<String, dynamic>),
        ),
        audio: $checkedConvert(
          'audio',
          (v) => (v as Map<String, dynamic>?)?.map(
            (k, e) => MapEntry(k, e as String),
          ),
        ),
      );
      return val;
    });

ExplainStep _$ExplainStepFromJson(Map<String, dynamic> json) =>
    $checkedCreate('ExplainStep', json, ($checkedConvert) {
      final val = ExplainStep(
        id: $checkedConvert('id', (v) => v as String),
        type: $checkedConvert('type', (v) => v as String),
        text: $checkedConvert(
          'text',
          (v) => LocalizedText.fromJson(v as Map<String, dynamic>),
        ),
        character: $checkedConvert(
          'character',
          (v) => v == null
              ? null
              : CharacterLine.fromJson(v as Map<String, dynamic>),
        ),
        image: $checkedConvert('image', (v) => v as String?),
      );
      return val;
    });

ChoiceStep _$ChoiceStepFromJson(Map<String, dynamic> json) =>
    $checkedCreate('ChoiceStep', json, ($checkedConvert) {
      final val = ChoiceStep(
        id: $checkedConvert('id', (v) => v as String),
        type: $checkedConvert('type', (v) => v as String),
        prompt: $checkedConvert(
          'prompt',
          (v) => LocalizedText.fromJson(v as Map<String, dynamic>),
        ),
        options: $checkedConvert(
          'options',
          (v) => (v as List<dynamic>)
              .map((e) => ChoiceOption.fromJson(e as Map<String, dynamic>))
              .toList(),
        ),
        character: $checkedConvert(
          'character',
          (v) => v == null
              ? null
              : CharacterLine.fromJson(v as Map<String, dynamic>),
        ),
      );
      return val;
    });

ChoiceOption _$ChoiceOptionFromJson(Map<String, dynamic> json) =>
    $checkedCreate('ChoiceOption', json, ($checkedConvert) {
      final val = ChoiceOption(
        id: $checkedConvert('id', (v) => v as String),
        text: $checkedConvert(
          'text',
          (v) => LocalizedText.fromJson(v as Map<String, dynamic>),
        ),
        correct: $checkedConvert('correct', (v) => v as bool),
        feedback: $checkedConvert(
          'feedback',
          (v) => LocalizedText.fromJson(v as Map<String, dynamic>),
        ),
        misconceptionId: $checkedConvert(
          'misconception_id',
          (v) => v as String?,
        ),
      );
      return val;
    }, fieldKeyMap: const {'misconceptionId': 'misconception_id'});

NumberStep _$NumberStepFromJson(Map<String, dynamic> json) => $checkedCreate(
  'NumberStep',
  json,
  ($checkedConvert) {
    final val = NumberStep(
      id: $checkedConvert('id', (v) => v as String),
      type: $checkedConvert('type', (v) => v as String),
      prompt: $checkedConvert(
        'prompt',
        (v) => LocalizedText.fromJson(v as Map<String, dynamic>),
      ),
      answer: $checkedConvert('answer', (v) => (v as num).toDouble()),
      checker: $checkedConvert('checker', (v) => v as String),
      hint: $checkedConvert(
        'hint',
        (v) => LocalizedText.fromJson(v as Map<String, dynamic>),
      ),
      feedbackCorrect: $checkedConvert(
        'feedback_correct',
        (v) => LocalizedText.fromJson(v as Map<String, dynamic>),
      ),
      feedbackWrong: $checkedConvert(
        'feedback_wrong',
        (v) => LocalizedText.fromJson(v as Map<String, dynamic>),
      ),
      tolerance: $checkedConvert(
        'tolerance',
        (v) => (v as num?)?.toDouble() ?? 0,
      ),
      unit: $checkedConvert(
        'unit',
        (v) => v == null
            ? null
            : LocalizedText.fromJson(v as Map<String, dynamic>),
      ),
      maxAttempts: $checkedConvert(
        'max_attempts',
        (v) => (v as num?)?.toInt() ?? 3,
      ),
      commonWrong: $checkedConvert(
        'common_wrong',
        (v) =>
            (v as List<dynamic>?)
                ?.map((e) => CommonWrong.fromJson(e as Map<String, dynamic>))
                .toList() ??
            const [],
      ),
      character: $checkedConvert(
        'character',
        (v) => v == null
            ? null
            : CharacterLine.fromJson(v as Map<String, dynamic>),
      ),
    );
    return val;
  },
  fieldKeyMap: const {
    'feedbackCorrect': 'feedback_correct',
    'feedbackWrong': 'feedback_wrong',
    'maxAttempts': 'max_attempts',
    'commonWrong': 'common_wrong',
  },
);

CommonWrong _$CommonWrongFromJson(Map<String, dynamic> json) => $checkedCreate(
  'CommonWrong',
  json,
  ($checkedConvert) {
    final val = CommonWrong(
      answer: $checkedConvert('answer', (v) => (v as num).toDouble()),
      feedback: $checkedConvert(
        'feedback',
        (v) => LocalizedText.fromJson(v as Map<String, dynamic>),
      ),
      misconceptionId: $checkedConvert('misconception_id', (v) => v as String?),
    );
    return val;
  },
  fieldKeyMap: const {'misconceptionId': 'misconception_id'},
);

SummaryStep _$SummaryStepFromJson(
  Map<String, dynamic> json,
) => $checkedCreate('SummaryStep', json, ($checkedConvert) {
  final val = SummaryStep(
    id: $checkedConvert('id', (v) => v as String),
    type: $checkedConvert('type', (v) => v as String),
    text: $checkedConvert(
      'text',
      (v) => LocalizedText.fromJson(v as Map<String, dynamic>),
    ),
    points: $checkedConvert(
      'points',
      (v) =>
          (v as List<dynamic>?)
              ?.map((e) => LocalizedText.fromJson(e as Map<String, dynamic>))
              .toList() ??
          const [],
    ),
    character: $checkedConvert(
      'character',
      (v) =>
          v == null ? null : CharacterLine.fromJson(v as Map<String, dynamic>),
    ),
  );
  return val;
});
