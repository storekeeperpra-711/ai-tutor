import 'package:flutter/material.dart';

import '../../character/mithu_controller.dart';
import '../../character/narrator.dart';
import '../../character/number_pictures.dart';
import '../../character/voice_lines.dart';
import '../../models/lesson_step.dart';

/// A big round button with only a picture, for children who can't read.
/// [label] is for screen readers.
class BigIconButton extends StatelessWidget {
  const BigIconButton({
    super.key,
    required this.icon,
    required this.label,
    required this.onPressed,
    this.color,
  });

  final IconData icon;
  final String label;
  final VoidCallback? onPressed;
  final Color? color;

  @override
  Widget build(BuildContext context) => Center(
    child: Tooltip(
      message: label,
      child: FilledButton(
        style: FilledButton.styleFrom(
          shape: const CircleBorder(),
          padding: const EdgeInsets.all(20),
          backgroundColor: color,
        ),
        onPressed: onPressed,
        child: Icon(icon, size: 56, semanticLabel: label),
      ),
    ),
  );
}

/// Mithu says the number [n] aloud, with [mithu]'s beak moving.
void sayNumber(
  Narrator narrator,
  MithuController mithu,
  BuildContext context,
  int n,
) => narrator.say(
  VoiceLine(
    line: CharacterLine(emotion: 'talking', say: numberWord(n)),
    language: Localizations.localeOf(context).languageCode,
  ),
  mithu,
);
