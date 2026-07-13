$ErrorActionPreference = "Stop"
Write-Host "Building YaSara desktop portable package..."
$Root = Split-Path -Parent $PSScriptRoot
$Out = Join-Path $Root "dist"
New-Item -ItemType Directory -Force -Path $Out | Out-Null
$Paths = @(
    (Join-Path $Root "backend"),
    (Join-Path $Root "docs"),
    (Join-Path $Root "deployment"),
    (Join-Path $Root "windows_runtime")
) | Where-Object { Test-Path $_ }
Compress-Archive -Path $Paths -DestinationPath (Join-Path $Out "yasara_desktop_portable.zip") -Force
Write-Host "Portable package created."
