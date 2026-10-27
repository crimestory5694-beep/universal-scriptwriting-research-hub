# Candidate-only exact GitHub source manifest — NOT an authorized export

Pinned original `main@ea07c53375e64ebbd6724a35a57d1b245526d1a8` (not a transfer destination). **13/13 source file Git blob IDs re-fetched and matched**. Roles below preserve Task 1 rights audit and Task 2 scope freeze; `rights_granted=false` for all.

| ID | Exact original path | Git blob SHA-1 | Disposition |
|---|---|---|---|
| F01 | `coordination/2026-10-27-master-research-acceptance-DRAFT/00_MASTER_RESEARCH_ACCEPTANCE_DECISION_DRAFT.md` | `350efa5871b8e7ae7f30df89a297ca7498793195` | CONDITIONAL_RIGHTS |
| F02 | `coordination/2026-10-27-master-research-acceptance-DRAFT/01_K001_K048_DRAFT_REQUIREMENTS_AND_DECISIONS.csv` | `a8d65227b52927814b9d23de42f0dc37ea7fe172` | CONDITIONAL_RIGHTS |
| F03 | `coordination/2026-10-27-master-research-acceptance-DRAFT/02_G01_G19_OWNER_DECISION_DRAFT.csv` | `4ed013fb6144f8b1cd3ce0123eec5693c0a217e2` | CONDITIONAL_RIGHTS |
| F04 | `coordination/2026-10-27-master-research-acceptance-DRAFT/03_S5_38_NICHE_WARNINGS_RECONCILED.csv` | `d0391bba1d9a62c487bdf3ccadacd4229251c6de` | CONDITIONAL_RIGHTS |
| F05 | `coordination/2026-10-27-master-research-acceptance-DRAFT/04_EVIDENCE_RIGHTS_CONFLICT_REGISTER.csv` | `af8c4ec42b8763d99c0d201908c1b94eff019acd` | CONDITIONAL_RIGHTS |
| F06 | `coordination/2026-10-27-master-research-acceptance-DRAFT/05_CLAUDE_PROTOTYPE_ELIGIBILITY_DRAFT.md` | `8d15255f9ceb14316f2145d36f6cb1f85d712263` | CONDITIONAL_RIGHTS |
| F07 | `worker-deliverables/skill-architecture/2026-10-27/01_ARCHITECTURE_AND_WORKFLOW.md` | `803f2d87969f1610d742110b8287ef3f31667434` | CONDITIONAL_RIGHTS |
| F08 | `worker-deliverables/skill-architecture/2026-10-27/02_INTERFACE_CONTRACTS.md` | `cfbd1340f747ff658e67b9e88bd956c472ad4165` | CONDITIONAL_RIGHTS |
| F09 | `worker-deliverables/skill-architecture/2026-10-27/03_NICHE_MODULES.md` | `04c208fda0872ada977d2406d299f54c318a0e32` | CONDITIONAL_RIGHTS |
| F10 | `worker-deliverables/skill-architecture/2026-10-27/04_EVIDENCE_GATES_AND_QA.md` | `33618d7e1905c4fa71730fe46fca17b9883f9cde` | CONDITIONAL_RIGHTS |
| F11 | `worker-deliverables/skill-architecture/2026-10-27/05_SOURCE_TRACEABILITY_AND_DECISIONS.md` | `826b4bd805fca459d45213a975b5cfcee24bc3ad` | LINK_SCOPE_HOLD_NO_IMPORT |
| F12 | `worker-deliverables/skill-architecture/2026-10-27/06_ACCEPTANCE_TEST_MATRIX.csv` | `88e89ee233c967c5b8a0b645b0d401f6c1d2ccea` | CONDITIONAL_RIGHTS |
| F13 | `coordination/CLAUDE_TRANSFER_GATE.md` | `7ccf873177f4ba4d0babd1350f0ac0a11dd035e7` | INTERNAL_CONTROL_DO_NOT_IMPORT |

### Export invariants

- F01–F10/F12 = **11 pending rights-custodian per-file decisions**, not a bundle, not approval.
- F11 = historical traceability index, **13 pinned linked GitHub targets existed** but are not additional allowlisted source files. No automatic following, copying or import; sanitize/reference-only with separate review.
- F13 = internal `CLAUDE_TRANSFER_GATE.md`, retain at source as an enforceable HOLD. No implementation payload.
- Preserve IDs, timestamp/commit pin, original legal status. A Git blob SHA1 proves file identity only; a future exporter should also compute SHA-256 from actual UTF-8 bytes after rights clearance and record exact byte size and target destination.
- Before transfer, create a **new** signed allowlist with file-by-file `ACCEPT_FOR_THIS_READ_ONLY_TRANSFER` decisions and approval IDs AP-01/AP-02. Without it, export set is empty.

**Transferable bytes in this dossier: NONE.** This file is authored manifest metadata, not a 13-file data copy.
