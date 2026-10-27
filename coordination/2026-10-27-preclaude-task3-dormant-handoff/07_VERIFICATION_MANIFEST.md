# Task3 Director Verification Manifest — no external transfer

Source baseline: `b587ac26944ccf629dc68f2db26909639679c636`, preserved. The following 7 task-specific files were GitHub-uploaded and remotely read back with matching blob IDs. No input research file was changed.

| Deliverable | Exact Git blob SHA-1 | Status |
|---|---|---|
| `00_HANDOFF_COVER_AND_VERDICT.md` | `221bbbcf1689e0f2a4a0a35823975c7002205932` | READ_BACK_PASS |
| `01_SOURCE_CANDIDATE_MANIFEST.md` | `d59c1749839f84e12dc79dbb61435cc1b3782d87` | READ_BACK_PASS |
| `02_DORMANT_CLAUDE_IMPLEMENTATION_WORK_ORDER.md` | `7c7794a25cf8161649af491e3a1dd9cd1d109315` | READ_BACK_PASS |
| `03_QA36_ACCEPTANCE_AND_REPRODUCIBILITY.md` | `554ef0baf9d1da8ee514aec4f4e5d0aad7110fdd` | READ_BACK_PASS |
| `04_BLOCKED_MATERIAL_AND_RIGHTS_GATE.md` | `e83f41db7b1ea9a82363f2732348be01fb9387a4` | READ_BACK_PASS |
| `05_OWNER_APPROVAL_AND_READINESS_MATRIX.md` | `542d195500e237da0d00a407d533dda6593e2ae0` | READ_BACK_PASS |
| `06_INDEPENDENT_READINESS_AUDIT.md` | `520ecfd9445ce6844421dd6c73c10878f2c7b01b` | READ_BACK_PASS |

Remote read-back verifies exact known Git blob identity. It does not prove legal authorship or rights. GitHub F01–F13 source content blobs were checked separately at pinned input commit; **13/13 match**, and the original 36 test fixture IDs were counted as **36/36 DESIGN_ONLY**. There is no Claude export artifact, no approved subset ZIP, no implementation runtime or test log.

**Readiness by category:** documentation YES; AP-01 NO; AP-02 NO; developer workspace NOT_SELECTED; rights custodian signoff NOT_RECEIVED; F11 links read-only reference graph, 0 export permissions; F13 internal control; code tests 0/36; human/science T01–T13 0/13; production G18 HOLD; future code QA G19 NOT_STARTED.

Exact file content may be recomputed at a later stage using the Git object SHA-1 formula `SHA1("blob " + utf8_byte_length + "\0" + raw_UTF8_file_bytes)` against the stored Git blob. For a future *approved* export, calculate independent raw-file SHA-256 and exact bytes after approved sanitization. Raw source files must not be copied simply to run this check; read-only GitHub verification suffices for document audit.
