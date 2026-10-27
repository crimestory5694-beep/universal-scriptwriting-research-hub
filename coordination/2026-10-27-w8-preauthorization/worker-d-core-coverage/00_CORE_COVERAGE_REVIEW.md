# Worker D — Independent A00–A10 Core Coverage Review

Date: 2026-10-27 | Nature: public-safe, original technical analysis | Approval: NONE | QA36: DESIGN_ONLY, NOT_EXECUTED.

## Scope and evidence pinning

Repository: crimestory5694-beep/universal-scriptwriting-research-hub; actual main and Worker D branch start at 0776afd52001c2d9021b1749f7b936bc1dc4e37d (verified from GitHub branch metadata). This audit reads, but does not modify, Draft PR #12, head 1e496c994835742bfdd63ffac0679ba8123e1734 (draft, open, unmerged).

- Master orchestration plan: research/w8-master-orchestration, coordination/2026-10-27-w8-preauthorization/00_MASTER_ORCHESTRATION_PLAN.md, blob 7d59098426914016f76918050efd1f74abf62a23.
- Candidate B1 (comparison target): PR #12 head, coordination/2026-10-27-ap00-source-strategy-option-b/02_OPTION_B_SOURCE_LIGHT_MOCK_SPEC_V01_PROPOSED.md, blob b8d477e00a965862bb6e3ac3ece6b1e00cecd5bb, manifest-reported 8425 UTF-8 bytes / SHA-256 1e499670d1c554f77c6dbac64d715d9d5196a45fc711eddc2d50be76fcc8cd46. Rights unresolved.
- Candidate v0.2 (comparison authority is **proposed**, not approved): research/ap00-final-spec-review@9ed29940cc435520ae64e12df95d8823a8e7fc41, coordination/2026-10-27-final-owner-review-workers/worker-a-ap00/03_PROPOSED_PROTOTYPE_SPEC_V02.md, blob d4b4a19f67772d4588b2ea7c3cd15b0b74e600fb.
- Original technical predecessors on pinned main: F07 01_ARCHITECTURE_AND_WORKFLOW.md, blob 803f2d87969f1610d742110b8287ef3f31667434; F08 02_INTERFACE_CONTRACTS.md, blob cfbd1340f747ff658e67b9e88bd956c472ad4165; F10 04_EVIDENCE_GATES_AND_QA.md, blob 33618d7e1905c4fa71730fe46fca17b9883f9cde. All live under worker-deliverables/skill-architecture/2026-10-27/.
- Canonical QA design matrix: same folder 06_ACCEPTANCE_TEST_MATRIX.csv, blob 88e89ee233c967c5b8a0b645b0d401f6c1d2ccea; 36 unique QA-001–036, all DESIGN_ONLY, no execution.

Pinning is evidence of repository content identity, not a statement of licence, ownership, safety approval, or transfer permission. F07/F08/F10 source rights have not been certified here. This review is an original summary, not a sanitized legal derivative certificate.

## Review method

Compared B1's nine compact record descriptions, eleven one-line core responsibilities and seven stop rules against v0.2's eleven conceptual interfaces, detailed SourceRecord/EvidenceLink/AtomicClaim/TopicLock/RunBundle contracts and P0–P10 gates, then checked F07 state machine / recovery, F08 field invariants, F10 negative controls and independence rules. Static design comparison only: no runtime, fixture execution, QA36 run, source-byte transfer, rights decision, Claude operation, or production evaluation. The full 11-row input/output/requirement/missing-field/failure matrix is in 01_A00_A10_TRACEABILITY.csv.

## Findings

**Verdict: B1 is a credible source-light orientation brief, but it is NOT a sufficiently lossless engineering contract for proposed v0.2.** It preserves the eleven named responsibilities, synthetic-only boundary, topic referent preservation, rights distinction in prose, independent-review principle, uncertainty and terminal production prohibition. However it omits typed field and transition obligations that determine whether those principles can be audited, replayed or fail closed.

Module severity by exact one-row-per-module coverage: 9 MATERIAL_GAP (A00–A04 and A06–A09); 2 MINOR_CLARIFICATION (A05 and A10); 0 COMPLETE at full interface level; 0 CRITICAL_GAP at the *document orientation* level. Not assigning CRITICAL does not permit implementation. Crosscutting release denial itself is COMPLETE in stated intent, while its wire contract is still under-specified. Every missing mandatory field is HOLD rather than implicitly accepted.

### Eleven module judgements (not implementation permission)

| Module | B1 correctly carries | Essential meaning too compressed | Status |
|---|---|---|---|
| A00 | synthetic marker and subject/object | mode, content type, roles, scope authority and overlay/time schema | MATERIAL_GAP |
| A01 | distinct read/copy concept, source versions | immutable historical IDs, fields for depth, permissions, verified hash method and revisions | MATERIAL_GAP |
| A02 | quarantine and inaccessible sources | explicit source-role classifications, independence/conflict and historic no-promotion register | MATERIAL_GAP |
| A03 | more restrictive policy | named policy applicability/version/union, unmatched niche HOLD and risk roles | MATERIAL_GAP |
| A04 | five epistemic labels, claim links | typed atomic propositions, quantity/quote/time details, EvidenceLink relation and review denominator | MATERIAL_GAP |
| A05 | hypotheses, not success claims | explicit method statuses, counterexamples, editorial choice and scoped claim promises | MINOR_CLARIFICATION |
| A06 | original referents and qualifiers | title lock hash, uncertainty tokens, editorial approval, changed-revision rejection | MATERIAL_GAP |
| A07 | mock spans and disclosure | typed per-span lineage, source revision digest, visual authenticity and safe rejection | MATERIAL_GAP |
| A08 | independent reviewer and frozen dissent | formal reviewer-role lanes, critical coverage, NOT_ASSESSABLE and adjudication linkage | MATERIAL_GAP |
| A09 | science vs analytics separation | metric tier/denominator, separate approval record, T protocol NOT_EXECUTED enforcement | MATERIAL_GAP |
| A10 | production_allowed=false / release inaccessible | signed authorization identities, native gate ledger and exact P10 export decision shape | MINOR_CLARIFICATION |

### Ordering ambiguity requiring explicit resolution

F07 and v0.2 describe A05 as consuming TopicLock but A06 as producing TopicLock. This is not an executable acyclic dependency as written. B1 gives only sequential roles and conceals this tension. Minimum original design amendment: A00 first produces a provisional TopicIdentity (subject/object/question/status) that A05 uses; A06 then commits the final TopicLock after candidate evaluation, or A06 has an initial LOCK_PROVISIONAL step and finalization. Both approaches are **proposals, not silently accepted edits**. HOLD_DEPENDENCY until a named reviewer chooses one for a later contract.

A02 and A04 likewise need deterministic eligibility/evidence links; A05 must not treat provisional creative structures as source evidence; P5 time rechecks may rewind the graph before A06 or A08. Neither B1 nor this audit authorizes runtime evaluation.

## Architecture invariants

- Immutable provenance: historical S/F/R/V/K/EDU IDs never rekeyed; every relevant claim has version+locator+review identity. B1 mentions revisions but not their lifecycle.
- Rights orthogonality: lawful read, internal analytic use, public export and external Claude transfer are distinct. B1 correctly rejects implicit rights, but lacks per-purpose allowlist schema.
- Digest semantics: an actual verified hash is cryptographic identity of known bytes; nullable hash is never inferred from title/URL. B1's wording is safe, not field-complete.
- Two clocks: retrieved_at describes acquisition; reviewed_at describes evidence judgement. Both cannot be collapsed into a single source timestamp.
- Semantics: original subject/object, time, claimant, modality, doubt and allegedly/forecast qualifiers survive title and script restyling.
- Claim states: UNSUPPORTED, CONTRADICTED and NOT_CHECKABLE remain different; unassessable evidence may not improve support.
- QA: reviewer != sole author; frozen verdicts and appended adjudication; revoked downstream signoffs after evidence changes.
- HOLDs: all native reason codes coexist, optional human-friendly groups do not overwrite them; unknown codes HOLD.
- Release: final mock path never emits real RELEASED, production_allowed remains false; no source transfer or publication hook.
- Revisions: changed source invalidates dependent evidence, claims, topic/title, spans, reviewer signoffs and bundle.
- Simulation: fabricated records only; research-labelled outputs; no external fetch, account, API, live event publication or empirical experiment.
- P-gates: all P0–P10 checks remain gates in the proposed candidate, not a promise B1 currently specifies each interface.

## Contrary interpretations and limitations

A charitable reading is that B1 intentionally serves as a short planning brief, not a field-level implementation spec. Under that document purpose, compression is expected and some absences are *scope limits*, not textual errors. Under the user's requested standard—whether B1 adequately captures v0.2 core engineering meaning—it cannot yet be the sole future technical handoff. F07/F08/F10 are design sources with unresolved provenance/rights; finding a shared architecture does not grant permission to transfer or publish their original text. The candidate v0.2 itself may still change after AP-00 and technical review. No legal opinion, scientific-efficacy finding, rights-custodian attestation or owner decision is made.

## Required continuation

Apply original, source-light amendments from 03_MINIMUM_TECHNICAL_AMENDMENTS.md only after technical owner review; maintain an independent rights assessment and explicit AP-00 decision. Repeat deterministic paper mapping of all eleven A modules to P0–P10 and B2/QA36 semantics before any AP-01/AP-02 path. No original files changed, no Claude transfer, no production SKILL.md, no code generated, no test run.
