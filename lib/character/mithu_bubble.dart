import 'package:flutter/material.dart';

import '../lessons/lesson_text.dart';
import '../models/lesson_step.dart';

/// Placeholder for Mithu: a bird icon with a speech bubble.
/// Replaced by the Rive character with emotions and audio in Phase 7.
class MithuBubble extends StatelessWidget {
  const MithuBubble({super.key, required this.line});

  final CharacterLine line;

  @override
  Widget build(BuildContext context) {
    final colors = Theme.of(context).colorScheme;
    return Row(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        CircleAvatar(
          radius: 28,
          backgroundColor: const Color(0xFF43A047),
          child: Semantics(
            label: 'Mithu (${line.emotion})',
            child: const Icon(
              Icons.flutter_dash,
              color: Colors.white,
              size: 36,
            ),
          ),
        ),
        const SizedBox(width: 12),
        Expanded(
          child: Container(
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(
              color: colors.secondaryContainer,
              borderRadius: BorderRadius.circular(16),
            ),
            child: LessonText(
              line.say,
              style: Theme.of(context).textTheme.titleMedium,
            ),
          ),
        ),
      ],
    );
  }
}
