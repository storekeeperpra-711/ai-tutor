import 'dart:convert';
import 'dart:io';

import 'package:ai_tutor/features/home/home_parts.dart';
import 'package:ai_tutor/lessons/lesson_repository.dart';
import 'package:ai_tutor/models/lesson.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  Lesson load(String id, String status) {
    final json = jsonDecode(
      File('content/lessons/$id.json').readAsStringSync(),
    ) as Map<String, dynamic>;
    json['review'] = {'status': status};
    return Lesson.fromJson(json);
  }

  final lessons = {
    'g6-maths-02-adding-fractions': load(
      'g6-maths-02-adding-fractions',
      'draft',
    ),
    'g9-maths-05-linear-programming': load(
      'g9-maths-05-linear-programming',
      'approved',
    ),
  };

  Future<List<String>> visible({required bool drafts}) async {
    final container = ProviderContainer(
      overrides: [
        showDraftLessonsProvider.overrideWithValue(drafts),
        lessonIdsProvider.overrideWith((ref) async => lessons.keys.toList()),
        lessonProvider.overrideWith((ref, id) async => lessons[id]!),
      ],
    );
    addTearDown(container.dispose);
    await container.read(lessonIdsProvider.future);
    for (final id in lessons.keys) {
      await container.read(lessonProvider(id).future);
    }
    return [for (final l in container.read(visibleLessonsProvider)) l.id];
  }

  test('the dev test app shows lessons still waiting for review', () async {
    expect(await visible(drafts: true), [
      'g6-maths-02-adding-fractions',
      'g9-maths-05-linear-programming',
    ]);
  });

  test('the prod app shows approved lessons only', () async {
    expect(await visible(drafts: false), ['g9-maths-05-linear-programming']);
  });
}
