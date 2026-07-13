# Apply v5.2-alpha Package D

```cmd
cd /d D:\yasara_clean
python yasara.py patch
python yasara.py test
python scripts\build_first_real_windows_exe.py --execute
cd /d D:\yasara_clean\dist\windows\portable\YaSara
YaSara.exe
cd /d D:\yasara_clean
python scripts\check_yasara_launcher_runtime.py
```
