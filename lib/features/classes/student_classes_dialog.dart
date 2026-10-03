import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../classes/class_service.dart';
import '../../classes/class_store.dart';
import '../../l10n/app_localizations.dart';
import '../../services/local_db.dart';

/// For parents: the classes a child is in, and joining one with the
/// teacher's code after agreeing to share (Phase 9).
Future<void> showStudentClasses(BuildContext context, Student student) =>
    showDialog<void>(
      context: context,
      builder: (context) => StudentClassesDialog(student: student),
    );

class StudentClassesDialog extends ConsumerStatefulWidget {
  const StudentClassesDialog({super.key, required this.student});

  final Student student;

  @override
  ConsumerState<StudentClassesDialog> createState() =>
      _StudentClassesDialogState();
}

class _StudentClassesDialogState extends ConsumerState<StudentClassesDialog> {
  final _code = TextEditingController();
  ClassInfo? _found;
  ClassProblem? _problem;
  var _agreed = false;
  var _busy = false;

  @override
  void dispose() {
    _code.dispose();
    super.dispose();
  }

  Future<void> _run(Future<void> Function(ClassService) action) async {
    setState(() {
      _busy = true;
      _problem = null;
    });
    try {
      await action(ref.read(classServiceProvider));
    } on ClassException catch (e) {
      _problem = e.problem;
    }
    if (mounted) setState(() => _busy = false);
  }

  Future<void> _find() => _run((s) async {
    _found = null;
    _agreed = false;
    _found = await s.find(_code.text);
  });

  Future<void> _join() => _run((s) async {
    await s.join(widget.student, _found!);
    _found = null;
    _agreed = false;
    _code.clear();
  });

  Future<void> _leave(ClassMembership m) async {
    final l10n = AppLocalizations.of(context);
    final ok = await showDialog<bool>(
      context: context,
      builder: (context) => AlertDialog(
        content: Text(
          l10n.leaveClassConfirm(widget.student.firstName, m.className),
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context, false),
            child: Text(l10n.cancelButton),
          ),
          FilledButton(
            key: const Key('confirm-leave-class'),
            onPressed: () => Navigator.pop(context, true),
            child: Text(l10n.leaveClass),
          ),
        ],
      ),
    );
    if (ok == true) {
      await ref.read(classServiceProvider).leave(m.studentId, m.classId);
    }
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final name = widget.student.firstName;
    final memberships =
        ref.watch(membershipsProvider(widget.student.id)).value ?? const [];
    final found = _found;
    return AlertDialog(
      title: Text(l10n.classesTitle(name)),
      content: SingleChildScrollView(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            if (memberships.isEmpty) Text(l10n.classesNone),
            for (final m in memberships)
              ListTile(
                key: Key('class-${m.classId}'),
                contentPadding: EdgeInsets.zero,
                leading: const Icon(Icons.groups_outlined),
                title: Text(m.className),
                trailing: TextButton(
                  key: Key('leave-${m.classId}'),
                  onPressed: _busy ? null : () => _leave(m),
                  child: Text(l10n.leaveClass),
                ),
              ),
            const Divider(height: 24),
            TextField(
              key: const Key('class-code'),
              controller: _code,
              textCapitalization: TextCapitalization.characters,
              autocorrect: false,
              textDirection: TextDirection.ltr,
              decoration: InputDecoration(labelText: l10n.classCodeLabel),
              onSubmitted: (_) => _find(),
            ),
            const SizedBox(height: 8),
            OutlinedButton(
              key: const Key('find-class'),
              onPressed: _busy ? null : _find,
              child: Text(l10n.findClass),
            ),
            if (_problem != null)
              Padding(
                padding: const EdgeInsets.only(top: 8),
                child: Text(
                  switch (_problem!) {
                    ClassProblem.notFound => l10n.classNotFound,
                    ClassProblem.noConnection => l10n.classNoConnection,
                  },
                  key: const Key('class-problem'),
                  style: TextStyle(color: Theme.of(context).colorScheme.error),
                ),
              ),
            if (found != null) ...[
              const SizedBox(height: 16),
              Text(
                l10n.classFound(found.name),
                key: const Key('class-found'),
                style: Theme.of(context).textTheme.titleMedium,
              ),
              CheckboxListTile(
                key: const Key('class-consent'),
                contentPadding: EdgeInsets.zero,
                controlAffinity: ListTileControlAffinity.leading,
                value: _agreed,
                onChanged: (v) => setState(() => _agreed = v ?? false),
                title: Text(l10n.classConsent(name)),
              ),
              FilledButton(
                key: const Key('join-class'),
                onPressed: _busy || !_agreed ? null : _join,
                child: Text(l10n.joinClass),
              ),
            ],
            if (_busy)
              const Padding(
                padding: EdgeInsets.all(8),
                child: Center(child: CircularProgressIndicator()),
              ),
          ],
        ),
      ),
      actions: [
        TextButton(
          key: const Key('close-classes'),
          onPressed: () => Navigator.pop(context),
          child: Text(MaterialLocalizations.of(context).closeButtonLabel),
        ),
      ],
    );
  }
}
