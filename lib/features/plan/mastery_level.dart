import 'package:flutter/material.dart';

import '../../l10n/app_localizations.dart';
import '../../mastery/skill_state.dart';

String levelName(AppLocalizations l10n, MasteryLevel level) => switch (level) {
  MasteryLevel.notStarted => l10n.levelNotStarted,
  MasteryLevel.learning => l10n.levelLearning,
  MasteryLevel.practising => l10n.levelPractising,
  MasteryLevel.mastered => l10n.levelMastered,
  MasteryLevel.secure => l10n.levelSecure,
};

/// Four dots that fill up from Learning to Secure, with the level's name.
class MasteryDots extends StatelessWidget {
  const MasteryDots({super.key, required this.level});

  final MasteryLevel level;

  @override
  Widget build(BuildContext context) {
    final colors = Theme.of(context).colorScheme;
    final name = levelName(AppLocalizations.of(context), level);
    return Semantics(
      label: name,
      excludeSemantics: true,
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          for (var i = 1; i < MasteryLevel.values.length; i++)
            Padding(
              padding: const EdgeInsetsDirectional.only(end: 3),
              child: Icon(
                level.index >= i ? Icons.circle : Icons.circle_outlined,
                size: 10,
                color: level == MasteryLevel.secure
                    ? const Color(0xFF2E7D32)
                    : colors.primary,
              ),
            ),
          const SizedBox(width: 4),
          Text(name, style: Theme.of(context).textTheme.bodySmall),
        ],
      ),
    );
  }
}
