@echo off
setlocal
cd /d "%~dp0..\.."

set TARGET=windows_runtime\YaSara_Start_Backend.bat

(
echo @echo off
echo setlocal
echo cd /d "%%~dp0..\backend"
echo if not exist ".venv" ^(
echo     python -m venv .venv
echo ^)
echo call .venv\Scripts\activate
echo python -m pip install --upgrade pip
echo if exist requirements.txt ^(
echo     pip install -r requirements.txt
echo ^)
echo set PYTHONPATH=%%CD%%
echo start "" "http://127.0.0.1:8000/app"
echo python -m uvicorn app.main:app --reload
) > "%TARGET%"

echo Launcher updated to open http://127.0.0.1:8000/app
pause
