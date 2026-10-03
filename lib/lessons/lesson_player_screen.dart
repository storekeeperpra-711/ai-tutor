import 'dart:async';

import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../features/common/celebration.dart';
import '../features/common/language_toggle.dart';
import '../features/common/sync_status.dart';
import '../features/effort/celebration_view.dart';
import '../features/effort/effort.dart';
import '../features/plan/mastery_level.dart';
import '../media/media_cache.dart';
import '../l10n/app_localizations.dart';
import '../mastery/skill_state.dart';
import '../mastery/stuck.dart';
import '../models/lesson.dart';
import '../models/lesson_step.dart';
import '../services/local_db.dart';
import '../services/mastery_service.dart';
import '../services/profiles.dart';
import '../services/sync_service.dart';
import 'lesson_repository.dart';
import 'lesson_text.dart';
import 'step_registry.dart';
import 'step_result.dart';
import 'steps_screen.dart';

/// Plays a lesson step by step. With a learner chosen, each finished step
/// is saved and the lesson reopens where they stopped.
class LessonPlayerScreen extends ConsumerWidget {
  const LessonPlayerScreen({super.key, required this.lessonId, this.onNote});

  final String lessonId;

  /// Set when a teacher reviews the lesson (Phase 8): a note button on
  /// every step calls it, and nothing is saved for any learner.
  final void Function(BuildContext context, LessonStep step)? onNote;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final lesson = ref.watch(lessonProvider(lessonId));
    final student = onNote != null ? null : ref.watch(currentStudentProvider);
    final progress = student == null
        ? const AsyncData(<String, LessonProgress>{})
        : ref.watch(progressProvider(student.id));
    return switch ((lesson, progress)) {
      (AsyncData(value: final l), AsyncData(value: final p)) => _LessonPlayer(
        lesson: l,
        student: student,
        startIndex: resumeIndex(l, p[l.id]),
        onNote: onNote,
      ),
      (AsyncError(:final error), _) ||
      (_, AsyncError(:final error)) => Scaffold(
        appBar: AppBar(),
        body: Padding(
          padding: const EdgeInsets.all(16),
          child: Text(
            '${AppLocalizations.of(context).lessonLoadError}\n\n$error',
          ),
        ),
      ),
      _ => const Scaffold(body: Center(child: CircularProgressIndicator())),
    };
  }
}

/// Where to open [lesson]: the step after the last one finished, or the
/// start if the lesson was finished or has changed since.
int resumeIndex(Lesson lesson, LessonProgress? progress) {
  if (progress == null ||
      progress.completed ||
      progress.lessonVersion != lesson.version) {
    return 0;
  }
  return progress.nextStep.clamp(0, lesson.steps.length - 1);
}

class _LessonPlayer extends ConsumerStatefulWidget {
  const _LessonPlayer({
    required this.lesson,
    required this.student,
    required this.startIndex,
    this.onNote,
  });

  final Lesson lesson;
  final void Function(BuildContext context, LessonStep step)? onNote;

  /// null in the previewer without a learner: nothing is saved.
  final Student? student;
  final int startIndex;

  @override
  ConsumerState<_LessonPlayer> createState() => _LessonPlayerState();
}

class _LessonPlayerState extends ConsumerState<_LessonPlayer> {
  late var _index = widget.startIndex;

  /// Results of the steps played in this visit.
  final _results = <StepResult>[];

  /// Saves the step on the phone (instant, works offline), then asks the
  /// sync service to copy it to the account. The lesson never waits.
  Future<void> _save(int index, StepResult result) async {
    final student = widget.student;
    if (student == null) return;
    await ref
        .read(localDbProvider)
        .recordStep(
          studentId: student.id,
          lessonId: widget.lesson.id,
          lessonVersion: widget.lesson.version,
          stepIndex: index,
          stepCount: widget.lesson.steps.length,
          result: result,
        );
    unawaited(ref.read(syncServiceProvider).sync());
  }

  var _prefetched = false;

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    // Start downloading the lesson's linked videos now, so they are
    // ready by the time the child reaches them.
    if (!_prefetched) {
      _prefetched = true;
      ref
          .read(mediaCacheProvider)
          .prefetch(
            widget.lesson,
            Localizations.localeOf(context).languageCode,
          );
    }
  }

  /// Alternative explanations already shown in this visit.
  final _shownAlternatives = <String>{};

  /// Waits for the step to be saved and scored, then helps a stuck
  /// student (spec B3) before moving on.
  var _busy = false;

  Future<void> _onStepDone(StepResult result) async {
    if (_busy) return;
    _busy = true;
    try {
      final step = widget.lesson.steps[_index];
      await _save(_index, result);
      _results.add(result);
      final change = await _recordMastery(step, result);
      if (!mounted) return;
      if (change != null && result.correct == false) {
        final keepGoing = await _helpWhenStuck(step, change.state);
        if (!keepGoing || !mounted) return;
      }
      final last = _index == widget.lesson.steps.length - 1;
      if (last) {
        await _finish();
        return;
      }
      if (change != null && change.levelledUp) await _celebrateLevel(change);
      if (mounted) setState(() => _index++);
    } finally {
      _busy = false;
    }
  }

  /// Shown when the lesson is finished.
  ({LessonStars stars, Lesson? next})? _finished;

  Future<void> _finish() async {
    final student = widget.student;
    final answers = <String, StepAnswer>{};
    var progress = const <String, LessonProgress>{};
    if (student != null) {
      final db = ref.read(localDbProvider);
      for (final r in await db.stepResultsOf(student.id)) {
        if (r.lessonId == widget.lesson.id) answers[r.stepId] = answerOf(r);
      }
      progress = ref.read(progressProvider(student.id)).value ?? progress;
    }
    for (final r in _results) {
      answers[r.stepId] = (
        stepId: r.stepId,
        correct: r.correct,
        attempts: r.attempts,
      );
    }
    final curriculum = await ref.read(curriculumProvider.future);
    if (!mounted) return;
    setState(
      () => _finished = (
        stars: starsFor(widget.lesson, answers.values, completed: true),
        next: nextLessonAfter(curriculum, widget.lesson, progress),
      ),
    );
  }

  Future<void> _celebrateLevel(SkillChange change) async {
    final curriculum = await ref.read(curriculumProvider.future);
    if (!mounted) return;
    final l10n = AppLocalizations.of(context);
    final skill = change.state.skill;
    celebrate(
      context,
      l10n.levelUp(
        curriculum.titleOf(skill)?.of(context) ?? skill,
        levelName(l10n, change.after),
      ),
    );
  }

  /// Feeds the answer to the mastery engine (learners only).
  Future<SkillChange?> _recordMastery(LessonStep step, StepResult result) {
    final student = widget.student;
    if (student == null) return Future.value();
    return ref
        .read(masteryServiceProvider)
        .recordStep(student.id, widget.lesson, step, result);
  }

  /// Shows the next idea on the stuck ladder. Returns false if the student
  /// chose to stop for now (the lesson closes; their place is saved).
  Future<bool> _helpWhenStuck(LessonStep step, SkillState state) async {
    final student = widget.student!;
    final curriculum = await ref.read(curriculumProvider.future);
    final states = await ref.read(localDbProvider).skillStatesOf(student.id);
    if (!mounted) return true;
    final advice = adviseWhenStuck(
      state: state,
      lesson: widget.lesson,
      stepId: step.id,
      curriculum: curriculum,
      states: states,
      shownAlternatives: _shownAlternatives,
    );
    final l10n = AppLocalizations.of(context);
    switch (advice) {
      case null:
        return true;
      case ShowAlternative(:final alternative):
        _shownAlternatives.add(alternative.id);
        await Navigator.of(context).push(
          MaterialPageRoute<void>(
            builder: (_) => StepsScreen(
              title: l10n.tryAnotherWay,
              lessonId: widget.lesson.id,
              steps: alternative.steps,
              onStepDone: (s, r) => _recordMastery(s, r),
            ),
          ),
        );
        return true;
      case GoBackToPrerequisite(:final skill, :final lessonId):
        final title = curriculum.titleOf(skill)?.of(context) ?? skill;
        final open = await _ask(l10n.stuckPrerequisite(title), l10n.openLesson);
        if (open && mounted) unawaited(context.push('/lesson/$lessonId'));
        return true;
      case TakeABreak():
        return !await _ask(l10n.stuckBreak, l10n.takeBreak);
      case GetHelp():
        return !await _ask(l10n.stuckHelp, l10n.takeBreak);
    }
  }

  /// A small dialog with "Keep going" and [action]. True if [action] was
  /// chosen.
  Future<bool> _ask(String message, String action) async {
    final l10n = AppLocalizations.of(context);
    final chosen = await showDialog<bool>(
      context: context,
      barrierDismissible: false,
      builder: (context) => AlertDialog(
        key: const Key('stuck-dialog'),
        content: Text(message),
        actions: [
          TextButton(
            key: const Key('stuck-action'),
            onPressed: () => Navigator.pop(context, true),
            child: Text(action),
          ),
          FilledButton(
            key: const Key('stuck-keep-going'),
            onPressed: () => Navigator.pop(context, false),
            child: Text(l10n.keepGoing),
          ),
        ],
      ),
    );
    if (chosen == true && action == l10n.takeBreak && mounted) {
      await Navigator.of(context).maybePop(_results);
    }
    return chosen ?? false;
  }

  @override
  Widget build(BuildContext context) {
    final steps = widget.lesson.steps;
    final step = steps[_index];
    final l10n = AppLocalizations.of(context);
    if (_finished case (:final stars, :final next)) {
      return Scaffold(
        appBar: AppBar(title: LessonText(widget.lesson.title)),
        body: CelebrationView(
          lesson: widget.lesson,
          stars: stars,
          next: next,
          onNext: () => context.pushReplacement('/lesson/${next!.id}'),
          onHome: () => Navigator.of(context).maybePop(_results),
        ),
      );
    }

    return Scaffold(
      appBar: AppBar(
        title: LessonText(widget.lesson.title),
        actions: [
          if (widget.onNote case final onNote?)
            IconButton(
              key: const Key('review-note'),
              tooltip: l10n.reviewAddNote,
              icon: const Icon(Icons.edit_note),
              onPressed: () => onNote(context, step),
            ),
          const LanguageToggle(),
        ],
        bottom: PreferredSize(
          preferredSize: const Size.fromHeight(28),
          child: Padding(
            padding: const EdgeInsets.fromLTRB(16, 0, 16, 8),
            child: Row(
              children: [
                Expanded(
                  child: LinearProgressIndicator(
                    value: (_index + 1) / steps.length,
                  ),
                ),
                const SizedBox(width: 12),
                Text(l10n.stepProgress(_index + 1, steps.length)),
              ],
            ),
          ),
        ),
      ),
      body: Column(
        children: [
          const Padding(
            padding: EdgeInsets.symmetric(horizontal: 16),
            child: SyncStatus(),
          ),
          Expanded(
            // The key gives each step a fresh state.
            child: KeyedSubtree(
              key: ValueKey(step.id),
              child: buildStep(
                step,
                (r) => unawaited(_onStepDone(r)),
                lessonId: widget.lesson.id,
              ),
            ),
          ),
        ],
      ),
    );
  }
}
