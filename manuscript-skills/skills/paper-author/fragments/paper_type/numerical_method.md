# Numerical-method papers (new discretizations, algorithms, solvers)

If suitable numerical-method exemplars are available, follow [EXEMPLARS.md](../../exemplars/EXEMPLARS.md); otherwise use the built-in writing criteria.

- **Open with a computation that looks credible but violates a key structure** (conservation, dissipation, positivity, stability), or with a cost existing methods cannot pay. A specific, reproducible failure beats "accuracy is limited".
- **Before the method appears, say which step of the old method fails.** Each component of the new method answers one failure.
- **Each benchmark settles one question:** accuracy, stability, complex geometry or cost, each with its own test. A single set of curves does not show that a method is "better".
- **State fairness next to the comparison:** same resolution, same compute, same tolerance.
- **Keep three claims apart:** structure preservation (`THEOREM`), observed convergence order (`NUMERICAL`), and "therefore the physics is right". Numerical agreement does not validate the physical model.
- **Report failed settings in the results.** They show where the method's limits are. Do not interpolate over them or move them to an appendix.
