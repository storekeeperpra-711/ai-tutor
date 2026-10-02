import 'package:flutter/material.dart';

import '../../l10n/app_localizations.dart';

/// Developer screen for checking Urdu rendering on a real phone:
/// clipping of tall Nastaliq letters, Urdu digits, English terms inside
/// Urdu sentences, and short left-to-right formulas.
///
/// The sample text is original test text, not lesson content.
class UrduTestScreen extends StatelessWidget {
  const UrduTestScreen({super.key});

  static const _samples = [
    'زمین ہر چیز کو اپنی طرف کھینچتی ہے۔ اس کھنچاؤ کو کششِ ثقل (Gravity) کہتے ہیں۔',
    'عائشہ کے پاس ۳ روٹیاں ہیں۔ ہر دوست کو آدھی روٹی چاہیے۔ وہ کتنے دوستوں کو کھلا سکتی ہے؟',
    'اردو ہندسے: ۰ ۱ ۲ ۳ ۴ ۵ ۶ ۷ ۸ ۹',
    // \u2066 ... \u2069 keep the formula left-to-right inside Urdu text.
    'رفتار کا فارمولا \u2066v = d / t\u2069 ہے۔',
    'پانی کا کیمیائی فارمولا \u2066H₂O\u2069 ہے۔',
    'گھیں، ڈھیر، ٹھیک، کچھ، پیچھے، بیٹھ، چھوٹی، لکھیں',
  ];

  @override
  Widget build(BuildContext context) {
    final textTheme = Theme.of(context).textTheme;
    final sizes = [
      textTheme.bodyMedium,
      textTheme.titleLarge,
      textTheme.headlineMedium,
    ];

    // Always right-to-left, even when the app language is English,
    // so the screen can be checked from either language.
    return Directionality(
      textDirection: TextDirection.rtl,
      child: Scaffold(
        appBar: AppBar(title: Text(AppLocalizations.of(context).urduTestTitle)),
        body: ListView(
          padding: const EdgeInsets.all(16),
          children: [
            for (final style in sizes)
              for (final s in _samples)
                Container(
                  margin: const EdgeInsets.only(bottom: 8),
                  // The outline shows if any letter is cut off.
                  decoration: BoxDecoration(
                    border: Border.all(color: Colors.black12),
                  ),
                  child: Text(
                    s,
                    style: style?.copyWith(fontFamily: 'NotoNastaliqUrdu'),
                  ),
                ),
          ],
        ),
      ),
    );
  }
}
