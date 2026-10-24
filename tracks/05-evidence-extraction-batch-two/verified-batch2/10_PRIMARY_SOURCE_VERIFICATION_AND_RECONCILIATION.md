# Batch 2 — Primary Source Verification and Reconciliation (2026-10-18)

**Status:** QUALIFIED / awaiting Research Director review. This appendix verifies and reconciles the already-existing controlled Batch 2 archive; it does not initiate Batch 3 or change original historical GitHub finding verdicts.

## Scope and source-by-source confirmation

| R ID | Publisher and inspected original | Access depth / source-specific caution |
|---|---|---|
| R079 | Philip J. Guo / Juho Kim / Rob Rubin; ACM Learning@Scale / MIT CSAIL-hosted copy; https://up.csail.mit.edu/other-pubs/las2014-pguo-engagement.pdf | Original 2014 ACM/MIT-hosted PDF opened; quantitative Table 2 and Figure 3 visually checked. 862 video records, 6,902,358 viewing sessions, 127,839 course-reported student counts. Table 2 does not document across-course de-duplication. No random script intervention; PH207x 33% versus 33% attempt-rate null; approximate figure-level 95% median CIs, not a complete numeric effect CI table. |
| R133 | BBC Editorial Guidelines; http://www.bbc.com/editorialguidelines/guidance/natural-world | The registered BBC HTML URL returned an access error; official BBC PDF (September 2012) accessible separately and visually checked. Historical editorial guidance, not proof of current BBC policy or an audience experiment. |
| R141 | Sportscasters Talent Agency of America / Jon Chelesnik; https://staatalent.com/sportscasting-prep-tools/staa-play-by-play-pyramid.pdf | One-page original copyrighted STAA pyramid PDF visually checked. Score orientation roughly every 90 seconds, recap roughly 8–10 minutes: advice for live radio, not measured YouTube narrative-retention timing. |
| R150 | W3C Web Accessibility Initiative; https://www.w3.org/WAI/media/av/captions/ | Original W3C WAI Captions/Subtitles page read. Accurate speech and salient non-speech captions required where applicable; unchecked automatic output insufficient. W3C default document license restricts modification; special CC-licensed exceptions are separate. |
| R156 | U.S. Securities and Exchange Commission / Investor.gov; https://www.investor.gov/additional-resources/spotlight/videos | Original Investor.gov SEC video gallery read: video-topic titles/index ONLY, not actual produced-video audio, transcript, or draft script. |
| R157 | SEC Investor.gov; https://www.investor.gov/introduction-investing | Original SEC Investor.gov Introduction to Investing guide read: explanations of risk, asset allocation and compound growth. No content-effect experiment or proof of optimal story order. |
| R158 | Consumer Financial Protection Bureau; https://www.consumerfinance.gov/consumer-tools/educator-tool/your-money-your-goals/videos/ | Original CFPB Videos to Spark Action page read; topic-linked video index only. Intro-video-plus-tool instructional sequence is publisher guidance, not tested causal lift. |
| R159 | Consumer Financial Protection Bureau; https://www.consumerfinance.gov/consumer-tools/educator-tools/adult-financial-education/tools-and-resources/ | Original CFPB Adult Financial Education tools and resources page read, organized by topic/audience. Transcript LINKS listed; linked transcript PDFs not read. Broadcast/event transcripts are not necessarily preproduction scripts. |
| R160 | YouTube Help; https://support.google.com/youtube/answer/12942217?co=YOUTUBE._YTVideoType%3Dshorts&hl=en | Original YouTube Shorts content tips page read. Feed appearances, view counts, choices to view vs swipe are differentiated; no performance causal experiment. |
| R161 | YouTube Help; https://support.google.com/youtube/answer/12220281?co=GENIE.Platform%3DDesktop&hl=en | Original YouTube content-performance help read. Aug 24 2026 views-at-start definition confirmed; engaged and qualified Shorts views and watch-time/retention are distinct. |

## Provenance, numeric checks and decision integrity

- Ten previous pilot assessments were compared record-by-record and retained **byte-equivalent at the parsed field level** (10 of 10 matching rows, same ordering).
- Previous 24 source-to-F crosswalk records are unchanged and appear in the same order (24/24 exact CSV field matches).
- Batch 2 adds 18 source-to-F candidate links, totaling 42 across 19 unique F IDs. No link is an approved efficacy finding.
- 171 registered R-sources, 63 GitHub sources, 90 historical original F-ID findings: archival baselines, not replaced or re-audited in this append-only verification.
- R133 was an access exception. Nine exact registered source URLs were accessible in Batch 2; an alternate official historic BBC PDF was separately inspected.
- The underlying 171-row discovery master and 90-row canonical GitHub finding master were **not available as unchanged source files inside the two recovered pilot/batch archives**. Therefore their global byte-level hashes were not independently rechecked in this verification; the archived original manifest records their historical hashes.
- **Accuracy edit:** Batch 2 R079 text now reports 127,839 student counts summed across four course rows. Because the paper does not explicitly document cross-course de-duplication, the former expression “127,839 distinct viewers” was narrowed. All historical pilot rows and verdicts remain unchanged.

## Independence and category limits

- Original new-source families: SEC R156/R157; CFPB R158/R159; Guo–Kim–Rubin R079; historical BBC R133; W3C R150; YouTube R160/R161; STAA R141 = 7 origin groups, **not** seven independent randomized experiments.
- W3C R150 shares institutional origin with previous R149. YouTube R160/R161 share publisher with previous R098. STAA R141 and earlier commentator R142 have framework citation links. No independent corroboration should be counted for these overlaps.
- Educational video outcomes cannot be automatically extrapolated to 20-minute aviation explainers, financial education in all languages, German historical voiceover, edited sports storytelling, documentary wildlife, or Shorts.
- Difference between final broadcast narration, post-hoc transcript, resource index and actual preproduction script remains unresolved; do not reclassify videos/indexes as original writing scripts.

## Rights and permitted use (verification, not legal advice)

- ACM/MIT 2014 paper: personal/classroom copies subject to notice and restrictions; no bulk commercial republication.
- BBC 2012 guidance and STAA pyramid: original copyrighted texts/diagram; analytical paraphrases with source references only.
- SEC sec.gov dissemination notice allows distribution of SEC-origin website information, but does not grant an unconditional license to every third-party media asset on external services or to trademarks/seals.
- CFPB states Bureau-created content is public domain; linked third-party assets, recorded participants, trademarks and videos require separate checks.
- W3C WAI default Document License allows attributed unchanged distribution, not general modifications; specially marked CC material has separate conditions.
- YouTube Help definitions may be summarized with attribution; YouTube videos/audio are not copied or republished in these deliverables.

## Direct original sources and rights references

- R079 paper: https://up.csail.mit.edu/other-pubs/las2014-pguo-engagement.pdf
- R133 archival alternate: https://downloads.bbc.co.uk/guidelines/editorialguidelines/pdfs/natural-world.pdf
- R141 PDF: https://staatalent.com/sportscasting-prep-tools/staa-play-by-play-pyramid.pdf
- R150 WAI: https://www.w3.org/WAI/media/av/captions/
- SEC dissemination: https://www.sec.gov/about/privacy-information
- CFPB copyright: https://www.consumerfinance.gov/privacy/website-privacy-policy/
- WAI rights: https://www.w3.org/WAI/about/using-wai-material/
- YouTube updated metric: https://support.google.com/youtube/answer/12220281?co=GENIE.Platform%3DDesktop&hl=en

## Research Director decision gate

**BATCH 2 COMPLETE — QUALIFIED. STOP.** Do not convert crosswalk connections into final writing rules or a SKILL.md. Continue to a later controlled batch only after explicit review/approval, with pre-existing R IDs and read-access checks.
