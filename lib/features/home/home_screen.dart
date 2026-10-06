import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../../app/motion_widgets.dart';
import '../../app/theme/age_tier.dart';
import '../../l10n/app_localizations.dart';
import '../../services/local_db.dart';
import '../../services/profiles.dart';
import '../common/sync_status.dart';
import '../profiles/avatar.dart';
import '../profiles/pin_pad.dart';
import 'early_home.dart';
import 'home_style.dart';
import 'main_tabs.dart';
import 'tier_homes.dart';

/// Home: "Who is learning?" until a child picks their picture, then the
/// home for that child's age group (spec C4).
class HomeScreen extends ConsumerStatefulWidget {
  const HomeScreen({super.key});

  @override
  ConsumerState<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends ConsumerState<HomeScreen> {
  var _tab = HomeTab.home;

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final students = ref.watch(studentsProvider);
    final current = ref.watch(currentStudentProvider);
    // A new child starts on Home.
    ref.listen(currentStudentProvider, (_, _) => _tab = HomeTab.home);
    // The little ones keep their one big Play button and no menu.
    final showBar =
        current != null &&
        students.hasValue &&
        ref.watch(ageTierProvider) != AgeTier.early;
    final tab = showBar ? _tab : HomeTab.home;

    return TintedBackground(
      dots: true,
      child: Scaffold(
        backgroundColor: Colors.transparent,
        appBar: AppBar(
          backgroundColor: Colors.transparent,
          surfaceTintColor: Colors.transparent,
          // The child's own greeting replaces the app name once they pick.
          title: current == null ? Text(l10n.appTitle) : null,
          actions: [
            HeaderButton(
              key: const Key('open-account'),
              icon: Icons.family_restroom,
              tooltip: l10n.accountTitle,
              onPressed: () => context.push('/account'),
            ),
            // Settings is in the bottom menu once it shows.
            if (!showBar) ...[
              const SizedBox(width: 8),
              HeaderButton(
                icon: Icons.settings,
                tooltip: l10n.settingsTitle,
                onPressed: () => context.push('/settings'),
              ),
            ],
            const SizedBox(width: 16),
          ],
        ),
        bottomNavigationBar: showBar
            ? HomeBottomBar(
                tab: tab,
                onTab: (t) => setState(() => _tab = t),
                onSettings: () => context.push('/settings'),
              )
            : null,
        body: ListView(
          padding: const EdgeInsets.fromLTRB(20, 4, 20, 24),
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
              AsyncData() => [
                switch (tab) {
                  HomeTab.home => _StudentHome(student: current!),
                  HomeTab.lessons => LessonsTab(student: current!),
                  HomeTab.badges => BadgesTab(student: current!),
                },
              ],
              AsyncError(:final error) => [Text('$error')],
              _ => [const Center(child: CircularProgressIndicator())],
            },
            if (kDebugMode && tab == HomeTab.home) ...[
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
              Pressable(
                child: Card(
                  margin: EdgeInsets.zero,
                  child: InkWell(
                    key: Key('student-${s.id}'),
                    borderRadius: BorderRadius.circular(24),
                    onTap: () => _pick(context, ref, s),
                    child: Padding(
                      padding: const EdgeInsets.all(16),
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
    final tier = ref.watch(ageTierProvider);
    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        EnterAnimation(child: HomeHeader(student: student)),
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
