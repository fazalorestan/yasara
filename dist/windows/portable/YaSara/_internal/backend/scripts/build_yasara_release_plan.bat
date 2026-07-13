@echo off
setlocal

echo ================================
echo YaSara Production Release Plan
echo ================================
echo.
echo 1. Run regression tests
echo 2. Run safe cleanup
echo 3. Validate dependencies
echo 4. Validate environment
echo 5. Build portable package
echo 6. Build Docker package
echo 7. Build Windows installer
echo 8. Run smoke tests
echo 9. Create release archive
echo.
pause
