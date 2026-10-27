# Worker F — Gaps and proposed corrections

**Decision:** B2 cannot be accepted as fully semantically equivalent to original F12 without amendments. 13 material gaps, 18 conditional matches, 5 semantic matches; zero executed tests.

## Material gaps requiring re-review

- **QA-002:** B2 covers an access label plus missing assessment date; it does not exercise missing access_state and could confuse access/retrieval timestamp with independent review timestamp. HOLD missing identity is not explicit. **Fix:** Add two separate missing-field fixtures; store accessed_at/retrieved_at distinct from reviewed_at and require explicit HOLD_MISSING_IDENTITY and verification=UNKNOWN.
- **QA-007:** B2 changes precise lost archive/surrogate distinction into generic unavailable original and an independently summarized substitute, erasing the historic exception. **Fix:** Retain B70-B72 as identifiers only; use invented missing exact member plus surrogate cumulative ledger and require HOLD_ORIGINAL_MISSING without promotion.
- **QA-008:** B2 substitutes a generic unverified research finding and omits the explicit quarantined identifier and role block. **Fix:** Introduce synthetic metadata row with identifier F-190 and quarantined source_role; any promotion to positive evidence must give HOLD_SOURCE_ROLE.
- **QA-009:** B2 uses an index pointing to an unread study, partly matching noninspection but drops blocked R052 provenance and its source-role restriction. **Fix:** Use synthetic R052 blocked/read_status metadata; disallow independently_read_original claim and return HOLD_SOURCE_ROLE.
- **QA-019:** B2 substitutes recovered footage for original archival testimony and focuses staged disclosure, losing human dignity review. **Fix:** Require a synthetic reenacted survivor testimony falsely attributed to archive; HOLD_HARM for false archival authenticity and dignity risk even if visually disclosed.
- **QA-020:** B2 switches moving rescue video to still image; disclosure is retained but video-specific authenticity and harm gate are absent. **Fix:** Use entirely fictional synthetic rescue video as a recorded-live claim; require HOLD_HARM and prominent synthetic disclosure before use.
- **QA-022:** B2 changes a flood mechanism to any fictional complex event, omitting domain-specific attribution and study threshold. **Fix:** Use fictional flood and explicit multiple possible mechanisms; absent valid attribution study return HOLD_UNVERIFIED_FACT.
- **QA-023:** B2 generic artificial voice-to-natural-speech proof drops named R163 evidence and WPM unit, so a different extrapolation may pass. **Fix:** Use synthetic R163 TTS WPM figure and an attempted natural-voice WPM rule; block with HOLD_SOURCE_ROLE.
- **QA-024:** B2 generic course-session technique vs video-story rule drops source identifier, quantitative 90-second mandate and required HOLD_SOURCE_ROLE. **Fix:** Use mock R079 course observation promoted to a compulsory 90-second YouTube opening; block universal rule with HOLD_SOURCE_ROLE.
- **QA-030:** B2 asks about general vocal expressiveness, which is not the original pause-specific media leap; the negative proposition changed. **Fix:** Use synthetic timed subtitle intervals and claim of exact recorded pauses; reject pause inference absent actual audio evidence.
- **QA-031:** B2 changes geographic color-only map to generic chart and uncorrected auto-captions to unchecked synthetic captions; map legend geography and spoken meaning are lost. **Fix:** Use invented geographic map needing text/pattern labels plus auto-caption transcription error changing meaning; HOLD_REVIEW until both are corrected.
- **QA-033:** B2 generic incomplete experiment validation loses T12 specificity, RCT status and HOLD_NOT_APPROVED. **Fix:** Use synthetic T12 plan with no participants/randomization/outcomes, a claimed successful RCT and HOLD_NOT_APPROVED.
- **QA-035:** B2 generic release gate blocks publication but omits identity of G18 signoff, distinction between user request and authorized approver, and HOLD_NOT_APPROVED token. **Fix:** Use synthetic quality-passing draft with G18 absent; return HOLD_NOT_APPROVED even if user requests production; never infer AP-01/AP-02 authorization.

## Conditional matches requiring explicit closure

- **QA-001:** B2 asks for separation and source non-edits but does not explicitly assert main unchanged or constrain every output to the reserved worker path. **Fix:** Add a synthetic diff fixture proving main remains unchanged and all newly created paths stay inside the designated folder.
- **QA-003:** B2 uses an invented protected historical identifier, but omits namespace coverage and the append-relation-only repair behavior. **Fix:** Exercise each protected namespace and require reject-rekey plus append-only linked relation while preserving the original ID.
- **QA-004:** B2 external script paragraphs express the general protection, but do not cover transcript-length/public-output boundary explicitly. **Fix:** Include synthetic public/export boundary, substantial transcript fixture, rejection, and recorded rights-risk reason; use wholly invented text.
- **QA-005:** B2 covers a viewable mock with blank permission, but its expected handling does not name HOLD_RIGHTS or all forms of reuse. **Fix:** Keep readable/source-access state distinct from rights state; return HOLD_RIGHTS on attempted public reuse/copy/export.
- **QA-006:** B2 covers synthetic disagreement with manifest, but drops exact nine-member scope and explicit prohibition against rewriting historic evidence. **Fix:** Use nine synthetic disagreement records, preserve originals immutably and emit HOLD_DISPUTED_PROVENANCE; no hash repair by rewriting.
- **QA-010:** B2 says a guaranteed audience effect, preserving causal skepticism but omitting the 90% retention metric and unverified creator-provided basis. **Fix:** Use synthetic unsupported 90% retention improvement claim and require attribution-only labeling, never scientific validation.
- **QA-013:** B2 preserves historical-only review but does not require a traceable issue date and source link. **Fix:** Attach synthetic archived bulletin issue_date and immutable locator; allow editorial review only when correctly dated and linked.
- **QA-014:** B2 preserves contract-versus-deployment, but lacks engine-stage granularity and explicit HOLD_UNVERIFIED_FACT. **Fix:** Specify synthetic engine-only award versus fielded fleet and require stage claim HOLD_UNVERIFIED_FACT.
- **QA-016:** B2 catches raised certainty and referents, but does not explicitly pin competitor source premise or object invariance. **Fix:** Add synthetic competitor-title input and rewritten title; assert same subject/object, preserved dispute status, HOLD_TITLE_PREMISE on certainty upgrade.
- **QA-017:** B2 generic fictional witness words preserve misquotation but lose last-words historical sensitivity and documentary fact framing. **Fix:** Use fully invented last-words witness fixture; block direct quotation as archival certainty and require provenance.
- **QA-018:** B2 detects removal of a possibility marker but omits German-language direction and source-to-translation review. **Fix:** Supply paired invented source/German target with allegedly/likely qualifier; return HOLD_REVIEW when nuance drops.
- **QA-021:** B2 retains provisional/final distinction but lacks explicit HOLD_UNVERIFIED_FACT, timestamp/recheck and superseding source requirements. **Fix:** Record synthetic as_of and estimation stage; withhold final status until independently corroborated newer source, emit HOLD_UNVERIFIED_FACT.
- **QA-027:** B2 catches deleting disagreements but not the distinct preserve-forms + append-adjudication record design. **Fix:** Keep original independent reviewer forms immutable; record a separate adjudication and reject in-place edits.
- **QA-028:** B2 retains high-score-versus-severe-claim veto but omits explicit severity=3, 100/100 and HOLD_UNVERIFIED_FACT. **Fix:** Use synthetic style=100/100 and severity=3 unsupported factual claim; return HOLD_UNVERIFIED_FACT regardless of style.
- **QA-029:** B2 rejects a made-up score but does not directly contrast zero with unknown or explicitly retain blocking HOLD. **Fix:** Use unavailable-source score=0 failure and required NOT_ASSESSABLE + HOLD until original accessible.
- **QA-032:** B2 tests only CTR, excluding start count and definition of retention. **Fix:** Use two synthetic metric substitutions: CTR and video start counts; reject either as retention improvement.
- **QA-034:** B2 changes a warning correction to generic agency-record change; invalidation of linked signoffs is mostly retained. **Fix:** Use versioned synthetic original warning and corrected edition, record dependency graph and revoke every linked downstream signoff until re-review.
- **QA-036:** B2 correctly distinguishes read and redistribution, but 'internal review' must remain permission-scoped, and public redistribution beyond simple byte export needs explicit denial. **Fix:** Require separately documented permission per use; allow only authorized private reading, prohibit all public source-byte redistribution and record HOLD_RIGHTS if reuse rights unknown.

## Semantically preserved cases

- **QA-011:** Outdated warning must never be presented as live warning.
- **QA-012:** Model output is not a warning formally issued by an agency.
- **QA-015:** One-party battlefield allegation cannot be asserted as established fact.
- **QA-025:** Three-act story design is optional and must have counterexample.
- **QA-026:** Author cannot act as sole independent fact reviewer.

## High-priority resolution order

1. **QA-035 + QA-036:** Explicit G18 denial; never conflate reading access, reuse rights, public redistribution and release authorization.
2. **QA-002 + QA-034:** Require independent review time and evidence-version dependency invalidation; distinguish retrieval/access timestamps.
3. **QA-031 + QA-019 + QA-020:** Restore meaning-critical caption/map/testimony/video conditions and separate synthetic disclosure from harm checks.
4. **QA-007..009 + QA-023..024 + QA-033:** Preserve exact disputed and limited source roles as identifiers-only metadata, with typed holds.
5. **QA-022 + QA-030:** Restore discipline-specific climate attribution study condition and measured narrator pause condition.

## Acceptance checklist before any future B2 adoption

- 36 unique IDs in replacement matrix; source-light invented content only; no original restricted bytes.
- All 13 material gaps restored and all 18 conditional items reviewed by independent QA; choose retain/or explicitly document accepted divergence.
- Expected typed HOLD/PASS/NOT_ASSESSABLE statuses must be unambiguous, with adverse-case observable behavior.
- Rights custodian and owner authorizations are separate; **AP-01/AP-02/G18 remain HOLD**.
- Future software QA execution must be a separately authorized activity; this file reports **zero** executions.
