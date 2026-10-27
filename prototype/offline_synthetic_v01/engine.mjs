export const evaluate = function evaluate(doc) {
  const HOLD = new Set(), stages = Object.fromEntries(Array.from({length:11},(_,i)=>["A"+String(i).padStart(2,"0"),"NOT_STARTED"]));
  const mark = code => HOLD.add(code);
  const time = x => typeof x === "string" && /[zZ]$|[+-]\d\d:\d\d$/.test(x) && Number.isFinite(Date.parse(x)) ? Date.parse(x) : null;
  const name = x => typeof x === "string" ? (/^N-0[1-5]$/i.test(x) ? "N"+x.toUpperCase().slice(2) : x.toUpperCase()) : "";
  const valid = x => ["N01","N02","N03","N04","N05"].includes(x);
  const contains = (a,b) => typeof a==="string" && typeof b==="string" && (" "+a.toLowerCase().replace(/[^a-z0-9]+/g," ").trim()+" ").includes(" "+b.toLowerCase().replace(/[^a-z0-9]+/g," ").trim()+" ");
  const output = (status, artifact=null) => ({status, label:"RESEARCH_ONLY_NOT_PUBLISHABLE",production_allowed:false,claude_transfer_allowed:false,independent_human_review_performed:false, hold_reasons:[...HOLD].sort(),stage_status:stages,artifact});
  if (!doc || typeof doc!=="object" || Array.isArray(doc)) {mark("HOLD_SCOPE");return output("HOLD");}
  const t=doc.topic||{}, ctx=doc.niche_context||{}, sources=doc.sources||[], claims=doc.claims||[];
  const primary=name(doc.niche), raw=Array.isArray(doc.overlays)?doc.overlays:[], overlays=raw.map(name), all=[...new Set([primary,...overlays])];
  const asOf=time(doc.as_of);
  if (!doc.run_id||doc.synthetic!==true||!asOf||doc.has_live_or_real_world_inputs||!valid(primary)||overlays.some(n=>!valid(n))||!Array.isArray(doc.overlays))mark("HOLD_SCOPE");
  if (!Array.isArray(doc.source_copy_manifest)||doc.source_copy_manifest.length>0)mark("HOLD_SCOPE");
  if (!t.subject||!t.object||!t.mechanism||!t.original_title||!t.uncertainty)mark("HOLD_SCOPE");
  if (doc.request_release||doc.request_claude_transfer)mark("HOLD_NOT_APPROVED");
  if (doc.branch_isolation_broken||doc.historical_id_rekey_attempt)mark("HOLD_MISSING_IDENTITY");
  if (doc.public_transcript_export_attempt)mark("HOLD_RIGHTS");
  stages.A00="CHECKED";
  let sm=new Map();
  if (!Array.isArray(sources)||!sources.length)mark("HOLD_ORIGINAL_MISSING");
  else for(const s of sources){
    if(!s||typeof s!=="object"||!s.id||sm.has(s.id)){mark("HOLD_MISSING_IDENTITY");continue;}
    sm.set(s.id,s);
    if(s.synthetic!==true)mark("HOLD_SCOPE");
    if(!["FULL_READ","PARTIAL","INDEX_ONLY","BLOCKED","MISSING"].includes(s.access_state)||!time(s.retrieved_at))mark("HOLD_MISSING_IDENTITY");
    if(["BLOCKED","MISSING"].includes(s.access_state))mark("HOLD_ORIGINAL_MISSING");
    if(["QUARANTINED","BLOCKED","DISPUTED","MISSING"].includes(s.role)||["F-190","R052","B70","B71","B72","K029","K030","K031"].includes(s.id))mark("HOLD_SOURCE_ROLE");
    if(["B70","B71","B72"].includes(s.id))mark("HOLD_ORIGINAL_MISSING");
    if(s.hash_mismatch)mark("HOLD_DISPUTED_PROVENANCE");
    if(s.can_read!==true||s.can_use_for_synthetic!==true)mark("HOLD_RIGHTS");
    if(s.redistribution_attempted&&s.can_redistribute!==true)mark("HOLD_RIGHTS");
  }
  stages.A01="CHECKED";stages.A02="CHECKED";
  if(!Array.isArray(claims)||!claims.length)mark("HOLD_UNVERIFIED_FACT");
  else for(const c of claims){
    if(!c||typeof c!=="object"||!c.id||!c.text||!["confirmed","qualified","disputed","unknown"].includes(c.epistemic)){mark("HOLD_UNVERIFIED_FACT");continue;}
    if(c.subject!==t.subject||c.object!==t.object)mark("HOLD_TITLE_PREMISE");
    if(!Array.isArray(c.source_ids)||!c.source_ids.length||c.source_ids.some(id=>!sm.has(id)))mark("HOLD_ORIGINAL_MISSING");
    if(!time(c.reviewed_at)||!c.reviewer_id)mark("HOLD_MISSING_IDENTITY");
    if(c.epistemic==="disputed"||c.epistemic==="unknown"||c.unsupported_quantitative_claim||c.unverified_retention_promise)mark("HOLD_UNVERIFIED_FACT");
    if(["QUARANTINED","BLOCKED","DISPUTED"].includes(c.source_role))mark("HOLD_SOURCE_ROLE");
    if(c.epistemic==="confirmed"){
      let fam=new Set((c.source_ids||[]).filter(x=>sm.has(x)).map(id=>sm.get(id).independence_family).filter(Boolean));
      if(fam.size<2)mark("HOLD_UNVERIFIED_FACT");
    }
  }
  stages.A03="CHECKED";stages.A04="CHECKED";
  for(const n of all){
    if(n==="N01"){
      const iss=time(ctx.issued_at),exp=time(ctx.valid_until);
      if(!iss||!exp||!ctx.issuer||!ctx.locality)mark("HOLD_SCOPE");
      if(iss&&exp&&(exp<iss||(exp<asOf&&!ctx.historical_context)))mark("HOLD_STALE_FORECAST");
      if(ctx.projection_labelled_official_warning)mark("HOLD_UNVERIFIED_FACT");
    }
    if(n==="N02"){
      if(ctx.claimed_operational&&!["fielded","reported_in_combat"].includes(ctx.technology_stage))mark("HOLD_UNVERIFIED_FACT");
      if(ctx.single_party_claim_as_fact)mark("HOLD_UNVERIFIED_FACT");
      if(ctx.actionable_targeting_details)mark("HOLD_HARM");
    }
    if(n==="N03"){
      if(ctx.invented_quote_as_historical||ctx.reenactment_claimed_archival||ctx.reenacted_survivor_as_archival)mark("HOLD_HARM");
      if(ctx.translation_lost_qualifier)mark("HOLD_REVIEW");
    }
    if(n==="N04"){
      if(ctx.synthetic_video_claimed_authentic||ctx.reenacted_survivor_as_archival)mark("HOLD_HARM");
      if(ctx.provisional_casualties_called_final||ctx.single_climate_cause_without_study)mark("HOLD_UNVERIFIED_FACT");
    }
    if(n==="N05"){
      if(ctx.universal_retention_claim||ctx.ttspeech_wpm_as_human_law||ctx.mooc_hook_as_video_law)mark("HOLD_SOURCE_ROLE");
      if(ctx.rct_success_without_study)mark("HOLD_NOT_APPROVED");
    }
  }
  if(ctx.false_media_audio_inference||ctx.inaccessible_source_scored_zero||ctx.accessibility_errors)mark("HOLD_REVIEW");
  if(doc.metric_substitution_as_retention)mark("HOLD_UNVERIFIED_FACT");
  const title=doc.candidate_title||t.original_title;
  if(!contains(title,t.subject)||!contains(title,t.object)||doc.premise_strengthened||doc.changed_topic_mechanism)mark("HOLD_TITLE_PREMISE");
  if(!["certain","confirmed"].includes(String(t.uncertainty).toLowerCase())&&/\b(confirmed|proven|proves|definitely|certainly|guaranteed|destroyed|will)\b/i.test(title))mark("HOLD_TITLE_PREMISE");
  stages.A06="CHECKED";
  if(!doc.author_id||!doc.reviewer_id||doc.author_id===doc.reviewer_id||doc.review_overwrote_dissent)mark("HOLD_REVIEW");
  if(doc.severity_three_unsupported)mark("HOLD_UNVERIFIED_FACT");
  if(doc.revision_changed_after_review)mark("HOLD_NEEDS_RECHECK");
  if(doc.claims_executed_experiment_without_data)mark("HOLD_NOT_APPROVED");
  stages.A08="CHECKED";
  if(HOLD.size){stages.A10="HOLD_NOT_PUBLISHABLE";return output("HOLD");}
  stages.A05="CHECKED";stages.A07="MOCK_DRAFT_GENERATED";stages.A09="DESIGN_ONLY_NO_ANALYTICS";stages.A10="RESEARCH_ONLY_TERMINAL";
  const sections=[
    {heading:"Opening question",text:`This is an entirely fictional example, not real reporting. How might ${t.subject} relate to ${t.object} through ${t.mechanism}? The starting assertion remains ${t.uncertainty}.`},
    {heading:"Invented evidence",text:"The fictional case provides these bounded observations: "+claims.map(c=>"According to a simulated record, "+String(c.text).replace(/\.+$/,"")+".").join(" ")},
    {heading:"Limits and unresolved questions",text:"These invented claims illustrate how an outline can preserve topic identity and attribution. A real documentary would need independently verified sources and authorized human review."}
  ];
  return output("RESEARCH_ONLY_TERMINAL",{title,primary_niche:primary,applied_niches:all,claim_ids:claims.map(x=>x.id),source_ids:[...sm.keys()],sections,draft:sections.map(s=>s.heading+"\n"+s.text).join("\n\n"),label:"RESEARCH_ONLY_NOT_PUBLISHABLE"});
};
