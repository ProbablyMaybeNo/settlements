# Settlements — Start here

- **[[Settlements/Rules System/Second Draft/Rule Cards - Complete Index|Rule index]]** — every rule, with Name, ID, Status, Parent, Family, Updated, description, tags and Notes. This is the only rule inventory.
- **[[Settlements/Rules System/Second Draft/Settlements Rule Workspace.base#Family progress|Family progress]]** — the high-level completion board. Open a family for its parents and their progress; open a parent for its rules.
- **[[Settlements/Rules System/Second Draft/Settlements Rule Workspace.base#Parent progress|Parent progress]]** — the same completion stages at parent level.
- **[[Settlements/Rules System/Second Draft/Settlements Rule Parents.canvas|Parent canvas]]** — the compact family/parent map you chose to keep.
- [[Settlements/Rules System/Second Draft/Settlements Rulebook - Assembled|Read the manuscript]] · [[Settlements/Rules System/Second Draft/Draft 2 - Battle Quick Reference|Battle reference]] · [[Settlements/Research/Wargaming Research Hub|Research]]

## Edit a rule

Open its name in the index. Edit the owning **Rule text** and keep its visible Summary, `summary` property and profile values consistent. Follow an embedded passage to its source. Existing V2 IDs and block anchors must stay intact. Put feedback in the index’s **Notes** field or the card’s **Design notes**; that feedback stays on the owning card.

Only changes to a rule’s meaning/procedure/values/limits/exceptions advance **Updated** (`last_rule_update`, YYYY-MM-DD, Pacific time). Formatting, status, parent and navigation edits do not. The index is a live Base: it needs no copied rows or manual date synchronization.

## Assign a parent

Change **Parent** in the index. The destination parent’s rule page updates automatically, as do completion totals. Parent uses `rule_parent`; Family uses `book_section`. These organize the library separately from the manuscript’s subsection and proposed chapter placement. Keep Family within the thirteen existing rulebook families. A new parent name creates its page and canvas card automatically.

## Parents and families

Group pages live under `Rules System/Second Draft/Rule Parents/` and `Rule Families/`. Their tables are live views of the owning cards. Parent/family planning comments belong under Parent notes or Family notes. Moving a card on the parent canvas changes its visual position only. It does not reassign its children.

## Completion progress

- **Written %:** Drafted + Confirmed + Locked, divided by included rules.
- **Confirmed %:** Confirmed + Locked, divided by included rules.
- **Final text %:** Locked, divided by included rules.
- **Parent completion:** included parents whose rules are all Locked.

Deferred rules are counted separately and excluded from first-edition percentages. Empty groups remain Pending. Family percentages count individual rules; separate totals show finished parents. A group reaches Drafted only when every included rule is written, Confirmed when all are Confirmed/Locked, and Locked when all are Locked. Board stages are calculated automatically—change the owning rules’ Status to record progress. Locked means text complete, not playtested balance.

## Create a rule

**Ctrl+P → Settlements Rule Workspace: Add a new rule card.** Enter name, Family, Parent, category, tags, description and full text. It creates a unique V2 note as Drafted and updates the live index, parent pages, canvas and completion figures. New profiles also need their proper entry type/profile fields. Add the owning block to the manuscript during editorial review.

## Access and recovery

Enable **Bases**, **Settlements Rule Workspace**, **Colored Tags** and the **bases-wrap** CSS snippet. **Ctrl+P → Settlements Rule Workspace: Refresh rulebook progress** refreshes totals. Generated progress properties and marked blocks should be maintained by the plugin; personal planning notes are preserved.

Current rule text lives only in `Rules System/Second Draft/Rule Cards/`; the manuscript’s chapter/context files embed those blocks. Research, design ideas and decision records remain reference material. Superseded organizational notes, old catalogue exports and historical drafts are stored outside this project under `Archive/Settlements/2026-10-24 - Retired organization/`. The archive is recoverable history, not another active workspace. [Obsidian Bases](https://obsidian.md/help/bases/syntax) supplies the live views.

The repository’s `rules-vault/` is a one-way mirror. Edit the live Obsidian vault, then mirror it with `scripts/sync-rules.ps1`.
