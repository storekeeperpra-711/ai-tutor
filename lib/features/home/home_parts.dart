import 'package:flutter/foundation.dart';
import 'package:flutter/services.dart' show appFlavor;
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../app/preferences.dart';
import '../../app/theme/age_tier.dart';
import '../../l10n/app_localizations.dart';
import '../../lessons/lesson_repository.dart';
import '../../mastery/skill_state.dart';
import '../../models/lesson.dart';
import '../../services/local_db.dart';
import '../../services/mastery_service.dart';
import '../../services/profiles.dart';

String subjectName(AppLocalizations l10n, String subject) => switch (subject) {
  'maths' => l10n.subjectMaths,
  'chemistry' => l10n.subjectChemistry,
  'physics' => l10n.subjectPhysics,
  'biology' => l10n.subjectBiology,
  'science' => l10n.subjectScience,
  'english' => l10n.subjectEnglish,
  'urdu' => l10n.subjectUrdu,
  _ => subject[0].toUpperCase() + subject.substring(1).replaceAll('_', ' '),
};

/// Whether lessons a teacher has not approved yet are shown. Only the dev
/// test app (and debug builds) shows them, so lessons can be tried before
/// review; the prod app shows approved lessons only.
final showDraftLessonsProvider = Provider<bool>(
  (ref) => kDebugMode || appFlavor == 'dev',
);

/// The lessons a child sees: reviewed ones, plus drafts in the dev app.
final visibleLessonsProvider = Provider<List<Lesson>>((ref) {
  final ids = ref.watch(lessonIdsProvider).value ?? const <String>[];
  final drafts = ref.watch(showDraftLessonsProvider);
  return [
    for (final id in ids)
      if (ref.watch(lessonProvider(id)).value case final lesson?)
        if (lesson.review.isApproved || drafts) lesson,
  ];
});

/// Lessons made for [tier]; all lessons if there are none yet.
List<Lesson> lessonsForTier(List<Lesson> lessons, AgeTier tier) {
  final mine = lessons.where((l) => l.tier == tier.name).toList();
  return mine.isEmpty ? lessons : mine;
}

/// How far a child is in one subject.
class SubjectSummary {
  const SubjectSummary({
    required this.subject,
    required this.skills,
    required this.mastered,
    required this.secure,
  });

  final String subject;
  final int skills;

  /// Mastered or Secure.
  final int mastered;
  final int secure;

  /// Level 1, plus one per skill mastered.
  int get level => 1 + mastered;
}

List<SubjectSummary> subjectSummaries(
  List<Lesson> lessons,
  Map<String, SkillState> states,
  MasteryCriteria? Function(String skill) criteriaFor,
) {
  final skills = <String, Set<String>>{};
  for (final l in lessons) {
    (skills[l.subject] ??= {}).addAll(l.skills);
  }
  return [
    for (final MapEntry(key: subject, value: set) in skills.entries)
      SubjectSummary(
        subject: subject,
        skills: set.length,
        mastered: set
            .where(
              (s) =>
                  (states[s]?.level(criteriaFor(s)).index ?? 0) >=
                  MasteryLevel.mastered.index,
            )
            .length,
        secure: set
            .where(
              (s) => states[s]?.level(criteriaFor(s)) == MasteryLevel.secure,
            )
            .length,
      ),
  ];
}

/// The subject summaries for a child, from their saved mastery.
final subjectSummariesProvider = Provider.family<List<SubjectSummary>, String>((
  ref,
  studentId,
) {
  final lessons = ref.watch(visibleLessonsProvider);
  final states = ref.watch(skillStatesProvider(studentId)).value ?? {};
  final curriculum = ref.watch(curriculumProvider).value;
  return subjectSummaries(lessons, states, (s) => curriculum?.criteriaFor(s));
});

/// The first lesson not finished yet, else the first one.
Lesson? nextLessonFor(
  List<Lesson> lessons,
  Map<String, LessonProgress> progress,
) =>
    lessons.where((l) => progress[l.id]?.completed != true).firstOrNull ??
    lessons.firstOrNull;

/// The board exam date of the child using the app (Phase 7 decision 6),
/// kept on this phone per child.
final examDateProvider = NotifierProvider<ExamDate, DateTime?>(ExamDate.new);

class ExamDate extends Notifier<DateTime?> {
  String? get _key {
    final id = ref.read(currentStudentProvider)?.id;
    return id == null ? null : 'examDate.$id';
  }

  @override
  DateTime? build() {
    ref.watch(currentStudentProvider);
    final key = _key;
    final text = key == null
        ? null
        : ref.read(sharedPreferencesProvider).getString(key);
    return text == null ? null : DateTime.tryParse(text);
  }

  Future<void> set(DateTime? date) async {
    final key = _key;
    if (key == null) return;
    state = date;
    final prefs = ref.read(sharedPreferencesProvider);
    if (date == null) {
      await prefs.remove(key);
    } else {
      await prefs.setString(key, date.toIso8601String().substring(0, 10));
    }
  }
}

/// Whole days from [now] to [exam] (0 on the day).
int daysUntil(DateTime exam, DateTime now) => DateTime.utc(
  exam.year,
  exam.month,
  exam.day,
).difference(DateTime.utc(now.year, now.month, now.day)).inDays;
