# Worker C — Independent B2 QA-36 Rights, Provenance and Expression Audit

**Date:** 2026-10-27 (Asia/Dubai) · **Workstream:** Worker C rights/expression only · **Branch:** `research/w8-b2-provenance` · **Scope:** independent static content review; no semantic-equivalence ruling.

## Finding and limits

The candidate Option B2 CSV has 36 synthetic-design cases, mapped in order to canonical QA-001…QA-036. The source files were read from their exact GitHub refs and blob checks passed. Every original and B2 row is `DESIGN_ONLY`. In B2 every row says `current_source_copy_authorized=NO` and `PENDING_INDEPENDENT_QA_AND_RIGHTS_REVIEW`.

**Content screen (not permission):**

- `CONTENT_SCREEN_CONDITIONAL`: **12** rows
- `CONTENT_SCREEN_SANITIZATION_REQUIRED`: **2** rows
- `CONTENT_SCREEN_PASS`: **22** rows
- `EXCLUDE`: **0** rows identified from currently visible text; future discovery of third-party material could change the result.
- **36/36 external-reproduction rights statuses: `RIGHTS_UNRESOLVED`.**
- **0/36 source transfers authorized**; permitted Claude/source-copy manifest remains `[]`.

No complete distinctive narrative passages, externally sourced quotations, transcript extracts, original archived identifiers in fixtures, source code, images, or copied real bulletin/incident content were observed *in the B2 CSV text*. This is a narrow textual observation, not a conclusive evidence-of-absence finding for the underlying drafting workflow, original F12, linked documents, or future expanded fixtures. B2 remains a potentially derivative artifact; fresh words do not independently establish a licence or ownership. The test concepts are largely general functional constraints, but unique test-fixture expression and ownership chain require separate documentary review.

## Audit method and evidence

1. Verified live `main=0776afd52001c2d9021b1749f7b936bc1dc4e37d` and dedicated branch head on the same SHA before writing. Read Master plan `research/w8-master-orchestration`; Draft PR #12 confirmed open/draft and reviewed read-only.
2. Obtained original F12 from pinned main and candidate B2 from pinned source commit `1e496c994835742bfdd63ffac0679ba8123e1734`. Exact blob IDs and UTF-8/SHA-256 fingerprints are specified in `02_B2_HASH_AND_SOURCE_LINEAGE.md`.
3. Parsed quote-aware CSV and paired by exact, contiguous QA ID (36 unique original IDs, 36 unique new IDs); inspected both original fixture/expected handling and B2 intent/handling. Recorded **36 case-specific editorial analyses** in the ledger.
4. Added a small reproducible diagnostic per case: longest consecutive word sequence shared between the original's case/fixture/expected text and B2's intent/expected handling. This is **only a lexical pointer**, not an infringement probability, a copyright determination, or a finding of semantic equivalence.
5. Tested text visible in B2 for direct third-party paragraphs/quotes, source identifiers, proprietary examples, notices and substantive source-byte inclusion. A hypothetical mention of a licence, agency bulletin or primary study is distinguished from importing its text.
6. Flagged cases needing optional wording improvement separately from blockers requiring actual custodian/owner authority. An unverified ownership chain prevents all actual outside reproduction, including copying to Claude.

## Highest attention cases

- **QA-003:** source-layer phrasing calls a mock identifier “protected”; this can confuse referential integrity with legal protection. Recast as a *reserved fictitious identifier* and keep the lineage check.
- **QA-006:** generic wording still evokes disputed historical source part hashes. Ensure this is *entirely fictional*, no historic EDU keys/hashes or archived member-body leakage.
- **QA-007/008/009:** source-availability and quarantine ideas are usable in abstraction; real B70–72 archive, F-190 and R052 excerpts/identifiers are not needed for a standalone mock.
- **QA-016:** preserve fully invented competitor-title fixtures. Rights review should not silently import a real person's uploaded title, narrative or video transcript.
- **QA-023/024/033:** no R163 dataset, R079 lecture content, T12 protocol or experiment-result language should be imported.
- **QA-035/036:** production-release permission and access-versus-copy licensing are separate rights and governance questions. The mock expected denial is not authorization to release or reproduce.

## Provenance and rights determination

F12 original has a project-repository “analyst-original/public-safe” manifest claim. That manifest is useful documentation, **not an independently verified contract, contributor assignment, exclusive licence or consent to copy elsewhere**. PR #12 identifies B2 as a newly authored derivative candidate and itself leaves rights unresolved. Public visibility on GitHub cannot by itself establish an open-source licence or external copying permission. Even short functional tests might include third-party expression once concrete fixtures are substituted.

**Rights evidence required before any future external reproduction:** named author(s) and contributions; chain-of-title or licence permitting derivative and recipient-specific reproduction; evidence inventory for any borrowed wording/fixtures/quotes/source claims; privacy/confidentiality and contract checks; required attribution/notice; version-locked SHA-1, SHA-256, bytes; exact external destination and purpose; custodian decision and dated owner AP-02 authorization. A separate AP-01 mock-build decision would still be required. The absence of textually obvious third-party extracts is not a legal clearance.

**No legal infringement conclusion:** similarity does not prove infringement; paraphrasing does not guarantee clearance. This is an independent rights-risk screen, not a legal opinion, a rights-owner attestation, or Worker F's QA semantics acceptance.

## Controlled conclusion

Use B2 only as an unsigned, public-safe **owner-review document** pending further independent evidence. Sanitize QA-003 and QA-006 in *proposals only*; do **not** modify original F12, original B2 or Draft PR #12. Independently document source/rewrite/rights decisions before any future transfer. `AP-00=PENDING`, `AP-01/AP-02=NOT_AUTHORIZED`, `G17/G18=HOLD`, all 36 `DESIGN_ONLY`; production, live QA and Claude transfer prohibited.
