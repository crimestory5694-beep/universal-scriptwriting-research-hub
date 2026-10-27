# Wave 8 — Master Remote Readback Receipt

Verified remote branch HEAD before this receipt: `47568a9daaa2a0373f29b201196dcade8769a580`. This receipt commit advances the branch; final HEAD must be verified separately.

## File-by-file GitHub readback

| Verified new file | Git blob SHA-1 | UTF-8 bytes | SHA-256 if computed |
|---|---|---:|---|
| `00_MASTER_AUDIT_AND_VERDICTS.md` | `32272458e32978705bb799c314cd537b13c4ce36` | 9231 | not computed for this report |
| `01_50_WORKER_FILES_HASH_MANIFEST.csv` | `c879917efbe98078a4393d7d81cf62f03e3abf08` | 16360 | not computed for this report |
| `02_CROSS_WORKER_CONFLICTS_AND_PRIORITY.csv` | `40af8b09c4fb8a44c27ff09e599340b63f66f199` | 9923 | not computed for this report |
| `03_B1_V02_SOURCE_LIGHT_CANDIDATE.md` | `96f45cbb9570d00c2a22a499b0ec34a821362d0c` | 15188 | `5d15a03fd2a583a226cc0abc1175e6c00d8947164a48ad0eb427bf860c4982a5` |
| `04_B2_V02_QA36_CANDIDATE.csv` | `a643befb8e74536b4572d4f22812a2d411629bf2` | 13584 | `89e1d0d92b3c090a5598d82d2b8ebd35a8081524962fb6d390785833648eaebf` |
| `05_TECHNICAL_RIGHTS_TRACEABILITY_AND_QA.md` | `9fb7157c71b6c997dcaf943534c3202bb2afee97` | 7310 | not computed for this report |
| `06_OWNER_AP00_AND_SOURCE_APPROACH_UNSIGNED.md` | `b23da8b57838adb5a85e53610185a0d49c3e5b1f` | 5374 | not computed for this report |
| `07_AP01_AP02_RIGHTS_GATE_HANDOFF.md` | `93272e8b0a57bea1483b4280e2772affb6fecbad` | 6709 | not computed for this report |
| `09_NEXT_PHASE_CONTINUATION.md` | `4aa94ccef8b81c64602ee9385c2bef0a4915cda4` | 4570 | not computed for this report |
| `11_A_B_FILE_VERIFICATION_PART.csv` | `f0e00cc3943da1a8af2e412028fab3489875b457` | 3981 | not computed for this report |
| `12_C_D_FILE_VERIFICATION_PART.csv` | `9610e8cc4ac5f282ba0e631e2957d2fad2c536df` | 4017 | not computed for this report |
| `13_E_F_FILE_VERIFICATION_PART.csv` | `272b06092138267fc522aa69463741a5af3cccc8` | 3999 | not computed for this report |
| `14_G_H_FILE_VERIFICATION_PART.csv` | `eb5551ef421d9568e2ddf99be1e1a801e2022697` | 4768 | not computed for this report |

## Static verification
- **files_before_receipt:** 13
- **manifest_rows:** 50
- **revised_qa_ids:** 36
- **qa_exact_order:** true
- **additions_only:** true

The 50 worker SHA-256 checks are individually recorded in `01_50_WORKER_FILES_HASH_MANIFEST.csv`, which was independently read back above. B1/B2 SHA-256 values above were independently calculated. All 36 B2 rows are DESIGN_ONLY; no software or participant tests executed. Canonical QA original remains blob `88e89ee233c967c5b8a0b645b0d401f6c1d2ccea`.

File integrity is not legal rights clearance. AP-00 PENDING; AP-01/AP-02 NOT_AUTHORIZED; source-copy allowlist []; G17/G18 HOLD; G19 NOT_STARTED; no production Skill or release. PR #10–#13 observed draft/unmerged. New Draft PR #16 for owner research review only. **Do not merge as authorization.**
