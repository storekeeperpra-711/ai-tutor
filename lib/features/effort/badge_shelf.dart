import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../l10n/app_localizations.dart';
import 'effort.dart';

IconData badgeIcon(EffortBadge badge) => switch (badge) {
  EffortBadge.firstLesson => Icons.flag_rounded,
  EffortBadge.triedAgain => Icons.replay_rounded,
  EffortBadge.explained => Icons.record_voice_over_rounded,
  EffortBadge.checkedPhoto => Icons.photo_camera_rounded,
  EffortBadge.cameBack => Icons.event_repeat_rounded,
  EffortBadge.fiveDays => Icons.calendar_month_rounded,
};

String badgeName(AppLocalizations l10n, EffortBadge badge) => switch (badge) {
  EffortBadge.firstLesson => l10n.badgeFirstLesson,
  EffortBadge.triedAgain => l10n.badgeTriedAgain,
  EffortBadge.explained => l10n.badgeExplained,
  EffortBadge.checkedPhoto => l10n.badgeCheckedPhoto,
  EffortBadge.cameBack => l10n.badgeCameBack,
  EffortBadge.fiveDays => l10n.badgeFiveDays,
};

/// All effort badges: earned ones in colour, the rest as outlines to aim
/// for. [compact] shows only the icons.
class BadgeShelf extends ConsumerWidget {
  const BadgeShelf({super.key, required this.studentId, this.compact = false});

  final String studentId;
  final bool compact;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final l10n = AppLocalizations.of(context);
    final theme = Theme.of(context);
    final earned = ref.watch(badgesProvider(studentId));
    return Column(
      key: const Key('badge-shelf'),
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Row(
          children: [
            Expanded(
              child: Text(l10n.badgesTitle, style: theme.textTheme.titleLarge),
            ),
            Text(
              l10n.badgesEarned(earned.length, EffortBadge.values.length),
              style: theme.textTheme.labelLarge,
            ),
          ],
        ),
        const SizedBox(height: 8),
        Wrap(
          spacing: 8,
          runSpacing: 8,
          children: [
            for (final badge in EffortBadge.values)
              _Badge(
                badge: badge,
                earned: earned.contains(badge),
                compact: compact,
              ),
          ],
        ),
      ],
    );
  }
}

class _Badge extends StatelessWidget {
  const _Badge({
    required this.badge,
    required this.earned,
    required this.compact,
  });

  final EffortBadge badge;
  final bool earned;
  final bool compact;

  @override
  Widget build(BuildContext context) {
    final colors = Theme.of(context).colorScheme;
    final name = badgeName(AppLocalizations.of(context), badge);
    final icon = CircleAvatar(
      radius: 22,
      backgroundColor: earned
          ? colors.tertiaryContainer
          : colors.surfaceContainerHighest,
      child: Icon(
        badgeIcon(badge),
        color: earned ? colors.onTertiaryContainer : colors.outline,
      ),
    );
    return Semantics(
      key: Key('badge-${badge.name}-${earned ? 'earned' : 'not-yet'}'),
      label: name,
      checked: earned,
      child: compact
          ? Tooltip(message: name, child: icon)
          : SizedBox(
              width: 104,
              child: Column(
                children: [
                  icon,
                  const SizedBox(height: 4),
                  Text(
                    name,
                    textAlign: TextAlign.center,
                    style: Theme.of(context).textTheme.labelSmall
                        ?.copyWith(color: earned ? null : colors.outline),
                  ),
                ],
              ),
            ),
    );
  }
}
