import 'package:flutter/widgets.dart';

import '../models/lesson_step.dart';
import 'step_context.dart';
import 'step_result.dart';
import 'steps/ai_explain_step_view.dart';
import 'steps/choice_step_view.dart';
import 'steps/explain_step_view.dart';
import 'steps/lottie_step_view.dart';
import 'steps/number_step_view.dart';
import 'steps/photo_check_step_view.dart';
import 'steps/pick_picture_step_view.dart';
import 'steps/sim_step_view.dart';
import 'steps/summary_step_view.dart';
import 'steps/tap_count_step_view.dart';
import 'steps/text_check_step_view.dart';
import 'steps/unsupported_step_view.dart';
import 'steps/video_step_view.dart';

typedef StepBuilder = Widget Function(LessonStep step, StepDone onDone);

/// Which widget plays which step type. New lessons never need new code;
/// a new step type needs one new widget and one line here.
final stepBuilders = <String, StepBuilder>{
  'explain': (s, done) => ExplainStepView(step: s as ExplainStep, onDone: done),
  'choice': (s, done) => ChoiceStepView(step: s as ChoiceStep, onDone: done),
  'number': (s, done) => NumberStepView(step: s as NumberStep, onDone: done),
  'text_check': (s, done) =>
      TextCheckStepView(step: s as TextCheckStep, onDone: done),
  'summary': (s, done) => SummaryStepView(step: s as SummaryStep, onDone: done),
  'sim': (s, done) => SimStepView(step: s as SimStep, onDone: done),
  'video': (s, done) => VideoStepView(step: s as VideoStep, onDone: done),
  'lottie': (s, done) => LottieStepView(step: s as LottieStep, onDone: done),
  'ai_explain': (s, done) =>
      AiExplainStepView(step: s as AiExplainStep, onDone: done),
  'photo_check': (s, done) =>
      PhotoCheckStepView(step: s as PhotoCheckStep, onDone: done),
  'tap_count': (s, done) =>
      TapCountStepView(step: s as TapCountStep, onDone: done),
  'pick_picture': (s, done) =>
      PickPictureStepView(step: s as PickPictureStep, onDone: done),
};

/// The widget for [step] of lesson [lessonId].
Widget buildStep(LessonStep step, StepDone onDone, {required String lessonId}) {
  final builder = stepBuilders[step.type];
  if (builder == null || step is UnsupportedStep) {
    return UnsupportedStepView(step: step, onDone: onDone);
  }
  return StepContext(
    lessonId: lessonId,
    stepId: step.id,
    child: builder(step, onDone),
  );
}
