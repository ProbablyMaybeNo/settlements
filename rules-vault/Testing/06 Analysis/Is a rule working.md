---
type: settlements-testing-note
testing_id: TST-025
testing_section: Analysis
status: Planning
created: 2026-11-11
updated: 2026-11-11
summary: Evaluate resolution, understanding, choices, counterplay, pace and integration separately.
cssclasses:
- settlements-rule-group
tags:
- settlements/testing
---

# Is a rule working?

## Summary

A rule can be mechanically correct but hard to learn, powerful but fairly restricted, enjoyable but too slow, or useful alone but oppressive in combination. Diagnose which dimension needs work.

^testing-summary

## Evaluation scorecard

| Dimension | Evidence to look for | A warning | Next test |
| --- | --- | --- | --- |
| Resolves legally | Same stated situation reaches a consistent answer | Contradiction, infinite chain or missing required result | Deterministic reproducer and wording/source check |
| Understandable | Players find and apply the rule at actual opportunities | Repeated wrong interpretation or designer rescue | Revised presentation with fresh readers |
| Meaningful choice | Player can explain a relevant benefit and cost | Always mandatory, always ignored, or a choice with no practical effect | Intended-use opportunity plus an alternative |
| Counterplay | Opponent can change position, timing, tool or objective plan | Unavoidable repeated punishment with no useful response | Competent counterbuild or alternative approach |
| Worth its friction | Decision value justifies time, lookups and tokens | Repeated bookkeeping without a useful decision | Observe elapsed time; test a concise simplification |
| Appropriate lethality | Risk and recovery match the intended feel | Whole crews removed before choices, or no progress despite successful tactics | Controlled attack samples then full objective battle |
| Recoverable pressure | Stress/conditions create decisions without long exclusion | Several turns unable to contribute with no practical assistance | Recovery-under-pressure fixture and lost-action observations |
| Distinct role | Profile has a niche versus realistic alternatives | Another option is better in every relevant context | Matched substitution including hands/slots/actions and future price context |
| Integrates | Behaviour survives full battles and normal timing | Works only in a scripted duel or creates a loop with another effect | Related-combo test plus full-battle regression |
| Reproducible improvement | Changed version addresses the original problem | A favourable anecdote or different board is the only evidence | Original fixture, counterplay and version-matched comparison |

## Make the expectation falsifiable

Before a session write: **We expect [behaviour] when [opportunity]. We will observe [measure and denominator]. We will reconsider if [concrete contradictory evidence].**

For example, an ALERT test should ask whether players identify and value a legal reaction when one is available. It should not ask whether they agree that ALERT is balanced. A mechanic that is never available has not failed a usefulness test.

Choose timing and success targets after initial baselines, and label them proposed design targets. There is no universal desirable to-hit percentage, kill rate, activation duration or fun score for every skirmish game.

## Small changes first

Check packet clarity and correct application before changing a mechanic. Then investigate terrain, mission, player experience and resources. If power is the issue, preserve the intended niche while adjusting the smallest necessary part. A price may later address a strong option; it cannot fix a non-terminating loop or an action that cannot be resolved.

## Links

- [[Settlements/Testing/06 Analysis/Feedback to decision to retest|Feedback to decision to retest]]
- [[Settlements/Testing/03 Modules/Modules and priorities|Modules and priorities]]
- [[Settlements/Testing/START HERE - Settlements Testing|Testing workspace]]
