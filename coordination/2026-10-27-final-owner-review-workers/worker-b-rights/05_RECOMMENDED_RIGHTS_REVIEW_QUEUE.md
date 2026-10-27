# File-by-file rights custodian review queue — priorities, NOT permissions

**NO FILE IS OWNER-APPROVED FOR CLAUDE TRANSFER**

**Queue-only recommendation:** choose the minimum implementation context before seeking transfer rights. It is appropriate to review the five originals if Option A is desired, but none is approved. PR #10 F02D is separate and optional. Legal/custodian determinations belong to the actual rights controller, not Worker B.

| Priority | Candidate | Why review | Exact SHA256 | Intake outcome now | Required next action |
|---|---|---|---|---|---|
| P0 | F07 | Core architecture and scope boundary | `f8088f0831fa7f23a2a0c9f71d924ea7d5478db573ebc3bf7ac110d56b42dd8b` | RIGHTS_UNRESOLVED | Authorship/control and protected-expression scan |
| P0 | F08 | Rights-aware source/claim interface contracts | `bc30a495e5e445b69b38e41eb20190b695e9fe95cd7084aa64ad8a00173a47bb` | RIGHTS_UNRESOLVED | Interface/library attribution and exact reuse terms |
| P0 | F10 | Hard HOLDs, independence and evidence rules | `e7720f7320b832dc24c66861f7e46fa5c3ca12ac03ce7575f5b15fba01ad382c` | RIGHTS_UNRESOLVED | Verify scientific-source/methodology boundary and legal origin |
| P1 | F12 | 36 original QA identifiers, DESIGN_ONLY | `012d11ac37464f3aacc4b9414f184f160b392fdf051e808cfda21f19d8583aa4` | RIGHTS_UNRESOLVED | Authorship of QA prose; no fabricated test PASS |
| P1 | F09 | Five niche policy overlays, largest source | `713d2a5f069d975d64afb376b04e8ded7e7ddc4e5ac559aaabfb2faf88597b48` | RIGHTS_UNRESOLVED | Review cited agencies/history source obligations, scenario paraphrases |
| P2 OPTIONAL | F02D, PR #10 only | 48 metadata IDs/statuses, not needed for mock code | `771163edf744f896ef209a694a156a59c31872c77d5439dd484315232303da23` | RIGHTS_UNRESOLVED | Rights for remaining metadata, exact recipient and AP-02 if proposed |

### Rights custodian workflow
1. For **each** reviewed row, record legal owner/creator, original drafting provenance, third-party expression/code/quotes and licence or exception basis; do not treat Git commit attribution as legal authorship.
2. Confirm exact original path, source commit, Git blob SHA-1, independently calculated SHA-256 and UTF-8 byte count. A changed byte creates a new candidate needing review.
3. Separate (a) permission to view the source, (b) permission to reuse/copy content, (c) permission to copy into the *named* separate Claude workspace, and (d) downstream publication rights.
4. Record allowed recipient, purpose (read-only, limited synthetic mock), storage/security, scope, date/expiry and revocation. Unknown => HOLD; qualified/sanitized replacement => new revision and fresh audit.
5. Request **owner AP-02 exact-file manifest**, in addition to separate **AP-01** only if prototype work was actually approved; maintain F11/F13 restricted scope and G18/G19 stop rules.

### Explicit nonqueue
Original F02; F11 plus 13 linked bodies; F13 original control; private EDU/transcripts; S08 and unresolved S31/S39/S40; blocked R052; B70–B72 missing/surrogate; F-190/K029–K031 efficacy; participant data/private analytics. They are **not pending implicit inclusion**.

**No approval form is preselected or signed.** Custodian may clear, require sanitized replacement, or deny each exact file; owner decides permitted scope separately.
