#!/usr/bin/env python3
"""Zero-source, offline, synthetic-only Universal Scriptwriting prototype v0.1.

Standard library only. This is a fictional test harness, not a production SKILL,
not a real-world fact checker, not an LLM and not an approved external transfer.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

LABEL = "RESEARCH_ONLY_NOT_PUBLISHABLE"
ADAPTERS = {"N01", "N02", "N03", "N04", "N05"}
RESTRICTED_ROLES = {"QUARANTINED", "BLOCKED", "DISPUTED", "MISSING"}
ACCESS_STATES = {"FULL_READ", "PARTIAL", "INDEX_ONLY", "BLOCKED", "MISSING"}
EPISTEMIC_STATES = {"confirmed", "qualified", "disputed", "unknown"}
STAGES = [f"A{i:02d}" for i in range(11)]
BAD_CERTAINTY = {"confirmed", "proven", "proves", "definitely", "certainly",
                 "guaranteed", "undeniable", "destroyed", "will"}
RESTRICTED_META_IDS = {"F-190", "R052", "B70", "B71", "B72", "K029", "K030", "K031"}


def digest(item: Any) -> str:
    """Stable content fingerprint; NOT an authenticity or copyright certificate."""
    raw = json.dumps(item, ensure_ascii=False, sort_keys=True,
                     separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def timestamp(s: Any) -> datetime | None:
    if not isinstance(s, str) or not s:
        return None
    try:
        v = datetime.fromisoformat(s.replace("Z", "+00:00"))
        return v if v.tzinfo is not None else None
    except ValueError:
        return None


def canon_niche(value: Any) -> str:
    if not isinstance(value, str):
        return ""
    v = value.upper()
    if re.fullmatch(r"N-0[1-5]", v):
        return "N" + v[2:]
    return v if v in ADAPTERS else ""


def words(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def contains_identity(text: Any, identity: Any) -> bool:
    if not isinstance(text, str) or not isinstance(identity, str):
        return False
    needle = words(identity)
    hay = words(text)
    return bool(needle) and any(hay[i:i + len(needle)] == needle
                                for i in range(len(hay) - len(needle) + 1))


def active_niches(doc: dict[str, Any]) -> tuple[str, set[str], bool]:
    primary = canon_niche(doc.get("niche"))
    extras = doc.get("overlays", [])
    if not isinstance(extras, list):
        return primary, set(), False
    normalized = [canon_niche(x) for x in extras]
    return primary, (set(normalized) | {primary}) - {""}, all(normalized) and bool(primary)


def run_document(doc: Any) -> dict[str, Any]:
    """Validate and produce an intentionally limited research-only synthetic draft.

    Negative results are deterministic and fail closed with ALL native HOLD codes.
    No filesystem/network access occurs inside this function.
    """
    holds: set[str] = set()
    notes: list[str] = []
    stages = {stage: "NOT_STARTED" for stage in STAGES}
    result: dict[str, Any] = {
        "status": "HOLD",
        "label": LABEL,
        "production_allowed": False,
        "claude_transfer_allowed": False,
        "independent_human_review_performed": False,
        "hold_reasons": [],
        "notes": notes,
        "stage_status": stages,
        "artifact": None,
        "run_digest": None,
    }
    if not isinstance(doc, dict):
        result["hold_reasons"] = ["HOLD_SCOPE"]
        return result

    result["run_digest"] = digest(doc)
    if doc.get("synthetic") is not True or doc.get("source_copy_manifest", []) != []:
        holds.add("HOLD_SCOPE")
    if doc.get("request_release") or doc.get("request_claude_transfer"):
        holds.add("HOLD_NOT_APPROVED")
    if doc.get("has_live_or_real_world_inputs"):
        holds.add("HOLD_SCOPE")
    as_of = timestamp(doc.get("as_of"))
    if as_of is None or not doc.get("run_id"):
        holds.add("HOLD_SCOPE")
    primary, applicable, niches_ok = active_niches(doc)
    if not niches_ok:
        holds.add("HOLD_SCOPE")
        notes.append("Unknown niche/overlay requires review; there is no default adapter.")
    topic = doc.get("topic", {})
    if not isinstance(topic, dict):
        topic = {}
        holds.add("HOLD_SCOPE")
    for key in ("subject", "object", "mechanism", "original_title", "uncertainty"):
        if not isinstance(topic.get(key), str) or not topic[key].strip():
            holds.add("HOLD_SCOPE")
    if not holds.intersection({"HOLD_SCOPE"}):
        stages["A00"] = "PASS_SYNTHETIC_SCOPE"

    sources = doc.get("sources", [])
    source_map: dict[str, dict[str, Any]] = {}
    if not isinstance(sources, list) or not sources:
        holds.add("HOLD_ORIGINAL_MISSING")
        sources = []
    for src in sources:
        if not isinstance(src, dict):
            holds.add("HOLD_MISSING_IDENTITY")
            continue
        sid = src.get("id")
        if not isinstance(sid, str) or not sid or sid in source_map:
            holds.add("HOLD_MISSING_IDENTITY")
            continue
        source_map[sid] = src
        if src.get("synthetic") is not True:
            holds.add("HOLD_SCOPE")
        if src.get("access_state") not in ACCESS_STATES:
            holds.add("HOLD_MISSING_IDENTITY")
        if timestamp(src.get("retrieved_at")) is None:
            holds.add("HOLD_MISSING_IDENTITY")
        if src.get("access_state") in {"BLOCKED", "MISSING"}:
            holds.add("HOLD_ORIGINAL_MISSING")
        if src.get("role") in RESTRICTED_ROLES or sid in RESTRICTED_META_IDS:
            holds.add("HOLD_SOURCE_ROLE")
        if src.get("hash_mismatch"):
            holds.add("HOLD_DISPUTED_PROVENANCE")
        if src.get("can_read") is not True:
            holds.add("HOLD_RIGHTS")
        # Permissions are independent. Never infer rights from public visibility.
        if src.get("can_use_for_synthetic") is not True:
            holds.add("HOLD_RIGHTS")
        if src.get("redistribution_attempted") and src.get("can_redistribute") is not True:
            holds.add("HOLD_RIGHTS")
    if sources:
        stages["A01"] = "CHECKED"

    claims = doc.get("claims", [])
    if not isinstance(claims, list) or not claims:
        claims = []
        holds.add("HOLD_UNVERIFIED_FACT")
    seen_claims: set[str] = set()
    for claim in claims:
        if not isinstance(claim, dict):
            holds.add("HOLD_UNVERIFIED_FACT")
            continue
        cid = claim.get("id")
        if not isinstance(cid, str) or not cid or cid in seen_claims:
            holds.add("HOLD_MISSING_IDENTITY")
            continue
        seen_claims.add(cid)
        if claim.get("epistemic") not in EPISTEMIC_STATES:
            holds.add("HOLD_UNVERIFIED_FACT")
        if not isinstance(claim.get("text"), str) or not claim["text"].strip():
            holds.add("HOLD_UNVERIFIED_FACT")
        if claim.get("subject") != topic.get("subject") or claim.get("object") != topic.get("object"):
            holds.add("HOLD_TITLE_PREMISE")
        refs = claim.get("source_ids", [])
        if not isinstance(refs, list) or not refs:
            holds.add("HOLD_ORIGINAL_MISSING")
            refs = []
        if any(not isinstance(r, str) or r not in source_map for r in refs):
            holds.add("HOLD_ORIGINAL_MISSING")
        if timestamp(claim.get("reviewed_at")) is None or not claim.get("reviewer_id"):
            holds.add("HOLD_MISSING_IDENTITY")
        if claim.get("source_role") in RESTRICTED_ROLES:
            holds.add("HOLD_SOURCE_ROLE")
        if claim.get("epistemic") in {"unknown", "disputed"}:
            holds.add("HOLD_UNVERIFIED_FACT")
        if claim.get("epistemic") == "confirmed":
            families = {source_map[r].get("independence_family") for r in refs if r in source_map}
            families.discard(None)
            if len(families) < 2:
                holds.add("HOLD_UNVERIFIED_FACT")
        if claim.get("unsupported_quantitative_claim"):
            holds.add("HOLD_UNVERIFIED_FACT")
    stages["A02"] = "CHECKED"
    stages["A04"] = "CHECKED"

    ctx = doc.get("niche_context", {})
    if not isinstance(ctx, dict):
        ctx = {}
        holds.add("HOLD_SCOPE")
    for niche in sorted(applicable):
        if niche == "N01":
            expiry = timestamp(ctx.get("valid_until"))
            issued = timestamp(ctx.get("issued_at"))
            if not expiry or not issued or not ctx.get("issuer") or not ctx.get("locality"):
                holds.add("HOLD_SCOPE")
            elif expiry < issued:
                holds.add("HOLD_STALE_FORECAST")
            elif as_of and expiry < as_of and not ctx.get("historical_context"):
                holds.add("HOLD_STALE_FORECAST")
            if ctx.get("projection_labelled_official_warning"):
                holds.add("HOLD_UNVERIFIED_FACT")
        elif niche == "N02":
            if ctx.get("claimed_operational") and ctx.get("technology_stage") not in {"fielded", "reported_in_combat"}:
                holds.add("HOLD_UNVERIFIED_FACT")
            if ctx.get("single_party_claim_as_fact"):
                holds.add("HOLD_UNVERIFIED_FACT")
            if ctx.get("actionable_targeting_details"):
                holds.add("HOLD_HARM")
        elif niche == "N03":
            if ctx.get("invented_quote_as_historical") or ctx.get("reenactment_claimed_archival"):
                holds.add("HOLD_HARM")
            if ctx.get("translation_lost_qualifier"):
                holds.add("HOLD_REVIEW")
        elif niche == "N04":
            if ctx.get("synthetic_video_claimed_authentic") or ctx.get("reenacted_survivor_as_archival"):
                holds.add("HOLD_HARM")
            if ctx.get("provisional_casualties_called_final") or ctx.get("single_climate_cause_without_study"):
                holds.add("HOLD_UNVERIFIED_FACT")
        elif niche == "N05":
            if ctx.get("universal_retention_claim") or ctx.get("ttspeech_wpm_as_human_law") or ctx.get("mooc_hook_as_video_law"):
                holds.add("HOLD_SOURCE_ROLE")
            if ctx.get("rct_success_without_study"):
                holds.add("HOLD_NOT_APPROVED")
    if ctx.get("false_media_audio_inference"):
        holds.add("HOLD_REVIEW")
    if ctx.get("inaccessible_source_scored_zero"):
        holds.add("HOLD_REVIEW")
    if ctx.get("accessibility_errors"):
        holds.add("HOLD_REVIEW")
    stages["A03"] = "CHECKED"

    title = doc.get("candidate_title") or topic.get("original_title", "")
    if not contains_identity(title, topic.get("subject")) or not contains_identity(title, topic.get("object")):
        holds.add("HOLD_TITLE_PREMISE")
    uncertainty = str(topic.get("uncertainty", "")).lower()
    if uncertainty not in {"certain", "confirmed"} and set(words(title)).intersection(BAD_CERTAINTY):
        holds.add("HOLD_TITLE_PREMISE")
    if doc.get("premise_strengthened") or doc.get("changed_topic_mechanism"):
        holds.add("HOLD_TITLE_PREMISE")
    stages["A06"] = "CHECKED"

    if doc.get("author_id") == doc.get("reviewer_id") or not doc.get("reviewer_id") or not doc.get("author_id"):
        holds.add("HOLD_REVIEW")
    if doc.get("review_overwrote_dissent"):
        holds.add("HOLD_REVIEW")
    if doc.get("severity_three_unsupported"):
        holds.add("HOLD_UNVERIFIED_FACT")
    if doc.get("revision_changed_after_review"):
        holds.add("HOLD_NEEDS_RECHECK")
    if doc.get("claims_executed_experiment_without_data"):
        holds.add("HOLD_NOT_APPROVED")
    stages["A08"] = "CHECKED"

    if holds:
        result["hold_reasons"] = sorted(holds)
        notes.append("Mock gate evaluation failed; no draft emitted and no output is publishable.")
        stages["A10"] = "HOLD_NOT_PUBLISHABLE"
        return result

    # Safe positive result: a deterministic, demonstrably fictional *short* draft.
    # It is not comprehensive documentary scriptwriting or human source verification.
    stages["A05"] = "CHECKED"
    sections = [
        {
            "heading": "Opening question",
            "text": "This is a fictional demonstration, not a report of a real event. "
                    f"How might {topic['subject']} relate to {topic['object']} through "
                    f"{topic['mechanism']}? The question remains framed as {topic['uncertainty']}."
        },
        {
            "heading": "Synthetic evidence",
            "text": "The invented record offers the following bounded observations: "
                    + " ".join(("According to this fictional example, " + c["text"].rstrip(".") + ".")
                               for c in claims),
        },
        {
            "heading": "What remains unresolved",
            "text": "These invented examples demonstrate how a topic, claim and source "
                    "can remain linked without claiming that anything occurred in the real "
                    "world. An actual documentary would require separately obtained, "
                    "lawfully used primary evidence and independent editorial review."
        },
    ]
    result["artifact"] = {
        "title": title,
        "topic_lock_digest": digest(topic),
        "source_ids": sorted(source_map),
        "claim_ids": sorted(seen_claims),
        "primary_niche": primary,
        "applied_niches": sorted(applicable),
        "outline": [s["heading"] for s in sections],
        "sections": sections,
        "draft": "\n\n".join(s["heading"] + "\n" + s["text"] for s in sections),
        "label": LABEL,
    }
    stages["A07"] = "MOCK_DRAFT_GENERATED"
    stages["A09"] = "DESIGN_ONLY_NO_ANALYTICS"
    stages["A10"] = "RESEARCH_ONLY_TERMINAL"
    result["status"] = "RESEARCH_ONLY_TERMINAL"
    notes.append("Synthetic mock draft generated. Human review and production are not authorized.")
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Offline synthetic-only scriptwriting demo")
    parser.add_argument("--input", required=True, help="Local JSON fixture (fictional data only)")
    parser.add_argument("--output", help="Write JSON diagnostic/output to this local file")
    args = parser.parse_args(argv)
    path = Path(args.input)
    try:
        content = json.loads(path.read_text(encoding="utf-8"))
        report = run_document(content)
        raw = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
        if args.output:
            Path(args.output).write_text(raw, encoding="utf-8")
        else:
            sys.stdout.write(raw)
        return 0 if report["status"] == "RESEARCH_ONLY_TERMINAL" else 2
    except (OSError, ValueError) as exc:
        print(f"Input/output error: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
