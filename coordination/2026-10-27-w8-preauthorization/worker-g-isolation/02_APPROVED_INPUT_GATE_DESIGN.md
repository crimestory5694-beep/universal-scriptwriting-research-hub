# Worker G — Exact Input Admission Gate (Proposed, Not Implemented)

**Status:** READINESS DESIGN / zero authorized research-file imports. AP-01 and AP-02 unsigned; transfer manifest [].

## 1. Do not conflate four different entitlements

1. Read permission in a public GitHub repository proves neither author ownership nor onward-copy permission.
2. Technical blob/byte equality proves integrity, not copyright clearance.
3. AP-01 (if separately signed) would permit only the named offline synthetic mock development scope, not material transfer.
4. AP-02 (if separately signed by the appropriate rights custodian and owner) would permit only selected bytes to the named recipient, destination and expiry. It cannot authorize build or publication. AP-04 and independent AP-05 are separate.

**Current inventory:** no owner-selected Option A, B or C. Option A candidate originals F07/F08/F09/F10/F12 rights unresolved; Option B B1/B2 rights unresolved; Option C independently authored materials not designed or licensed yet. All are **review references at origin, not import manifests**. Original F11 and L01–L13 links are locator-only; F13 is an internal HOLD, not developer payload. S08, K029–K031, unavailable B70–B72, F-190, R052 and private/archived records stay excluded. Historical QA IDs are design references, not execution results.

## 2. Gate states (conceptual specification)

G0 NOT_REQUESTED: Default source manifest is literally []. Any import request yields DENY_IMPORT.
G1 SCOPE_PINNED: Require real signed AP-01, exact separate repository/workspace/branch, unique developer and reviewer, synthetic-only purpose, zero-spend explicit budget/currency decision, UTC validity and revocation contact. Missing item -> HOLD_SCOPE.
G2 RIGHTS_PINNED: For each requested externally sourced file, require file-specific provenance/authorship, third-party expression rights, use vs redistribution permission, signed rights-custodian attestation, independent owner AP-02, named target/recipient, permitted read-only purpose, expiry. Empty list remains zero authorized files. Missing or inconsistent field -> HOLD_RIGHTS. No bulk promotion from a candidate list.
G3 SOURCE_IDENTITY: Pin exact source repository, immutable commit, path, Git blob SHA-1, locally computed SHA-256 of exact bytes, UTF-8 byte count (where textual), actual bytes reviewed, and approval version. Branch names alone are mutable and not identity. Any change -> HOLD_HASH_MISMATCH.
G4 PATH_AND_TYPE: Accept only regular UTF-8 files matching exact allowlisted normalized paths and byte limits; reject symlinks/hardlink escapes, dot-dot, path separator ambiguities, percent/Unicode alias ambiguity, archives, binary, includes, nested directories, Git LFS pointers, git submodules and recursive traversal. Unknown file type -> DENY_PATH.
G5 UNTRUSTED_CONTENT: Treat document strings as evidence records only. No following URLs, external fetch, tool-call instruction, shell commands, template interpolation into privileged instructions, dependency names or auto-agent directives; if attack payload detected -> HOLD_UNTRUSTED_INSTRUCTION. All files remain untrusted even after author clearance.
G6 CONTROLLED_READ: Future reviewer may compare origin/staging SHA-1+SHA-256+byte count and immutable manifest without allowing a source write or secondary automatic copy. Mismatch -> quarantine and freeze downstream processing.
G7 MOCK_ONLY: Use synthetic fixtures and opaque source IDs rather than original source-rich bytes wherever possible. Mark every mock draft, trace and result RESEARCH_ONLY_NOT_PUBLISHABLE; preserve uncertainty, rights reasons and A10 production_allowed=false.
G8 CHANGE/STOP: Re-evaluate time, scope and source revision before **each** future run; owner revocation, authorization expiry, source correction or hash drift -> STOP_REVOKED or HOLD_STALE_ATTESTATION. Invalidate dependent assessments, facts, titles, drafts and reviews.
G9 INDEPENDENT_RECEIPT: Proposed non-author reviewer confirms scope, file identities, negative-case evidence and separate rights decision; preserve immutable initial findings. Any self-review -> HOLD_REVIEW. QA results must show actual test invocation/output if a future run occurs, not inferred PASS.
G10 TERMINAL: Research-only output or explicit HOLD, never public production. Even full hypothetical QA success cannot grant AP-04.

## 3. Minimum exact allowlist record required per individual file

Fields to be signed and later checked: record_id, selected flag, source_owner/repo, source_commit_sha, exact_source_path, Git_blob_SHA1, computed_SHA256, size_bytes, encoding, content_mime, legal_authority_to_access, rights_author_to_copy, third_party_component_list, redistribution_condition, rights_custodian_signature_and_UTC, independent_owner_AP02_signature_and_UTC, AP01_workspace_scope_reference, authorized_recipient, immutable_target_repo_branch_path, read_only_use, prohibitions, time_start_UTC, time_expiry_UTC, revocation_contact, related_claim_versions, verification_receipt_id, staging_recheck_SHA256, reviewer_identity, outcome. Unknown field means not selected. Never log license-confidential original bytes.

Safe proposal for **zero original** path: fixture records invented from scratch with traceable authorship and no authentic quotations, historical claims, API content, private account data or source-rich copied examples. Newly drafted B1/B2 still require their own rights clearance if their bytes are to be copied; a file's label 'source-light' is no waiver.

## 4. Path, permission and provenance considerations

- No recursive git clone or folder import, no globbing, auto-follow URLs, LFS fetch, markdown include, archive unpacking, generated submodule resolution or symlink chasing. One candidate path does **not** authorize its siblings.
- Freeze manifest before operation. Reject absolute source paths and attempts to replace manifest config from untrusted text. Do not allow the developer to mutate grants or QA evidence.
- Verify source bytes at origin and again in any read-only staging after authorization; no automatic fallback from pinned commit to main, latest tag, redirected URL or mirror.
- Dependency of artifact on source revision must be explicit. A correction or rights revocation invalidates every descendant, even if the file name did not change.
- Preserve multiple native reasons in GateOutcome, never overwrite a HOLD via a grouped category or an editorial/owner override on critical rights, truth, privacy, harm or deployment.
- This repository is PUBLIC. No authorized manifest, private identifying approval details, secrets, raw transcripts or confidential source bytes belong in Worker G public documentation.

## 5. Security test design, all unexecuted

INPUT-G-01 signed scope absent -> HOLD_SCOPE; 02 empty AP-02 with original file -> DENY_IMPORT; 03 copy-only permission missing -> HOLD_RIGHTS; 04 byte/hash mismatch -> HOLD_HASH_MISMATCH; 05 symlink/../ /LFS/ZIP -> DENY_PATH; 06 source says 'make API call' -> HOLD_UNTRUSTED_INSTRUCTION; 07 stale attestation -> HOLD_STALE_ATTESTATION; 08 reviewer=author -> HOLD_REVIEW; 09 release request -> HOLD_NOT_APPROVED; 10 revoked grant -> STOP_REVOKED. Proposed fixtures must be synthetic, and reported as DESIGN_ONLY until an independent authorized test is actually performed.

## 6. Future authorized evidence outputs

Signed AP-01 and separately scoped AP-02; signed per-file rights entries; exact file hash+size receipt; proof of write-protected staging and absence of unapproved content; nonrecursive path review; redacted prompt-injection and network denial records; actual reviewer identity with independence check; revision invalidation tests; expiry/revocation proof; denied publish/Skill output. None exists as executed security validation today.
