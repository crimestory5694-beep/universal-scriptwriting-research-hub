# S5 - Corrected SHA256 and remote read-back verification receipt
Date: 2026-10-27 | Branch `research/s5-audit`
First content commit `fd3a9cb55811f083a2e2c2182e6e530516a23de3`. Interim receipt commit `27a6dc2f49772388f612315d98aea52a975ecca9`.

## Transparent checksum erratum
The interim SHA256 calculation used an incorrect SHA256 constant; its digest strings are INVALID, although Git blob SHA1 and row counts were matched correctly. This receipt and corrected manifest supersede those checksum values. The historical commit remains visible and was not rewritten.
Two SHA256 known-vector tests PASS:
- "abc": `ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad`
- "hello world": `b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9`

## Independently fetched source deliverables
- `00_PUBLIC_SAFE_S5_INDEPENDENT_AUDIT_REPORT.md`: 6898 UTF-8 bytes; Git SHA1 `3198c76bda1abe1ecef5218916ecfbf4fa604af3` MATCH; SHA256 `3555a2ab8458269f952ce12dda869eecc1e6ae9998975dfbe4093b9fce7c64f5` PASS
- `01_PUBLIC_SAFE_S5_K48_INDEPENDENT_QA.csv`: 21391 UTF-8 bytes; Git SHA1 `ef3a6463d208c3e5dd4bd8bca9f584b390ffb1ad` MATCH; SHA256 `581048799b4a5043ff54dccc2f2137424188a1c5785980d282737476065c3617` PASS
- `02_PUBLIC_SAFE_S5_240_NICHE_COUNTERCASES.csv`: 146293 UTF-8 bytes; Git SHA1 `31323edaded1a61f1030bb50d6b53911b0e4527a` MATCH; SHA256 `087bbb5570a88fb04e35e059e10fa8a486e50df5f9ff480b71693a2ef69cbc44` PASS
- `03_PUBLIC_SAFE_S5_G19_GATE_DECISIONS.csv`: 3254 UTF-8 bytes; Git SHA1 `ce1df59caca89ea7d5ec99bf2b7349b3695c98d4` MATCH; SHA256 `344db8df40b5ac032ed09162e6435c33a994046f19bfa7be1f4c85dfdb35d430` PASS
- `05_PUBLIC_SAFE_S5_CONTINUATION_HANDOFF.md`: 927 UTF-8 bytes; Git SHA1 `970b042b08723435aaf2434c799e06796becd2b0` MATCH; SHA256 `3d47a3f021793a4986c89e8850c0e08fa686de51fd3a0a062c57cec894723c7d` PASS
Original K48/Niche240/G19 CSV counts 48/240/19 PASS. Original 48 proposals production approval NO; no empirical tests executed.
S4 public source ZIP: 27,473 bytes, SHA256 `3f676976c26fa61999a2b8cfb714cd4c2c1ccaed983f0b7c484d0db8494e8e43` (7/7 CRC PASS).
S4 PRIVATE continuity ZIP: 31,591,609 bytes, SHA256 `ec03c8132d511c047701b4c29be563fe705ca5a3155941c77f3f948ec3920aab` (15/15 CRC PASS); source rich material NOT uploaded publicly.
The two amended receipt/manifest blobs require final remote read-back after this correction commit. No S5 ZIP generated.
NO-GO production; no main edits/merge, no SKILL.md, no owner approval, no external source efficacy reauthentication.
