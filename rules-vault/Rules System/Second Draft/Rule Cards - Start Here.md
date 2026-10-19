# Settlements Rule Cards

**484 individual notes** now cover the review inventory and the additional named profile/advancement entries found during migration. Every original V2 ID and review-table comment is preserved.

Start with [[Settlements/Rules System/Second Draft/Settlements Rule Cards.base|the table and card views]]. Switch between All entries, All cards, book sections, Battle rules, Combat, To-hit bonuses, Armour bonuses, weapons, keywords, skills, equipment/devices, terrain, structures and deferred proposals. The existing Bases core plugin is enabled in this vault; no plugin installation or configuration changes were made.

- [[Settlements/Rules System/Second Draft/Rule Cards - Complete Index|Complete linked index]] — every individual note.
- [[Settlements/Rules System/Second Draft/Settlements Rulebook - Assembled|Assembled rulebook]] — the agreed chapter order, using the same rule text.
- [[Settlements/Rules System/Second Draft/Settlements Rules System Version 2 - Rules and Mechanics Review|Annotated review table]] — original feedback workflow, now linking directly to cards.

## Editing and filtering

Each card has a stable `rule_id`, name, type, category, book section/subsection, tags, concise summary, status, scope and review fields. Profiles also expose their printed fields, such as Credits, Dice, Damage, Range, use, Materials or Power. Weapon profiles link to their keyword cards.

Use a card's **Design notes** for detailed feedback or its **review_notes** property for a short comment visible in the table. Existing review-table Notes remain preserved; future edits must consider both places. An empty note is not approval.

Full rule text is stored once in the card that owns its block. Other cards and section views embed that block. To edit an embedded passage, open its source note; do not replace the embed with a pasted duplicate. Keep a card's summary and profile properties consistent when changing its text. The master manuscript and chapter views reuse these blocks automatically through Obsidian embeds.

`publication: Deferred` identifies earlier objective/scenario proposals reserved for Ross. All entries includes them; Battle rules and the assembled rulebook exclude them. `review_status: Needs review` marks existing unresolved details, including attack templates. Draft proposal does not mean playtested or adopted balance.

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
| Skill | 40 |
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
