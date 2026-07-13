@echo off
setlocal
cd /d "%~dp0.."
set PYTHONPATH=%CD%

echo =====================================
echo YaSara Professional Final Closeout
echo =====================================
echo.
python -m pytest tests
echo.
echo If tests are green, project is ready for final package export.
echo.
echo Optional endpoint after backend start:
echo http://127.0.0.1:8000/api/v1/final-closeout-v1/summary
pause
