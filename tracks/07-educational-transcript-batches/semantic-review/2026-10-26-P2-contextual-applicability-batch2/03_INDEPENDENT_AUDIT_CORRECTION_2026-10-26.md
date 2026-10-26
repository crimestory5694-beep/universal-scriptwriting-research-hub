# Independent P2 Batch 2 audit correction — 2026-10-26

**Verdict:** Private/public ZIP CRC PASS; 6/6 manifest file SHA checks PASS; prior original private B01 archive preserved byte-identical. GitHub Batch 2 public report and metadata match their recorded Git blob hashes. Batch 2 has 100 unique source-qualified decisions over 47 source members with 100 distinct context-specific reasons and safe-use boundaries. The original 495 P2 source keys partition cleanly into 60 B01 decisions + 100 B02 decisions + 335 currently listed pending keys.

**Progress reporting correction:** The 26-record original individual semantic pilot comprises 5 P1, 7 P2, and 14 P3 records based on the preserved original queue assignments. Five of its P2 records were reviewed *again* in B01/B02 and double-counted in previous overall totals. Two further pilot-reviewed P2 keys still appear in the B02 '335 pending' list, although they already have pilot individual review decisions. Keep both original review records; never delete or silently rename them. Report unique review coverage by `staging_key`.

### Corrected unique coverage
| Queue | Unique reviewed | Truly pending |
|---|---:|---:|
| P1 | 128/128 | 0 |
| P2 | 162/495 | 333 |
| P3 | 14/599 | 585 |
| **Overall** | **304/1,222** | **918** |

The dedicated B01/B02 P2 batches still correctly report 160 decisions (60 + 100). The 162 unique P2 count includes two pilot-only records missing from that 160. The prior **309 individually reviewed** total erroneously counts five P2 review activities twice.

**Metadata limitation:** All 100 B02 individual review rows retain `manual_status=PROVISIONAL_AUTO_ROUTING_ONLY` inherited from first-pass triage while a separate completed-review field and actual individual reasons are populated. This is a contradictory-looking status label, not missing decisions. Preserve the original value, and distinguish preliminary automated routing from later individually completed semantic review in downstream views.

Eighteen of the 100 B02 rows still have historical *per-part* source-hash mismatches, relying on verified original composite parent; retain this limitation. No retention-effectiveness experiments verified, new EDU-C IDs created or production Skill approved.

**Publication boundaries:** Original transcripts, source-exact offsets and 30MB private ZIP remain private. This public report includes only integrity checks, anonymous counts and process findings. Original B70–B72 private archive missing; surrogate is not original. T01–T13 unexecuted, B25/B58 issues open.
