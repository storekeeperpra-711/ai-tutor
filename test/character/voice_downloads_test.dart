import 'dart:convert';
import 'dart:io';

import 'package:ai_tutor/character/voice_downloads.dart';
import 'package:ai_tutor/character/voice_lines.dart';
import 'package:ai_tutor/models/lesson_step.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:http/http.dart' as http;
import 'package:http/testing.dart';

const lesson = 'g9-maths-05-solving-linear-equations';
const urdu = '${lesson}__s1_scale_ur.m4a';

void main() {
  late Directory dir;
  late List<String> asked;
  late Map<String, String> files;

  setUp(() {
    dir = Directory.systemTemp.createTempSync('voice');
    asked = [];
    files = {
      urdu: 'v1',
      '${lesson}__s1_scale_en.m4a': 'v1',
      'other__s1_ur.m4a': 'v1',
    };
  });
  tearDown(() => dir.deleteSync(recursive: true));

  VoiceDownloads downloads({String url = 'https://ai.example.com'}) =>
      VoiceDownloads(
        baseUrl: url,
        folderDir: dir,
        client: MockClient((request) async {
          final name = request.url.pathSegments.last;
          asked.add(
            '$name${request.url.hasQuery ? '?${request.url.query}' : ''}',
          );
          if (name == 'index') {
            return http.Response(
              jsonEncode({'voice': 'Sulafat', 'files': files}),
              200,
            );
          }
          return http.Response(name.endsWith('.mouth') ? '0369' : 'audio', 200);
        }),
      );

  test('downloads only the lesson\'s lines in the child\'s language', () async {
    expect(await downloads().prepare(lesson, 'ur'), 1);
    expect(asked, [
      'index',
      '$urdu?v=v1',
      '${urdu.replaceAll('.m4a', '.mouth')}?v=v1',
    ]);
    expect(File('${dir.path}/$urdu').readAsStringSync(), 'audio');
  });

  test('skips what it has, and downloads a line made again', () async {
    await downloads().prepare(lesson, 'ur');
    asked.clear();
    expect(await downloads().prepare(lesson, 'ur'), 0);
    expect(asked, ['index']);

    files[urdu] = 'v2';
    asked.clear();
    expect(await downloads().prepare(lesson, 'ur'), 1);
    expect(asked, contains('$urdu?v=v2'));
  });

  test(
    'a failed download keeps nothing half-written, and never throws',
    () async {
      final failing = VoiceDownloads(
        baseUrl: 'https://ai.example.com',
        folderDir: dir,
        client: MockClient((request) async {
          if (request.url.pathSegments.last == 'index') {
            return http.Response(jsonEncode({'files': files}), 200);
          }
          if (request.url.path.endsWith('.mouth')) {
            throw const SocketException('offline');
          }
          return http.Response('audio', 200);
        }),
      );
      expect(await failing.prepare(lesson, 'ur'), 0);
      expect(File('${dir.path}/$urdu').existsSync(), isFalse);
      expect(await downloads(url: '').prepare(lesson, 'ur'), 0);
    },
  );

  test(
    'the voice library plays a downloaded line, with its beak track',
    () async {
      await downloads().prepare(lesson, 'ur');
      final library = VoiceLibrary(
        recordingsDir: Directory.systemTemp.createTempSync('rec'),
        downloadsDir: dir,
      );
      final line = VoiceLine(
        line: CharacterLine.fromJson({
          'emotion': 'happy',
          'say': {'en': 'Hello', 'ur': 'سلام'},
        }),
        language: 'ur',
        lessonId: lesson,
        stepId: 's1_scale',
      );
      final recording = await library.find(line);
      expect(recording?.path, '${dir.path}/$urdu');
      expect(recording?.isAsset, isFalse);
      expect(recording?.mouth.levels.length, 4);
    },
  );
}
