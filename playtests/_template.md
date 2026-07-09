# Playtest — YYYY-MM-DD — <Scenario Name>

**Rules version under test:** v0.X
**Players:** solo / 2P / N
**Scenario:** link or copy from `scenarios/<name>.md`
**Question of the session:** (one specific thing you wanted to learn)

---

## Forces used

**Attacker:** specific units, specific equipment.
**Defender:** same.

## Outcome

Who won, by what margin, how long it actually took (clock the setup,
gameplay, packdown separately).

## What the session said about the question

Two paragraphs max. The answer, or "still inconclusive — try again with X."

## Rules to revise

- **Rule:** [name] — what went wrong → **Proposed fix:** [one line].
- **Rule:** ... → **Proposed fix:** ...

## Rules confirmed working

- ...

## New ideas surfaced

(Bullet each one, then add to `ideas/INBOX.md` for triage.)

- ...

## Pace / fun rating

- Pace: too slow / right / too fast
- Fun: 1-5
- Would replay: yes / no / with changes

---

After writing this, add a row to `TRACKERS/playtests.csv` and run
`py -3.13 scripts/notion_sync.py sync-playtests`.
