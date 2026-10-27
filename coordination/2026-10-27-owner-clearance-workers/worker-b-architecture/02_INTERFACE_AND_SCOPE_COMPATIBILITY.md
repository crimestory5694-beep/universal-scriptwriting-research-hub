# Worker B — Interface and Frozen Scope Compatibility

**Source pin:** original F07–F10/F12 `main@ea07c53375e64ebbd6724a35a57d1b245526d1a8` (same Git blob identities at `main@38d743640534cb390865824d36aeb2c890d628aa`). Frozen candidate `coordination/2026-10-27-preclaude-task2-prototype-scope-freeze/00_FROZEN_CANDIDATE_SPEC_NO_AUTH.md` at `38d743640534cb390865824d36aeb2c890d628aa`. **Review type:** documentation-only crosswalk, not amendment to original files or deployed interface.

## Aligned requirements (design review only)
1. F07 lists A00–A10: 11 logical components. F08 includes IntakeEnvelope, ContextProfile, SourceRecord, EvidenceLink, AtomicClaim, TopicLock, OptionCard/Outline, DraftSpan/VisualSpan, GateDecision, ReviewPacket, RunBundle/ReleaseDecision.
2. F09 defines five domains corresponding to frozen N01–N05; F07's risk overlays and the "most protective" policy are consistent with the freeze.
3. F10 P0–P10 controls distinguish source access versus redistributable rights, unsupported material, consequences, time, subject/object topic lock, independent reviewer, experiment consent and owner publication approval.
4. F08 `claim_verdict=NOT_CHECKABLE` is distinct from CONTRADICTED, and F10 asserts zero production approvals; both match Task2.
5. All texts prohibit unsupported causal or audience efficacy conclusions; K029–K031 not promoted; original QA ID set stays intact.

## Documentation anomalies and proposed **future** clarifications (do not change original IDs)
| ID | Location at source pin | Severity | Observation | Proposed documentation-only resolution (requires owner/technical reviewer) |
|---|---|---|---|---|
| WB-C01 | F09 headings `N-01..N-05`; Task2 `N01..N05` | LOW | Typographical naming mismatch for same five domains | Add an external crosswalk `N-01=N01` etc. Never rekey historical source or mock adapter automatically. |
| WB-C02 | F07 state holds `HOLD_MISSING_SOURCE`, `HOLD_RIGHTS`; F10 P0-P10 `HOLD_SCOPE`, `HOLD_ORIGINAL_MISSING`, `HOLD_SOURCE_ROLE` | MODERATE | No single enumerated HOLD reason-code registry links state machine to evidence gates | Draft versioned mapping outside frozen interfaces for signoff; preserve all original names and fail-closed statuses. |
| WB-C03 | F08 SourceRecord field `source_hash_if_verified`, but its prose says `hash_if_verified` | LOW | Ambiguous optional field alias | Clarify canonical field in a proposed v0.2 change note only, retaining original USW-IFACE/0.1 unchanged. |
| WB-C04 | F12 QA-002 fixture "without access_state or review time"; F08 SourceRecord has `retrieved_at`, while `reviewed_at` lives on EvidenceLink | MODERATE | Fixture does not specify which review timestamp must be absent to trigger hold | Document field-level trace: source retrieval time vs evidence review time; QA-002 original fixture untouched and remains DESIGN_ONLY. |
| WB-C05 | F08 GateDecision lists `WAIVED_BY_NAMED_OWNER`; F10 critical constraints explicitly nonwaivable | MODERATE | A future naive implementer could treat all blockers as waivable | Define a separate non-waivable gate allow/deny list for approval; preserve nonwaivable source fabrication, rights/privacy/harm/public safety bars. |
| WB-C06 | F07 future `RELEASED` state; F08 `production_allowed` hard false; Task2 mock prototype `RESEARCH_ONLY_NOT_PUBLISHABLE` | MODERATE | Conceptual full-process graph can be confused with available mock release | Document explicitly that `RELEASED` and production transitions are *unreachable* in authorized mock scope. No production gate may self-authorize. |
| WB-C07 | F12 QA-036 expected "private review only; no source bytes"; F10 P1 uses `HOLD_RIGHTS` | LOW | Expected narrative outcome lacks machine reason-code equivalence | Future design-only expected-outcome crosswalk should retain QA-036 text and require `HOLD_RIGHTS` for attempted public export without rights. |

## Not mismatches; important distinctions
- F08 `PASS_FOR_DESIGN` means only limited design review, while Task2 `PASS_DESIGN_DOCUMENTATION` is a report label; neither grants AP-01/02 or production permission.
- F09's references to live NWS/GAO/archival guidance are a verification protocol, **not** actual as-of verification of public events and not redistribution rights.
- F10's source-depth and F08's rights fields are intentionally orthogonal; `FULL_READ` never entails redistribution.
- F08's no causal retentions rules and F10's `research_effect_status` are research classifications, not experimentally measured results.
- F10 P9 is a *future* experiment gate, not evidence that T01–T13 took place.

## Status of identified differences
All seven items are **documentation clarification proposals**, not approved changes to frozen v0.1. No original F07–F10/F12 content, historic QA ID, S/F/R/K/V/EDU ID, canonical G row, or source text was edited. Until actual owner AP-01/AP-02 and rights-custodian clearance, no code schema, Claude transfer or mock runtime should be created.

**Limitations:** Static textual comparison only; cannot establish executable interface compatibility, runtime behavior, formal type safety, file ownership or science efficacy without separately approved work.
