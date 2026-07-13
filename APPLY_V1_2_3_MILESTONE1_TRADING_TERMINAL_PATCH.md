# Apply YaSara v1.2.3 Milestone 1 Trading Terminal Patch

Extract into:

```text
D:\yasara_clean
```

Then run:

```cmd
cd /d D:\yasara_clean\backend
python scripts\apply_v1_2_3_milestone1_trading_terminal_router_patch.py
set PYTHONPATH=%CD%
python -m pytest tests
```

Important: install the new frontend dependency:

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

Open:

```text
http://127.0.0.1:5173
```

Adds 5 tests.
