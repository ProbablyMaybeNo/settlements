---
type: settlements-testing-note
testing_id: TST-018
testing_section: Recruitment
status: Planning
created: 2026-11-11
updated: 2026-11-11
summary: "Use online play to extend reach, while testing physical and software effects separately."
cssclasses:
- settlements-rule-group
tags:
- settlements/testing
---

# Remote and virtual tabletop testing

## Summary

Use online play to extend reach, while testing physical and software effects separately.

^testing-summary

## Is Tabletop Simulator an option?

Yes. Official TTS documentation supports custom mods and controlled Workshop visibility: [Steam Workshop](https://kb.tabletopsimulator.com/custom-content/steam-workshop/). That makes a private pilot or later public prototype possible. An existing repository `tts/` integration is historical and must be checked against current rules; no ready-to-play current module is claimed here.

**Community compatibility matters.** Protospiel Online currently does not support TTS; its FAQ discusses other virtual tabletops ([FAQ](https://protospiel.online/faq/)). Break My Game lists several alternatives and asks designers/testers to check the event's platform ([Weekly Online Playtesting](https://www.breakmygame.com/weekly-online-playtesting)). Do not assume that a TTS module gives access to every testing event. A 2D platform may be adequate for early procedure tests but needs an explicit height/LOS convention.

## Minimum remote build checklist

- [ ] Correct board scale: 48x48 inches, 6-inch deployment and current bases/templates.
- [ ] Fixed crews, profile rules, status markers, round/VP tracker and easily found PDF/reference.
- [ ] Facing, movement measurement, cover, roof height, model volume and hidden information work as intended.
- [ ] Public Hidden positions stay public; concealed device identity is not accidentally exposed.
- [ ] Both participants can load all assets; no host-only local file dependency.
- [ ] Save state and a reset copy with exact version/hash.
- [ ] A short control tutorial is timed separately from learning Settlements.
- [ ] Scripts do not silently auto-resolve, prevent or alter a legal rule choice.
- [ ] Log platform bugs and control confusion separately from game-rule issues.
- [ ] Avoid automating the very rule comprehension being tested in an unguided packet study.

## Physical regression

Test tape measuring, terrain reach, facing markers, token clutter, picking up models, actual template placement and vertical LOS with physical pieces. An instructive miniatures example is the Firefight developer's account of building/height concerns surfacing after extensive remote play: [Firefight Playtest Designer Notes: Part One](https://www.manticgames.com/news/firefight-playtest-designer-notes-part-one/).

## Sharing and rights

Use your own or appropriately licensed assets and agree recording/screenshot use with participants. Choose private/friends/public access deliberately. A public PDF or mod can circulate beyond the initial group; version and credit it accordingly. This is a practical distribution choice, not legal advice or a promise of control over copies.

## Links

- [[Settlements/Testing/START HERE - Settlements Testing|Testing workspace]]
- [[Settlements/Rules System/Master Rules System/Master Rules System|Approved Master Rules System]]
