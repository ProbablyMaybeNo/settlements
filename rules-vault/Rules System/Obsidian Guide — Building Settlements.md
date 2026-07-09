---
type: guide
title: Obsidian Guide — Building Settlements
tags: [settlements/guide]
---
# 📖 Obsidian Guide — Building the Settlements Rules System

> [!tip] How to read this
> You don't need to memorise it. Skim once, then keep it open in a side tab and refer back. The only two things you *must* learn today are in **[§3 Moving around fast](#3-·-moving-around-fast)** — everything else you can pick up as you go.
> Jump to: [[#1 · What Obsidian actually is]] · [[#2 · The interface, in plain terms]] · [[#3 · Moving around fast]] · [[#4 · The five building blocks]] · [[#5 · Markdown you'll actually use]] · [[#6 · Your Settlements vault — what's where]] · [[#7 · The rule lifecycle — the core loop]] · [[#8 · Your toolkit, tool by tool]] · [[#9 · From rules → rulebook]] · [[#10 · Your first 30-minute session]] · [[#11 · Habits & gotchas]] · [[#12 · Cheat sheet]]

---
## 1 · What Obsidian actually is

Three ideas and you understand the whole app:

1. **It's just a folder of text files.** Every note is a plain `.md` (Markdown) file sitting in `Documents\Obsidian Vault` on your disk. Obsidian is a nice window onto that folder. If Obsidian vanished tomorrow, your rules are still readable in Notepad. **You can never get locked in.** That whole folder is called a **vault**.
2. **Notes link to each other.** You type `[[Movement]]` and it becomes a clickable link to the Movement note. Follow links, and knowledge becomes a web instead of a filing cabinet. This is the entire point of Obsidian.
3. **Everything else is plugins.** Canvas, graphs, dashboards, dice — all optional features layered on top of the text. You've already installed the good ones.

> [!note] Why this matters for a rulebook
> A wargame rules system is a *web of interconnected rules* — Shooting references Cover references Terrain references Line-of-Sight. A filing cabinet hides those connections; Obsidian shows them. That's why we're building here.

---
## 2 · The interface, in plain terms

When you open Obsidian you see three regions:

- **Left sidebar** — your **File Explorer** (the folder tree) and **Search**. Click the file icon at top-left if it's hidden.
- **Middle** — the note you're editing. You can split this into multiple **tabs** and **panes** side by side (great for keeping a rule open next to the roadmap).
- **Right sidebar** — context panels: **Outline** (the note's headings), **Backlinks** (what links *to* this note), **Properties**, **Tags**.

Toggle either sidebar with the icons in the top corners, or `Ctrl+\` to split a pane.

> [!tip] Reading view vs Editing view
> Press **`Ctrl+E`** to flip a note between **Editing** (you see the raw `## heading` and `[[links]]`) and **Reading** (the pretty rendered version). Dashboards and dice only *run* in Reading/Live-Preview view — if you ever see raw code, that's why.

---
## 3 · Moving around fast

Learn these two and you're 80% fluent. Everything in Obsidian is reachable without hunting through menus.

- **`Ctrl+P` — Command Palette.** Type what you want ("graph", "commit", "new canvas", "insert template") and hit Enter. When in doubt, `Ctrl+P`. This is the single most important key.
- **`Ctrl+O` — Quick Switcher.** Type a note name to jump to it instantly. Type `Movement`, Enter, you're there. Start a name that doesn't exist and it offers to *create* it.

Also worth knowing:

| Key | Does |
|---|---|
| `Ctrl+N` | New note |
| `Ctrl+E` | Toggle Editing / Reading view |
| `Ctrl+Click` a `[[link]]` | Open it in a new tab |
| `Ctrl+Hover` a `[[link]]` | Peek at it without leaving |
| `Ctrl+Shift+F` | Search the whole vault |
| `Ctrl+,` | Settings |
| `Ctrl+\` | Split the screen into two panes |

> [!warning] Don't over-organise with folders
> The noob instinct is to build deep folder trees. Resist it. In Obsidian you find things by **linking, searching, and the dashboards** — not by remembering which folder something is in. Your rules already live in one flat `Rules System` folder on purpose.

---
## 4 · The five building blocks

Everything you'll do is one of these five things.

### a) Notes
One `.md` file = one idea. Your convention here: **one note per rule phase** (e.g. `Shooting`), **one note per rule** in the ledger, **one note per unit** later. Small, focused notes link together better than giant ones.

### b) Folders
Just containers. You have `Settlements/Rules System/` (the phases), `Rules Ledger/` (rule stubs), and `Settlements/Templates/`. That's enough structure — don't add more yet.

### c) Links — `[[ ]]`
The heartbeat. Type `[[` and Obsidian pops up a search; pick a note. Variants:

- `[[Terrain]]` → link to the Terrain note.
- `[[Terrain|the board layer]]` → same link, but displays "the board layer".
- `[[Terrain#Cover]]` → jump to the **Cover** heading inside Terrain.
- `![[Terrain#Cover]]` → **embed** (transclude) that section right here — the text appears inline and stays in sync. Powerful for the rulebook later.

**A link to a note that doesn't exist yet is fine** — it shows up faintly, and clicking it creates the note. This lets you write "this interacts with [[Overwatch]]" before Overwatch exists, and come back later.

### d) Tags — `#tag`
Lightweight labels you type anywhere: `#settlements/rules`. Yours are set in each note's properties. Use them to slice across folders (e.g. every note tagged `#settlements/phase`). Links are for *specific* connections; tags are for *categories*.

### e) Properties (frontmatter)
The block at the very top of each note between `---` lines:

```
---
type: rule-phase
stage: S2 Core Combat
status: Not Started
build_order: 7
depends_on: [Unit Design, Movement]
---
```

Obsidian renders this as a tidy **Properties panel**, and — crucially — **your Bases dashboard and Open Decisions board read these fields to build themselves automatically.** When you change `status: Not Started` → `status: Designing`, the dashboards update on their own. **Keeping properties accurate is how the whole system stays alive.** More on the exact values in [§7](#7-·-the-rule-lifecycle-—-the-core-loop).

---
## 5 · Markdown you'll actually use

Markdown = plain text that renders nicely. Here's the 12 things you need; ignore the rest.

```markdown
# Big heading        ## Smaller       ### Smaller still
**bold**   *italic*   ~~strikethrough~~   `inline code`

- bullet
- another
  - nested (indent with Tab)

1. numbered
2. list

- [ ] an unchecked task      ← these power your Open Decisions board
- [x] a done task

> a quote / note

| Col A | Col B |     ← a table
|-------|-------|
| a     | b     |

[[Another Note]]             ← a link
![[Image.png]]              ← embed an image or note
---                          ← a horizontal divider line
```

**Callouts** (the coloured boxes in this guide) — great for "designer's note", warnings, open questions:

```markdown
> [!tip] Title here
> body text
```
Types you'll use: `[!note]` `[!tip]` `[!warning]` `[!question]` `[!danger]` `[!example]`.

> [!example] In practice
> When drafting Shooting, an open question becomes:
> `> [!question] Does moving-and-shooting cost accuracy? Decide before locking.`
> …and it stands out in yellow so you never lose it.

---
## 6 · Your Settlements vault — what's where

Everything lives under `Settlements/Rules System/`. Here's the map and what each thing is *for*:

| File / folder | What it is | When you touch it |
|---|---|---|
| **`Rules System MOC.md`** | "Map of Content" — the front door / index | Start here each session |
| **`Rules System — Master Roadmap.md`** | The ordered plan + 154 decision checkboxes | To see *what to do next* |
| **`Open Decisions.md`** | Live auto-list of everything unresolved | Your daily "what's left" |
| **`_Rules Map.canvas`** | The visual board — phases + dependency arrows | To think spatially / see the whole system |
| **`Rules System.base`** | The Bases dashboard (status tables) | To browse/update phase statuses |
| **32 phase notes** (`Shooting.md`, `Terrain.md`…) | One per design phase — *this is where the actual rules get written* | Constantly |
| **`Rules Ledger/`** | 13 individual rule stubs (`core-001 Movement`…) | As rules formalise |
| **`Settlements/Templates/`** | Blank templates for new phases/units | When adding new notes |

> [!note] MOC = "Map of Content"
> A plain note whose only job is to link to everything else in a topic. Your `Rules System MOC` is the hub — pin it, and you're never lost.

**Anatomy of a phase note** (open `Shooting` to follow along): properties at top (stage/status/dependencies) → a **Focus** section (the checklist of what must be decided) → a **Working rules / decisions** section (currently blank — *this is your writing space*) → links to related rules.

---
## 7 · The rule lifecycle — the core loop

This is the actual job. Every rule travels the same path, and you signal where it is using the **`status`** property. **Use these five values and nothing else** — the dashboards depend on them:

`Not Started` → `Designing` → `Drafted` → `Testing` → `Done`

Here's the loop for one rule, start to finish:

1. **Pick the next thing.** Open **`Open Decisions.md`** or the **Master Roadmap**. Dependencies decide order — you can't finalise Shooting before Unit Design exists. The roadmap's critical path already sequences this.
2. **Open the phase note.** Read its **Focus** checklist — that's literally the list of decisions this rule needs.
3. **Flip status to `Designing`.** Click the `status` property, change it. (The dashboards now show it as in-progress.)
4. **Write in the "Working rules / decisions" section.** Draft the actual rule in plain English. Use a `> [!question]` callout for anything unresolved. Link freely: "resolved on a [[Rules Engine|core test]] vs the target's Cover."
5. **Prototype if it's mathy.** For dice/probability, use the **Dice Roller** ([§8](#8-·-your-toolkit-tool-by-tool)) right in the note to sanity-check odds before committing.
6. **Tick the Focus checkboxes** as you resolve each sub-decision. They vanish from your Open Decisions board automatically.
7. **Flip status to `Drafted`** when the rule is written end-to-end.
8. **Commit a save point** (`Ctrl+P` → "Git: Commit all changes"). Now you can always roll back.
9. Later: `Testing` when you playtest it, `Done` when it's locked.

> [!tip] The golden habit
> **Status property + checkboxes are how the machine knows your progress.** Keep them honest and your dashboards are always a true picture. Skip them and the dashboards lie. It's 5 seconds per rule.

> [!warning] The Canvas colours don't auto-update
> The dashboards (Bases, Open Decisions) read your `status` live. **The Canvas is different** — its node colours were set when I generated it and won't recolour when you change a status. To recolour a canvas card by hand: click it → click the colour dot on its toolbar. Or ask me to regenerate the map. (Treat the Canvas as your *thinking* space, the dashboards as your *source of truth*.)

---
## 8 · Your toolkit, tool by tool

You installed a lot. Here's what each one is *for in this project* and how to open it. Reach everything via `Ctrl+P`.

### 🗺️ The Canvas — `_Rules Map.canvas`
Your see-everything-at-once board. Open it and: **scroll** to pan, **Ctrl+scroll** to zoom, **drag** any card to rearrange, **drag from a card's edge** to draw a new arrow. Double-click empty space for a new card. Because you have **Advanced Canvas**, you can label arrows (e.g. "modifies", "requires") — right-click an arrow. Use this when you want to *reason about the whole system* or spot a rule with too many dependencies.

### 🧠 ExcaliBrain & Graph — the auto-map
Open ExcaliBrain from the left ribbon (or `Ctrl+P` → "ExcaliBrain"). Click any phase and it draws that rule's parents (what it depends on) and children (what depends on it), pulled from your `depends_on`/`feeds_into` properties. Unlike the Canvas, **this rebuilds itself** as you edit links — no manual layout. The core **Graph View** (`Ctrl+P` → "Open graph view") shows the entire web at once; pretty, occasionally useful.

### 📊 Bases dashboard — `Rules System.base`
Enable Bases first (`Ctrl+,` → Core plugins → Bases). Three tabs: Roadmap, Not-started, Rule ledger. It's a live spreadsheet over your notes — and you can **edit a status right in the table** and it writes back to the note. Your at-a-glance control panel.

### 🔓 Open Decisions — `Open Decisions.md`
Powered by **Dataview**. Open it in Reading view: it lists every not-started phase, every in-progress phase, and **every unticked checkbox across all rules**, grouped by phase. This is your honest "what's left to decide" — never manually maintained.

### ☑️ Tasks / checkboxes
Any `- [ ]` line is a task. Tick them as you make decisions. The **Tasks** plugin can also build custom queries (e.g. "show me everything due this week") but you don't need that yet — the Open Decisions board already aggregates them.

### 🧩 Templater — new notes done right
When you add a new phase or unit, don't start blank. `Ctrl+P` → "Templater: Insert template" (or set a hotkey), pick `Rule Phase` or `Unit`, and it fills the correct properties and structure. **One-time setup:** `Ctrl+,` → Templater → set **Template folder location** to `Settlements/Templates`.

### 🎲 Dice Roller — prototype the maths
Turn it on (`Ctrl+,` → Community plugins). Then in any note, a fenced block like:
````
```dice
1d10
```
````
gives you a clickable roller. For a game designer this is gold: while designing the **[[Rules Engine|core dice mechanic]]**, you can test "how often does 1d10 ≥ 7 succeed?" by rolling, or use it to feel out probability curves before you commit the rule. (It also does `2d6`, `1d10+3`, etc.)

### 📇 Fantasy Statblocks — unit cards
For when you reach **[[Unit Design]]**. It renders clean stat cards from a `statblock` code block. Your `Unit` template already lays out the Wounds/Move/STR/DEX/INT/MEN/MOR line; Statblocks makes it print-pretty later. Park it until units exist.

### 🗺️ Leaflet — settlement & territory maps
For **[[Settlement]]** and **[[Territory]]**. Drops an interactive, zoomable, pin-able map into a note from an image. Perfect for "here's the settlement layout that becomes the board." Later-stage tool.

### 🔒 Obsidian Git — your undo button
The safety net. `Ctrl+P` → **"Git: Commit all changes"** makes a save point; **"Git: Create backup"** commits everything at once. If you ever break something or want yesterday's version, every commit is recoverable. **Commit at the end of every session** — it's the one habit that turns "I lost my work" into "I'll just roll back."

### Housekeeping you still owe
- **Turn ON** (installed but disabled): Fantasy Statblocks, Dice Roller, Leaflet, Charts.
- **Pick ONE** banner plugin — you have two (`pexels-banner` + `obsidian-banners`) and they conflict.

---
## 9 · From rules → rulebook

You are not writing the rulebook *now* — you're locking the *system*. But the vault is built so the book falls out of it:

- Every phase note, once `Done`, is a written chapter's worth of rules.
- The **[[Rules System — Master Roadmap#6 · From rules → rulebook (target table of contents)|rulebook table of contents]]** already maps each phase to a chapter (Learn-to-Play → Core → Campaign → Factions → Reference).
- When enough is `Done`, you (or I) assemble the book by **embedding** the locked sections with `![[Shooting#Working rules]]` into a master rulebook note — so the book *quotes the live rules* and never drifts from them.
- Then export to PDF (`Ctrl+P` → "Export to PDF") or hand it to me to lay out.

The takeaway: **write each rule well in its own note, keep status honest, and the rulebook assembles itself.**

---
## 10 · Your first 30-minute session

A concrete dry-run so the whole thing clicks. Do this now:

1. `Ctrl+O` → type `Rules System MOC` → Enter. This is your front door. Read the top.
2. Click through to **`Open Decisions`**. See what's unresolved. (Everything — you just blanked it.)
3. The roadmap says the highest-leverage decision is the **core dice mechanic**. `Ctrl+O` → `Rules Engine`.
4. Change its `status` property to `Designing`.
5. In the **Working rules / decisions** section, write a first draft — e.g. *"Core test: roll 1d10, add the relevant stat, meet-or-beat a Target Value. Nat 10 crits, nat 1 fumbles."*
6. Enable **Dice Roller**, drop a `` ```dice `` `1d10` `` ``` `` block, and roll it 20 times to feel the spread.
7. Add a `> [!question]` callout for anything you're unsure about.
8. Tick one Focus checkbox that you've now resolved.
9. `Ctrl+P` → **"Git: Commit all changes"**, type a message like "first dice draft". Done — that's a permanent save point.
10. Open **`_Rules Map.canvas`** and just look at what you've started to move.

That's the entire workflow. Every rule is a repeat of steps 3–9.

---
## 11 · Habits & gotchas

**Good habits**
- Start every session at the **MOC** or **Open Decisions**.
- Keep the **`status`** property honest — it's the engine.
- **Commit** at the end of every session (`Git: Commit all changes`).
- Write rules in **plain English first**; formalise numbers second.
- Use `> [!question]` callouts for open points so they never get buried.
- Link generously — even to notes that don't exist yet.

**Gotchas**
- **Dashboards blank / showing raw code?** You're in Editing view — press `Ctrl+E` to render, and make sure Dataview/Bases are enabled.
- **Canvas colours look wrong?** They don't auto-sync to `status` — recolour by hand or ask me to regenerate ([§7](#7-·-the-rule-lifecycle-—-the-core-loop)).
- **Two notes, same name?** Links get ambiguous. Keep names unique.
- **Don't rename via the OS file explorer** — rename *inside* Obsidian (right-click → Rename) so it fixes all the links for you.
- **Editing the same note in Obsidian while I edit it** can clash — tell me if a note's open and I'll steer clear.
- **This vault is a Git repo now** but only *local*. Ask me to push to private GitHub for off-machine backup.

---
## 12 · Cheat sheet

**Navigation**
`Ctrl+P` command palette (the one to remember) · `Ctrl+O` jump to/create note · `Ctrl+E` edit/read · `Ctrl+Click` open link in tab · `Ctrl+\` split panes · `Ctrl+Shift+F` search vault

**Writing**
`[[note]]` link · `[[note|label]]` renamed link · `[[note#heading]]` deep link · `![[note]]` embed · `- [ ]` task · `> [!tip]` callout · `#tag` tag · `**bold**` `*italic*`

**Your files**
Front door → `Rules System MOC` · What next → `Open Decisions` / `Master Roadmap` · Visual → `_Rules Map.canvas` · Status board → `Rules System.base` · Write rules → the phase notes

**Rule lifecycle** (the `status` values)
`Not Started → Designing → Drafted → Testing → Done`

**Save your work**
`Ctrl+P` → "Git: Commit all changes" — at the end of every session.

---
*Made for you. If any step doesn't match what you see on screen, tell me what's different and I'll fix the guide. See also [[Rules System MOC]] · [[Rules System — Master Roadmap]].*
