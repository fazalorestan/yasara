@echo off
setlocal

cd /d "%~dp0..\.."
set EXPORT_NAME=yasara_professional_v1_0_stable.zip

echo Checking final export...
if exist "%CD%\%EXPORT_NAME%" (
    echo Found: %CD%\%EXPORT_NAME%
    echo Final export package exists.
) else (
    echo Final export package not found.
)

pause
