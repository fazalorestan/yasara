@echo off
setlocal enabledelayedexpansion
cd /d "%~dp0..\.."

echo ==========================================
echo YaSara Professional v2.0 Final Release
echo ==========================================

set ROOT=%CD%
set OUT=%ROOT%\dist
set WIN_FINAL=%OUT%\YaSara_Professional_v2_0_Windows_Final.zip
set WIN_PORTABLE=%OUT%\YaSara_Professional_v2_0_Windows_Portable.zip
set MOBILE_ZIP=%OUT%\YaSara_Professional_v2_0_Mobile_PWA.zip

if not exist "%OUT%" mkdir "%OUT%"

echo Running backend tests...
cd /d "%ROOT%\backend"
set PYTHONPATH=%CD%
python -m pytest tests
if errorlevel 1 (
    echo Tests failed. Build stopped.
    pause
    exit /b 1
)

echo Building React frontend...
cd /d "%ROOT%\frontend"
call npm install
call npm run build
if errorlevel 1 (
    echo Frontend build failed.
    pause
    exit /b 1
)

cd /d "%ROOT%"

echo Creating final packages...
if exist "%WIN_FINAL%" del /q "%WIN_FINAL%"
if exist "%WIN_PORTABLE%" del /q "%WIN_PORTABLE%"
if exist "%MOBILE_ZIP%" del /q "%MOBILE_ZIP%"

powershell -NoProfile -ExecutionPolicy Bypass -Command "Compress-Archive -Path 'backend','frontend','docs','deployment','windows_runtime','desktop_packaging','release_automation','VERSION','BUILD_INFO.json','RELEASE_NOTES_V2_0.md','CHANGELOG_V2_0.md','FINAL_RELEASE_MANIFEST_V2_0.json' -DestinationPath '%WIN_FINAL%' -Force"

powershell -NoProfile -ExecutionPolicy Bypass -Command "Compress-Archive -Path 'backend','frontend\dist','windows_runtime','VERSION','BUILD_INFO.json','RELEASE_NOTES_V2_0.md' -DestinationPath '%WIN_PORTABLE%' -Force"

if exist "mobile_output" (
  powershell -NoProfile -ExecutionPolicy Bypass -Command "Compress-Archive -Path 'mobile_output','frontend\dist','VERSION','BUILD_INFO.json' -DestinationPath '%MOBILE_ZIP%' -Force"
) else (
  powershell -NoProfile -ExecutionPolicy Bypass -Command "Compress-Archive -Path 'frontend\dist','VERSION','BUILD_INFO.json' -DestinationPath '%MOBILE_ZIP%' -Force"
)

powershell -NoProfile -ExecutionPolicy Bypass -Command "Get-FileHash -Algorithm SHA256 '%WIN_FINAL%','%WIN_PORTABLE%','%MOBILE_ZIP%' | ForEach-Object { $_.Hash + '  ' + (Split-Path $_.Path -Leaf) } | Set-Content -Path '%OUT%\SHA256SUMS_V2_0.txt' -Encoding UTF8"

echo.
echo YaSara Professional v2.0 Final outputs:
echo %WIN_FINAL%
echo %WIN_PORTABLE%
echo %MOBILE_ZIP%
echo %OUT%\SHA256SUMS_V2_0.txt
echo.
pause
