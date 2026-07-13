@echo off
setlocal enabledelayedexpansion

cd /d "%~dp0..\.."

echo ==========================================
echo YaSara Professional v1.1 RC1 Package
echo ==========================================
echo.

set ROOT=%CD%
set OUT=%ROOT%\dist
set ZIP=%OUT%\yasara_professional_v1_1_rc1.zip

if not exist "%OUT%" mkdir "%OUT%"
if exist "%ZIP%" del /q "%ZIP%"

echo Running tests before package...
cd /d "%ROOT%\backend"
set PYTHONPATH=%CD%
python -m pytest tests
if errorlevel 1 (
    echo Tests failed. RC package stopped.
    pause
    exit /b 1
)

cd /d "%ROOT%"
echo Creating RC1 ZIP...
powershell -NoProfile -ExecutionPolicy Bypass -Command "Compress-Archive -Path 'backend','docs','deployment','windows_runtime','desktop_packaging','release_automation','FINAL_VERSION_FREEZE_MANIFEST.json','YASARA_V1_FINAL_README.md','YASARA_V1_TO_V1_1_ROADMAP.md','YASARA_V2_ROADMAP.md' -DestinationPath '%ZIP%' -Force"

echo.
echo RC1 package created:
echo %ZIP%
pause
