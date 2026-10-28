# Where conditions go

Readers should know the limits of a result when they need them, without being interrupted by disclaimers.

| Kind of condition | Where it goes |
|---|---|
| Shared setting (`S#`: model, oracle, global assumptions, notation) | Once, in the setting or model section; later referred to by name |
| Accounting convention (`S#`, `accounting: yes`) | One natural sentence where it first matters. Not a formal definition, and not a tag repeated after every result |
| A claim's `reader_condition` (usually one, at most two) | The only conditions the abstract and introduction carry for that claim, written into the sentence once. If it is `none`, the claim is stated plainly |
| A claim's `truth_conditions` | Inside the theorem or proposition. In prose, a short natural reference ("for a fixed domain", "in the natural step-size regime") |
| A parameter range that is part of the result ("when n ≥ d log d") | Part of the result itself, next to it |
| Error, truncation or convergence affecting a specific number | Next to that number, or in the caption |
| Extensions beyond the ledger | Only in the Discussion, and only if P6 lists them |

## The repeat test

Before writing a condition a second time, ask whether it adds a new scope, a new level of evidence, or a new interpretation. If it does, keep it, compressed. If it does not, delete it. A condition usually needs to appear twice at most: once in the theorem, and once where the reader first meets the idea.

## Never in the text

Verification status, workflow, file names, and the literal `do_not_say` sentences.
