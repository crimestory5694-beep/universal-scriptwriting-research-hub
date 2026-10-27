# Universal Scriptwriting — Option B1 v0.2 Source-Light Contract (NEW CANDIDATE)

**PROPOSED / DESIGN_ONLY / RESEARCH_ONLY_NOT_PUBLISHABLE.** Independently re-authored conceptual research interface; not a runnable engine, not rights-attested, not technically accepted, and not approved for Claude copying. Supersedes **nothing** in the original PR #12. Date: 2026-10-27.

## 1. Scope, identities and terminal result

A hypothetical later-authorized **offline, text-only, synthetic-only** mock evaluation flow. Inputs must be fictional records with explicit `synthetic=true`, recorded test authorship, and a single task scope. No network access, current claims, real media, third-party transcripts, uploaded private data, external model/API use, automated installations, experiments, expenditures, source-file transfer, deployment, or production `SKILL.md`. Every output (including positive results) bears `RESEARCH_ONLY_NOT_PUBLISHABLE`, `production_allowed=false`, and `claude_transfer_allowed=false`; `RELEASED` is not a legal mock state.

**Exact canonical modules:** A00,A01,A02,A03,A04,A05,A06,A07,A08,A09,A10. **Exactly five canonical adapters:** N01,N02,N03,N04,N05. Each legacy `N-0x` alias resolves to the corresponding `N0x`; an unknown alias is HOLD, not a sixth adapter. One primary adapter is assigned; all applicable specialist/privacy/right/time overlays accumulate and never cancel a critical blocker.

## 2. Versioning and common record envelope

Every logical record carries `schema_version`, `record_id`, `immutable_revision_id`, `record_digest` (only when actually calculated), `created_at_utc`, `actor_role`, `source_revision_refs[]`, `sensitivity`, `null_reason` for missing required data, and `synthetic=true`. Revision updates create new linked records; they never edit the antecedent. Hashes identify bytes, **not** authorship, authenticity, ownership or rights. Distinguish `SHA-1 Git object ID` from independently computed `SHA-256 digest`. The canonical field is `source_hash_if_verified` with `source_hash_method`; old `hash_if_verified` is a read-only alias, never evidence from unobserved bytes. Timestamp strings require explicit timezone; as-of and event/expiry time are separate.

**Conceptual types, not software schemas:**

| Logical type | Minimum required attributes | Mandatory failure boundary |
|---|---|---|
| `IntakeEnvelope` | run_id, task_mode, exact original title/topic, subject, object, mechanism, domain, source-as-of, output language, restrictions, synthetic scope | Missing identity, time, domain or permitted activity → HOLD_SCOPE |
| `ContextProfile` | primary N adapter, other applicable overlays, hazard class, geographic granularity, as-of timezone, domain reviewer requirement, `PolicySet` version | Unknown domain/contradicting policies → HOLD_SCOPE |
| `SourceRecord` | immutable original namespace+ID, source_revision, publisher/type, access_state FULL_READ/PARTIAL/INDEX_ONLY/BLOCKED/MISSING, retrieved_at, permission-to-read, permission-to-analyze, permission-to-reproduce, permission-to-redistribute, allowed purpose, scoped locator, source_hash_if_verified, source_hash_method, independent_family, correction_of | No actual bytes ⇒ null hash; unavailable ≠ verified; rights unknown ⇒ HOLD_RIGHTS on copying |
| `EvidenceDisposition` | source_id/revision, role ADMISSIBLE/CONTEXT/INACCESSIBLE/QUARANTINED/DISPUTED, independent family, reason list, immutable decision, reviewer | Blocked historic metadata cannot become affirmative claim evidence |
| `EvidenceLink` | claim_id, source_id+revision, locator, relation SUPPORTS/SUPPORTS_QUALIFIED/CONTRADICTS/CONTEXT/NON_SUPPORT/INACCESSIBLE, reviewer_id, reviewed_at, actor_role, rights/attribution note | Review time is not `retrieved_at`; missing review identity/time ⇒ HOLD_MISSING_IDENTITY |
| `AtomicClaim` | proposition, subject/object, claim kind, modal/epistemic qualifier, quote/number unit and denominator, baseline, issue/event/as-of/validity clocks, severity 0..3, source links, review_status, next_recheck | SUPPORT_WITH_QUALIFICATION is not unqualified confirmation; NOT_CHECKABLE is not 0 or PASS |
| `TopicLock` | exact received premise and claimant, canonical subject/object, event/mechanism, geography/date, modality/uncertainty tokens, source_revision_set and lock digest, editorial state | Changed referents or stronger certainty ⇒ HOLD_TITLE_PREMISE |
| `OptionSet/Outline` | source revision basis, niche eligibility, OptionCard promise, counterexample, declared hypothesis, quarantined K references, selected outline | Creator patterns/retention tips not causal laws |
| `DraftSpan/VisualSpan` | draft and span revision, links to invented claim IDs, claim strength, local time scope, synthetic visual flag and prominent disclosure, accessibility meaning | A caption does not prove recorded sound or authentic footage |
| `ReviewPacket/GateDecision` | author+distinct reviewer IDs, frozen draft digest, immutable initial forms, append-only adjudication, independent fact/rights/harm/accessibility checks, NOT_ASSESSABLE denominators, P0-P10 gate IDs, `native_reason_codes[]`, typed HOLD-set, reviewed_at | Unknown reason ⇒ HOLD_UNKNOWN_REASON; multiple HOLDS retained losslessly |
| `RunBundle/ReleaseDecision` | pinned input digests, source-dependency DAG, revocation/expiry, stage trace and reviewers, every open HOLD, research-only terminal status | `production_allowed=false`; no export, Claude-copy or RELEASED branch |

## 3. Stage ownership and dependency order (no A05/A06 cycle)

The preliminary identity binding is owned by A00 and is **not** the final lock. A06 is a two-part stage with a pre-option lock and a later outline approval, or its two substeps are represented separately in planning. That ordering eliminates a dependency on a result not yet created.

| Stage | Required inputs → deliverable | Immutability / stop behavior |
|---|---|---|
| **A00** Intake | IntakeEnvelope → provisional TopicIdentity + ContextProfile | Only this provisional identity may feed early planning |
| **A01** Registry | scoped fictional SourceRecord[] → pinned SourceLedger | Access ≠ copy permission; null actual hashes remain null |
| **A02** Eligibility | SourceLedger → EvidenceDisposition[] | Quarantine blocked roles/archival absence and preserve competing evidence |
| **A03** Arbitration | ContextProfile + disposition + hazard overlays → versioned **PolicySet** | Any restrictive overlay wins; no silent N05 fallback |
| **A04** Claim verification | TopicIdentity + SourceLedger + evidence links + PolicySet → ClaimLedger | Synthetic claims are not real nonfiction proof |
| **A06-pre** Identity lock | TopicIdentity + ClaimLedger + PolicySet → provisional immutable TopicLock | Exact original referents, claimant and modal markers pinned |
| **A05** Narrative options | ClaimLedger + **A06-pre TopicLock** + PolicySet → OptionSet | Reject unsupported promises, quarantined K claims and fixed metric laws |
| **A06-final** Outline | provisional TopicLock + OptionSet + ClaimLedger → final TopicLock + Outline | Reaffirm original semantic premise; no reverse circular edge |
| **A07** Draft assembly | Outline + ClaimLedger + **PolicySet** + final TopicLock → DraftSpan/VisualSpan[] | PolicySet provenance stays attached to output |
| **A08** Independent review | Draft + ClaimLedger + PolicySet + frozen authorship → ReviewPacket | Reviewer ≠ sole author; preserve dissent and severity-3 coverage |
| **A09** Evaluation | ReviewPacket + optional bounded synthetic metrics → EvaluationRecord | Style ≠ CTR ≠ retention ≠ causal trial |
| **A10** No-release checkpoint | pinned RunBundle + decisions → ResearchResult or HOLD | Both always NOT_PUBLISHABLE; no production transition |

A06 is one canonical module with two internal conceptual milestones, **not** a twelfth module. A06-pre is not a separately approved module or executable API. The stage graph requires A00→A01/A03→A02/A04→A06-pre→A05→A06-final→A07→A08→A09→A10, with independent source eligibility and recheck edges; each absent prerequisite yields HOLD_DEPENDENCY. Order notation does not authorize implementation.

## 4. Five domain adapters and union-of-guards policy

- **N01 / N-01 — USA weather:** type of watch/warning/advisory versus a mere projection; fictional issuer authority, issue/validity and as-of/local zone, county and map revision, observed/forecast/historical distinction, next recheck, urgency-safe wording. No stale bulletin presented as current; no geographic specificity stronger than evidence.
- **N02 / N-02 — Military/aviation/conflict:** precise aircraft/engine variant and production maturity (proposed, contracted, prototype, testing, low-rate production, fielded, reported-in-combat); attributed disputed battlefield outcomes, scenario dates, corroboration independence, civilian dignity and no actionable targeting instructions. Brochure capability ≠ verified operational result.
- **N03 / N-03 — German WWI/WWII human stories:** archival collection/edition/date/locator and testimony status, exact fictional quote versus dramatization, German translation reviewer and retained ambiguity, dignified treatment, no fabricated final words passed as authentic.
- **N04 / N-04 — Disaster reporting:** invented incident and source clock, estimate versus verified final figure, corrected casualty provenance, synthetic-video or scene authenticity and disclosure, privacy, multiple possible causal mechanisms, separate climate-attribution evidence threshold.
- **N05 / N-05 — General explainers/psychology:** bounded study population, confounders and research type, hypotheses and counterexamples, discipline/domain checks. No universal audience-retention, natural-speech WPM, clinical or neuroscience claim inferred from synthetic TTS or MOOC cases. Active hazard or sensitive advice invokes specialist overlays rather than general default.

Unknown authority, absent safety reviewer, expired time, protected expression, invented-media authenticity, contradictory overlays or inappropriate domain transfer yields a HOLD. All simultaneous HOLD reasons are retained; a passing primary adapter does not clear a failed secondary overlay.

## 5. Mandatory P0–P10 gates, typed reasons and waiver policy

| Gate | Decision invariant | Design-only expected blocker |
|---|---|---|
| **P0 Scope** | Complete task, context, consent/authority for scope and synthetic boundary | HOLD_SCOPE; unknown niche ⇒ GENERAL_REVIEW_REQUIRED/HOLD |
| **P1 Rights** | Separate access, analysis, derivative, private copy, transfer and public redistribution | HOLD_RIGHTS |
| **P2 Identity** | Original historic IDs, revisions and archived digests cannot be silently changed | HOLD_MISSING_IDENTITY, HOLD_DISPUTED_PROVENANCE, HOLD_ORIGINAL_MISSING |
| **P3 Source role** | R052 and F-190 quarantines, no K029–K031 scientific promotion | HOLD_SOURCE_ROLE |
| **P4 Fact** | Claim, number, quotation, severity and qualified support traceable | HOLD_UNVERIFIED_FACT / REJECT_CONTRADICTED |
| **P5 Time** | Issue/validity/retrieval/review/recheck independent, stale sources flagged | HOLD_STALE_FORECAST / HOLD_NEEDS_RECHECK |
| **P6 Topic** | Same subject, object and epistemic qualifier; no confirmation upgrade | HOLD_TITLE_PREMISE |
| **P7 Harm** | No fabricated eyewitness authenticities, privacy violations or unsafe disclosures | HOLD_HARM |
| **P8 Independent QA** | Distinct reviewer and preserved initial/dissent record, accessibility | HOLD_REVIEW / NOT_ASSESSABLE |
| **P9 Experiment/consent** | No simulated success presented as empirical RCT; scope and consent mandatory | HOLD_NOT_APPROVED |
| **P10 Publication/transfer** | No release, tool spend, Claude import or source-copy approval inferred | HOLD_NOT_APPROVED / HOLD_RIGHTS |

**All critical blockers are non-waivable**, including P0 scope/consent where applicable, P1 rights, P2 source identity, P3 quarantined evidence, P4 factual harm, P5 urgent safety/time, P6 false premise, P7 harm, P8 required independent review, P9 participants/experiment consent, and P10 authorization. A real future owner may select an *optional editorial* variant only; no role can re-label a critical HOLD as PASS. Preserve `native_reason_codes[]` losslessly; grouped aliases are advisory. Unknown reason or conflicting permission always remains HOLD.

## 6. Clock, correction, negative tests and provenance chain

- `SourceRecord.retrieved_at` describes receipt; `EvidenceLink.reviewed_at` describes an independent assessment. Missing either required access_state or required review time creates separate QA-002-style negative fixture with `verification=UNKNOWN` and `HOLD_MISSING_IDENTITY`. Never rewrite canonical QA-002 source wording to resolve an interface ambiguity.
- Change of SourceRecord revision/rights/issue-valid time invalidates affected EvidenceDisposition, EvidenceLink, AtomicClaim, TopicLock, OptionSet, Outline, DraftSpan, ReviewPacket and release signoffs **by exact revision dependency**, appending new versions; original audit data is not erased.
- `source_hash_if_verified` is only populated from actually inspected bytes with method and version. A surrogate, old excerpt, a URL, or a historical member-part hash disagreement cannot be silently treated as verified originals.
- Author and reviewer cannot be the same sole person. Frozen initial review + dissent + separate adjudication are mandatory. A 100/100 style rating never cancels severity-3 unsupported material or a NOT_ASSESSABLE evidentiary claim.
- Canonical QA-001…QA-036 remain DESIGN_ONLY and zero executed; T01–T13 human/science protocols remain NOT_EXECUTED. Suggested B2 v0.2 is a revision candidate requiring a separate static equivalence review and eventual, independently approved real execution.

## 7. Rights, authorization and non-approval record

Historical evidence metadata exceptions: K029–K031 quarantined, F-190 not positive support, R052 not independently read, B70–B72 exact archive missing, S08 restricted, F11 links locator-only. No data from source-rich EDU archives, copied script passages, videos, original QA fixtures or linked source bodies are included.

**Human checkpoints are separate:** AP-00 spec PENDING; A/B/C source strategy UNSELECTED; rights custodian external copying clearance ABSENT; AP-01 offline build NOT_AUTHORIZED; AP-02 **exact-file** Claude transfer NOT_AUTHORIZED (manifest `[]`); AP-03 studies NOT_AUTHORIZED; AP-04 production Skill HOLD; AP-05 independent code QA NOT_STARTED; G17/G18 HOLD; G19 NOT_STARTED. No "PASS" in this document grants any of them. New candidate requires independent technical/QA **and** provenance/rights review before owner consideration.

**Trace anchors (locator only):** prior B1 blob `b8d477e00a965862bb6e3ac3ece6b1e00cecd5bb`, conceptual v0.2 blob `d4b4a19f67772d4588b2ea7c3cd15b0b74e600fb`; Worker A technical clarification matrix `research/w8-ap00-contract-review`; Worker D interface amendment report `research/w8-core-traceability`; Worker E overlay assessment `research/w8-niche-safety`. These references supply historical research lineage, **not redistribution rights**.
