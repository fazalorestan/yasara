# Apply v2.1 Real Data Activation Phase 1

Extract into `D:\yasara_clean`.

```cmd
cd /d D:\yasara_clean\backend
python scripts\apply_v2_1_real_data_activation_router_patch.py
set PYTHONPATH=%CD%
python -m pytest tests
```

Operational progress: 60%
Remaining to full operational: 40%
Adds 6 tests.
