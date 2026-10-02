/// An exact fraction, so 1/3 + 1/3 is exactly 2/3 (no rounding errors).
/// Always stored in lowest terms with a positive denominator.
class Rational implements Comparable<Rational> {
  factory Rational(int numerator, [int denominator = 1]) {
    if (denominator == 0) throw ArgumentError('denominator is zero');
    final sign = denominator < 0 ? -1 : 1;
    final g = _gcd(numerator.abs(), denominator.abs());
    final d = g == 0 ? 1 : g;
    return Rational._(sign * numerator ~/ d, sign * denominator ~/ d);
  }

  const Rational._(this.numerator, this.denominator);

  /// Reads a decimal like `2.5` or `-0.75` exactly. Null if not a number.
  static Rational? tryParseDecimal(String text) {
    final match = RegExp(r'^([+-]?)(\d*)(?:\.(\d+))?$').firstMatch(text);
    if (match == null || (match[2]!.isEmpty && match[3] == null)) return null;
    final whole = match[2]!.isEmpty ? '0' : match[2]!;
    final decimals = match[3] ?? '';
    if (whole.length + decimals.length > 15) return null; // stays in int range
    var scale = 1;
    for (var i = 0; i < decimals.length; i++) {
      scale *= 10;
    }
    final value = int.parse('$whole$decimals');
    return Rational(match[1] == '-' ? -value : value, scale);
  }

  static const zero = Rational._(0, 1);
  static const one = Rational._(1, 1);

  final int numerator;
  final int denominator;

  bool get isZero => numerator == 0;
  bool get isInteger => denominator == 1;
  double toDouble() => numerator / denominator;

  Rational operator +(Rational o) => Rational(
    numerator * o.denominator + o.numerator * denominator,
    denominator * o.denominator,
  );
  Rational operator -(Rational o) => this + (-o);
  Rational operator -() => Rational._(-numerator, denominator);
  Rational operator *(Rational o) =>
      Rational(numerator * o.numerator, denominator * o.denominator);
  Rational operator /(Rational o) =>
      Rational(numerator * o.denominator, denominator * o.numerator);

  @override
  bool operator ==(Object other) =>
      other is Rational &&
      other.numerator == numerator &&
      other.denominator == denominator;

  @override
  int get hashCode => Object.hash(numerator, denominator);

  @override
  int compareTo(Rational other) =>
      (numerator * other.denominator).compareTo(other.numerator * denominator);

  @override
  String toString() => isInteger ? '$numerator' : '$numerator/$denominator';
}

int _gcd(int a, int b) => b == 0 ? a : _gcd(b, a % b);

/// Greatest common divisor of positive whole numbers.
int gcdOf(Iterable<int> values) => values.fold(0, (g, v) => _gcd(g, v.abs()));
