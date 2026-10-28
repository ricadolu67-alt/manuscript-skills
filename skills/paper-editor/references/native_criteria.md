# Writing standard: what must hold, and what to weigh

This file is the single source for the prose rules shared by paper-author and paper-editor. Other files point here and do not restate these rules. These are editorial criteria, not evidence of measured performance across research fields.

Rules come in three tiers:
- **Tier A** protects scientific truth.
- **Tier B** addresses repeated qualifiers and workflow language that can distract from supported findings.
- **Tier C** is a set of diagnostics: signals that something may be wrong.

Tiers A and B must hold. Tier C asks for judgement. When a draft deviates from a tier C default, either fix the deviation or write one line in `AUTHOR_NOTES.md` or `EDIT_NOTES.md` saying why it serves this paper's reader. A theorem-dense COLT paper, a mechanism paper in JFM and an engineering study have different right answers.

## The two readers

The first two pages serve two readers, and a good draft satisfies both.
- **The stranger:** would they keep reading, and would they remember the main finding tomorrow?
- **The expert:** how many substantive claims could they check by the end of page two, each with an explicit formula and a pointer to where it is established?

The usual solution is layering: the opening tells the story, and a main-results passage or table makes it checkable. Do not trade one reader for the other.

## Tier A: truth (must hold)

1. **Strength matches the ledger.** No overreach (wider quantifiers, dropped regimes, conditional results written as theorems). No under-claiming (Θ stated as an upper bound, "we prove" softened to "suggests").
2. **Formal statements carry their full `truth_conditions`.** Prose refers to them naturally.
3. **Every `DECISIVE` claim appears on the first two pages with its key formula:** rate, threshold, scaling or leading constant. A headline result paraphrased without its formula is an under-claim.
4. **Each claim's `reader_condition` is present** wherever the abstract or introduction states that claim.
5. **Every symbol in a front-matter formula is defined before it is used,** in words or by an exact formula. Central objects are described exactly; a loose paraphrase is an error, not a simplification.
6. **Numbers carry no more digits than the method resolves.** Full precision goes in tables or appendices.

## Tier B: anti-defensive (must hold)

1. **No disclaimers about prior work.** Never write that a comparison is incomplete or that no priority is claimed. Name the authors, give their bound or formula, and state what changes. Gaps in what was checked belong in the ledger's internal record.
2. **No workflow in the text.** No verification status, ledger, handoff, file names or tool traces.
3. **No ledger shorthand.** Claim titles, fence words and labels from `do_not_say` or `truth_conditions` are rewritten as what they refer to. `do_not_say` lines are never turned into sentences.
4. **No empty sentences.** No generic summary ("These results highlight…"), no bridging sentence that names no quantity, mechanism, object or comparison, and no truism ("remains an experimental question").
5. **Each caveat is said once** outside the formal statement, in the abstract and introduction combined. Notation clashes and source-version notes go in a footnote or the notation section.

[defensive_vs_native.md](defensive_vs_native.md) illustrates tier B patterns with invented teaching sentences and gives the three-question test for any qualifying sentence.

## Tier C: diagnostics (defaults; deviate with a reason)

1. **Order.** The default is phenomenon → why → mechanism → result → prior work → open question, but the opening should fit the material. A theory paper may open from an open problem or a counterexample. A mechanism paper usually opens from the null result the effect breaks: the symmetry or cancellation that makes the naive answer "nothing happens". An experimental paper may open from an observation, and an engineering paper from a decision under pressure. Never open with a conclusion whose key terms are undefined.
2. **The abstract follows the talk note.** If the talk opens with a concrete surprise, the abstract usually states it, with its number, within its first two sentences.
3. **Words before symbols.** About four new symbols at most on page one, and at most one coined term in the abstract, glossed in the same sentence.
4. **Conditions in the abstract.** About two condition clauses in the whole abstract. A sentence carrying two chained conditions ("under X and the Y conditions") usually wants "in the regime defined below".
5. **Payoff claims.** Claims with `story_role: payoff` usually appear on the first two pages, with their formula, in the main-results passage or a comparison table. A result mentioned only as "also covers…" hides its content.
6. **Numbers in the front matter.** Prefer exact symbolic forms when they carry the result. Use only the significant figures justified by the method and state the setup each number needs. Three significant figures is a stylistic default, not a substitute for an uncertainty analysis.
7. **Compression.** Watch for stacked attribute lists, noun piles and undefined anthropomorphic shorthand ("the walk finds the bottleneck"). Write the clause out unless the shorthand has been defined.
8. **Construction detail.** Budget formulas, round allocations and grid sizes usually belong in the theorem or proof, not the introduction.
9. **Repeated or unnecessary phrases** from the editor's tic list, and short sequences repeated several times in the front matter. Frequency is a prompt to reread, not an empirical threshold.
10. **Shape.** A theory abstract usually runs 5–7 sentences and 150–200 words. Main results usually hold 3–5 items.

A diagnostic is a reason to look again, not a verdict. Fix it when the fix helps the reader. Leave it, with a reason, when the paper's content needs it.
