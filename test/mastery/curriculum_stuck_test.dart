import 'package:ai_tutor/mastery/curriculum.dart';
import 'package:ai_tutor/mastery/skill_state.dart';
import 'package:ai_tutor/mastery/stuck.dart';
import 'package:ai_tutor/models/lesson_step.dart';
import 'package:flutter_test/flutter_test.dart';

import 'lessons.dart';

void main() {
  final curriculum = Curriculum(loadLessons());
  final g6 = curriculum.lesson('g6-maths-02-dividing-fractions')!;

  test('the skills graph knows skills, prerequisites and lessons', () {
    expect(curriculum.skills, containsAll([fractions, equations, balancing]));
    expect(
      curriculum.prerequisitesOf(fractions),
      containsAll(['maths.fractions.unit_fraction_meaning']),
    );
    expect(curriculum.lessonsTeaching(fractions).single.id, g6.id);
    expect(
      curriculum.lessonFor(equations),
      'g9-maths-05-solving-linear-equations',
    );
    expect(curriculum.criteriaFor(fractions)!.days, 2);
    expect(curriculum.titleOf(fractions)!.en, g6.title.en);
    // Lessons come in grade order.
    expect(curriculum.lessons.map((l) => l.grade), [
      0,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      6,
      9,
      9,
      9,
      9,
      9,
      9,
      9,
      9,
      10,
    ]);
  });

  test('every mastery criterion can be met with the questions available', () {
    for (final lesson in curriculum.lessons) {
      for (final MapEntry(key: skill, value: criteria)
          in lesson.masteryCriteria.entries) {
        final types = {
          for (final q in curriculum.questionsFor(skill)) q.type,
          for (final s in lesson.steps.whereType<QuestionStep>())
            ?s.questionType,
        };
        expect(types, containsAll(criteria.questionTypes), reason: skill);
      }
    }
  });

  test('prerequisites are found however far back', () {
    final a = lessonJson('g9-maths-05-solving-linear-equations');
    final b = lessonJson('g6-maths-02-dividing-fractions');
    // Pretend the equations lesson needs the fractions skill.
    (a['prerequisites'] as List).add({'skill': fractions});
    final c = Curriculum([loadLessonJson(a), loadLessonJson(b)]);
    expect(
      c.allPrerequisitesOf(equations),
      containsAll([
        'maths.algebra.expressions_basic',
        fractions,
        'maths.multiplication.facts',
      ]),
    );
  });

  group('when stuck', () {
    SkillState stuckState(int n) => SkillState(
      skill: fractions,
      answered: n,
      stuck: n,
      needsHelp: n >= needsHelpAfter,
    );

    StuckAdvice? advise(
      int n, {
      String step = 's5_quarters',
      Set<String> shown = const {},
      Map<String, SkillState> states = const {},
      Curriculum? c,
    }) => adviseWhenStuck(
      state: stuckState(n),
      lesson: g6,
      stepId: step,
      curriculum: c ?? curriculum,
      states: states,
      shownAlternatives: shown,
    );

    test('first: explain it another way', () {
      final advice = advise(1);
      expect(advice, isA<ShowAlternative>());
      expect((advice! as ShowAlternative).alternative.id, 'alt_count_quarters');
      // The alternative is for one step only.
      expect(advise(1, step: 's8_ribbon'), isNull);
    });

    test('an alternative is not shown twice', () {
      expect(advise(2, shown: {'alt_count_quarters'}), isNull);
    });

    test('then: back to a prerequisite the student is struggling with', () {
      final json = lessonJson('g6-maths-02-dividing-fractions');
      (json['prerequisites'] as List)[0]['lesson'] =
          'g9-maths-05-solving-linear-equations';
      final c = Curriculum([loadLessonJson(json)]);
      const unitFractions = 'maths.fractions.unit_fraction_meaning';
      final states = {
        unitFractions: const SkillState(
          skill: unitFractions,
          answered: 1,
          stuck: 1,
        ),
      };
      final advice = advise(
        2,
        shown: {'alt_count_quarters'},
        states: states,
        c: c,
      );
      expect(advice, isA<GoBackToPrerequisite>());
      expect((advice! as GoBackToPrerequisite).skill, unitFractions);
    });

    test('then a break, then help from an adult; never a loop', () {
      expect(advise(3), isA<TakeABreak>());
      expect(advise(4), isA<GetHelp>());
      expect(advise(9), isA<GetHelp>());
      expect(advise(0), isNull);
    });
  });
}
