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
        questionType: $checkedConvert('question_type', (v) => v as String?),
        skill: $checkedConvert('skill', (v) => v as String?),
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
    }, fieldKeyMap: const {'questionType': 'question_type'});

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
      questionType: $checkedConvert('question_type', (v) => v as String?),
      skill: $checkedConvert('skill', (v) => v as String?),
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
      requireSimplest: $checkedConvert(
        'require_simplest',
        (v) => v as bool? ?? false,
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
    'questionType': 'question_type',
    'feedbackCorrect': 'feedback_correct',
    'feedbackWrong': 'feedback_wrong',
    'requireSimplest': 'require_simplest',
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

TextCheckStep _$TextCheckStepFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'TextCheckStep',
      json,
      ($checkedConvert) {
        final val = TextCheckStep(
          id: $checkedConvert('id', (v) => v as String),
          type: $checkedConvert('type', (v) => v as String),
          questionType: $checkedConvert('question_type', (v) => v as String?),
          skill: $checkedConvert('skill', (v) => v as String?),
          prompt: $checkedConvert(
            'prompt',
            (v) => LocalizedText.fromJson(v as Map<String, dynamic>),
          ),
          checker: $checkedConvert('checker', (v) => v as String),
          expected: $checkedConvert('expected', (v) => v as String),
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
          accept: $checkedConvert(
            'accept',
            (v) =>
                (v as List<dynamic>?)?.map((e) => e as String).toList() ??
                const [],
          ),
          variable: $checkedConvert('variable', (v) => v as String? ?? 'x'),
          requireSimplest: $checkedConvert(
            'require_simplest',
            (v) => v as bool? ?? false,
          ),
          multiline: $checkedConvert('multiline', (v) => v as bool? ?? false),
          maxAttempts: $checkedConvert(
            'max_attempts',
            (v) => (v as num?)?.toInt() ?? 3,
          ),
          commonWrong: $checkedConvert(
            'common_wrong',
            (v) =>
                (v as List<dynamic>?)
                    ?.map(
                      (e) =>
                          CommonWrongText.fromJson(e as Map<String, dynamic>),
                    )
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
        'questionType': 'question_type',
        'feedbackCorrect': 'feedback_correct',
        'feedbackWrong': 'feedback_wrong',
        'requireSimplest': 'require_simplest',
        'maxAttempts': 'max_attempts',
        'commonWrong': 'common_wrong',
      },
    );

CommonWrongText _$CommonWrongTextFromJson(Map<String, dynamic> json) =>
    $checkedCreate('CommonWrongText', json, ($checkedConvert) {
      final val = CommonWrongText(
        answer: $checkedConvert('answer', (v) => v as String),
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

SimStep _$SimStepFromJson(Map<String, dynamic> json) => $checkedCreate(
  'SimStep',
  json,
  ($checkedConvert) {
    final val = SimStep(
      id: $checkedConvert('id', (v) => v as String),
      type: $checkedConvert('type', (v) => v as String),
      questionType: $checkedConvert('question_type', (v) => v as String?),
      skill: $checkedConvert('skill', (v) => v as String?),
      prompt: $checkedConvert(
        'prompt',
        (v) => LocalizedText.fromJson(v as Map<String, dynamic>),
      ),
      renderer: $checkedConvert('renderer', (v) => v as String),
      src: $checkedConvert('src', (v) => v as String?),
      simId: $checkedConvert('sim_id', (v) => v as String?),
      params: $checkedConvert(
        'params',
        (v) => v as Map<String, dynamic>? ?? const {},
      ),
      expected: $checkedConvert(
        'expected',
        (v) =>
            v == null ? null : SimExpected.fromJson(v as Map<String, dynamic>),
      ),
      hint: $checkedConvert(
        'hint',
        (v) => v == null
            ? null
            : LocalizedText.fromJson(v as Map<String, dynamic>),
      ),
      feedbackCorrect: $checkedConvert(
        'feedback_correct',
        (v) => v == null
            ? null
            : LocalizedText.fromJson(v as Map<String, dynamic>),
      ),
      feedbackWrong: $checkedConvert(
        'feedback_wrong',
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
                ?.map(
                  (e) => CommonWrongText.fromJson(e as Map<String, dynamic>),
                )
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
    'questionType': 'question_type',
    'simId': 'sim_id',
    'feedbackCorrect': 'feedback_correct',
    'feedbackWrong': 'feedback_wrong',
    'maxAttempts': 'max_attempts',
    'commonWrong': 'common_wrong',
  },
);

SimExpected _$SimExpectedFromJson(Map<String, dynamic> json) =>
    $checkedCreate('SimExpected', json, ($checkedConvert) {
      final val = SimExpected(
        result: $checkedConvert('result', (v) => v as String),
        checker: $checkedConvert('checker', (v) => v as String),
        answer: $checkedConvert('answer', (v) => v as String),
        tolerance: $checkedConvert(
          'tolerance',
          (v) => (v as num?)?.toDouble() ?? 0,
        ),
      );
      return val;
    });

VideoStep _$VideoStepFromJson(
  Map<String, dynamic> json,
) => $checkedCreate('VideoStep', json, ($checkedConvert) {
  final val = VideoStep(
    id: $checkedConvert('id', (v) => v as String),
    type: $checkedConvert('type', (v) => v as String),
    src: $checkedConvert(
      'src',
      (v) => LocalizedText.fromJson(v as Map<String, dynamic>),
    ),
    summary: $checkedConvert(
      'summary',
      (v) => LocalizedText.fromJson(v as Map<String, dynamic>),
    ),
    title: $checkedConvert(
      'title',
      (v) =>
          v == null ? null : LocalizedText.fromJson(v as Map<String, dynamic>),
    ),
    captions: $checkedConvert(
      'captions',
      (v) =>
          v == null ? null : LocalizedText.fromJson(v as Map<String, dynamic>),
    ),
    durationSeconds: $checkedConvert(
      'duration_seconds',
      (v) => (v as num?)?.toDouble(),
    ),
    character: $checkedConvert(
      'character',
      (v) =>
          v == null ? null : CharacterLine.fromJson(v as Map<String, dynamic>),
    ),
  );
  return val;
}, fieldKeyMap: const {'durationSeconds': 'duration_seconds'});

LottieStep _$LottieStepFromJson(
  Map<String, dynamic> json,
) => $checkedCreate('LottieStep', json, ($checkedConvert) {
  final val = LottieStep(
    id: $checkedConvert('id', (v) => v as String),
    type: $checkedConvert('type', (v) => v as String),
    src: $checkedConvert('src', (v) => v as String),
    text: $checkedConvert(
      'text',
      (v) =>
          v == null ? null : LocalizedText.fromJson(v as Map<String, dynamic>),
    ),
    loop: $checkedConvert('loop', (v) => v as bool? ?? false),
    character: $checkedConvert(
      'character',
      (v) =>
          v == null ? null : CharacterLine.fromJson(v as Map<String, dynamic>),
    ),
  );
  return val;
});

AiExplainStep _$AiExplainStepFromJson(
  Map<String, dynamic> json,
) => $checkedCreate(
  'AiExplainStep',
  json,
  ($checkedConvert) {
    final val = AiExplainStep(
      id: $checkedConvert('id', (v) => v as String),
      type: $checkedConvert('type', (v) => v as String),
      questionType: $checkedConvert('question_type', (v) => v as String?),
      skill: $checkedConvert('skill', (v) => v as String?),
      task: $checkedConvert(
        'task',
        (v) => LocalizedText.fromJson(v as Map<String, dynamic>),
      ),
      keywords: $checkedConvert(
        'keywords',
        (v) => (v as List<dynamic>)
            .map((e) => (e as List<dynamic>).map((e) => e as String).toList())
            .toList(),
      ),
      fallbackFeedback: $checkedConvert(
        'fallback_feedback',
        (v) => FeedbackLevels.fromJson(v as Map<String, dynamic>),
      ),
      taskKind: $checkedConvert('task_kind', (v) => v as String? ?? 'explain'),
      limitPerDay: $checkedConvert(
        'limit_per_day',
        (v) => (v as num?)?.toInt() ?? 3,
      ),
      maxAttempts: $checkedConvert(
        'max_attempts',
        (v) => (v as num?)?.toInt() ?? 2,
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
    'questionType': 'question_type',
    'fallbackFeedback': 'fallback_feedback',
    'taskKind': 'task_kind',
    'limitPerDay': 'limit_per_day',
    'maxAttempts': 'max_attempts',
  },
);

FeedbackLevels _$FeedbackLevelsFromJson(Map<String, dynamic> json) =>
    $checkedCreate('FeedbackLevels', json, ($checkedConvert) {
      final val = FeedbackLevels(
        gotIt: $checkedConvert(
          'got_it',
          (v) => LocalizedText.fromJson(v as Map<String, dynamic>),
        ),
        partly: $checkedConvert(
          'partly',
          (v) => LocalizedText.fromJson(v as Map<String, dynamic>),
        ),
        notYet: $checkedConvert(
          'not_yet',
          (v) => LocalizedText.fromJson(v as Map<String, dynamic>),
        ),
      );
      return val;
    }, fieldKeyMap: const {'gotIt': 'got_it', 'notYet': 'not_yet'});

PhotoCheckStep _$PhotoCheckStepFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'PhotoCheckStep',
      json,
      ($checkedConvert) {
        final val = PhotoCheckStep(
          id: $checkedConvert('id', (v) => v as String),
          type: $checkedConvert('type', (v) => v as String),
          questionType: $checkedConvert('question_type', (v) => v as String?),
          skill: $checkedConvert('skill', (v) => v as String?),
          problem: $checkedConvert(
            'problem',
            (v) => LocalizedText.fromJson(v as Map<String, dynamic>),
          ),
          checker: $checkedConvert('checker', (v) => v as String),
          expected: $checkedConvert('expected', (v) => v as String),
          hint: $checkedConvert(
            'hint',
            (v) => LocalizedText.fromJson(v as Map<String, dynamic>),
          ),
          feedbackCorrect: $checkedConvert(
            'feedback_correct',
            (v) => LocalizedText.fromJson(v as Map<String, dynamic>),
          ),
          correctWorking: $checkedConvert(
            'correct_working',
            (v) => LocalizedText.fromJson(v as Map<String, dynamic>),
          ),
          variable: $checkedConvert('variable', (v) => v as String? ?? 'x'),
          tolerance: $checkedConvert(
            'tolerance',
            (v) => (v as num?)?.toDouble() ?? 0,
          ),
          requireSimplest: $checkedConvert(
            'require_simplest',
            (v) => v as bool? ?? false,
          ),
          commonWrong: $checkedConvert(
            'common_wrong',
            (v) =>
                (v as List<dynamic>?)
                    ?.map(
                      (e) =>
                          CommonWrongText.fromJson(e as Map<String, dynamic>),
                    )
                    .toList() ??
                const [],
          ),
          limitPerDay: $checkedConvert(
            'limit_per_day',
            (v) => (v as num?)?.toInt() ?? 2,
          ),
          maxAttempts: $checkedConvert(
            'max_attempts',
            (v) => (v as num?)?.toInt() ?? 3,
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
        'questionType': 'question_type',
        'feedbackCorrect': 'feedback_correct',
        'correctWorking': 'correct_working',
        'requireSimplest': 'require_simplest',
        'commonWrong': 'common_wrong',
        'limitPerDay': 'limit_per_day',
        'maxAttempts': 'max_attempts',
      },
    );
