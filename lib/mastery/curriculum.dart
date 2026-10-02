import '../models/lesson.dart';
import '../models/lesson_step.dart';
import '../models/localized_text.dart';

/// A question the daily plan can ask, from a lesson's question bank or
/// review questions.
class PlanQuestion {
  const PlanQuestion({
    required this.lessonId,
    required this.skill,
    required this.type,
    required this.step,
    this.forReview = false,
  });

  final String lessonId;
  final String skill;

  /// recall, explain, apply, find_error or exam_style.
  final String type;
  final LessonStep step;

  /// From `review_questions` (preferred for spaced review).
  final bool forReview;

  /// Unique across lessons.
  String get id => '$lessonId/${step.id}';

  /// About how long it takes, for the daily plan.
  int get minutes => step is TextCheckStep ? 2 : 1;
}

/// The skills graph: every skill, what it needs first, the lessons that
/// teach it, and what a student must show to master it. Built from the
/// lesson files, so new lessons extend it automatically.
class Curriculum {
  Curriculum(List<Lesson> lessons)
    : lessons = List.of(lessons)..sort(_byGradeThenId) {
    for (final lesson in this.lessons) {
      for (final skill in lesson.skills) {
        (_lessonsBySkill[skill] ??= []).add(lesson);
        (_prerequisites[skill] ??= {}).addAll(
          lesson.prerequisites.map((p) => p.skill),
        );
      }
      for (final p in lesson.prerequisites) {
        _prerequisites.putIfAbsent(p.skill, () => {});
        if (p.lesson != null) _prerequisiteLesson[p.skill] ??= p.lesson!;
      }
      lesson.masteryCriteria.forEach((skill, c) => _criteria[skill] ??= c);
      lesson.questionBank.forEach((skill, questions) {
        for (final q in questions) {
          _add(lesson, q, q.skill ?? skill, forReview: false);
        }
      });
      for (final q in lesson.reviewQuestions) {
        _add(lesson, q, q.skill ?? lesson.mainSkill, forReview: true);
      }
    }
  }

  void _add(
    Lesson lesson,
    Question q,
    String skill, {
    required bool forReview,
  }) {
    (_questions[skill] ??= []).add(
      PlanQuestion(
        lessonId: lesson.id,
        skill: skill,
        type: q.type,
        step: q.step,
        forReview: forReview,
      ),
    );
  }

  static int _byGradeThenId(Lesson a, Lesson b) =>
      a.grade != b.grade ? a.grade.compareTo(b.grade) : a.id.compareTo(b.id);

  /// All lessons, by grade then id.
  final List<Lesson> lessons;

  final _lessonsBySkill = <String, List<Lesson>>{};
  final _prerequisites = <String, Set<String>>{};
  final _prerequisiteLesson = <String, String>{};
  final _criteria = <String, MasteryCriteria>{};
  final _questions = <String, List<PlanQuestion>>{};

  /// Every skill a lesson teaches or needs.
  Set<String> get skills => _prerequisites.keys.toSet();

  Lesson? lesson(String id) => lessons.where((l) => l.id == id).firstOrNull;

  List<Lesson> lessonsTeaching(String skill) => _lessonsBySkill[skill] ?? [];

  /// Skills needed directly before [skill].
  Set<String> prerequisitesOf(String skill) => _prerequisites[skill] ?? {};

  /// Every skill needed before [skill], however far back.
  Set<String> allPrerequisitesOf(String skill) {
    final found = <String>{};
    void walk(String s) {
      for (final p in prerequisitesOf(s)) {
        if (found.add(p)) walk(p);
      }
    }

    walk(skill);
    return found;
  }

  /// A lesson to go back to for [skill]: one named in a prerequisite, or
  /// any lesson that teaches it.
  String? lessonFor(String skill) =>
      _prerequisiteLesson[skill] ?? lessonsTeaching(skill).firstOrNull?.id;

  MasteryCriteria? criteriaFor(String skill) => _criteria[skill];

  List<PlanQuestion> questionsFor(String skill) => _questions[skill] ?? [];

  /// A name for the skill: the title of the first lesson that teaches it.
  LocalizedText? titleOf(String skill) =>
      lessonsTeaching(skill).firstOrNull?.title;

  /// The skill a step tests (its own, or its lesson's first skill).
  static String skillOf(Lesson lesson, QuestionStep step) =>
      step.skill ?? lesson.mainSkill;
}
