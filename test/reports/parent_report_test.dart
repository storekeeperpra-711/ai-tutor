import 'package:ai_tutor/l10n/app_localizations.dart';
import 'package:ai_tutor/mastery/curriculum.dart';
import 'package:ai_tutor/mastery/skill_state.dart';
import 'package:ai_tutor/reports/parent_report.dart';
import 'package:ai_tutor/services/local_db.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:intl/date_symbol_data_local.dart';

import '../features/mastery_flow_test.dart' show practising;
import '../mastery/lessons.dart' show loadLessons;

const fractions = 'maths.fractions.divide_by_fraction';
const equations = 'maths.linear_equations.solve_two_step';
const fractionsLesson = 'g6-maths-02-dividing-fractions';

void main() {
  final curriculum = Curriculum(loadLessons());
  // Saturday 3 October 2026.
  final now = DateTime(2026, 10, 3, 18);

  setUpAll(() => initializeDateFormatting());

  StepResultRow answer(DateTime at, {bool? correct = true, String id = 's'}) =>
      StepResultRow(
        studentId: 'ayesha',
        lessonId: fractionsLesson,
        stepId: '$id${at.millisecondsSinceEpoch}',
        correct: correct,
        attempts: 1,
        misconceptions: '[]',
        answeredAt: at,
        synced: true,
      );

  ParentReport build(Map<String, SkillState> states) => buildParentReport(
    states: states,
    progress: {
      fractionsLesson: LessonProgress(
        studentId: 'ayesha',
        lessonId: fractionsLesson,
        lessonVersion: 1,
        nextStep: 4,
        completed: false,
        updatedAt: now.subtract(const Duration(days: 1)),
      ),
    },
    steps: [
      answer(now),
      answer(now.subtract(const Duration(hours: 2))),
      answer(now.subtract(const Duration(days: 2))),
      // A step without a question isn't counted as a question.
      answer(now.subtract(const Duration(days: 2)), correct: null, id: 'v'),
      // Older than 7 days: not this week.
      answer(now.subtract(const Duration(days: 9))),
    ],
    curriculum: curriculum,
    now: now,
  );

  SkillState mastered(String skill, {required DateTime at, DateTime? review}) =>
      SkillState.fromJson({
        ...practising(skill).toJson(),
        'mastered_at': at.toIso8601String(),
        'next_review': review?.toIso8601String(),
      });

  test('learned, practice, home activity and effort for the last 7 days', () {
    final report = build({
      fractions: mastered(
        fractions,
        at: now.subtract(const Duration(days: 3)),
        review: DateTime(2026, 10, 5),
      ),
      equations: practising(equations, needsHelp: true),
    });
    expect(report.learned, [fractions]);
    expect(report.workingOn, [equations]);
    expect(report.needsHelp, [equations]);
    expect(report.reviews.single, (
      skill: fractions,
      day: DateTime(2026, 10, 5),
    ));
    expect(report.homeTask?.id, 'h_fold_quarters');
    expect(report.daysPractised, 2);
    expect(report.questionsAnswered, 3);
  });

  test('a skill mastered weeks ago is not "learned this week"', () {
    final report = build({
      fractions: mastered(
        fractions,
        at: now.subtract(const Duration(days: 20)),
        review: DateTime(2026, 11, 1),
      ),
    });
    expect(report.learned, isEmpty);
    expect(report.reviews, isEmpty);
  });

  test('the sentences read naturally in English and Urdu', () {
    final report = build({
      fractions: mastered(
        fractions,
        at: now.subtract(const Duration(days: 3)),
        review: DateTime(2026, 10, 5),
      ),
      equations: practising(equations, needsHelp: true),
    });
    final en = reportSentences(
      report,
      l10n: lookupAppLocalizations(const Locale('en')),
      name: 'Ayesha',
      curriculum: curriculum,
    );
    final texts = [for (final s in en) s.text];
    expect(texts.first, startsWith('This week Ayesha learned: '));
    expect(texts, contains(contains('comes back for practice on Monday')));
    expect(texts, contains(startsWith('Ayesha finds ')));
    expect(texts, contains(startsWith('Fold two paper circles')));
    expect(
      texts.last,
      'Ayesha practised on 2 of the last 7 days and answered 3 questions.',
    );
    expect({for (final s in en) s.part}, ReportPart.values.toSet());

    final ur = reportSentences(
      report,
      l10n: lookupAppLocalizations(const Locale('ur')),
      name: 'عائشہ',
      curriculum: curriculum,
    );
    expect(ur, hasLength(en.length));
    expect(ur.first.text, startsWith('اس ہفتے عائشہ نے سیکھا'));
    expect(ur.any((s) => s.text.startsWith('کاغذ')), isTrue);
  });

  test('an empty week still says something kind', () {
    final report = buildParentReport(
      states: const {},
      progress: const {},
      steps: const [],
      curriculum: curriculum,
      now: now,
    );
    final texts = [
      for (final s in reportSentences(
        report,
        l10n: lookupAppLocalizations(const Locale('en')),
        name: 'Ali',
        curriculum: curriculum,
      ))
        s.text,
    ];
    expect(texts, [
      'Ali is still working towards the next skill. That is normal; '
          'understanding takes time.',
      'Nothing needs extra practice right now.',
      'No home activity this week.',
      'Ali practised on 0 of the last 7 days and answered 0 questions.',
    ]);
  });
}
