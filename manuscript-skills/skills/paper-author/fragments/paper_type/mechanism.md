# Mechanism and physical-theory papers (fluids, complex fluids, mechanics, geoscience)

Use for papers that explain a phenomenon through a model, a derivation or an analytic result. If suitable exemplars are available, follow `exemplars/EXEMPLARS.md`; otherwise use the built-in writing criteria.

- **Start from the baseline the effect breaks.** In most mechanism papers the strongest opening is a null result: a symmetry or cancellation that makes the naive answer zero (for example, d'Alembert's zero drag in ideal flow, which viscosity then breaks). Say why it cancels, then which ingredient breaks the symmetry. The rest of the introduction is one argument from that baseline to the result. Check the ledger for CLASSICAL claims marked `story_role: setup`; they are usually this baseline.
- **Otherwise, open with an obstacle that changes what the reader does next:** where an accepted assumption fails, or what an observation leaves unexplained. Do not open with a generic "research gap" sentence and fill the results in afterwards.
- **Fix the basis of comparison before attributing a cause.** Compare at the same base state and the same control parameters. If several differences survive the common constraints, keep the competing explanations alive (the ledger should list them).
- **Introduce an equation when the reader needs it for the next inference:** say why the quantity matters, give it, then say what it implies.
- **After a surprising result, give its physical meaning at once,** in a sentence or two. No mechanism story the evidence does not support.
- **Keep levels of evidence separate.** The observed phenomenon (`MEASUREMENT` or `NUMERICAL`) and "this mechanism explains it" (`HYPOTHESIS` or `THEOREM`) are separate statements, with verbs set by `assertion`.
- **Limitations should change how a conclusion can be used,** for example a linear threshold versus the bifurcation type. Put them with the conclusion they limit, not in a generic list.
