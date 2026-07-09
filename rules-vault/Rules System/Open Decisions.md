---
type: dashboard
title: Open Decisions
tags: [settlements/dashboard]
---
# 🔓 Open Decisions — live

Auto-generated from the phase notes. Tick a box or change a `status:` and these refresh. See [[Rules System — Master Roadmap]] for the full plan and [[_Rules Map.canvas|the map]].

## Phases still to start
```dataview
TABLE WITHOUT ID file.link AS "Phase", stage AS "Stage", depends_on AS "Depends on"
FROM "Settlements/Rules System"
WHERE type = "rule-phase" AND status = "Not Started"
SORT build_order ASC
```

## In progress (drafting / designing)
```dataview
TABLE WITHOUT ID file.link AS "Phase", status AS "Status", stage AS "Stage"
FROM "Settlements/Rules System"
WHERE type = "rule-phase" AND (status = "Designing" OR status = "Drafted")
SORT build_order ASC
```

## Every unresolved decision (unticked checkboxes)
```dataview
TASK
FROM "Settlements/Rules System"
WHERE !completed AND !contains(file.name, "Master Roadmap")
GROUP BY file.link
```

## Rule ledger status
```dataview
TABLE WITHOUT ID file.link AS "Rule", category AS "Category", status AS "Status", parent_phase AS "Phase"
FROM "Settlements/Rules System/Rules Ledger"
WHERE type = "rule"
SORT category ASC, file.name ASC
```
