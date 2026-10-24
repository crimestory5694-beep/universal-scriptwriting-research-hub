# Supplement — Complete Test Protocol Specifications T01–T13

**All entries are proposals, not completed assessments.** Original K/F/R/V links here denote review relevance and established source relationship roles; no effectiveness study is inferred from a link. Each test includes the required protocol fields. For machine-readable filtering, see `04_TEST_PROTOCOL_MASTER_REGISTER.csv`.

## T01 — Provenance, access, license and independence gate

**ID:** T01

**Research question:** Can a test case be connected to intact, lawful, independently assessed source lines without converting non-support links into support?

**Relevant K / F / R / V / priority IDs:** K001;K007;K040;K041;K042;S01–S63;F-190;R052;R149;R150;V01;V04;V07;V10;P01;P03;P04

**Test population / reviewer role:** Archive custodian plus non-author source auditor and rights reviewer

**Required source material:** Current corrected ZIP, canonical sealed ZIP, source-role audit, source manifests, candidate case permissions

**Candidate and comparator:** Original provenance ledger versus blinded independently reconstructed identity/source-role ledger; no writing-treatment claim

**Assessment rubric:** Per-row traceability; unchanged SHA; source-depth score 0=not accessible/1=index/2=excerpt/3=substantive; rights status allowed/conditional/blocked

**Measurable outcome:** Fraction of cases with legal rights and complete source chain; incorrect support promotion count; verified source-family count

**Proposed success / concern:** Success for phase entry: all test cases lawful, full source chain, zero misclassified F-190/R052 support; concern=any link unresolved, mark blocked (not failed study).

**Reviewer independence:** Custodian cannot serve as sole verifier; auditor independently assigned with source-family tracking

**Confounds:** Incomplete historic GitHub tool logs; institutional duplication; naming collisions; un-cleared upstream licenses

**Costs and access:** A; 3–6 staff-hours for 8 source packets depending on rights; no external access assumed

**Rights and ethics:** Only metadata/excerpts within permission; no media copying or redistribution without rights confirmation

**Stop conditions:** Stop use of a sample if permission, identity, independent source or role provenance cannot be established

**Feasibility:** A

**Proposed phase:** 0

**Execution:** NOT_EXECUTED;DIRECTOR_APPROVAL_REQUIRED


## T02 — Atomic claims, factuality and contemporaneous as-of-date review

**ID:** T02

**Research question:** How many meaningful assertions in each candidate passage can independent fact-checkers verify at the relevant historical or forecast time?

**Relevant K / F / R / V / priority IDs:** K002;K003;K006;K025;K026;K027;K028;K029;K043;K047;F-070;F-073;F-100;F-121;F-201;R145;R133;R157;V01;V03;V04;V05;V06;V07;V08;V09;P02;P08

**Test population / reviewer role:** At least two category-specific fact checkers plus independent adjudicator for critical disagreements

**Required source material:** Consented/creator-owned passages and legal primary archive/manual/official advisory as-issued packets (source timestamps preserved)

**Candidate and comparator:** Claims as presented in source-faithful candidate versus matched control text with deliberate non-harmful ambiguity; additionally sample known counterexample assertions

**Assessment rubric:** Atomize every material fact, named quotation, date, number, causal inference and forecast; label SUPPORTED / QUALIFIED / UNSUPPORTED / CONTRADICTED / NOT_CHECKABLE; severity 0–3

**Measurable outcome:** Claim coverage numerator/denominator; major error count; unsupported fraction; trace link accuracy; adjudicated discrepancy distribution

**Proposed success / concern:** Proposed editorial gate: 100% critical hazard/quotation/death/legal claims traced; 0 severity-3 errors; >=95% sampled ordinary factual atoms supported or qualified; concern=any critical fail or <95%; thresholds are design choices not validated metrics.

**Reviewer independence:** Checkers score independently with variant/source identity masked where possible; conflicts logged before adjudication

**Confounds:** Archive incompleteness; claim complexity; outdated advisories; narrative inference indistinguishable from quotation; manual source mismatch

**Costs and access:** A if original source sheets already legitimately available; 8–16 reviewer-hours for 8 short cases, not counting expensive archive acquisition

**Rights and ethics:** No medical/financial instructions as participant advice; privacy and survivor harm screening; quotations only when licensed/briefly legally usable

**Stop conditions:** Stop case and escalate on fabricated quote, erroneous current hazard, defamation, private identification or unresolved primary source

**Feasibility:** A_CONDITIONAL

**Proposed phase:** 1

**Execution:** NOT_EXECUTED;DIRECTOR_APPROVAL_REQUIRED


## T03 — Four-category editorial quality and counterexample rubric

**ID:** T03

**Research question:** Are optional K techniques editorially suitable for their category without harming factual integrity?

**Relevant K / F / R / V / priority IDs:** K008;K009;K010;K011;K012;K013;K014;K015;K016;K017;K018;K019;K020;K021;K024;K032;K033;K038;K039;K040;K044;K048;F-001;F-010;F-063;F-202;R137;V01;V04;V07;V10;V12;P05

**Test population / reviewer role:** 2 independent editors per category, each fluent in target language and familiar with intended viewers

**Required source material:** 8 licensed short source-bounded case prompts; 16 neutral short paired test texts prepared only if approved; four frozen rubric cards

**Candidate and comparator:** Within-case candidate versus factual-equivalent comparator; order counterbalanced; include legitimate counterexamples and negative case

**Assessment rubric:** 0–4 anchored subdomain scales with category weights; safety factuality separately hard-gated; track N/A, preference and written reasons

**Measurable outcome:** Weighted 0–100 editorial score, paired delta, reviewer spread, fraction rated inappropriate, qualitative exception ledger

**Proposed success / concern:** Exploratory accept-for-further-study only if no critical error, average >=75/100, no rubric subdimension below 2 on consensus and no negative-case harm; no retention implications.

**Reviewer independence:** Blind treatment labels, order randomized locally only after approval, no author-rater overlap, shared calibration excluded from scoring

**Confounds:** Variant author skill; case familiarity; jargon baseline; four categories not exchangeable; editorial preference not behavioral impact

**Costs and access:** A; 8–12 reviewer-hours + case-author prep, using in-house experts with explicit authorization

**Rights and ethics:** Creator-owned or licensed passage excerpts; avoid copied commercial transcripts; no covert participants

**Stop conditions:** Stop or report as inconclusive if comparator factual matching fails, reviewers recognize variants, or error gates fail

**Feasibility:** A_CONDITIONAL

**Proposed phase:** 1

**Execution:** NOT_EXECUTED;DIRECTOR_APPROVAL_REQUIRED


## T04 — Inter-rater independence and agreement

**ID:** T04

**Research question:** Can independent experts reliably identify source errors and make rubric distinctions beyond chance?

**Relevant K / F / R / V / priority IDs:** K001;K007;K041;K042;K043;F-074;F-080;F-083;R145;P04;P14

**Test population / reviewer role:** At least two fully independent reviewers per case; non-voting third-party adjudicator

**Required source material:** Anonymous rating forms, sealed case identities, 2 practice examples distinct from scored set, independently randomized order

**Candidate and comparator:** Double-blind score first; separately adjudicated resolutions used only for final case labels, never to inflate raw agreement

**Assessment rubric:** Categorical percent agreement + Gwet AC1 where feasible; ordinal weighted kappa; Krippendorff alpha only if item design/size allow; raw contingency matrices

**Measurable outcome:** Raw agreement, chance-adjusted estimate and 95% uncertainty where possible; bias and rater drift audit

**Proposed success / concern:** Exploratory target >=80% raw agreement for critical labels; >=0.67 chance-adjusted as minimal provisional coordination; <0.67 triggers redesign; do not interpret small sample as population reliability.

**Reviewer independence:** No access to peers ratings until locking; all disagreements preserved even after adjudication; declare institutional/LLM lineage

**Confounds:** Prevalence paradox for rare hazards; related reviewers; small n; shared prompt/source training; selection bias

**Costs and access:** A; 4–8 hours review/moderation, no paid tools

**Rights and ethics:** Anonymize internal assessments, inform evaluators, avoid storing personal evaluations beyond minimum

**Stop conditions:** Stop safety-critical adjudication if no independent qualified reviewer; never fill missing ratings by consensus guesses

**Feasibility:** A

**Proposed phase:** 1

**Execution:** NOT_EXECUTED;DIRECTOR_APPROVAL_REQUIRED


## T05 — English/German semantic-transfer and register panel

**ID:** T05

**Research question:** Do meaning, uncertainty, temporal relationships and source qualifications survive English/German adaptation in the applicable cases?

**Relevant K / F / R / V / priority IDs:** K020;K023;F-090;F-091;R149;R150;V01;V04;P09

**Test population / reviewer role:** Two native German editors familiar with history + one native English technical editor; bilingual cross-checker independent of translator

**Required source material:** Legally owned aligned source atoms and paired DE/EN test text; original dates/names/mechanism definitions

**Candidate and comparator:** Source-language meaning map versus target-language adaptation; alternative literal version only as comparator; no German register universalization

**Assessment rubric:** 0–4 accuracy/fluency; atomic terminology, modality hedge, chronology, pronoun register, grammatical ambiguity, back-translation discrepancy

**Measurable outcome:** Meaning-retention proportion; material mistranslation rate; terminological disagreements; unresolved-cultural-analogy log

**Proposed success / concern:** Zero material source/uncertainty changes and >=90% noncritical idea-unit equivalence as exploratory threshold; concern any safety/quote meaning drift.

**Reviewer independence:** Translator does not rate their own output; independent native category raters record disagreements

**Confounds:** Different narrator audiences; German formal/informal register; natural localization versus literal translation

**Costs and access:** A if qualified bilingual staff and permissioned excerpts exist; estimated 4–7 staff-hours; otherwise blocked

**Rights and ethics:** Protect named private persons; no full copyrighted translations for redistribution; disclose translation provenance

**Stop conditions:** Stop on material defamation, changed safety advice or unresolved disputed historic quote

**Feasibility:** A_CONDITIONAL

**Proposed phase:** 1

**Execution:** NOT_EXECUTED;DIRECTOR_APPROVAL_REQUIRED


## T06 — Accessibility and semantic visual alignment desk check

**ID:** T06

**Research question:** Can the intended meaning be received without the essential information being invisible, uncaptained or dependent on unlicensed playback?

**Relevant K / F / R / V / priority IDs:** K004;K022;K023;K046;F-170;F-171;F-172;F-182;R149;R150;V04;V07;P03;P09;P15

**Test population / reviewer role:** Accessibility specialist + category graphics reviewer, independently judging accessible source/storyboard packet

**Required source material:** Authorized caption file if present; semantic storyboard / approved diagram references; reading/terminology register

**Candidate and comparator:** Meaning-by-voice only against authorized combined voice+visual/caption packet; intentional no-visual equivalent as negative control

**Assessment rubric:** Checklist for caption semantics, non-speech cues, identification of deictics, dependency on color-only or unmapped objects; 0–4

**Measurable outcome:** Count unresolved visual references; accessible information parity; caption omission/errors; high-stakes content missing

**Proposed success / concern:** All critical map/hazard/diagram information has an equivalent accessible path; 0 inaccessible safety instructions; unresolved rights -> NOT_TESTABLE.

**Reviewer independence:** Accessibility and content reviewers score independently before reconciliation

**Confounds:** Actual audio and on-screen visuals unavailable in original V cases; visual style confounding; subtitle quality unknown

**Costs and access:** A on synthetic/owned semantic map, B for actual users; D if no legally available media

**Rights and ethics:** W3C principles only used within their scope; do not reproduce third-party media or pretend captions verify audio

**Stop conditions:** Stop at source-level design if legally accessible media absent; label playback and hearing outcomes UNTESTED

**Feasibility:** A_CONDITIONAL_OR_D

**Proposed phase:** 1

**Execution:** NOT_EXECUTED;DIRECTOR_APPROVAL_REQUIRED


## T07 — Consented spoken comprehension and accessibility listening

**ID:** T07

**Research question:** Can intended listeners understand properly sourced information when delivered as speech, beyond silent reading judgments?

**Relevant K / F / R / V / priority IDs:** K004;K019;K020;K021;K022;K023;K031;K044;K045;K046;F-060;F-063;R149;R150;R163;V10;P07;P09;P15

**Test population / reviewer role:** Opt-in adult listeners stratified by EN/DE native fluency and relevant novices; include accessibility participants only with accessible accommodations

**Required source material:** Rights-cleared human-narrated matched clips (not inferred old video audio), source packets, short neutral comprehension questions with answer keys

**Candidate and comparator:** Counterbalanced within-topic variation for sentence clarity or visual-reference resolution; identify modality separately; optional audio vs text explicitly labeled non-causal exploratory unless random allocation approved

**Assessment rubric:** Pre-checked question validity, factual answer, delayed free recall, self-rated effort, open-ended misinterpretations, accessible interaction completion

**Measurable outcome:** Accuracy by question and stratum with uncertainty interval; critical misunderstanding count; task completion; listening burden

**Proposed success / concern:** No universal effect threshold; require no additional critical misunderstandings and report uncertainty; exploratory 10 percentage-point practical difference for planning only, not a demonstrated outcome.

**Reviewer independence:** Independent question-author and scorer; order/randomization recorded if approved; no experiment claimed before consent

**Confounds:** Voice/prosody/speaker, audio quality, language fluency, hearing accessibility, repetition, device, prior knowledge

**Costs and access:** B; informed consent, participant reimbursement if chosen later, recording access and IRB/ethics route assessed; NOT IN FIRST PILOT

**Rights and ethics:** Opt-in adults, no personal sensitive profiling without necessity, participant withdrawal, minimal retention; compliant accessibility

**Stop conditions:** Never run without explicit human-study approval; stop for distress, inaccessible design or invalid questions

**Feasibility:** B

**Proposed phase:** 2

**Execution:** NOT_EXECUTED;DIRECTOR_APPROVAL_REQUIRED


## T08 — Weather service understanding and uncertainty safety test

**ID:** T08

**Research question:** Does a warning or forecast test passage enable correct region, issue date, hazard and uncertainty understanding?

**Relevant K / F / R / V / priority IDs:** K010;K026;K047;K002;F-070;F-201;R145;V07;V08;V09;P02;P08

**Test population / reviewer role:** Phase 1 meteorological fact-checker; phase 2 consented adult users unfamiliar with test forecast geography

**Required source material:** Historical as-issued official advisories paired with timestamped sample messages; snapshots, not live guidance

**Candidate and comparator:** Dated service-first versus narrative-urgent comparator matched for hazard data; include negative counterexample outdated forecast and wrong-location paraphrase

**Assessment rubric:** Five-field extraction: where/when/what/severity/uncertainty; scored against issued source; error severity and false-certainty label

**Measurable outcome:** Correct field fraction; region and time confusion; unsafe erroneous action rate; hedging retention

**Proposed success / concern:** Gate: 0 invented warnings, 0 false current directive, 100% high-risk facts source-tied; phase 2 comprehension effect unknown pending study.

**Reviewer independence:** Blind weather specialist independent of writer; participant scorers blinded

**Confounds:** Forecast changes with issue times; same-channel V08/V09 are not independent; participant weather familiarity

**Costs and access:** A desk check first; B later consent and forecast mock-ups; owner analytics not applicable here

**Rights and ethics:** Prominently label HISTORICAL SCENARIO; never publish stale warnings as actionable; avoid inducing panic

**Stop conditions:** Stop on wrong area, expired date concealed, unsupported high-risk statement, or real-time confusion

**Feasibility:** A_THEN_B

**Proposed phase:** 1/2

**Execution:** NOT_EXECUTED;DIRECTOR_APPROVAL_REQUIRED


## T09 — Psychology mechanism and educational transfer safeguards

**ID:** T09

**Research question:** Are mechanism statements verifiable and teaching examples understood without treating R079/R163 as script intervention evidence?

**Relevant K / F / R / V / priority IDs:** K011;K021;K029;K030;K031;K032;K044;F-070;F-121;F-173;R079;R163;V10;V11;V12;P07;P12

**Test population / reviewer role:** Phase 1 independent behavioral-science reviewer; phase 2 consenting educational listeners if cleared

**Required source material:** Primary mechanism sources plus publication population/outcome ledger; owned short lesson passages

**Candidate and comparator:** Source-calibrated mechanism explanation versus equal-length overconfident causal control for critical-failure detection; later paired clarity versions only

**Assessment rubric:** Source claim consistency, uncertainty attribution, understanding of general mechanism vs personal diagnosis; novel transfer item with expert key

**Measurable outcome:** Rate of invalid mechanism claims, personal overgeneralization, comprehension and false inference

**Proposed success / concern:** 0 diagnostic or unsupported mechanism claims; R163 observed health text/default-TTS association only; no transfer claim without new listener data.

**Reviewer independence:** Psych scientist cannot author/rate same condition; participant study questions scored blind

**Confounds:** R079 MOOC platform, duration and student selection; R163 health-specific synthetic voice and non-established randomization

**Costs and access:** A desk expert precheck; B new audio/listener study; first pilot A only

**Rights and ethics:** No mental health diagnosis, no sensitive participant data or misleading self-treatment statements

**Stop conditions:** Stop on personal diagnosis, fabricated study mechanism, unsupported causality or missing paper full text

**Feasibility:** A_THEN_B

**Proposed phase:** 1/2

**Execution:** NOT_EXECUTED;DIRECTOR_APPROVAL_REQUIRED


## T10 — Positive, negative and nonapplicable counterexamples

**ID:** T10

**Research question:** Which candidate techniques can be recognized as suitable in one context and actively inappropriate in another?

**Relevant K / F / R / V / priority IDs:** K008;K010;K011;K012;K013;K014;K015;K035;K036;K037;K038;K040;K048;F-180;F-181;F-202;R079;V01;V07;V12;P05;P13

**Test population / reviewer role:** Two masked category editors per case; independent negative-case coder

**Required source material:** Licensed four-category cases, plus abstract noncopyrighted negative fixtures and original counterexample ledger

**Candidate and comparator:** Each scoped choice contrasted with a legitimate nonapplicable case (e.g. weather alert delayed for intrigue; historical invented quotes; procurement award treated as delivery)

**Assessment rubric:** True-positive suitability, true-negative rejection, applicability and error severity 0–3; false-rule acceptance

**Measurable outcome:** TP/TN/FP/FN matrix by category; rate of damaging false positives; reviewer differences

**Proposed success / concern:** No candidate passes portability unless both matching and negative cases score acceptable, with 0 severe false positives; sample only exploratory.

**Reviewer independence:** Coders blind to technique provenance/advocate and other coders judgments

**Confounds:** Mismatch of topic difficulty; deliberately bad controls easy to reject; awareness of study intent

**Costs and access:** A; 4–8 additional reviewer-hours if separate from T03

**Rights and ethics:** Fiction negative cases clearly labeled fabricated fixtures; never confuse them with source facts

**Stop conditions:** Stop use of a candidate in any category where high-severity false positives appear

**Feasibility:** A

**Proposed phase:** 1

**Execution:** NOT_EXECUTED;DIRECTOR_APPROVAL_REQUIRED


## T11 — Adversarial factuality, privacy and harm stop review

**ID:** T11

**Research question:** Can an adversarial independent checker find a single disqualifying distortion before any craft consideration?

**Relevant K / F / R / V / priority IDs:** K002;K003;K006;K025;K026;K028;K029;K043;F-074;F-075;F-080;F-100;R145;R133;V01;V07;P02

**Test population / reviewer role:** Independent skeptical fact-checker and specialist with authority to fail a case

**Required source material:** Claim ledger, permissioned sources and anonymized excerpts, risk checklist per category

**Candidate and comparator:** Candidate versus deliberately flawed control with severity-known errors (date/quote/contract/forecast/mechanism)

**Assessment rubric:** Risk rubric levels 0 none/1 editorial/2 material misinformation/3 safety, human dignity or defamatory critical

**Measurable outcome:** Severity 2/3 catch rate and false-alarm count; issue-to-source trace

**Proposed success / concern:** All planted severity-3 items should be caught; zero severity-3 in accepted case; pilot inconclusive if known critical item missed.

**Reviewer independence:** Adversarial reviewer not on original source-authorship, independent from primary editor

**Confounds:** Test fixture cueing; planted flaws may not mirror real-world prevalence; missing source packets

**Costs and access:** A; 4–6 staff-hours; source rights clearance required

**Rights and ethics:** No real-world release of intentionally flawed content; mark all negative controls TEST ONLY

**Stop conditions:** Immediate stop on a missing critical trap; isolate from any downstream exposure

**Feasibility:** A

**Proposed phase:** 1

**Execution:** NOT_EXECUTED;DIRECTOR_APPROVAL_REQUIRED


## T12 — Retention uplift feasibility only — owner-controlled

**ID:** T12

**Research question:** Could a later genuine channel experiment identify a script-only effect on viewer retention with adequate power and meaningful allocation?

**Relevant K / F / R / V / priority IDs:** K005;K030;K038;K039;K040;K042;F-022;F-180;R079;R098;R160;R161;V01–V12;P06

**Test population / reviewer role:** Channel owner/analytics custodian, platform-methods statistician, independent research ethicist

**Required source material:** Owner Analytics event/retention exports with allowed granularity; assignment method; comparable audiences/titles/thumbnails/publication schedules

**Candidate and comparator:** Preregistered script condition vs factually matched control; only if valid concurrent randomized exposure possible; otherwise observational cohort explicitly noncausal

**Assessment rubric:** Primary outcome platform-defined AVD or completion; co-primary not multiplied casually; confidence interval, uncertainty, covariate plan and attrition, negative findings

**Measurable outcome:** Viewer-level or upload-level aggregate effective sample; uncertainty, selection imbalance, horizon, competing packaging variables

**Proposed success / concern:** Feasible only with owner consent + identifiable treatment isolation, credible assignment and power simulation; absent these, HOLD_NO_RETENTION_CLAIM; no universal numeric uplift target.

**Reviewer independence:** Analyst not script author, preregistration and immutable analysis plan, blind analysts to arm when feasible

**Confounds:** Algorithmic distribution, CTR, topic/title/thumbnail, time effects, repeated viewers, platform metric definition shifts, content quality

**Costs and access:** C; likely greatest cost; no owner access presently asserted; no exports or services activated

**Rights and ethics:** No scraping private audience data; use owner-authorized aggregate exports; comply with platform terms; data minimization

**Stop conditions:** Do not initiate without owner rights, platform-valid design, baseline variance and privacy/legal approval; stop if randomization impossible for causal claim

**Feasibility:** C

**Proposed phase:** 3

**Execution:** NOT_EXECUTED;DIRECTOR_APPROVAL_REQUIRED


## T13 — Native caption/audio provenance access decision

**ID:** T13

**Research question:** Is original player timing and audio lawfully accessible, and can unavailable source windows remain explicitly unknown?

**Relevant K / F / R / V / priority IDs:** K041;K045;K031;F-190;R149;V01;V04;V07;V10;P01;P10

**Test population / reviewer role:** Rights/source-access specialist; no assumed voice listener

**Required source material:** Original player Show Transcript (if accessible) and authorization for a few playback windows; existing blocker report

**Candidate and comparator:** Native player cue versus prior third-party mirrored V10 cue, tracked as different provenance; no inferred proxy

**Assessment rubric:** Timestamp present with original-source proof / source denied / playback legal but unavailable / no verification

**Measurable outcome:** Exact count true source verified cues, verified audio windows and documented barriers (not script-quality outcome)

**Proposed success / concern:** Success only genuine timestamped native cues and separately listened windows; concern unresolved access -> BLOCKED, no duration/prosody reconstruction.

**Reviewer independence:** Separate checker verifies link provenance; do not treat mirrored footage as original

**Confounds:** Geoblocking; age-gates; vanished captions; interface changes; transcribed playback not equivalent to listened voice

**Costs and access:** D; may become A after rights+access; NOT in phase-1; no paid transcripts

**Rights and ethics:** Lawful ordinary player use; no circumvention; no copying or scraping beyond allowed permissions

**Stop conditions:** Immediately halt if absent cue, access control or rights; log blocker precisely

**Feasibility:** D_OR_A_AFTER_APPROVAL

**Proposed phase:** 0_DEFERRED

**Execution:** NOT_EXECUTED;DIRECTOR_APPROVAL_REQUIRED
