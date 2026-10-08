import 'dart:convert';

import 'package:flutter/services.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../classes/class_store.dart';
import '../lessons/hidden_units.dart';
import '../lessons/lesson_repository.dart';
import '../lessons/lesson_updates.dart';
import '../mastery/curriculum.dart';
import '../mastery/skill_state.dart';
import '../models/lesson.dart';
import '../services/remote_store.dart';

/// Every lesson for the dashboard: the ones bundled with the app, replaced
/// or joined by newer ones published to Firestore. The website has no
/// phone database, so it reads them straight away each time it opens.
/// Hidden units are left out, as in the app.
Future<Curriculum> loadDashboardCurriculum(
  RemoteStore remote, {
  Set<String> hidden = hiddenUnits,
}) async {
  final lessons = <String, Lesson>{};
  final manifest = await AssetManifest.loadFromAssetBundle(rootBundle);
  for (final path in manifest.listAssets()) {
    if (!path.startsWith(lessonsFolder) || !path.endsWith('.json')) continue;
    try {
      final lesson = Lesson.fromJson(
        jsonDecode(await loadLessonText(path)) as Map<String, dynamic>,
      );
      lessons[lesson.id] = lesson;
    } catch (_) {
      // Skipped, like in the app.
    }
  }
  try {
    final catalog = await remote.fetchLessonCatalog();
    for (final MapEntry(key: id, value: entry) in catalog.entries) {
      if ((lessons[id]?.version ?? 0) >= entry.version) continue;
      final published = await remote.fetchPublishedLesson(id);
      if (published == null || published.format > supportedLessonFormat) {
        continue;
      }
      try {
        lessons[id] = Lesson.fromJson(
          jsonDecode(published.content) as Map<String, dynamic>,
        );
      } catch (_) {
        // A broken lesson is left out.
      }
    }
  } catch (_) {
    // Without the catalog, the bundled lessons still work.
  }
  return Curriculum([
    for (final lesson in lessons.values)
      if (!isHiddenLesson(lesson.id, hidden)) lesson,
  ]);
}

/// One student's level in one skill, for the grid.
MasteryLevel memberLevel(ClassMember member, String skill) {
  final level = member.skills.where((s) => s.skill == skill).firstOrNull?.level;
  return MasteryLevel.values.where((l) => l.name == level).firstOrNull ??
      MasteryLevel.notStarted;
}

/// The skills any student in the class has started, in curriculum order
/// (grade, then lesson), then any the curriculum doesn't know.
List<String> classSkills(List<ClassMember> members, Curriculum? curriculum) {
  final started = {
    for (final m in members)
      for (final s in m.skills) s.skill,
  };
  final ordered = <String>[
    for (final lesson in curriculum?.lessons ?? const <Lesson>[])
      for (final skill in lesson.skills)
        if (started.contains(skill)) skill,
  ];
  final seen = <String>{};
  return [
    for (final s in ordered)
      if (seen.add(s)) s,
    for (final s in started.toList()..sort())
      if (seen.add(s)) s,
  ];
}

/// A misconception and who showed it, with how often.
typedef ClassMistake = ({
  String lessonId,
  String id,
  List<({String name, int count})> students,
});

/// The class's misconceptions, the ones most students showed first.
List<ClassMistake> classMistakes(List<ClassMember> members) {
  final who = <(String, String), List<({String name, int count})>>{};
  for (final m in members) {
    for (final x in m.misconceptions) {
      (who[(x.lessonId, x.id)] ??= []).add((name: m.firstName, count: x.count));
    }
  }
  int total(List<({String name, int count})> s) =>
      s.fold(0, (sum, e) => sum + e.count);
  final list = [
    for (final MapEntry(key: (lessonId, id), value: students) in who.entries)
      (lessonId: lessonId, id: id, students: students),
  ];
  list.sort((a, b) {
    final byStudents = b.students.length.compareTo(a.students.length);
    return byStudents != 0
        ? byStudents
        : total(b.students).compareTo(total(a.students));
  });
  return list;
}

/// Students marked "needs help", with the skill and the day last tried.
typedef StuckStudent = ({String name, String skill, String? lastDay});

List<StuckStudent> stuckStudents(List<ClassMember> members) => [
  for (final m in members)
    for (final s in m.skills)
      if (s.needsHelp) (name: m.firstName, skill: s.skill, lastDay: s.lastDay),
]..sort((a, b) => a.name.compareTo(b.name));

/// The lesson's own words for a misconception (written for teachers).
String describeMistake(Curriculum? curriculum, String lessonId, String id) {
  final lesson = curriculum?.lesson(lessonId);
  for (final m in lesson?.misconceptions ?? const <Misconception>[]) {
    if (m.id == id) return m.description;
  }
  return id;
}

/// The dashboard's lessons; it stands in for the app's `curriculumProvider`.
final dashboardCurriculumProvider = FutureProvider<Curriculum>(
  (ref) => loadDashboardCurriculum(
    ref.watch(remoteStoreProvider),
    hidden: ref.watch(hiddenUnitsProvider),
  ),
);
