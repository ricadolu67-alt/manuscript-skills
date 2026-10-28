# Theory papers (theorems, bounds, complexity, asymptotics)

Use for papers whose main evidence is theorems and proofs: COLT, ALT, NeurIPS theory, SIAM, short theory papers in JFM, mathematical physics. If suitable theory exemplars are available, follow exemplars/EXEMPLARS.md; otherwise use the built-in writing criteria.

## What the reader gets on page one

1. **The question,** posed in the language of the predecessor or the classical theory, and concrete enough to have an answer ("how many samples are needed to reach accuracy ε", not "sample size matters").
2. **The answer:** the main result stated informally, with the key quantity (rate, threshold, exponent). A "Main results" paragraph or short list is the usual vehicle: typically 3–5 items, one sentence and one key formula each, each pointing to its formal theorem. Every DECISIVE result must be there; other results join when the reader benefits.
3. **Why it is new:** the precise difference from the closest prior work. When P4 lists improvements or separations, put them in a comparison table (rows: settings; columns: prior work, this paper).
4. **Why it is true:** one paragraph, expanded from the ledger's `mechanism`, naming the single idea that makes the result work. The reader should know the main idea before seeing any proof.

If the headline is a general characterization, lead with the most concrete surprise, a counter-intuitive fact already visible in the simplest instance, and generalize right after. All of this fits in the first page to page and a half. Related work can follow in the introduction or get its own section, written as where existing methods hold and where they stop, not as a list of papers.

## How to write a theorem

- **State the formal theorem with all its hypotheses.** Parameter conditions, comparators and quantifiers from `truth_conditions` all go inside. Anything a theorem states is not repeated in the abstract or the introduction.
- **Follow it with a paragraph on the idea of the proof,** in the reader's language. Say which step makes the argument work and why that step is possible ("after symmetrization, only one combinatorial quantity is left to count", not "by Lemmas 3 and 4").
- **Then say what it changes,** in a sentence or two. Turn the symbols into a consequence the reader can judge, ideally through the smallest special case that shows it.
- **Full proofs go in the appendix.** The main text keeps only the constructions and inequalities needed to understand the main results.

## Upper and lower bounds, and "tight"

- Put matching upper and lower bounds side by side, or merge them into one corollary. The reader should not have to assemble them.
- When you say "tight", say **what matches** (the whole quantity, one term, or one exponent), **where** (the parameter regime), and **up to what** (constants, logarithms, polynomial factors). P4 usually gives all three.
- A parameter regime is part of the result, not a disclaimer added afterwards. "For n ≥ d log d the sample complexity is Θ(f)" is clearer than "the sample complexity is Θ(f) under suitable conditions".

## Verbs by assertion

| `assertion` | How to write it |
|---|---|
| `ESTABLISHED` | Theorem / Proposition / Lemma; "we prove", "we show" |
| `CONDITIONAL` | Put the hypothesis in the statement: "Assume (H). Then …"; say briefly what supports (H) |
| `NUMERICAL` | A remark or a numerical section: "numerically, for n ≤ 200, …" |
| `CONJECTURED` | Conjecture, with the evidence that supports it |

Cite classical tools (standard concentration inequalities, classical convex analysis); never present them as new.

## Ending

- Open problems come only from P6, written as research questions.
- No generic Limitations paragraph; limits already sit next to the results they qualify.
- Theory papers often need no separate Conclusion. A Discussion is enough.

## Common failures

- A third of the abstract restating the theorem hypotheses.
- The same distinction repeated in five places instead of once, where the object is defined.
- "The bounds agree up to a polynomial factor" with no word on where they agree up to constants.
- "Comparable" or "in some sense" in place of a precise restricted statement.
- An accounting convention turned into a formal definition, or into a phrase appended to every result.
- A proof sketch that is a list of short assertions ("A holds. B follows. C gives the bound.") and never says why the key step works.
- Three or four coined terms in one section, none of them explained.
