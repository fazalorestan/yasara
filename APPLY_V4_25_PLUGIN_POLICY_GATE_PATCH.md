# Apply YaSara v4.25 Plugin Policy Gate

```cmd
cd /d D:\yasara_clean
python yasara.py patch
python yasara.py test
python yasara.py start
```

API:

```text
http://127.0.0.1:8000/api/v1/v4-25/policy-gate/summary
http://127.0.0.1:8000/api/v1/v4-25/policy-gate/execution-contract
```

Adds 8 tests.
