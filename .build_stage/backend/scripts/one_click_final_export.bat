@echo off
setlocal enabledelayedexpansion

echo ==========================================
echo YaSara Professional v1.0 Final Export
echo ==========================================
echo.

cd /d "%~dp0.."
set BACKEND_DIR=%CD%
set PROJECT_ROOT=%BACKEND_DIR%\..
set EXPORT_NAME=yasara_professional_v1_0_stable.zip
set EXPORT_PATH=%PROJECT_ROOT%\%EXPORT_NAME%

echo Backend:
echo %BACKEND_DIR%
echo.
echo Project root:
echo %PROJECT_ROOT%
echo.

echo [1/4] Running full tests...
set PYTHONPATH=%BACKEND_DIR%
python -m pytest tests
if errorlevel 1 (
    echo.
    echo Tests failed. Export stopped.
    pause
    exit /b 1
)

echo.
echo [2/4] Safe cleanup...
if exist "%BACKEND_DIR%\scripts\safe_consolidation_cleanup.bat" (
    call "%BACKEND_DIR%\scripts\safe_consolidation_cleanup.bat"
) else (
    echo Safe cleanup script not found. Skipping cleanup.
)

echo.
echo [3/4] Creating final ZIP...
cd /d "%PROJECT_ROOT%"
if exist "%EXPORT_PATH%" del /q "%EXPORT_PATH%"

powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "Compress-Archive -Path 'backend','docs','deployment' -DestinationPath '%EXPORT_PATH%' -Force"

if not exist "%EXPORT_PATH%" (
    echo.
    echo ZIP creation failed.
    pause
    exit /b 1
)

echo.
echo [4/4] Done.
echo Final package:
echo %EXPORT_PATH%
echo.
pause
