# sims

Simulations for the lesson `sim` step (Phase 5). The step itself is
`lib/lessons/steps/sim_step_view.dart`: it shows the simulation, checks
the result with the answer checkers and reports a normal step result.

- `sim_host.dart`: what every simulation gets (`SimArgs`) and reports
  (`SimEvent`: `ready`, `result` with data, `error`).
- `web_sim_view.dart`: one HTML file from `assets/sims/` in a WebView.
  Calls `initSim(config)`, listens on `TutorBridge`, blocks navigation.
- `native/`: the Flutter interactives, by `sim_id` (`native_sims.dart`).
  Each has big buttons as well as dragging, and a Check button that
  reports its state.

## Writing an HTML simulation

One self-contained file in `assets/sims/` (CSS and JavaScript inside, no
links to anything outside the file, so it works offline). It must:

```js
function initSim(config) { /* config = {lang: "en" | "ur", reduce_motion, ...params} */ }
function post(event, data) {
  if (window.TutorBridge) TutorBridge.postMessage(JSON.stringify({event: event, data: data || {}}));
}
// post('ready') when started; post('result', {...}) when the child presses Check.
```

Write all text in English and Urdu inside the file, use big buttons, and
skip decorative motion when `reduce_motion` is true. Try it in the
developer screen (**Simulations (developer)** on the home screen).
