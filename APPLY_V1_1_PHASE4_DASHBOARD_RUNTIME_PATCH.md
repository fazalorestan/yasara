# Apply YaSara v1.1 Phase 4 Dashboard Runtime Patch

Extract into your current YaSara project root:

`D:\yasara_clean`

Then run:

```cmd
cd /d D:\yasara_clean\backend
python scripts\apply_v1_1_phase4_dashboard_runtime_router_patch.py
set PYTHONPATH=%CD%
python -m pytest tests
```

Adds 5 tests.
