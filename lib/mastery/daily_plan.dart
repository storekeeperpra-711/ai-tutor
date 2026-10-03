import 'dart:math';

import '../app/theme/age_tier.dart';
import '../models/lesson.dart';
import 'curriculum.dart';
import 'skill_state.dart';

/// One thing to do today. [key] identifies it, so a plan can be saved and
/// rebuilt the same way all day.
sealed class PlanItem {
  const PlanItem();

  String get key;

  /// About how long it takes.
  int get minutes;
}

enum QuestionPurpose {
  /// A spaced review that is due.
  review,

  /// Practice on the skill being learned now.
  practice,

  /// One question from another skill, mixed in.
  mixed,

  /// Explain it or find the mistake.
  explain,
}

class QuestionItem extends PlanItem {
  const QuestionItem(this.purpose, this.question);

  final QuestionPurpose purpose;
  final PlanQuestion question;

  @override
  String get key => '${purpose.name}:${question.id}';

  @override
  int get minutes => question.minutes;
}

/// Continue or start a lesson.
class LessonItem extends PlanItem {
  const LessonItem(this.lesson, {required this.fromStep, this.timeLimit});

  final Lesson lesson;

  /// 0 for a new lesson.
  final int fromStep;

  /// Minutes planned for it today when the rest of the lesson doesn't fit
  /// (progress is saved, so it carries on tomorrow).
  final int? timeLimit;

  @override
  String get key => 'lesson:${lesson.id}';

  /// Minutes the rest of the lesson takes.
  int get minutesLeft {
    final total = lesson.steps.length;
    final left = (total - fromStep).clamp(1, total);
    return (lesson.estimatedMinutes * left / total).ceil();
  }

  @override
  int get minutes => min(minutesLeft, timeLimit ?? minutesLeft);
}

/// A real-world task away from the phone. Takes no screen time.
class HomeTaskItem extends PlanItem {
  const HomeTaskItem(this.lesson, this.task);

  final Lesson lesson;
  final HomeTask task;

  @override
  String get key => 'home:${lesson.id}/${task.id}';

  @override
  int get minutes => 0;
}

/// Key facts to remember, only for skills already understood.
class FlashcardsItem extends PlanItem {
  const FlashcardsItem(this.lesson);

  final Lesson lesson;

  @override
  String get key => 'cards:${lesson.id}';

  @override
  int get minutes => 2;
}

class DailyPlan {
  const DailyPlan(this.day, this.items);

  final DateTime day;
  final List<PlanItem> items;

  int get minutes => items.fold(0, (sum, i) => sum + i.minutes);
  List<String> get keys => [for (final i in items) i.key];
}

/// Where a student is in each lesson: (next step, finished).
typedef LessonPosition = ({int nextStep, bool completed});

/// Spec B4: about 10–15 minutes of homework per day, built on the phone
/// from what the student knows. The same inputs always give the same
/// plan, and questions asked in the last [_restDays] days are skipped
/// where there is a choice.
DailyPlan buildDailyPlan({
  required Curriculum curriculum,
  required Map<String, SkillState> states,
  required Map<String, LessonPosition> lessons,
  required DateTime now,
  required String studentId,
  int minutes = 15,
  AgeTier? tier,
}) {
  final today = dayOf(now);
  final random = Random(_seed('$studentId ${dayKey(today)}'));
  final items = <PlanItem>[];
  final used = <String>{};
  var left = minutes;

  MasteryLevel levelOf(String skill) =>
      states[skill]?.level(curriculum.criteriaFor(skill)) ??
      MasteryLevel.notStarted;

  bool fresh(PlanQuestion q) {
    final asked = states[q.skill]?.recent[q.id];
    return asked == null || today.difference(dayOf(asked)).inDays >= _restDays;
  }

  /// Picks a question for [skill], preferring [types] and unasked ones.
  PlanQuestion? pick(
    String skill, {
    Set<String> types = const {},
    bool review = false,
  }) {
    final options = curriculum
        .questionsFor(skill)
        .where((q) => !used.contains(q.id))
        .toList();
    if (options.isEmpty) return null;
    int score(PlanQuestion q) =>
        (fresh(q) ? 4 : 0) +
        (types.contains(q.type) ? 2 : 0) +
        (review && q.forReview ? 1 : 0);
    final best = options.map(score).reduce(max);
    final top = options.where((q) => score(q) == best).toList();
    return top[random.nextInt(top.length)];
  }

  void add(PlanItem item, {bool always = false}) {
    if (!always && item.minutes > left) return;
    items.add(item);
    if (item is QuestionItem) used.add(item.question.id);
    left -= item.minutes;
  }

  // 1. Due reviews first: retrieval practice (at most 3).
  final due = states.values.where((s) => s.reviewDue(now)).toList()
    ..sort((a, b) => a.nextReview!.compareTo(b.nextReview!));
  for (final s in due.take(3)) {
    final q = pick(s.skill, review: true);
    if (q != null) add(QuestionItem(QuestionPurpose.review, q), always: true);
  }

  // 2. Practice on the skill being learned now: the types still missing.
  final learning =
      states.values
          .where(
            (s) =>
                curriculum.questionsFor(s.skill).isNotEmpty &&
                switch (levelOf(s.skill)) {
                  MasteryLevel.learning || MasteryLevel.practising => true,
                  _ => false,
                },
          )
          .toList()
        ..sort((a, b) => b.lastAnswered!.compareTo(a.lastAnswered!));
  final current = learning.firstOrNull?.skill;
  if (current != null) {
    final missing = states[current]!.missingTypes(
      curriculum.criteriaFor(current),
    );
    for (var i = 0; i < 2; i++) {
      final q = pick(current, types: missing);
      if (q == null) break;
      add(QuestionItem(QuestionPurpose.practice, q));
    }
  }

  // 3. Continue the unfinished lesson, or start the next one that is ready.
  final lessonItem = _nextLesson(curriculum, lessons, levelOf, tier);
  // A lesson can be stopped half way (progress is saved), so it only
  // needs half its time to fit; then only part of it is planned today.
  if (lessonItem != null && left * 2 >= lessonItem.minutesLeft) {
    final planned = LessonItem(
      lessonItem.lesson,
      fromStep: lessonItem.fromStep,
      timeLimit: left < lessonItem.minutesLeft ? left : null,
    );
    items.add(planned);
    left -= planned.minutes;
  }

  // 4. One mixed question from another skill already practised.
  final practised = [
    for (final s in states.values)
      if (s.skill != current &&
          levelOf(s.skill).index >= MasteryLevel.practising.index)
        s.skill,
  ]..sort();
  if (practised.isNotEmpty) {
    final q = pick(practised[random.nextInt(practised.length)]);
    if (q != null) add(QuestionItem(QuestionPurpose.mixed, q));
  }

  // 5. One "explain it" or "find the mistake" question.
  final understood = [?current, ...practised];
  for (final skill in understood) {
    final q = pick(skill, types: const {'explain', 'find_error'});
    if (q != null && (q.type == 'explain' || q.type == 'find_error')) {
      add(QuestionItem(QuestionPurpose.explain, q));
      break;
    }
  }

  // Skills understood well enough for flashcards and home tasks.
  final ready = [
    for (final lesson in curriculum.lessons)
      if (levelOf(lesson.mainSkill).index >= MasteryLevel.practising.index)
        lesson,
  ];

  // 6. Sometimes a real-world task at home.
  final homeLessons = ready.where((l) => l.homeTasks.isNotEmpty).toList();
  if (today.difference(DateTime(2026)).inDays % 3 == 0 &&
      homeLessons.isNotEmpty) {
    final lesson = homeLessons[random.nextInt(homeLessons.length)];
    add(
      HomeTaskItem(
        lesson,
        lesson.homeTasks[random.nextInt(lesson.homeTasks.length)],
      ),
    );
  }

  // 7. Flashcards, only after understanding.
  final cardLessons = ready.where((l) => l.flashcards.isNotEmpty).toList();
  if (cardLessons.isNotEmpty) {
    add(FlashcardsItem(cardLessons[random.nextInt(cardLessons.length)]));
  }

  return DailyPlan(today, items);
}

/// Rebuilds a saved plan from its keys (items whose content is gone are
/// dropped).
DailyPlan planFromKeys(
  DateTime day,
  List<String> keys,
  Curriculum c, {
  Map<String, LessonPosition> lessons = const {},
}) {
  PlanQuestion? question(String id) {
    final lessonId = id.split('/').first;
    final lesson = c.lesson(lessonId);
    if (lesson == null) return null;
    for (final skill in lesson.skills) {
      for (final q in c.questionsFor(skill)) {
        if (q.id == id) return q;
      }
    }
    return null;
  }

  final items = <PlanItem>[];
  for (final key in keys) {
    final colon = key.indexOf(':');
    final kind = key.substring(0, colon);
    final rest = key.substring(colon + 1);
    final purpose = QuestionPurpose.values
        .where((p) => p.name == kind)
        .firstOrNull;
    if (purpose != null) {
      if (question(rest) case final q?) items.add(QuestionItem(purpose, q));
      continue;
    }
    switch (kind) {
      case 'lesson':
        if (c.lesson(rest) case final l?) {
          final p = lessons[l.id];
          items.add(
            LessonItem(l, fromStep: p == null || p.completed ? 0 : p.nextStep),
          );
        }
      case 'cards':
        if (c.lesson(rest) case final l?) items.add(FlashcardsItem(l));
      case 'home':
        final [lessonId, taskId] = rest.split('/');
        final lesson = c.lesson(lessonId);
        final task = lesson?.homeTasks.where((t) => t.id == taskId).firstOrNull;
        if (lesson != null && task != null) {
          items.add(HomeTaskItem(lesson, task));
        }
    }
  }
  return DailyPlan(dayOf(day), items);
}

const _restDays = 2;

LessonItem? _nextLesson(
  Curriculum curriculum,
  Map<String, LessonPosition> positions,
  MasteryLevel Function(String) levelOf,
  AgeTier? tier,
) {
  // An unfinished lesson comes first.
  for (final lesson in curriculum.lessons) {
    final p = positions[lesson.id];
    if (p != null && !p.completed && p.nextStep > 0) {
      return LessonItem(lesson, fromStep: p.nextStep);
    }
  }
  // Understanding before speed (spec B1, B3): a new lesson only once the
  // skills of every lesson started so far are mastered.
  final allMastered = curriculum.lessons
      .where((l) => positions[l.id] != null)
      .every((l) => levelOf(l.mainSkill).index >= MasteryLevel.mastered.index);
  if (!allMastered) return null;

  // Then the first new lesson, made for the student's age group, whose
  // prerequisites aren't known gaps. (Without lessons for their group
  // yet, any lesson except the youngest children's.)
  var fitting = curriculum.lessons.where(
    (l) => tier == null || l.tier == tier.name,
  );
  if (fitting.isEmpty) {
    fitting = curriculum.lessons.where((l) => l.tier != AgeTier.early.name);
  }
  for (final lesson in fitting) {
    if (positions[lesson.id] != null) continue;
    if (levelOf(lesson.mainSkill) != MasteryLevel.notStarted) continue;
    final gap = lesson.prerequisites.any(
      (p) => levelOf(p.skill) == MasteryLevel.learning,
    );
    if (!gap) return LessonItem(lesson, fromStep: 0);
  }
  return null;
}

/// A small stable hash (String.hashCode may differ between runs).
int _seed(String text) {
  var h = 0x811c9dc5;
  for (final c in text.codeUnits) {
    h = ((h ^ c) * 0x01000193) & 0x7fffffff;
  }
  return h;
}
