# AP-00 Worker A — Source Manifest, Static QA & Pre-Commit Receipt
**Status: PROPOSED — OWNER REVIEW PENDING.** Main baseline `0776afd52001c2d9021b1749f7b936bc1dc4e37d`; PR #10 head `afa8600bcb62b26e9b2101ba732e7f7259d41c6c`; new isolated worker branch `research/ap00-final-spec-review`.

## Source Git object references (read-only)
- Task1 audit: `coordination/2026-10-27-preclaude-13file-rights-audit/00_RIGHTS_AND_ELIGIBILITY_AUDIT.md` — Git blob `9a014574284ca7e4fb64bd09b072fabc71cdca16`
- Task2 v0.1: `coordination/2026-10-27-preclaude-task2-prototype-scope-freeze/00_FROZEN_CANDIDATE_SPEC_NO_AUTH.md` — Git blob `591dabfd1ee026bbe31fd086c152f4824f32a577`
- Task2 QA: `coordination/2026-10-27-preclaude-task2-prototype-scope-freeze/02_QA36_FROZEN_TEST_CONTRACT.md` — Git blob `bc52135a003b85035b9f826f43d8a4f1024ed966`
- Task3 handoff: `coordination/2026-10-27-preclaude-task3-dormant-handoff/00_HANDOFF_COVER_AND_VERDICT.md` — Git blob `221bbbcf1689e0f2a4a0a35823975c7002205932`
- Master audit: `coordination/2026-10-27-five-worker-master-audit/00_MASTER_AUDIT_MERGE_REPORT.md` — Git blob `ceb2b0190f540da7e199c34b55d30a65902eb7a0`
- Master K register F02: `coordination/2026-10-27-master-research-acceptance-DRAFT/01_K001_K048_DRAFT_REQUIREMENTS_AND_DECISIONS.csv` — Git blob `a8d65227b52927814b9d23de42f0dc37ea7fe172`
- G01–G19: `coordination/2026-10-27-master-research-acceptance-DRAFT/02_G01_G19_OWNER_DECISION_DRAFT.csv` — Git blob `4ed013fb6144f8b1cd3ce0123eec5693c0a217e2`
- Master clearance: `coordination/2026-10-27-owner-clearance-master-integration/02_OWNER_DECISION_ORDER.md` — Git blob `684fa5ca12c6522c3c750035bd28677b2b75d7cb`
- Original F07: `worker-deliverables/skill-architecture/2026-10-27/01_ARCHITECTURE_AND_WORKFLOW.md` — Git blob `803f2d87969f1610d742110b8287ef3f31667434`
- Original F08: `worker-deliverables/skill-architecture/2026-10-27/02_INTERFACE_CONTRACTS.md` — Git blob `cfbd1340f747ff658e67b9e88bd956c472ad4165`
- Original F09: `worker-deliverables/skill-architecture/2026-10-27/03_NICHE_MODULES.md` — Git blob `04c208fda0872ada977d2406d299f54c318a0e32`
- Original F10: `worker-deliverables/skill-architecture/2026-10-27/04_EVIDENCE_GATES_AND_QA.md` — Git blob `33618d7e1905c4fa71730fe46fca17b9883f9cde`
- Original F12: `worker-deliverables/skill-architecture/2026-10-27/06_ACCEPTANCE_TEST_MATRIX.csv` — Git blob `88e89ee233c967c5b8a0b645b0d401f6c1d2ccea`
- WB independent crosswalk: `coordination/2026-10-27-owner-clearance-workers/worker-b-architecture/02_INTERFACE_AND_SCOPE_COMPATIBILITY.md` — Git blob `9732e17be66e1bfce7ab76e0ec23ed2be2a4d739`
- PR10 derivative: `coordination/2026-10-27-f02-sanitization-technical-clarification-review/01_F02_SOURCE_LIGHT_K48_STATUS_DERIVATIVE.csv` — Git blob `e64d182ac2ffee416313e5b5905e9f245bfe38a0` (PR #10 head)
- PR10 seven-point review: `coordination/2026-10-27-f02-sanitization-technical-clarification-review/02_WORKER_B_7_TECHNICAL_CLARIFICATIONS_REVIEW.md` — Git blob `d545f838aed8e926c44e2b15f36771c829b55850` (PR #10 head)

## Independently recomputed source-file checks
- F02 original (source) Git blob `a8d65227b52927814b9d23de42f0dc37ea7fe172`; derivative Git blob `e64d182ac2ffee416313e5b5905e9f245bfe38a0`; original/derivative UTF-8 lengths 21597 / 10990.
- CSV parsed with quoted-field-aware parser. K rows 48/48 exact sequence, 8 retained source-status fields 384/384 equal; extracted multiple source-ID sets 48/48 equal after the derivative's semicolon delimiter; K status 36 bounded/9 draft amendments/3 quarantine K029–K031.
- Derivative rights not attested and transfer = NO across all rows. Original efficacy and owner authorization = NO; original prototype use = NOT_AUTHORIZED across all rows. No full source-title/behavior scope columns reintroduced.
- Original F12 QA fixture blob `88e89ee233c967c5b8a0b645b0d401f6c1d2ccea` contains QA-001–036, 36/36 `DESIGN_ONLY`; tests actually run 0. T01–T13 are distinct and NOT_EXECUTED.
- The seven WB proposed issues are source-anchored; no approvals recorded, no executable schemas. The static assertions succeeded with 0 discrepancies.
- Source Git blob SHA is a repository identity, not rights permission. Copyright/embedded text/custodian and exact transfer destination remain unverified.

## Eight other newly authored candidate file blobs, calculated by GitHub object creation
| New file in dedicated folder | Git blob SHA-1 | UTF-8 bytes |
|---|---|---:|
| `00_AP00_SPECIFICATION_REVIEW.md` | `7c47afb078c927a3e90b38590306b43e53ab3fd6` | 6211 |
| `01_F02_DERIVATIVE_INTEGRITY_REPORT.md` | `b28c915b08a1b031d1253b431affdadc3efab164` | 3630 |
| `02_WB_C01_C07_DECISION_MATRIX.csv` | `cf6792824a31ca101a318d5c544cf2ee2e19ad79` | 5790 |
| `03_PROPOSED_PROTOTYPE_SPEC_V02.md` | `d4b4a19f67772d4588b2ea7c3cd15b0b74e600fb` | 11902 |
| `04_V01_V02_CHANGELOG_AND_COMPATIBILITY.md` | `d415169524a1220c68050e7a81ca89779935813e` | 4430 |
| `05_QA36_SPECIFICATION_COMPATIBILITY.md` | `b5a3cad7fca55693b90334b8b7b315e5ab8c58ef` | 4740 |
| `06_OWNER_AP00_DECISION_DRAFT.md` | `9e85a1bc806670c20e4872bddd0dd315978272d0` | 3136 |
| `08_CONTINUATION_HANDOFF.md` | `15b16f36fe817f51ed69a9c0339274e42445c183` | 2827 |

This ninth document is itself append-only and will be independently read back after remote branch commit. This pre-commit receipt is **not** a claim that remote read-back, executable QA, source rights or approvals already occurred. Subsequent branch read-back checks should compare all nine SHA1 object identities, bytes and branch/main diff; print final branch commit externally to avoid a circular self-reference.

**STATIC_DOCUMENT_INTEGRITY_PASS; OWNER_REVIEW_PENDING; RIGHTS_REVIEW_PENDING; CLAUDE_TRANSFER_NO_GO; PROTOTYPE_BUILD_NO_GO.**
