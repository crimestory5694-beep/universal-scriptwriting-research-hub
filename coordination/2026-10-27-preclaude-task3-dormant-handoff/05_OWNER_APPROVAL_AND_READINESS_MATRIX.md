# Director decision checklist — AP-01/AP-02 NOT SIGNED

**This is a pre-authorization draft, not a consent document.** The user instructed completion of the ChatGPT preparation task, not actual code development or transfer.

| Gate | Required future decision | Status now |
|---|---|---|
| AP-00 | Accept or revise spec v0.1 for *planning* | PENDING |
| AP-01 | Explicit authorize isolated offline synthetic text-only prototype, name target repository/workspace/branch/developer, spend and expiry | NOT_AUTHORIZED |
| AP-02 | Independently authorize exact read-only file subset F01–F10/F12 with paths, pinned SHA1+actual source SHA256, legal content review and exact separate Claude destination | NOT_AUTHORIZED |
| F11 | Scope/sanitize linked provenance; no auto-follow of 13 historical links | HOLD |
| F13 | Keep internal transfer gate enforced, exclude from developer payload | EXCLUDED |
| AP-03 | Rights/ethics/data/case approval to execute T01–T13 human/scientific trials | NOT_AUTHORIZED |
| AP-04/G18 | Production SKILL.md and deployment | HOLD |
| AP-05/G19 | After-build independent Codex code QA | NOT_STARTED |

Before AP-01: document exact feature scope, mock-only input/data sources, no external provider budget, independent reviewer, intended new workspace and branch, original frozen GitHub input. Before AP-02: per-file rights-custodian attestations and explicit list of transferred exact SHA256 bytes, no omitted-file assumptions, no linked-source traversal, target Claude workspace identity, read-only action and revocation rules. **AP-01 is not AP-02 and does not grant rights.**

## Release states
- `DOC_READY`: planning bundle written, verified in GitHub, no material transfer.
- `RIGHTS_PENDING`: eleven candidate references require named custodian decisions; F11 needs scoped derivative, F13 withheld.
- `OWNER_SCOPE_PENDING`: no AP-01 or developer target.
- `TRANSFER_NOT_ELIGIBLE`: no AP-02; no Claude files copied.
- `IMPLEMENTATION_NOT_STARTED`: no code and no 36 software tests executed.
- `PRODUCTION_NO_GO`: G18 HOLD and wider source/rights/validation gates remain.

## Immediate owner options
Accept documentation as a reference, request corrections, or decline the proposed internal prototype. If approving development later, issue specific AP-01 and separate AP-02 decisions rather than a generic 'go ahead'. Do not retrofit any historical G01–G19 ledger row or reinterpret this drafting request as implicit approval.

Next owner authorization form must remain **blank/unsigned** until an explicit owner statement is supplied. No signed permission is stored in this task.
