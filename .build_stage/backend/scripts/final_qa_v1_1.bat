@echo off
setlocal
cd /d "%~dp0.."

echo ==========================================
echo YaSara Professional v1.1 Final QA
echo ==========================================

set PYTHONPATH=%CD%
python -m pytest tests
if errorlevel 1 (
    echo Final QA failed.
    pause
    exit /b 1
)

python scripts\project_health_check.py
if errorlevel 1 (
    echo Health check failed.
    pause
    exit /b 1
)

python scripts\verify_release.py
if errorlevel 1 (
    echo Release verification failed.
    pause
    exit /b 1
)

echo Final QA passed.
pause
