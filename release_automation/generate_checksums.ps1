$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Out = Join-Path $Root "dist"
New-Item -ItemType Directory -Force -Path $Out | Out-Null
$ChecksumFile = Join-Path $Out "SHA256SUMS.txt"
Get-ChildItem -Path $Out -File | Where-Object { $_.Name -ne "SHA256SUMS.txt" } | ForEach-Object {
    $Hash = Get-FileHash -Algorithm SHA256 -Path $_.FullName
    "$($Hash.Hash)  $($_.Name)"
} | Set-Content -Path $ChecksumFile -Encoding UTF8
Write-Host "Checksums generated at $ChecksumFile"
