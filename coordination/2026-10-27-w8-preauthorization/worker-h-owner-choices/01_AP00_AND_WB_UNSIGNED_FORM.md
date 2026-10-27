# AP-00 — v0.2 and WB-C01–C07 Owner Decision Form

**DRAFT — NOT SIGNED — NOT AUTHORIZED**

**Candidate (immutable identity):** `USW-IFACE/0.2-PROPOSED`; `research/ap00-final-spec-review@9ed29940cc435520ae64e12df95d8823a8e7fc41`; path `coordination/2026-10-27-final-owner-review-workers/worker-a-ap00/03_PROPOSED_PROTOTYPE_SPEC_V02.md`; Git blob `d4b4a19f67772d4588b2ea7c3cd15b0b74e600fb`. **Seven-item evidence:** Worker A `02_WB_C01_C07_DECISION_MATRIX.csv`; blob `cf6792824a31ca101a318d5c544cf2ee2e19ad79`.

## AP-00 actual planning choice — NO CHOICE SELECTED
- [ ] `ACCEPT_AS_PLANNING_ONLY` — accept exactly identified planning reference, **not** implementation
- [ ] `REVISE` — list required changes and new hash/version before re-review
- [ ] `REJECT`
- [ ] `DEFER`

Owner decision: __________   Owner legal identity/authority: __________

Rationale, scope of decision and caveats: __________

Proposed version changes / replacement commit & blob (if revising): __________

Technical reviewer name, independent findings and date: __________

Safety reviewer name, findings and date: __________

Owner date and signature: __________   Decision expiry or reconsideration date: __________

## Mandatory individual WB choices (all unselected)
For **each** item: decision `ACCEPT_FOR_PLANNING_ONLY / REVISE / REJECT / DEFER`, exact amended wording, assigned reviewer and evidence, all blank.

| ID | Decision subject; future non-bypass condition | Owner decision | Revision / reviewer / evidence |
|---|---|---|---|
| WB-C01 | Five one-to-one aliases `N-01…N-05` → `N01…N05`; reject collision, never rewrite historical IDs | ______ | ______ |
| WB-C02 | Preserve all native HOLD/FAIL reason codes; optional canonical groups never upgrade verdicts | ______ | ______ |
| WB-C03 | `source_hash_if_verified` canonical; legacy `hash_if_verified` alias; unknown hash stays unknown | ______ | ______ |
| WB-C04 | Separate `SourceRecord.retrieved_at` from `EvidenceLink.reviewed_at`; QA-002 missing review date must HOLD | ______ | ______ |
| WB-C05 | Never waive critical rights, factuality, safety, harm, privacy, provenance, authorization or publication gates | ______ | ______ |
| WB-C06 | `RELEASED`/production/export unreachable in synthetic mock; `production_allowed=false`, mandatory research-only label | ______ | ______ |
| WB-C07 | QA-036 private read permission **not** redistribution; externally copying bytes without independent grant => `HOLD_RIGHTS` | ______ | ______ |

No decision is populated or inherited from PR recommendations. **Reviewers may recommend without acting as owner or legal custodian.**

## Hard exclusions / scope acknowledgement
- [ ] Reviewer has examined all A00–A10 modules, five niche overlays, P0–P10 fail-closed gates and typed-record constraints.
- [ ] Reviewer has examined no-copy/no-network/no-spend/no-real-human/no-production limits.
- [ ] Reviewer confirms non-waivable HOLDS, revision invalidation, independent reviewer and immutable disagreement records are essential.
- [ ] Reviewer has acknowledged original QA-001–036 = 36 DESIGN_ONLY / 0 EXECUTED; B2 = 36 newly described DESIGN_ONLY cases, not tests executed or proven equivalent.
- [ ] Reviewer has acknowledged T01–T13 NOT_EXECUTED, no causal viewer outcome/retention evidence; K029–K031 quarantine, F-190/R052 limits, original source-rights unresolved.
- [ ] Reviewer has acknowledged accepting AP-00 **never** authorizes AP-01, AP-02, AP-03, AP-04 or AP-05.

Unresolved issue ledger (WB item, severity, owner, disposition, deadline): __________

**Present state:** `AP00=PENDING`, `WB_C01..WB_C07=OWNER_REVIEW_PENDING`, `AP01=NOT_AUTHORIZED`, `AP02=NOT_AUTHORIZED`, `AP03=NOT_AUTHORIZED`, `AP04=HOLD`, `AP05=NOT_STARTED`.
