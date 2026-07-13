@echo off
setlocal
cd /d "%~dp0..\.."

echo ========================================
echo YaSara Professional v1.0 Manual Package
echo ========================================
echo.
echo This script is a safe packaging guide.
echo It does not delete source files.
echo.
echo Recommended steps:
echo 1. Run backend\scripts\final_package_validation.bat
echo 2. Run backend\scripts\safe_consolidation_cleanup.bat
echo 3. Zip backend, docs, deployment, README.md and CHANGELOG.md
echo 4. Name it: yasara_professional_v1_0_stable.zip
echo.
pause
