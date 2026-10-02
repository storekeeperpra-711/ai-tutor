import 'package:flutter/material.dart';

import '../../l10n/app_localizations.dart';
import '../../services/local_db.dart';
import '../../services/profiles.dart';
import 'avatar.dart';

/// Asks for [student]'s 4-digit PIN with big buttons. Returns true when the
/// PIN is right, false or null when the child gives up.
Future<bool?> askForPin(BuildContext context, Student student) =>
    showDialog<bool>(
      context: context,
      builder: (context) => PinPadDialog(student: student),
    );

class PinPadDialog extends StatefulWidget {
  const PinPadDialog({super.key, required this.student});

  final Student student;

  @override
  State<PinPadDialog> createState() => _PinPadDialogState();
}

class _PinPadDialogState extends State<PinPadDialog> {
  var _pin = '';
  var _wrong = false;

  void _press(String digit) {
    if (_pin.length >= 4) return;
    setState(() {
      _pin += digit;
      _wrong = false;
    });
    if (_pin.length == 4) {
      if (checkPin(_pin, widget.student.pinHash!)) {
        Navigator.of(context).pop(true);
      } else {
        setState(() {
          _pin = '';
          _wrong = true;
        });
      }
    }
  }

  void _back() {
    if (_pin.isEmpty) return;
    setState(() => _pin = _pin.substring(0, _pin.length - 1));
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final colors = Theme.of(context).colorScheme;
    Widget key(String digit) => Padding(
      padding: const EdgeInsets.all(4),
      child: SizedBox(
        width: 64,
        height: 64,
        child: FilledButton.tonal(
          key: Key('pin-$digit'),
          onPressed: () => _press(digit),
          child: Text(digit, style: const TextStyle(fontSize: 24)),
        ),
      ),
    );

    return AlertDialog(
      title: Row(
        children: [
          StudentAvatar(avatar: widget.student.avatar, size: 40),
          const SizedBox(width: 12),
          Expanded(child: Text(l10n.enterPin)),
        ],
      ),
      content: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          // Dots for the digits typed so far. Digits read left to right.
          Directionality(
            textDirection: TextDirection.ltr,
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                for (var i = 0; i < 4; i++)
                  Padding(
                    padding: const EdgeInsets.all(6),
                    child: Icon(
                      i < _pin.length ? Icons.circle : Icons.circle_outlined,
                      size: 20,
                      color: colors.primary,
                    ),
                  ),
              ],
            ),
          ),
          if (_wrong)
            Padding(
              padding: const EdgeInsets.only(top: 8),
              child: Text(
                l10n.wrongPin,
                key: const Key('pin-wrong'),
                style: TextStyle(color: colors.error),
              ),
            ),
          const SizedBox(height: 12),
          Directionality(
            textDirection: TextDirection.ltr,
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                for (final row in const [
                  ['1', '2', '3'],
                  ['4', '5', '6'],
                  ['7', '8', '9'],
                ])
                  Row(
                    mainAxisSize: MainAxisSize.min,
                    children: [for (final d in row) key(d)],
                  ),
                Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    const SizedBox(width: 72),
                    key('0'),
                    SizedBox(
                      width: 72,
                      child: IconButton(
                        key: const Key('pin-back'),
                        onPressed: _back,
                        icon: const Icon(Icons.backspace_outlined),
                      ),
                    ),
                  ],
                ),
              ],
            ),
          ),
        ],
      ),
      actions: [
        TextButton(
          onPressed: () => Navigator.of(context).pop(false),
          child: Text(l10n.cancelButton),
        ),
      ],
    );
  }
}
