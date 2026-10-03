import 'package:flutter/material.dart';
import 'package:flutter/services.dart' show appFlavor;
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../app/theme/age_tier.dart';
import '../l10n/app_localizations.dart';
import '../lessons/lesson_text.dart';
import '../lessons/step_context.dart';
import '../models/lesson_step.dart';
import 'feel_settings.dart';
import 'mithu.dart';
import 'mithu_controller.dart';
import 'narrator.dart';
import 'voice_lines.dart';

/// An answer Mithu reacts to. [attempt] tells two wrong answers in a row
/// apart, so Mithu reacts to each.
typedef MithuReaction = ({bool correct, int attempt});

/// Mithu with a speech bubble and a speaker button, at the top of a step.
/// With Mithu switched off in Settings, only the bubble shows.
///
/// The lesson's `character.emotion` sets the mood; [reaction] (the last
/// checked answer) moves it to happy, or curious and then encouraging.
/// For Nursery to Grade 2 Mithu says the line by itself.
class MithuBubble extends ConsumerStatefulWidget {
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
  ConsumerState<MithuBubble> createState() => _MithuBubbleState();
}

class _MithuBubbleState extends ConsumerState<MithuBubble> {
  MithuController? _own;
  late final Narrator _narrator;
  var _phoneVoice = false;

  MithuController get _controller =>
      widget.controller ??
      (_own ??= MithuController(mood: MithuMood.parse(widget.line.emotion)));

  @override
  void initState() {
    super.initState();
    _controller.base = MithuMood.parse(widget.line.emotion);
    _narrator = ref.read(narratorProvider);
    WidgetsBinding.instance.addPostFrameCallback((_) => _start());
  }

  VoiceLine _voice() {
    final step = StepContext.of(context);
    return VoiceLine(
      line: widget.line,
      language: Localizations.localeOf(context).languageCode,
      lessonId: step?.lessonId,
      stepId: step?.stepId,
    );
  }

  Future<void> _start() async {
    if (!mounted) return;
    final voice = _voice();
    if (appFlavor == 'dev') {
      final recorded = await _narrator.hasRecording(voice);
      if (mounted) setState(() => _phoneVoice = !recorded);
    }
    if (mounted && ref.read(ageTierProvider) == AgeTier.early) _say();
  }

  void _say() => _narrator.say(_voice(), _controller);

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
    if (_controller.speaking) _narrator.stop();
    _own?.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final theme = Theme.of(context);
    final early = ref.watch(ageTierProvider) == AgeTier.early;
    final showMithu = ref.watch(mithuOnProvider);
    return Row(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        if (showMithu) ...[
          ListenableBuilder(
            listenable: _controller,
            builder: (context, _) => MithuView(
              key: const Key('mithu'),
              mood: _controller.mood,
              size: early ? 96 : 72,
              mouth: _controller.speaking ? _controller.mouth : null,
            ),
          ),
          const SizedBox(width: 8),
        ],
        Expanded(
          child: Container(
            margin: EdgeInsets.only(top: showMithu ? 8 : 0),
            padding: const EdgeInsetsDirectional.fromSTEB(16, 8, 4, 8),
            decoration: BoxDecoration(
              color: theme.colorScheme.secondaryContainer,
              borderRadius: BorderRadius.circular(16),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Expanded(
                      child: Padding(
                        padding: const EdgeInsets.symmetric(vertical: 8),
                        child: LessonText(
                          widget.line.say,
                          style: theme.textTheme.titleMedium,
                        ),
                      ),
                    ),
                    IconButton(
                      key: const Key('mithu-listen'),
                      tooltip: l10n.listenToMithu,
                      iconSize: early ? 40 : 24,
                      onPressed: _say,
                      icon: const Icon(Icons.volume_up_rounded),
                    ),
                  ],
                ),
                if (_phoneVoice)
                  Text(l10n.phoneVoiceLabel, style: theme.textTheme.labelSmall),
              ],
            ),
          ),
        ),
      ],
    );
  }
}
