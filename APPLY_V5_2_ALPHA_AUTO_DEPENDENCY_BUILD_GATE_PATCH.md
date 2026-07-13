# Apply v5.2-alpha Package J

```cmd
cd /d D:\yasara_clean
python yasara.py patch
python yasara.py test
python scripts\build_first_real_windows_exe.py --execute
python scripts\check_yasara_executable_validation.py
python scripts\show_yasara_backend_logs.py
```

اگر فقط Build بدون Validation خواستی:

```cmd
python scripts\build_first_real_windows_exe.py --execute --skip-exe-validation
```
