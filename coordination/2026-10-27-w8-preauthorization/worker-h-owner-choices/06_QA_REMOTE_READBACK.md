# Worker H — GitHub Remote QA / Read-Back Receipt

**DRAFT — NOT SIGNED — NOT AUTHORIZED**

## Method and chain of custody
- **Source main observed:** `0776afd52001c2d9021b1749f7b936bc1dc4e37d`, matching historical checkpoint.
- **Worker branch:** `research/w8-owner-decision-package`; pre-receipt HEAD `39d4d810023e43f5276aa6ddc0b1fa41005c6d45` (7 newly added files). This receipt itself is created as the **eighth** file after checking these 7; its published SHA-1/UTF-8 count and branch's final commit must be checked independently after its remote read-back.
- **Compare at pre-receipt point:** `main@0776afd... → worker@39d4d810...` was `ahead_by=7`, `behind_by=0`, with **7 added-only files entirely within the exclusive Worker H folder; 0 modifications, 0 deletions**. Final comparison must show 8 added-only files.
- For each of the 7 initial documents, connector `fetch_file` at exact immutable worker commit `39d4d810...` returned complete UTF-8 content, matching immediate post-write read-back. Blob SHA-1 values below are returned by GitHub. SHA-256 values below were freshly computed from the **full remote-fetched UTF-8 content** by a pure JavaScript SHA-256 implementation, first validated against standard `""` and `"abc"` test vectors. Byte sizes counted via UTF-8 octets. Not file signature or legal rights evidence.
- Published files contain **original governance/decision wording only** and metadata/locator-level historical references; no production code, private files, transcripts or implemented tooling.

## Per-file exact remote identities — pre-receipt seven
| Filename | Remote Git blob SHA-1 | Independently computed remote-content SHA-256 | UTF-8 bytes | Read-back |
|---|---|---|---:|---|
| `00_OWNER_DECISION_OVERVIEW.md` | `b38d7c51b4f27311e1f6eff63df7479005c7f912` | `233dec3240a12b17f4d947450980e30ccf46e5c7fe4679f1c2cf58049f977a99` | 5621 | MATCH |
| `01_AP00_AND_WB_UNSIGNED_FORM.md` | `1d54a55d57d3350e1bfd920032c115870ff26739` | `2b3681404e4439a94a14958c4f68f04bb3bfbc8bb7efd2b65dcee83618b5cff4` | 3757 | MATCH |
| `02_SOURCE_STRATEGY_ABC_UNSIGNED.md` | `20d95dd3419489c3a63f049b6e02b114f6a00b32` | `5c16cd1e4c8af20e811324c4a52ee9cae76b8efc20e63d9cf72aa2a40e47f839` | 5409 | MATCH |
| `03_AP01_AP02_SEPARATE_FORMS.md` | `57492a48f6bf9cab0882adac2b034115714d25f4` | `15ee176ee5becb49c40a8b99fc7d47974022c842e7d0ce52af889a2b67ed720a` | 6654 | MATCH |
| `04_RIGHTS_CUSTODIAN_CHECKLIST.md` | `144bc4563dd2031ecf5296c87261604620ac1351` | `3320b702738ebe0a2a9631f9b8b2aa69d5fbc2cfc84488b0f14fdc75663a760f` | 6988 | MATCH |
| `05_OPEN_APPROVAL_DEPENDENCIES.csv` | `8f87b2826be064c04e4bb724f86e7632277eb36b` | `ee49f7d8c0ca6353df9034159477fb7b08db1652bfe1b461b738985f8dc7d07a` | 6168 | MATCH |
| `07_CONTINUATION_HANDOFF.md` | `496ced77d8e31bf8eb415dcee9feb7dcd3357c10` | `5daa5b4dd33c7ed1148050aee9f81cdf06ce17c89ce9d1916ece22d84eb6e6f9` | 5408 | MATCH |

**Total pre-receipt data files:** 7; **total UTF-8 bytes:** 40005. This receipt deliberately excludes its own SHA-256 to avoid a self-referential digest. The final human handoff should include its verified blob/digest/bytes and final branch HEAD.

## Content/governance QA assertions
1. `01`: AP-00 four unselected outcomes and separate WB-C01–C07 decision blanks; explicit mock-only safety, native HOLD non-waivers and QA/science limitations.
2. `02`: Options A/B/C compared on source/copyright risk, completeness and remaining tasks; B recommendation not a selection.
3. `03`: AP-01 dedicated new repo/branch, offline synthetic only, named developer/reviewer, zero default paid budget, network/API prohibitions, stop/retention/revocation/expiry; AP-02 separate per-file SHA-1/SHA-256/bytes/legal custodian plus owner decision and recipient/use/expiry.
4. `04`: rights-custodian item-by-item checklist; five original files and B1/B2 separately unresolved, C still unprepared.
5. `05`: CSV lists AP-00, all seven clarifications, rights, cross-worker findings, AP-01/02/03/04/05, science and QA dependencies; **no actual approval entries**.
6. `07`: continuation handoff forbids granting unearned permissions and does not assume Workers A–G finished.
7. Original QA36 **36 DESIGN_ONLY, 0 executed**, T01–T13 unexecuted. Source rights unresolved; `AP00=PENDING`, `AP01=NOT_AUTHORIZED`, `AP02=NOT_AUTHORIZED`, `AP03=NOT_AUTHORIZED`, `AP04=HOLD`, `AP05=NOT_STARTED`. External file allowlist `[]`; no source-byte transfer performed under Worker H.

## Explicit verification limits
- GitHub SHA-1 and SHA-256 of *this authored documentation* establish integrity **not** authorship, content rights, licence to transfer, accuracy of the underlying scientific claims, execution of QA36, or signatory authority.
- Other W8 workers' output branches were **not treated as completed** and their evidence cannot be presumed reconciled. PR #10/#11/#12 were observed **OPEN/DRAFT/UNMERGED** at input verification and not modified by Worker H.
- This file contains no electronic signature. A signed AP-00/AP-01/AP-02 decision is not present here or implied by a final GitHub QA check.
