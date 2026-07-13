# Apply YaSara v3.2 Advanced AI Indicator Engine

Extract into:

```text
D:\yasara_clean
```

Apply and test:

```cmd
cd /d D:\yasara_clean\backend
python scripts\apply_v3_2_advanced_ai_indicators_router_patch.py
set PYTHONPATH=%CD%
python -m pytest tests
```

Test API:

```text
http://127.0.0.1:8000/api/v1/v3-2/ai-indicators/summary
```

Adds 6 tests.
