---
type: rule
rule_id: core-000
category: core
status: draft
version: v0.1
parent_phase: "[[Rules Engine]]"
tags:
  - settlements/rule
  - settlements/cat/core
---
# core-000 · Core Test
> **core** · status **draft** · v0.1
**Parent phase:** [[Rules Engine]]

## Text
The single resolution mechanic every system reuses — attacks, skill tests, terrain and objective interactions.

```
1d10 + Stat + Modifiers   →   7+ = Success
```

- **Natural 1** = automatic failure (regardless of modifiers).
- **Natural 10** = automatic success (regardless of modifiers).
- **Opposed Test:** both sides roll `1d10 + Stat + Modifiers`; highest total wins; **ties go to the defender.**

*Any rule that resolves an uncertain outcome should cite this as **core-000**, not restate it.*

## Probability
Because nat 1 always fails and nat 10 always succeeds, every result is bounded **10%–90%**. Each point of net modifier = **±10%**. "Net modifier" = your Stat + all positive mods − all negative mods.

| Net modifier | Roll needed | Hit chance |
|:---:|:---:|:---:|
| +5 or more | 2+ | **90%** |
| +4 | 3+ | 80% |
| +3 | 4+ | 70% |
| +2 | 5+ | 60% |
| +1 | 6+ | 50% |
| 0 | 7+ | 40% |
| −1 | 8+ | 30% |
| −2 | 9+ | 20% |
| −3 | 10 | 10% |
| −4 or less | 10 | **10%** |

### Worked example — a shooting matrix
Standard fighter, **Dexterity +1**, shooting. Cover as −1 (light) / −2 (heavy) / −3 (hidden). **Armour is not on this table — it applies to the Injury roll, not the hit** (see [[Damage]]).

| Target | Net | Hit chance |
|---|:---:|:---:|
| In the open | +1 | 50% |
| Light cover | 0 | 40% |
| Heavy cover | −1 | 30% |
| Hidden / obscured | −2 | 20% |

> [!note] Design read
> Deliberately swingy toward defence — a hidden target drops a decent shooter to a 1-in-5 shot, and after a hit the target's **armour** bites again on the injury roll. That's **Terrain is the core**: positioning beats stats. Nat-10 means no shot is ever truly impossible; nat-1 caps the best shot at 90%.

---
*Graduated from [[Rules Engine]]. See [[Rules System MOC]].*
