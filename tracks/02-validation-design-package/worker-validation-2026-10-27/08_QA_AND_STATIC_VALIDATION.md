# Structural QA checklist and reporting rules
State at authoring: planned tests are NOT_EXECUTED. A separate GitHub read-back receipt is appended after upload.

## Structural checks to perform on actual uploaded bytes
QA-01: folder contains exactly one operational row for T01,T02,...,T13, no duplicates; each has requirement/comparator/role/outcome/prospective acceptance/stop status.
QA-02: eight A1 case slots identical to accepted H01,H02,A01,A02,W01,W02,P01,P02; all initially CONDITIONAL/NO authorization.
QA-03: rubric weight sums exactly 100 per category; 16 dimension IDs unique across four contexts; ordinal anchors 0..4.
QA-04: separate fact/safety gate; 0 != NOT_CHECKABLE or missing; confidence/uncertainty not hidden by a percentage.
QA-05: all planned T execution status NOT_EXECUTED, no synthetic ratings represented as measurements.
QA-06: B listener, C Analytics and D native media are separately gated, never converted to A1 automatically.
QA-07: source-role quarantine for R052, F-190, R079/R163 scope, non-audio-caption inferences and outdated forecasts preserved.
QA-08: all published text original and public-safe: no copied copyrighted transcripts, raw case manuscripts, financial/private data or credentials.
QA-09: GitHub readback identical to uploaded strings, compare blob SHA and computed local SHA256 if supported; report every path failure.
QA-10: no changes to main, coordination/, sibling tracks or existing historical files; compare only new task-folder paths.
QA-11: no unexpected ZIP. If none was created, ZIP CRC/integrity = NOT_APPLICABLE, not PASS.
QA-12: manifest covers all first-wave deliverables with actual SHA256 and byte counts; self/receipt excluded to avoid circular metadata.

## QA outcomes vocabulary
STATIC_PASS = schema/number/rights scan passed; NOT experimental pass.
STATIC_FAIL = specific structural assertion failed, repair via new version and recheck.
NOT_CHECKED = never claim pass for this row.
READBACK_PASS = identical fetched bytes/hashes on GitHub branch.
RIGHTS_PUBLIC_SAFE = original operational text and references only; access permissions for underlying manuscripts still unknown.

## No scientific certifications
Static checks can establish only internal consistency and reliable upload. They cannot establish real-case rights, historical fact correctness, German narration behavior, participant accessibility, inter-rater agreement, cause of YouTube retention, population generalizability or efficacy of K hypotheses. Never show static QA as T01-T13 execution.