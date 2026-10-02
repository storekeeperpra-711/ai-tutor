import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../l10n/app_localizations.dart';
import '../../lessons/step_registry.dart';
import '../../lessons/step_result.dart';
import '../../mastery/daily_plan.dart';
import '../../mastery/skill_state.dart';
import '../../services/local_db.dart';
import '../../services/mastery_service.dart';
import '../../services/profiles.dart';
import '../common/sync_status.dart';

/// The plan's questions not yet answered today, one after another.
class PracticeScreen extends ConsumerStatefulWidget {
  const PracticeScreen({super.key});

  @override
  ConsumerState<PracticeScreen> createState() => _PracticeScreenState();
}

class _PracticeScreenState extends ConsumerState<PracticeScreen> {
  List<QuestionItem>? _items;
  var _index = 0;
  var _right = 0;

  @override
  void initState() {
    super.initState();
    _load();
  }

  Future<void> _load() async {
    final student = ref.read(currentStudentProvider);
    if (student == null) return;
    final plan = await ref.read(todayPlanProvider(student.id).future);
    final states = await ref.read(localDbProvider).skillStatesOf(student.id);
    if (!mounted) return;
    setState(() => _items = undoneQuestions(plan, states, DateTime.now()));
  }

  Future<void> _done(StepResult result) async {
    final student = ref.read(currentStudentProvider);
    final item = _items![_index];
    if (result.correct ?? false) _right++;
    if (student != null) {
      await ref
          .read(masteryServiceProvider)
          .recordQuestion(student.id, item.question, result);
    }
    if (mounted) setState(() => _index++);
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final items = _items;
    return Scaffold(
      appBar: AppBar(title: Text(l10n.practiceTitle)),
      body: switch (items) {
        null => const Center(child: CircularProgressIndicator()),
        _ when _index >= items.length => Center(
          child: Padding(
            padding: const EdgeInsets.all(24),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                const Icon(Icons.emoji_events, size: 64, color: Colors.amber),
                const SizedBox(height: 16),
                Text(
                  l10n.practiceDone(_right, items.length),
                  key: const Key('practice-done'),
                  textAlign: TextAlign.center,
                  style: Theme.of(context).textTheme.titleLarge,
                ),
                const SizedBox(height: 24),
                FilledButton(
                  key: const Key('practice-finish'),
                  onPressed: () => Navigator.of(context).pop(),
                  child: Text(l10n.continueButton),
                ),
              ],
            ),
          ),
        ),
        _ => Column(
          children: [
            const Padding(
              padding: EdgeInsets.symmetric(horizontal: 16),
              child: SyncStatus(),
            ),
            Padding(
              padding: const EdgeInsets.fromLTRB(16, 8, 16, 0),
              child: LinearProgressIndicator(value: _index / items.length),
            ),
            Expanded(
              child: KeyedSubtree(
                key: ValueKey(items[_index].key),
                child: buildStep(items[_index].question.step, _done),
              ),
            ),
          ],
        ),
      },
    );
  }
}

/// Question items of [plan] not answered yet today.
List<QuestionItem> undoneQuestions(
  DailyPlan plan,
  Map<String, SkillState> states,
  DateTime now,
) => [
  for (final item in plan.items.whereType<QuestionItem>())
    if (!questionDoneToday(item, states, now)) item,
];

bool questionDoneToday(
  QuestionItem item,
  Map<String, SkillState> states,
  DateTime now,
) {
  final asked = states[item.question.skill]?.recent[item.question.id];
  return asked != null && dayOf(asked) == dayOf(now);
}
