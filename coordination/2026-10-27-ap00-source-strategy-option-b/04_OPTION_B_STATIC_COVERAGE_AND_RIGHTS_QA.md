# Option B — Static Coverage, Provenance and Rights-Screen QA

**Research status:** STATIC_QA_PASS_WITH_REVIEW_LIMITS. NOT legal clearance, code acceptance, independent scientific validation or owner authorization. Date 2026-10-27.

## Verified input and authored output identities

| Artifact | Git blob SHA-1 | Treatment |
|---|---|---|
| Candidate v0.2 Worker A `03_PROPOSED_PROTOTYPE_SPEC_V02.md` | `d4b4a19f67772d4588b2ea7c3cd15b0b74e600fb` | Read only; proposed ideas/constraints, not an accepted owner spec |
| Original QA36 matrix `06_ACCEPTANCE_TEST_MATRIX.csv` | `88e89ee233c967c5b8a0b645b0d401f6c1d2ccea` | Read only; ID and test-domain comparison; 36 DESIGN_ONLY |
| New Option B1 `02_OPTION_B_SOURCE_LIGHT_MOCK_SPEC_V01_PROPOSED.md` | `b8d477e00a965862bb6e3ac3ece6b1e00cecd5bb` | New derivative candidate, copyright/reuse rights unresolved |
| New Option B2 `03_OPTION_B_QA36_SOURCE_LIGHT_COVERAGE.csv` | `8055702ab7fab28619c565dc21defd7ba22be79b` | Newly authored 36 condensed synthetic scenario intents, rights unresolved |

## Actually performed structural checks

1. New B1 contains **exactly 11 distinct A00…A10 core role IDs** and **five distinct N01…N05 adapter IDs**, cross-referenced with the proposed v0.2 research spec. The old N-01…N-05 are aliases, not a second five.
2. Original F12 and B2 CSVs parsed with proper quoted-CSV field handling: both have **36 rows**, contiguous identical `QA-001…QA-036`, no missing or duplicated IDs.
3. B2 has **36 distinct newly phrased synthetic scenario intents**; 36/36 test rows are `DESIGN_ONLY` and every row has `current_source_copy_authorized=NO`.
4. Key safeguard concepts are present in B1: inaccessible evidence, access-versus-copy rights, timestamp differences, no self-review, synthetic disclosures, no title-certainty upgrade, immutable revisions, no waiver of critical rights/harm gates, mock-only terminal state.
5. Original F02 48 K rows remain untouched; the new B1/B2 do not require original F02 or its optional PR10 source-light derivative as transfer inputs. K029–K031 remain excluded as positive scientific evidence.
6. No source archive, raw third-party transcript, authentic current-event claim, private data, licensed code, real media or external API input was copied into the new conceptual B1/B2 as an explicit attachment or linked-body import.

## Coverage notes (not executable test proof)

The B2 table is a **condensed design intent crosswalk**, *not* a replacement for the original F12 test-body semantics unless a technical/rights reviewer explicitly confirms equivalence. The QA-031 line was refined on the same isolated branch to include both accessible visual descriptions and unchecked synthetic captions. A later technical acceptance reviewer must inspect every new scenario for lost qualifiers, especially QA-002 retrieval/review timestamps and QA-036 access/copy permission. The original F12 remains immutable and all actual test execution counts are zero.

No source-to-derived textual similarity/licence opinion or independent copyright ownership chain has been established. New language is freshly composed, but draws on project design ideas whose provenance and legal reuse rights still need substantive assessment. A public README or the act of rewriting cannot supply that consent.

## Mandatory rights-screen before a future external copy

For B1 and B2 independently: name actual writer/rights controller and any other contributors; verify the source idea/expression lineage and third-party quotation/code; inspect confidentiality/privacy; document any required attribution/licence; pin exact SHA-1 plus independently computed SHA-256 and UTF-8 bytes; specify the approved Claude account/workspace/read-only purpose, duration, retention and revocation; obtain independent custodian opinion and specific owner AP-02 countersignature. If any element missing, output `RIGHTS_UNRESOLVED` and leave transferable manifest `[]`.

Even if B1/B2 ultimately become rights-cleared, AP-01 separate isolated mock-code authorization must precede development, AP-03 human/scientific tests remain unexecuted, and AP-04 production Skill release is unrelated.

**Final disposition:** `AP00_REVIEW_RECOMMENDATION_READY`, `OPTION_B_CANDIDATE_MATERIALS_CREATED`, `QA_ID_COVERAGE_36_OF_36`, `OWNER_DECISIONS_PENDING`, `LEGAL_TRANSFER_RIGHTS_UNRESOLVED`, `NO_CLAUDE_TRANSFER`.
