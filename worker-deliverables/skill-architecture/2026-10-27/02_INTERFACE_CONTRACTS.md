# Versioned logical interfaces and validation invariants

**Status:** interface specification only (`USW-IFACE/0.1`), not a JSON Schema file, executable API, connector integration, or production SKILL.md. A future implementer may translate these field-level contracts into typed schema only **after approval**. All records require `schema_version`, `record_id`, `created_at_utc`, `actor_role`, `provenance_ref` (or explicit null reason), `sensitivity`.

## Input and source interfaces

### `IntakeEnvelope` (required)
`run_id` (UUID-like unique ID); `task_mode` (`verify_topic | convert_title | outline | draft | audit | research_design`); `niche`, `subniche`, `format`, `narration_language`, `audience_region`, `audience_expertise`, `publication_window`; `nonfiction_status` (`fiction | nonfiction | mixed`); `topic_exact`; `user_constraints`; `source_leads[]` (`url | original_file_ref | source_id`); `research_authorization`; `release_authorization` (default `NO`); `paid_tool_spend_authorized` (default `NO`). Empty essential fields → `HOLD_SCOPE`, never inferred as approved.

### `ContextProfile` (required)
`primary_adapter`, `overlays[]`, `geographic_scope`, `temporal_scope`, `risk_class` (`ordinary | consequential | immediate_hazard`), `applicable_policy_ids[]`, `translator_required`, `independent_subject_reviewer_required`, `as_of_utc`. Context versions immutable once reviewed.

### `SourceRecord` (one per *version*, even if same URL)
`source_id`, `historical_id_namespace` (`S | F | R | V | K | EDU | NEW_EXT`), `source_kind` (`government_primary | scholarly_original | archival_primary | official_policy | journalistic_secondary | creator_caption | untrusted_upload | other`), `publisher`, `title`, `original_url_or_restricted_ref`, `access_state` (`FULL_READ | PARTIAL | INDEX_ONLY | BLOCKED | MISSING`), `source_depth`, `published_at`, `issued_at`, `valid_until`, `retrieved_at`, `source_hash_method`, `source_hash_if_verified`, `independence_family`, `rights_access_status`, `rights_redistribution_status`, `allowed_usage`, `locator_policy`, `correction_of`. `hash_if_verified` is null when no actual bytes have been hashed. Historical `F` closure status stored separately from source verification. `FULL_READ` alone is not rights clearance.

### `EvidenceLink`
`claim_id`, `source_id`, `source_version`, `locator`, `relationship` (`supports | supports_with_qualification | contradicts | contextualizes | non_support | inaccessible`), `source_role`, `reviewer_id`, `reviewed_at`, `independent_source_group`, `confidence_rationale`, `rights_note`. An external quote is represented as a link and **not redistributed** inside public exports. At most one authoritative current version per claim's operational as-of interval, while older versions remain linked in audit history.

## Assertions and user-facing design interfaces

### `AtomicClaim`
`claim_id`, `assertion_paraphrase`, `entity_ids[]`, `topic_subject`, `topic_object`, `claim_kind` (`fact | quote | quantity | attribution | time | geography | forecast | model_projection | interpretation | causal | synthetic_reconstruction`), `epistemic_qualifier`, `quantity{value,unit,denominator,baseline}` or explicit `not_applicable`, `time{issued,valid_from,valid_until,timezone}`, `source_links[]`, `claim_verdict` (`SUPPORTED | SUPPORTED_WITH_QUALIFICATION | UNSUPPORTED | CONTRADICTED | NOT_CHECKABLE`), `severity` (0/1/2/3), `reviewer`, `adjudication`, `next_recheck_reason`. **`NOT_CHECKABLE` is a distinct state, never interpreted as “false” or “true.”** Quote approval requires a traceable original; otherwise label paraphrase or remove.

### `TopicLock`
`original_user_title`, `canonical_subject`, `canonical_object`, `central_mechanism_question`, `scope`, `qualification_tokens`, `approved_exact_title`, `editorial_owner_approval`, `source_revision_set`, `lock_hash`. Converter passes when canonical subject/object are semantically invariant and evidence status does not strengthen; superficial title formatting alone cannot change a disputed event into a confirmed event.

### `OptionCard` / `Outline`
`option_id`, `niche_applicability`, `K_ids[]`, `evidence_grade`, `method_status` (`source_attributed_hypothesis | context_sensitive | verified_process_requirement | forbidden | hold`), `counterexamples[]`, `promises[]`, `critical_claim_refs[]`, `sections[]`, `open_questions[]`, `editorial_selection`. No mandatory 3-act, hook seconds, scenes, WPM, emotional pivot quota, or purported expected retention lift.

### `DraftSpan` / `VisualSpan`
`span_id`, `section_id`, `text`, `claim_ids[]`, `source_revision_set`, `assertion_strength`, `uncertainty_lineage`; visual side adds `semantic_purpose`, `media_license`, `synthetic_status`, `disclosure_needed`, `alt_meaning`. Textual captions cannot set `audio_verified=true`. Actual voice performance requires qualified native-audio check.

## Control, review and handoff interfaces

### `GateDecision`
`gate_id`, `scope`, `decision` (`PASS_FOR_DESIGN | HOLD | FAIL | WAIVED_BY_NAMED_OWNER`), `basis_evidence_ids[]`, `revision_hashes[]`, `reviewer_role`, `reviewed_at`, `remaining_risks[]`, `explicit_approval_id`. A design PASS never sets `production_authorized`; only a separate signed decision can authorize an eligible future process. Critical non-waivable safety constraints remain blocking despite owner preference.

### `ReviewPacket`
`draft_hash`, `claim_coverage{critical_total,reviewed_total,unsupported_total,not_checkable_total}`, `rights_coverage`, `style_dimensions[]` (`0..4` ordinal where assessable), `independent_reviews[]`, `adjudication`, `accessibility_check`, `domain_check`, `disclosures`, `exception_ledger`, `overall_disposition`. Mark `NOT_ASSESSABLE` on missing sources, not zero. Style may not override fact/rights HARD HOLD.

### `RunBundle` and `ReleaseDecision`
`run_id`, `all_artifact_hashes`, `source_versions`, `applicable_gate_decisions`, `rights_export_class`, `approval_scope`, `open_holds`, `implemented_by` (future), `independently_checked_by` (future), `production_allowed` (currently hard **false**), `decision_memo`. Distinguish `RESEARCH_DESIGN_READY` from `PRODUCTION_APPROVED`.

## Invariants (MUST in a future implementation)
1. IDs historical S/F/R/V/K/EDU remain immutable; reconciliation uses a new relation object, not renumbering.
2. Each factual sentence or paragraph span maps to one or more AtomicClaim IDs; each consequential claim carries contemporary original locator and status.
3. A claim can be conditionally verified or qualified but cannot cite a `FAIL`/`UNVERIFIED` audit finding as positive evidence; F-190 and original-blocked R052 remain quarantined.
4. A source rights field MUST distinguish lawful access from public redistribution. Public export fails if `rights_redistribution_status` is missing for any non-original content.
5. Time validity is evaluated at the **target publication and audience local time**, with UTC audit conversion and explicit as-issued archive reference.
6. Any changed `SourceRecord` that supports a draft invalidates downstream signoffs. A held claim cannot silently disappear from QA denominator.
7. Multiple reviewers' initial verdicts are immutable; adjudication is append-only with names/roles and locators.
8. Analytics are separated by observed metric unit (impressions, CTR, starts, avg view duration, retention); none infers causal script improvement without approved design.
9. An `OptionCard` supporting storytelling choices cannot be relabeled a scientifically established formula without separate approved validation.
10. The interface contract is **not evidence that any connector/API, runtime, media verification, paid source, or experiment has been operationally tested**.
