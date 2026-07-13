# Apply YaSara v4.35 Enterprise Configuration Center

```cmd
cd /d D:\yasara_clean
python yasara.py patch
python yasara.py test
python yasara.py start
```

API:

```text
http://127.0.0.1:8000/api/v1/v4-35/configuration-center/summary
http://127.0.0.1:8000/api/v1/v4-35/configuration-center/snapshot
```

Adds 10 tests.
