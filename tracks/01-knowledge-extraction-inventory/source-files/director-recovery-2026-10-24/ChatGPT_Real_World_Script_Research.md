# AGENT B — ChatGPT | Real-world Scriptwriting Evidence Research

## Mission
Build an original, source-linked **real-world evidence package** for a universal, category-aware YouTube scriptwriting Agent Skill. Focus on observed videos, available legitimate transcripts, research literature, credible professional writing guidance, official YouTube documentation, and audience feedback. Do not audit or copy GitHub skills in this research track. Do not generate the final SKILL.md yet.

## Taxonomy
Category -> Niche -> Sub-niche are classification labels; Format, Audience, Viewer Intent, Language, and Duration are independent dimensions. Cover both factual and creative storytelling. Prioritize adaptive, conditional writing rules over universal fixed numerical quotas.

## Available tools and priorities
- NexLev: public video discovery, metadata, outliers, permitted transcript acquisition, sometimes 10 transcripts per batch. Check tool usage guide first.
- vidIQ: channel/outlier discovery, video metadata, audience comments and video transcripts; many MCP calls cost credits. Use selectively, avoid duplicate paid calls.
- Exa / Tavily: relevant expert sources, writing guidance, research and primary documents.
- Firecrawl: extract source content where access and site policy permit.
- Research Server / deep research: cross-check factual or research claims and find original sources.
- Gemini Video Research or vidIQ video watch: sample only when **visual editing/presentation** materially changes interpretation; transcript alone is insufficient for visual evidence.
Do not depend on a single MCP provider; report rate limits, retrieval failures, transcript availability and costs when known. Do not use unknown third-party YouTube server deployments or assume that described 'free' calls are reliably free or independent.

## Pilot sampling: quality before volume
- Pilot target: 20 distinct YouTube videos split between 2 substantially different categories, starting with Psychology/Education and History/Documentary; include multiple authors and multiple formats within categories.
- Mix proven relative outperformers, typical performers, and underperformers **only when channel-specific comparable performance data exists**. Raw view counts are not enough to label a video an outlier.
- Match comparable publication ages, durations and channel baselines where possible. Label selection bias and gaps.
- Expand later across entertainment, sports, news, gaming, tech, nature, etc. when the pilot analysis is consistent.
- Prefer verified transcripts; when unavailable use a video-watching service or clearly mark no-transcript rather than hallucinating words.
- Never treat captions as the guaranteed exact authored script; acknowledge automatic-caption mistakes, overlapping timed segments and edits.

## Evidence captured for each video
`video_id`, `url`, `channel`, `title`, `observed_date`, `publish_date`, `category`, `niche`, `sub_niche`, `format`, `language`, `duration`, `views_at_observation`, `channel_context`, `outlier_metric_if_supported`, `transcript_status`, `transcript_provenance`, `analysis_timestamp`, `script_DNA_observations`, `counterexamples`, `limitations`, `source_links`.

## Script DNA extraction checklist
Opening/hook type and exact timestamp; title-to-opening promise match; setup/early value; macro structure; explanatory progression; evidence integration; framing and audience knowledge; pacing transitions; stakes/emotional calibration; curiosity loops and their payoff; ending/CTA; distinct format-specific choices; weak segments and plausible alternative explanations.
For each observation provide a timestamp and a SHORT original paraphrase, not long copied passages. Separate `OBSERVED`, `INFERRED`, and `HYPOTHESIS`.

## Broader research requirements
Collect primary studies, research syntheses, institutional guides and official YouTube guidance relevant to narration, comprehension, storytelling, engagement, cognitive load, information organization and ethical/factual scriptwriting. Separate claims about **learning/comprehension** from claims about **YouTube retention, CTR or recommendation effects**; evidence for one does not automatically establish the other.
Document authorship, date, method, sample, key finding, limitations and original URL. Cross-check important empirical claims with independent sources where possible. Three blog posts re-citing one study count as one research origin.

## Rules and validation
Create candidate rule IDs `RW-R001`, etc. For each record `rule`, `scope`, `trigger`, `benefit_hypothesis`, `counterexamples`, `evidence_ids`, `confidence` (`STRONG_EMPIRICAL`, `SUPPORTED_OBSERVATION`, `TENTATIVE`, `DISPUTED`), `test_design`, `copyright/usage_notes`.
Rules must remain conditional and falsifiable. E.g., do not claim "add a re-hook every 30 seconds" or "a successful title guarantees retention" without proper evidence. Public views, comments and titles do NOT prove script-caused retention; detailed retention is usually available only to the channel owner.
Avoid bulk redistribution/storage of copyrighted full transcripts. Preserve authorized source pointers and concise analytical notes; follow site terms and licenses.

## Required deliverables (real-world-research/)
1. `real-world-source-register.md` — source provenance and permitted use.
2. `video-sample-and-methodology.md` — selection logic and comparability caveats.
3. `video-script-dna.md` — timestamped structured original observations.
4. `empirical-evidence-and-claims.md` — research claims, methods, limits.
5. `real-world-rule-ledger.md` — RW-R IDs, evidence and counterexamples.
6. `handoff-agent-b.md` — standalone integration summary and uncertain areas.

## Stop condition
Finish the 20-video pilot and evidence synthesis before expanding. Provide all artifacts and exact gaps. No repeated setup loops, no unlimited crawling, no invented retention data. Do not build the final skill before the GitHub audit and evidence merger.
