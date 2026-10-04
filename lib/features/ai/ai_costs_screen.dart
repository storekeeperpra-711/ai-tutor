import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../ai/ai_service.dart';
import '../../l10n/app_localizations.dart';
import '../../services/profiles.dart';

final _costsProvider = FutureProvider.autoDispose<CostReport>(
  (ref) => ref.read(aiServiceProvider).costs(),
);

/// The cost dashboard: AI calls and estimated cost per student per day,
/// last 7 days. An admin sees every student in the project; other
/// accounts see their own children.
class AiCostsScreen extends ConsumerWidget {
  const AiCostsScreen({super.key});

  static String usd(double value) => '\$${value.toStringAsFixed(4)}';

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final l10n = AppLocalizations.of(context);
    final textTheme = Theme.of(context).textTheme;
    final names = {
      for (final s in ref.watch(studentsProvider).value ?? const [])
        s.id: s.firstName,
    };
    return Scaffold(
      appBar: AppBar(title: Text(l10n.aiCostsTitle)),
      body: switch (ref.watch(_costsProvider)) {
        AsyncData(:final value) => RefreshIndicator(
          onRefresh: () => ref.refresh(_costsProvider.future),
          child: ListView(
            padding: const EdgeInsets.all(16),
            children: [
              Text(
                value.all ? l10n.aiCostsAll : l10n.aiCostsMine,
                style: textTheme.titleMedium,
              ),
              Text(
                l10n.aiCostsTotal(usd(value.totalUsd)),
                key: const Key('costs-total'),
                style: textTheme.headlineSmall,
              ),
              if (value.learning.isNotEmpty) ...[
                const Divider(height: 32),
                Text(l10n.learningTotalsTitle, style: textTheme.titleMedium),
                for (final t in value.learning)
                  ListTile(
                    key: Key('learning-${t.day}'),
                    title: Text(t.day),
                    subtitle: Text(
                      l10n.learningTotalsRow(
                        t.students,
                        t.lessons,
                        t.lessonsFinished,
                        t.questions,
                        t.firstTry,
                        t.aiCalls,
                      ),
                    ),
                  ),
              ],
              const Divider(height: 32),
              if (value.rows.isEmpty) Text(l10n.aiCostsEmpty),
              for (final row in value.rows)
                ListTile(
                  key: Key('cost-${row.day}-${row.studentId}'),
                  title: Text(
                    '${row.day}  ${names[row.studentId] ?? row.studentId}',
                  ),
                  subtitle: Text(
                    l10n.aiCostsRow(
                      row.calls,
                      row.text,
                      row.photo,
                      usd(row.costUsd),
                    ),
                  ),
                ),
            ],
          ),
        ),
        AsyncError() => Center(
          child: Padding(
            padding: const EdgeInsets.all(24),
            child: Text(l10n.needsInternet, key: const Key('costs-error')),
          ),
        ),
        _ => const Center(child: CircularProgressIndicator()),
      },
    );
  }
}
