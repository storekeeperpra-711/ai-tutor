import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../features/account/account_screen.dart';
import '../features/debug/urdu_test_screen.dart';
import '../features/home/home_screen.dart';
import '../features/previewer/lesson_list_screen.dart';
import '../features/profiles/add_student_screen.dart';
import '../features/settings/settings_screen.dart';
import '../lessons/lesson_player_screen.dart';

/// All screens and their paths. Add new screens here.
final routerProvider = Provider<GoRouter>(
  (ref) => GoRouter(
    initialLocation: '/',
    routes: [
      GoRoute(path: '/', builder: (context, state) => const HomeScreen()),
      GoRoute(
        path: '/settings',
        builder: (context, state) => const SettingsScreen(),
      ),
      GoRoute(
        path: '/learners/new',
        builder: (context, state) => const AddStudentScreen(),
      ),
      GoRoute(
        path: '/account',
        builder: (context, state) => const AccountScreen(),
      ),
      GoRoute(
        path: '/lesson/:id',
        builder: (context, state) =>
            LessonPlayerScreen(lessonId: state.pathParameters['id']!),
      ),
      GoRoute(
        path: '/dev/lessons',
        builder: (context, state) => const LessonListScreen(),
      ),
      GoRoute(
        path: '/debug/urdu',
        builder: (context, state) => const UrduTestScreen(),
      ),
    ],
  ),
);
