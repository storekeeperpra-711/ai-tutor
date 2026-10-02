import 'dart:convert';
import 'dart:io';

import 'package:ai_tutor/models/lesson.dart';

/// Every lesson file, read straight from content/lessons/.
List<Lesson> loadLessons() =>
    Directory('content/lessons')
        .listSync()
        .whereType<File>()
        .where((f) => f.path.endsWith('.json'))
        .map((f) => loadLessonJson(jsonDecode(f.readAsStringSync())))
        .toList();

Lesson loadLessonJson(Object? json) =>
    Lesson.fromJson(json! as Map<String, dynamic>);

Map<String, dynamic> lessonJson(String id) =>
    jsonDecode(File('content/lessons/$id.json').readAsStringSync())
        as Map<String, dynamic>;

const fractions = 'maths.fractions.divide_by_fraction';
const equations = 'maths.linear_equations.solve_two_step';
const balancing = 'chemistry.stoichiometry.balance_equations';
