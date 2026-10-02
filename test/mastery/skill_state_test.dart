import 'package:ai_tutor/mastery/skill_state.dart';
import 'package:ai_tutor/models/lesson.dart';
import 'package:flutter_test/flutter_test.dart';

const criteria = MasteryCriteria(
  questionTypes: ['recall', 'apply', 'find_error'],
  days: 2,
);

/// Day [d] of a pretend month, at 5 pm.
DateTime day(int d, [int hour = 17]) => DateTime(2026, 10, d, hour);

Evidence answer(
  int d,
  String type, {
  bool right = true,
  bool solved = false,
  int hour = 17,
}) => Evidence(
  skill: 'maths.x.y',
  itemId: 'q-$type-$d-$hour',
  at: day(d, hour),
  questionType: type,
  firstTry: right,
  solved: right || solved,
);

SkillState play(List<Evidence> answers, [SkillState? from]) => answers.fold(
  from ?? const SkillState(skill: 'maths.x.y'),
  (s, e) => s.record(e, criteria),
);

/// A skill mastered on day 2.
SkillState mastered() =>
    play([answer(1, 'recall'), answer(1, 'apply'), answer(2, 'find_error')]);

void main() {
  test('levels go from not started to practising', () {
    var s = const SkillState(skill: 'maths.x.y');
    expect(s.level(criteria), MasteryLevel.notStarted);

    s = play([answer(1, 'apply', right: false)], s);
    expect(s.level(criteria), MasteryLevel.learning);

    s = play([answer(1, 'apply')], s);
    expect(s.level(criteria), MasteryLevel.practising);
    expect(s.missingTypes(criteria), {'recall', 'find_error'});
  });

  test('every type on one day is not yet mastered: it needs two days', () {
    final s = play([
      answer(1, 'recall'),
      answer(1, 'apply'),
      answer(1, 'find_error'),
    ]);
    expect(s.level(criteria), MasteryLevel.practising);

    final next = play([answer(3, 'apply')], s);
    expect(next.level(criteria), MasteryLevel.mastered);
    expect(next.nextReview, DateTime(2026, 10, 5)); // 2 days later
  });

  test('answers right only after a retry do not prove mastery', () {
    final s = play([
      answer(1, 'recall', right: false, solved: true),
      answer(1, 'apply', right: false, solved: true),
      answer(2, 'find_error', right: false, solved: true),
    ]);
    expect(s.level(criteria), MasteryLevel.learning);
  });

  test('reviews after 2 days, 1 week, 1 month; secure after a week', () {
    var s = mastered();
    expect(s.nextReview, DateTime(2026, 10, 4));

    // Answering before the review is due changes nothing.
    s = play([answer(3, 'apply')], s);
    expect(s.nextReview, DateTime(2026, 10, 4));

    s = play([answer(4, 'apply')], s);
    expect(s.level(criteria), MasteryLevel.mastered);
    expect(s.nextReview, DateTime(2026, 10, 11)); // 1 week

    s = play([answer(11, 'recall')], s);
    expect(s.level(criteria), MasteryLevel.secure);
    expect(s.nextReview, DateTime(2026, 11, 10)); // 1 month
  });

  test('a review right only after a retry repeats the same gap', () {
    final s = play([
      answer(4, 'apply', right: false, solved: true),
    ], mastered());
    expect(s.level(criteria), MasteryLevel.mastered);
    expect(s.nextReview, DateTime(2026, 10, 6));
  });

  test('a forgotten review goes back to practising', () {
    var s = play([answer(4, 'apply', right: false)], mastered());
    expect(s.level(criteria), MasteryLevel.practising);
    expect(s.nextReview, isNull);

    // It has to be shown again on two new days.
    s = play([answer(5, 'apply')], s);
    expect(s.level(criteria), MasteryLevel.practising);
    s = play([answer(6, 'recall')], s);
    expect(s.level(criteria), MasteryLevel.mastered);
    expect(s.nextReview, DateTime(2026, 10, 8));
  });

  test('a slip between reviews brings the review forward', () {
    final s = play([
      answer(4, 'apply'), // next review on the 11th
      answer(6, 'apply', right: false),
    ], mastered());
    expect(s.nextReview, DateTime(2026, 10, 7));
  });

  test('needs help after four misses in a row, cleared by a right answer', () {
    var s = play([
      for (var i = 0; i < 3; i++) answer(1, 'apply', right: false),
    ]);
    expect(s.stuck, 3);
    expect(s.needsHelp, isFalse);
    s = play([answer(1, 'apply', right: false)], s);
    expect(s.needsHelp, isTrue);
    s = play([answer(2, 'apply')], s);
    expect(s.needsHelp, isFalse);
    expect(s.stuck, 0);
  });

  test('remembers only recent questions', () {
    final s = play([
      for (var h = 0; h < 30; h++) answer(1, 'apply', hour: h % 24),
    ]);
    expect(s.recent.length, lessThanOrEqualTo(20));
  });

  test('saves and loads', () {
    final s = play([
      answer(4, 'apply', right: false),
      answer(5, 'apply'),
    ], mastered());
    final copy = SkillState.fromJson(s.toJson());
    expect(copy.toJson(), s.toJson());
    expect(copy.level(criteria), s.level(criteria));
  });
}
