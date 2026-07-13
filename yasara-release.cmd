@echo off
cd /d "%~dp0"
python yasara.py release %*
exit /b %ERRORLEVEL%
