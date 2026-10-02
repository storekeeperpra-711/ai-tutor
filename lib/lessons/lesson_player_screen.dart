import 'dart:async';

import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../features/common/language_toggle.dart';
import '../features/common/sync_status.dart';
import '../l10n/app_localizations.dart';
import '../models/lesson.dart';
import '../services/local_db.dart';
import '../services/profiles.dart';
import '../services/sync_service.dart';
import 'lesson_repository.dart';
import 'lesson_text.dart';
import 'step_registry.dart';
import 'step_result.dart';

/// Plays a lesson step by step. With a learner chosen, each finished step
/// is saved and the lesson reopens where they stopped.
class LessonPlayerScreen extends ConsumerWidget {
  const LessonPlayerScreen({super.key, required this.lessonId});

  final String lessonId;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final lesson = ref.watch(lessonProvider(lessonId));
    final student = ref.watch(currentStudentProvider);
    final progress = student == null
        ? const AsyncData(<String, LessonProgress>{})
        : ref.watch(progressProvider(student.id));
    return switch ((lesson, progress)) {
      (AsyncData(value: final l), AsyncData(value: final p)) => _LessonPlayer(
        lesson: l,
        student: student,
        startIndex: resumeIndex(l, p[l.id]),
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
  });

  final Lesson lesson;

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

  void _onStepDone(StepResult result) {
    unawaited(_save(_index, result));
    _results.add(result);
    if (_index < widget.lesson.steps.length - 1) {
      setState(() => _index++);
    } else {
      Navigator.of(context).maybePop(_results);
    }
  }

  @override
  Widget build(BuildContext context) {
    final steps = widget.lesson.steps;
    final step = steps[_index];
    final l10n = AppLocalizations.of(context);

    return Scaffold(
      appBar: AppBar(
        title: LessonText(widget.lesson.title),
        actions: const [LanguageToggle()],
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
              child: buildStep(step, _onStepDone),
            ),
          ),
        ],
      ),
    );
  }
}
