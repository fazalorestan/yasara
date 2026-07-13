# Apply YaSara v4.21.1 Frontend Compatibility Layer

Extract into:

```text
D:\yasara_clean
```

Run:

```cmd
cd /d D:\yasara_clean
python scripts\apply_v4_21_1_frontend_compatibility.py
python yasara.py patch
python yasara.py test
python yasara.py start
```

API:

```text
http://127.0.0.1:8000/api/v1/v4-21-1/frontend-compatibility/summary
```

Adds 3 tests and restores old UI test compatibility.
