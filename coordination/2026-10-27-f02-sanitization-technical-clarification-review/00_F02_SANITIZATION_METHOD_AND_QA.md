# F02 Source-Light Derivative — Data Dictionary & Preservation QA

**New research-only derivative, NOT a modified canonical ledger, NOT approved for external transfer.**
Original F02 immutable path: `coordination/2026-10-27-master-research-acceptance-DRAFT/01_K001_K048_DRAFT_REQUIREMENTS_AND_DECISIONS.csv`, Git blob `a8d65227b52927814b9d23de42f0dc37ea7fe172`; verified unchanged at input main `0776afd52001c2d9021b1749f7b936bc1dc4e37d`.

## Provenance-limited transformation

New `01_F02_SOURCE_LIGHT_K48_STATUS_DERIVATIVE.csv` includes **one row per exact K001–K048 ID**, preserved in source order. Data fields copied only as research *status/identity metadata* from the 2026-10-27 F02 report, not from underlying S/R/V/EDU originals:

- `K_id` — exact historic ID (not renumbered).
- `original_S4_class_metadata` — source's existing classification label.
- `S5_independent_status_metadata` — source's existing status.
- `S3_source_depth_metadata` — inherited or limited-verification label.
- `S3_source_ids_only` — syntax-extracted R### / S3EXT### identifiers only, not article text, study details, hyperlinks or outcome claims.
- `master_research_draft_decision_metadata` — original research proposal status.
- `scientific_retention_effect_confirmed_original` — original source value (all NO).
- `owner_skill_approval_original` — original source value (all NO).
- `prototype_usage_now_original` — original source value (all NOT_AUTHORIZED).
- `derived_file_rights` — newly appended NOT_YET_ATTESTED.
- `derived_file_transfer_authorized` — newly appended NO.
- `source_f02_pinned_git_blob` — constant source linkage.

**Purposeful omissions:** historical_title, original_S4_proposed_behavior, master_proposed_scope_or_correction, free-form source_role_limit paragraphs. These have inherited source-specific expressions or qualitative rules which require separate rights/source review. Their omission reduces copying risk; it does not conclusively prove copyright clearance.

## Mechanical integrity checks

- 48 data rows, unique contiguous `K001`–`K048`, source row order preserved.
- `DRAFT_ACCEPT_BOUNDED_RESEARCH_DESCRIPTION` **36**, `DRAFT_AMENDMENT_AWAIT_OWNER` **9**, `QUARANTINE_NO_TRANSFER` **3** (`K029/K030/K031`).
- Original statuses preserved **48/48**: retention efficacy confirmed = NO, owner skill approval = NO, prototype use = NOT_AUTHORIZED.
- Original `S3_source_depth`: **22** inherited S2-only/not-reverified, **26** limited targeted primary check. These labels do NOT certify underlying primary sources.
- Qualitative or copied third-party excerpts **none deliberately imported**; no URL, code, original transcript, copyright licence, private EDU dataset, video/audio or scientific performance estimate transferred into derivative.
- Derivative is append-only: original F02 never edited or reclassified. Other original K/G/source data unchanged.

## Risk, rights and implementation restriction

Worker A's stricter `SANITIZATION_REQUIRED` disposition is adopted as a **screening decision**, not a signed legal determination. The derivative remains `CANDIDATE_PENDING_RIGHTS` because file authorship, even short labels' provenance, exact intended recipient and lawful copy/export terms still need an authorized custodian's per-file review.

Do **not** reinsert original historic titles or claim these 36 statuses are approved software requirements. K029–K031 are quarantined; 9 draft amendments remain owner-pending. This derivative by itself is **not** sufficient to implement a working scriptwriting engine—there are deliberately no behavior instructions.

Approval state: AP-00 PENDING, AP-01 NOT_AUTHORIZED, AP-02 NOT_AUTHORIZED, G17 HOLD, G18 HOLD, G19 NOT_STARTED. No Claude import or code execution.

**Disposition:** `SOURCE_LIGHT_DERIVATIVE_CREATED_AND_VERIFIED`; `RIGHTS_CLEARANCE_NOT_PERFORMED`; `TRANSFER_NO_GO`.
