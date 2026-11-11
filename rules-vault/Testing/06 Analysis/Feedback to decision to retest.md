---
type: settlements-testing-note
testing_id: TST-014
testing_section: Analysis
status: Planning
created: 2026-11-11
updated: 2026-11-11
summary: "Translate observed problems into small, justified changes and verify that they worked."
cssclasses:
- settlements-rule-group
tags:
- settlements/testing
---

# Feedback to decision to retest

## Summary

Translate observed problems into small, justified changes and verify that they worked.

^testing-summary

## Separate the evidence layers

1. **Observation:** what happened, with session/round/position or a rule lookup.
2. **Player response:** what the player expected, felt or chose, preferably in their words.
3. **Interpretation:** why it may have happened; include alternatives.
4. **Proposal:** a possible remedy, not automatically the player's suggested fix.
5. **Decision:** an explicit accepted/rejected/deferred choice and its rationale.
6. **Retest:** evidence on the changed version, including neighbouring mechanics.

Use [[Settlements/Testing/08 Templates/Issue template|Issue template]] and [[Settlements/Testing/08 Templates/Decision and retest template|Decision and retest template]]. Link duplicates to one issue; keep the number of independent groups affected separate from the number of comments.

## Diagnose before adjusting power

| Category | Typical question | Likely next step |
| --- | --- | --- |
| Rules contradiction / missing resolution | Can the action be resolved consistently? | Clarify the source and retest the packet. |
| Learnability / reference | Did the player find the correct rule? | Placement/example/wording test before a mechanical nerf. |
| Mechanical power / counterplay | Does competent opposition have a useful response? | Reproduce under controlled conditions; compare resources and terrain. |
| Pacing / cognitive load | What repeatedly consumes time or attention? | Observe steps, trim duplication and test the revised flow. |
| Scenario / terrain | Is the apparent winner favoured by the mission or map? | Repeat on a matched/alternative board with swapped roles. |
| Price / availability | Is it strong but limited or costly enough? | Record measured value for the later pricing pass. |
| Audience preference | Is it outside this player's desired genre/experience? | Preserve the report; distinguish taste from universal failure. |
| Tool / implementation | Did a virtual module or simulator apply the wrong rule? | Fix the tool and rerun; do not change the real rule to fit it. |

## Triage

- **Critical:** no legal resolution, non-terminating loop, impossible objective or whole session blocked.
- **Major:** recurrent loss of useful choices, severe unresolved counterplay problem, or core rule misunderstood across independent groups.
- **Moderate:** avoidable pauses, uncommon ambiguity or a weak/overloaded option that still allows play.
- **Minor:** presentation polish or isolated low-impact wording.

Record frequency, opportunity, impact, confidence and audience separately. Do not multiply them into a fake objective truth score. One severe incident can matter more than many cosmetic comments.

## Handling feedback fairly

Collect individual responses before the loudest player shapes a group verdict. Look at winners and losers, beginners and experienced players, repeat and fresh groups, physical and virtual sessions separately. Disagreement can reveal different conditions rather than bad feedback. Ask why an option was skipped: not noticed, misunderstood, never relevant, too risky, or genuinely ineffective.

Do not count friends' encouragement as proof of market demand. Do not ignore a novice's confusion because an expert guessed the intended rule. Preserve praise tied to a concrete moment: that is evidence about what should survive a revision.

## Change-control loop

- [ ] Reproduce or document the issue and counter-evidence.
- [ ] State the design intent and smallest plausible remedy.
- [ ] Identify every affected owner/profile, packet page and simulator assumption.
- [ ] Ross chooses approve, reject, defer or isolated test variant.
- [ ] On approval, update the live owners through the normal rules workflow; preserve provenance and semantic dates appropriately.
- [ ] Regenerate the packet/aids, create a new snapshot/hash and concise change log.
- [ ] Run the original reproducer, related counterplay and a normal full-battle regression.
- [ ] Close only after the retest supports closure; otherwise revise/reopen.

Body language can suggest a follow-up question; it is not a diagnosis of a player's feelings. Combine behaviour and explanation rather than averaging every opinion into one fun number. Research framing: [Choose the right playtest method](https://gamesuserresearch.com/choose-the-right-playtest-method/), [Find usability issues in games with playtests](https://gamesuserresearch.com/find-usability-issues-in-games-with-playtests/).

## Links

- [[Settlements/Testing/START HERE - Settlements Testing|Testing workspace]]
- [[Settlements/Rules System/Master Rules System/Master Rules System|Approved Master Rules System]]
