---
type: reference
title: Quick Reference — Writing Rules
tags: [settlements/reference]
cssclasses: [quickref]
---
# ⌨️ Quick Reference

> [!tip] Dock me on the right
> Right-click this tab → **Move to right sidebar** (or drag the tab into the right panel). Keep it open while you write. Full detail: [[Obsidian Guide — Building Settlements]].

---
## ✅ Finish a roadmap step
1. `Ctrl+O` → **Open Decisions** — pick what's next.
2. `Ctrl+O` → the phase note (e.g. **Rules Engine**).
3. Set `status:` → **Designing**.
4. Read `## Focus` = the decisions to make.
5. Write under `## Working rules / decisions` (plain English first).
6. Numbers? drop a dice block, click to roll.
7. Unsure? add `> [!question] …`.
8. Tick `- [ ]` → `- [x]` as you decide.
9. Link with `[[ ]]`.
10. Done drafting → `status:` **Drafted**.
11. Save: `Ctrl+P` → **Git: Commit all changes**.

## ➕ Add a brand-new rule
1. `Ctrl+P` → **Templater: Create new note from template** → **Rule Phase**.
2. Name it → fill `stage`, `depends_on`.
3. Write it (steps 4–9 above).
4. Link it from its parent + **Rules System MOC**.
5. Optional: drag onto **_Rules Map** canvas, draw an arrow.
6. Commit.

> [!warning] The 3 habits
> ① always set `status`  ② tick the boxes  ③ commit at the end.
> Do these and the dashboards + map stay true.

---
## Status ladder
`Not Started` → `Designing` → `Drafted` → `Testing` → `Done`

---
## 🧭 Keys — get around
| Key | Does |
|---|---|
| `Ctrl+P` | Command palette (the big one) |
| `Ctrl+O` | Jump to / create a note |
| `Ctrl+E` | Edit ⇄ Reading view |
| `Ctrl+Click` | Open link in new tab |
| `Ctrl+Hover` | Peek a link |
| `Ctrl+Shift+F` | Search whole vault |
| `Ctrl+\` | Split pane |
| `Ctrl+,` | Settings |

## ⌨️ Custom hotkeys (this vault)
| Key | Does |
|---|---|
| `Alt+1` | H1 — **note title** (e.g. `# 03 · Rules Engine`) |
| `Alt+2` | H2 — **section title** (e.g. `## Working rules / decisions`) |
| `Alt+3` | H3 — **rule title** (e.g. `### Priority`) ← your workhorse |
| `Alt+4` | H4 — **sub-rule** (e.g. `#### Opposed Tests`) |
| _(same heading key again)_ | removes the heading |
| `Ctrl+B` `Ctrl+I` | Bold / italic |
| `Alt+C` | Insert callout |
| `Alt+B` | Insert table |
| `Alt+T` | Insert tag |
| `Alt+I` | Capture idea → Ideas Inbox |
| `Alt+K` | Add Kanban lane |
| `Ctrl+Q` | Run QuickAdd |

## ✍️ Keys — write (syntax, type it)
| Type | Gives |
|---|---|
| `[[` | link to a note |
| `[[note\|label]]` | link, custom text |
| `[[note#head]]` | link to a heading |
| `![[note]]` | embed a note |
| `- [ ]` | a task/checkbox |
| `> [!question]` | callout box |
| `#tag` | a tag |
| `**x**` `*x*` | bold / italic |
| ` ```dice ` | dice roller block |

## ⚙️ Commands (`Ctrl+P`, then type…)
| Type | Does |
|---|---|
| `commit` | Git: save a restore point |
| `backup` | Git: commit everything now |
| `template` | Templater: insert template |
| `graph` | Open graph view |
| `reload` | Reload app (after theme edits) |
| `pdf` | Export note to PDF |
| `properties` | Add/edit a property |

---
## 🔁 Recall a rule in another note (embeds)
The S1 engine is the **single source** for the core rules — other notes *quote* it live so they never drift:

- `![[core-000 Core Test#Text]]` → drops the whole core-test rule inline (auto-updates when the source changes).
- `![[Rules Engine#House Conventions]]` → embeds just that one section.
- `[[Rules Engine#Priority|the priority roll]]` → a plain deep-link with custom display text.

Every S2 combat note already has an **"Inherits from the engine"** panel doing this. View it in **Reading mode** (`Ctrl+E`) to see the rules render. Edit the engine once → every note that embeds it updates.

## ✍️ House style (how we format rules)
| Element | Use for | Example |
|---|---|---|
| `# Note title` | one per note | `# 03 · Rules Engine` |
| `## Section` | the note's fixed sections | `## Working rules / decisions` |
| `### Rule name` | **one rule / subsystem — the linkable anchor** | `### Priority` |
| `#### Sub-rule` | parts within a rule | `#### Opposed Tests` |
| `**bold**` | a defined game **term** / a value that matters | **Natural 10**, **+1** |
| `*italic*` | asides, examples, notes-to-self (never a term) | *swingy toward defence* |
| `` `code` `` | dice + exact formulas | `1d10 + Stat`, `7+` |
| table | stat / modifier / probability data | the core-test odds table |
| `> [!question]` | an open decision (shows on your board) | — |
| `> [!example]` | a worked example | — |
| `^block-id` | tag one line so it's embeddable alone | `…unless charging. ^one-inch-rule` |

**Bold = keyword.** If a word is a defined term the rules reuse, bold it (it's usually a future link/ledger entry). Heading links are **case-insensitive**, so write headings however reads best.

## 📂 Where things are
| Need | Open |
|---|---|
| Front door | **Rules System MOC** |
| What's next | **Open Decisions** / **Master Roadmap** |
| Visual board | **_Rules Map** (canvas) |
| Status tables | **Rules System** (base) |
| Write rules | the **phase notes** |

---
*Keep this docked. See also [[Rules System MOC]] · [[Rules System — Master Roadmap]].*
