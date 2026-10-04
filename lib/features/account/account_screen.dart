import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../classes/student_classes_dialog.dart';
import '../../app/preferences.dart';
import '../../l10n/app_localizations.dart';
import '../../services/account_actions.dart';
import '../../services/auth_service.dart';
import '../../services/local_db.dart';
import '../../services/mastery_service.dart';
import '../../services/profiles.dart';
import '../../services/remote_store.dart';
import '../../services/sync_service.dart';
import '../profiles/avatar.dart';
import '../profiles/grade_names.dart';

/// For parents and teachers: sign in or create an account (so learners'
/// work can come back on a new phone), and manage the learners.
class AccountScreen extends ConsumerStatefulWidget {
  const AccountScreen({super.key});

  @override
  ConsumerState<AccountScreen> createState() => _AccountScreenState();
}

class _AccountScreenState extends ConsumerState<AccountScreen> {
  final _email = TextEditingController();
  final _password = TextEditingController();
  var _role = AccountRole.parent;
  var _busy = false;
  AuthProblem? _problem;

  @override
  void dispose() {
    _email.dispose();
    _password.dispose();
    super.dispose();
  }

  Future<void> _run(Future<void> Function(AccountActions) action) async {
    setState(() {
      _busy = true;
      _problem = null;
    });
    try {
      await action(ref.read(accountActionsProvider));
    } on AuthException catch (e) {
      _problem = e.problem;
    } catch (_) {
      _problem = AuthProblem.other;
    }
    if (mounted) setState(() => _busy = false);
  }

  Future<void> _signOut() async {
    final l10n = AppLocalizations.of(context);
    final pending = ref.read(pendingSyncCountProvider).value ?? 0;
    final ok = await showDialog<bool>(
      context: context,
      builder: (context) => AlertDialog(
        content: Text(
          pending > 0 ? l10n.signOutUnsynced(pending) : l10n.signOutConfirm,
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context, false),
            child: Text(l10n.cancelButton),
          ),
          FilledButton(
            key: const Key('confirm-sign-out'),
            onPressed: () => Navigator.pop(context, true),
            child: Text(l10n.signOut),
          ),
        ],
      ),
    );
    if (ok == true) await _run((a) => a.signOut());
  }

  Future<void> _remove(Student student) async {
    final l10n = AppLocalizations.of(context);
    final ok = await showDialog<bool>(
      context: context,
      builder: (context) => AlertDialog(
        content: Text(l10n.removeLearnerConfirm(student.firstName)),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context, false),
            child: Text(l10n.cancelButton),
          ),
          FilledButton(
            key: const Key('confirm-remove'),
            onPressed: () => Navigator.pop(context, true),
            child: Text(l10n.removeButton),
          ),
        ],
      ),
    );
    if (ok == true) {
      await ref.read(accountActionsProvider).removeStudent(student);
    }
  }

  String _problemText(AppLocalizations l10n, AuthProblem problem) =>
      switch (problem) {
        AuthProblem.wrongPassword => l10n.authWrongPassword,
        AuthProblem.emailInUse => l10n.authEmailInUse,
        AuthProblem.weakPassword => l10n.authWeakPassword,
        AuthProblem.invalidEmail => l10n.authInvalidEmail,
        AuthProblem.noConnection => l10n.authNoConnection,
        AuthProblem.other => l10n.authOther,
      };

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final user = ref.watch(authUserProvider).value;
    final students = ref.watch(studentsProvider).value ?? const [];
    final role = ref.watch(sharedPreferencesProvider).getString(accountRoleKey);
    final textTheme = Theme.of(context).textTheme;

    return Scaffold(
      appBar: AppBar(title: Text(l10n.accountTitle)),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          if (user != null && user.isAdult) ...[
            Text(
              l10n.signedInAs(user.email!),
              key: const Key('signed-in-as'),
              style: textTheme.titleMedium,
            ),
            if (role == AccountRole.teacher.name) ...[
              const SizedBox(height: 8),
              FilledButton.icon(
                key: const Key('my-classes'),
                icon: const Icon(Icons.groups_outlined),
                label: Text(l10n.myClasses),
                onPressed: () => context.push('/classes'),
              ),
            ],
            const SizedBox(height: 16),
            OutlinedButton(
              key: const Key('sign-out'),
              onPressed: _busy ? null : _signOut,
              child: Text(l10n.signOut),
            ),
          ] else ...[
            Text(l10n.accountPhoneOnly),
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
            ),
            const SizedBox(height: 16),
            SegmentedButton<AccountRole>(
              segments: [
                ButtonSegment(
                  value: AccountRole.parent,
                  label: Text(l10n.roleParent),
                ),
                ButtonSegment(
                  value: AccountRole.teacher,
                  label: Text(l10n.roleTeacher),
                ),
              ],
              selected: {_role},
              onSelectionChanged: (s) => setState(() => _role = s.first),
            ),
            const SizedBox(height: 16),
            if (_problem != null)
              Padding(
                padding: const EdgeInsets.only(bottom: 8),
                child: Text(
                  _problemText(l10n, _problem!),
                  key: const Key('auth-problem'),
                  style: TextStyle(color: Theme.of(context).colorScheme.error),
                ),
              ),
            FilledButton(
              key: const Key('create-account'),
              onPressed: _busy
                  ? null
                  : () => _run(
                      (a) =>
                          a.signUp(_email.text.trim(), _password.text, _role),
                    ),
              child: Text(l10n.createAccount),
            ),
            const SizedBox(height: 8),
            OutlinedButton(
              key: const Key('sign-in'),
              onPressed: _busy
                  ? null
                  : () => _run(
                      (a) => a.signIn(_email.text.trim(), _password.text),
                    ),
              child: Text(l10n.signIn),
            ),
          ],
          if (_busy)
            const Padding(
              padding: EdgeInsets.all(16),
              child: Center(child: CircularProgressIndicator()),
            ),
          if (students.isNotEmpty) ...[
            const Divider(height: 48),
            Text(l10n.learnersTitle, style: textTheme.titleMedium),
            for (final s in students)
              ListTile(
                leading: StudentAvatar(avatar: s.avatar, size: 40),
                title: Text(s.firstName),
                subtitle: _LearnerSubtitle(student: s),
                trailing: Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    IconButton(
                      key: Key('classes-${s.id}'),
                      icon: const Icon(Icons.groups_outlined),
                      tooltip: l10n.classesButton,
                      onPressed: () => showStudentClasses(context, s),
                    ),
                    IconButton(
                      key: Key('report-${s.id}'),
                      icon: const Icon(Icons.summarize_outlined),
                      tooltip: l10n.reportButton,
                      onPressed: () => context.push('/report/${s.id}'),
                    ),
                    IconButton(
                      key: Key('remove-${s.id}'),
                      icon: const Icon(Icons.delete_outline),
                      tooltip: l10n.removeLearner,
                      onPressed: () => _remove(s),
                    ),
                  ],
                ),
              ),
          ],
        ],
      ),
    );
  }
}

/// Grade, and the topics a learner is stuck on (spec B3: tell an adult).
class _LearnerSubtitle extends ConsumerWidget {
  const _LearnerSubtitle({required this.student});

  final Student student;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final l10n = AppLocalizations.of(context);
    final states = ref.watch(skillStatesProvider(student.id)).value ?? {};
    final curriculum = ref.watch(curriculumProvider).value;
    final topics = [
      for (final s in states.values)
        if (s.needsHelp) curriculum?.titleOf(s.skill)?.of(context) ?? s.skill,
    ];
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(gradeName(l10n, student.grade)),
        if (topics.isNotEmpty)
          Text(
            l10n.needsHelpWith(topics.join(', ')),
            key: Key('needs-help-${student.id}'),
            style: TextStyle(color: Theme.of(context).colorScheme.error),
          ),
      ],
    );
  }
}
