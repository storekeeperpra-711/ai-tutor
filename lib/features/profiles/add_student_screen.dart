import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../l10n/app_localizations.dart';
import '../../services/account_actions.dart';
import '../../services/local_db.dart';
import '../../services/profiles.dart';
import 'avatar.dart';
import 'grade_names.dart';

/// Adds a child profile: first name, class, picture and an optional PIN,
/// with a parent's or guardian's consent.
class AddStudentScreen extends ConsumerStatefulWidget {
  const AddStudentScreen({super.key});

  @override
  ConsumerState<AddStudentScreen> createState() => _AddStudentScreenState();
}

class _AddStudentScreenState extends ConsumerState<AddStudentScreen> {
  final _name = TextEditingController();
  final _pin = TextEditingController();
  int? _grade;
  var _avatar = avatarIds.first;
  var _consent = false;
  var _saving = false;

  @override
  void initState() {
    super.initState();
    // Rebuild so the Save button follows what is typed.
    _name.addListener(() => setState(() {}));
    _pin.addListener(() => setState(() {}));
  }

  @override
  void dispose() {
    _name.dispose();
    _pin.dispose();
    super.dispose();
  }

  bool get _pinOk => _pin.text.isEmpty || _pin.text.length == 4;

  bool get _canSave =>
      !_saving &&
      _name.text.trim().isNotEmpty &&
      _grade != null &&
      _pinOk &&
      _consent;

  Future<void> _save() async {
    setState(() => _saving = true);
    final student = await ref
        .read(accountActionsProvider)
        .addStudent(
          firstName: _name.text,
          grade: _grade!,
          avatar: _avatar,
          pin: _pin.text,
        );
    if (!mounted) return;
    ref.read(currentStudentProvider.notifier).select(student);
    Navigator.of(context).pop();
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final textTheme = Theme.of(context).textTheme;
    return Scaffold(
      appBar: AppBar(title: Text(l10n.addLearner)),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          TextField(
            key: const Key('first-name'),
            controller: _name,
            maxLength: 30,
            textCapitalization: TextCapitalization.words,
            decoration: InputDecoration(
              labelText: l10n.firstNameLabel,
              helperText: l10n.firstNameHelp,
            ),
          ),
          const SizedBox(height: 16),
          DropdownButtonFormField<int>(
            key: const Key('grade'),
            initialValue: _grade,
            decoration: InputDecoration(labelText: l10n.gradeLabel),
            items: [
              for (final g in grades)
                DropdownMenuItem(value: g, child: Text(gradeName(l10n, g))),
            ],
            onChanged: (g) => setState(() => _grade = g),
          ),
          const SizedBox(height: 24),
          Text(l10n.pictureLabel, style: textTheme.titleMedium),
          const SizedBox(height: 8),
          Wrap(
            spacing: 8,
            runSpacing: 8,
            children: [
              for (final id in avatarIds)
                InkWell(
                  key: Key('avatar-$id'),
                  customBorder: const CircleBorder(),
                  onTap: () => setState(() => _avatar = id),
                  child: Container(
                    padding: const EdgeInsets.all(3),
                    decoration: BoxDecoration(
                      shape: BoxShape.circle,
                      border: Border.all(
                        width: 3,
                        color: id == _avatar
                            ? Theme.of(context).colorScheme.primary
                            : Colors.transparent,
                      ),
                    ),
                    child: StudentAvatar(avatar: id, size: 56),
                  ),
                ),
            ],
          ),
          const SizedBox(height: 24),
          TextField(
            key: const Key('pin'),
            controller: _pin,
            keyboardType: TextInputType.number,
            obscureText: true,
            maxLength: 4,
            inputFormatters: [FilteringTextInputFormatter.digitsOnly],
            decoration: InputDecoration(
              labelText: l10n.pinOptionalLabel,
              helperText: l10n.pinHelp,
              helperMaxLines: 2,
              errorText: _pinOk ? null : l10n.pinTooShort,
            ),
          ),
          const SizedBox(height: 16),
          CheckboxListTile(
            key: const Key('consent'),
            value: _consent,
            onChanged: (v) => setState(() => _consent = v ?? false),
            title: Text(l10n.consentLabel),
            controlAffinity: ListTileControlAffinity.leading,
            contentPadding: EdgeInsets.zero,
          ),
          const SizedBox(height: 16),
          FilledButton(
            key: const Key('save-learner'),
            onPressed: _canSave ? _save : null,
            child: Text(l10n.saveButton),
          ),
        ],
      ),
    );
  }
}
