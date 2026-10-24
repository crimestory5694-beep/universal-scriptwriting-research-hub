# Educational Batch Public-Safe GitHub Packaging Workflow

**Effective:** 2026-10-24. **Scope:** all subsequently executed `EDU_REAUDIT_Bxx` historical research batches in the public research hub. Do not interpret this document as an active autonomous background process.

After executing each actual source research batch:
1. Preserve its full detailed research package separately with all original historical inputs, exact source SHA-256 records, claim IDs and QA addenda. Reuse rights and access controls apply; do **not** automatically publish original copyrighted transcripts or source-dense copies.
2. Publish the batch's publication-safe, researcher-authored reports and safe claim/QA summaries to `tracks/07-educational-transcript-batches/historical-batches/EDU_REAUDIT_Bxx/`. Preserve old versions/IDs, append rather than silently overwrite.
3. Create `EDU_BATCHxx_PUBLIC_SAFE_GITHUB_ARCHIVE.zip` from those **already published, rights-filtered** files with a clear README distinguishing the derivative archive from the full original bundle.
4. Commit the ZIP **as a binary file** using the GitHub Git Data blob/tree/commit flow with a non-forced branch update and expected branch head. Do not use text-only file creation for binary.
5. Fetch current GitHub `main` tree, check the ZIP's blob SHA and byte size, fetch base64 blob bytes and verify internal entry CRC/inventory. Record the actual commit SHA and missing/withheld original artifacts.
6. Update `coordination/TRACK_STATUS.md` with reviewed sources, pending first-time/QA units, next claim ID, next source IDs, exact GitHub paths, and an explicit PUBLIC_RIGHTS_LIMIT.
7. **Never claim** the complete original research ZIP was uploaded merely because the filtered ZIP has been archived. Full original transfer requires a separately permitted destination and demonstrated redistribution rights.

**Existing completed example:** [Batch 17 verified publication-safe ZIP](../tracks/07-educational-transcript-batches/historical-batches/EDU_REAUDIT_B17/06_PUBLIC_SAFE_ZIP_RECEIPT.md).

This standard is a workflow instruction for each next user-requested execution; it does not initiate unattended uploads on its own.
