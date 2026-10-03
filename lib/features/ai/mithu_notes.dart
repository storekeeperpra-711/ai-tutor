import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../../ai/ai_service.dart';
import '../../l10n/app_localizations.dart';
import '../../services/local_db.dart';
import '../../services/profiles.dart';

/// A child's answers that waited offline for AI feedback, newest first.
final queuedAnswersProvider = StreamProvider.family<List<QueuedAnswer>, String>(
  (ref, studentId) => ref.watch(localDbProvider).watchQueuedAnswers(studentId),
);

/// Home card: Mithu's replies arrived for answers given offline.
class MithuNotesCard extends ConsumerWidget {
  const MithuNotesCard({super.key, required this.student});

  final Student student;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final answers = ref.watch(queuedAnswersProvider(student.id)).value ?? [];
    final fresh = answers
        .where((a) => a.status == 'answered' && !a.seen)
        .length;
    if (fresh == 0) return const SizedBox.shrink();
    return Card(
      child: ListTile(
        key: const Key('mithu-notes-card'),
        leading: const Icon(Icons.mark_chat_unread),
        title: Text(AppLocalizations.of(context).mithuNotesNew(fresh)),
        trailing: const Icon(Icons.chevron_right),
        onTap: () => context.push('/notes'),
      ),
    );
  }
}

/// Mithu's notes: each queued answer with the AI's reply, or "waiting".
class MithuNotesScreen extends ConsumerStatefulWidget {
  const MithuNotesScreen({super.key});

  @override
  ConsumerState<MithuNotesScreen> createState() => _MithuNotesScreenState();
}

class _MithuNotesScreenState extends ConsumerState<MithuNotesScreen> {
  late final LocalDb _db;
  String? _studentId;

  @override
  void initState() {
    super.initState();
    // Kept for dispose, where `ref` can't be used any more.
    _db = ref.read(localDbProvider);
    _studentId = ref.read(currentStudentProvider)?.id;
  }

  @override
  void dispose() {
    // Leaving the notes counts as having read them.
    if (_studentId case final id?) _db.markRepliesSeen(id);
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final textTheme = Theme.of(context).textTheme;
    final student = ref.watch(currentStudentProvider);
    final answers = student == null
        ? const <QueuedAnswer>[]
        : ref.watch(queuedAnswersProvider(student.id)).value ?? const [];
    return Scaffold(
      appBar: AppBar(title: Text(l10n.mithuNotesTitle)),
      body: answers.isEmpty
          ? Center(child: Text(l10n.mithuNotesEmpty))
          : ListView(
              padding: const EdgeInsets.all(16),
              children: [
                for (final a in answers)
                  Card(
                    key: Key('note-${a.id}'),
                    child: Padding(
                      padding: const EdgeInsets.all(16),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(a.task, style: textTheme.titleMedium),
                          const SizedBox(height: 8),
                          Text('“${a.answer}”', style: textTheme.bodyLarge),
                          const Divider(height: 24),
                          Text(switch (a.status) {
                            'answered' => a.reply ?? '',
                            'failed' => l10n.mithuNotesFailed,
                            _ => l10n.mithuNotesWaiting,
                          }, style: textTheme.bodyLarge),
                          if (a.status == 'answered') ...[
                            const SizedBox(height: 4),
                            Text(
                              [
                                switch (AiLevel.fromId(a.level)) {
                                  AiLevel.gotIt => l10n.levelGotIt,
                                  AiLevel.partly => l10n.levelPartly,
                                  _ => l10n.levelNotYet,
                                },
                                l10n.checkedByAi,
                              ].join(' · '),
                              style: textTheme.labelSmall,
                            ),
                          ],
                        ],
                      ),
                    ),
                  ),
              ],
            ),
    );
  }
}
