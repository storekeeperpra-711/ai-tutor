import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../../app/theme/age_tier.dart';
import '../../l10n/app_localizations.dart';
import '../../services/local_db.dart';
import '../../services/profiles.dart';
import '../common/sync_status.dart';
import '../profiles/avatar.dart';
import '../profiles/pin_pad.dart';
import 'early_home.dart';
import 'tier_homes.dart';

/// Home: "Who is learning?" until a child picks their picture, then the
/// home for that child's age group (spec C4).
class HomeScreen extends ConsumerWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final l10n = AppLocalizations.of(context);
    final students = ref.watch(studentsProvider);
    final current = ref.watch(currentStudentProvider);

    return Scaffold(
      appBar: AppBar(
        title: Text(l10n.appTitle),
        actions: [
          IconButton(
            key: const Key('open-account'),
            icon: const Icon(Icons.family_restroom),
            tooltip: l10n.accountTitle,
            onPressed: () => context.push('/account'),
          ),
          IconButton(
            icon: const Icon(Icons.settings),
            tooltip: l10n.settingsTitle,
            onPressed: () => context.push('/settings'),
          ),
        ],
      ),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          const Center(child: SyncStatus()),
          ...switch (students) {
            AsyncData(value: final list) when list.isEmpty => [
              const SizedBox(height: 24),
              Text(
                l10n.homeWelcome,
                style: Theme.of(context).textTheme.headlineSmall,
                textAlign: TextAlign.center,
              ),
              const SizedBox(height: 24),
              Center(
                child: FilledButton.icon(
                  key: const Key('add-learner'),
                  icon: const Icon(Icons.person_add),
                  label: Text(l10n.addLearner),
                  onPressed: () => context.push('/learners/new'),
                ),
              ),
              const SizedBox(height: 8),
              Center(
                child: TextButton.icon(
                  key: const Key('home-privacy'),
                  icon: const Icon(Icons.privacy_tip_outlined),
                  label: Text(l10n.privacyTitle),
                  onPressed: () => context.push('/privacy'),
                ),
              ),
            ],
            AsyncData(value: final list) when current == null => [
              _WhoIsLearning(students: list),
            ],
            AsyncData() => [_StudentHome(student: current!)],
            AsyncError(:final error) => [Text('$error')],
            _ => [const Center(child: CircularProgressIndicator())],
          },
          if (kDebugMode) ...[
            const Divider(height: 48),
            Center(
              child: FilledButton(
                key: const Key('open-previewer'),
                onPressed: () => context.push('/dev/lessons'),
                child: Text(l10n.lessonsPreviewTitle),
              ),
            ),
            const SizedBox(height: 12),
            Center(
              child: OutlinedButton(
                key: const Key('open-sim-gallery'),
                onPressed: () => context.push('/dev/sims'),
                child: Text(l10n.simGalleryTitle),
              ),
            ),
            const SizedBox(height: 12),
            Center(
              child: OutlinedButton(
                key: const Key('open-recorder'),
                onPressed: () => context.push('/dev/voice'),
                child: Text(l10n.recorderTitle),
              ),
            ),
            const SizedBox(height: 12),
            Center(
              child: OutlinedButton(
                onPressed: () => context.push('/debug/urdu'),
                child: Text(l10n.urduTestTitle),
              ),
            ),
          ],
        ],
      ),
    );
  }
}

/// Big pictures; a child taps their own (and enters their PIN if set).
class _WhoIsLearning extends ConsumerWidget {
  const _WhoIsLearning({required this.students});

  final List<Student> students;

  Future<void> _pick(BuildContext context, WidgetRef ref, Student s) async {
    if (s.pinHash != null && await askForPin(context, s) != true) return;
    ref.read(currentStudentProvider.notifier).select(s);
  }

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final l10n = AppLocalizations.of(context);
    return Column(
      children: [
        const SizedBox(height: 8),
        Text(
          l10n.whoIsLearning,
          style: Theme.of(context).textTheme.headlineSmall,
        ),
        const SizedBox(height: 24),
        Wrap(
          alignment: WrapAlignment.center,
          spacing: 24,
          runSpacing: 24,
          children: [
            for (final s in students)
              InkWell(
                key: Key('student-${s.id}'),
                borderRadius: BorderRadius.circular(16),
                onTap: () => _pick(context, ref, s),
                child: Padding(
                  padding: const EdgeInsets.all(8),
                  child: Column(
                    children: [
                      StudentAvatar(avatar: s.avatar, size: 88),
                      const SizedBox(height: 8),
                      Text(
                        s.firstName,
                        style: Theme.of(context).textTheme.titleMedium,
                      ),
                      if (s.pinHash != null)
                        const Icon(Icons.lock_outline, size: 16),
                    ],
                  ),
                ),
              ),
          ],
        ),
        const SizedBox(height: 24),
        OutlinedButton.icon(
          key: const Key('add-learner'),
          icon: const Icon(Icons.person_add),
          label: Text(l10n.addLearner),
          onPressed: () => context.push('/learners/new'),
        ),
      ],
    );
  }
}

/// The current child's greeting, then the home for their age group.
class _StudentHome extends ConsumerWidget {
  const _StudentHome({required this.student});

  final Student student;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final l10n = AppLocalizations.of(context);
    final tier = ref.watch(ageTierProvider);
    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        Row(
          children: [
            StudentAvatar(avatar: student.avatar, size: 48),
            const SizedBox(width: 12),
            Expanded(
              child: Text(
                l10n.helloName(student.firstName),
                style: Theme.of(context).textTheme.headlineSmall,
              ),
            ),
            Flexible(
              child: TextButton(
                key: const Key('switch-learner'),
                onPressed: () =>
                    ref.read(currentStudentProvider.notifier).clear(),
                child: Text(
                  l10n.switchLearner,
                  overflow: TextOverflow.ellipsis,
                ),
              ),
            ),
          ],
        ),
        const SizedBox(height: 16),
        switch (tier) {
          AgeTier.early => EarlyHome(student: student),
          AgeTier.primary => PrimaryHome(student: student),
          AgeTier.middle => MiddleHome(student: student),
          AgeTier.older => OlderHome(student: student),
        },
      ],
    );
  }
}
