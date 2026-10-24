---
type: design-migration
status: Implemented; document validation only
started: 2026-10-18
---
# Individual rule cards and section views

Ross explicitly requested one note/card for every rule and mechanic, including weapons, weapon keywords, skills, equipment, interactive terrain and settlement structures, so these can be filtered and displayed in different views.

## Delivered

- 484 individual notes under `Rules System/Second Draft/Rule Cards/`.
- All 453 existing V2 IDs and their feedback preserved; thirty-one additional entries cover named profile stats, the Heavy keyword, the action menu, individual advancement levels, interaction types, XP deeds and the confirmed objective limit/diameters.
- 22 weapon profiles, six weapon classes, eighteen weapon keywords, forty skills, twenty terrain profiles, nine deployables including the utility drone, sixteen armour/supply entries, twenty structures, four grades and ten lasting-injury outcomes.
- Stable IDs, category/type, book placement, tags, summary, scope/status, review fields, printed profile data and related-rule links.
- Fifteen table/card views in [[Settlements/Rules System/Second Draft/Settlements Rule Workspace.base#Rule index]], a complete index, thirteen section notes and [[Settlements Rulebook - Assembled]].

## Text ownership

455 source blocks are stored once in their owning card. Shared passages, source-family assemblies, the compatible master and the new chapter views reuse those blocks through live embeds. Original chapter links remain valid. A card can show contextual blocks owned by another card; follow that embed to edit its source. Summaries and profile properties must be kept consistent with rule text.

The original manuscript and annotated review table were preserved before migration. All original feedback cells survive, and their links now open the corresponding card. The migration generator refuses to overwrite an existing library. Older catalogue generators do not support this structure.

## Scope and evidence

Eighteen earlier objective/scenario proposals are marked Deferred and omitted from the assembled rulebook. The two confirmed objective-area cards state the six-objective maximum, 6-inch circles for one to three objectives, 3-inch circles for four to six, and no additional control distance. Scenario specifics remain Ross's placeholders. The no-killing-required principle is retained.

Source text, table-row coverage, IDs, feedback, properties, links and embeds were checked with `scripts/check_rule_cards_20261018.py`; its report is in `docs/draft2-rule-cards-2026-10-18/validation.json`. This does not establish Obsidian UI rendering, game balance or tabletop acceptance. No Fibery import, new faction rules, simulation or gameplay experiment was performed.
