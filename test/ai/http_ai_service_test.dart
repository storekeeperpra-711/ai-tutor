import 'dart:convert';
import 'dart:typed_data';

import 'package:ai_tutor/ai/ai_service.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:http/http.dart' as http;
import 'package:http/testing.dart';

void main() {
  final requests = <http.Request>[];

  HttpAiService service(
    http.Response Function(http.Request) answer, {
    String url = 'https://ai.example.com',
    String? token = 'token-u1',
  }) => HttpAiService(
    baseUrl: url,
    idToken: () async => token,
    client: MockClient((request) async {
      requests.add(request);
      return answer(request);
    }),
  );

  setUp(requests.clear);

  test('sends the sign-in token and reads AI feedback', () async {
    final ai = service(
      // The server sends UTF-8 (Urdu replies).
      (_) => http.Response.bytes(
        utf8.encode(
          jsonEncode({'checked_by': 'ai', 'level': 'partly', 'reply': 'شاباش'}),
        ),
        200,
      ),
    );
    final reply = await ai.explain(
      studentId: 's1',
      lessonId: 'l1',
      stepId: 'st1',
      language: 'ur',
      answer: 'because',
    );
    expect(reply.byAi, isTrue);
    expect(reply.level, AiLevel.partly);
    expect(reply.reply, 'شاباش');
    final request = requests.single;
    expect(request.url.toString(), 'https://ai.example.com/v1/feedback');
    expect(request.headers['authorization'], 'Bearer token-u1');
    expect(jsonDecode(request.body), containsPair('lang', 'ur'));
  });

  test('passes on the server\'s fallback reason', () async {
    final ai = service(
      (_) => http.Response(
        jsonEncode({'checked_by': 'fallback', 'reason': 'student_limit'}),
        200,
      ),
    );
    final reading = await ai.readPhoto(
      studentId: 's1',
      lessonId: 'l1',
      stepId: 'st1',
      photo: Uint8List.fromList([1, 2, 3]),
    );
    expect(reading.byAi, isFalse);
    expect(reading.reason, 'student_limit');
    expect(jsonDecode(requests.single.body)['image'], 'AQID');
  });

  test('server errors, no address and no sign-in mean "unavailable"', () async {
    Future<void> explain(HttpAiService ai) => ai.explain(
      studentId: 's1',
      lessonId: 'l1',
      stepId: 'st1',
      language: 'en',
      answer: 'x',
    );
    final ok = http.Response('{}', 200);
    await expectLater(
      explain(service((_) => http.Response('{"error":"x"}', 500))),
      throwsA(isA<AiUnavailable>()),
    );
    await expectLater(
      explain(service((_) => ok, url: '')),
      throwsA(isA<AiUnavailable>()),
    );
    await expectLater(
      explain(service((_) => ok, token: null)),
      throwsA(isA<AiUnavailable>()),
    );
    // Only the server error reached the server.
    expect(requests, hasLength(1));
  });
}
