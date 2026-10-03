import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../l10n/app_localizations.dart';
import '../../services/auth_service.dart';
import '../../services/local_db.dart';
import '../../services/remote_store.dart';

/// Shows the latest weekly note for parents (written by the server's
/// batch job on Sunday evenings). Needs internet.
Future<void> showWeeklyReport(
  BuildContext context,
  WidgetRef ref,
  Student student,
) => showDialog<void>(
  context: context,
  builder: (context) => _WeeklyReportDialog(student: student),
);

class _WeeklyReportDialog extends ConsumerWidget {
  const _WeeklyReportDialog({required this.student});

  final Student student;

  Future<WeeklyReport?> _latest(WidgetRef ref) async {
    final user = ref.read(authServiceProvider).currentUser;
    if (user == null) return null;
    final reports = await ref
        .read(remoteStoreProvider)
        .fetchReports(user.uid, student.id);
    return reports.firstOrNull;
  }

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final l10n = AppLocalizations.of(context);
    final urdu = Localizations.localeOf(context).languageCode == 'ur';
    return AlertDialog(
      title: Text('${l10n.weeklyReport}: ${student.firstName}'),
      content: FutureBuilder<WeeklyReport?>(
        future: _latest(ref),
        builder: (context, snapshot) {
          if (snapshot.connectionState != ConnectionState.done) {
            return const SizedBox(
              height: 80,
              child: Center(child: CircularProgressIndicator()),
            );
          }
          if (snapshot.hasError) {
            return Text(l10n.needsInternet, key: const Key('report-error'));
          }
          final report = snapshot.data;
          if (report == null) {
            return Text(l10n.weeklyReportNone, key: const Key('report-none'));
          }
          return Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(report.week, style: Theme.of(context).textTheme.labelLarge),
              const SizedBox(height: 8),
              Text(
                urdu ? report.noteUr : report.noteEn,
                key: const Key('report-note'),
              ),
              const SizedBox(height: 12),
              Text(
                l10n.weeklyReportStats(
                  report.stats['active_days'] ?? 0,
                  report.stats['lessons_finished'] ?? 0,
                  report.stats['questions_answered'] ?? 0,
                ),
                style: Theme.of(context).textTheme.bodySmall,
              ),
            ],
          );
        },
      ),
      actions: [
        TextButton(
          onPressed: () => Navigator.of(context).pop(),
          child: Text(MaterialLocalizations.of(context).closeButtonLabel),
        ),
      ],
    );
  }
}
