# LEDGER_PUBLIC — Quadratic teaching example

This is a deliberately elementary teaching artifact. It demonstrates fields, conditions and rescoping; it is not a research result, novelty claim, review certificate or submission-ready ledger. Local claim IDs organize the example and do not represent original contributions.

- ledger_version: demo-1
- source_versions: self-contained algebra below
- date: 2026-10-28

## P1 Core contribution

- core_contribution: The square function is strictly increasing on the nonnegative real axis.
- reader_change: Restricting a domain can recover a true monotonicity statement from a false global one.

## P2 Shared setting

- S1: f(x)=x² for real x.

## P3 Claims

### C1 Strict increase on a restricted domain

- role: CLASSICAL
- statement: For all real x and y satisfying 0≤x<y, f(x)<f(y).
- basis: THEOREM
- assertion: ESTABLISHED
- truth_conditions: S1; 0≤x<y.
- reader_condition: on the nonnegative real axis
- evidence: f(y)-f(x)=(y-x)(y+x)>0 under the stated conditions.
- prior_work: Elementary algebra; no novelty is claimed in this teaching example.
- do_not_say: f is increasing on the entire real axis.
- rescope_note: The unrestricted statement fails, for example at x=-2 and y=-1.
- plain_reading: Squaring preserves strict order between nonnegative numbers.
- mechanism: Both factors of the difference of squares are positive.
- surprise: none
- story_role: setup

## P4 Implications and comparisons

### I1 Minimum on the restricted domain

- statement: f has its unique minimum at x=0 on x≥0.
- from: C1 and f(0)=0
- regime: x≥0
- why_it_matters: A domain restriction must remain attached to a derived conclusion.

## P5 Relations that fix the order of presentation

- Introduce S1 before C1; derive I1 after C1.

## P6 Open problems

- None in this elementary example.
