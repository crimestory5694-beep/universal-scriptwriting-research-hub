# Worker E — Five Niche Safety & Documentation Review

**Status:** INDEPENDENT DESIGN REVIEW / `DESIGN_ONLY` / `RESEARCH_ONLY_NOT_PUBLISHABLE`. Date: 2026-10-27. Owner and rights approvals: **NOT GRANTED**. No implementation, live research, real media, transfer, actual incident reporting, publishable script or executed QA.

## Verified baseline, document identity and scope

- Latest observed `main`: `0776afd52001c2d9021b1749f7b936bc1dc4e37d`; Worker E pre-write branch `research/w8-niche-safety` was at the same SHA.
- Master orchestration: `research/w8-master-orchestration`, path `coordination/2026-10-27-w8-preauthorization/00_MASTER_ORCHESTRATION_PLAN.md`, blob `7d59098426914016f76918050efd1f74abf62a23`.
- Draft PR #12 (open, draft, unmerged): `https://github.com/crimestory5694-beep/universal-scriptwriting-research-hub/pull/12`, head `1e496c994835742bfdd63ffac0679ba8123e1734`; Option B1 `coordination/2026-10-27-ap00-source-strategy-option-b/02_OPTION_B_SOURCE_LIGHT_MOCK_SPEC_V01_PROPOSED.md`, blob `b8d477e00a965862bb6e3ac3ece6b1e00cecd5bb`.
- Proposed v0.2: `coordination/2026-10-27-final-owner-review-workers/worker-a-ap00/03_PROPOSED_PROTOTYPE_SPEC_V02.md` at `9ed29940cc435520ae64e12df95d8823a8e7fc41`, blob `d4b4a19f67772d4588b2ea7c3cd15b0b74e600fb`; **unsigned and conceptual**.
- Original F09: `worker-deliverables/skill-architecture/2026-10-27/03_NICHE_MODULES.md` at `main@0776afd52001c2d9021b1749f7b936bc1dc4e37d`, blob `04c208fda0872ada977d2406d299f54c318a0e32`.
- Original QA-001–QA-036: `worker-deliverables/skill-architecture/2026-10-27/06_ACCEPTANCE_TEST_MATRIX.csv` at `main@0776afd52001c2d9021b1749f7b936bc1dc4e37d`, blob `88e89ee233c967c5b8a0b645b0d401f6c1d2ccea`; **36/36 DESIGN_ONLY, zero executed**. B2 synthetic crosswalk at PR12 head blob `8055702ab7fab28619c565dc21defd7ba22be79b` is a proposed aid, not an authorization.
- Original source architecture/third-party rights remain unresolved. Reviewed ideas and status, not permission to redistribute original files. This document is newly written review prose; public-readability is not transfer rights clearance.

## Adapters — count and conflict policy

Exactly five canonical context adapters (`N01`…`N05`), bijective aliases `N-01`…`N-05`. Alias pairs are **not ten adapters**. Exactly one primary context adapter for each mock intake; additional applicable controls accumulate. Safety, privacy, time, rights, evidence and authorization gates remain mandatory regardless of selected primary. An unrecognized niche or unclassified hazard must return `GENERAL_REVIEW_REQUIRED` / HOLD, not default to safety-free N05. Topic and uncertainty preservation are crosscutting invariants.

## N01 — USA Weather (N-01)

**Finding: DESIGN-COVERAGE CONDITIONAL.** F09 is more specific than B1's concise summary: require hazard type, source-issuer authority, issued/valid-from/valid-until, as-of including local time zone, exact affected counties/regions, map revision, observed-versus-forecast-versus-historical status, confidence, and next-recheck policy. NWS/WFO/NOAA/NHC/WPC/SPC are examples of role-appropriate *real-world review targets*, not sources consulted for this fictional audit. A mock model forecast cannot become an issued WATCH, WARNING or ADVISORY. Protect immediately useful safety information from a curiosity-hook delay. Do not claim street-level certainty on unsupported geography. Existing design case mapping: QA-011/012/013, QA-034.

**Unresolved design gap:** B1 mentions expiry and locality but does not independently specify an unambiguous issuer/alert-category typed field, region-map version or urgency override. V0.2/F09 add these. The proposed B1 contract should require a strict time/issuer/authority triage with a failing unknown state. No live warning verification was performed.

## N02 — Military / Aviation / Conflict (N-02)

**Finding: DESIGN-COVERAGE CONDITIONAL.** Explicitly track technology maturity (`proposed / contracted / prototype / testing / low_rate_production / fielded / reported_in_combat`), exact variant, as-of/event date, test conditions, claimants and independent corroboration. Brochure performance is not achieved operational effect. Single-party conflict reports remain attributed allegations; unknown battlefield outcomes cannot turn into confirmed victory or causal air-defense failure. Competitor-title restyling must preserve subject, object and disputed/conditional premise (TopicLock). Civilian harm, dignity and absence of detailed tactical targeting instructions are overriding hazards. QA-014/015/016; also QA-034 for corrections.

**Unresolved design gap:** B1 says only proposed/contracted/tested/operational; F09/v0.2 add intermediate phases, test context and civilian-harm review. Make the distinctions explicit in a future typed fixture; independent source count alone does not guarantee independent evidence.

## N03 — German WWI/WWII Human Stories (N-03)

**Finding: DESIGN-COVERAGE CONDITIONAL.** Archive locator, date, person identity, exact original-language quotation, edition, verbatim/transcription status, translation reviewer and retained grammatical uncertainty are separate checks. Dramatic inferences about private thoughts or unrecorded last words are not authentic historical quotations. Reenactments and synthetic tableaux must be identified, not described as recovered archive. Dignity, survivor privacy and sensitive-person review beat narrative hooks. QA-017/018/019 and QA-005/036 where archive reproduction rights matter.

**Unresolved design gap:** B1's compact statement does not enumerate archive collection, quotation status, German idiom/uncertainty preservation or individual rights. A German-language reviewer is not proof an archived quote exists; audio quality must not be inferred without actual sound.

## N04 — Disaster Documentary (N-04)

**Finding: DESIGN-COVERAGE CONDITIONAL.** Incident identity, geography, time/as-of, authority, provisional casualty evidence, correction chain, eyewitness/source status, footage origin, reproduction rights, generation flag, disclosure, affected-person privacy and climate-attribution scope require separate treatment. Realistic AI illustrations or avatars must never masquerade as incident recording or an eyewitness. Distinguish observed event facts, causal explanations and long-term climate attribution. Incident estimates are not final totals. QA-020/021/022; QA-034 for changed evidence. All incidents used in this package are invented and not asserted as actual news.

**Unresolved design gap:** B1 abbreviates rights/privacy, which F09 requires. Where N04 overlaps N01, the stricter hazard and alert checks win. No live-disaster or official media policy check has been run.

## N05 — General Explainer / Psychology (N-05)

**Finding: DESIGN-COVERAGE CONDITIONAL.** Require precise research question, discipline, evidence type, population, selection bias, confounding, limits of analogy, disagreement and domain transfer. For educational/psychology claims, study findings are not universal neuroscience or clinical advice. Creative strategies (direct answer, paradox, chronology, optional acts) are unvalidated options, not fixed word-count/hook/retention laws. MOOC and synthetic TTS examples cannot establish video viewer outcomes. CTR, starts, watch duration and retention are distinct measures. K029–K031 remain quarantined, T01–T13 remain NOT_EXECUTED. QA-010/023/024/025/032/033.

**Unresolved design gap:** N05's 'general' label might conceal a health, real conflict, active hazard or finance claim. Require hazard/domain overlay arbitration and specialized HOLD before general editorial eligibility; an absence of the right reviewer cannot default to PASS.

## Crosscutting design risks, severity and repairs to propose (not implement)

| Priority | Design concern | Suggested non-executable interface correction | Crosswalk |
|---|---|---|---|
| P0 | Unknown niche / issue-as-of / issuer | HOLD_SCOPE until context and local timestamp complete | A00/A03, P0/P5 |
| P0 | Conflicting multiple overlays | Carry union of reasons; any critical blocker means HOLD, even after a permissive check | A03, P1–P10 |
| P0 | False/current/historic alert or incident | Validity + revision provenance; invalidate titles, draft spans and QA downstream | A01/A04/A08, P4/P5 |
| P0 | Topic certainty upgraded | Preserve referents, epistemic status and exact allegation through title/outline | A06, P6 |
| P0 | Source rights/privacy | Separate reading, reuse, derivative and redistribution. Refuse source-byte copying without clearance | A01/A10, P1/P10 |
| P0 | Synthetic authenticity claims | Preserve generator flag and clear prominent disclosure; disallow impersonation | A07/A08, P7/P8 |
| P1 | Specialist reviewer missing | Domain knowledge gaps marked NOT_ASSESSABLE/HOLD, no self-certified review | A08, P8; QA-026/029 |
| P1 | Unproven retention/causal claims | Keep hypothesis, analytics, empirical study and attribution separate | A05/A09, P3/P9 |

**Alternative hypotheses and conflicts:** (1) Short B1 may intentionally be a compact planning index, not a complete runtime contract; missing field enumeration may be resolvable by external typed schemas, but absent schemas cannot count as implemented protection. (2) A safer treatment of double-tagged events is to hold on *all* applicable failures; selecting only the primary adapter is more convenient but directly conflicts with F09/v0.2 fail-closed arbitration. (3) A visibly fictional positive text mock can meet *design eligibility* without proving factual authenticity or licensed redistribution; positive mocks cannot reduce P10 restrictions. (4) Some historical/local hazards are retrospective; an expired alert can be contextually valid **only** if clearly historical and never masquerades as active.

## Evaluation and limits

- Case design: 15 fictional negative + 5 fictional positive single-adapter fixtures in `02_SYNTHETIC_COUNTEREXAMPLES.md`; eight additional combined-overlay fixtures in `03_CROSS_OVERLAY_FAIL_CLOSED_CHECKS.md` (all `DESIGN_ONLY`).
- Guard matrix: 35 rows, seven per adapter in `01_FIVE_NICHE_GUARD_MATRIX.csv`, each `DESIGN_ONLY`.
- This review checks documentary consistency and identifies design gaps only. **No executable gate was run, no live agency warning was checked, no real-world testimonial or casualty was collected, no human retention study was performed and no genuine copyright authorization was obtained.** Evidence of proposed wording is not evidence of functioning controls.
- Proposed technical spec v0.2 still awaiting AP-00 owner decision; AP-01/AP-02 NOT_AUTHORIZED; G17/G18 HOLD, G19 NOT_STARTED. Production remains hard false and `RESEARCH_ONLY_NOT_PUBLISHABLE` for any hypothetical result.

## Recommended Worker E finding

**CONDITIONAL_DESIGN_COMPLETENESS / NO_RELEASE / NO_TRANSFER.** Preserve five adapter identities, expand B1's terse distinctions using rights-safe newly authored typed requirements only after independent architecture/rights review, and require written independent review before any future mock execution. Do not import F09 verbatim into another workspace or treat this audit as rights clearance.
