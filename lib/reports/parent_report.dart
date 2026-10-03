import 'package:intl/intl.dart';

import '../l10n/app_localizations.dart';
import '../mastery/curriculum.dart';
import '../mastery/skill_state.dart';
import '../models/lesson.dart';
import '../services/local_db.dart';

/// What happened in a child's last 7 days, made on the phone from the
/// child's own data: no internet and no AI (Phase 9, task 9.1).
class ParentReport {
  const ParentReport({
    required this.learned,
    required this.workingOn,
    required this.reviews,
    required this.needsHelp,
    required this.homeTask,
    required this.daysPractised,
    required this.questionsAnswered,
  });

  /// Skills mastered (or made secure) this week.
  final List<String> learned;

  /// Skills practised this week and not mastered yet.
  final List<String> workingOn;

  /// Skills the app brings back soon, with the day.
  final List<({String skill, DateTime day})> reviews;

  /// Skills the child is stuck on.
  final List<String> needsHelp;

  /// One thing to do at home, from the lesson the child is working on.
  final HomeTask? homeTask;

  /// Days of the last 7 with at least one answer.
  final int daysPractised;
  final int questionsAnswered;
}

/// Builds the report for the 7 days up to [now].
ParentReport buildParentReport({
  required Map<String, SkillState> states,
  required Map<String, LessonProgress> progress,
  required List<StepResultRow> steps,
  required Curriculum curriculum,
  required DateTime now,
}) {
  final weekStart = dayOf(now).subtract(const Duration(days: 6));
  bool thisWeek(DateTime? t) => t != null && !t.isBefore(weekStart);

  final learned = <String>[];
  final workingOn = <String>[];
  final reviews = <({String skill, DateTime day})>[];
  final needsHelp = <String>[];
  final sorted = states.values.toList()
    ..sort((a, b) => a.skill.compareTo(b.skill));
  for (final s in sorted) {
    final level = s.level(curriculum.criteriaFor(s.skill));
    if (thisWeek(s.masteredAt) || thisWeek(s.secureAt)) {
      learned.add(s.skill);
    } else if (thisWeek(s.lastAnswered) &&
        (level == MasteryLevel.learning || level == MasteryLevel.practising)) {
      workingOn.add(s.skill);
    }
    if (s.needsHelp) needsHelp.add(s.skill);
    final next = s.nextReview;
    if (next != null &&
        dayOf(next).difference(dayOf(now)).inDays <= 7 &&
        level.index >= MasteryLevel.mastered.index) {
      reviews.add((
        skill: s.skill,
        day: dayOf(next).isBefore(dayOf(now)) ? dayOf(now) : dayOf(next),
      ));
    }
  }
  reviews.sort((a, b) => a.day.compareTo(b.day));

  // The lesson worked on most recently, unfinished first.
  final recent = progress.values.toList()
    ..sort((a, b) {
      if (a.completed != b.completed) return a.completed ? 1 : -1;
      return b.updatedAt.compareTo(a.updatedAt);
    });
  HomeTask? homeTask;
  for (final p in recent) {
    final tasks = curriculum.lesson(p.lessonId)?.homeTasks ?? const [];
    if (tasks.isEmpty) continue;
    // A different task each week, the same all week.
    final week = weekStart.difference(DateTime(2026)).inDays ~/ 7;
    homeTask = tasks[week % tasks.length];
    break;
  }

  final answered = steps.where((r) => thisWeek(r.answeredAt)).toList();
  return ParentReport(
    learned: learned,
    workingOn: workingOn,
    reviews: reviews,
    needsHelp: needsHelp,
    homeTask: homeTask,
    daysPractised: {for (final r in answered) dayKey(r.answeredAt)}.length,
    questionsAnswered: answered.where((r) => r.correct != null).length,
  );
}

/// The report's parts, each with a picture on screen.
enum ReportPart { learned, practice, home, effort }

/// One sentence of the report, read aloud and highlighted in turn.
typedef ReportSentence = ({ReportPart part, String text});

/// The report as sentences in [l10n]'s language, for the screen and for
/// the phone's voice.
List<ReportSentence> reportSentences(
  ParentReport report, {
  required AppLocalizations l10n,
  required String name,
  required Curriculum curriculum,
}) {
  final lang = l10n.localeName;
  String title(String skill) =>
      curriculum.titleOf(skill)?.inLanguage(lang) ?? skill;
  String list(List<String> skills) =>
      skills.map(title).join(lang == 'ur' ? '، ' : ', ');
  final weekday = DateFormat.EEEE(lang);

  return [
    if (report.learned.isNotEmpty)
      (
        part: ReportPart.learned,
        text: l10n.reportLearned(name, list(report.learned)),
      )
    else
      (part: ReportPart.learned, text: l10n.reportLearnedNone(name)),
    if (report.workingOn.isNotEmpty)
      (
        part: ReportPart.learned,
        text: l10n.reportWorkingOn(list(report.workingOn)),
      ),
    for (final skill in report.needsHelp)
      (
        part: ReportPart.practice,
        text: l10n.reportNeedsHelp(name, title(skill)),
      ),
    for (final r in report.reviews)
      (
        part: ReportPart.practice,
        text: l10n.reportReview(title(r.skill), weekday.format(r.day)),
      ),
    if (report.needsHelp.isEmpty && report.reviews.isEmpty)
      (part: ReportPart.practice, text: l10n.reportPracticeNone),
    if (report.homeTask case final task?)
      (part: ReportPart.home, text: task.text.inLanguage(lang))
    else
      (part: ReportPart.home, text: l10n.reportHomeNone),
    (
      part: ReportPart.effort,
      text: l10n.reportEffort(
        name,
        report.daysPractised,
        report.questionsAnswered,
      ),
    ),
  ];
}
