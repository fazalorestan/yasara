# Apply YaSara v4.36 Enterprise Scheduler

```cmd
cd /d D:\yasara_clean
python yasara.py patch
python yasara.py test
python yasara.py start
```

API:

```text
http://127.0.0.1:8000/api/v1/v4-36/enterprise-scheduler/summary
http://127.0.0.1:8000/api/v1/v4-36/enterprise-scheduler/tasks
http://127.0.0.1:8000/api/v1/v4-36/enterprise-scheduler/metrics
```

Adds 9 tests.
