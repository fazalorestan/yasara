@echo off
setlocal
cd /d "%~dp0..\.."
echo =========================================
echo YaSara Final Release Archive Plan
echo =========================================
echo.
echo 1. Run backend tests
echo 2. Run safe cleanup
echo 3. Create portable ZIP
echo 4. Generate checksums
echo 5. Validate artifact manifest
echo.
pause
