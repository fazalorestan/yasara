# Apply YaSara v4.32 Platform Versioning & Migration Plan

```cmd
cd /d D:\yasara_clean
python yasara.py patch
python yasara.py test
python yasara.py start
```

API:

```text
http://127.0.0.1:8000/api/v1/v4-32/platform-versioning/summary
http://127.0.0.1:8000/api/v1/v4-32/platform-versioning/upgrade-path
```

Adds 9 tests.
