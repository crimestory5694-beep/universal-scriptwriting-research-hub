# Universal Scriptwriting — PROPOSED Offline Mock Prototype Specification v0.2
**Status: PROPOSED — OWNER REVIEW PENDING**
**ID:** `USW-IFACE/0.2-PROPOSED`; parent `USW-IFACE/0.1` (unmodified). This candidate is documentation, not executable schema, run-time, permission, authorization, or production `SKILL.md`.

## 0. Exact allowed planning boundary
Isolated, offline, text-only **future hypothetical prototype**, synthetic/mock inputs and outputs exclusively. No actual software implementation under this work order; no real current-event generation or publication; no network, external APIs, external accounts, source-rich archives, protected transcriptions, real media, paid inference, actual human study, performance assertion or external Claude transfer. Every hypothetical draft or output bears literal `RESEARCH_ONLY_NOT_PUBLISHABLE`. No fallback may remove the label. Internal data descriptions do not authorize moving even public repo files to another workspace.

## 1. Eleven conceptual core modules A00–A10
| ID | Ownership | Logical interface | Non-bypass invariant |
|---|---|---|---|
| `A00` | Intake & scope router | `IntakeEnvelope` → `ContextProfile` | require exact task, niche, subject, object, as-of and owner scope |
| `A01` | Source/rights registry | `SourceCandidate[]` → `SourceLedger` | immutably separate access/use/redistribution with per-version identity |
| `A02` | Evidence eligibility/conflict | `SourceLedger` → `EvidenceDisposition[]` | quarantine blocked R052; F-190; K029–K031 and disputed provenance |
| `A03` | Context/policy arbitration | `ContextProfile` → `PolicySet` | union of applicable restrictive niche, hazard and rights overlays |
| `A04` | Atomic claim laboratory | `TopicBrief + SourceLedger` → `ClaimLedger` | record SUPPORTED, QUALIFIED, UNSUPPORTED, CONTRADICTED, NOT_CHECKABLE |
| `A05` | Creative option registry | `ClaimLedger + TopicLock` → `OptionSet` | options/hypotheses only; no universal watch-time formula |
| `A06` | Subject/object lock and outline | `TopicBrief + OptionSet` → `TopicLock + Outline` | retain original referents and epistemic strength |
| `A07` | Synthetic draft assembly | `Outline + ClaimLedger` → `Draft` | trace each mock factual span to synthetic claim; research-only label |
| `A08` | Independent review | `Draft + ClaimLedger` → `ReviewPacket` | non-author reviewer and immutable disagreement records |
| `A09` | Quality and research separation | `ReviewPacket` → `EvaluationRecord` | style/analytics/human tests distinct; T01–T13 NOT_EXECUTED |
| `A10` | Release/transfer checkpoint | `RunBundle` → `ReleaseDecision` | hard false production_allowed; no Claude export or real release |
Source architectures original F07 Git blob `803f2d87969f1610d742110b8287ef3f31667434`, F08 `cfbd1340f747ff658e67b9e88bd956c472ad4165`; this revision adds only proposed reconciliation language, not new independent universal writing advice.

## 2. Exactly five contextual niche adapters
| Alias pair | Domain | Additional guard |
|---|---|---|
| N01 / N-01 | USA weather | as-issued official warning; issue and expiry; local counties, timezone; watch/warning/advisory distinct; no unsafe delayed warnings |
| N02 / N-02 | Military aircraft/conflict | procurement/prototype/testing/fielding distinct; competing war claims labelled; variant/date; civilian harm |
| N03 / N-03 | German WWI/II history | quotation/original archive, translation uncertainty, named source/date and dignified reconstruction |
| N04 / N-04 | Disaster reporting | update interval and casualty qualifiers; authentic versus synthetic footage disclosure; no unsupported causality |
| N05 / N-05 | General explainers/psychology | context-limited studies; optional structure; avoid MOOC/TTS extrapolation as viewer-effect law |
Canonical candidate adapter IDs are N01–N05; originals N-01–N-05 remain exact source aliases. Alias mapping is bijective and versioned; never create 10 adapters or mutate F09. Multiple overlays accumulate gates and choose the more protective result. Unmatched niche => `GENERAL_REVIEW_REQUIRED`/HOLD rather than permissive inference.

## 3. Versioned logical interfaces and provenance
All records: `schema_version`, `record_id`, `created_at_utc`, `actor_role`, `provenance_ref` or explicit null reason, and `sensitivity`. Versioned interfaces are descriptive, not executable:
- `IntakeEnvelope/0.2`: run_id, task_mode, niche/subniche, exact title+topic, language/audience region/expertise, publication_window, nonfiction_status, user_constraints, source leads, research authorization, release_authorization=NO, paid_tool_spend_authorized=NO. Unknown material field => HOLD_SCOPE.
- `ContextProfile/0.2`: primary adapter, overlays, local geographic and time/as-of scope, risk class, source issue/valid period, domain reviewer requirement, applicable policies.
- `SourceRecord/0.2`: immutable ID/namespace/version; source_kind, publisher, original URL or restricted ref (never protected content in public export), access_state (FULL_READ/PARTIAL/INDEX_ONLY/BLOCKED/MISSING), `retrieved_at`, `source_hash_method`, `source_hash_if_verified` (nullable, only actual bytes), `rights_access_status`, `rights_redistribution_status`, allowed usage and locator, independence family, `correction_of`. Old prose term `hash_if_verified` is a deprecated alias, not a second digest.
- `EvidenceLink/0.2`: source_id+revision, claim_id, source role, exact permitted locator, reviewer_id, `reviewed_at`, support/qualified/contradicts/contextual/non_support/inaccessible relationship, attribution and rights note. A retrieval date never substitutes for evidence review time.
- `AtomicClaim/0.2`: assertive paraphrase, subject/object, numeric scope, quote/date/as-of, epistemic status `SUPPORTED | SUPPORTED_WITH_QUALIFICATION | UNSUPPORTED | CONTRADICTED | NOT_CHECKABLE`, severity 0–3, provenance links, independent reviewer, next recheck. NOT_CHECKABLE is neither verified true nor false. A claim linked solely to synthetic input is *mock*, not authenticated nonfiction.
- `TopicLock/0.2`: original user topic/title, canonical subject and object, mechanism/question, qualification tokens, source revision set, title/lock hash and editorial owner approval state. Style can transform syntax but not referents, allegations or certainty.
- `OptionCard/Outline/0.2`: context-eligible structure, K source IDs as **research-only references**, uncertainty, counterexample and promises; forbidden scientific efficacy claims. Any K029–031 option is quarantined; 9 amendments await owner.
- `DraftSpan/VisualSpan/0.2`: span_ids, synthetic claim_refs, source revisions, text, disclosed synthetic visual status and accessibility meaning; no media/voice verification from captions.
- `GateDecision/0.2`: native_reason_codes[] preserved, `canonical_group` documentary crosswalk; PASS_FOR_DESIGN/HOLD/FAIL, critical_waiver_allowed=false, provenance revision, reviewer and remaining risks; never autogrant rights.
- `ReviewPacket/0.2`: dated frozen independent reviews, severity-3 coverage, NOT_ASSESSABLE for unavailable evidence, rights/safety/accessibility results, append-only adjudication (initial verdict immutable).
- `RunBundle/ReleaseDecision/0.2`: pinned artifact digests/source revisions, hold history, exact scope authorization (missing by default), production_allowed=false, result `RESEARCH_ONLY_NOT_PUBLISHABLE` only.

Historical IDs S/F/R/V/K/EDU/T/G/QA are immutable. An original Git hash represents file identity, not rights clearance. No private material or raw external source may be embedded in public output; publication-safe abstracts are separate from restricted bytes.

## 4. P0–P10 gate chain — fail closed
| Gate | Requirement | Mock proposed blocker |
|---|---|---|
| P0 SCOPE | exact user subject/object, niche, as-of, permissions | HOLD_SCOPE |
| P1 RIGHTS | separate lawful access, private analysis and redistribution | HOLD_RIGHTS |
| P2 IDENTITY | original revisions and historical IDs unchanged | HOLD_ORIGINAL_MISSING / HOLD_DISPUTED_PROVENANCE |
| P3 ADMISSIBILITY | no F-190/R052, creator or caption leap | HOLD_SOURCE_ROLE |
| P4 CLAIMS | traceable evidence/number/date/quote, qualifier | HOLD_UNVERIFIED_FACT / REJECT_CONTRADICTED |
| P5 TIME | current issue/validity/local time checked | HOLD_STALE_FORECAST / HOLD_NEEDS_RECHECK |
| P6 TOPIC | topic/subject/object/epistemic lock | HOLD_TITLE_PREMISE |
| P7 NARRATIVE | safe optional story options; no made-up reporting | HOLD_HARM / HOLD_SOURCE_ROLE |
| P8 INDEPENDENT_QA | non-author evidence review, disagreement, disclosure | HOLD_REVIEW |
| P9 EXPERIMENT | no observational metric as science; consent/scope | HOLD_NOT_APPROVED |
| P10 PUBLICATION | rights and separate formal signoffs plus code QA | HOLD_NOT_APPROVED |

Candidate `GateDecision.native_reason_codes[]` logs every original reason, never flattens out holds. Canonical grouping is **non-authoritative categorization**; all reasons remain attached. Unknown code => HOLD_UNKNOWN_REASON. Multiple simultaneous blockers accumulate, cannot convert to PASS. `WAIVED_BY_NAMED_OWNER` appears in original F08 but in this proposed mock **cannot apply to critical rights/privacy/factuality/source integrity/public-harm/authorization gates**; optional editorial choices never clear them.

## 5. State model and impossible production path
Candidate review states: RECEIVED → SCOPE_VALIDATED → SOURCES_TRIAGED → CLAIMS_REVIEWED → TOPIC_LOCKED → OPTION_SELECTED → OUTLINED → DRAFTED → INDEPENDENT_QA → RELEASE_REVIEW → `RESEARCH_ONLY_TERMINAL`. Conceptual original F07 state `RELEASED` is specifically **unreachable in v0.2 prototype**. Even positive QA, named mock owner or valid AP-00 cannot change `production_allowed=false`. Deny requests to publish, deploy, transfer source bytes, or generate production SKILL.md; output explicit HOLD_NOT_APPROVED. No production transition may exist in executable future mock scope.

Revision invalidation: any changed SourceRecord supporting a claim must invalidate dependent evidence-review/claim/topic/title/draft/signoff attestations and demand fresh independent review. Never silently reuse an older timestamp, hash, original title or prior approval.

## 6. Original QA contract compatibility and reviewer separation
Canonical QA source: `worker-deliverables/skill-architecture/2026-10-27/06_ACCEPTANCE_TEST_MATRIX.csv` blob `88e89ee233c967c5b8a0b645b0d401f6c1d2ccea`; exactly QA-001–036, 36 DESIGN_ONLY. Do not edit test IDs or expected original source text. QA-002 timestamp and QA-036 rights reason mappings live only in candidate adapter document; synthetic future fixture traces needed before any actual success claim. Independent reviewer cannot equal draft sole author; adjudicator preserves initial forms. `PASS_FOR_DESIGN` is not release approval. T01–T13 trials all unexecuted and separate from QA36.

## 7. Explicit knowledge and rights limitations
Original archive B70–72 exact missing; nine historical hash/91 observation boundary decisions unresolved; B25/B58/B06 exceptions; S08 restricted license; F-190 UNVERIFIED, blocked NPR R052, S63/R171 verification-depth differences, S39/S40 provenance issues, native A/V not verified. The 48-K register provides *no demonstrated viewer retention effectiveness*. Avoid imported universal hooks, hard word counts, mandatory 3-act, WPM optima, medical/neuroscience claims or performance forecasts. All nine proposed K amendments need case-specific owner/domain reviewer decisions, not implicit acceptance.

## 8. Authorization gates
AP-00 SPEC REVIEW PENDING. AP-01 isolated synthetic build NOT_AUTHORIZED. AP-02 item-level rights and transfer NOT_AUTHORIZED. AP-03 human/scientific studies NOT_AUTHORIZED. AP-04 production SKILL.md HOLD. AP-05 independent code QA NOT_STARTED. G17 HOLD; G18 HOLD; G19 NOT_STARTED. Nothing in v0.2 creates these approvals.
