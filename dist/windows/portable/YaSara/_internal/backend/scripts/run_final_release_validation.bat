@echo off
setlocal
cd /d "%~dp0.."
set PYTHONPATH=%CD%
echo Running YaSara Final Release validation...
python -m pytest tests
echo.
echo Final release endpoints:
echo http://127.0.0.1:8000/api/v1/final-release-v1/summary
echo http://127.0.0.1:8000/api/v1/final-release-v1/manifest
pause
