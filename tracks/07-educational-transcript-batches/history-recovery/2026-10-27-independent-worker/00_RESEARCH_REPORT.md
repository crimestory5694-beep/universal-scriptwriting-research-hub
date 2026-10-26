# Independent historical integrity recovery - 2026-10-27

Branch: `research/history-recovery`. Base `main` HEAD independently checked as `fb04d86f1512e71ba571c10315fd4d6a9fa26200`. Repository is PUBLIC. This work is scoped to a new worker-owned Track07 folder; no canonical source hashes, prior manifests, claims, other workers' files or production SKILL.md are modified.

## Original evidence verified
- User-provided S4 private continuity ZIP: 31,591,609 bytes; SHA256 `ec03c8132d511c047701b4c29be563fe705ca5a3155941c77f3f948ec3920aab`.
- Independent recursive examination: **65 distinct nested ZIP byte identities, 65/65 ZIP CRC PASS** (includes side branches, not just linear predecessor).
- Original loose composite parent, recovered separately from the user's Library: `Pasted markdown (4)(1).md`, 202,482 bytes, SHA256 `3e6a80d931f2d5ef0b181470ab1ba72a10a7db4272958e09c4afda3cab6854b8`; matches frozen physical-parent provenance on existing main.
- Earlier B67-B69 original preserved intact: 14,255,899 bytes, SHA256 `dcf7bbda139c96a9988dd12bec65bc92cc9c53c48635c32af6802a54a7f9af4a`.
- B70-B72 original **NOT FOUND** in all 65 distinct nested ZIPs. Expected archive 15,051,407 bytes SHA256 `5df730958eccdce94a99643e8b8e0f5f81d552146bc4cf2cb026a56eef84b6d6`. A 14,990,802-byte surrogate SHA256 `5ef7a7b1d02d372e5ac7d1479ee1585386f18e91b0d921183b33b73b0f21f9b5` exists, but **cannot certify/reconstruct the missing historical original**. Negative search is limited to accessible user-supplied chain plus separately checked Library lookup; does not establish worldwide absence.

## Important nine-hash forensic finding
The historical `EDU-SRC0139` through `EDU-SRC0147` checksums were repeatedly reported as source-part conflicts. We independently verified the ORIGINAL loose physical parent and the frozen B67-B69 source-progress register. We split the document on its ten numbered Markdown section headings and SHA256-hashed each **full section after the heading, stripped at its outer boundaries, encoded UTF-8**.

**10/10 complete section SHA256 values exactly match their original frozen historical checksums**, including 9/9 previously disputed records. The **body-only** SHA256 differs in 9/9 because those nine sections begin with link/metadata material on separate lines; the first section's link is on the heading and its body-only hash also matches. This is an **input-boundary/provenance convention mismatch**, not demonstrated loss or alteration of source content. Every frozen historical hash is PRESERVED; an independent director must approve reclassifying prior conflicts before canonical closure. Exact values and counterpart hashes are in `01_SECTION_SHA_RECONCILIATION.csv`.

## Other forensic cases
- **B25:** Historical public receipt claimed outer SHA256 `4c2765c0...`; nested preserved 3,506,773-byte ZIP actually SHA256 `88358c15c6358bbe6242fcaf6c5bc511269e75ff7c7057a211f115976db7c325`. All 11/11 internal manifest file checks and ZIP CRC PASS. The historic claimed outer byte sequence is still unlocated: **OPEN**, do not rewrite its original receipt.
- **P3-B06 manifest:** 12/12 nonself listed files check out. Historical `11_PRIVATE_QA_AND_HASH_MANIFEST.json` claims its OWN SHA256 `c017c655...` but the actual preserved manifest bytes SHA256 `a6d3ccebfa973cf51bd18069140715907e4b7069e5b9d159381960e09bfd5ecb`. Self-embedded hash is not a trustworthy verification design. Treat this addendum as external witness; original manifest remains immutable.
- **B58:** Original surviving `EDU-SRC0056` caption file is exactly 173 bytes SHA256 `85637432c26d77d791237cd0d0ede016fedf17a80ca10b85c416856c5cfda105` (exact match). It remains an incomplete two-line supplied fragment. No full-video source recovery or invented continuation.

## Scope and decision
This report provides **archival integrity and hash-boundary evidence**, not truth of transcript claims, access rights, audio/video validation, psychology/algorithm effects, approved EDU-C merges or production writing mandates. Existing official historical checkpoint (104/162 and EDU-C3051) stays unchanged. T01-T13 remain NOT EXECUTED. Production SKILL.md and broader approval remain HOLD.

Potential verified repair is append-only (external hash-scope reconciliation matrix); historical original files and frozen checksums are not rewritten. See QA protocol, rights manifest, and continuation handoff in this worker-owned folder.
