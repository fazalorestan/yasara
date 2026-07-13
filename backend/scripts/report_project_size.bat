@echo off
setlocal enabledelayedexpansion

echo ================================
echo YaSara Project Size Report
echo ================================
echo.

for /d %%d in (*) do (
    for /f "tokens=3" %%s in ('dir /s /-c "%%d" ^| find "File(s)"') do (
        echo %%d : %%s bytes
    )
)

echo.
echo Tip: remove .venv, __pycache__, .pytest_cache, build and dist for safe cleanup.
pause
