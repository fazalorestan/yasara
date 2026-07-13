# Apply YaSara v4.24 Plugin Registry Sync

```cmd
cd /d D:\yasara_clean
python yasara.py patch
python yasara.py test
python yasara.py start
```

API:

```text
http://127.0.0.1:8000/api/v1/v4-24/plugin-registry-sync/summary
http://127.0.0.1:8000/api/v1/v4-24/plugin-registry-sync/lifecycle
http://127.0.0.1:8000/api/v1/v4-24/plugin-registry-sync/governance
```

Manual sync:

```cmd
curl -X POST http://127.0.0.1:8000/api/v1/v4-24/plugin-registry-sync/sync
```

Adds 8 tests.
