# Sprint 33 to 37 Batch

## Sprint 33
Symbol registry.

## Sprint 34
Exchange routing engine.

## Sprint 35
Market snapshot aggregator.

## Sprint 36
Multi-exchange watchlist feed.

## Sprint 37
Extra API routes and router patch script.

After extracting patch, run:

```cmd
cd /d D:\yasara\yasara\backend
python scripts\apply_sprint37_router_patch.py
set PYTHONPATH=%CD%
python -m pytest tests
```

Expected: 96 passed.
