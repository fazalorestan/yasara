@echo off
setlocal
cd /d "%~dp0"
python scripts\yasara_release.py %*
exit /b %errorlevel%
