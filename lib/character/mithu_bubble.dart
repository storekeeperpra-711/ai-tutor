import 'package:flutter/material.dart';

import '../lessons/lesson_text.dart';
import '../models/lesson_step.dart';
import 'mithu.dart';
import 'mithu_controller.dart';

/// An answer Mithu reacts to. [attempt] tells two wrong answers in a row
/// apart, so Mithu reacts to each.
typedef MithuReaction = ({bool correct, int attempt});

/// Mithu with a speech bubble, at the top of a lesson step.
///
/// The lesson's `character.emotion` sets the mood; [reaction] (the last
/// checked answer) moves it to happy, or curious and then encouraging.
class MithuBubble extends StatefulWidget {
  const MithuBubble({
    super.key,
    required this.line,
    this.reaction,
    this.controller,
  });

  final CharacterLine line;
  final MithuReaction? reaction;

  /// For screens that drive Mithu themselves; otherwise the bubble keeps
  /// its own.
  final MithuController? controller;

  @override
  State<MithuBubble> createState() => _MithuBubbleState();
}

class _MithuBubbleState extends State<MithuBubble> {
  MithuController? _own;

  MithuController get _controller =>
      widget.controller ??
      (_own ??= MithuController(mood: MithuMood.parse(widget.line.emotion)));

  @override
  void initState() {
    super.initState();
    _controller.base = MithuMood.parse(widget.line.emotion);
  }

  @override
  void didUpdateWidget(MithuBubble old) {
    super.didUpdateWidget(old);
    _controller.base = MithuMood.parse(widget.line.emotion);
    final reaction = widget.reaction;
    if (reaction != old.reaction) {
      if (reaction == null) {
        _controller.reset();
      } else {
        _controller.react(correct: reaction.correct);
      }
    }
  }

  @override
  void dispose() {
    _own?.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final colors = Theme.of(context).colorScheme;
    return Row(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        ListenableBuilder(
          listenable: _controller,
          builder: (context, _) => MithuView(
            key: const Key('mithu'),
            mood: _controller.mood,
            size: 72,
            mouth: _controller.speaking ? _controller.mouth : null,
          ),
        ),
        const SizedBox(width: 8),
        Expanded(
          child: Container(
            margin: const EdgeInsets.only(top: 8),
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(
              color: colors.secondaryContainer,
              borderRadius: BorderRadius.circular(16),
            ),
            child: LessonText(
              widget.line.say,
              style: Theme.of(context).textTheme.titleMedium,
            ),
          ),
        ),
      ],
    );
  }
}
