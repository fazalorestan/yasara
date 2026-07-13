# YaSara v1.0 RC1 User Guide

## Start Backend

```cmd
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
set PYTHONPATH=%CD%
uvicorn app.main:app --reload
```

## Open
- Health: `http://127.0.0.1:8000/health`
- Swagger: `http://127.0.0.1:8000/docs`

## Safety
Live trading is disabled by default. Use paper trading and dry-run execution until production approval.
