# Admission gates, evidence control and QA specification

**Status:** proposed gates for future implementation; design QA is not evidence that they were executed as production checks. These requirements preserve S4 source/approval HOLDs and historical T01–T13 NOT_EXECUTED.

## 1. Gate chain (fail closed for consequential nonfiction)
| Gate | Check / acceptance | HOLD or rejection |
|---|---|---|
| P0 `SCOPE` | Niche, subniche, intended claim type, audience, target as-of time, user permissions and task mode explicitly declared | `HOLD_SCOPE` |
| P1 `RIGHTS` | Access rights, internal analysis rights, redistribution rights, likeness/consent and protected content separately recorded | `HOLD_RIGHTS`; no public bytes |
| P2 `IDENTITY` | Preserved S/F/R/V/K/EDU IDs; source version/hash only if actually verified; inaccessible original labelled | `HOLD_ORIGINAL_MISSING` or `HOLD_DISPUTED_PROVENANCE` |
| P3 `ADMISSIBILITY` | Qualify the *role* of each source; prohibit positive promotion of failed/unverified F, blocked original, creator assertions or caption-only inferences | `HOLD_SOURCE_ROLE` |
| P4 `CLAIMS` | Material assertions atomized; numeric/quote/date/geography/causal source link; independent corroboration as appropriate; preserve contradiction | `HOLD_UNVERIFIED_FACT` or `REJECT_CONTRADICTED` |
| P5 `TIME` | Current forecasts, active conflict and incident updates checked against source issue/validity/publication and audience local clocks | `HOLD_STALE_FORECAST` / `HOLD_NEEDS_RECHECK` |
| P6 `TOPIC` | Exact title / subject / object invariant; factual certainty and scope unchanged through creative formatting | `HOLD_TITLE_PREMISE` |
| P7 `NARRATIVE` | Only context-applicable and disclosed hypotheses offered; creative structure never delays safety info or invents nonfiction | `HOLD_HARM` / `HOLD_SOURCE_ROLE` |
| P8 `INDEPENDENT_QA` | Immutable reviewer forms, critical-claim coverage, local language, alt/captions, synthetic disclosures, subject dignity, adjudication | `HOLD_REVIEW` |
| P9 `EXPERIMENT` | Distinguish editorial score from human comprehension from causal retention; preregistration + consent + access required independently | `HOLD_NOT_APPROVED` |
| P10 `PUBLICATION` | Audit hashes, selected source revisions, exception ledger, rights-approved public export, final owner signoff, separate code QA | `HOLD_NOT_APPROVED` |

**Critical non-negotiables:** source fabrication, knowingly false safety instructions, privacy breach, unsupported active warning, synthetic media deceptively passed off as source footage, unverified documentary quote asserted as exact, or unauthorized source-rich export must block publication regardless of style or owner waiver. A `PASS_FOR_DESIGN` does not mean P10 passed.

## 2. Source grading and admissible inference
Store orthogonal fields, not a single magic “verified” scalar:

`access_depth` = `FULL_READ | PARTIAL | INDEX_ONLY | BLOCKED | MISSING`;
`source_role` = `original_evidence | official_guidance | professional_standard | descriptive_example | educational_creator_claim | analogy | research_hypothesis`;
`evidence_status` = `SUPPORTED | SUPPORTED_WITH_QUALIFICATION | UNSUPPORTED | CONTRADICTED | NOT_CHECKABLE`;
`source_independence` = same-family, corroborating-independent, conflict, unknown;
`research_effect_status` = `not_tested | observational_association | controlled_context_limited | validated_for_declared_population` (last value never auto-assigned);
`public_rights` = original_analyst_safe, licensed_for_redistribution, private_only, unclear_hold.

S2/S3/S4 have research classifications but **none of 48 K is owner-approved production guidance**. Historical F PASS means specific source audit closure only; it is not proof of retention. R079 counts ~6.9m *sessions* (not viewers) in MOOCs; R163 health readability / default Azure TTS with allocation uncertainty is not a YouTube script-style experiment. R052 source remains inaccessible; F-190 UNVERIFIED. Caption V01–V12 cannot establish prosody, exact pauses or viewer effects. All source scopes and conflicts survive the transformation into guidance.

## 3. Atomic factuality review
For each draft case, every severity-3 and all high-impact material claims must be explicitly reviewed. Proposed historical T02 pilot design suggests all critical plus up to 20 ordinarily material sampled assertions/case; **this is only a study proposal, not a production coverage limit**. Each atom records proposition, quote/number/time, contemporaneous locator, evidence state, severity 0–3, reason, reviewer, revision and resolution. Missing evidence yields `NOT_CHECKABLE`; false explicit statement yields `CONTRADICTED`. A quote needs original exact text or `unverified_quote` removed/rephrased. Every correction records downstream scope (title, description, VO, image). Contradictions remain on the ledger after editing.

Sensible design hard block: any unresolved severity-3 factual or ethics error. The historical T02 ≥95% ordinary sample support and editorial ≥75/100 style screen are **proposed study thresholds**; neither should be silently installed as an approved production pass rate. The four categorical rubrics are ordinal expert judgments; missing dimensions → `NOT_ASSESSABLE` rather than a manufactured total. Never convert style points into retention uplift percentages.

## 4. Independent QA lane definitions
- `FACT_REVIEWER`: primary evidence, dates, numbers, source provenance, contradictory interpretations. Separate reviewer freeze before adjudication.
- `DOMAIN_REVIEWER`: weather agency/local hazard knowledge, aircraft phase/variant, historian/archivist, disaster incident, psychology/science/economics as relevant.
- `LANGUAGE_REVIEWER`: German-native idiom/register and meaning-preserving translation where needed; English spoken syntactic clarity as text desk check.
- `ACCESSIBILITY_REVIEWER`: correct captions and meaningful non-speech audio; alt explanation for essential maps/visuals; color-only references avoided; actual recorded audio/voice assessed only if available.
- `RIGHTS_AND_HARM_REVIEWER`: licensing, third-party excerpts, privacy, consent, synthetic likeness/event depiction and disclosure.
- `EDITORIAL_REVIEWER`: structure coherence, payoff honesty, audience relevance; cannot override an evidence gate.
- `ADJUDICATOR`: documents conflicts with evidence, does not erase raw forms.
- `DIRECTOR`: signs scoped acceptance and future implementation permission; no implicit approval via source count, passed style QA or branch merge.
- `CODEX` (future): independent implementation audit after authorized Claude Code build; not executed in this research work.

## 5. S4 G01–G19 decision register compatibility
The future implementation must read these as **external decisions**, not self-satisfying Boolean flags:

| S4 gate IDs | Reconciliation required before promotion |
|---|---|
| G01, G17, G18, G19 | named owner scope; separate Claude workspace transfer authorization; explicit production SKILL.md authorization; later independent Codex QA |
| G02, G15, G16 | original/publication rights, consent/synthetic-media review, seven-track archive completeness |
| G03, G04, G05, G06 | original B70–72 missing; 9 part hashes/91 observations disputed; B25/B58 unresolved; B06 legacy manifest document-only (never silently rewrite) |
| G07, G08, G09, G10 | quarantined F-190/K031; blocked R052 original; partial S63/R171 provenance; native A/V unverified |
| G11 | 13 existing validation T protocols none executed; participant recruitment, analytics and studies require separate ethical/data approvals |
| G12, G13, G14 | case-level historical, weather/disaster and military subject-expert gates |

Design publication in its own branch can be `PASS_DESIGN_DOCUMENTATION` while **all production gates remain HOLD**. Gate reclassification demands dated director decision, evidence locator, responsible owner and explicit affected files.

## 6. Required negative controls for future tests
1. Weather: expired warning advertised as active; NWS watch turned into warning; model run called official advisory → detect.
2. Aviation: award/contract equated to fielded jets; old configuration speed attributed to current variant → detect.
3. War: one side's battlefield claim relabelled independent confirmation; alleged event in user title changed to proven → detect.
4. History: invented dying words / inner speech / spurious diary quote; German translation strengthens disputed claim → detect.
5. Disaster: synthetic video depicted as authentic rescue footage; climate cause asserted without case-specific attribution; evolving casualty count called final → detect.
6. General: educational creator assertion converted to measured retention law; R079 sessions called people; R163 synthetic TTS exported to natural VO recommendations; F-190 or R052 cited as source-verified → detect.
7. All niches: no source accessible; incomplete rights for public excerpt; restricted EDU private observation key leaked; dependency on single secondary source described as independent confirmation; 75/100 stylistic rubric used to bypass severity-3 error → detect.

**QA design outcomes:** a negative control must trigger appropriate HOLD/FAIL and retain a documented exception, never merely warn-and-publish. A positive control needs source, valid permission, scoped user intent, reviewers and explicit decision; no fixture proves the system works until an authorized implementation and test actually execute.
