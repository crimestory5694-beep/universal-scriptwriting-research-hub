# Cross-Worker Conflict Register and Proposed Repair Sequencing

**Status:** cross-worker evidence reconciliation, not owner, safety authority, legal clearance, or completed implementation. In all cases the original files and original QA fixture text remain unchanged.

## Priority 0 — No implementation until resolved

| Master ID | Source workers | Independent issue | Proposed limited repair in NEW source-light candidate | No-go validation |
|---|---|---|---|---|
| CR-01 | A + D | v0.2 A05 consumes TopicLock, but A06 creates it; B1's narrative obscures circular flow | Introduce an A00-derived provisional topic-identity boundary without authorizing premise changes; A06 commits immutable final lock; explicitly version and invalidate both | No cycle, no unsupported certainty change |
| CR-02 | A + D + E | A07 contract omitted immutable resolved PolicySet/context required by original F07; A08 review trace also missing applied policy revision | Pin resolved safety/niche PolicySet revision as mandatory A07 composition and A08 review input, with fail-closed mismatch | Missing/superseded policy version produces HOLD |
| CR-03 | A + F | WB-C04 / QA-002 mixes SourceRecord access/retrieval timestamp and EvidenceLink independent review timestamp | Keep original QA-002 wording unchanged; design TWO missing-field synthetic tests (absent access_state; absent evidence reviewed_at) and block both as unverified | Retrieved timestamp alone never satisfies review |
| CR-04 | A + D + G | WB-C05 enumeration P1–P8/P10 omits P0 and P9 despite scope and study-consent risks | Explicit all-applicable-critical P0–P10 gate matrix: owner/editorial waiver cannot bypass scope, rights, truth, harm, privacy, research authorization, or production | Attempted P0/P9 waiver yields HOLD |
| CR-05 | A + D + G | A09 study approval/authorization input less explicit than F07; B1 compresses science-vs-analytics logic | Add explicit StudyApproval status/role, mandatory absent-by-default records and no human/analytics study path in mock | No T01–T13 data or causal claims; attempted study HOLD |
| CR-06 | F + C | B2 13 MATERIAL_GAP cases; 36 IDs alone do not preserve original QA meaning | Rewrite B2 as a new versioned candidate using only rights-screened original prose, exact negative preconditions and expected fail/HOLD tokens; run new independent static mapping | Full 36/36 semantic preservation required before treating as QA handoff |
| CR-07 | C + F | QA-003 and QA-006 need expression/provenance isolation, while QA-003/006 semantics still require original ID and provenance constraints | Use fictional collision/checksum cases with explicit original-ID immutability and disputed-source HOLD, no real EDU bytes/hashes; independently re-review rights + meaning | No original private archive leakage or lost denial reason |
| CR-08 | B + C + H | Neither original B1/B2 nor any new revision has affirmative rights/third-party expression reuse attestation | External transfer manifest remains []; authorized custodian documents author/control, embedded material, allowed recipient, attribution, exact bytes and revocation for every chosen new file | No AP-02 with missing rights evidence |
| CR-09 | G + H | Offline/cloud isolation is an untested design; exact target account/repository, network deny, developer and consent unsigned | Owner-specific AP-01 only later; preflight least-privilege, synthetic-only, no egress, no auto-import, non-author reviewer, no paid providers | No actual workspace, tool install, Claude run until approval |
| CR-10 | H + A | Owner AP-00 acceptance/source A/B/C selection not evidenced; reviewer technical recommendations not an owner's choice | Present an unsigned consolidated owner form with exact v0.2 revision and source strategy alternatives | No signed AP-00 or strategy choice inferred |
| CR-11 | E + D | B1 lacks detailed weather issuers/times, maturity/evidence provenance, archive/translation status and disaster/psychology safeguards | Extend source-light typed overlay contract in new B1 version, keep highest-risk overlays additive and unwaivable | Unrecognized or conflicting overlay => HOLD |
| CR-12 | A + F | Original QA-036 read vs export boundary can be weakened by general `internal review` wording | Gate by separately established access, reuse and redistribution scopes; unauthorized reproduction returns HOLD_RIGHTS | Read-only access never permits copied file export |

## Exact B2 material semantic gaps (Worker F)

`QA-002, QA-007, QA-008, QA-009, QA-019, QA-020, QA-022, QA-023, QA-024, QA-030, QA-031, QA-033, QA-035` = **13 MATERIAL_GAP**.

18 further cases are `CONDITIONAL_MATCH`; the remaining 5 are `SEMANTIC_MATCH`. Thus *all 36* original-ID semantics must be independently examined in a revised B2, not just the 13 material gaps.

Worker C expression classification is a different independent axis: **22 PASS** for bounded content screen, **12 CONDITIONAL**, **2 SANITIZATION_REQUIRED** (`QA-003`, `QA-006`), **0 EXCLUDE** in the visible text. These verdicts do not establish copyright copying rights. In particular, QA-003 is a *conditional semantic match* in Worker F and a sanitization case in Worker C; both perspectives must be satisfied simultaneously.

## Core modules exact design-gap summary (Worker D)

- `MATERIAL_GAP`: A00, A01, A02, A03, A04, A06, A07, A08, A09 (**9**).
- `MINOR_CLARIFICATION`: A05, A10 (**2**).
- `COMPLETE`: 0 at the full interface-definition standard.
- A short B1 orientation brief is not invalid solely for being short; it is **insufficient as sole source for a future executable mock's detailed contract**.

## WB clarification disposition (Worker A)

- `RECOMMEND_ACCEPT` for *technical owner consideration*: WB-C01, C02, C03, C06, C07 (5).
- `REVISION_REQUIRED`: WB-C04, C05 (2).
- `OWNER_SIGNED_ACCEPTED`: 0. WB-C05 omission of P0/P9 in a proposed waiver enumeration is a meaningful defect, not permission to bypass them.

## Safety overlay (Worker E)

Five adapter identities preserved; 35 guard rows (seven per adapter), 15 negative and five positive fictional single-adapter designs, plus eight dual-overlay examples, all **DESIGN_ONLY**. Missing typed domain specificity and real-world review are blockers to asserting that B1 has implemented a functioning safety system.

## Proposed revision workflow

R1: A+D+G coordinated technical re-authoring of a **new** proposed B1/v0.2 contract, addressing CR-01…05 and CR-11…12, with parent version/commit and explicit reject/default state; all new prose must be independently rights-screened.

R2: F prepares a new B2 coverage draft, C audits expression including QA-003/006, and F independently re-evaluates exact 36 semantics; neither may declare copyright clearance or actual executed test PASS.

R3: B reassesses revised B1 authorship/copying rights; C reassesses revised B2; E verifies niche overlays; H refreshes unsigned owner AP-00 and A/B/C decision forms to point at the **actual new** byte-pinned versions.

R4: Master reviews only completed new work and reports evidence. Actual owner/custodian approvals are **separate**, not automatically initiated by a passing research QA.

**No original files changed, no PR merged, no source copying, no implementation or production approval.**
