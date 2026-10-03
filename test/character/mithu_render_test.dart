import 'dart:io';
import 'dart:ui' as ui;

import 'package:ai_tutor/character/mithu.dart';
import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:flutter_test/flutter_test.dart';

/// Not a real test: renders every mood to a PNG for a visual check
/// (MITHU_PNG_DIR=/some/dir flutter test test/character/mithu_render_test.dart).
void main() {
  final dir = Platform.environment['MITHU_PNG_DIR'];
  testWidgets('render moods', (tester) async {
    final key = GlobalKey();
    await tester.pumpWidget(
      MaterialApp(
        home: Center(
          child: RepaintBoundary(
            key: key,
            child: Container(
              color: Colors.white,
              width: 640,
              height: 320,
              child: Wrap(
                children: [
                  for (final m in MithuMood.values)
                    MithuView(mood: m, size: 160),
                ],
              ),
            ),
          ),
        ),
      ),
    );
    await tester.pump(const Duration(milliseconds: 300));
    if (dir == null) return;
    await tester.runAsync(() async {
      final boundary =
          key.currentContext!.findRenderObject()! as RenderRepaintBoundary;
      final image = await boundary.toImage(pixelRatio: 1);
      final bytes = await image.toByteData(format: ui.ImageByteFormat.png);
      File('$dir/mithu.png').writeAsBytesSync(bytes!.buffer.asUint8List());
    });
  }, skip: dir == null);
}
