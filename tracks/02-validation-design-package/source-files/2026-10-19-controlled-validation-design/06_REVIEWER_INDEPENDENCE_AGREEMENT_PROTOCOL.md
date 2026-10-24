# Deliverable 6 — Reviewer Independence & Agreement Protocol

**Protocol:** T04, plus independent requirements on T01/T02/T03/T05/T06/T08/T09/T10/T11. P14 remains MEDIUM in historic priority but is essential to the first testing phase.

## Roles and conflicts

- **Source custodian:** keeps original archive, hashes, permission/source-chain ledger; does not score the final credibility of their own extraction.
- **Independent fact-checker A and B:** each checks claims with source locators without consultation or seeing the other score. At least one has relevant category expertise; assign a second with independent source access.
- **Category editor A and B:** separately score texts under a frozen four-category rubric. Neither is the author of their scored material or employed as the candidate's advocate in a way that prejudges outcome.
- **Bilingual reviewer(s):** at least one native target-language reviewer and one independent bilingual check for transfer. Translator never self-approves meaning fidelity.
- **Adjudicator/methods lead:** resolves factual disagreement after raw forms are locked; signs a reason trace. Is not included in pre-adjudication agreement calculations.

Where two ratings come from the same prompt/model family, shared editorial team, common source lineage or coordinated discussion, they do **not** automatically count as independent. LLM-assisted reviewers must identify model provenance, not be counted as human replications.

## Blind rating workflow

1. Research director approves cases, rights, candidate-to-control contrasts, scoring anchors and change log; reserve separate calibration examples.
2. Assign anonymized labels and randomize presentation order only after approval. Conceal candidate category/author/status where practicable; category itself stays visible to apply correct rubric.
3. Reviewers score independently and freeze timestamped forms before discussion; predefine `N/A` and `NOT_CHECKABLE` separately from zero.
4. Calculate raw two-by-two or multi-level tables, percentage agreement, class prevalence and ordinal agreement; attempt chance-adjusted Gwet AC1 or weighted kappa when reasonable. Report Krippendorff alpha only with appropriate coding and uncertainty; avoid false precision on small pilot.
5. Adjudicate conflict without erasing original ratings; record exact source line or reason for every override. Revisions prompt a clearly versioned **new** round, not hidden changes to the original.
6. Compare by category and severity; do not pool weather safety labels and subjective narrative-emotion judgments uncritically.

## Provisional planning criteria

A proposed **≥80% raw agreement on high-impact factual labels** and chance-adjusted statistic **≥0.67 exploratory threshold** prompts continued calibration; below that flags revision. For high-stakes use, consider a **≥0.80** chance-adjusted consistency objective with larger sample and lower uncertainty. These are **design goals**, not empirically established results. Always publish numerator/denominator, uncertainty when computable, class imbalance, disagreement examples, and a disposition of `INCONCLUSIVE` for low n or missing raters.

**Stop conditions:** reviewer authorship/conflict contaminates blinding, not enough independent subject expertise, missing reference material, serious reviewer distress or privacy concern, or failure to detect intentionally serious negative control. Do not use consensus to create spurious initial agreement.
