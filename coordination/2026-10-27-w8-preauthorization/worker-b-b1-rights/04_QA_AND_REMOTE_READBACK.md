# Worker B — Remote QA and GitHub read-back receipt

**Date:** 2026-10-27. Dedicated branch: `research/w8-b1-provenance`. **Read-only B1:** unchanged; no authorization to transfer.

## Fixed input verification
- GitHub `main`: `0776afd52001c2d9021b1749f7b936bc1dc4e37d` (matched prior checkpoint).
- B1 source pinned commit `1e496c994835742bfdd63ffac0679ba8123e1734`; Git blob `b8d477e00a965862bb6e3ac3ece6b1e00cecd5bb`.
- Independently computed B1 SHA-256 `1e499670d1c554f77c6dbac64d715d9d5196a45fc711eddc2d50be76fcc8cd46`; UTF-8 bytes `8425`, both match expected.
- Master orchestration plan read at `research/w8-master-orchestration`. Draft PR #12 reviewed read-only; initially OPEN/DRAFT/UNMERGED. B1 and master plan unchanged by this worker.
- F07–F10 Git blobs matched expected main files. Original and downstream source-dependent rights remain unresolved.
- Correct SHA-256 digest algorithm validated against independently pinned B1 digest *before* publishing this QA file. Results below are from remote retrieved UTF-8 content, not unverified pre-upload guesses.

## Exact remote read-back of preceding five files

| Uploaded worker file | UTF-8 bytes (remote) | SHA-256 (remote) | Git blob (remote) | Text/size read-back |
|---|---:|---|---|---|
| `00_B1_INDEPENDENT_RIGHTS_SCREEN.md` | 7643 | `3177f6de8a5f02f5cd238bf7ee1c803d6d0e27856f85d3ef5dc43638dcf2a4c2` | `154a5e0514005537c01cef38c94b89e573d4fe7b` | MATCH |
| `01_B1_SECTION_LEVEL_RISK_LEDGER.csv` | 8108 | `d4f4fb358da3c7f2803280d66acf14c591bb71b62e44e46bde05b4c431bb5fb0` | `fb81bfca20aabca03f8aa707c95712e72674ff98` | MATCH |
| `02_HASH_PROVENANCE_RECEIPT.md` | 1552 | `58501a5f8d6c958fe6184a8fe953ff70bf363fe311c154e99a434aea68431015` | `a3c379e05afe7e99bd925c94b5db5c476440bab0` | MATCH |
| `03_CUSTODIAN_EVIDENCE_REQUEST.md` | 3742 | `6a172cc1fb72e9511463f1314e26c989ce7e6bd297960d616d369137b1cef48b` | `0db0988cd1330f53730f4b4cdcbacc75e2f8eb89` | MATCH |
| `05_CONTINUATION_HANDOFF.md` | 2420 | `5936687e0b1fcd0a92e5149703edb56440e0ebca3d3ba623f559d43ff5a46419` | `1c6b1280913a49c048339758942d89e1c112c186` | MATCH |

**Method:** Each published file was retrieved from its actual Github branch path after upload. Retrieved UTF-8 byte count, SHA-256 and Git blob were recorded; uploaded/returned text matched exactly. The independent exact-file screen includes all 35 CSV ledger rows. No protected original content has been republished in this folder.

## Sixth-file QA closure and limitations

This receipt itself (`04_QA_AND_REMOTE_READBACK.md`) must be independently retrieved **after** publishing, so its final blob/SHA-256 and the six-file final branch commit are documented in the **Worker B final report**, not predicted inside the file. A future reader should fetch all six files by the reported final commit and compare this manifest.

**Outcomes:** INPUT_HASH_PASS; F07–F10_READ_ONLY_COMPARISON_DONE; FIVE_FILES_REMOTE_MATCH; NO_PRODUCTION_CODE; NO_CLAUDE_TRANSFER; NO_PR_MERGE.
**Rights result:** `CONTENT_SCREEN=CONDITIONAL`; `LEGAL_TRANSFER=RIGHTS_UNRESOLVED`; `AP-00=PENDING`; `AP-01/AP-02=NOT_AUTHORIZED`; `TRANSFER_ALLOWLIST=[]`; `G17/G18=HOLD`.
**Limitations:** mechanical overlap screen does not detect all adapted expression; GitHub author identity is not chain of title; no signed custodian or owner rights clearance available. No representation of legal permission is implied.
