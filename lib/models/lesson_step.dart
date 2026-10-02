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
        'text_check' => TextCheckStep.fromJson(json),
        'summary' => SummaryStep.fromJson(json),
        'sim' => SimStep.fromJson(json),
        'video' => VideoStep.fromJson(json),
        'lottie' => LottieStep.fromJson(json),
        _ => UnsupportedStep(
          id: json['id'] as String,
          type: json['type'] as String,
        ),
      };

  final String id;
  final String type;
}

/// A step that asks a question. With a [questionType], its answers count
/// as mastery evidence (Phase 4).
abstract interface class QuestionStep {
  String get id;

  /// recall, explain, apply, find_error or exam_style; null = practice only.
  String? get questionType;

  /// The skill tested; null = the lesson's first skill.
  String? get skill;
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
class ChoiceStep extends LessonStep implements QuestionStep {
  const ChoiceStep({
    required super.id,
    required super.type,
    this.questionType,
    this.skill,
    required this.prompt,
    required this.options,
    this.character,
  });

  factory ChoiceStep.fromJson(Map<String, dynamic> json) =>
      _$ChoiceStepFromJson(json);

  @override
  final String? questionType;
  @override
  final String? skill;

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
class NumberStep extends LessonStep implements QuestionStep {
  const NumberStep({
    required super.id,
    required super.type,
    this.questionType,
    this.skill,
    required this.prompt,
    required this.answer,
    required this.checker,
    required this.hint,
    required this.feedbackCorrect,
    required this.feedbackWrong,
    this.tolerance = 0,
    this.requireSimplest = false,
    this.unit,
    this.maxAttempts = 3,
    this.commonWrong = const [],
    this.character,
  });

  factory NumberStep.fromJson(Map<String, dynamic> json) =>
      _$NumberStepFromJson(json);

  @override
  final String? questionType;
  @override
  final String? skill;

  final LocalizedText prompt;
  final double answer;
  final double tolerance;
  final LocalizedText? unit;

  /// `numeric` or `fraction`.
  final String checker;

  /// Fraction checker: a right value not in lowest terms gets its own feedback.
  final bool requireSimplest;

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

/// The student types text (or several lines of working) and a checker
/// decides: `fraction`, `chem_equation`, `linear_equation` or `text`.
@JsonSerializable()
class TextCheckStep extends LessonStep implements QuestionStep {
  const TextCheckStep({
    required super.id,
    required super.type,
    this.questionType,
    this.skill,
    required this.prompt,
    required this.checker,
    required this.expected,
    required this.hint,
    required this.feedbackCorrect,
    required this.feedbackWrong,
    this.accept = const [],
    this.variable = 'x',
    this.requireSimplest = false,
    this.multiline = false,
    this.maxAttempts = 3,
    this.commonWrong = const [],
    this.character,
  });

  factory TextCheckStep.fromJson(Map<String, dynamic> json) =>
      _$TextCheckStepFromJson(json);

  @override
  final String? questionType;
  @override
  final String? skill;

  final LocalizedText prompt;
  final String checker;

  /// What `expected` means depends on the checker; see the lesson schema.
  final String expected;
  final List<String> accept;
  final String variable;
  final bool requireSimplest;
  final bool multiline;
  final LocalizedText hint;
  final LocalizedText feedbackCorrect;
  final LocalizedText feedbackWrong;
  final int maxAttempts;
  final List<CommonWrongText> commonWrong;
  final CharacterLine? character;
}

/// A typed wrong answer students often give, with feedback for it.
@JsonSerializable()
class CommonWrongText {
  const CommonWrongText({
    required this.answer,
    required this.feedback,
    this.misconceptionId,
  });

  factory CommonWrongText.fromJson(Map<String, dynamic> json) =>
      _$CommonWrongTextFromJson(json);

  final String answer;
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

/// A simulation (HTML in a WebView, or a native interactive) and,
/// optionally, a question about its result (Phase 5).
@JsonSerializable()
class SimStep extends LessonStep implements QuestionStep {
  const SimStep({
    required super.id,
    required super.type,
    this.questionType,
    this.skill,
    required this.prompt,
    required this.renderer,
    this.src,
    this.simId,
    this.params = const {},
    this.expected,
    this.hint,
    this.feedbackCorrect,
    this.feedbackWrong,
    this.maxAttempts = 3,
    this.commonWrong = const [],
    this.character,
  });

  factory SimStep.fromJson(Map<String, dynamic> json) =>
      _$SimStepFromJson(json);

  @override
  final String? questionType;
  @override
  final String? skill;

  final LocalizedText prompt;

  /// webview or native.
  final String renderer;

  /// webview: file name in assets/sims/.
  final String? src;

  /// native: which interactive, e.g. fraction_bars.
  final String? simId;
  final Map<String, dynamic> params;

  /// What to check in the result; null = explore only.
  final SimExpected? expected;
  final LocalizedText? hint;
  final LocalizedText? feedbackCorrect;
  final LocalizedText? feedbackWrong;
  final int maxAttempts;
  final List<CommonWrongText> commonWrong;
  final CharacterLine? character;

  bool get isWebView => renderer == 'webview';
}

/// Which value of a simulation's result is the answer, and its checker.
@JsonSerializable()
class SimExpected {
  const SimExpected({
    required this.result,
    required this.checker,
    required this.answer,
    this.tolerance = 0,
  });

  factory SimExpected.fromJson(Map<String, dynamic> json) =>
      _$SimExpectedFromJson(json);

  /// Key in the result data, e.g. `pieces`.
  final String result;

  /// numeric, fraction, chem_equation or text.
  final String checker;
  final String answer;
  final double tolerance;
}

/// A short explainer video, one file per language, with captions.
@JsonSerializable()
class VideoStep extends LessonStep {
  const VideoStep({
    required super.id,
    required super.type,
    required this.src,
    required this.summary,
    this.title,
    this.captions,
    this.durationSeconds,
    this.character,
  });

  factory VideoStep.fromJson(Map<String, dynamic> json) =>
      _$VideoStepFromJson(json);

  /// Per language: a file in assets/videos/ or an https link.
  final LocalizedText src;
  final LocalizedText? captions;

  /// Shown when the video can't play, so the lesson can go on.
  final LocalizedText summary;
  final LocalizedText? title;
  final double? durationSeconds;
  final CharacterLine? character;
}

/// A small animation (assets/lottie/), with an optional line of text.
@JsonSerializable()
class LottieStep extends LessonStep {
  const LottieStep({
    required super.id,
    required super.type,
    required this.src,
    this.text,
    this.loop = false,
    this.character,
  });

  factory LottieStep.fromJson(Map<String, dynamic> json) =>
      _$LottieStepFromJson(json);

  final String src;
  final LocalizedText? text;
  final bool loop;
  final CharacterLine? character;
}

/// A step type that is valid in the schema but not playable yet
/// (ai_explain, photo_check).
class UnsupportedStep extends LessonStep {
  const UnsupportedStep({required super.id, required super.type});
}
