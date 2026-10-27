# Worker B — Architecture and Rights Audit (F07–F10, F12)

**Date:** 2026-10-27 | **Disposition:** DOCUMENTATION-READY / RIGHTS-PENDING / CLAUDE TRANSFER NO-GO  
**Repository:** `crimestory5694-beep/universal-scriptwriting-research-hub`  
**Checked main:** `38d743640534cb390865824d36aeb2c890d628aa` (GitHub compare from previous checkpoint: **identical**, 0 commits)  
**Original source revision:** `ea07c53375e64ebbd6724a35a57d1b245526d1a8` (all five original Git blobs unchanged at current main)  
**Scope:** read-only analysis of five specified research documents, no executable prototype, no actual QA execution, no external import. Dedicated output branch `research/ap-rights-architecture`.

## Source-of-truth and method
1. Directly fetched F07/F08/F09/F10/F12 from original revision and latest main; each GitHub blob SHA agreed with Task 1 exact-path ledger `coordination/2026-10-27-preclaude-13file-rights-audit/01_INDIVIDUAL_13_FILE_ALLOWLIST_AUDIT.csv`.
2. Compared with Task 1 `00_RIGHTS_AND_ELIGIBILITY_AUDIT.md`, Task 2 `00_FROZEN_CANDIDATE_SPEC_NO_AUTH.md`, `01_MODULE_VERIFICATION_INDEX.md`, `02_QA36_FROZEN_TEST_CONTRACT.md`, `04_RIGHTS_SAFE_FILE_DISPOSITION.md`, Task 3 `03_QA36_ACCEPTANCE_AND_REPRODUCIBILITY.md`, `04_BLOCKED_MATERIAL_AND_RIGHTS_GATE.md`, `05_OWNER_APPROVAL_AND_READINESS_MATRIX.md`, and origin `coordination/CLAUDE_TRANSFER_GATE.md`. All were fetched at the checked main.
3. Computed raw UTF-8 file byte lengths and independent SHA-256 digests using an internal SHA-256 computation validated against the standard `abc` test vector. Blob SHA-1 is the GitHub returned original Git object ID; SHA-256 proves content digest, not ownership.
4. Scanned five bounded files for program code, substantial reproduced third-party text, URLs, referenced source IDs, rights/approval statements and cross-file contract consistency. **No executable source modules or embedded full third-party transcripts or external URLs were observed in the five inspected source texts.** This is not a claim of full copyright originality, legal licensing, or independent review of every linked historic source.

## File-by-file rights and provenance verdict
| File | Classification | Technical eligibility | Outstanding rights and dependency concerns |
|---|---|---|---|
| F07 Architecture/workflow | **CONDITIONAL_CANDIDATE** | 11 logical A00–A10 definitions, staged review and release HOLDs | Analyst-style proposed writing; origin/ownership not certified; depends on prior M01–M09, S/F/R/K/V/EDU lineage and G01–G19 approvals. State names need crosswalk. |
| F08 Interface contracts | **CONDITIONAL_CANDIDATE** | `USW-IFACE/0.1` prose-only typed fields and invariant proposals | Not licensed as deployable code/API; field-name and gate-vocabulary reconciliation needed. Source/example ownership review remains. |
| F09 Niche adapters | **CONDITIONAL_CANDIDATE** | Five safety-oriented N-01–N-05 descriptions | No actual weather, conflict, archival or disaster fact is validated by this design. Linked external source families/agency rules require fresh, scoped rights and accuracy checks; normalize adapter labels in *future crosswalk only*. |
| F10 Evidence and QA | **CONDITIONAL_CANDIDATE** | P0–P10 proposed safeguards, 0 actual gate executions | R079/R163 and F-190/R052 mentions describe limitations only, not cleared evidence; human scientific validation not performed. |
| F12 QA fixture matrix | **CONDITIONAL_CANDIDATE** | 36 unique QA-001..QA-036 rows; all `DESIGN_ONLY` | Test wording is original research design, not test implementation or fixture data; reviewer must clear precise text; 0 software results and 0 human/science results. |

**Meaning of CONDITIONAL_CANDIDATE:** bounded analyst-style source suitable for *research discussion*, **not** legal clearance, import authorization, code-building permission, or public replication license. Each F item is `rights_status=RIGHTS_NOT_CLEARED_NO_REPOSITORY_LICENSE`, `transfer_authorized=NO`. No item reached `SANITIZATION_REQUIRED` by a *confirmed* embedded copyrighted-copy finding during this bounded screen; if custodian identifies such content, downgrade to `SANITIZATION_REQUIRED` or `EXCLUDE` before any AP-02 review.

## Structural scope observations
- A00–A10: **11** distinct proposal components in F07. F09 enumerates **5** niche adapters `N-01`..`N-05`; Task 2 expects the canonical compact labels `N01`..`N05`. Same five topic domains; record notation ambiguity, do not edit original.
- F08 separates `SourceRecord.access_state` from `rights_access_status` and `rights_redistribution_status`; a full read never establishes public redistribution. F10 P1 RIGHTS blocks public text without permission.
- F07 holds/returns on missing material source; F08 `NOT_CHECKABLE` means uncertainty, not contradiction; F10 P0–P10 gates and F09 active-hazard safety overlay apply stronger controls. Original source revisions invalidate downstream attestation.
- Creative methods are context-sensitive options, not scientifically proven, and **no measured improvement in retention, average view duration, CTR or watch time** can be inferred. `K029`–`K031`, `F-190`, inaccessible `R052`, and contested research remain quarantined.
- Canonical `QA-001`..`QA-036`: **36 unique, contiguous, 36 `DESIGN_ONLY`, 0 executed**. T01–T13 original human/scientific protocols likewise **0 executed**. See `03_QA36_INTEGRITY_REPORT.md`.

## Open issues requiring explicit owner/custodian determination
See `02_INTERFACE_AND_SCOPE_COMPATIBILITY.md` for seven scope, naming and gate mapping notes. No existing interface, QA fixture or historical ID was rewritten. Further checking of authorship, external attribution/rights, permissions for *exact files* and destination workspace, and legal review of any derivatives is necessary.

## Approval boundary
`AP-00=PENDING`; `AP-01=NOT_AUTHORIZED`; `AP-02=NOT_AUTHORIZED`; `G17=HOLD`; `G18=HOLD`; `G19=NOT_STARTED`. Public repository status and hash consistency are not licenses. **Approved Claude transfer list: empty. Production SKILL.md: HOLD.** This report is not owner approval.

## Evidence pointers and limitations
Primary original path prefix: `worker-deliverables/skill-architecture/2026-10-27/` at `ea07c53375e64ebbd6724a35a57d1b245526d1a8` and `38d743640534cb390865824d36aeb2c890d628aa`. Task1 ledger `coordination/2026-10-27-preclaude-13file-rights-audit/01_INDIVIDUAL_13_FILE_ALLOWLIST_AUDIT.csv` at `38d743640534cb390865824d36aeb2c890d628aa`; Task2 frozen specification `coordination/2026-10-27-preclaude-task2-prototype-scope-freeze/00_FROZEN_CANDIDATE_SPEC_NO_AUTH.md` at `38d743640534cb390865824d36aeb2c890d628aa`; Task3 hold `coordination/2026-10-27-preclaude-task3-dormant-handoff/05_OWNER_APPROVAL_AND_READINESS_MATRIX.md` at `38d743640534cb390865824d36aeb2c890d628aa`. Human rights attestation, author provenance, historical original linked data and scientific/real-world efficacy are **not independently adjudicated**.
