# Apply Sprint 43

```cmd
cd /d D:\yasara_clean
python yasara.py patch
python scripts\apply_sprint43_trading_os.py
python scripts\validate_python_compile.py
python yasara.py test
cd frontend
npm run build
cd ..
python scripts\build_first_real_windows_exe.py --execute
python scripts\check_yasara_executable_validation.py
```

API:

```text
http://127.0.0.1:8000/api/v1/enterprise/trading-os/snapshot
```
