# Apply YaSara v1.2 Phase 2 Market Workspace Patch

Extract into:

```text
D:\yasara_clean
```

Then run:

```cmd
cd /d D:\yasara_clean\backend
python scripts\apply_v1_2_phase2_market_workspace_router_patch.py
set PYTHONPATH=%CD%
python -m pytest tests
```

Run backend and frontend as before:

```cmd
py -3.12 -m uvicorn app.main:app
```

```cmd
cd /d D:\yasara_clean\frontend
npm run dev
```

Open:

```text
http://127.0.0.1:5173
```

Adds 4 tests.
