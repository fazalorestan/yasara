@echo off
setlocal enabledelayedexpansion
cd /d "%~dp0..\.."

echo ==========================================
echo YaSara Professional v2.7 Final Distribution
echo ==========================================

set ROOT=%CD%
set OUT=%ROOT%\dist
set WIN_FINAL=%OUT%\YaSara_Professional_v2_7_Windows_Final.zip
set WIN_PORTABLE=%OUT%\YaSara_Professional_v2_7_Windows_Portable.zip
set MOBILE=%OUT%\YaSara_Professional_v2_7_Mobile_PWA.zip

if not exist "%OUT%" mkdir "%OUT%"

echo Running full tests...
cd /d "%ROOT%\backend"
set PYTHONPATH=%CD%
python -m pytest tests
if errorlevel 1 (
    echo Tests failed. Distribution stopped.
    pause
    exit /b 1
)

echo Building frontend production files...
cd /d "%ROOT%\frontend"
call npm install
call npm run build
if errorlevel 1 (
    echo Frontend build failed.
    pause
    exit /b 1
)

cd /d "%ROOT%"

echo Creating Windows Final package...
if exist "%WIN_FINAL%" del /q "%WIN_FINAL%"
powershell -NoProfile -ExecutionPolicy Bypass -Command "Compress-Archive -Path 'backend','frontend','docs','VERSION','FINAL_DISTRIBUTION_MANIFEST_V2_7.json' -DestinationPath '%WIN_FINAL%' -Force"

echo Creating Windows Portable package...
if exist "%WIN_PORTABLE%" del /q "%WIN_PORTABLE%"
powershell -NoProfile -ExecutionPolicy Bypass -Command "Compress-Archive -Path 'backend','frontend\dist','VERSION','FINAL_DISTRIBUTION_MANIFEST_V2_7.json' -DestinationPath '%WIN_PORTABLE%' -Force"

echo Creating Mobile PWA package...
if exist "%MOBILE%" del /q "%MOBILE%"
powershell -NoProfile -ExecutionPolicy Bypass -Command "Compress-Archive -Path 'frontend\dist','VERSION','FINAL_DISTRIBUTION_MANIFEST_V2_7.json' -DestinationPath '%MOBILE%' -Force"

echo Generating SHA256 checksums...
powershell -NoProfile -ExecutionPolicy Bypass -Command "Get-FileHash -Algorithm SHA256 '%WIN_FINAL%','%WIN_PORTABLE%','%MOBILE%' | ForEach-Object { $_.Hash + '  ' + (Split-Path $_.Path -Leaf) } | Set-Content -Path '%OUT%\SHA256SUMS_V2_7.txt' -Encoding UTF8"

echo.
echo Final outputs created:
echo %WIN_FINAL%
echo %WIN_PORTABLE%
echo %MOBILE%
echo %OUT%\SHA256SUMS_V2_7.txt
echo.
pause
