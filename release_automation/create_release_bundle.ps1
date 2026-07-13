$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Out = Join-Path $Root "dist"
New-Item -ItemType Directory -Force -Path $Out | Out-Null
$Bundle = Join-Path $Out "yasara_professional_v1_0_release_bundle.zip"
$Paths = @(
    (Join-Path $Root "backend"),
    (Join-Path $Root "docs"),
    (Join-Path $Root "deployment"),
    (Join-Path $Root "windows_runtime"),
    (Join-Path $Root "desktop_packaging"),
    (Join-Path $Root "release_automation"),
    (Join-Path $Root "FINAL_VERSION_FREEZE_MANIFEST.json"),
    (Join-Path $Root "YASARA_V1_FINAL_README.md"),
    (Join-Path $Root "YASARA_V1_TO_V1_1_ROADMAP.md")
)
$Existing = $Paths | Where-Object { Test-Path $_ }
Compress-Archive -Path $Existing -DestinationPath $Bundle -Force
Write-Host "Release bundle created at $Bundle"
