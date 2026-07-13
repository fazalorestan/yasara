# Apply YaSara v2.6 Final Operational Bridge

Extract into `D:\yasara_clean`.

```cmd
cd /d D:\yasara_clean\backend
python scripts\apply_v2_6_final_operational_router_patch.py
set PYTHONPATH=%CD%
python -m pytest tests
```

Test:
`http://127.0.0.1:8000/api/v1/v2-6/final-operational/summary`

Operational progress: 100%
Remaining: 0%

Adds 7 tests.
