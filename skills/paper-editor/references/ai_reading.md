# "Does this read like AI?" (AI_READ)

Look for **missing writing decisions**, not keywords. For each problem, give the locations and the fix. When one kind of problem occurs in several places, list it once with every location.

| Symptom | What it looks like | Fix |
|---|---|---|
| One claim per sentence | Short declaratives in a row, each stating one fact, with no because, so or but between them | Merge them into a paragraph that reasons |
| Defensive repetition | The same qualifier or distinction in several places; paragraphs ending in "this does not imply …" | Say it once, where the object is defined; delete the rest |
| Generic endings | "These results highlight the importance of …", "Together, X, Y and Z determine …" | Replace with one concrete consequence, or delete |
| Templated structure | Every section is definition, theorem, one remark, transition; every paragraph ends with a summary | Follow the reasoning; drop summaries that do not advance it |
| No authorial judgement | Results listed flat, with nothing saying which matters most, which is surprising, which overturns an expectation | Rank them and say why, in the introduction and the discussion |
| Broken narrative | Paragraph openings that do not pick up the previous question; sections joined by "Next, we …" | Make each paragraph the question the reader is now asking |
| Inflated vocabulary | "leverage", "crucially", "notably", "a comprehensive framework" | A concrete verb and a concrete object, or nothing |
| Process traces | Mentions of materials, ledgers, drafts, checks or tools | Delete; the text discusses the research only |
| Tic phrases | Repeated or unnecessary phrases from [tic_list.md](tic_list.md) (a qualitative diagnostic) | Reread; apply the fix listed there where it helps |
| Repeated caveat | The same scope remark three or more times, in different wordings | Keep it where the result is stated, plus once at most |
| Compression | Stacked attribute lists, noun piles, undefined anthropomorphic shorthand | Write the clause out |
| Symbols before the picture | Several symbols on page one before the reader knows what they measure | Words first; symbols when needed, each defined exactly |
| Thin prior work | A paragraph of theorem numbers without the competing bound | Name the authors, give their bound, state the change |
| Qualitative main results | Headline results paraphrased with no formula | Add the key formula from the theorem |
| Spurious precision | 8–12 significant figures in prose; decimals where a symbolic form exists | Use the symbolic form or three significant figures; full digits go in a table |
| Priority disclaimers | "no priority is claimed", "the comparison remains incomplete" | Delete; describe the precedents accurately |
| Construction detail up front | Budget formulas, round allocations or grid sizes in the introduction | Move them into the theorem or the proof |

## Report

1. **Overall judgement,** in two or three sentences: what pulls the reader's attention away from the findings.
2. **Issue list:** symptom, locations, fix, with the three worst kinds first.
3. **One sample rewrite:** the paragraph where the problems are densest, rewritten, for the author to compare.

No "AI probability" and no score.
