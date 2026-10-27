# Exact Prototype Modules — Proposed Design Only

**Not implemented. Owner AP-01 and AP-02 are both absent.** Derived from the 2026-10-27 accepted research architecture `ARCH-DESIGN-v0.1` and interfaces `USW-IFACE/0.1`. Preserve historical M01–M09 boundaries; A00–A10 are finer implementation proposals and are NOT an approved replacement.

| ID | Module | Mock inputs and outputs | Planned purpose | Expected future negative case |
|---|---|---|---|---|
| A00 | Intake & scope router | IntakeEnvelope → ContextProfile | Niche, as-of date, ownership, exact topic and task declared | Missing required high-stakes context -> HOLD_SCOPE |
| A01 | Provenance & rights registry | SourceRecord[] → SourceLedger | Independent access and redistribution rights, versioned source identity | Readable but non-transferable source -> HOLD_RIGHTS |
| A02 | Evidence eligibility/conflicts | SourceLedger → EvidenceDisposition | Block F-190/R052 use as positive proof; preserve immutable historical labels | UNVERIFIED promoted as SUPPORTED -> HOLD_SOURCE_ROLE |
| A03 | Context/policy resolver | ContextProfile → PolicySet | Choose niche and strongest cross-niche hazard/safety policy | Weather+synthetic scene missing provenance -> HOLD |
| A04 | Atomic claim laboratory | Synthetic TopicBrief → AtomicClaim[] | Time, numerical, quote and causal atoms; NOT_CHECKABLE first class | Invented nonfiction quotation -> HOLD_UNVERIFIED_FACT |
| A05 | Creative options registry | TopicLock+ClaimLedger → OptionCards | Optional outline structures, examples/counterexamples, no efficacy promise | One optimal hook-second law -> reject |
| A06 | Topic/title and outline lock | Subject/object/qualifiers → TopicLock+Outline | Subject/object and disputed certainty never strengthened | Alleged converted to confirmed -> HOLD_TITLE_PREMISE |
| A07 | Draft assembly | Mock Outline+Claims → DraftSpan[] | Synthetic illustrative script text fully linked to claim IDs | Untraceable factual-style assertion -> HOLD |
| A08 | Independent QA design | Mock Draft+Reviewers → ReviewPacket | Separate author from independent reviewer; append-only adjudication | Self-QA called independent -> HOLD_REVIEW |
| A09 | Testing/analytics registry | Synthetic metrics → EvaluationRecord | Separate observed stats, editorial score, experiments and causal inference | Unrun T12 called successful -> HOLD_NOT_APPROVED |
| A10 | Release checkpoint | RunBundle+unsigned G register → ReleaseDecision | Mock-only state, no production or transfer bypass | Missing owner signature -> HOLD_NOT_APPROVED |
| N01 | USA Weather | Mock dated official-alert semantics → Overlay | Watch/warning/advisory; location, time and uncertainty clarity | Expired warning presented current -> HOLD_STALE_FORECAST |
| N02 | Military/Aviation | Mock procurement/conflict → Overlay | Contract vs prototype vs testing vs operational; claimant attribution | Contract equals fielded -> HOLD_UNVERIFIED_FACT |
| N03 | German WWII/WWI History | Mock archival text → Overlay | Date, original quote, translation qualifiers and human dignity | Invented last words -> HOLD_UNVERIFIED_FACT |
| N04 | Disaster Documentary | Mock incident description → Overlay | Evolving casualties, climate mechanism caution, synthetic media labels | Generated footage called authentic -> HOLD_HARM |
| N05 | General Long Form | Mock explainer → Overlay | Audience intent and optional narrative; no universal retention law | MOOC/video association promoted to YouTube causality -> HOLD_SOURCE_ROLE |

## Exact data interfaces proposed

`IntakeEnvelope`, `ContextProfile`, `SourceRecord`, `EvidenceLink`, `AtomicClaim`, `TopicLock`, `OptionCard`, `Outline`, `DraftSpan`, semantic-only `VisualSpan`, `GateDecision`, `ReviewPacket`, `RunBundle`, `ReleaseDecision`.

Mandatory design properties: versioned immutable record identifiers, source time/version and reference, access versus redistribution rights, factual state `SUPPORTED | SUPPORTED_WITH_QUALIFICATION | UNSUPPORTED | CONTRADICTED | NOT_CHECKABLE`, topic subject/object and epistemic qualifiers, separate reviewer identity, explicit gate/exception log, and invalidation of downstream approval on source changes. Historical S/F/R/K/V/EDU names/IDs never renumbered.

Proposed `P0–P10` safety chain preserves strict scope, provenance, rights, claim checking, topic invariance, independent QA and publication-signature gates. Every future synthetic software fixture must produce deterministic HOLD/REJECT outcomes where expected. A pass in this prototype can NEVER be a production release decision, scientific proof or permission to copy third-party originals.

**Stage state now:** all modules are specified as DRAFT; code count = 0; fixtures run = 0. First mock V0 may generate illustrative synthetic drafts but must label them `RESEARCH_ONLY_NOT_PUBLISHABLE`.
