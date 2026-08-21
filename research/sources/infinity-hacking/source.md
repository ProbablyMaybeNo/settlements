# Infinity — Hacking / Electronic Warfare capture

Second capture for Infinity (see `research/sources/` — the first Infinity pass, cited only via
`docs/POINTS-RESEARCH.md`, covered SWC costing only). This capture is scoped to the
**Quantronic Combat (Hacking)** module and adjacent Electronic Warfare equipment/skills, pulled
from **infinitythewiki.com**, Corvus Belli's own official rules reference. Current edition tag on
the wiki at capture time: **N5.2 + N5 FAQ v0.0.0 (October 2025)**. Where the wiki's own text
notes an N5.2-specific change, that is preserved below. Edition-drift material (N3 vs N5) is
pulled from a linked, dated Corvus Belli official forum thread and a third-party tactics article,
both cited inline.

Retrieved 2026-08-20. All text below is copied verbatim from the cited page (markdown extraction
via Firecrawl `onlyMainContent`); navigation link clutter (the repeated A-Z skill/equipment index
bars every wiki page carries) has been trimmed for readability, no rules text has been altered.

---

## Quantronic Combat (Hacking) — main page

Source: https://infinitythewiki.com/Quantronic_Combat_(Hacking)

> In Infinity, infowar and cyberwarfare tasks, defined as Hacking, are shouldered by the Hackers,
> specialized Troopers who can use the different Hacking Programs which define quantronic combat.

> **Update PDF 5.2, October 2025.** According to their nature, Hacking Programs can either be
> aggressive to affect enemy Troopers, defensive to protect Allied Troopers, supportive to boost
> Allied Troopers or affect scenery items and objectives in scenario missions.
>
> *(Original pre-5.2 text, shown by the wiki as superseded: "Hacking Programs allow the Hacker to
> act in an aggressive or defensive manner, support other Troopers, interact with scenery, etc.")*

### Upgrade Programs (UPGRADE)
> Custom-made software tailored to the style and preference of specific infowar operatives. If
> available, they will be listed in the Unit Profile, in round brackets next to the name of the
> Hacker or the Device.

### Supportware Programs
> These are programs of extended duration which are mainly designed to support allied Troopers on
> the battlefield by granting them bonuses to improve their combat capabilities. Likewise, they
> may also be designed to hinder enemy Troopers, applying negative MODs to them.
>
> **SUPPORTWARE (IMPORTANT box):**
> - A Trooper can benefit from the effects of only one Program with the Supportware Label at a time.
> - Each Hacker can only sustain one active Supportware Program at a time.
> - A Hacker can cancel an active Supportware Program by declaring another Program and expending
>   the corresponding Order or ARO.
> - A Supportware Program is automatically cancelled if the target of the Supportware is targeted
>   by a new Supportware Program, or if the Hacker running the Program enters Isolated State or
>   any Null States.

### Hacking Devices and Hacking Programs: Characteristics
> - They act in the user's Hacking Area.
> - They do not require LoF to act, unless the Hacking Program's own description states otherwise.
> - Only Troopers in Model form may be targeted by Hacking Programs.
> - They benefit, if applicable, from the target's Targeted State.

### Worked example (Step 1–3)
> **Step 1.** The Active Trooper declares a Move from point A to point B. The Reactive Trooper
> declares a Carbonite Hacking Program ARO. The Active Trooper declares Reset for their second
> Skill of the Order. They do not declare a BS Attack against the Hacker because it is clear that
> they lack LoF to the Hacker along their entire movement path.
>
> **Step 2.** The Face to Face Rolls are performed. Active Trooper, Reset (WIP Roll, no MODs):
> 1d20 SV=13. Reactive Trooper, Carbonite (WIP Roll, no MODs): 1d20 SV=13. They both succeed, but
> the Reactive Trooper's 7 cancels the Active Trooper's 3.
>
> **Step 3.** Therefore, as the Hacker wins the Face to Face Roll, the Active Trooper must perform
> 2 Saving Rolls due to DA Ammunition, against PS 7. Saving Roll = 13 (PS 7 + BTS 6). Due to the
> 14, the Active Trooper enters Immobilized-B State, placing an Immobilized-B Token next to them.

---

## Hacker

Source: https://infinitythewiki.com/Hacker

> The term Hacker designates a set of Troopers who have received specific training in Infowar.
> This training allows them to make use of Hacking Devices, and the programs specifically designed
> for them.
>
> **HACKER — AUTOMATIC SKILL (Obligatory)**
> - Hackers may be equipped with a Hacking Device that will grant them access to certain Hacking
>   Programs, depending on the type of Device they are using, or to make direct use of certain
>   Programs without requiring a device.
> - Hackers may have Upgrade Programs assigned to them.
> - This Special Skill remains active even when its owner is in a Null State.

---

## Hacking Device (and family)

Source: https://infinitythewiki.com/Hacking_Device

> Hacking Devices are the tools used during cybercombat. Multipurpose and versatile, these devices
> can be useful as support elements or to perform powerful cyberattacks, depending on the Device.

**Device → Program grant table (verbatim):**

| Device | Program 1 | Program 2 | Program 3 | Program 4 | Program 5 | Program 6 |
|---|---|---|---|---|---|---|
| Hacking Device | Carbonite | Spotlight | Total Control | Oblivion | -- | -- |
| Hacking Device Plus | Carbonite | Spotlight | Total Control | Oblivion | White Noise | Cybermask |
| Killer Hacking Device | Trinity | Cybermask | -- | -- | -- | -- |
| EVO Hacking Device | Assisted Fire | Enhanced Reaction | Fairy Dust | Controlled Jump | -- | -- |

> **REMEMBER:** Both Hackers and Hacking Devices may benefit from Upgrades. Check all the rules on
> Hacking.

---

## Hacking Programs Chart

Source: https://infinitythewiki.com/Hacking_Programs_Chart

| Name | Attack MOD | Opp. MOD | PS | Burst | Target | Skill Type | Special |
|---|---|---|---|---|---|---|---|
| Assisted Fire | -- | -- | -- | -- | REM | Long Skill | Target Model gains Marksmanship. |
| Carbonite | 0 | 0 | 7 | 2 | TAG, HI, REM, VH, Hacker | Short Skill / ARO | DA Ammo, Non-Lethal, State: Immobilized-B. |
| Controlled Jump | -- | -- | -- | -- | -- | Short Skill / ARO | +3/-3 MOD to the PH of every Trooper that performs Combat Jump. |
| Cybermask | -- | -- | -- | -- | -- | Long Skill | Replace user with IMP-2 Marker. |
| Enhanced Reaction | -- | -- | -- | -- | REM | Long Skill | Target gains B2 in ARO. |
| Fairy Dust | -- | -- | -- | -- | TAG, REM, HI, VH | Long Skill | The targets gain Firewall MODs. |
| Oblivion | 0 | 0 | 4 | 2 | TAG, HI, REM, VH, Hacker | Short Skill / ARO | AP Ammo, Non-Lethal, State: Isolated. |
| Spotlight | 0 | 0 | 5 | 2 | -- | Short Skill / ARO | AP Ammo, Non-Lethal, State: Targeted. |
| Total Control | 0 | 0 | 4 | 1 | TAG | Short Skill / ARO | DA Ammo, Non-Lethal, State: POS/Normal. |
| Trinity | +3 | 0 | 6 | 3 | Hacker | Short Skill / ARO | Target receives 1 Wound for each failed Saving Roll. |
| White Noise | -- | -- | -- | 1 | -- | Short Skill | NFB, Reflective, Circular Template. |
| Zero Pain | 0 | -3 | -- | 2 | -- | Short Skill / ARO | Nullifies Comms Attack. B2 in ARO, Non-Lethal. |

> **Key.** Attack MOD applies to the user's WIP. Opponent's MOD applies to the enemy's Attribute in
> the Face to Face Roll. **PS (Possibility of Survival)** — unless stated otherwise, the Saving
> Roll to resist a Hacking Program uses **BTS**. **Burst (B)** is the number of dice rolled;
> divisible across multiple targets. **Target** = the Troop Type(s) that can be targeted.
>
> **REMEMBER:** Unless otherwise stated, the range of every Program is always the Hacker's Hacking
> Area.

---

## Hacking Area

Source: https://infinitythewiki.com/Hacking_Area

> This term refers to the Area of Effect of Hacking Programs. In Infinity a Hacker's Hacking Area
> matches their Zone of Control, and the Zone of Control of Repeaters and Deployable Repeaters of
> either the Player or their Allies.
>
> In addition, **if a Hacker is within the Zone of Control of an Enemy Repeater or Deployable
> Repeater, their Hacking Area includes all Enemy Troopers on the game table.** However, if the
> Enemy Trooper is not a Hacker, any ARO or Hacking Program using the Enemy Repeater will fail its
> Requirements, and instead an Idle will be performed.

### Hacking Area in ARO
> Enemies entering or acting inside the Hacking Area of a Hacker while remaining outside that
> Hacker's LoF and ZoC can be reacted to. In the ARO Check steps of the Order Expenditure Sequence,
> players can check if the Active Trooper is inside any Reactive Troopers' Hacking Areas.
> Measurements must always be made from the Active Trooper, checking a maximum of 8 inches from
> any point along their path, and from the Active Trooper's Repeaters. If the measurements show
> that the Active Trooper is within the Hacking Area of the Reactive Trooper, they can declare an
> ARO.

### Worked example, with Firewall MODs shown
> Therefore, since the Active Hacker is within the Hacking Area of the Enemy Hacker, this one
> declares his ARO: Oblivion. The Enemy Heavy Infantry (HI) cannot declare an ARO as the Active
> Hacker is outside their LoF and ZoC. The second Skill of the Active Hacker is Carbonite, dividing
> his B2 between the Enemy Heavy Infantry and the enemy Hacker. As the Enemy Heavy Infantry has
> been targeted by a Hacking Program (a Comms Attack), they can declare an ARO, choosing to declare
> a Reset.
>
> The following Face to Face Rolls occur: Reset by the Enemy Heavy Infantry vs Carbonite from the
> Hacker — No MODs. Oblivion from the Enemy Hacker vs Carbonite from the Hacker — Enemy Hacker
> MODs: -3 Firewall MOD for using an Enemy Repeater; Hacker MODs: none. If a Saving Roll is
> required, the PS of Oblivion will suffer a +3 MOD from the Firewall.

---

## Repeater

Source: https://infinitythewiki.com/Repeater

> This is a range amplifier for Hackers.
>
> **REPEATER — AUTOMATIC EQUIPMENT (Comms Equipment, Obligatory, Zone of Control)**
> - Repeaters extend the Hacking Area of all Hackers in the same Army List.
> - **Hackers within the Zone of Control of an enemy Repeater may use it to apply Hacking Programs
>   against any enemy Hacker, but applying Firewall MODs (-3).**
> - **There can be no reaction against a Repeater that is being used by an enemy Hacker, only
>   against the Hacker, if possible.**
>
> This piece of Equipment is automatically active and cannot be deactivated by its owner, unless
> its carrier is in Isolated State or any Null States.

---

## Deployable Repeater

Source: https://infinitythewiki.com/Deployable_Repeater

> This is a hacking range amplifier designed for deployment onto the battlefield.
>
> **DEPLOYABLE REPEATER — EQUIPMENT (Comms Equipment, Deployable, Disposable (3), Indiscriminate,
> Zone of Control)**
> - When the player declares the Place Deployable Common Skill, the Trooper places a Deployable
>   Repeater Token (REPEATER) on the game table.
> - The Deployable Repeater is a piece of Equipment that contains a Repeater.
>
> Stats: ARM 0, BTS 0, STR 1, S 1. Traits: Disposable (3), Deployable.

---

## Firewall

Source: https://infinitythewiki.com/Firewall

> Some Troopers or Hacking Devices have pieces of Equipment which provide extra protection against
> Comms Attacks. These defenses are codified in the Firewall rule, which applies a series of MODs
> to hinder the Attack and enhance the target's protection.
>
> **FIREWALL — EQUIPMENT (Obligatory)**
> - Any enemy that declares a Comms Attack against a Trooper benefitting from a Firewall must apply
>   a negative MOD to his WIP Attribute, as indicated between brackets: Firewall (-3), Firewall
>   (-6)...
> - A Trooper benefiting from a Firewall also applies a MOD of +3 to their Saving Rolls (SR)
>   against Comms Attacks.
> - Troopers can only benefit from one Firewall at a time. If a Trooper can benefit from more than
>   one Firewall, their player will decide which one to apply.
>
> **Sibylla's Advice:** *"The Firewall in a Comms Attack is the equivalent of Cover in a BS Attack,
> it hinders the Attack and aids the target's Saving Roll. Although the MOD to the Attack varies
> (-3, -6…), the MOD to the Saving Roll is always fixed (+3), unless a specific rule indicates
> otherwise."*

---

## Total Control / Possessed State

Sources: https://infinitythewiki.com/Total_Control (via Hacking Programs Chart, above) and
https://infinitythewiki.com/Possessed_State

> **POSSESSED STATE (Null)**
>
> **Activation:** The Trooper suffers a successful Attack or Effect using an Ammunition, Hacking
> Program or game condition/Scenario Special Rule capable of causing this state.
>
> **Effects:**
> - **Restriction:** Troopers in this state cannot be activated or receive Orders from their
>   player's Order Pool. While Possessed, Troopers are considered enemies by the rest of their
>   owner's Troopers and allies by the Troopers of the player that caused the state.
> - Troopers in this state do **not** contribute Orders during the Tactical Phases of either
>   player.
> - Troopers in this state may be activated and receive Orders from the Order Pool of the **Combat
>   Group of the Trooper who caused them to enter the Possessed state.** A Possessed Trooper does
>   not count towards the maximum number of members that Combat Group may contain.
> - **Possessed Troopers must use the Possessed Trooper profile instead of their own:**
>
> | Possessed Trooper | MOV | CC | BS | PH | WIP | ARM | BTS | STR | S |
> |---|---|---|---|---|---|---|---|---|---|
> | | 4-4 | 13 | 12 | * | 11 | * | * | * | * |
>
> *(\* = use the Trooper's original Attribute values.)*
>
> - This state does not interfere with Automatic Special Skills or Automatic Equipment.
> - **A Possessed Trooper does not count towards either Player's Victory Points.**
> - **Restriction:** A Trooper in Possessed State cannot be part of a Fireteam.
>
> **Cancellation:**
> - In the owning player's Tactical Phase, during the Executive Use of Command Tokens step, the
>   player can automatically cancel this state by spending **1 Command Token**.
> - The Possessed State is automatically canceled if the owning player successfully affects the
>   Possessed Trooper with the Total Control Hacking Program (i.e., hack it back).
>
> **Total Control (from Hacking Programs Chart cross-reference):** *"Any failed Saving Roll causes
> the target to enter Possessed State, placing a Possessed State Token (POS) by them. If this
> Program is used against a TAG in Possessed State, any failed Saving Roll cancels the target's
> Possessed State, causing them to enter Normal State, and the Possessed State Token (POS) is
> removed."* Total Control's Target column reads **TAG only**, Burst 1, PS 4, DA Ammo.

---

## Isolated State (Oblivion's payload)

Source: https://infinitythewiki.com/Isolated_State

> **Effects (selected):**
> - Cannot receive Orders from their Order Pool.
> - If still Isolated at the start of their next Active Turn, they are Irregular and do not add
>   their Order to the Order Pool; that Irregular Order cannot become Regular.
> - **All Comms Attack / Comms Equipment Skills and Equipment (Hacking Device, Repeater...) are
>   disabled, and all Hacking Programs are disabled.** Other Automatic Special Skills/Equipment
>   keep working.
> - If the Isolated Trooper is the army's Lieutenant, Loss of Lieutenant triggers next Active Turn
>   unless cancelled first.
> - **Troopers in this state must apply a -9 WIP MOD to their Reset rolls.**
>
> **Cancellation:** an Engineer (or equivalent) may cancel it with a Short Skill in Silhouette
> contact plus a Normal WIP roll; or the affected Trooper may self-cancel via a successful Reset
> roll (applying the -9 WIP MOD).

---

## Non-Hackable

Source: https://infinitythewiki.com/Non-Hackable

> Troopers that have technological systems that are so rudimentary that they are not susceptible
> to Hacking attempts.
>
> **NON-HACKABLE — AUTOMATIC SKILL (Obligatory)**
> - The user of this Special Skill cannot be the target of Hacking Attacks whose Requirements
>   require the target have a specific Unit Type (HI, REM, TAG, etc.).
> - This Special Skill remains active even when its owner is in a Null State.

---

## ECM

Source: https://infinitythewiki.com/ECM

> Electronic Countermeasures cover all systems carried by Troopers, Vehicles and TAGs with the goal
> of disrupting and deactivating enemy guided projectiles, Comms Attacks etc. depending on the type
> of ECM they are equipped with.
>
> **ECM — AUTOMATIC EQUIPMENT.** Requirements: to use this, its owner must be the target of the
> Attack type listed in round brackets. Effects: ECM imposes a series of negative MODs on the Enemy
> when they attempt to Attack the Trooper that owns it. Both the affected Attack type and the MOD
> it imposes are listed in the Unit Profile of the Trooper.

---

## Mimetism

Source: https://infinitythewiki.com/Mimetism

> This Special Skill represents the soldier's ability to conceal their position and move
> stealthily, making them difficult to target in combat.
>
> **MIMETISM — AUTOMATIC SKILL (NFB, Obligatory)**
> - Any enemy declaring a BS Attack that requires LoF, or Discover, against the user must apply a
>   negative MOD to their Attribute, shown in round brackets: Mimetism (-3), Mimetism (-6)...
> - The Mimetism MOD does not apply to CC Attacks.

## Camouflage

Source: https://infinitythewiki.com/Camouflage

> This Special Skill represents the soldier's ability to conceal their position and move
> stealthily.
>
> **CAMOUFLAGE — AUTOMATIC SKILL (Optional).** During the Deployment Phase, it allows the user to
> deploy in Camouflaged State. In game, it allows the user to enter Camouflaged State.

## Sensor

Source: https://infinitythewiki.com/Sensor

> Hyper-developed senses and sophisticated tracking technology are the two sides of the Sensor
> coin... the ability to uncover hidden threats in one's immediate surroundings.
>
> **SENSOR — SHORT SKILL (Attack, Optional, Zone of Control)**
> - By declaring Sensor, the user may make a Normal WIP +6 Roll (without applying Range or
>   Mimetism MODs) to simultaneously Discover all enemy Troopers, Weapons or pieces of Equipment in
>   the Hidden Deployment or Camouflaged States, who are inside the user's Zone of Control.
> - The user does not need LoF to a target, or to designate a target at all.
> - Enemies with the Camouflage Special Skill cannot regain Camouflaged State inside the Zone of
>   Control of the user.
> - Sensor also grants its user, automatically and without making Rolls or spending Orders, a +6
>   MOD to WIP when declaring Discover against Camouflage Markers.

## Multispectral Visor (MSV) — Levels 1–3

Source: https://infinitythewiki.com/Multispectral_Visor

> This piece of Equipment was designed to combat the effects of different military concealment and
> camouflage technologies.
>
> **MSV L1:** Reduces Mimetism (-3) and Low Visibility Zone MODs to 0; reduces Mimetism (-6) and
> Poor Visibility Zone MODs to -3; allows LoF through Zero Visibility Zones at a flat -6 MOD to any
> Skill requiring LoF; ignores Face to Face Rolls against Smoke Ammunition attacks.
>
> **MSV L2:** Reduces Mimetism and all Visibility Zone MODs to 0 outright; draws LoF through
> Visibility Zones with no MOD at all; ignores Smoke Ammunition Face to Face Rolls.
>
> **MSV L3:** As L2, **plus**: Discover rolls against a Camouflaged target auto-succeed; ignores
> Surprise Attack MODs (with LoF for ranged, unconditionally for CC); **may BS Attack a Camouflage
> Marker directly in LoF without a prior Discover roll**, applying only the Marker's own printed
> Mimetism MOD.
>
> **IMPORTANT (cross-vulnerability):** Troopers with Multispectral Visor (or the Marksmanship
> Skill) are affected by White Noise Zones, the Reflective Trait, and the Albedo piece of
> Equipment — i.e., detection tech itself has printed counters.

---

## Edition drift: N3's five-family taxonomy vs N5's collapse to two labelled categories

Source: Corvus Belli official forum, "Hacking in HSN3 – Summary and Rules Clarifications"
(http://forum.corvusbelli.com/threads/hacking-in-hsn3-summary-and-rules-clarifications.3372/,
started by user inane.imp, March 2018; unofficial community summary, not itself an official CB
rules document, but hosted on CB's own forum and widely cited — tagged CONSENSUS/community
reconstruction below, not FACT).

> "Troops equipped with a Hacking Device can use Hacking to attack enemies or support and protect
> friendly troops. There are different kinds of Hacking devices: *Assault Hacking Device (AHD),
> Hacking Device (HD), Hacking Device Plus (HD+), Killer Hacking Device (KHD), Defensive Hacking
> Device (DHD), White Hacking Device (WHD)* and *EVO Hacking Device (EVO).*"
>
> "Hacking programmes are broken down into five types **SWORD, SHIELD, CLAW, GADGET and UPGRADE**.
> ... The most common ones are those that attack enemy Heavy Infantry, TAGs, REMs or Hackers (CLAW
> programmes). You can also attack enemy's Comms Equipment... Hacking Programmes only cause
> physical damage to your models (read: Wound/Structure) if specifically stated... Hacking
> Programmes can only cause physical damage to other Hackers (**SWORD** programmes)... the
> Supportware Programmes for your REMs [are] **GADGET**."
>
> "**ARMY SHIELDS** [SHIELD-1]: EXORCISM, HACK-TRANSPORT AIRCRAFT and U-TURN... general purpose
> defensive programmes... EXORCISM allows you to cancel your TAG's Possessed state, HACK-TRANSPORT
> AIRCRAFT allows your Hacker to FTF an enemy's PH roll to drop with AD:3+ and U-TURN applies a -3
> MOD to enemy Guided attacks."
>
> "**Defense Protocols** [SHIELD-2/3]: BREAKWATER, ZERO PAIN and COUNTERSTRIKE. These are much
> maligned because you need to be the target of a Hacking Attack *before* you can declare them."

By N5.2 (current), the wiki's Quantronic Combat page names only **two** labelled program
categories — **Upgrade Programs** and **Supportware Programs** — with the remaining programs
(Carbonite, Oblivion, Spotlight, Total Control, Trinity, White Noise, Zero Pain) unlabelled by
family, just listed against the four devices in the table above. The N3-era **CLAW/SWORD/SHIELD/
GADGET** taxonomy, the extra device types (**AHD/DHD/WHD**), and army-wide passive "Army Shield"
programs (EXORCISM, HACK-TRANSPORT AIRCRAFT, U-TURN) do not appear anywhere in the current wiki's
Hacking Device or Hacking Programs Chart pages. **[FACT — absence confirmed by direct page read,
not inference]**: none of AHD/DHD/WHD, EXORCISM, U-TURN, HACK-TRANSPORT AIRCRAFT, BREAKWATER, or
COUNTERSTRIKE appear on the current (N5.2) Hacking Device, Hacker, or Hacking Programs Chart pages.

---

## Third-party tactics commentary (community meta, tagged CONSENSUS)

Source: Thanqol Decadion, "Infinity Tactics: Cybersecurity," Tabletop Battles / Goonhammer,
15 Dec 2020 (https://www.tabletopbattles.com/infinity-tactics-cybersecurity). Written for N4;
program names/values it cites (Carbonite Damage 13, Oblivion Damage 16, Total Control Damage 16,
Trinity Damage 14) use **N4-era damage numbers**, not the PS values in the current N5.2 chart
above — flagged as a second data point on edition drift, not reconciled against N5.2.

> "Hacking totally changed in N4 Infinity and has gone from a weird gimmick mostly used to buff
> remotes to a serious threat that every army needs to have a plan for, especially heavy infantry
> armies."
>
> "Repeaters are the terrain of the cyber battlefield, and engaging through one of your opponent's
> repeaters is like engaging when they have cover and you do not."
>
> "hacking is primarily **reactive** and always **non lethal** (unless you've got a hacker of your
> own)... because hacking programs are low burst and are opposed with free reset activations —
> that if successful clear **all** current hacking states — people rarely spend orders on them."
>
> "**Category One:** WIP 13 BTS 0, no special gear... **Category Two:** WIP 13-15, BTS 3-6, various
> hacking gear... 25-35 point range... **Category Three:** WIP 15+, BTS 6-9, multiple wounds,
> powerful hacking assets... 50+ points and utterly dominate lesser hackers."
>
> Counterplay recommended: focus-fire the enemy's hackers one at a time so the rest only get
> unopposed AROs; bring an Engineer to repair Isolated/Immobilized troops; use a cheap disposable
> piece to physically destroy the enemy's Repeater network; **body-block a TAG with a friendly
> model in base-to-base contact so a successful Possession is immediately Engaged in melee instead
> of free to shoot your own army**; consider assassinating the "lynchpin hacker" directly.
>
> "hacked troops aren't dead... One successful reset clears all states and returns the model to
> full capacity... hacked units still count as points in zones... they can be repaired by
> engineers."
>
> (Aside on terrain, tagged CONSENSUS, one author's opinion): "Hacking benefits from tight, closed
> spaces with lots of hook turns and vertical space. If you're consistently finding hackers
> impossible to engage that might be a sign that the tables you're playing on are too dense and you
> should open the map up some more."
