import 'package:ai_tutor/features/effort/effort.dart';
import 'package:ai_tutor/mastery/curriculum.dart';
import 'package:ai_tutor/mastery/skill_state.dart';
import 'package:ai_tutor/models/lesson_step.dart';
import 'package:ai_tutor/services/local_db.dart';
import 'package:flutter_test/flutter_test.dart';

import '../mastery/lessons.dart';

void main() {
  final lessons = loadLessons();
  final curriculum = Curriculum(lessons);
  final g6 = lessons.firstWhere((l) => l.id.startsWith('g6-'));
  final explain = g6.steps.whereType<AiExplainStep>().first.id;
  final photoLesson = lessons.firstWhere(
    (l) => l.steps.any((s) => s is PhotoCheckStep),
  );
  final photo = photoLesson.steps.whereType<PhotoCheckStep>().first.id;

  StepResultRow row(
    String stepId, {
    String? lessonId,
    int attempts = 1,
    bool? correct = true,
    DateTime? at,
  }) => StepResultRow(
    studentId: 's1',
    lessonId: lessonId ?? g6.id,
    stepId: stepId,
    correct: correct,
    attempts: attempts,
    misconceptions: '[]',
    answeredAt: at ?? DateTime(2026, 10, 3),
    synced: true,
  );

  group('lesson stars count effort', () {
    final questions = g6.steps.whereType<QuestionStep>().map((q) => q.id);

    test('finishing, trying again and explaining give three', () {
      final answers = [
        for (final id in questions)
          answerOf(row(id, attempts: id == questions.first ? 2 : 1)),
      ];
      final stars = starsFor(g6, answers, completed: true);
      expect(stars.count, 3);
    });

    test('no mistakes still counts as keeping going', () {
      final stars = starsFor(g6, [
        for (final id in questions) answerOf(row(id)),
      ], completed: true);
      expect(stars.keptTrying, isTrue);
    });

    test('giving up on a question without trying again loses that star', () {
      final stars = starsFor(g6, [
        answerOf(row(questions.first, correct: false)),
        answerOf(row(explain)),
      ], completed: true);
      expect(stars.keptTrying, isFalse);
      expect(stars.explained, isTrue);
      expect(stars.count, 2);
    });

    test('skipping the explanation loses the explaining star', () {
      final stars = starsFor(g6, [
        for (final id in questions)
          if (id != explain) answerOf(row(id)),
      ], completed: true);
      expect(stars.explained, isFalse);
    });
  });

  test('badges come from saved answers, with no streaks', () {
    Set<EffortBadge> badges({
      List<LessonProgress> progress = const [],
      List<StepResultRow> steps = const [],
      List<SkillState> skills = const [],
    }) => badgesFor(
      curriculum: curriculum,
      progress: progress,
      steps: steps,
      skills: skills,
      now: DateTime(2026, 10, 20),
    );

    expect(badges(), isEmpty);
    expect(
      badges(
        progress: [
          LessonProgress(
            studentId: 's1',
            lessonId: g6.id,
            lessonVersion: 1,
            nextStep: 9,
            completed: true,
            updatedAt: DateTime(2026, 10, 3),
          ),
        ],
      ),
      {EffortBadge.firstLesson},
    );
    expect(badges(steps: [row(g6.steps.first.id, attempts: 2)]), {
      EffortBadge.triedAgain,
    });
    expect(badges(steps: [row(explain)]), {EffortBadge.explained});
    expect(badges(steps: [row(photo, lessonId: photoLesson.id, attempts: 2)]), {
      EffortBadge.checkedPhoto,
    });
    expect(
      badges(
        skills: [
          const SkillState(
            skill: fractions,
            correctDays: ['2026-10-01', '2026-10-05'],
          ),
        ],
      ),
      {EffortBadge.cameBack},
    );

    // Any five days this month; they don't need to be in a row, and last
    // month doesn't count.
    final days = [1, 4, 9, 15];
    final some = [
      for (final d in days) row('a$d', at: DateTime(2026, 10, d)),
      row('old', at: DateTime(2026, 9, 30)),
    ];
    expect(badges(steps: some), isEmpty);
    expect(
      badges(
        steps: [
          ...some,
          row('b', at: DateTime(2026, 10, 19)),
        ],
      ),
      {EffortBadge.fiveDays},
    );
  });

  test('the next lesson is the next unfinished one in the subject', () {
    final maths = curriculum.lessons.where((l) => l.subject == 'maths');
    final first = maths.first;
    expect(nextLessonAfter(curriculum, first, {}), maths.elementAt(1));
    expect(nextLessonAfter(curriculum, maths.last, {}), isNull);
  });
}
