# F11 independent provenance and linked-source audit (Worker C)
Date: 2026-10-27 | Status: RESEARCH_AUDIT_ONLY | Decision: TRANSFER_NO_GO

## Immutable inputs
- Repository: `crimestory5694-beep/universal-scriptwriting-research-hub` (PUBLIC; no root LICENSE/NOTICE documented by Task 1).
- Verified current main: `38d743640534cb390865824d36aeb2c890d628aa`; previous expected checkpoint exactly matched.
- Original F11: `worker-deliverables/skill-architecture/2026-10-27/05_SOURCE_TRACEABILITY_AND_DECISIONS.md` SHA-1 `826b4bd805fca459d45213a975b5cfcee24bc3ad`.
- Original F11 historical link pin: `fb04d86f1512e71ba571c10315fd4d6a9fa26200`. No links were rewritten or retargeted.
- Input reference: Task 1 rights/allowlist audit, Task 2 frozen v0.1 and `03_F11_LINK_SCOPE_ONE_HOP.md`, Task 3 dormant NO-GO and `coordination/CLAUDE_TRANSFER_GATE.md`.

## Independent verification method and result
1. Extracted 13 distinct literal `github.com/.../blob/<40-character-commit>/<path>` links from F11 without changing their URL string; percent-decoded paths only to resolve their exact Git object names.
2. Queried GitHub's recursive historical tree `git/trees/fb04d86f1512e71ba571c10315fd4d6a9fa26200?recursive=1`: 958 entries, `truncated=false`. Exact 13 paths are present, with blob SHAs and byte sizes recorded in `01_THIRTEEN_LINK_VERIFICATION_LEDGER.csv`.
3. Independently fetched all 13 file bodies at the exact pinned commit. All 13 direct `fetch_file` SHAs matched tree SHAs and Task 2's historical one-hop list. Direct file reading is file-identity and report-content verification, NOT independent external paper checking.
4. Classified each as historical audit, research summary, research methodology, or protected-source-reference risk. No recursive link traversal, linked private archive fetch or transitive candidate addition.
5. 13/13 exist, 13/13 tree-to-readback SHA matches, 13/13 byte sizes captured, 0/13 transfer permissions evidenced.

## Non-equivalent evidence levels
- Source existence: Git object at pinned repository commit, VERIFIED.
- Historical report content: bounded authored summary actually read, VERIFIED_AS_HISTORICAL_REPORT only.
- Independent scientific conclusion: NOT_VERIFIED by this audit; T01-T13 remain NOT_EXECUTED.
- Copyright, licensing and external redistribution: NOT_CLEARED. Public availability and matching hashes convey neither copyright grant nor owner AP-02.

## Historical conflicts preserved without ledger mutation
- Original exact B70-B72 cumulative source-rich archive: MISSING; a reconstructed/surrogate package must not be relabeled as its original.
- EDU: 162/162 supplied text reviewed; 153/162 independent source-member SHA matches; nine disputed historical member-part SHAs (`EDU-SRC0139`-`EDU-SRC0147`) and 91 associated observations remain provenance-qualified, despite matching original composite parent and verified character/byte ranges.
- Canonical merged ledger remains 104/162 and 3,051 EDU-C IDs; no new canonical IDs or frozen classification rewrites.
- B25 hash discrepancy, B58 incomplete text, B06 self-manifest hash exception remain unresolved/document-only.
- F-190 UNVERIFIED; K031 HOLD; R163 (487 health-information readers/listeners comparing text with default Azure TTS) cannot establish YouTube retention, natural human voice, or causal generality; reported assignment method lacks explicit randomization detail.
- R052 NPR original source was inaccessible during S3; it cannot become positive proof. S08 licensed/restricted code or text excluded; S31/S40 licensing/version issues unresolved.
- V01-V12 captions do not validate audiovisual patterns or native audience-retention effects. No scientific T01-T13 executions.
- All K and G legacy statuses remain frozen; no grant for G02/G09/G16/G17/G18/G19.

## Rights-safe disposition
- All 13 original linked files: EXCLUDE_FROM_IMPLEMENTATION_PAYLOAD; retain exactly pinned URLs only as internal research-reference locators. This does not approve republication or automatic external disclosure of any individual URL.
- Original F11 F11: `LINK_SCOPE_REVIEW_HOLD`. New `03_SANITIZED_F11_REFERENCE_PROPOSAL.md` is newly authored, proposal only, and NOT automatically transfer-approved.
- F13 canonical internal gate remains effective and excluded from any future implementation payload.
- No AP-01/AP-02 approvals; no Claude transfer, code, SKILL.md, real tests or private export.

## Source trail
Task1: `coordination/2026-10-27-preclaude-13file-rights-audit/`.
Task2: `coordination/2026-10-27-preclaude-task2-prototype-scope-freeze/`.
Task3: `coordination/2026-10-27-preclaude-task3-dormant-handoff/`.
Historical exact URL/path/hash/size evidence: `01_THIRTEEN_LINK_VERIFICATION_LEDGER.csv`.
