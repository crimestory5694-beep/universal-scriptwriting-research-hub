# 8. Exact Research Director Execution-Approval Checkpoint

**Checkpoint ID:** `RD-A1-EXECUTION-GATE-01`

**Antecedent binding decision:** `RD-VALIDATION-DESIGN-01 = ACCEPT_TEST_DESIGN_ONLY`, so T01–T13 are accepted as *research designs* only. Nothing in the present readiness package overrides that decision.

**Submitted status:** `RETURN_FOR_EXECUTION_AUTHORIZATION_REVIEW` — with eight case slots conditional, no confirmed consent/rightsholders/raters/materials; **execution recommendation = NO-GO UNTIL VERIFIED**. The Director should not select an unconditional `AUTHORIZE` on the current evidence.

| Decision ID | Exact approval question | Current response | Evidence required for a future YES |
| --- | --- | --- | --- |
| A1-G01 | Are 8 specific owner-controlled/permissioned subjects actually identified? | NO | Identifiers + owner attestation per H01–P02 |
| A1-G02 | Is each factual packet original, dated, locatable and reviewable? | NO | Primary record index, date/version, assertion map |
| A1-G03 | Are all comparison texts lawfully accessible and derivative use cleared? | NO | Paired version IDs + rights grant |
| A1-G04 | Are independent category experts, native DE/EN qualifications and reserved adjudicator confirmed? | NO | Named roster/capability/conflict declarations |
| A1-G05 | Are A1 text/visual boundaries and evidence-role addendum accepted? | PENDING DIRECTOR ACCEPTANCE | Signed addendum and text-only/semantic-only limitations |
| A1-G06 | Are baseline 16 dimensions and proposed v0.1 operational rubric mappings accepted/frozen? | NOT FROZEN | Explicit rubric version and signatory |
| A1-G07 | Are calibration fixtures, masking, pre-reg code key and exclusions authorized/frozen? | NO | Separate written material-prep authority then approved manifest |
| A1-G08 | Is the 38–69 gross vs 30–59 conditional overlap and new setup/authoring budget approved? | NO | Work ledger, actual rates/availability, capped funding |
| A1-G09 | Are rights, storage, risk escalation and reporting authorities assigned? | NO | Named owner, access policy and response lead |
| A1-G10 | Can A1 explicitly exclude real VO prosody, rendered-video synchronization, human listeners and Analytics? | YES PROPOSED / DIRECTOR TO CONFIRM | Narrow approved scope only |

## Director-only exact decision block

```text
CHECKPOINT_ID: RD-A1-EXECUTION-GATE-01
PRIOR_DIRECTOR_DECISION: ACCEPT_TEST_DESIGN_ONLY
EVIDENCE_ROLE_ADDENDUM_ACCEPTED: YES | RETURN_WITH_CORRECTIONS | NO
A1_CASE_IDENTITIES_AND_OWNER_PERMISSION_DOCUMENT_IDS: [ALL EIGHT OR NONE]
A1_CASE_DECISIONS: A1-H01=[...]; A1-H02=[...]; A1-A01=[...]; A1-A02=[...]; A1-W01=[...]; A1-W02=[...]; A1-P01=[...]; A1-P02=[...]
PRIMARY_FACTUAL_PACKET_AND_VERSION_IDS: [CASE-BOUND ACTUAL IDS OR NONE]
MATCHED_CASE_TEXT_PAIR_PERMISSION_IDS: [CASE-BOUND ACTUAL IDS OR NONE]
INDEPENDENT_REVIEWER_AND_ADJUDICATOR_SIGNOFF_IDS: [ACTUAL IDS OR NONE]
LANGUAGE_COMPETENCE_AND_TRANSFER_SCOPE: [VERIFIED OR DEFERRED]
RUBRIC_VERSION_AND_FIXTURE_SET_APPROVED: [EXACT VERSION AND IDS OR NONE]
PREREGISTRATION_AND_BLINDING_FREEZE_ID: [ID OR NONE]
APPROVED_A1_PROTOCOLS: [T01;T02;T03;T04;T05;T06;T10;T11; OTHER IF EXPLICIT]
APPROVED_SCOPE: INDEPENDENT_PERMISSIONED_TEXT_DESK_REVIEW_ONLY
AUDIO_PROSODY_TESTING_AUTHORIZED: NO
ACTUAL_AUDIOVISUAL_SYNCHRONIZATION_TESTING_AUTHORIZED: NO
B_CONSENTED_LISTENERS_AUTHORIZED: NO
C_OWNER_YOUTUBE_ANALYTICS_AUTHORIZED: NO
D_ORIGINAL_PLAYER_RESEARCH_AUTHORIZED: NO
PUBLICATION_OR_MEDIA_REUSE_AUTHORIZED: NO
EXTERNAL_PAID_SPEND_CAP_USD: 0 UNLESS SEPARATELY APPROVED
ASSIGNED_INTERNAL_PERSON_HOUR_CAP_AND_BUDGET: [ACTUAL NUMBER / NONE]
TEST_MATERIAL_AUTHORING_AUTHORIZED: NO UNTIL SEPARATE EXPLICIT MATERIAL-PREPARATION CONSENT
A1_EXECUTION_DECISION: HOLD_PENDING_VERIFICATION | RETURN_WITH_CORRECTIONS | AUTHORIZE_NAMED_SCOPE | REJECT
A1_PILOT_EXECUTION_AUTHORIZED_NOW: NO
APPROVER_ROLE_NAME_AND_DATE: [DIRECTOR TO COMPLETE]
EVIDENCE_GAPS_AND_NEXT_REVIEW_DATE: [DIRECTOR TO COMPLETE]
PRODUCTION_SKILL_MD_AUTHORIZED: NO
```

**Safe default:** `HOLD_PENDING_VERIFICATION`, `A1_PILOT_EXECUTION_AUTHORIZED_NOW: NO`. An authorization is only meaningful if it names the exact rights-cleared materials, owners, competent independent staff, signed frozen preregistration, applicable category, risk controls and hours/budget. A Director may first authorize **a separate narrowly scoped case-material preparation stage**, but that is not A1 execution and must be explicit. No test scripts, variants or fixtures can be drafted merely because this checkpoint exists.

**STOP:** No tests, recruits, private analytics, paid services, audio recordings, SKILL.md or production instructions until a later explicit Research Director decision.
