// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'local_db.dart';

// ignore_for_file: type=lint
class $StudentsTable extends Students with TableInfo<$StudentsTable, Student> {
  @override
  final GeneratedDatabase attachedDatabase;
  final String? _alias;
  $StudentsTable(this.attachedDatabase, [this._alias]);
  static const VerificationMeta _idMeta = const VerificationMeta('id');
  @override
  late final GeneratedColumn<String> id = GeneratedColumn<String>(
    'id',
    aliasedName,
    false,
    type: DriftSqlType.string,
    requiredDuringInsert: true,
  );
  static const VerificationMeta _firstNameMeta = const VerificationMeta(
    'firstName',
  );
  @override
  late final GeneratedColumn<String> firstName = GeneratedColumn<String>(
    'first_name',
    aliasedName,
    false,
    additionalChecks: GeneratedColumn.checkTextLength(
      minTextLength: 1,
      maxTextLength: 30,
    ),
    type: DriftSqlType.string,
    requiredDuringInsert: true,
  );
  static const VerificationMeta _gradeMeta = const VerificationMeta('grade');
  @override
  late final GeneratedColumn<int> grade = GeneratedColumn<int>(
    'grade',
    aliasedName,
    false,
    type: DriftSqlType.int,
    requiredDuringInsert: true,
  );
  static const VerificationMeta _avatarMeta = const VerificationMeta('avatar');
  @override
  late final GeneratedColumn<String> avatar = GeneratedColumn<String>(
    'avatar',
    aliasedName,
    false,
    type: DriftSqlType.string,
    requiredDuringInsert: true,
  );
  static const VerificationMeta _pinHashMeta = const VerificationMeta(
    'pinHash',
  );
  @override
  late final GeneratedColumn<String> pinHash = GeneratedColumn<String>(
    'pin_hash',
    aliasedName,
    true,
    type: DriftSqlType.string,
    requiredDuringInsert: false,
  );
  static const VerificationMeta _createdAtMeta = const VerificationMeta(
    'createdAt',
  );
  @override
  late final GeneratedColumn<DateTime> createdAt = GeneratedColumn<DateTime>(
    'created_at',
    aliasedName,
    false,
    type: DriftSqlType.dateTime,
    requiredDuringInsert: true,
  );
  static const VerificationMeta _consentAtMeta = const VerificationMeta(
    'consentAt',
  );
  @override
  late final GeneratedColumn<DateTime> consentAt = GeneratedColumn<DateTime>(
    'consent_at',
    aliasedName,
    false,
    type: DriftSqlType.dateTime,
    requiredDuringInsert: true,
  );
  static const VerificationMeta _syncedMeta = const VerificationMeta('synced');
  @override
  late final GeneratedColumn<bool> synced = GeneratedColumn<bool>(
    'synced',
    aliasedName,
    false,
    type: DriftSqlType.bool,
    requiredDuringInsert: false,
    defaultConstraints: GeneratedColumn.constraintIsAlways(
      'CHECK ("synced" IN (0, 1))',
    ),
    defaultValue: const Constant(false),
  );
  @override
  List<GeneratedColumn> get $columns => [
    id,
    firstName,
    grade,
    avatar,
    pinHash,
    createdAt,
    consentAt,
    synced,
  ];
  @override
  String get aliasedName => _alias ?? actualTableName;
  @override
  String get actualTableName => $name;
  static const String $name = 'students';
  @override
  VerificationContext validateIntegrity(
    Insertable<Student> instance, {
    bool isInserting = false,
  }) {
    final context = VerificationContext();
    final data = instance.toColumns(true);
    if (data.containsKey('id')) {
      context.handle(_idMeta, id.isAcceptableOrUnknown(data['id']!, _idMeta));
    } else if (isInserting) {
      context.missing(_idMeta);
    }
    if (data.containsKey('first_name')) {
      context.handle(
        _firstNameMeta,
        firstName.isAcceptableOrUnknown(data['first_name']!, _firstNameMeta),
      );
    } else if (isInserting) {
      context.missing(_firstNameMeta);
    }
    if (data.containsKey('grade')) {
      context.handle(
        _gradeMeta,
        grade.isAcceptableOrUnknown(data['grade']!, _gradeMeta),
      );
    } else if (isInserting) {
      context.missing(_gradeMeta);
    }
    if (data.containsKey('avatar')) {
      context.handle(
        _avatarMeta,
        avatar.isAcceptableOrUnknown(data['avatar']!, _avatarMeta),
      );
    } else if (isInserting) {
      context.missing(_avatarMeta);
    }
    if (data.containsKey('pin_hash')) {
      context.handle(
        _pinHashMeta,
        pinHash.isAcceptableOrUnknown(data['pin_hash']!, _pinHashMeta),
      );
    }
    if (data.containsKey('created_at')) {
      context.handle(
        _createdAtMeta,
        createdAt.isAcceptableOrUnknown(data['created_at']!, _createdAtMeta),
      );
    } else if (isInserting) {
      context.missing(_createdAtMeta);
    }
    if (data.containsKey('consent_at')) {
      context.handle(
        _consentAtMeta,
        consentAt.isAcceptableOrUnknown(data['consent_at']!, _consentAtMeta),
      );
    } else if (isInserting) {
      context.missing(_consentAtMeta);
    }
    if (data.containsKey('synced')) {
      context.handle(
        _syncedMeta,
        synced.isAcceptableOrUnknown(data['synced']!, _syncedMeta),
      );
    }
    return context;
  }

  @override
  Set<GeneratedColumn> get $primaryKey => {id};
  @override
  Student map(Map<String, dynamic> data, {String? tablePrefix}) {
    final effectivePrefix = tablePrefix != null ? '$tablePrefix.' : '';
    return Student(
      id: attachedDatabase.typeMapping.read(
        DriftSqlType.string,
        data['${effectivePrefix}id'],
      )!,
      firstName: attachedDatabase.typeMapping.read(
        DriftSqlType.string,
        data['${effectivePrefix}first_name'],
      )!,
      grade: attachedDatabase.typeMapping.read(
        DriftSqlType.int,
        data['${effectivePrefix}grade'],
      )!,
      avatar: attachedDatabase.typeMapping.read(
        DriftSqlType.string,
        data['${effectivePrefix}avatar'],
      )!,
      pinHash: attachedDatabase.typeMapping.read(
        DriftSqlType.string,
        data['${effectivePrefix}pin_hash'],
      ),
      createdAt: attachedDatabase.typeMapping.read(
        DriftSqlType.dateTime,
        data['${effectivePrefix}created_at'],
      )!,
      consentAt: attachedDatabase.typeMapping.read(
        DriftSqlType.dateTime,
        data['${effectivePrefix}consent_at'],
      )!,
      synced: attachedDatabase.typeMapping.read(
        DriftSqlType.bool,
        data['${effectivePrefix}synced'],
      )!,
    );
  }

  @override
  $StudentsTable createAlias(String alias) {
    return $StudentsTable(attachedDatabase, alias);
  }
}

class Student extends DataClass implements Insertable<Student> {
  final String id;
  final String firstName;

  /// -1 = Nursery, 0 = Prep, 1 to 12 = Grade 1 to 12.
  final int grade;

  /// One of [avatarIds].
  final String avatar;

  /// `salt:sha256` of the child's PIN, or null for picture-only login.
  final String? pinHash;
  final DateTime createdAt;

  /// When a parent or guardian agreed to save this child's data.
  final DateTime consentAt;
  final bool synced;
  const Student({
    required this.id,
    required this.firstName,
    required this.grade,
    required this.avatar,
    this.pinHash,
    required this.createdAt,
    required this.consentAt,
    required this.synced,
  });
  @override
  Map<String, Expression> toColumns(bool nullToAbsent) {
    final map = <String, Expression>{};
    map['id'] = Variable<String>(id);
    map['first_name'] = Variable<String>(firstName);
    map['grade'] = Variable<int>(grade);
    map['avatar'] = Variable<String>(avatar);
    if (!nullToAbsent || pinHash != null) {
      map['pin_hash'] = Variable<String>(pinHash);
    }
    map['created_at'] = Variable<DateTime>(createdAt);
    map['consent_at'] = Variable<DateTime>(consentAt);
    map['synced'] = Variable<bool>(synced);
    return map;
  }

  StudentsCompanion toCompanion(bool nullToAbsent) {
    return StudentsCompanion(
      id: Value(id),
      firstName: Value(firstName),
      grade: Value(grade),
      avatar: Value(avatar),
      pinHash: pinHash == null && nullToAbsent
          ? const Value.absent()
          : Value(pinHash),
      createdAt: Value(createdAt),
      consentAt: Value(consentAt),
      synced: Value(synced),
    );
  }

  factory Student.fromJson(
    Map<String, dynamic> json, {
    ValueSerializer? serializer,
  }) {
    serializer ??= driftRuntimeOptions.defaultSerializer;
    return Student(
      id: serializer.fromJson<String>(json['id']),
      firstName: serializer.fromJson<String>(json['firstName']),
      grade: serializer.fromJson<int>(json['grade']),
      avatar: serializer.fromJson<String>(json['avatar']),
      pinHash: serializer.fromJson<String?>(json['pinHash']),
      createdAt: serializer.fromJson<DateTime>(json['createdAt']),
      consentAt: serializer.fromJson<DateTime>(json['consentAt']),
      synced: serializer.fromJson<bool>(json['synced']),
    );
  }
  @override
  Map<String, dynamic> toJson({ValueSerializer? serializer}) {
    serializer ??= driftRuntimeOptions.defaultSerializer;
    return <String, dynamic>{
      'id': serializer.toJson<String>(id),
      'firstName': serializer.toJson<String>(firstName),
      'grade': serializer.toJson<int>(grade),
      'avatar': serializer.toJson<String>(avatar),
      'pinHash': serializer.toJson<String?>(pinHash),
      'createdAt': serializer.toJson<DateTime>(createdAt),
      'consentAt': serializer.toJson<DateTime>(consentAt),
      'synced': serializer.toJson<bool>(synced),
    };
  }

  Student copyWith({
    String? id,
    String? firstName,
    int? grade,
    String? avatar,
    Value<String?> pinHash = const Value.absent(),
    DateTime? createdAt,
    DateTime? consentAt,
    bool? synced,
  }) => Student(
    id: id ?? this.id,
    firstName: firstName ?? this.firstName,
    grade: grade ?? this.grade,
    avatar: avatar ?? this.avatar,
    pinHash: pinHash.present ? pinHash.value : this.pinHash,
    createdAt: createdAt ?? this.createdAt,
    consentAt: consentAt ?? this.consentAt,
    synced: synced ?? this.synced,
  );
  Student copyWithCompanion(StudentsCompanion data) {
    return Student(
      id: data.id.present ? data.id.value : this.id,
      firstName: data.firstName.present ? data.firstName.value : this.firstName,
      grade: data.grade.present ? data.grade.value : this.grade,
      avatar: data.avatar.present ? data.avatar.value : this.avatar,
      pinHash: data.pinHash.present ? data.pinHash.value : this.pinHash,
      createdAt: data.createdAt.present ? data.createdAt.value : this.createdAt,
      consentAt: data.consentAt.present ? data.consentAt.value : this.consentAt,
      synced: data.synced.present ? data.synced.value : this.synced,
    );
  }

  @override
  String toString() {
    return (StringBuffer('Student(')
          ..write('id: $id, ')
          ..write('firstName: $firstName, ')
          ..write('grade: $grade, ')
          ..write('avatar: $avatar, ')
          ..write('pinHash: $pinHash, ')
          ..write('createdAt: $createdAt, ')
          ..write('consentAt: $consentAt, ')
          ..write('synced: $synced')
          ..write(')'))
        .toString();
  }

  @override
  int get hashCode => Object.hash(
    id,
    firstName,
    grade,
    avatar,
    pinHash,
    createdAt,
    consentAt,
    synced,
  );
  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      (other is Student &&
          other.id == this.id &&
          other.firstName == this.firstName &&
          other.grade == this.grade &&
          other.avatar == this.avatar &&
          other.pinHash == this.pinHash &&
          other.createdAt == this.createdAt &&
          other.consentAt == this.consentAt &&
          other.synced == this.synced);
}

class StudentsCompanion extends UpdateCompanion<Student> {
  final Value<String> id;
  final Value<String> firstName;
  final Value<int> grade;
  final Value<String> avatar;
  final Value<String?> pinHash;
  final Value<DateTime> createdAt;
  final Value<DateTime> consentAt;
  final Value<bool> synced;
  final Value<int> rowid;
  const StudentsCompanion({
    this.id = const Value.absent(),
    this.firstName = const Value.absent(),
    this.grade = const Value.absent(),
    this.avatar = const Value.absent(),
    this.pinHash = const Value.absent(),
    this.createdAt = const Value.absent(),
    this.consentAt = const Value.absent(),
    this.synced = const Value.absent(),
    this.rowid = const Value.absent(),
  });
  StudentsCompanion.insert({
    required String id,
    required String firstName,
    required int grade,
    required String avatar,
    this.pinHash = const Value.absent(),
    required DateTime createdAt,
    required DateTime consentAt,
    this.synced = const Value.absent(),
    this.rowid = const Value.absent(),
  }) : id = Value(id),
       firstName = Value(firstName),
       grade = Value(grade),
       avatar = Value(avatar),
       createdAt = Value(createdAt),
       consentAt = Value(consentAt);
  static Insertable<Student> custom({
    Expression<String>? id,
    Expression<String>? firstName,
    Expression<int>? grade,
    Expression<String>? avatar,
    Expression<String>? pinHash,
    Expression<DateTime>? createdAt,
    Expression<DateTime>? consentAt,
    Expression<bool>? synced,
    Expression<int>? rowid,
  }) {
    return RawValuesInsertable({
      if (id != null) 'id': id,
      if (firstName != null) 'first_name': firstName,
      if (grade != null) 'grade': grade,
      if (avatar != null) 'avatar': avatar,
      if (pinHash != null) 'pin_hash': pinHash,
      if (createdAt != null) 'created_at': createdAt,
      if (consentAt != null) 'consent_at': consentAt,
      if (synced != null) 'synced': synced,
      if (rowid != null) 'rowid': rowid,
    });
  }

  StudentsCompanion copyWith({
    Value<String>? id,
    Value<String>? firstName,
    Value<int>? grade,
    Value<String>? avatar,
    Value<String?>? pinHash,
    Value<DateTime>? createdAt,
    Value<DateTime>? consentAt,
    Value<bool>? synced,
    Value<int>? rowid,
  }) {
    return StudentsCompanion(
      id: id ?? this.id,
      firstName: firstName ?? this.firstName,
      grade: grade ?? this.grade,
      avatar: avatar ?? this.avatar,
      pinHash: pinHash ?? this.pinHash,
      createdAt: createdAt ?? this.createdAt,
      consentAt: consentAt ?? this.consentAt,
      synced: synced ?? this.synced,
      rowid: rowid ?? this.rowid,
    );
  }

  @override
  Map<String, Expression> toColumns(bool nullToAbsent) {
    final map = <String, Expression>{};
    if (id.present) {
      map['id'] = Variable<String>(id.value);
    }
    if (firstName.present) {
      map['first_name'] = Variable<String>(firstName.value);
    }
    if (grade.present) {
      map['grade'] = Variable<int>(grade.value);
    }
    if (avatar.present) {
      map['avatar'] = Variable<String>(avatar.value);
    }
    if (pinHash.present) {
      map['pin_hash'] = Variable<String>(pinHash.value);
    }
    if (createdAt.present) {
      map['created_at'] = Variable<DateTime>(createdAt.value);
    }
    if (consentAt.present) {
      map['consent_at'] = Variable<DateTime>(consentAt.value);
    }
    if (synced.present) {
      map['synced'] = Variable<bool>(synced.value);
    }
    if (rowid.present) {
      map['rowid'] = Variable<int>(rowid.value);
    }
    return map;
  }

  @override
  String toString() {
    return (StringBuffer('StudentsCompanion(')
          ..write('id: $id, ')
          ..write('firstName: $firstName, ')
          ..write('grade: $grade, ')
          ..write('avatar: $avatar, ')
          ..write('pinHash: $pinHash, ')
          ..write('createdAt: $createdAt, ')
          ..write('consentAt: $consentAt, ')
          ..write('synced: $synced, ')
          ..write('rowid: $rowid')
          ..write(')'))
        .toString();
  }
}

class $LessonProgressTableTable extends LessonProgressTable
    with TableInfo<$LessonProgressTableTable, LessonProgress> {
  @override
  final GeneratedDatabase attachedDatabase;
  final String? _alias;
  $LessonProgressTableTable(this.attachedDatabase, [this._alias]);
  static const VerificationMeta _studentIdMeta = const VerificationMeta(
    'studentId',
  );
  @override
  late final GeneratedColumn<String> studentId = GeneratedColumn<String>(
    'student_id',
    aliasedName,
    false,
    type: DriftSqlType.string,
    requiredDuringInsert: true,
    defaultConstraints: GeneratedColumn.constraintIsAlways(
      'REFERENCES students (id)',
    ),
  );
  static const VerificationMeta _lessonIdMeta = const VerificationMeta(
    'lessonId',
  );
  @override
  late final GeneratedColumn<String> lessonId = GeneratedColumn<String>(
    'lesson_id',
    aliasedName,
    false,
    type: DriftSqlType.string,
    requiredDuringInsert: true,
  );
  static const VerificationMeta _lessonVersionMeta = const VerificationMeta(
    'lessonVersion',
  );
  @override
  late final GeneratedColumn<int> lessonVersion = GeneratedColumn<int>(
    'lesson_version',
    aliasedName,
    false,
    type: DriftSqlType.int,
    requiredDuringInsert: true,
  );
  static const VerificationMeta _nextStepMeta = const VerificationMeta(
    'nextStep',
  );
  @override
  late final GeneratedColumn<int> nextStep = GeneratedColumn<int>(
    'next_step',
    aliasedName,
    false,
    type: DriftSqlType.int,
    requiredDuringInsert: true,
  );
  static const VerificationMeta _completedMeta = const VerificationMeta(
    'completed',
  );
  @override
  late final GeneratedColumn<bool> completed = GeneratedColumn<bool>(
    'completed',
    aliasedName,
    false,
    type: DriftSqlType.bool,
    requiredDuringInsert: true,
    defaultConstraints: GeneratedColumn.constraintIsAlways(
      'CHECK ("completed" IN (0, 1))',
    ),
  );
  static const VerificationMeta _updatedAtMeta = const VerificationMeta(
    'updatedAt',
  );
  @override
  late final GeneratedColumn<DateTime> updatedAt = GeneratedColumn<DateTime>(
    'updated_at',
    aliasedName,
    false,
    type: DriftSqlType.dateTime,
    requiredDuringInsert: true,
  );
  @override
  List<GeneratedColumn> get $columns => [
    studentId,
    lessonId,
    lessonVersion,
    nextStep,
    completed,
    updatedAt,
  ];
  @override
  String get aliasedName => _alias ?? actualTableName;
  @override
  String get actualTableName => $name;
  static const String $name = 'lesson_progress';
  @override
  VerificationContext validateIntegrity(
    Insertable<LessonProgress> instance, {
    bool isInserting = false,
  }) {
    final context = VerificationContext();
    final data = instance.toColumns(true);
    if (data.containsKey('student_id')) {
      context.handle(
        _studentIdMeta,
        studentId.isAcceptableOrUnknown(data['student_id']!, _studentIdMeta),
      );
    } else if (isInserting) {
      context.missing(_studentIdMeta);
    }
    if (data.containsKey('lesson_id')) {
      context.handle(
        _lessonIdMeta,
        lessonId.isAcceptableOrUnknown(data['lesson_id']!, _lessonIdMeta),
      );
    } else if (isInserting) {
      context.missing(_lessonIdMeta);
    }
    if (data.containsKey('lesson_version')) {
      context.handle(
        _lessonVersionMeta,
        lessonVersion.isAcceptableOrUnknown(
          data['lesson_version']!,
          _lessonVersionMeta,
        ),
      );
    } else if (isInserting) {
      context.missing(_lessonVersionMeta);
    }
    if (data.containsKey('next_step')) {
      context.handle(
        _nextStepMeta,
        nextStep.isAcceptableOrUnknown(data['next_step']!, _nextStepMeta),
      );
    } else if (isInserting) {
      context.missing(_nextStepMeta);
    }
    if (data.containsKey('completed')) {
      context.handle(
        _completedMeta,
        completed.isAcceptableOrUnknown(data['completed']!, _completedMeta),
      );
    } else if (isInserting) {
      context.missing(_completedMeta);
    }
    if (data.containsKey('updated_at')) {
      context.handle(
        _updatedAtMeta,
        updatedAt.isAcceptableOrUnknown(data['updated_at']!, _updatedAtMeta),
      );
    } else if (isInserting) {
      context.missing(_updatedAtMeta);
    }
    return context;
  }

  @override
  Set<GeneratedColumn> get $primaryKey => {studentId, lessonId};
  @override
  LessonProgress map(Map<String, dynamic> data, {String? tablePrefix}) {
    final effectivePrefix = tablePrefix != null ? '$tablePrefix.' : '';
    return LessonProgress(
      studentId: attachedDatabase.typeMapping.read(
        DriftSqlType.string,
        data['${effectivePrefix}student_id'],
      )!,
      lessonId: attachedDatabase.typeMapping.read(
        DriftSqlType.string,
        data['${effectivePrefix}lesson_id'],
      )!,
      lessonVersion: attachedDatabase.typeMapping.read(
        DriftSqlType.int,
        data['${effectivePrefix}lesson_version'],
      )!,
      nextStep: attachedDatabase.typeMapping.read(
        DriftSqlType.int,
        data['${effectivePrefix}next_step'],
      )!,
      completed: attachedDatabase.typeMapping.read(
        DriftSqlType.bool,
        data['${effectivePrefix}completed'],
      )!,
      updatedAt: attachedDatabase.typeMapping.read(
        DriftSqlType.dateTime,
        data['${effectivePrefix}updated_at'],
      )!,
    );
  }

  @override
  $LessonProgressTableTable createAlias(String alias) {
    return $LessonProgressTableTable(attachedDatabase, alias);
  }
}

class LessonProgress extends DataClass implements Insertable<LessonProgress> {
  final String studentId;
  final String lessonId;
  final int lessonVersion;

  /// Index of the step to show when the lesson is opened again.
  final int nextStep;
  final bool completed;
  final DateTime updatedAt;
  const LessonProgress({
    required this.studentId,
    required this.lessonId,
    required this.lessonVersion,
    required this.nextStep,
    required this.completed,
    required this.updatedAt,
  });
  @override
  Map<String, Expression> toColumns(bool nullToAbsent) {
    final map = <String, Expression>{};
    map['student_id'] = Variable<String>(studentId);
    map['lesson_id'] = Variable<String>(lessonId);
    map['lesson_version'] = Variable<int>(lessonVersion);
    map['next_step'] = Variable<int>(nextStep);
    map['completed'] = Variable<bool>(completed);
    map['updated_at'] = Variable<DateTime>(updatedAt);
    return map;
  }

  LessonProgressTableCompanion toCompanion(bool nullToAbsent) {
    return LessonProgressTableCompanion(
      studentId: Value(studentId),
      lessonId: Value(lessonId),
      lessonVersion: Value(lessonVersion),
      nextStep: Value(nextStep),
      completed: Value(completed),
      updatedAt: Value(updatedAt),
    );
  }

  factory LessonProgress.fromJson(
    Map<String, dynamic> json, {
    ValueSerializer? serializer,
  }) {
    serializer ??= driftRuntimeOptions.defaultSerializer;
    return LessonProgress(
      studentId: serializer.fromJson<String>(json['studentId']),
      lessonId: serializer.fromJson<String>(json['lessonId']),
      lessonVersion: serializer.fromJson<int>(json['lessonVersion']),
      nextStep: serializer.fromJson<int>(json['nextStep']),
      completed: serializer.fromJson<bool>(json['completed']),
      updatedAt: serializer.fromJson<DateTime>(json['updatedAt']),
    );
  }
  @override
  Map<String, dynamic> toJson({ValueSerializer? serializer}) {
    serializer ??= driftRuntimeOptions.defaultSerializer;
    return <String, dynamic>{
      'studentId': serializer.toJson<String>(studentId),
      'lessonId': serializer.toJson<String>(lessonId),
      'lessonVersion': serializer.toJson<int>(lessonVersion),
      'nextStep': serializer.toJson<int>(nextStep),
      'completed': serializer.toJson<bool>(completed),
      'updatedAt': serializer.toJson<DateTime>(updatedAt),
    };
  }

  LessonProgress copyWith({
    String? studentId,
    String? lessonId,
    int? lessonVersion,
    int? nextStep,
    bool? completed,
    DateTime? updatedAt,
  }) => LessonProgress(
    studentId: studentId ?? this.studentId,
    lessonId: lessonId ?? this.lessonId,
    lessonVersion: lessonVersion ?? this.lessonVersion,
    nextStep: nextStep ?? this.nextStep,
    completed: completed ?? this.completed,
    updatedAt: updatedAt ?? this.updatedAt,
  );
  LessonProgress copyWithCompanion(LessonProgressTableCompanion data) {
    return LessonProgress(
      studentId: data.studentId.present ? data.studentId.value : this.studentId,
      lessonId: data.lessonId.present ? data.lessonId.value : this.lessonId,
      lessonVersion: data.lessonVersion.present
          ? data.lessonVersion.value
          : this.lessonVersion,
      nextStep: data.nextStep.present ? data.nextStep.value : this.nextStep,
      completed: data.completed.present ? data.completed.value : this.completed,
      updatedAt: data.updatedAt.present ? data.updatedAt.value : this.updatedAt,
    );
  }

  @override
  String toString() {
    return (StringBuffer('LessonProgress(')
          ..write('studentId: $studentId, ')
          ..write('lessonId: $lessonId, ')
          ..write('lessonVersion: $lessonVersion, ')
          ..write('nextStep: $nextStep, ')
          ..write('completed: $completed, ')
          ..write('updatedAt: $updatedAt')
          ..write(')'))
        .toString();
  }

  @override
  int get hashCode => Object.hash(
    studentId,
    lessonId,
    lessonVersion,
    nextStep,
    completed,
    updatedAt,
  );
  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      (other is LessonProgress &&
          other.studentId == this.studentId &&
          other.lessonId == this.lessonId &&
          other.lessonVersion == this.lessonVersion &&
          other.nextStep == this.nextStep &&
          other.completed == this.completed &&
          other.updatedAt == this.updatedAt);
}

class LessonProgressTableCompanion extends UpdateCompanion<LessonProgress> {
  final Value<String> studentId;
  final Value<String> lessonId;
  final Value<int> lessonVersion;
  final Value<int> nextStep;
  final Value<bool> completed;
  final Value<DateTime> updatedAt;
  final Value<int> rowid;
  const LessonProgressTableCompanion({
    this.studentId = const Value.absent(),
    this.lessonId = const Value.absent(),
    this.lessonVersion = const Value.absent(),
    this.nextStep = const Value.absent(),
    this.completed = const Value.absent(),
    this.updatedAt = const Value.absent(),
    this.rowid = const Value.absent(),
  });
  LessonProgressTableCompanion.insert({
    required String studentId,
    required String lessonId,
    required int lessonVersion,
    required int nextStep,
    required bool completed,
    required DateTime updatedAt,
    this.rowid = const Value.absent(),
  }) : studentId = Value(studentId),
       lessonId = Value(lessonId),
       lessonVersion = Value(lessonVersion),
       nextStep = Value(nextStep),
       completed = Value(completed),
       updatedAt = Value(updatedAt);
  static Insertable<LessonProgress> custom({
    Expression<String>? studentId,
    Expression<String>? lessonId,
    Expression<int>? lessonVersion,
    Expression<int>? nextStep,
    Expression<bool>? completed,
    Expression<DateTime>? updatedAt,
    Expression<int>? rowid,
  }) {
    return RawValuesInsertable({
      if (studentId != null) 'student_id': studentId,
      if (lessonId != null) 'lesson_id': lessonId,
      if (lessonVersion != null) 'lesson_version': lessonVersion,
      if (nextStep != null) 'next_step': nextStep,
      if (completed != null) 'completed': completed,
      if (updatedAt != null) 'updated_at': updatedAt,
      if (rowid != null) 'rowid': rowid,
    });
  }

  LessonProgressTableCompanion copyWith({
    Value<String>? studentId,
    Value<String>? lessonId,
    Value<int>? lessonVersion,
    Value<int>? nextStep,
    Value<bool>? completed,
    Value<DateTime>? updatedAt,
    Value<int>? rowid,
  }) {
    return LessonProgressTableCompanion(
      studentId: studentId ?? this.studentId,
      lessonId: lessonId ?? this.lessonId,
      lessonVersion: lessonVersion ?? this.lessonVersion,
      nextStep: nextStep ?? this.nextStep,
      completed: completed ?? this.completed,
      updatedAt: updatedAt ?? this.updatedAt,
      rowid: rowid ?? this.rowid,
    );
  }

  @override
  Map<String, Expression> toColumns(bool nullToAbsent) {
    final map = <String, Expression>{};
    if (studentId.present) {
      map['student_id'] = Variable<String>(studentId.value);
    }
    if (lessonId.present) {
      map['lesson_id'] = Variable<String>(lessonId.value);
    }
    if (lessonVersion.present) {
      map['lesson_version'] = Variable<int>(lessonVersion.value);
    }
    if (nextStep.present) {
      map['next_step'] = Variable<int>(nextStep.value);
    }
    if (completed.present) {
      map['completed'] = Variable<bool>(completed.value);
    }
    if (updatedAt.present) {
      map['updated_at'] = Variable<DateTime>(updatedAt.value);
    }
    if (rowid.present) {
      map['rowid'] = Variable<int>(rowid.value);
    }
    return map;
  }

  @override
  String toString() {
    return (StringBuffer('LessonProgressTableCompanion(')
          ..write('studentId: $studentId, ')
          ..write('lessonId: $lessonId, ')
          ..write('lessonVersion: $lessonVersion, ')
          ..write('nextStep: $nextStep, ')
          ..write('completed: $completed, ')
          ..write('updatedAt: $updatedAt, ')
          ..write('rowid: $rowid')
          ..write(')'))
        .toString();
  }
}

class $StepResultsTable extends StepResults
    with TableInfo<$StepResultsTable, StepResultRow> {
  @override
  final GeneratedDatabase attachedDatabase;
  final String? _alias;
  $StepResultsTable(this.attachedDatabase, [this._alias]);
  static const VerificationMeta _studentIdMeta = const VerificationMeta(
    'studentId',
  );
  @override
  late final GeneratedColumn<String> studentId = GeneratedColumn<String>(
    'student_id',
    aliasedName,
    false,
    type: DriftSqlType.string,
    requiredDuringInsert: true,
    defaultConstraints: GeneratedColumn.constraintIsAlways(
      'REFERENCES students (id)',
    ),
  );
  static const VerificationMeta _lessonIdMeta = const VerificationMeta(
    'lessonId',
  );
  @override
  late final GeneratedColumn<String> lessonId = GeneratedColumn<String>(
    'lesson_id',
    aliasedName,
    false,
    type: DriftSqlType.string,
    requiredDuringInsert: true,
  );
  static const VerificationMeta _stepIdMeta = const VerificationMeta('stepId');
  @override
  late final GeneratedColumn<String> stepId = GeneratedColumn<String>(
    'step_id',
    aliasedName,
    false,
    type: DriftSqlType.string,
    requiredDuringInsert: true,
  );
  static const VerificationMeta _correctMeta = const VerificationMeta(
    'correct',
  );
  @override
  late final GeneratedColumn<bool> correct = GeneratedColumn<bool>(
    'correct',
    aliasedName,
    true,
    type: DriftSqlType.bool,
    requiredDuringInsert: false,
    defaultConstraints: GeneratedColumn.constraintIsAlways(
      'CHECK ("correct" IN (0, 1))',
    ),
  );
  static const VerificationMeta _attemptsMeta = const VerificationMeta(
    'attempts',
  );
  @override
  late final GeneratedColumn<int> attempts = GeneratedColumn<int>(
    'attempts',
    aliasedName,
    false,
    type: DriftSqlType.int,
    requiredDuringInsert: true,
  );
  static const VerificationMeta _misconceptionsMeta = const VerificationMeta(
    'misconceptions',
  );
  @override
  late final GeneratedColumn<String> misconceptions = GeneratedColumn<String>(
    'misconceptions',
    aliasedName,
    false,
    type: DriftSqlType.string,
    requiredDuringInsert: false,
    defaultValue: const Constant('[]'),
  );
  static const VerificationMeta _answeredAtMeta = const VerificationMeta(
    'answeredAt',
  );
  @override
  late final GeneratedColumn<DateTime> answeredAt = GeneratedColumn<DateTime>(
    'answered_at',
    aliasedName,
    false,
    type: DriftSqlType.dateTime,
    requiredDuringInsert: true,
  );
  static const VerificationMeta _syncedMeta = const VerificationMeta('synced');
  @override
  late final GeneratedColumn<bool> synced = GeneratedColumn<bool>(
    'synced',
    aliasedName,
    false,
    type: DriftSqlType.bool,
    requiredDuringInsert: false,
    defaultConstraints: GeneratedColumn.constraintIsAlways(
      'CHECK ("synced" IN (0, 1))',
    ),
    defaultValue: const Constant(false),
  );
  @override
  List<GeneratedColumn> get $columns => [
    studentId,
    lessonId,
    stepId,
    correct,
    attempts,
    misconceptions,
    answeredAt,
    synced,
  ];
  @override
  String get aliasedName => _alias ?? actualTableName;
  @override
  String get actualTableName => $name;
  static const String $name = 'step_results';
  @override
  VerificationContext validateIntegrity(
    Insertable<StepResultRow> instance, {
    bool isInserting = false,
  }) {
    final context = VerificationContext();
    final data = instance.toColumns(true);
    if (data.containsKey('student_id')) {
      context.handle(
        _studentIdMeta,
        studentId.isAcceptableOrUnknown(data['student_id']!, _studentIdMeta),
      );
    } else if (isInserting) {
      context.missing(_studentIdMeta);
    }
    if (data.containsKey('lesson_id')) {
      context.handle(
        _lessonIdMeta,
        lessonId.isAcceptableOrUnknown(data['lesson_id']!, _lessonIdMeta),
      );
    } else if (isInserting) {
      context.missing(_lessonIdMeta);
    }
    if (data.containsKey('step_id')) {
      context.handle(
        _stepIdMeta,
        stepId.isAcceptableOrUnknown(data['step_id']!, _stepIdMeta),
      );
    } else if (isInserting) {
      context.missing(_stepIdMeta);
    }
    if (data.containsKey('correct')) {
      context.handle(
        _correctMeta,
        correct.isAcceptableOrUnknown(data['correct']!, _correctMeta),
      );
    }
    if (data.containsKey('attempts')) {
      context.handle(
        _attemptsMeta,
        attempts.isAcceptableOrUnknown(data['attempts']!, _attemptsMeta),
      );
    } else if (isInserting) {
      context.missing(_attemptsMeta);
    }
    if (data.containsKey('misconceptions')) {
      context.handle(
        _misconceptionsMeta,
        misconceptions.isAcceptableOrUnknown(
          data['misconceptions']!,
          _misconceptionsMeta,
        ),
      );
    }
    if (data.containsKey('answered_at')) {
      context.handle(
        _answeredAtMeta,
        answeredAt.isAcceptableOrUnknown(data['answered_at']!, _answeredAtMeta),
      );
    } else if (isInserting) {
      context.missing(_answeredAtMeta);
    }
    if (data.containsKey('synced')) {
      context.handle(
        _syncedMeta,
        synced.isAcceptableOrUnknown(data['synced']!, _syncedMeta),
      );
    }
    return context;
  }

  @override
  Set<GeneratedColumn> get $primaryKey => {studentId, lessonId, stepId};
  @override
  StepResultRow map(Map<String, dynamic> data, {String? tablePrefix}) {
    final effectivePrefix = tablePrefix != null ? '$tablePrefix.' : '';
    return StepResultRow(
      studentId: attachedDatabase.typeMapping.read(
        DriftSqlType.string,
        data['${effectivePrefix}student_id'],
      )!,
      lessonId: attachedDatabase.typeMapping.read(
        DriftSqlType.string,
        data['${effectivePrefix}lesson_id'],
      )!,
      stepId: attachedDatabase.typeMapping.read(
        DriftSqlType.string,
        data['${effectivePrefix}step_id'],
      )!,
      correct: attachedDatabase.typeMapping.read(
        DriftSqlType.bool,
        data['${effectivePrefix}correct'],
      ),
      attempts: attachedDatabase.typeMapping.read(
        DriftSqlType.int,
        data['${effectivePrefix}attempts'],
      )!,
      misconceptions: attachedDatabase.typeMapping.read(
        DriftSqlType.string,
        data['${effectivePrefix}misconceptions'],
      )!,
      answeredAt: attachedDatabase.typeMapping.read(
        DriftSqlType.dateTime,
        data['${effectivePrefix}answered_at'],
      )!,
      synced: attachedDatabase.typeMapping.read(
        DriftSqlType.bool,
        data['${effectivePrefix}synced'],
      )!,
    );
  }

  @override
  $StepResultsTable createAlias(String alias) {
    return $StepResultsTable(attachedDatabase, alias);
  }
}

class StepResultRow extends DataClass implements Insertable<StepResultRow> {
  final String studentId;
  final String lessonId;
  final String stepId;

  /// null for steps without a question.
  final bool? correct;
  final int attempts;

  /// JSON list of misconception ids.
  final String misconceptions;
  final DateTime answeredAt;
  final bool synced;
  const StepResultRow({
    required this.studentId,
    required this.lessonId,
    required this.stepId,
    this.correct,
    required this.attempts,
    required this.misconceptions,
    required this.answeredAt,
    required this.synced,
  });
  @override
  Map<String, Expression> toColumns(bool nullToAbsent) {
    final map = <String, Expression>{};
    map['student_id'] = Variable<String>(studentId);
    map['lesson_id'] = Variable<String>(lessonId);
    map['step_id'] = Variable<String>(stepId);
    if (!nullToAbsent || correct != null) {
      map['correct'] = Variable<bool>(correct);
    }
    map['attempts'] = Variable<int>(attempts);
    map['misconceptions'] = Variable<String>(misconceptions);
    map['answered_at'] = Variable<DateTime>(answeredAt);
    map['synced'] = Variable<bool>(synced);
    return map;
  }

  StepResultsCompanion toCompanion(bool nullToAbsent) {
    return StepResultsCompanion(
      studentId: Value(studentId),
      lessonId: Value(lessonId),
      stepId: Value(stepId),
      correct: correct == null && nullToAbsent
          ? const Value.absent()
          : Value(correct),
      attempts: Value(attempts),
      misconceptions: Value(misconceptions),
      answeredAt: Value(answeredAt),
      synced: Value(synced),
    );
  }

  factory StepResultRow.fromJson(
    Map<String, dynamic> json, {
    ValueSerializer? serializer,
  }) {
    serializer ??= driftRuntimeOptions.defaultSerializer;
    return StepResultRow(
      studentId: serializer.fromJson<String>(json['studentId']),
      lessonId: serializer.fromJson<String>(json['lessonId']),
      stepId: serializer.fromJson<String>(json['stepId']),
      correct: serializer.fromJson<bool?>(json['correct']),
      attempts: serializer.fromJson<int>(json['attempts']),
      misconceptions: serializer.fromJson<String>(json['misconceptions']),
      answeredAt: serializer.fromJson<DateTime>(json['answeredAt']),
      synced: serializer.fromJson<bool>(json['synced']),
    );
  }
  @override
  Map<String, dynamic> toJson({ValueSerializer? serializer}) {
    serializer ??= driftRuntimeOptions.defaultSerializer;
    return <String, dynamic>{
      'studentId': serializer.toJson<String>(studentId),
      'lessonId': serializer.toJson<String>(lessonId),
      'stepId': serializer.toJson<String>(stepId),
      'correct': serializer.toJson<bool?>(correct),
      'attempts': serializer.toJson<int>(attempts),
      'misconceptions': serializer.toJson<String>(misconceptions),
      'answeredAt': serializer.toJson<DateTime>(answeredAt),
      'synced': serializer.toJson<bool>(synced),
    };
  }

  StepResultRow copyWith({
    String? studentId,
    String? lessonId,
    String? stepId,
    Value<bool?> correct = const Value.absent(),
    int? attempts,
    String? misconceptions,
    DateTime? answeredAt,
    bool? synced,
  }) => StepResultRow(
    studentId: studentId ?? this.studentId,
    lessonId: lessonId ?? this.lessonId,
    stepId: stepId ?? this.stepId,
    correct: correct.present ? correct.value : this.correct,
    attempts: attempts ?? this.attempts,
    misconceptions: misconceptions ?? this.misconceptions,
    answeredAt: answeredAt ?? this.answeredAt,
    synced: synced ?? this.synced,
  );
  StepResultRow copyWithCompanion(StepResultsCompanion data) {
    return StepResultRow(
      studentId: data.studentId.present ? data.studentId.value : this.studentId,
      lessonId: data.lessonId.present ? data.lessonId.value : this.lessonId,
      stepId: data.stepId.present ? data.stepId.value : this.stepId,
      correct: data.correct.present ? data.correct.value : this.correct,
      attempts: data.attempts.present ? data.attempts.value : this.attempts,
      misconceptions: data.misconceptions.present
          ? data.misconceptions.value
          : this.misconceptions,
      answeredAt: data.answeredAt.present
          ? data.answeredAt.value
          : this.answeredAt,
      synced: data.synced.present ? data.synced.value : this.synced,
    );
  }

  @override
  String toString() {
    return (StringBuffer('StepResultRow(')
          ..write('studentId: $studentId, ')
          ..write('lessonId: $lessonId, ')
          ..write('stepId: $stepId, ')
          ..write('correct: $correct, ')
          ..write('attempts: $attempts, ')
          ..write('misconceptions: $misconceptions, ')
          ..write('answeredAt: $answeredAt, ')
          ..write('synced: $synced')
          ..write(')'))
        .toString();
  }

  @override
  int get hashCode => Object.hash(
    studentId,
    lessonId,
    stepId,
    correct,
    attempts,
    misconceptions,
    answeredAt,
    synced,
  );
  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      (other is StepResultRow &&
          other.studentId == this.studentId &&
          other.lessonId == this.lessonId &&
          other.stepId == this.stepId &&
          other.correct == this.correct &&
          other.attempts == this.attempts &&
          other.misconceptions == this.misconceptions &&
          other.answeredAt == this.answeredAt &&
          other.synced == this.synced);
}

class StepResultsCompanion extends UpdateCompanion<StepResultRow> {
  final Value<String> studentId;
  final Value<String> lessonId;
  final Value<String> stepId;
  final Value<bool?> correct;
  final Value<int> attempts;
  final Value<String> misconceptions;
  final Value<DateTime> answeredAt;
  final Value<bool> synced;
  final Value<int> rowid;
  const StepResultsCompanion({
    this.studentId = const Value.absent(),
    this.lessonId = const Value.absent(),
    this.stepId = const Value.absent(),
    this.correct = const Value.absent(),
    this.attempts = const Value.absent(),
    this.misconceptions = const Value.absent(),
    this.answeredAt = const Value.absent(),
    this.synced = const Value.absent(),
    this.rowid = const Value.absent(),
  });
  StepResultsCompanion.insert({
    required String studentId,
    required String lessonId,
    required String stepId,
    this.correct = const Value.absent(),
    required int attempts,
    this.misconceptions = const Value.absent(),
    required DateTime answeredAt,
    this.synced = const Value.absent(),
    this.rowid = const Value.absent(),
  }) : studentId = Value(studentId),
       lessonId = Value(lessonId),
       stepId = Value(stepId),
       attempts = Value(attempts),
       answeredAt = Value(answeredAt);
  static Insertable<StepResultRow> custom({
    Expression<String>? studentId,
    Expression<String>? lessonId,
    Expression<String>? stepId,
    Expression<bool>? correct,
    Expression<int>? attempts,
    Expression<String>? misconceptions,
    Expression<DateTime>? answeredAt,
    Expression<bool>? synced,
    Expression<int>? rowid,
  }) {
    return RawValuesInsertable({
      if (studentId != null) 'student_id': studentId,
      if (lessonId != null) 'lesson_id': lessonId,
      if (stepId != null) 'step_id': stepId,
      if (correct != null) 'correct': correct,
      if (attempts != null) 'attempts': attempts,
      if (misconceptions != null) 'misconceptions': misconceptions,
      if (answeredAt != null) 'answered_at': answeredAt,
      if (synced != null) 'synced': synced,
      if (rowid != null) 'rowid': rowid,
    });
  }

  StepResultsCompanion copyWith({
    Value<String>? studentId,
    Value<String>? lessonId,
    Value<String>? stepId,
    Value<bool?>? correct,
    Value<int>? attempts,
    Value<String>? misconceptions,
    Value<DateTime>? answeredAt,
    Value<bool>? synced,
    Value<int>? rowid,
  }) {
    return StepResultsCompanion(
      studentId: studentId ?? this.studentId,
      lessonId: lessonId ?? this.lessonId,
      stepId: stepId ?? this.stepId,
      correct: correct ?? this.correct,
      attempts: attempts ?? this.attempts,
      misconceptions: misconceptions ?? this.misconceptions,
      answeredAt: answeredAt ?? this.answeredAt,
      synced: synced ?? this.synced,
      rowid: rowid ?? this.rowid,
    );
  }

  @override
  Map<String, Expression> toColumns(bool nullToAbsent) {
    final map = <String, Expression>{};
    if (studentId.present) {
      map['student_id'] = Variable<String>(studentId.value);
    }
    if (lessonId.present) {
      map['lesson_id'] = Variable<String>(lessonId.value);
    }
    if (stepId.present) {
      map['step_id'] = Variable<String>(stepId.value);
    }
    if (correct.present) {
      map['correct'] = Variable<bool>(correct.value);
    }
    if (attempts.present) {
      map['attempts'] = Variable<int>(attempts.value);
    }
    if (misconceptions.present) {
      map['misconceptions'] = Variable<String>(misconceptions.value);
    }
    if (answeredAt.present) {
      map['answered_at'] = Variable<DateTime>(answeredAt.value);
    }
    if (synced.present) {
      map['synced'] = Variable<bool>(synced.value);
    }
    if (rowid.present) {
      map['rowid'] = Variable<int>(rowid.value);
    }
    return map;
  }

  @override
  String toString() {
    return (StringBuffer('StepResultsCompanion(')
          ..write('studentId: $studentId, ')
          ..write('lessonId: $lessonId, ')
          ..write('stepId: $stepId, ')
          ..write('correct: $correct, ')
          ..write('attempts: $attempts, ')
          ..write('misconceptions: $misconceptions, ')
          ..write('answeredAt: $answeredAt, ')
          ..write('synced: $synced, ')
          ..write('rowid: $rowid')
          ..write(')'))
        .toString();
  }
}

class $SkillStatesTable extends SkillStates
    with TableInfo<$SkillStatesTable, SkillStateRow> {
  @override
  final GeneratedDatabase attachedDatabase;
  final String? _alias;
  $SkillStatesTable(this.attachedDatabase, [this._alias]);
  static const VerificationMeta _studentIdMeta = const VerificationMeta(
    'studentId',
  );
  @override
  late final GeneratedColumn<String> studentId = GeneratedColumn<String>(
    'student_id',
    aliasedName,
    false,
    type: DriftSqlType.string,
    requiredDuringInsert: true,
    defaultConstraints: GeneratedColumn.constraintIsAlways(
      'REFERENCES students (id)',
    ),
  );
  static const VerificationMeta _skillMeta = const VerificationMeta('skill');
  @override
  late final GeneratedColumn<String> skill = GeneratedColumn<String>(
    'skill',
    aliasedName,
    false,
    type: DriftSqlType.string,
    requiredDuringInsert: true,
  );
  static const VerificationMeta _dataMeta = const VerificationMeta('data');
  @override
  late final GeneratedColumn<String> data = GeneratedColumn<String>(
    'data',
    aliasedName,
    false,
    type: DriftSqlType.string,
    requiredDuringInsert: true,
  );
  static const VerificationMeta _updatedAtMeta = const VerificationMeta(
    'updatedAt',
  );
  @override
  late final GeneratedColumn<DateTime> updatedAt = GeneratedColumn<DateTime>(
    'updated_at',
    aliasedName,
    false,
    type: DriftSqlType.dateTime,
    requiredDuringInsert: true,
  );
  static const VerificationMeta _syncedMeta = const VerificationMeta('synced');
  @override
  late final GeneratedColumn<bool> synced = GeneratedColumn<bool>(
    'synced',
    aliasedName,
    false,
    type: DriftSqlType.bool,
    requiredDuringInsert: false,
    defaultConstraints: GeneratedColumn.constraintIsAlways(
      'CHECK ("synced" IN (0, 1))',
    ),
    defaultValue: const Constant(false),
  );
  @override
  List<GeneratedColumn> get $columns => [
    studentId,
    skill,
    data,
    updatedAt,
    synced,
  ];
  @override
  String get aliasedName => _alias ?? actualTableName;
  @override
  String get actualTableName => $name;
  static const String $name = 'skill_states';
  @override
  VerificationContext validateIntegrity(
    Insertable<SkillStateRow> instance, {
    bool isInserting = false,
  }) {
    final context = VerificationContext();
    final data = instance.toColumns(true);
    if (data.containsKey('student_id')) {
      context.handle(
        _studentIdMeta,
        studentId.isAcceptableOrUnknown(data['student_id']!, _studentIdMeta),
      );
    } else if (isInserting) {
      context.missing(_studentIdMeta);
    }
    if (data.containsKey('skill')) {
      context.handle(
        _skillMeta,
        skill.isAcceptableOrUnknown(data['skill']!, _skillMeta),
      );
    } else if (isInserting) {
      context.missing(_skillMeta);
    }
    if (data.containsKey('data')) {
      context.handle(
        _dataMeta,
        this.data.isAcceptableOrUnknown(data['data']!, _dataMeta),
      );
    } else if (isInserting) {
      context.missing(_dataMeta);
    }
    if (data.containsKey('updated_at')) {
      context.handle(
        _updatedAtMeta,
        updatedAt.isAcceptableOrUnknown(data['updated_at']!, _updatedAtMeta),
      );
    } else if (isInserting) {
      context.missing(_updatedAtMeta);
    }
    if (data.containsKey('synced')) {
      context.handle(
        _syncedMeta,
        synced.isAcceptableOrUnknown(data['synced']!, _syncedMeta),
      );
    }
    return context;
  }

  @override
  Set<GeneratedColumn> get $primaryKey => {studentId, skill};
  @override
  SkillStateRow map(Map<String, dynamic> data, {String? tablePrefix}) {
    final effectivePrefix = tablePrefix != null ? '$tablePrefix.' : '';
    return SkillStateRow(
      studentId: attachedDatabase.typeMapping.read(
        DriftSqlType.string,
        data['${effectivePrefix}student_id'],
      )!,
      skill: attachedDatabase.typeMapping.read(
        DriftSqlType.string,
        data['${effectivePrefix}skill'],
      )!,
      data: attachedDatabase.typeMapping.read(
        DriftSqlType.string,
        data['${effectivePrefix}data'],
      )!,
      updatedAt: attachedDatabase.typeMapping.read(
        DriftSqlType.dateTime,
        data['${effectivePrefix}updated_at'],
      )!,
      synced: attachedDatabase.typeMapping.read(
        DriftSqlType.bool,
        data['${effectivePrefix}synced'],
      )!,
    );
  }

  @override
  $SkillStatesTable createAlias(String alias) {
    return $SkillStatesTable(attachedDatabase, alias);
  }
}

class SkillStateRow extends DataClass implements Insertable<SkillStateRow> {
  final String studentId;
  final String skill;

  /// [SkillState] as JSON.
  final String data;
  final DateTime updatedAt;
  final bool synced;
  const SkillStateRow({
    required this.studentId,
    required this.skill,
    required this.data,
    required this.updatedAt,
    required this.synced,
  });
  @override
  Map<String, Expression> toColumns(bool nullToAbsent) {
    final map = <String, Expression>{};
    map['student_id'] = Variable<String>(studentId);
    map['skill'] = Variable<String>(skill);
    map['data'] = Variable<String>(data);
    map['updated_at'] = Variable<DateTime>(updatedAt);
    map['synced'] = Variable<bool>(synced);
    return map;
  }

  SkillStatesCompanion toCompanion(bool nullToAbsent) {
    return SkillStatesCompanion(
      studentId: Value(studentId),
      skill: Value(skill),
      data: Value(data),
      updatedAt: Value(updatedAt),
      synced: Value(synced),
    );
  }

  factory SkillStateRow.fromJson(
    Map<String, dynamic> json, {
    ValueSerializer? serializer,
  }) {
    serializer ??= driftRuntimeOptions.defaultSerializer;
    return SkillStateRow(
      studentId: serializer.fromJson<String>(json['studentId']),
      skill: serializer.fromJson<String>(json['skill']),
      data: serializer.fromJson<String>(json['data']),
      updatedAt: serializer.fromJson<DateTime>(json['updatedAt']),
      synced: serializer.fromJson<bool>(json['synced']),
    );
  }
  @override
  Map<String, dynamic> toJson({ValueSerializer? serializer}) {
    serializer ??= driftRuntimeOptions.defaultSerializer;
    return <String, dynamic>{
      'studentId': serializer.toJson<String>(studentId),
      'skill': serializer.toJson<String>(skill),
      'data': serializer.toJson<String>(data),
      'updatedAt': serializer.toJson<DateTime>(updatedAt),
      'synced': serializer.toJson<bool>(synced),
    };
  }

  SkillStateRow copyWith({
    String? studentId,
    String? skill,
    String? data,
    DateTime? updatedAt,
    bool? synced,
  }) => SkillStateRow(
    studentId: studentId ?? this.studentId,
    skill: skill ?? this.skill,
    data: data ?? this.data,
    updatedAt: updatedAt ?? this.updatedAt,
    synced: synced ?? this.synced,
  );
  SkillStateRow copyWithCompanion(SkillStatesCompanion data) {
    return SkillStateRow(
      studentId: data.studentId.present ? data.studentId.value : this.studentId,
      skill: data.skill.present ? data.skill.value : this.skill,
      data: data.data.present ? data.data.value : this.data,
      updatedAt: data.updatedAt.present ? data.updatedAt.value : this.updatedAt,
      synced: data.synced.present ? data.synced.value : this.synced,
    );
  }

  @override
  String toString() {
    return (StringBuffer('SkillStateRow(')
          ..write('studentId: $studentId, ')
          ..write('skill: $skill, ')
          ..write('data: $data, ')
          ..write('updatedAt: $updatedAt, ')
          ..write('synced: $synced')
          ..write(')'))
        .toString();
  }

  @override
  int get hashCode => Object.hash(studentId, skill, data, updatedAt, synced);
  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      (other is SkillStateRow &&
          other.studentId == this.studentId &&
          other.skill == this.skill &&
          other.data == this.data &&
          other.updatedAt == this.updatedAt &&
          other.synced == this.synced);
}

class SkillStatesCompanion extends UpdateCompanion<SkillStateRow> {
  final Value<String> studentId;
  final Value<String> skill;
  final Value<String> data;
  final Value<DateTime> updatedAt;
  final Value<bool> synced;
  final Value<int> rowid;
  const SkillStatesCompanion({
    this.studentId = const Value.absent(),
    this.skill = const Value.absent(),
    this.data = const Value.absent(),
    this.updatedAt = const Value.absent(),
    this.synced = const Value.absent(),
    this.rowid = const Value.absent(),
  });
  SkillStatesCompanion.insert({
    required String studentId,
    required String skill,
    required String data,
    required DateTime updatedAt,
    this.synced = const Value.absent(),
    this.rowid = const Value.absent(),
  }) : studentId = Value(studentId),
       skill = Value(skill),
       data = Value(data),
       updatedAt = Value(updatedAt);
  static Insertable<SkillStateRow> custom({
    Expression<String>? studentId,
    Expression<String>? skill,
    Expression<String>? data,
    Expression<DateTime>? updatedAt,
    Expression<bool>? synced,
    Expression<int>? rowid,
  }) {
    return RawValuesInsertable({
      if (studentId != null) 'student_id': studentId,
      if (skill != null) 'skill': skill,
      if (data != null) 'data': data,
      if (updatedAt != null) 'updated_at': updatedAt,
      if (synced != null) 'synced': synced,
      if (rowid != null) 'rowid': rowid,
    });
  }

  SkillStatesCompanion copyWith({
    Value<String>? studentId,
    Value<String>? skill,
    Value<String>? data,
    Value<DateTime>? updatedAt,
    Value<bool>? synced,
    Value<int>? rowid,
  }) {
    return SkillStatesCompanion(
      studentId: studentId ?? this.studentId,
      skill: skill ?? this.skill,
      data: data ?? this.data,
      updatedAt: updatedAt ?? this.updatedAt,
      synced: synced ?? this.synced,
      rowid: rowid ?? this.rowid,
    );
  }

  @override
  Map<String, Expression> toColumns(bool nullToAbsent) {
    final map = <String, Expression>{};
    if (studentId.present) {
      map['student_id'] = Variable<String>(studentId.value);
    }
    if (skill.present) {
      map['skill'] = Variable<String>(skill.value);
    }
    if (data.present) {
      map['data'] = Variable<String>(data.value);
    }
    if (updatedAt.present) {
      map['updated_at'] = Variable<DateTime>(updatedAt.value);
    }
    if (synced.present) {
      map['synced'] = Variable<bool>(synced.value);
    }
    if (rowid.present) {
      map['rowid'] = Variable<int>(rowid.value);
    }
    return map;
  }

  @override
  String toString() {
    return (StringBuffer('SkillStatesCompanion(')
          ..write('studentId: $studentId, ')
          ..write('skill: $skill, ')
          ..write('data: $data, ')
          ..write('updatedAt: $updatedAt, ')
          ..write('synced: $synced, ')
          ..write('rowid: $rowid')
          ..write(')'))
        .toString();
  }
}

abstract class _$LocalDb extends GeneratedDatabase {
  _$LocalDb(QueryExecutor e) : super(e);
  $LocalDbManager get managers => $LocalDbManager(this);
  late final $StudentsTable students = $StudentsTable(this);
  late final $LessonProgressTableTable lessonProgressTable =
      $LessonProgressTableTable(this);
  late final $StepResultsTable stepResults = $StepResultsTable(this);
  late final $SkillStatesTable skillStates = $SkillStatesTable(this);
  @override
  Iterable<TableInfo<Table, Object?>> get allTables =>
      allSchemaEntities.whereType<TableInfo<Table, Object?>>();
  @override
  List<DatabaseSchemaEntity> get allSchemaEntities => [
    students,
    lessonProgressTable,
    stepResults,
    skillStates,
  ];
}

typedef $$StudentsTableCreateCompanionBuilder = StudentsCompanion Function({
  required String id,
  required String firstName,
  required int grade,
  required String avatar,
  Value<String?> pinHash,
  required DateTime createdAt,
  required DateTime consentAt,
  Value<bool> synced,
  Value<int> rowid,
});
typedef $$StudentsTableUpdateCompanionBuilder = StudentsCompanion Function({
  Value<String> id,
  Value<String> firstName,
  Value<int> grade,
  Value<String> avatar,
  Value<String?> pinHash,
  Value<DateTime> createdAt,
  Value<DateTime> consentAt,
  Value<bool> synced,
  Value<int> rowid,
});

final class $$StudentsTableReferences
    extends BaseReferences<_$LocalDb, $StudentsTable, Student> {
  $$StudentsTableReferences(super.$_db, super.$_table, super.$_typedResult);

  static MultiTypedResultKey<$LessonProgressTableTable, List<LessonProgress>>
  _lessonProgressTableRefsTable(_$LocalDb db) => MultiTypedResultKey.fromTable(
    db.lessonProgressTable,
    aliasName: 'students__id__lesson_progress__student_id',
  );

  $$LessonProgressTableTableProcessedTableManager get lessonProgressTableRefs {
    final manager = $$LessonProgressTableTableTableManager(
      $_db,
      $_db.lessonProgressTable,
    ).filter((f) => f.studentId.id.sqlEquals($_itemColumn<String>('id')!));

    final cache = $_typedResult.readTableOrNull(
      _lessonProgressTableRefsTable($_db),
    );
    return ProcessedTableManager(
      manager.$state.copyWith(prefetchedData: cache),
    );
  }

  static MultiTypedResultKey<$StepResultsTable, List<StepResultRow>>
  _stepResultsRefsTable(_$LocalDb db) => MultiTypedResultKey.fromTable(
    db.stepResults,
    aliasName: 'students__id__step_results__student_id',
  );

  $$StepResultsTableProcessedTableManager get stepResultsRefs {
    final manager = $$StepResultsTableTableManager(
      $_db,
      $_db.stepResults,
    ).filter((f) => f.studentId.id.sqlEquals($_itemColumn<String>('id')!));

    final cache = $_typedResult.readTableOrNull(_stepResultsRefsTable($_db));
    return ProcessedTableManager(
      manager.$state.copyWith(prefetchedData: cache),
    );
  }

  static MultiTypedResultKey<$SkillStatesTable, List<SkillStateRow>>
  _skillStatesRefsTable(_$LocalDb db) => MultiTypedResultKey.fromTable(
    db.skillStates,
    aliasName: 'students__id__skill_states__student_id',
  );

  $$SkillStatesTableProcessedTableManager get skillStatesRefs {
    final manager = $$SkillStatesTableTableManager(
      $_db,
      $_db.skillStates,
    ).filter((f) => f.studentId.id.sqlEquals($_itemColumn<String>('id')!));

    final cache = $_typedResult.readTableOrNull(_skillStatesRefsTable($_db));
    return ProcessedTableManager(
      manager.$state.copyWith(prefetchedData: cache),
    );
  }
}

class $$StudentsTableFilterComposer
    extends Composer<_$LocalDb, $StudentsTable> {
  $$StudentsTableFilterComposer({
    required super.$db,
    required super.$table,
    super.joinBuilder,
    super.$addJoinBuilderToRootComposer,
    super.$removeJoinBuilderFromRootComposer,
  });
  ColumnFilters<String> get id => $composableBuilder(
    column: $table.id,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<String> get firstName => $composableBuilder(
    column: $table.firstName,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<int> get grade => $composableBuilder(
    column: $table.grade,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<String> get avatar => $composableBuilder(
    column: $table.avatar,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<String> get pinHash => $composableBuilder(
    column: $table.pinHash,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<DateTime> get createdAt => $composableBuilder(
    column: $table.createdAt,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<DateTime> get consentAt => $composableBuilder(
    column: $table.consentAt,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<bool> get synced => $composableBuilder(
    column: $table.synced,
    builder: (column) => ColumnFilters(column),
  );

  Expression<bool> lessonProgressTableRefs(
    Expression<bool> Function($$LessonProgressTableTableFilterComposer f) f,
  ) {
    final $$LessonProgressTableTableFilterComposer composer = $composerBuilder(
      composer: this,
      getCurrentColumn: (t) => t.id,
      referencedTable: $db.lessonProgressTable,
      getReferencedColumn: (t) => t.studentId,
      builder:
          (
            joinBuilder, {
            $addJoinBuilderToRootComposer,
            $removeJoinBuilderFromRootComposer,
          }) => $$LessonProgressTableTableFilterComposer(
            $db: $db,
            $table: $db.lessonProgressTable,
            $addJoinBuilderToRootComposer: $addJoinBuilderToRootComposer,
            joinBuilder: joinBuilder,
            $removeJoinBuilderFromRootComposer:
                $removeJoinBuilderFromRootComposer,
          ),
    );
    return f(composer);
  }

  Expression<bool> stepResultsRefs(
    Expression<bool> Function($$StepResultsTableFilterComposer f) f,
  ) {
    final $$StepResultsTableFilterComposer composer = $composerBuilder(
      composer: this,
      getCurrentColumn: (t) => t.id,
      referencedTable: $db.stepResults,
      getReferencedColumn: (t) => t.studentId,
      builder:
          (
            joinBuilder, {
            $addJoinBuilderToRootComposer,
            $removeJoinBuilderFromRootComposer,
          }) => $$StepResultsTableFilterComposer(
            $db: $db,
            $table: $db.stepResults,
            $addJoinBuilderToRootComposer: $addJoinBuilderToRootComposer,
            joinBuilder: joinBuilder,
            $removeJoinBuilderFromRootComposer:
                $removeJoinBuilderFromRootComposer,
          ),
    );
    return f(composer);
  }

  Expression<bool> skillStatesRefs(
    Expression<bool> Function($$SkillStatesTableFilterComposer f) f,
  ) {
    final $$SkillStatesTableFilterComposer composer = $composerBuilder(
      composer: this,
      getCurrentColumn: (t) => t.id,
      referencedTable: $db.skillStates,
      getReferencedColumn: (t) => t.studentId,
      builder:
          (
            joinBuilder, {
            $addJoinBuilderToRootComposer,
            $removeJoinBuilderFromRootComposer,
          }) => $$SkillStatesTableFilterComposer(
            $db: $db,
            $table: $db.skillStates,
            $addJoinBuilderToRootComposer: $addJoinBuilderToRootComposer,
            joinBuilder: joinBuilder,
            $removeJoinBuilderFromRootComposer:
                $removeJoinBuilderFromRootComposer,
          ),
    );
    return f(composer);
  }
}

class $$StudentsTableOrderingComposer
    extends Composer<_$LocalDb, $StudentsTable> {
  $$StudentsTableOrderingComposer({
    required super.$db,
    required super.$table,
    super.joinBuilder,
    super.$addJoinBuilderToRootComposer,
    super.$removeJoinBuilderFromRootComposer,
  });
  ColumnOrderings<String> get id => $composableBuilder(
    column: $table.id,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<String> get firstName => $composableBuilder(
    column: $table.firstName,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<int> get grade => $composableBuilder(
    column: $table.grade,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<String> get avatar => $composableBuilder(
    column: $table.avatar,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<String> get pinHash => $composableBuilder(
    column: $table.pinHash,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<DateTime> get createdAt => $composableBuilder(
    column: $table.createdAt,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<DateTime> get consentAt => $composableBuilder(
    column: $table.consentAt,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<bool> get synced => $composableBuilder(
    column: $table.synced,
    builder: (column) => ColumnOrderings(column),
  );
}

class $$StudentsTableAnnotationComposer
    extends Composer<_$LocalDb, $StudentsTable> {
  $$StudentsTableAnnotationComposer({
    required super.$db,
    required super.$table,
    super.joinBuilder,
    super.$addJoinBuilderToRootComposer,
    super.$removeJoinBuilderFromRootComposer,
  });
  GeneratedColumn<String> get id =>
      $composableBuilder(column: $table.id, builder: (column) => column);

  GeneratedColumn<String> get firstName =>
      $composableBuilder(column: $table.firstName, builder: (column) => column);

  GeneratedColumn<int> get grade =>
      $composableBuilder(column: $table.grade, builder: (column) => column);

  GeneratedColumn<String> get avatar =>
      $composableBuilder(column: $table.avatar, builder: (column) => column);

  GeneratedColumn<String> get pinHash =>
      $composableBuilder(column: $table.pinHash, builder: (column) => column);

  GeneratedColumn<DateTime> get createdAt =>
      $composableBuilder(column: $table.createdAt, builder: (column) => column);

  GeneratedColumn<DateTime> get consentAt =>
      $composableBuilder(column: $table.consentAt, builder: (column) => column);

  GeneratedColumn<bool> get synced =>
      $composableBuilder(column: $table.synced, builder: (column) => column);

  Expression<T> lessonProgressTableRefs<T extends Object>(
    Expression<T> Function($$LessonProgressTableTableAnnotationComposer a) f,
  ) {
    final $$LessonProgressTableTableAnnotationComposer composer =
        $composerBuilder(
          composer: this,
          getCurrentColumn: (t) => t.id,
          referencedTable: $db.lessonProgressTable,
          getReferencedColumn: (t) => t.studentId,
          builder:
              (
                joinBuilder, {
                $addJoinBuilderToRootComposer,
                $removeJoinBuilderFromRootComposer,
              }) => $$LessonProgressTableTableAnnotationComposer(
                $db: $db,
                $table: $db.lessonProgressTable,
                $addJoinBuilderToRootComposer: $addJoinBuilderToRootComposer,
                joinBuilder: joinBuilder,
                $removeJoinBuilderFromRootComposer:
                    $removeJoinBuilderFromRootComposer,
              ),
        );
    return f(composer);
  }

  Expression<T> stepResultsRefs<T extends Object>(
    Expression<T> Function($$StepResultsTableAnnotationComposer a) f,
  ) {
    final $$StepResultsTableAnnotationComposer composer = $composerBuilder(
      composer: this,
      getCurrentColumn: (t) => t.id,
      referencedTable: $db.stepResults,
      getReferencedColumn: (t) => t.studentId,
      builder:
          (
            joinBuilder, {
            $addJoinBuilderToRootComposer,
            $removeJoinBuilderFromRootComposer,
          }) => $$StepResultsTableAnnotationComposer(
            $db: $db,
            $table: $db.stepResults,
            $addJoinBuilderToRootComposer: $addJoinBuilderToRootComposer,
            joinBuilder: joinBuilder,
            $removeJoinBuilderFromRootComposer:
                $removeJoinBuilderFromRootComposer,
          ),
    );
    return f(composer);
  }

  Expression<T> skillStatesRefs<T extends Object>(
    Expression<T> Function($$SkillStatesTableAnnotationComposer a) f,
  ) {
    final $$SkillStatesTableAnnotationComposer composer = $composerBuilder(
      composer: this,
      getCurrentColumn: (t) => t.id,
      referencedTable: $db.skillStates,
      getReferencedColumn: (t) => t.studentId,
      builder:
          (
            joinBuilder, {
            $addJoinBuilderToRootComposer,
            $removeJoinBuilderFromRootComposer,
          }) => $$SkillStatesTableAnnotationComposer(
            $db: $db,
            $table: $db.skillStates,
            $addJoinBuilderToRootComposer: $addJoinBuilderToRootComposer,
            joinBuilder: joinBuilder,
            $removeJoinBuilderFromRootComposer:
                $removeJoinBuilderFromRootComposer,
          ),
    );
    return f(composer);
  }
}

class $$StudentsTableTableManager
    extends
        RootTableManager<
          _$LocalDb,
          $StudentsTable,
          Student,
          $$StudentsTableFilterComposer,
          $$StudentsTableOrderingComposer,
          $$StudentsTableAnnotationComposer,
          $$StudentsTableCreateCompanionBuilder,
          $$StudentsTableUpdateCompanionBuilder,
          (Student, $$StudentsTableReferences),
          Student,
          PrefetchHooks Function({
            bool lessonProgressTableRefs,
            bool stepResultsRefs,
            bool skillStatesRefs,
          })
        > {
  $$StudentsTableTableManager(_$LocalDb db, $StudentsTable table)
    : super(
        TableManagerState(
          db: db,
          table: table,
          createFilteringComposer: () =>
              $$StudentsTableFilterComposer($db: db, $table: table),
          createOrderingComposer: () =>
              $$StudentsTableOrderingComposer($db: db, $table: table),
          createComputedFieldComposer: () =>
              $$StudentsTableAnnotationComposer($db: db, $table: table),
          updateCompanionCallback:
              ({
                Value<String> id = const Value.absent(),
                Value<String> firstName = const Value.absent(),
                Value<int> grade = const Value.absent(),
                Value<String> avatar = const Value.absent(),
                Value<String?> pinHash = const Value.absent(),
                Value<DateTime> createdAt = const Value.absent(),
                Value<DateTime> consentAt = const Value.absent(),
                Value<bool> synced = const Value.absent(),
                Value<int> rowid = const Value.absent(),
              }) => StudentsCompanion(
                id: id,
                firstName: firstName,
                grade: grade,
                avatar: avatar,
                pinHash: pinHash,
                createdAt: createdAt,
                consentAt: consentAt,
                synced: synced,
                rowid: rowid,
              ),
          createCompanionCallback:
              ({
                required String id,
                required String firstName,
                required int grade,
                required String avatar,
                Value<String?> pinHash = const Value.absent(),
                required DateTime createdAt,
                required DateTime consentAt,
                Value<bool> synced = const Value.absent(),
                Value<int> rowid = const Value.absent(),
              }) => StudentsCompanion.insert(
                id: id,
                firstName: firstName,
                grade: grade,
                avatar: avatar,
                pinHash: pinHash,
                createdAt: createdAt,
                consentAt: consentAt,
                synced: synced,
                rowid: rowid,
              ),
          withReferenceMapper: (p0) => p0
              .map(
                (e) => (
                  e.readTable<$StudentsTable, Student>(table),
                  $$StudentsTableReferences(db, table, e),
                ),
              )
              .toList(),
          prefetchHooksCallback:
              ({
                lessonProgressTableRefs = false,
                stepResultsRefs = false,
                skillStatesRefs = false,
              }) {
                return PrefetchHooks(
                  db: db,
                  explicitlyWatchedTables: [
                    if (lessonProgressTableRefs) db.lessonProgressTable,
                    if (stepResultsRefs) db.stepResults,
                    if (skillStatesRefs) db.skillStates,
                  ],
                  addJoins: null,
                  getPrefetchedDataCallback: (items) async {
                    return [
                      if (lessonProgressTableRefs)
                        await $_getPrefetchedData<
                          Student,
                          $StudentsTable,
                          LessonProgress
                        >(
                          currentTable: table,
                          referencedTable: $$StudentsTableReferences
                              ._lessonProgressTableRefsTable(db),
                          managerFromTypedResult: (p0) =>
                              $$StudentsTableReferences(
                                db,
                                table,
                                p0,
                              ).lessonProgressTableRefs,
                          referencedItemsForCurrentItem:
                              (item, referencedItems) => referencedItems.where(
                                (e) => e.studentId == item.id,
                              ),
                          typedResults: items,
                        ),
                      if (stepResultsRefs)
                        await $_getPrefetchedData<
                          Student,
                          $StudentsTable,
                          StepResultRow
                        >(
                          currentTable: table,
                          referencedTable: $$StudentsTableReferences
                              ._stepResultsRefsTable(db),
                          managerFromTypedResult: (p0) =>
                              $$StudentsTableReferences(
                                db,
                                table,
                                p0,
                              ).stepResultsRefs,
                          referencedItemsForCurrentItem:
                              (item, referencedItems) => referencedItems.where(
                                (e) => e.studentId == item.id,
                              ),
                          typedResults: items,
                        ),
                      if (skillStatesRefs)
                        await $_getPrefetchedData<
                          Student,
                          $StudentsTable,
                          SkillStateRow
                        >(
                          currentTable: table,
                          referencedTable: $$StudentsTableReferences
                              ._skillStatesRefsTable(db),
                          managerFromTypedResult: (p0) =>
                              $$StudentsTableReferences(
                                db,
                                table,
                                p0,
                              ).skillStatesRefs,
                          referencedItemsForCurrentItem:
                              (item, referencedItems) => referencedItems.where(
                                (e) => e.studentId == item.id,
                              ),
                          typedResults: items,
                        ),
                    ];
                  },
                );
              },
        ),
      );
}

typedef $$StudentsTableProcessedTableManager =
    ProcessedTableManager<
      _$LocalDb,
      $StudentsTable,
      Student,
      $$StudentsTableFilterComposer,
      $$StudentsTableOrderingComposer,
      $$StudentsTableAnnotationComposer,
      $$StudentsTableCreateCompanionBuilder,
      $$StudentsTableUpdateCompanionBuilder,
      (Student, $$StudentsTableReferences),
      Student,
      PrefetchHooks Function({
        bool lessonProgressTableRefs,
        bool stepResultsRefs,
        bool skillStatesRefs,
      })
    >;
typedef $$LessonProgressTableTableCreateCompanionBuilder =
    LessonProgressTableCompanion Function({
      required String studentId,
      required String lessonId,
      required int lessonVersion,
      required int nextStep,
      required bool completed,
      required DateTime updatedAt,
      Value<int> rowid,
    });
typedef $$LessonProgressTableTableUpdateCompanionBuilder =
    LessonProgressTableCompanion Function({
      Value<String> studentId,
      Value<String> lessonId,
      Value<int> lessonVersion,
      Value<int> nextStep,
      Value<bool> completed,
      Value<DateTime> updatedAt,
      Value<int> rowid,
    });

final class $$LessonProgressTableTableReferences
    extends
        BaseReferences<_$LocalDb, $LessonProgressTableTable, LessonProgress> {
  $$LessonProgressTableTableReferences(
    super.$_db,
    super.$_table,
    super.$_typedResult,
  );

  static $StudentsTable _studentIdTable(_$LocalDb db) =>
      db.students.createAlias('lesson_progress__student_id__students__id');

  $$StudentsTableProcessedTableManager get studentId {
    final $_column = $_itemColumn<String>('student_id')!;

    final manager = $$StudentsTableTableManager(
      $_db,
      $_db.students,
    ).filter((f) => f.id.sqlEquals($_column));
    final item = $_typedResult.readTableOrNull(_studentIdTable($_db));
    if (item == null) return manager;
    return ProcessedTableManager(
      manager.$state.copyWith(prefetchedData: [item]),
    );
  }
}

class $$LessonProgressTableTableFilterComposer
    extends Composer<_$LocalDb, $LessonProgressTableTable> {
  $$LessonProgressTableTableFilterComposer({
    required super.$db,
    required super.$table,
    super.joinBuilder,
    super.$addJoinBuilderToRootComposer,
    super.$removeJoinBuilderFromRootComposer,
  });
  ColumnFilters<String> get lessonId => $composableBuilder(
    column: $table.lessonId,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<int> get lessonVersion => $composableBuilder(
    column: $table.lessonVersion,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<int> get nextStep => $composableBuilder(
    column: $table.nextStep,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<bool> get completed => $composableBuilder(
    column: $table.completed,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<DateTime> get updatedAt => $composableBuilder(
    column: $table.updatedAt,
    builder: (column) => ColumnFilters(column),
  );

  $$StudentsTableFilterComposer get studentId {
    final $$StudentsTableFilterComposer composer = $composerBuilder(
      composer: this,
      getCurrentColumn: (t) => t.studentId,
      referencedTable: $db.students,
      getReferencedColumn: (t) => t.id,
      builder:
          (
            joinBuilder, {
            $addJoinBuilderToRootComposer,
            $removeJoinBuilderFromRootComposer,
          }) => $$StudentsTableFilterComposer(
            $db: $db,
            $table: $db.students,
            $addJoinBuilderToRootComposer: $addJoinBuilderToRootComposer,
            joinBuilder: joinBuilder,
            $removeJoinBuilderFromRootComposer:
                $removeJoinBuilderFromRootComposer,
          ),
    );
    return composer;
  }
}

class $$LessonProgressTableTableOrderingComposer
    extends Composer<_$LocalDb, $LessonProgressTableTable> {
  $$LessonProgressTableTableOrderingComposer({
    required super.$db,
    required super.$table,
    super.joinBuilder,
    super.$addJoinBuilderToRootComposer,
    super.$removeJoinBuilderFromRootComposer,
  });
  ColumnOrderings<String> get lessonId => $composableBuilder(
    column: $table.lessonId,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<int> get lessonVersion => $composableBuilder(
    column: $table.lessonVersion,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<int> get nextStep => $composableBuilder(
    column: $table.nextStep,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<bool> get completed => $composableBuilder(
    column: $table.completed,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<DateTime> get updatedAt => $composableBuilder(
    column: $table.updatedAt,
    builder: (column) => ColumnOrderings(column),
  );

  $$StudentsTableOrderingComposer get studentId {
    final $$StudentsTableOrderingComposer composer = $composerBuilder(
      composer: this,
      getCurrentColumn: (t) => t.studentId,
      referencedTable: $db.students,
      getReferencedColumn: (t) => t.id,
      builder:
          (
            joinBuilder, {
            $addJoinBuilderToRootComposer,
            $removeJoinBuilderFromRootComposer,
          }) => $$StudentsTableOrderingComposer(
            $db: $db,
            $table: $db.students,
            $addJoinBuilderToRootComposer: $addJoinBuilderToRootComposer,
            joinBuilder: joinBuilder,
            $removeJoinBuilderFromRootComposer:
                $removeJoinBuilderFromRootComposer,
          ),
    );
    return composer;
  }
}

class $$LessonProgressTableTableAnnotationComposer
    extends Composer<_$LocalDb, $LessonProgressTableTable> {
  $$LessonProgressTableTableAnnotationComposer({
    required super.$db,
    required super.$table,
    super.joinBuilder,
    super.$addJoinBuilderToRootComposer,
    super.$removeJoinBuilderFromRootComposer,
  });
  GeneratedColumn<String> get lessonId =>
      $composableBuilder(column: $table.lessonId, builder: (column) => column);

  GeneratedColumn<int> get lessonVersion => $composableBuilder(
    column: $table.lessonVersion,
    builder: (column) => column,
  );

  GeneratedColumn<int> get nextStep =>
      $composableBuilder(column: $table.nextStep, builder: (column) => column);

  GeneratedColumn<bool> get completed =>
      $composableBuilder(column: $table.completed, builder: (column) => column);

  GeneratedColumn<DateTime> get updatedAt =>
      $composableBuilder(column: $table.updatedAt, builder: (column) => column);

  $$StudentsTableAnnotationComposer get studentId {
    final $$StudentsTableAnnotationComposer composer = $composerBuilder(
      composer: this,
      getCurrentColumn: (t) => t.studentId,
      referencedTable: $db.students,
      getReferencedColumn: (t) => t.id,
      builder:
          (
            joinBuilder, {
            $addJoinBuilderToRootComposer,
            $removeJoinBuilderFromRootComposer,
          }) => $$StudentsTableAnnotationComposer(
            $db: $db,
            $table: $db.students,
            $addJoinBuilderToRootComposer: $addJoinBuilderToRootComposer,
            joinBuilder: joinBuilder,
            $removeJoinBuilderFromRootComposer:
                $removeJoinBuilderFromRootComposer,
          ),
    );
    return composer;
  }
}

class $$LessonProgressTableTableTableManager
    extends
        RootTableManager<
          _$LocalDb,
          $LessonProgressTableTable,
          LessonProgress,
          $$LessonProgressTableTableFilterComposer,
          $$LessonProgressTableTableOrderingComposer,
          $$LessonProgressTableTableAnnotationComposer,
          $$LessonProgressTableTableCreateCompanionBuilder,
          $$LessonProgressTableTableUpdateCompanionBuilder,
          (LessonProgress, $$LessonProgressTableTableReferences),
          LessonProgress,
          PrefetchHooks Function({bool studentId})
        > {
  $$LessonProgressTableTableTableManager(
    _$LocalDb db,
    $LessonProgressTableTable table,
  ) : super(
        TableManagerState(
          db: db,
          table: table,
          createFilteringComposer: () =>
              $$LessonProgressTableTableFilterComposer($db: db, $table: table),
          createOrderingComposer: () =>
              $$LessonProgressTableTableOrderingComposer(
                $db: db,
                $table: table,
              ),
          createComputedFieldComposer: () =>
              $$LessonProgressTableTableAnnotationComposer(
                $db: db,
                $table: table,
              ),
          updateCompanionCallback:
              ({
                Value<String> studentId = const Value.absent(),
                Value<String> lessonId = const Value.absent(),
                Value<int> lessonVersion = const Value.absent(),
                Value<int> nextStep = const Value.absent(),
                Value<bool> completed = const Value.absent(),
                Value<DateTime> updatedAt = const Value.absent(),
                Value<int> rowid = const Value.absent(),
              }) => LessonProgressTableCompanion(
                studentId: studentId,
                lessonId: lessonId,
                lessonVersion: lessonVersion,
                nextStep: nextStep,
                completed: completed,
                updatedAt: updatedAt,
                rowid: rowid,
              ),
          createCompanionCallback:
              ({
                required String studentId,
                required String lessonId,
                required int lessonVersion,
                required int nextStep,
                required bool completed,
                required DateTime updatedAt,
                Value<int> rowid = const Value.absent(),
              }) => LessonProgressTableCompanion.insert(
                studentId: studentId,
                lessonId: lessonId,
                lessonVersion: lessonVersion,
                nextStep: nextStep,
                completed: completed,
                updatedAt: updatedAt,
                rowid: rowid,
              ),
          withReferenceMapper: (p0) => p0
              .map(
                (e) => (
                  e.readTable<$LessonProgressTableTable, LessonProgress>(table),
                  $$LessonProgressTableTableReferences(db, table, e),
                ),
              )
              .toList(),
          prefetchHooksCallback: ({studentId = false}) {
            return PrefetchHooks(
              db: db,
              explicitlyWatchedTables: [],
              addJoins:
                  <
                    T extends TableManagerState<
                      dynamic,
                      dynamic,
                      dynamic,
                      dynamic,
                      dynamic,
                      dynamic,
                      dynamic,
                      dynamic,
                      dynamic,
                      dynamic,
                      dynamic
                    >
                  >(state) {
                    if (studentId) {
                      state = state.withJoin(
                        currentTable: table,
                        currentColumn: table.studentId,
                        referencedTable: $$LessonProgressTableTableReferences
                            ._studentIdTable(db),
                        referencedColumn: $$LessonProgressTableTableReferences
                            ._studentIdTable(db)
                            .id,
                      ) as T;
                    }

                    return state;
                  },
              getPrefetchedDataCallback: (items) async {
                return [];
              },
            );
          },
        ),
      );
}

typedef $$LessonProgressTableTableProcessedTableManager =
    ProcessedTableManager<
      _$LocalDb,
      $LessonProgressTableTable,
      LessonProgress,
      $$LessonProgressTableTableFilterComposer,
      $$LessonProgressTableTableOrderingComposer,
      $$LessonProgressTableTableAnnotationComposer,
      $$LessonProgressTableTableCreateCompanionBuilder,
      $$LessonProgressTableTableUpdateCompanionBuilder,
      (LessonProgress, $$LessonProgressTableTableReferences),
      LessonProgress,
      PrefetchHooks Function({bool studentId})
    >;
typedef $$StepResultsTableCreateCompanionBuilder =
    StepResultsCompanion Function({
      required String studentId,
      required String lessonId,
      required String stepId,
      Value<bool?> correct,
      required int attempts,
      Value<String> misconceptions,
      required DateTime answeredAt,
      Value<bool> synced,
      Value<int> rowid,
    });
typedef $$StepResultsTableUpdateCompanionBuilder =
    StepResultsCompanion Function({
      Value<String> studentId,
      Value<String> lessonId,
      Value<String> stepId,
      Value<bool?> correct,
      Value<int> attempts,
      Value<String> misconceptions,
      Value<DateTime> answeredAt,
      Value<bool> synced,
      Value<int> rowid,
    });

final class $$StepResultsTableReferences
    extends BaseReferences<_$LocalDb, $StepResultsTable, StepResultRow> {
  $$StepResultsTableReferences(super.$_db, super.$_table, super.$_typedResult);

  static $StudentsTable _studentIdTable(_$LocalDb db) =>
      db.students.createAlias('step_results__student_id__students__id');

  $$StudentsTableProcessedTableManager get studentId {
    final $_column = $_itemColumn<String>('student_id')!;

    final manager = $$StudentsTableTableManager(
      $_db,
      $_db.students,
    ).filter((f) => f.id.sqlEquals($_column));
    final item = $_typedResult.readTableOrNull(_studentIdTable($_db));
    if (item == null) return manager;
    return ProcessedTableManager(
      manager.$state.copyWith(prefetchedData: [item]),
    );
  }
}

class $$StepResultsTableFilterComposer
    extends Composer<_$LocalDb, $StepResultsTable> {
  $$StepResultsTableFilterComposer({
    required super.$db,
    required super.$table,
    super.joinBuilder,
    super.$addJoinBuilderToRootComposer,
    super.$removeJoinBuilderFromRootComposer,
  });
  ColumnFilters<String> get lessonId => $composableBuilder(
    column: $table.lessonId,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<String> get stepId => $composableBuilder(
    column: $table.stepId,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<bool> get correct => $composableBuilder(
    column: $table.correct,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<int> get attempts => $composableBuilder(
    column: $table.attempts,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<String> get misconceptions => $composableBuilder(
    column: $table.misconceptions,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<DateTime> get answeredAt => $composableBuilder(
    column: $table.answeredAt,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<bool> get synced => $composableBuilder(
    column: $table.synced,
    builder: (column) => ColumnFilters(column),
  );

  $$StudentsTableFilterComposer get studentId {
    final $$StudentsTableFilterComposer composer = $composerBuilder(
      composer: this,
      getCurrentColumn: (t) => t.studentId,
      referencedTable: $db.students,
      getReferencedColumn: (t) => t.id,
      builder:
          (
            joinBuilder, {
            $addJoinBuilderToRootComposer,
            $removeJoinBuilderFromRootComposer,
          }) => $$StudentsTableFilterComposer(
            $db: $db,
            $table: $db.students,
            $addJoinBuilderToRootComposer: $addJoinBuilderToRootComposer,
            joinBuilder: joinBuilder,
            $removeJoinBuilderFromRootComposer:
                $removeJoinBuilderFromRootComposer,
          ),
    );
    return composer;
  }
}

class $$StepResultsTableOrderingComposer
    extends Composer<_$LocalDb, $StepResultsTable> {
  $$StepResultsTableOrderingComposer({
    required super.$db,
    required super.$table,
    super.joinBuilder,
    super.$addJoinBuilderToRootComposer,
    super.$removeJoinBuilderFromRootComposer,
  });
  ColumnOrderings<String> get lessonId => $composableBuilder(
    column: $table.lessonId,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<String> get stepId => $composableBuilder(
    column: $table.stepId,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<bool> get correct => $composableBuilder(
    column: $table.correct,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<int> get attempts => $composableBuilder(
    column: $table.attempts,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<String> get misconceptions => $composableBuilder(
    column: $table.misconceptions,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<DateTime> get answeredAt => $composableBuilder(
    column: $table.answeredAt,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<bool> get synced => $composableBuilder(
    column: $table.synced,
    builder: (column) => ColumnOrderings(column),
  );

  $$StudentsTableOrderingComposer get studentId {
    final $$StudentsTableOrderingComposer composer = $composerBuilder(
      composer: this,
      getCurrentColumn: (t) => t.studentId,
      referencedTable: $db.students,
      getReferencedColumn: (t) => t.id,
      builder:
          (
            joinBuilder, {
            $addJoinBuilderToRootComposer,
            $removeJoinBuilderFromRootComposer,
          }) => $$StudentsTableOrderingComposer(
            $db: $db,
            $table: $db.students,
            $addJoinBuilderToRootComposer: $addJoinBuilderToRootComposer,
            joinBuilder: joinBuilder,
            $removeJoinBuilderFromRootComposer:
                $removeJoinBuilderFromRootComposer,
          ),
    );
    return composer;
  }
}

class $$StepResultsTableAnnotationComposer
    extends Composer<_$LocalDb, $StepResultsTable> {
  $$StepResultsTableAnnotationComposer({
    required super.$db,
    required super.$table,
    super.joinBuilder,
    super.$addJoinBuilderToRootComposer,
    super.$removeJoinBuilderFromRootComposer,
  });
  GeneratedColumn<String> get lessonId =>
      $composableBuilder(column: $table.lessonId, builder: (column) => column);

  GeneratedColumn<String> get stepId =>
      $composableBuilder(column: $table.stepId, builder: (column) => column);

  GeneratedColumn<bool> get correct =>
      $composableBuilder(column: $table.correct, builder: (column) => column);

  GeneratedColumn<int> get attempts =>
      $composableBuilder(column: $table.attempts, builder: (column) => column);

  GeneratedColumn<String> get misconceptions => $composableBuilder(
    column: $table.misconceptions,
    builder: (column) => column,
  );

  GeneratedColumn<DateTime> get answeredAt => $composableBuilder(
    column: $table.answeredAt,
    builder: (column) => column,
  );

  GeneratedColumn<bool> get synced =>
      $composableBuilder(column: $table.synced, builder: (column) => column);

  $$StudentsTableAnnotationComposer get studentId {
    final $$StudentsTableAnnotationComposer composer = $composerBuilder(
      composer: this,
      getCurrentColumn: (t) => t.studentId,
      referencedTable: $db.students,
      getReferencedColumn: (t) => t.id,
      builder:
          (
            joinBuilder, {
            $addJoinBuilderToRootComposer,
            $removeJoinBuilderFromRootComposer,
          }) => $$StudentsTableAnnotationComposer(
            $db: $db,
            $table: $db.students,
            $addJoinBuilderToRootComposer: $addJoinBuilderToRootComposer,
            joinBuilder: joinBuilder,
            $removeJoinBuilderFromRootComposer:
                $removeJoinBuilderFromRootComposer,
          ),
    );
    return composer;
  }
}

class $$StepResultsTableTableManager
    extends
        RootTableManager<
          _$LocalDb,
          $StepResultsTable,
          StepResultRow,
          $$StepResultsTableFilterComposer,
          $$StepResultsTableOrderingComposer,
          $$StepResultsTableAnnotationComposer,
          $$StepResultsTableCreateCompanionBuilder,
          $$StepResultsTableUpdateCompanionBuilder,
          (StepResultRow, $$StepResultsTableReferences),
          StepResultRow,
          PrefetchHooks Function({bool studentId})
        > {
  $$StepResultsTableTableManager(_$LocalDb db, $StepResultsTable table)
    : super(
        TableManagerState(
          db: db,
          table: table,
          createFilteringComposer: () =>
              $$StepResultsTableFilterComposer($db: db, $table: table),
          createOrderingComposer: () =>
              $$StepResultsTableOrderingComposer($db: db, $table: table),
          createComputedFieldComposer: () =>
              $$StepResultsTableAnnotationComposer($db: db, $table: table),
          updateCompanionCallback:
              ({
                Value<String> studentId = const Value.absent(),
                Value<String> lessonId = const Value.absent(),
                Value<String> stepId = const Value.absent(),
                Value<bool?> correct = const Value.absent(),
                Value<int> attempts = const Value.absent(),
                Value<String> misconceptions = const Value.absent(),
                Value<DateTime> answeredAt = const Value.absent(),
                Value<bool> synced = const Value.absent(),
                Value<int> rowid = const Value.absent(),
              }) => StepResultsCompanion(
                studentId: studentId,
                lessonId: lessonId,
                stepId: stepId,
                correct: correct,
                attempts: attempts,
                misconceptions: misconceptions,
                answeredAt: answeredAt,
                synced: synced,
                rowid: rowid,
              ),
          createCompanionCallback:
              ({
                required String studentId,
                required String lessonId,
                required String stepId,
                Value<bool?> correct = const Value.absent(),
                required int attempts,
                Value<String> misconceptions = const Value.absent(),
                required DateTime answeredAt,
                Value<bool> synced = const Value.absent(),
                Value<int> rowid = const Value.absent(),
              }) => StepResultsCompanion.insert(
                studentId: studentId,
                lessonId: lessonId,
                stepId: stepId,
                correct: correct,
                attempts: attempts,
                misconceptions: misconceptions,
                answeredAt: answeredAt,
                synced: synced,
                rowid: rowid,
              ),
          withReferenceMapper: (p0) => p0
              .map(
                (e) => (
                  e.readTable<$StepResultsTable, StepResultRow>(table),
                  $$StepResultsTableReferences(db, table, e),
                ),
              )
              .toList(),
          prefetchHooksCallback: ({studentId = false}) {
            return PrefetchHooks(
              db: db,
              explicitlyWatchedTables: [],
              addJoins:
                  <
                    T extends TableManagerState<
                      dynamic,
                      dynamic,
                      dynamic,
                      dynamic,
                      dynamic,
                      dynamic,
                      dynamic,
                      dynamic,
                      dynamic,
                      dynamic,
                      dynamic
                    >
                  >(state) {
                    if (studentId) {
                      state = state.withJoin(
                        currentTable: table,
                        currentColumn: table.studentId,
                        referencedTable: $$StepResultsTableReferences
                            ._studentIdTable(db),
                        referencedColumn: $$StepResultsTableReferences
                            ._studentIdTable(db)
                            .id,
                      ) as T;
                    }

                    return state;
                  },
              getPrefetchedDataCallback: (items) async {
                return [];
              },
            );
          },
        ),
      );
}

typedef $$StepResultsTableProcessedTableManager =
    ProcessedTableManager<
      _$LocalDb,
      $StepResultsTable,
      StepResultRow,
      $$StepResultsTableFilterComposer,
      $$StepResultsTableOrderingComposer,
      $$StepResultsTableAnnotationComposer,
      $$StepResultsTableCreateCompanionBuilder,
      $$StepResultsTableUpdateCompanionBuilder,
      (StepResultRow, $$StepResultsTableReferences),
      StepResultRow,
      PrefetchHooks Function({bool studentId})
    >;
typedef $$SkillStatesTableCreateCompanionBuilder =
    SkillStatesCompanion Function({
      required String studentId,
      required String skill,
      required String data,
      required DateTime updatedAt,
      Value<bool> synced,
      Value<int> rowid,
    });
typedef $$SkillStatesTableUpdateCompanionBuilder =
    SkillStatesCompanion Function({
      Value<String> studentId,
      Value<String> skill,
      Value<String> data,
      Value<DateTime> updatedAt,
      Value<bool> synced,
      Value<int> rowid,
    });

final class $$SkillStatesTableReferences
    extends BaseReferences<_$LocalDb, $SkillStatesTable, SkillStateRow> {
  $$SkillStatesTableReferences(super.$_db, super.$_table, super.$_typedResult);

  static $StudentsTable _studentIdTable(_$LocalDb db) =>
      db.students.createAlias('skill_states__student_id__students__id');

  $$StudentsTableProcessedTableManager get studentId {
    final $_column = $_itemColumn<String>('student_id')!;

    final manager = $$StudentsTableTableManager(
      $_db,
      $_db.students,
    ).filter((f) => f.id.sqlEquals($_column));
    final item = $_typedResult.readTableOrNull(_studentIdTable($_db));
    if (item == null) return manager;
    return ProcessedTableManager(
      manager.$state.copyWith(prefetchedData: [item]),
    );
  }
}

class $$SkillStatesTableFilterComposer
    extends Composer<_$LocalDb, $SkillStatesTable> {
  $$SkillStatesTableFilterComposer({
    required super.$db,
    required super.$table,
    super.joinBuilder,
    super.$addJoinBuilderToRootComposer,
    super.$removeJoinBuilderFromRootComposer,
  });
  ColumnFilters<String> get skill => $composableBuilder(
    column: $table.skill,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<String> get data => $composableBuilder(
    column: $table.data,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<DateTime> get updatedAt => $composableBuilder(
    column: $table.updatedAt,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<bool> get synced => $composableBuilder(
    column: $table.synced,
    builder: (column) => ColumnFilters(column),
  );

  $$StudentsTableFilterComposer get studentId {
    final $$StudentsTableFilterComposer composer = $composerBuilder(
      composer: this,
      getCurrentColumn: (t) => t.studentId,
      referencedTable: $db.students,
      getReferencedColumn: (t) => t.id,
      builder:
          (
            joinBuilder, {
            $addJoinBuilderToRootComposer,
            $removeJoinBuilderFromRootComposer,
          }) => $$StudentsTableFilterComposer(
            $db: $db,
            $table: $db.students,
            $addJoinBuilderToRootComposer: $addJoinBuilderToRootComposer,
            joinBuilder: joinBuilder,
            $removeJoinBuilderFromRootComposer:
                $removeJoinBuilderFromRootComposer,
          ),
    );
    return composer;
  }
}

class $$SkillStatesTableOrderingComposer
    extends Composer<_$LocalDb, $SkillStatesTable> {
  $$SkillStatesTableOrderingComposer({
    required super.$db,
    required super.$table,
    super.joinBuilder,
    super.$addJoinBuilderToRootComposer,
    super.$removeJoinBuilderFromRootComposer,
  });
  ColumnOrderings<String> get skill => $composableBuilder(
    column: $table.skill,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<String> get data => $composableBuilder(
    column: $table.data,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<DateTime> get updatedAt => $composableBuilder(
    column: $table.updatedAt,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<bool> get synced => $composableBuilder(
    column: $table.synced,
    builder: (column) => ColumnOrderings(column),
  );

  $$StudentsTableOrderingComposer get studentId {
    final $$StudentsTableOrderingComposer composer = $composerBuilder(
      composer: this,
      getCurrentColumn: (t) => t.studentId,
      referencedTable: $db.students,
      getReferencedColumn: (t) => t.id,
      builder:
          (
            joinBuilder, {
            $addJoinBuilderToRootComposer,
            $removeJoinBuilderFromRootComposer,
          }) => $$StudentsTableOrderingComposer(
            $db: $db,
            $table: $db.students,
            $addJoinBuilderToRootComposer: $addJoinBuilderToRootComposer,
            joinBuilder: joinBuilder,
            $removeJoinBuilderFromRootComposer:
                $removeJoinBuilderFromRootComposer,
          ),
    );
    return composer;
  }
}

class $$SkillStatesTableAnnotationComposer
    extends Composer<_$LocalDb, $SkillStatesTable> {
  $$SkillStatesTableAnnotationComposer({
    required super.$db,
    required super.$table,
    super.joinBuilder,
    super.$addJoinBuilderToRootComposer,
    super.$removeJoinBuilderFromRootComposer,
  });
  GeneratedColumn<String> get skill =>
      $composableBuilder(column: $table.skill, builder: (column) => column);

  GeneratedColumn<String> get data =>
      $composableBuilder(column: $table.data, builder: (column) => column);

  GeneratedColumn<DateTime> get updatedAt =>
      $composableBuilder(column: $table.updatedAt, builder: (column) => column);

  GeneratedColumn<bool> get synced =>
      $composableBuilder(column: $table.synced, builder: (column) => column);

  $$StudentsTableAnnotationComposer get studentId {
    final $$StudentsTableAnnotationComposer composer = $composerBuilder(
      composer: this,
      getCurrentColumn: (t) => t.studentId,
      referencedTable: $db.students,
      getReferencedColumn: (t) => t.id,
      builder:
          (
            joinBuilder, {
            $addJoinBuilderToRootComposer,
            $removeJoinBuilderFromRootComposer,
          }) => $$StudentsTableAnnotationComposer(
            $db: $db,
            $table: $db.students,
            $addJoinBuilderToRootComposer: $addJoinBuilderToRootComposer,
            joinBuilder: joinBuilder,
            $removeJoinBuilderFromRootComposer:
                $removeJoinBuilderFromRootComposer,
          ),
    );
    return composer;
  }
}

class $$SkillStatesTableTableManager
    extends
        RootTableManager<
          _$LocalDb,
          $SkillStatesTable,
          SkillStateRow,
          $$SkillStatesTableFilterComposer,
          $$SkillStatesTableOrderingComposer,
          $$SkillStatesTableAnnotationComposer,
          $$SkillStatesTableCreateCompanionBuilder,
          $$SkillStatesTableUpdateCompanionBuilder,
          (SkillStateRow, $$SkillStatesTableReferences),
          SkillStateRow,
          PrefetchHooks Function({bool studentId})
        > {
  $$SkillStatesTableTableManager(_$LocalDb db, $SkillStatesTable table)
    : super(
        TableManagerState(
          db: db,
          table: table,
          createFilteringComposer: () =>
              $$SkillStatesTableFilterComposer($db: db, $table: table),
          createOrderingComposer: () =>
              $$SkillStatesTableOrderingComposer($db: db, $table: table),
          createComputedFieldComposer: () =>
              $$SkillStatesTableAnnotationComposer($db: db, $table: table),
          updateCompanionCallback:
              ({
                Value<String> studentId = const Value.absent(),
                Value<String> skill = const Value.absent(),
                Value<String> data = const Value.absent(),
                Value<DateTime> updatedAt = const Value.absent(),
                Value<bool> synced = const Value.absent(),
                Value<int> rowid = const Value.absent(),
              }) => SkillStatesCompanion(
                studentId: studentId,
                skill: skill,
                data: data,
                updatedAt: updatedAt,
                synced: synced,
                rowid: rowid,
              ),
          createCompanionCallback:
              ({
                required String studentId,
                required String skill,
                required String data,
                required DateTime updatedAt,
                Value<bool> synced = const Value.absent(),
                Value<int> rowid = const Value.absent(),
              }) => SkillStatesCompanion.insert(
                studentId: studentId,
                skill: skill,
                data: data,
                updatedAt: updatedAt,
                synced: synced,
                rowid: rowid,
              ),
          withReferenceMapper: (p0) => p0
              .map(
                (e) => (
                  e.readTable<$SkillStatesTable, SkillStateRow>(table),
                  $$SkillStatesTableReferences(db, table, e),
                ),
              )
              .toList(),
          prefetchHooksCallback: ({studentId = false}) {
            return PrefetchHooks(
              db: db,
              explicitlyWatchedTables: [],
              addJoins:
                  <
                    T extends TableManagerState<
                      dynamic,
                      dynamic,
                      dynamic,
                      dynamic,
                      dynamic,
                      dynamic,
                      dynamic,
                      dynamic,
                      dynamic,
                      dynamic,
                      dynamic
                    >
                  >(state) {
                    if (studentId) {
                      state = state.withJoin(
                        currentTable: table,
                        currentColumn: table.studentId,
                        referencedTable: $$SkillStatesTableReferences
                            ._studentIdTable(db),
                        referencedColumn: $$SkillStatesTableReferences
                            ._studentIdTable(db)
                            .id,
                      ) as T;
                    }

                    return state;
                  },
              getPrefetchedDataCallback: (items) async {
                return [];
              },
            );
          },
        ),
      );
}

typedef $$SkillStatesTableProcessedTableManager =
    ProcessedTableManager<
      _$LocalDb,
      $SkillStatesTable,
      SkillStateRow,
      $$SkillStatesTableFilterComposer,
      $$SkillStatesTableOrderingComposer,
      $$SkillStatesTableAnnotationComposer,
      $$SkillStatesTableCreateCompanionBuilder,
      $$SkillStatesTableUpdateCompanionBuilder,
      (SkillStateRow, $$SkillStatesTableReferences),
      SkillStateRow,
      PrefetchHooks Function({bool studentId})
    >;

class $LocalDbManager {
  final _$LocalDb _db;
  $LocalDbManager(this._db);
  $$StudentsTableTableManager get students =>
      $$StudentsTableTableManager(_db, _db.students);
  $$LessonProgressTableTableTableManager get lessonProgressTable =>
      $$LessonProgressTableTableTableManager(_db, _db.lessonProgressTable);
  $$StepResultsTableTableManager get stepResults =>
      $$StepResultsTableTableManager(_db, _db.stepResults);
  $$SkillStatesTableTableManager get skillStates =>
      $$SkillStatesTableTableManager(_db, _db.skillStates);
}
