# S5 PUBLIC GitHub first-commit remote read-back verification
Date: 2026-10-27. Branch `research/s5-audit`. First content commit `fd3a9cb55811f083a2e2c2182e6e530516a23de3`.
All **6/6 original S5 output files** fetched back from the remote branch and every remote Git blob SHA-1 matched the original returned upload SHA; per-file SHA256 and exact UTF-8 byte counts recorded in accompanying manifest. Parsed CSV key-count checks: **48/48 K rows, 240/240 niche records, 19/19 G records**. Original S2-to-S4 fit/exception match independently completed from local user-held ZIP 240/240. Public S4 7/7 ZIP CRC and private S4 15/15 ZIP CRC PASS locally; no original/source-rich ZIP uploaded.
Main branch HEAD rechecked unchanged at `fb04d86f1512e71ba571c10315fd4d6a9fa26200`. This receipt is a post-readback audit record, not production acceptance. Full recorded SHA-256 file digests below:
- `00_PUBLIC_SAFE_S5_INDEPENDENT_AUDIT_REPORT.md` - 6898 UTF-8 bytes - SHA256 `20e5a50394efa07e8d9ef119723a0e1a7051c3c38e47e08f01f4a0ba10952055` - Git blob `3198c76bda1abe1ecef5218916ecfbf4fa604af3`
- `01_PUBLIC_SAFE_S5_K48_INDEPENDENT_QA.csv` - 21391 UTF-8 bytes - SHA256 `799acc5bfb7693c9b442b1b5ede7c97d55264385080ea21b95e381060d35cb1d` - Git blob `ef3a6463d208c3e5dd4bd8bca9f584b390ffb1ad`
- `02_PUBLIC_SAFE_S5_240_NICHE_COUNTERCASES.csv` - 146293 UTF-8 bytes - SHA256 `52f06c2b0d45d03c4c3599c20fc7c37be8621d6264e2055d8c085fec4c468b88` - Git blob `31323edaded1a61f1030bb50d6b53911b0e4527a`
- `03_PUBLIC_SAFE_S5_G19_GATE_DECISIONS.csv` - 3254 UTF-8 bytes - SHA256 `ff062db487b56359d22e2cb3140028afbd24dd81cc88da2675e068ec0dd97cc8` - Git blob `ce1df59caca89ea7d5ec99bf2b7349b3695c98d4`
- `05_PUBLIC_SAFE_S5_CONTINUATION_HANDOFF.md` - 927 UTF-8 bytes - SHA256 `503d19ec3834ad34dff6391b6685603100a3cbf0a40f1ada223582e601434177` - Git blob `970b042b08723435aaf2434c799e06796becd2b0`
No experiments were run and no permissioned original audiovisual or archive-rights materials were published.
