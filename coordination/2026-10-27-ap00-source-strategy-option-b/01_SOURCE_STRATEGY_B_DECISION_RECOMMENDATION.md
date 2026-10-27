# Step 2 — Source Strategy A/B/C Decision Analysis & B Preparation

**Decision status:** `OPTION_B_PREPARED_FOR_OWNER_REVIEW`, not an owner-selected strategy, not a licensed transfer. Date 2026-10-27.

## Alternative comparison

| Strategy | Existing source files needed at Claude destination | New design artifacts | Technical strengths | Main limitation | Current transfer readiness |
|---|---:|---|---|---|---|
| **A — Original research bundle** | 5: F07/F08/F09/F10/F12 (41,537 UTF-8 bytes) | None necessarily | Highest exact correspondence to original technical research | 5 separate file-author/licensing checks and AP-02 grants; more source exposure | NO-GO, 0/5 cleared |
| **B — Newly written source-light brief** | **0 original files**; potentially 2 new, explicitly reviewed documents | Core/safety contract + original-ID-only synthetic QA coverage | Preserves key engineering scope with less inherited text than originals, easier purpose-specific review | Must separately prove derivative expression permissions and coverage; newly drafted material not automatically independent or lawful to transfer | **PREPARED FOR REVIEW**, not cleared |
| **C — Fully independent mock design** | 0 historical source files | Entire independently designed mock specification + independently designed QA | Lowest dependence on protected research text if genuinely independently created | Lowest direct fidelity to accumulated architecture; new safety/coverage design and technical comparison required | NOT PREPARED, not approved |

### Recommended choice for the owner's consideration
**Prefer B as the working documentation path**, because the already verified 11-core/5-niche/36-test architecture can be condensed into a narrowly limited design that remains useful without moving all five original research files. Worker B ranks C as lowest in *original-file exposure*, and this finding remains valid; B is chosen here only as a **practical fidelity versus review-workload compromise**, not because its legality has been established.

To move Step 2 beyond a recommendation, the owner must explicitly choose B (or A/C), then an actual rights custodian must inspect the new exact files and approve their permitted use; if those files are copied to Claude, source-specific permission plus **AP-02** still applies. AP-01 for development is separate. No external transfer today.

## Actual Option B materials produced in this review branch

**B1:** `02_OPTION_B_SOURCE_LIGHT_MOCK_SPEC_V01_PROPOSED.md` — a newly phrased high-level conceptual design, with 11 roles, five overlays, minimal logical data contract, refusal/hold boundaries and a nonproduction terminal state.

**B2:** `03_OPTION_B_QA36_SOURCE_LIGHT_COVERAGE.csv` — 36 very short, independently rewritten *design-only* test intents keyed by the existing `QA-001…QA-036` IDs; original fixture wording not copied. A mapping report checks count/coverage against the canonical matrix.

These two files are **candidate documents only**, not a completed implementation package. Their final exact hashes and byte sizes are recorded in the GitHub receipt. Future legal review must establish authorship/derivative rights, the sufficiency of summaries, presence of external expressions and any need for further sanitization. A successful content screen is not a licence.

## No additional historical material imported

Do not include F02 original, even if its K48 summary is relevant. F02D from Draft PR #10 is *optional*, not used as B1/B2 source payload. F11 original and 13 linked historical bodies excluded; F13 origin no-transfer gate remains in original repository, not an implementation file. Raw YouTube transcripts, third-party research papers, protected archives, S08 source code, R052 original, F-190 or K029–K031 efficacy claims are not supplied.

## Exact minimal approval matrix

1. **AP-00:** owner confirms v0.2 as planning candidate; selects seven corrections or revisions, without authorizing build.
2. **Step 2 strategy:** owner confirms `B` or another option; recommended B is NOT a signed decision.
3. **Custodian B1/B2 rights:** authored expression, third-party dependencies, privacy, permitted use and recipient, exact Git SHA-1/SHA-256/bytes reviewed; dispositions `RIGHTS_UNRESOLVED` until signed.
4. **AP-01:** owner selects isolated offline mock workspace, toolchain, developer, reviewer, scope, zero spend and stop conditions.
5. **AP-02:** for any actual B1/B2 copying into a Claude workspace, the owner plus custodian authorize exact bytes and exact destination; absent -> allowed manifest `[]`.
6. **AP-03/04/05:** science, production release, post-build independent QA remain separate and unapproved.

**End state:** Two prospective rights-review documents created; no selected strategy formally approved, no source byte transfer, no prototype execution and no production Skill.
