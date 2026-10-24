# Shared Research Protocol — Universal Scriptwriting Skill

## Target
Two independent research agents produce evidence packages. A later integration pass merges and tests rules before implementing a portable SKILL.md and references.

## Responsibilities
- AGENT A / Claude Code: public GitHub repositories and Agent Skills architectures only.
- AGENT B / ChatGPT: real video examples, available authorized transcripts, expert research, papers, original web sources, and performance-context observations.
- INTEGRATOR: resolve overlap and conflicts; write taxonomy and adaptation logic; benchmark on held-out topics. Neither agent unilaterally declares rules proven.

## Evidence gates
1. Discovery: exact source URL and provenance.
2. Independence: distinguish same-source reposts, forks, clones, and study citations.
3. Corroboration: >=3 independent repo lineages = triangulated DESIGN PATTERN, not effectiveness proof.
4. Domain-specific support: real examples + original studies where applicable; record applicability and limitations.
5. Generalization: test across formats/categories and on negative/counterexamples.
6. Implementation: adopt as UNIVERSAL, CONDITIONAL, EXPERIMENTAL, or REJECTED. Even accepted rules remain revisable.

## Shared rule exchange record
```yaml
rule_id: GH-R001  # or RW-R001
rule_statement: "Conditional, testable original-language rule"
taxonomy_scope:
  categories: ["any"]
  niches: ["any"]
  sub_niches: ["any"]
  formats: ["explainer"]
trigger_conditions: []
non_applicability_conditions: []
evidence_ids: []
source_independence_notes: ""
evidence_type: "GITHUB_PATTERN | DIRECT_OBSERVATION | PRIMARY_RESEARCH | OFFICIAL_GUIDE"
source_strength: "STRONG | MODERATE | TENTATIVE | DISPUTED"
causal_claim_supported: false
counterexamples: []
implementation_risk: ""
verification_needed: []
benchmark_case: ""
status: "CANDIDATE"
```

## Integration decisions
- Universal: broad independent applicability, negligible counterexamples, consistent tests.
- Conditional: only when format, audience, purpose and evidence support it.
- Experimental: intriguing but missing corroboration or divergent outcomes.
- Reject: misleading, copied without right, causally ungrounded, contradictory, or repeated hard quotas with no justification.

## Initial reality checks — 2026-10-12
NexLev YouTube discovery returned TED-Ed 'Why you procrastinate even when it feels bad' (https://www.youtube.com/watch?v=FWTNMzK9vG4; 5:46; approx. 10.94M views when observed) and Memoirs of WWII 'WW2 Veteran’s Heartbreaking Story' (https://www.youtube.com/watch?v=9ryE4NzcBhs; 10:18; approx. 1.56M views). NexLev bulk transcript retrieval reported 2 successful/2 requested. No detailed script coding of the second video has yet been completed.
Official YouTube audience-retention documentation: https://support.google.com/youtube/answer/9314415 (title/thumbnail-to-intro fit and limitations of interpreting spikes and dips).
Multimedia learning signaling meta-analysis: https://www.sciencedirect.com/science/article/pii/S1747938X17300581 (learning, not YouTube retention outcomes).

## Ownership and permission
Keep public repo licenses and transcript-content rights visible. Use independent original summaries and source links rather than copying or redistributing third-party scripts. Maintain source register; no remote code execution during auditing.

## Merge gate
Require `github-rule-ledger.md` and `real-world-rule-ledger.md`, plus supporting source registers, before writing final skill. Any unresolved conflicts must be surfaced for editorial decision and tests.
