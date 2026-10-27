# Worker D — Data Contract, Gate and Transition Gap Ledger

Date 2026-10-27. Source-light engineering comparison only. Status values below refer to documentation completeness, not authorship or rights. Reference pins: B1 b8d477e00a965862bb6e3ac3ece6b1e00cecd5bb; proposed v0.2 d4b4a19f67772d4588b2ea7c3cd15b0b74e600fb; F07 803f2d87969f1610d742110b8287ef3f31667434; F08 cfbd1340f747ff658e67b9e88bd956c472ad4165; F10 33618d7e1905c4fa71730fe46fca17b9883f9cde.

Classification meanings: COMPLETE = sufficient source-light expression of invariant; MINOR_CLARIFICATION = principle correct but presentation/label incomplete; MATERIAL_GAP = a necessary independently checkable data or gate condition is not expressed; CRITICAL_GAP = explicit bypass or contradiction of a non-waivable guard. No critical bypass was found **in B1's stated constraints**; that does NOT mean building from B1 is safe or approved.

| ID | Tested invariant | Assessment | Loss of engineering meaning | Proposed repair reference |
|---|---|---|---|---|
| D01 | Record envelope and immutable revision identity | MATERIAL_GAP | B1 lists nine conceptual shapes but omits common schema_version, created_at_utc, actor_role, sensitivity and provenance null reason; claim revision is not pinned | T01/T02 |
| D02 | Access vs copying vs external transfer | MATERIAL_GAP | Separate access and reuse named, but no purpose-specific rights/allowed usage, private analysis vs redistribution or exact transfer allowlist and target | T02/T11 |
| D03 | Verified hashes vs unknown hash | MATERIAL_GAP | Good 'if any' warning, but no method/bytes/nullable source_hash_if_verified and no identity-conflict branch | T02 |
| D04 | Acquisition time vs evidentiary review time | MATERIAL_GAP | Two clocks acknowledged, yet required reviewed_at, reviewer_id, timezone and revision association not typed | T03 |
| D05 | Five distinct claim verdicts | MINOR_CLARIFICATION | Prose uses qualified vs proposed SUPPORTED_WITH_QUALIFICATION / NOT_CHECKABLE; enum and severity handling should be canonical | T03 |
| D06 | Stable subject/object and doubt | MATERIAL_GAP | B1 says preserve, but no lock digest, claimant, modal qualifier, approval field or revision-dependent revalidation | T04 |
| D07 | Reviewer independence and immutability | MATERIAL_GAP | Different reviewer stated; missing immutable initial verdict, review-version binding, coverage fractions and role separation | T06 |
| D08 | Multiple simultaneous HOLD reasons | MATERIAL_GAP | Stated preserve all reasons, but no native_reason_codes[] keyed by gate, unknown-reason handling and append-only transition log | T05 |
| D09 | Production and external release blocked | COMPLETE | B1 unambiguously requires never-public mock output, production_allowed=false and no RELEASED path; implementation still untested | Retain T11 |
| D10 | Source-revision invalidation | MATERIAL_GAP | Dependency and revocation narrative exists but lacks graph, recheck trigger and superseded hash on every descendant | T07 |
| D11 | Offline synthetic-only I/O boundary | COMPLETE | B1 forbids live calls and real source ingestion, uses fabricated fixtures and research-only outputs | Retain T08/T11 |
| D12 | P0–P10 explicit checks | MATERIAL_GAP | B1 stop rules cannot be traced mechanically to eleven canonical gate IDs, gate outputs and safety HOLD codes | T05 |
| D13 | State-machine and A05/A06 producer cycle | MATERIAL_GAP | No transition metadata or resolvable provisional TopicLock; source refresh rewind and idempotent retry missing | T01/T07 |
| D14 | Creative-science distinction | COMPLETE | B1 correctly labels options as hypotheses and prohibits automatic efficacy claims | Retain T09 |
| D15 | Evidence-source admissibility and quarantine | MATERIAL_GAP | No formal role matrix preventing F-190, R052, K029–K031 and creator/caption upgrades | T03/T10 |
| D16 | Review vs quality score or trial execution | MATERIAL_GAP | QA36 design and T01–T13 unexecuted acknowledged but no typed experiment/study approval, denominator and NOT_ASSESSABLE | T06/T09 |
| D17 | AP/G authorization identities | MATERIAL_GAP | AP00/01/02/G17/G18 status mentioned but exact scope, responsible approver, destination and G19 independent QA not gates | T11 |

## Explicit P0–P10 coverage table

| Gate | Required engineering outcome | B1 status | Missing structured element / required HOLD |
|---|---|---|---|
| P0 SCOPE | fail incomplete intake | MATERIAL_GAP | IntakeEnvelope mode, authority and version; HOLD_SCOPE |
| P1 RIGHTS | separate read and redistribute/transfer | MATERIAL_GAP | scoped rights decisions and export class; HOLD_RIGHTS |
| P2 IDENTITY | source revision and original-identity integrity | MATERIAL_GAP | hash method and historical namespace; HOLD_ORIGINAL_MISSING or HOLD_DISPUTED_PROVENANCE |
| P3 ADMISSIBILITY | source role/conflict quarantine | MATERIAL_GAP | EvidenceDisposition relationships; HOLD_SOURCE_ROLE |
| P4 CLAIMS | full claim attribution and truth state | MATERIAL_GAP | EvidenceLink clock/locator/severity coverage; HOLD_UNVERIFIED_FACT or REJECT_CONTRADICTED |
| P5 TIME | as-issued and local validity recheck | MATERIAL_GAP | issued_at/valid_until/timezone/recheck; HOLD_STALE_FORECAST or HOLD_NEEDS_RECHECK |
| P6 TOPIC | locked referents and uncertainty | MATERIAL_GAP | versioned topic digest, owner decision; HOLD_TITLE_PREMISE |
| P7 NARRATIVE | optional safe structure with honest promises | MINOR_CLARIFICATION | option grade/status, story promise and domain precedence; HOLD_HARM |
| P8 INDEPENDENT_QA | frozen independent reviewer evidence | MATERIAL_GAP | role and coverage schema; HOLD_REVIEW |
| P9 EXPERIMENT | no unapproved human/causal tests | MINOR_CLARIFICATION | typed StudyApproval and metric origin; HOLD_NOT_APPROVED |
| P10 PUBLICATION | permanently impossible actual release in mock | COMPLETE in denial rule; MATERIAL_GAP in audit wire contract | no real release; deny export/transfer; HOLD_NOT_APPROVED |

## Dependency ledger and negative thought experiments (NOT executed)

- A05 consumes TopicLock while A06 is its producer in F07/v0.2. Thought case: offer an option before immutable referents exist. Result required: HOLD_DEPENDENCY, do not infer a lock.
- A02 receives inaccessible, disputed or creator-only sources. Thought case: R052 or F-190 cited as independently verified. Result required: HOLD_SOURCE_ROLE.
- A01 reads allowed restricted source; external export not granted. Thought case: SourceRecord FULL_READ but rights_redistribution_status unset. Result required: HOLD_RIGHTS, no bytes transferred (QA-036 is DESIGN_ONLY).
- A04 receives NOT_CHECKABLE high-severity number. Thought case: positive option attempts to reclassify unknown as supported. Result required: HOLD_UNVERIFIED_FACT; keep NOT_CHECKABLE as semantic status, never zero or false.
- A08 reviews a corrected-source descendant with stale signoff. Result required: revoke downstream validity while retaining frozen historical review.
- A10 receives all mock approvals stamped PASS_FOR_DESIGN. Result required: production_allowed=false; RESEARCH_ONLY_NOT_PUBLISHABLE or HOLD_NOT_APPROVED.

These are proposed contract expectations, not QA results. Original QA-001–036 remain DESIGN_ONLY (0 executed); T01–T13 remain NOT_EXECUTED. Rights review and strategy choice occur outside Worker D.
