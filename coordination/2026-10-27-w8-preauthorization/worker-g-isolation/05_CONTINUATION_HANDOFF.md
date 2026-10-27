# Worker G — Continuation Handoff / No Authorization

**Date:** 2026-10-27. **Worker:** G — Security / Isolation architecture. **Branch:** research/w8-isolation-security. **Exclusive folder:** coordination/2026-10-27-w8-preauthorization/worker-g-isolation/.

## Delivered for Master research integration

- 00_OFFLINE_THREAT_MODEL.md — 14 concrete threat scenarios, future detection, control, fail-closed behavior and required independent evidence; 14 conceptual negative cases.
- 01_SCOPE_SECURITY_CONTROL_MATRIX.csv — 20 candidate controls with threats, detection, expected deny, evidence and owner dependencies, all PROPOSED_NOT_TESTED.
- 02_APPROVED_INPUT_GATE_DESIGN.md — default-empty nonrecursive AP-02 allowlist and G0–G10 admission model, per-file rights/hash/revision/injection checks.
- 03_LOCAL_RUNTIME_OPTIONS_AND_NO_SPEND.md — proposed local Windows vs proposed separate cloud, cost/egress/retention tradeoffs without selecting a runtime or budget.
- 04_SECURITY_QA_RECEIPT.md — independent GitHub read-back/limitations record (see file for observed result).

## Required decisions before ANY actual future work

1. Owner independently chooses/revises AP-00 v0.2 planning specification, with WB-C01..C07 decisions. Source strategy A/B/C still not owner-selected.
2. Rights custodian establishes authorship and third-party rights for any requested content; public URL or source-light label is not authorization.
3. Owner signs exact AP-01 development scope (new repo, branch, workspace, developer, independent reviewer, offline controls, expense cap and currency, UTC expiry).
4. For **each** source file to be copied, custodian and owner separately sign exact AP-02 (source commit/path, blob SHA-1, verified SHA-256, byte count, recipient, target, allowed read-only purpose, expiry, revocation). Until then authorized manifest [] and zero transfer bytes.
5. Independent technical security reviewer validates effective egress denial, source isolation, negative cases, permissions, log redaction, revocation and absence of deployment path. Only after authorized actual build could AP-05 collect executed QA36, separately from rights/science and AP-04 release.
6. Require follow-up Master reconciliation with Worker A through H; unresolved cross-worker disagreements remain explicit and do not become inherited PASS statuses.

## Nonnegotiable inherited limits

Original QA-001..QA-036 DESIGN_ONLY, actual software tests zero. T01..T13 human experiments NOT_EXECUTED. K029..K031 quarantined, F-190/R052 missing/unverified limitations preserved, S08 code/text restrictions remain; F11 links locator-only; F13 and original Claude HOLD remain. No source archive, private information, production Skill, live script, media, provider connection, paid action, cloud resource, Claude transfer, workspace creation or source import was authorized in this workstream.

## Security open questions (owner/platform-specific, do not assume answers)

- Which entirely separate implementation repo, host, branch and exact sandbox will be approved?
- Can effective OS-level egress blocking be independently attested without affecting the user's other projects?
- Who has legally sufficient rights authority to attest each contemplated source-byte object, especially B1/B2 derivative expression?
- Who is the named non-author security/technical reviewer, and what redacted evidence access will they have?
- What exact retention, revocation, incident response and cloud/OS telemetry controls can the owner authorize?
- How will the owner confirm no billable service is enabled and no implicit release path exists?

**Final task boundary:** this Worker G output is documentation research, not AP-00/01/02 approval, a rights grant, an executed penetration test, certified containment or a deployable implementation. A non-author Master must compare claimed research coverage with actual source snapshots and may request revisions.
