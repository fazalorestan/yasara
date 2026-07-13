# Apply YaSara v2.2 Market Data Engine Phase 1 Patch

Extract into `D:\yasara_clean`.

```cmd
cd /d D:\yasara_clean\backend
python scripts\apply_v2_2_market_data_engine_router_patch.py
set PYTHONPATH=%CD%
python -m pytest tests
```

Test:
`http://127.0.0.1:8000/api/v1/v2-2/market-engine/summary`

Operational progress: 75%
Remaining: 25%
Adds 6 tests.
