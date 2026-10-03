import 'dart:async';

import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../../classes/class_service.dart';
import '../../l10n/app_localizations.dart';
import '../../lessons/lesson_text.dart';
import '../../mastery/daily_plan.dart';
import '../../mastery/skill_state.dart';
import '../../models/localized_text.dart';
import '../../services/local_db.dart';
import '../../services/mastery_service.dart';
import '../../services/profiles.dart';
import 'practice_screen.dart';

/// Today's 10–15 minute plan (spec B4), with a tick for each part done.
class TodayPlanCard extends ConsumerWidget {
  const TodayPlanCard({super.key, required this.student});

  final Student student;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final l10n = AppLocalizations.of(context);
    final plan = ref.watch(todayPlanProvider(student.id)).value;
    final states = ref.watch(skillStatesProvider(student.id)).value ?? {};
    final progress = ref.watch(progressProvider(student.id)).value ?? {};
    final marked = ref.watch(planDoneProvider(student.id));
    final curriculum = ref.watch(curriculumProvider).value;
    final assigned = ref.watch(assignmentsProvider(student.id)).value ?? [];
    if (plan == null || curriculum == null) return const SizedBox.shrink();
    final now = DateTime.now();

    // Lessons from the child's teachers come first, until finished
    // (Phase 9). The same lesson from two classes shows once.
    final seen = <String>{};
    final teacherLessons = [
      for (final a in assigned)
        if (curriculum.lesson(a.lessonId) case final lesson?
            when progress[a.lessonId]?.completed != true &&
                seen.add(a.lessonId))
          (lesson: lesson, due: a.due),
    ];
    if (plan.items.isEmpty && teacherLessons.isEmpty) {
      return const SizedBox.shrink();
    }

    bool done(PlanItem item) => switch (item) {
      QuestionItem() => questionDoneToday(item, states, now),
      LessonItem(:final lesson) =>
        progress[lesson.id]?.completed == true ||
            (progress[lesson.id] != null &&
                dayOf(progress[lesson.id]!.updatedAt) == dayOf(now)),
      _ => marked.contains(item.key),
    };

    String title(String skill) =>
        curriculum.titleOf(skill)?.of(context) ?? skill;

    final questionsLeft = plan.items.whereType<QuestionItem>().any(
      (i) => !done(i),
    );
    final allDone = teacherLessons.isEmpty && plan.items.every(done);

    return Card(
      key: const Key('today-plan'),
      child: Padding(
        padding: const EdgeInsets.all(12),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Row(
              children: [
                Expanded(
                  child: Text(
                    l10n.todaysPlan,
                    style: Theme.of(context).textTheme.titleLarge,
                  ),
                ),
                Text(l10n.planMinutes(plan.minutes)),
              ],
            ),
            const SizedBox(height: 8),
            for (final (:lesson, :due) in teacherLessons)
              ListTile(
                key: Key('plan-assigned-${lesson.id}'),
                dense: true,
                contentPadding: EdgeInsets.zero,
                leading: const Icon(Icons.school_outlined),
                title: _Localized(lesson.title, (t) => l10n.planAssigned(t)),
                subtitle: due == null
                    ? null
                    : Text(
                        l10n.planDue(
                          MaterialLocalizations.of(context)
                              .formatShortDate(due),
                        ),
                      ),
                onTap: () => context.push('/lesson/${lesson.id}'),
              ),
            for (final item in plan.items)
              ListTile(
                key: Key('plan-${item.key}'),
                dense: true,
                contentPadding: EdgeInsets.zero,
                leading: Icon(
                  done(item) ? Icons.check_circle : _icon(item),
                  color: done(item) ? Colors.green : null,
                ),
                title: switch (item) {
                  LessonItem(:final lesson) => _Localized(
                    lesson.title,
                    (t) => l10n.planLesson(t),
                  ),
                  FlashcardsItem(:final lesson) => _Localized(
                    lesson.title,
                    (t) => l10n.planFlashcards(t),
                  ),
                  HomeTaskItem() => Text(l10n.planHomeTask),
                  QuestionItem(:final purpose, :final question) => Text(
                    switch (purpose) {
                      QuestionPurpose.review => l10n.planReview(
                        title(question.skill),
                      ),
                      QuestionPurpose.practice => l10n.planPractice(
                        title(question.skill),
                      ),
                      QuestionPurpose.mixed => l10n.planMixed,
                      QuestionPurpose.explain => l10n.planExplain,
                    },
                  ),
                },
                onTap: switch (item) {
                  LessonItem(:final lesson) => () => context.push(
                    '/lesson/${lesson.id}',
                  ),
                  FlashcardsItem(:final lesson) => () => context.push(
                    '/flashcards/${lesson.id}',
                  ),
                  HomeTaskItem() => () => _showHomeTask(context, ref, item),
                  QuestionItem() => null,
                },
              ),
            const SizedBox(height: 8),
            if (allDone)
              Text(
                l10n.planAllDone,
                key: const Key('plan-all-done'),
                textAlign: TextAlign.center,
              )
            else if (questionsLeft)
              FilledButton.icon(
                key: const Key('start-practice'),
                icon: const Icon(Icons.play_arrow),
                label: Text(l10n.startPractice),
                onPressed: () => context.push('/practice'),
              ),
          ],
        ),
      ),
    );
  }

  static IconData _icon(PlanItem item) => switch (item) {
    QuestionItem(purpose: QuestionPurpose.review) => Icons.replay,
    QuestionItem(purpose: QuestionPurpose.explain) => Icons.lightbulb_outline,
    QuestionItem() => Icons.edit_outlined,
    LessonItem() => Icons.menu_book_outlined,
    HomeTaskItem() => Icons.home_outlined,
    FlashcardsItem() => Icons.style_outlined,
  };

  void _showHomeTask(BuildContext context, WidgetRef ref, HomeTaskItem item) {
    final l10n = AppLocalizations.of(context);
    unawaited(
      showDialog<void>(
        context: context,
        builder: (context) => AlertDialog(
          title: Text(l10n.homeTaskTitle),
          content: LessonText(item.task.text),
          actions: [
            TextButton(
              onPressed: () => Navigator.pop(context),
              child: Text(l10n.cancelButton),
            ),
            FilledButton(
              key: const Key('home-task-done'),
              onPressed: () {
                unawaited(
                  ref
                      .read(planDoneProvider(student.id).notifier)
                      .markDone(item.key),
                );
                Navigator.pop(context);
              },
              child: Text(l10n.markDone),
            ),
          ],
        ),
      ),
    );
  }
}

/// A sentence around a lesson title in the app's language.
class _Localized extends StatelessWidget {
  const _Localized(this.title, this.sentence);

  final LocalizedText title;
  final String Function(String title) sentence;

  @override
  Widget build(BuildContext context) => Text(sentence(title.of(context)));
}
