# Independent worker continuation handoff - history-recovery

**Scope completed here:** inspected original S4 ZIP chain and separately available loose original parent, 10 frozen section hashes, B25, P3-B06 manifest, and B58 source fragment. Publication on dedicated `research/history-recovery` branch ONLY. No merge to main, no other-worker edits, no canonical ID changes, no production SKILL.md.

**Current verified judgment:**
- 65/65 distinct nested ZIP CRC checks PASS.
- Exact B70-B72 historical private ZIP 15,051,407-byte / SHA256 `5df730958eccdce94a99643e8b8e0f5f81d552146bc4cf2cb026a56eef84b6d6` not found; 14,990,802-byte surrogate must remain labelled as reconstructed and non-identical.
- All ten frozen EDU-SRC0138..0147 per-section SHA256 checks PASS using the full-source-section convention; nine former disputes are explained by body-only versus entire-section hashing. No frozen SHA edited; independent director acceptance remains pending.
- Historical B25 claimed SHA unlocated; actual archived ZIP `88358c15...` has valid CRC and 11/11 internal manifest checks.
- P3-B06 manifest self-hash mismatch remains documented; other 12/12 checks PASS, solution is external append-only witness, not rewriting original.
- B58 173-byte original source verified but incomplete; original native A/V and any unsupplied continuation NOT_VERIFIED.

**Controller next actions:** review exact section-boundary convention and 10-row hash matrix; accept or contest the nine-hash explanation with independently obtained physical parent; recover exact original B70-B72 ZIP by expected SHA from a trustworthy owner-held copy, do not replace with surrogate; compare claimed versus observed B25 archive bytes if a second historical version is found; maintain external detached witness for B06 self-hash; procure rights-cleared full source for B58 only if it exists.

**Hold:** official 3,051 claims and 104/162 milestone not changed; external postfreeze staging remains separate; T01-T13 NOT_EXECUTED; SKILL.md NOT_AUTHORIZED; no scientific approval. This report is not a merge instruction or an owner decision. For exact artifact verification, see branch commit SHA and remote readback receipt.
