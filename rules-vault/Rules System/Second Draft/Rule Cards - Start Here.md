# Settlements Rule Cards

**483 active-library notes** now cover the review inventory and the additional named profile/advancement entries found during migration. Every original V2 ID and review-table comment is preserved.

Start with [[Rule Cards - Visual Workspace|the visual workspace]], [[Settlements/Rules System/Second Draft/Settlements Rule Cards.base|the table, cards and review board]], or [[Settlements Rulebook Layout.base|the chapter placement board]]. Switch between All entries, All cards, book sections, Battle rules, Combat, To-hit bonuses, Armour bonuses, weapons, keywords, skills, equipment/devices, terrain, structures and deferred proposals. Native Bases and the existing Colored Tags plugin provide these views. Scoped styling in the already-enabled bases-wrap CSS snippet adds readable cards and category/review strips; the local Settlements Rule Workspace plugin now handles canvas-to-note placement and the new-rule command. Last updated and Status are visible in the table. Planned section is outline-only metadata, with changes collected by the layout's Moved cards view.

- [[Settlements/Rules System/Second Draft/Rule Cards - Complete Index|Complete linked index]] — every individual note.
- [[Settlements/Rules System/Second Draft/Settlements Rulebook - Assembled|Assembled rulebook]] — the agreed chapter order, using the same rule text.
- [[Settlements/Rules System/Second Draft/Settlements Rules System Version 2 - Rules and Mechanics Review|Annotated review table]] — original feedback workflow, now linking directly to cards.

## Visual editing and new rules

- [[Settlements Rulebook Layout.canvas|Draggable chapter canvas]] — move live note cards between chapter groups to update Planned section; table/board edits move the canvas card too.
- **Ctrl+P → Settlements Rule Workspace: Add a new rule card** — generates the unique ID, fields, dates and index links from your entered rule text.
- [[Rule Cards - Visual Workspace|Full view, canvas and creation instructions]].

## Editing and filtering

Each card has a stable `rule_id`, name, type, category, book section/subsection, tags, concise summary, status, scope and review fields. Profiles also expose their printed fields, such as Credits, Dice, Damage, Range, use, Materials or Power. Weapon profiles link to their keyword cards.

Use a card's **Design notes** for detailed feedback or its **review_notes** property for a short comment visible in the table. Existing review-table Notes remain preserved; future edits must consider both places. An empty note is not approval.

Full rule text is stored once in the card that owns its block. Other cards and section views embed that block. To edit an embedded passage, open its source note; do not replace the embed with a pasted duplicate. Keep a card's summary and profile properties consistent when changing its text. The master manuscript and chapter views reuse these blocks automatically through Obsidian embeds.

`publication: Deferred` identifies earlier objective/scenario proposals reserved for Ross. All entries includes them; Battle rules and the assembled rulebook exclude them. `review_status: Needs review` marks existing unresolved details, including attack templates. Draft proposal does not mean playtested or adopted balance.

The **Last updated** column in the [[Rule Cards - Complete Index|complete card-name index]], table/card views and annotated review table records each owning card's last confirmed rule-text change. It uses `last_rule_update: YYYY-MM-DD` in Pacific time (`America/Los_Angeles`). Blank means unknown or not yet recorded. For an actual rule-text change, update that property, the card's concise summary where needed, and its complete-index date and review-table date/description while preserving feedback. Formatting, metadata, links, indexing and other housekeeping do not advance the date. Do not infer rule revisions from filesystem timestamps. See [[Settlements/Rules System/Second Draft/AGENTS|rule-update maintenance instructions]].

## Coverage

| Type | Individual cards |
| --- | ---: |
| Advancement level | 10 |
| Armour | 3 |
| Deployable | 9 |
| Equipment | 13 |
| Experience deed | 4 |
| Interaction | 5 |
| Interactive terrain | 20 |
| Lasting injury | 10 |
| Objective convention | 2 |
| Rule | 282 |
| Scenario proposal | 8 |
| Skill | 39 |
| Stat | 8 |
| Structure | 20 |
| Training grade | 4 |
| Weapon | 22 |
| Weapon class | 6 |
| Weapon keyword | 18 |

## Source and maintenance

The pre-migration manuscript and annotated table are preserved in `Rules System/Archived/Before individual rule cards - 2026-10-18/`. The new migration script is create-only and refuses to overwrite this library. Do not run legacy catalogue generators against these notes.

The card/section library is local Obsidian content. No Fibery import has been performed. These properties and stable IDs provide the mapping for a later import.

Base configuration follows [Obsidian's Bases syntax](https://help.obsidian.md/bases/syntax) and [Cards view documentation](https://help.obsidian.md/bases/views/cards). Live reuse follows [Obsidian embeds](https://help.obsidian.md/embeds). File/link checks do not establish a visual check in the Obsidian application.

## Open the library

![[Settlements/Rules System/Second Draft/Settlements Rule Cards.base]]
