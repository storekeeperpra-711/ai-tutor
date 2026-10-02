import 'dart:async';

import 'package:ai_tutor/lessons/step_result.dart';
import 'package:ai_tutor/services/auth_service.dart';
import 'package:ai_tutor/services/local_db.dart';
import 'package:ai_tutor/services/remote_store.dart';
import 'package:drift/drift.dart';
import 'package:drift/native.dart';

/// A pretend Firebase for tests: an in-memory "server" that holds writes
/// back while [online] is false, like Firestore does, and sends them when
/// the connection returns.
class FakeBackend {
  FakeBackend() {
    auth = FakeAuthService(this);
    remote = FakeRemoteStore(this);
  }

  late final FakeAuthService auth;
  late final FakeRemoteStore remote;

  /// The phone's database, in memory.
  final db = LocalDb(
    DatabaseConnection(
      NativeDatabase.memory(),
      closeStreamsSynchronously: true,
    ),
  );

  var _online = true;
  bool get online => _online;
  final _onlineChanges = StreamController<bool>.broadcast();

  /// For `onlineProvider`.
  Stream<bool> get onlineStream async* {
    yield _online;
    yield* _onlineChanges.stream;
  }

  void setOnline(bool value) {
    _online = value;
    _onlineChanges.add(value);
    if (value) remote.flushHeld();
  }
}

class FakeAuthService implements AuthService {
  FakeAuthService(this._backend);

  final FakeBackend _backend;
  final _changes = StreamController<AppUser?>.broadcast();

  /// Adult accounts on the "server": email -> (password, uid).
  final accounts = <String, (String, String)>{};
  var _nextUid = 1;

  AppUser? _user;

  @override
  AppUser? get currentUser => _user;

  @override
  Stream<AppUser?> get userChanges async* {
    yield _user;
    yield* _changes.stream;
  }

  void _set(AppUser? user) {
    _user = user;
    _changes.add(user);
  }

  @override
  Future<void> ensureSignedIn() async {
    if (_user != null || !_backend.online) return;
    _set(AppUser(uid: 'phone-${_nextUid++}'));
  }

  @override
  Future<AppUser> signUp(String email, String password) async {
    if (!_backend.online) throw const AuthException(AuthProblem.noConnection);
    if (accounts.containsKey(email)) {
      throw const AuthException(AuthProblem.emailInUse);
    }
    if (password.length < 6) {
      throw const AuthException(AuthProblem.weakPassword);
    }
    // Like linkWithCredential: the phone's account keeps its uid.
    final uid = _user?.uid ?? 'adult-${_nextUid++}';
    accounts[email] = (password, uid);
    final user = AppUser(uid: uid, email: email);
    _set(user);
    return user;
  }

  @override
  Future<AppUser> signIn(String email, String password) async {
    if (!_backend.online) throw const AuthException(AuthProblem.noConnection);
    final account = accounts[email];
    if (account == null || account.$1 != password) {
      throw const AuthException(AuthProblem.wrongPassword);
    }
    final user = AppUser(uid: account.$2, email: email);
    _set(user);
    return user;
  }

  @override
  Future<void> signOut() async => _set(null);
}

class FakeRemoteStore implements RemoteStore {
  FakeRemoteStore(this._backend);

  final FakeBackend _backend;

  /// The "server": document path -> data.
  final docs = <String, Map<String, Object?>>{};

  /// Writes waiting for the connection.
  final _held = <(Completer<void>, void Function())>[];
  var writes = 0;

  Future<void> _write(void Function() apply) {
    if (_backend.online) {
      writes++;
      apply();
      return Future.value();
    }
    final done = Completer<void>();
    _held.add((done, apply));
    return done.future;
  }

  void flushHeld() {
    for (final (done, apply) in List.of(_held)) {
      writes++;
      apply();
      done.complete();
    }
    _held.clear();
  }

  static Map<String, Object?> _merge(
    Map<String, Object?> into,
    Map<String, Object?> data,
  ) {
    final result = Map<String, Object?>.of(into);
    data.forEach((key, value) {
      final old = result[key];
      result[key] = value is Map<String, Object?> && old is Map<String, Object?>
          ? _merge(old, value)
          : value;
    });
    return result;
  }

  @override
  Future<void> setRole(String uid, AccountRole role) => _write(() {
    docs['accounts/$uid'] = _merge(docs['accounts/$uid'] ?? {}, {
      'role': role.name,
    });
  });

  @override
  Future<void> putStudent(String uid, Student student) => _write(() {
    docs['accounts/$uid/students/${student.id}'] = studentToJson(student);
  });

  @override
  Future<void> putProgress(String uid, ProgressUpload upload) => _write(() {
    final path =
        'accounts/$uid/students/${upload.progress.studentId}'
        '/progress/${upload.progress.lessonId}';
    docs[path] = _merge(docs[path] ?? {}, progressToJson(upload));
  });

  @override
  Future<void> putSkill(String uid, SkillStateRow row) => _write(() {
    docs['accounts/$uid/students/${row.studentId}/skills/${row.skill}'] =
        skillToJson(row);
  });

  @override
  Future<void> deleteStudent(String uid, String studentId) => _write(() {
    docs.removeWhere(
      (path, _) => path.startsWith('accounts/$uid/students/$studentId'),
    );
  });

  @override
  Future<RemoteData> fetchAll(String uid) async {
    if (!_backend.online) throw StateError('offline');
    final students = <Student>[];
    final progress = <LessonProgress>[];
    final steps = <StepResultRow>[];
    final skills = <SkillStateRow>[];
    final skillPath = RegExp(
      '^accounts/$uid/students/([^/]+)/skills/([^/]+)\$',
    );
    final studentPath = RegExp('^accounts/$uid/students/([^/]+)\$');
    final progressPath = RegExp(
      '^accounts/$uid/students/([^/]+)/progress/([^/]+)\$',
    );
    docs.forEach((path, data) {
      if (studentPath.firstMatch(path) case final m?) {
        students.add(studentFromJson(m[1]!, Map.of(data)));
      } else if (progressPath.firstMatch(path) case final m?) {
        final (row, rows) = progressFromJson(m[1]!, m[2]!, Map.of(data));
        progress.add(row);
        steps.addAll(rows);
      } else if (skillPath.firstMatch(path) case final m?) {
        skills.add(skillFromJson(m[1]!, Map.of(data)));
      }
    });
    return RemoteData(
      role: docs['accounts/$uid']?['role'] as String?,
      students: students,
      progress: progress,
      steps: steps,
      skills: skills,
    );
  }

  /// The progress document of one lesson, for checks.
  Map<String, Object?>? progressDoc(
    String uid,
    String studentId,
    String lessonId,
  ) => docs['accounts/$uid/students/$studentId/progress/$lessonId'];
}

/// A learner for tests.
Student student(String id, {String name = 'Ayesha'}) => Student(
  id: id,
  firstName: name,
  grade: 6,
  avatar: 'star',
  createdAt: DateTime(2026, 10, 1),
  consentAt: DateTime(2026, 10, 1),
  synced: false,
);

/// Saves step [index] of a lesson as answered correctly.
Future<void> answer(
  LocalDb db,
  String studentId,
  int index, {
  String lessonId = 'lesson-a',
  int stepCount = 5,
  DateTime? now,
}) => db.recordStep(
  studentId: studentId,
  lessonId: lessonId,
  lessonVersion: 1,
  stepIndex: index,
  stepCount: stepCount,
  result: StepResult(stepId: 's$index', correct: true, attempts: 1),
  now: now,
);
