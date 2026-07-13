@echo off
setlocal
cd /d "%~dp0.."

set PYTHONPATH=%CD%

echo Starting YaSara Professional v2.0 Backend...
start "YaSara Backend" cmd /k "cd /d %CD% && py -3.12 -m uvicorn app.main:app --host 127.0.0.1 --port 8000"

cd /d "%~dp0..\..\frontend"
echo Starting YaSara React Dashboard...
start "YaSara Dashboard" cmd /k "cd /d %CD% && npm run dev"

timeout /t 3 >nul
start "" "http://127.0.0.1:5173"
