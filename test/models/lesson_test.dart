import 'dart:convert';
import 'dart:io';

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
