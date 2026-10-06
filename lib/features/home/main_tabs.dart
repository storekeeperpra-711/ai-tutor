import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../app/motion_widgets.dart';
import '../../app/theme/app_theme.dart';
import '../../l10n/app_localizations.dart';
import '../../services/local_db.dart';
import '../effort/badge_shelf.dart';
import 'home_parts.dart';
import 'home_style.dart';

/// The pages of the bottom menu. Settings is not a page here: it opens the
/// Settings screen, as the gear button did.
enum HomeTab { home, lessons, badges }

/// The bottom menu from the approved mock-ups: Home, Lessons, Badges and
/// Settings, on a white bar.
class HomeBottomBar extends StatelessWidget {
  const HomeBottomBar({
    super.key,
    required this.tab,
    required this.onTab,
    required this.onSettings,
  });

  final HomeTab tab;
  final ValueChanged<HomeTab> onTab;
  final VoidCallback onSettings;

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    return NavigationBar(
      key: const Key('bottom-bar'),
      backgroundColor: Colors.white,
      surfaceTintColor: Colors.transparent,
      indicatorColor: AppColors.lilacSoft,
      shadowColor: const Color(0x225B4BDB),
      elevation: 3,
      selectedIndex: tab.index,
      onDestinationSelected: (i) =>
          i < HomeTab.values.length ? onTab(HomeTab.values[i]) : onSettings(),
      destinations: [
        NavigationDestination(
          key: const Key('nav-home'),
          icon: const Icon(Icons.home_outlined),
          selectedIcon: const Icon(Icons.home_rounded, color: AppColors.lilac),
          label: l10n.navHome,
        ),
        NavigationDestination(
          key: const Key('nav-lessons'),
          icon: const Icon(Icons.auto_stories_outlined),
          selectedIcon: const Icon(
            Icons.auto_stories_rounded,
            color: AppColors.lilac,
          ),
          label: l10n.navLessons,
        ),
        NavigationDestination(
          key: const Key('nav-badges'),
          icon: const Icon(Icons.emoji_events_outlined),
          selectedIcon: const Icon(
            Icons.emoji_events_rounded,
            color: AppColors.lilac,
          ),
          label: l10n.navBadges,
        ),
        NavigationDestination(
          key: const Key('nav-settings'),
          icon: const Icon(Icons.settings),
          label: l10n.settingsTitle,
        ),
      ],
    );
  }
}

/// Every lesson, with the subject buttons.
class LessonsTab extends ConsumerWidget {
  const LessonsTab({super.key, required this.student});

  final Student student;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final lessons = ref.watch(visibleLessonsProvider);
    return Column(
      key: const Key('lessons-tab'),
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        EnterAnimation(child: HomeHeader(student: student)),
        const SizedBox(height: 16),
        LessonList(student: student, lessons: lessons),
      ],
    );
  }
}

/// All the child's effort badges, with what they are for.
class BadgesTab extends StatelessWidget {
  const BadgesTab({super.key, required this.student});

  final Student student;

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    return Column(
      key: const Key('badges-tab'),
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        EnterAnimation(child: HomeHeader(student: student)),
        const SizedBox(height: 16),
        EnterAnimation(
          index: 1,
          child: Container(
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(AppRadius.card),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                BadgeShelf(studentId: student.id),
                const SizedBox(height: 12),
                Text(
                  l10n.badgesIntro,
                  style: Theme.of(context).textTheme.bodyMedium
                      ?.copyWith(color: AppColors.muted),
                ),
              ],
            ),
          ),
        ),
      ],
    );
  }
}
