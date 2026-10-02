import 'dart:convert';

import 'package:ai_tutor/lessons/step_result.dart';
import 'package:ai_tutor/mastery/curriculum.dart';
import 'package:ai_tutor/mastery/daily_plan.dart';
import 'package:ai_tutor/mastery/skill_state.dart';
import 'package:ai_tutor/models/lesson_step.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:shared_preferences/shared_preferences.dart';

import '../fakes.dart';
import '../helpers.dart';
import '../lessons/play_helpers.dart';
import '../mastery/lessons.dart';
import 'profiles_and_progress_test.dart' show lesson, playSteps;

final curriculum = Curriculum(loadLessons());

/// A skill at Practising: one required type right on the first try,
/// yesterday.
SkillState practising(String skill, {bool needsHelp = false}) {
  final criteria = curriculum.criteriaFor(skill)!;
  final yesterday = DateTime.now().subtract(const Duration(days: 1));
  final s = SkillState(skill: skill).record(
    Evidence(
      skill: skill,
      itemId: 'seed',
      at: yesterday,
      firstTry: true,
      solved: true,
      questionType: criteria.questionTypes.first,
    ),
    criteria,
  );
  return needsHelp
      ? SkillState.fromJson({...s.toJson(), 'stuck': 4, 'needs_help': true})
      : s;
}

void main() {
  setUp(() {
    final view =
        TestWidgetsFlutterBinding.instance.platformDispatcher.views.first;
    view.physicalSize = const Size(1080, 2340);
    view.devicePixelRatio = 3;
  });

  tearDown(() {
    TestWidgetsFlutterBinding.instance.platformDispatcher.views.first
      ..resetPhysicalSize()
      ..resetDevicePixelRatio();
  });

  testWidgets('a wrong answer shows another way to explain the step', (
    tester,
  ) async {
    final backend = FakeBackend();
    await backend.db.addStudent(student('ayesha'));
    await tester.pumpWidget(await buildTestApp(backend: backend));
    await tester.pumpAndSettle();

    await tapKey(tester, 'student-ayesha');
    await tapKey(tester, 'home-lesson-${lesson.id}');
    final quarters = lesson.steps.indexWhere((s) => s.id == 's5_quarters');
    await playSteps(tester, 0, quarters);

    // Three wrong answers, then the worked answer and Continue.
    final step = lesson.steps[quarters] as NumberStep;
    for (var i = 0; i < step.maxAttempts; i++) {
      await tester.enterText(find.byKey(const Key('answer-input')), '0.5');
      await tapKey(tester, 'step-check');
    }
    await tapKey(tester, 'step-continue');

    // The alternative explanation, then back to the lesson's next step.
    expect(find.text("Let's try it another way."), findsOneWidget);
    await tapKey(tester, 'step-continue');
    await tester.enterText(find.byKey(const Key('answer-input')), '8');
    await tapKey(tester, 'step-check');
    await tapKey(tester, 'step-continue');
    expect(
      find.text('Step ${quarters + 2} of ${lesson.steps.length}'),
      findsOneWidget,
    );

    final state = (await backend.db.skillStatesOf('ayesha'))[fractions]!;
    expect(state.stuck, 0, reason: 'the alternative was right first time');
    expect(state.firstTryCorrect, greaterThan(0));
    expect(await backend.db.unsyncedSkillStates(), isEmpty);
    final uid = backend.auth.currentUser!.uid;
    expect(
      backend.remote.docs['accounts/$uid/students/ayesha/skills/$fractions'],
      isNotNull,
    );
  });

  testWidgets("today's plan: practice questions, flashcards and dots", (
    tester,
  ) async {
    final backend = FakeBackend();
    await backend.db.addStudent(student('ayesha'));
    await backend.db.saveSkillState('ayesha', practising(fractions));
    // The lesson is finished, so the plan is practice, not a new lesson.
    await backend.db.recordStep(
      studentId: 'ayesha',
      lessonId: lesson.id,
      lessonVersion: lesson.version,
      stepIndex: lesson.steps.length - 1,
      stepCount: lesson.steps.length,
      result: StepResult(stepId: lesson.steps.last.id),
    );
    await tester.pumpWidget(await buildTestApp(backend: backend));
    await tester.pumpAndSettle();

    await tapKey(tester, 'student-ayesha');
    expect(find.byKey(const Key('today-plan')), findsOneWidget);
    expect(find.byKey(Key('mastery-${lesson.id}')), findsOneWidget);

    final prefs = await SharedPreferences.getInstance();
    final saved =
        jsonDecode(prefs.getString('plan.ayesha')!) as Map<String, dynamic>;
    final plan = planFromKeys(
      DateTime.now(),
      (saved['keys'] as List<dynamic>).cast(),
      curriculum,
    );
    final questions = plan.items.whereType<QuestionItem>().toList();
    expect(questions, isNotEmpty);
    expect(plan.items.whereType<FlashcardsItem>(), isNotEmpty);

    // Practice: answer every plan question right.
    await tapKey(tester, 'start-practice');
    for (final q in questions) {
      await answerStep(tester, q.question.step, tryWrongFirst: false);
      await tapKey(tester, 'step-continue');
    }
    expect(
      find.text(
        'Well done! ${questions.length} of ${questions.length} right the first time.',
      ),
      findsOneWidget,
    );
    await tapKey(tester, 'practice-finish');
    expect(find.byKey(const Key('start-practice')), findsNothing);

    // Flashcards: turn and go through every card.
    final cards = plan.items.whereType<FlashcardsItem>().first;
    await tapKey(tester, 'plan-${cards.key}');
    for (var i = 0; i < 20; i++) {
      if (find.byKey(const Key('flashcard')).evaluate().isEmpty) break;
      await tapKey(tester, 'flashcard');
      await tapKey(tester, 'flashcard-next');
    }
    expect(find.byKey(const Key('today-plan')), findsOneWidget);
    final tile = tester.widget<ListTile>(find.byKey(Key('plan-${cards.key}')));
    expect((tile.leading! as Icon).icon, Icons.check_circle);
  });

  testWidgets('the account screen shows who needs help', (tester) async {
    final backend = FakeBackend();
    await backend.db.addStudent(student('ayesha'));
    await backend.db.saveSkillState(
      'ayesha',
      practising(fractions, needsHelp: true),
    );
    await tester.pumpWidget(await buildTestApp(backend: backend));
    await tester.pumpAndSettle();

    await tapKey(tester, 'open-account');
    expect(find.byKey(const Key('needs-help-ayesha')), findsOneWidget);
  });
}
