# Worker C GitHub QA and remote read-back receipt
Date: 2026-10-27 | Branch: `research/ap-f11-link-scope`
Initial source `main@38d743640534cb390865824d36aeb2c890d628aa`; source F11 SHA `826b4bd805fca459d45213a975b5cfcee24bc3ad`.
Read-back snapshot (first six file commit): `570407ef63aa566a5e44676cec927f99b2e736e1`.
Source-historical commit: `fb04d86f1512e71ba571c10315fd4d6a9fa26200`.

## Remote read-back checks, actually completed
- Branch ref read-back equaled `570407ef63aa566a5e44676cec927f99b2e736e1` at verification.
- 6/6 initial published files fetched independently from branch; every returned blob SHA equals `create_blob` SHA, every received UTF-8 ASCII content byte count equals created-byte count.
- CSV `01_THIRTEEN_LINK_VERIFICATION_LEDGER.csv` has 14 lines total (header + 13 historical targets), 13 source pinned URLs; the sanitized index contains 13 exact source-historical GitHub locators.
- Input historical git tree `fb04d86f1512e71ba571c10315fd4d6a9fa26200` returned `truncated=false`, 958 entries. All 13 exact objects found; independent `fetch_file` at each exact pinned path returned matching SHA-1. Sizes and exact original URLs preserved in ledger.
- Internal gates unchanged: F11 link HOLD, F13 internal control, AP-01/AP-02 absent, no developer payload, no Claude transfer, no production SKILL.md or scientific tests.

## Six-file read-back manifest
| Exact worker-folder filename | Git blob SHA-1 (verified) | Bytes |
|---|---|---:|
| `00_F11_INDEPENDENT_AUDIT.md` | `7588eb4275ad0b3bf7b221db303ef9a6891a9b5f` | 4720 |
| `01_THIRTEEN_LINK_VERIFICATION_LEDGER.csv` | `745dbc89a13d1c98533a6a4f5d45419b8b08a6f2` | 9295 |
| `02_SOURCE_RIGHTS_AND_PROVENANCE_RISKS.md` | `ee0b7f2e0a4a1946fe437666a4efa8dd51edc584` | 6271 |
| `03_SANITIZED_F11_REFERENCE_PROPOSAL.md` | `7a7b5b25b8ecc399cb796c31e6c06c86f3c3acd0` | 7525 |
| `04_EXCLUDED_AND_UNRESOLVED_TARGETS.md` | `00f0b2a0358c88c7b29f9985e0588cc2ae961b13` | 2785 |
| `06_CONTINUATION_HANDOFF.md` | `0fb502d998670c8e113ce19b5426e2167eddd8cb` | 1993 |

## Seventh-file and final-commit validation
This QA receipt is written as the seventh file *after* the above six-file remote read-back. For a non-circular proof of its own remote receipt blob SHA and the resulting final branch commit SHA, fetch this document and query the branch ref independently after its creation. Those values must not be asserted inside this pre-commit receipt as if known in advance. They are reported to the owner in the Worker C completion message.

## Limits of QA
- Hash equality proves exact bytes and immutable Git identity only; not copyright permission, actual scientific efficacy, archived external primary-source correctness or cross-workspace access consent.
- This is a publication-safe audit/QA receipt, not a legal signoff.
- 13 linked original content bodies excluded from implementation payload, with reference locators scoped to internal use.
- Do not merge to main or alter source files. Results remain NO-GO until human rights custodian and owner approve explicit scope.
