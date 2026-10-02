import 'package:flutter/material.dart';

import '../app/bidi.dart';
import '../models/localized_text.dart';

/// Shows lesson text in the app's language. In Urdu, maths inside the
/// sentence is kept left-to-right.
class LessonText extends StatelessWidget {
  const LessonText(this.text, {super.key, this.style, this.textAlign});

  final LocalizedText text;
  final TextStyle? style;
  final TextAlign? textAlign;

  @override
  Widget build(BuildContext context) {
    final value = text.of(context);
    final rtl = Directionality.of(context) == TextDirection.rtl;
    return Text(
      rtl ? isolateMath(value) : value,
      style: style,
      textAlign: textAlign,
    );
  }
}
