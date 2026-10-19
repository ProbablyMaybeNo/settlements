# Second Draft rule-update tracking

When an actual rule-text edit changes a rule's meaning, procedure, values, limits or exceptions:

1. Edit the owning card's canonical block; preserve its stable ID, block anchors, links and embeds.
2. Set that card's `last_rule_update` to the edit date as `YYYY-MM-DD` in Pacific time (`America/Los_Angeles`). Preserve all unrelated properties. Leave unknown dates blank or absent; never derive semantic rule revisions from filesystem timestamps.
3. Keep its existing frontmatter `summary` and visible Summary consistent, using a brief description of the current rule. Update its Last updated cell in `Rule Cards - Complete Index.md`, plus only its corresponding row's Concise description and Last updated cells in `Settlements Rules System Version 2 - Rules and Mechanics Review.md`; preserve Notes and links.
4. `Settlements Rule Cards.base` displays `last_rule_update` as **Last updated** automatically. Do not stamp cards that merely embed a changed block; the date belongs to its source owner. Date an embedding card only if its own rule text also changes.

Formatting, spelling cleanup without a meaning change, metadata, summaries, links, indexes and other housekeeping do not count as rule revisions and must not advance this date. Tracking setup or repair also does not advance it. Keep rule changes within the user's approved scope.
