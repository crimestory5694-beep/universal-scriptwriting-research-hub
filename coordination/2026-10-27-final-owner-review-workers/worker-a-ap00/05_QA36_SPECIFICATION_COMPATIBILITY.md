# QA-001–QA-036 — v0.2 Candidate Specification Compatibility
**Decision: PROPOSED — OWNER REVIEW PENDING**. Contract compatibility is reviewed **statically**; actual fixture runs = **0/36** and T01–T13 executed = **0/13**.
Immutable original: `worker-deliverables/skill-architecture/2026-10-27/06_ACCEPTANCE_TEST_MATRIX.csv` Git blob `88e89ee233c967c5b8a0b645b0d401f6c1d2ccea`, 4754 UTF-8 bytes; all original 36 unique contiguous test IDs and `DESIGN_ONLY` statuses preserved.

| Exact source IDs | Scope | Proposed original test intent | v0.2 compatible expected interpretation | Execution status |
|---|---|---|---|---|
| QA-001..003 | source & branch provenance | branch isolation, missing provenance/timestamps, immutable IDs | only new folder; missing review trace HOLD; re-key rejected | DESIGN_ONLY / NOT_RUN |
| QA-004..005 | restricted export/rights | third-party byte export and read-vs-republish | HOLD_RIGHTS; no raw source bytes | DESIGN_ONLY / NOT_RUN |
| QA-006..010 | archival & evidence eligibility | EDU disputed, missing B70–72, F-190, R052 and creator effect | historic HOLD retained; not positive scientific support | DESIGN_ONLY / NOT_RUN |
| QA-011..013 | weather | expired warning, agency warning vs model, dated historical example | fail stale/mislabelled; historically labelled example eligible for review only | DESIGN_ONLY / NOT_RUN |
| QA-014..016 | military/war | contract vs fielded, single-side battlefield claim, topic title lock | HOLD on factual stage, claimant or certainty upgrade | DESIGN_ONLY / NOT_RUN |
| QA-017..019 | German history | fabricated quote, lost uncertainty in translation, reenactment | HOLD_UNVERIFIED_FACT/HOLD_REVIEW/HOLD_HARM | DESIGN_ONLY / NOT_RUN |
| QA-020..022 | disaster | synthetic actual footage, changing casualty count, unsupported causality | HOLD_HARM and disclosure / HOLD_UNVERIFIED_FACT | DESIGN_ONLY / NOT_RUN |
| QA-023..025 | general | R163 audio leap, R079 MOOC analogy, optional three-act | HOLD_SOURCE_ROLE or optional hypothesis card only | DESIGN_ONLY / NOT_RUN |
| QA-026..030 | review | self-review, overwritten disagreement, severity-3, unknown source, subtitle-as-prosody | HOLD_REVIEW / reject immutability / NOT_ASSESSABLE / reject media claim | DESIGN_ONLY / NOT_RUN |
| QA-031 | accessibility | color-only maps / uncorrected captions | HOLD_REVIEW | DESIGN_ONLY / NOT_RUN |
| QA-032..033 | analytics/science | CTR called retention; unexecuted T12 called RCT | reject metric conversion / HOLD_NOT_APPROVED | DESIGN_ONLY / NOT_RUN |
| QA-034 | change control | changed source invalidates dependent claim/title/draft | rewind and HOLD stale signoffs | DESIGN_ONLY / NOT_RUN |
| QA-035 | owner production | missing G18 owner authorization | HOLD_NOT_APPROVED; production_allowed=false | DESIGN_ONLY / NOT_RUN |
| QA-036 | read vs redistribution | private licensed access, no public redistribution | retain original prose; candidate machine export reason HOLD_RIGHTS | DESIGN_ONLY / NOT_RUN |

## Detailed WB crosswalk regression cases (new supplements, not rewritten QA source)
1. WB-C01: N-01 and N01 address the same adapter (positive); N-01 to N02 collision or N-06 alias denied.
2. WB-C02: multiple native HOLD reasons are emitted together (positive); a mapping from HOLD_SOURCE_ROLE to PASS is rejected.
3. WB-C03: verified hash only with actual source hash method/bytes; null source hash never becomes verified.
4. WB-C04 / QA-002: `SourceRecord.retrieved_at` does not satisfy `EvidenceLink.reviewed_at`; absent `access_state` or assessment time holds. No original fixture mutation.
5. WB-C05: named owner attempting to waive active-hazard misinformation, copyrighted export, privacy, fabricated quote or unapproved release is blocked. Editorial option changes do not clear gates.
6. WB-C06: even simulated complete QA and AP-00 planning review cannot reach `RELEASED` or `production_allowed=true`; research-only terminal state enforced.
7. WB-C07 / QA-036: permitted private read-only review does not allow source-byte export; attempted public export yields machine `HOLD_RIGHTS`, while original source expectation is unchanged.

## Future runtime evidence requirements, not claimed
A separately authorized implementation would need deterministic synthetic fixtures with exact original QA IDs; test input pins and output files; gate reason log, timestamps, source versions, independent reviewer, negative & positive expected-vs-actual diffs, reproducible command/environment and 36 actual pass/fail verdicts. 36/36 hypothetical passes would not prove a legal right or retention effectiveness; it would not trigger production `RELEASED`.

**STATIC_QA36_CONTRACT_COMPATIBLE_AS_PROPOSAL**; **RUNTIME_QA_NOT_EXECUTED**; **PROTOTYPE_NO_GO**.
