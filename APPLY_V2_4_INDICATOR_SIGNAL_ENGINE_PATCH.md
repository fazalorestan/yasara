# Apply YaSara v2.4 Indicator & Signal Engine Patch

Extract into `D:\yasara_clean`.

```cmd
cd /d D:\yasara_clean\backend
python scripts\apply_v2_4_indicator_signal_router_patch.py
set PYTHONPATH=%CD%
python -m pytest tests
```

Test:
`http://127.0.0.1:8000/api/v1/v2-4/indicator-signal/summary`

Operational progress: 93%
Remaining: 7%

Adds 6 tests.
