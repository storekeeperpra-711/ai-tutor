import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../features/common/language_toggle.dart';
import '../l10n/app_localizations.dart';
import '../models/lesson.dart';
import 'lesson_repository.dart';
import 'lesson_text.dart';
import 'step_registry.dart';
import 'step_result.dart';

/// Plays a lesson step by step.
class LessonPlayerScreen extends ConsumerWidget {
  const LessonPlayerScreen({super.key, required this.lessonId});

  final String lessonId;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final lesson = ref.watch(lessonProvider(lessonId));
    return switch (lesson) {
      AsyncData(:final value) => _LessonPlayer(lesson: value),
      AsyncError(:final error) => Scaffold(
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

class _LessonPlayer extends StatefulWidget {
  const _LessonPlayer({required this.lesson});

  final Lesson lesson;

  @override
  State<_LessonPlayer> createState() => _LessonPlayerState();
}

class _LessonPlayerState extends State<_LessonPlayer> {
  var _index = 0;

  /// Results so far. Saved to the device and Firebase in Phase 3.
  final _results = <StepResult>[];

  void _onStepDone(StepResult result) {
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
      // The key gives each step a fresh state.
      body: KeyedSubtree(
        key: ValueKey(step.id),
        child: buildStep(step, _onStepDone),
      ),
    );
  }
}
