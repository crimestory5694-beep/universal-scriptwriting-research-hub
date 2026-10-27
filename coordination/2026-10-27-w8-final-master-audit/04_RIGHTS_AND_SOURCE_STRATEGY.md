# Rights Clearance & Source Strategy — Independent Reconciliation

**Date:** 2026-10-27. **Rights decisions by AI workers: NONE.** This is a screening and research synthesis, not a legal determination or a copyright licence.

## Source A/B/C compared

| Approach | Existing original source bytes to copy | Prospective new files | Evidence fidelity / practical advantage | Blocking conditions |
|---|---:|---|---|---|
| A: exact five original technical documents | 41,537 UTF-8 bytes, five individual originals F07/F08/F09/F10/F12 | No replacement required | Best historical engineering detail | All five need real authorship/control and reuse/recipient permissions; no file currently cleared |
| B: compact amended source-light | Zero original research files if carefully authored | Two newly revised B1/B2 design files (byte sizes UNKNOWN until written) | Direct mapping to existing 11/5/36 plan, less textual exposure if actually sanitized | Prior B1/B2 still unresolved rights; technical failures (9 B1 material module gaps, 13 B2 semantic gaps); expression cases QA-003/QA-006 |
| C: independently created concept/spec | Zero original research files | One or more genuinely independent specs/QA descriptions, not authored yet | Lowest intentional original-source reliance | Sufficiency/rights of new expression, owner scope/permissions and QA need new independent review |

**Recommendation:** Keep **B as a future revision candidate**, not a selected/cleared strategy. Option C remains a relevant alternative if zero-original-file independence can be substantiated without copying research expression. Option A is available only after individual lawful rights are confirmed.

## Worker B — B1 bounded rights screen

Source B1 at Draft PR #12 head `1e496c994835742bfdd63ffac0679ba8123e1734`, blob `b8d477e00a965862bb6e3ac3ece6b1e00cecd5bb`, 8,425 UTF-8 bytes; prior independently checked SHA256 `1e499670d1c554f77c6dbac64d715d9d5196a45fc711eddc2d50be76fcc8cd46`.

Worker B reported **35 reviewed B1 segments**: 10 low and 25 moderate expression risk; content-screen overall CONDITIONAL and permission `RIGHTS_UNRESOLVED`. A bounded exact-word overlap test found zero 5–8-word exact runs compared with predecessor architecture files; this does **not** prove ownership, original expression, lack of protectable selection/arrangement, legal reuse or safe onward copying. Project Git author is not a signed natural-person copyright declaration. No complete rights chain-of-title or recipient-specific grant found.

## Worker C — B2 bounded expression and provenance screen

Prior B2 at same PR #12, blob `8055702ab7fab28619c565dc21defd7ba22be79b`, 6,966 bytes, prior SHA256 `2df26fcbcfb35c3500550d54212c9e8d499777782a30f604d949009e993e48fe`.

Worker C screened all 36 rows: **22 content PASS; 12 CONDITIONAL; 2 SANITIZATION_REQUIRED (QA-003, QA-006)**, no currently identified full-row EXCLUDE. **36/36 rights statuses unresolved; 0/36 external reproduction permission**. The expression risk is a content-screen finding, *not* technical semantic correctness. Worker F independently found 13 material QA intent gaps; copy-risk improvement must not remove original test fail/HOLD guarantees.

## Exact rights review before any external file copy

For *each selected future revised B1/B2 or original F file*:
1. Identify actual natural-person author/controller, commission/contribution/AI assistance and chain of reuse control.
2. Examine possible incorporated copyright-protected wording, tables, code, fixtures, third-party methodological excerpts and licensing/attribution.
3. Check confidential, personal or credential material and whether transfer destination storage/retention and account rights permit use.
4. Pin exact Git revision/path, Git blob SHA-1, SHA-256 over exact UTF-8 bytes and byte size; separately screen newly revised files because old SHA certificates will not apply.
5. Obtain named, dated, file-specific custodian attestation and *separate* explicit owner AP-02 file/destination/revocation authorization.
6. Test proposed source allowlist is nonrecursive; no F11 linked-body traversal, no private EDU/source archives, copyrighted transcripts, unlicensed S08 code, F13 internal gate or whole repository clone.
7. On missing evidence => `RIGHTS_UNRESOLVED / NO_TRANSFER`, external transfer list remains `[]`.

## Rights-review vs safety/security gate

Public GitHub read access, no visible protected quotes, source-light rewording or bounded overlap findings do not certify a licence. A named workspace, genuine owner AP-01 authorization and separately verified rights and AP-02 for any copying are still required. A technical candidate accepted as **planning only** never becomes an authorized source payload.

**Current result:** 0 existing original files cleared, B1/B2 uncleared, B2 needs revision, approved Claude-transfer bytes 0, actual transfers 0. `G17=HOLD`; production `G18=HOLD`.
