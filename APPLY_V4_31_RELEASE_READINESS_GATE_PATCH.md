# Apply YaSara v4.31 Release Readiness Gate

```cmd
cd /d D:\yasara_clean
python yasara.py patch
python yasara.py test
python yasara.py start
```

API:

```text
http://127.0.0.1:8000/api/v1/v4-31/release-readiness/summary
http://127.0.0.1:8000/api/v1/v4-31/release-readiness/gate
```

Adds 9 tests.
