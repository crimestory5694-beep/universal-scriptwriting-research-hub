# Rights Custodian — File-by-File Evidence Checklist

**DRAFT — NOT SIGNED — NOT AUTHORIZED**

**Role constraint:** this checklist is for a real authorized rights custodian, counsel if needed, and an independent owner. Worker H performs documentation preparation only and does **not** attest original authorship, copyright ownership, licences, privacy compliance or external-transfer legality. The existence of a file, Git hash, public URL or AI-generated prose is never a copyright licence.

## Minimum gate for EACH proposed copy
Create a distinct signed review packet for each selected immutable file. A file must **stay `RIGHTS_UNRESOLVED / NO_TRANSFER`** unless *all* necessary evidence, signatories and AP-02 allowlist details are complete.

- [ ] Exact **full origin** repository and path: __________
- [ ] Exact immutable Git commit (40 hex) with verified file membership: __________
- [ ] Git blob SHA-1 recomputed/matched from bytes (not merely commit hash): __________
- [ ] Independent SHA-256 from downloaded **exact** UTF-8 bytes, with method/tool and reviewer: __________
- [ ] Exact UTF-8 byte count and byte-for-byte read-back, plus BOM/line-ending behavior if relevant: __________
- [ ] File identifier and version, date/custodian, no mismatched aliases: __________
- [ ] Documented human/legal author(s), assignment or contract, publisher, custody and permissions: __________
- [ ] Third-party embedded quotations, licensed data/tables, diagrams, schemas, copied prompts, code or fixtures inventoried: __________
- [ ] Source-by-source licence terms (redistribution, sublicensing, attribution, derivatives, commercial use, territorial/expiry restrictions): __________
- [ ] Permissions allowing **exact external copy to named Claude recipient/workspace**; access/read permission alone is insufficient: __________
- [ ] Public/private confidentiality, personal data, sensitive-source, credentials and third-party processors review: __________
- [ ] Original content contamination review (e.g. source-rich records, past scripts or third-party prose accidentally embedded): __________
- [ ] Explicit scope/restrictions in recipient's destination and human acknowledgement: __________
- [ ] Legal/rights verdict: [ ] VERIFIED FOR IDENTIFIED READ-ONLY COPY [ ] NEEDS REWRITE [ ] REJECT [ ] HOLD. None selected.
- [ ] Independent rights-custodian name/authority/signature/time: __________
- [ ] Independent owner AP-02 per-file countersignature/time: __________
- [ ] Effective date, mandatory expiry, revocation mechanism, recipient deletion/audit evidence: __________
- [ ] Post-rewrite *new* SHA-1, SHA-256, byte count, review and AP-02 (old attestation never auto-inherits): __________

## Candidate-by-candidate queue — NOT an authorization list
| Candidate | Exact identity context | Specific review question | Present transfer verdict |
|---|---|---|---|
| A:F07 | main `0776afd...`, Git blob `803f2d87969f1610d742110b8287ef3f31667434`; 8,275 prior recorded UTF-8 bytes | Architecture diagrams/module wording and inherited third-party expression/rights | RIGHTS_UNRESOLVED |
| A:F08 | same main, blob `cfbd1340f747ff658e67b9e88bd956c472ad4165`; 7,718 prior bytes | Interfaces/gate contract wording, field schemas, licence and permitted external copy | RIGHTS_UNRESOLVED |
| A:F09 | same main, blob `04c208fda0872ada977d2406d299f54c318a0e32`; 11,287 prior bytes | Niche overlay source lineage, nontransferable sections and copyright | RIGHTS_UNRESOLVED |
| A:F10 | same main, blob `33618d7e1905c4fa71730fe46fca17b9883f9cde`; 9,503 prior bytes | P0–P10 reason maps, external expression and nonwaivable safety language | RIGHTS_UNRESOLVED |
| A:F12 | `worker-deliverables/skill-architecture/2026-10-27/06_ACCEPTANCE_TEST_MATRIX.csv`, same main, blob `88e89ee233c967c5b8a0b645b0d401f6c1d2ccea`; 4,754 prior bytes | Original QA36 cases, possible inherited fixture wording, redistribution terms | RIGHTS_UNRESOLVED |
| B:B1 | PR12 `research/ap00-option-b-owner-decision-ready@1e496c994835742bfdd63ffac0679ba8123e1734`, `coordination/2026-10-27-ap00-source-strategy-option-b/02_OPTION_B_SOURCE_LIGHT_MOCK_SPEC_V01_PROPOSED.md`, blob `b8d477e00a965862bb6e3ac3ece6b1e00cecd5bb` | Newly phrased derivative expression; origins, independent redraft evidence, technical completeness (Worker D), content rights (Worker B) | RIGHTS_UNRESOLVED |
| B:B2 | same PR12 commit, `coordination/2026-10-27-ap00-source-strategy-option-b/03_OPTION_B_QA36_SOURCE_LIGHT_COVERAGE.csv`, blob `8055702ab7fab28619c565dc21defd7ba22be79b` | Historic QA IDs vs protected fixture phrasing; fresh expression rights (Worker C) **and** case-level semantic fidelity (Worker F) | RIGHTS_UNRESOLVED |
| C:new | File(s) not yet identified | Genuine independent authorship, clean-room provenance, separate engineering/safety/QA review; no original research-file copying | NOT_PREPARED / NO_TRANSFER |

**Important:** Original A file paths and independent SHA-256 values are recorded in the prior rights-review ledger. At AP-02 signing time every path, digest and byte count **must be freshly checked from pinned immutable objects**, not accepted blindly from this queue. New B1 and B2 also require independent verification at the instant of authorization. B has *two distinct* decisions; clearing one never clears the other.

## Default exclusions and HOLD evidence
- **No recursive source acquisition:** F11's 13 link targets, original F11, F02 original, internal F13; unreviewed S/F/R/V/K/EDU archives; protected original transcripts and screenshots; copyrighted scripts; third-party scientific PDFs; restricted S08 source code; private data/credentials.
- Blocked R052 and F-190 are not upgraded to support; K029–K031 remain quarantined; missing B70–72 exact archive, nine disputed EDU hash cases, and uncertain studies remain caveated.
- Rights custodian explicitly reviews derivative provenance: reducing or paraphrasing original wording is not, by itself, a guarantee of lawfulness or licence to share.
- Any custody conflict, unverifiable authored portion, scope change or ambiguity => HOLD; either remove that file, seek permission or produce an independently reviewed replacement.

## Ready-to-sign one-file verdict stub — ALL BLANK
File ID: __________    Owner-selected strategy: __________

Full origin repository/path: __________   Pinned commit: __________

Git blob SHA-1: __________   Independent SHA-256 + method: __________   UTF-8 bytes: __________

Legal author/control evidence: __________   Embedded material/third-party permission evidence: __________

Disposition / exact use allowed / geographic or contractual restrictions: __________

Recipient and Claude workspace: __________   Read-only purpose: __________   Expiry/revocation: __________

Rights custodian verdict, authority, signature/date: __________

**Independent owner AP-02 file approval**, authority, signature/date: __________

**Until both actual decisions are complete:** `NO_TRANSFER` and allowlist `[]`.
