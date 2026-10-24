# Rulebook progress — start here

![[Settlements Rule Progress.base#Family progress]]

Open [[Settlements Rule Progress.base|the progress workspace]] full-screen. Switch between **Family progress**, **Parent progress** and **Family totals**. Click/open a family card to see every parent in that family with its current stage and completion figures. Open a parent for its live rule list, then a rule for its full text.

## What completion means

- **Written %:** Drafted + Confirmed + Locked rules, divided by first-edition rules.
- **Confirmed %:** Confirmed + Locked rules, divided by first-edition rules.
- **Final text %:** Locked rules, divided by first-edition rules. This is publication-text completion, not playtesting completion.
- **Parent completion:** included parents whose rules are all Locked, divided by parents containing first-edition rules.
- **Deferred:** counted separately and excluded from first-edition percentages. A deferred-only family/parent shows Deferred. Empty groups show Pending / No rules assigned.

Family percentages count individual rules, rather than averaging percentages of differently sized parents. Each family also shows how many parents are fully finished. Percentages are rounded; use the exact counts to check completion.

## Automatic stages

| Stage | Computed meaning |
| --- | --- |
| Pending | No included rule has been partly or fully written, or no rules assigned. |
| Partial | At least one included rule is Partial or written, but some are still Pending/Partial. |
| Drafted | Every included rule is at least Drafted; some await confirmation. |
| Confirmed | Every included rule is Confirmed or Locked; some await final text review. |
| Locked | Every included rule is Locked. |
| Deferred | Only Deferred rules are assigned. |

Board columns are computed views, not manual approvals. Change the individual rule’s **Status** in [[Rule Cards - Complete Index#Editable index|the editable index]] or on its owning card; the parent and family totals refresh automatically through Settlements Rule Workspace. Do not edit the generated progress properties to approve a section. Metadata updates do not revise rule-text dates.

**Type / Parent** reassignments update membership and progress. New rules created through the rule-card command are included. The plugin also recalculates when it loads, and **Ctrl+P → Settlements Rule Workspace: Refresh rulebook progress** refreshes manually.

Planning comments belong under **Family notes** or **Parent notes**. The automatic progress block and properties are maintained by the plugin; your planning notes are preserved. Rule text remains in the original rule cards. The [[Settlements Rule Parents.canvas|parent canvas]] is the compact navigation map; the [[Settlements Rulebook Layout.canvas|original canvas]] still handles planned chapter placement.
