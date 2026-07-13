# Apply v5.2-alpha Package I

```cmd
cd /d D:\yasara_clean
python yasara.py patch
python yasara.py test
python scripts\build_first_real_windows_exe.py --execute
cd /d D:\yasara_clean\dist\windows\portable\YaSara
YaSara.exe
echo ExitCode=%ERRORLEVEL%
cd /d D:\yasara_clean
python scripts\check_yasara_launcher_runtime.py
python scripts\show_yasara_backend_logs.py
```
