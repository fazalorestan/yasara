@echo off
setlocal
cd /d "%~dp0.."
set PYTHONPATH=%CD%
echo Running final delivery pack validation...
python -m pytest tests
echo.
echo Final endpoint:
echo http://127.0.0.1:8000/api/v1/final-delivery-pack-v1/summary
pause
