# Context-sensitive niche adapter specifications (five S4 domains)

**Architecture status:** design-only; the presence of an adapter is not permission to generate final channel narration. Context-specific facts need independently verified, dated original sources at run time. Every module inherits the common fact/rights/independence gates. Niche-specific styles are optional when they conflict with facts, safety, clarity or the user's central topic.

## N-01 USA Weather / service forecast documentary
**Profile:** primarily US viewers; English; immediate public-safety relevance may override an ordinary storytelling goal. **Source hierarchy:** as-issued responsible NWS WFO advisory/warning and forecast discussion; NOAA/NHC/WPC/SPC as germane; reissue date, local hazard geography, timezone and effective period checked. Secondary weather model outputs and creator videos never supersede an applicable issued warning.

**Required extra fields:** `hazard_type`, `forecast_issued_at`, `valid_from`, `valid_until`, `forecast_region`, `official_warning_type`, `confidence_and_scenario`, `next_recheck_policy`, `affected_counties_or_regions`, `source_map_version`, `event_status` (`forecast | ongoing | observed_historic`).

**Opening policy:** when there is a genuine public hazard, give verified *what/where/when* and uncertainty early; no long delayed reveal of necessary actionable information. Keep agency WATCH vs WARNING vs ADVISORY distinct. Separate weather *model projection* from operational warning and observed outcome. No street-level impact forecast without supporting granularity; no fabricated emergency alert graphics. A season-wide explainer must not be written as if a warning is active.

**QA/hard stops:** issue/expiration dates absent, wrong location or timezone, archived headline presented as current, model certainty overstated, stale map, purported warning with no original agency locator → `HOLD_STALE_FORECAST`/`HOLD_UNVERIFIED_FACT`. Refresh official source immediately before time-sensitive publication approval. Negative fixture: “Storm warning in effect tonight” built from a prior week's forecast → FAIL. Positive fixture: archive analysis explicitly labelled with original issue time and historical scope → eligible for editorial review.

**Reference boundaries:** K002/K003/K010/K026/K047, S3EXT001 and S4 G13; R145 journalism guidance; T08 not executed. **Not** a claim of superior viewer retention.

## N-02 Military aircraft / Russia–Ukraine / NATO technical documentary
**Profile:** English US/UK adult explanatory documentary; present tense war developments are time-sensitive. **Source hierarchy:** dated engineering and procurement primary records (GAO, manufacturer documents qualified as claims, official government award/test/deployment records), official incident statements, independently corroborated conflict reporting when first-hand sources are limited; identify parties making disputed battlefield claims. Do not equate PR or unverified combat footage with proven outcomes.

**Extra fields:** `platform_or_system`, `capability_stage` (`proposed | contracted | prototype | testing | low_rate_production | fielded | reported_in_combat`), `configuration_variant`, `test_conditions`, `claiming_party`, `independent_confirmation`, `event_date`, `reported_vs_established`, `civilian_harm_review`.

**Content guardrails:** contract award ≠ fielded deployment; advertised max speed/range ≠ achieved combat conditions; apparent drone penetration ≠ proven causal “air-defense collapse.” Separate strategic implications, hypothesized mechanism and observed material effects. When viewer provides competitor title, preserve central subject and object while retaining contested status. Explain uncertainty in military damage claims, especially in active conflict; avoid unsupported triumphalism or unverifiable casualty attribution. No operational targeting instructions or weaponization how-to in editorial docs.

**QA/hard stops:** dated claims about capability without variant/capability phase; one propaganda source masquerading as independently corroborated; unverified combat claim written as certain → `HOLD_UNVERIFIED_FACT`. Negative: “new engine contract means current fleet already upgraded” → FAIL. Positive: “engine upgrade awarded, testing and fielding dates remain distinct” with sourced timeline → fact-review candidate.

**Reference boundaries:** K002/K003/K009/K021/K027/K047, S4 G14, GAO S3EXT acquisition check, four-category Aviation rubric. World events require fresh primary verification.

## N-03 German WW1/WW2 historical emotional documentary
**Profile:** DACH German narration; source-first human history; emotionally restrained and respectful. **Source hierarchy:** original archival correspondence with exact repository locator and contemporary records; authenticated interviews/translations with edition/version; scholarly secondary histories for context. A photograph alone does not authenticate quoted last words.

**Extra fields:** `person_id`, `event_and_date`, `archival_collection`, `document_language`, `quote_verbatim_status`, `translation_review`, `chronology_provenance`, `sensitivity_and_survivor_risk`, `names_pronunciation_review`, `german_register_review`, `reenactment_label`.

**Content guardrails:** no invented internal motives, diaries, dialogue, eyewitness accounts, dying words, or fabricated letters. Distinguish witnessed fact, contested archival reconstruction, historical inference, and dramatic reenactment. German translation must preserve uncertainty: *soll*, *laut*, *vermutlich*, *belegt* correspond to source status, not a German stylistic intensifier. German-native reviewer checks idiom and spoken plausibility, but cannot certify actual audio without recording. Avoid dehumanizing portrayal and treating victims as narrative props.

**QA/hard stops:** unattributed quote, unverified letter, suspect death date, fictional dialogue presented as documentary, no historical/ethical reviewer for sensitive case → `HOLD_HARM` or `HOLD_UNVERIFIED_FACT`. Negative: invented “his last words were...” → FAIL. Positive: quoted dated letter with archive link, date and documented translation uncertainty → eligible for review.

**Reference boundaries:** K006/K008/K023/K025/K028/K041, S4 G12, R145 archives ethics, historical rubric and T05 language design. Curiosity hooks cannot overrule archive truth.

## N-04 Disaster news / climate and emergency documentary
**Profile:** English, US/UK/CA/AU; natural disasters, accidents, wildfires, climate context, response, social consequences; current events may affect safety. **Source hierarchy:** event-specific official incident reports, weather/emergency agencies and dated local records; scientific attribution claims require original study and inferential scope; footage provenance must be authenticated separately.

**Extra fields:** `incident_id`, `location_and_date`, `casualties_claim_status`, `response_authority`, `current_versus_historic`, `climate_attribution_scope`, `footage_source`, `footage_license`, `synthetic_scene_flag`, `synthetic_disclosure_decision`, `affected_people_privacy`.

**Guardrails:** distinguish disaster event description from causal climate attribution; do not attribute a single specific event to climate change absent case-specific evidence and valid scope. No invented live footage, newsroom witness, rescue transcript or casualty statement. Synthetic depiction must not masquerade as authentic event footage; use clear disclosures appropriate to platform requirements and editorial context; genuine-looking AI avatar does not give license to impersonate a real reporter or eyewitness. Do not assert unverified “100% real” provenance.

**QA/hard stops:** wrong event geography, evolving casualties presented final, fabricated emergency footage or missing required disclosure, consent/privacy risk → HOLD. Negative: photoreal flood animation labelled “raw footage from today” → FAIL. Positive: clearly labelled reconstruction with established incident facts and separated visual evidence → review candidate.

**Reference boundaries:** K002/K006/K025/K026/K034/K041/K046, S4 G13/G15, R145/R150, S3 official synthetic-media guidance with timestamp-recheck before release.

## N-05 General long-form explainer / cross-niche documentary
**Profile:** choose specific language and expertise; no assumed genre, uniform 15–25 minutes, universal viewer psychology or mandated curiosity loop. Covers economic/trade mechanisms, science/history explainers and similar, but `health_claim`, `personal_finance`, `live_conflict` and `active_hazard` overlays always trigger stricter domain review instead of falling back here.

**Extra fields:** `discipline`, `principal_research_question`, `evidence_kind`, `contested_views[]`, `audience_prior_knowledge`, `model_or_analogy_limitations`, `narrative_option_rationale`, `public_interest_factuality_class`.

**Creative alternatives (explicitly untested):** paradox hook, direct-answer opening, chronological investigation, modular technical explanation, authentic clue/payoff, metaphor, optional act structure; provide negative-case examples and select per intent, not a universal rank. No claims that one improves YouTube CTR, percentage viewed or watch duration without actual owner data and approved study.

**QA/hard stops:** causal scientific claim without valid study population/method, metaphor presented as mechanistic proof, one-sided contested account suppressing uncertainty, creative technique asserted as scientifically proven. For educational psychology, retain the K029/K030/K031 HOLDs; R079 MOOC observations and R163 health synthetic-audio comparisons do not justify general documentary formulas.

**Reference boundaries:** K001/K012/K014/K016/K018/K024/K032/K038/K040/K042/K044/K048, S4 general domain; T03/T09/T12 unexecuted.

## Cross-niche review matrix
| Attribute | Weather | Defense | German history | Disaster | General |
|---|---|---|---|---|---|
| Primary hard truth | forecast issue + validity | capability stage / claimants | archive + dialogue authenticity | incident, image and attribution | original domain evidence |
| Editorial title eligibility | hazard geography / time | subject-object + contested status | faithful historical claim | source footage authenticity | question + qualifier |
| Language | English (US) | English (US/UK) | native German reviewer | English regional contexts | explicit per project |
| Visual/audio gate | dated forecast map / caption | technical diagram accuracy | archival rights / translation | synthetic disclosure / privacy | case-dependent |
| High priority HOLD | stale warning | prototype=fielded | invented quotation | fake real-event footage | unsupported universal psychology |
| Optional narrative | direct hazard answer | verified engineering paradox | sourced human dilemma | explanation / chronology | flexible hypothesis set |

**Scalability constraint:** Plugin/runtime connectors and upload orchestration are *future* integration concerns. Architectural adapters are plain data and policy abstractions; they neither authorize autonomous publishing nor specify live news-check intervals without the corresponding owner-approved workflow.
