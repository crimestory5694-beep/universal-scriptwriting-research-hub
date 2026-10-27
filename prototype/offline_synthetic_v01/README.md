# Universal Scriptwriting — Offline Synthetic MVP v0.1

**STATUS: RUNNABLE RESEARCH DEMO, NOT A PRODUCTION SKILL.**

The earlier eight-worker data-collection/research work is frozen. This isolated branch is the first actual *working* milestone: a dependency-free JavaScript engine, a Node.js CLI, a fully fictional example, and 36 QA scenario fixtures. The prototype **does not** connect to Claude, import original research text, use paid APIs, make online requests, claim true fact-checking, or publish content.

## What the executable currently does

- Accepts a local JSON object: fictional topic, canonical subject/object, existing proposed title, invented sources, invented atomic claims and review-role labels.
- Enforces `synthetic: true`, `source_copy_manifest: []`, explicit UTC-offset clocks, one of five canonical niche codes N01–N05 (aliases N-01…N-05), and accumulation of additional niche overlays.
- Validates source-access/reuse fields, claim-source links, independence families for simulated confirmed claims, reviewer-role separation, qualification/certainty signals and basic topic identity.
- Runs fictional weather, military, history, disaster and general-explainer negative-case flags.
- Emits all matching typed HOLD reasons with **no draft** when a basic gate fails.
- Otherwise emits a deterministic illustrative outline and **approximately 80-word** three-section synthetic text sample; this is *not* a 15–25 minute final documentary script.
- Always sets `production_allowed: false` and `claude_transfer_allowed: false` and reports `RESEARCH_ONLY_NOT_PUBLISHABLE`. No `RELEASED` state.

**Important limitations:** This is a lightweight structural validator and templated writer, **not** an LLM scriptwriting engine. No evidence actually comes from the real world; an invented source ID is not verification. String-level topic matching does not prove full semantic invariance. Names for author and reviewer do not prove an independent human actually reviewed. The code does not implement full typed data contracts or a comprehensive A00–A10 production system. No security sandbox, operating-system network prohibition or copyright rights-custodian assessment was independently certified.

## Requirements

Node.js **18+**; no `npm install`, packages, API keys, accounts or external connectivity required to run. Git is optional if downloading a GitHub branch ZIP instead.

## Quick start on Windows PowerShell

1. Clone the isolated branch. (This initial download uses the internet; **running the prototype itself is offline**.)

```powershell
git clone --single-branch --branch build/offline-synthetic-mvp-v01 https://github.com/crimestory5694-beep/universal-scriptwriting-research-hub.git
cd universal-scriptwriting-research-hub\prototype\offline_synthetic_v01
```

2. Run actual local Node test runner:

```powershell
node test_engine.mjs
```

Expected: `PASS 37 / 37 offline synthetic execution checks.` This is **36 scenario tests + one positive baseline**, not production certification.

3. Run a local synthetic draft:

```powershell
node cli.mjs sample.json generated_result.json
```

Open `generated_result.json` to inspect the three-section fictional draft, trace IDs, HOLD reasons, and fixed no-release flags. The checked-in `demo_result.json` is one saved execution result.

4. For a negative test, change `"request_release": false` to `true` in a COPY of `sample.json` and invoke CLI with the copied filename. Expect exit code 2, `HOLD_NOT_APPROVED`, and `artifact: null`.

## Files

| File | Actual use |
|---|---|
| `RESEARCH_FREEZE.md` | Pins historical research to Wave 8 checkpoint, prevents more batch collection |
| `engine.mjs` | Real pure-JS mock function `evaluate(doc)` |
| `cli.mjs` | Local file-in/JSON-out runnable Node CLI |
| `sample.json` | Fiction-only positive scenario |
| `test_cases.json` | 36 independent source-light QA design fixtures |
| `test_engine.mjs` | Executable Node runner for all 36 fixtures plus baseline |
| `demo_result.json` | Saved actual synthetic 80-word draft output |
| `TEST_EXECUTION_RECEIPT.json` | Exact fetched Git blobs and 45/45 V8 checks (36 + 8 supplementary + baseline) |

## Verification record and method

A fresh V8 evaluation executed **45/45 successful checks** directly against the pure `evaluate` function re-fetched from the GitHub branch, along with the exact JSON fixture/test matrix. Read `TEST_EXECUTION_RECEIPT.json` for exact object IDs and execution boundaries. This is actual code execution in a JS isolate, but **the Node.js CLI and `test_engine.mjs` had not been launched as Node subprocesses** in that receipt. The local Node commands above are the reproducibility path and should be run in the intended machine environment. Their syntax was checked after normalizing module-only constructs.

## Freeze and nonauthorization boundaries

- Frozen base main: `0776afd52001c2d9021b1749f7b936bc1dc4e37d`.
- Frozen Wave 8 research head: `0416f7bcbd2cb939fb95aafb09afa63d258116dc`.
- All implementation work is only on `build/offline-synthetic-mvp-v01`; original GitHub research is untouched, and no unmerged Wave 8 worker files were copied into this branch.
- AP-00 still pending; formal AP-01/AP-02 rights/Claude grants remain NOT_AUTHORIZED, `source_copy_manifest: []`; G17/G18 HOLD.
- This prototype is a standalone zero-source proof of concept in response to the owner's freeze-to-build direction, **not** a claim of a signed formal authorization for an external Claude implementation.
- No production `SKILL.md`, real weather/disaster/conflict reporting, real media, human research or retention-effect claims.

## Next actual product milestone (not another research batch)

Build an *owner-authorized* independent implementation of a full-length script drafting module (outline → section budgets → several-thousand-word drafts), while preserving source/claim citations and gate traceability. Add reproducible integration tests for full-length output, source revision invalidation, title/topic semantics, and modular reviewer workflow. New research is opened only for a specific failing test or a genuine blocking evidence gap.
