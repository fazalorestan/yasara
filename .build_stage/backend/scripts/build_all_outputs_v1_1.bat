@echo off
setlocal
cd /d "%~dp0"

call build_windows_output_v1_1.bat
call build_mobile_output_v1_1.bat

echo.
echo All YaSara v1.1 outputs completed.
pause
