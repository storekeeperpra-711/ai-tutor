import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../../app/motion_widgets.dart';
import '../../app/theme/app_theme.dart';
import '../../l10n/app_localizations.dart';
import '../../lessons/lesson_text.dart';
import '../../mastery/skill_state.dart';
import '../../models/lesson.dart';
import '../../services/local_db.dart';
import '../../services/mastery_service.dart';
import '../../services/profiles.dart';
import '../plan/mastery_level.dart';
import '../profiles/avatar.dart';
import '../profiles/grade_names.dart';
import 'home_parts.dart';

/// The new look's home pieces, from the approved "Home" mock-up:
/// a greeting header, Mithu on a soft card, pastel tiles and a lesson grid.

/// A white rounded square button, as in the header.
class HeaderButton extends StatelessWidget {
  const HeaderButton({
    super.key,
    required this.icon,
    required this.tooltip,
    required this.onPressed,
  });

  final IconData icon;
  final String tooltip;
  final VoidCallback onPressed;

  @override
  Widget build(BuildContext context) => Pressable(
    child: Material(
      color: Colors.white,
      elevation: 1,
      shadowColor: const Color(0x225B4BDB),
      borderRadius: BorderRadius.circular(14),
      child: IconButton(
        icon: Icon(icon, color: AppColors.ink),
        tooltip: tooltip,
        onPressed: onPressed,
      ),
    ),
  );
}

/// The child's picture, grade and a big hello.
class HomeHeader extends ConsumerWidget {
  const HomeHeader({super.key, required this.student});

  final Student student;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final l10n = AppLocalizations.of(context);
    final theme = Theme.of(context);
    return Row(
      children: [
        Container(
          width: 52,
          height: 52,
          alignment: Alignment.center,
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(18),
          ),
          child: StudentAvatar(avatar: student.avatar, size: 40),
        ),
        const SizedBox(width: 12),
        Expanded(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                gradeName(l10n, student.grade),
                style: theme.textTheme.labelLarge?.copyWith(
                  color: AppColors.muted,
                ),
              ),
              Text(
                l10n.helloName(student.firstName),
                style: theme.textTheme.headlineSmall,
                maxLines: 2,
                overflow: TextOverflow.ellipsis,
              ),
            ],
          ),
        ),
        const SizedBox(width: 8),
        // An icon, so a long name (or the little ones' big text) still fits.
        HeaderButton(
          key: const Key('switch-learner'),
          icon: Icons.swap_horiz_rounded,
          tooltip: l10n.switchLearner,
          onPressed: () => ref.read(currentStudentProvider.notifier).clear(),
        ),
      ],
    );
  }
}

/// Mithu's tip on a soft green-to-lilac card.
class MithuCard extends StatelessWidget {
  const MithuCard({super.key, required this.child});

  final Widget child;

  @override
  Widget build(BuildContext context) => Container(
    margin: const EdgeInsets.only(bottom: 12),
    padding: const EdgeInsets.all(8),
    decoration: BoxDecoration(
      gradient: const LinearGradient(
        begin: Alignment.topLeft,
        end: Alignment.bottomRight,
        colors: [Color(0xFFDDF4E7), Color(0xFFE6E2FF)],
      ),
      borderRadius: BorderRadius.circular(AppRadius.card),
    ),
    child: child,
  );
}

/// A pastel tile: an icon in a white square, a title, then [footer].
class SoftTile extends StatelessWidget {
  const SoftTile({
    super.key,
    required this.colorIndex,
    required this.icon,
    required this.title,
    this.footer,
    this.onTap,
  });

  final int colorIndex;
  final IconData icon;
  final Widget title;
  final Widget? footer;
  final VoidCallback? onTap;

  @override
  Widget build(BuildContext context) {
    final colors = AppColors.tiles[colorIndex % AppColors.tiles.length];
    final tile = Material(
      color: colors.soft,
      borderRadius: BorderRadius.circular(AppRadius.tile),
      child: InkWell(
        borderRadius: BorderRadius.circular(AppRadius.tile),
        onTap: onTap,
        child: Padding(
          padding: const EdgeInsets.all(14),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Container(
                width: 40,
                height: 40,
                decoration: BoxDecoration(
                  color: Colors.white,
                  borderRadius: BorderRadius.circular(12),
                ),
                child: Icon(icon, color: colors.strong, size: 22),
              ),
              const SizedBox(height: 8),
              DefaultTextStyle.merge(
                style: Theme.of(context).textTheme.titleSmall
                    ?.copyWith(fontWeight: FontWeight.w900, height: 1.25),
                child: title,
              ),
              if (footer != null) ...[
                const SizedBox(height: 8),
                DefaultTextStyle.merge(
                  style: TextStyle(
                    color: colors.strong,
                    fontWeight: FontWeight.w800,
                  ),
                  child: IconTheme.merge(
                    data: IconThemeData(color: colors.strong),
                    child: footer!,
                  ),
                ),
              ],
            ],
          ),
        ),
      ),
    );
    return onTap == null ? tile : Pressable(child: tile);
  }
}

/// A thin rounded progress bar on a white track.
class TileProgress extends StatelessWidget {
  const TileProgress({super.key, required this.value, required this.color});

  final double value;
  final Color color;

  @override
  Widget build(BuildContext context) => ClipRRect(
    borderRadius: BorderRadius.circular(999),
    child: LinearProgressIndicator(
      value: value,
      minHeight: 6,
      color: color,
      backgroundColor: Colors.white,
    ),
  );
}

IconData subjectIcon(String subject) => switch (subject) {
  'maths' => Icons.calculate_rounded,
  'chemistry' => Icons.science_rounded,
  'physics' => Icons.bolt_rounded,
  'biology' => Icons.eco_rounded,
  'science' => Icons.science_rounded,
  'english' => Icons.translate_rounded,
  'urdu' => Icons.menu_book_rounded,
  _ => Icons.auto_stories_rounded,
};

/// Every lesson as a pastel tile, two to a row, with chips to show one
/// subject: start, continue (with a bar) or done, and mastery dots.
class LessonList extends ConsumerStatefulWidget {
  const LessonList({super.key, required this.student, required this.lessons});

  final Student student;
  final List<Lesson> lessons;

  @override
  ConsumerState<LessonList> createState() => _LessonListState();
}

class _LessonListState extends ConsumerState<LessonList> {
  String? _subject;

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final theme = Theme.of(context);
    final id = widget.student.id;
    final progress = ref.watch(progressProvider(id)).value ?? const {};
    final states = ref.watch(skillStatesProvider(id)).value ?? {};
    final curriculum = ref.watch(curriculumProvider).value;
    final subjects = {for (final l in widget.lessons) l.subject}.toList();
    final shown = [
      for (final l in widget.lessons)
        if (_subject == null || l.subject == _subject) l,
    ];

    Widget chip(String? subject, String label) => Padding(
      padding: const EdgeInsetsDirectional.only(end: 8),
      child: ChoiceChip(
        key: Key('lesson-filter-${subject ?? 'all'}'),
        label: Text(label),
        selected: _subject == subject,
        showCheckmark: false,
        selectedColor: AppColors.ink,
        labelStyle: TextStyle(
          color: _subject == subject ? Colors.white : AppColors.ink,
          fontWeight: FontWeight.w800,
        ),
        onSelected: (_) => setState(() => _subject = subject),
      ),
    );

    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        Text(l10n.lessonsTitle, style: theme.textTheme.titleLarge),
        const SizedBox(height: 8),
        if (widget.lessons.isEmpty)
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 16),
            child: Text(l10n.noLessonsYet),
          ),
        if (subjects.length > 1) ...[
          SingleChildScrollView(
            scrollDirection: Axis.horizontal,
            child: Row(
              children: [
                chip(null, l10n.allSubjects),
                for (final s in subjects) chip(s, subjectName(l10n, s)),
              ],
            ),
          ),
          const SizedBox(height: 12),
        ],
        LayoutBuilder(
          builder: (context, box) {
            const gap = 12.0;
            final columns = box.maxWidth > 560 ? 3 : 2;
            final width = (box.maxWidth - gap * (columns - 1)) / columns;
            return Wrap(
              spacing: gap,
              runSpacing: gap,
              children: [
                for (final (i, lesson) in shown.indexed)
                  SizedBox(
                    width: width,
                    child: EnterAnimation(
                      index: i,
                      child: _lessonTile(
                        lesson,
                        i,
                        progress[lesson.id],
                        states[lesson.mainSkill]?.level(
                          curriculum?.criteriaFor(lesson.mainSkill),
                        ),
                        l10n,
                      ),
                    ),
                  ),
              ],
            );
          },
        ),
      ],
    );
  }

  Widget _lessonTile(
    Lesson lesson,
    int index,
    LessonProgress? p,
    MasteryLevel? level,
    AppLocalizations l10n,
  ) {
    final colors = AppColors.tiles[index % AppColors.tiles.length];
    final status = switch (p) {
      null => l10n.lessonStart,
      LessonProgress(completed: true) => l10n.lessonDone,
      final p => l10n.lessonContinue(p.nextStep + 1, lesson.steps.length),
    };
    return SoftTile(
      key: Key('home-lesson-${lesson.id}'),
      colorIndex: index,
      icon: p?.completed == true
          ? Icons.check_circle_rounded
          : subjectIcon(lesson.subject),
      title: LessonText(lesson.title),
      onTap: () => context.push('/lesson/${lesson.id}'),
      footer: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          if (p != null && !p.completed) ...[
            TileProgress(
              value: lesson.steps.isEmpty
                  ? 0
                  : (p.nextStep / lesson.steps.length).clamp(0.0, 1.0),
              color: colors.strong,
            ),
            const SizedBox(height: 6),
          ],
          Text(status, key: Key('home-lesson-status-${lesson.id}')),
          if (level != null)
            MasteryDots(key: Key('mastery-${lesson.id}'), level: level),
        ],
      ),
    );
  }
}
