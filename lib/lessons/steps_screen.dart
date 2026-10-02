import 'package:flutter/material.dart';

import '../models/lesson_step.dart';
import 'step_registry.dart';
import 'step_result.dart';

/// Plays a short list of steps on its own screen (an alternative
/// explanation, or practice questions) and closes at the end.
class StepsScreen extends StatefulWidget {
  const StepsScreen({
    super.key,
    required this.title,
    required this.steps,
    required this.onStepDone,
  });

  final String title;
  final List<LessonStep> steps;
  final Future<void> Function(LessonStep step, StepResult result) onStepDone;

  @override
  State<StepsScreen> createState() => _StepsScreenState();
}

class _StepsScreenState extends State<StepsScreen> {
  var _index = 0;

  Future<void> _done(StepResult result) async {
    await widget.onStepDone(widget.steps[_index], result);
    if (!mounted) return;
    if (_index < widget.steps.length - 1) {
      setState(() => _index++);
    } else {
      Navigator.of(context).pop();
    }
  }

  @override
  Widget build(BuildContext context) {
    final step = widget.steps[_index];
    return Scaffold(
      appBar: AppBar(title: Text(widget.title)),
      body: KeyedSubtree(key: ValueKey(step.id), child: buildStep(step, _done)),
    );
  }
}
