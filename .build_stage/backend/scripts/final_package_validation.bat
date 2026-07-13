@echo off
setlocal
cd /d "%~dp0.."
set PYTHONPATH=%CD%
echo Running YaSara Final Package validation...
python -m pytest tests
echo.
echo Final package summary endpoint:
echo http://127.0.0.1:8000/api/v1/final-package-v1/summary
pause
