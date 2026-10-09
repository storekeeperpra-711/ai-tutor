import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../../app/theme/app_theme.dart';
import '../../l10n/app_localizations.dart';
import '../../lessons/lesson_text.dart';
import '../../lessons/units.dart';
import '../../models/lesson.dart';
import '../../services/local_db.dart';
import '../../services/profiles.dart';
import 'home_style.dart';

/// The child's course: how much is done, then every unit with its
/// lessons marked done, started or not started. The course is the
/// lessons of the child's class; lessons of other classes come last.
class CourseProgress extends ConsumerWidget {
  const CourseProgress({
    super.key,
    required this.student,
    required this.lessons,
  });

  final Student student;
  final List<Lesson> lessons;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final l10n = AppLocalizations.of(context);
    final progress = ref.watch(progressProvider(student.id)).value ?? const {};
    final mine = lessons.where((l) => l.grade == student.grade).toList();
    final course = mine.isEmpty ? lessons : mine;
    final others = mine.isEmpty
        ? const <Lesson>[]
        : lessons.where((l) => l.grade != student.grade).toList();
    final done = course.where((l) => progress[l.id]?.completed == true).length;
    final domains = courseDomains(course);
    final units = [for (final d in domains) ...d.units];
    // Open the first unit that isn't finished, so the next lesson shows.
    final open = units
        .where((u) => u.lessons.any((l) => progress[l.id]?.completed != true))
        .firstOrNull;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        _CourseCard(done: done, total: course.length),
        const SizedBox(height: 16),
        for (final domain in domains)
          ..._domain(context, domain, progress, open),
        if (others.isNotEmpty) ...[
          const SizedBox(height: 8),
          Text(
            l10n.otherLessons,
            style: Theme.of(context).textTheme.titleLarge,
          ),
          const SizedBox(height: 8),
          for (final domain in courseDomains(others))
            ..._domain(context, domain, progress, null),
        ],
      ],
    );
  }

  /// A domain's heading (like "Numbers and Operations"), then its units.
  List<Widget> _domain(
    BuildContext context,
    CourseDomain domain,
    Map<String, LessonProgress> progress,
    CourseUnit? open,
  ) => [
    if (domain.title case final title?)
      Padding(
        padding: const EdgeInsets.only(top: 8, bottom: 8),
        child: LessonText(
          title,
          key: Key('domain-${domain.units.first.id}'),
          style: Theme.of(context).textTheme.titleLarge,
        ),
      ),
    for (final unit in domain.units)
      _UnitCard(unit: unit, progress: progress, open: unit == open),
  ];
}

/// The share of the course done, as a big number and a bar.
class _CourseCard extends StatelessWidget {
  const _CourseCard({required this.done, required this.total});

  final int done;
  final int total;

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final theme = Theme.of(context);
    final percent = total == 0 ? 0 : (done * 100 / total).floor();
    return Container(
      key: const Key('course-card'),
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(AppRadius.card),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Text(l10n.courseTitle, style: theme.textTheme.titleMedium),
          const SizedBox(height: 4),
          Text(
            l10n.coursePercent(percent),
            key: const Key('course-percent'),
            style: theme.textTheme.headlineMedium?.copyWith(
              color: AppColors.greenDark,
              fontWeight: FontWeight.w900,
            ),
          ),
          const SizedBox(height: 8),
          ClipRRect(
            borderRadius: BorderRadius.circular(999),
            child: LinearProgressIndicator(
              value: total == 0 ? 0 : done / total,
              minHeight: 12,
              color: AppColors.green,
              backgroundColor: AppColors.greenSoft,
            ),
          ),
          const SizedBox(height: 8),
          Text(
            l10n.courseLessonsDone(done, total),
            key: const Key('course-lessons-done'),
            style: const TextStyle(fontWeight: FontWeight.w800),
          ),
          const SizedBox(height: 8),
          Text(
            l10n.courseDoneMeans,
            style: theme.textTheme.bodySmall?.copyWith(color: AppColors.muted),
          ),
        ],
      ),
    );
  }
}

/// One unit: its name, how many lessons are done, and (opened) its lessons.
class _UnitCard extends StatelessWidget {
  const _UnitCard({
    required this.unit,
    required this.progress,
    required this.open,
  });

  final CourseUnit unit;
  final Map<String, LessonProgress> progress;
  final bool open;

  @override
  Widget build(BuildContext context) {
    final done = unit.lessons
        .where((l) => progress[l.id]?.completed == true)
        .length;
    final total = unit.lessons.length;
    final finished = done == total;
    return Padding(
      padding: const EdgeInsets.only(bottom: 8),
      child: Material(
        color: Colors.white,
        borderRadius: BorderRadius.circular(AppRadius.tile),
        clipBehavior: Clip.antiAlias,
        child: ExpansionTile(
          key: Key('unit-${unit.id}'),
          initiallyExpanded: open,
          shape: const Border(),
          leading: Icon(
            finished ? Icons.check_circle_rounded : Icons.folder_rounded,
            color: finished ? AppColors.green : AppColors.lilac,
          ),
          title: LessonText(
            unit.title,
            style: const TextStyle(fontWeight: FontWeight.w900),
          ),
          subtitle: Padding(
            padding: const EdgeInsets.only(top: 6),
            child: Row(
              children: [
                Expanded(
                  child: TileProgress(
                    value: total == 0 ? 0 : done / total,
                    color: AppColors.green,
                  ),
                ),
                const SizedBox(width: 8),
                Text(
                  '$done / $total',
                  key: Key('unit-done-${unit.id}'),
                  style: const TextStyle(fontWeight: FontWeight.w800),
                ),
              ],
            ),
          ),
          children: [
            for (final lesson in unit.lessons)
              _LessonRow(lesson: lesson, progress: progress[lesson.id]),
          ],
        ),
      ),
    );
  }
}

/// A lesson with a tick (done), a half circle (started) or an empty
/// circle (not started).
class _LessonRow extends StatelessWidget {
  const _LessonRow({required this.lesson, required this.progress});

  final Lesson lesson;
  final LessonProgress? progress;

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final (icon, color, status) = switch (progress) {
      null => (
        Icons.radio_button_unchecked_rounded,
        AppColors.muted,
        l10n.lessonNotStarted,
      ),
      LessonProgress(completed: true) => (
        Icons.check_circle_rounded,
        AppColors.green,
        l10n.lessonDone,
      ),
      final p => (
        Icons.timelapse_rounded,
        AppColors.orange,
        l10n.lessonAtStep(p.nextStep + 1, lesson.steps.length),
      ),
    };
    return ListTile(
      key: Key('course-lesson-${lesson.id}'),
      leading: Icon(icon, color: color),
      title: LessonText(lesson.title),
      subtitle: Text(
        status,
        key: Key('course-lesson-status-${lesson.id}'),
        style: TextStyle(color: color, fontWeight: FontWeight.w700),
      ),
      onTap: () => context.push('/lesson/${lesson.id}'),
    );
  }
}
