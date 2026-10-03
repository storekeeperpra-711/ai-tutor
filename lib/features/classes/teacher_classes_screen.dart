import 'dart:async';

import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../../classes/class_store.dart';
import '../../l10n/app_localizations.dart';
import '../../mastery/skill_state.dart';
import '../../models/lesson.dart';
import '../../services/auth_service.dart';
import '../../services/mastery_service.dart';
import '../profiles/grade_names.dart';

/// The signed-in teacher's classes.
final teacherClassesProvider = FutureProvider<List<SchoolClass>>((ref) async {
  final user = ref.watch(authUserProvider).value;
  if (user == null || !user.isAdult) return const [];
  return ref.watch(classStoreProvider).classesOf(user.uid);
});

final classMembersProvider = FutureProvider.family<List<ClassMember>, String>(
  (ref, classId) => ref.watch(classStoreProvider).members(classId),
);

final classLessonsProvider = FutureProvider.family<List<Assignment>, String>(
  (ref, classId) => ref.watch(classStoreProvider).assignments(classId),
);

/// For teachers: their classes, and making a new one (Phase 9).
class TeacherClassesScreen extends ConsumerWidget {
  const TeacherClassesScreen({super.key});

  Future<void> _create(BuildContext context, WidgetRef ref) async {
    final text = await showDialog<String>(
      context: context,
      builder: (context) => const _NewClassDialog(),
    );
    if (text == null || text.isEmpty) return;
    final uid = ref.read(authServiceProvider).currentUser?.uid;
    if (uid == null) return;
    try {
      final created = await ref.read(classStoreProvider).createClass(uid, text);
      ref.invalidate(teacherClassesProvider);
      if (context.mounted) unawaited(context.push('/classes/${created.id}'));
    } catch (_) {
      if (context.mounted) _showProblem(context);
    }
  }

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final l10n = AppLocalizations.of(context);
    final classes = ref.watch(teacherClassesProvider);
    return Scaffold(
      appBar: AppBar(title: Text(l10n.myClasses)),
      floatingActionButton: FloatingActionButton.extended(
        key: const Key('new-class'),
        icon: const Icon(Icons.add),
        label: Text(l10n.newClass),
        onPressed: () => _create(context, ref),
      ),
      body: switch (classes) {
        AsyncData(:final value) when value.isEmpty => Padding(
          padding: const EdgeInsets.all(24),
          child: Text(l10n.noClassesYet, key: const Key('no-classes')),
        ),
        AsyncData(:final value) => ListView(
          children: [
            for (final c in value)
              ListTile(
                key: Key('open-class-${c.id}'),
                leading: const Icon(Icons.groups_outlined),
                title: Text(c.name),
                subtitle: Text(l10n.classCode(c.code)),
                onTap: () => context.push('/classes/${c.id}'),
              ),
          ],
        ),
        AsyncError() => _Retry(
          onRetry: () => ref.invalidate(teacherClassesProvider),
        ),
        _ => const Center(child: CircularProgressIndicator()),
      },
    );
  }
}

/// One class: its code, students, common mistakes and assigned lessons.
class ClassDetailScreen extends ConsumerWidget {
  const ClassDetailScreen({super.key, required this.classId});

  final String classId;

  Future<void> _assign(BuildContext context, WidgetRef ref) async {
    final picked = await showDialog<(String, DateTime?)>(
      context: context,
      builder: (context) => const _AssignDialog(),
    );
    if (picked == null) return;
    try {
      await ref
          .read(classStoreProvider)
          .assign(classId, lessonId: picked.$1, due: picked.$2);
      ref.invalidate(classLessonsProvider(classId));
    } catch (_) {
      if (context.mounted) _showProblem(context);
    }
  }

  Future<void> _delete(
    BuildContext context,
    WidgetRef ref,
    SchoolClass schoolClass,
  ) async {
    final l10n = AppLocalizations.of(context);
    final ok = await showDialog<bool>(
      context: context,
      builder: (context) => AlertDialog(
        content: Text(l10n.deleteClassConfirm(schoolClass.name)),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context, false),
            child: Text(l10n.cancelButton),
          ),
          FilledButton(
            key: const Key('confirm-delete-class'),
            onPressed: () => Navigator.pop(context, true),
            child: Text(l10n.deleteClass),
          ),
        ],
      ),
    );
    if (ok != true) return;
    try {
      await ref.read(classStoreProvider).deleteClass(schoolClass);
      ref.invalidate(teacherClassesProvider);
      if (context.mounted) context.pop();
    } catch (_) {
      if (context.mounted) _showProblem(context);
    }
  }

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final l10n = AppLocalizations.of(context);
    final textTheme = Theme.of(context).textTheme;
    final schoolClass = ref
        .watch(teacherClassesProvider)
        .value
        ?.where((c) => c.id == classId)
        .firstOrNull;
    final members = ref.watch(classMembersProvider(classId));
    final lessons = ref.watch(classLessonsProvider(classId));
    final curriculum = ref.watch(curriculumProvider).value;

    if (schoolClass == null) {
      return Scaffold(
        appBar: AppBar(),
        body: const Center(child: CircularProgressIndicator()),
      );
    }

    String skillTitle(String skill) =>
        curriculum?.titleOf(skill)?.of(context) ?? skill;
    String lessonTitle(String id) =>
        curriculum?.lesson(id)?.title.of(context) ?? id;

    final list = members.value ?? const <ClassMember>[];
    return Scaffold(
      appBar: AppBar(
        title: Text(schoolClass.name),
        actions: [
          IconButton(
            key: const Key('delete-class'),
            icon: const Icon(Icons.delete_outline),
            tooltip: l10n.deleteClass,
            onPressed: () => _delete(context, ref, schoolClass),
          ),
        ],
      ),
      body: RefreshIndicator(
        onRefresh: () async {
          ref
            ..invalidate(classMembersProvider(classId))
            ..invalidate(classLessonsProvider(classId));
        },
        child: ListView(
          padding: const EdgeInsets.all(16),
          children: [
            SelectableText(
              l10n.classCode(schoolClass.code),
              key: const Key('class-code-text'),
              style: textTheme.headlineMedium,
            ),
            Text(l10n.classCodeHelp),
            const Divider(height: 32),
            Text(l10n.classMembers, style: textTheme.titleMedium),
            if (members.hasError)
              _Retry(
                onRetry: () => ref.invalidate(classMembersProvider(classId)),
              )
            else if (members.isLoading)
              const Center(child: CircularProgressIndicator())
            else if (list.isEmpty)
              Text(l10n.noMembersYet)
            else
              for (final m in list) _MemberTile(member: m, title: skillTitle),
            if (list.isNotEmpty)
              ..._commonMistakes(context, list, curriculum?.lesson),
            const Divider(height: 32),
            Text(l10n.classAssignments, style: textTheme.titleMedium),
            switch (lessons) {
              AsyncData(:final value) when value.isEmpty => Text(
                l10n.noAssignments,
              ),
              AsyncData(:final value) => Column(
                children: [
                  for (final a in value)
                    ListTile(
                      key: Key('assignment-${a.lessonId}'),
                      contentPadding: EdgeInsets.zero,
                      leading: const Icon(Icons.menu_book_outlined),
                      title: Text(lessonTitle(a.lessonId)),
                      subtitle: Text(
                        [
                          if (a.due != null)
                            l10n.planDue(
                              MaterialLocalizations.of(context)
                                  .formatShortDate(a.due!),
                            ),
                          l10n.assignmentDone(
                            list
                                .where(
                                  (m) => m.lessons.any(
                                    (l) =>
                                        l.lessonId == a.lessonId && l.completed,
                                  ),
                                )
                                .length,
                            list.length,
                          ),
                        ].join(' · '),
                      ),
                      trailing: IconButton(
                        key: Key('unassign-${a.lessonId}'),
                        icon: const Icon(Icons.close),
                        tooltip: l10n.removeButton,
                        onPressed: () async {
                          try {
                            await ref
                                .read(classStoreProvider)
                                .unassign(classId, a.id);
                            ref.invalidate(classLessonsProvider(classId));
                          } catch (_) {
                            if (context.mounted) _showProblem(context);
                          }
                        },
                      ),
                    ),
                ],
              ),
              AsyncError() => _Retry(
                onRetry: () => ref.invalidate(classLessonsProvider(classId)),
              ),
              _ => const Center(child: CircularProgressIndicator()),
            },
            const SizedBox(height: 8),
            OutlinedButton.icon(
              key: const Key('assign-lesson'),
              icon: const Icon(Icons.add),
              label: Text(l10n.assignLesson),
              onPressed: () => _assign(context, ref),
            ),
          ],
        ),
      ),
    );
  }

  /// The misconceptions most students in the class showed, in the
  /// lesson's own words for teachers.
  List<Widget> _commonMistakes(
    BuildContext context,
    List<ClassMember> members,
    Lesson? Function(String id)? lessonOf,
  ) {
    final l10n = AppLocalizations.of(context);
    final who = <(String, String), List<String>>{};
    for (final m in members) {
      for (final x in m.misconceptions) {
        (who[(x.lessonId, x.id)] ??= []).add(m.firstName);
      }
    }
    if (who.isEmpty) return const [];
    final top = who.entries.toList()
      ..sort((a, b) => b.value.length.compareTo(a.value.length));
    String describe(String lessonId, String id) {
      final lesson = lessonOf?.call(lessonId);
      for (final x in lesson?.misconceptions ?? const <Misconception>[]) {
        if (x.id == id) return x.description;
      }
      return id;
    }

    return [
      const SizedBox(height: 16),
      Text(l10n.commonMistakes, style: Theme.of(context).textTheme.titleMedium),
      for (final MapEntry(key: (lessonId, id), value: names) in top.take(5))
        ListTile(
          key: Key('mistake-$lessonId-$id'),
          contentPadding: EdgeInsets.zero,
          leading: const Icon(Icons.warning_amber_outlined),
          title: Text(describe(lessonId, id)),
          subtitle: Text(l10n.mistakeStudents(names.join(', '))),
        ),
    ];
  }
}

class _MemberTile extends StatelessWidget {
  const _MemberTile({required this.member, required this.title});

  final ClassMember member;
  final String Function(String skill) title;

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final mastered = member.skills
        .where(
          (s) =>
              s.level == MasteryLevel.mastered.name ||
              s.level == MasteryLevel.secure.name,
        )
        .length;
    final stuck = [
      for (final s in member.skills)
        if (s.needsHelp) title(s.skill),
    ];
    return ListTile(
      key: Key('member-${member.docId}'),
      contentPadding: EdgeInsets.zero,
      leading: const Icon(Icons.person_outline),
      title: Text(member.firstName),
      subtitle: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            '${gradeName(l10n, member.grade)} · '
            '${l10n.memberProgress(mastered, member.skills.length)}',
          ),
          if (stuck.isNotEmpty)
            Text(
              l10n.needsHelpWith(stuck.join(', ')),
              style: TextStyle(color: Theme.of(context).colorScheme.error),
            ),
        ],
      ),
    );
  }
}

/// Asks for the new class's name.
class _NewClassDialog extends StatefulWidget {
  const _NewClassDialog();

  @override
  State<_NewClassDialog> createState() => _NewClassDialogState();
}

class _NewClassDialogState extends State<_NewClassDialog> {
  final _name = TextEditingController();

  @override
  void dispose() {
    _name.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    return AlertDialog(
      title: Text(l10n.newClass),
      content: TextField(
        key: const Key('class-name'),
        controller: _name,
        maxLength: 60,
        autofocus: true,
        decoration: InputDecoration(labelText: l10n.classNameLabel),
      ),
      actions: [
        TextButton(
          onPressed: () => Navigator.pop(context),
          child: Text(l10n.cancelButton),
        ),
        FilledButton(
          key: const Key('create-class'),
          onPressed: () => Navigator.pop(context, _name.text.trim()),
          child: Text(l10n.createButton),
        ),
      ],
    );
  }
}

/// Picks a lesson and an optional due date.
class _AssignDialog extends ConsumerStatefulWidget {
  const _AssignDialog();

  @override
  ConsumerState<_AssignDialog> createState() => _AssignDialogState();
}

class _AssignDialogState extends ConsumerState<_AssignDialog> {
  String? _lesson;
  DateTime? _due;

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final lessons = ref.watch(curriculumProvider).value?.lessons ?? const [];
    final materialL10n = MaterialLocalizations.of(context);
    return AlertDialog(
      title: Text(l10n.assignLesson),
      content: Column(
        mainAxisSize: MainAxisSize.min,
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          DropdownButton<String>(
            key: const Key('assign-lesson-choice'),
            isExpanded: true,
            value: _lesson,
            hint: Text(l10n.assignLesson),
            items: [
              for (final lesson in lessons)
                DropdownMenuItem(
                  key: Key('assign-${lesson.id}'),
                  value: lesson.id,
                  child: Text(
                    '${gradeName(l10n, lesson.grade)}: '
                    '${lesson.title.of(context)}',
                    overflow: TextOverflow.ellipsis,
                  ),
                ),
            ],
            onChanged: (id) => setState(() => _lesson = id),
          ),
          const SizedBox(height: 8),
          TextButton.icon(
            key: const Key('assign-due'),
            icon: const Icon(Icons.event_outlined),
            label: Text(
              _due == null
                  ? l10n.setDueDate
                  : l10n.planDue(materialL10n.formatShortDate(_due!)),
            ),
            onPressed: () async {
              final now = DateTime.now();
              final picked = await showDatePicker(
                context: context,
                firstDate: dayOf(now),
                lastDate: now.add(const Duration(days: 365)),
                initialDate: _due ?? now.add(const Duration(days: 7)),
              );
              if (picked != null) setState(() => _due = picked);
            },
          ),
        ],
      ),
      actions: [
        TextButton(
          onPressed: () => Navigator.pop(context),
          child: Text(l10n.cancelButton),
        ),
        FilledButton(
          key: const Key('confirm-assign'),
          onPressed: _lesson == null
              ? null
              : () => Navigator.pop(context, (_lesson!, _due)),
          child: Text(l10n.assignLesson),
        ),
      ],
    );
  }
}

class _Retry extends StatelessWidget {
  const _Retry({required this.onRetry});

  final VoidCallback onRetry;

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    return Padding(
      padding: const EdgeInsets.all(16),
      child: Column(
        children: [
          Text(l10n.classNoConnection),
          TextButton(
            key: const Key('classes-retry'),
            onPressed: onRetry,
            child: Text(l10n.tryAgainButton),
          ),
        ],
      ),
    );
  }
}

void _showProblem(BuildContext context) => ScaffoldMessenger.of(context)
    .showSnackBar(
      SnackBar(content: Text(AppLocalizations.of(context).classNoConnection)),
    );
