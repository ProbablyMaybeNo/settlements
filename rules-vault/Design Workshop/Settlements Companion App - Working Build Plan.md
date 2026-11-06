---
type: working-plan
status: planning
created: 2026-11-06
tags:
  - settlements/companion-app
  - settlements/planning
---

# Settlements Companion App - Working Build Plan

Working record of Ross's direction for a Settlements companion app. Agreed direction, proposed ideas, and open questions are kept separate below. This is a planning note; it does not approve implementation choices or change game rules.

## Agreed direction

### Purpose and scope

- Maintain persistent unit rosters.
- Maintain persistent settlements, including a top-down layout.
- Provide searchable rules and a player-selected one-page cheat sheet.
- Prioritize usability and lean scope. A vintage terminal aesthetic should support clarity and remain subordinate to it.
- Use visual UI best practices to guide the app's presentation.

### Rosters and unit details

- Roster rows show essential unit information. The exact columns are still to be decided.
- A detailed mobile unit sheet provides the fuller unit view.
- Include brief reminders for the unit's skills and weapons.
- Tapping a rule opens a short bottom sheet or a fuller view when needed.
- Returning from a rule restores the player's previous scroll position.

## Proposed ideas - not yet decisions

### Rules and cheat sheet

- Allow players to reorder their chosen cheat-sheet entries.
- Provide a preview and print option for the cheat sheet.
- On desktop, consider a side panel for rules so the roster or unit context stays visible.

### Settlement layout

- Consider a top-down grid.
- Offer tap-to-place alongside dragging, with undo for placement changes.

### Navigation and controls

- Keep primary navigation visible.
- Use accessible controls that are clear and easy to operate.

## Open questions

| Topic | Decision still needed |
| --- | --- |
| Settlement map | Is the top-down layout visual, mechanically meaningful, or both? Which game rules, if any, depend on placement? |
| Platforms | Which platforms should the first version support? |
| Offline use and sync | What must work offline, and should data sync between devices? |
| Roster columns | Which information is essential in each row, and which belongs only on the detailed sheet? |
| Rule versioning | How will the app identify and update rule versions, including references from units and cheat sheets? |
| Cheat-sheet overflow | What happens when the player's selected content does not fit on one page? |

## Visual UI research and prototype guidance

### Published accessibility criteria

These are external criteria to use when evaluating designs, separate from the prototype suggestions below. Recording them does not mean a design has been tested or that a compliance scope has been approved.

- **Text contrast:** WCAG 2.1 SC 1.4.3 (Level AA) requires at least **4.5:1 for normal text** and **3:1 for large text**, subject to the criterion's exceptions. Large text means at least 18 pt (24 CSS px), or 14 pt (about 18.67 CSS px) when bold. A heading is not automatically large text. [W3C explanation of Contrast (Minimum)](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html).
- **Text resizing:** WCAG 2.1 SC 1.4.4 (Level AA) requires text to resize to **200% without loss of content or function**, except captions and images of text. Check controls and labels as well as rule paragraphs. [W3C explanation of Resize Text](https://www.w3.org/WAI/WCAG21/Understanding/resize-text).

### Design-system references - guidance, not universal specifications

- [GOV.UK type scale](https://design-system.service.gov.uk/styles/type-scale/) demonstrates consistent font-size and line-height roles, responsive typography, and relative CSS units that support resizing. Its particular sizes belong to that design system; they are not mandatory app sizes.
- [GOV.UK colour guidance](https://design-system.service.gov.uk/styles/colour/) assigns colours to functional roles such as text, backgrounds, links, focus, errors, and success. Use the role-based approach as a reference without assuming its palette has been adopted for this app.
- [Material typography: applying type](https://m3.material.io/styles/typography/applying-type) is a further typography reference for the visual design pass.

### Starting prototype suggestions - not approved specifications

- Try neutral background, surface, and text colours, one primary accent, and semantic warning, error, and success colours accompanied by labels or icons.
- Try body text at **16-18 CSS px**, headings at **20-24 CSS px**, and body line height around **1.5**. These are starting values to test, not universal standards or fixed sizes for every heading.
- Use a readable sans-serif for long rule text. Consider monospace for headings or statistics where it remains clear. Avoid pixel fonts for paragraphs.
- Keep the vintage terminal character secondary to reading and operating the app.

### Validation still to do

- Measure actual foreground/background contrast pairs, including text and control states; no palette has been selected or shown to pass.
- Check 200% text resizing in the proposed roster, unit-sheet, rule, and cheat-sheet views for clipped content or lost functionality.
- Verify touch-target size and spacing on the intended devices, including placement controls and bottom-sheet actions.
- Test readability under real gaming-table lighting and typical viewing distances.

## Proposed planning sequence - for discussion

1. Define the lean first version around the agreed features; decide what can wait.
2. Sketch the roster, mobile unit sheet, rule lookup, cheat-sheet selection, and settlement layout flows. Use these to settle the open questions rather than assume answers.
3. Agree the essential information each view needs and how rules link to units and cheat sheets.
4. Choose platforms, storage, offline behavior, and any sync approach after the product needs are clearer.

Implementation has not started. No technology stack, delivery schedule, or additional feature commitments have been selected in this note.

## Project context

- [[Settlements/START HERE - Settlements Project|Settlements project home]]
- [[Settlements/Rules System/Second Draft/Rule Cards - Complete Index|Current rule index]]
- [[Settlements/Rules System/Second Draft/Item Cards - Library|Current item-card library]]

These links provide project context. The app's rule-version and update policy remains an open question.
