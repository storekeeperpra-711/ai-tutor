import 'package:json_annotation/json_annotation.dart';

import 'localized_text.dart';

part 'lesson_step.g.dart';

/// One step of a lesson. The `type` field in the JSON decides which
/// subclass is created. Types the app can't play yet become
/// [UnsupportedStep], so a lesson never fails to load because of them.
sealed class LessonStep {
  const LessonStep({required this.id, required this.type});

  factory LessonStep.fromJson(Map<String, dynamic> json) =>
      switch (json['type']) {
        'explain' => ExplainStep.fromJson(json),
        'choice' => ChoiceStep.fromJson(json),
        'number' => NumberStep.fromJson(json),
        'summary' => SummaryStep.fromJson(json),
        _ => UnsupportedStep(
          id: json['id'] as String,
          type: json['type'] as String,
        ),
      };

  final String id;
  final String type;
}

/// What Mithu says (and how Mithu looks) at a step.
@JsonSerializable()
class CharacterLine {
  const CharacterLine({required this.emotion, required this.say, this.audio});

  factory CharacterLine.fromJson(Map<String, dynamic> json) =>
      _$CharacterLineFromJson(json);

  final String emotion;
  final LocalizedText say;

  /// Audio file names per language, e.g. {"ur": "s3_ur.mp3"} (Phase 7).
  final Map<String, String>? audio;
}

@JsonSerializable()
class ExplainStep extends LessonStep {
  const ExplainStep({
    required super.id,
    required super.type,
    required this.text,
    this.character,
    this.image,
  });

  factory ExplainStep.fromJson(Map<String, dynamic> json) =>
      _$ExplainStepFromJson(json);

  final LocalizedText text;
  final CharacterLine? character;
  final String? image;
}

@JsonSerializable()
class ChoiceStep extends LessonStep {
  const ChoiceStep({
    required super.id,
    required super.type,
    required this.prompt,
    required this.options,
    this.character,
  });

  factory ChoiceStep.fromJson(Map<String, dynamic> json) =>
      _$ChoiceStepFromJson(json);

  final LocalizedText prompt;
  final List<ChoiceOption> options;
  final CharacterLine? character;
}

@JsonSerializable()
class ChoiceOption {
  const ChoiceOption({
    required this.id,
    required this.text,
    required this.correct,
    required this.feedback,
    this.misconceptionId,
  });

  factory ChoiceOption.fromJson(Map<String, dynamic> json) =>
      _$ChoiceOptionFromJson(json);

  final String id;
  final LocalizedText text;
  final bool correct;

  /// Shown after this option is picked. Every option has its own feedback.
  final LocalizedText feedback;
  final String? misconceptionId;
}

@JsonSerializable()
class NumberStep extends LessonStep {
  const NumberStep({
    required super.id,
    required super.type,
    required this.prompt,
    required this.answer,
    required this.checker,
    required this.hint,
    required this.feedbackCorrect,
    required this.feedbackWrong,
    this.tolerance = 0,
    this.unit,
    this.maxAttempts = 3,
    this.commonWrong = const [],
    this.character,
  });

  factory NumberStep.fromJson(Map<String, dynamic> json) =>
      _$NumberStepFromJson(json);

  final LocalizedText prompt;
  final double answer;
  final double tolerance;
  final LocalizedText? unit;
  final String checker;

  /// Shown after the first wrong answer.
  final LocalizedText hint;
  final LocalizedText feedbackCorrect;

  /// Shown after the last attempt, with the full working.
  final LocalizedText feedbackWrong;
  final int maxAttempts;
  final List<CommonWrong> commonWrong;
  final CharacterLine? character;
}

/// A wrong answer students often give, with feedback for that exact mistake.
@JsonSerializable()
class CommonWrong {
  const CommonWrong({
    required this.answer,
    required this.feedback,
    this.misconceptionId,
  });

  factory CommonWrong.fromJson(Map<String, dynamic> json) =>
      _$CommonWrongFromJson(json);

  final double answer;
  final LocalizedText feedback;
  final String? misconceptionId;
}

@JsonSerializable()
class SummaryStep extends LessonStep {
  const SummaryStep({
    required super.id,
    required super.type,
    required this.text,
    this.points = const [],
    this.character,
  });

  factory SummaryStep.fromJson(Map<String, dynamic> json) =>
      _$SummaryStepFromJson(json);

  final LocalizedText text;
  final List<LocalizedText> points;
  final CharacterLine? character;
}

/// A step type that is valid in the schema but not playable yet
/// (text_check, sim, video, lottie, ai_explain, photo_check).
class UnsupportedStep extends LessonStep {
  const UnsupportedStep({required super.id, required super.type});
}
