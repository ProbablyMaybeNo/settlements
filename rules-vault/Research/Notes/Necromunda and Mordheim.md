---
type: research-note
title: Necromunda and Mordheim
game: Necromunda (1995 / N18) and Mordheim
publisher: Games Workshop
depth: campaign-economy lineage, published rules + community simulation
tags: [settlements/research]
---
# 🎲 Necromunda & Mordheim

> [!abstract] In one breath
> The **founding lineage** of the warband-campaign genre Settlements sits in. Between them they settle two of our open questions outright — **stashed gear doesn't count toward rating**, and **publish deltas, never the derivation** — and they document the snowball source nobody expects: **how often you play beats how well you play.**

| | |
|---|---|
| **Publisher** | Games Workshop (Necromunda 1995 & N18; Mordheim 1999) |
| **Currencies** | **Credits** to buy; **Gang Rating** to match |
| **Depth of read** | Published rules + a 100,000-run community simulation |
| **Long-form** | `docs/POINTS-RESEARCH.md` §10, §7.9 |

---
## Rating is a snapshot

**Type:** Campaign · **Take:** ⭐ steal — settles an open fork

**Stashed gear does not count toward gang rating.** 1995 Necromunda states it outright. **[FACT]**

> **Ownership is wealth; rating is fielded power.**

**Why it works.** It is what makes **underdog banding** work at all. If rating were cumulative spend, a gang that lost fighters would keep the rating of the gear those fighters were carrying and never qualify for the handicap it needs. A snapshot of *what's on the table* is the only measure that tracks actual strength.

**For Settlements.** This settles the open **Armoury fork** and matches the already-locked principle — *Credits buy what you own; the Credits you field are your Crew Rating.* An armoury of stashed kit is wealth and should never inflate the number that matches you against an opponent. See [[List Building]] and [[Economy]].

---
## Underdog banding

**Type:** Campaign · **Take:** ⭐ steal

Underdog bonuses **scale by the *difference* in rating**, not by win/loss record. **[FACT]**

**Why it works.** It self-adjusts with no tuning. A gap of 50 gives a small bump; a gap of 500 gives a real one; equal ratings give nothing at all — and it stops applying the moment the gap closes, without anyone having to decide when the catch-up should end.

**For Settlements.** [[Campaign]]. Worth reading against [[Trench Crusade#The rubber band you choose]], which solves the same problem the opposite way — opt-in, at a stated price, chosen by the losing player. **Banding is automatic and invisible; the Trench Crusade rubber band is deliberate and costly. They compose fine, but pick a primary.**

---
## Play frequency beats skill

**Type:** Campaign · **Take:** ⚠️ the snowball source nobody plans for

A **100,000-run community simulation** found median campaign income of **750 credits at one game per week versus 1,170 at two.** **[FACT]**

**Why it matters.** **Schedule, not skill, is the largest snowball source in an open campaign.** The player who can play twice a week wins the campaign before anyone's tactics are tested, and no amount of balance work on the rules touches it.

**For Settlements — this is our exposed structure.** We persist **outside** campaigns by design, which is precisely the shape that gets hit. The cheapest shipped mitigation found anywhere is a **diminishing-returns income "wash table"** — income per game falls as games-played rises — which caps the schedule advantage without policing anyone's calendar. See [[Economy]] and [[Campaign]]. Compare the alternative structural answer in [[Trench Crusade#The published threshold ladder]]: a fixed ceiling schedule makes frequency irrelevant to power, only to progress rate.

---
## Publish deltas, never the derivation

**Type:** Costing · **Take:** ⭐ steal

Base fighter and weapon costs have **no published derivation** and never have. **But the advancement table is a genuine published marginal-cost table** — GW prints what one point of a stat costs in credits — and N18 publishes an **escalating XP cost: each advance costs base XP +2 per prior advance.** **[FACT for the structure; the specific credit figures need a rulebook check — see the to-read list on [[Wargaming Research]].]**

> **Necromunda solves the derivation problem by only ever publishing *deltas*, never the absolutes.** Base costs stay hand-tuned and opaque; growth is fully transparent and rules-legible.

**Why it works.** You get a designer-controlled starting point **and** a player-verifiable progression system, and **you never have to defend a global formula.** Nobody can arbitrage a derivation you didn't publish — but everyone can check that their own fighter's advance was priced correctly.

**For Settlements.** Direct guidance for `docs/GLOBAL-POINTS-SYSTEM.md`: the global points system is **a designer-side tool and players should never see it** (already locked). The **deltas** — what a Level costs, what an Advance costs — are exactly what *should* be printed. And the **escalating XP cost** (+2 per prior advance) is a second, free anti-snowball valve on the [[Progression]] track that costs one sentence.

---
## Lasting injuries

**Type:** Combat · **Take:** ⭐ steal — the direct ancestor

A model taken out of action rolls on an **injury table**: concussion, broken arm, broken leg, severed limb, gouged eye, full recovery, death — **each with a lasting or permanent effect.** This is the mechanic that made the genre emotionally sticky, and Mordheim (and later [[Trench Crusade]], by the same designer) is where it comes from.

**For Settlements.** Already the model for our own post-battle fate rolls ([[Ideas Inbox]], [[Progression]]) — broken arm = −1 STR next battle, severed leg = permanent −2 MOV, gouged eye = permanent −1 to hit. Two design notes worth carrying over:

- **A permanent injury should have a second life, not just be a debit.** A fighter who loses a leg becoming a settlement **worker** turns a punishment into a story and feeds [[Structures]]. That's our idea, and it's better than the source.
- **Cap the death rate or the campaign hollows out.** Compare [[Trench Crusade#Cap the veterans, don't tax them]]: ELITE models get exactly two Battle Scar slots and die on the third — a *finite veteran lifespan*, published up front.

> ⚠️ **Some failures cannot be priced away.** **[CONSENSUS, strongly corroborated]** The lineage's known flaw is the death spiral: a gang that loses fighters loses income, loses more fighters, and stops being playable. Injury tables are the cause. **Any lasting-injury system needs a floor** — that's what underdog banding and rubber-banding are actually for.

---
## Other published figures

**[FACT]** Starting budgets: Necromunda 1995 gangs start at **1,000 credits**; Mordheim warbands at **500 gold crowns**. Wealth is gated twice in some editions (buy-in *and* rating) and once in others — a deliberate choice, not an accident.

---
## Source

- Primary: Necromunda 1995 & N18, Mordheim published rules; community campaign simulation (100k runs)
- Long-form: `docs/POINTS-RESEARCH.md` §10 (full lineage), §7.9 (the advancement-delta point)
- Related: [[Wargaming Research]] · [[Trench Crusade]] (same designer lineage) · [[Frostgrave and Stargrave]] · [[Progression]] · [[Campaign]] · [[Damage]]
