# CLAUDE CODE — BUILD THE ACTUAL UNIVERSAL SCRIPTWRITING SKILL (CANDIDATE)

**Owner request, 2026-10-28:** Wave 8 research collection is frozen. Use **Claude Code as the implementation agent**, NOT ChatGPT or the initial Node.js demo as the final Skill. Perform implementation, not another research audit. This is a self-contained **newly authored instruction**, not a grant of rights to import prior repository contents.

## Important repository/isolation rule

The historical research repository `crimestory5694-beep/universal-scriptwriting-research-hub` includes materials whose **external reuse/Claude transfer rights are unresolved**. **DO NOT clone, mirror, bulk-download, recursively browse or import this research repository in a Claude Cloud environment**, even if a GitHub URL or branch was mentioned as a checkpoint. Reading/using a GitHub public repository is not proof of permission to copy all its contents to an external workspace.

Start inside a **new, empty, separately owned implementation repository or empty local working folder** approved by the owner. The only initial source input is the original instruction in this handoff, **pasted by the owner directly into Claude Code**. Do not fetch Wave 8 B1/B2, transcripts, archives, unpublished source records or internal files. The historical wave checkpoint is a project tracking label only: `0416f7bcbd2cb939fb95aafb09afa63d258116dc`. Current allowed external research-source file manifest: `[]`.

If a connected cloud Claude Code session requires a repository, use a new clean, isolated repository. Do not choose the existing research hub as the session's repository. If you cannot establish isolation, explain the precise blocker; still create complete local original source files and tests in a suitably isolated working folder if available, rather than reopening research.

## Role

You are **Claude Code, lead implementation engineer and Skill author**. Deliver an *actually runnable, tested, source-free candidate Universal Scriptwriting Skill*. Write actual files and tests, not merely an architecture plan, progress report or handoff. Do not run third-party paid APIs, use secrets, scrape YouTube or fetch external protected transcripts. Do not make a production publication or external-file transfer.

## What the user is trying to obtain

A reusable Claude-driven documentary scriptwriting Skill supporting five styles:
- N01: USA weather documentary
- N02: military / aviation / current conflict documentary
- N03: German WWI/WWII human-story documentary
- N04: disaster documentary
- N05: general explainer / psychology documentary

The target is factual, evidence-linked 15–25 minute narration in English, except N03 can generate German after qualified German source-language review. The Skill must preserve topic **subject**, **object**, source attribution, modal language, geographic/time scope, uncertainty and supported mechanism. The exact narration length is a user input (e.g. 2,500–3,000 words), not an invented universal effectiveness law.

## Required actual deliverables

1. `candidate_skill/SKILL_CANDIDATE.md`: newly written candidate instructions organized into meaningful stages, with testable input/output contracts and no claim of production approval. The eventual deployable `.claude/skills/universal-scriptwriting/SKILL.md` is **not** approved; do not install/deploy it in this task.
2. `candidate_skill/modules/`: **11 independently understandable modules A00–A10**, with A00 intake, A01 source/rights registry, A02 evidence admission, A03 context policies, A04 atomic claims, A05 narrative options, A06 topic/outline lock, A07 draft generation, A08 independent review, A09 output quality/metric separation, A10 release denial. A06 can have internal pre-lock and final-lock milestones so A05 is not circular. Explicit versioned inputs/outputs and typed HOLD reasons.
3. `candidate_skill/adapters/`: exactly N01–N05. Policies accumulate; no implicit permissive fallback for unknown hazard/domain. Explicitly label synthetic visuals vs. authentic source media, quotation status, language uncertainties, and false impact claims.
4. `candidate_skill/contracts/`: original, self-authored JSON Schemas or equivalent validators for TopicLock, SourceRecord, EvidenceLink, AtomicClaim, PolicySet, DraftSpan, ReviewPacket, RunBundle. Use separate `retrieved_at` and `reviewed_at`; source byte hash only if really calculated. Multiple HOLD reasons must never be discarded.
5. `candidate_skill/runner/`: runnable **offline**, **zero-dependency if practical** interface taking fictional JSON fixtures and emitting an outline, source/claim matrix, structured synthetic script draft, and typed QA/HOLD report. No actual web browsing or external service in this prototype.
6. `candidate_skill/tests/`: executable positive and adverse cases, including all **36 distinct QA-001...QA-036 synthetic test *intents***, invented from this contract. Never copy the historical QA test case wording or original restricted archives. Add explicit no-release/no-transfer and multi-overlay checks.
7. `candidate_skill/demo/`: at least one complete, understandable invented documentary example, plus expected test commands, observed stdout/test report and reproducible output.
8. `BUILD_RESULT.md`: actual file list, git commit SHA if available, exact tests executed and PASS/FAIL (do not claim checks that were not run), demonstrated shortcoming(s), and one specific next engineering milestone.

## Functional definition of done

- The candidate can process one input document end to end and produce actual sections with linked fictional source/claim IDs. A section must not be filled with unsupported invented factual assertions; if evidence is insufficient, emit `HOLD_INSUFFICIENT_EVIDENCE` rather than padding words.
- Show working topic subject/object lock, uncertainty preservation, source roles, frozen review revisions, five niche guard overlays, no fabricated real event assertions, and HOLD reasons that can co-exist.
- If enough fully fictional evidence exists to support a 2,500–3,000-word example, produce one. Otherwise produce an honest shorter sample plus a failing full-length scenario that explicitly reports missing evidence/coverage. **Never inflate script length or fake completion.**
- Execute tests using the actual implementation runtime. A CSV labeled DESIGN_ONLY does not count as an executed test.
- Do not assert scientifically proven hook/retention improvement, copyright clearance, independence of a real human reviewer or production readiness without proper evidence.
- Every generated artifact includes `RESEARCH_ONLY_NOT_PUBLISHABLE`, `production_allowed=false`, and `claude_transfer_allowed=false`.
- Never publish/deploy an active Skill or use true historical scripts, news, private files or claims for testing.

## Run order — strict

1. Create an isolated empty working tree, choose a new project branch; write a minimal project README and module skeleton. **Do not begin another educational or source audit.**
2. Implement the working contracts, small engine and adapter checks. Use self-authored fictional test fixtures only.
3. Implement the candidate Skill instructions and real script-drafting path, with citation/claim traceability.
4. Run an executable test suite, fix failed functional tests, produce one generated output and a test receipt.
5. Commit/push only newly authored source-safe implementation files **if the owner has granted repository write access**, leave changes on a feature branch or DRAFT PR, never merge to protected/main without explicit approval.
6. Return a compact completion report including paths, tested counts, runnable command, demonstrated demo, known limitations and next owner decision.

## Stops, not rabbit holes

NO new education batches, rights research loops, 8-worker parallel audits, PR merges, research archives, giant architectural documents, or vague claims of 'ready'. If a rights/access dependency actually blocks use of historical source, leave it out and continue the completely independent source-free candidate. Build and test before elaborating further governance. Ask the owner only if working directory or authorized source scope is genuinely unavailable.

## Governance

This is authorization to **prepare and test a non-production, independently authored candidate in an isolated workspace** only to the extent the owner's Claude environment permits. It is not a formal signed AP-01 implementation grant, a specific AP-02 file-transfer licence, a rights-custodian certification, production G18 release, or permission to import historical source bytes. Keep external source manifest `[]`; production and release HOLDS remain closed.

**User-facing final reply: Roman Urdu. Source code, candidate Skill and test documentation: English.**
