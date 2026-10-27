# Worker D — Minimum Original Technical Amendments to B1 (Proposals Only)

These are newly authored source-light change requests, not modifications to B1, v0.2, F07/F08/F10, an implementable schema, or software. All require future owner/technical review; none certifies third-party rights.

## Amendment set (smallest adequate additions)

**T01 — Resolve graph and lifecycle (MATERIAL_GAP).** Add a one-page interface ownership diagram listing A00 through A10, mandatory stage inputs/outputs and stage dependency checks. Explicitly distinguish an A00 provisional TopicIdentity from an A06 final immutable TopicLock, or place a provisional A06 step before A05. A05 cannot require the final lock before its producer. Reject circular/unknown dependencies with HOLD_DEPENDENCY. Keep monotonic, archived stage outputs, not mutable in-place decisions.

**T02 — Common record and source integrity (MATERIAL_GAP).** All nine B1 logical types should carry schema_version, record_id, revision_id/digest, actor_role, created_at_utc, source/version references and sensitivity, with explicit unknown/null reasons. Source identity contains original namespace+ID, version, origin, access depth, internal usage/redistribution permission separately, allowed purpose, content hash method, verified hash if actually computed, correction_of, scoped locator, independence family. Unknown source bytes require null digest and HOLD; never label a URL-derived guess verified. Explicitly distinguish analyst access from allowed Claude transfer and public dissemination.

**T03 — Evidence and claims (MATERIAL_GAP).** Define EvidenceLink as (claim_id, source_id, immutable source_revision, locator, reviewer_id, reviewed_at, relation, reviewer evidence role, attribution). Retrieval time is a separate source event. Preserve evidence relations supports, supports_with_qualification, contradicts, contextualizes, non_support, inaccessible. AtomicClaim has proposition, entity/subject/object/claim kind, epistemic qualifier, numeric unit/denominator/baseline, issue and validity clocks/timezone, severity 0..3, verdict SUPPORTED / SUPPORTED_WITH_QUALIFICATION / UNSUPPORTED / CONTRADICTED / NOT_CHECKABLE, next recheck. No claim is verified by attaching only a fabricated source.

**T04 — Immutable topic and qualification (MATERIAL_GAP).** TopicLock stores exact received topic/title, claimant, canonical referents, disputed/forecast modal words, date/geography mechanism, source_revision_set, hash and editorial approval status. A candidate title/outline causing stronger certainty or changed referents emits HOLD_TITLE_PREMISE and cannot replace the old lock. On revisions, create an explicitly linked replacement, not a rewrite.

**T05 — Gate decision contract (MATERIAL_GAP).** Publish a concise P0–P10 to module/output/HOLD crosswalk. GateDecision retains gate_id, source/claim revision hashes, native_reason_codes[] (multiple supported), review_at, reviewer role, unresolved_risks, override prohibition and optional non-authoritative grouping. Unrecognized reason -> HOLD_UNKNOWN_REASON; unresolved reasons are a set, never collapsed to 'other' or PASS. P1/P4/P8/P10 critical restrictions cannot be waived through a cosmetic owner override.

**T06 — Review integrity (MATERIAL_GAP).** ReviewPacket explicitly records frozen draft_digest, independent review participants/roles, initial form digests, severity-3 totals and reviewed/unsupported/NOT_CHECKABLE denominators, source rights, harm, accessibility and translation, with NOT_ASSESSABLE for missing evidence. Require reviewer identity different from sole author; append adjudication after freeze; never erase dissent or promote a style score over source-related HOLD.

**T07 — Revisions and recovery (MATERIAL_GAP).** Document dependency edges SourceRecord(version) -> EvidenceLink -> AtomicClaim -> TopicLock -> OptionSet/Outline -> DraftSpan -> ReviewPacket -> RunBundle. Changed or corrected source invalidates **all** affected descendants by exact revision/hash (including title, disclosures and approval), produces new immutable versions and reopens time checks. Retries are idempotent by run_id, stage and source_revision_set. For active hazards re-enter SOURCES_TRIAGED when warning issue/validity changes.

**T08 — Per-span synthetic safety (MATERIAL_GAP).** DraftSpan fields include span_id, draft version, linked synthetic claim revisions, assertion strength, uncertainty lineage, safe disclosure and source-clock. VisualSpan includes whether synthetic, disclosure requirement and semantic accessibility notes; no video/audio authenticity inferred from text/captions. Every artifact carries RESEARCH_ONLY_NOT_PUBLISHABLE, and no externally readable media is accepted by the mock engine.

**T09 — Optionality and effect science (MINOR_CLARIFICATION).** OptionCard stores niche eligibility, evidence grade, research hypothesis status, counterexample, promises, critical-claim IDs, option selection and blocked K status. EvaluationRecord separates descriptive style rating, observed metric (with unit/time/population), and independently approved causal/human study. QA design success is not retention improvement. T01–T13 NOT_EXECUTED; observational metric cannot become randomized-study support.

**T10 — Explicit admission quarantine (MATERIAL_GAP).** Add role-typed EvidenceDisposition preventing the promotion of F-190, R052 and K029–K031 into verification or viewer-effect law. Historical ID and finding classifications remain immutable. Source depth, conflict and independent family recorded separately. Source links into historical F/R/S/EDU material remain locator-only unless independently permitted; no automatic source-body import.

**T11 — Permanent mock no-release and approval record (MINOR_CLARIFICATION).** Keep v0.2 mock terminal results exactly research-only/HOLD and production_allowed=false. Document denied transitions for RELEASED, public publishing, tool/network calls, paid spending, actual Claude transfer and production SKILL.md; no executable export primitive. Explicitly list AP-00 pending, option B not selected, AP-01/AP-02 NOT_AUTHORIZED, AP-03/04 HOLD, AP-05/G19 NOT_STARTED, G17/G18 HOLD. A future sign-off may authorize a separate task, never mutate this mock result into public release. Transfer allowlist empty until exact file hashes, rights custodian, named owner, destination and permitted scope are recorded elsewhere.

## Paper acceptance obligations for a later independent reviewer

1. Exactly eleven modules A00…A10 with single stage ownership and a resolved A05/A06 dependency.
2. A field-level crosswalk covering each v0.2 conceptual interface and mandatory common record metadata.
3. Every P0–P10 gate with at least one explicit HOLD path and an unoverrideable prohibition for critical conditions.
4. Distinct missing/read/reuse/redistribution and actual-hash states; no unverified evidence promotion.
5. Multi-HOLD plus source-revision invalidation graph retaining audit history.
6. Reviewer non-self signoff and frozen dissent; study-vs-mock execution status unambiguous.
7. No live/production/Claude transfer ability from the mock specification.

These are **static review criteria, not executed QA36 cases**. This worker has neither authorized nor implemented them. If any mandatory condition cannot be expressed in source-light original prose, classify B1 as INCOMPLETE_FOR_IMPLEMENTATION, retain rights and authorization HOLD, and seek an independent technical and rights review rather than importing restricted originals.
