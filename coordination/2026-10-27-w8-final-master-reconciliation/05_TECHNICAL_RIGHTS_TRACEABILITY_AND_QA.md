# Wave 8 — Integrated Technical, Rights and QA Traceability (Design Review Only)

**Date:** 2026-10-27. Original main `0776afd52001c2d9021b1749f7b936bc1dc4e37d`; no merge; no owner approval. Evidence matrix and 50 independent worker file identities: `01_50_WORKER_FILES_HASH_MANIFEST.csv`. Comparison of A–H against unchanged main: all 50 additions restricted to their assigned coordination folders. The manifest gives each SHA-1 Git blob, independent content SHA-256 and byte length.

## Distinct scope judgments

| Dimension | Verified point | State |
|---|---|---|
| Source file integrity | 50/50 retrieved; 50 self-consistent Git blob values and independent SHA-256 records; 50 ADDED only; main unchanged at pinned SHA | File-content receipt verified, no original edits in branch compares |
| First B1 source-light proposal | B1 original blob `b8d477e00a965862bb6e3ac3ece6b1e00cecd5bb`; Worker D: 9 MATERIAL_GAP, 2 MINOR_CLARIFICATION; Worker B: CONTENT_SCREEN_CONDITIONAL | Not adequate as complete technical contract; external rights unresolved |
| Original B2 proposal | B2 original blob `8055702ab7fab28619c565dc21defd7ba22be79b`; Worker F: 5 match, 18 conditional, 13 material gap; Worker C: 22 content PASS, 12 conditional, 2 sanitization required; **36 rights unresolved** | Cannot claim semantic equivalence or reproduction licence |
| New B1 v0.2 | Fresh contract blob `96f45cbb9570d00c2a22a499b0ec34a821362d0c`; 15188 UTF-8 bytes, A00–A10 and N01–N05 design-only | Proposed correction, **independent acceptance pending** |
| New B2 v0.2 | Fresh contract blob `a643befb8e74536b4572d4f22812a2d411629bf2`; 13584 UTF-8 bytes, contiguous QA-001..036, DESIGN_ONLY | Proposed correction, **independent semantic and expression screen pending** |
| Software and human testing | Canonical QA36 all DESIGN_ONLY and T01–T13 NOT_EXECUTED | **0 real tests**; no claimed functional PASS |
| External file reproduction | No signed chain of title, exact destination, AP-02 or authorized original file manifest | RIGHTS_UNRESOLVED; `[]` |
| Development and release | AP-00 pending, AP-01 not authorized, G17/G18 HOLD, G19 unstarted | STOP before implementation and release |

## Detailed B1 trace and unresolved checks

1. Worker A identifies WB-C01/C02/C03/C06/C07 as research-level RECOMMEND_ACCEPT; WB-C04 (QA-002 retrieved_at/access_state/reviewed_at binding) and WB-C05 (P0/P9 and all critical waiver exclusions) require revision. The new B1 includes both corrections without rewriting original source tests. All seven still need **actual** owner/technical choices.
2. Worker D's 11-row matrix found nine material interface omissions and two minor issues. The revised B1 explicitly describes common immutable metadata, SourceRecord/EvidenceLink/AtomicClaim/TopicLock, native reason set, multi-HOLD graph, per-span metadata, independent frozen review and RELEASED impossibility. This is a paper remedy, not verified schema or executable validation.
3. The new B1 splits A06 *conceptually* into pre-lock and final outline, preventing an A05/A06 cycle while retaining **exactly one A06 module**. A07 takes PolicySet explicitly, and A08 retains PolicySet revision. A future independent state-machine reviewer must decide if every required dependency and role is unambiguous.
4. Worker E's five overlay safety review found fail-open potential where N05 appears general or the primary niche suppresses another hazard. The proposed union policy denies that shortcut. Later reviewers must check N01 alert authority/expiry, N02 deployment claims/civilian harm, N03 testimony/translation, N04 casualty/visual/climate causality, and N05 research generalization; fictional fixtures never substantiate real events.
5. Hash identity must only be computed from actual bytes; archived digest disagreements and `source_hash_if_verified`/legacy alias need explicit migration review. A metadata pointer does not grant provenance verification or reuse rights.

## Detailed B2 trace and remaining 36-case review

**Canonical source:** `worker-deliverables/skill-architecture/2026-10-27/06_ACCEPTANCE_TEST_MATRIX.csv`, Git blob `88e89ee233c967c5b8a0b645b0d401f6c1d2ccea`; each row `DESIGN_ONLY`.

**Worker F prior assessment:** 5 SEMANTIC_MATCH; 18 CONDITIONAL_MATCH; 13 MATERIAL_GAP. Material IDs: `QA-002, QA-007, QA-008, QA-009, QA-019, QA-020, QA-022, QA-023, QA-024, QA-030, QA-031, QA-033, QA-035`. Their proposed case intents are now all explicitly represented in new B2 descriptions. This is **traceable repair intent**, not an independently confirmed semantic PASS.

**Worker C prior expression screen:** `QA-003` (ambiguous 'protected' identifier) and `QA-006` (historical hash-like expression) were SANITIZATION_REQUIRED. New 003 uses an entirely fictional namespace assignment and append-only links; 006 uses *nine invented* hash disagreements and no historical EDU hash bytes. Separating test concept from protected source expression cannot by itself establish ownership or permission.

Remaining one-to-one verification criteria for an independent reviewer: fixture premise/negative oracle, denial or allowed outcome, source-role metadata, missing-field granularity, rights and media boundaries, P-gate reason fidelity, version invalidation, no copied historic fixtures, no missing QA IDs, no false claims of executed tests. Every row in new B2 has `PENDING_INDEPENDENT_EQUIVALENCE_AND_RIGHTS_REVIEW`, `source_copy_authorized=NO`, and `DESIGN_ONLY`.

Specific high-risk crosswalk: QA-002 provenance clocks; QA-007–009 historic exceptions (label-only B70–72/F-190/R052); QA-019–020 dignity and generated *video* authenticity; QA-022 hypothetical flood attribution; QA-023–024 R163 WPM/R079 90-second extrapolation; QA-030 media-audio inference; QA-031 map and spoken-caption semantics; QA-033 T12 non-executed RCT; QA-035 G18 signoff missing.

## Rights and security mismatch

Worker B and C content screens are not legal licence checks. The original B1 and B2 authorship/derivative chain requires an actual named custodian, licence/notices, source-specific rights scope, owner signature and destination matching. Any later signed AP-01 limited development permission cannot grant AP-02 transfer; a hypothetical read-only AP-02 cannot authorize code execution. Worker G's offline threat model remains unimplemented and must be independently tested under a *separate* authorized AP-01.

No bulk repo clone, automatic archive or F11 link traversal, third-party YouTube transcripts, participant data, credentials, real imagery, executable code, external service access or production `SKILL.md` is authorized. Source transfer allowlist remains empty. All candidate text is research-only and needs its own content/rights review.

## Honest verification boundary

New files were checked on GitHub for readable UTF-8, expected presence, exact 36 unique QA IDs, original QA IDs, basic stage/adapter/gate presence and DESIGN_ONLY labels. This is **static structural QA**, not an external expert opinion, legal clearance, program execution or peer-reviewed scientific evaluation. Rights custodian and independent technical reviewer must assess every crosswalk and decide whether original semantics are restored without using unlicensed source wording. Any unresolved material semantic difference remains HOLD.
