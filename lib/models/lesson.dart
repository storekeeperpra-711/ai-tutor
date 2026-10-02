import 'package:json_annotation/json_annotation.dart';

import 'lesson_step.dart';
import 'localized_text.dart';

part 'lesson.g.dart';

/// One lesson, read from a JSON file in content/lessons/.
/// The format is defined in content/schema/lesson.schema.json.
@JsonSerializable()
class Lesson {
  const Lesson({
    required this.id,
    required this.version,
    required this.schema,
    required this.subject,
    required this.grade,
    required this.tier,
    required this.curriculumRefs,
    required this.skills,
    required this.title,
    required this.estimatedMinutes,
    required this.prerequisites,
    required this.misconceptions,
    required this.glossary,
    required this.steps,
    required this.review,
    this.flashcards = const [],
    this.homeTasks = const [],
    this.teacherNotes = const [],
    this.masteryCriteria = const {},
    this.questionBank = const {},
    this.alternatives = const [],
    this.reviewQuestions = const [],
  });

  factory Lesson.fromJson(Map<String, dynamic> json) => _$LessonFromJson(json);

  final String id;
  final int version;
  final String schema;
  final String subject;
  final int grade;
  final String tier;
  final List<CurriculumRef> curriculumRefs;
  final List<String> skills;
  final LocalizedText title;
  final int estimatedMinutes;
  final List<Prerequisite> prerequisites;
  final List<Misconception> misconceptions;
  final List<GlossaryEntry> glossary;
  @JsonKey(fromJson: _stepsFromJson)
  final List<LessonStep> steps;
  final Review review;
  final List<Flashcard> flashcards;
  final List<HomeTask> homeTasks;
  final List<String> teacherNotes;

  /// Per skill: what a student must show to reach Mastered.
  final Map<String, MasteryCriteria> masteryCriteria;

  /// Per skill: practice questions, tagged by type.
  final Map<String, List<Question>> questionBank;

  /// Other explanations for when a student is stuck.
  final List<Alternative> alternatives;

  /// Questions for spaced review.
  final List<Question> reviewQuestions;

  /// The skill a step or question tests when it doesn't name one.
  String get mainSkill => skills.first;
}

@JsonSerializable()
class MasteryCriteria {
  const MasteryCriteria({required this.questionTypes, required this.days});

  factory MasteryCriteria.fromJson(Map<String, dynamic> json) =>
      _$MasteryCriteriaFromJson(json);

  /// recall, explain, apply, find_error, exam_style.
  final List<String> questionTypes;

  /// Correct answers needed on this many different days.
  final int days;
}

/// A question outside the lesson's main steps (question bank, review).
@JsonSerializable()
class Question {
  const Question({
    required this.id,
    required this.type,
    required this.step,
    this.skill,
  });

  factory Question.fromJson(Map<String, dynamic> json) =>
      _$QuestionFromJson(json);

  final String id;

  /// recall, explain, apply, find_error or exam_style.
  final String type;
  final String? skill;
  final LessonStep step;
}

@JsonSerializable()
class Alternative {
  const Alternative({
    required this.id,
    required this.description,
    required this.steps,
    this.forStep,
  });

  factory Alternative.fromJson(Map<String, dynamic> json) =>
      _$AlternativeFromJson(json);

  final String id;

  /// The step this explains another way.
  final String? forStep;

  /// For teachers.
  final String description;
  @JsonKey(fromJson: _stepsFromJson)
  final List<LessonStep> steps;
}

List<LessonStep> _stepsFromJson(List<dynamic> json) => json
    .map((s) => LessonStep.fromJson(s as Map<String, dynamic>))
    .toList(growable: false);

@JsonSerializable()
class CurriculumRef {
  const CurriculumRef({required this.outcome, this.code, this.textbook});

  factory CurriculumRef.fromJson(Map<String, dynamic> json) =>
      _$CurriculumRefFromJson(json);

  final String outcome;
  final String? code;
  final String? textbook;
}

@JsonSerializable()
class Prerequisite {
  const Prerequisite({required this.skill, this.lesson});

  factory Prerequisite.fromJson(Map<String, dynamic> json) =>
      _$PrerequisiteFromJson(json);

  final String skill;
  final String? lesson;
}

@JsonSerializable()
class Misconception {
  const Misconception({required this.id, required this.description});

  factory Misconception.fromJson(Map<String, dynamic> json) =>
      _$MisconceptionFromJson(json);

  final String id;
  final String description;
}

@JsonSerializable()
class GlossaryEntry {
  const GlossaryEntry({required this.en, required this.ur});

  factory GlossaryEntry.fromJson(Map<String, dynamic> json) =>
      _$GlossaryEntryFromJson(json);

  final String en;
  final String ur;
}

@JsonSerializable()
class Flashcard {
  const Flashcard({required this.id, required this.front, required this.back});

  factory Flashcard.fromJson(Map<String, dynamic> json) =>
      _$FlashcardFromJson(json);

  final String id;
  final LocalizedText front;
  final LocalizedText back;
}

@JsonSerializable()
class HomeTask {
  const HomeTask({required this.id, required this.text});

  factory HomeTask.fromJson(Map<String, dynamic> json) =>
      _$HomeTaskFromJson(json);

  final String id;
  final LocalizedText text;
}

/// Teacher review state. The app only shows `approved` lessons to students;
/// the developer previewer shows all of them.
@JsonSerializable()
class Review {
  const Review({required this.status, this.reviewedBy, this.date});

  factory Review.fromJson(Map<String, dynamic> json) => _$ReviewFromJson(json);

  final String status;
  final String? reviewedBy;
  final String? date;

  bool get isApproved => status == 'approved';
}
