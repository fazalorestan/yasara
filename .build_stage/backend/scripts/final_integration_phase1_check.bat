@echo off
setlocal
cd /d "%~dp0.."
set PYTHONPATH=%CD%
python -m pytest tests
echo.
echo Final Integration Phase 1 completed if all tests passed.
pause
