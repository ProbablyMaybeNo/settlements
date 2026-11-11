---
type: settlements-testing-note
testing_id: TST-008
testing_section: Plan
status: Planning
created: 2026-11-11
updated: 2026-11-11
summary: "Use learning gates and uncertainty, not a universal game quota."
cssclasses:
- settlements-rule-group
tags:
- settlements/testing
---

# How many games are enough

## Summary

Use learning gates and uncertainty, not a universal game quota.

^testing-summary

## There is no single number

The initial 15-19 external battles in the programme are a resource estimate, not an industry rule or a release certificate. One repeatable rule contradiction can justify action immediately; many favourable games cannot prove an unexercised subsystem works.

Count separately: **sessions, complete games, short fixtures, unique players, unique groups, repeat games, independent opponent pairs, exact rules versions and actual mechanic opportunities**. Ten games by the same pair are not ten independent views of learnability. A revised mechanic needs fresh evidence; old games remain history, not current-version confirmations.

## What is enough for a decision?

| Decision | Appropriate evidence |
| --- | --- |
| Text prevents setup or a legal resolution | A clear reproducible case can be enough to fix text. Retest the corrected packet. |
| A rule is confusing | Observe fresh players, identify the mistaken interpretation, revise placement/wording and try again. |
| An option feels oppressive | Reproduce with competent counterplay and compare position, skill, scenario and resource differences. |
| A choice is rarely used | Count eligible opportunities; ask why. Lack of use alone is not weak power. |
| Two roster packages are closely balanced | Many controlled comparisons across contexts, with statistical uncertainty; use simulation for cheap repetitions, humans for behaviour. |
| The whole product is release-ready | All declared scope and regression gates, not one win-rate total. |

## Why small win samples cannot settle close balance

Illustrative **95% Wilson intervals**, assuming independent binary win/loss games, exactly half wins, no draws or repeated-player dependence:

| Games | Observed wins | Approximate interval |
| ---: | ---: | --- |
| 10 | 5 | 23.7%-76.3% |
| 20 | 10 | 29.9%-70.1% |
| 50 | 25 | 36.6%-63.4% |
| 100 | 50 | 40.4%-59.6% |

These are calculations, not Settlements results. Formula reference: [Confidence intervals for proportions](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm). Draws, paired swaps, shared players, selected opponents and changing rules invalidate treating all results as independent binary trials. Use group/pair-aware analysis for comparisons; never hide draws or incomplete games.

## Stopping rule for each wave

Before starting, write the question and what evidence could change the decision. Review after the planned wave rather than repeatedly checking until a favourite result appears. Stop collecting for that question when the decision is clear enough, coverage is adequate and important alternative explanations have been checked. Extend when evidence conflicts or the relevant event has not occurred.

Before release, require clean regression on the final packet and all release-scope mechanics. More tests of the easy parts cannot substitute for missing tests of rare or advanced content.

## Links

- [[Settlements/Testing/START HERE - Settlements Testing|Testing workspace]]
- [[Settlements/Rules System/Master Rules System/Master Rules System|Approved Master Rules System]]
