# Apply YaSara v3.5 Smart Money Engine Core

Extract into:

```text
D:\yasara_clean
```

Apply and test:

```cmd
cd /d D:\yasara_clean\backend
python scripts\apply_v3_5_smart_money_router_patch.py
set PYTHONPATH=%CD%
python -m pytest tests
```

Test API:

```text
http://127.0.0.1:8000/api/v1/v3-5/smart-money/summary
```

Adds 6 tests.
