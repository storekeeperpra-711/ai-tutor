import 'dart:async';
import 'dart:convert';

import 'package:ai_tutor/ai/ai_service.dart';
import 'package:ai_tutor/ai/keyword_fallback.dart';
import 'package:ai_tutor/character/mithu_controller.dart';
import 'package:ai_tutor/classes/class_store.dart';
import 'package:ai_tutor/character/narrator.dart';
import 'package:ai_tutor/character/sounds.dart';
import 'package:ai_tutor/character/voice_lines.dart';
import 'package:ai_tutor/lessons/lesson_updates.dart';
import 'package:ai_tutor/lessons/step_result.dart';
import 'package:ai_tutor/media/media_cache.dart';
import 'package:ai_tutor/reports/report_voice.dart';
import 'package:ai_tutor/review/review_store.dart';
import 'package:ai_tutor/services/auth_service.dart';
import 'package:ai_tutor/services/local_db.dart';
import 'package:ai_tutor/services/remote_store.dart';
import 'package:drift/drift.dart';
import 'package:drift/native.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:file/memory.dart';
import 'package:flutter_cache_manager/flutter_cache_manager.dart';

/// A pretend Firebase for tests: an in-memory "server" that holds writes
/// back while [online] is false, like Firestore does, and sends them when
/// the connection returns.
class FakeBackend {
  FakeBackend() {
    auth = FakeAuthService(this);
    remote = FakeRemoteStore(this);
    reviews = FakeReviewStore(this);
    classes = FakeClassStore(this);
    ai = FakeAiService(this);
  }

  late final FakeAuthService auth;
  late final FakeRemoteStore remote;
  late final FakeReviewStore reviews;
  late final FakeClassStore classes;
  late final FakeAiService ai;
  final narrator = FakeNarrator();
  final reportVoice = FakeReportVoice();
  final sounds = FakeSounds();

  /// Saved lesson videos, with nothing saved.
  final mediaIndex = FakeMediaIndex();
  late final mediaManager = FakeMediaManager(mediaIndex);
  late final media = MediaCache(manager: mediaManager, repo: mediaIndex);

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

  var _wifi = true;
  final _wifiChanges = StreamController<bool>.broadcast();

  /// For `onWifiProvider`.
  Stream<bool> get wifiStream async* {
    yield _wifi;
    yield* _wifiChanges.stream;
  }

  void setWifi(bool value) {
    _wifi = value;
    _wifiChanges.add(value);
  }

  /// What Android says the app has used, for `appByteCounterProvider`.
  int? appBytes;

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

  /// What the cost dashboard shows (a default when null).
  CostReport? costReport;
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
    return costReport ??
        const CostReport(
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
    final user = AppUser(
      uid: account.$2,
      email: email,
      emailVerified: verified.contains(email),
    );
    _set(user);
    return user;
  }

  @override
  Future<void> signOut() async => _set(null);

  /// Emails a verification link went to.
  final verificationsSent = <String>[];

  /// Emails whose link was tapped.
  final verified = <String>{};

  @override
  Future<void> sendVerificationEmail() async {
    if (!_backend.online) throw const AuthException(AuthProblem.noConnection);
    if (_user?.email case final email?) verificationsSent.add(email);
  }

  @override
  Future<AppUser?> refreshUser() async {
    final user = _user;
    if (user?.email == null) return user;
    final updated = AppUser(
      uid: user!.uid,
      email: user.email,
      emailVerified: verified.contains(user.email),
    );
    _set(updated);
    return updated;
  }
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

  @override
  Future<Map<String, CatalogEntry>> fetchLessonCatalog() async {
    if (!_backend.online) throw StateError('offline');
    lessonReads++;
    return catalogFromJson(docs['lesson_catalog/current']);
  }

  @override
  Future<PublishedLesson?> fetchPublishedLesson(String lessonId) async {
    if (!_backend.online) throw StateError('offline');
    lessonReads++;
    final data = docs['published_lessons/$lessonId'];
    return data == null ? null : publishedLessonFromJson(Map.of(data));
  }

  /// Reads of the lesson catalog and published lessons.
  var lessonReads = 0;

  /// Publishes [lesson] on the "server", like tools/upload.py.
  void publishLesson(Map<String, Object?> lesson, {int version = 1}) {
    final content = jsonEncode(lesson);
    final hash = lessonFingerprint(content);
    final id = lesson['id']! as String;
    docs['published_lessons/$id'] = {
      'version': version,
      'hash': hash,
      'format': 1,
      'content': content,
    };
    final catalog = Map<String, Object?>.from(
      (docs['lesson_catalog/current']?['lessons'] as Map?) ?? const {},
    );
    catalog[id] = {'version': version, 'hash': hash};
    docs['lesson_catalog/current'] = {'lessons': catalog};
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
Student student(String id, {String name = 'Ayesha', int grade = 6}) => Student(
  id: id,
  firstName: name,
  grade: grade,
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

/// Records what Mithu was asked to say; plays nothing.
class FakeNarrator implements Narrator {
  final said = <VoiceLine>[];
  final recorded = <String>{};

  @override
  Future<bool> hasRecording(VoiceLine voice) async =>
      recorded.contains(voice.fileName);

  @override
  Future<VoiceKind> say(VoiceLine voice, MithuController mithu) async {
    said.add(voice);
    return VoiceKind.none;
  }

  @override
  Future<void> stop() async {}
}

/// Records the sound effects the app played.
class FakeSounds implements SoundPlayer {
  final played = <Sound>[];

  @override
  void play(Sound sound) => played.add(sound);
}

/// Teacher review on the pretend server, checked like firestore.rules: only
/// a listed reviewer with a verified email gets in.
class FakeReviewStore implements ReviewStore {
  FakeReviewStore(this._backend);

  final FakeBackend _backend;

  /// config/reviewers.
  final reviewers = <String>{};

  /// lesson_reviews, by lesson id.
  final docs = <String, LessonReview>{};

  /// Notes, by lesson id.
  final notesOf = <String, List<ReviewNote>>{};

  /// Puts [lessonId]'s published version up for review, like
  /// tools/upload.py.
  void submit(String lessonId) {
    final published = _backend.remote.docs['published_lessons/$lessonId']!;
    docs[lessonId] = LessonReview(
      lessonId: lessonId,
      hash: published['hash']! as String,
      version: published['version']! as int,
      status: ReviewStatus.inReview,
    );
  }

  void _check() {
    if (!_backend.online) throw StateError('offline');
    final user = _backend.auth.currentUser;
    if (user == null ||
        !user.emailVerified ||
        !reviewers.contains(user.email?.toLowerCase())) {
      throw StateError('permission-denied');
    }
  }

  @override
  Future<bool> isReviewer() async {
    if (!_backend.online) throw StateError('offline');
    try {
      _check();
      return true;
    } on StateError {
      return false;
    }
  }

  @override
  Future<List<LessonReview>> reviews() async {
    _check();
    return docs.values.toList();
  }

  @override
  Future<List<ReviewNote>> notes(String lessonId) async {
    _check();
    return List.of(notesOf[lessonId] ?? const <ReviewNote>[]);
  }

  @override
  Future<void> addNote(String lessonId, ReviewNote note) async {
    _check();
    if (note.hash != docs[lessonId]?.hash) throw StateError('wrong version');
    (notesOf[lessonId] ??= []).add(note);
  }

  @override
  Future<void> decide(
    String lessonId, {
    required String hash,
    required bool approved,
    required String reviewer,
  }) async {
    _check();
    final review = docs[lessonId]!;
    if (approved && hash != review.hash) throw StateError('wrong version');
    docs[lessonId] = LessonReview(
      lessonId: lessonId,
      hash: review.hash,
      version: review.version,
      status: approved ? ReviewStatus.approved : ReviewStatus.changesRequested,
      reviewer: reviewer,
    );
  }
}

/// Classes on the pretend server, checked like firestore.rules.
class FakeClassStore implements ClassStore {
  FakeClassStore(this._backend);

  final FakeBackend _backend;

  final classes = <String, SchoolClass>{};

  /// Members by class id, then by document id.
  final membersOf = <String, Map<String, ClassMember>>{};

  /// Family uids by class id.
  final families = <String, Set<String>>{};
  final assignmentsOf = <String, List<Assignment>>{};

  /// Writes of children's summaries.
  var memberWrites = 0;
  var _ids = 0;

  String _signedIn() {
    if (!_backend.online) throw StateError('offline');
    final uid = _backend.auth.currentUser?.uid;
    if (uid == null) throw StateError('signed out');
    return uid;
  }

  static FirebaseException _denied() =>
      FirebaseException(plugin: 'cloud_firestore', code: 'permission-denied');

  SchoolClass _teaching(String classId) {
    final uid = _signedIn();
    final c = classes[classId];
    if (c == null || c.teacherUid != uid) throw _denied();
    return c;
  }

  /// A class made by [teacherUid] straight on the server, for tests.
  SchoolClass addClass({
    String id = 'class1',
    String name = '9 A',
    String code = 'ABC234',
    String teacherUid = 'teacher1',
  }) => classes[id] = SchoolClass(
    id: id,
    name: name,
    code: code,
    teacherUid: teacherUid,
  );

  /// The teacher assigning a lesson, straight on the server.
  Future<void> assignAs(
    String classId,
    String lessonId, {
    DateTime? due,
  }) async {
    (assignmentsOf[classId] ??= []).add(
      Assignment(
        id: 'a${++_ids}',
        lessonId: lessonId,
        due: due,
        createdAt: DateTime(2026, 10, 3, 9, _ids),
      ),
    );
  }

  @override
  Future<SchoolClass> createClass(String teacherUid, String name) async {
    if (_signedIn() != teacherUid) throw _denied();
    return addClass(
      id: 'class${++_ids}',
      name: name,
      code: newClassCode(),
      teacherUid: teacherUid,
    );
  }

  @override
  Future<List<SchoolClass>> classesOf(String teacherUid) async {
    if (_signedIn() != teacherUid) throw _denied();
    return [
      for (final c in classes.values)
        if (c.teacherUid == teacherUid) c,
    ];
  }

  @override
  Future<List<ClassMember>> members(String classId) async {
    _teaching(classId);
    return [...?membersOf[classId]?.values];
  }

  @override
  Future<List<Assignment>> assignments(String classId) async {
    final uid = _signedIn();
    final c = classes[classId];
    if (c == null ||
        (c.teacherUid != uid && !(families[classId]?.contains(uid) ?? false))) {
      throw _denied();
    }
    return [...?assignmentsOf[classId]];
  }

  @override
  Future<void> assign(
    String classId, {
    required String lessonId,
    DateTime? due,
  }) async {
    _teaching(classId);
    (assignmentsOf[classId] ??= []).add(
      Assignment(
        id: 'a${++_ids}',
        lessonId: lessonId,
        due: due,
        createdAt: DateTime(2026, 10, 3, 9, _ids),
      ),
    );
  }

  @override
  Future<void> unassign(String classId, String assignmentId) async {
    _teaching(classId);
    assignmentsOf[classId]?.removeWhere((a) => a.id == assignmentId);
  }

  @override
  Future<void> deleteClass(SchoolClass schoolClass) async {
    _teaching(schoolClass.id);
    classes.remove(schoolClass.id);
    membersOf.remove(schoolClass.id);
    families.remove(schoolClass.id);
    assignmentsOf.remove(schoolClass.id);
  }

  @override
  Future<ClassInfo?> findClass(String code) async {
    _signedIn();
    final c = classes.values.where((c) => c.code == code).firstOrNull;
    return c == null ? null : (id: c.id, name: c.name);
  }

  @override
  Future<void> putMember(
    String classId,
    ClassMember member, {
    bool join = false,
  }) async {
    final uid = _signedIn();
    if (!classes.containsKey(classId) || member.uid != uid) throw _denied();
    if (join) (families[classId] ??= {}).add(uid);
    if (!(families[classId]?.contains(uid) ?? false)) throw _denied();
    memberWrites++;
    (membersOf[classId] ??= {})[member.docId] = member;
  }

  @override
  Future<void> removeMember(
    String classId,
    String uid,
    String studentId, {
    bool lastChild = false,
  }) async {
    if (_signedIn() != uid) throw _denied();
    membersOf[classId]?.remove(memberDocId(uid, studentId));
    if (lastChild) families[classId]?.remove(uid);
  }
}

/// The phone's voice for the parent report: records what it said. Each
/// sentence waits for [finishSentence] when [holdEach] is set.
class FakeReportVoice implements ReportVoice {
  /// Languages the "phone" can speak.
  final languages = {'en', 'ur'};
  final said = <(String, String)>[];
  var holdEach = false;
  Completer<void>? _current;
  var stopped = 0;

  @override
  Future<bool> canSpeak(String languageCode) async =>
      languages.contains(languageCode);

  @override
  Future<void> speak(String text, String languageCode) async {
    said.add((text, languageCode));
    if (!holdEach) return;
    final done = _current = Completer<void>();
    await done.future;
  }

  void finishSentence() {
    _current?.complete();
    _current = null;
  }

  @override
  Future<void> stop() async {
    stopped++;
    finishSentence();
  }
}

/// Saved files as the cache's index lists them.
class FakeMediaIndex implements CacheInfoRepository {
  final objects = <String, CacheObject>{};

  void add(String url, int length, DateTime touched) =>
      objects[url] = CacheObject(
        url,
        relativePath: url,
        validTill: touched,
        length: length,
        touched: touched,
      );

  @override
  Future<bool> open() async => true;

  @override
  Future<CacheObject?> get(String key) async => objects[key];

  @override
  Future<List<CacheObject>> getAllObjects() async => objects.values.toList();

  @override
  dynamic noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);
}

class FakeMediaManager implements BaseCacheManager {
  FakeMediaManager(this.repo);

  final FakeMediaIndex repo;
  final removed = <String>[];

  @override
  Future<void> removeFile(String key) async {
    removed.add(key);
    repo.objects.remove(key);
  }

  @override
  Future<void> emptyCache() async => repo.objects.clear();

  /// Links downloaded, in order; [failDownloads] makes them fail.
  final downloaded = <String>[];
  var failDownloads = false;

  @override
  Future<FileInfo> downloadFile(
    String url, {
    String? key,
    Map<String, String>? authHeaders,
    bool force = false,
  }) async {
    if (failDownloads) throw Exception('offline');
    downloaded.add(url);
    repo.add(url, 5 * 1024 * 1024, DateTime(2026, 10, 4));
    return FileInfo(
      MemoryFileSystem().file('/$url'),
      FileSource.Online,
      DateTime(2026, 11, 4),
      url,
    );
  }

  @override
  dynamic noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);
}
