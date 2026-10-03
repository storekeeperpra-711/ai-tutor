import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../character/mithu_bubble.dart';
import '../../character/sounds.dart';
import '../../l10n/app_localizations.dart';
import '../../models/lesson.dart';
import '../../models/lesson_step.dart';
import '../../models/localized_text.dart';
import 'effort.dart';

/// The end of a lesson: Mithu celebrates, up to three effort stars, one
/// line of praise and one clear next step (spec C3).
class CelebrationView extends ConsumerStatefulWidget {
  const CelebrationView({
    super.key,
    required this.lesson,
    required this.stars,
    required this.next,
    required this.onNext,
    required this.onHome,
  });

  final Lesson lesson;
  final LessonStars stars;

  /// The lesson to suggest next; null: come back tomorrow.
  final Lesson? next;
  final VoidCallback onNext;
  final VoidCallback onHome;

  @override
  ConsumerState<CelebrationView> createState() => _CelebrationViewState();
}

class _CelebrationViewState extends ConsumerState<CelebrationView> {
  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addPostFrameCallback((_) {
      if (mounted) ref.playSound(Sound.celebrate);
    });
  }

  /// The same praise in both languages, so Mithu can say it.
  LocalizedText _praise() {
    final pick = widget.lesson.id.hashCode % 3;
    String line(AppLocalizations l) => switch (pick) {
      0 => l.praise1,
      1 => l.praise2,
      _ => l.praise3,
    };
    return LocalizedText(
      en: line(lookupAppLocalizations(const Locale('en'))),
      ur: line(lookupAppLocalizations(const Locale('ur'))),
    );
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final theme = Theme.of(context);
    final stars = widget.stars;
    final next = widget.next;
    final reasons = [
      (stars.finished, l10n.starFinished),
      (stars.keptTrying, l10n.starKeptTrying),
      (stars.explained, l10n.starExplained),
    ];
    return ListView(
      key: const Key('lesson-celebration'),
      padding: const EdgeInsets.all(24),
      children: [
        MithuBubble(
          line: CharacterLine(emotion: 'celebrating', say: _praise()),
        ),
        const SizedBox(height: 24),
        Semantics(
          label: '${stars.count} / 3',
          child: Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              for (final (i, (earned, _)) in reasons.indexed)
                Icon(
                  earned ? Icons.star_rounded : Icons.star_outline_rounded,
                  key: Key('star-$i-${earned ? 'on' : 'off'}'),
                  size: 64,
                  color: earned ? Colors.amber.shade600 : theme.disabledColor,
                ),
            ],
          ),
        ),
        const SizedBox(height: 8),
        for (final (earned, reason) in reasons)
          if (earned)
            Text(
              reason,
              textAlign: TextAlign.center,
              style: theme.textTheme.titleMedium,
            ),
        const SizedBox(height: 32),
        if (next != null)
          FilledButton.icon(
            key: const Key('celebration-next'),
            icon: const Icon(Icons.arrow_forward_rounded),
            label: Text(l10n.nextLesson(next.title.of(context))),
            onPressed: widget.onNext,
          )
        else
          Text(
            l10n.comeBackTomorrow,
            key: const Key('come-back-tomorrow'),
            textAlign: TextAlign.center,
            style: theme.textTheme.titleMedium,
          ),
        const SizedBox(height: 12),
        OutlinedButton.icon(
          key: const Key('celebration-done'),
          icon: const Icon(Icons.home_rounded),
          label: Text(l10n.backHome),
          onPressed: widget.onHome,
        ),
      ],
    );
  }
}
