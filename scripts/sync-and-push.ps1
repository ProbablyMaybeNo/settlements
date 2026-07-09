#requires -Version 5
<#
  sync-and-push.ps1 — auto-sync ONLY the Settlements folder from the Obsidian
  vault into this repo's rules-vault/, then commit + push if it changed.

  Designed to run on a schedule (Windows Task Scheduler, "Settlements Rules Sync").
  ONE-WAY: Obsidian vault -> repo. Obsidian stays the source of truth; nothing
  else in the vault is ever touched. The whole vault is backed up separately by
  Obsidian Sync — this only version-controls the Settlements rules.
#>
$ErrorActionPreference = 'Stop'
$repo = Split-Path $PSScriptRoot -Parent
$src  = Join-Path $env:USERPROFILE 'Documents\Obsidian Vault\Settlements'
$dst  = Join-Path $repo 'rules-vault'

if (-not (Test-Path $src)) { Write-Error "Vault Settlements folder not found: $src"; exit 1 }

# Mirror the notes (adds, updates, deletes) — only the Settlements folder.
robocopy $src $dst /MIR /NFL /NDL /NJH /NJS /NP | Out-Null
if ($LASTEXITCODE -ge 8) { Write-Error "robocopy failed (exit $LASTEXITCODE)"; exit 1 }

# Stage only rules-vault so unrelated repo work is never swept in.
git -C $repo add rules-vault
git -C $repo diff --cached --quiet -- rules-vault
if ($LASTEXITCODE -ne 0) {
  $stamp = Get-Date -Format 'yyyy-MM-dd HH:mm'
  git -C $repo commit -q -m "Sync rules from Obsidian ($stamp)" -- rules-vault
  Write-Host "Committed rules update ($stamp)"
}

# Always attempt a push (harmless if nothing pending; also flushes a prior failed push).
git -C $repo push -q origin main
if ($LASTEXITCODE -eq 0) { Write-Host "Push OK." }
else { Write-Host "Push failed (exit $LASTEXITCODE) - will retry next run." }
