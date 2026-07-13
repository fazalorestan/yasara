# Apply YaSara v1.2 Phase 1 Web Dashboard Shell Patch

Extract into your current YaSara project root:

`D:\yasara_clean`

Then run:

```cmd
cd /d D:\yasara_clean\backend
python scripts\apply_v1_2_phase1_dashboard_shell_patch.py
set PYTHONPATH=%CD%
python -m pytest tests
```

To update Windows launcher:

```cmd
cd /d D:\yasara_clean
backend\scripts\update_windows_launcher_for_dashboard.bat
```

Open:

```text
http://127.0.0.1:8000/app
```

Adds 3 tests.
