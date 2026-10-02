import 'dart:convert';
import 'dart:io';

import 'package:ai_tutor/checkers/chem_equation_checker.dart';
import 'package:ai_tutor/checkers/linear_equation_checker.dart';
import 'package:ai_tutor/checkers/numeric_checker.dart';
import 'package:ai_tutor/models/lesson.dart';
import 'package:ai_tutor/models/lesson_step.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  final files = Directory('content/lessons')
      .listSync()
      .whereType<File>()
      .where((f) => f.path.endsWith('.json'))
      .toList();

  test('there is at least one lesson', () => expect(files, isNotEmpty));

  for (final file in files) {
    test('${file.uri.pathSegments.last} loads into the Dart models', () {
      final lesson = Lesson.fromJson(
        jsonDecode(file.readAsStringSync()) as Map<String, dynamic>,
      );
      expect(lesson.schema, '0.2');
      expect(lesson.steps, isNotEmpty);
      expect(lesson.steps.last, isA<SummaryStep>());

      // Every checked answer in the lesson must be readable by its checker,
      // so a typo in a lesson file can't make a question impossible.
      final questionSteps = [
        ...lesson.steps,
        for (final qs in lesson.questionBank.values)
          for (final q in qs) q.step,
        for (final q in lesson.reviewQuestions) q.step,
        for (final alt in lesson.alternatives) ...alt.steps,
      ];
      for (final step in questionSteps.whereType<TextCheckStep>()) {
        final reason = '${lesson.id}/${step.id}';
        switch (step.checker) {
          case 'chem_equation':
            expect(
              checkChemEquation(step.expected, step.expected).isCorrect,
              isTrue,
              reason: reason,
            );
          case 'linear_equation':
            expect(
              parseLinearEquation(
                step.expected,
                variable: step.variable,
              ).solution,
              isA<OneSolution>(),
              reason: reason,
            );
          case 'fraction':
            expect(parseRational(step.expected), isNotNull, reason: reason);
        }
      }
    });
  }

  test('the first lesson has the expected steps', () {
    final lesson = Lesson.fromJson(
      jsonDecode(
        File('content/lessons/g6-maths-02-dividing-fractions.json')
            .readAsStringSync(),
      ) as Map<String, dynamic>,
    );
    expect(lesson.steps.map((s) => s.type), [
      'explain',
      'choice',
      'choice',
      'explain',
      'number',
      'explain',
      'choice',
      'number',
      'summary',
    ]);
    final quarters = lesson.steps[4] as NumberStep;
    expect(quarters.answer, 8);
    expect(quarters.commonWrong.first.misconceptionId, 'divide_by_denominator');
  });

  test('unknown step types load as UnsupportedStep', () {
    final step = LessonStep.fromJson({'id': 'v1', 'type': 'video'});
    expect(step, isA<UnsupportedStep>());
    expect(step.type, 'video');
  });
}
