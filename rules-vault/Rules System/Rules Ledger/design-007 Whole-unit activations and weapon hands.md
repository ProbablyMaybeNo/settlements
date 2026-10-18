---
type: design-decisions
status: User rulings integrated; related implementation choices await playtesting
created: 2026-10-18
---
# Whole-unit activations and weapon hands

## Confirmed by Ross

- Weapon slots reflect a fighter's two literal hands. No weapon needs more than two; Heavy weapons use both.
- Alternate whole-unit activations. The activated fighter has one Move and one Core and resolves them before the opponent activates a fighter.
- Ross explicitly selected either action order.

## Integration

[[Settlements Rules System Version 2]] updates definitions, Chapter 6 timing, Pinned recovery, Run and Gun, drone commands, morale movement, roster fields and examples. Heavy weapon profiles and the custom Heavy class now take two weapon slots. The included knife remains slot-free while stowed and needs one hand to use. Equipment slots, armour, costs and existing Heavy handling limits are unchanged.

Each ordinary Move/Core has its own reaction window; existing one-reactor-per-action and one-reaction-per-model limits remain. Both-cost actions still spend both slots. Run and Gun retains a distinct effect: fire partway through movement and use one combined reaction window. A revived or assisted fighter cannot reactivate after its activation has ended.

Implementation choices supporting the ruling: spend/forfeit unused slots within the activation, track Activated, and convert the previous two-slot Pass calculation into the eligible-fighter count difference. This preserves the old Pass count when every fighter had two available slots; it is not a new user-approved balance result. No unspent slot is banked across activations.

## Coordinated carrying

The former two-carrier rule spent another fighter's Move outside its activation. Ross was asked whether to simplify to one carrier at half speed or retain an explicit coordinated exception. Record his response here before treating a replacement as confirmed.

## Verification scope

The reference notes, section index, outline, progress tracker, source status, research adaptation notes, project roadmap and quick-reference PDF are updated alongside the master. Historical drafts and prior simulation contracts remain historical. Text/link/profile checks do not establish playtested balance.
