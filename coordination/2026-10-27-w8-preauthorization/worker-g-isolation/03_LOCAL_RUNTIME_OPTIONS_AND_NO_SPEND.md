# Worker G — Future Workspace Options and No-Spend Architecture

**RESEARCH PROPOSAL ONLY:** No local/cloud environment chosen or created, no software installed, no code or scripts run, no Claude initiated, no network or paid API invoked. AP-01/AP-02 NOT_AUTHORIZED.

## 1. Option comparison

| Property | Separately isolated local Windows workstation (proposal) | Separate cloud development environment (proposal) |
|---|---|---|
| Repository | Owner-selected NEW implementation repository, never the public research repo; new pinned branch | Owner-selected NEW independent private-by-default repository, never the research repo |
| Setup dependencies | May use already available, verifiably pinned Python 3 stdlib or local Node LTS; no package install in this task | Provisioning, container pulls and remote access usually require network/cloud identity; incompatible with strict no-network operation until separately engineered and approved |
| Data boundary | Dedicated new unprivileged account/sandbox; avoid other local projects, drives, cloud folders and synced directories | Dedicated tenant/project and short-lived isolated volume, no production mounts, private storage and egress controls |
| Network | Host firewall + process restrictions, disable editor telemetry/extensions/sync, independently verify | Cloud VPC egress-deny, private endpoints disabled unless specially authorized, metadata/token access blocked, provider logs reviewed |
| Credentials | None inside sandbox; avoid GitHub/Claude/LLM or cloud credentials during runtime | Cloud bootstrap necessarily involves identity; strip workload credentials, deny metadata service, specify provider-side retention |
| Cost | Proposed 0 new spending, but existing device/electricity are not proof of 'free' | Cannot assume free credits, zero charges, account entitlements or predictable cost; resource creation is currently forbidden |
| Supply chain | Pin and attest local preinstalled runtime; restrict extensions and auto-updates | Pin image by digest, verify origin and avoid unknown image pulls; requires separately authorized build pipeline |
| Independent reviewer | Read-only pinned redacted output snapshot and denial traces | Separately authorized read-only scope, isolated reviewer account and provider audit log |
| Cleanup | Signed expiry, erase scratch/ephemeral logs, revoke any granted access | Destroy resources/volumes/tokens, stop billing and verify provider data/log retention; owner-authorized only |
| Residual risk | Existing system software, personal secrets, local sync and administrative rights | Remote operator, platform telemetry, cloud defaults, surprise network/billing paths and provider snapshot retention |

**Conditional design preference, not a selection:** For a truly offline, no-new-spend *future* tiny synthetic mock, a separately restricted local environment with a pre-installed trusted runtime could have fewer cloud-account and billing exposures. It is **not automatically safe**: verify local ability to deny egress and isolate secrets before use. Cloud is not 'offline' merely because application code makes no calls; even bootstrap and telemetry count. If local isolation cannot be independently demonstrated, **HOLD**, not automatic cloud substitution.

## 2. Proposed zero-spend contract

- Authorization field for maximum expenditure and currency must be deliberately chosen by owner. Blank approval means **no expenditure permitted**; a suggested zero cap is not a signed budget.
- No API keys or account sessions for Claude, OpenAI, YouTube, analytics, paid model providers, GitHub Actions runners, cloud compute, telemetry or package registries.
- No browser automation, package installation, auto-update, remote model inference, remote testing or accidental cloud-synced storage.
- No promise of cloud free-tier entitlement. Before any later cloud path, owner must separately identify price/limits and approve explicit billing boundaries, disabling auto-spend; **not done** in this audit.
- Already-owned machines and preinstalled software are only possible options; no operating system version, CPU capability, workstation path or installed tool has been verified here.

## 3. Suggested workspace separation for future AP-01 completion

Conceptual logical zones, not actual paths: Z0 source research origin (READ ONLY through authorized GitHub view); Z1 signed static-manifest approval store (owner and rights custodian only); Z2 isolated read-only staged **approved** inputs (EMPTY until AP-02); Z3 synthetic fixture area; Z4 separate restricted mock working scratch; Z5 restricted event logs; Z6 non-author reviewer read-only evidence; Z7 forbidden publish/deploy (no credentials or filesystem target). Do not create directories or assign paths yet.

Minimum future authorization parameters: exact new repository ID and visibility, implementation branch and pinned base, exact operating path and isolation method, developer and independent QA identities, software version and trusted hash, permission/ACL record, expiry start/end UTC, revocation channel, approved fixture provenance, data/log retention, zero budget/currency, and verification owner. Each field remains unfilled today.

## 4. Startup and ongoing safety gates (future only)

No authorized AP-01 -> no development. No AP-02 -> no source-file copy, including B1/B2. No proof of real egress denial -> no runtime. No independent reviewer -> no QA acceptance. Missing or expired rights/owner signature -> block immediately. No approved supply-chain source -> no install. Source revision changes -> invalidate dependent reviews. Actual code results never prove scientific viewer efficacy and cannot authorize production or a Skill release. Deleting a scratch directory alone is not sufficient if backups, sync, telemetry, logs or provider snapshots still exist.

## 5. Distinct approval outcomes

AP-00 may accept a planning concept, and cannot unlock implementation. AP-01 could later permit a scoped synthetic-only prototype. AP-02 could separately permit exact read-only files to an exact recipient; it is not a dependency for inventing original fixtures, but is mandatory for any external source-file transfer. AP-03/T01–T13 human research not authorized. AP-04/G18 production release HOLD. AP-05/G19 independent post-build technical QA not started. PR merges, tool access, GitHub push ability and a verbal intention are not these grants.
