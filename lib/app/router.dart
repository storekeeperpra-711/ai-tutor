import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../features/debug/urdu_test_screen.dart';
import '../features/home/home_screen.dart';
import '../features/settings/settings_screen.dart';

/// All screens and their paths. Add new screens here.
final routerProvider = Provider<GoRouter>(
  (ref) => GoRouter(
    routes: [
      GoRoute(path: '/', builder: (context, state) => const HomeScreen()),
      GoRoute(
        path: '/settings',
        builder: (context, state) => const SettingsScreen(),
      ),
      GoRoute(
        path: '/debug/urdu',
        builder: (context, state) => const UrduTestScreen(),
      ),
    ],
  ),
);
