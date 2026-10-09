import 'dart:convert';
import 'dart:io';

import 'package:ai_tutor/lessons/hidden_units.dart';
import 'package:ai_tutor/lessons/units.dart';
import 'package:ai_tutor/models/lesson.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  final lessons = [
    for (final f in Directory('content/lessons').listSync().whereType<File>())
      if (f.path.endsWith('.json'))
        Lesson.fromJson(
          jsonDecode(f.readAsStringSync()) as Map<String, dynamic>,
        ),
  ];
  final domains = courseDomains(lessons);
  final units = [for (final d in domains) ...d.units];

  test('every lesson is in exactly one unit', () {
    final ids = [for (final u in units) ...u.lessons.map((l) => l.id)];
    expect(ids.length, lessons.length);
    expect(ids.toSet(), lessons.map((l) => l.id).toSet());
  });

  test('the book lists real lessons, each once', () {
    final ids = lessons.map((l) => l.id).toSet();
    final listed = [
      for (final d in grade6Book)
        for (final c in d.chapters) ...c.lessons,
    ];
    expect(listed.toSet().length, listed.length);
    for (final id in listed) {
      expect(ids, contains(id), reason: id);
      expect(isHiddenLesson(id), isFalse, reason: id);
    }
  });

  test('every shown Grade 6 lesson is in a chapter of the book', () {
    final listed = {
      for (final d in grade6Book)
        for (final c in d.chapters) ...c.lessons,
    };
    for (final l in lessons.where((l) => l.grade == 6)) {
      if (isHiddenLesson(l.id)) continue;
      expect(listed, contains(l.id), reason: l.id);
    }
  });

  test('Grade 6 follows the book contents', () {
    expect(domains.take(5).map((d) => d.title!.en), [
      '1. Numbers and Operations',
      '2. Algebra',
      '3. Measurement',
      '4. Geometry',
      '5. Statistics and Probability',
    ]);
    expect(domains.first.units.map((u) => u.title.en), [
      'Factors and Multiples',
      'Integers',
      'Laws of Integers',
      'Rate, Ratio and Percentage',
      'Sets',
    ]);
    expect(units.where((u) => u.id.startsWith('g6-book-')).length, 12);
    // The off-book units come after the book.
    expect(domains[5].title, morePractice);
    expect(domains[5].units.map((u) => u.id), [
      'g6-maths-02',
      'g6-maths-03',
      'g6-maths-12',
      'g6-maths-15',
    ]);
    expect(domains.last.title, isNull);
  });

  test('the lesson order lists real lessons, each once', () {
    final ids = lessons.map((l) => l.id).toSet();
    for (final MapEntry(key: unit, value: order) in lessonOrder.entries) {
      expect(order.toSet().length, order.length, reason: unit);
      for (final id in order) {
        expect(ids, contains(id), reason: id);
        expect(unitIdOf(id), unit, reason: id);
      }
    }
  });

  test('a lesson comes after the lessons teaching what it needs', () {
    for (final unit in units) {
      final taught = <String>{};
      final inUnit = {for (final l in unit.lessons) ...l.skills};
      for (final l in unit.lessons) {
        for (final p in l.prerequisites) {
          if (inUnit.contains(p.skill) && !l.skills.contains(p.skill)) {
            expect(taught, contains(p.skill), reason: '${unit.id}: ${l.id}');
          }
        }
        taught.addAll(l.skills);
      }
    }
  });
}
