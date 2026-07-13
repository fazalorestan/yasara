@echo off
setlocal
set TARGET=%~dp0run_yasara_v2_7.bat
set SHORTCUT=%USERPROFILE%\Desktop\YaSara Professional v2.7.lnk

powershell -NoProfile -ExecutionPolicy Bypass -Command "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%SHORTCUT%'); $Shortcut.TargetPath = '%TARGET%'; $Shortcut.WorkingDirectory = Split-Path '%TARGET%'; $Shortcut.Save()"

echo Desktop shortcut created:
echo %SHORTCUT%
pause
