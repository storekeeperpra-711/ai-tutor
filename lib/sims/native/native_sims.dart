import '../sim_host.dart';
import 'atom_balancer.dart';
import 'balance_scale.dart';
import 'feasible_region.dart';
import 'fraction_bars.dart';
import 'graph_plotter.dart';
import 'inequality_line.dart';
import 'inequality_plane.dart';
import 'number_line.dart';

/// Native interactives by `sim_id`. Keep in step with the schema's
/// `sim_id` list and tools/validate_lessons.py.
final nativeSims = <String, SimBuilder>{
  'fraction_bars': (args) => FractionBars(args: args),
  'balance_scale': (args) => BalanceScale(args: args),
  'atom_balancer': (args) => AtomBalancer(args: args),
  'number_line': (args) => NumberLine(args: args),
  'graph_plotter': (args) => GraphPlotter(args: args),
  'inequality_line': (args) => InequalityLine(args: args),
  'inequality_plane': (args) => InequalityPlane(args: args),
  'feasible_region': (args) => FeasibleRegion(args: args),
};
