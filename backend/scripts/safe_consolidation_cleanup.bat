@echo off
setlocal enabledelayedexpansion

echo ================================
echo YaSara Consolidation Safe Cleanup
echo ================================
echo.

set ROOT=%CD%
echo Running from:
echo %ROOT%
echo.

echo Removing safe cache folders...
for /d /r "%ROOT%" %%d in (__pycache__) do if exist "%%d" rmdir /s /q "%%d"
for /d /r "%ROOT%" %%d in (.pytest_cache) do if exist "%%d" rmdir /s /q "%%d"
for /d /r "%ROOT%" %%d in (.mypy_cache) do if exist "%%d" rmdir /s /q "%%d"
for /d /r "%ROOT%" %%d in (.ruff_cache) do if exist "%%d" rmdir /s /q "%%d"

echo Removing compiled/cache files...
del /s /q "%ROOT%\*.pyc" 2>nul
del /s /q "%ROOT%\*.pyo" 2>nul
del /s /q "%ROOT%\*.log" 2>nul
del /s /q "%ROOT%\*.tmp" 2>nul

echo.
echo Cleanup completed. Source files were not removed.
pause
