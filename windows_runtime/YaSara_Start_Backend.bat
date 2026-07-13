@echo off
setlocal
cd /d "%~dp0..\backend"
if not exist ".venv" (
    python -m venv .venv
)
call .venv\Scripts\activate
python -m pip install --upgrade pip
if exist requirements.txt (
    pip install -r requirements.txt
)
set PYTHONPATH=%CD%
start "" "http://127.0.0.1:8000/app"
python -m uvicorn app.main:app --reload
