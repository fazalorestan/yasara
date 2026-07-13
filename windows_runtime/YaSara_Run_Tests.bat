@echo off
setlocal
cd /d "%~dp0..\backend"
if not exist ".venv" (
    echo Creating virtual environment...
    python -m venv .venv
)
call .venv\Scripts\activate
python -m pip install --upgrade pip
if exist requirements.txt (
    pip install -r requirements.txt
)
set PYTHONPATH=%CD%
python -m pytest tests
pause
