import 'dart:convert';
import 'dart:typed_data';

import 'package:cloud_functions/cloud_functions.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

/// How well an explanation shows the idea.
enum AiLevel {
  gotIt('got_it'),
  partly('partly'),
  notYet('not_yet');

  const AiLevel(this.id);

  /// As in the lesson JSON and the server: got_it, partly, not_yet.
  final String id;

  static AiLevel? fromId(String? id) =>
      values.where((l) => l.id == id).firstOrNull;
}

/// Feedback from the AI proxy. When [byAi] is false the server chose not to
/// call the AI ([reason]: student_limit, step_limit, budget, unknown_step,
/// error) and the app uses its pre-written feedback.
class AiFeedback {
  const AiFeedback.ai(AiLevel this.level, String this.reply)
    : byAi = true,
      reason = null;

  const AiFeedback.fallback(String this.reason)
    : byAi = false,
      level = null,
      reply = null;

  final bool byAi;
  final AiLevel? level;
  final String? reply;
  final String? reason;
}

/// What the AI read in a photo of notebook working.
class PhotoReading {
  const PhotoReading.ai({
    required this.readable,
    required this.lines,
    required this.finalAnswer,
  }) : byAi = true,
       reason = null;

  const PhotoReading.fallback(String this.reason)
    : byAi = false,
      readable = false,
      lines = const [],
      finalAnswer = '';

  final bool byAi;
  final bool readable;
  final List<String> lines;
  final String finalAnswer;
  final String? reason;
}

/// The AI couldn't be reached (offline, timeout or a server error): the
/// app checks with its fallback and, for explanations, queues the answer.
class AiUnavailable implements Exception {
  const AiUnavailable([this.cause]);

  final Object? cause;

  @override
  String toString() => 'AiUnavailable($cause)';
}

/// One student's AI use on one day (cost dashboard).
class CostRow {
  const CostRow({
    required this.day,
    required this.studentId,
    required this.calls,
    required this.text,
    required this.photo,
    required this.costUsd,
  });

  final String day;
  final String studentId;
  final int calls;
  final int text;
  final int photo;
  final double costUsd;
}

class CostReport {
  const CostReport({
    required this.all,
    required this.rows,
    required this.totalUsd,
  });

  /// True for an admin, who sees every student in the project.
  final bool all;
  final List<CostRow> rows;
  final double totalUsd;
}

/// The app's only way to the AI: Cloud Functions that check the student,
/// the limits and the prompts on the server (spec D6). The Claude API is
/// never called from the app.
abstract class AiService {
  /// Feedback on an `ai_explain` answer.
  Future<AiFeedback> explain({
    required String studentId,
    required String lessonId,
    required String stepId,
    required String language,
    required String answer,
  });

  /// Turns the app checker's verdict on photographed working into kind
  /// words. The checker has already decided the working is wrong.
  Future<AiFeedback> explainVerdict({
    required String studentId,
    required String lessonId,
    required String stepId,
    required String language,
    required String working,
    required String checkerMessage,
  });

  /// Reads the working in a photo (JPEG, PNG or WebP).
  Future<PhotoReading> readPhoto({
    required String studentId,
    required String lessonId,
    required String stepId,
    required Uint8List photo,
  });

  /// AI calls and estimated cost per student per day, last 7 days.
  Future<CostReport> costs();
}

class FunctionsAiService implements AiService {
  FunctionsAiService(this._functions);

  final FirebaseFunctions _functions;

  Future<Map<String, dynamic>> _call(
    String name,
    Map<String, Object?> data,
    Duration timeout,
  ) async {
    try {
      final result = await _functions
          .httpsCallable(name, options: HttpsCallableOptions(timeout: timeout))
          .call<Map<String, dynamic>>(data);
      return Map<String, dynamic>.from(result.data);
    } on FirebaseFunctionsException catch (e) {
      throw AiUnavailable(e.code);
    } on Exception catch (e) {
      throw AiUnavailable(e);
    }
  }

  AiFeedback _feedback(Map<String, dynamic> data) {
    final level = AiLevel.fromId(data['level'] as String?);
    final reply = data['reply'] as String?;
    if (data['checked_by'] == 'ai' && level != null && reply != null) {
      return AiFeedback.ai(level, reply);
    }
    return AiFeedback.fallback(data['reason'] as String? ?? 'error');
  }

  @override
  Future<AiFeedback> explain({
    required String studentId,
    required String lessonId,
    required String stepId,
    required String language,
    required String answer,
  }) async => _feedback(
    await _call('aiFeedback', {
      'student_id': studentId,
      'lesson_id': lessonId,
      'step_id': stepId,
      'lang': language,
      'kind': 'explain',
      'answer': answer,
    }, const Duration(seconds: 20)),
  );

  @override
  Future<AiFeedback> explainVerdict({
    required String studentId,
    required String lessonId,
    required String stepId,
    required String language,
    required String working,
    required String checkerMessage,
  }) async => _feedback(
    await _call('aiFeedback', {
      'student_id': studentId,
      'lesson_id': lessonId,
      'step_id': stepId,
      'lang': language,
      'kind': 'verdict',
      'answer': working,
      'checker_message': checkerMessage,
    }, const Duration(seconds: 20)),
  );

  @override
  Future<PhotoReading> readPhoto({
    required String studentId,
    required String lessonId,
    required String stepId,
    required Uint8List photo,
  }) async {
    final data = await _call('photoRead', {
      'student_id': studentId,
      'lesson_id': lessonId,
      'step_id': stepId,
      'image': base64Encode(photo),
    }, const Duration(seconds: 45));
    if (data['checked_by'] != 'ai') {
      return PhotoReading.fallback(data['reason'] as String? ?? 'error');
    }
    return PhotoReading.ai(
      readable: data['readable'] == true,
      lines: [for (final l in data['lines'] as List? ?? []) '$l'],
      finalAnswer: data['final_answer'] as String? ?? '',
    );
  }

  @override
  Future<CostReport> costs() async {
    final data = await _call('aiCosts', {}, const Duration(seconds: 20));
    return CostReport(
      all: data['all'] == true,
      totalUsd: (data['total_usd'] as num? ?? 0).toDouble(),
      rows: [
        for (final r
            in (data['rows'] as List? ?? []).cast<Map<Object?, Object?>>())
          CostRow(
            day: r['day'] as String,
            studentId: r['student_id'] as String,
            calls: (r['calls'] as num? ?? 0).toInt(),
            text: (r['text'] as num? ?? 0).toInt(),
            photo: (r['photo'] as num? ?? 0).toInt(),
            costUsd: (r['cost_usd'] as num? ?? 0).toDouble(),
          ),
      ],
    );
  }
}

/// Region next to Firestore (functions/src/config.ts).
const functionsRegion = 'asia-south1';

final aiServiceProvider = Provider<AiService>(
  (ref) => FunctionsAiService(
    FirebaseFunctions.instanceFor(region: functionsRegion),
  ),
);
