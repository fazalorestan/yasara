# Apply YaSara v3.5.1 Constitution Audit & Repair

Extract into:

```text
D:\yasara_clean
```

Apply router:

```cmd
cd /d D:\yasara_clean\backend
python scripts\apply_v3_5_1_constitution_audit_router_patch.py
```

Sync frontend operational status components:

```cmd
python scripts\sync_operational_frontend_status.py
```

Generate audit report:

```cmd
python scripts\yasara_v4_project_audit.py
```

Run tests:

```cmd
set PYTHONPATH=%CD%
python -m pytest tests
```

Test API:

```text
http://127.0.0.1:8000/api/v1/v3-5-1/constitution-audit/summary
http://127.0.0.1:8000/api/v1/v3-5-1/constitution-audit/health
http://127.0.0.1:8000/api/v1/v3-5-1/constitution-audit/recommendations
```

Adds 5 tests.
