# Supplement — QA & Integrity Results

**Test-design package checks only**. 26 PASS / 0 FAIL. These checks verify file structure and conservative evidence labeling, **not** candidate effectiveness, research approval, an experiment or a completed source fact-check.

- Preserved: 63 S; 90 historical F; 171 R; 12 V; 336 source records; 48 K; 12 A; 15 P.
- New design-only records: 13 T protocols; 16 four-category rubric dimensions; 9 cost/access rows.
- Original F verdict distribution: 20 PASS, 63 CONDITIONAL, 2 UNVERIFIED, 5 FAIL. Derived historical closure not overwritten.
- Input corrected synthesis ZIP SHA-256: `b7f1cfbefaeabdb514eb8a200e49d87a56f1780d13dfe43bfa4a98d22630f20c`.
- Read-only copy SHA-256: `b7f1cfbefaeabdb514eb8a200e49d87a56f1780d13dfe43bfa4a98d22630f20c`.
- K primary proposed triage counts: {'PROFESSIONAL_ETHICAL_METHOD_REQUIREMENT': 11, 'SOURCE_FAITHFUL_CONTEXTUAL_REVIEW': 12, 'UNTESTED_EFFECTIVENESS_HYPOTHESIS': 18, 'DESCRIPTIVE_CAPTION_PATTERN': 5, 'EMPIRICAL_RESTRICTED': 2}.
- Nothing tested, no data collected, no human subjects, no owner Analytics queried.

## Individual file QA

| Check | Machine result | Detail |
| --- | --- | --- |
| Q01: Read-only original input copied byte-for-byte | PASS | b7f1cfbefaeabdb514eb8a200e49d87a56f1780d13dfe43bfa4a98d22630f20c |
| Q02: Master corpus = 336 | PASS | 336 |
| Q03: Master source slot types 63 S/90 F/171 R/12 V | PASS | Counter({'REAL_WORLD_SOURCE': 171, 'GITHUB_ORIGINAL_FINDING': 90, 'GITHUB_SOURCE_SLOT': 63, 'YOUTUBE_VIDEO_CASE': 12}) |
| Q04: Historic 90 F verdict distribution immutable in source | PASS |  |
| Q05: 48 unique K records, precisely K001–K048 | PASS |  |
| Q06: 15 unique P records, precisely P01–P15 | PASS |  |
| Q07: 13 unique T records, precisely T01–T13 | PASS |  |
| Q08: 16 dimension rows across 4 categories, weights sum to 100 | PASS |  |
| Q09: All 48 candidates have source and testing links | PASS |  |
| Q10: Every T ID linked from K exists | PASS |  |
| Q11: Every P ID linked from T exists | PASS |  |
| Q12: Every full protocol field populated | PASS |  |
| Q13: K031 F-190 is relation-only and R163 only positive | PASS |  |
| Q14: K043 R052 relation-only; R145 positive only | PASS |  |
| Q15: R163 non-support for K011 K019 K029 K044 | PASS |  |
| Q16: No K ID classified positively as supported by unverified F-190 | PASS |  |
| Q17: No K ID classified positively as supported by blocked R052 | PASS |  |
| Q18: P06 deferred separately to owner-only retention | PASS |  |
| Q19: Original V cue/audio decision class D maintained | PASS |  |
| Q20: No human test status marked executed | PASS |  |
| Q21: Rights and cost design has A/B/C/D rows | PASS |  |
| Q22: No production SKILL.md artifact | PASS |  |
| Q23: A03/A04 remain unmapped in source | PASS |  |
| Q24: Markdown references do not introduce unknown existing IDs (prospective V13+ is explicitly deferred) | PASS | [] |
| Q25: No premium retrieval endpoints or external writes used in design | PASS | Offline based on provided archive only; manual procedural assertion |
| Q26: Source package same hash as copied read-only version | PASS |  |

## Limitations

Automated identity checks cannot authenticate each historic source's copyright, primary citation quality, human reviewer independence, content meaning, actual spoken comprehensibility or YouTube performance. A separate independent Research Director review remains essential, especially for the K031/F-190 and K043/R052 exceptions, source license/access and the preliminary scoring thresholds.

The `13_OUTPUT_SHA256_MANIFEST.csv` contains hashes of all payload files *except itself*. The read-only input archive is hashed as a payload member. The outer ZIP's detached sidecar `.sha256` is created after finalizing ZIP bytes, so it is not part of the archive and has no circular self-hash.
