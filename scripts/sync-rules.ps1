#requires -Version 5
<#
  sync-rules.ps1 — mirror the Settlements design notes from the Obsidian vault
  into this repo's rules-vault/ folder.

  WHY: the Obsidian vault is the LIVE editing surface for the rules (Obsidian +
  Obsidian Sync). This repo keeps a mirror so the standalone Settlements repo is
  self-contained. Run this after changing rules in Obsidian, then commit rules-vault/.

  ONE-WAY: vault -> repo. Never hand-edit rules-vault/ — it is overwritten here.
#>
$ErrorActionPreference = 'Stop'
$src = Join-Path $env:USERPROFILE 'Documents\Obsidian Vault\Settlements'
$dst = Join-Path $PSScriptRoot '..\rules-vault'

if (-not (Test-Path $src)) { Write-Error "Vault Settlements folder not found: $src"; exit 1 }

# /MIR mirrors src into dst (adds, updates, and deletes removed files).
robocopy $src $dst /MIR /NFL /NDL /NJH /NJS /NP | Out-Null
if ($LASTEXITCODE -ge 8) { Write-Error "robocopy failed (exit $LASTEXITCODE)"; exit 1 }

Write-Host "Synced vault Settlements -> rules-vault/."
Write-Host "Next: git add rules-vault && git commit -m 'Sync rules from Obsidian'"
