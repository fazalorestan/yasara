# Apply v5.2-alpha Package Q

```cmd
cd /d D:\yasara_clean
python yasara.py patch
python scripts\repair_literal_newlines_projectwide.py
python scripts\validate_python_compile.py
python yasara.py test
python scripts\build_first_real_windows_exe.py --execute
python scripts\check_yasara_executable_validation.py
python scripts\show_yasara_backend_logs.py
type D:\yasara_clean\dist\windows\portable\YaSara\runtime_reports\auto_router_registry_report.json
```
