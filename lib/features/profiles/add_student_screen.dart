import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../../l10n/app_localizations.dart';
import '../../services/account_actions.dart';
import '../../services/local_db.dart';
import '../../services/profiles.dart';
import '../../app/motion_widgets.dart';
import '../../app/theme/app_theme.dart';
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
    return TintedBackground(
      child: Scaffold(
        backgroundColor: Colors.transparent,
        appBar: AppBar(
          backgroundColor: Colors.transparent,
          title: Text(l10n.addLearner),
        ),
        body: ListView(
          padding: const EdgeInsets.fromLTRB(20, 8, 20, 24),
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
            Text(l10n.gradeLabel, style: textTheme.titleMedium),
            const SizedBox(height: 8),
            // Big buttons, one per class, so the class is one tap.
            Wrap(
              key: const Key('grade'),
              spacing: 8,
              runSpacing: 8,
              children: [
                for (final g in grades)
                  ChoiceChip(
                    key: Key('grade-$g'),
                    label: Text(gradeName(l10n, g)),
                    selected: _grade == g,
                    showCheckmark: false,
                    selectedColor: AppColors.lilac,
                    labelStyle: TextStyle(
                      color: _grade == g ? Colors.white : AppColors.ink,
                      fontWeight: FontWeight.w800,
                    ),
                    onSelected: (_) => setState(() => _grade = g),
                  ),
              ],
            ),
            const SizedBox(height: 24),
            Text(l10n.pictureLabel, style: textTheme.titleMedium),
            const SizedBox(height: 8),
            Wrap(
              spacing: 8,
              runSpacing: 8,
              children: [
                for (final id in avatarIds)
                  Pressable(
                    child: InkWell(
                      key: Key('avatar-$id'),
                      borderRadius: BorderRadius.circular(20),
                      onTap: () => setState(() => _avatar = id),
                      child: AnimatedContainer(
                        duration: const Duration(milliseconds: 200),
                        padding: const EdgeInsets.all(6),
                        decoration: BoxDecoration(
                          color: id == _avatar
                              ? AppColors.lilacSoft
                              : Colors.white,
                          borderRadius: BorderRadius.circular(20),
                          border: Border.all(
                            width: 3,
                            color: id == _avatar
                                ? AppColors.lilac
                                : Colors.transparent,
                          ),
                        ),
                        child: StudentAvatar(avatar: id, size: 52),
                      ),
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
            // Parents read (or listen to) the privacy note before agreeing.
            ListTile(
              key: const Key('open-privacy'),
              leading: const Icon(Icons.privacy_tip_outlined),
              title: Text(l10n.privacyTitle),
              trailing: const Icon(Icons.chevron_right),
              contentPadding: EdgeInsets.zero,
              onTap: () => context.push('/privacy'),
            ),
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
      ),
    );
  }
}
