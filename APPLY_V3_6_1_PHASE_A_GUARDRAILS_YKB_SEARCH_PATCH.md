# Apply YaSara v3.6.1 Phase A Guardrails, YKB Search & Registry Validation

Extract into:

```text
D:\yasara_clean
```

Apply router:

```cmd
cd /d D:\yasara_clean\backend
python scripts\apply_v3_6_1_phase_a_guardrails_router_patch.py
```

Sync Frontend:

```cmd
python scripts\sync_operational_frontend_status.py
```

Validate:

```cmd
set PYTHONPATH=%CD%
python scripts\validate_v3_6_1_guardrails.py
python -m pytest tests
```

Test APIs:

```text
http://127.0.0.1:8000/api/v1/v3-6-1/phase-a-guardrails/summary
http://127.0.0.1:8000/api/v1/v3-6-1/phase-a-guardrails/health
http://127.0.0.1:8000/api/v1/v3-6-1/phase-a-guardrails/ykb/stats
```

Adds 9 tests.
