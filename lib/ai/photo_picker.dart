import 'dart:typed_data';

import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:image_picker/image_picker.dart';

enum PhotoSource { camera, gallery }

/// Takes or picks a photo and returns it as a small JPEG (about 100 KB),
/// or null if the child cancelled. Small photos cost less AI and data
/// (spec D9.5).
typedef PhotoPicker = Future<Uint8List?> Function(PhotoSource source);

/// Longest side in pixels: enough to read handwriting.
const photoMaxSide = 1200.0;

final photoPickerProvider = Provider<PhotoPicker>((ref) {
  final picker = ImagePicker();
  return (source) async {
    final file = await picker.pickImage(
      source: source == PhotoSource.camera
          ? ImageSource.camera
          : ImageSource.gallery,
      maxWidth: photoMaxSide,
      maxHeight: photoMaxSide,
      imageQuality: 70,
      requestFullMetadata: false,
    );
    return file?.readAsBytes();
  };
});
