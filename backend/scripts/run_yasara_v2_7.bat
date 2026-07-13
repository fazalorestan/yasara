@echo off
setlocal
cd /d "%~dp0.."
set PYTHONPATH=%CD%

echo ==========================================
echo YaSara Professional v2.7 Final Run
echo ==========================================

start "YaSara Backend v2.7" cmd /k "cd /d %CD% && set PYTHONPATH=%CD% && py -3.12 -m uvicorn app.main:app --host 127.0.0.1 --port 8000"

cd /d "%~dp0..\..\frontend"
start "YaSara Dashboard v2.7" cmd /k "cd /d %CD% && npm run dev"

timeout /t 4 >nul
start "" "http://127.0.0.1:5173"
