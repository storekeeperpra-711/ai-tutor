import '../models/lesson.dart';

/// Spec B3: Not started → Learning → Practising → Mastered → Secure.
enum MasteryLevel { notStarted, learning, practising, mastered, secure }

/// Days between spaced reviews after mastery (spec B2: about 2 days,
/// 1 week, 1 month), then longer once the skill keeps being remembered.
const reviewIntervals = [2, 7, 30, 60, 120];

/// A review answered right this long after mastery makes a skill Secure.
const secureAfter = Duration(days: 7);

/// Question steps missed in a row before a parent or teacher is told.
const needsHelpAfter = 4;

/// How many recently asked questions to remember (to avoid repeats).
const _recentLimit = 20;

/// One answer, as evidence about one skill.
class Evidence {
  const Evidence({
    required this.skill,
    required this.itemId,
    required this.at,
    required this.firstTry,
    this.solved = false,
    this.questionType,
  });

  final String skill;

  /// The question or step, e.g. `g6-maths-02-dividing-fractions/s5_quarters`.
  final String itemId;
  final DateTime at;

  /// recall, explain, apply, find_error or exam_style.
  final String? questionType;

  /// Right on the first try. Only these count towards mastery.
  final bool firstTry;

  /// Right in the end (after a hint or retry).
  final bool solved;
}

/// What the app knows about one child and one skill. Small on purpose:
/// this is what is stored and synced, not every answer.
class SkillState {
  const SkillState({
    required this.skill,
    this.answered = 0,
    this.firstTryCorrect = 0,
    this.typesShown = const {},
    this.correctDays = const [],
    this.lastAnswered,
    this.masteredAt,
    this.secureAt,
    this.reviewStage = 0,
    this.nextReview,
    this.stuck = 0,
    this.needsHelp = false,
    this.recent = const {},
  });

  final String skill;
  final int answered;
  final int firstTryCorrect;

  /// Question types answered right on the first try.
  final Set<String> typesShown;

  /// Days (`yyyy-mm-dd`) with a first-try correct answer, oldest first.
  final List<String> correctDays;
  final DateTime? lastAnswered;
  final DateTime? masteredAt;
  final DateTime? secureAt;

  /// Index in [reviewIntervals] of the gap before [nextReview].
  final int reviewStage;

  /// When the next spaced review is due (start of that day).
  final DateTime? nextReview;

  /// Question steps not right on the first try since the last one that was.
  final int stuck;

  /// Repeatedly stuck: a parent or teacher should look at it.
  final bool needsHelp;

  /// Recently asked questions and when.
  final Map<String, DateTime> recent;

  MasteryLevel level(MasteryCriteria? criteria) {
    if (secureAt != null) return MasteryLevel.secure;
    if (masteredAt != null) return MasteryLevel.mastered;
    if (answered == 0) return MasteryLevel.notStarted;
    final required = criteria?.questionTypes.toSet();
    final shown = required == null
        ? typesShown
        : typesShown.intersection(required);
    return shown.isEmpty ? MasteryLevel.learning : MasteryLevel.practising;
  }

  /// Question types still needed for mastery.
  Set<String> missingTypes(MasteryCriteria? criteria) =>
      (criteria?.questionTypes.toSet() ?? {}).difference(typesShown);

  bool reviewDue(DateTime now) =>
      nextReview != null && !dayOf(now).isBefore(nextReview!);

  /// Adds one answer. [criteria] decides when the skill becomes Mastered.
  SkillState record(Evidence e, MasteryCriteria? criteria) {
    final day = dayOf(e.at);
    final recent = Map.of(this.recent)..[e.itemId] = e.at;
    if (recent.length > _recentLimit) {
      final oldest = recent.entries.reduce(
        (a, b) => a.value.isBefore(b.value) ? a : b,
      );
      recent.remove(oldest.key);
    }

    var next = _copy(
      answered: answered + 1,
      lastAnswered: e.at,
      recent: recent,
    );

    if (e.firstTry) {
      next = next._copy(
        firstTryCorrect: firstTryCorrect + 1,
        typesShown: {...typesShown, ?e.questionType},
        correctDays: _addDay(correctDays, dayKey(day)),
        stuck: 0,
        needsHelp: false,
      );
    } else {
      final stuck = this.stuck + 1;
      next = next._copy(
        stuck: stuck,
        needsHelp: needsHelp || stuck >= needsHelpAfter,
      );
    }

    if (masteredAt != null) return next._review(e, day);

    if (criteria != null &&
        next.typesShown.containsAll(criteria.questionTypes) &&
        next.correctDays.length >= criteria.days) {
      return next._copy(
        masteredAt: e.at,
        reviewStage: 0,
        nextReview: day.add(Duration(days: reviewIntervals.first)),
      );
    }
    return next;
  }

  /// Spaced review, adapted to how the answer went.
  SkillState _review(Evidence e, DateTime day) {
    if (!reviewDue(e.at)) {
      // A slip between reviews brings the next review closer.
      if (!e.firstTry) {
        final soon = day.add(const Duration(days: 1));
        if (nextReview == null || soon.isBefore(nextReview!)) {
          return _copy(nextReview: soon);
        }
      }
      return this;
    }
    if (e.firstTry) {
      final stage = (reviewStage + 1).clamp(0, reviewIntervals.length - 1);
      final secure =
          secureAt ??
          (e.at.difference(masteredAt!) >= secureAfter ? e.at : null);
      return _copy(
        reviewStage: stage,
        nextReview: day.add(Duration(days: reviewIntervals[stage])),
        secureAt: secure,
      );
    }
    if (e.solved) {
      // Remembered with some help: same gap again.
      return _copy(
        nextReview: day.add(Duration(days: reviewIntervals[reviewStage])),
      );
    }
    // Forgotten: back to Practising, to be shown again on new days.
    return SkillState(
      skill: skill,
      answered: answered,
      firstTryCorrect: firstTryCorrect,
      typesShown: typesShown,
      lastAnswered: lastAnswered,
      stuck: stuck,
      needsHelp: needsHelp,
      recent: recent,
    );
  }

  SkillState _copy({
    int? answered,
    int? firstTryCorrect,
    Set<String>? typesShown,
    List<String>? correctDays,
    DateTime? lastAnswered,
    DateTime? masteredAt,
    DateTime? secureAt,
    int? reviewStage,
    DateTime? nextReview,
    int? stuck,
    bool? needsHelp,
    Map<String, DateTime>? recent,
  }) => SkillState(
    skill: skill,
    answered: answered ?? this.answered,
    firstTryCorrect: firstTryCorrect ?? this.firstTryCorrect,
    typesShown: typesShown ?? this.typesShown,
    correctDays: correctDays ?? this.correctDays,
    lastAnswered: lastAnswered ?? this.lastAnswered,
    masteredAt: masteredAt ?? this.masteredAt,
    secureAt: secureAt ?? this.secureAt,
    reviewStage: reviewStage ?? this.reviewStage,
    nextReview: nextReview ?? this.nextReview,
    stuck: stuck ?? this.stuck,
    needsHelp: needsHelp ?? this.needsHelp,
    recent: recent ?? this.recent,
  );

  static List<String> _addDay(List<String> days, String day) {
    if (days.contains(day)) return days;
    final all = [...days, day]..sort();
    return all.length > 10 ? all.sublist(all.length - 10) : all;
  }

  Map<String, Object?> toJson() => {
    'skill': skill,
    'answered': answered,
    'first_try_correct': firstTryCorrect,
    'types_shown': typesShown.toList()..sort(),
    'correct_days': correctDays,
    'last_answered': lastAnswered?.toIso8601String(),
    'mastered_at': masteredAt?.toIso8601String(),
    'secure_at': secureAt?.toIso8601String(),
    'review_stage': reviewStage,
    'next_review': nextReview?.toIso8601String(),
    'stuck': stuck,
    'needs_help': needsHelp,
    'recent': {
      for (final e in recent.entries) e.key: e.value.toIso8601String(),
    },
  };

  factory SkillState.fromJson(Map<String, dynamic> json) {
    DateTime? date(String key) =>
        json[key] == null ? null : DateTime.parse(json[key] as String);
    return SkillState(
      skill: json['skill'] as String,
      answered: json['answered'] as int? ?? 0,
      firstTryCorrect: json['first_try_correct'] as int? ?? 0,
      typesShown: {...(json['types_shown'] as List<dynamic>? ?? []).cast()},
      correctDays: [...(json['correct_days'] as List<dynamic>? ?? []).cast()],
      lastAnswered: date('last_answered'),
      masteredAt: date('mastered_at'),
      secureAt: date('secure_at'),
      reviewStage: json['review_stage'] as int? ?? 0,
      nextReview: date('next_review'),
      stuck: json['stuck'] as int? ?? 0,
      needsHelp: json['needs_help'] as bool? ?? false,
      recent: {
        for (final e in (json['recent'] as Map<String, dynamic>? ?? {}).entries)
          e.key: DateTime.parse(e.value as String),
      },
    );
  }
}

/// Midnight at the start of [t]'s day.
DateTime dayOf(DateTime t) => DateTime(t.year, t.month, t.day);

String dayKey(DateTime t) =>
    '${t.year.toString().padLeft(4, '0')}-'
    '${t.month.toString().padLeft(2, '0')}-'
    '${t.day.toString().padLeft(2, '0')}';
