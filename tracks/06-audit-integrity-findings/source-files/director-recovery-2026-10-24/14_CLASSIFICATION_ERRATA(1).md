# Classification Index Errata and ID Crosswalk

The extraction ledger (02) defines the immutable original F-ID identity. The classification map (04) is nonauthoritative whenever its F-ID title differs; its labels cannot be back-propagated into ledger IDs. `errata_classification_crosswalk.csv` lists specific mismatches and missing IDs without renumbering.

**Examples:** F-010 = three-act default in ledger but scene/sequel in map; F-012 = scene/sequel in ledger but show-don't-tell in map; F-015 = hierarchy in ledger but controlling idea/theme in map; F-022 = pacing diagnostics in ledger but Truby 22-step in map; F-023 = gather-point convergence in ledger but MICE quotient in map; F-100 is no fabricated dialogue in ledger but one idea/sentence in map. The classification map reuses F-182 for two separate labels (caption-to-visual and semantic units). These are ID integrity errors, independent of whether the underlying ideas are good.

**Result:** The existing classification percentages are not valid coverage counts until the map is rebuilt using original ledger IDs. Reclassification of an individual claim has been stored only as an auditor comment in the new matrix; no original rule is approved.

**Count:** 93 errata entries, including duplicate-map and not-in-map rows.
