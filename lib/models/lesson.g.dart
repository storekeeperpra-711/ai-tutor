// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'lesson.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Lesson _$LessonFromJson(Map<String, dynamic> json) => $checkedCreate(
  'Lesson',
  json,
  ($checkedConvert) {
    final val = Lesson(
      id: $checkedConvert('id', (v) => v as String),
      version: $checkedConvert('version', (v) => (v as num).toInt()),
      schema: $checkedConvert('schema', (v) => v as String),
      subject: $checkedConvert('subject', (v) => v as String),
      grade: $checkedConvert('grade', (v) => (v as num).toInt()),
      tier: $checkedConvert('tier', (v) => v as String),
      curriculumRefs: $checkedConvert(
        'curriculum_refs',
        (v) => (v as List<dynamic>)
            .map((e) => CurriculumRef.fromJson(e as Map<String, dynamic>))
            .toList(),
      ),
      skills: $checkedConvert(
        'skills',
        (v) => (v as List<dynamic>).map((e) => e as String).toList(),
      ),
      title: $checkedConvert(
        'title',
        (v) => LocalizedText.fromJson(v as Map<String, dynamic>),
      ),
      estimatedMinutes: $checkedConvert(
        'estimated_minutes',
        (v) => (v as num).toInt(),
      ),
      prerequisites: $checkedConvert(
        'prerequisites',
        (v) => (v as List<dynamic>)
            .map((e) => Prerequisite.fromJson(e as Map<String, dynamic>))
            .toList(),
      ),
      misconceptions: $checkedConvert(
        'misconceptions',
        (v) => (v as List<dynamic>)
            .map((e) => Misconception.fromJson(e as Map<String, dynamic>))
            .toList(),
      ),
      glossary: $checkedConvert(
        'glossary',
        (v) => (v as List<dynamic>)
            .map((e) => GlossaryEntry.fromJson(e as Map<String, dynamic>))
            .toList(),
      ),
      steps: $checkedConvert('steps', (v) => _stepsFromJson(v as List)),
      review: $checkedConvert(
        'review',
        (v) => Review.fromJson(v as Map<String, dynamic>),
      ),
      flashcards: $checkedConvert(
        'flashcards',
        (v) =>
            (v as List<dynamic>?)
                ?.map((e) => Flashcard.fromJson(e as Map<String, dynamic>))
                .toList() ??
            const [],
      ),
      homeTasks: $checkedConvert(
        'home_tasks',
        (v) =>
            (v as List<dynamic>?)
                ?.map((e) => HomeTask.fromJson(e as Map<String, dynamic>))
                .toList() ??
            const [],
      ),
      teacherNotes: $checkedConvert(
        'teacher_notes',
        (v) =>
            (v as List<dynamic>?)?.map((e) => e as String).toList() ?? const [],
      ),
      masteryCriteria: $checkedConvert(
        'mastery_criteria',
        (v) => v as Map<String, dynamic>? ?? const {},
      ),
      questionBank: $checkedConvert(
        'question_bank',
        (v) => v as Map<String, dynamic>? ?? const {},
      ),
      alternatives: $checkedConvert(
        'alternatives',
        (v) => v as List<dynamic>? ?? const [],
      ),
      reviewQuestions: $checkedConvert(
        'review_questions',
        (v) => v as List<dynamic>? ?? const [],
      ),
    );
    return val;
  },
  fieldKeyMap: const {
    'curriculumRefs': 'curriculum_refs',
    'estimatedMinutes': 'estimated_minutes',
    'homeTasks': 'home_tasks',
    'teacherNotes': 'teacher_notes',
    'masteryCriteria': 'mastery_criteria',
    'questionBank': 'question_bank',
    'reviewQuestions': 'review_questions',
  },
);

CurriculumRef _$CurriculumRefFromJson(Map<String, dynamic> json) =>
    $checkedCreate('CurriculumRef', json, ($checkedConvert) {
      final val = CurriculumRef(
        outcome: $checkedConvert('outcome', (v) => v as String),
        code: $checkedConvert('code', (v) => v as String?),
        textbook: $checkedConvert('textbook', (v) => v as String?),
      );
      return val;
    });

Prerequisite _$PrerequisiteFromJson(Map<String, dynamic> json) =>
    $checkedCreate('Prerequisite', json, ($checkedConvert) {
      final val = Prerequisite(
        skill: $checkedConvert('skill', (v) => v as String),
        lesson: $checkedConvert('lesson', (v) => v as String?),
      );
      return val;
    });

Misconception _$MisconceptionFromJson(Map<String, dynamic> json) =>
    $checkedCreate('Misconception', json, ($checkedConvert) {
      final val = Misconception(
        id: $checkedConvert('id', (v) => v as String),
        description: $checkedConvert('description', (v) => v as String),
      );
      return val;
    });

GlossaryEntry _$GlossaryEntryFromJson(Map<String, dynamic> json) =>
    $checkedCreate('GlossaryEntry', json, ($checkedConvert) {
      final val = GlossaryEntry(
        en: $checkedConvert('en', (v) => v as String),
        ur: $checkedConvert('ur', (v) => v as String),
      );
      return val;
    });

Flashcard _$FlashcardFromJson(Map<String, dynamic> json) =>
    $checkedCreate('Flashcard', json, ($checkedConvert) {
      final val = Flashcard(
        id: $checkedConvert('id', (v) => v as String),
        front: $checkedConvert(
          'front',
          (v) => LocalizedText.fromJson(v as Map<String, dynamic>),
        ),
        back: $checkedConvert(
          'back',
          (v) => LocalizedText.fromJson(v as Map<String, dynamic>),
        ),
      );
      return val;
    });

HomeTask _$HomeTaskFromJson(Map<String, dynamic> json) =>
    $checkedCreate('HomeTask', json, ($checkedConvert) {
      final val = HomeTask(
        id: $checkedConvert('id', (v) => v as String),
        text: $checkedConvert(
          'text',
          (v) => LocalizedText.fromJson(v as Map<String, dynamic>),
        ),
      );
      return val;
    });

Review _$ReviewFromJson(Map<String, dynamic> json) =>
    $checkedCreate('Review', json, ($checkedConvert) {
      final val = Review(
        status: $checkedConvert('status', (v) => v as String),
        reviewedBy: $checkedConvert('reviewed_by', (v) => v as String?),
        date: $checkedConvert('date', (v) => v as String?),
      );
      return val;
    }, fieldKeyMap: const {'reviewedBy': 'reviewed_by'});
