import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../l10n/app_localizations.dart';
import '../../services/connectivity.dart';
import '../../services/sync_service.dart';

/// A small, friendly line about the connection. It only informs: lessons
/// always carry on, and work is saved on the phone either way.
/// Shows nothing when online with nothing waiting.
class SyncStatus extends ConsumerWidget {
  const SyncStatus({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final l10n = AppLocalizations.of(context);
    final online = ref.watch(onlineProvider).value ?? true;
    final pending = ref.watch(pendingSyncCountProvider).value ?? 0;
    final (IconData icon, String text) = switch ((online, pending)) {
      (false, _) => (Icons.cloud_off, l10n.offlineStatus),
      (true, > 0) => (Icons.cloud_upload_outlined, l10n.waitingToSync(pending)),
      _ => (Icons.cloud_done_outlined, ''),
    };
    if (text.isEmpty) return const SizedBox.shrink();
    final colors = Theme.of(context).colorScheme;
    return Row(
      key: const Key('sync-status'),
      mainAxisSize: MainAxisSize.min,
      children: [
        Icon(icon, size: 18, color: colors.onSurfaceVariant),
        const SizedBox(width: 6),
        Flexible(
          child: Text(
            text,
            style: Theme.of(context).textTheme.bodySmall,
            overflow: TextOverflow.ellipsis,
          ),
        ),
      ],
    );
  }
}
