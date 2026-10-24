# 03 — Transcript Provider and Cost Verification

## Scope and outcome
No transcript extraction API (including vidIQ, Nexlev, Supadata, TranscriptAPI, or the user's connected `yt_research_server2` tool) was invoked during **this repair run**. Public web transcript pages and read-only GitHub source files were inspected. **No new paid transcript API request was deliberately made in this turn.** Whether a downstream site paid to render its pages is not auditable here.

## Prior-pilot evidence and code-level verification
1. The original 12-video pilot `10_SOURCE_METHOD_AND_RIGHTS_NOTES.md` documents V01/V04 captions retrieved via vidIQ and own server, and V07/V10 via `yt_research_server2`. It records returned `full_transcript` fields without `segments`, and an original response-provided `source: supadata.ai` for the own-server route; it also notes vidIQ credits exhausted, Nexlev quota exhausted, Gemini rejected. These are **previous-run records**, not fresh service-log observations.
2. The user's repository, `crimestory5694-beep/yt-research-server`, **default/main** `main.py` `tool_get_video_transcript` (roughly lines 651–760) tries **TranscriptAPI.com first, Supadata.ai second**, then direct YouTube captions. Its Supadata success branch explicitly labels `source: supadata.ai` and returns `full_transcript` in the same legacy shape seen in the pilot. **Thus free-first was NOT established by these old responses.** Code can explain the response but does not certify the exact deployed commit, current runtime environment, or invoicing.
3. The distinct reviewed branch `claude/charming-babbage-mo3ags` has `transcript_service.py` implementing **cache → YouTube direct → yt-dlp → proxy → optional TranscriptAPI/Supadata**, default `ENABLE_PAID_TRANSCRIPT_APIS=false`; its richer outputs can contain `status`, `source`, `cached`, `segments`, `attempts`. **Code does not prove that this branch was live on Render when earlier pilot transcripts were retrieved.**
4. The legacy response explicitly naming Supadata means a **Supadata-sourced transcript was returned** in the prior pilot. Under the legacy function, that is evidence a Supadata request may have been invoked. **Whether any fee was billed, a free allowance was used, a cached result was returned by an intermediate layer, or which endpoint build executed remains UNKNOWN without Render logs, provider usage ledgers and deployment version.**

## Audit conclusion
- `REPAIR_NEW_PAID_CALLS`: **NONE INITIATED**.
- `PRIOR_RESPONSES_PROVIDER_LABEL`: **SUPADATA.AI OBSERVED**; cannot certify no external paid API call in previous pilot.
- `PRIOR_ACTUAL_BILLING`: **UNVERIFIED**.
- `DEPLOYED_RENDER_BUILD_SHA/BRANCH`: **UNVERIFIED**.
- `PRODUCTION_FREE_FIRST_POLICY`: **NOT DEMONSTRATED** despite improved branch implementation; do not state it as proven.
- `NEW_TIMED_SOURCE_V10`: static public English subtitles mirrored on a third-party website; vendor-side acquisition route and costs unknown, **no API charge authorized or requested by analyst**.

## Zero-charge runtime attestation still required (read-only)
- Record Render deployed commit SHA and branch of the exact `yt_research_server2` endpoint, not just GitHub's latest code.
- Record *redacted* Render environment flags: `ENABLE_PAID_TRANSCRIPT_APIS`, enabled provider order, `SUPADATA_API_KEY` **presence only (not key)**, `TRANSCRIPT_API_KEY` presence only, cache mode, `RUN_TRANSCRIPT_PROBE_ON_STARTUP`.
- Preserve request-correlated Render logs for V01/V04/V07/V10 **as already issued**, including cache hit, provider attempts and any `supadata` / `transcriptapi` usage counters. Read logs only; do not probe/pay to recreate records.
- Reconcile Supadata and TranscriptAPI provider-dashboard usage entries and invoices/credits for the dates of the prior pilot. A plan's free allowance is not proof a third-party API was not invoked.
- Add explicit per-request provider audit provenance to future exports (`provider_chain`, `origin`, `cached`, `paid_call_attempted`, `paid_call_charged` if supplied by provider, timestamped-caption availability). Never infer spend from `source` alone.

**Evidence URLs (read-only GitHub code):**
- https://github.com/crimestory5694-beep/yt-research-server/blob/main/main.py
- https://github.com/crimestory5694-beep/yt-research-server/blob/claude/charming-babbage-mo3ags/transcript_service.py

**Security note (out of research scope, no secrets copied):** The legacy public `main.py` contains a default literal for an API credential. This should be treated as potential credential exposure and rotated independently; no values reproduced here.
