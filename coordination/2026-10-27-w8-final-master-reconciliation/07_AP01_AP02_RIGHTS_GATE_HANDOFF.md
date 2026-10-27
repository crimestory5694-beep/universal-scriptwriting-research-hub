# AP-01 / AP-02 — Separate Unsigned Gate Package and Custodian Evidence

**Status: ALL APPROVALS BLANK; NO DEVELOPMENT OR TRANSFER AUTHORIZED.** This document is a proposed decision framework, NOT permission. Security Worker G and Governance Worker H are the analysis sources; neither has owner, technical, or rights-custodian authority.

## Gate prerequisite map

1. **AP-00 (planning specification only):** owner considers revised B1/B2 technical completeness and seven WB clarifications; B1/B2 independent technical and rights audit **pending**. Owner strategy A/B/C choice not recorded.
2. **Copyright / title / contributor assessment:** actual named rights custodian must establish permitted internal use, source copying, derivative distribution, citations/notices, privacy and confidential material for *each exact version*, including the newly written B1/B2 if selected. A public GitHub repository is NOT a licence grant.
3. **AP-01 (separate potential build):** owner may authorize a bounded, isolated **offline synthetic-text-only** prototype effort *only after* the scoped plan, security evidence and independent developer/reviewer roles are agreed. AP-01 **does not permit source-copy or external LLM use**.
4. **AP-02 (separate external file transfer):** owner and rights custodian must explicitly approve exact source files, versioned full bytes and designated Claude destination, purpose, retention and revocation. AP-02 **does not permit build/execution** by itself.
5. Future AP-03 participant/causal study, AP-04 production Skill and AP-05 independent code QA remain separate projects/approvals; G17/G18 HOLD, G19 NOT_STARTED.

## AP-01 — limited prototype DEVELOPMENT proposal (unsigned)

| Required field | Proposed safe restriction / blank human decision |
|---|---|
| Named project owner and authorization proof | __________________ |
| Exact task and AP-00 accepted version reference | __________________ |
| Start and expiry, revocation authority | __________________ |
| Dedicated isolated path/repository, developer identity | __________________ |
| Independent technical/security reviewer distinct from developer | __________________ |
| Allowed input kind | **Fictional, authored synthetic text only**; no files copied from original research unless a separately signed AP-02 grants them |
| Network/telemetry/CI/editor/extension behavior | Proposed DENY outbound network/DNS/sync, disable automatic downloads and installs; **not tested** |
| Accounts/tokens/spend/API access | No credentials; no paid services; no inference providers; no source fetch |
| Logs | IDs, SHA fingerprints, bounded synthetic QA metadata only; redact secret or source payload |
| Deployment/release/publishing | Unconditionally forbidden, no production SKILL.md, no export-to-production |
| User-selected AP-01 choice | [ ] Approve exact written scope  [ ] Revise  [ ] Decline  [ ] Defer |
| Owner signature/date | __________________ |

**Current AP-01:** NOT_AUTHORIZED. Threat scenarios SEC-G-01…14 are paper negative-case designs and have **not** been run. A future independent runtime/security assessment must verify actual egress denial, permission boundaries, supply-chain hashes, isolated source staging, secret/log controls, time-bound grants and revocation.

## AP-02 — EXACT item-specific source transfer proposal (unsigned)

**Current authorized transfer manifest:** `[]` (zero files, zero source bytes).

For EACH proposed item, the custodian/owner must independently complete:

| Permission field | Blank / required evidence |
|---|---|
| Canonical repository/path + precise source commit | __________________ |
| Git blob SHA-1 + independently calculated SHA-256 + exact UTF-8 bytes | __________________ |
| Author/contributor identities, contractor assignment and origin evidence | __________________ |
| Upstream third-party expression, licences, attribution, derivative permissions and privacy | __________________ |
| Access/analysis/copy/external recipient/public-distribution rights **separately** | __________________ |
| Exact Claude account/workspace/destination and transfer mechanism | __________________ |
| Read-only purpose, access control, retention/deletion, expiry/revocation | __________________ |
| Independent rights-custodian decision/signature/date | __________________ |
| Actual project-owner AP-02 decision/signature/date | __________________ |
| Decision | [ ] Permit ONLY exact listed item  [ ] Exclude  [ ] Revise  [ ] Defer |

**Possible candidate fingerprint references for future assessment, NOT an approved transfer list:**
- `03_B1_V02_SOURCE_LIGHT_CANDIDATE.md` at this Master branch: Git blob `96f45cbb9570d00c2a22a499b0ec34a821362d0c`, 15,188 bytes.
- `04_B2_V02_QA36_CANDIDATE.csv` at this Master branch: Git blob `a643befb8e74536b4572d4f22812a2d411629bf2`, 13,584 bytes.
- Old B1 Git blob `b8d477e00a965862bb6e3ac3ece6b1e00cecd5bb` (8,425 bytes), old B2 `8055702ab7fab28619c565dc21defd7ba22be79b` (6,966 bytes), and original F07–F10/F12 source files still carry **unresolved** cross-workspace reproduction permission.

Neither the old nor the revised candidates were accepted by a rights custodian, so candidate fingerprints must **not** be copied into a list of authorized transfers. Do not equate this inventory with a signed manifest. The exact source SHA-256 may be obtained from a final verified digest receipt when and if custodian review occurs.

## Immediate deny behavior (design requirements, not executed controls)

- No signed AP-01 ⇒ NO BUILD.
- No signed AP-02 for an exact original or source-derived research file ⇒ NO FILE IMPORT or Claude access.
- No right to read/reproduce an item ⇒ HOLD_RIGHTS even if an editor or public GitHub fetch succeeds.
- Unknown, expired, revoked or mismatching item path/hash/size ⇒ HOLD_HASH_MISMATCH or STOP_REVOKED; do not widen scope.
- No self-review, no copying third-party transcripts, no F11 recursive links, no historical originals B70–B72, no source-rich ZIP, no private participants, and no generated incident footage presented as real.
- No production approval ⇒ research-only termination; `production_allowed=false`, `RELEASED` unreachable.

### Roles requiring actual future evidence

Owner decides work authorization; rights custodian clears expression rights; developer implements only signed scope; separate technical/QA reviewer verifies implementation; human research reviewer approves studies; production authority separately reviews any release. No ChatGPT worker substitutes for these roles.

**Until genuine signatures:** AP-00=PENDING, Source A/B/C=UNSELECTED, Rights=UNRESOLVED, AP-01/AP-02=NOT_AUTHORIZED, Claude manifest=[], G17/G18=HOLD, G19=NOT_STARTED.
