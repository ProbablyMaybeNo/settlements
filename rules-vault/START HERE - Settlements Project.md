---
type: project-guide
updated: 2026-10-23
tags:
  - settlements
  - project-guide
---

# Settlements — Start here

**This is the project’s front door.** Open the **Obsidian Vault** vault, then the **Settlements** folder. Press **Ctrl+O** and search for **START HERE - Settlements Project** to return here.

The current rules live in **individual Draft 2 rule-card notes**. The rulebook, tables, boards and canvas reuse those notes. The setup recorded here contains **483 cards**, including eighteen deferred proposals; new cards will increase that inventory.

## 1. Choose what you want to do

| I want to… | Open / run |
| --- | --- |
| Browse, filter or compare rules | [[Settlements/Rules System/Second Draft/Settlements Rule Cards.base\|Rules table, card gallery and review board]] |
| See the visual-workspace instructions | [[Settlements/Rules System/Second Draft/Rule Cards - Visual Workspace\|Visual workspace]] |
| Move rules beneath chapter headings on a canvas | [[Settlements/Rules System/Second Draft/Settlements Rulebook Layout.canvas\|Rulebook layout canvas]] |
| Plan chapters using columns instead | [[Settlements/Rules System/Second Draft/Settlements Rulebook Layout.base\|Rulebook layout board / placement table]] |
| Create a new rule | **Ctrl+P → Settlements Rule Workspace: Add a new rule card** |
| Find an individual rule by name | [[Settlements/Rules System/Second Draft/Rule Cards - Complete Index\|Complete rule-card index]], or **Ctrl+O** and its name / V2 ID |
| Read the whole rulebook | [[Settlements/Rules System/Second Draft/Settlements Rulebook - Assembled\|Assembled rulebook]] |
| See the chapter and subsection outline | [[Settlements/Rules System/Second Draft/Settlements Core Rulebook Outline\|Rulebook outline]] |
| Use the compatible older master view | [[Settlements/Rules System/Second Draft/Settlements Rules System Version 2\|Rules System Version 2]] |
| Leave feedback in the review table | [[Settlements/Rules System/Second Draft/Settlements Rules System Version 2 - Rules and Mechanics Review\|Rules and Mechanics Review]] |
| Check decisions and outstanding work | [[Settlements/Rules System/Second Draft/Draft 2 - Progress and Decisions\|Progress and Decisions]] |
| Look up design research | [[Settlements/Research/Wargaming Research Hub\|Research hub]] or [[Settlements/Research/Rule of Carnage Skirmish Game Design Reference\|Rule of Carnage design reference]] |

## Parent overview

Open [[Settlements/Rules System/Second Draft/Settlements Rule Parents.canvas|the parent canvas]] for one card per parent under its rulebook family. Double-click a parent to open its live rule table. Change Type / Parent in [[Settlements/Rules System/Second Draft/Rule Cards - Complete Index#Editable index|Complete Index → Editable index]] to update membership automatically. See [[Settlements/Rules System/Second Draft/Rule Parents - Start Here|parent-view instructions]].

## 2. Browse the rules as tables, cards or Kanban

Open [[Settlements/Rules System/Second Draft/Settlements Rule Cards.base\|Settlements Rule Cards.base]]. Use the view menu at the upper left to switch layouts.

- **Rules table:** names, Last updated, Status, Category, Description, Tags, current chapter/subsection, Planned section and review notes. Scroll horizontally for additional columns.
- **All cards:** a gallery of concise descriptions. Open a card for its complete rule and linked mechanics.
- **Review board:** Kanban columns based on review status. Dragging between columns changes that card’s review status. Add another status column through **Group** when needed.
- **By book section / Battle rules / Combat:** focused reading and comparison views.
- **To-hit bonuses / Armour bonuses:** modifier views using the relevant tags.
- **Weapons / Weapon keywords / Skills / Equipment and devices / Interactive terrain / Structures:** catalogue views.
- **Needs review / Recently updated / Deferred objective proposals:** review and maintenance views.

Use **Filter** to combine tags, category, status and scope. For example, combine the Combat category with the `hit-plus` tag to examine positive hit modifiers in that category. Use **Properties** to choose visible fields and **Sort** to change their order. The toolbar’s **Search** searches the displayed properties.

The [[Settlements/Rules System/Second Draft/Rule Cards - Complete Index|complete index]] includes Status beside every rule. Change the card’s Status in its properties or the Rules table; the workspace plugin refreshes the index automatically. Its **Refresh rule statuses in the complete index** command also refreshes the column. Edit the owning property rather than the index copy.

**Family → Type / Parent → Rule** provides the rulebook hierarchy: for example, **Core Mechanics → Stats → DEX**. Family is the recorded chapter; Type / Parent is an editable `rule_parent` assignment, initially seeded from catalogue type or ordinary-rule subsection. These index columns follow the owning card’s placement fields. Planned section remains a proposed move until the manuscript layout is applied.

### What the fields mean

| Visible field | Stored property | Meaning |
| --- | --- | --- |
| Status | `status` | Pending, Partial, Drafted, Confirmed, Locked or Deferred; definitions in the complete index. |
| Review flag | `review_status` | Unreviewed or Needs review; separate from writing/approval status. |
| Scope | `publication` | Follows Status: Deferred or Included. Change Status to defer/restore a card; inclusion is not approval or playtesting. |
| Last updated | `last_rule_update` | Last confirmed change to the rule’s meaning or procedure. Blank means unknown. |
| Family / Current chapter / Current subsection | `book_section` / `book_subsection` | Recorded placement in the existing rulebook structure. |
| Planned section | `planned_section` | Proposed chapter placement shared by the planning board and canvas. |

Tags have coloured chips. In the galleries and boards, category strips use coral for combat/weapons, blue for movement/actions/setup, teal for terrain/interactions/devices, purple for morale/casualties/stealth, green for skills, gold for equipment/settlements/structures, and slate for other rules. **Amber marks Needs review; grey marks Deferred.** Read the written status and scope alongside the colour.

## 3. Create a new rule

1. Press **Ctrl+P**.
2. Run **Settlements Rule Workspace: Add a new rule card**. The rule-card icon in the left ribbon opens the same form.
3. Enter the **rule name, category, chapter, optional subsection, tags, concise description and full rule text**. Separate tags with commas; omit `#` and spaces inside a tag name.
4. Select **Create rule card**.

The command creates a clean individual note with the next unused **V2 ID**, a unique rule-text block, the required properties, and Pacific creation/revision dates. It adds the card to the live views and canvas, updates the complete index and annotated review table, and records the addition in Progress and Decisions. New cards start with **Status: Drafted** and **Review flag: Unreviewed**.

Use this command for the complete creation workflow. The generic Bases **New** button does not perform the unique-ID and index setup.

The form currently creates an ordinary **Rule** entry. A new weapon, skill, piece of equipment, terrain feature or structure also needs its appropriate entry type and profile fields. I can create those profiles for you, or you can edit the new card’s properties and full profile after allocating its ID through the form.

**New cards appear in the library immediately.** Their owning rule block still needs to be embedded beneath the chosen chapter/subsection in the assembled manuscript. Creation does not automatically rewrite the rulebook’s chapter notes.

## 4. Edit an existing rule

Open the card from a table, board, canvas or index. The owning files are in:

`Settlements/Rules System/Second Draft/Rule Cards/`

1. Edit the owning card’s **Rule text**. A passage shown as an embed belongs to another note: follow that embed to its source and edit there.
2. Keep the visible **Summary** and the `summary` property consistent with the full rule. For catalogue entries, keep the profile properties and printed profile values consistent too.
3. Adjust category and tags if the mechanic’s classification changes.
4. For a change to meaning, procedure, values, limits or exceptions, set **Last updated** to the change date in `YYYY-MM-DD`, using Pacific time.
5. Update that rule’s date in the [[Settlements/Rules System/Second Draft/Rule Cards - Complete Index\|complete index]], and its concise description/date in the [[Settlements/Rules System/Second Draft/Settlements Rules System Version 2 - Rules and Mechanics Review\|annotated review table]]. Preserve existing feedback.
6. Check related rules, examples and the battle reference for wording that also needs updating.

The assembled rulebook and compatible master reuse the owning blocks through live embeds, so their displayed text follows edits to those blocks. Preserve existing V2 IDs, block anchors and links rather than pasting another independent copy into the master.

**Rule dates are maintained deliberately.** The creation command dates a new rule; ordinary text edits are not automatically classified or dated by the workspace plugin. Formatting, tags, feedback, status changes and chapter planning do not advance a semantic rule-revision date. Full maintenance instructions: [[Settlements/Rules System/Second Draft/AGENTS\|Draft 2 rule-update tracking]].

## 5. Leave feedback without rewriting the rule

Use whichever location is most comfortable:

- **Design notes** at the bottom of the individual card for detailed comments.
- **review_notes** for a short comment visible in table views.
- The **Notes** column in the annotated review table for the existing review workflow.

Start with **KEEP**, **CHANGE**, **REMOVE** or **QUESTION** if helpful, and refer to related rules by V2 ID. You can ask me to read those notes, revise the owning rules, check connected mechanics and update the indexes. Feedback and an empty review field do not automatically approve or change a rule.

## 6. Arrange the rulebook using the board or canvas

### Chapter board

Open [[Settlements/Rules System/Second Draft/Settlements Rulebook Layout.base\|Settlements Rulebook Layout.base]].

- **Rulebook layout:** thirteen chapter columns; drag a card under a chapter heading to change Planned section. The main view excludes Deferred material.
- **Placement table:** inspect current and planned chapter assignments together.
- **Moved cards:** find cards whose planned chapter differs from their current chapter.
- **All placements including deferred:** also inspect the parked proposals.

### Chapter canvas

Open [[Settlements/Rules System/Second Draft/Settlements Rulebook Layout.canvas\|Settlements Rulebook Layout.canvas]]. It contains the original library notes as live file cards, thirteen chapter groups, and separate deferred parking.

1. Use **Ctrl+P → Canvas: Jump to group** to find a chapter. Pan and zoom to work on its cards.
2. Drag a card by its title into another chapter group. Its **centre** determines which group contains it.
3. After Canvas saves, the card’s **Planned section** updates in the note, table and board.

Editing Planned section from the note or table/board also moves the existing canvas card into that chapter. The canvas initially shows each note’s Summary; open the note for its complete rule.

Cards outside chapter groups retain their previous assignment. Use one file card per rule on this canvas; duplicate copies are excluded from syncing to avoid competing assignments. Chapter group mappings are fixed, so renaming a group label does not rename a chapter. Moves made while the workspace plugin is disabled are not applied retrospectively when it restarts.

**This is a placement plan.** Moving cards does not change rule text, revision dates, approval, deferred status, current subsection, or the assembled manuscript. Positions within a group do not yet set precise reading order. Record proposed subsection/order changes in review notes; once the layout is chosen, ask me to apply it to the chapter notes and assembled rulebook.

## 7. Where the project lives

| Location within Settlements | Purpose |
| --- | --- |
| `Rules System/Second Draft/Rule Cards/` | Owning Draft 2 rule and catalogue notes. Edit current rules here. |
| `Rules System/Second Draft/Rulebook Sections/` | Thirteen chapter reading views made from live embeds. |
| `Rules System/Second Draft/Rule Text Assemblies/` | Shared context and source-family reading views, also using embeds. |
| `Rules System/Second Draft/` | Tables, boards, canvas, master/assembled views, reference sheets, indexes, decisions and instructions. |
| `Research/` | Other-game research and Rule of Carnage reference/episode material. Research is a design source, not automatically a Settlements ruling. |
| `Design Workshop/`, `Project Roadmap/`, `Records/`, `Templates/` | Supporting design work, planning, records and templates. |
| `Rules System/Archived/` | Earlier drafts, retired rules and snapshots. These preserve history rather than define the active system. |

For research, start with the [[Settlements/Research/Wargaming Research Hub\|Research hub]], [[Settlements/Research/Rule of Carnage Skirmish Game Design Reference\|Rule of Carnage design reference]], [[Settlements/Research/Rule of Carnage Episode Index\|episode index]] or [[Settlements/Research/Rule of Carnage Episode Notes\|episode notes]].

Some older root-level catalogue and canvas notes predate the current card system. Use this guide’s Draft 2 links for the active workspace. The rules remain a working proposal with playtesting and manuscript work still tracked in [[Settlements/Rules System/Second Draft/Draft 2 - Progress and Decisions\|Progress and Decisions]].

## 8. If something does not work

- **Missing creation command or canvas sync:** open **Settings → Community plugins** and enable **Settlements Rule Workspace**.
- **Missing tables/boards:** enable the **Bases** core plugin. Native Kanban requires Obsidian 1.14 or later.
- **Missing tag colours:** check **Colored Tags** under Community plugins.
- **Missing card styling:** check **Settings → Appearance → CSS snippets → bases-wrap**. The rule-card styling is included in that already-enabled snippet.
- **A card is absent from a view:** check its type, tags, Status, Scope and the view’s filters. Deferred cards are intentionally excluded from the main placement board.

The active vault is `C:\Users\Admin\Documents\Obsidian Vault`; Settlements is a folder inside it. The active plugin/configuration directory is the parent vault’s `.obsidian/`, rather than the small nested `Settlements/.obsidian/` folder.

The repository at `D:\AI-Workstation\Antigravity\apps\Settlements` contains development tools and a **one-way mirror** named `rules-vault/`. Edit the live Obsidian notes. I can refresh that mirror with `scripts/sync-rules.ps1` after changes. External exports, including Fibery copies, are not a live Obsidian sync provided by this workflow.

Guide updated **24 October 2026**. This document explains access and editing; it does not change any game rule.
