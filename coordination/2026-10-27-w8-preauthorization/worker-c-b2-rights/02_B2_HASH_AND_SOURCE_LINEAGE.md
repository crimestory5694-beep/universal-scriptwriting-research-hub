# B2 exact hash, ancestry, source revision and chain of custody

Verified live on **2026-10-27** using read-only GitHub connector and independently recomputed SHA-256 on fetched UTF-8 strings. The blob IDs were returned by GitHub for each exact ref.

| Item | Git commit/ref | Git blob SHA-1 | SHA-256 (UTF-8) | Bytes | Rows |
|---|---|---|---|---:|---:|
| Canonical original F12 | `main@0776afd52001c2d9021b1749f7b936bc1dc4e37d` | `88e89ee233c967c5b8a0b645b0d401f6c1d2ccea` | `012d11ac37464f3aacc4b9414f184f160b392fdf051e808cfda21f19d8583aa4` | 4,754 | 36 |
| Candidate Option B2 | `research/ap00-option-b-owner-decision-ready@1e496c994835742bfdd63ffac0679ba8123e1734` | `8055702ab7fab28619c565dc21defd7ba22be79b` | `2df26fcbcfb35c3500550d54212c9e8d499777782a30f604d949009e993e48fe` | 6,966 | 36 |

Source files: [F12 canonical](https://github.com/crimestory5694-beep/universal-scriptwriting-research-hub/blob/0776afd52001c2d9021b1749f7b936bc1dc4e37d/worker-deliverables/skill-architecture/2026-10-27/06_ACCEPTANCE_TEST_MATRIX.csv); [B2 candidate](https://github.com/crimestory5694-beep/universal-scriptwriting-research-hub/blob/1e496c994835742bfdd63ffac0679ba8123e1734/coordination/2026-10-27-ap00-source-strategy-option-b/03_OPTION_B_QA36_SOURCE_LIGHT_COVERAGE.csv); [Master plan](https://github.com/crimestory5694-beep/universal-scriptwriting-research-hub/blob/research/w8-master-orchestration/coordination/2026-10-27-w8-preauthorization/00_MASTER_ORCHESTRATION_PLAN.md); [Draft PR #12](https://github.com/crimestory5694-beep/universal-scriptwriting-research-hub/pull/12).

Both Git blobs match the task's expected SHA-1 values. The B2 digest/bytes independently match the task's SHA-256 and byte expectation; original SHA-256 and 4,754-byte count independently match original 99_SHA256_MANIFEST.csv. SHA-256 implementation was validated against the known `abc` digest `ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad`; source UTF-8 correctly counts two extra non-ASCII bytes beyond 4,752 UTF-16 code units.

## Source revision differences

Original F12 CSV columns (6): `test_id,module,test_case,adversarial_or_positive_fixture,expected_proposed_gate_behavior,test_execution_status`.

New B2 CSV columns (7): `original_qa_id,review_area,new_synthetic_case_intent,new_expected_mock_handling,execution_status,current_source_copy_authorized,review_status`.

The new matrix is a separately written crosswalk, not a byte-for-byte revision of F12; it adds explicit no-copy and review-pending columns, removes source fixture specificity such as historic identifier sets, actual archive labels, numbered research references, metrics and release gate identifiers. It reformulates original negative/positive test purposes into brief invented scenarios. 36 IDs aligned by row and by value; zero missing/extra/duplicate IDs; all `DESIGN_ONLY`, and B2 all `NO` for copy authorization. Differences may affect technical scenario meaning (Worker F scope). They do not establish independent creative ownership, nor a lawful licence to reproduce the source or derivative elsewhere.

## Chain-of-title uncertainty

Original source branch and author-origin attestation appear in project notes, but a Git commit, visibility or project “PUBLIC_SAFE_ANALYST_ORIGINAL” label does not authenticate ultimate authorship/contractual assignments/embedded rights. The B2 author and complete drafting/provenance chain have not been attested by a rights custodian. No external reproduction licence, attribution inventory or permitted destination has been supplied. No original file was modified in this audit. `RIGHTS_UNRESOLVED` governs all 36 for external copying.

## Source revision stability

`main` live SHA matched the previous checkpoint without drift at verification time. Read-only PR #12 head includes the exact B2 commit. Before any future owner rights vote, repeat these hash checks and compare any later source revision; never roll forward silently.
