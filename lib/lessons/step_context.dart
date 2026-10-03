import 'package:flutter/widgets.dart';

/// Which lesson (and step) is on screen. AI steps need it to ask the
/// server about the right step; Mithu needs it to find the line's recording.
class StepContext extends InheritedWidget {
  const StepContext({
    super.key,
    required this.lessonId,
    this.stepId,
    required super.child,
  });

  final String lessonId;
  final String? stepId;

  static String? lessonIdOf(BuildContext context) =>
      context.dependOnInheritedWidgetOfExactType<StepContext>()?.lessonId;

  static StepContext? of(BuildContext context) =>
      context.dependOnInheritedWidgetOfExactType<StepContext>();

  @override
  bool updateShouldNotify(StepContext oldWidget) =>
      lessonId != oldWidget.lessonId || stepId != oldWidget.stepId;
}
