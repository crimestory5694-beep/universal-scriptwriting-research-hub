# Worker A — Proposed v0.2 Gaps, Assumptions and Counterexamples
2026-10-27 | STATIC DOCUMENT REVIEW | NOT AN EXECUTABLE TEST

## GAP-01: Cyclic TopicLock construction — HIGH / REVISION_REQUIRED
Observation: F07 A05 uses TopicLock and ClaimLedger to create OptionSet; F07/v0.2 A06 uses OptionSet to create TopicLock and Outline. That is a producer/consumer cycle unless a preliminary immutable referent contract exists. v0.2 uses the same TopicLock name in both positions.
Proposed fix: A00 creates an initial immutable TopicBoundary containing verbatim user subject/object/qualifiers. A05 reads TopicBoundary, not the later final lock. A06 finalizes TopicLock with explicit provenance and comparison to TopicBoundary; no certainty amplification.
Negative test (DESIGN_ONLY): user 'alleged drone strike on radar'; option proposes confirmed destroyed airbase; must HOLD_TITLE_PREMISE before any outline/draft.
Remaining: owner editorial boundary approval; technical reviewer chooses typed contract, stage naming and invalidation graph. No actual test run.

## GAP-02: PolicySet propagation — HIGH / REVISION_REQUIRED
Observation: Original F07 A07 Draft input contains PolicySet, whereas v0.2 A07 signature omits it. A03 produces PolicySet. Narrative description alone is not a sufficient typed handoff.
Proposed fix: explicit A07 input Outline + ClaimLedger + PolicySet (pinned revision) + applicable TopicLock; ReviewPacket should preserve policy version and overlay decisions. Never downgrade union-of-restrictions.
Negative test (DESIGN_ONLY): N01 weather + synthetic media overlay is dropped at A07; draft omits disclosure and falsely claims current warning -> HOLD_HARM/HOLD_STALE_FORECAST.
Remaining: architecture reviewer signs interface map; negative fixture execution only after AP-01.

## GAP-03: Critical waiver scope incompleteness — HIGH / REVISION_REQUIRED
Observation: proposed C05 enumerates P1/P2/P3/P4/P5/P6/P7/P8/P10, omitting P0 (scope and user authorization) and P9 (experiment consent/preregistration). F10 requires explicit P0/P9 HOLDs.
Proposed fix: Non-waivable status must attach to every applicable critical rule across P0-P10. In particular, missing scope authority, participant consent, rights, privacy, veracity, urgent hazard and public release permission cannot be waived by editorial owner. Optional style changes cannot clear upstream HOLD.
Negative test (DESIGN_ONLY): named owner asks to bypass unapproved participant experiment or absent scope -> HOLD_NOT_APPROVED/HOLD_SCOPE.
Remaining: owner, subject safety, legal/rights and research ethics authorities; approvals cannot be inferred from this review.

## GAP-04: HOLD reason-code catalog — MODERATE / REVISION_REQUIRED
Observation: The candidate adds native_reason_codes[] plus canonical_group without an exhaustive documented crosswalk for all native F07/F10 codes or multi-error ordering.
Proposed fix: A separate versioned table with source filename/sha, full native literal, optional category, precedence for presentation only, unknown->HOLD_UNKNOWN_REASON. Round-tripping must preserve source literal and all simultaneous native reasons.
Negative test (DESIGN_ONLY): HOLD_RIGHTS and HOLD_SOURCE_ROLE jointly present; grouped UI shows one category but machine/log still has both; never PASS.
Remaining: technical contract owner; external consumer contract review.

## GAP-05: Hash and timestamp precision — MODERATE / REVISION_REQUIRED
Observation: F08 prose/field alias and QA-002 are ambiguous. `source_hash_method` is an algorithm label, not proof bytes were hashed. `retrieved_at` does not attest independent assessment.
Proposed fix: explicit nullable digest, method, actual-byte verification evidence and legacy field alias rules; EvidenceLink reviewer/time required where a factual verification claim is made.
Negative test (DESIGN_ONLY): `hash_if_verified` supplied by a user without access to original bytes, plus retrieval timestamp only -> NOT_CHECKABLE/HOLD.
Remaining: independent QA fixture author, schema designer and source reviewer.

## GAP-06: A09 study approval handoff — MODERATE / REVISION_REQUIRED
Observation: F07 original A09 takes ReviewPacket + StudyApproval; v0.2 A09 table omits StudyApproval. This could obscure required separate consent and protocol approval even in a conceptual interface.
Proposed fix: explicitly forbid execution of any human/scientific protocol (T01-T13) under current scope. Future A09 experiment path requires independent StudyApproval or HOLD_NOT_APPROVED, rather than treating ReviewPacket as permission.
Negative test (DESIGN_ONLY): a style metric or synthetic QA result is presented as a successful randomized trial -> HOLD_NOT_APPROVED; QA-032/033.
Remaining: research ethics, qualified scientific reviewer, separate owner authorization.

## Static compatibility boundary and assumptions
Assumption A1: The observed main and pinned branch content are trustworthy for text comparison, not legal source authenticity; hashes establish bytes only.
Assumption A2: Proposed v0.2 is documentation; words such as must/cannot describe intent, not running protection.
Assumption A3: QA36 is the 36-row original matrix at blob 88e89ee233c967c5b8a0b645b0d401f6c1d2ccea; no QA fixture was run or modified.
Assumption A4: Existing K001-K048 statuses remain 36 bounded-descriptive, nine owner-pending amendments, K029-031 quarantined; no viewer effect claims.
Assumption A5: Draft PR10/11/12 are competing research inputs, not merged or owner approved.
Assumption A6: Actual file rights, source-excerpt scope, third-party licensing, privacy, paid tool use, Claude export and production are outside Worker A competence/authorization.

## Safeguard checklist
- PASS (static): A00-A10 eleven; N01-N05 five; P0-P10 eleven; provenance revisions; separate access/redistribution; subject/object and uncertainty; 36 QA source IDs unchanged; synthetic-only label stated.
- CONDITIONAL: input/output reachability and policy propagation; precise reason-code map; QA-002 field-level binding; future schema and negative tests.
- HOLD: AP-00 owner decision; AP-01 build; AP-02 per-file rights and Claude transfer; AP-03 research; AP-04 production SKILL.md; code QA and T01-T13.

Sources: main@0776afd52001c2d9021b1749f7b936bc1dc4e37d original F07 803f2d87969f1610d742110b8287ef3f31667434, F08 cfbd1340f747ff658e67b9e88bd956c472ad4165, F09 04c208fda0872ada977d2406d299f54c318a0e32, F10 33618d7e1905c4fa71730fe46fca17b9883f9cde, QA 88e89ee233c967c5b8a0b645b0d401f6c1d2ccea; proposed v0.2@9ed29940cc435520ae64e12df95d8823a8e7fc41 blob d4b4a19f67772d4588b2ea7c3cd15b0b74e600fb.
