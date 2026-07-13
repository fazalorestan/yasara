# Apply YaSara v1.2.4 Milestone 2 Portfolio, Orders & Depth Patch

Extract into `D:\yasara_clean`.

```cmd
cd /d D:\yasara_clean\backend
python scripts\apply_v1_2_4_milestone2_portfolio_orders_router_patch.py
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

Open `http://127.0.0.1:5173`.

Adds 5 tests.
