import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../app/locale_controller.dart';
import '../app/theme/age_tier.dart';
import '../app/theme/app_theme.dart';
import '../features/classes/teacher_classes_screen.dart';
import '../features/common/language_toggle.dart';
import '../l10n/app_localizations.dart';
import '../services/auth_service.dart';
import '../services/remote_store.dart';
import 'class_dashboard_screen.dart';

/// The teacher website's screens.
final dashboardRouterProvider = Provider<GoRouter>(
  (ref) => GoRouter(
    initialLocation: '/',
    routes: [
      GoRoute(path: '/', builder: (context, state) => const DashboardHome()),
      GoRoute(
        path: '/classes/:id',
        builder: (context, state) =>
            ClassDashboardScreen(classId: state.pathParameters['id']!),
      ),
    ],
  ),
);

/// The teacher dashboard (Phase 9, task 9.2): a website on Firebase
/// Hosting that reads the same Firestore as the app. No server, no AI.
class DashboardApp extends ConsumerWidget {
  const DashboardApp({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final locale = ref.watch(localeProvider);
    return MaterialApp.router(
      onGenerateTitle: (context) => AppLocalizations.of(context).dashboardTitle,
      routerConfig: ref.watch(dashboardRouterProvider),
      theme: buildTheme(AgeTier.older, locale),
      locale: locale,
      supportedLocales: supportedLocales,
      debugShowCheckedModeBanner: false,
      localizationsDelegates: const [
        AppLocalizations.delegate,
        GlobalMaterialLocalizations.delegate,
        GlobalWidgetsLocalizations.delegate,
        GlobalCupertinoLocalizations.delegate,
      ],
    );
  }
}

/// Signed out: sign in. Signed in: the teacher's classes.
class DashboardHome extends ConsumerWidget {
  const DashboardHome({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final l10n = AppLocalizations.of(context);
    final user = ref.watch(authUserProvider).value;
    if (user == null || !user.isAdult) return const DashboardSignIn();
    return TeacherClassesScreen(
      title: l10n.dashboardTitle,
      actions: [
        const LanguageToggle(),
        IconButton(
          key: const Key('dashboard-sign-out'),
          icon: const Icon(Icons.logout),
          tooltip: l10n.signOut,
          onPressed: () => ref.read(authServiceProvider).signOut(),
        ),
      ],
    );
  }
}

class DashboardSignIn extends ConsumerStatefulWidget {
  const DashboardSignIn({super.key});

  @override
  ConsumerState<DashboardSignIn> createState() => _DashboardSignInState();
}

class _DashboardSignInState extends ConsumerState<DashboardSignIn> {
  final _email = TextEditingController();
  final _password = TextEditingController();
  var _busy = false;
  AuthProblem? _problem;

  @override
  void dispose() {
    _email.dispose();
    _password.dispose();
    super.dispose();
  }

  Future<void> _run({required bool create}) async {
    setState(() {
      _busy = true;
      _problem = null;
    });
    final auth = ref.read(authServiceProvider);
    try {
      final email = _email.text.trim();
      if (create) {
        final user = await auth.signUp(email, _password.text);
        await ref
            .read(remoteStoreProvider)
            .setRole(user.uid, AccountRole.teacher);
      } else {
        await auth.signIn(email, _password.text);
      }
      ref.invalidate(teacherClassesProvider);
    } on AuthException catch (e) {
      _problem = e.problem;
    } catch (_) {
      _problem = AuthProblem.other;
    }
    if (mounted) setState(() => _busy = false);
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    return Scaffold(
      appBar: AppBar(
        title: Text(l10n.dashboardTitle),
        actions: const [LanguageToggle()],
      ),
      body: Center(
        child: ConstrainedBox(
          constraints: const BoxConstraints(maxWidth: 420),
          child: ListView(
            shrinkWrap: true,
            padding: const EdgeInsets.all(24),
            children: [
              Text(l10n.dashboardSignIn),
              const SizedBox(height: 16),
              TextField(
                key: const Key('email'),
                controller: _email,
                keyboardType: TextInputType.emailAddress,
                autocorrect: false,
                textDirection: TextDirection.ltr,
                decoration: InputDecoration(labelText: l10n.emailLabel),
              ),
              TextField(
                key: const Key('password'),
                controller: _password,
                obscureText: true,
                textDirection: TextDirection.ltr,
                decoration: InputDecoration(labelText: l10n.passwordLabel),
                onSubmitted: (_) => _run(create: false),
              ),
              const SizedBox(height: 16),
              if (_problem != null)
                Padding(
                  padding: const EdgeInsets.only(bottom: 8),
                  child: Text(
                    switch (_problem!) {
                      AuthProblem.wrongPassword => l10n.authWrongPassword,
                      AuthProblem.emailInUse => l10n.authEmailInUse,
                      AuthProblem.weakPassword => l10n.authWeakPassword,
                      AuthProblem.invalidEmail => l10n.authInvalidEmail,
                      AuthProblem.noConnection => l10n.authNoConnection,
                      AuthProblem.other => l10n.authOther,
                    },
                    key: const Key('auth-problem'),
                    style: TextStyle(
                      color: Theme.of(context).colorScheme.error,
                    ),
                  ),
                ),
              FilledButton(
                key: const Key('sign-in'),
                onPressed: _busy ? null : () => _run(create: false),
                child: Text(l10n.signIn),
              ),
              const SizedBox(height: 8),
              OutlinedButton(
                key: const Key('create-account'),
                onPressed: _busy ? null : () => _run(create: true),
                child: Text(l10n.createTeacherAccount),
              ),
              if (_busy)
                const Padding(
                  padding: EdgeInsets.all(16),
                  child: Center(child: CircularProgressIndicator()),
                ),
            ],
          ),
        ),
      ),
    );
  }
}
