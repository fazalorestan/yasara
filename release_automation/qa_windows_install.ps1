$ErrorActionPreference = "Stop"
Write-Host "Running YaSara Windows QA install check..."
$Root = Split-Path -Parent $PSScriptRoot
$Backend = Join-Path $Root "backend"
if (!(Test-Path $Backend)) { throw "Backend folder not found." }
if (!(Test-Path (Join-Path $Backend "app"))) { throw "Backend app folder not found." }
if (!(Test-Path (Join-Path $Root "windows_runtime"))) { throw "windows_runtime folder not found." }
Write-Host "QA install check complete."
