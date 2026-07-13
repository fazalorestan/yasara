# Apply YaSara v4.33 Operations Runbook

```cmd
cd /d D:\yasara_clean
python yasara.py patch
python yasara.py test
python yasara.py start
```

API:
```text
http://127.0.0.1:8000/api/v1/v4-33/operations-runbook/summary
http://127.0.0.1:8000/api/v1/v4-33/operations-runbook/status
```

Adds 9 tests.
