# Proposed v0.1 → v0.2 Changelog and Compatibility
**Decision: PROPOSED — OWNER REVIEW PENDING**. Historical baselines remain unchanged: `ARCH-DESIGN-v0.1`, `USW-IFACE/0.1`, Task2 frozen 0.1, F07–F10/F12, original 48-K/G19 registers and QA36 fixture file.

## Seven proposed changes
| ID | Behavior change | External compatibility |
|---|---|---|
| WB-C01 | USW-IFACE/0.2 defines alias(N-0x)=N0x for x=1..5, bijective and immutable; alias is not a new adapter or a historic ID rewrite. | Documentation alias catalog; parser interface ONLY if implemented later. |
| WB-C02 | Keep native_reason_codes[] verbatim; attach versioned canonical_group; many-to-one mapping MAY group missing-source aliases; multiple native reasons retained; an original HOLD never becomes PASS. | New crosswalk output field; no canonical source changes. |
| WB-C03 | SourceRecord.source_hash_if_verified is proposed canonical field; hash_if_verified remains a deprecated prose alias, not independent evidence. Null+hash_method if not actually verified. | Interface name clarification and versioned alias migration; original unchanged. |
| WB-C04 | retrieved_at is source fetch timestamp; reviewed_at is EvidenceLink (or GateDecision) assessment timestamp. Missing SourceRecord.access_state or required EvidenceLink.reviewed_at => HOLD; a retrieved_at value cannot replace reviewed_at. | Trace/validation rule, may affect future validator; original QA untouched. |
| WB-C05 | In mock v0.2 WAIVED_BY_NAMED_OWNER cannot override P1/P2/P3/P4/P5/P6/P7/P8/P10 for critical source, rights, factuality, harm, safety, privacy, authorization and publication checks. No critical bypass including under owner selection. | Normative gate semantics refinement; mock-state interface constraints. |
| WB-C06 | Prototype transition to RELEASED, PRODUCTION_APPROVED or export/publish is unreachable. All drafts RESEARCH_ONLY_NOT_PUBLISHABLE; production_allowed=false always, even QA36 pass, signed AP-00 or synthetic QA. | Explicit state-machine guard and release decision interface. |
| WB-C07 | Private non-export review is a separate access-only activity if authorized; public byte export without redistribution rights yields HOLD_RIGHTS, while QA-036 original expected phrase is preserved. | QA mapping/rights policy documentation; reason emitted by later runner. |

## Contract impact detail
- **Compatible documentation:** 11 module boundaries, five niches, A00–A10 IDs, P0–P10 gates, original 36 fixture IDs/wording, rights split, claim_verdict states, evidence roles, immutable originals.
- **Additive candidate metadata:** adapter_alias, native_reason_codes[]/canonical_group, explicit timestamp field interpretation, waiver policy and research-only terminal states are proposed; any physical schema migration in a later approved build needs separate technical design review and explicit `schema_version=0.2`.
- **Potential breaking expectations:** a legacy consumer accepting any generic waiver, equating retrieval with review, treating `RELEASED` as active, or exporting source under read-only rights must fail safe under proposed 0.2. That is an intended *planning* safety guard, not evidence of an implemented break.
- **No silently rewritten fixtures:** QA-002 original `SourceRecord without access_state or review time` and QA-036 original `private review only; no source bytes` remain exactly in canonical F12; candidate mapping only.
- **No owner approvals:** 36 bounded K entries descriptive, nine owner-pending (K007/K027/K028/K032/K033/K034/K039/K043/K045), three quarantined K029–K031. Historic verdicts and scientific cautions untouched.

## Migration proposal if and only if implementation later authorized
Read original data read-only, add explicit v0.2 interpretation layer, record an append-only change map and reviewer signature; preserve original field names and source SHA in lineage; reject unknown aliases; test negative mappings before code passes. Do not allow code generation, Claude import or actual source transfer by accepting this migration proposal.

## Source evidence
F07 `803f2d87969f1610d742110b8287ef3f31667434`; F08 `cfbd1340f747ff658e67b9e88bd956c472ad4165`; F09 `04c208fda0872ada977d2406d299f54c318a0e32`; F10 `33618d7e1905c4fa71730fe46fca17b9883f9cde`; F12 `88e89ee233c967c5b8a0b645b0d401f6c1d2ccea`; original Task2 `591dabfd1ee026bbe31fd086c152f4824f32a577`; Worker B `9732e17be66e1bfce7ab76e0ec23ed2be2a4d739`.
