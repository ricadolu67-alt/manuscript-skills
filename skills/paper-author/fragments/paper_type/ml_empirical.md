# Empirical machine-learning papers (methods, benchmarks, analyses)

For theory-first ML papers, use `theory.md`.

- **Open with a concrete difficulty in the task, or a failure mode of existing methods,** not with the popularity of the field.
- **Tie the contribution to the difficulty:** one insight, one component that realizes it, and the benefit that follows.
- **Each experiment answers one question:** main results, ablations (which component matters), failure settings, out-of-distribution behaviour.
- **State fairness next to each comparison:** same compute, same data split, the strongest baseline. Leakage should already be ruled out in the ledger.
- **Do not:**
  - average away results that differ in direction;
  - hide failure settings in the appendix;
  - turn "better on these datasets" into "better in general".
