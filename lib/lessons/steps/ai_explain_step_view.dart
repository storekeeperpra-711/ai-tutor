import 'dart:async';

import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../ai/ai_help.dart';
import '../../ai/ai_service.dart';
import '../../ai/keyword_fallback.dart';
import '../../app/motion_widgets.dart';
import '../../character/mithu_bubble.dart';
import '../../l10n/app_localizations.dart';
import '../../models/lesson_step.dart';
import '../../models/localized_text.dart';
import '../../services/local_db.dart';
import '../../services/profiles.dart';
import '../../services/sync_service.dart';
import '../lesson_text.dart';
import '../step_context.dart';
import '../step_result.dart';
import 'step_scaffold.dart';

/// The student explains an idea in their own words (or makes up their own
/// question). Mithu's AI feedback comes through the server; offline, on an
/// error or when a limit is reached, the keywords score it on the phone and
/// the step's own feedback is shown. An answer that couldn't reach the AI
/// waits in the queue for the batch job.
class AiExplainStepView extends ConsumerStatefulWidget {
  const AiExplainStepView({
    super.key,
    required this.step,
    required this.onDone,
  });

  final AiExplainStep step;
  final StepDone onDone;

  @override
  ConsumerState<AiExplainStepView> createState() => _AiExplainStepViewState();
}

enum _Phase { writing, checking, feedback }

/// Who checked the answer, for the label under the feedback.
enum _CheckedBy { ai, keywords }

class _AiExplainStepViewState extends ConsumerState<AiExplainStepView> {
  final _controller = TextEditingController();
  var _phase = _Phase.writing;
  var _attempts = 0;
  var _solved = false;
  var _firstTry = false;

  AiLevel? _level;
  String? _reply;
  _CheckedBy? _checkedBy;

  /// Extra line: queued for later, or a limit was reached.
  String? _note;

  /// One queued answer per visit to this step; a better answer replaces it.
  String? _queuedId;

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  Future<void> _check() async {
    final answer = _controller.text.trim();
    if (answer.isEmpty) return;
    final l10n = AppLocalizations.of(context);
    final language = Localizations.localeOf(context).languageCode;
    final lessonId = StepContext.lessonIdOf(context);
    final student = ref.read(currentStudentProvider);
    setState(() => _phase = _Phase.checking);

    AiFeedback? feedback;
    var queue = false;
    // With AI help off, nothing is sent: the keywords check the answer.
    if (student != null && lessonId != null && ref.read(aiHelpProvider)) {
      try {
        feedback = await ref
            .read(aiServiceProvider)
            .explain(
              studentId: student.id,
              lessonId: lessonId,
              stepId: widget.step.id,
              language: language,
              answer: answer,
            );
      } on AiUnavailable {
        queue = true;
      }
    }
    if (!mounted) return;

    final level =
        feedback?.level ?? scoreByKeywords(answer, widget.step.keywords);
    final byAi = feedback?.byAi ?? false;
    String? note;
    if (queue) {
      note = l10n.aiQueued;
      await _queue(student!.id, lessonId!, language, answer);
    } else if (const {
      'student_limit',
      'step_limit',
      'budget',
    }.contains(feedback?.reason)) {
      note = l10n.aiLimitReached;
    }
    if (!mounted) return;

    setState(() {
      _attempts++;
      _phase = _Phase.feedback;
      _level = level;
      _reply = byAi
          ? feedback!.reply
          : _fallbackText(level).inLanguage(language);
      _checkedBy = byAi ? _CheckedBy.ai : _CheckedBy.keywords;
      _note = note;
      if (level == AiLevel.gotIt) {
        _solved = true;
        _firstTry = _attempts == 1;
      }
    });
  }

  LocalizedText _fallbackText(AiLevel level) => switch (level) {
    AiLevel.gotIt => widget.step.fallbackFeedback.gotIt,
    AiLevel.partly => widget.step.fallbackFeedback.partly,
    AiLevel.notYet => widget.step.fallbackFeedback.notYet,
  };

  Future<void> _queue(
    String studentId,
    String lessonId,
    String language,
    String answer,
  ) async {
    _queuedId ??= newId();
    await ref
        .read(localDbProvider)
        .queueAnswer(
          QueuedAnswer(
            id: _queuedId!,
            studentId: studentId,
            lessonId: lessonId,
            stepId: widget.step.id,
            task: widget.step.task.inLanguage(language),
            lang: language,
            answer: answer,
            createdAt: DateTime.now(),
            uploaded: false,
            status: 'waiting',
            seen: false,
          ),
        );
    unawaited(ref.read(syncServiceProvider).sync());
  }

  void _improve() => setState(() => _phase = _Phase.writing);

  void _finish() => widget.onDone(
    StepResult(
      stepId: widget.step.id,
      correct: _firstTry,
      solved: _solved,
      attempts: _attempts,
    ),
  );

  String _levelLabel(AppLocalizations l10n, AiLevel level) => switch (level) {
    AiLevel.gotIt => l10n.levelGotIt,
    AiLevel.partly => l10n.levelPartly,
    AiLevel.notYet => l10n.levelNotYet,
  };

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final textTheme = Theme.of(context).textTheme;
    final writing = _phase == _Phase.writing;
    final canImprove =
        _phase == _Phase.feedback &&
        !_solved &&
        _attempts < widget.step.maxAttempts;

    return StepScaffold(
      buttonKey: Key(writing ? 'step-check' : 'step-continue'),
      buttonLabel: writing ? l10n.checkButton : l10n.continueButton,
      onPressed: switch (_phase) {
        _Phase.writing => _check,
        _Phase.checking => null,
        _Phase.feedback => _finish,
      },
      children: [
        if (widget.step.character != null) ...[
          MithuBubble(line: widget.step.character!),
          const SizedBox(height: 24),
        ],
        LessonText(widget.step.task, style: textTheme.titleLarge),
        const SizedBox(height: 16),
        TextField(
          key: const Key('answer-input'),
          controller: _controller,
          enabled: writing,
          keyboardType: TextInputType.multiline,
          minLines: 3,
          maxLines: 8,
          maxLength: 1500,
          style: textTheme.bodyLarge,
          decoration: InputDecoration(
            labelText: l10n.answerLabel,
            helperText: l10n.explainInputHelp,
          ),
        ),
        if (_phase == _Phase.checking)
          Padding(
            padding: const EdgeInsets.only(top: 16),
            child: Row(
              children: [
                const ThinkingDots(),
                const SizedBox(width: 12),
                Expanded(child: Text(l10n.aiThinking)),
              ],
            ),
          ),
        if (_phase == _Phase.feedback && _level != null) ...[
          FeedbackBox(
            good: _level == AiLevel.gotIt,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  _levelLabel(l10n, _level!),
                  key: Key('ai-level-${_level!.id}'),
                  style: textTheme.titleMedium,
                ),
                const SizedBox(height: 4),
                Text(
                  _reply ?? '',
                  key: const Key('ai-reply'),
                  style: textTheme.bodyLarge,
                ),
              ],
            ),
          ),
          if (_note != null)
            Padding(
              padding: const EdgeInsets.only(top: 8),
              child: Text(
                _note!,
                key: const Key('ai-note'),
                style: textTheme.bodyMedium,
              ),
            ),
          Padding(
            padding: const EdgeInsets.only(top: 4),
            child: Text(
              _checkedBy == _CheckedBy.ai
                  ? l10n.checkedByAi
                  : l10n.checkedByKeywords,
              key: const Key('checked-by'),
              style: textTheme.labelSmall,
            ),
          ),
          if (canImprove)
            Align(
              alignment: AlignmentDirectional.centerStart,
              child: TextButton.icon(
                key: const Key('ai-improve'),
                onPressed: _improve,
                icon: const Icon(Icons.edit),
                label: Text(l10n.improveAnswer),
              ),
            ),
        ],
      ],
    );
  }
}
