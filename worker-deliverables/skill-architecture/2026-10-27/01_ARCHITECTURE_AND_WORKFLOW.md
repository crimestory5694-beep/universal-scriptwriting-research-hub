# Modular Universal Scriptwriting — Architecture and workflow contract

**Authority:** proposed design `ARCH-DESIGN-v0.1`; status `RESEARCH_ONLY`. This document does not enable production execution.

## 1. Component graph and owner of each decision
The 2026-10-19 nine-layer proposal M01–M09 remains the research baseline. The following adapter adds implementation-granular design boundaries **without changing that proposal's verdicts**.

| Logical component | Responsibility | Inputs → outputs | Release authority |
|---|---|---|---|
| A00 Intake / scope router | Require task, language, viewer intent, niche/subniche, format, fiction/nonfiction, region, date/time context and rights constraints; reject unstated defaults on high-stakes topics | `IntakeEnvelope` → `ContextProfile` | user scope; director authorizes rule catalogue |
| A01 Provenance/rights registry (M01) | Immutable references, source revisions and licenses; keep restricted bytes in rights-controlled vault, **never** embed third-party raw text in public exports | `SourceCandidate[]` → `SourceLedger` | qualified source reviewer |
| A02 Eligibility / conflict engine (M02) | Preserve S/F/R/K/V/EDU types and historic verdict; quarantine disallowed or inaccessible sources and derived claims; cross-check dependent citations | `SourceLedger, ContextProfile` → `EvidenceDisposition[]` | research director for promotion |
| A03 Context + policy resolver (M03–M04) | Choose explicit niche adapter, geographic/temporal rules, harm, fabrication, disclosure and change-control requirements | `ContextProfile` → `PolicySet` | editorial owner + subject expert |
| A04 Claim laboratory | Split an individual nonfiction assertion into dated, checkable atoms, identify quotations, entities, numerals, time and disputed causal inference; attach exact legal locator without redistributing restricted text | `TopicBrief, SourceLedger` → `ClaimLedger` | fact reviewer |
| A05 Creative option registry (M05) | Present **hypothesis-labelled**, niche-eligible outline options; mandatory safety constraints are distinct from storytelling alternatives | `TopicLock, ClaimLedger` → `OptionSet` | editorial choice; no outcome promise |
| A06 Topic/title and plan boundary | Lock user-provided topic/subject/object before changing title form; never transform unverified premise into fact; blueprint optional | `TopicBrief, OptionSet` → `TopicLock, Outline` | owner/title editor |
| A07 Draft assembly | Draft only with per-assertion traceability, suspense promises tracked, meaningful uncertainty preserved | `Outline, ClaimLedger, PolicySet` → `Draft` | future authorized implementer |
| A08 Independent editorial/claims review (M06–M07) | Severity-based claim QA, separate language/voice/visual/accessibility/disclosure reviews; freeze independent review before adjudication | `Draft, ClaimLedger` → `ReviewPacket` | independent reviewers |
| A09 Test & analytics registry (M08) | Isolate editorial quality from comprehension and retention measures; no analytics import or experiments without consent/preregistration | `ReviewPacket, StudyApproval` → `EvaluationRecord` | research director, owners, ethics/qualified reviewers |
| A10 Director promotion/transfer checkpoint (M09) | Change-control, rights audit, append-only artifacts, explicit signed GO/NO-GO; separate Claude Code and Codex handoff | `RunBundle` → `ReleaseDecision` | named director; independent implementation QA afterward |

**Cross-cutting properties:** versioned source and decision provenance, deterministic gates, audit log, rights separation, localization, subject expert independence, no hidden unverified efficacy scoring.

## 2. State machine with immutable artifacts

`RECEIVED` → `SCOPE_VALIDATED` → `SOURCES_TRIAGED` → `CLAIMS_REVIEWED` → `TOPIC_LOCKED` → `OPTION_SELECTED` → `OUTLINED` → `DRAFTED` → `INDEPENDENT_QA` → `RELEASE_REVIEW` → (future) `RELEASED`.

Any state may emit `HOLD_MISSING_SOURCE`, `HOLD_RIGHTS`, `HOLD_UNVERIFIED_FACT`, `HOLD_STALE_FORECAST`, `HOLD_HARM`, `HOLD_REVIEW`, `HOLD_NOT_APPROVED` or `REJECT_CONTRADICTED`; each holds `gate_id`, `affected_assertion_ids`, `required_action`, `reviewer`, `source_revision` and `resume_after` (not an automatic future time). A failed high-stakes gate **never** silently drops the claim and proceeds. A source refresh invalidates downstream claim/title/draft/review attestations that cite its replaced revision.

Every transition carries `from_state`, `to_state`, `actor_role`, `timestamp_utc`, `config_version`, `input_artifact_hashes`, `decision`, `reason`, `override_authority`. No `PASS` on unknown/missing approval. Partial drafts are allowed only as labelled research artifacts, never as publication-ready statements.

## 3. Dataflow and niche arbitration
A00 must set `content_domain`: `historical_nonfiction | engineering_defense | active_weather | disaster_reporting | general_explainer | fiction`. Cross-cutting overlays such as `current_event`, `sensitive_subject`, `translated`, `synthetic_visual`, `medical_claim`, `finance_claim` may all coexist. **More restrictive** active-hazard, factuality and safety policies override creative defaults. Unmatched subniche routes to `GENERAL_REVIEW_REQUIRED`, not permissive general fiction.

Example: a weather documentary with a synthetic flood visualization must satisfy BOTH NWS event time/location validity and synthetic-media representation disclosures; a military historical scene must satisfy both procurement-stage status and quotation/provenance rules. Multiple adapters accumulate gates by union; explicit conflicts resolve in favor of the stronger preservation, caution or HOLD.

## 4. Trust and evidence boundaries
- `user_supplied`, `retrieved_official`, `retrieved_secondary`, `creator_assertion`, `AI_generated`, `archival_excerpt` and `verified_fact` remain separate; untrusted source text is never instructions for the pipeline.
- Immutable evidence references: original ID and hash, access date/time, as-of issue date, exact locator, original language, version, permission status and independence family. When unavailable: `NOT_CHECKABLE` plus HOLD if material.
- Public GitHub export is generated only from a **preapproved allowlist** of analyst-created summaries/abstract identifiers, followed by rights/secret/privacy review. Hashes of private material are published only where already public and non-sensitive; never include private paths or identifying fragments.
- Disallowed transfers: caption timings → audio performance; views/CTR → retention; observational association → causality; creator anecdotes → independent verification; format examples → fixed universal formula; licensed access → republication rights.
- External provider and GitHub connectors are read-only by default in the future design; write side effects require separate explicit authorization and targeted branch/path.

## 5. Topic invariance and correction policy
A supplied competitor title or link can be used as *a research lead*, not authoritative evidence. Store `subject`, `object`, `central_question`, `scope_date`, `claim_status` separately. Any curiosity-title variant must retain referents and epistemic status. When a claim is alleged, disputed or forecast, equivalent qualifiers remain. Reject a requested style conversion that turns “alleged” into “confirmed.” Research must verify date-bounded updates before lock. The owner approves changes to the topic itself.

## 6. Failure recovery, version boundaries, QA independence
Archive the previous artifact, add a superseding revision (never overwrite original identifiers). Retried jobs are idempotent by `run_id + stage + source_revision_set`; downstream outputs revalidate against exact referenced hashes and gate configuration. Independent QA reviewer cannot be the draft's sole author. Adjudicator records disagreement; never rewrites reviewers' initial ratings. Language QA cannot supersede factual/source decisions. Any emergency alert refresh can rewind to `SOURCES_TRIAGED`.

The future implementation is separate and gated: until a signed work order satisfies G01–G19 as applicable and implementation authorization G18, this design **does not** instruct Claude Code to produce a live skill.
