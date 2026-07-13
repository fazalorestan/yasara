@echo off
setlocal
cd /d "%~dp0.."
if exist ".venv" (
    call .venv\Scripts\activate
)
set PYTHONPATH=%CD%
python -m pytest tests
pause
