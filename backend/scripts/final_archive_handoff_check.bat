@echo off
setlocal
cd /d "%~dp0.."
set PYTHONPATH=%CD%
echo Running YaSara Final Archive/Handoff validation...
python -m pytest tests
echo.
echo Completion endpoint:
echo http://127.0.0.1:8000/api/v1/archive-handoff-v1/done
pause
