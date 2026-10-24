# Multi-chat Upload Protocol (v1)

## Public repository safety and rights gate

The owner has chosen to keep this research hub **PUBLIC** for later retrieval by Claude Code Browser. Public visibility is not a blocker for **publishable, rights-cleared, nonconfidential research reports**. Before EACH file upload, check it can lawfully and safely be published to everyone on the internet.

Allowed, after checking content and rights: original ChatGPT-authored analysis and brief paraphrases; non-sensitive original evidence ledgers, source URLs and research metadata; reports, corrections, manifests, checkpoints, tests or prompts authored for this project.

NOT allowed for public publication without explicit relevant rights/consent: complete or substantial third-party transcripts; copyrighted books/course PDFs; private/paid/proprietary exports; user or third-party personal information; credentials, .env files, tokens, cookies; unpublished confidential research. A private repo would not automatically grant copyright rights either.

For restricted or uncertain items, do not upload bytes: record existence, original filename, hash if genuinely computed, scope, why withheld, and location of the user-held original in the track's manifest. If hash is unavailable, say so. Offer separate local ZIP exports for later permissioned private transfer, with rights respected. Never reconstruct original data from short summaries.

**WARNING:** Public Git history may remain visible through forks, clones or caches even after an item is deleted or repository visibility changes. Do not upload first and attempt to sanitize later.

## Exact destination

Repository: `crimestory5694-beep/universal-scriptwriting-research-hub`
Default branch at setup: `main`.

Each of the six named ChatGPT chats uses **only its allocated** `tracks/0X-.../` path. Educational transcript batch chat uses `tracks/07-educational-transcript-batches/`. Never edit a sibling track, root README, or `coordination/` from an individual chat.

## Archive the *complete* existing work, not just the latest answer

1. Recover accessible deliverables already produced by that chat: all original Markdown, CSV, JSON, reports, source ledgers, audit revisions, ZIPs and checkpoint files (where the chat can lawfully archive them).
2. Preserve the original filename and content in an append-only `source-files/`, `batches/` or `revisions/` subfolder within its own track. If identical versions are duplicated, keep a provenance and equivalence record rather than guessing.
3. For each file, record SHA-256 of actual bytes, byte count, source chat/workflow, original filename, archived repository path, version/batch, creation date when known, and verification status in that track's **own** `FILE_MANIFEST.csv`.
4. Include a `CHAT_HANDOFF.md` with purpose, full chronological progress, counts and statuses *as reported*, source gaps, corrections, limitations, exact continuation checkpoint, and which original inputs are missing.
5. Include `UPLOAD_REPORT.md` with list of actually uploaded paths, GitHub commit hashes, number of successful uploads, failures, items not uploaded and why, and any unresolved authenticity or rights restrictions.
6. Upload reports and accessible bytes; never recreate purported originals from a summary. If the chat lacks GitHub write access or cannot upload a binary/oversized file, report `NOT_UPLOADED` and provide an exact download/export artifact where possible. Do not claim a successful upload from an intended path or locally created ZIP.
7. Prior to any push, inspect for secrets, rights restrictions, and personal data. Publish only files safe for public release. Do not upload Git history, `.env`, credentials, unlicensed raw transcripts or proprietary/private collections; record existence and verification metadata without distributing bytes.
8. After upload, read back important files using the GitHub connector (not just local filesystem) and verify hashes/size wherever supported.

## Collaboration and concurrent writing

- Unique track-folder ownership prevents overwrites between research chats.
- Each chat may use its own branch/PR when available. Do not force-push or rewrite history.
- Files with the same name but different content get distinct versioned paths. Preserve original versions.
- **Only the central Research Director** modifies `coordination/TRACK_STATUS.md`, `coordination/MASTER_FILE_MANIFEST.csv` and the integration gate after verifying GitHub state.
- A chat must never assert the *entire project* is complete based on its own work alone.

## Evidence and integrity

Keep separately labelled: repository/source discovery, source reading, extracted author claims, evidence judgments, candidate hypotheses, editorial tests, scientific validation and final skill implementation. Preserve disputed claims, negative findings and failed checks.

Reported stats from a prior chat are not equivalent to independent source/byte verification. Do not manufacture cross-source proof, audio timestamps, rights clearance, retention/CTR lifts, approvals, or unobserved data.

## Intake completion criteria

An individual track is `UPLOADED_REVIEW_PENDING` only once source files, file manifest, handoff, and upload report have been verified as present on GitHub. `INTEGRITY_VERIFIED` is a separate director-level decision. Overall transfer to Claude Code Browser must not be marked complete until all seven tracks are audited.