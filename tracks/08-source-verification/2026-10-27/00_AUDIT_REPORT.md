# Independent Source Verification Audit — 2026-10-27

**Worker scope:** scientific source methods and limits; GitHub S01–S63 lineage; external R001–R171 identity and depth; F finding dependencies; public publication and licensing risks.  
**Base checkpoint:** `main@fb04d86f1512e71ba571c10315fd4d6a9fa26200` (observed 2026-10-27, repository public).  
**Branch:** `research/source-verification`; **folder:** `tracks/08-source-verification/2026-10-27/`.  
**Decision:** **AUDIT COMPLETED WITH BLOCKERS / NOT A SCIENTIFIC OR PUBLICATION RIGHTS CLEARANCE.** No production SKILL.md, scientific-efficacy claim, merge, or central status alteration is authorized.

## Method / exact access depth

Read the GitHub-hosted canonical S source master, R source master, F-90 ledger, S inspection accounting, S independent-licensing ledger, 42-link R–F crosswalk, cumulative copyright assessment, historical integration audit, Batch-2 verification, R163 erratum and publication protocol. Compared identifiers, statuses, dependencies and exceptions using RFC-4180-aware CSV parsing. Original journal/publisher online checks: JMIR R163 publication and methods, ACM R079 abstract, W3C reuse terms, GitHub licensing guidance. Live GitHub connector checks cover a **sample** of source repositories and license files, not all 63 repositories or all 171 URLs. Historical original October 14 GitHub tool logs, signed snapshots and exact source commit pins remain unavailable.

This verifies the **current committed audit registers and selected original sources**, not the identity of every upstream artifact, nor 171 independent experimental reads. Main input Git blob SHAs are recorded in `02_INPUT_LINEAGE_MANIFEST.csv`. Additional source-specific findings appear in `01_FINDINGS_AND_RIGHTS_LEDGER.csv`.

## Reproduced quantitative account

| Test | Reproduced observation | Interpretation |
|---|---|---|
| S identity | 63 rows, 63 unique IDs (S01–S63) | PASS archival register identity, not historical live source verification |
| S historical inspection class | 31 substantive named, 13 partial/non-method, 16 uninspected/deferred, 3 unsubstantiated V1 | 31 is less than historically claimed 42 deep; the missing 11 are not proven |
| Original Oct 14 extraction logs/pins | 0/63 dated logs; 0/63 exact Oct 14 commit pins; 0/63 "42 deep certified" | Historical 42 claim **UNVERIFIED**, not refuted |
| S repo metadata in historical closure | 29 YES, 34 not directly checked there | Metadata checks are not methodology/effect validation |
| S licensing evidence | 56 archival-only assertions, 5 verified GitHub license files, 1 verified README, 1 verified internal contradiction | Evidence categories are **historical ledger labels**; this worker performed additional selected spot checks |
| S commercial-reuse cleared | 0/63 marked YES | **HOLD** asset-by-asset clearance (not proof that all licenses prohibit commercial use) |
| R discovery identity | 171 rows, 171 unique R001–R171 | PASS identity, not 171 assessed empirical studies |
| R discovery depth | 132 "discovery and metadata screening only" + 39 "discovery/page metadata only" | 171/171 master rows are discovery-depth fields; separate historical registers assess ~20 sources |
| Canonical F closure | 20 PASS, 64 CONDITIONAL, 5 FAIL, 1 UNVERIFIED = 90 | PASS exact accounting, NOT 20 scientifically proven audience effects |
| R–F crosswalk | 42 links, 17 distinct R IDs and 19 distinct F IDs | Relationship proposals, no experiments or approvals |
| Referential validity | 0 unresolved explicit F→S and R–F crosswalk IDs | PASS **structural**, not validity of method/causality |
| Cumulative rights ledger | 20 assessed source-specific rows | Rights conclusions limited to scoped files/assets |

**Important register distinction:** `R079` and `R163` are marked discovery depth within the original R master even though separately archived assessments and this spot check have greater depth. Do not overwrite the historical master or retroactively call all R rows read.

## Findings requiring a director decision

1. **SV-01 HIGH — F-190 randomized contradiction.** The F-190 canonical register's `exceptions_and_limitations` and `closure_interpretation_note` describe the Ahmed R163 study as a "randomized modality comparison." The project's R163 methods erratum explicitly says allocation-sequence/concealment is unresolved. The [publisher's original Methods](https://www.jmir.org/2025/1/e69772/) describe parallel audio/text studies with screened/self-selected Mechanical Turk participants, **without explicit randomized allocation details**. Correct a future *derivative* interpretation to "parallel text/audio condition comparison; allocation mechanism unresolved." **Do not silently mutate historic F-190; it remains UNVERIFIED.**
2. **SV-02 HIGH — S39/S40 repository owner lineage unresolved.** Historic paths `HiTZ/TextDescriptives` and `neulab/DiscoScore` returned current 404s in a live repository lookup; `HLasse/TextDescriptives` and `AIPHES/DiscoScore` currently exist. Existence does not prove transfer, fork provenance, identical commit, or Oct 14 identity. Obtain original pinned SHAs, redirect/migration evidence and license snapshot before claiming historic mapping or reproducibility.
3. **SV-03 HIGH — 42 deep GitHub inspection gap.** The historical audit lists 31 individually substantive inspection headers, 13 partial, 16 deferred and 3 unsupported V1 entries; no dated extraction logs or pinned commits for any of 63. The gap of 11 cannot be certified using current repository metadata alone.
4. **SV-04 HIGH — no blanket commercial source clearance.** Only 7/63 S license evidence records go beyond archival assertion (5 direct LICENSE; 1 README; 1 internal contradiction), and all 63 `commercial_reuse_cleared=NO`. Confirm exact file/tree/version, notices, dependencies, trademarks and third-party inputs before code/content reuse. **No-license is not public-domain.** Live original `S08` [LICENSE](https://github.com/lyc4614/educational-explainer-video-skill/blob/main/LICENSE) expressly limits to personal noncommercial use and disallows derivative publication.
5. **SV-05 HIGH — scientific transfer boundary.** [R079 ACM abstract](https://doi.org/10.1145/2556325.2566239): 6.9m **viewing sessions** across four MOOC courses, not 6.9m unique viewers and not an experimental script-hook intervention. [R163 JMIR](https://www.jmir.org/2025/1/e69772/): 487 retained participants (274 text, 213 default synthesized audio), health information and comprehension/recall outcomes; not edited YouTube audiovisual attention, human VO or retention uplift. Session/student counts, effect interpretation and generalization must remain narrow.
6. **SV-06 MEDIUM — type confusion among R evidence.** R156 SEC and R158 CFPB are video galleries; R159 is a resource index with transcripts linked rather than full linked scripts verified. R052 was blocked by robots and cannot supply inspected quotation/instructions. R133 historical BBC 2012 PDF cannot establish its 2026 live guidelines.
7. **SV-07 MEDIUM — status of F findings.** Failed F IDs **F-071, F-092, F-122, F-160, F-191** and unverified **F-190** must stay quarantined. A code/text-coherence toolkit is not empirical proof of auditory writing effectiveness; independent repository count is not replication.
8. **SV-08 MEDIUM — nuanced rights.** [R163 publisher](https://www.jmir.org/2025/1/e69772/) explicitly licenses its paper CC BY 4.0 with detailed attribution requirements (copyright paragraph); this permits certain reuse **of that article under its license**, not unverified linked third-party resources/datasets. [W3C WAI terms](https://www.w3.org/WAI/about/using-wai-material/) generally allow attributed unchanged full-document distribution under W3C Document License, but not blanket modifications, with marked CC exceptions. [GitHub docs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository) confirm no license retains default copyright.

## Selected live repository/rights spot checks (2026-10-27)

- `danjdewhurst/story-skills` current root LICENSE: MIT (blob `6dc3c47c331652ddbf12759e8a6af340dd222bad`).
- `haowjy/creative-writing-skills` current LICENSE: Apache-2.0 (blob `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64`).
- `HLasse/TextDescriptives` current LICENSE: Apache-2.0 (same standard-license text blob `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64`).
- `AIPHES/DiscoScore` current root listing: **no root LICENSE observed**; current README does not establish an overall redistributable license. Do not claim no license exists anywhere in history or nested files.
- `lyc4614/educational-explainer-video-skill` current LICENSE: custom **personal non-commercial**, blob `1e5a0ab909126c7757ad98ab2ccb1a495cf9ca20`.
- These current observations do **not** recover Oct 14 commits, audit every file's sub-license or grant a blanket production clearance.

## Publication filtering and limitations

Only new original analytical prose, brief factual source observations and repository links/IDs were authored. **No raw transcript, article reproduction, proprietary export, private ZIP, credentials, publisher images/audio or source code are included.** The metadata ledger describes restrictions; it does not purport to transfer copyrighted materials. Rights review is research risk assessment, not formal legal advice.

Unresolved: 63-file-per-version license verification; S39/S40 exact legacy identity; claimed 42 deep inspection proof; full 171 publisher-level read; 151 or more R not separately assessed beyond 20 historical scope; original/derivative script permissions; full empirical validation and independent transfer tests. **Status: source-audit deliverable ready for independent director QA; science validation and publication clearance remain blocked.**
