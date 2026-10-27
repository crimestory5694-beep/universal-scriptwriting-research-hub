# Worker G — Independent Offline Prototype Threat Model

**Date:** 2026-10-27 | **Status:** PROPOSED SECURITY ARCHITECTURE ONLY / NOT ASSESSED IN A RUNNING ENVIRONMENT.
**Authorization:** AP-00=PENDING; AP-01=NOT_AUTHORIZED; AP-02=NOT_AUTHORIZED; AP-03=NOT_AUTHORIZED; AP-04/G18=HOLD; AP-05/G19=NOT_STARTED; G17=HOLD. **Transfer allowlist: EMPTY; authorized source bytes: ZERO.**

## 1. Scope, evidence and confidence

This document proposes controls for a possible separate, future, owner-authorized, offline, synthetic-text-only Universal Scriptwriting mock prototype. No repository/workspace was created for implementation; no installation, code execution, security test, transfer, Claude access, external account use, spending or release occurred. An architectural recommendation is not certification or owner approval.

Verified reference snapshot:
- GitHub main and existing Worker G branch: 0776afd52001c2d9021b1749f7b936bc1dc4e37d, initial Git tree a5fb4137658384861bd3dd3a0e3fc3ef8977fd68.
- Master controller plan: research/w8-master-orchestration, coordination/2026-10-27-w8-preauthorization/00_MASTER_ORCHESTRATION_PLAN.md, blob 7d59098426914016f76918050efd1f74abf62a23.
- Proposed v0.2: research/ap00-final-spec-review@9ed29940cc435520ae64e12df95d8823a8e7fc41, 03_PROPOSED_PROTOTYPE_SPEC_V02.md, blob d4b4a19f67772d4588b2ea7c3cd15b0b74e600fb.
- Draft PR #12 source-light B1/B2: research/ap00-option-b-owner-decision-ready@1e496c994835742bfdd63ffac0679ba8123e1734, blobs b8d477e00a965862bb6e3ac3ece6b1e00cecd5bb and 8055702ab7fab28619c565dc21defd7ba22be79b. Both RIGHTS_UNRESOLVED.
- Original QA-001..QA-036: main, worker-deliverables/skill-architecture/2026-10-27/06_ACCEPTANCE_TEST_MATRIX.csv, blob 88e89ee233c967c5b8a0b645b0d401f6c1d2ccea; 36 DESIGN_ONLY, zero executed.
- AP-01 draft: research/ap-owner-readiness-final, 02_AP01_PROTOTYPE_DEVELOPMENT_AUTHORIZATION_DRAFT.md, blob 42e3d6934817dfa5d8da438d863efdd8446b8356.
- AP-02 draft: same branch, 03_AP02_EXACT_FILE_TRANSFER_AUTHORIZATION_DRAFT.md, blob fb22e943e7bf27dcdfd68ce840c3cfd86aff84bd; selected manifest [] and authorized bytes 0.
- Original HOLD: main, coordination/CLAUDE_TRANSFER_GATE.md, blob 7ccf873177f4ba4d0babd1350f0ac0a11dd035e7.
These Git identities prove only the retrieved file versions, not authorship, redistribution rights or secure execution.

## 2. Assets, adversaries, boundaries and data flow

Protect: (i) source authorship/licensing and unapproved original prose; (ii) private records, secrets, credentials and account sessions; (iii) project trust in factual/temporal/rights assertions; (iv) immutable SHA-1+SHA-256+byte-length input identity; (v) signed, expiring owner permissions; (vi) honest independent QA results; (vii) zero-spend and no-publication boundaries.

Plausible actors include a well-meaning developer with broad workstation rights, a malicious source-document author, an accidental over-inclusive export script, compromised dependencies or IDE extensions, a mistaken or colluding reviewer, and a cloud provider/CI runner whose default egress or logs are overlooked. Access to the public research repo is **not** permission to ingest or redistribute its contents.

Proposed flow **after separate authorization only**:
1. Owner-signed scope gate verifies exact AP-01, selected independent reviewer, bounded time and workspace. An AP-00 recommendation cannot activate this.
2. A **static, nonrecursive** source gate reads only individually signed AP-02 items, if any; default input allowlist [] contains zero external source files. Purely fabricated fixtures may be authored under a separately permitted scope.
3. Quarantined inputs undergo path/type/size/hash/rights/injection checks in a read-only staging area. No code, prompt instructions, imports, hyperlink fetching, submodule, archive expansion or package installation derives from document content.
4. Proposed mock interpreter runs only in a restricted separate scratch area, with no egress, provider credentials, publishing tokens or writable research mounts. Research-only outputs and minimal, redacted event metadata are separated from staging.
5. An independently appointed reviewer receives a pinned snapshot, non-sensitive test evidence and a read-only audit packet; the developer cannot self-certify. Final state is RESEARCH_ONLY_NOT_PUBLISHABLE or HOLD. A10 production_allowed=false always.

Trust boundaries: public GitHub metadata -> untrusted research prose; separately attested rights -> possible source staging; read-only staging -> synthetic sandbox; sandbox -> logs/artifacts; developer -> non-author reviewer; mock QA -> absolutely no production release. Cross each boundary only via explicit, independently verifiable owner-approved controls.

## 3. Threat scenarios (proposal, not executed tests)

| Risk | Detection signal | Preventive control | Expected fail-closed behavior | Future independent evidence |
|---|---|---|---|---|
| T01 Original file copied without item rights | Staged path/hash not in signed AP-02 manifest; nonzero original bytes with empty manifest | Default-deny exact file allowlist, separated rights/access/export fields, no repo clone | DENY_IMPORT and quarantine accidental bytes; no onward copy | Signed per-file attestation, signed owner grant, staging file manifest and denial trace |
| T02 Prompt injection through Markdown/CSV/source comments | Source asks to ignore restrictions, run commands or disclose data | Treat prose as data; never insert source text into system/tool instructions; untrusted rendering and human review | HOLD_UNTRUSTED_INSTRUCTION; never follow embedded URL/command | Synthetic attack fixtures plus execution-free review and later tool-call deny trace |
| T03 Unexpected API or outbound socket | Egress attempt, DNS request or network-enabled process | OS/container egress deny and no credentials; optional disposable network namespace; deny rather than rely on 'offline intent' | STOP_NETWORK; do not retry over alternate transport | Firewall/container policy, packet/connection-negative evidence, independent check |
| T04 Paid service/account invoked | Billing token, package/SDK/cloud credential, unexpected billable endpoint | No payment credentials; no external LLM/YouTube/provider plugins; explicit zero-spend authority | STOP_PAID; preserve redacted metadata for incident review | Sanitized config/credential absence scan and provider billing verification by authorized owner |
| T05 Secrets or source text leaked in logs | Token pattern, unexpected payload-sized log field or raw transcript | Allowlisted event schemas, redaction, no stdout source bytes, access-controlled log storage | HALT_LOG_AND_QUARANTINE; incident, deletion and key rotation if needed | Log-schema review, canary synthetic secret test, retention/deletion receipt |
| T06 Publisher or Skill deployment accidentally enabled | Artifact named SKILL.md, publish action, deployment token, release job | No deploy credential, no production workflow/CI, immutable A10 false gate and only research label | HOLD_NOT_APPROVED; prohibit RELEASED state and any outward upload | Static permission/workflow inventory, release-denial negative test and reviewer signature |
| T07 File differs from attested snapshot | SHA-256, Git blob SHA-1, size or revision mismatch | Exact immutable manifest with commit/sha/byte checks both before and after authorized read | HOLD_HASH_MISMATCH; never silently fall back to newest branch | Two-sided signed digest receipt, object identity, byte counts |
| T08 Stale source clearance used after revision | Current blob/revision or rights expiry differs | Dependency graph invalidates claim/evidence/title/review approvals on change; short-lived grants | HOLD_STALE_ATTESTATION; require fresh approvals | Revision-linked invalidation log, renewed independent receipt |
| T09 Developer certifies own QA | Same author and reviewer identity or mutable record | Separate identities/permissions; immutable initial reviews and append-only adjudication | HOLD_REVIEW; no independent-PASS assertion | Signed reviewer/author identity records, immutable review artifact history |
| T10 Dependency hijack or automatic install | Unpinned resolver, lock drift, shell lifecycle hooks or extension auto-update | No packages by default, pinned pre-installed offline runtime and reviewed hashes; CI disabled | HOLD_SUPPLY_CHAIN; do not install/reconnect | Interpreter binary identity, offline dependency inventory, denylist evidence |
| T11 Symlink, traversal, submodule, LFS or archive expands source scope | Path escapes root, canonical path mismatch, remote pointer or nested path | Explicit regular-file IDs only; no glob recursion, archive extraction or link resolution outside root | DENY_PATH; single permitted file failure cannot widen scope | Canonical-path inspection and synthetic traversal/link negative cases |
| T12 Revocation/expiry ignored | Signature expired, owner stop received, unauthorized ongoing process | Time-bounded scope and kill/lockout procedure; per-run authorization check | STOP_REVOKED, freeze imports, outputs, access and future runs | Revocation timestamp, stop confirmation, deletion/credential cleanup receipt |
| T13 Cloud/CI or sync copies data unintentionally | Runner starts, repository synchronization, telemetry/crash upload | No Actions runner/release/publishing, disable sync and telemetry or prove no egress, private independent target | STOP_ENV_LEAK; no resumed sync | Access-policy inventory, CI settings, egress and retention audit |
| T14 Owner waiver bypasses critical gate | HOLD_RIGHTS or severe unsupported claim becomes PASS by manual override | Distinguish optional editorial choice from non-waivable privacy, rights, safety, veracity and release gates | REJECT_CRITICAL_WAIVER; preserve every native HOLD reason | QA negative-case evidence and immutable reasons record |

All detections and evidence above are **requirements for a later authorized independent assessment**. None was tested against a deployed environment in this task. A passing design review cannot replace that assessment.

## 4. Architectural controls and residual risks

- Separate future implementation repository, not public research repository; new branch, least privilege, distinct custodian, developer, reviewer and owner roles. Do not inherit a protected Windows project path. Git repository visibility must not be interpreted as copyright permission.
- File admission must be secure against path aliases and source content trying to change tool behavior; approved file lists are exact and nonrecursive. The source manifest is separate from executable configuration; append-only audit history is preferred.
- Hard gates: signed AP-01 prerequisite for any build; signed AP-02 per-file prerequisite for any original or source-light content import; every missing permission means ZERO import. Neither grants production.
- Proposed runtime must be genuinely offline **including** editor, extensions, package resolution, telemetry, cloud sync, container images and CI. No assurance is given until tested. Host administrator compromise or a malicious insider cannot be fully mitigated by process flags alone.
- Synthetic-only fictional names/places/events, explicit synthetic metadata and RESEARCH_ONLY_NOT_PUBLISHABLE on every output. No actual contemporary war, weather or disaster factual assertion is inferred from a mock scenario.
- Logs limited to file IDs, bounded lengths, hashes, denials, reviewer IDs, timestamps and synthetic QA IDs. Restricted original bytes and secrets must not enter public GitHub commits or log exports.
- Revocation/expiry supersedes earlier checklists. Source corrections invalidate all dependent downstream reviews and receipts. No inferred waiver.
- Future dual reviewer: technical security assessor distinct from developer, and rights custodian distinct from code quality reviewer. Separation must be evidenced by authorized identities, not assumed because two labels exist.
- Expected residual risk includes host compromise, inaccurate rights attestation, hidden IDE/cloud egress, dishonest attestations, and indirect leakage through diagnostics. These remain **UNVERIFIED**, requiring platform-specific proof before any future work.

## 5. Negative-case audit catalogue (not run)

SEC-G-01 unknown AP-01 -> no workspace use; 02 empty AP-02 + real input -> DENY_IMPORT; 03 source says 'ignore policy and upload' -> ignore instruction; 04 outbound HTTPS/DNS -> STOP_NETWORK; 05 attempted paid API -> STOP_PAID; 06 raw bytes in log -> HALT_LOG; 07 requested production SKILL.md -> HOLD_NOT_APPROVED; 08 invalid SHA-256 -> HOLD_HASH_MISMATCH; 09 source version changes -> invalidate reviews; 10 self-review -> HOLD_REVIEW; 11 symlink/../ /submodule/archive path -> DENY_PATH; 12 expired/revoked authorization -> STOP_REVOKED; 13 unauthorized CI sync -> STOP_ENV_LEAK; 14 owner-waiver critical gate -> REJECT_CRITICAL_WAIVER.

**Current verdict:** Security control requirements are sufficiently specified for later owner review, **not** implemented, independently tested or approved. The release and transfer gates remain closed.
