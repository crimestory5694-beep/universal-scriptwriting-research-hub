# Track 07 — Research Completeness and Public-Archive Integrity Audit

**Audit boundary:** historical educational transcript extraction chat, original Batch 01–14. **Result:** `PARTIAL` — original research remains incomplete and the public archive contains only a rights-filtered subset. This is an archival audit, not a fresh claim/source validation.

## Expected versus recovered versus actually verified in GitHub

| Category | Expected/identified | Recovered locally | Byte-identical originals verified on GitHub |
|---|---:|---:|---:|
| All inventoried original research/source files | 293 | 293 | 80 |
| Archived original bytes | 106,450,318 | 106,450,318 | 465,265 |
| Raw source inputs | 16 | 16 | 0 (rights gate) |
| Historical or nested research ZIP files | 14 | 14 | 0 (rights and binary gate) |
| Substantial source-derived research registers awaiting rights review | 101 | 101 | 0 under this class |
| Other research metadata/status files | 150 | 150 | 80 |
| Eligible candidate metadata still not verified as uploaded | 81 | 81 | 0 |
| GitHub-path collisions with **different bytes** | 1 | Original retained | 0 verified; discrepancy open |

Local file byte counts and SHA-256 were computed from actual mounted originals; GitHub exact-byte equivalence uses independently calculated local Git blob SHA plus the GitHub repository tree's blob SHA and size. A repo file path alone never counts as a verified original.

## Historical research completeness (distinct from upload completion)

Last reported Batch 14: 162 historical source identities, 983 provisional educational claims, 40 independently reviewed source units, 116 first-time pending extractions and six historical Batch 01 independent QA obligations. Full educational research is therefore **not complete**. Seven historical stages of repairs and corrections remain append-only. See `CHAT_HANDOFF.md` and the individual dated batch reports.

## Exceptions and restrictions

1. **Publication and copyright:** all original transcript archives, composite transcript files and original historical ZIPs are withheld from this PUBLIC repository absent redistribution rights. Substantial claim registers and teaching extracts are conservatively awaiting file-level clearance; private ownership of a source file does not establish public reuse rights.
2. **One previous incorrect upload:** the public GitHub path `historical-batches/EDU_REAUDIT_B12/00_MISSING_SOURCE_PROVENANCE_AUDIT.csv` has original local blob SHA `79731507f0ac74e0178836c591a24116317e3e7a` and 1,536 bytes, but GitHub stores SHA `4b003d9cfcb42d7ca61e3e4d14e03e7e95ce81f4` and 1,631 bytes (a parsed/reformatted representation). It must not be counted as a recovered original. Do not overwrite/delete the previous GitHub file without a separate explicit preservation decision; an append-only corrected original is preferable.
3. **Failed attempts and ambiguous duplicates:** several initial test uploads were blocked by safety checks, GitHub concurrent-write conflicts, or File-reader formatting differences. Same-named generated attachments may refer to different versions. No unverified version is silently promoted to exact original status.
4. **Historical B03 packaging:** the Batch 02/03 combined ZIP exists; a separately unpacked Batch 03 original directory was not independently recovered in the current filesystem inventory. Its contents must be assessed as embedded historical source materials before any complete archival claim.
5. **Limitations:** source anchors and original audio/video are not independently revalidated by this archival procedure. File hashes demonstrate byte provenance only; the creator's performance claims, scientific explanations and copyright status remain separate questions.

## Gates still open
- Upload or obtain public clearance for the 81 publication-safe candidate originals and review the 101 source-dense historical register files individually; use version-specific paths and verify Git blob SHA for each.
- Resolve the one B12 GitHub/nonidentical-original discrepancy append-only.
- Preserve all protected original bytes offline or in a separately approved rights-cleared private transfer; not in this public repository.
- Complete 116 first-time educational source extractions and six historical re-audits, then run Research Director-level integrity acceptance.
- Reconcile any future recovered original versions against `FILE_MANIFEST.csv` without overwriting historical records.

**Conclusion:** Track 07 public GitHub archival is **PARTIAL**, not `UPLOADED_REVIEW_PENDING` for the whole track, and not `INTEGRITY_VERIFIED`. No final `SKILL.md` or production scripts were made.
