@echo off
setlocal enabledelayedexpansion
cd /d "%~dp0..\.."

echo ==========================================
echo Building YaSara Professional v1.1 Final
echo ==========================================

set ROOT=%CD%
set OUT=%ROOT%\dist
set FINAL_ZIP=%OUT%\YaSara_Professional_v1_1_Final.zip
set PORTABLE_ZIP=%OUT%\YaSara_Professional_v1_1_Portable.zip

if not exist "%OUT%" mkdir "%OUT%"
if exist "%FINAL_ZIP%" del /q "%FINAL_ZIP%"
if exist "%PORTABLE_ZIP%" del /q "%PORTABLE_ZIP%"

echo 1.1.0> VERSION

powershell -NoProfile -ExecutionPolicy Bypass -Command "$json=@{product='YaSara Professional';version='1.1.0';status='final';live_trading_enabled=$false;built_at=(Get-Date).ToString('o')} | ConvertTo-Json; Set-Content -Path 'BUILD_INFO.json' -Value $json -Encoding UTF8"

powershell -NoProfile -ExecutionPolicy Bypass -Command "Compress-Archive -Path 'backend','docs','deployment','windows_runtime','desktop_packaging','release_automation','FINAL_VERSION_FREEZE_MANIFEST.json','YASARA_V1_FINAL_README.md','YASARA_V1_TO_V1_1_ROADMAP.md','YASARA_V2_ROADMAP.md','VERSION','BUILD_INFO.json','RELEASE_NOTES_V1_1.md','CHANGELOG_V1_1.md' -DestinationPath '%FINAL_ZIP%' -Force"

powershell -NoProfile -ExecutionPolicy Bypass -Command "Compress-Archive -Path 'backend','windows_runtime','VERSION','BUILD_INFO.json' -DestinationPath '%PORTABLE_ZIP%' -Force"

powershell -NoProfile -ExecutionPolicy Bypass -Command "Get-FileHash -Algorithm SHA256 '%FINAL_ZIP%','%PORTABLE_ZIP%' | ForEach-Object { $_.Hash + '  ' + (Split-Path $_.Path -Leaf) } | Set-Content -Path '%OUT%\SHA256SUMS.txt' -Encoding UTF8"

echo.
echo Final packages created:
echo %FINAL_ZIP%
echo %PORTABLE_ZIP%
echo %OUT%\SHA256SUMS.txt
pause
