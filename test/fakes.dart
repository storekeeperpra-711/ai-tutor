import 'dart:async';

import 'package:ai_tutor/ai/ai_service.dart';
import 'package:ai_tutor/ai/keyword_fallback.dart';
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
    ai = FakeAiService(this);
  }

  late final FakeAuthService auth;
  late final FakeRemoteStore remote;
  late final FakeAiService ai;

  /// What the fake camera returns; null = the child cancelled.
  Uint8List? photo = Uint8List.fromList([0xff, 0xd8, 0xff]);

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

/// A pretend AI proxy. Offline it throws [AiUnavailable], like the real
/// one. By default it scores explanations with the keywords and reads
/// photos as [photoLines].
class FakeAiService implements AiService {
  FakeAiService(this._backend);

  final FakeBackend _backend;

  /// Keyword groups by step id, so the fake can grade like a teacher would.
  final keywords = <String, List<List<String>>>{};

  /// Set to make the server answer with a fallback (e.g. step_limit).
  String? fallbackReason;

  /// What the "AI" reads in the next photo.
  List<String> photoLines = const [];
  bool photoReadable = true;

  final explained = <String>[];
  final verdicts = <String>[];
  var photosRead = 0;

  void _online() {
    if (!_backend.online) throw const AiUnavailable('offline');
  }

  @override
  Future<AiFeedback> explain({
    required String studentId,
    required String lessonId,
    required String stepId,
    required String language,
    required String answer,
  }) async {
    _online();
    explained.add(answer);
    if (fallbackReason case final reason?) return AiFeedback.fallback(reason);
    // Without keywords for the step: a long answer "gets it".
    final groups = keywords[stepId];
    final level = groups != null
        ? scoreByKeywords(answer, groups)
        : answer.length >= 20
        ? AiLevel.gotIt
        : AiLevel.notYet;
    return AiFeedback.ai(level, 'AI ($language): ${level.id}');
  }

  @override
  Future<AiFeedback> explainVerdict({
    required String studentId,
    required String lessonId,
    required String stepId,
    required String language,
    required String working,
    required String checkerMessage,
  }) async {
    _online();
    verdicts.add(checkerMessage);
    if (fallbackReason case final reason?) return AiFeedback.fallback(reason);
    return AiFeedback.ai(AiLevel.notYet, 'AI explains: $checkerMessage');
  }

  @override
  Future<PhotoReading> readPhoto({
    required String studentId,
    required String lessonId,
    required String stepId,
    required Uint8List photo,
  }) async {
    _online();
    photosRead++;
    if (fallbackReason case final reason?) return PhotoReading.fallback(reason);
    return PhotoReading.ai(
      readable: photoReadable,
      lines: photoLines,
      finalAnswer: photoLines.isEmpty ? '' : photoLines.last,
    );
  }

  @override
  Future<CostReport> costs() async {
    _online();
    return const CostReport(
      all: false,
      totalUsd: 0.0045,
      rows: [
        CostRow(
          day: '2026-10-03',
          studentId: 's1',
          calls: 3,
          text: 2,
          photo: 1,
          costUsd: 0.0045,
        ),
      ],
    );
  }
}

class FakeAuthService implements AuthService {
  FakeAuthService(this._backend);

  @override
  Future<String?> idToken() async =>
      _user == null ? null : 'token-${_user!.uid}';

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

  @override
  Future<void> putQueuedAnswer(String uid, QueuedAnswer answer) => _write(() {
    docs['ai_queue/${answer.id}'] = queuedToJson(uid, answer);
  });

  @override
  Future<Map<String, QueueReply>> fetchReplies(
    String uid,
    List<String> ids,
  ) async {
    if (!_backend.online) throw StateError('offline');
    return {
      for (final id in ids)
        if (docs['ai_queue/$id'] case final d?
            when d['uid'] == uid && d['status'] != 'waiting')
          id: QueueReply(
            status: d['status'] == 'answered' ? 'answered' : 'failed',
            level: d['level'] as String?,
            reply: d['reply'] as String?,
          ),
    };
  }

  @override
  Future<List<WeeklyReport>> fetchReports(String uid, String studentId) async {
    if (!_backend.online) throw StateError('offline');
    final prefix = 'accounts/$uid/students/$studentId/reports/';
    final paths = docs.keys.where((p) => p.startsWith(prefix)).toList()
      ..sort((a, b) => b.compareTo(a));
    return [for (final p in paths) reportFromJson(Map.of(docs[p]!))];
  }

  /// The batch job answering a queued answer on the "server".
  void answerQueued(String id, {required String level, required String reply}) {
    docs['ai_queue/$id'] = {
      ...docs['ai_queue/$id']!,
      'status': 'answered',
      'level': level,
      'reply': reply,
    };
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
