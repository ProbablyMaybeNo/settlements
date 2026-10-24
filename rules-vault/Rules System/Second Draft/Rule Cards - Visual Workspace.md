---
cssclasses:
- settlements-rule-workspace
---

# Rule cards — Visual workspace

Progress: [[Settlements Rule Progress.base|family and parent Kanban boards]] · [[Rulebook Progress - Start Here|completion definitions]].

Parent overview: [[Settlements Rule Parents.canvas|family/parent canvas]] → open a parent for its live rule list. Reassign rules in [[Rule Cards - Complete Index#Editable index|the editable index]]. [[Rule Parents - Start Here|Instructions]].


For project locations, creating/editing rules, feedback and troubleshooting, see [[Settlements/START HERE - Settlements Project|the Settlements project guide]].

Open **[[Settlements Rule Cards.base|Rules table / cards / review board]]**, **[[Settlements Rulebook Layout.base|Rulebook layout board]]**, or **[[Settlements Rulebook Layout.canvas|the draggable rulebook canvas]]** full-screen for the most room. These are live views of the individual notes.

## Table and review board

![[Settlements Rule Cards.base#Rules table]]

Switch the view menu to **All cards**, **Review board**, **Combat**, **To-hit bonuses**, **Armour bonuses**, or a catalogue. **Rules table** includes Last updated, Status, Category, Description, Tags, current chapter/subsection, Planned section, and review notes. Use Filter to combine category, tags, status and scope; use Search for the visible fields.

**Status** is `status`: Pending, Partial, Drafted, Confirmed, Locked or Deferred. See [[Rule Cards - Complete Index#Rule status|the definitions]]. Change it in a card’s properties or the Rules table; the workspace plugin updates its complete-index row. **Review flag** separately shows `review_status` (Unreviewed or Needs review). **Scope** follows Status: Deferred or Included. Change Status to defer or restore a card. Unreviewed does not mean approved or tested. Blank Last updated means unknown, not today; rearranging a card does not revise its rule date.

**Family → Type / Parent → Rule** gives the hierarchy, e.g. Core Mechanics → Stats → DEX. The [[Rule Cards - Complete Index|complete index]] shows both hierarchy columns; the live views expose Type / Parent and Family / Current chapter from the same owning fields.

**Review board:** drag a card between review-flag columns to change its review flag; this does not change the writing Status. Add a column through Group when you choose another status; no rules have been marked reviewed by this setup. Open a card to read its full text, follow linked mechanics, or write feedback in Design notes / review_notes.

## Rulebook layout

![[Settlements Rulebook Layout.base#Rulebook layout]]

The thirteen columns follow the agreed final rulebook chapters, including empty placeholder chapters. Scroll horizontally to reach later chapters; scroll within a column for its cards. Drag a card under a chapter header to edit **Planned section**. Its printed **Current subsection** remains visible as a reference.

This is an outline planning board. It does not rewrite the assembled rulebook, move note files, renumber IDs, change the rule text, or automatically assign a new subsection. The **Moved cards** view lists differences from current placement, ready for a later manuscript reassembly. **Placement table** lets you review all positions; **All placements including deferred** also shows the parked proposals. The main layout excludes Deferred material.

Cards are sorted by ID inside each column. Dragging changes chapter placement, not precise within-chapter reading order. Use review notes for a proposed subsection or sequence until we apply the layout to the manuscript.

## Draggable rulebook canvas

Open [[Settlements Rulebook Layout.canvas|Settlements Rulebook Layout.canvas]]. It contains all 483 original library notes as live file cards: thirteen chapter groups plus a separate parking group for the eighteen deferred proposals. The summary is embedded from each owning note rather than copied.

Drag a card by its title into another chapter group. Once its centre is inside that group and Canvas saves, **Planned section** updates in its note, table and board. Editing Planned section in those views also moves the existing canvas card to that chapter. The local **Settlements Rule Workspace** plugin must be enabled for automatic updates.

Use **Ctrl+P → Canvas: Jump to group** to navigate the chapter headings. Pan and zoom to work on individual cards. Cards outside chapter groups retain their previous placement. Deferred parking does not change Scope; moving a deferred card never approves its rule. Keep one file card per rule on this canvas so two copies cannot assign competing chapters.

Chapter placement is planning metadata. Positions inside a group do not set precise subsection/order, and the assembled manuscript is unchanged until we apply your chosen outline. Chapter groups have fixed mappings; renaming a group label does not rename the chapter. Canvas edits made while the plugin is disabled do not retrospectively change notes when it is enabled again.

## Adding a new rule

1. Press **Ctrl+P** and run **Settlements Rule Workspace: Add a new rule card** (or use the new rule-card ribbon icon).
2. Enter its name, category, chapter, optional subsection, comma-separated tags, concise description and full rule text.
3. Select **Create rule card**.

The command generates a clean card with the next unused V2 ID, required fields, Pacific dates, and a unique owning block. It adds the card to the canvas, both indexes and live views with **Status: Drafted / Review flag: Unreviewed**. You can then edit its text and Design notes normally. Use this command for an indexed new rule; the generic Bases **New** button does not perform the ID/index setup.

New cards still await placement of their owning block in the assembled chapter. Later semantic edits follow [[AGENTS|the normal rule-update tracking instructions]].

## Colours

The narrow strip marks category: coral for Combat/weapons; blue for movement/actions/setup; teal for terrain/interactions/devices; purple for morale/casualties/stealth; green for skills; gold for equipment/settlements/structures; slate for other rules. **Amber overrides category for Needs review; grey overrides it for Deferred.** Status and Scope remain written on the relevant views, so colour is not the only cue. Tags use the vault's existing Colored Tags palette.

## Sources

- [[Rule Cards - Start Here|Library and editing guide]]
- [[Rule Cards - Complete Index|Every card by name]]
- [[Settlements Rulebook - Assembled|Current assembled rulebook]]
- [[Settlements Core Rulebook Outline|Chapter and subsection outline]]

Presentation updated 2026-10-24. The individual cards still own the rules; the boards are views and planning metadata.
