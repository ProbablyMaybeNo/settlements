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
- Maintain persistent settlements, initially through a list-based settlement tracker. A graphical top-down map is a later proposal.
- Provide searchable rules and one customizable reference sheet, with a one-page goal.
- Prioritize usability and lean scope. A vintage terminal aesthetic should support clarity and remain subordinate to it.
- Use visual UI best practices to guide the app's presentation.

### Initial settlement tracker

- Provide a structure catalogue from which players can add structures. Whether it uses categories or one list remains undecided.
- The settlement page lists the structures the player has acquired.
- Tapping an acquired structure reveals its rules and benefits.
- Begin with this list-based flow; the graphical top-down map is a later proposed enhancement.

### Initial battle use

- Initial battle use is primarily reference: unit stats, weapon stats, what skills do, actions, core mechanics, and roll tables.
- Live wound or activation tracking has not been requested for this initial scope.

### Customizable battle reference sheet

- Provide **one customizable reference sheet** with a default layout containing most tables and rules needed during battle.
- Players start with that default layout and can add or remove tables and rule sections; they do not need to start from a blank sheet.
- Retain the one-page goal. How to handle selections that overflow one page remains unresolved.

### Mobile reference layout

- Present the same selected reference content as a customizable list of clearly named tables and rule sections.
- Supply a default list and let players add or remove entries.
- Tapping an entry opens the actual table or rule section in a readable view. Back returns to the same position in the list.
- This is the mobile presentation of the single customizable reference sheet, rather than a separate core/custom reference system.

### Rosters and unit details

- Roster rows show essential unit information. The exact columns are still to be decided.
- A detailed mobile unit sheet provides the fuller unit view.
- Include brief reminders for the unit's skills and weapons.
- Tapping a rule opens a bottom sheet or fuller view. Short versus full presentation remains undecided; Ross has not required exact skill wording.
- Returning from a rule restores the player's previous scroll position.

### Mobile navigation and utility controls

- Ross prefers a compact menu button in a top corner on mobile. The left or right corner is still undecided, as is a slide-out drawer versus a full-page menu.
- Label the main destinations **Roster**, **Settlement**, and **Rules** inside the menu.
- Familiar icon-only utility controls can work in clear context, including back, close, a contextual edit pencil, and an account avatar. Give these controls accessible names; a visible label is not mandatory on every utility control.

### Visual hierarchy

- Ross finds that neon green and dim green alone flatten the visual hierarchy.
- Distinguish text, interactive controls, headings, and stats through semantic colour roles, weight, spacing, and boundaries.
- The exact palette remains undecided.

## Proposed ideas - not yet decisions

### Rules and cheat sheet

- Allow players to reorder their chosen cheat-sheet entries.
- Provide a preview and print option for the cheat sheet.
- A print layout may arrange the selected content together. The one-page goal and overflow handling remain to be resolved.
- On desktop, consider a side panel for rules so the roster or unit context stays visible.

### Settlement layout

- Later enhancement: consider a graphical top-down map or grid after the initial list-based tracker.
- For that later map, consider tap-to-place alongside dragging, with undo for placement changes.

### Navigation and controls

- Use accessible controls that are clear and easy to operate.

### Superseded proposals

- The prior mobile bottom-navigation proposal is superseded by Ross's preference for a compact top-corner menu button. The earlier suggestion to keep primary navigation visible should not be treated as a requirement for persistent navigation tabs.
- Any proposal for separate core and custom reference sheets is superseded by the single customizable sheet with a useful default layout.
- Treating a graphical top-down settlement map as an initial requirement is superseded by the list-first settlement tracker.

## Open questions

| Topic | Decision still needed |
| --- | --- |
| Structure catalogue | Should players browse categories or one list? |
| Future settlement map | What should the later map show? Current drafted plots are accounting slots, not a placement puzzle; any new placement mechanics would need a separate rules decision. |
| Platforms | Which platforms should the first version support? |
| Offline use and sync | What must work offline, and should data sync between devices? |
| Roster columns | Which information is essential in each row, and which belongs only on the detailed sheet? |
| Rule versioning | How will the app identify and update rule versions, including references from units and cheat sheets? |
| Rule and skill presentation | Where should short reminders or full text appear? Short versus full presentation remains undecided; exact skill wording is not a requirement. |
| Cheat-sheet overflow | What happens when the player's selected content does not fit on one page? |
| Mobile menu placement | Should the compact menu button be in the left or right top corner? |
| Mobile menu presentation | Should it open a slide-out drawer or a full-page menu? |
| Visual palette | Which colours will express the semantic roles and visual hierarchy? The exact palette is undecided. |

## Settlement rules reviewed - drafted inputs for planning

Reviewed the current Second Draft owning rule cards and all twenty structure cards (V2-423 through V2-442). All reviewed settlement cards are **Drafted / Unreviewed**, not confirmed or locked. The findings below describe those drafts; possible tracker fields and automation remain planning candidates, beyond the explicitly agreed list/catalogue/detail flow above.

| Area | Current drafted rule and possible tracker needs | Source |
| --- | --- | --- |
| Founding | Start with 1,000 Credits, 125 Materials, twelve plots, and free Headquarters, Generator, Materials Processor, and Salvage Yard. Each occupies a plot. Founding purchases operate for the first battle; allocate Power once before it, with no founding production. | [[Settlements/Rules System/Second Draft/Rule Cards/V2-399 - Founding a settlement\|V2-399]] |
| Settlement rounds | One round follows each qualifying battle, not elapsed real time: record battle; allocate workers/Power; resolve injuries/services; collect resources; apply XP; manage roster/buildings; close records. New construction operates at the next Settlement round, except founding. Per-round limits do not refresh during pre-battle shopping. | [[Settlements/Rules System/Second Draft/Rule Cards/V2-401 - Settlement round and availability timing\|V2-401]] |
| Power and fuel | Each Generator supplies 10 Power per allocation; multiple Generators add output. Allocate each powered structure's entire requirement or leave it unpowered. Passive structures need none. Power expires at the next allocation and cannot be saved or sold. No fuel requirement was found in current Second Draft rules. | [[Settlements/Rules System/Second Draft/Rule Cards/V2-406 - Power and workers\|V2-406]]; [[Settlements/Rules System/Second Draft/Rule Cards/V2-422 - Structure catalogue conventions\|V2-422]] |
| Structure details and benefits | Catalogue fields are Materials cost, prerequisite, Power, benefit, and one-worker effect. Benefits include production, capacity, access, or a named service; limits and bonuses are specific to each structure. A Materials Processor uses 2 Power for 20 Materials/round (+2 with a worker); a Salvage Yard uses 2 for 50 Credits (+5). Passive housing/storage structures need no Power. | [[Settlements/Rules System/Second Draft/Rule Cards/V2-422 - Structure catalogue conventions\|V2-422 and linked V2-423–442 item cards]] |
| Workers | An available owned fighter who sat out the preceding Battle Roster, is not a prisoner/convalescent, and is not assigned elsewhere may work. One worker occupies a structure's slot. Apply only its printed benefit, only while powered where required; no generic 10% bonus. A Generator worker adds +1 Power before allocation. No recurring wages, food, water, or proficiency track. | [[Settlements/Rules System/Second Draft/Rule Cards/V2-401 - Settlement round and availability timing\|V2-401]]; [[Settlements/Rules System/Second Draft/Rule Cards/V2-406 - Power and workers\|V2-406]] |
| Construction and plots | Pay Materials and reserve a vacant plot; prerequisites must already be built, but need not be powered for construction. One of each unless specified. Demolition frees the plot without a refund; Headquarters cannot be demolished. Removing a prerequisite disables dependents. Plots are accounting slots, not a placement puzzle; buy four more for 40 Materials, at most three times, maximum 24. | [[Settlements/Rules System/Second Draft/Rule Cards/V2-413 - Construction, housing, plots and storage\|V2-413]] |
| Housing, storage, inventory | Headquarters houses twelve and stores 250 Materials; Bunkhouses add six residents, Storehouses add 250 storage. Housing includes workers, prisoners, and recovering fighters; overcapacity blocks recruitment without deleting people. Credits/equipment storage is unlimited. Discard excess Materials only at round close after spending. Keep shared stores and device scrap without double-counting carried items. | [[Settlements/Rules System/Second Draft/Rule Cards/V2-413 - Construction, housing, plots and storage\|V2-413]]; [[Settlements/Rules System/Second Draft/Rule Cards/V2-451 - Battle and settlement record sheets\|V2-451]] |
| Access and services | Powered facilities gate purchases, crafting, medical services, and device rebuilding. Last valid Power allocation persists between rounds for access; losing an unlock does not disable already owned equipment. Service limits apply per round. These are candidates for reference and counters, not approved automation. | [[Settlements/Rules System/Second Draft/Rule Cards/V2-410 - Purchasing, selling and unlocks\|V2-410]]; [[Settlements/Rules System/Second Draft/Rule Cards/V2-418 - Medical services and device rebuilding\|V2-418]]; [[Settlements/Rules System/Second Draft/Rule Cards/V2-443 - Crafting and access\|V2-443]] |
| Damage scope | No mandatory building-hit-point track is defined. V2-413 mentions disabled/destroyed capacity structures without deleting owned people or equipment, but supplies no general building-damage procedure. Device Offline/Destroyed states, scrap, and rebuilding are defined separately; do not infer building health or repair mechanics from them. | [[Settlements/Rules System/Second Draft/Rule Cards/V2-422 - Structure catalogue conventions\|V2-422]]; [[Settlements/Rules System/Second Draft/Rule Cards/V2-413 - Construction, housing, plots and storage\|V2-413]]; [[Settlements/Rules System/Second Draft/Rule Cards/V2-418 - Medical services and device rebuilding\|V2-418]] |

V2-451 explicitly calls for settlement records of Credits, Materials/capacity, plots, buildings, Power allocation, workers, pending construction, person availability/recovery, and shared inventory. This supports future tracker design; it does not itself commit the initial app to implementing every record field or live battle tracking.

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
2. Sketch the roster, mobile unit sheet, rule lookup, cheat-sheet selection, and settlement structure-list/catalogue/detail flows. Use these to settle the open questions rather than assume answers; keep the graphical map for a later pass.
3. Agree the essential information each view needs and how rules link to units and cheat sheets.
4. Choose platforms, storage, offline behavior, and any sync approach after the product needs are clearer.

Implementation has not started. No technology stack, delivery schedule, or additional feature commitments have been selected in this note.

## Project context

- [[Settlements/START HERE - Settlements Project|Settlements project home]]
- [[Settlements/Rules System/Second Draft/Rule Cards - Complete Index|Current rule index]]
- [[Settlements/Rules System/Second Draft/Item Cards - Library|Current item-card library]]

These links provide project context. The app's rule-version and update policy remains an open question.
