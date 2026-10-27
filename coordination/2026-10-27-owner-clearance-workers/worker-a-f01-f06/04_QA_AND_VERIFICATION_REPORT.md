# Worker A — QA and verification report

**Source baseline:** `main@38d743640534cb390865824d36aeb2c890d628aa`, exact requested checkpoint; no observed HEAD drift when this audit started. **Audit scope:** F01–F06 only. **Git identity verification:** 6/6 remote content blobs exactly match Task1 ledger and locally calculated Git blob SHA-1. **Bytes:** 6/6 independent UTF-8 sizes equal GitHub content API sizes. **SHA-256:** 6/6 independently calculated from fetched text bytes, recorded in `01_F01_F06_FILE_RIGHTS_LEDGER.csv`. Hash algorithms were self-tested with `abc`: SHA256 `ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad`; Git blob SHA1 for `abc` `f2ba8f84ab5c1bce84a7b441cb1959cfc7093b7f`.

## Source integrity QA

| Test | Actual observation | Result |
|---|---|---|
| Main drift from `38d743640534cb390865824d36aeb2c890d628aa` | same exact SHA at initial verification | PASS |
| F01–F06 paths, Task1 recorded blobs | 6 exist; 6 match SHA1 independently | PASS |
| F02 K count/status | 48 rows: 36 bounded, 9 proposed, 3 quarantined K029–31 | PASS |
| F02 approval/scientific claims | 48/48 NO scientific retention confirmed, NO owner skill approval, NOT_AUTHORIZED prototype | PASS |
| F03 G count and permission | 19/19 pending; 19/19 waivers NOT_GRANTED | PASS |
| F04 niche warning restrictions | 38/38 `CONDITION_NARROWING_OR_HOLD`, fixture YES, approval NO | PASS |
| F05 unresolved conflict index | MX01…MX11, all retained as active indexed issues | PASS — indexing only |
| F06 owner and Claude status | OD01–OD07 remain questions, G17 HOLD, G18 NO-GO | PASS |
| Physical primary S/F/R/V/EDU originals re-licensed | no such audit performed | UNVERIFIED |
| Author/title/source-copyright rights attested | no owner/custodian authorisation available | UNRESOLVED |
| Root LICENSE / NOTICE | neither found; repository metadata licence null | OBSERVED |
| Supported evidence of actual increased retention | none in these audit files | NOT ESTABLISHED |
| QA-001–036 execution and T01–T13 scientific tests | planned/design-only; zero executed | NOT_RUN |

## Bounded content screen and provenance

Explicit HTTP(S) links in six payloads: zero. PEM private-key-header or conventional email-address pattern matches in six: zero. These checks do not constitute a complete privacy/secret or quotation scan. GitHub path-specific creation history attributes all six to commit `ab198fc2d5dfdc9024e2fb226b16fc8dd58d0c4c`, labelled author `crimestory5694-beep`, but creator/rights-control certification is absent.

## Outstanding QA — not failure disguised as pass

- Legal authorship and third-party licensing; root public visibility is not permission.
- Source depth and original linked proof for F-190 / R163, blocked R052 and S08 legal conditions (referenced from workers, not opened).
- B70–B72 exact missing original, B25/B58/B06 and disputed 91 observations, plus S39/S40 versions.
- Distinguish five conditional candidates from F02 sanitization-first; **none is external-transfer eligible now**.
- Post-publication read-back of worker files and path-only diff is recorded in `06_GITHUB_READBACK_RECEIPT.md` upon separate verification.

**Disposition:** PASS technical/row integrity; RIGHTS_UNRESOLVED; CLAUDE_TRANSFER_NOT_AUTHORIZED.
