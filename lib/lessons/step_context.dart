import 'package:flutter/widgets.dart';

/// Which lesson the step on screen belongs to. AI steps need it to ask the
/// server about the right step (the server reads the step itself).
class StepContext extends InheritedWidget {
  const StepContext({super.key, required this.lessonId, required super.child});

  final String lessonId;

  static String? lessonIdOf(BuildContext context) =>
      context.dependOnInheritedWidgetOfExactType<StepContext>()?.lessonId;

  @override
  bool updateShouldNotify(StepContext oldWidget) =>
      lessonId != oldWidget.lessonId;
}
