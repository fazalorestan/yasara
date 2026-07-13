# Apply YaSara v4.22 Platform Core Foundation / Pre-v5

```cmd
cd /d D:\yasara_clean
python scripts\apply_v4_22_frontend_compatibility_tokens.py
python yasara.py patch
python yasara.py test
python yasara.py start
```

API:
```text
http://127.0.0.1:8000/api/v1/v4-22/platform-core/summary
```

Adds 11 tests.
