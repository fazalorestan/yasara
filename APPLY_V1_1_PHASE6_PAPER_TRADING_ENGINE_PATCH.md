# Apply YaSara v1.1 Phase 6 Paper Trading Engine Patch

Extract into your current YaSara project root:

`D:\yasara_clean`

Then run:

```cmd
cd /d D:\yasara_clean\backend
python scripts\apply_v1_1_phase6_paper_trading_router_patch.py
set PYTHONPATH=%CD%
python -m pytest tests
```

Adds 7 tests.
