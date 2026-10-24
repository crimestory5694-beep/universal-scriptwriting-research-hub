# CURRENT STATUS — Source provenance decision

**EDU-B11-UNINDEXED-01 = RESOLVED TO EXISTING HISTORICAL SOURCE EDU-SRC0162. No EDU-SRC0163 has been assigned.**

The original full-file SHA-256 is `99cff8c6319d265d6d57b4714645ef2b24a62d18f153be774832a1a1f2b0dc02`. The omitted text `[282999,315539)` (32,540 decoded normalized characters) has SHA-256 `e89d968314ea3cb5bd98d76c7fe1420661b7ac05a54f679adfcc6f6f2f080bab`, as recorded by Batch 11. Its structural segmentation is:

- `[282999,299268)` — first transcript, 16,269 characters, source hash `59dbc78a69c41e1c4e60df05e5566f14194c3ee0dec726e952d24ce6e2c20479`, corresponding raw byte interval `[424784,466509)`.
- `[299268,299270)` — two LF separators, not an educational source.
- `[299270,315539)` — repeated identical transcript, 16,269 characters, same SHA, corresponding raw byte interval `[466513,508238)`.

**Complete raw-byte identity was verified**: each 41,725-byte segment matches the original UTF-8 encoding of the other, so this is not merely title similarity. Both are existing historical `EDU-SRC0162` source copies, and the source inventory already has that exact hash and title `Voiceover guidance recording 10 / copy 1`. The inventoried source was pending extraction until this batch; only after the complete 16,269-character first-copy reading and source-located knowledge extraction can second-copy coverage legitimately reuse that processing. The original physical text and all 162 historical IDs are unchanged.

The 12 historical transcript ZIP archives and 266 archive entries, 137 distinct SHA-256 versions and 129 additional exact archive copies are preserved unchanged. Reconciliation of two **within-loose-document** copies does not reclassify the historical ZIP-archive inventory numbers. A 160-character probe partial-overlap screen was run against accessible ZIP members to flag candidates; it is not a proof of cross-language semantic equivalence and cannot justify excluding nonmatching documents.
