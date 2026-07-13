# Apply YaSara v4.28 Plugin State Store & Runtime Snapshot

```cmd
cd /d D:\yasara_clean
python yasara.py patch
python yasara.py test
python yasara.py start
```

API:

```text
http://127.0.0.1:8000/api/v1/v4-28/plugin-state-snapshot/summary
http://127.0.0.1:8000/api/v1/v4-28/plugin-state-snapshot/states
http://127.0.0.1:8000/api/v1/v4-28/plugin-state-snapshot/snapshot
http://127.0.0.1:8000/api/v1/v4-28/plugin-state-snapshot/extension-host-snapshot
```

Adds 9 tests.
