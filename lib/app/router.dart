import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../features/account/account_screen.dart';
import '../features/classes/teacher_classes_screen.dart';
import '../features/ai/ai_costs_screen.dart';
import '../features/ai/mithu_notes.dart';
import '../features/debug/narration_recorder_screen.dart';
import '../features/debug/urdu_test_screen.dart';
import '../features/home/home_screen.dart';
import '../features/debug/sim_gallery_screen.dart';
import '../features/plan/flashcards_screen.dart';
import '../features/plan/practice_screen.dart';
import '../features/previewer/lesson_list_screen.dart';
import '../features/profiles/add_student_screen.dart';
import '../features/report/parent_report_screen.dart';
import '../features/downloads/downloads_screen.dart';
import '../features/phone_check/phone_check_screen.dart';
import '../features/privacy/privacy_note_screen.dart';
import '../features/settings/settings_screen.dart';
import '../features/review/review_screens.dart';
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
        path: '/practice',
        builder: (context, state) => const PracticeScreen(),
      ),
      GoRoute(
        path: '/flashcards/:lessonId',
        builder: (context, state) =>
            FlashcardsScreen(lessonId: state.pathParameters['lessonId']!),
      ),
      GoRoute(
        path: '/notes',
        builder: (context, state) => const MithuNotesScreen(),
      ),
      GoRoute(
        path: '/ai-costs',
        builder: (context, state) => const AiCostsScreen(),
      ),
      GoRoute(
        path: '/account',
        builder: (context, state) => const AccountScreen(),
      ),
      GoRoute(
        path: '/report/:studentId',
        builder: (context, state) =>
            ParentReportScreen(studentId: state.pathParameters['studentId']!),
      ),
      GoRoute(
        path: '/classes',
        builder: (context, state) => const TeacherClassesScreen(),
      ),
      GoRoute(
        path: '/classes/:id',
        builder: (context, state) =>
            ClassDetailScreen(classId: state.pathParameters['id']!),
      ),
      GoRoute(
        path: '/lesson/:id',
        builder: (context, state) =>
            LessonPlayerScreen(lessonId: state.pathParameters['id']!),
      ),
      GoRoute(
        path: '/review',
        builder: (context, state) => const ReviewListScreen(),
      ),
      GoRoute(
        path: '/review/:id',
        builder: (context, state) =>
            ReviewLessonScreen(lessonId: state.pathParameters['id']!),
      ),
      GoRoute(
        path: '/review/:id/play',
        builder: (context, state) =>
            ReviewPlayerScreen(lessonId: state.pathParameters['id']!),
      ),
      GoRoute(
        path: '/downloads',
        builder: (context, state) => const DownloadsScreen(),
      ),
      GoRoute(
        path: '/privacy',
        builder: (context, state) => const PrivacyNoteScreen(),
      ),
      GoRoute(
        path: '/phone-check',
        builder: (context, state) => const PhoneCheckScreen(),
      ),
      GoRoute(
        path: '/dev/sims',
        builder: (context, state) => const SimGalleryScreen(),
      ),
      GoRoute(
        path: '/dev/lessons',
        builder: (context, state) => const LessonListScreen(),
      ),
      GoRoute(
        path: '/dev/voice',
        builder: (context, state) => const NarrationRecorderScreen(),
      ),
      GoRoute(
        path: '/debug/urdu',
        builder: (context, state) => const UrduTestScreen(),
      ),
    ],
  ),
);
