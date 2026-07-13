@echo off
setlocal enabledelayedexpansion

cd /d "%~dp0..\.."

echo ==========================================
echo YaSara Safe Project Cleanup
echo ==========================================
echo Project root: %CD%
echo.

echo Removing Python cache folders...
for /d /r %%d in (__pycache__) do (
    if exist "%%d" rmdir /s /q "%%d"
)

echo Removing pytest/mypy/ruff cache...
for /d /r %%d in (.pytest_cache .mypy_cache .ruff_cache) do (
    if exist "%%d" rmdir /s /q "%%d"
)

echo Removing compiled/temp/log files...
del /s /q *.pyc 2>nul
del /s /q *.pyo 2>nul
del /s /q *.tmp 2>nul
del /s /q *.log 2>nul

if "%1"=="--deep" (
    echo Running deep cleanup...
    if exist build rmdir /s /q build
    if exist dist rmdir /s /q dist
    del /q APPLY_V1_1_PHASE*.md 2>nul
    del /q V1_1_PHASE*_CHANGELOG.md 2>nul
    del /q V1_1_PHASE*_TEST_REPORT.md 2>nul
    del /q V1_1_PHASE*_SECURITY_REVIEW.md 2>nul
    del /q yasara_v1_1_phase*.zip 2>nul
)

echo.
echo Cleanup finished safely.
echo Source files were not removed.
pause
