import 'package:ai_tutor/app/theme/age_tier.dart';

import 'dart:math';

import 'package:ai_tutor/lessons/hidden_units.dart';
import 'package:ai_tutor/lessons/step_result.dart';
import 'package:ai_tutor/mastery/curriculum.dart';
import 'package:ai_tutor/mastery/daily_plan.dart';
import 'package:ai_tutor/mastery/evidence.dart';
import 'package:ai_tutor/mastery/skill_state.dart';
import 'package:ai_tutor/models/lesson.dart';
import 'package:flutter_test/flutter_test.dart';

import 'lessons.dart';

/// A pretend student who does the daily plan for some weeks. [skill]
/// decides how often an answer is right on the first try.
class SimulatedStudent {
  SimulatedStudent(this.curriculum, {this.skill = 0.85, int seed = 1})
    : _random = Random(seed);

  final Curriculum curriculum;
  final double skill;
  final Random _random;

  final states = <String, SkillState>{};
  final lessons = <String, LessonPosition>{};
  final plans = <DateTime, DailyPlan>{};

  /// (day, skill, level) whenever a level changes.
  final levelChanges = <(DateTime, String, MasteryLevel)>[];

  /// Skills to get wrong from this day on (to simulate forgetting).
  final forgets = <String, DateTime>{};

  bool _right(String skill, DateTime now) {
    final from = forgets[skill];
    if (from != null && !now.isBefore(from)) return false;
    return _random.nextDouble() < this.skill;
  }

  void record(Evidence e) {
    final criteria = curriculum.criteriaFor(e.skill);
    final before = states[e.skill]?.level(criteria) ?? MasteryLevel.notStarted;
    final after = (states[e.skill] ?? SkillState(skill: e.skill)).record(
      e,
      criteria,
    );
    states[e.skill] = after;
    final level = after.level(criteria);
    if (level != before) levelChanges.add((dayOf(e.at), e.skill, level));
  }

  void answer(Lesson lesson, PlanQuestion q, DateTime at) {
    final right = _right(q.skill, at);
    record(
      evidenceFor(
        lesson,
        q.step,
        StepResult(stepId: q.step.id, correct: right, solved: right),
        at,
        questionType: q.type,
        skill: q.skill,
        itemId: q.id,
      )!,
    );
  }

  void playLesson(LessonItem item, DateTime at) {
    final lesson = item.lesson;
    // About one minute per step, stopping when today's time is used up.
    final steps = lesson.steps.length;
    final perStep = lesson.estimatedMinutes / steps;
    final last = min(
      steps,
      item.fromStep + (item.minutes / perStep).floor().clamp(1, steps),
    );
    for (var i = item.fromStep; i < last; i++) {
      final step = lesson.steps[i];
      final right = _right(lesson.mainSkill, at);
      final e = evidenceFor(
        lesson,
        step,
        StepResult(stepId: step.id, correct: right, solved: true),
        at,
      );
      if (e != null) record(e);
    }
    lessons[lesson.id] = (nextStep: last, completed: last >= steps);
  }

  void studyDay(DateTime now, {int minutes = 15}) {
    final plan = buildDailyPlan(
      curriculum: curriculum,
      states: states,
      lessons: lessons,
      now: now,
      studentId: 'sim',
      minutes: minutes,
    );
    plans[dayOf(now)] = plan;
    for (final item in plan.items) {
      switch (item) {
        case QuestionItem(:final question):
          answer(curriculum.lesson(question.lessonId)!, question, now);
        case LessonItem():
          playLesson(item, now);
        case HomeTaskItem() || FlashcardsItem():
          break;
      }
    }
  }

  /// Studies every day except Fridays, for [days] days.
  void studyFor(int days, DateTime start, {int minutes = 15}) {
    for (var d = 0; d < days; d++) {
      final now = start.add(Duration(days: d));
      if (now.weekday == DateTime.friday) continue;
      studyDay(now, minutes: minutes);
    }
  }
}

final start = DateTime(2026, 10, 5, 17); // a Monday, after school

void main() {
  // A secondary student: the Nursery lessons aren't theirs.
  final curriculum = Curriculum(
    loadLessons().where((l) => l.tier != 'early').toList(),
  );
  MasteryLevel levelOf(SimulatedStudent s, String skill) =>
      s.states[skill]?.level(curriculum.criteriaFor(skill)) ??
      MasteryLevel.notStarted;

  test('two hundred weeks of plans: every lesson done, skills secure', () {
    final s = SimulatedStudent(curriculum)..studyFor(2000, start);

    for (final lesson in curriculum.lessons) {
      expect(s.lessons[lesson.id]?.completed, isTrue, reason: lesson.id);
    }
    for (final skill in [fractions, equations, balancing]) {
      expect(
        levelOf(s, skill).index,
        greaterThanOrEqualTo(MasteryLevel.mastered.index),
        reason: skill,
      );
    }
    expect(levelOf(s, fractions), MasteryLevel.secure);
  });

  test('with the hidden units left out, every shown lesson is still done', () {
    final shown = Curriculum([
      for (final l in curriculum.lessons)
        if (!isHiddenLesson(l.id)) l,
    ]);
    expect(shown.lessons.length, lessThan(curriculum.lessons.length));
    expect(isHiddenLesson('g6-maths-02-dividing-fractions'), isTrue);
    expect(isHiddenLesson('g6-maths-04-adding-integers'), isFalse);
    final s = SimulatedStudent(shown)..studyFor(2000, start);
    for (final lesson in shown.lessons) {
      expect(s.lessons[lesson.id]?.completed, isTrue, reason: lesson.id);
    }
  });

  test('levels only rise in order for a strong student', () {
    final s = SimulatedStudent(curriculum, skill: 1)..studyFor(2000, start);
    for (final skill in [fractions, equations, balancing]) {
      final levels = [
        for (final (_, sk, level) in s.levelChanges)
          if (sk == skill) level.index,
      ];
      expect(levels, orderedEquals([...levels]..sort()), reason: skill);
      expect(levels.last, MasteryLevel.secure.index, reason: skill);
    }
  });

  test('mastery needs two different days, then reviews follow 2, 7, 30', () {
    final s = SimulatedStudent(curriculum, skill: 1)..studyFor(60, start);
    final mastered = s.levelChanges.firstWhere(
      (c) => c.$2 == fractions && c.$3 == MasteryLevel.mastered,
    );
    // The fractions lesson is on day 1, so mastery comes on day 2 at the
    // earliest.
    expect(mastered.$1.isAfter(dayOf(start)), isTrue);

    // Replay the review dates the plans asked for.
    final reviewDays = [
      for (final MapEntry(key: day, value: plan) in s.plans.entries)
        if (plan.items.any(
          (i) =>
              i is QuestionItem &&
              i.purpose == QuestionPurpose.review &&
              i.question.skill == fractions,
        ))
          day,
    ]..sort();
    final gaps = [
      reviewDays.first.difference(mastered.$1).inDays,
      for (var i = 1; i < reviewDays.length; i++)
        reviewDays[i].difference(reviewDays[i - 1]).inDays,
    ];
    // About 2 days, 1 week, 1 month (a day later if it lands on a Friday).
    expect(gaps[0], inInclusiveRange(2, 3));
    expect(gaps[1], inInclusiveRange(7, 8));
    expect(gaps[2], inInclusiveRange(30, 31));
  });

  test('a forgotten skill drops back to practising and is practised again', () {
    final s = SimulatedStudent(curriculum, skill: 1)..studyFor(10, start);
    expect(
      levelOf(s, fractions).index,
      greaterThanOrEqualTo(MasteryLevel.mastered.index),
    );

    s.forgets[fractions] = start.add(const Duration(days: 10));
    // Study until the next fractions review comes up and is failed.
    final review = s.states[fractions]!.nextReview!;
    final days = review.difference(dayOf(start)).inDays + 1;
    for (var d = 10; d < days; d++) {
      s.studyDay(start.add(Duration(days: d)));
    }
    expect(levelOf(s, fractions), MasteryLevel.practising);

    // The next plan practises fractions again.
    s.forgets.clear();
    final next = start.add(Duration(days: days));
    final plan = buildDailyPlan(
      curriculum: curriculum,
      states: s.states,
      lessons: s.lessons,
      now: next,
      studentId: 'sim',
    );
    expect(
      plan.items.whereType<QuestionItem>().where(
        (i) =>
            i.purpose == QuestionPurpose.practice &&
            i.question.skill == fractions,
      ),
      isNotEmpty,
    );
  });

  test(
    'every plan fits the time, never repeats a question, and is sensible',
    () {
      for (final minutes in [10, 15]) {
        final s = SimulatedStudent(curriculum, skill: 0.7, seed: minutes)
          ..studyFor(42, start, minutes: minutes);
        for (final MapEntry(key: day, value: plan) in s.plans.entries) {
          final reviews = plan.items
              .whereType<QuestionItem>()
              .where((i) => i.purpose == QuestionPurpose.review)
              .fold(0, (sum, i) => sum + i.minutes);
          // Due reviews always come first; the rest fits the time.
          expect(
            plan.minutes,
            lessThanOrEqualTo(max(minutes, reviews)),
            reason: '$day',
          );
          expect(plan.keys.toSet().length, plan.keys.length, reason: '$day');
          expect(plan.items, isNotEmpty, reason: '$day');
        }
      }
    },
  );

  test('flashcards and home tasks only after the skill is understood', () {
    final s = SimulatedStudent(curriculum, skill: 0.8);
    for (var d = 0; d < 42; d++) {
      final now = start.add(Duration(days: d));
      final plan = buildDailyPlan(
        curriculum: curriculum,
        states: s.states,
        lessons: s.lessons,
        now: now,
        studentId: 'sim',
      );
      for (final item in plan.items) {
        final lesson = switch (item) {
          FlashcardsItem(:final lesson) ||
          HomeTaskItem(:final lesson) => lesson,
          _ => null,
        };
        if (lesson != null) {
          expect(
            levelOf(s, lesson.mainSkill).index,
            greaterThanOrEqualTo(MasteryLevel.practising.index),
          );
        }
      }
      s.studyDay(now);
    }
    // Over six weeks both appear at least once.
    final all = s.plans.values.expand((p) => p.items);
    expect(all.whereType<FlashcardsItem>(), isNotEmpty);
    expect(all.whereType<HomeTaskItem>(), isNotEmpty);
  });

  test('the first day starts the first lesson', () {
    final plan = buildDailyPlan(
      curriculum: curriculum,
      states: const {},
      lessons: const {},
      now: start,
      studentId: 'new',
    );
    expect(plan.items.single, isA<LessonItem>());
    expect(
      (plan.items.single as LessonItem).lesson.id,
      'g6-maths-02-dividing-fractions',
    );
  });

  test('a missed warm-up on a skill no lesson teaches never blocks', () {
    // The first Ratio lesson warms up with times tables, which no lesson
    // teaches. One wrong answer leaves that skill at Learning for ever.
    final ratio = Curriculum([
      for (final l in loadLessons())
        if (l.id == 'g6-maths-06-what-is-a-ratio') l,
    ]);
    const facts = 'maths.multiplication.facts';
    expect(ratio.lessons.single.prerequisites.map((p) => p.skill), [
      'maths.fractions.unit_fraction_meaning',
      facts,
    ]);
    final plan = buildDailyPlan(
      curriculum: ratio,
      states: const {facts: SkillState(skill: facts, answered: 1)},
      lessons: const {},
      now: start,
      studentId: 'sim',
    );
    expect(
      plan.items.whereType<LessonItem>().single.lesson.id,
      'g6-maths-06-what-is-a-ratio',
    );
  });

  test('new lessons come from the student\'s age group', () {
    final all = Curriculum(loadLessons());
    String first(AgeTier? tier) =>
        (buildDailyPlan(
                  curriculum: all,
                  states: const {},
                  lessons: const {},
                  now: start,
                  studentId: 'new',
                  tier: tier,
                ).items.single
                as LessonItem)
            .lesson
            .id;
    expect(first(AgeTier.early), 'g0-maths-01-count-the-mangoes');
    expect(first(AgeTier.middle), 'g6-maths-02-dividing-fractions');
    expect(first(AgeTier.older), 'g9-maths-05-solving-linear-equations');
    // No Grade 3-5 lessons yet: anything but the Nursery ones.
    expect(first(AgeTier.primary), 'g6-maths-02-dividing-fractions');
  });

  test('the plan is the same all day and can be saved and rebuilt', () {
    final s = SimulatedStudent(curriculum)..studyFor(12, start);
    final now = start.add(const Duration(days: 12));
    DailyPlan plan(DateTime t) => buildDailyPlan(
      curriculum: curriculum,
      states: s.states,
      lessons: s.lessons,
      now: t,
      studentId: 'sim',
    );
    final morning = plan(now.subtract(const Duration(hours: 9)));
    expect(plan(now).keys, morning.keys);
    expect(
      planFromKeys(now, morning.keys, curriculum, lessons: s.lessons).keys,
      morning.keys,
    );
  });
}
