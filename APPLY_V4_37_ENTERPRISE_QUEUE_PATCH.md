# Apply YaSara v4.37 Enterprise Queue

```cmd
cd /d D:\yasara_clean
python yasara.py patch
python yasara.py test
python yasara.py start
```

API:

```text
http://127.0.0.1:8000/api/v1/v4-37/enterprise-queue/summary
http://127.0.0.1:8000/api/v1/v4-37/enterprise-queue/metrics
http://127.0.0.1:8000/api/v1/v4-37/enterprise-queue/snapshot
```

Adds 10 tests.
