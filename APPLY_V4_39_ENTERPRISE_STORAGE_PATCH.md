# Apply YaSara v4.39 Enterprise Storage

```cmd
cd /d D:\yasara_clean
python yasara.py patch
python yasara.py test
python yasara.py start
```

API:

```text
http://127.0.0.1:8000/api/v1/v4-39/enterprise-storage/summary
http://127.0.0.1:8000/api/v1/v4-39/enterprise-storage/inventory
http://127.0.0.1:8000/api/v1/v4-39/enterprise-storage/metrics
```

Adds 10 tests.
