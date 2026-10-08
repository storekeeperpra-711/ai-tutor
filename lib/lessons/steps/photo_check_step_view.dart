import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../ai/ai_help.dart';
import '../../ai/ai_service.dart';
import '../../ai/photo_picker.dart';
import '../../character/mithu_bubble.dart';
import '../../l10n/app_localizations.dart';
import '../../models/lesson_step.dart';
import '../../services/profiles.dart';
import '../answer_checking.dart';
import '../lesson_figure.dart';
import '../lesson_text.dart';
import '../step_context.dart';
import '../step_result.dart';
import 'step_scaffold.dart';

/// The student solves a problem in their notebook and sends a photo:
///
/// 1. AI reads the working (on the server).
/// 2. The student confirms what was read, fixing any misreading.
/// 3. The app's checker decides (never the AI).
/// 4. For a wrong answer, AI explains the checker's verdict.
///
/// Without internet, after a daily limit or for an unreadable photo, the
/// student types the working instead and the same checker decides.
class PhotoCheckStepView extends ConsumerStatefulWidget {
  const PhotoCheckStepView({
    super.key,
    required this.step,
    required this.onDone,
  });

  final PhotoCheckStep step;
  final StepDone onDone;

  @override
  ConsumerState<PhotoCheckStepView> createState() => _PhotoCheckStepViewState();
}

enum _Phase {
  /// Choose: take a photo, pick one, or type.
  start,
  reading,

  /// The working is in the text box (read by AI or typed), ready to check.
  confirm,
  checked,
  correct,
  outOfAttempts,
}

class _PhotoCheckStepViewState extends ConsumerState<PhotoCheckStepView> {
  final _controller = TextEditingController();

  /// With AI help off, there is no photo reading: the student types.
  late var _phase = _startPhase;

  _Phase get _startPhase =>
      ref.read(aiHelpProvider) ? _Phase.start : _Phase.confirm;
  var _attempts = 0;
  final _misconceptions = <String>[];

  /// The text in the box came from the AI reading a photo.
  var _readByAi = false;

  /// Shown on the start screen (unreadable photo) or above the box
  /// (offline, limit).
  String? _notice;
  AnswerCheck? _check;

  /// Mithu's explanation of a wrong answer; null while it loads or if the
  /// AI couldn't be reached.
  String? _explanation;
  var _explaining = false;

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  String? get _studentId => ref.read(currentStudentProvider)?.id;

  Future<void> _takePhoto(PhotoSource source) async {
    final l10n = AppLocalizations.of(context);
    final lessonId = StepContext.lessonIdOf(context);
    final photo = await ref.read(photoPickerProvider)(source);
    if (photo == null || !mounted) return;
    final studentId = _studentId;
    if (studentId == null || lessonId == null) {
      _typeInstead(l10n.photoOffline);
      return;
    }
    setState(() {
      _phase = _Phase.reading;
      _notice = null;
    });
    PhotoReading reading;
    try {
      reading = await ref
          .read(aiServiceProvider)
          .readPhoto(
            studentId: studentId,
            lessonId: lessonId,
            stepId: widget.step.id,
            photo: photo,
          );
    } on AiUnavailable {
      if (mounted) _typeInstead(l10n.photoOffline);
      return;
    }
    if (!mounted) return;
    if (!reading.byAi) {
      _typeInstead(
        const {'student_limit', 'step_limit', 'budget'}.contains(reading.reason)
            ? l10n.photoLimit
            : l10n.photoOffline,
      );
      return;
    }
    if (!reading.readable) {
      setState(() {
        _phase = _Phase.start;
        _notice = l10n.photoUnreadable;
      });
      return;
    }
    final lines = widget.step.checksWorking
        ? reading.lines
        : [
            reading.finalAnswer.isNotEmpty
                ? reading.finalAnswer
                : reading.lines.last,
          ];
    _controller.text = lines.join('\n');
    setState(() {
      _phase = _Phase.confirm;
      _readByAi = true;
      _check = null;
    });
  }

  void _typeInstead([String? notice]) {
    _controller.clear();
    setState(() {
      _phase = _Phase.confirm;
      _readByAi = false;
      _notice = notice;
      _check = null;
    });
  }

  Future<void> _checkAnswer() async {
    final l10n = AppLocalizations.of(context);
    final language = Localizations.localeOf(context).languageCode;
    final lessonId = StepContext.lessonIdOf(context);
    final working = _controller.text.trim();
    final result = checkPhotoStep(widget.step, working, l10n, language);
    setState(() {
      _check = result;
      _explanation = null;
      if (result.correct) {
        _attempts++;
        _phase = _Phase.correct;
        return;
      }
      // Unreadable or "almost": fix it in the box; no attempt used.
      if (!result.countsAsAttempt) return;
      _attempts++;
      if (result.misconceptionId != null) {
        _misconceptions.add(result.misconceptionId!);
      }
      _phase = _attempts >= widget.step.maxAttempts
          ? _Phase.outOfAttempts
          : _Phase.checked;
    });
    if (result.correct || !result.countsAsAttempt) return;

    // Only a wrong answer uses AI, to explain the checker's verdict.
    final studentId = _studentId;
    if (studentId == null || lessonId == null) return;
    if (!ref.read(aiHelpProvider)) return;
    setState(() => _explaining = true);
    String? explanation;
    try {
      final reply = await ref
          .read(aiServiceProvider)
          .explainVerdict(
            studentId: studentId,
            lessonId: lessonId,
            stepId: widget.step.id,
            language: language,
            working: working,
            checkerMessage: result.message ?? l10n.tryAgain,
          );
      if (reply.byAi) explanation = reply.reply;
    } on AiUnavailable {
      // The checker's message and the hint are enough.
    }
    if (!mounted) return;
    setState(() {
      _explaining = false;
      _explanation = explanation;
    });
  }

  void _tryAgain() {
    _controller.clear();
    setState(() {
      _phase = _startPhase;
      _check = null;
      _explanation = null;
      _notice = null;
    });
  }

  void _finish() => widget.onDone(
    StepResult(
      stepId: widget.step.id,
      correct: _phase == _Phase.correct && _attempts == 1,
      solved: _phase == _Phase.correct,
      attempts: _attempts,
      misconceptionIds: _misconceptions,
    ),
  );

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final textTheme = Theme.of(context).textTheme;
    final check = _check;

    final notice =
        _notice ??
        (!ref.watch(aiHelpProvider) && _phase == _Phase.confirm
            ? l10n.photoAiOff
            : null);
    final (
      String buttonLabel,
      Key buttonKey,
      VoidCallback? onPressed,
    ) = switch (_phase) {
      _Phase.start || _Phase.reading => (
        l10n.photoTake,
        const Key('photo-camera'),
        _phase == _Phase.start ? () => _takePhoto(PhotoSource.camera) : null,
      ),
      _Phase.confirm => (
        l10n.checkButton,
        const Key('step-check'),
        _checkAnswer,
      ),
      _Phase.checked => (
        l10n.tryAgainButton,
        const Key('photo-try-again'),
        _explaining ? null : _tryAgain,
      ),
      _Phase.correct || _Phase.outOfAttempts => (
        l10n.continueButton,
        const Key('step-continue'),
        _finish,
      ),
    };

    return StepScaffold(
      buttonKey: buttonKey,
      buttonLabel: buttonLabel,
      onPressed: onPressed,
      children: [
        if (widget.step.character != null) ...[
          MithuBubble(line: widget.step.character!),
          const SizedBox(height: 24),
        ],
        StepPrompt(
          widget.step.problem,
          figure: widget.step.figure,
          style: textTheme.titleLarge,
        ),
        const SizedBox(height: 16),
        if (notice != null)
          Padding(
            padding: const EdgeInsets.only(bottom: 12),
            child: Text(
              notice,
              key: const Key('photo-notice'),
              style: textTheme.bodyLarge,
            ),
          ),
        if (_phase == _Phase.start) ...[
          OutlinedButton.icon(
            key: const Key('photo-gallery'),
            onPressed: () => _takePhoto(PhotoSource.gallery),
            icon: const Icon(Icons.photo_library),
            label: Text(l10n.photoChoose),
          ),
          TextButton(
            key: const Key('photo-type'),
            onPressed: _typeInstead,
            child: Text(l10n.photoTypeInstead),
          ),
        ],
        if (_phase == _Phase.reading)
          Row(
            children: [
              const SizedBox.square(
                dimension: 20,
                child: CircularProgressIndicator(strokeWidth: 2),
              ),
              const SizedBox(width: 12),
              Expanded(child: Text(l10n.photoReading)),
            ],
          ),
        if (_phase.index >= _Phase.confirm.index) ...[
          if (_readByAi && _phase == _Phase.confirm)
            Padding(
              padding: const EdgeInsets.only(bottom: 8),
              child: Text(l10n.photoConfirm, style: textTheme.bodyLarge),
            ),
          TextField(
            key: const Key('answer-input'),
            controller: _controller,
            enabled: _phase == _Phase.confirm,
            // Working is written left-to-right even in Urdu.
            textDirection: TextDirection.ltr,
            keyboardType: TextInputType.multiline,
            minLines: widget.step.checksWorking ? 3 : 1,
            maxLines: 10,
            autocorrect: false,
            enableSuggestions: false,
            style: textTheme.headlineSmall,
            decoration: InputDecoration(
              labelText: widget.step.checksWorking
                  ? l10n.photoWorkingLabel
                  : l10n.answerLabel,
              border: const OutlineInputBorder(),
            ),
          ),
        ],
        if (_phase == _Phase.correct)
          FeedbackBox(
            good: true,
            child: LessonText(
              widget.step.feedbackCorrect,
              style: textTheme.bodyLarge,
            ),
          ),
        if (_phase == _Phase.confirm && check != null)
          FeedbackBox(
            good: false,
            child: Text(
              check.message ?? l10n.tryAgain,
              style: textTheme.bodyLarge,
            ),
          ),
        if (_phase == _Phase.checked || _phase == _Phase.outOfAttempts)
          FeedbackBox(
            good: false,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  check?.message ?? l10n.tryAgain,
                  key: const Key('checker-message'),
                  style: textTheme.bodyLarge,
                ),
                if (_explaining) ...[
                  const SizedBox(height: 8),
                  Text(l10n.photoExplaining, style: textTheme.bodyMedium),
                ],
                if (_explanation != null) ...[
                  const SizedBox(height: 8),
                  Text(
                    _explanation!,
                    key: const Key('ai-reply'),
                    style: textTheme.bodyLarge,
                  ),
                ],
                if (_phase == _Phase.checked && _explanation == null) ...[
                  const SizedBox(height: 8),
                  Text('${l10n.hintLabel}:', style: textTheme.labelLarge),
                  LessonText(widget.step.hint, style: textTheme.bodyLarge),
                ],
                if (_phase == _Phase.outOfAttempts) ...[
                  const SizedBox(height: 8),
                  LessonText(
                    widget.step.correctWorking,
                    style: textTheme.bodyLarge,
                  ),
                ],
              ],
            ),
          ),
        if (_phase.index >= _Phase.confirm.index)
          Padding(
            padding: const EdgeInsets.only(top: 4),
            child: Text(
              [
                if (_readByAi) l10n.readByAi,
                if (check != null) l10n.checkedByCode,
                if (_explanation != null) l10n.explainedByAi,
              ].join(' · '),
              key: const Key('checked-by'),
              style: textTheme.labelSmall,
            ),
          ),
      ],
    );
  }
}
