import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../classes/class_store.dart';
import '../features/classes/teacher_classes_screen.dart';
import '../features/plan/mastery_level.dart';
import '../features/profiles/grade_names.dart';
import '../l10n/app_localizations.dart';
import '../mastery/curriculum.dart';
import '../mastery/skill_state.dart';
import '../services/mastery_service.dart';
import 'dashboard_data.dart';

/// Colours for the mastery grid, from not started (grey) to secure (dark
/// green). Each cell also has the level's first letter, so it reads
/// without colour too.
Color levelColor(MasteryLevel level) => switch (level) {
  MasteryLevel.notStarted => const Color(0xFFE0E0E0),
  MasteryLevel.learning => const Color(0xFFFFCC80),
  MasteryLevel.practising => const Color(0xFFFFF59D),
  MasteryLevel.mastered => const Color(0xFFA5D6A7),
  MasteryLevel.secure => const Color(0xFF2E7D32),
};

/// One class on the teacher website (Phase 9, task 9.2): the mastery grid,
/// recurring mistakes, stuck students, and assigned lessons.
class ClassDashboardScreen extends ConsumerWidget {
  const ClassDashboardScreen({super.key, required this.classId});

  final String classId;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final l10n = AppLocalizations.of(context);
    final schoolClass = ref
        .watch(teacherClassesProvider)
        .value
        ?.where((c) => c.id == classId)
        .firstOrNull;
    final members = ref.watch(classMembersProvider(classId));
    final curriculum = ref.watch(curriculumProvider).value;
    if (schoolClass == null) {
      return Scaffold(
        appBar: AppBar(),
        body: const Center(child: CircularProgressIndicator()),
      );
    }
    final list = members.value ?? const <ClassMember>[];

    return DefaultTabController(
      length: 4,
      child: Scaffold(
        appBar: AppBar(
          title: Text(schoolClass.name),
          actions: [
            Padding(
              padding: const EdgeInsetsDirectional.only(end: 8),
              child: Center(
                child: SelectableText(
                  l10n.classCode(schoolClass.code),
                  key: const Key('dashboard-code'),
                ),
              ),
            ),
            IconButton(
              key: const Key('dashboard-refresh'),
              icon: const Icon(Icons.refresh),
              tooltip: l10n.tryAgainButton,
              onPressed: () => ref
                ..invalidate(classMembersProvider(classId))
                ..invalidate(classLessonsProvider(classId)),
            ),
            IconButton(
              key: const Key('delete-class'),
              icon: const Icon(Icons.delete_outline),
              tooltip: l10n.deleteClass,
              onPressed: () => confirmDeleteClass(context, ref, schoolClass),
            ),
          ],
          bottom: TabBar(
            isScrollable: true,
            tabs: [
              Tab(key: const Key('tab-mastery'), text: l10n.tabMastery),
              Tab(key: const Key('tab-mistakes'), text: l10n.tabMistakes),
              Tab(key: const Key('tab-needs-help'), text: l10n.tabNeedsHelp),
              Tab(key: const Key('tab-lessons'), text: l10n.tabLessons),
            ],
          ),
        ),
        body: members.hasError
            ? ClassesRetry(
                onRetry: () => ref.invalidate(classMembersProvider(classId)),
              )
            : members.isLoading
            ? const Center(child: CircularProgressIndicator())
            : TabBarView(
                children: [
                  _MasteryGrid(members: list, curriculum: curriculum),
                  _Mistakes(members: list, curriculum: curriculum),
                  _NeedsHelp(members: list, curriculum: curriculum),
                  _Lessons(
                    classId: classId,
                    members: list,
                    curriculum: curriculum,
                  ),
                ],
              ),
      ),
    );
  }
}

String _skillTitle(BuildContext context, Curriculum? c, String skill) =>
    c?.titleOf(skill)?.of(context) ?? skill;

class _Empty extends StatelessWidget {
  const _Empty(this.text);

  final String text;

  @override
  Widget build(BuildContext context) =>
      Padding(padding: const EdgeInsets.all(24), child: Text(text));
}

/// Students down, skills across, coloured by mastery level.
class _MasteryGrid extends StatelessWidget {
  const _MasteryGrid({required this.members, required this.curriculum});

  final List<ClassMember> members;
  final Curriculum? curriculum;

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    if (members.isEmpty) return _Empty(l10n.noMembersYet);
    final skills = classSkills(members, curriculum);
    const cell = 36.0;
    final textTheme = Theme.of(context).textTheme;

    return ListView(
      padding: const EdgeInsets.all(16),
      children: [
        Wrap(
          spacing: 12,
          runSpacing: 4,
          children: [
            for (final level in MasteryLevel.values)
              Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  _Cell(level: level, size: 16, letter: false),
                  const SizedBox(width: 4),
                  Text(levelName(l10n, level), style: textTheme.bodySmall),
                ],
              ),
          ],
        ),
        const SizedBox(height: 16),
        SingleChildScrollView(
          scrollDirection: Axis.horizontal,
          child: Table(
            defaultColumnWidth: const FixedColumnWidth(cell + 4),
            columnWidths: const {0: FixedColumnWidth(160)},
            defaultVerticalAlignment: TableCellVerticalAlignment.middle,
            children: [
              TableRow(
                children: [
                  const SizedBox.shrink(),
                  for (final (i, skill) in skills.indexed)
                    Tooltip(
                      message: _skillTitle(context, curriculum, skill),
                      child: SizedBox(
                        height: 40,
                        child: Center(
                          child: Text(
                            '${i + 1}',
                            key: Key('grid-skill-$skill'),
                            style: textTheme.labelMedium,
                          ),
                        ),
                      ),
                    ),
                ],
              ),
              for (final m in members)
                TableRow(
                  children: [
                    Text(
                      '${m.firstName} · ${gradeName(l10n, m.grade)}',
                      overflow: TextOverflow.ellipsis,
                    ),
                    for (final skill in skills)
                      Padding(
                        padding: const EdgeInsets.all(2),
                        child: Tooltip(
                          message:
                              '${m.firstName}: '
                              '${_skillTitle(context, curriculum, skill)}: '
                              '${levelName(l10n, memberLevel(m, skill))}',
                          child: _Cell(
                            key: Key('grid-${m.docId}-$skill'),
                            level: memberLevel(m, skill),
                            size: cell,
                            needsHelp: m.skills.any(
                              (s) => s.skill == skill && s.needsHelp,
                            ),
                          ),
                        ),
                      ),
                  ],
                ),
            ],
          ),
        ),
        const SizedBox(height: 16),
        for (final (i, skill) in skills.indexed)
          Text(
            '${i + 1}. ${_skillTitle(context, curriculum, skill)}',
            style: textTheme.bodySmall,
          ),
      ],
    );
  }
}

class _Cell extends StatelessWidget {
  const _Cell({
    super.key,
    required this.level,
    required this.size,
    this.letter = true,
    this.needsHelp = false,
  });

  final MasteryLevel level;
  final double size;
  final bool letter;
  final bool needsHelp;

  @override
  Widget build(BuildContext context) {
    final name = levelName(AppLocalizations.of(context), level);
    return Container(
      width: size,
      height: size,
      decoration: BoxDecoration(
        color: levelColor(level),
        borderRadius: BorderRadius.circular(4),
        border: needsHelp
            ? Border.all(color: Theme.of(context).colorScheme.error, width: 3)
            : null,
      ),
      alignment: Alignment.center,
      child: letter && level != MasteryLevel.notStarted
          ? Text(
              name.characters.first,
              style: TextStyle(
                fontWeight: FontWeight.bold,
                color: level == MasteryLevel.secure
                    ? Colors.white
                    : Colors.black87,
              ),
            )
          : null,
    );
  }
}

class _Mistakes extends StatelessWidget {
  const _Mistakes({required this.members, required this.curriculum});

  final List<ClassMember> members;
  final Curriculum? curriculum;

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final mistakes = classMistakes(members);
    if (mistakes.isEmpty) return _Empty(l10n.noMistakesYet);
    return ListView(
      padding: const EdgeInsets.all(16),
      children: [
        for (final x in mistakes)
          Card(
            key: Key('dashboard-mistake-${x.lessonId}-${x.id}'),
            child: ListTile(
              leading: CircleAvatar(child: Text('${x.students.length}')),
              title: Text(describeMistake(curriculum, x.lessonId, x.id)),
              subtitle: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    l10n.mistakeIn(
                      curriculum?.lesson(x.lessonId)?.title.of(context) ??
                          x.lessonId,
                    ),
                  ),
                  Text(
                    l10n.mistakeStudents(
                      [for (final s in x.students) '${s.name} (${s.count})']
                          .join(', '),
                    ),
                  ),
                ],
              ),
            ),
          ),
      ],
    );
  }
}

class _NeedsHelp extends StatelessWidget {
  const _NeedsHelp({required this.members, required this.curriculum});

  final List<ClassMember> members;
  final Curriculum? curriculum;

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final stuck = stuckStudents(members);
    if (stuck.isEmpty) return _Empty(l10n.nobodyStuck);
    return ListView(
      padding: const EdgeInsets.all(16),
      children: [
        for (final s in stuck)
          ListTile(
            key: Key('stuck-${s.name}-${s.skill}'),
            leading: Icon(
              Icons.front_hand_outlined,
              color: Theme.of(context).colorScheme.error,
            ),
            title: Text(
              '${s.name}: ${_skillTitle(context, curriculum, s.skill)}',
            ),
            subtitle: s.lastDay == null
                ? null
                : Text(l10n.lastTried(s.lastDay!)),
          ),
      ],
    );
  }
}

class _Lessons extends ConsumerWidget {
  const _Lessons({
    required this.classId,
    required this.members,
    required this.curriculum,
  });

  final String classId;
  final List<ClassMember> members;
  final Curriculum? curriculum;

  Future<void> _assign(BuildContext context, WidgetRef ref) async {
    final picked = await showDialog<(String, DateTime?)>(
      context: context,
      builder: (context) => const AssignLessonDialog(),
    );
    if (picked == null) return;
    try {
      await ref
          .read(classStoreProvider)
          .assign(classId, lessonId: picked.$1, due: picked.$2);
      ref.invalidate(classLessonsProvider(classId));
    } catch (_) {
      if (context.mounted) showClassProblem(context);
    }
  }

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final l10n = AppLocalizations.of(context);
    final lessons = ref.watch(classLessonsProvider(classId));
    final dates = MaterialLocalizations.of(context);
    return ListView(
      padding: const EdgeInsets.all(16),
      children: [
        Align(
          alignment: AlignmentDirectional.centerStart,
          child: FilledButton.icon(
            key: const Key('dashboard-assign'),
            icon: const Icon(Icons.add),
            label: Text(l10n.assignLesson),
            onPressed: () => _assign(context, ref),
          ),
        ),
        const SizedBox(height: 8),
        switch (lessons) {
          AsyncData(:final value) when value.isEmpty => _Empty(
            l10n.noAssignments,
          ),
          AsyncData(:final value) => Column(
            children: [
              for (final a in value)
                _AssignmentCard(
                  classId: classId,
                  assignment: a,
                  members: members,
                  title:
                      curriculum?.lesson(a.lessonId)?.title.of(context) ??
                      a.lessonId,
                  due: a.due == null ? null : dates.formatShortDate(a.due!),
                ),
            ],
          ),
          AsyncError() => ClassesRetry(
            onRetry: () => ref.invalidate(classLessonsProvider(classId)),
          ),
          _ => const Center(child: CircularProgressIndicator()),
        },
      ],
    );
  }
}

class _AssignmentCard extends ConsumerWidget {
  const _AssignmentCard({
    required this.classId,
    required this.assignment,
    required this.members,
    required this.title,
    required this.due,
  });

  final String classId;
  final Assignment assignment;
  final List<ClassMember> members;
  final String title;
  final String? due;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final l10n = AppLocalizations.of(context);
    bool finished(ClassMember m) =>
        m.lessons.any((l) => l.lessonId == assignment.lessonId && l.completed);
    final done = [for (final m in members.where(finished)) m.firstName];
    final notYet = [
      for (final m in members.where((m) => !finished(m))) m.firstName,
    ];
    return Card(
      key: Key('dashboard-assignment-${assignment.lessonId}'),
      child: ListTile(
        leading: const Icon(Icons.menu_book_outlined),
        title: Text(title),
        subtitle: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              [
                if (due != null) l10n.planDue(due!),
                l10n.assignmentDone(done.length, members.length),
              ].join(' · '),
            ),
            if (done.isNotEmpty) Text(l10n.finishedBy(done.join(', '))),
            if (notYet.isNotEmpty) Text(l10n.notFinishedBy(notYet.join(', '))),
          ],
        ),
        trailing: IconButton(
          key: Key('dashboard-unassign-${assignment.lessonId}'),
          icon: const Icon(Icons.close),
          tooltip: l10n.removeButton,
          onPressed: () async {
            try {
              await ref
                  .read(classStoreProvider)
                  .unassign(classId, assignment.id);
              ref.invalidate(classLessonsProvider(classId));
            } catch (_) {
              if (context.mounted) showClassProblem(context);
            }
          },
        ),
      ),
    );
  }
}
