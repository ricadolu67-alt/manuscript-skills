# Scientific Claim Language｜主张形式与核验的双轴

字段与枚举以 [check_record_schema.md](check_record_schema.md) 为准，审查汇总按 [review_status_rules.md](review_status_rules.md)。

`claim_basis` records what kind of evidence the manuscript *purports* to offer; `check_status` records what checking was **actually** done. Neither substitutes for the other.

| Claim basis | Allowed as manuscript wording ONLY if actual evidence supports it | Watch-out |
|---|---|---|
| `THEOREM_CLAIM` | Under assumptions A–C, we establish/prove... | A numbered theorem is not proof of correctness; distinguish sufficient vs necessary, local vs global. |
| `CONDITIONAL_DERIVATION` | Provided X holds, the model implies... | A conjectured geometric sufficiency remains an assumption. |
| `ASYMPTOTIC_DERIVATION` | In the limit epsilon→0 with parameters fixed... | Do not swap limits or infer finite-range uniformity. |
| `NUMERICAL_RESULT` | For tested parameters, numerical calculations yield... | Do not turn parameter sweep into complete phase diagram. |
| `PHYSICAL_MEASUREMENT` | Under instrument/protocol X, we observed... | Correlation not equivalent to isolated causal mechanism. |
| `EMPIRICAL_ASSOCIATION` | X is associated with Y in data set Z... | May not generalize to all reservoirs/materials/tasks. |
| `MECHANISM_HYPOTHESIS` | The results are consistent with a mechanism in which... | State rival explanations and needed discriminating evidence. |

`check_status`: `PASS / FAIL / INCONCLUSIVE / NOT_CHECKED / UNAVAILABLE / NOT_APPLICABLE` is independent of above.

**Mapping to the public ledger.** `assertion` (ESTABLISHED / CONDITIONAL / NUMERICAL / CONJECTURED) follows the evidence type and known errors only. A written, unrefuted proof is ESTABLISHED even while its independent check is NOT_CHECKED; that gap lowers `gate_status`, not the wording. A FAIL lowers the assertion or triggers [strongest_claim.md](strongest_claim.md). If text claims fully proved but no derivation checked, status is `THEOREM_CLAIM + NOT_CHECKED`, not `PASS`.

### Required checks for proof-like manuscripts

Definitions and quantified domain; sufficient vs necessary; regularity and boundaries; singular limits and their order; comparison to known special cases; counterexample search; proof citations and lemmas; independence and actual check performed.

A PASS record covers one claim–check pair, method, version and scope. List all required checks and actual `check_record_id` links; one successful check does not establish the whole theorem/claim. Critical prerequisite failures or unresolved checks propagate through genuine REQUIRES relationships; auxiliary support and an explanatory link do not automatically invalidate independent observations. See [claim_dependency_map.md](claim_dependency_map.md).
