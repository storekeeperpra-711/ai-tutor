# Phase 2 plan: checkers

Status: in progress. Date: 2026-10-02.
Spec: [master-prompt.md](../master-prompt.md), Part D7 (checkers) and Part F, Phase 2.

**Goal:** reliable, offline answer checking.
**Done when:** all checkers pass their tests and work inside lessons with the phone in airplane mode.

All checkers are pure Dart in `lib/checkers/` with no Flutter, network or AI. They run on the phone, so they work offline by design.

## Tasks

| # | Task |
|---|---|
| 2.1 | Shared input clean-up: Urdu/Arabic digits, Unicode subscripts (H₂O), `×` `÷` `−` `→`, number words 0–20 in English, Roman Urdu and Urdu script (`aath`, `آٹھ`). |
| 2.2 | Exact fractions (`Rational`) so `1/3 + 1/3` never becomes `0.6666`. |
| 2.3 | `numeric` checker: tolerance, number words. |
| 2.4 | `fraction` checker: `3/4`, mixed numbers `1 1/2`, Urdu digits; equal value is correct; optional "must be in lowest terms" with its own feedback. |
| 2.5 | `chem_equation` checker: parses formulas with brackets (`Ca(OH)2`), coefficients and state symbols. It finds unknown element symbols, wrong or missing substances, changed subscripts, unbalanced atoms (it names the element and the counts) and coefficients that aren't in lowest terms. |
| 2.6 | `linear_equation` checker: the student writes working line by line. Each line is checked against the one before (same solution), the first broken line is named, and the final answer is checked by substitution. |
| 2.7 | `text_check` step (schema, Dart model, widget). The student types text or several lines, and a checker decides. It supports `common_wrong` answers with specific feedback, like the number step. The number step also gets the `fraction` checker. |
| 2.8 | Two short draft lessons that use the checkers: Grade 9 Maths Unit 5 (solving linear equations, balance idea) and Grade 10 Chemistry Ch. 15 (balancing equations). They are original content, marked draft, and the play-through test covers them. |
| 2.9 | Unit tests for every mistake type. |

## Decisions (tell me if you want any changed)

1. **Every checker returns a mistake type plus details,** for example "unbalanced, O: 2 left, 3 right". The lesson screen turns that into English or Urdu text. This keeps the checkers free of language code and lets Phase 4 count mistakes per misconception.
2. **Roman Urdu input means number words only.** Phase 2 accepts number words from 0 to 20 (ek, do, teen … bees, plus the Urdu script versions). Free-text Roman Urdu answers are open-ended and need AI, which comes in Phase 6.
3. **Chemistry is case-sensitive, as in real chemistry.** `Co` (cobalt) and `CO` (carbon monoxide) are different. If a student writes `Nacl`, the feedback says "Nacl is not an element symbol" and explains capital letters.
4. **A linear equation can be answered with just `x = 4`.** That counts as correct. Mastery rules in Phase 4 can require written working later.
5. **Units and significant figures are not included yet.** The spec says "more as needed", so they come when a lesson needs them.
