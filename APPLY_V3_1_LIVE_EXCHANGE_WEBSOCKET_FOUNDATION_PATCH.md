# Apply YaSara v3.1 Live Exchange WebSocket Foundation

Extract into:

```text
D:\yasara_clean
```

Apply and test:

```cmd
cd /d D:\yasara_clean\backend
python scripts\apply_v3_1_live_exchange_router_patch.py
set PYTHONPATH=%CD%
python -m pytest tests
```

Test API:

```text
http://127.0.0.1:8000/api/v1/v3-1/live-exchange/summary
```

Adds 8 tests.
