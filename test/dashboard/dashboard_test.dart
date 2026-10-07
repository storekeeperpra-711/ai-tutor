import 'package:ai_tutor/app/preferences.dart';
import 'package:ai_tutor/classes/class_store.dart';
import 'package:ai_tutor/dashboard/dashboard_app.dart';
import 'package:ai_tutor/dashboard/dashboard_data.dart';
import 'package:ai_tutor/lessons/hidden_units.dart';
import 'package:ai_tutor/mastery/curriculum.dart';
import 'package:ai_tutor/mastery/skill_state.dart';
import 'package:ai_tutor/services/auth_service.dart';
import 'package:ai_tutor/services/mastery_service.dart';
import 'package:ai_tutor/services/remote_store.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:shared_preferences/shared_preferences.dart';

import '../fakes.dart';
import '../features/classes_test.dart' show waitFor;
import '../lessons/lesson_updates_test.dart' show lessonJson, newId;
import '../lessons/play_helpers.dart';
import '../mastery/lessons.dart' show loadLessons;

const fractionsLesson = 'g6-maths-02-dividing-fractions';
const teacherEmail = 'teacher@school.pk';

ClassMember member(
  String name, {
  List<MemberSkill> skills = const [],
  List<MemberMisconception> misconceptions = const [],
  List<MemberLesson> lessons = const [],
}) => ClassMember(
  uid: 'phone-$name',
  studentId: 's1',
  firstName: name,
  grade: 6,
  joinedAt: DateTime(2026, 10, 1),
  skills: skills,
  misconceptions: misconceptions,
  lessons: lessons,
);

MemberSkill skill(String id, MasteryLevel level, {bool needsHelp = false}) => (
  skill: id,
  level: level.name,
  needsHelp: needsHelp,
  lastDay: '2026-10-02',
  nextReview: null,
);

/// The website as main_dashboard.dart builds it, on the pretend Firebase.
Future<Widget> buildDashboard(FakeBackend backend) async {
  rootBundle.clear();
  SharedPreferences.setMockInitialValues({});
  final prefs = await SharedPreferences.getInstance();
  return ProviderScope(
    overrides: [
      // The test class did the Fractions lesson, which children don't see.
      hiddenUnitsProvider.overrideWithValue(const {}),
      sharedPreferencesProvider.overrideWithValue(prefs),
      authServiceProvider.overrideWithValue(backend.auth),
      remoteStoreProvider.overrideWithValue(backend.remote),
      classStoreProvider.overrideWithValue(backend.classes),
      curriculumProvider.overrideWith(
        (ref) => ref.watch(dashboardCurriculumProvider.future),
      ),
    ],
    child: const DashboardApp(),
  );
}

void main() {
  const fractions = 'maths.fractions.divide_by_fraction';
  const equations = 'maths.linear_equations.solve_two_step';

  group('class data', () {
    final curriculum = Curriculum(loadLessons());

    test('skills come in curriculum order, unknown ones last', () {
      final members = [
        member('Ali', skills: [skill('zz.unknown', MasteryLevel.learning)]),
        member(
          'Sara',
          skills: [
            skill(equations, MasteryLevel.mastered),
            skill(fractions, MasteryLevel.learning),
          ],
        ),
      ];
      final skills = classSkills(members, curriculum);
      expect(skills.last, 'zz.unknown');
      expect(skills.indexOf(fractions), lessThan(skills.indexOf(equations)));
      expect(memberLevel(members[1], equations), MasteryLevel.mastered);
      expect(memberLevel(members[0], equations), MasteryLevel.notStarted);
    });

    test('mistakes most students made come first, with counts', () {
      final mistakes = classMistakes([
        member(
          'Ali',
          misconceptions: [
            (lessonId: fractionsLesson, id: 'a', count: 5),
            (lessonId: fractionsLesson, id: 'b', count: 1),
          ],
        ),
        member(
          'Sara',
          misconceptions: [(lessonId: fractionsLesson, id: 'b', count: 2)],
        ),
      ]);
      expect([for (final m in mistakes) m.id], ['b', 'a']);
      expect(mistakes.first.students, [
        (name: 'Ali', count: 1),
        (name: 'Sara', count: 2),
      ]);
      expect(
        describeMistake(curriculum, fractionsLesson, 'division_makes_smaller'),
        'Believes dividing always gives a smaller answer.',
      );
      expect(describeMistake(curriculum, fractionsLesson, 'x'), 'x');
    });

    test('stuck students list the skill and the day last tried', () {
      final stuck = stuckStudents([
        member(
          'Sara',
          skills: [skill(fractions, MasteryLevel.learning, needsHelp: true)],
        ),
        member('Ali', skills: [skill(fractions, MasteryLevel.learning)]),
      ]);
      expect(stuck, [(name: 'Sara', skill: fractions, lastDay: '2026-10-02')]);
    });
  });

  group('website', () {
    setUp(() {
      final view =
          TestWidgetsFlutterBinding.instance.platformDispatcher.views.first;
      view.physicalSize = const Size(1600, 1000);
      view.devicePixelRatio = 1;
    });

    tearDown(() {
      TestWidgetsFlutterBinding.instance.platformDispatcher.views.first
        ..resetPhysicalSize()
        ..resetDevicePixelRatio();
    });

    testWidgets('a new teacher creates an account with the teacher role', (
      tester,
    ) async {
      final backend = FakeBackend();
      await tester.pumpWidget(await buildDashboard(backend));
      await tester.pumpAndSettle();

      await tester.enterText(find.byKey(const Key('email')), teacherEmail);
      await tester.enterText(find.byKey(const Key('password')), 'secret1');
      await tapKey(tester, 'sign-in');
      expect(find.byKey(const Key('auth-problem')), findsOneWidget);

      await tapKey(tester, 'create-account');
      final uid = backend.auth.currentUser!.uid;
      expect(backend.remote.docs['accounts/$uid']!['role'], 'teacher');
      await waitFor(tester, find.byKey(const Key('no-classes')));
      expect(find.byKey(const Key('no-classes')), findsOneWidget);

      await tapKey(tester, 'dashboard-sign-out');
      expect(find.byKey(const Key('sign-in')), findsOneWidget);
    });

    testWidgets(
      'a teacher sees the grid, mistakes, stuck students and lessons',
      (tester) async {
        final backend = FakeBackend();
        backend.auth.accounts[teacherEmail] = ('secret1', 'teacher1');
        backend.classes.addClass(name: '6 B Maths');
        backend.classes.membersOf['class1'] = {
          for (final m in [
            member(
              'Sara',
              skills: [skill(fractions, MasteryLevel.secure)],
              lessons: [
                (lessonId: fractionsLesson, completed: true, nextStep: 10),
              ],
            ),
            member(
              'Ali',
              skills: [
                skill(fractions, MasteryLevel.learning, needsHelp: true),
              ],
              misconceptions: [
                (
                  lessonId: fractionsLesson,
                  id: 'division_makes_smaller',
                  count: 3,
                ),
              ],
            ),
          ])
            m.docId: m,
        };
        await backend.classes.assignAs('class1', fractionsLesson);
        await tester.pumpWidget(await buildDashboard(backend));
        await tester.pumpAndSettle();

        await tester.enterText(find.byKey(const Key('email')), teacherEmail);
        await tester.enterText(find.byKey(const Key('password')), 'secret1');
        await tapKey(tester, 'sign-in');
        await tapKey(tester, 'open-class-class1');
        expect(find.text('Code: ABC234'), findsOneWidget);

        // Mastery grid: one cell per student and skill.
        await waitFor(tester, find.byKey(const Key('grid-skill-$fractions')));
        expect(
          find.byKey(const Key('grid-phone-Sara_s1-$fractions')),
          findsOneWidget,
        );
        expect(
          find.byKey(const Key('grid-phone-Ali_s1-$fractions')),
          findsOneWidget,
        );

        await tapKey(tester, 'tab-mistakes');
        expect(
          find.text('Believes dividing always gives a smaller answer.'),
          findsOneWidget,
        );
        expect(find.text('Made by: Ali (3)'), findsOneWidget);

        await tapKey(tester, 'tab-needs-help');
        expect(find.byKey(const Key('stuck-Ali-$fractions')), findsOneWidget);
        expect(find.text('Last tried 2026-10-02'), findsOneWidget);

        await tapKey(tester, 'tab-lessons');
        final card = find.byKey(
          const Key('dashboard-assignment-$fractionsLesson'),
        );
        expect(card, findsOneWidget);
        expect(
          find.descendant(of: card, matching: find.text('Finished: Sara')),
          findsOneWidget,
        );
        expect(
          find.descendant(of: card, matching: find.text('Not yet: Ali')),
          findsOneWidget,
        );
        await tapKey(tester, 'dashboard-unassign-$fractionsLesson');
        expect(backend.classes.assignmentsOf['class1'], isEmpty);
        expect(card, findsNothing);
      },
    );

    testWidgets('lessons published to Firestore join the bundled ones', (
      tester,
    ) async {
      // Asset loads cached by an earlier test belong to its fake clock.
      rootBundle.clear();
      final backend = FakeBackend();
      backend.remote.publishLesson(lessonJson(title: 'Only online'));
      final curriculum = (await tester.runAsync(
        () => loadDashboardCurriculum(backend.remote, hidden: const {}),
      ))!;
      expect(curriculum.lesson(newId)?.title.en, 'Only online');
      expect(curriculum.lesson(fractionsLesson), isNotNull);

      // Offline, the bundled lessons still load.
      backend.setOnline(false);
      final offline = (await tester.runAsync(
        () => loadDashboardCurriculum(backend.remote, hidden: const {}),
      ))!;
      expect(offline.lesson(fractionsLesson), isNotNull);
      expect(offline.lesson(newId), isNull);

      // Units not in the Grade 6 book are left out.
      backend.setOnline(true);
      final shown = (await tester.runAsync(
        () => loadDashboardCurriculum(backend.remote),
      ))!;
      expect(shown.lesson(fractionsLesson), isNull);
      expect(shown.lesson(newId), isNotNull);
    });
  });
}
