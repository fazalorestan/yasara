# Apply YaSara v1.2 Phase 1 React Dashboard Foundation Patch

Extract into:
`D:\yasara_clean`

Then run:
```cmd
cd /d D:\yasara_clean\backend
python scripts\apply_v1_2_phase1_react_dashboard_foundation_patch.py
set PYTHONPATH=%CD%
python -m pytest tests
```

Run React dashboard:
```cmd
cd /d D:\yasara_clean\backend
scripts\run_react_dashboard_v1_2.bat
```

Open:
`http://127.0.0.1:5173`

Adds 4 tests.
