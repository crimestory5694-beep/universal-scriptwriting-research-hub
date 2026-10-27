# Minimum affirmative evidence needed before any exact-file AP-02 request

**NO FILE IS OWNER-APPROVED FOR CLAUDE TRANSFER**

This is an unsigned evidence-request template; it **does not** issue permission, attest copyright or create a destination. **AP-01 isolated synthetic mock coding and AP-02 research-file copying are independent gates.**

## Required custodian decision per file
| Evidence field | Required content and why |
|---|---|
| Identity/version | F07/F08/F09/F10/F12 or optional F02D; full Git path, source commit ref, Git blob SHA-1, independently verified SHA-256, UTF-8 byte size |
| Creator & chain-of-title | Actual writer(s), contractual assignment/work-for-hire or other legal basis, prior source-writing provenance; GitHub account alone insufficient |
| Embedded third-party expression | Inventory exact passage/code/example/diagram if any, original author/publisher, whether paraphrase or substantively copied, documentary locator |
| License and attribution | Specific applicable terms, permitted copying/derivatives/redistribution, obligations (attribution, notice, noncommercial restrictions), exceptions if counsel confirms |
| Privacy and confidentiality | Actual reviewer checks for personal identifiers, participant records, private analytics, credentials, nonpublic customer/research content |
| Distinct usage rights | Reading/analysis versus exact copying/reproduction versus external Claude workspace import; publication/deployment rights are not implied |
| Named target | Exact separate Claude workspace/repository/branch, developer/operator, organization/account, restricted purpose and access controls |
| Time and accountability | Named custodian, dated signed result, expiry, revocation path, limitation/conflict notes; separate named project owner AP-02 authorization |
| Technical/version safeguards | All safety holds preserved, no F11 follow-link imports, origin F13 gate enforced internally, no executable code/test result claimed |

## File-specific evidence prompts
- **F07** (`f8088f0831fa7f23a2a0c9f71d924ea7d5478db573ebc3bf7ac110d56b42dd8b`): Custodian attestation on proposed prose, examples, conceptual method dependencies and reuse rights.
- **F08** (`bc30a495e5e445b69b38e41eb20190b695e9fe95cd7084aa64ad8a00173a47bb`): Attest authorship and any borrowed API/schema/notation text; resolve license/attribution, and v0.2 crosswalk separately.
- **F09** (`713d2a5f069d975d64afb376b04e8ded7e7ddc4e5ac559aaabfb2faf88597b48`): Confirm original wording, policy-summary sources, external attribution, jurisdictional applicability and hypothetical-only status.
- **F10** (`e7720f7320b832dc24c66861f7e46fa5c3ca12ac03ce7575f5b15fba01ad382c`): Attest rule-language origin and any incorporated external methodology/excerpts; preserve R079/R163/F-190 limitations.
- **F12** (`012d11ac37464f3aacc4b9414f184f160b392fdf051e808cfda21f19d8583aa4`): Attest exact fixture-language authorship and approval to copy the 36 original-ID expectations; no executed-test inference.
- **F02D** (`771163edf744f896ef209a694a156a59c31872c77d5439dd484315232303da23`): Custodian attest metadata-label authorship/reuse, provenance from F02, license scope and specific purpose; optional only, original F02 not included.

## Template — intentionally blank/unapproved
```text
File ID: __________
Exact source Git path/ref: __________
Git blob SHA-1 / verified SHA-256 / UTF-8 bytes: __________
Named creator/control evidence and chain-of-title: __________
Third-party passages/codes/links, license, attribution: __________
Privacy/credential/confidentiality review by whom/date: __________
READ allowed? ______ REPRODUCE allowed? ______ COPY_TO_CLAUDE allowed? ______
Approved destination repository/workspace/branch: __________
Permitted use and restrictions: __________
Custodian signed identity / timestamp / decision / expiry: __________
Owner AP-02 signed identity / timestamp / exact-file decision: __________
AP-01 isolated mock build approval (separate): __________
Revoke/retain/dispose terms: __________
```

When any required evidence is missing, disposition stays `RIGHTS_UNRESOLVED` or `EXCLUDE`; no imported bytes. If author-created option B/C documents replace sources, each new artifact requires its own origin/reuse assessment and SHA256. **Do not assume the user message authorizes a transfer.**
