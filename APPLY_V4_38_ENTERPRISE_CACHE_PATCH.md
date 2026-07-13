# Apply YaSara v4.38 Enterprise Cache

```cmd
cd /d D:\yasara_clean
python yasara.py patch
python yasara.py test
python yasara.py start
```

API:

```text
http://127.0.0.1:8000/api/v1/v4-38/enterprise-cache/summary
http://127.0.0.1:8000/api/v1/v4-38/enterprise-cache/metrics
http://127.0.0.1:8000/api/v1/v4-38/enterprise-cache/redis-contract
```

Adds 10 tests.
