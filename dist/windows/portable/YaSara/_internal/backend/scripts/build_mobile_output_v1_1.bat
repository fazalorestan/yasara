@echo off
setlocal enabledelayedexpansion
cd /d "%~dp0..\.."

echo ==========================================
echo YaSara Professional v1.1 Mobile Output
echo ==========================================

set ROOT=%CD%
set OUT=%ROOT%\dist
set MOBILE=%ROOT%\mobile_output
set MOBILE_ZIP=%OUT%\YaSara_Professional_v1_1_Mobile_PWA.zip

if not exist "%OUT%" mkdir "%OUT%"
if not exist "%MOBILE%" mkdir "%MOBILE%"
if exist "%MOBILE_ZIP%" del /q "%MOBILE_ZIP%"

echo Creating Mobile PWA files...

(
echo ^<!doctype html^>
echo ^<html lang="en"^>
echo ^<head^>
echo ^<meta charset="utf-8" /^>
echo ^<meta name="viewport" content="width=device-width, initial-scale=1" /^>
echo ^<title^>YaSara Professional v1.1^</title^>
echo ^<link rel="manifest" href="./manifest.webmanifest" /^>
echo ^<style^>body{font-family:Arial;margin:20px;background:#0f172a;color:#e5e7eb} .card{background:#111827;padding:16px;border-radius:12px;margin:12px 0} button{padding:10px;border-radius:8px;border:0}^</style^>
echo ^</head^>
echo ^<body^>
echo ^<h1^>YaSara Professional v1.1^</h1^>
echo ^<div class="card"^>Mobile dashboard shell. Connect this app to your backend API.^</div^>
echo ^<div class="card"^>Default API: ^<code^>http://127.0.0.1:8000/api/v1^</code^>^</div^>
echo ^</body^>
echo ^</html^>
) > "%MOBILE%\index.html"

(
echo {
echo   "name": "YaSara Professional",
echo   "short_name": "YaSara",
echo   "version": "1.1.0",
echo   "display": "standalone",
echo   "start_url": "./index.html",
echo   "background_color": "#0f172a",
echo   "theme_color": "#111827",
echo   "icons": []
echo }
) > "%MOBILE%\manifest.webmanifest"

(
echo {
echo   "product": "YaSara Professional",
echo   "version": "1.1.0",
echo   "api_base_url": "http://127.0.0.1:8000/api/v1",
echo   "endpoints": {
echo     "dashboard": "/v1-1/dashboard-runtime/snapshot",
echo     "market": "/v1-1/market-data/snapshot",
echo     "alerts": "/v1-1/alerts/snapshot",
echo     "paperTrading": "/v1-1/paper-trading/snapshot"
echo   },
echo   "live_trading_enabled": false
echo }
) > "%MOBILE%\mobile_api_config.json"

(
echo # YaSara Android Build Guide
echo.
echo This mobile output is a PWA/mobile shell.
echo.
echo ## Option 1: Test as PWA
echo Open `mobile_output\index.html` in a browser.
echo.
echo ## Option 2: Android wrapper
echo Use Capacitor or Android Studio WebView wrapper.
echo.
echo Required backend:
echo `http://127.0.0.1:8000`
echo.
echo Live trading remains disabled.
) > "%MOBILE%\ANDROID_BUILD_GUIDE.md"

powershell -NoProfile -ExecutionPolicy Bypass -Command "Compress-Archive -Path 'mobile_output' -DestinationPath '%MOBILE_ZIP%' -Force"
powershell -NoProfile -ExecutionPolicy Bypass -Command "Get-FileHash -Algorithm SHA256 '%MOBILE_ZIP%' | ForEach-Object { $_.Hash + '  ' + (Split-Path $_.Path -Leaf) } | Set-Content -Path '%OUT%\SHA256SUMS_MOBILE.txt' -Encoding UTF8"

echo.
echo Mobile outputs created:
echo %MOBILE_ZIP%
echo %OUT%\SHA256SUMS_MOBILE.txt
pause
