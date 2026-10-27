# Worker C B2 — GitHub remote read-back and static QA receipt

**Date:** 2026-10-27. **Branch:** `research/w8-b2-provenance`. **First-batch commit:** `cacbb703caa8fc961498621b7faa782a81951ec3`. This receipt is appended by a second commit after independently fetching the initial five output files from the remote branch.

## Remote objects (read-back from GitHub, not local presumptions)

| Filename | Exact remote UTF-8 bytes | Git blob SHA-1 | Independently recomputed SHA-256 |
|---|---:|---|---|
| `00_B2_INDEPENDENT_RIGHTS_AUDIT.md` | 6,373 | `1417d61a9c7c971574eb106cf941aaa4b06c05b2` | `d480a070090659f94c28632b5799a145b5a6962576f4a3b65e250bd7851c842c` |
| `01_QA36_EXPRESSION_RISK_LEDGER.csv` | 20,808 | `3e83f3f2e323fb9fdeec66932483513732809736` | `b47d01e51882c3631797ef840e2d5375fb69d9967233d0abd1f264ec00d23b6e` |
| `02_B2_HASH_AND_SOURCE_LINEAGE.md` | 3,958 | `f6820b7c69935ef73aad97e9b90fce99b9f299e2` | `7d6cd01c800d4a430abaac929a71b82ba66f05ac7eed36bb3195507e8500843a` |
| `03_REWRITE_OR_EXCLUDE_PROPOSALS.md` | 5,219 | `a4354c953ce611f851713308756f4efc958a5e71` | `5211ce74bebcd0c36ed371d1bca4a6d520eb1f53757fc87acd9b874aaa82c58c` |
| `05_CONTINUATION_HANDOFF.md` | 2,171 | `281142c833ba27636ec65961a912f9b3be335fdd` | `7909d6683a15ca0efcd0904c5e00004f42072090fe5b3bafe65e3d495ca625ae` |

Source pins rechecked: original F12 `main@0776afd52001c2d9021b1749f7b936bc1dc4e37d`, Git blob `88e89ee233c967c5b8a0b645b0d401f6c1d2ccea`, SHA-256 `012d11ac37464f3aacc4b9414f184f160b392fdf051e808cfda21f19d8583aa4`, 4,754 UTF-8 bytes; new B2 `research/ap00-option-b-owner-decision-ready@1e496c994835742bfdd63ffac0679ba8123e1734`, Git blob `8055702ab7fab28619c565dc21defd7ba22be79b`, SHA-256 `2df26fcbcfb35c3500550d54212c9e8d499777782a30f604d949009e993e48fe`, 6,966 bytes.

## Reproducible QA record

- **Read-back:** first five files retrieved individually from `ref=research/w8-b2-provenance`; exact SHA-256 over returned UTF-8 bytes and byte counts calculated anew, Git blobs recorded.
- **Ledger:** 36/36 distinct contiguous `QA-001…QA-036`; 16 columns; no missing/duplicate rows; every row `DESIGN_ONLY`, `source_copy_authorized=NO`, `rights_evidence=NOT_PROVIDED_RIGHTS_UNRESOLVED`.
- **Content screen:** 22 `CONTENT_SCREEN_PASS`; 12 `CONTENT_SCREEN_CONDITIONAL`; 2 `CONTENT_SCREEN_SANITIZATION_REQUIRED`; 0 `EXCLUDE` observed. **All 36 external-transfer cases `RIGHTS_UNRESOLVED`.**
- **PR isolation:** Draft PR #12 still open and draft, head `1e496c994835742bfdd63ffac0679ba8123e1734` (unchanged); verified `main` `0776afd52001c2d9021b1749f7b936bc1dc4e37d` (unchanged); no original F12/B2 rewrite, no other worker folder edit, no merge.
- **Limits:** Static text and structural validation only. No runtime QA execution, no fixture execution, no scientific validation, no rights-owner/legal authorization and no Claude transfer. QA-003/006 proposed sanitation is documented but **not applied to B2**.

**Second receipt commit:** the branch head will advance when this very file is created. Its own Git blob and exact bytes must be separately read back after upload; this file does not pretend to know its own commit SHA in advance. The user-facing final report must quote the verified new HEAD. This receipt itself is research-only and unsigned.

**Gate invariant:** `AP-00=PENDING`, `AP-01/AP-02=NOT_AUTHORIZED`, `G17/G18=HOLD`, `36/36 DESIGN_ONLY`, `CLAUDE_TRANSFER_MANIFEST=[]`.
