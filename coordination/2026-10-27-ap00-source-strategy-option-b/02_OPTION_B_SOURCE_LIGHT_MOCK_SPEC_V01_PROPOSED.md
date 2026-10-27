# Option B1 — Source-Light Mock Engine Contract v0.1-PROPOSED

**RESEARCH DOCUMENT — RIGHTS REVIEW REQUIRED — NOT APPROVED FOR CLAUDE COPY OR CODE.**

Date: 2026-10-27. This is new concise planning prose synthesized from the project’s proposed v0.2 research architecture, **not an independently proven or legally cleared original invention**. No copyrighted original source body, raw transcript, private research, credentials, external code or archived file is appended here. Do not infer a right to reproduce this document externally without separate custodian review.

## Purpose and boundary

A possible future *offline, text-only*, synthetic/mock-data-only engine for evaluating whether draft script plans respect topic, evidence, rights, niche context and review gates. It neither writes publishable current-affairs documentaries nor connects to live databases, accounts, models, audio/video providers or paid services. A simulation must expose `RESEARCH_ONLY_NOT_PUBLISHABLE` prominently and must not provide an export-to-publication command.

Inputs are **fabricated** short records provided with the synthetic fixture; no online discovery is part of the engine. Outputs are diagnostics, a nonpublic mock outline/text and an audit trail of blocked decisions. Production and empirical effectiveness are explicitly outside this scope.

## Logical data model — compact proposed shapes, not software schemas

| Record | Minimum logical fields |
|---|---|
| RunContext | run ID, synthetic flag, project niche, intended language, as-of timestamp, original subject/object/topic, allowed scope, expiry |
| SourceEntry | invented source ID, source revision, accessibility status, reuse/redistribution status, content-verification status, retrieval timestamp, exact verified hash if any |
| EvidenceAssessment | source revision, distinct assessment timestamp, reviewer identity, relation to claim, independence flag, explicit uncertainty |
| ClaimEntry | claim ID, referents, supporting assessments, current epistemic label, qualifying phrases, severity, related source versions |
| TopicBoundary | unchanged original referents, uncertainty qualifiers, topic mechanism, proposed syntactic restyling and mismatch flag |
| DraftTrace | outline/draft span ID, linked synthetic claim IDs, optional story-card selection, synthetic disclosure and time scope |
| ReviewRecord | author ID, genuinely different reviewer ID, immutable initial verdict, later separate adjudication and revision links |
| GateOutcome | all original deny/hold reasons, optional grouped labels, review version, unresolved risks and non-overridable block |
| MockResult | research-only outline/draft or HOLD report, revision/digest list, never-public flag and next-action explanation |

A record's existence is not evidence that its source was read or that its rights were cleared. Source retrieval time and independent evidence-review time are different. If any required record, timestamp, original ID, reuse right or claim-support evidence is unknown, mark it **unknown/HOLD**, not verified or available for redistribution.

## Eleven conceptual processing responsibilities

- **A00 Intake:** validate synthetic marker, clear topic/subject/object, niche, date context and explicit scope; otherwise HOLD.
- **A01 Source provenance:** register invented sources by immutable ID/revision, record separate reading and copying permissions.
- **A02 Evidence triage:** quarantine inaccessible, disputed, missing, unreviewed or out-of-domain support; never promote a historical limitation to proof.
- **A03 Context arbitration:** combine all applicable safety, rights and niche protections; select the stricter requirement whenever they conflict.
- **A04 Claim inspection:** split draft assertions into small checkable claims and label each as supported, qualified, unsupported, contradicted or not-checkable; a fictional citation is not authentic nonfiction proof.
- **A05 Creative choices:** offer optional narrative orderings/format choices as *hypotheses*, never assert a guaranteed viewer metric.
- **A06 Topic boundary:** prevent a headline or outline from changing the subject/object or strengthening a reported allegation into a verified event.
- **A07 Mock composition:** build sample paragraphs from explicitly fake claims only; keep trace IDs and disclosure on every factual-style passage.
- **A08 Independent critique:** require a reviewer distinct from the author, retain disagreements without overwriting originals and invalidate obsolete approvals.
- **A09 Measurement separation:** distinguish synthetic unit-test outcomes, actual analytics and controlled scientific evidence; do not translate one into another.
- **A10 No-release boundary:** all paths finish in research-only result or HOLD; mock PASS never authorizes upload, public distribution, production Skill or Claude-file copy.

These are conceptual responsibilities only. The brief does not reproduce source code, full original schemas, or all detailed research requirements.

## Five context overlays (exactly one primary; additional protections may accumulate)

- **N01 Weather simulation:** treat alert issue time, validity end, locality and warning category distinctly; reject expired or wrongly attributed warnings.
- **N02 Military/aviation simulation:** preserve distinction between proposed, contracted, tested and operational equipment; label a party's battlefield assertion as an assertion.
- **N03 Historical human-story simulation:** no fabricated authentic quotations; carry uncertainty through translations and distinguish reconstruction from archive.
- **N04 Disaster simulation:** do not use invented casualty counts as confirmed, declare synthetic visuals and avoid unsupported single-cause narratives.
- **N05 General explainer simulation:** present studies and frameworks as conditional choices; do not claim universal hooks, fixed video durations or performance increases.

Aliases `N-01`…`N-05` may point to `N01`…`N05` one-to-one in future design, but are not six to ten distinct modules.

## Crosscutting stop rules

1. **Rights:** reading a record never implies permission to export source bytes; copying without proper permission is denied, including when a simulated owner demands an override.
2. **Evidence:** unavailable/missing/contradictory support cannot become positive evidence; keep all underlying HOLD reasons rather than collapsing to a green status.
3. **Time:** stale information and later source revisions invalidate their downstream claims, titles, drafts and sign-offs until fresh review.
4. **Truthfulness:** unsupported numeric facts, fabricated quotes, certainty upgrades, false media authenticity or harmful synthetic presentation block progression.
5. **Review:** the only author cannot certify independent fact review; a severity-high unsupported claim cannot be hidden by good style scores.
6. **Authorization:** source transfers, live calls, payment, implementation and publication require separate genuine approvals; a planning recommendation is not an approval.
7. **Simulation boundary:** final state is `RESEARCH_ONLY_NOT_PUBLISHABLE` or a HOLD record. Real `RELEASED` is unreachable and `production_allowed=false` for every test.

A future reviewer must determine whether this minimal description covers the source architecture adequately, particularly the legacy QA-002 timestamp nuance and QA-036 read/copy distinction. Missing technical detail should produce explicit change requests, **not a silent import of old files**.

## Related source lineage and excluded use

Lineage of **ideas/statuses only**: proposed `USW-IFACE/0.2-PROPOSED` at Worker A commit `9ed29940cc435520ae64e12df95d8823a8e7fc41`, original QA ID matrix blob `88e89ee233c967c5b8a0b645b0d401f6c1d2ccea`, seven-issue review blob `cf6792824a31ca101a318d5c544cf2ee2e19ad79`. References remain in the research origin, **not** authorized for recursive copying.

Original F07/F08/F09/F10/F12 all remain copyright/provenance-rights unresolved. Original F02, F11 and linked materials, F13 internal gate, protected transcripts and archives are excluded from any prospective B package. Experimental retention claims remain unproven, original QA-001…QA-036 tests DESIGN_ONLY and T01–T13 unexecuted.

**Approval state:** AP-00 pending; AP-01/AP-02 not authorized; G17/G18 HOLD; this newly authored contract itself not yet rights-attested and not transferable.
