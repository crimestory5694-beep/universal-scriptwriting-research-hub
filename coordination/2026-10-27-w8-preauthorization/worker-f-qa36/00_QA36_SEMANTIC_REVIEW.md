# Worker F — Independent QA-001..QA-036 semantic review

**Date:** 2026-10-27  
**Status:** REVIEW_COMPLETE / DESIGN_ONLY / NO SOFTWARE TESTS EXECUTED  
**Authorization:** NONE (AP-00 undecided; AP-01/AP-02 not authorized; G18 not signed)  
**Exclusive worker branch:** `research/w8-qa36-semantic-audit`

## Exact input identity and method

- GitHub repository: `crimestory5694-beep/universal-scriptwriting-research-hub`
- Verified main and Worker F starting commit: `0776afd52001c2d9021b1749f7b936bc1dc4e37d` (both read from GitHub branch endpoints).
- Original `worker-deliverables/skill-architecture/2026-10-27/06_ACCEPTANCE_TEST_MATRIX.csv` at `main`; blob `88e89ee233c967c5b8a0b645b0d401f6c1d2ccea`.
- B2 `coordination/2026-10-27-ap00-source-strategy-option-b/03_OPTION_B_QA36_SOURCE_LIGHT_COVERAGE.csv` at pinned `1e496c994835742bfdd63ffac0679ba8123e1734`; blob `8055702ab7fab28619c565dc21defd7ba22be79b`.
- Master orchestration: `research/w8-master-orchestration`, `00_MASTER_ORCHESTRATION_PLAN.md`, blob `7d59098426914016f76918050efd1f74abf62a23`.

Checked both CSVs one-to-one by original QA identifiers, compared original module/fixture/gate against B2 scenario/handling; extracted loss of condition, evidence status, explicit safety gates, uncertainty, and change invalidation. This is a static document-analysis audit, **not an executable test harness**. No rights determination made.

## Result

| Classification | Cases | Meaning |
|---|---:|---|
| SEMANTIC_MATCH | 5 | Core scenario, premise and outcome aligned; optional specificity may remain |
| CONDITIONAL_MATCH | 18 | Intent substantially aligned but explicit guard/check is lost |
| MATERIAL_GAP | 13 | B2 changes a critical input or omits a critical specific restriction |
| TOTAL | 36 | 36 distinct original and B2 IDs |

**All 36 are DESIGN_ONLY. 0/36 software tests executed. No B2 row is a measured PASS.** This classification records preservation of *test intent*, not implementation readiness or source/rights permission.

Coverage codes: **Y** = original meaning retained; **P** = retained partly / underspecified; **N** = materially changed or absent; **-** = requirement was not explicitly stated in original row (do not invent a test). Nine dimensions: P purpose, M module, C preconditions, E evidence assumptions, G expected gate/eligibility, N negative fixture, S safety/rights, U uncertainty, V review/version invalidation. Original CSV only explicitly specified revision-based downstream invalidation for QA-034; '-' is not proof that production can ignore versioning. A conditional match still requires the proposed correction; no verdict is a software PASS.

## Individual findings (all 36)

### QA-001 — CONDITIONAL_MATCH
- **Original intended behavior:** Prevent worker changes escaping isolated branch and assigned folder.
- **B2 comparison / lost information:** B2 asks for separation and source non-edits but does not explicitly assert main unchanged or constrain every output to the reserved worker path.
- **Coverage P/M/C/E/G/N/S/U/V:** Y / P / P / Y / P / Y / P / - / -.
- **Source-light correction:** Add a synthetic diff fixture proving main remains unchanged and all newly created paths stay inside the designated folder.
- **Execution:** DESIGN_ONLY; no software run.

### QA-002 — MATERIAL_GAP
- **Original intended behavior:** Missing SourceRecord access_state OR independent review-time field must block verification.
- **B2 comparison / lost information:** B2 covers an access label plus missing assessment date; it does not exercise missing access_state and could confuse access/retrieval timestamp with independent review timestamp. HOLD missing identity is not explicit.
- **Coverage P/M/C/E/G/N/S/U/V:** P / Y / N / N / P / P / P / N / P.
- **Source-light correction:** Add two separate missing-field fixtures; store accessed_at/retrieved_at distinct from reviewed_at and require explicit HOLD_MISSING_IDENTITY and verification=UNKNOWN.
- **Execution:** DESIGN_ONLY; no software run.

### QA-003 — CONDITIONAL_MATCH
- **Original intended behavior:** Protected S/F/R/K/V/EDU historic IDs must not be rekeyed; relation append is legal path.
- **B2 comparison / lost information:** B2 uses an invented protected historical identifier, but omits namespace coverage and the append-relation-only repair behavior.
- **Coverage P/M/C/E/G/N/S/U/V:** Y / P / P / P / P / Y / P / - / -.
- **Source-light correction:** Exercise each protected namespace and require reject-rekey plus append-only linked relation while preserving the original ID.
- **Execution:** DESIGN_ONLY; no software run.

### QA-004 — CONDITIONAL_MATCH
- **Original intended behavior:** Public export of substantial third-party transcript text must be blocked and logged as rights risk.
- **B2 comparison / lost information:** B2 external script paragraphs express the general protection, but do not cover transcript-length/public-output boundary explicitly.
- **Coverage P/M/C/E/G/N/S/U/V:** Y / Y / P / P / Y / Y / P / - / -.
- **Source-light correction:** Include synthetic public/export boundary, substantial transcript fixture, rejection, and recorded rights-risk reason; use wholly invented text.
- **Execution:** DESIGN_ONLY; no software run.

### QA-005 — CONDITIONAL_MATCH
- **Original intended behavior:** Reading a whole source with unknown reuse rights is not redistribution permission.
- **B2 comparison / lost information:** B2 covers a viewable mock with blank permission, but its expected handling does not name HOLD_RIGHTS or all forms of reuse.
- **Coverage P/M/C/E/G/N/S/U/V:** Y / Y / Y / P / P / Y / Y / P / -.
- **Source-light correction:** Keep readable/source-access state distinct from rights state; return HOLD_RIGHTS on attempted public reuse/copy/export.
- **Execution:** DESIGN_ONLY; no software run.

### QA-006 — CONDITIONAL_MATCH
- **Original intended behavior:** Disputed provenance must remain disputed for nine historical member-part hash mismatches.
- **B2 comparison / lost information:** B2 covers synthetic disagreement with manifest, but drops exact nine-member scope and explicit prohibition against rewriting historic evidence.
- **Coverage P/M/C/E/G/N/S/U/V:** Y / Y / P / P / P / Y / P / P / P.
- **Source-light correction:** Use nine synthetic disagreement records, preserve originals immutably and emit HOLD_DISPUTED_PROVENANCE; no hash repair by rewriting.
- **Execution:** DESIGN_ONLY; no software run.

### QA-007 — MATERIAL_GAP
- **Original intended behavior:** Missing original B70-B72 archive cannot be replaced by a cumulative surrogate ledger.
- **B2 comparison / lost information:** B2 changes precise lost archive/surrogate distinction into generic unavailable original and an independently summarized substitute, erasing the historic exception.
- **Coverage P/M/C/E/G/N/S/U/V:** P / Y / N / N / P / P / P / P / P.
- **Source-light correction:** Retain B70-B72 as identifiers only; use invented missing exact member plus surrogate cumulative ledger and require HOLD_ORIGINAL_MISSING without promotion.
- **Execution:** DESIGN_ONLY; no software run.

### QA-008 — MATERIAL_GAP
- **Original intended behavior:** Quarantined F-190 cannot be used as positive support.
- **B2 comparison / lost information:** B2 substitutes a generic unverified research finding and omits the explicit quarantined identifier and role block.
- **Coverage P/M/C/E/G/N/S/U/V:** P / Y / N / N / P / Y / N / P / -.
- **Source-light correction:** Introduce synthetic metadata row with identifier F-190 and quarantined source_role; any promotion to positive evidence must give HOLD_SOURCE_ROLE.
- **Execution:** DESIGN_ONLY; no software run.

### QA-009 — MATERIAL_GAP
- **Original intended behavior:** Blocked R052 must not be represented as independently read original.
- **B2 comparison / lost information:** B2 uses an index pointing to an unread study, partly matching noninspection but drops blocked R052 provenance and its source-role restriction.
- **Coverage P/M/C/E/G/N/S/U/V:** P / Y / N / N / P / Y / N / P / -.
- **Source-light correction:** Use synthetic R052 blocked/read_status metadata; disallow independently_read_original claim and return HOLD_SOURCE_ROLE.
- **Execution:** DESIGN_ONLY; no software run.

### QA-010 — CONDITIONAL_MATCH
- **Original intended behavior:** Creator efficacy/90% retention assertions are attributed, not scientific proof.
- **B2 comparison / lost information:** B2 says a guaranteed audience effect, preserving causal skepticism but omitting the 90% retention metric and unverified creator-provided basis.
- **Coverage P/M/C/E/G/N/S/U/V:** Y / Y / P / P / Y / Y / P / P / -.
- **Source-light correction:** Use synthetic unsupported 90% retention improvement claim and require attribution-only labeling, never scientific validation.
- **Execution:** DESIGN_ONLY; no software run.

### QA-011 — SEMANTIC_MATCH
- **Original intended behavior:** Outdated warning must never be presented as live warning.
- **B2 comparison / lost information:** Synthetic expired alert evaluated at a draft as-of time adequately preserves staleness negative and ban on current phrasing.
- **Coverage P/M/C/E/G/N/S/U/V:** Y / Y / Y / Y / Y / Y / Y / Y / -.
- **Source-light correction:** Optional clarity: use an explicit alert_expiry and as_of to exercise HOLD_STALE_FORECAST.
- **Execution:** DESIGN_ONLY; no software run.

### QA-012 — SEMANTIC_MATCH
- **Original intended behavior:** Model output is not a warning formally issued by an agency.
- **B2 comparison / lost information:** Projection-to-official-warning category confusion and corrective hold are preserved.
- **Coverage P/M/C/E/G/N/S/U/V:** Y / Y / Y / Y / Y / Y / Y / Y / -.
- **Source-light correction:** Optional clarity: map hold to HOLD_UNVERIFIED_FACT pending issuer/type verification.
- **Execution:** DESIGN_ONLY; no software run.

### QA-013 — CONDITIONAL_MATCH
- **Original intended behavior:** Old forecast explicitly dated and linked can be reviewed historically, not used as live authority.
- **B2 comparison / lost information:** B2 preserves historical-only review but does not require a traceable issue date and source link.
- **Coverage P/M/C/E/G/N/S/U/V:** Y / Y / P / P / Y / Y / Y / P / -.
- **Source-light correction:** Attach synthetic archived bulletin issue_date and immutable locator; allow editorial review only when correctly dated and linked.
- **Execution:** DESIGN_ONLY; no software run.

### QA-014 — CONDITIONAL_MATCH
- **Original intended behavior:** An engine contract award is not evidence of fielded operational fleet.
- **B2 comparison / lost information:** B2 preserves contract-versus-deployment, but lacks engine-stage granularity and explicit HOLD_UNVERIFIED_FACT.
- **Coverage P/M/C/E/G/N/S/U/V:** Y / Y / P / P / P / Y / Y / P / -.
- **Source-light correction:** Specify synthetic engine-only award versus fielded fleet and require stage claim HOLD_UNVERIFIED_FACT.
- **Execution:** DESIGN_ONLY; no software run.

### QA-015 — SEMANTIC_MATCH
- **Original intended behavior:** One-party battlefield allegation cannot be asserted as established fact.
- **B2 comparison / lost information:** B2 retains single-party source context, attribution, and denial of unqualified certainty.
- **Coverage P/M/C/E/G/N/S/U/V:** Y / Y / Y / Y / Y / Y / Y / Y / -.
- **Source-light correction:** Optional clarity: render HOLD_UNVERIFIED_FACT for any unqualified outcome.
- **Execution:** DESIGN_ONLY; no software run.

### QA-016 — CONDITIONAL_MATCH
- **Original intended behavior:** Title conversions must not convert a disputed competitor premise into confirmed fact.
- **B2 comparison / lost information:** B2 catches raised certainty and referents, but does not explicitly pin competitor source premise or object invariance.
- **Coverage P/M/C/E/G/N/S/U/V:** Y / Y / P / P / P / Y / Y / Y / -.
- **Source-light correction:** Add synthetic competitor-title input and rewritten title; assert same subject/object, preserved dispute status, HOLD_TITLE_PREMISE on certainty upgrade.
- **Execution:** DESIGN_ONLY; no software run.

### QA-017 — CONDITIONAL_MATCH
- **Original intended behavior:** Invented historical last words must not be presented as documentary quotation.
- **B2 comparison / lost information:** B2 generic fictional witness words preserve misquotation but lose last-words historical sensitivity and documentary fact framing.
- **Coverage P/M/C/E/G/N/S/U/V:** Y / Y / P / P / Y / Y / P / P / -.
- **Source-light correction:** Use fully invented last-words witness fixture; block direct quotation as archival certainty and require provenance.
- **Execution:** DESIGN_ONLY; no software run.

### QA-018 — CONDITIONAL_MATCH
- **Original intended behavior:** German translation must preserve allegedly/likely markers and uncertainty.
- **B2 comparison / lost information:** B2 detects removal of a possibility marker but omits German-language direction and source-to-translation review.
- **Coverage P/M/C/E/G/N/S/U/V:** Y / Y / P / P / P / Y / Y / Y / -.
- **Source-light correction:** Supply paired invented source/German target with allegedly/likely qualifier; return HOLD_REVIEW when nuance drops.
- **Execution:** DESIGN_ONLY; no software run.

### QA-019 — MATERIAL_GAP
- **Original intended behavior:** Mislabeling reconstructed testimony as authentic violates dignity and authenticity constraints.
- **B2 comparison / lost information:** B2 substitutes recovered footage for original archival testimony and focuses staged disclosure, losing human dignity review.
- **Coverage P/M/C/E/G/N/S/U/V:** P / Y / N / N / P / P / N / P / -.
- **Source-light correction:** Require a synthetic reenacted survivor testimony falsely attributed to archive; HOLD_HARM for false archival authenticity and dignity risk even if visually disclosed.
- **Execution:** DESIGN_ONLY; no software run.

### QA-020 — MATERIAL_GAP
- **Original intended behavior:** Synthetic disaster rescue video cannot be marketed as actual event footage.
- **B2 comparison / lost information:** B2 switches moving rescue video to still image; disclosure is retained but video-specific authenticity and harm gate are absent.
- **Coverage P/M/C/E/G/N/S/U/V:** P / Y / N / P / P / Y / P / P / -.
- **Source-light correction:** Use entirely fictional synthetic rescue video as a recorded-live claim; require HOLD_HARM and prominent synthetic disclosure before use.
- **Execution:** DESIGN_ONLY; no software run.

### QA-021 — CONDITIONAL_MATCH
- **Original intended behavior:** An early casualty estimate cannot be upgraded to confirmed final count.
- **B2 comparison / lost information:** B2 retains provisional/final distinction but lacks explicit HOLD_UNVERIFIED_FACT, timestamp/recheck and superseding source requirements.
- **Coverage P/M/C/E/G/N/S/U/V:** Y / Y / P / P / P / Y / Y / Y / P.
- **Source-light correction:** Record synthetic as_of and estimation stage; withhold final status until independently corroborated newer source, emit HOLD_UNVERIFIED_FACT.
- **Execution:** DESIGN_ONLY; no software run.

### QA-022 — MATERIAL_GAP
- **Original intended behavior:** Flood/climate mechanism cannot be declared proven single cause without suitable study.
- **B2 comparison / lost information:** B2 changes a flood mechanism to any fictional complex event, omitting domain-specific attribution and study threshold.
- **Coverage P/M/C/E/G/N/S/U/V:** P / Y / N / N / P / Y / P / P / -.
- **Source-light correction:** Use fictional flood and explicit multiple possible mechanisms; absent valid attribution study return HOLD_UNVERIFIED_FACT.
- **Execution:** DESIGN_ONLY; no software run.

### QA-023 — MATERIAL_GAP
- **Original intended behavior:** R163 synthetic-TTS measurement does not establish natural narrator WPM.
- **B2 comparison / lost information:** B2 generic artificial voice-to-natural-speech proof drops named R163 evidence and WPM unit, so a different extrapolation may pass.
- **Coverage P/M/C/E/G/N/S/U/V:** P / Y / N / N / P / P / P / P / -.
- **Source-light correction:** Use synthetic R163 TTS WPM figure and an attempted natural-voice WPM rule; block with HOLD_SOURCE_ROLE.
- **Execution:** DESIGN_ONLY; no software run.

### QA-024 — MATERIAL_GAP
- **Original intended behavior:** R079 course data cannot mandate universal 90-second hook.
- **B2 comparison / lost information:** B2 generic course-session technique vs video-story rule drops source identifier, quantitative 90-second mandate and required HOLD_SOURCE_ROLE.
- **Coverage P/M/C/E/G/N/S/U/V:** P / Y / N / N / P / P / P / P / -.
- **Source-light correction:** Use mock R079 course observation promoted to a compulsory 90-second YouTube opening; block universal rule with HOLD_SOURCE_ROLE.
- **Execution:** DESIGN_ONLY; no software run.

### QA-025 — SEMANTIC_MATCH
- **Original intended behavior:** Three-act story design is optional and must have counterexample.
- **B2 comparison / lost information:** B2 retains optional nature, counterexample and non-universal framing.
- **Coverage P/M/C/E/G/N/S/U/V:** Y / Y / Y / Y / Y / Y / Y / Y / -.
- **Source-light correction:** Optional: name OptionCard eligibility explicitly.
- **Execution:** DESIGN_ONLY; no software run.

### QA-026 — SEMANTIC_MATCH
- **Original intended behavior:** Author cannot act as sole independent fact reviewer.
- **B2 comparison / lost information:** B2 directly preserves writer/self-review separation and independent-check gate.
- **Coverage P/M/C/E/G/N/S/U/V:** Y / Y / Y / Y / Y / Y / Y / Y / -.
- **Source-light correction:** Optional: require HOLD_REVIEW token.
- **Execution:** DESIGN_ONLY; no software run.

### QA-027 — CONDITIONAL_MATCH
- **Original intended behavior:** Adjudication must not overwrite original reviewer records.
- **B2 comparison / lost information:** B2 catches deleting disagreements but not the distinct preserve-forms + append-adjudication record design.
- **Coverage P/M/C/E/G/N/S/U/V:** Y / Y / P / P / P / Y / Y / P / P.
- **Source-light correction:** Keep original independent reviewer forms immutable; record a separate adjudication and reject in-place edits.
- **Execution:** DESIGN_ONLY; no software run.

### QA-028 — CONDITIONAL_MATCH
- **Original intended behavior:** Severe unsupported claim blocks approval despite perfect style score.
- **B2 comparison / lost information:** B2 retains high-score-versus-severe-claim veto but omits explicit severity=3, 100/100 and HOLD_UNVERIFIED_FACT.
- **Coverage P/M/C/E/G/N/S/U/V:** Y / Y / P / P / P / Y / Y / Y / -.
- **Source-light correction:** Use synthetic style=100/100 and severity=3 unsupported factual claim; return HOLD_UNVERIFIED_FACT regardless of style.
- **Execution:** DESIGN_ONLY; no software run.

### QA-029 — CONDITIONAL_MATCH
- **Original intended behavior:** Unreadable source is NOT_ASSESSABLE, not score zero; gate remains HOLD.
- **B2 comparison / lost information:** B2 rejects a made-up score but does not directly contrast zero with unknown or explicitly retain blocking HOLD.
- **Coverage P/M/C/E/G/N/S/U/V:** Y / Y / P / P / P / Y / Y / Y / -.
- **Source-light correction:** Use unavailable-source score=0 failure and required NOT_ASSESSABLE + HOLD until original accessible.
- **Execution:** DESIGN_ONLY; no software run.

### QA-030 — MATERIAL_GAP
- **Original intended behavior:** Subtitle timing cannot certify narrator pauses without audio.
- **B2 comparison / lost information:** B2 asks about general vocal expressiveness, which is not the original pause-specific media leap; the negative proposition changed.
- **Coverage P/M/C/E/G/N/S/U/V:** P / Y / N / N / P / P / P / P / -.
- **Source-light correction:** Use synthetic timed subtitle intervals and claim of exact recorded pauses; reject pause inference absent actual audio evidence.
- **Execution:** DESIGN_ONLY; no software run.

### QA-031 — MATERIAL_GAP
- **Original intended behavior:** A color-only map and inaccurate auto-captions fail meaningful accessibility.
- **B2 comparison / lost information:** B2 changes geographic color-only map to generic chart and uncorrected auto-captions to unchecked synthetic captions; map legend geography and spoken meaning are lost.
- **Coverage P/M/C/E/G/N/S/U/V:** P / Y / N / N / P / P / P / P / P.
- **Source-light correction:** Use invented geographic map needing text/pattern labels plus auto-caption transcription error changing meaning; HOLD_REVIEW until both are corrected.
- **Execution:** DESIGN_ONLY; no software run.

### QA-032 — CONDITIONAL_MATCH
- **Original intended behavior:** CTR and start counts must not be substituted for retention improvement.
- **B2 comparison / lost information:** B2 tests only CTR, excluding start count and definition of retention.
- **Coverage P/M/C/E/G/N/S/U/V:** Y / Y / P / P / Y / P / Y / Y / -.
- **Source-light correction:** Use two synthetic metric substitutions: CTR and video start counts; reject either as retention improvement.
- **Execution:** DESIGN_ONLY; no software run.

### QA-033 — MATERIAL_GAP
- **Original intended behavior:** Unexecuted T12 protocol cannot be described as successful randomized trial.
- **B2 comparison / lost information:** B2 generic incomplete experiment validation loses T12 specificity, RCT status and HOLD_NOT_APPROVED.
- **Coverage P/M/C/E/G/N/S/U/V:** P / Y / N / N / P / Y / P / P / -.
- **Source-light correction:** Use synthetic T12 plan with no participants/randomization/outcomes, a claimed successful RCT and HOLD_NOT_APPROVED.
- **Execution:** DESIGN_ONLY; no software run.

### QA-034 — CONDITIONAL_MATCH
- **Original intended behavior:** Agency correction after draft invalidates linked downstream signoffs.
- **B2 comparison / lost information:** B2 changes a warning correction to generic agency-record change; invalidation of linked signoffs is mostly retained.
- **Coverage P/M/C/E/G/N/S/U/V:** Y / Y / P / P / Y / Y / Y / Y / P.
- **Source-light correction:** Use versioned synthetic original warning and corrected edition, record dependency graph and revoke every linked downstream signoff until re-review.
- **Execution:** DESIGN_ONLY; no software run.

### QA-035 — MATERIAL_GAP
- **Original intended behavior:** Production release without G18 authorization must be held irrespective of quality.
- **B2 comparison / lost information:** B2 generic release gate blocks publication but omits identity of G18 signoff, distinction between user request and authorized approver, and HOLD_NOT_APPROVED token.
- **Coverage P/M/C/E/G/N/S/U/V:** P / Y / N / P / P / Y / N / P / P.
- **Source-light correction:** Use synthetic quality-passing draft with G18 absent; return HOLD_NOT_APPROVED even if user requests production; never infer AP-01/AP-02 authorization.
- **Execution:** DESIGN_ONLY; no software run.

### QA-036 — CONDITIONAL_MATCH
- **Original intended behavior:** A licence to read does not grant permission to publicly redistribute source bytes.
- **B2 comparison / lost information:** B2 correctly distinguishes read and redistribution, but 'internal review' must remain permission-scoped, and public redistribution beyond simple byte export needs explicit denial.
- **Coverage P/M/C/E/G/N/S/U/V:** Y / Y / P / P / P / Y / Y / P / P.
- **Source-light correction:** Require separately documented permission per use; allow only authorized private reading, prohibit all public source-byte redistribution and record HOLD_RIGHTS if reuse rights unknown.
- **Execution:** DESIGN_ONLY; no software run.

## Cross-cutting concerns

1. **Gate token regression:** B2 frequently preserves an English blocking notion but loses typed statuses such as HOLD_RIGHTS, HOLD_SOURCE_ROLE, HOLD_UNVERIFIED_FACT, HOLD_HARM, HOLD_REVIEW, HOLD_NOT_APPROVED and NOT_ASSESSABLE. The amendment proposes matching gate semantics without importing source text.
2. **Synthetic fixtures must still constrain source roles:** F-190, R052, R163, R079, B70-B72 and T12 are metadata/limitation identifiers, **not** licenses to import restricted upstream bytes. Synthetic values and fabricated events only.
3. **Historical review proof:** QA-002 must distinguish access_state, retrieval time and independent reviewed_at. QA-034 should invalidates dependent reviews after an evidence version change; all other timing/version fields marked partial or not explicit as applicable.
4. **Safety is not optional:** Video/still distinctions, map meaning, caption transcription fidelity and G18 production hold cannot be generalized away.
5. **Alternative interpretations:** B2 may intentionally abstract domain-specific inputs to avoid source contamination. That explains some language changes but does not remove the need for traceable behavior; strict classification treats lost negative test conditions as gaps. Conversely, adding identifiers in a mock requirement is *not* authorization to copy their underlying contents.

## Scope and limitations

- Purely documentary static comparison of two pinned CSVs; no real test fixtures were generated, executed, or validated against software.
- No repository originals, PR #12, branch `main`, production SKILL or Claude file transfer are changed by this work.
- Reviewer is not rights custodian or project owner. Pending independent provenance/copyright screen and owner choices remain separate.
- Amendments are unsigned candidate text for future authorized spec work, **not changes to canonical B2**.
