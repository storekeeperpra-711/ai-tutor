/// Cleans up what a student typed so the checkers see one standard form.
library;

const _subscriptDigits = '₀₁₂₃₄₅₆₇₈₉';
const _superscriptDigits = '⁰¹²³⁴⁵⁶⁷⁸⁹';

/// Turns Urdu (۰–۹) and Arabic (٠–٩) digits into 0–9, subscript and
/// superscript digits (H₂O) into plain digits, and maths symbols
/// (× ÷ − → and the Arabic decimal point) into their keyboard forms.
String normalizeInput(String input) {
  final out = StringBuffer();
  for (final rune in input.trim().runes) {
    final char = String.fromCharCode(rune);
    if (rune >= 0x06F0 && rune <= 0x06F9) {
      out.writeCharCode(0x30 + rune - 0x06F0);
    } else if (rune >= 0x0660 && rune <= 0x0669) {
      out.writeCharCode(0x30 + rune - 0x0660);
    } else if (_subscriptDigits.contains(char)) {
      out.write(_subscriptDigits.indexOf(char));
    } else if (_superscriptDigits.contains(char)) {
      out.write(_superscriptDigits.indexOf(char));
    } else {
      out.write(switch (rune) {
        0x066B => '.', // Arabic decimal separator
        0x066C || 0x060C => ',', // Arabic thousands separator, Urdu comma
        0x2212 || 0x2013 => '-', // minus sign, en dash
        0x00D7 => '*', // ×
        0x00F7 => '/', // ÷
        0x2192 || 0x27F6 => '->', // → ⟶
        0x00A0 => ' ', // no-break space
        _ => char,
      });
    }
  }
  return out.toString();
}

/// Whole numbers 0–20 written as words: English, Roman Urdu and Urdu.
/// Several spellings because Roman Urdu has no fixed spelling.
const numberWords = <String, int>{
  // English
  'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
  'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11,
  'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
  'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19,
  'twenty': 20,
  // Roman Urdu
  'sifar': 0, 'ek': 1, 'aik': 1, 'do': 2, 'teen': 3, 'tin': 3,
  'char': 4, 'chaar': 4, 'panch': 5, 'paanch': 5,
  'chhe': 6, 'chay': 6, 'che': 6, 'chhay': 6, 'saat': 7, 'sat': 7,
  'aath': 8, 'ath': 8, 'nau': 9, 'no': 9, 'das': 10,
  'gyarah': 11, 'gyara': 11, 'barah': 12, 'bara': 12, 'terah': 13,
  'tera': 13, 'chaudah': 14, 'choda': 14, 'chodah': 14, 'pandrah': 15,
  'pandra': 15, 'solah': 16, 'sola': 16, 'satrah': 17, 'satra': 17,
  'atharah': 18, 'athara': 18, 'unnees': 19, 'unees': 19, 'bees': 20,
  // Urdu script
  'صفر': 0, 'ایک': 1, 'دو': 2, 'تین': 3, 'چار': 4, 'پانچ': 5, 'چھ': 6,
  'سات': 7, 'آٹھ': 8, 'نو': 9, 'دس': 10, 'گیارہ': 11, 'بارہ': 12,
  'تیرہ': 13, 'چودہ': 14, 'پندرہ': 15, 'سولہ': 16, 'سترہ': 17,
  'اٹھارہ': 18, 'انیس': 19, 'بیس': 20,
};

/// The number for a single number word, or null.
int? numberFromWord(String input) =>
    numberWords[input.trim().toLowerCase().replaceAll('.', '')];
