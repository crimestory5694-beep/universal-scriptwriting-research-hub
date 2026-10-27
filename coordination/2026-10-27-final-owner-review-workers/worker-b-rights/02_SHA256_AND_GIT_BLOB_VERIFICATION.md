# Six source files — independent UTF-8/SHA-256 and Git blob verification

**NO FILE IS OWNER-APPROVED FOR CLAUDE TRANSFER**

**Method:** GitHub `fetch_file` returned the full textual content at the pinned revision. Independently converted Unicode scalar values to UTF-8 bytes; computed SHA-256 over the exact returned string, not the Git blob name. SHA-256 implementation passed standard vectors: `SHA256("abc")=ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad` and `SHA256("")=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`. GitHub-reported `sha` values are Git blob SHA-1 identifiers, **not SHA-256**. These checks prove retrieved text integrity relative to pinned Git data only, not authorship/rights.

| ID | Exact pinned Git blob SHA-1 | Independently recomputed SHA-256 | UTF-8 bytes | Source ref |
|---|---|---|---:|---|
| F07 | `803f2d87969f1610d742110b8287ef3f31667434` | `f8088f0831fa7f23a2a0c9f71d924ea7d5478db573ebc3bf7ac110d56b42dd8b` | 8275 | `0776afd52001c2d9021b1749f7b936bc1dc4e37d` |
| F08 | `cfbd1340f747ff658e67b9e88bd956c472ad4165` | `bc30a495e5e445b69b38e41eb20190b695e9fe95cd7084aa64ad8a00173a47bb` | 7718 | `0776afd52001c2d9021b1749f7b936bc1dc4e37d` |
| F09 | `04c208fda0872ada977d2406d299f54c318a0e32` | `713d2a5f069d975d64afb376b04e8ded7e7ddc4e5ac559aaabfb2faf88597b48` | 11287 | `0776afd52001c2d9021b1749f7b936bc1dc4e37d` |
| F10 | `33618d7e1905c4fa71730fe46fca17b9883f9cde` | `e7720f7320b832dc24c66861f7e46fa5c3ca12ac03ce7575f5b15fba01ad382c` | 9503 | `0776afd52001c2d9021b1749f7b936bc1dc4e37d` |
| F12 | `88e89ee233c967c5b8a0b645b0d401f6c1d2ccea` | `012d11ac37464f3aacc4b9414f184f160b392fdf051e808cfda21f19d8583aa4` | 4754 | `0776afd52001c2d9021b1749f7b936bc1dc4e37d` |
| F02D | `e64d182ac2ffee416313e5b5905e9f245bfe38a0` | `771163edf744f896ef209a694a156a59c31872c77d5439dd484315232303da23` | 10990 | `PR #10 afa8600bcb62b26e9b2101ba732e7f7259d41c6c` |

**Checks:** 5/5 originals match exact user-supplied pinned blob IDs; F02D matches exact PR #10 supplied blob. Sum originals F07/F08/F09/F10/F12 = `41537` UTF-8 bytes. F02D = 10,990 bytes separately. Optional F02D is *not* a member of Option A.

## Independent structural F02D comparison
Original F02 Git blob `a8d65227b52927814b9d23de42f0dc37ea7fe172`, originally 21,597 UTF-8 bytes. Full parsed CSV comparison: 48 vs 48 data rows, unique sequential K001–K048 in identical order; **eight aligned source-to-derivative metadata columns x 48 = 384/384 equal**; 36 DRAFT_ACCEPT_BOUNDED_RESEARCH_DESCRIPTION, nine DRAFT_AMENDMENT_AWAIT_OWNER, three QUARANTINE_NO_TRANSFER. Every F02D row retained `derived_file_rights=NOT_YET_ATTESTED`, `derived_file_transfer_authorized=NO` and original source blob linkage. Inherited prose/title/behavior columns absent; no claim of independently proved rights.

## Verification scope
Six GitHub text reads, no binary archives or private materials, no historic linked-body fetch. A returned UTF-8 content string is the hashing input, with no invisible binary encoding assertion. SHA-1 file identity and SHA-256 byte digest are independent concepts. This report's hashes are not legal reuse certifications; AP-02 and rights remain HOLD.
