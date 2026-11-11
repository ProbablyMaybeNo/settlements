---
type: settlements-testing-note
testing_id: TST-013
testing_section: Data
status: Planning
created: 2026-11-11
updated: 2026-11-11
summary: "Empty raw CSV records with explicit units, identifiers, missing values and denominators."
cssclasses:
- settlements-rule-group
tags:
- settlements/testing
---

# Data dictionary and recording

## Summary

Empty raw CSV records with explicit units, identifiers, missing values and denominators.

^testing-summary

## Ownership and entry

The CSVs in this folder are the **structured raw records**. Session notes contain narrative and evidence links, not an independently maintained numeric duplicate. Transcribe the paper forms after play. Keep original wording in observations; separate interpretation into the Issue record. Files start with headers only: zero real data.

| File | Row means | Key details |
| --- | --- | --- |
| `sessions.csv` | One actual session | ID, rules/packet revision and hash, module, mode, platform, board/scenario/rosters, player/group/pair IDs, first player, separate timings, completed/incomplete and outcome. |
| `rounds.csv` | One round snapshot in one session | Duration in minutes; **VP earned that round**, not cumulative; conscious on-board fighters; Break failures and action-loss notes. |
| `observations.csv` | One concrete event | Round/actor/owner ID, expected and actual behaviour, consequence, intervention, temporary ruling and evidence link. |
| `feedback.csv` | One participant's independent exit sheet | Pseudonymous participant ID; experience; five responses; no contact details. |
| `attacks.csv` | One sampled single-target shooting or melee exchange | Record attack dice, hits, Injury checks versus dice, Wounds, Stress and state; use only declared instrumented blocks. |
| `opportunities.csv` | One mechanic's tally in a declared session block | Eligible opportunities, uses, successes, actions/resources, benefit and non-use explanation. |
| `issues.csv` | One consolidated concern | Category, severity, related owners, supporting and contradictory session IDs, hypothesis, proposal, owner and state. |
| `decisions.csv` | One actual decision | Issue, rationale, approver, affected version, retest and result. A proposal is not an approval. |
| `coverage.csv` | One approved source owner | Planned module, actual evidence IDs, use/understanding/integration status and limitations. Not a second source of rules text. |
| `recruitment.csv` | One consented recruitment lead | Pseudonym/route, experience and availability notes; contact details stored separately if needed. |

## Definitions

- Session and round time fields use **minutes**; attacks.csv uses seconds for duration_seconds. Timings are counted separately for setup, teaching, play and feedback. Round duration is not time since the session started.
- `outcome`: `red_win`, `blue_win`, `draw`, `incomplete` or `not_applicable`. Do not infer a winner from a stopped score.
- `mode`: `solo`, `guided`, `focused`, `integration`, `unguided` or `regression`; `platform`: `physical`, `TTS`, `TTP`, `Tabletopia`, `Screentop` or another named platform.
- `assistance`: `none`, `initial_teach`, `rule_rescue` or `logistical_only`; explain actual assistance. The label unguided does not override a logged rescue.
- Blank = **not recorded / not applicable**, with a note where useful. Zero = measured absence. Never replace unknown opportunities with zero.
- In opportunities.csv, successes means successful **uses**, counted once per use. Do not enter individual hits there; a multi-die attack can hit more than once.
- attacks.csv is for single-target shooting/melee only. Area placement and multiple affected targets belong in the event/focused fixture record and must not be pooled into a single-target hit rate. Injury checks are Wound opportunities; Injury dice can exceed checks for best-of effects.
- Opportunity means the action/skill was legally available and relevant in the observed block. `uses <= opportunities`; successes cannot exceed uses. Explain exception-based multiple outcomes separately.
- Hits, Wounds and attacks are different denominators. Conditional Injury success uses Injury attempts, not total shots or elapsed rounds.
- Use `source_version` and IDs for affected rules. Do not pool different versions, boards or player populations without explicit stratification.

## Updating reports

Run the repository script `tools/testing-workspace/analyse_data.py` after transcribing data. It validates basic IDs, counts and enums and regenerates Current findings. It does not decide which mechanics to change or certify statistical independence. Review the event and group context yourself.

## Data care

Use participant IDs in analysis. Keep optional contact details outside public packets. Recording requires explicit permission; store the permission and retention plan with the session, not inside anonymous feedback. Public summaries should not expose private recordings or identifying messages.

## Links

- [[Settlements/Testing/START HERE - Settlements Testing|Testing workspace]]
- [[Settlements/Rules System/Master Rules System/Master Rules System|Approved Master Rules System]]
