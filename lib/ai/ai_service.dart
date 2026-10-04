import 'dart:convert';
import 'dart:typed_data';

import 'package:flutter/services.dart' show appFlavor;
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:http/http.dart' as http;

import '../services/auth_service.dart';

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

/// The whole project's learning on one day (counted by the AI server once
/// a day, totals only; shown to admins).
class LearningDay {
  const LearningDay({
    required this.day,
    required this.students,
    required this.lessons,
    required this.lessonsFinished,
    required this.questions,
    required this.firstTry,
    required this.aiCalls,
  });

  final String day;
  final int students;
  final int lessons;
  final int lessonsFinished;
  final int questions;
  final int firstTry;
  final int aiCalls;
}

class CostReport {
  const CostReport({
    required this.all,
    required this.rows,
    required this.totalUsd,
    this.learning = const [],
  });

  /// True for an admin, who sees every student in the project.
  final bool all;
  final List<CostRow> rows;
  final double totalUsd;

  /// Learning totals, newest first (admins only).
  final List<LearningDay> learning;
}

/// The app's only way to the AI: the AI server (worker/) checks the student,
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

/// The AI server (worker/, a Cloudflare Worker), called over HTTPS with the
/// user's Firebase sign-in. Any failure becomes [AiUnavailable], and the
/// step falls back to its offline check.
class HttpAiService implements AiService {
  HttpAiService({
    required this.baseUrl,
    required this.idToken,
    http.Client? client,
  }) : _client = client ?? http.Client();

  /// e.g. https://ai-tutor-ai-dev.example.workers.dev (no trailing slash).
  final String baseUrl;
  final Future<String?> Function() idToken;
  final http.Client _client;

  Future<Map<String, dynamic>> _call(
    String path,
    Map<String, Object?> data,
    Duration timeout,
  ) async {
    if (baseUrl.isEmpty) throw const AiUnavailable('not set up');
    try {
      final token = await idToken();
      if (token == null) throw const AiUnavailable('not signed in');
      final response = await _client
          .post(
            Uri.parse('$baseUrl$path'),
            headers: {
              'authorization': 'Bearer $token',
              'content-type': 'application/json',
            },
            body: jsonEncode(data),
          )
          .timeout(timeout);
      if (response.statusCode != 200) {
        throw AiUnavailable('HTTP ${response.statusCode}');
      }
      return jsonDecode(utf8.decode(response.bodyBytes))
          as Map<String, dynamic>;
    } on AiUnavailable {
      rethrow;
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
    await _call('/v1/feedback', {
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
    await _call('/v1/feedback', {
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
    final data = await _call('/v1/photo', {
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
    final data = await _call('/v1/costs', {}, const Duration(seconds: 20));
    return CostReport(
      all: data['all'] == true,
      totalUsd: (data['total_usd'] as num? ?? 0).toDouble(),
      rows: [
        for (final r
            in (data['rows'] as List? ?? []).cast<Map<String, dynamic>>())
          CostRow(
            day: r['day'] as String,
            studentId: r['student_id'] as String,
            calls: (r['calls'] as num? ?? 0).toInt(),
            text: (r['text'] as num? ?? 0).toInt(),
            photo: (r['photo'] as num? ?? 0).toInt(),
            costUsd: (r['cost_usd'] as num? ?? 0).toDouble(),
          ),
      ],
      learning: [
        for (final t
            in (data['learning'] as List? ?? []).cast<Map<String, dynamic>>())
          LearningDay(
            day: t['day'] as String,
            students: (t['students_active'] as num? ?? 0).toInt(),
            lessons: (t['lessons_active'] as num? ?? 0).toInt(),
            lessonsFinished: (t['lessons_finished'] as num? ?? 0).toInt(),
            questions: (t['questions_answered'] as num? ?? 0).toInt(),
            firstTry: (t['first_try_correct'] as num? ?? 0).toInt(),
            aiCalls: (t['ai_calls'] as num? ?? 0).toInt(),
          ),
      ],
    );
  }
}

/// The AI server's address for each app version. Empty until the Worker
/// is deployed (docs/setup/ai-setup.md); until then every AI step uses its
/// offline check. A build can also set it: --dart-define=AI_URL=https://...
const aiServerUrls = {
  'dev': 'https://ai-tutor-ai-dev.aitutor1.workers.dev',
  'prod': '',
};

String aiServerUrl() {
  const override = String.fromEnvironment('AI_URL');
  if (override.isNotEmpty) return override;
  return aiServerUrls[appFlavor ?? 'dev'] ?? '';
}

final aiServiceProvider = Provider<AiService>((ref) {
  final auth = ref.watch(authServiceProvider);
  return HttpAiService(baseUrl: aiServerUrl(), idToken: auth.idToken);
});
