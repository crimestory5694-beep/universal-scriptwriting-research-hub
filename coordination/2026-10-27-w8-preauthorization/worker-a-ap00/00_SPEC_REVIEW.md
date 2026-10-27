# Worker A — Independent AP-00 Specification / Interface Contract Audit
Date: 2026-10-27 | RESEARCH ONLY | NON-BINDING REVIEW | NO SIGNATURE

Repository: crimestory5694-beep/universal-scriptwriting-research-hub
Main observed: 0776afd52001c2d9021b1749f7b936bc1dc4e37d (verified through recent commit query, commit fetch and branch comparison).
Dedicated branch: research/w8-ap00-contract-review; assigned output folder: coordination/2026-10-27-w8-preauthorization/worker-a-ap00/
Proposed v0.2: https://github.com/crimestory5694-beep/universal-scriptwriting-research-hub/blob/9ed29940cc435520ae64e12df95d8823a8e7fc41/coordination/2026-10-27-final-owner-review-workers/worker-a-ap00/03_PROPOSED_PROTOTYPE_SPEC_V02.md
Master plan: https://github.com/crimestory5694-beep/universal-scriptwriting-research-hub/blob/research/w8-master-orchestration/coordination/2026-10-27-w8-preauthorization/00_MASTER_ORCHESTRATION_PLAN.md

## Method and source boundary
Independently inspected Git blob bodies for F07, F08, F09 and F10, canonical QA-001..036 CSV, main v0.1 scope freeze, pinned v0.2, its seven-row candidate matrix, WB source audit and Draft PR #10/#11/#12 metadata and relevant PR #12 Option B1 proposal. This is static source-text analysis, not parser, type, runtime, legal, safety or production validation.
Original Git blobs: F07 803f2d87969f1610d742110b8287ef3f31667434; F08 cfbd1340f747ff658e67b9e88bd956c472ad4165; F09 04c208fda0872ada977d2406d299f54c318a0e32; F10 33618d7e1905c4fa71730fe46fca17b9883f9cde; QA36 88e89ee233c967c5b8a0b645b0d401f6c1d2ccea; frozen v0.1 591dabfd1ee026bbe31fd086c152f4824f32a577; proposed v0.2 d4b4a19f67772d4588b2ea7c3cd15b0b74e600fb; Worker B baseline 9732e17be66e1bfce7ab76e0ec23ed2be2a4d739; original candidate WB matrix cf6792824a31ca101a318d5c544cf2ee2e19ad79.

## Direct contract findings
| Check | Static disposition | Independent reasoning |
|---|---|---|
| Exactly A00-A10 | PASS (design inventory) | v0.2 defines 11 unique conceptual IDs; not executable modules. |
| Exactly N01-N05 | PASS (design inventory) | Five one-to-one aliases of the F09 N-01..N-05 roles; not ten adapters. |
| P0-P10 guards | CONDITIONAL | Eleven named gates and fail-closed HOLD language exist; scope/experimentation critical-waiver policy needs explicit completeness (GAP-03). |
| Access vs copying rights | PASS (textual invariant), HOLD (permission) | Separate rights_access_status and rights_redistribution_status; no item rights granted. |
| Topic subject/object/epistemic invariant | CONDITIONAL | Safeguard clear; circular A05/A06 TopicLock producer/consumer order unresolved (GAP-01). |
| Immutable revisions | PASS (textual invariant) | Superseding SourceRecord invalidates evidence, title, draft, reviewer signoffs; runtime never tested. |
| Source admission limits | PASS (textual invariant) | F-190, blocked R052, K029/K030/K031 barred from scientific proof; original provenance limits retained. |
| Synthetic-only future boundary | PASS (textual invariant), HOLD (implementation) | Explicit offline, fabricated inputs, no live API/accounts, always RESEARCH_ONLY_NOT_PUBLISHABLE. |
| QA-001..QA-036 immutable | PASS (file comparison) | Canonical QA CSV has exactly 36 consecutive IDs, all DESIGN_ONLY; proposed crosswalk is not a rewrite. |
| T01-T13 | HOLD | NOT_EXECUTED, 0/13; no human or scientific inference. |
| Production/release | HOLD | AP-00 pending; AP-01 and AP-02 not authorized; no production SKILL.md or RELEASED. |

## Seven clarification recommendations — NOT owner decisions
1. WB-C01 RECOMMEND_ACCEPT. Versioned one-to-one alias catalog; reject N-06, collisions, double-activation. Parser review remains future work.
2. WB-C02 RECOMMEND_ACCEPT, conditional on a complete reason-code registry and lossless native-reason serialization. Group labels cannot erase simultaneous blockers.
3. WB-C03 RECOMMEND_ACCEPT, conditional on null/method semantics and old-field compatibility tests. Only actual byte-hash evidence is verifiable.
4. WB-C04 REVISION_REQUIRED. Retrieval clock and assessment clock are distinct, but QA-002's original wording describes a SourceRecord without 'review time' whereas reviewed_at is on EvidenceLink. Define explicit two-object fixture bindings and required reviewer role without changing QA-002.
5. WB-C05 REVISION_REQUIRED. The candidate prose names critical gates P1/P2/P3/P4/P5/P6/P7/P8/P10 but omits P0 and P9. Scope authority, research consent and experiment authorization must be explicitly unwaivable. No editorial override should alter ANY applicable critical blocker.
6. WB-C06 RECOMMEND_ACCEPT, conditional on defining total transition closure and distinction between research-only terminal and HOLD. RELEASED/PRODUCTION_APPROVED must have no transition.
7. WB-C07 RECOMMEND_ACCEPT, conditional on asset-specific lawful read scope and rights-custodian clearance. QA-036 literal expected phrase stays unchanged; export attempt returns HOLD_RIGHTS.

## Independently identified architecture gaps
- GAP-01 (HIGH, REVISION_REQUIRED): v0.2 A05 input includes TopicLock, while A06 produces TopicLock after consuming A05 OptionSet. This creates a conceptual cycle. Define a non-authorizing provisional referent boundary derived from A00/TopicBrief for A05, then a distinctly versioned final TopicLock at A06; reject any certainty change during either phase.
- GAP-02 (HIGH, REVISION_REQUIRED): F07 A07 uses Outline + ClaimLedger + PolicySet, while proposed v0.2 A07 signature lists only Outline + ClaimLedger. Restore immutable resolved PolicySet/context input explicitly; otherwise required niche/safety overlay provenance could be lost. A08 review should also pin the applied PolicySet revision.
- GAP-03 (HIGH, REVISION_REQUIRED): Critical waiver list must expressly encompass P0 and P9 as appropriate, including scope permissions and consent/ethics, and P10 cannot self-approve.
- GAP-04 (MODERATE, REVISION_REQUIRED): The proposed many-to-one canonical_group field lacks a closed documented mapping and unknown-code round-trip fixture. Define a versioned table, native reason array preservation, unknown->HOLD.
- GAP-05 (MODERATE, REVISION_REQUIRED): SHA field alias and timestamp fixture migrations lack actual type tests. Treat unset hash as unverified and do not imply hash_method is verified evidence.
- GAP-06 (MODERATE, REVISION_REQUIRED): A09 original signature includes StudyApproval but v0.2 conceptual signature does not. Specify mandatory no-study authorization/HOLD on any proposed human, behavioral or analytics study, with no execution under current scope.

## PR context and authorization
Draft PR #10: https://github.com/crimestory5694-beep/universal-scriptwriting-research-hub/pull/10, 8 added research documents; open/unmerged. Draft PR #11: https://github.com/crimestory5694-beep/universal-scriptwriting-research-hub/pull/11, 5 added research documents; open/unmerged. Draft PR #12: https://github.com/crimestory5694-beep/universal-scriptwriting-research-hub/pull/12, 8 added research documents; open/unmerged. Their design reports are reference material, not approval or rights attestations.
Recommended planning posture: CONDITIONAL / REVISION_REQUIRED before any AP-00 owner acceptance; exact missing signatures remain HOLD. All findings are reviewer recommendations, not owner, legal or QA authority.
