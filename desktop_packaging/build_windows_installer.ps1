$ErrorActionPreference = "Stop"
Write-Host "YaSara Windows installer build scaffold"
$Root = Split-Path -Parent $PSScriptRoot
$Out = Join-Path $Root "dist"
New-Item -ItemType Directory -Force -Path $Out | Out-Null
$InstallerPlan = Join-Path $Out "YaSara_Setup_Plan.txt"
@"
YaSara Professional v1.0 Installer Plan
1. Copy backend, docs and deployment files
2. Create Python virtual environment
3. Install requirements
4. Create Start Backend shortcut
5. Create Run Tests shortcut

For real installer compilation, install Inno Setup and compile:
desktop_packaging\yasara_desktop_installer.iss
"@ | Set-Content -Path $InstallerPlan -Encoding UTF8
Write-Host "Installer plan created at $InstallerPlan"
