# Apply YaSara v1.2.6 Workspace Settings Polish Patch

Extract into `D:\yasara_clean`.

```cmd
cd /d D:\yasara_clean\backend
python scripts\apply_v1_2_6_workspace_polish_router_patch.py
set PYTHONPATH=%CD%
python -m pytest tests
```

Frontend:

```cmd
cd /d D:\yasara_clean\frontend
npm install
npm run dev
```

Backend:

```cmd
cd /d D:\yasara_clean\backend
py -3.12 -m uvicorn app.main:app
```

Adds 5 tests.
