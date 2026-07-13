# Apply YaSara v3.3 Strategy Builder Core

Extract into:

```text
D:\yasara_clean
```

Apply and test:

```cmd
cd /d D:\yasara_clean\backend
python scripts\apply_v3_3_strategy_builder_router_patch.py
set PYTHONPATH=%CD%
python -m pytest tests
```

Test API:

```text
http://127.0.0.1:8000/api/v1/v3-3/strategy-builder/summary
```

Create demo strategy:

```cmd
curl -X POST http://127.0.0.1:8000/api/v1/v3-3/strategy-builder/demo
```

Adds 7 tests.
