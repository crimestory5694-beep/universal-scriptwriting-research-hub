# Research Director Decision — Educational Transcript Corpus After Batch 14

**Decision ID:** `RD-EDU-B14-COVERAGE-01`  
**Date:** 2026-10-24 (Asia/Dubai)  
**Status:** `AUTHORIZE_STAGED_SOURCE_COVERAGE_AND_QA`; `FULL_CORPUS_CLOSURE=HOLD`; `SKILL_MD_PRODUCTION_AUTHORIZATION=NO`  
**Scope:** Historical educational transcript evidence corpus **only**, not all independent scientific/YouTube scriptwriting source tracks.

## 1. Basis of decision — independently checked, not inferred

Original attached input: `EDU_FULL_ARCHIVE_ZERO_SKIP_REAUDIT_B14 (1).zip` (**10,336,822 bytes**). It contains 24 top-level entries, including preserved earlier research archives and the authoritative Batch14 progress and cumulative claim registers.

- `EDU_REAUDIT_B14/11_UPDATED_162_SOURCE_PROGRESS_REGISTER.csv`: 162 distinct `EDU-SRC` source rows; 116 exactly `INDEXED_NOT_CLAIM_EXTRACTED`; six exactly `BATCH01_REPORTED_COMPLETE_REAUDIT_OPEN`; 40 other reported independently reviewed/completed entries.
- `EDU_REAUDIT_B14/02_CUMULATIVE_HISTORICAL_PRESERVING_983_CLAIMS.csv`: **983 claim rows**, **983 unique `EDU-C` IDs**, beginning `EDU-C0001` and ending `EDU-C0983`. These are **provisional source-teaching records**, not scientifically established performance improvements.
- `EDU_REAUDIT_B14/15_EXACT_CONTINUATION_CHECKPOINT.md`: next `EDU-SRC0006`, next claim ID `EDU-C0984`, old versions immutable.
- Historical nested Batch13–Batch08 research ZIPs are present in the Batch14 archive. **Their presence does not establish access to all 12 original raw transcript ZIPs**. The actual source archives need separate file/hash verification before any new extraction. Raw third-party transcript bytes may not be published to this public repository.

This review verified source and claim **accounting**, not full substantive fidelity of all 983 claims to unseen original audio/teaching transcripts.

## 2. Decision

### 2.1 Full educational corpus (the 162-source completeness claim)

**APPROVE the requirement to finish all 116 first-time source dispositions plus six historical Batch01 independent QA reviews.**

A complete source disposition means original source text, access and hash/identity were checked, the entire source text was read without gaps (if accessible), unique educational scriptwriting knowledge and real worked examples were extracted with exact source anchors, and limitations/duplicates/out-of-scope judgments were explicitly recorded. It does **not** mean forcing extra claim IDs from every irrelevant video. If the source is genuinely out of scope after original review, mark `FULL_READ_OUT_OF_SCOPE_NO_NEW_CLAIMS` with rationale. If original source is unavailable, keep `SOURCE_ACCESS_BLOCKED`, not `REVIEWED`.

No source should be silently skipped to meet a completion metric. Exact source IDs, historic claim IDs and all past addenda remain unchanged.

### 2.2 Narrower early pilot vs full research

For a **separately authorized scope-bounded prototype**, it is not scientifically necessary to extract all 162 educational sources before *planning* a test on a carefully specified category. Such a pilot may use only actually read, reliable and rights-cleared claims **if** a separate Director scope/rights/evidence/validation gate is later approved. No such pilot is automatically approved now.

Do **not** describe a scoped pilot as completion of the universal educational archive. Do **not** treat completing all 162 source reviews as evidence that a script technique improves YouTube retention.

### 2.3 Historical QA (six exact sources; original claim count 83)

| Source ID | Original teaching title | Historical claims to re-audit |
|---|---|---:|
| EDU-SRC0021 | 7 Storytelling Techniques to Tell Great Stories | 9 |
| EDU-SRC0114 | Storytelling Science To Hook Viewer Till End — 4 Years in 10 Mins. | 16 |
| EDU-SRC0123 | The Storytelling Formula YouTubers Use to Hook You | 13 |
| EDU-SRC0148 | Film Script Formatting — Michaela Lizac | 16 |
| EDU-SRC0149 | Hindi teaching — YouTube niche, TAM, lens and AVE | 13 |
| EDU-SRC0150 | How I Write YouTube Video Scripts — Nolan Molt / Think Media | 16 |
| **Total** | **6 historical source QA reviews** | **83** |

Check original recorded claims, source-text anchors, numbered versus alternative frameworks, examples, source roles and missing substantive teachings. Preserve historical 83 original claims unchanged; append correction-only records. Allocate new claim IDs only for genuinely distinct newly established teachings after source-level de-duplication.

### 2.4 First-time source extraction (116)

Follow the [exact queue](EDU_122_PENDING_SOURCE_REVIEW_QUEUE_2026-10-24.csv). **Begin with EDU-SRC0006** as the fixed Batch15 continuation, subject to obtaining the original bytes and independently confirming its SHA.

- Source: `EDU-SRC0006` — *25 Storytelling Secrets I Wish I Knew In My 20s*.
- Historical container: `transcripts (1) (1).zip`; historical member SHA-256: `f1db6e3dc80e82a03300f3c9022234610466702a48e316a92eb0a275d6fc96ed`.
- Next unused claim: **`EDU-C0984`**; it is a reserved *next* ID, **not** an already extracted claim.
- Parallel QA candidate at Batch15: **EDU-SRC0021**. Claim IDs must be issued centrally and sequentially after any new full-read claims to prevent race collisions. For reliable accounting, sequential claims allocation is preferred.
- Continue all remaining 115 pending first-time sources using the queue and file-availability gates. Sources whose titles suggest adjacent channel business, AI-tooling or unrelated topics must still receive a defensible full-read scope disposition, but shall not have artificial scriptwriting lessons invented to boost claim totals.

An archive may be processed in manageable source-specific batches; **do not force a new arbitrary quota of claims per source**, or assign a numeric batch count unsupported by source length.

## 3. Required operations and quality gates

1. **Preflight original source access:** locate original raw member bytes, compare SHA-256 to recorded historical hash, verify exact member path and stable source ID; check text encoding and completeness. Library metadata, previous text quotes or title similarity do not substitute for a full original.
2. **Full continuous text coverage:** record source character/byte total, contiguous ordered reading spans, and any gaps/ASR uncertainties. Avoid inventing audiovisual timestamps or source audio fidelity.
3. **Deep teaching extraction:** distinguish concrete step, mechanism as creator describes it, actual example, hypothetical example, claims of results, known counterexample and optional format applicability. Do not collapse twenty substantive lessons to a generic summary.
4. **Evidence role:** creator claim ≠ validated neuroscience or causal CTR/retention impact; rhetorical percentage/viral titles ≠ measured outcomes; cite external research only when independently examined.
5. **Repetition/relations:** preserve full past claim and relationship ledgers, append corrections, audit duplicates and near-duplicates, preserve titled-source distinct byte versions.
6. **Historical QA:** independently review six earlier Batch01 sources against original text; add only justified corrections, and record both original and amended interpretation.
7. **Publication safety:** this GitHub hub is **PUBLIC**. Do not upload unlicensed raw third-party transcript text/ZIPs, source-dense copyrighted reconstructions, credentials or private content. Keep such materials in a separately permissioned, lawfully held work context. Only write metadata, own publication-safe derived analysis, progress and director decisions here.
8. **Independent closure audit:** after each batch, update a new version of the 162-source progress register; verify source partition sums exactly 162, claim IDs consecutive and unique, source SHA and evidence anchors, rights/status exceptions, and a traceable full-historical correction chain. Issue no blanket completion until every source has a verified resolution and all six QA are actually complete.
9. **Final completion criteria:** `FIRST_TIME_PENDING=0`, `HISTORICAL_QA_PENDING=0`, all 162 source IDs accounted for, no unresolved full-source-access exceptions masquerading as successful reads, versioned integrity manifests and original-hash checks passed, no unsupported content-effect assertions. New claim total must be **computed**, never preselected.
10. **Separate production gate:** even then, test designs T01–T13 remain unexecuted until cleared owner permissions, reviewers and an explicit test decision; completion of transcript extraction by itself does not authorize claims of universal effectiveness or final `SKILL.md`.

## 4. Execution feasibility / outstanding blockers

The Batch14 ZIP available for this decision preserves historical research artifacts; original 12 raw transcript ZIP containers have **not been independently verified accessible within the available working attachments**. Earlier Library searches located some source-related loose text files (including composite material relevant to EDU-SRC0148/0149/0150), but verified member boundaries and exact historical hashes still have to be checked before claiming completed QA. The `transcripts (1) (1).zip` original file needed for EDU-SRC0006 has **not yet been verified available to this execution**.

**Therefore:** source-queue planning is authorized and complete, but **no Batch15 claim extraction or independent QA completion is claimed in this decision**. Preserve `EDU-C0984` as the next unused claim ID; do not mint IDs without actual full source text.

## 5. Research Director decision record

```text
DECISION_ID: RD-EDU-B14-COVERAGE-01
RESEARCH_COVERAGE_POLICY: COMPLETE_ALL_162_SOURCE_DISPOSITIONS
SOURCE_CENSUS: 162
B14_REVIEWED: 40
FIRST_TIME_PENDING: 116
HISTORICAL_QA_PENDING: 6
B14_PROVISIONAL_CLAIMS: 983
NEXT_SOURCE_ID: EDU-SRC0006
NEXT_UNUSED_CLAIM_ID: EDU-C0984
BATCH15_SOURCE_ACCESS: NOT_YET_INDEPENDENTLY_VERIFIED
BATCH15_EXTRACTION_COMPLETED: NO
HISTORICAL_SIX_QA_COMPLETED: NO
ALL_EDUCATIONAL_RESEARCH_COMPLETE: NO
STAGED_EXTRACTION_PLAN: ACCEPTED
SOURCE_TEXT_REDISTRIBUTION_TO_PUBLIC_GITHUB: NO_WITHOUT_RIGHTS
SCOPED_PILOT_OPTION: FUTURE_SEPARATE_AUTHORIZATION_ONLY
A1_EXECUTION_AUTHORIZED: NO
PRODUCTION_SKILL_MD_AUTHORIZED: NO
```

**Final decision:** `COVERAGE_PLAN_APPROVED`; `RESEARCH_SOURCE_COMPLETION_PENDING`; `CLAUDE_FULL_CORPUS_HANDOFF=HOLD`. This file is an original Director governance decision; it is not a new substantive creator teaching or empirical study.
