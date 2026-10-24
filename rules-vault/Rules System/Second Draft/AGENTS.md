# Second Draft rule-update tracking

When an actual rule-text edit changes a rule's meaning, procedure, values, limits or exceptions:

1. Edit the owning card's canonical block; preserve its stable ID, block anchors, links and embeds.
2. Set that card's `last_rule_update` to the edit date as `YYYY-MM-DD` in Pacific time (`America/Los_Angeles`). Preserve all unrelated properties. Leave unknown dates blank or absent; never derive semantic rule revisions from filesystem timestamps.
3. Keep its existing frontmatter `summary` and visible Summary consistent, using a brief description of the current rule. Update its Last updated cell in `Rule Cards - Complete Index.md`, plus only its corresponding row's Concise description and Last updated cells in `Settlements Rules System Version 2 - Rules and Mechanics Review.md`; preserve Notes and links.
4. `Settlements Rule Cards.base` displays `last_rule_update` as **Last updated** automatically. Do not stamp cards that merely embed a changed block; the date belongs to its source owner. Date an embedding card only if its own rule text also changes.

Formatting, spelling cleanup without a meaning change, metadata, summaries, links, indexes and other housekeeping do not count as rule revisions and must not advance this date. Tracking setup or repair also does not advance it. Keep rule changes within the user's approved scope.

## Editorial status and hierarchy

`status` uses exactly Pending (unwritten), Partial (incomplete/nonfunctional), Drafted (written, awaiting confirmation), Confirmed (confirmed, awaiting final text review), Locked (final text ready for rulebook), or Deferred (outside first edition). Do not infer confirmation or locking from presence of text. `review_status` remains a separate Review flag. Scope (`publication`) is derived by the workspace plugin: Deferred iff Status is Deferred, otherwise Included. Change Status to defer/restore a card.

The Complete Index mirrors Status plus Type / Parent and Family for each V2 ID. Family comes from `book_section`; Type / Parent from editable `rule_parent` (initially seeded from catalogue type or ordinary-rule subsection). The plugin refreshes these cells after card edits and on startup; preserve user link/date annotations. Planned section is separate from recorded chapter placement. These metadata changes do not advance `last_rule_update`.

Parent pages under `Rule Parents/` use live Bases filters on `book_section` plus `rule_parent`. Complete Index → Editable index embeds the Parent assignments Base view; edit that live cell rather than the static mirror. Parent canvas moves are visual only, and parent reassignment does not change entry_type, book_subsection, semantic dates or manuscript embeds.
