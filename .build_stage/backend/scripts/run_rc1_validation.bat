@echo off
setlocal
cd /d "%~dp0.."
set PYTHONPATH=%CD%
echo Running YaSara RC1 validation...
python -m pytest tests
echo.
echo Open after backend starts:
echo http://127.0.0.1:8000/api/v1/rc1-v1/summary
pause
