--[[ Settlements — TTS rules layer
     Generated table: see tts/build_table.py. Rules source of truth: the Obsidian
     vault (Rules System/), master note "Full Rules System v1".

     DESIGN RULE FOR THIS FILE: automate the bookkeeping a player gets wrong, and
     nothing else. It rolls tests, tracks Stress, runs the End Phase in order, and
     polices the terrain density band. It does NOT move models, decide targets, or
     enforce legality — the players still play the game.

     Every command acts on the model you are HOVERING over (or your selection),
     which is the only interaction pattern that works reliably without custom UI.
]]

INCH = 1.0                -- TTS units per game inch. Calibrate once with the ruler.
BOARD = 36                -- 3'x3'
TARGET = 7                -- the one test target: 1d10 + Stat + Mods vs 7+
HOLD_RADIUS = 3           -- objective hold/contest radius (§12.7)
DENSITY_MIN, DENSITY_MAX = 9, 12   -- the sacred band (§5)

state = { round = 0, vp = { White = 0, Red = 0 }, firstPlayer = nil }

COND = {
  pinned = 'Pinned', prone = 'Prone', down = 'Down', hidden = 'Hidden',
  ready = 'Ready', fire = 'Fire', bleed = 'Bleed', poison = 'Poison',
  suppressed = 'Suppressed', offbalance = 'Off-Balance', hobbled = 'Hobbled',
  blind = 'Blind', shocked = 'Shocked', grappled = 'Grappled', snared = 'Snared',
}

-- ---------------------------------------------------------------- dice / tests

function d10() return math.random(1, 10) end

--[[ The core test. Natural 1 always fails, natural 10 always succeeds — those
     override the modifier entirely, which is why this is not just d+mod>=7. ]]
function coreTest(stat, mods)
  local d = d10()
  local total = d + stat + mods
  local pass, why
  if d == 1 then pass, why = false, 'natural 1 — automatic failure'
  elseif d == 10 then pass, why = true, 'natural 10 — automatic success'
  else pass, why = total >= TARGET, string.format('%d+%d%s = %d vs %d+',
        d, stat, mods ~= 0 and string.format('%+d', mods) or '', total, TARGET) end
  return pass, d, total, why
end

function capMod(m)   -- ±3 cap on any single roll (§10)
  if m > 3 then return 3 end
  if m < -3 then return -3 end
  return m
end

function report(colour, msg) printToAll(msg, colour or {1, 1, 1}) end

local GOOD, BAD, INFO = {0.45, 0.9, 0.45}, {0.95, 0.45, 0.4}, {0.7, 0.8, 1.0}

-- ---------------------------------------------------------------- unit records

--[[ A "unit" is any object carrying a JSON blob in its GMNotes. The table's
     model blocks ship with one; anything you drag in can be enrolled with
     !enrol. Keeping state in GMNotes means it survives save/load for free. ]]
function unitData(obj)
  if not obj then return nil end
  local raw = obj.getGMNotes()
  if raw == nil or raw == '' then return nil end
  local ok = JSON.decode(raw)
  if type(ok) ~= 'table' or not ok.unit then return nil end
  return ok
end

function writeUnit(obj, d) obj.setGMNotes(JSON.encode(d)) end

function target(player)
  local sel = player.getSelectedObjects()
  if sel and #sel == 1 then return sel[1] end
  local hov = player.getHoverObject()
  if hov then return hov end
  report(BAD, '[Settlements] Hover over a model (or select exactly one) first.')
  return nil
end

function unitAt(player)
  local obj = target(player)
  if not obj then return nil, nil end
  local d = unitData(obj)
  if not d then
    report(BAD, '[Settlements] "' .. (obj.getName() ~= '' and obj.getName() or 'that object')
      .. '" is not an enrolled unit. Use: !enrol <name> STR AGI DEX INT NRV')
    return nil, nil
  end
  return obj, d
end

function label(obj, d)
  local bits = {}
  if d.stress > 0 then table.insert(bits, 'Stress ' .. d.stress) end
  for k, on in pairs(d.cond or {}) do if on then table.insert(bits, COND[k] or k) end end
  local suffix = #bits > 0 and ('\n[b]' .. table.concat(bits, ' · ') .. '[/b]') or ''
  obj.setDescription(string.format('%s  W%d\nSTR %d AGI %d DEX %d INT %d NRV %d%s',
    d.rank or 'Fighter', d.wnd, d.str, d.agi, d.dex, d.int, d.nrv, suffix))
end

-- Shaken: a flat -1 on all rolls at 1+ Stress. It does NOT double-apply on the
-- Break test itself (§11), which is the single easiest rule here to get wrong.
function shaken(d) return (d.stress or 0) >= 1 and -1 or 0 end

function allUnits()
  local out = {}
  for _, obj in ipairs(getAllObjects()) do
    local d = unitData(obj)
    if d then table.insert(out, { obj = obj, d = d }) end
  end
  return out
end

-- ---------------------------------------------------------------- geometry

function inches(a, b)
  local p, q = a.getPosition(), b.getPosition()
  return math.sqrt((p.x - q.x) ^ 2 + (p.z - q.z) ^ 2) / INCH
end

function boardSquare(obj)   -- which of the nine 12"x12" density squares (§5)
  local p = obj.getPosition()
  local col = math.floor((p.x / INCH + BOARD / 2) / 12)
  local row = math.floor((p.z / INCH + BOARD / 2) / 12)
  if col < 0 or col > 2 or row < 0 or row > 2 then return nil end
  return row * 3 + col + 1
end

-- ---------------------------------------------------------------- commands

function onLoad()
  math.randomseed(os.time())
  report(INFO, '[Settlements] Rules layer loaded. Type [b]!help[/b] for commands.')
end

local HELP = {
  '[b]Settlements — chat commands[/b]  (hover a model, then type)',
  '  !help                        this list',
  '  !enrol <name> S A D I N [W]  make the hovered object a unit',
  '  !sheet                       show the hovered unit',
  '  !test <stat> [mods]          the core test, 1d10+Stat+Mods vs 7+',
  '  !shoot [cover]               DEX test; cover 0/1/2/3 -> 0/-1/-2/-3',
  '  !melee                       opposed STR vs a second model (ties -> defender)',
  '  !injury <dmg> [armour]       1d10 + Damage - Armour vs 7+',
  '  !stress <+n|-n>              adjust Stress (auto-applies Shaken)',
  '  !cond <name> [off]           toggle a condition token',
  '  !break                       one Break test (End Phase does all of them)',
  '  !endphase                    conditions -> Break tests -> score, in order',
  '  !priority                    1d10 each, +1 to whoever has fewer models',
  '  !round                       advance the round counter',
  '  !density                     check the 9-12 band and the nine squares',
  '  !score                       objective hold/contest right now',
  '',
  '[b]Terrain setup[/b] — terrain ships locked so physics cannot shift it',
  '  !unlock                      unlock terrain so you can DRAG it',
  '  !link                        fix each model to its footprint pad (do this first)',
  '  !unlink                      separate models from pads again',
  '  !lock                        re-lock once you are happy with the layout',
}

function onChat(msg, player)
  if msg:sub(1, 1) ~= '!' then return true end
  local args = {}
  for w in msg:gmatch('%S+') do table.insert(args, w) end
  local cmd = args[1]:lower()
  local n = function(i, dflt) return tonumber(args[i]) or dflt end

  if cmd == '!help' then
    for _, l in ipairs(HELP) do printToAll(l, INFO) end

  elseif cmd == '!enrol' or cmd == '!enroll' then
    local obj = target(player); if not obj then return false end
    if #args < 7 then
      report(BAD, 'Usage: !enrol <name> STR AGI DEX INT NRV [WND]'); return false end
    local d = { unit = true, name = args[2], rank = 'Fighter',
                str = n(3, 0), agi = n(4, 0), dex = n(5, 0), int = n(6, 0), nrv = n(7, 0),
                wnd = n(8, 1), stress = 0, cond = {} }
    writeUnit(obj, d); obj.setName(d.name); label(obj, d)
    report(GOOD, string.format('[Settlements] Enrolled %s — STR %d AGI %d DEX %d INT %d NRV %d, WND %d',
      d.name, d.str, d.agi, d.dex, d.int, d.nrv, d.wnd))

  elseif cmd == '!sheet' then
    local obj, d = unitAt(player); if not d then return false end
    report(INFO, string.format('[%s] STR %d AGI %d DEX %d INT %d NRV %d · WND %d · Stress %d%s',
      d.name, d.str, d.agi, d.dex, d.int, d.nrv, d.wnd, d.stress,
      shaken(d) < 0 and ' (Shaken -1)' or ''))

  elseif cmd == '!test' then
    local stat, mods = n(2, 0), capMod(n(3, 0))
    local pass, _, _, why = coreTest(stat, mods)
    report(pass and GOOD or BAD, string.format('[Test] %s — %s', why, pass and 'PASS' or 'FAIL'))

  elseif cmd == '!shoot' then
    local obj, d = unitAt(player); if not d then return false end
    local cover = n(2, 0)
    local mods = capMod(-cover + shaken(d))
    local pass, _, _, why = coreTest(d.dex, mods)
    report(pass and GOOD or BAD, string.format('[Shoot] %s DEX %d, cover -%d%s — %s → %s',
      d.name, d.dex, cover, shaken(d) < 0 and ', Shaken -1' or '', why,
      pass and 'HIT — roll !injury' or 'MISS'))

  elseif cmd == '!melee' then
    local sel = player.getSelectedObjects()
    if not sel or #sel ~= 2 then
      report(BAD, '[Melee] Select exactly TWO models: attacker first, then defender.'); return false end
    local a, b = unitData(sel[1]), unitData(sel[2])
    if not a or not b then report(BAD, '[Melee] Both models must be enrolled.'); return false end
    local ra = d10() + a.str + shaken(a)
    local rb = d10() + b.str + shaken(b)
    -- ties go to the DEFENDER (§8)
    local winner = ra > rb and a or b
    local loser = ra > rb and b or a
    report(INFO, string.format('[Melee] %s %d vs %s %d — %s wins%s. %s takes the Injury roll.',
      a.name, ra, b.name, rb, winner.name, ra == rb and ' (tie → defender)' or '', loser.name))

  elseif cmd == '!injury' then
    local dmg, armour = n(2, 0), n(3, 0)
    local d = d10()
    local total = d + dmg - armour
    local pass = (d ~= 1) and (d == 10 or total >= TARGET)
    report(pass and BAD or GOOD, string.format(
      '[Injury] %d+%d-%d = %d vs 7+ — %s', d, dmg, armour, total,
      pass and 'WOUND (ranged/hazard → Down · melee → Out of Action)'
           or 'no wound — ranged: Pinned +1 Stress · melee: +1 Stress (Shaken)'))

  elseif cmd == '!stress' then
    local obj, d = unitAt(player); if not d then return false end
    local delta = n(2, 0)
    d.stress = math.max(0, (d.stress or 0) + delta)
    writeUnit(obj, d); label(obj, d)
    local note = d.stress >= 2 and ' — Break test due in the End Phase'
      or (d.stress == 1 and ' — Shaken (-1 to all rolls)' or '')
    report(INFO, string.format('[%s] Stress %d%s', d.name, d.stress, note))

  elseif cmd == '!cond' then
    local obj, d = unitAt(player); if not d then return false end
    local key = (args[2] or ''):lower()
    if not COND[key] then
      local keys = {}
      for k in pairs(COND) do table.insert(keys, k) end
      table.sort(keys)
      report(BAD, '[Cond] Unknown. One of: ' .. table.concat(keys, ' ')); return false end
    d.cond = d.cond or {}
    local turningOn = not d.cond[key] and (args[3] or ''):lower() ~= 'off'
    d.cond[key] = turningOn or nil
    -- Gaining a negative condition costs +1 Stress the FIRST time, and Pinned's
    -- own +1 already counted as that — don't double it (§10).
    if turningOn and key ~= 'pinned' and key ~= 'ready' and key ~= 'hidden' then
      d.stress = (d.stress or 0) + 1
      report(INFO, '  +1 Stress for gaining a condition (first application only)')
    end
    writeUnit(obj, d); label(obj, d)
    report(INFO, string.format('[%s] %s %s', d.name, COND[key], turningOn and 'ON' or 'OFF'))

  elseif cmd == '!break' then
    local obj, d = unitAt(player); if not d then return false end
    breakTest(obj, d)

  elseif cmd == '!endphase' then endPhase()
  elseif cmd == '!priority' then priority()
  elseif cmd == '!round' then
    state.round = state.round + 1
    report(INFO, string.format('[Settlements] ===== ROUND %d =====%s', state.round,
      state.round > 6 and '  (game ends after round 6)' or ''))
  elseif cmd == '!density' then density()
  elseif cmd == '!score' then score()
  elseif cmd == '!unlock' then setTerrainLock(false)
  elseif cmd == '!lock' then setTerrainLock(true)
  elseif cmd == '!link' then linkScenery()
  elseif cmd == '!unlink' then unlinkScenery()
  else return true end
  return false
end

-- ---------------------------------------------------------------- morale

--[[ Break test (§11): 1d10 + NRV - (Stress-1) vs 7+. Shaken's -1 does NOT apply
     here. Fail margin decides the nerve state: 2 Bolt / 3 Broken / 4+ BugOut. ]]
function breakTest(obj, d)
  if (d.stress or 0) < 2 then
    report(INFO, string.format('[%s] Stress %d — no Break test needed (2+ required).',
      d.name, d.stress or 0))
    return
  end
  local penalty = d.stress - 1
  local roll = d10()
  local total = roll + d.nrv - penalty
  if roll == 10 or (roll ~= 1 and total >= TARGET) then
    report(GOOD, string.format('[%s] Break %d+%d-%d = %d vs 7+ — HOLDS',
      d.name, roll, d.nrv, penalty, total))
    return
  end
  local margin = TARGET - total
  local outcome = margin >= 4 and 'BugOut — routs off the board, removed from play'
    or (margin == 3 and 'Broken — freezes, cannot act'
    or 'Bolt — flees toward the nearest board edge, hugging cover')
  d.cond = d.cond or {}
  d.cond.broken = (margin == 3) or nil
  writeUnit(obj, d); label(obj, d)
  report(BAD, string.format('[%s] Break %d+%d-%d = %d vs 7+ — FAIL by %d → %s',
    d.name, roll, d.nrv, penalty, total, margin, outcome))
end

-- ---------------------------------------------------------------- end phase

--[[ The End Phase in the order the rules give it (§3): refresh, then persistent
     conditions, then Break tests for everyone at 2+ Stress, then score. Doing
     these out of order changes outcomes, which is exactly why it is automated. ]]
function endPhase()
  report(INFO, '[Settlements] ---------- END PHASE ----------')
  local units = allUnits()

  report(INFO, '1. Persistent conditions')
  local any = false
  for _, u in ipairs(units) do
    local d, c = u.d, u.d.cond or {}
    if c.fire then
      any = true
      local r = d10(); local t = r + 1     -- +1 Damage, ignores Armour
      local wound = (r ~= 1) and (r == 10 or t >= TARGET)
      report(wound and BAD or GOOD, string.format('   %s burning: %d+1 = %d vs 7+ — %s',
        d.name, r, t, wound and 'WOUND' or 'no wound'))
    end
    if c.bleed then
      any = true
      d.wnd = d.wnd - 1
      report(BAD, string.format('   %s bleeding: -1 WND (now %d)%s', d.name, d.wnd,
        d.wnd <= 0 and ' — DOWN, and Down+Bleed bleeds out' or ''))
      writeUnit(u.obj, d); label(u.obj, d)
    end
    if c.poison then
      any = true
      local pass = coreTest(d.str, 0)
      if pass then
        d.cond.poison = nil; writeUnit(u.obj, d); label(u.obj, d)
        report(GOOD, string.format('   %s shakes off Poison (STR test passed)', d.name))
      else
        report(BAD, string.format('   %s still Poisoned (-1 all rolls)', d.name))
      end
    end
  end
  if not any then report(INFO, '   none') end

  report(INFO, '2. Break tests (every unit at 2+ Stress)')
  local tested = false
  for _, u in ipairs(units) do
    if (u.d.stress or 0) >= 2 then tested = true; breakTest(u.obj, u.d) end
  end
  if not tested then report(INFO, '   none') end

  report(INFO, '3. Stress shed — a unit at exactly 1 Stress that took none this round')
  for _, u in ipairs(units) do
    if u.d.stress == 1 and not u.d.gainedThisRound then
      u.d.stress = 0; writeUnit(u.obj, u.d); label(u.obj, u.d)
      report(GOOD, string.format('   %s sheds its last Stress', u.d.name))
    end
    u.d.gainedThisRound = nil; writeUnit(u.obj, u.d)
  end

  report(INFO, '4. Objectives')
  score()
  report(INFO, '[Settlements] ------ END PHASE COMPLETE ------')
end

-- ---------------------------------------------------------------- objectives

--[[ Holding (§12.7): a standing friendly within 3" and no enemy within 3".
     Both sides within 3" = contested, nobody scores. Down/Out/Broken can't hold.
     No scoring in round 1. ]]
function score()
  local objectives = {}
  for _, obj in ipairs(getAllObjects()) do
    local gm = obj.getGMNotes()
    if gm and gm ~= '' then
      local j = JSON.decode(gm)
      if type(j) == 'table' and j.objective then table.insert(objectives, obj) end
    end
  end
  if #objectives == 0 then report(BAD, '[Score] No objective markers found.'); return end
  if state.round <= 1 then
    report(INFO, '[Score] No scoring in round 1 (§12.7).')
    return
  end

  local units = allUnits()
  for i, o in ipairs(objectives) do
    local near = { White = 0, Red = 0 }
    for _, u in ipairs(units) do
      local c = u.d.cond or {}
      local standing = not (c.down or c.broken) and u.d.wnd > 0
      if standing and inches(u.obj, o) <= HOLD_RADIUS then
        local side = u.obj.getColorTint and colourSide(u.obj) or 'White'
        near[side] = (near[side] or 0) + 1
      end
    end
    local holder
    if near.White > 0 and near.Red > 0 then holder = nil
    elseif near.White > 0 then holder = 'White'
    elseif near.Red > 0 then holder = 'Red' end
    if holder then
      state.vp[holder] = state.vp[holder] + 1
      report(GOOD, string.format('   Objective %d — held by %s (+1 VP)', i, holder))
    elseif near.White > 0 and near.Red > 0 then
      report(INFO, string.format('   Objective %d — CONTESTED, nobody scores', i))
    else
      report(INFO, string.format('   Objective %d — unheld', i))
    end
  end
  report(INFO, string.format('   VP — White %d · Red %d', state.vp.White, state.vp.Red))
end

function colourSide(obj)
  local t = obj.getColorTint()
  return (t.r >= t.b) and 'Red' or 'White'
end

-- ---------------------------------------------------------------- priority

function priority()
  local count = { White = 0, Red = 0 }
  for _, u in ipairs(allUnits()) do
    local c = u.d.cond or {}
    if u.d.wnd > 0 and not c.down then
      local s = colourSide(u.obj); count[s] = count[s] + 1
    end
  end
  local under = nil
  if count.White < count.Red then under = 'White'
  elseif count.Red < count.White then under = 'Red' end
  local rolls = {}
  for _, side in ipairs({ 'White', 'Red' }) do
    local r = d10()
    local bonus = (side == under) and 1 or 0
    rolls[side] = r + bonus
    report(INFO, string.format('   %s: %d%s = %d  (%d models)', side, r,
      bonus > 0 and ' +1 underdog' or '', rolls[side], count[side]))
  end
  if rolls.White == rolls.Red then
    report(INFO, '[Priority] Tie — re-roll. (In a RAID the defender simply takes it, §5.)')
  else
    local w = rolls.White > rolls.Red and 'White' or 'Red'
    state.firstPlayer = w
    report(GOOD, string.format('[Priority] %s chooses to activate first or second.', w))
  end
end

-- ---------------------------------------------------------------- terrain setup

--[[ Terrain ships LOCKED so physics cannot shove a building off its footprint
     mid-game. That also means you cannot drag it, so setup needs an explicit
     unlock -> arrange -> re-lock cycle.

     Each building is TWO objects: a thin rules-true PAD carrying the cover value
     and the density GMNotes, plus the scenery model standing on it. Dragging one
     would leave the other behind, so !link fixes each model to its pad first and
     they move as a single piece. ]]

function terrainObjects()
  local out = {}
  for _, o in ipairs(getAllObjects()) do
    local gm = o.getGMNotes()
    if gm and gm ~= '' then
      local j = JSON.decode(gm)
      if type(j) == 'table' and (j.terrain or j.scenery or j.board or j.deploy) then
        table.insert(out, { obj = o, d = j })
      end
    end
  end
  return out
end

function setTerrainLock(locked)
  local n = 0
  for _, t in ipairs(terrainObjects()) do
    -- the board slab and deployment bands stay locked always: they are the
    -- coordinate system, and nudging them silently moves every measurement
    if not (t.d.board or t.d.deploy) then
      t.obj.setLock(locked)
      n = n + 1
    end
  end
  report(locked and GOOD or INFO, string.format(
    '[Terrain] %d pieces %s. %s', n, locked and 'LOCKED' or 'UNLOCKED',
    locked and 'Physics can no longer shove them off their footprints.'
           or 'Drag to arrange. Run !link first so models carry their pads, '
              .. 'then !density to re-check the 9-12 band, then !lock.'))
end

function linkScenery()
  --[[ Joint each scenery model to the pad beneath it. Nearest pad within 4"
       claims the model — pads sit directly under their own model, so proximity
       is unambiguous here. ]]
  local pads, models = {}, {}
  for _, t in ipairs(terrainObjects()) do
    if t.d.terrain then table.insert(pads, t.obj)
    elseif t.d.scenery then table.insert(models, t.obj) end
  end
  local n = 0
  for _, m in ipairs(models) do
    local best, bd = nil, 4.0
    for _, p in ipairs(pads) do
      local d = inches(m, p)
      if d < bd then best, bd = p, d end
    end
    if best then
      m.jointTo(best, { type = 'Fixed', collision = false })
      n = n + 1
    end
  end
  report(GOOD, string.format('[Terrain] linked %d scenery model(s) to their '
    .. 'footprint pads — each building now drags as one piece.', n))
  if n < #models then
    report(INFO, string.format('   %d model(s) had no pad within 4" and stayed loose.',
      #models - n))
  end
end

function unlinkScenery()
  local n = 0
  for _, t in ipairs(terrainObjects()) do
    if t.d.scenery then
      t.obj.jointTo()          -- no argument = clear joints
      n = n + 1
    end
  end
  report(INFO, string.format('[Terrain] unlinked %d model(s) — pads and models '
    .. 'now move independently.', n))
end

-- ---------------------------------------------------------------- density

--[[ The most powerful balance dial in the game (§5): 9-12 large features, at
     least one in each of the nine 12"x12" squares. Terrain density alone swung
     win rate 66 points in simulation — more than any points cost could. This is
     the check most likely to be skipped at a real table, so it is one command. ]]
function density()
  local large, per = 0, {}
  for i = 1, 9 do per[i] = 0 end
  for _, obj in ipairs(getAllObjects()) do
    local gm = obj.getGMNotes()
    if gm and gm ~= '' then
      local j = JSON.decode(gm)
      if type(j) == 'table' and j.terrain and j.large then
        large = large + 1
        local sq = boardSquare(obj)
        if sq then per[sq] = per[sq] + 1 end
      end
    end
  end
  local ok = large >= DENSITY_MIN and large <= DENSITY_MAX
  report(ok and GOOD or BAD, string.format(
    '[Density] %d large features — %s (band is %d-%d, and %d is a HARD ceiling)',
    large, ok and 'LEGAL' or 'ILLEGAL', DENSITY_MIN, DENSITY_MAX, DENSITY_MAX))
  local empty = {}
  for i = 1, 9 do if per[i] == 0 then table.insert(empty, i) end end
  if #empty > 0 then
    report(BAD, '[Density] Empty 12" squares (each needs at least one): '
      .. table.concat(empty, ', '))
  else
    report(GOOD, '[Density] All nine squares occupied.')
  end
  report(INFO, string.format('   per square: %d %d %d / %d %d %d / %d %d %d',
    per[7], per[8], per[9], per[4], per[5], per[6], per[1], per[2], per[3]))
  if not ok then
    report(INFO, '   Sparse boards hand it to shooters; crowded boards hand it to swarms.')
  end
end
