# Apply YaSara v4.27 Extension Host & Plugin Sandbox

```cmd
cd /d D:\yasara_clean
python yasara.py patch
python yasara.py test
python yasara.py start
```

API:

```text
http://127.0.0.1:8000/api/v1/v4-27/extension-host/summary
http://127.0.0.1:8000/api/v1/v4-27/extension-host/health
http://127.0.0.1:8000/api/v1/v4-27/extension-host/startup-profile
http://127.0.0.1:8000/api/v1/v4-27/extension-host/quotas
```

Adds 12 tests.
