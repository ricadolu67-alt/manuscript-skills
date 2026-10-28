# Two-sided fidelity check (CHECK)

Goal: the text agrees with `LEDGER_PUBLIC.md`. It is neither stronger nor weaker than the ledger, keeps every truth-changing condition in the formal statements, and shows no trace of the workflow. The sentences that matter most are the ones a reader takes away: the abstract, the main-result statements in the introduction, the theorems and corollaries, and the conclusions.

## Step 1: map assertions to the ledger

List every scientific assertion in the text: theorems, propositions, corollaries, and every sentence in the abstract, introduction or discussion that states a result. Tag each one with a ledger ID (C#, I#, S#) or with "not in ledger". Keep the map internal; the report cites only the problems.

## Step 2: checks that bind (tiers A and B of native_criteria.md)

| # | Check | What failure looks like | Route |
|---|---|---|---|
| 1 | Overreach | An assertion not in the ledger, or one stronger than its `statement`: a wider quantifier, a dropped regime, a `CONDITIONAL` claim written as a theorem | Rewording fixes it → `FIX`. A genuinely new result → `RETURN_TO_LEDGER` |
| 2 | Under-claim | A `DECISIVE` claim or P4 implication missing or weakened: Θ stated as an upper bound, "we prove" turned into "suggests", a result moved entirely to the appendix | Wording → `FIX`. Missing or misplaced → `RETURN_TO_AUTHOR` |
| 2b | Front matter | A `DECISIVE` claim absent from the first two pages, or present there without its key formula | Add the formula from the theorem → `FIX`. Absent from the main text → `RETURN_TO_AUTHOR` |
| 3 | Formal conditions | A theorem or proposition lacks its `truth_conditions` | `FIX` |
| 3a | Front-matter conditions | A claim stated without its `reader_condition`, or the abstract or introduction carrying further conditions that the theorem already holds. Never add conditions to make the abstract "self-contained" | `FIX`: add the missing one, or move the extras to the theorem |
| 4 | Defensive sentences | A qualifying sentence that fails the three-question test in defensive_vs_native.md; a caveat said more than once outside the formal statement | `FIX`, rewritten on the native model |
| 5 | Internal consistency | The abstract, introduction, theorems and conclusion disagree about one result's object, exponent, regime or constant | `FIX`. If it is unclear which version is right → `RETURN_TO_LEDGER` |
| 6 | Process traces and labels | The ledger, handoffs, verification status, file names or tool traces, including LaTeX comments; ledger shorthand or `do_not_say` wording in the text; disclaimers about incomplete comparisons or priority | `FIX` |
| 6b | Undefined symbols | A symbol in a front-matter formula without a prior definition | `FIX`: add the definition from the theorem |
| 7 | Carry-forward | An I7 review item marked `OPEN` or `ADOPTED` that the text still does not address | Route by content |

## Step 3: diagnostics (tier C, reported but not binding)

Payoff claims missing from the front matter, clause and symbol counts, tic ceilings and departures from the default order go in a short `Diagnostics` list. Each entry is one line saying what was seen and whether it was changed. If the author's notes give a reason for a departure, quote the reason and leave the text alone unless a binding check fails.

## Step 4: format and venue rules (pre-submission only)

Check the template, page limit, anonymization and required statements (data, code, AI use, conflicts) against the official rules only. If the rules cannot be found, write "not checked" rather than assuming. Never write or confirm statements on the authors' behalf.

## Report format

```
Verdict: PASS / FIX / RETURN_TO_AUTHOR / RETURN_TO_LEDGER   (the most severe content route)
Environment: OK / ENV — one line, only for compile, font or toolchain problems

Issues (by impact)
E1 [check #] location (file:line) — problem — minimal fix — route

Diagnostics (not binding)
D1 location — what was seen — changed / left, with reason

Not checked: (only what was genuinely not checked, and why)
```

Do not list passed checks or count what was checked. If one problem occurs in several places, report it once with all its locations.
