@echo off
cd /d "%~dp0..\.."
if not exist dist mkdir dist

echo ==========================================
echo YaSara v2.6 Final Operational Release
echo ==========================================

cd /d backend
set PYTHONPATH=%CD%
python -m pytest tests
if errorlevel 1 (
  echo Tests failed.
  pause
  exit /b 1
)

cd /d ..\frontend
call npm install
call npm run build
if errorlevel 1 (
  echo Frontend build failed.
  pause
  exit /b 1
)

cd /d ..
powershell -NoProfile -ExecutionPolicy Bypass -Command "Compress-Archive -Path 'backend','frontend','docs','VERSION','BUILD_INFO.json' -DestinationPath 'dist\YaSara_v2_6_Final_Operational.zip' -Force"
powershell -NoProfile -ExecutionPolicy Bypass -Command "Get-FileHash -Algorithm SHA256 'dist\YaSara_v2_6_Final_Operational.zip' | ForEach-Object { $_.Hash + '  YaSara_v2_6_Final_Operational.zip' } | Set-Content -Path 'dist\SHA256SUMS_V2_6.txt' -Encoding UTF8"

echo Final operational output created:
echo dist\YaSara_v2_6_Final_Operational.zip
echo dist\SHA256SUMS_V2_6.txt
pause
