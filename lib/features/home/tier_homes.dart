import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../../app/theme/age_tier.dart';
import '../../character/feel_settings.dart';
import '../../character/mithu_bubble.dart';
import '../../l10n/app_localizations.dart';
import '../../lessons/lesson_text.dart';
import '../../models/lesson.dart';
import '../../models/lesson_step.dart';
import '../../models/localized_text.dart';
import '../../services/local_db.dart';
import '../../services/profiles.dart';
import '../ai/mithu_notes.dart';
import '../effort/badge_shelf.dart';
import '../plan/today_plan_card.dart';
import 'home_parts.dart';

/// Home for Grades 3 to 5: a quest, subject tiles, badges and one tip.
class PrimaryHome extends ConsumerWidget {
  const PrimaryHome({super.key, required this.student});

  final Student student;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final all = ref.watch(visibleLessonsProvider);
    final lessons = lessonsForTier(all, AgeTier.primary);
    final progress = ref.watch(progressProvider(student.id)).value ?? const {};
    final summaries = ref.watch(subjectSummariesProvider(student.id));
    return Column(
      key: const Key('primary-home'),
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        _MithuTip(day: DateTime.now().day),
        const SizedBox(height: 8),
        if (lessons.isNotEmpty)
          QuestCard(
            subject: lessons.first.subject,
            lessons: [
              for (final l in lessons)
                if (l.subject == lessons.first.subject) l,
            ],
            progress: progress,
          ),
        TodayPlanCard(student: student),
        MithuNotesCard(student: student),
        const SizedBox(height: 16),
        _SubjectTiles(
          summaries: summaries,
          label: (l10n, s) => l10n.secureSkills(s.secure, s.skills),
        ),
        const SizedBox(height: 16),
        BadgeShelf(studentId: student.id),
        const SizedBox(height: 16),
        LessonList(student: student, lessons: all),
      ],
    );
  }
}

/// Home for Grades 6 to 8: today's challenges, levels per subject and a
/// badge collection. Mithu stays small.
class MiddleHome extends ConsumerWidget {
  const MiddleHome({super.key, required this.student});

  final Student student;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final lessons = ref.watch(visibleLessonsProvider);
    final summaries = ref.watch(subjectSummariesProvider(student.id));
    return Column(
      key: const Key('middle-home'),
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        if (ref.watch(mithuOnProvider)) _MithuTip(day: DateTime.now().day),
        TodayPlanCard(student: student),
        MithuNotesCard(student: student),
        const SizedBox(height: 16),
        _SubjectTiles(
          summaries: summaries,
          label: (l10n, s) => l10n.subjectLevel(s.level),
          detail: (l10n, s) => l10n.masteredSkills(s.mastered, s.skills),
        ),
        const SizedBox(height: 16),
        BadgeShelf(studentId: student.id, compact: true),
        const SizedBox(height: 16),
        LessonList(student: student, lessons: lessons),
      ],
    );
  }
}

/// Home for Grades 9 to 12: clean and focused. Today's 15-minute plan,
/// the board exam countdown, mastery by subject and AI notes.
class OlderHome extends ConsumerWidget {
  const OlderHome({super.key, required this.student});

  final Student student;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final l10n = AppLocalizations.of(context);
    final lessons = ref.watch(visibleLessonsProvider);
    final summaries = ref.watch(subjectSummariesProvider(student.id));
    return Column(
      key: const Key('older-home'),
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        if (ref.watch(mithuOnProvider)) _MithuTip(day: DateTime.now().day),
        const ExamCountdownCard(),
        TodayPlanCard(student: student),
        MithuNotesCard(student: student),
        const SizedBox(height: 16),
        Text(
          l10n.masteryBySubject,
          style: Theme.of(context).textTheme.titleLarge,
        ),
        for (final s in summaries)
          Padding(
            key: Key('subject-mastery-${s.subject}'),
            padding: const EdgeInsets.symmetric(vertical: 6),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    Expanded(child: Text(subjectName(l10n, s.subject))),
                    const SizedBox(width: 8),
                    Flexible(
                      flex: 2,
                      child: Text(
                        l10n.masteredSkills(s.mastered, s.skills),
                        textAlign: TextAlign.end,
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 4),
                LinearProgressIndicator(
                  value: s.skills == 0 ? 0 : s.mastered / s.skills,
                  minHeight: 6,
                  borderRadius: BorderRadius.circular(3),
                ),
              ],
            ),
          ),
        const SizedBox(height: 16),
        LessonList(student: student, lessons: lessons),
      ],
    );
  }
}

/// Days to the board exam, or a prompt to set the date.
class ExamCountdownCard extends ConsumerWidget {
  const ExamCountdownCard({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final l10n = AppLocalizations.of(context);
    final exam = ref.watch(examDateProvider);
    final days = exam == null ? null : daysUntil(exam, DateTime.now());
    if (days != null && days < 0) return const SizedBox.shrink();
    return Card(
      key: const Key('exam-countdown'),
      child: ListTile(
        leading: const Icon(Icons.event_rounded),
        title: Text(switch (days) {
          null => l10n.examSetPrompt,
          0 => l10n.examToday,
          final d => l10n.examCountdown(d),
        }),
        trailing: days == null ? const Icon(Icons.chevron_right) : null,
        onTap: days == null ? () => context.push('/settings') : null,
      ),
    );
  }
}

/// The current quest: a chain of lessons in one subject.
class QuestCard extends StatelessWidget {
  const QuestCard({
    super.key,
    required this.subject,
    required this.lessons,
    required this.progress,
  });

  final String subject;
  final List<Lesson> lessons;
  final Map<String, LessonProgress> progress;

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final theme = Theme.of(context);
    final done = lessons.where((l) => progress[l.id]?.completed == true).length;
    final next = nextLessonFor(lessons, progress);
    final finished = done == lessons.length;
    return Card(
      key: const Key('quest-card'),
      color: theme.colorScheme.tertiaryContainer,
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Row(
              children: [
                const Icon(Icons.explore_rounded, size: 32),
                const SizedBox(width: 8),
                Expanded(
                  child: Text(
                    l10n.questTitle(subjectName(l10n, subject)),
                    style: theme.textTheme.titleLarge,
                  ),
                ),
              ],
            ),
            const SizedBox(height: 8),
            LinearProgressIndicator(
              value: lessons.isEmpty ? 0 : done / lessons.length,
              minHeight: 10,
              borderRadius: BorderRadius.circular(5),
            ),
            const SizedBox(height: 4),
            Text(l10n.questProgress(done, lessons.length)),
            const SizedBox(height: 8),
            if (finished)
              Text(l10n.questDone)
            else if (next != null)
              FilledButton.icon(
                key: const Key('quest-next'),
                icon: const Icon(Icons.play_arrow_rounded),
                label: LessonText(next.title),
                onPressed: () => context.push('/lesson/${next.id}'),
              ),
          ],
        ),
      ),
    );
  }
}

class _SubjectTiles extends StatelessWidget {
  const _SubjectTiles({
    required this.summaries,
    required this.label,
    this.detail,
  });

  final List<SubjectSummary> summaries;
  final String Function(AppLocalizations, SubjectSummary) label;
  final String Function(AppLocalizations, SubjectSummary)? detail;

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final theme = Theme.of(context);
    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        Text(l10n.subjectsTitle, style: theme.textTheme.titleLarge),
        const SizedBox(height: 8),
        Wrap(
          spacing: 8,
          runSpacing: 8,
          children: [
            for (final s in summaries)
              SizedBox(
                width: 160,
                child: Card(
                  key: Key('subject-${s.subject}'),
                  margin: EdgeInsets.zero,
                  child: Padding(
                    padding: const EdgeInsets.all(12),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          subjectName(l10n, s.subject),
                          style: theme.textTheme.titleMedium,
                        ),
                        const SizedBox(height: 4),
                        Text(label(l10n, s), style: theme.textTheme.bodyLarge),
                        if (detail != null)
                          Text(
                            detail!(l10n, s),
                            style: theme.textTheme.bodySmall,
                          ),
                      ],
                    ),
                  ),
                ),
              ),
          ],
        ),
      ],
    );
  }
}

/// One of Mithu's tips, a different one on different days.
class _MithuTip extends ConsumerWidget {
  const _MithuTip({required this.day});

  final int day;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    String tip(AppLocalizations l) => switch (day % 3) {
      0 => l.mithuTip1,
      1 => l.mithuTip2,
      _ => l.mithuTip3,
    };
    return MithuBubble(
      key: const Key('mithu-tip'),
      line: CharacterLine(
        emotion: 'encouraging',
        say: LocalizedText(
          en: tip(lookupAppLocalizations(const Locale('en'))),
          ur: tip(lookupAppLocalizations(const Locale('ur'))),
        ),
      ),
    );
  }
}
