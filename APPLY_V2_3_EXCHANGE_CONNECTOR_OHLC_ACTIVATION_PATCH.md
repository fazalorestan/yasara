# Apply YaSara v2.3 Exchange Connector & OHLC Activation Patch

Extract into `D:\yasara_clean`.

```cmd
cd /d D:\yasara_clean\backend
python scripts\apply_v2_3_exchange_connector_router_patch.py
set PYTHONPATH=%CD%
python -m pytest tests
```

Test:
`http://127.0.0.1:8000/api/v1/v2-3/exchange-connector/summary`

Operational progress: 85%
Remaining: 15%

Adds 7 tests.
