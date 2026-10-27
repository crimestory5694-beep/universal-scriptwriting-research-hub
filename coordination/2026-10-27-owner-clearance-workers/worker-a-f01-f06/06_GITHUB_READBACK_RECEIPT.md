# Worker A — actual GitHub remote read-back receipt (documented, not a permission grant)

**Date:** 2026-10-27. **Repository:** `crimestory5694-beep/universal-scriptwriting-research-hub`. **Branch only:** `research/ap-rights-f01-f06`. **Source main frozen:** `38d743640534cb390865824d36aeb2c890d628aa`. **First publication commit:** `a4acf226692bae524ae7247939fdae441e8a9d71`. **Read-back method:** GitHub connector fetch_file of each exact path at worker branch after remote commit, fresh hash calculations over returned UTF-8 text; comparison with precommit create_blob SHA-1, and GitHub compare endpoint main...branch.

| Verified newly published file | Remote blob SHA-1 | Remote UTF-8 bytes | Independently recomputed remote SHA-256 | Read-back |
|---|---|---:|---|---|
| `00_AUDIT_REPORT.md` | `3c16654a4e6e48006f61f6e193d0282bbc50bc4f` | 6087 | `607275bfbd435468258e246b33053bd8cb543214ae81d4ed61aca85a091375c9` | PASS |
| `01_F01_F06_FILE_RIGHTS_LEDGER.csv` | `a9a915b4b39824d07bdf0893325763b3f41b7a96` | 3849 | `01dad6a902f451df382b8094fb08ba6581cc790a34d795acdc29ea960ff581ae` | PASS |
| `02_SOURCE_PROVENANCE_AND_RISKS.md` | `a3a72cbe3e9ba2ccd56c58d6e8ff32c1747d1393` | 5429 | `58f158f56e30a926be6fae1446e5a69d3dc81d6561e4bb733a883529fc71c013` | PASS |
| `03_RECOMMENDED_CANDIDATE_ALLOWLIST.md` | `8e71e15bb2937f1b923062dd20ab4bbb4b1e17d1` | 2945 | `33aadfc346dd830f39d021c36a00fac3549ff20a486943d0adaad2ddb32759ae` | PASS |
| `04_QA_AND_VERIFICATION_REPORT.md` | `085dc6350d1db0a8ea27f77fb1b2260857fd3c92` | 3284 | `979480f78abdfa9e269c57d84aa67bc1c7b359b76faf10f55e3cd5f7d2158670` | PASS |
| `05_CONTINUATION_HANDOFF.md` | `d101da9eb13c1a87590b6e562dae72a59102e41d` | 2506 | `563dda1e03257f3476d565863a6f722ed221e86f46c5d4794325b0d3b91eebc9` | PASS |

## First publication reconciliation

- Exactly **6** planned authored research files returned from the worker branch; 6/6 prepublication blob identities equal subsequent fetched remote Git blobs. All 6/6 remote payloads readable and UTF-8 byte counts / SHA-256 independently recomputed.
- Compared `main@38d743640534cb390865824d36aeb2c890d628aa` with Worker A first publication commit: **ahead 1 / behind 0**, six **added**, zero modified or deleted, all paths beneath `coordination/2026-10-27-owner-clearance-workers/worker-a-f01-f06/`. No other worker or source file modified.
- This seventh receipt is committed *after* the six-file verification. It is not self-attesting: final branch commit, seventh-file exact hash and complete seven-file diff must be checked **after receipt publication**, and may not be encoded inside this self-referential receipt without changing its own digest. External final handoff records that result.
- Baseline GitHub original F01–F06: 6/6 recorded Git blob SHA-1s and independent Git blob SHA-1s match; UTF-8 byte counts and SHA-256 are in the file ledger.
- No ZIP artifact produced; ZIP CRC checks **NOT_APPLICABLE**. No source originals copied; no Claude transfer or production implementation executed.

## Protection and rights status

**Effective Claude transfer allowlist is empty.** AP-01 and AP-02 remain unsigned/unobserved. Owner/rightscustodian signatures and file-level licences remain unverified; all six input files have unresolved reuse rights. Worker A F02 requires source-light sanitization before even candidate transfer consideration. The canonical origin gate `coordination/CLAUDE_TRANSFER_GATE.md` remains HOLD. This is a technical read-back and independent research audit, not legal approval.
