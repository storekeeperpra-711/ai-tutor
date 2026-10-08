import 'dart:convert';
import 'dart:io';

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
  final units = courseUnits(lessons);

  test('every lesson is in exactly one unit', () {
    final ids = [for (final u in units) ...u.lessons.map((l) => l.id)];
    expect(ids.length, lessons.length);
    expect(ids.toSet(), lessons.map((l) => l.id).toSet());
    for (final u in units) {
      expect(u.lessons.every((l) => unitIdOf(l.id) == u.id), isTrue);
    }
  });

  test('every unit has a name in both languages', () {
    for (final u in units) {
      expect(unitTitles.containsKey(u.id), isTrue, reason: u.id);
    }
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

  test('Grade 6 follows the book, with each unit test last', () {
    final g6 = units.where((u) => u.id.startsWith('g6-')).toList();
    expect(g6.take(3).map((u) => u.id), [
      'g6-maths-05',
      'g6-maths-04',
      'g6-maths-13',
    ]);
    final sets = g6.firstWhere((u) => u.id == 'g6-maths-01');
    expect(sets.lessons.first.id, 'g6-maths-01-what-is-a-set');
    expect(sets.lessons.last.id, 'g6-maths-01-set-word-problems');
    final ratio = g6.firstWhere((u) => u.id == 'g6-maths-06');
    expect(ratio.lessons.last.id, 'g6-maths-06-ratio-word-problems');
  });

  test('a lesson comes after the lessons teaching what it needs', () {
    for (final unit in units) {
      final ordered = teachingOrder(unit.lessons.reversed.toList());
      final taught = <String>{};
      final inUnit = {for (final l in unit.lessons) ...l.skills};
      for (final l in ordered) {
        for (final p in l.prerequisites) {
          if (inUnit.contains(p.skill) && !l.skills.contains(p.skill)) {
            expect(taught, contains(p.skill), reason: l.id);
          }
        }
        taught.addAll(l.skills);
      }
    }
  });
}
