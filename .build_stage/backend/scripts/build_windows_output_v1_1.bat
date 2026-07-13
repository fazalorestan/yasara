@echo off
setlocal enabledelayedexpansion
cd /d "%~dp0..\.."

echo ==========================================
echo YaSara Professional v1.1 Windows Output
echo ==========================================

set ROOT=%CD%
set OUT=%ROOT%\dist
set WIN_FINAL=%OUT%\YaSara_Professional_v1_1_Windows_Final.zip
set WIN_PORTABLE=%OUT%\YaSara_Professional_v1_1_Windows_Portable.zip

if not exist "%OUT%" mkdir "%OUT%"
if exist "%WIN_FINAL%" del /q "%WIN_FINAL%"
if exist "%WIN_PORTABLE%" del /q "%WIN_PORTABLE%"

echo Running tests...
cd /d "%ROOT%\backend"
set PYTHONPATH=%CD%
python -m pytest tests
if errorlevel 1 (
    echo Tests failed. Windows output stopped.
    pause
    exit /b 1
)

cd /d "%ROOT%"

echo Creating Windows Final ZIP...
powershell -NoProfile -ExecutionPolicy Bypass -Command "Compress-Archive -Path 'backend','docs','deployment','windows_runtime','desktop_packaging','release_automation','VERSION','BUILD_INFO.json','RELEASE_NOTES_V1_1.md','CHANGELOG_V1_1.md','FINAL_VERSION_FREEZE_MANIFEST.json','YASARA_V1_FINAL_README.md','YASARA_V1_TO_V1_1_ROADMAP.md','YASARA_V2_ROADMAP.md' -DestinationPath '%WIN_FINAL%' -Force"

echo Creating Windows Portable ZIP...
powershell -NoProfile -ExecutionPolicy Bypass -Command "Compress-Archive -Path 'backend','windows_runtime','VERSION','BUILD_INFO.json' -DestinationPath '%WIN_PORTABLE%' -Force"

echo Creating installer plan...
(
echo YaSara Professional v1.1 Windows Installer Plan
echo 1. Extract Windows Final ZIP
echo 2. Create Python venv inside backend
echo 3. Install requirements
echo 4. Create desktop shortcut to windows_runtime\YaSara_Start_Backend.bat
echo 5. Create test shortcut to windows_runtime\YaSara_Run_Tests.bat
echo 6. Open http://127.0.0.1:8000/docs
) > "%OUT%\YaSara_Windows_Installer_Plan.txt"

powershell -NoProfile -ExecutionPolicy Bypass -Command "Get-FileHash -Algorithm SHA256 '%WIN_FINAL%','%WIN_PORTABLE%' | ForEach-Object { $_.Hash + '  ' + (Split-Path $_.Path -Leaf) } | Set-Content -Path '%OUT%\SHA256SUMS_WINDOWS.txt' -Encoding UTF8"

echo.
echo Windows outputs created:
echo %WIN_FINAL%
echo %WIN_PORTABLE%
echo %OUT%\SHA256SUMS_WINDOWS.txt
pause
