# Apply YaSara v3.6 Phase A Meta-Infrastructure & YKB Foundation

Extract into:

```text
D:\yasara_clean
```

Apply router:

```cmd
cd /d D:\yasara_clean\backend
python scripts\apply_v3_6_phase_a_meta_ykb_router_patch.py
```

Sync Frontend status components:

```cmd
python scripts\sync_operational_frontend_status.py
```

Validate Phase A files:

```cmd
python scripts\validate_v3_6_phase_a_meta_ykb.py
```

Run tests:

```cmd
set PYTHONPATH=%CD%
python -m pytest tests
```

Test APIs:

```text
http://127.0.0.1:8000/api/v1/v3-6/phase-a-meta-ykb/summary
http://127.0.0.1:8000/api/v1/v3-6/phase-a-meta-ykb/health
http://127.0.0.1:8000/api/v1/v3-6/phase-a-meta-ykb/ykb/status
```

Adds 9 tests.
