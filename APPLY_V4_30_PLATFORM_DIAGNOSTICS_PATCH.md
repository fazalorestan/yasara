# Apply YaSara v4.30 Platform Diagnostics

```cmd
cd /d D:\yasara_clean
python yasara.py patch
python yasara.py test
python yasara.py start
```

API:

```text
http://127.0.0.1:8000/api/v1/v4-30/platform-diagnostics/summary
http://127.0.0.1:8000/api/v1/v4-30/platform-diagnostics/readiness
http://127.0.0.1:8000/api/v1/v4-30/platform-diagnostics/runtime
```

Adds 10 tests.
