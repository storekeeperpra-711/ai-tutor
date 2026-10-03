import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../character/mithu_bubble.dart';
import '../../character/mithu_controller.dart';
import '../../character/narrator.dart';
import '../../character/number_pictures.dart';
import '../../character/sounds.dart';
import '../../l10n/app_localizations.dart';
import '../../models/lesson_step.dart';
import '../lesson_text.dart';
import '../step_result.dart';
import 'picture_step_parts.dart';

/// Pick the picture card with the same number as the big picture. The
/// app compares the numbers; no reading needed.
class PickPictureStepView extends ConsumerStatefulWidget {
  const PickPictureStepView({
    super.key,
    required this.step,
    required this.onDone,
  });

  final PickPictureStep step;
  final StepDone onDone;

  @override
  ConsumerState<PickPictureStepView> createState() =>
      _PickPictureStepViewState();
}

class _PickPictureStepViewState extends ConsumerState<PickPictureStepView> {
  final _mithu = MithuController();
  late final Narrator _narrator = ref.read(narratorProvider);
  final _tried = <String>{};
  var _solved = false;
  MithuReaction? _reaction;

  bool get _done => _solved || _tried.length >= widget.step.maxAttempts;

  @override
  void dispose() {
    _narrator.stop();
    _mithu.dispose();
    super.dispose();
  }

  void _pick(PictureOption option) {
    if (_done || _tried.contains(option.id)) return;
    final right = widget.step.isRight(option);
    ref.playSound(right ? Sound.right : Sound.tryAgain);
    setState(() {
      _tried.add(option.id);
      _solved = right;
      _reaction = (correct: right, attempt: _tried.length);
    });
    if (_done) sayNumber(_narrator, _mithu, context, widget.step.show.value);
  }

  void _finish() => widget.onDone(
    StepResult(
      stepId: widget.step.id,
      correct: _solved && _tried.length == 1,
      solved: _solved,
      attempts: _tried.length,
    ),
  );

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final step = widget.step;
    final colors = Theme.of(context).colorScheme;
    return ListView(
      padding: const EdgeInsets.all(16),
      children: [
        if (step.character != null)
          MithuBubble(
            line: step.character!,
            reaction: _reaction,
            controller: _mithu,
          ),
        const SizedBox(height: 8),
        LessonText(step.prompt, style: Theme.of(context).textTheme.titleMedium),
        const SizedBox(height: 12),
        Center(
          child: Card(
            key: const Key('picture-shown'),
            color: colors.primaryContainer,
            child: Padding(
              padding: const EdgeInsets.all(12),
              child: NumberPictureView(
                kind: step.show.kind,
                value: step.show.value,
                size: 160,
              ),
            ),
          ),
        ),
        const SizedBox(height: 16),
        Wrap(
          alignment: WrapAlignment.center,
          spacing: 12,
          runSpacing: 12,
          children: [
            for (final o in step.options)
              _Card(
                option: o,
                state: !_tried.contains(o.id)
                    ? (_done && step.isRight(o) ? _CardState.shownRight : null)
                    : step.isRight(o)
                    ? _CardState.right
                    : _CardState.wrong,
                onTap: () => _pick(o),
              ),
          ],
        ),
        const SizedBox(height: 24),
        if (_done)
          BigIconButton(
            key: const Key('step-continue'),
            icon: Icons.arrow_forward_rounded,
            label: l10n.continueButton,
            color: Colors.green,
            onPressed: _finish,
          ),
      ],
    );
  }
}

enum _CardState { right, wrong, shownRight }

class _Card extends StatelessWidget {
  const _Card({required this.option, required this.state, required this.onTap});

  final PictureOption option;
  final _CardState? state;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    final border = switch (state) {
      _CardState.right || _CardState.shownRight => Colors.green,
      _CardState.wrong => Colors.grey,
      null => Theme.of(context).colorScheme.outlineVariant,
    };
    return Opacity(
      opacity: state == _CardState.wrong ? 0.4 : 1,
      child: Material(
        key: Key('picture-${option.id}'),
        color: Theme.of(context).colorScheme.surface,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(20),
          side: BorderSide(color: border, width: state == null ? 2 : 5),
        ),
        clipBehavior: Clip.antiAlias,
        child: InkWell(
          onTap: onTap,
          child: Padding(
            padding: const EdgeInsets.all(8),
            child: NumberPictureView(
              kind: option.picture.kind,
              value: option.picture.value,
            ),
          ),
        ),
      ),
    );
  }
}
