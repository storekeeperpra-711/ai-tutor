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

class $AiQueueTable extends AiQueue
    with TableInfo<$AiQueueTable, QueuedAnswer> {
  @override
  final GeneratedDatabase attachedDatabase;
  final String? _alias;
  $AiQueueTable(this.attachedDatabase, [this._alias]);
  static const VerificationMeta _idMeta = const VerificationMeta('id');
  @override
  late final GeneratedColumn<String> id = GeneratedColumn<String>(
    'id',
    aliasedName,
    false,
    type: DriftSqlType.string,
    requiredDuringInsert: true,
  );
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
  static const VerificationMeta _taskMeta = const VerificationMeta('task');
  @override
  late final GeneratedColumn<String> task = GeneratedColumn<String>(
    'task',
    aliasedName,
    false,
    type: DriftSqlType.string,
    requiredDuringInsert: true,
  );
  static const VerificationMeta _langMeta = const VerificationMeta('lang');
  @override
  late final GeneratedColumn<String> lang = GeneratedColumn<String>(
    'lang',
    aliasedName,
    false,
    type: DriftSqlType.string,
    requiredDuringInsert: true,
  );
  static const VerificationMeta _answerMeta = const VerificationMeta('answer');
  @override
  late final GeneratedColumn<String> answer = GeneratedColumn<String>(
    'answer',
    aliasedName,
    false,
    type: DriftSqlType.string,
    requiredDuringInsert: true,
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
  static const VerificationMeta _uploadedMeta = const VerificationMeta(
    'uploaded',
  );
  @override
  late final GeneratedColumn<bool> uploaded = GeneratedColumn<bool>(
    'uploaded',
    aliasedName,
    false,
    type: DriftSqlType.bool,
    requiredDuringInsert: false,
    defaultConstraints: GeneratedColumn.constraintIsAlways(
      'CHECK ("uploaded" IN (0, 1))',
    ),
    defaultValue: const Constant(false),
  );
  static const VerificationMeta _statusMeta = const VerificationMeta('status');
  @override
  late final GeneratedColumn<String> status = GeneratedColumn<String>(
    'status',
    aliasedName,
    false,
    type: DriftSqlType.string,
    requiredDuringInsert: false,
    defaultValue: const Constant('waiting'),
  );
  static const VerificationMeta _levelMeta = const VerificationMeta('level');
  @override
  late final GeneratedColumn<String> level = GeneratedColumn<String>(
    'level',
    aliasedName,
    true,
    type: DriftSqlType.string,
    requiredDuringInsert: false,
  );
  static const VerificationMeta _replyMeta = const VerificationMeta('reply');
  @override
  late final GeneratedColumn<String> reply = GeneratedColumn<String>(
    'reply',
    aliasedName,
    true,
    type: DriftSqlType.string,
    requiredDuringInsert: false,
  );
  static const VerificationMeta _seenMeta = const VerificationMeta('seen');
  @override
  late final GeneratedColumn<bool> seen = GeneratedColumn<bool>(
    'seen',
    aliasedName,
    false,
    type: DriftSqlType.bool,
    requiredDuringInsert: false,
    defaultConstraints: GeneratedColumn.constraintIsAlways(
      'CHECK ("seen" IN (0, 1))',
    ),
    defaultValue: const Constant(false),
  );
  @override
  List<GeneratedColumn> get $columns => [
    id,
    studentId,
    lessonId,
    stepId,
    task,
    lang,
    answer,
    createdAt,
    uploaded,
    status,
    level,
    reply,
    seen,
  ];
  @override
  String get aliasedName => _alias ?? actualTableName;
  @override
  String get actualTableName => $name;
  static const String $name = 'ai_queue';
  @override
  VerificationContext validateIntegrity(
    Insertable<QueuedAnswer> instance, {
    bool isInserting = false,
  }) {
    final context = VerificationContext();
    final data = instance.toColumns(true);
    if (data.containsKey('id')) {
      context.handle(_idMeta, id.isAcceptableOrUnknown(data['id']!, _idMeta));
    } else if (isInserting) {
      context.missing(_idMeta);
    }
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
    if (data.containsKey('task')) {
      context.handle(
        _taskMeta,
        task.isAcceptableOrUnknown(data['task']!, _taskMeta),
      );
    } else if (isInserting) {
      context.missing(_taskMeta);
    }
    if (data.containsKey('lang')) {
      context.handle(
        _langMeta,
        lang.isAcceptableOrUnknown(data['lang']!, _langMeta),
      );
    } else if (isInserting) {
      context.missing(_langMeta);
    }
    if (data.containsKey('answer')) {
      context.handle(
        _answerMeta,
        answer.isAcceptableOrUnknown(data['answer']!, _answerMeta),
      );
    } else if (isInserting) {
      context.missing(_answerMeta);
    }
    if (data.containsKey('created_at')) {
      context.handle(
        _createdAtMeta,
        createdAt.isAcceptableOrUnknown(data['created_at']!, _createdAtMeta),
      );
    } else if (isInserting) {
      context.missing(_createdAtMeta);
    }
    if (data.containsKey('uploaded')) {
      context.handle(
        _uploadedMeta,
        uploaded.isAcceptableOrUnknown(data['uploaded']!, _uploadedMeta),
      );
    }
    if (data.containsKey('status')) {
      context.handle(
        _statusMeta,
        status.isAcceptableOrUnknown(data['status']!, _statusMeta),
      );
    }
    if (data.containsKey('level')) {
      context.handle(
        _levelMeta,
        level.isAcceptableOrUnknown(data['level']!, _levelMeta),
      );
    }
    if (data.containsKey('reply')) {
      context.handle(
        _replyMeta,
        reply.isAcceptableOrUnknown(data['reply']!, _replyMeta),
      );
    }
    if (data.containsKey('seen')) {
      context.handle(
        _seenMeta,
        seen.isAcceptableOrUnknown(data['seen']!, _seenMeta),
      );
    }
    return context;
  }

  @override
  Set<GeneratedColumn> get $primaryKey => {id};
  @override
  QueuedAnswer map(Map<String, dynamic> data, {String? tablePrefix}) {
    final effectivePrefix = tablePrefix != null ? '$tablePrefix.' : '';
    return QueuedAnswer(
      id: attachedDatabase.typeMapping.read(
        DriftSqlType.string,
        data['${effectivePrefix}id'],
      )!,
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
      task: attachedDatabase.typeMapping.read(
        DriftSqlType.string,
        data['${effectivePrefix}task'],
      )!,
      lang: attachedDatabase.typeMapping.read(
        DriftSqlType.string,
        data['${effectivePrefix}lang'],
      )!,
      answer: attachedDatabase.typeMapping.read(
        DriftSqlType.string,
        data['${effectivePrefix}answer'],
      )!,
      createdAt: attachedDatabase.typeMapping.read(
        DriftSqlType.dateTime,
        data['${effectivePrefix}created_at'],
      )!,
      uploaded: attachedDatabase.typeMapping.read(
        DriftSqlType.bool,
        data['${effectivePrefix}uploaded'],
      )!,
      status: attachedDatabase.typeMapping.read(
        DriftSqlType.string,
        data['${effectivePrefix}status'],
      )!,
      level: attachedDatabase.typeMapping.read(
        DriftSqlType.string,
        data['${effectivePrefix}level'],
      ),
      reply: attachedDatabase.typeMapping.read(
        DriftSqlType.string,
        data['${effectivePrefix}reply'],
      ),
      seen: attachedDatabase.typeMapping.read(
        DriftSqlType.bool,
        data['${effectivePrefix}seen'],
      )!,
    );
  }

  @override
  $AiQueueTable createAlias(String alias) {
    return $AiQueueTable(attachedDatabase, alias);
  }
}

class QueuedAnswer extends DataClass implements Insertable<QueuedAnswer> {
  /// Also the Firestore document id in `ai_queue`.
  final String id;
  final String studentId;
  final String lessonId;
  final String stepId;

  /// The question, so the notes screen can show it without the lesson.
  final String task;
  final String lang;
  final String answer;
  final DateTime createdAt;
  final bool uploaded;

  /// waiting, answered or failed (the server's status).
  final String status;
  final String? level;
  final String? reply;

  /// The child has opened Mithu's reply.
  final bool seen;
  const QueuedAnswer({
    required this.id,
    required this.studentId,
    required this.lessonId,
    required this.stepId,
    required this.task,
    required this.lang,
    required this.answer,
    required this.createdAt,
    required this.uploaded,
    required this.status,
    this.level,
    this.reply,
    required this.seen,
  });
  @override
  Map<String, Expression> toColumns(bool nullToAbsent) {
    final map = <String, Expression>{};
    map['id'] = Variable<String>(id);
    map['student_id'] = Variable<String>(studentId);
    map['lesson_id'] = Variable<String>(lessonId);
    map['step_id'] = Variable<String>(stepId);
    map['task'] = Variable<String>(task);
    map['lang'] = Variable<String>(lang);
    map['answer'] = Variable<String>(answer);
    map['created_at'] = Variable<DateTime>(createdAt);
    map['uploaded'] = Variable<bool>(uploaded);
    map['status'] = Variable<String>(status);
    if (!nullToAbsent || level != null) {
      map['level'] = Variable<String>(level);
    }
    if (!nullToAbsent || reply != null) {
      map['reply'] = Variable<String>(reply);
    }
    map['seen'] = Variable<bool>(seen);
    return map;
  }

  AiQueueCompanion toCompanion(bool nullToAbsent) {
    return AiQueueCompanion(
      id: Value(id),
      studentId: Value(studentId),
      lessonId: Value(lessonId),
      stepId: Value(stepId),
      task: Value(task),
      lang: Value(lang),
      answer: Value(answer),
      createdAt: Value(createdAt),
      uploaded: Value(uploaded),
      status: Value(status),
      level: level == null && nullToAbsent
          ? const Value.absent()
          : Value(level),
      reply: reply == null && nullToAbsent
          ? const Value.absent()
          : Value(reply),
      seen: Value(seen),
    );
  }

  factory QueuedAnswer.fromJson(
    Map<String, dynamic> json, {
    ValueSerializer? serializer,
  }) {
    serializer ??= driftRuntimeOptions.defaultSerializer;
    return QueuedAnswer(
      id: serializer.fromJson<String>(json['id']),
      studentId: serializer.fromJson<String>(json['studentId']),
      lessonId: serializer.fromJson<String>(json['lessonId']),
      stepId: serializer.fromJson<String>(json['stepId']),
      task: serializer.fromJson<String>(json['task']),
      lang: serializer.fromJson<String>(json['lang']),
      answer: serializer.fromJson<String>(json['answer']),
      createdAt: serializer.fromJson<DateTime>(json['createdAt']),
      uploaded: serializer.fromJson<bool>(json['uploaded']),
      status: serializer.fromJson<String>(json['status']),
      level: serializer.fromJson<String?>(json['level']),
      reply: serializer.fromJson<String?>(json['reply']),
      seen: serializer.fromJson<bool>(json['seen']),
    );
  }
  @override
  Map<String, dynamic> toJson({ValueSerializer? serializer}) {
    serializer ??= driftRuntimeOptions.defaultSerializer;
    return <String, dynamic>{
      'id': serializer.toJson<String>(id),
      'studentId': serializer.toJson<String>(studentId),
      'lessonId': serializer.toJson<String>(lessonId),
      'stepId': serializer.toJson<String>(stepId),
      'task': serializer.toJson<String>(task),
      'lang': serializer.toJson<String>(lang),
      'answer': serializer.toJson<String>(answer),
      'createdAt': serializer.toJson<DateTime>(createdAt),
      'uploaded': serializer.toJson<bool>(uploaded),
      'status': serializer.toJson<String>(status),
      'level': serializer.toJson<String?>(level),
      'reply': serializer.toJson<String?>(reply),
      'seen': serializer.toJson<bool>(seen),
    };
  }

  QueuedAnswer copyWith({
    String? id,
    String? studentId,
    String? lessonId,
    String? stepId,
    String? task,
    String? lang,
    String? answer,
    DateTime? createdAt,
    bool? uploaded,
    String? status,
    Value<String?> level = const Value.absent(),
    Value<String?> reply = const Value.absent(),
    bool? seen,
  }) => QueuedAnswer(
    id: id ?? this.id,
    studentId: studentId ?? this.studentId,
    lessonId: lessonId ?? this.lessonId,
    stepId: stepId ?? this.stepId,
    task: task ?? this.task,
    lang: lang ?? this.lang,
    answer: answer ?? this.answer,
    createdAt: createdAt ?? this.createdAt,
    uploaded: uploaded ?? this.uploaded,
    status: status ?? this.status,
    level: level.present ? level.value : this.level,
    reply: reply.present ? reply.value : this.reply,
    seen: seen ?? this.seen,
  );
  QueuedAnswer copyWithCompanion(AiQueueCompanion data) {
    return QueuedAnswer(
      id: data.id.present ? data.id.value : this.id,
      studentId: data.studentId.present ? data.studentId.value : this.studentId,
      lessonId: data.lessonId.present ? data.lessonId.value : this.lessonId,
      stepId: data.stepId.present ? data.stepId.value : this.stepId,
      task: data.task.present ? data.task.value : this.task,
      lang: data.lang.present ? data.lang.value : this.lang,
      answer: data.answer.present ? data.answer.value : this.answer,
      createdAt: data.createdAt.present ? data.createdAt.value : this.createdAt,
      uploaded: data.uploaded.present ? data.uploaded.value : this.uploaded,
      status: data.status.present ? data.status.value : this.status,
      level: data.level.present ? data.level.value : this.level,
      reply: data.reply.present ? data.reply.value : this.reply,
      seen: data.seen.present ? data.seen.value : this.seen,
    );
  }

  @override
  String toString() {
    return (StringBuffer('QueuedAnswer(')
          ..write('id: $id, ')
          ..write('studentId: $studentId, ')
          ..write('lessonId: $lessonId, ')
          ..write('stepId: $stepId, ')
          ..write('task: $task, ')
          ..write('lang: $lang, ')
          ..write('answer: $answer, ')
          ..write('createdAt: $createdAt, ')
          ..write('uploaded: $uploaded, ')
          ..write('status: $status, ')
          ..write('level: $level, ')
          ..write('reply: $reply, ')
          ..write('seen: $seen')
          ..write(')'))
        .toString();
  }

  @override
  int get hashCode => Object.hash(
    id,
    studentId,
    lessonId,
    stepId,
    task,
    lang,
    answer,
    createdAt,
    uploaded,
    status,
    level,
    reply,
    seen,
  );
  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      (other is QueuedAnswer &&
          other.id == this.id &&
          other.studentId == this.studentId &&
          other.lessonId == this.lessonId &&
          other.stepId == this.stepId &&
          other.task == this.task &&
          other.lang == this.lang &&
          other.answer == this.answer &&
          other.createdAt == this.createdAt &&
          other.uploaded == this.uploaded &&
          other.status == this.status &&
          other.level == this.level &&
          other.reply == this.reply &&
          other.seen == this.seen);
}

class AiQueueCompanion extends UpdateCompanion<QueuedAnswer> {
  final Value<String> id;
  final Value<String> studentId;
  final Value<String> lessonId;
  final Value<String> stepId;
  final Value<String> task;
  final Value<String> lang;
  final Value<String> answer;
  final Value<DateTime> createdAt;
  final Value<bool> uploaded;
  final Value<String> status;
  final Value<String?> level;
  final Value<String?> reply;
  final Value<bool> seen;
  final Value<int> rowid;
  const AiQueueCompanion({
    this.id = const Value.absent(),
    this.studentId = const Value.absent(),
    this.lessonId = const Value.absent(),
    this.stepId = const Value.absent(),
    this.task = const Value.absent(),
    this.lang = const Value.absent(),
    this.answer = const Value.absent(),
    this.createdAt = const Value.absent(),
    this.uploaded = const Value.absent(),
    this.status = const Value.absent(),
    this.level = const Value.absent(),
    this.reply = const Value.absent(),
    this.seen = const Value.absent(),
    this.rowid = const Value.absent(),
  });
  AiQueueCompanion.insert({
    required String id,
    required String studentId,
    required String lessonId,
    required String stepId,
    required String task,
    required String lang,
    required String answer,
    required DateTime createdAt,
    this.uploaded = const Value.absent(),
    this.status = const Value.absent(),
    this.level = const Value.absent(),
    this.reply = const Value.absent(),
    this.seen = const Value.absent(),
    this.rowid = const Value.absent(),
  }) : id = Value(id),
       studentId = Value(studentId),
       lessonId = Value(lessonId),
       stepId = Value(stepId),
       task = Value(task),
       lang = Value(lang),
       answer = Value(answer),
       createdAt = Value(createdAt);
  static Insertable<QueuedAnswer> custom({
    Expression<String>? id,
    Expression<String>? studentId,
    Expression<String>? lessonId,
    Expression<String>? stepId,
    Expression<String>? task,
    Expression<String>? lang,
    Expression<String>? answer,
    Expression<DateTime>? createdAt,
    Expression<bool>? uploaded,
    Expression<String>? status,
    Expression<String>? level,
    Expression<String>? reply,
    Expression<bool>? seen,
    Expression<int>? rowid,
  }) {
    return RawValuesInsertable({
      if (id != null) 'id': id,
      if (studentId != null) 'student_id': studentId,
      if (lessonId != null) 'lesson_id': lessonId,
      if (stepId != null) 'step_id': stepId,
      if (task != null) 'task': task,
      if (lang != null) 'lang': lang,
      if (answer != null) 'answer': answer,
      if (createdAt != null) 'created_at': createdAt,
      if (uploaded != null) 'uploaded': uploaded,
      if (status != null) 'status': status,
      if (level != null) 'level': level,
      if (reply != null) 'reply': reply,
      if (seen != null) 'seen': seen,
      if (rowid != null) 'rowid': rowid,
    });
  }

  AiQueueCompanion copyWith({
    Value<String>? id,
    Value<String>? studentId,
    Value<String>? lessonId,
    Value<String>? stepId,
    Value<String>? task,
    Value<String>? lang,
    Value<String>? answer,
    Value<DateTime>? createdAt,
    Value<bool>? uploaded,
    Value<String>? status,
    Value<String?>? level,
    Value<String?>? reply,
    Value<bool>? seen,
    Value<int>? rowid,
  }) {
    return AiQueueCompanion(
      id: id ?? this.id,
      studentId: studentId ?? this.studentId,
      lessonId: lessonId ?? this.lessonId,
      stepId: stepId ?? this.stepId,
      task: task ?? this.task,
      lang: lang ?? this.lang,
      answer: answer ?? this.answer,
      createdAt: createdAt ?? this.createdAt,
      uploaded: uploaded ?? this.uploaded,
      status: status ?? this.status,
      level: level ?? this.level,
      reply: reply ?? this.reply,
      seen: seen ?? this.seen,
      rowid: rowid ?? this.rowid,
    );
  }

  @override
  Map<String, Expression> toColumns(bool nullToAbsent) {
    final map = <String, Expression>{};
    if (id.present) {
      map['id'] = Variable<String>(id.value);
    }
    if (studentId.present) {
      map['student_id'] = Variable<String>(studentId.value);
    }
    if (lessonId.present) {
      map['lesson_id'] = Variable<String>(lessonId.value);
    }
    if (stepId.present) {
      map['step_id'] = Variable<String>(stepId.value);
    }
    if (task.present) {
      map['task'] = Variable<String>(task.value);
    }
    if (lang.present) {
      map['lang'] = Variable<String>(lang.value);
    }
    if (answer.present) {
      map['answer'] = Variable<String>(answer.value);
    }
    if (createdAt.present) {
      map['created_at'] = Variable<DateTime>(createdAt.value);
    }
    if (uploaded.present) {
      map['uploaded'] = Variable<bool>(uploaded.value);
    }
    if (status.present) {
      map['status'] = Variable<String>(status.value);
    }
    if (level.present) {
      map['level'] = Variable<String>(level.value);
    }
    if (reply.present) {
      map['reply'] = Variable<String>(reply.value);
    }
    if (seen.present) {
      map['seen'] = Variable<bool>(seen.value);
    }
    if (rowid.present) {
      map['rowid'] = Variable<int>(rowid.value);
    }
    return map;
  }

  @override
  String toString() {
    return (StringBuffer('AiQueueCompanion(')
          ..write('id: $id, ')
          ..write('studentId: $studentId, ')
          ..write('lessonId: $lessonId, ')
          ..write('stepId: $stepId, ')
          ..write('task: $task, ')
          ..write('lang: $lang, ')
          ..write('answer: $answer, ')
          ..write('createdAt: $createdAt, ')
          ..write('uploaded: $uploaded, ')
          ..write('status: $status, ')
          ..write('level: $level, ')
          ..write('reply: $reply, ')
          ..write('seen: $seen, ')
          ..write('rowid: $rowid')
          ..write(')'))
        .toString();
  }
}

class $DownloadedLessonsTable extends DownloadedLessons
    with TableInfo<$DownloadedLessonsTable, DownloadedLesson> {
  @override
  final GeneratedDatabase attachedDatabase;
  final String? _alias;
  $DownloadedLessonsTable(this.attachedDatabase, [this._alias]);
  static const VerificationMeta _idMeta = const VerificationMeta('id');
  @override
  late final GeneratedColumn<String> id = GeneratedColumn<String>(
    'id',
    aliasedName,
    false,
    type: DriftSqlType.string,
    requiredDuringInsert: true,
  );
  static const VerificationMeta _versionMeta = const VerificationMeta(
    'version',
  );
  @override
  late final GeneratedColumn<int> version = GeneratedColumn<int>(
    'version',
    aliasedName,
    false,
    type: DriftSqlType.int,
    requiredDuringInsert: true,
  );
  static const VerificationMeta _hashMeta = const VerificationMeta('hash');
  @override
  late final GeneratedColumn<String> hash = GeneratedColumn<String>(
    'hash',
    aliasedName,
    false,
    type: DriftSqlType.string,
    requiredDuringInsert: true,
  );
  static const VerificationMeta _contentMeta = const VerificationMeta(
    'content',
  );
  @override
  late final GeneratedColumn<String> content = GeneratedColumn<String>(
    'content',
    aliasedName,
    false,
    type: DriftSqlType.string,
    requiredDuringInsert: true,
  );
  static const VerificationMeta _downloadedAtMeta = const VerificationMeta(
    'downloadedAt',
  );
  @override
  late final GeneratedColumn<DateTime> downloadedAt = GeneratedColumn<DateTime>(
    'downloaded_at',
    aliasedName,
    false,
    type: DriftSqlType.dateTime,
    requiredDuringInsert: true,
  );
  @override
  List<GeneratedColumn> get $columns => [
    id,
    version,
    hash,
    content,
    downloadedAt,
  ];
  @override
  String get aliasedName => _alias ?? actualTableName;
  @override
  String get actualTableName => $name;
  static const String $name = 'downloaded_lessons';
  @override
  VerificationContext validateIntegrity(
    Insertable<DownloadedLesson> instance, {
    bool isInserting = false,
  }) {
    final context = VerificationContext();
    final data = instance.toColumns(true);
    if (data.containsKey('id')) {
      context.handle(_idMeta, id.isAcceptableOrUnknown(data['id']!, _idMeta));
    } else if (isInserting) {
      context.missing(_idMeta);
    }
    if (data.containsKey('version')) {
      context.handle(
        _versionMeta,
        version.isAcceptableOrUnknown(data['version']!, _versionMeta),
      );
    } else if (isInserting) {
      context.missing(_versionMeta);
    }
    if (data.containsKey('hash')) {
      context.handle(
        _hashMeta,
        hash.isAcceptableOrUnknown(data['hash']!, _hashMeta),
      );
    } else if (isInserting) {
      context.missing(_hashMeta);
    }
    if (data.containsKey('content')) {
      context.handle(
        _contentMeta,
        content.isAcceptableOrUnknown(data['content']!, _contentMeta),
      );
    } else if (isInserting) {
      context.missing(_contentMeta);
    }
    if (data.containsKey('downloaded_at')) {
      context.handle(
        _downloadedAtMeta,
        downloadedAt.isAcceptableOrUnknown(
          data['downloaded_at']!,
          _downloadedAtMeta,
        ),
      );
    } else if (isInserting) {
      context.missing(_downloadedAtMeta);
    }
    return context;
  }

  @override
  Set<GeneratedColumn> get $primaryKey => {id};
  @override
  DownloadedLesson map(Map<String, dynamic> data, {String? tablePrefix}) {
    final effectivePrefix = tablePrefix != null ? '$tablePrefix.' : '';
    return DownloadedLesson(
      id: attachedDatabase.typeMapping.read(
        DriftSqlType.string,
        data['${effectivePrefix}id'],
      )!,
      version: attachedDatabase.typeMapping.read(
        DriftSqlType.int,
        data['${effectivePrefix}version'],
      )!,
      hash: attachedDatabase.typeMapping.read(
        DriftSqlType.string,
        data['${effectivePrefix}hash'],
      )!,
      content: attachedDatabase.typeMapping.read(
        DriftSqlType.string,
        data['${effectivePrefix}content'],
      )!,
      downloadedAt: attachedDatabase.typeMapping.read(
        DriftSqlType.dateTime,
        data['${effectivePrefix}downloaded_at'],
      )!,
    );
  }

  @override
  $DownloadedLessonsTable createAlias(String alias) {
    return $DownloadedLessonsTable(attachedDatabase, alias);
  }
}

class DownloadedLesson extends DataClass
    implements Insertable<DownloadedLesson> {
  final String id;
  final int version;

  /// The upload tool's fingerprint of [content] (tools/upload.py).
  final String hash;

  /// The lesson's JSON.
  final String content;
  final DateTime downloadedAt;
  const DownloadedLesson({
    required this.id,
    required this.version,
    required this.hash,
    required this.content,
    required this.downloadedAt,
  });
  @override
  Map<String, Expression> toColumns(bool nullToAbsent) {
    final map = <String, Expression>{};
    map['id'] = Variable<String>(id);
    map['version'] = Variable<int>(version);
    map['hash'] = Variable<String>(hash);
    map['content'] = Variable<String>(content);
    map['downloaded_at'] = Variable<DateTime>(downloadedAt);
    return map;
  }

  DownloadedLessonsCompanion toCompanion(bool nullToAbsent) {
    return DownloadedLessonsCompanion(
      id: Value(id),
      version: Value(version),
      hash: Value(hash),
      content: Value(content),
      downloadedAt: Value(downloadedAt),
    );
  }

  factory DownloadedLesson.fromJson(
    Map<String, dynamic> json, {
    ValueSerializer? serializer,
  }) {
    serializer ??= driftRuntimeOptions.defaultSerializer;
    return DownloadedLesson(
      id: serializer.fromJson<String>(json['id']),
      version: serializer.fromJson<int>(json['version']),
      hash: serializer.fromJson<String>(json['hash']),
      content: serializer.fromJson<String>(json['content']),
      downloadedAt: serializer.fromJson<DateTime>(json['downloadedAt']),
    );
  }
  @override
  Map<String, dynamic> toJson({ValueSerializer? serializer}) {
    serializer ??= driftRuntimeOptions.defaultSerializer;
    return <String, dynamic>{
      'id': serializer.toJson<String>(id),
      'version': serializer.toJson<int>(version),
      'hash': serializer.toJson<String>(hash),
      'content': serializer.toJson<String>(content),
      'downloadedAt': serializer.toJson<DateTime>(downloadedAt),
    };
  }

  DownloadedLesson copyWith({
    String? id,
    int? version,
    String? hash,
    String? content,
    DateTime? downloadedAt,
  }) => DownloadedLesson(
    id: id ?? this.id,
    version: version ?? this.version,
    hash: hash ?? this.hash,
    content: content ?? this.content,
    downloadedAt: downloadedAt ?? this.downloadedAt,
  );
  DownloadedLesson copyWithCompanion(DownloadedLessonsCompanion data) {
    return DownloadedLesson(
      id: data.id.present ? data.id.value : this.id,
      version: data.version.present ? data.version.value : this.version,
      hash: data.hash.present ? data.hash.value : this.hash,
      content: data.content.present ? data.content.value : this.content,
      downloadedAt: data.downloadedAt.present
          ? data.downloadedAt.value
          : this.downloadedAt,
    );
  }

  @override
  String toString() {
    return (StringBuffer('DownloadedLesson(')
          ..write('id: $id, ')
          ..write('version: $version, ')
          ..write('hash: $hash, ')
          ..write('content: $content, ')
          ..write('downloadedAt: $downloadedAt')
          ..write(')'))
        .toString();
  }

  @override
  int get hashCode => Object.hash(id, version, hash, content, downloadedAt);
  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      (other is DownloadedLesson &&
          other.id == this.id &&
          other.version == this.version &&
          other.hash == this.hash &&
          other.content == this.content &&
          other.downloadedAt == this.downloadedAt);
}

class DownloadedLessonsCompanion extends UpdateCompanion<DownloadedLesson> {
  final Value<String> id;
  final Value<int> version;
  final Value<String> hash;
  final Value<String> content;
  final Value<DateTime> downloadedAt;
  final Value<int> rowid;
  const DownloadedLessonsCompanion({
    this.id = const Value.absent(),
    this.version = const Value.absent(),
    this.hash = const Value.absent(),
    this.content = const Value.absent(),
    this.downloadedAt = const Value.absent(),
    this.rowid = const Value.absent(),
  });
  DownloadedLessonsCompanion.insert({
    required String id,
    required int version,
    required String hash,
    required String content,
    required DateTime downloadedAt,
    this.rowid = const Value.absent(),
  }) : id = Value(id),
       version = Value(version),
       hash = Value(hash),
       content = Value(content),
       downloadedAt = Value(downloadedAt);
  static Insertable<DownloadedLesson> custom({
    Expression<String>? id,
    Expression<int>? version,
    Expression<String>? hash,
    Expression<String>? content,
    Expression<DateTime>? downloadedAt,
    Expression<int>? rowid,
  }) {
    return RawValuesInsertable({
      if (id != null) 'id': id,
      if (version != null) 'version': version,
      if (hash != null) 'hash': hash,
      if (content != null) 'content': content,
      if (downloadedAt != null) 'downloaded_at': downloadedAt,
      if (rowid != null) 'rowid': rowid,
    });
  }

  DownloadedLessonsCompanion copyWith({
    Value<String>? id,
    Value<int>? version,
    Value<String>? hash,
    Value<String>? content,
    Value<DateTime>? downloadedAt,
    Value<int>? rowid,
  }) {
    return DownloadedLessonsCompanion(
      id: id ?? this.id,
      version: version ?? this.version,
      hash: hash ?? this.hash,
      content: content ?? this.content,
      downloadedAt: downloadedAt ?? this.downloadedAt,
      rowid: rowid ?? this.rowid,
    );
  }

  @override
  Map<String, Expression> toColumns(bool nullToAbsent) {
    final map = <String, Expression>{};
    if (id.present) {
      map['id'] = Variable<String>(id.value);
    }
    if (version.present) {
      map['version'] = Variable<int>(version.value);
    }
    if (hash.present) {
      map['hash'] = Variable<String>(hash.value);
    }
    if (content.present) {
      map['content'] = Variable<String>(content.value);
    }
    if (downloadedAt.present) {
      map['downloaded_at'] = Variable<DateTime>(downloadedAt.value);
    }
    if (rowid.present) {
      map['rowid'] = Variable<int>(rowid.value);
    }
    return map;
  }

  @override
  String toString() {
    return (StringBuffer('DownloadedLessonsCompanion(')
          ..write('id: $id, ')
          ..write('version: $version, ')
          ..write('hash: $hash, ')
          ..write('content: $content, ')
          ..write('downloadedAt: $downloadedAt, ')
          ..write('rowid: $rowid')
          ..write(')'))
        .toString();
  }
}

class $ClassMembershipsTable extends ClassMemberships
    with TableInfo<$ClassMembershipsTable, ClassMembership> {
  @override
  final GeneratedDatabase attachedDatabase;
  final String? _alias;
  $ClassMembershipsTable(this.attachedDatabase, [this._alias]);
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
  static const VerificationMeta _classIdMeta = const VerificationMeta(
    'classId',
  );
  @override
  late final GeneratedColumn<String> classId = GeneratedColumn<String>(
    'class_id',
    aliasedName,
    false,
    type: DriftSqlType.string,
    requiredDuringInsert: true,
  );
  static const VerificationMeta _classNameMeta = const VerificationMeta(
    'className',
  );
  @override
  late final GeneratedColumn<String> className = GeneratedColumn<String>(
    'class_name',
    aliasedName,
    false,
    type: DriftSqlType.string,
    requiredDuringInsert: true,
  );
  static const VerificationMeta _joinedAtMeta = const VerificationMeta(
    'joinedAt',
  );
  @override
  late final GeneratedColumn<DateTime> joinedAt = GeneratedColumn<DateTime>(
    'joined_at',
    aliasedName,
    false,
    type: DriftSqlType.dateTime,
    requiredDuringInsert: true,
  );
  static const VerificationMeta _sharedUidMeta = const VerificationMeta(
    'sharedUid',
  );
  @override
  late final GeneratedColumn<String> sharedUid = GeneratedColumn<String>(
    'shared_uid',
    aliasedName,
    true,
    type: DriftSqlType.string,
    requiredDuringInsert: false,
  );
  static const VerificationMeta _sharedAtMeta = const VerificationMeta(
    'sharedAt',
  );
  @override
  late final GeneratedColumn<DateTime> sharedAt = GeneratedColumn<DateTime>(
    'shared_at',
    aliasedName,
    true,
    type: DriftSqlType.dateTime,
    requiredDuringInsert: false,
  );
  static const VerificationMeta _sharedSummaryMeta = const VerificationMeta(
    'sharedSummary',
  );
  @override
  late final GeneratedColumn<String> sharedSummary = GeneratedColumn<String>(
    'shared_summary',
    aliasedName,
    true,
    type: DriftSqlType.string,
    requiredDuringInsert: false,
  );
  @override
  List<GeneratedColumn> get $columns => [
    studentId,
    classId,
    className,
    joinedAt,
    sharedUid,
    sharedAt,
    sharedSummary,
  ];
  @override
  String get aliasedName => _alias ?? actualTableName;
  @override
  String get actualTableName => $name;
  static const String $name = 'class_memberships';
  @override
  VerificationContext validateIntegrity(
    Insertable<ClassMembership> instance, {
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
    if (data.containsKey('class_id')) {
      context.handle(
        _classIdMeta,
        classId.isAcceptableOrUnknown(data['class_id']!, _classIdMeta),
      );
    } else if (isInserting) {
      context.missing(_classIdMeta);
    }
    if (data.containsKey('class_name')) {
      context.handle(
        _classNameMeta,
        className.isAcceptableOrUnknown(data['class_name']!, _classNameMeta),
      );
    } else if (isInserting) {
      context.missing(_classNameMeta);
    }
    if (data.containsKey('joined_at')) {
      context.handle(
        _joinedAtMeta,
        joinedAt.isAcceptableOrUnknown(data['joined_at']!, _joinedAtMeta),
      );
    } else if (isInserting) {
      context.missing(_joinedAtMeta);
    }
    if (data.containsKey('shared_uid')) {
      context.handle(
        _sharedUidMeta,
        sharedUid.isAcceptableOrUnknown(data['shared_uid']!, _sharedUidMeta),
      );
    }
    if (data.containsKey('shared_at')) {
      context.handle(
        _sharedAtMeta,
        sharedAt.isAcceptableOrUnknown(data['shared_at']!, _sharedAtMeta),
      );
    }
    if (data.containsKey('shared_summary')) {
      context.handle(
        _sharedSummaryMeta,
        sharedSummary.isAcceptableOrUnknown(
          data['shared_summary']!,
          _sharedSummaryMeta,
        ),
      );
    }
    return context;
  }

  @override
  Set<GeneratedColumn> get $primaryKey => {studentId, classId};
  @override
  ClassMembership map(Map<String, dynamic> data, {String? tablePrefix}) {
    final effectivePrefix = tablePrefix != null ? '$tablePrefix.' : '';
    return ClassMembership(
      studentId: attachedDatabase.typeMapping.read(
        DriftSqlType.string,
        data['${effectivePrefix}student_id'],
      )!,
      classId: attachedDatabase.typeMapping.read(
        DriftSqlType.string,
        data['${effectivePrefix}class_id'],
      )!,
      className: attachedDatabase.typeMapping.read(
        DriftSqlType.string,
        data['${effectivePrefix}class_name'],
      )!,
      joinedAt: attachedDatabase.typeMapping.read(
        DriftSqlType.dateTime,
        data['${effectivePrefix}joined_at'],
      )!,
      sharedUid: attachedDatabase.typeMapping.read(
        DriftSqlType.string,
        data['${effectivePrefix}shared_uid'],
      ),
      sharedAt: attachedDatabase.typeMapping.read(
        DriftSqlType.dateTime,
        data['${effectivePrefix}shared_at'],
      ),
      sharedSummary: attachedDatabase.typeMapping.read(
        DriftSqlType.string,
        data['${effectivePrefix}shared_summary'],
      ),
    );
  }

  @override
  $ClassMembershipsTable createAlias(String alias) {
    return $ClassMembershipsTable(attachedDatabase, alias);
  }
}

class ClassMembership extends DataClass implements Insertable<ClassMembership> {
  final String studentId;
  final String classId;
  final String className;
  final DateTime joinedAt;

  /// The account the summary was last shared from, when, and what was
  /// shared (as JSON), so an unchanged summary isn't written again.
  final String? sharedUid;
  final DateTime? sharedAt;
  final String? sharedSummary;
  const ClassMembership({
    required this.studentId,
    required this.classId,
    required this.className,
    required this.joinedAt,
    this.sharedUid,
    this.sharedAt,
    this.sharedSummary,
  });
  @override
  Map<String, Expression> toColumns(bool nullToAbsent) {
    final map = <String, Expression>{};
    map['student_id'] = Variable<String>(studentId);
    map['class_id'] = Variable<String>(classId);
    map['class_name'] = Variable<String>(className);
    map['joined_at'] = Variable<DateTime>(joinedAt);
    if (!nullToAbsent || sharedUid != null) {
      map['shared_uid'] = Variable<String>(sharedUid);
    }
    if (!nullToAbsent || sharedAt != null) {
      map['shared_at'] = Variable<DateTime>(sharedAt);
    }
    if (!nullToAbsent || sharedSummary != null) {
      map['shared_summary'] = Variable<String>(sharedSummary);
    }
    return map;
  }

  ClassMembershipsCompanion toCompanion(bool nullToAbsent) {
    return ClassMembershipsCompanion(
      studentId: Value(studentId),
      classId: Value(classId),
      className: Value(className),
      joinedAt: Value(joinedAt),
      sharedUid: sharedUid == null && nullToAbsent
          ? const Value.absent()
          : Value(sharedUid),
      sharedAt: sharedAt == null && nullToAbsent
          ? const Value.absent()
          : Value(sharedAt),
      sharedSummary: sharedSummary == null && nullToAbsent
          ? const Value.absent()
          : Value(sharedSummary),
    );
  }

  factory ClassMembership.fromJson(
    Map<String, dynamic> json, {
    ValueSerializer? serializer,
  }) {
    serializer ??= driftRuntimeOptions.defaultSerializer;
    return ClassMembership(
      studentId: serializer.fromJson<String>(json['studentId']),
      classId: serializer.fromJson<String>(json['classId']),
      className: serializer.fromJson<String>(json['className']),
      joinedAt: serializer.fromJson<DateTime>(json['joinedAt']),
      sharedUid: serializer.fromJson<String?>(json['sharedUid']),
      sharedAt: serializer.fromJson<DateTime?>(json['sharedAt']),
      sharedSummary: serializer.fromJson<String?>(json['sharedSummary']),
    );
  }
  @override
  Map<String, dynamic> toJson({ValueSerializer? serializer}) {
    serializer ??= driftRuntimeOptions.defaultSerializer;
    return <String, dynamic>{
      'studentId': serializer.toJson<String>(studentId),
      'classId': serializer.toJson<String>(classId),
      'className': serializer.toJson<String>(className),
      'joinedAt': serializer.toJson<DateTime>(joinedAt),
      'sharedUid': serializer.toJson<String?>(sharedUid),
      'sharedAt': serializer.toJson<DateTime?>(sharedAt),
      'sharedSummary': serializer.toJson<String?>(sharedSummary),
    };
  }

  ClassMembership copyWith({
    String? studentId,
    String? classId,
    String? className,
    DateTime? joinedAt,
    Value<String?> sharedUid = const Value.absent(),
    Value<DateTime?> sharedAt = const Value.absent(),
    Value<String?> sharedSummary = const Value.absent(),
  }) => ClassMembership(
    studentId: studentId ?? this.studentId,
    classId: classId ?? this.classId,
    className: className ?? this.className,
    joinedAt: joinedAt ?? this.joinedAt,
    sharedUid: sharedUid.present ? sharedUid.value : this.sharedUid,
    sharedAt: sharedAt.present ? sharedAt.value : this.sharedAt,
    sharedSummary: sharedSummary.present
        ? sharedSummary.value
        : this.sharedSummary,
  );
  ClassMembership copyWithCompanion(ClassMembershipsCompanion data) {
    return ClassMembership(
      studentId: data.studentId.present ? data.studentId.value : this.studentId,
      classId: data.classId.present ? data.classId.value : this.classId,
      className: data.className.present ? data.className.value : this.className,
      joinedAt: data.joinedAt.present ? data.joinedAt.value : this.joinedAt,
      sharedUid: data.sharedUid.present ? data.sharedUid.value : this.sharedUid,
      sharedAt: data.sharedAt.present ? data.sharedAt.value : this.sharedAt,
      sharedSummary: data.sharedSummary.present
          ? data.sharedSummary.value
          : this.sharedSummary,
    );
  }

  @override
  String toString() {
    return (StringBuffer('ClassMembership(')
          ..write('studentId: $studentId, ')
          ..write('classId: $classId, ')
          ..write('className: $className, ')
          ..write('joinedAt: $joinedAt, ')
          ..write('sharedUid: $sharedUid, ')
          ..write('sharedAt: $sharedAt, ')
          ..write('sharedSummary: $sharedSummary')
          ..write(')'))
        .toString();
  }

  @override
  int get hashCode => Object.hash(
    studentId,
    classId,
    className,
    joinedAt,
    sharedUid,
    sharedAt,
    sharedSummary,
  );
  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      (other is ClassMembership &&
          other.studentId == this.studentId &&
          other.classId == this.classId &&
          other.className == this.className &&
          other.joinedAt == this.joinedAt &&
          other.sharedUid == this.sharedUid &&
          other.sharedAt == this.sharedAt &&
          other.sharedSummary == this.sharedSummary);
}

class ClassMembershipsCompanion extends UpdateCompanion<ClassMembership> {
  final Value<String> studentId;
  final Value<String> classId;
  final Value<String> className;
  final Value<DateTime> joinedAt;
  final Value<String?> sharedUid;
  final Value<DateTime?> sharedAt;
  final Value<String?> sharedSummary;
  final Value<int> rowid;
  const ClassMembershipsCompanion({
    this.studentId = const Value.absent(),
    this.classId = const Value.absent(),
    this.className = const Value.absent(),
    this.joinedAt = const Value.absent(),
    this.sharedUid = const Value.absent(),
    this.sharedAt = const Value.absent(),
    this.sharedSummary = const Value.absent(),
    this.rowid = const Value.absent(),
  });
  ClassMembershipsCompanion.insert({
    required String studentId,
    required String classId,
    required String className,
    required DateTime joinedAt,
    this.sharedUid = const Value.absent(),
    this.sharedAt = const Value.absent(),
    this.sharedSummary = const Value.absent(),
    this.rowid = const Value.absent(),
  }) : studentId = Value(studentId),
       classId = Value(classId),
       className = Value(className),
       joinedAt = Value(joinedAt);
  static Insertable<ClassMembership> custom({
    Expression<String>? studentId,
    Expression<String>? classId,
    Expression<String>? className,
    Expression<DateTime>? joinedAt,
    Expression<String>? sharedUid,
    Expression<DateTime>? sharedAt,
    Expression<String>? sharedSummary,
    Expression<int>? rowid,
  }) {
    return RawValuesInsertable({
      if (studentId != null) 'student_id': studentId,
      if (classId != null) 'class_id': classId,
      if (className != null) 'class_name': className,
      if (joinedAt != null) 'joined_at': joinedAt,
      if (sharedUid != null) 'shared_uid': sharedUid,
      if (sharedAt != null) 'shared_at': sharedAt,
      if (sharedSummary != null) 'shared_summary': sharedSummary,
      if (rowid != null) 'rowid': rowid,
    });
  }

  ClassMembershipsCompanion copyWith({
    Value<String>? studentId,
    Value<String>? classId,
    Value<String>? className,
    Value<DateTime>? joinedAt,
    Value<String?>? sharedUid,
    Value<DateTime?>? sharedAt,
    Value<String?>? sharedSummary,
    Value<int>? rowid,
  }) {
    return ClassMembershipsCompanion(
      studentId: studentId ?? this.studentId,
      classId: classId ?? this.classId,
      className: className ?? this.className,
      joinedAt: joinedAt ?? this.joinedAt,
      sharedUid: sharedUid ?? this.sharedUid,
      sharedAt: sharedAt ?? this.sharedAt,
      sharedSummary: sharedSummary ?? this.sharedSummary,
      rowid: rowid ?? this.rowid,
    );
  }

  @override
  Map<String, Expression> toColumns(bool nullToAbsent) {
    final map = <String, Expression>{};
    if (studentId.present) {
      map['student_id'] = Variable<String>(studentId.value);
    }
    if (classId.present) {
      map['class_id'] = Variable<String>(classId.value);
    }
    if (className.present) {
      map['class_name'] = Variable<String>(className.value);
    }
    if (joinedAt.present) {
      map['joined_at'] = Variable<DateTime>(joinedAt.value);
    }
    if (sharedUid.present) {
      map['shared_uid'] = Variable<String>(sharedUid.value);
    }
    if (sharedAt.present) {
      map['shared_at'] = Variable<DateTime>(sharedAt.value);
    }
    if (sharedSummary.present) {
      map['shared_summary'] = Variable<String>(sharedSummary.value);
    }
    if (rowid.present) {
      map['rowid'] = Variable<int>(rowid.value);
    }
    return map;
  }

  @override
  String toString() {
    return (StringBuffer('ClassMembershipsCompanion(')
          ..write('studentId: $studentId, ')
          ..write('classId: $classId, ')
          ..write('className: $className, ')
          ..write('joinedAt: $joinedAt, ')
          ..write('sharedUid: $sharedUid, ')
          ..write('sharedAt: $sharedAt, ')
          ..write('sharedSummary: $sharedSummary, ')
          ..write('rowid: $rowid')
          ..write(')'))
        .toString();
  }
}

class $ClassAssignmentsTable extends ClassAssignments
    with TableInfo<$ClassAssignmentsTable, ClassAssignment> {
  @override
  final GeneratedDatabase attachedDatabase;
  final String? _alias;
  $ClassAssignmentsTable(this.attachedDatabase, [this._alias]);
  static const VerificationMeta _classIdMeta = const VerificationMeta(
    'classId',
  );
  @override
  late final GeneratedColumn<String> classId = GeneratedColumn<String>(
    'class_id',
    aliasedName,
    false,
    type: DriftSqlType.string,
    requiredDuringInsert: true,
  );
  static const VerificationMeta _idMeta = const VerificationMeta('id');
  @override
  late final GeneratedColumn<String> id = GeneratedColumn<String>(
    'id',
    aliasedName,
    false,
    type: DriftSqlType.string,
    requiredDuringInsert: true,
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
  static const VerificationMeta _dueMeta = const VerificationMeta('due');
  @override
  late final GeneratedColumn<DateTime> due = GeneratedColumn<DateTime>(
    'due',
    aliasedName,
    true,
    type: DriftSqlType.dateTime,
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
  @override
  List<GeneratedColumn> get $columns => [classId, id, lessonId, due, createdAt];
  @override
  String get aliasedName => _alias ?? actualTableName;
  @override
  String get actualTableName => $name;
  static const String $name = 'class_assignments';
  @override
  VerificationContext validateIntegrity(
    Insertable<ClassAssignment> instance, {
    bool isInserting = false,
  }) {
    final context = VerificationContext();
    final data = instance.toColumns(true);
    if (data.containsKey('class_id')) {
      context.handle(
        _classIdMeta,
        classId.isAcceptableOrUnknown(data['class_id']!, _classIdMeta),
      );
    } else if (isInserting) {
      context.missing(_classIdMeta);
    }
    if (data.containsKey('id')) {
      context.handle(_idMeta, id.isAcceptableOrUnknown(data['id']!, _idMeta));
    } else if (isInserting) {
      context.missing(_idMeta);
    }
    if (data.containsKey('lesson_id')) {
      context.handle(
        _lessonIdMeta,
        lessonId.isAcceptableOrUnknown(data['lesson_id']!, _lessonIdMeta),
      );
    } else if (isInserting) {
      context.missing(_lessonIdMeta);
    }
    if (data.containsKey('due')) {
      context.handle(
        _dueMeta,
        due.isAcceptableOrUnknown(data['due']!, _dueMeta),
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
    return context;
  }

  @override
  Set<GeneratedColumn> get $primaryKey => {classId, id};
  @override
  ClassAssignment map(Map<String, dynamic> data, {String? tablePrefix}) {
    final effectivePrefix = tablePrefix != null ? '$tablePrefix.' : '';
    return ClassAssignment(
      classId: attachedDatabase.typeMapping.read(
        DriftSqlType.string,
        data['${effectivePrefix}class_id'],
      )!,
      id: attachedDatabase.typeMapping.read(
        DriftSqlType.string,
        data['${effectivePrefix}id'],
      )!,
      lessonId: attachedDatabase.typeMapping.read(
        DriftSqlType.string,
        data['${effectivePrefix}lesson_id'],
      )!,
      due: attachedDatabase.typeMapping.read(
        DriftSqlType.dateTime,
        data['${effectivePrefix}due'],
      ),
      createdAt: attachedDatabase.typeMapping.read(
        DriftSqlType.dateTime,
        data['${effectivePrefix}created_at'],
      )!,
    );
  }

  @override
  $ClassAssignmentsTable createAlias(String alias) {
    return $ClassAssignmentsTable(attachedDatabase, alias);
  }
}

class ClassAssignment extends DataClass implements Insertable<ClassAssignment> {
  final String classId;
  final String id;
  final String lessonId;
  final DateTime? due;
  final DateTime createdAt;
  const ClassAssignment({
    required this.classId,
    required this.id,
    required this.lessonId,
    this.due,
    required this.createdAt,
  });
  @override
  Map<String, Expression> toColumns(bool nullToAbsent) {
    final map = <String, Expression>{};
    map['class_id'] = Variable<String>(classId);
    map['id'] = Variable<String>(id);
    map['lesson_id'] = Variable<String>(lessonId);
    if (!nullToAbsent || due != null) {
      map['due'] = Variable<DateTime>(due);
    }
    map['created_at'] = Variable<DateTime>(createdAt);
    return map;
  }

  ClassAssignmentsCompanion toCompanion(bool nullToAbsent) {
    return ClassAssignmentsCompanion(
      classId: Value(classId),
      id: Value(id),
      lessonId: Value(lessonId),
      due: due == null && nullToAbsent ? const Value.absent() : Value(due),
      createdAt: Value(createdAt),
    );
  }

  factory ClassAssignment.fromJson(
    Map<String, dynamic> json, {
    ValueSerializer? serializer,
  }) {
    serializer ??= driftRuntimeOptions.defaultSerializer;
    return ClassAssignment(
      classId: serializer.fromJson<String>(json['classId']),
      id: serializer.fromJson<String>(json['id']),
      lessonId: serializer.fromJson<String>(json['lessonId']),
      due: serializer.fromJson<DateTime?>(json['due']),
      createdAt: serializer.fromJson<DateTime>(json['createdAt']),
    );
  }
  @override
  Map<String, dynamic> toJson({ValueSerializer? serializer}) {
    serializer ??= driftRuntimeOptions.defaultSerializer;
    return <String, dynamic>{
      'classId': serializer.toJson<String>(classId),
      'id': serializer.toJson<String>(id),
      'lessonId': serializer.toJson<String>(lessonId),
      'due': serializer.toJson<DateTime?>(due),
      'createdAt': serializer.toJson<DateTime>(createdAt),
    };
  }

  ClassAssignment copyWith({
    String? classId,
    String? id,
    String? lessonId,
    Value<DateTime?> due = const Value.absent(),
    DateTime? createdAt,
  }) => ClassAssignment(
    classId: classId ?? this.classId,
    id: id ?? this.id,
    lessonId: lessonId ?? this.lessonId,
    due: due.present ? due.value : this.due,
    createdAt: createdAt ?? this.createdAt,
  );
  ClassAssignment copyWithCompanion(ClassAssignmentsCompanion data) {
    return ClassAssignment(
      classId: data.classId.present ? data.classId.value : this.classId,
      id: data.id.present ? data.id.value : this.id,
      lessonId: data.lessonId.present ? data.lessonId.value : this.lessonId,
      due: data.due.present ? data.due.value : this.due,
      createdAt: data.createdAt.present ? data.createdAt.value : this.createdAt,
    );
  }

  @override
  String toString() {
    return (StringBuffer('ClassAssignment(')
          ..write('classId: $classId, ')
          ..write('id: $id, ')
          ..write('lessonId: $lessonId, ')
          ..write('due: $due, ')
          ..write('createdAt: $createdAt')
          ..write(')'))
        .toString();
  }

  @override
  int get hashCode => Object.hash(classId, id, lessonId, due, createdAt);
  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      (other is ClassAssignment &&
          other.classId == this.classId &&
          other.id == this.id &&
          other.lessonId == this.lessonId &&
          other.due == this.due &&
          other.createdAt == this.createdAt);
}

class ClassAssignmentsCompanion extends UpdateCompanion<ClassAssignment> {
  final Value<String> classId;
  final Value<String> id;
  final Value<String> lessonId;
  final Value<DateTime?> due;
  final Value<DateTime> createdAt;
  final Value<int> rowid;
  const ClassAssignmentsCompanion({
    this.classId = const Value.absent(),
    this.id = const Value.absent(),
    this.lessonId = const Value.absent(),
    this.due = const Value.absent(),
    this.createdAt = const Value.absent(),
    this.rowid = const Value.absent(),
  });
  ClassAssignmentsCompanion.insert({
    required String classId,
    required String id,
    required String lessonId,
    this.due = const Value.absent(),
    required DateTime createdAt,
    this.rowid = const Value.absent(),
  }) : classId = Value(classId),
       id = Value(id),
       lessonId = Value(lessonId),
       createdAt = Value(createdAt);
  static Insertable<ClassAssignment> custom({
    Expression<String>? classId,
    Expression<String>? id,
    Expression<String>? lessonId,
    Expression<DateTime>? due,
    Expression<DateTime>? createdAt,
    Expression<int>? rowid,
  }) {
    return RawValuesInsertable({
      if (classId != null) 'class_id': classId,
      if (id != null) 'id': id,
      if (lessonId != null) 'lesson_id': lessonId,
      if (due != null) 'due': due,
      if (createdAt != null) 'created_at': createdAt,
      if (rowid != null) 'rowid': rowid,
    });
  }

  ClassAssignmentsCompanion copyWith({
    Value<String>? classId,
    Value<String>? id,
    Value<String>? lessonId,
    Value<DateTime?>? due,
    Value<DateTime>? createdAt,
    Value<int>? rowid,
  }) {
    return ClassAssignmentsCompanion(
      classId: classId ?? this.classId,
      id: id ?? this.id,
      lessonId: lessonId ?? this.lessonId,
      due: due ?? this.due,
      createdAt: createdAt ?? this.createdAt,
      rowid: rowid ?? this.rowid,
    );
  }

  @override
  Map<String, Expression> toColumns(bool nullToAbsent) {
    final map = <String, Expression>{};
    if (classId.present) {
      map['class_id'] = Variable<String>(classId.value);
    }
    if (id.present) {
      map['id'] = Variable<String>(id.value);
    }
    if (lessonId.present) {
      map['lesson_id'] = Variable<String>(lessonId.value);
    }
    if (due.present) {
      map['due'] = Variable<DateTime>(due.value);
    }
    if (createdAt.present) {
      map['created_at'] = Variable<DateTime>(createdAt.value);
    }
    if (rowid.present) {
      map['rowid'] = Variable<int>(rowid.value);
    }
    return map;
  }

  @override
  String toString() {
    return (StringBuffer('ClassAssignmentsCompanion(')
          ..write('classId: $classId, ')
          ..write('id: $id, ')
          ..write('lessonId: $lessonId, ')
          ..write('due: $due, ')
          ..write('createdAt: $createdAt, ')
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
  late final $AiQueueTable aiQueue = $AiQueueTable(this);
  late final $DownloadedLessonsTable downloadedLessons =
      $DownloadedLessonsTable(this);
  late final $ClassMembershipsTable classMemberships = $ClassMembershipsTable(
    this,
  );
  late final $ClassAssignmentsTable classAssignments = $ClassAssignmentsTable(
    this,
  );
  @override
  Iterable<TableInfo<Table, Object?>> get allTables =>
      allSchemaEntities.whereType<TableInfo<Table, Object?>>();
  @override
  List<DatabaseSchemaEntity> get allSchemaEntities => [
    students,
    lessonProgressTable,
    stepResults,
    skillStates,
    aiQueue,
    downloadedLessons,
    classMemberships,
    classAssignments,
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

  static MultiTypedResultKey<$AiQueueTable, List<QueuedAnswer>>
  _aiQueueRefsTable(_$LocalDb db) => MultiTypedResultKey.fromTable(
    db.aiQueue,
    aliasName: 'students__id__ai_queue__student_id',
  );

  $$AiQueueTableProcessedTableManager get aiQueueRefs {
    final manager = $$AiQueueTableTableManager(
      $_db,
      $_db.aiQueue,
    ).filter((f) => f.studentId.id.sqlEquals($_itemColumn<String>('id')!));

    final cache = $_typedResult.readTableOrNull(_aiQueueRefsTable($_db));
    return ProcessedTableManager(
      manager.$state.copyWith(prefetchedData: cache),
    );
  }

  static MultiTypedResultKey<$ClassMembershipsTable, List<ClassMembership>>
  _classMembershipsRefsTable(_$LocalDb db) => MultiTypedResultKey.fromTable(
    db.classMemberships,
    aliasName: 'students__id__class_memberships__student_id',
  );

  $$ClassMembershipsTableProcessedTableManager get classMembershipsRefs {
    final manager = $$ClassMembershipsTableTableManager(
      $_db,
      $_db.classMemberships,
    ).filter((f) => f.studentId.id.sqlEquals($_itemColumn<String>('id')!));

    final cache = $_typedResult.readTableOrNull(
      _classMembershipsRefsTable($_db),
    );
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

  Expression<bool> aiQueueRefs(
    Expression<bool> Function($$AiQueueTableFilterComposer f) f,
  ) {
    final $$AiQueueTableFilterComposer composer = $composerBuilder(
      composer: this,
      getCurrentColumn: (t) => t.id,
      referencedTable: $db.aiQueue,
      getReferencedColumn: (t) => t.studentId,
      builder:
          (
            joinBuilder, {
            $addJoinBuilderToRootComposer,
            $removeJoinBuilderFromRootComposer,
          }) => $$AiQueueTableFilterComposer(
            $db: $db,
            $table: $db.aiQueue,
            $addJoinBuilderToRootComposer: $addJoinBuilderToRootComposer,
            joinBuilder: joinBuilder,
            $removeJoinBuilderFromRootComposer:
                $removeJoinBuilderFromRootComposer,
          ),
    );
    return f(composer);
  }

  Expression<bool> classMembershipsRefs(
    Expression<bool> Function($$ClassMembershipsTableFilterComposer f) f,
  ) {
    final $$ClassMembershipsTableFilterComposer composer = $composerBuilder(
      composer: this,
      getCurrentColumn: (t) => t.id,
      referencedTable: $db.classMemberships,
      getReferencedColumn: (t) => t.studentId,
      builder:
          (
            joinBuilder, {
            $addJoinBuilderToRootComposer,
            $removeJoinBuilderFromRootComposer,
          }) => $$ClassMembershipsTableFilterComposer(
            $db: $db,
            $table: $db.classMemberships,
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

  Expression<T> aiQueueRefs<T extends Object>(
    Expression<T> Function($$AiQueueTableAnnotationComposer a) f,
  ) {
    final $$AiQueueTableAnnotationComposer composer = $composerBuilder(
      composer: this,
      getCurrentColumn: (t) => t.id,
      referencedTable: $db.aiQueue,
      getReferencedColumn: (t) => t.studentId,
      builder:
          (
            joinBuilder, {
            $addJoinBuilderToRootComposer,
            $removeJoinBuilderFromRootComposer,
          }) => $$AiQueueTableAnnotationComposer(
            $db: $db,
            $table: $db.aiQueue,
            $addJoinBuilderToRootComposer: $addJoinBuilderToRootComposer,
            joinBuilder: joinBuilder,
            $removeJoinBuilderFromRootComposer:
                $removeJoinBuilderFromRootComposer,
          ),
    );
    return f(composer);
  }

  Expression<T> classMembershipsRefs<T extends Object>(
    Expression<T> Function($$ClassMembershipsTableAnnotationComposer a) f,
  ) {
    final $$ClassMembershipsTableAnnotationComposer composer = $composerBuilder(
      composer: this,
      getCurrentColumn: (t) => t.id,
      referencedTable: $db.classMemberships,
      getReferencedColumn: (t) => t.studentId,
      builder:
          (
            joinBuilder, {
            $addJoinBuilderToRootComposer,
            $removeJoinBuilderFromRootComposer,
          }) => $$ClassMembershipsTableAnnotationComposer(
            $db: $db,
            $table: $db.classMemberships,
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
            bool aiQueueRefs,
            bool classMembershipsRefs,
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
                aiQueueRefs = false,
                classMembershipsRefs = false,
              }) {
                return PrefetchHooks(
                  db: db,
                  explicitlyWatchedTables: [
                    if (lessonProgressTableRefs) db.lessonProgressTable,
                    if (stepResultsRefs) db.stepResults,
                    if (skillStatesRefs) db.skillStates,
                    if (aiQueueRefs) db.aiQueue,
                    if (classMembershipsRefs) db.classMemberships,
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
                      if (aiQueueRefs)
                        await $_getPrefetchedData<
                          Student,
                          $StudentsTable,
                          QueuedAnswer
                        >(
                          currentTable: table,
                          referencedTable: $$StudentsTableReferences
                              ._aiQueueRefsTable(db),
                          managerFromTypedResult: (p0) =>
                              $$StudentsTableReferences(
                                db,
                                table,
                                p0,
                              ).aiQueueRefs,
                          referencedItemsForCurrentItem:
                              (item, referencedItems) => referencedItems.where(
                                (e) => e.studentId == item.id,
                              ),
                          typedResults: items,
                        ),
                      if (classMembershipsRefs)
                        await $_getPrefetchedData<
                          Student,
                          $StudentsTable,
                          ClassMembership
                        >(
                          currentTable: table,
                          referencedTable: $$StudentsTableReferences
                              ._classMembershipsRefsTable(db),
                          managerFromTypedResult: (p0) =>
                              $$StudentsTableReferences(
                                db,
                                table,
                                p0,
                              ).classMembershipsRefs,
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
        bool aiQueueRefs,
        bool classMembershipsRefs,
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
typedef $$AiQueueTableCreateCompanionBuilder = AiQueueCompanion Function({
  required String id,
  required String studentId,
  required String lessonId,
  required String stepId,
  required String task,
  required String lang,
  required String answer,
  required DateTime createdAt,
  Value<bool> uploaded,
  Value<String> status,
  Value<String?> level,
  Value<String?> reply,
  Value<bool> seen,
  Value<int> rowid,
});
typedef $$AiQueueTableUpdateCompanionBuilder = AiQueueCompanion Function({
  Value<String> id,
  Value<String> studentId,
  Value<String> lessonId,
  Value<String> stepId,
  Value<String> task,
  Value<String> lang,
  Value<String> answer,
  Value<DateTime> createdAt,
  Value<bool> uploaded,
  Value<String> status,
  Value<String?> level,
  Value<String?> reply,
  Value<bool> seen,
  Value<int> rowid,
});

final class $$AiQueueTableReferences
    extends BaseReferences<_$LocalDb, $AiQueueTable, QueuedAnswer> {
  $$AiQueueTableReferences(super.$_db, super.$_table, super.$_typedResult);

  static $StudentsTable _studentIdTable(_$LocalDb db) =>
      db.students.createAlias('ai_queue__student_id__students__id');

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

class $$AiQueueTableFilterComposer extends Composer<_$LocalDb, $AiQueueTable> {
  $$AiQueueTableFilterComposer({
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

  ColumnFilters<String> get lessonId => $composableBuilder(
    column: $table.lessonId,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<String> get stepId => $composableBuilder(
    column: $table.stepId,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<String> get task => $composableBuilder(
    column: $table.task,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<String> get lang => $composableBuilder(
    column: $table.lang,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<String> get answer => $composableBuilder(
    column: $table.answer,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<DateTime> get createdAt => $composableBuilder(
    column: $table.createdAt,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<bool> get uploaded => $composableBuilder(
    column: $table.uploaded,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<String> get status => $composableBuilder(
    column: $table.status,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<String> get level => $composableBuilder(
    column: $table.level,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<String> get reply => $composableBuilder(
    column: $table.reply,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<bool> get seen => $composableBuilder(
    column: $table.seen,
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

class $$AiQueueTableOrderingComposer
    extends Composer<_$LocalDb, $AiQueueTable> {
  $$AiQueueTableOrderingComposer({
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

  ColumnOrderings<String> get lessonId => $composableBuilder(
    column: $table.lessonId,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<String> get stepId => $composableBuilder(
    column: $table.stepId,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<String> get task => $composableBuilder(
    column: $table.task,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<String> get lang => $composableBuilder(
    column: $table.lang,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<String> get answer => $composableBuilder(
    column: $table.answer,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<DateTime> get createdAt => $composableBuilder(
    column: $table.createdAt,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<bool> get uploaded => $composableBuilder(
    column: $table.uploaded,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<String> get status => $composableBuilder(
    column: $table.status,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<String> get level => $composableBuilder(
    column: $table.level,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<String> get reply => $composableBuilder(
    column: $table.reply,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<bool> get seen => $composableBuilder(
    column: $table.seen,
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

class $$AiQueueTableAnnotationComposer
    extends Composer<_$LocalDb, $AiQueueTable> {
  $$AiQueueTableAnnotationComposer({
    required super.$db,
    required super.$table,
    super.joinBuilder,
    super.$addJoinBuilderToRootComposer,
    super.$removeJoinBuilderFromRootComposer,
  });
  GeneratedColumn<String> get id =>
      $composableBuilder(column: $table.id, builder: (column) => column);

  GeneratedColumn<String> get lessonId =>
      $composableBuilder(column: $table.lessonId, builder: (column) => column);

  GeneratedColumn<String> get stepId =>
      $composableBuilder(column: $table.stepId, builder: (column) => column);

  GeneratedColumn<String> get task =>
      $composableBuilder(column: $table.task, builder: (column) => column);

  GeneratedColumn<String> get lang =>
      $composableBuilder(column: $table.lang, builder: (column) => column);

  GeneratedColumn<String> get answer =>
      $composableBuilder(column: $table.answer, builder: (column) => column);

  GeneratedColumn<DateTime> get createdAt =>
      $composableBuilder(column: $table.createdAt, builder: (column) => column);

  GeneratedColumn<bool> get uploaded =>
      $composableBuilder(column: $table.uploaded, builder: (column) => column);

  GeneratedColumn<String> get status =>
      $composableBuilder(column: $table.status, builder: (column) => column);

  GeneratedColumn<String> get level =>
      $composableBuilder(column: $table.level, builder: (column) => column);

  GeneratedColumn<String> get reply =>
      $composableBuilder(column: $table.reply, builder: (column) => column);

  GeneratedColumn<bool> get seen =>
      $composableBuilder(column: $table.seen, builder: (column) => column);

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

class $$AiQueueTableTableManager
    extends
        RootTableManager<
          _$LocalDb,
          $AiQueueTable,
          QueuedAnswer,
          $$AiQueueTableFilterComposer,
          $$AiQueueTableOrderingComposer,
          $$AiQueueTableAnnotationComposer,
          $$AiQueueTableCreateCompanionBuilder,
          $$AiQueueTableUpdateCompanionBuilder,
          (QueuedAnswer, $$AiQueueTableReferences),
          QueuedAnswer,
          PrefetchHooks Function({bool studentId})
        > {
  $$AiQueueTableTableManager(_$LocalDb db, $AiQueueTable table)
    : super(
        TableManagerState(
          db: db,
          table: table,
          createFilteringComposer: () =>
              $$AiQueueTableFilterComposer($db: db, $table: table),
          createOrderingComposer: () =>
              $$AiQueueTableOrderingComposer($db: db, $table: table),
          createComputedFieldComposer: () =>
              $$AiQueueTableAnnotationComposer($db: db, $table: table),
          updateCompanionCallback:
              ({
                Value<String> id = const Value.absent(),
                Value<String> studentId = const Value.absent(),
                Value<String> lessonId = const Value.absent(),
                Value<String> stepId = const Value.absent(),
                Value<String> task = const Value.absent(),
                Value<String> lang = const Value.absent(),
                Value<String> answer = const Value.absent(),
                Value<DateTime> createdAt = const Value.absent(),
                Value<bool> uploaded = const Value.absent(),
                Value<String> status = const Value.absent(),
                Value<String?> level = const Value.absent(),
                Value<String?> reply = const Value.absent(),
                Value<bool> seen = const Value.absent(),
                Value<int> rowid = const Value.absent(),
              }) => AiQueueCompanion(
                id: id,
                studentId: studentId,
                lessonId: lessonId,
                stepId: stepId,
                task: task,
                lang: lang,
                answer: answer,
                createdAt: createdAt,
                uploaded: uploaded,
                status: status,
                level: level,
                reply: reply,
                seen: seen,
                rowid: rowid,
              ),
          createCompanionCallback:
              ({
                required String id,
                required String studentId,
                required String lessonId,
                required String stepId,
                required String task,
                required String lang,
                required String answer,
                required DateTime createdAt,
                Value<bool> uploaded = const Value.absent(),
                Value<String> status = const Value.absent(),
                Value<String?> level = const Value.absent(),
                Value<String?> reply = const Value.absent(),
                Value<bool> seen = const Value.absent(),
                Value<int> rowid = const Value.absent(),
              }) => AiQueueCompanion.insert(
                id: id,
                studentId: studentId,
                lessonId: lessonId,
                stepId: stepId,
                task: task,
                lang: lang,
                answer: answer,
                createdAt: createdAt,
                uploaded: uploaded,
                status: status,
                level: level,
                reply: reply,
                seen: seen,
                rowid: rowid,
              ),
          withReferenceMapper: (p0) => p0
              .map(
                (e) => (
                  e.readTable<$AiQueueTable, QueuedAnswer>(table),
                  $$AiQueueTableReferences(db, table, e),
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
                        referencedTable: $$AiQueueTableReferences
                            ._studentIdTable(db),
                        referencedColumn: $$AiQueueTableReferences
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

typedef $$AiQueueTableProcessedTableManager =
    ProcessedTableManager<
      _$LocalDb,
      $AiQueueTable,
      QueuedAnswer,
      $$AiQueueTableFilterComposer,
      $$AiQueueTableOrderingComposer,
      $$AiQueueTableAnnotationComposer,
      $$AiQueueTableCreateCompanionBuilder,
      $$AiQueueTableUpdateCompanionBuilder,
      (QueuedAnswer, $$AiQueueTableReferences),
      QueuedAnswer,
      PrefetchHooks Function({bool studentId})
    >;
typedef $$DownloadedLessonsTableCreateCompanionBuilder =
    DownloadedLessonsCompanion Function({
      required String id,
      required int version,
      required String hash,
      required String content,
      required DateTime downloadedAt,
      Value<int> rowid,
    });
typedef $$DownloadedLessonsTableUpdateCompanionBuilder =
    DownloadedLessonsCompanion Function({
      Value<String> id,
      Value<int> version,
      Value<String> hash,
      Value<String> content,
      Value<DateTime> downloadedAt,
      Value<int> rowid,
    });

class $$DownloadedLessonsTableFilterComposer
    extends Composer<_$LocalDb, $DownloadedLessonsTable> {
  $$DownloadedLessonsTableFilterComposer({
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

  ColumnFilters<int> get version => $composableBuilder(
    column: $table.version,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<String> get hash => $composableBuilder(
    column: $table.hash,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<String> get content => $composableBuilder(
    column: $table.content,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<DateTime> get downloadedAt => $composableBuilder(
    column: $table.downloadedAt,
    builder: (column) => ColumnFilters(column),
  );
}

class $$DownloadedLessonsTableOrderingComposer
    extends Composer<_$LocalDb, $DownloadedLessonsTable> {
  $$DownloadedLessonsTableOrderingComposer({
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

  ColumnOrderings<int> get version => $composableBuilder(
    column: $table.version,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<String> get hash => $composableBuilder(
    column: $table.hash,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<String> get content => $composableBuilder(
    column: $table.content,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<DateTime> get downloadedAt => $composableBuilder(
    column: $table.downloadedAt,
    builder: (column) => ColumnOrderings(column),
  );
}

class $$DownloadedLessonsTableAnnotationComposer
    extends Composer<_$LocalDb, $DownloadedLessonsTable> {
  $$DownloadedLessonsTableAnnotationComposer({
    required super.$db,
    required super.$table,
    super.joinBuilder,
    super.$addJoinBuilderToRootComposer,
    super.$removeJoinBuilderFromRootComposer,
  });
  GeneratedColumn<String> get id =>
      $composableBuilder(column: $table.id, builder: (column) => column);

  GeneratedColumn<int> get version =>
      $composableBuilder(column: $table.version, builder: (column) => column);

  GeneratedColumn<String> get hash =>
      $composableBuilder(column: $table.hash, builder: (column) => column);

  GeneratedColumn<String> get content =>
      $composableBuilder(column: $table.content, builder: (column) => column);

  GeneratedColumn<DateTime> get downloadedAt => $composableBuilder(
    column: $table.downloadedAt,
    builder: (column) => column,
  );
}

class $$DownloadedLessonsTableTableManager
    extends
        RootTableManager<
          _$LocalDb,
          $DownloadedLessonsTable,
          DownloadedLesson,
          $$DownloadedLessonsTableFilterComposer,
          $$DownloadedLessonsTableOrderingComposer,
          $$DownloadedLessonsTableAnnotationComposer,
          $$DownloadedLessonsTableCreateCompanionBuilder,
          $$DownloadedLessonsTableUpdateCompanionBuilder,
          (
            DownloadedLesson,
            BaseReferences<
              _$LocalDb,
              $DownloadedLessonsTable,
              DownloadedLesson
            >,
          ),
          DownloadedLesson,
          PrefetchHooks Function()
        > {
  $$DownloadedLessonsTableTableManager(
    _$LocalDb db,
    $DownloadedLessonsTable table,
  ) : super(
        TableManagerState(
          db: db,
          table: table,
          createFilteringComposer: () =>
              $$DownloadedLessonsTableFilterComposer($db: db, $table: table),
          createOrderingComposer: () =>
              $$DownloadedLessonsTableOrderingComposer($db: db, $table: table),
          createComputedFieldComposer: () =>
              $$DownloadedLessonsTableAnnotationComposer(
                $db: db,
                $table: table,
              ),
          updateCompanionCallback:
              ({
                Value<String> id = const Value.absent(),
                Value<int> version = const Value.absent(),
                Value<String> hash = const Value.absent(),
                Value<String> content = const Value.absent(),
                Value<DateTime> downloadedAt = const Value.absent(),
                Value<int> rowid = const Value.absent(),
              }) => DownloadedLessonsCompanion(
                id: id,
                version: version,
                hash: hash,
                content: content,
                downloadedAt: downloadedAt,
                rowid: rowid,
              ),
          createCompanionCallback:
              ({
                required String id,
                required int version,
                required String hash,
                required String content,
                required DateTime downloadedAt,
                Value<int> rowid = const Value.absent(),
              }) => DownloadedLessonsCompanion.insert(
                id: id,
                version: version,
                hash: hash,
                content: content,
                downloadedAt: downloadedAt,
                rowid: rowid,
              ),
          withReferenceMapper: (p0) => p0
              .map(
                (e) => (
                  e.readTable<$DownloadedLessonsTable, DownloadedLesson>(table),
                  BaseReferences<
                    _$LocalDb,
                    $DownloadedLessonsTable,
                    DownloadedLesson
                  >(db, table, e),
                ),
              )
              .toList(),
          prefetchHooksCallback: null,
        ),
      );
}

typedef $$DownloadedLessonsTableProcessedTableManager =
    ProcessedTableManager<
      _$LocalDb,
      $DownloadedLessonsTable,
      DownloadedLesson,
      $$DownloadedLessonsTableFilterComposer,
      $$DownloadedLessonsTableOrderingComposer,
      $$DownloadedLessonsTableAnnotationComposer,
      $$DownloadedLessonsTableCreateCompanionBuilder,
      $$DownloadedLessonsTableUpdateCompanionBuilder,
      (
        DownloadedLesson,
        BaseReferences<_$LocalDb, $DownloadedLessonsTable, DownloadedLesson>,
      ),
      DownloadedLesson,
      PrefetchHooks Function()
    >;
typedef $$ClassMembershipsTableCreateCompanionBuilder =
    ClassMembershipsCompanion Function({
      required String studentId,
      required String classId,
      required String className,
      required DateTime joinedAt,
      Value<String?> sharedUid,
      Value<DateTime?> sharedAt,
      Value<String?> sharedSummary,
      Value<int> rowid,
    });
typedef $$ClassMembershipsTableUpdateCompanionBuilder =
    ClassMembershipsCompanion Function({
      Value<String> studentId,
      Value<String> classId,
      Value<String> className,
      Value<DateTime> joinedAt,
      Value<String?> sharedUid,
      Value<DateTime?> sharedAt,
      Value<String?> sharedSummary,
      Value<int> rowid,
    });

final class $$ClassMembershipsTableReferences
    extends BaseReferences<_$LocalDb, $ClassMembershipsTable, ClassMembership> {
  $$ClassMembershipsTableReferences(
    super.$_db,
    super.$_table,
    super.$_typedResult,
  );

  static $StudentsTable _studentIdTable(_$LocalDb db) =>
      db.students.createAlias('class_memberships__student_id__students__id');

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

class $$ClassMembershipsTableFilterComposer
    extends Composer<_$LocalDb, $ClassMembershipsTable> {
  $$ClassMembershipsTableFilterComposer({
    required super.$db,
    required super.$table,
    super.joinBuilder,
    super.$addJoinBuilderToRootComposer,
    super.$removeJoinBuilderFromRootComposer,
  });
  ColumnFilters<String> get classId => $composableBuilder(
    column: $table.classId,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<String> get className => $composableBuilder(
    column: $table.className,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<DateTime> get joinedAt => $composableBuilder(
    column: $table.joinedAt,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<String> get sharedUid => $composableBuilder(
    column: $table.sharedUid,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<DateTime> get sharedAt => $composableBuilder(
    column: $table.sharedAt,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<String> get sharedSummary => $composableBuilder(
    column: $table.sharedSummary,
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

class $$ClassMembershipsTableOrderingComposer
    extends Composer<_$LocalDb, $ClassMembershipsTable> {
  $$ClassMembershipsTableOrderingComposer({
    required super.$db,
    required super.$table,
    super.joinBuilder,
    super.$addJoinBuilderToRootComposer,
    super.$removeJoinBuilderFromRootComposer,
  });
  ColumnOrderings<String> get classId => $composableBuilder(
    column: $table.classId,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<String> get className => $composableBuilder(
    column: $table.className,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<DateTime> get joinedAt => $composableBuilder(
    column: $table.joinedAt,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<String> get sharedUid => $composableBuilder(
    column: $table.sharedUid,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<DateTime> get sharedAt => $composableBuilder(
    column: $table.sharedAt,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<String> get sharedSummary => $composableBuilder(
    column: $table.sharedSummary,
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

class $$ClassMembershipsTableAnnotationComposer
    extends Composer<_$LocalDb, $ClassMembershipsTable> {
  $$ClassMembershipsTableAnnotationComposer({
    required super.$db,
    required super.$table,
    super.joinBuilder,
    super.$addJoinBuilderToRootComposer,
    super.$removeJoinBuilderFromRootComposer,
  });
  GeneratedColumn<String> get classId =>
      $composableBuilder(column: $table.classId, builder: (column) => column);

  GeneratedColumn<String> get className =>
      $composableBuilder(column: $table.className, builder: (column) => column);

  GeneratedColumn<DateTime> get joinedAt =>
      $composableBuilder(column: $table.joinedAt, builder: (column) => column);

  GeneratedColumn<String> get sharedUid =>
      $composableBuilder(column: $table.sharedUid, builder: (column) => column);

  GeneratedColumn<DateTime> get sharedAt =>
      $composableBuilder(column: $table.sharedAt, builder: (column) => column);

  GeneratedColumn<String> get sharedSummary => $composableBuilder(
    column: $table.sharedSummary,
    builder: (column) => column,
  );

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

class $$ClassMembershipsTableTableManager
    extends
        RootTableManager<
          _$LocalDb,
          $ClassMembershipsTable,
          ClassMembership,
          $$ClassMembershipsTableFilterComposer,
          $$ClassMembershipsTableOrderingComposer,
          $$ClassMembershipsTableAnnotationComposer,
          $$ClassMembershipsTableCreateCompanionBuilder,
          $$ClassMembershipsTableUpdateCompanionBuilder,
          (ClassMembership, $$ClassMembershipsTableReferences),
          ClassMembership,
          PrefetchHooks Function({bool studentId})
        > {
  $$ClassMembershipsTableTableManager(
    _$LocalDb db,
    $ClassMembershipsTable table,
  ) : super(
        TableManagerState(
          db: db,
          table: table,
          createFilteringComposer: () =>
              $$ClassMembershipsTableFilterComposer($db: db, $table: table),
          createOrderingComposer: () =>
              $$ClassMembershipsTableOrderingComposer($db: db, $table: table),
          createComputedFieldComposer: () =>
              $$ClassMembershipsTableAnnotationComposer($db: db, $table: table),
          updateCompanionCallback:
              ({
                Value<String> studentId = const Value.absent(),
                Value<String> classId = const Value.absent(),
                Value<String> className = const Value.absent(),
                Value<DateTime> joinedAt = const Value.absent(),
                Value<String?> sharedUid = const Value.absent(),
                Value<DateTime?> sharedAt = const Value.absent(),
                Value<String?> sharedSummary = const Value.absent(),
                Value<int> rowid = const Value.absent(),
              }) => ClassMembershipsCompanion(
                studentId: studentId,
                classId: classId,
                className: className,
                joinedAt: joinedAt,
                sharedUid: sharedUid,
                sharedAt: sharedAt,
                sharedSummary: sharedSummary,
                rowid: rowid,
              ),
          createCompanionCallback:
              ({
                required String studentId,
                required String classId,
                required String className,
                required DateTime joinedAt,
                Value<String?> sharedUid = const Value.absent(),
                Value<DateTime?> sharedAt = const Value.absent(),
                Value<String?> sharedSummary = const Value.absent(),
                Value<int> rowid = const Value.absent(),
              }) => ClassMembershipsCompanion.insert(
                studentId: studentId,
                classId: classId,
                className: className,
                joinedAt: joinedAt,
                sharedUid: sharedUid,
                sharedAt: sharedAt,
                sharedSummary: sharedSummary,
                rowid: rowid,
              ),
          withReferenceMapper: (p0) => p0
              .map(
                (e) => (
                  e.readTable<$ClassMembershipsTable, ClassMembership>(table),
                  $$ClassMembershipsTableReferences(db, table, e),
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
                        referencedTable: $$ClassMembershipsTableReferences
                            ._studentIdTable(db),
                        referencedColumn: $$ClassMembershipsTableReferences
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

typedef $$ClassMembershipsTableProcessedTableManager =
    ProcessedTableManager<
      _$LocalDb,
      $ClassMembershipsTable,
      ClassMembership,
      $$ClassMembershipsTableFilterComposer,
      $$ClassMembershipsTableOrderingComposer,
      $$ClassMembershipsTableAnnotationComposer,
      $$ClassMembershipsTableCreateCompanionBuilder,
      $$ClassMembershipsTableUpdateCompanionBuilder,
      (ClassMembership, $$ClassMembershipsTableReferences),
      ClassMembership,
      PrefetchHooks Function({bool studentId})
    >;
typedef $$ClassAssignmentsTableCreateCompanionBuilder =
    ClassAssignmentsCompanion Function({
      required String classId,
      required String id,
      required String lessonId,
      Value<DateTime?> due,
      required DateTime createdAt,
      Value<int> rowid,
    });
typedef $$ClassAssignmentsTableUpdateCompanionBuilder =
    ClassAssignmentsCompanion Function({
      Value<String> classId,
      Value<String> id,
      Value<String> lessonId,
      Value<DateTime?> due,
      Value<DateTime> createdAt,
      Value<int> rowid,
    });

class $$ClassAssignmentsTableFilterComposer
    extends Composer<_$LocalDb, $ClassAssignmentsTable> {
  $$ClassAssignmentsTableFilterComposer({
    required super.$db,
    required super.$table,
    super.joinBuilder,
    super.$addJoinBuilderToRootComposer,
    super.$removeJoinBuilderFromRootComposer,
  });
  ColumnFilters<String> get classId => $composableBuilder(
    column: $table.classId,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<String> get id => $composableBuilder(
    column: $table.id,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<String> get lessonId => $composableBuilder(
    column: $table.lessonId,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<DateTime> get due => $composableBuilder(
    column: $table.due,
    builder: (column) => ColumnFilters(column),
  );

  ColumnFilters<DateTime> get createdAt => $composableBuilder(
    column: $table.createdAt,
    builder: (column) => ColumnFilters(column),
  );
}

class $$ClassAssignmentsTableOrderingComposer
    extends Composer<_$LocalDb, $ClassAssignmentsTable> {
  $$ClassAssignmentsTableOrderingComposer({
    required super.$db,
    required super.$table,
    super.joinBuilder,
    super.$addJoinBuilderToRootComposer,
    super.$removeJoinBuilderFromRootComposer,
  });
  ColumnOrderings<String> get classId => $composableBuilder(
    column: $table.classId,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<String> get id => $composableBuilder(
    column: $table.id,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<String> get lessonId => $composableBuilder(
    column: $table.lessonId,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<DateTime> get due => $composableBuilder(
    column: $table.due,
    builder: (column) => ColumnOrderings(column),
  );

  ColumnOrderings<DateTime> get createdAt => $composableBuilder(
    column: $table.createdAt,
    builder: (column) => ColumnOrderings(column),
  );
}

class $$ClassAssignmentsTableAnnotationComposer
    extends Composer<_$LocalDb, $ClassAssignmentsTable> {
  $$ClassAssignmentsTableAnnotationComposer({
    required super.$db,
    required super.$table,
    super.joinBuilder,
    super.$addJoinBuilderToRootComposer,
    super.$removeJoinBuilderFromRootComposer,
  });
  GeneratedColumn<String> get classId =>
      $composableBuilder(column: $table.classId, builder: (column) => column);

  GeneratedColumn<String> get id =>
      $composableBuilder(column: $table.id, builder: (column) => column);

  GeneratedColumn<String> get lessonId =>
      $composableBuilder(column: $table.lessonId, builder: (column) => column);

  GeneratedColumn<DateTime> get due =>
      $composableBuilder(column: $table.due, builder: (column) => column);

  GeneratedColumn<DateTime> get createdAt =>
      $composableBuilder(column: $table.createdAt, builder: (column) => column);
}

class $$ClassAssignmentsTableTableManager
    extends
        RootTableManager<
          _$LocalDb,
          $ClassAssignmentsTable,
          ClassAssignment,
          $$ClassAssignmentsTableFilterComposer,
          $$ClassAssignmentsTableOrderingComposer,
          $$ClassAssignmentsTableAnnotationComposer,
          $$ClassAssignmentsTableCreateCompanionBuilder,
          $$ClassAssignmentsTableUpdateCompanionBuilder,
          (
            ClassAssignment,
            BaseReferences<_$LocalDb, $ClassAssignmentsTable, ClassAssignment>,
          ),
          ClassAssignment,
          PrefetchHooks Function()
        > {
  $$ClassAssignmentsTableTableManager(
    _$LocalDb db,
    $ClassAssignmentsTable table,
  ) : super(
        TableManagerState(
          db: db,
          table: table,
          createFilteringComposer: () =>
              $$ClassAssignmentsTableFilterComposer($db: db, $table: table),
          createOrderingComposer: () =>
              $$ClassAssignmentsTableOrderingComposer($db: db, $table: table),
          createComputedFieldComposer: () =>
              $$ClassAssignmentsTableAnnotationComposer($db: db, $table: table),
          updateCompanionCallback:
              ({
                Value<String> classId = const Value.absent(),
                Value<String> id = const Value.absent(),
                Value<String> lessonId = const Value.absent(),
                Value<DateTime?> due = const Value.absent(),
                Value<DateTime> createdAt = const Value.absent(),
                Value<int> rowid = const Value.absent(),
              }) => ClassAssignmentsCompanion(
                classId: classId,
                id: id,
                lessonId: lessonId,
                due: due,
                createdAt: createdAt,
                rowid: rowid,
              ),
          createCompanionCallback:
              ({
                required String classId,
                required String id,
                required String lessonId,
                Value<DateTime?> due = const Value.absent(),
                required DateTime createdAt,
                Value<int> rowid = const Value.absent(),
              }) => ClassAssignmentsCompanion.insert(
                classId: classId,
                id: id,
                lessonId: lessonId,
                due: due,
                createdAt: createdAt,
                rowid: rowid,
              ),
          withReferenceMapper: (p0) => p0
              .map(
                (e) => (
                  e.readTable<$ClassAssignmentsTable, ClassAssignment>(table),
                  BaseReferences<
                    _$LocalDb,
                    $ClassAssignmentsTable,
                    ClassAssignment
                  >(db, table, e),
                ),
              )
              .toList(),
          prefetchHooksCallback: null,
        ),
      );
}

typedef $$ClassAssignmentsTableProcessedTableManager =
    ProcessedTableManager<
      _$LocalDb,
      $ClassAssignmentsTable,
      ClassAssignment,
      $$ClassAssignmentsTableFilterComposer,
      $$ClassAssignmentsTableOrderingComposer,
      $$ClassAssignmentsTableAnnotationComposer,
      $$ClassAssignmentsTableCreateCompanionBuilder,
      $$ClassAssignmentsTableUpdateCompanionBuilder,
      (
        ClassAssignment,
        BaseReferences<_$LocalDb, $ClassAssignmentsTable, ClassAssignment>,
      ),
      ClassAssignment,
      PrefetchHooks Function()
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
  $$AiQueueTableTableManager get aiQueue =>
      $$AiQueueTableTableManager(_db, _db.aiQueue);
  $$DownloadedLessonsTableTableManager get downloadedLessons =>
      $$DownloadedLessonsTableTableManager(_db, _db.downloadedLessons);
  $$ClassMembershipsTableTableManager get classMemberships =>
      $$ClassMembershipsTableTableManager(_db, _db.classMemberships);
  $$ClassAssignmentsTableTableManager get classAssignments =>
      $$ClassAssignmentsTableTableManager(_db, _db.classAssignments);
}
