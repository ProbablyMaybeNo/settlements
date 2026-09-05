# Settlements Sim Explorer - launch the browsable UI.
#   powershell -File test-bench/explorer/serve.ps1
#
# Clears the port FIRST. Datasette holds the SQLite file open for the life of
# the server, so a rebuild while one is running dies on a Windows file lock.
$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$port = 8765

$busy = Get-NetTCPConnection -LocalPort $port -State Listen -ErrorAction SilentlyContinue
if ($busy) {
    Write-Host "stopping the server already on :$port ..." -ForegroundColor Yellow
    $busy | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force }
    Start-Sleep -Seconds 2
}

Write-Host "rebuilding settlements-sims.db ..." -ForegroundColor Cyan
py -3.13 "$here\build_db.py"
if ($LASTEXITCODE -ne 0) { throw "build_db.py failed - not serving a stale database" }

Write-Host "`nserving on http://127.0.0.1:$port/  - Ctrl+C to stop" -ForegroundColor Green
py -3.13 -m datasette serve "$here\settlements-sims.db" `
    --metadata "$here\metadata.json" `
    --port $port --setting sql_time_limit_ms 5000 --setting max_returned_rows 2000 -o
