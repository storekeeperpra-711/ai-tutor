import 'package:ai_tutor/media/media_cache.dart';
import 'package:flutter_test/flutter_test.dart';

import '../fakes.dart';

void main() {
  final day = DateTime(2026, 10, 4);
  const mb = 1024 * 1024;

  late FakeMediaIndex repo;
  late FakeMediaManager manager;
  late MediaCache cache;

  setUp(() {
    repo = FakeMediaIndex();
    manager = FakeMediaManager(repo);
    cache = MediaCache(manager: manager, repo: repo, maxBytes: 100 * mb);
  });

  test('under the limit nothing is removed', () async {
    repo
      ..add('a', 40 * mb, day)
      ..add('b', 50 * mb, day);
    await cache.trim();
    expect(manager.removed, isEmpty);
    expect(await cache.usedBytes(), 90 * mb);
  });

  test('over the limit the files used longest ago go first', () async {
    repo
      ..add('new', 40 * mb, day)
      ..add('oldest', 30 * mb, day.subtract(const Duration(days: 9)))
      ..add('old', 30 * mb, day.subtract(const Duration(days: 3)))
      ..add('newer', 20 * mb, day.add(const Duration(hours: 1)));
    await cache.trim();
    expect(manager.removed, ['oldest']);
    expect(await cache.usedBytes(), 90 * mb);
  });

  test('the lesson open now is never removed', () async {
    repo
      ..add('open-video', 80 * mb, day.subtract(const Duration(days: 30)))
      ..add('other', 50 * mb, day);
    await cache.trim(keep: {'open-video'});
    expect(manager.removed, ['other']);
  });

  test('clear removes everything', () async {
    repo.add('a', 10 * mb, day);
    await cache.clear();
    expect(await cache.usedBytes(), 0);
  });

  test('the default limit is 300 MB', () {
    expect(MediaCache.defaultMaxBytes, 300 * mb);
  });
}
