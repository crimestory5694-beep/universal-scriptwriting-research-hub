# Worker C GitHub QA and Remote Read-Back Receipt

**DRAFT — NOT SIGNED — NOT AUTHORIZED**

QA checkpoint: 2026-10-27, just before publication of this receipt. Repository `crimestory5694-beep/universal-scriptwriting-research-hub`. Source `main@0776afd52001c2d9021b1749f7b936bc1dc4e37d`. Dedicated branch `research/ap-owner-readiness-final`. Pre-receipt branch commit `764f80a2836f2a4b602dfe9075780bf41d2df213` (09 continuation handoff upload). This receipt itself must be read back separately after publication; it is not self-certifying.

## A. Verified read-back of nine earlier Worker C output objects
Each of files 00–07 was independently retrieved by exact branch path and its UTF-8 bytes SHA-256 recalculated; local Git-object SHA-1 `SHA1("blob <bytecount>\\0" + bytes)` matched the GitHub returned blob ID for **8/8**. The 09 handoff was subsequently fetched and SHA-256 / bytes rechecked; GitHub reported its blob SHA. Values below are exact remote read-back metadata, NOT rights approval.

| Filename | Git blob SHA-1 from GitHub | Exact UTF-8 bytes | Independently calculated SHA-256 |
|---|---|---:|---|
| 00_FINAL_OWNER_READINESS_OVERVIEW.md | `d03776a920c8702758e1cab4c3105cb162a813a3` | 4498 | `6d8da54bbb62c7f5e8c70fcd488b5a80a929f433428c9efc21de74f4f9e7e2bd` |
| 01_AP00_PLANNING_DECISION_DRAFT.md | `6f9bca584238cd0504d12600c671cb8d2b9edcd1` | 4505 | `8930c5c08b096d808675686887e823fffcdf26df45520ed96eb73bea51116478` |
| 02_AP01_PROTOTYPE_DEVELOPMENT_AUTHORIZATION_DRAFT.md | `42e3d6934817dfa5d8da438d863efdd8446b8356` | 7643 | `1f1556baba08fd6dc9bdd6db9afac985bef4f4915e515b80fb8cef1c264d1232` |
| 03_AP02_EXACT_FILE_TRANSFER_AUTHORIZATION_DRAFT.md | `fb22e943e7bf27dcdfd68ce840c3cfd86aff84bd` | 14820 | `94e90e8d8cca3738ac2ee75a9bd9b86a84e2e6c991f67d4411d06963c3216d37` |
| 04_AP01_AP02_DEPENDENCY_AND_GATES_MATRIX.csv | `63525cde1299c99ab804aef84cb89ae83e8e4ed3` | 3922 | `3195756fe97ce662bfd21011fc14772532adf0e4518eeea4e0bfecd544e0abf7` |
| 05_PROPOSED_ISOLATED_WORKSPACE_REQUIREMENTS.md | `2f8b5670eedd0694489fcdbc2d3282a0a904f4ea` | 4302 | `843a74a6fa47b32cf189619756293710ca63f5a6f096c8b8cccb57b283b60c67` |
| 06_FUTURE_CLAUDE_HANDOFF_READINESS_CHECKLIST.md | `4ee5539248a9a5349e629a045bb7014b11aa0400` | 4586 | `f0737f4684480036eb3ade85f297783612878f38aea25380c6886820f1f44e9a` |
| 07_UNRESOLVED_OWNER_AND_RIGHTS_DECISIONS.md | `86121700a0a9e30ef86a7fe131551f7d708776e4` | 4721 | `ae45f7bfc1516aa0e35a4f2ccd22c5f5ab92ffd15de6560c4ac05da16d25786c` |
| 09_CONTINUATION_HANDOFF.md | `8d74bee1677a1905de47aa7b4c4e8ad4702617a5` | 4504 | `cfca89adef5aa09e73f52942912ca40fd88843cbfb9b454df02e487a5bcaceb3` |

The hash implementation independently passed published known-message `SHA1("abc")` and `SHA256("abc")` vectors. UTF-8 byte counts are explicitly measured, not JavaScript character counts. The local Git blob recomputation for 09 and the final 08 receipt are separately checkable in a follow-up final-branch read-back.

## B. Independently retrieved historical minimal source reference metadata
At original pinned source commit `ea07c53375e64ebbd6724a35a57d1b245526d1a8`, the five original F07/F08/F09/F10/F12 fetched blob IDs, SHA-256s and byte counts exactly matched Worker B and the PR #10 minimal candidate queue. Source sizes: **8275, 7718, 11287, 9503, 4754** = **41,537** bytes. Five identity matches; **zero rights/legal attestations**. Exact digests are reproduced as metadata in 03 AP-02 review form, not the source prose itself.

## C. Source preservation / scope verification
- Initial verified main `0776afd52001c2d9021b1749f7b936bc1dc4e37d`; rechecked after first 8 uploads and unchanged. Compare `main...research/ap-owner-readiness-final` after ninth file showed **9/9 ADDED** under only `coordination/2026-10-27-final-owner-review-workers/worker-c-authorizations/`; **zero modified/deleted files**, branch ahead 9, behind 0.
- Historical G01–G19 gate data, original Task1–3, original `coordination/CLAUDE_TRANSFER_GATE.md` and all source K/F/R/S/EDU ledgers necessarily unchanged because the diff is add-only and path-isolated. This is GitHub diff evidence, not a legal or scientific clearance.
- PR #10 fetched again after ninth write: **open, draft, unmerged**, head `afa8600bcb62b26e9b2101ba732e7f7259d41c6c`; no operations issued to it.
- No Worker A/B branch writes, no main merge, new implementation repo, CLAUDE transfer, source ZIP, raw transcript, private research export, `SKILL.md`, paid API call, research participant testing or executable QA work.
- Verified all seven MD forms/reports in 00–07 show `DRAFT — NOT SIGNED — NOT AUTHORIZED`; 09 likewise. CSV is a decision matrix, not a signed form. No checkboxes selected, signatures or actual destination populated.

## D. Final verification after 08 publication
A separate final GitHub read-back must: (1) fetch this exact 08 blob and verify SHA-1, SHA-256/bytes, (2) compare all 10 branch files to unchanged main with only added paths, (3) inspect final branch HEAD, (4) verify original G gate + transfer control unchanged and PR #10 still draft. The ultimate **branch HEAD and 08 self-hash** are to be reported in the user-facing final verification, not fabricated into a receipt before their creation.

**QA verdict for first nine files: PASS identity and append-only scope; legal/owner/signature status unchanged. Final tenth-file integrity requires explicit post-publication read-back.**
