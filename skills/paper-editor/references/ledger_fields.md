# Ledger fields the author reads

The full schema lives with science-ledger (`ledger_schema.md`). The author reads only `LEDGER_PUBLIC.md`. Its author-facing fields are written in English.

| Field | Meaning | How to use it |
|---|---|---|
| P1 `core_contribution`, `reader_change` | The headline and what changes for the reader | The spine of the introduction |
| P2 `S#` | Shared setting: model, oracle, notation | State once, in the setting section. Entries marked `accounting: yes` are conventions for judging matches: mention once, in a natural sentence, and do not turn them into a formal definition or a recurring phrase |
| `role` | DECISIVE / SUPPORTING / EXTENSION / CLASSICAL | Scientific weight. Classical results are cited, not claimed |
| `statement` | The strongest true version | The source of theorem statements |
| `assertion` | ESTABLISHED / CONDITIONAL / NUMERICAL / CONJECTURED | Sets the verbs |
| `truth_conditions` | Conditions without which the statement is false | Belong inside the theorem; prose refers to them naturally |
| `reader_condition` | Usually one, at most two conditions per claim that a typical peer would otherwise misread, or `none`; a second one comes with its reason | The only conditions the abstract and introduction carry for that claim |
| `plain_reading` | What the claim means, in a peer's words | Raw material for the abstract and introduction |
| `mechanism` | Why it is true, in one sentence | Grows into the explanation paragraph after the theorem |
| `surprise` | What is counter-intuitive about it | A candidate opening |
| `story_role` | `setup` / `payoff` / `aside` | A `setup` claim (often a CLASSICAL null result) is the natural opening baseline |
| `prior_work` | The closest precedent and the exact difference | Related work and the comparison table |
| `do_not_say` | The nearest stronger claim that is false | A fence: avoid it, do not print it |
| P4 implications | Consequences, improvements and separations worth stating | Every one appears in the paper |
| P5 relations | Dependencies that fix the order | Section order |
| P6 open problems | Genuine scientific open questions | Discussion |
| P7 proof units | Proof text, by claim | Appendix proofs |
