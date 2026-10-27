# Step 1 — AP-00 Independent Technical Review of v0.2 (Recommendation, NOT Owner Decision)

**Status:** TECHNICAL_RECOMMENDATION_PASS_WITH_CONDITIONS / OWNER_AP00_PENDING. Research-only, dated 2026-10-27. No code build, transfer, skill release or scientific validation.

## Exact reviewed basis

- Canonical candidate v0.1: `main@0776afd52001c2d9021b1749f7b936bc1dc4e37d`, `coordination/2026-10-27-preclaude-task2-prototype-scope-freeze/00_FROZEN_CANDIDATE_SPEC_NO_AUTH.md`, Git blob `591dabfd1ee026bbe31fd086c152f4824f32a577`.
- Worker A proposed v0.2: `research/ap00-final-spec-review@9ed29940cc435520ae64e12df95d8823a8e7fc41`, `coordination/2026-10-27-final-owner-review-workers/worker-a-ap00/03_PROPOSED_PROTOTYPE_SPEC_V02.md`, blob `d4b4a19f67772d4588b2ea7c3cd15b0b74e600fb`.
- Seven-row decision matrix: Worker A `02_WB_C01_C07_DECISION_MATRIX.csv`, blob `cf6792824a31ca101a318d5c544cf2ee2e19ad79`; seven rows checked in the prior Master Audit.
- QA matrix: `worker-deliverables/skill-architecture/2026-10-27/06_ACCEPTANCE_TEST_MATRIX.csv`, blob `88e89ee233c967c5b8a0b645b0d401f6c1d2ccea`; 36 unique `DESIGN_ONLY` rows, zero actually executed.
- Rights review: Worker B `research/ap02-minimal-rights-audit@be96bcc937614c79714ebf9bb1bf38928bc5d4be`; six candidate documents all `RIGHTS_UNRESOLVED`, zero AP-02 signatures.

## Technical review of WB-C01…WB-C07

| ID | Reviewed question | Review recommendation | Minimum future verification |
|---|---|---|---|
| WB-C01 | N01 and N-01 are aliases | RECOMMEND_ACCEPT: explicit one-to-one alias map for five adapters, no IDs rewritten | Unsupported alias or duplicate adapter fails |
| WB-C02 | Original HOLD reasons versus grouped reporting | RECOMMEND_ACCEPT: retain all native HOLD codes, optional summary grouping never changes decision | Several blockers stay visible; none becomes PASS |
| WB-C03 | Source hash field mismatch | RECOMMEND_ACCEPT: `source_hash_if_verified` proposed canonical, legacy prose name alias only | Missing bytes/hash never becomes verified |
| WB-C04 | Retrieval timestamp and evidence-review timestamp | RECOMMEND_ACCEPT_WITH_NOTE: SourceRecord retrieval and EvidenceLink review are independent; missing required one blocks corresponding claim | Retrieval clock alone never certifies review |
| WB-C05 | Owner waiver language conflicts with critical blockers | RECOMMEND_ACCEPT_AS_HARD_GUARD: rights, provenance, privacy, factual accuracy, harm and production authorization cannot be bypassed by any editorial override | Simulated owner waiver of restricted copying or fabricated quote must fail |
| WB-C06 | Release path exists in conceptual lifecycle | RECOMMEND_ACCEPT_AS_HARD_GUARD: in the **mock prototype** real publish/deploy/RELEASED transitions are unreachable; `production_allowed=false` | Even 36 hypothetical passes cannot publish |
| WB-C07 | QA-036 private read versus redistribution | RECOMMEND_ACCEPT: interpret original QA as access-only where permission exists, attempted export without rights -> `HOLD_RIGHTS` | Protected source bytes must not be emitted |

**Seven proposals reviewed, seven recommended for an AP-00 planning vote; zero actually accepted by an owner.** The two hard-guard proposals C05 and C06 are the highest priority for a later independent safety/technical acceptance check. C02/C03 may require versioned schema adapters in a future build, so compatibility is conditional until actually implemented and tested.

## Proposed AP-00 planning outcome

Recommend **ACCEPT_WITH_RECORDED_CONDITIONS** only *if the actual owner subsequently chooses it*: retain `USW-IFACE/0.2-PROPOSED` as a candidate planning baseline, document the seven recommendations above, and require the future code phase to preserve all 36 QA IDs and a full negative-control gate audit. Do **not** treat the spec as a scientifically proven writing method or production Skill.

Conditions: 11 conceptual core roles A00–A10, five N01–N05 adapters, strict fail-closed policy, mock/synthetic text only, no external accounts/network/paid tools, explicit source rights, `RESEARCH_ONLY_NOT_PUBLISHABLE`; K029–K031 remain quarantined, nine research amendments are not approved, QA-001…QA-036 are `DESIGN_ONLY`, T01–T13 human/scientific protocols unexecuted. Historical F/R/S/EDU source limitations and original G gates unchanged.

**Authorization checkpoint:** `AP-00=PENDING`, `AP-01=NOT_AUTHORIZED`, `AP-02=NOT_AUTHORIZED`, `G17=HOLD`, `G18=HOLD`. This document neither signs AP-00 nor modifies the original v0.1, Worker A branch, PR #10/#11, QA matrix or source ledger.

## What the owner must still decide

The owner can ACCEPT / ACCEPT WITH REVISIONS / REJECT / DEFER, naming the exact v0.2 path/commit, whether C01…C07 are accepted individually, version/time, and reviewer. A recommendation in this report is **not** a choice already made by the owner.
